<!DOCTYPE html>
<!-- saved from url=(0072)https://github.com/anweasha/Pharmacy_Management_System/blob/main/main.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/light-f13f84a2af0d.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/dark-1ee85695b584.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-8c42799cfb52.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-dc99d916bf90.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-0a83868d0e43.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-3c798f5a8bef.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-4c72a7f3b765.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-222bf22536c7.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-c1d9496197fa.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/primer-primitives-0b5bee5c70e9.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/primer-241a089e9a0a.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/global-32f8814d2265.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/github-da273831c5c7.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/repository-33a7c32c5a6c.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/code-111be5e4092d.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["code_vulnerability_scanning","copilot_conversational_ux_history_refs","copilot_smell_icebreaker_ux","copilot_implicit_context","copilot_stop_response","failbot_handle_non_errors","geojson_azure_maps","image_metric_tracking","marketing_forms_api_integration_contact_request","marketing_pages_search_explore_provider","turbo_experiment_risky","sample_network_conn_type","no_character_key_shortcuts_in_inputs","react_start_transition_for_navigations","custom_inp","remove_child_patch"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/wp-runtime-cbf820ed770f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_dompurify_dist_purify_js-13ee51630182.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-7bd350d761f4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_smoothscroll-polyfill_dist_smoothscroll_js-node_modules_stacktrace-parse-a448e4-bb5415637fe0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/environment-5555c6700ada.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-9f960d9b217c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-086f7a27bac0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_relative-time-element_dist_index_js-c76945c5961a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_combobox-nav_dist_index_js-node_modules_github_markdown-toolbar-e-820fc0-bc8f02b96749.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_details-d-ed9a97-3fb8ce186301.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_text-expander-element_dist_index_js-8a621df59e80.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_stacktrace-parser_dist_stack-443cd5-1ba4dbac454f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b7d8f4-7dc906febe69.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-3959a9-28f0ee9fece0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_onfocus_ts-ui_packages_trusted-types-policies_policy_ts-ui_packages-6fe316-d6d20db61005.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/github-elements-f7fe73c93e30.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/element-registry-450bd60214bd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-4da1df-9de8d527f925.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-fd5530-6f4d94175afe.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_lit-html_lit-html_js-5b376145beff.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_morphdom_dist_morphdom-esm_js-node_modules_github_memoize_dist_esm_index_js-05801f7ca718.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-c91f4ad18b62.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-a8ec7ed862cf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_scroll-anchoring_dist_scroll-anchoring_esm_js-node_modules_github_hotkey-1a1d91-49c03ceb2f0c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_color-convert_index_js-72c9fbde5ad4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_jtml_lib_index_js-95b84ee6bc34.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-da6ec6-3f39339c9d98.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_textarea-autosi-9e0349-b0f4de5b992f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_sudo_sudo_ts-74c0d1051bc3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-82813f-05346aa543fe.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-421cec-355eb4940fad.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_sticky-scroll-into-view_ts-1390d8d5a0dc.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-05fd80a7ea89.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-9285faa0e011.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/behaviors-af6aed1ee94e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-06ff531-2ea61fcc9a71.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/notifications-global-6d6db5144cc3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-878844713bc9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-e53a3f-f924cc31bbb1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_ref-selector_ts-2b432e185ab2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/codespaces-8facb83d6ec7.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_mini-throt-1f9a80-8656545a294a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_mini-th-9dbbd2-70f465bbe0b9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_github_repositories_get-repo-element_ts-f6b365a47eda.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/repositories-dea97b58db36.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/code-menu-67595c3a6d0c.js.download"></script>
  

  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  




      



        


  <meta http-equiv="x-pjax-version" content="3d291df433d6dc2420ae88746d5ba31d6ac55cf287d41e36bb0de76fbdb12027" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="f226bf37af9c33162063db3eb018fed7f088f86d0a20ca54c013fda96c7f2e05" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="51091e1689a8e12a5662b5d5d94b9f9bf826e08f5cb723d52baee89230b38376" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="5ea871766c54060eda52d3618dd03dbb97e38c21911d53bad9d7e3a56b339330" data-turbo-track="reload">

  

      
  

  



      


    


  

  

  
  
  





  

  <style data-styled="active" data-styled-version="5.3.6"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link crossorigin="anonymous" media="all" rel="stylesheet" href="./main_files/react-code-view.f2d60f636eb02c2001df.module.css"><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/react-lib-1fbfc5be2c18.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-541a38-ade861844008.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-8f8c5e2a2cbf.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-95a7748e3c39.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_TooltipV2_Tooltip_js-5c105bd4b6bc.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_node_modules_primer_octicons-react_dist_index_esm_mjs-cb996b1b8e38.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-f41028bf9254.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-7813b4d5597b.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-5f6d6fb70bbd.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_AnchoredOverlay_AnchoredOverlay_js-6305545ffa4a.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_react-router-dom_dist_index_js-3b41341d50fe.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_ConfirmationDialog_ConfirmationDialog_js-0e5bf03de200.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Heading_Heading_js-node_modules_primer_react_lib-es-09461f-2d30446b267e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Label_Label_js-node_modules_primer_react_lib-esm_Se-443e5e-685ada640c03.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_AvatarStack_AvatarStack_js-node_modules_primer_reac-6dc608-e4063b816185.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-7f6456-e4e9e26a4e79.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_react-core_create-browser-history_ts-ui_packages_safe-storage_safe-storage_ts-ui_-682c2c-e45e451173ec.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_react-core_register-app_ts-431888770d93.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_paths_index_ts-922fee1fcbe0.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_ref-selector_RefSelector_tsx-b257014a1aab.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-59a8e3-97e4e17c18e1.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/app_assets_modules_react-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_ho-e725dc-7c9b46c9f2b9.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/node_modules_github_mini-throttle_dist_index_js-app_assets_modules_github_blob-anchor_ts-app_-55c012-6f0349cfd4d6.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/ui_packages_code-view-shared_components_files-search_FileResultsList_tsx-dbd52a61902c.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/react-code-view-145a97048319.js.download"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>Pharmacy_Management_System/main.py at main · anweasha/Pharmacy_Management_System · GitHub</title><meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="blob" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7"><meta name="request-id" content="C2A5:1700EA:35FB4C5:3BF40E2:663A5064" data-turbo-transient="true"><meta name="html-safe-nonce" content="a781ba0a472b00d1214ef670cb67689150007cf578d3168fbd06a6b208b04c21" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9hbndlYXNoYS9QaGFybWFjeV9NYW5hZ2VtZW50X1N5c3RlbSIsInJlcXVlc3RfaWQiOiJDMkE1OjE3MDBFQTozNUZCNEM1OjNCRjQwRTI6NjYzQTUwNjQiLCJ2aXNpdG9yX2lkIjoiNzM5MjU2Mzg3MTI1NjYyOTg1MyIsInJlZ2lvbl9lZGdlIjoiY2VudHJhbGluZGlhIiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-turbo-transient="true"><meta name="visitor-hmac" content="8e41fab767b2c8029d3c9c2d10cdda78494f6d9af4e05022ec93f8f94a752a74" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:488082647" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true"><meta name="user-login" content=""><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/anweasha/Pharmacy_Management_System git https://github.com/anweasha/Pharmacy_Management_System.git"><meta name="octolytics-dimension-user_id" content="86158020"><meta name="octolytics-dimension-user_login" content="anweasha"><meta name="octolytics-dimension-repository_id" content="488082647"><meta name="octolytics-dimension-repository_nwo" content="anweasha/Pharmacy_Management_System"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="true"><meta name="octolytics-dimension-repository_parent_id" content="475079825"><meta name="octolytics-dimension-repository_parent_nwo" content="Aditimittal2809/Pharmacy_Management_System"><meta name="octolytics-dimension-repository_network_root_id" content="475079825"><meta name="octolytics-dimension-repository_network_root_nwo" content="Aditimittal2809/Pharmacy_Management_System"><meta name="turbo-body-classes" content="logged-out env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-out env-production page-responsive intent-mouse" style="overflow-wrap: break-word; --dialog-scrollgutter: 0px;">
    <div data-turbo-body="" class="logged-out env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/anweasha/Pharmacy_Management_System/blob/main/main.py#start-of-content" data-skip-target-assigned="false" class="px-2 py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      






<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_primer_react_lib-esm_Button_IconButton_js-node_modules_primer_react_lib--b964b4-74797afc8053.js.download"></script>

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/keyboard-shortcuts-dialog-b4f13290b41c.js.download"></script>

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r1t:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




      

        

            
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-674f4853d4fe.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./main_files/sessions-ff11af600d3e.js.download"></script>
<header class="Header-old header-logged-out js-details-container Details position-relative f4 py-3" role="banner" data-color-mode="light" data-light-theme="light" data-dark-theme="dark">
  <h2 class="sr-only">Navigation Menu</h2>

  <button type="button" class="Header-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class=" d-flex flex-column flex-lg-row flex-items-center p-responsive height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <a class="mr-lg-3 color-fg-inherit flex-order-2" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
        <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
      </a>

      <div class="flex-1">
        <a href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fanweasha%2FPharmacy_Management_System%2Fblob%2Fmain%2Fdrug_data.db" class="d-inline-block d-lg-none flex-order-1 f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="e9ddb64bc836d847d4e5bdb94ec70a1c232cec97dc5070cb6e681b5137d66e9c" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
          Sign in
        </a>
      </div>

      <div class="flex-1 flex-order-2 text-right">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target Button--link Button--medium Button d-lg-none color-fg-inherit p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>
    </div>


    <div class="HeaderMenu--logged-out p-responsive height-fit position-lg-relative d-lg-flex flex-column flex-auto pt-7 pb-4 top-0">
      <div class="header-menu-wrapper d-flex flex-column flex-self-end flex-lg-row flex-justify-between flex-auto p-3 p-lg-0 rounded rounded-lg-0 mt-3 mt-lg-0">
          <nav class="mt-0 px-3 px-lg-0 mb-3 mb-lg-0" aria-label="Global">
            <ul class="d-lg-flex list-style-none">
                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-3 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false" fdprocessedid="6jflmh">
        Product
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 py-2 py-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 d-lg-flex dropdown-menu-wide">
          <div class="px-lg-4 border-lg-right mb-4 mb-lg-0 pr-lg-7">
            <ul class="list-style-none f5">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Actions&quot;,&quot;label&quot;:&quot;ref_cta:Actions;&quot;}" href="https://github.com/features/actions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-workflow color-fg-subtle mr-3">
    <path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Actions</div>
        Automate any workflow
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Packages&quot;,&quot;label&quot;:&quot;ref_cta:Packages;&quot;}" href="https://github.com/features/packages">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-package color-fg-subtle mr-3">
    <path d="M12.876.64V.639l8.25 4.763c.541.313.875.89.875 1.515v9.525a1.75 1.75 0 0 1-.875 1.516l-8.25 4.762a1.748 1.748 0 0 1-1.75 0l-8.25-4.763a1.75 1.75 0 0 1-.875-1.515V6.917c0-.625.334-1.202.875-1.515L11.126.64a1.748 1.748 0 0 1 1.75 0Zm-1 1.298L4.251 6.34l7.75 4.474 7.75-4.474-7.625-4.402a.248.248 0 0 0-.25 0Zm.875 19.123 7.625-4.402a.25.25 0 0 0 .125-.216V7.639l-7.75 4.474ZM3.501 7.64v8.803c0 .09.048.172.125.216l7.625 4.402v-8.947Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Packages</div>
        Host and manage packages
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Security&quot;,&quot;label&quot;:&quot;ref_cta:Security;&quot;}" href="https://github.com/features/security">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-shield-check color-fg-subtle mr-3">
    <path d="M16.53 9.78a.75.75 0 0 0-1.06-1.06L11 13.19l-1.97-1.97a.75.75 0 0 0-1.06 1.06l2.5 2.5a.75.75 0 0 0 1.06 0l5-5Z"></path><path d="m12.54.637 8.25 2.675A1.75 1.75 0 0 1 22 4.976V10c0 6.19-3.771 10.704-9.401 12.83a1.704 1.704 0 0 1-1.198 0C5.77 20.705 2 16.19 2 10V4.976c0-.758.489-1.43 1.21-1.664L11.46.637a1.748 1.748 0 0 1 1.08 0Zm-.617 1.426-8.25 2.676a.249.249 0 0 0-.173.237V10c0 5.46 3.28 9.483 8.43 11.426a.199.199 0 0 0 .14 0C17.22 19.483 20.5 15.461 20.5 10V4.976a.25.25 0 0 0-.173-.237l-8.25-2.676a.253.253 0 0 0-.154 0Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Security</div>
        Find and fix vulnerabilities
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Codespaces&quot;,&quot;label&quot;:&quot;ref_cta:Codespaces;&quot;}" href="https://github.com/features/codespaces">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-codespaces color-fg-subtle mr-3">
    <path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Codespaces</div>
        Instant dev environments
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Copilot&quot;,&quot;label&quot;:&quot;ref_cta:Copilot;&quot;}" href="https://github.com/features/copilot">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-copilot color-fg-subtle mr-3">
    <path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Copilot</div>
        Write better code with AI
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Code review&quot;,&quot;label&quot;:&quot;ref_cta:Code review;&quot;}" href="https://github.com/features/code-review">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-code-review color-fg-subtle mr-3">
    <path d="M10.3 6.74a.75.75 0 0 1-.04 1.06l-2.908 2.7 2.908 2.7a.75.75 0 1 1-1.02 1.1l-3.5-3.25a.75.75 0 0 1 0-1.1l3.5-3.25a.75.75 0 0 1 1.06.04Zm3.44 1.06a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.908-2.7-2.908-2.7Z"></path><path d="M1.5 4.25c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v12.5a1.75 1.75 0 0 1-1.75 1.75h-9.69l-3.573 3.573A1.458 1.458 0 0 1 5 21.043V18.5H3.25a1.75 1.75 0 0 1-1.75-1.75ZM3.25 4a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 .75.75v3.19l3.72-3.72a.749.749 0 0 1 .53-.22h10a.25.25 0 0 0 .25-.25V4.25a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Code review</div>
        Manage code changes
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center pb-lg-3" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Issues&quot;,&quot;label&quot;:&quot;ref_cta:Issues;&quot;}" href="https://github.com/features/issues">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-issue-opened color-fg-subtle mr-3">
    <path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Zm9.5 2a2 2 0 1 1-.001-3.999A2 2 0 0 1 12 14Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Issues</div>
        Plan and track work
      </div>

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Discussions&quot;,&quot;label&quot;:&quot;ref_cta:Discussions;&quot;}" href="https://github.com/features/discussions">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-comment-discussion color-fg-subtle mr-3">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 14.25 14H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 15.543V14H1.75A1.75 1.75 0 0 1 0 12.25v-9.5C0 1.784.784 1 1.75 1ZM1.5 2.75v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Z"></path><path d="M22.5 8.75a.25.25 0 0 0-.25-.25h-3.5a.75.75 0 0 1 0-1.5h3.5c.966 0 1.75.784 1.75 1.75v9.5A1.75 1.75 0 0 1 22.25 20H21v1.543a1.457 1.457 0 0 1-2.487 1.03L15.939 20H10.75A1.75 1.75 0 0 1 9 18.25v-1.465a.75.75 0 0 1 1.5 0v1.465c0 .138.112.25.25.25h5.5a.75.75 0 0 1 .53.22l2.72 2.72v-2.19a.75.75 0 0 1 .75-.75h2a.25.25 0 0 0 .25-.25v-9.5Z"></path>
</svg>
      <div>
        <div class="color-fg-default h4">Discussions</div>
        Collaborate outside of code
      </div>

    
</a></li>

            </ul>
          </div>
          <div class="px-lg-4">
              <span class="d-block h4 color-fg-default my-1" id="product-explore-heading">Explore</span>
            <ul class="list-style-none f5" aria-labelledby="product-explore-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to All features&quot;,&quot;label&quot;:&quot;ref_cta:All features;&quot;}" href="https://github.com/features">
      All features

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Documentation&quot;,&quot;label&quot;:&quot;ref_cta:Documentation;&quot;}" href="https://docs.github.com/">
      Documentation

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to GitHub Skills&quot;,&quot;label&quot;:&quot;ref_cta:GitHub Skills;&quot;}" href="https://skills.github.com/">
      GitHub Skills

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Product&quot;,&quot;action&quot;:&quot;click to go to Blog&quot;,&quot;label&quot;:&quot;ref_cta:Blog;&quot;}" href="https://github.blog/">
      Blog

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-3 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false" fdprocessedid="we16z">
        Solutions
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 py-2 py-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 px-lg-4">
          <div class="border-bottom pb-3 mb-3">
              <span class="d-block h4 color-fg-default my-1" id="solutions-for-heading">For</span>
            <ul class="list-style-none f5" aria-labelledby="solutions-for-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Enterprise&quot;,&quot;label&quot;:&quot;ref_cta:Enterprise;&quot;}" href="https://github.com/enterprise">
      Enterprise

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Teams&quot;,&quot;label&quot;:&quot;ref_cta:Teams;&quot;}" href="https://github.com/team">
      Teams

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Startups&quot;,&quot;label&quot;:&quot;ref_cta:Startups;&quot;}" href="https://github.com/enterprise/startups">
      Startups

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Education&quot;,&quot;label&quot;:&quot;ref_cta:Education;&quot;}" href="https://education.github.com/">
      Education

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
          <div class="border-bottom pb-3 mb-3">
              <span class="d-block h4 color-fg-default my-1" id="solutions-by-solution-heading">By Solution</span>
            <ul class="list-style-none f5" aria-labelledby="solutions-by-solution-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to CI/CD &amp;amp; Automation&quot;,&quot;label&quot;:&quot;ref_cta:CI/CD &amp;amp; Automation;&quot;}" href="https://github.com/solutions/ci-cd">
      CI/CD &amp; Automation

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to DevOps&quot;,&quot;label&quot;:&quot;ref_cta:DevOps;&quot;}" href="https://github.com/solutions/devops">
      DevOps

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to DevSecOps&quot;,&quot;label&quot;:&quot;ref_cta:DevSecOps;&quot;}" href="https://resources.github.com/devops/fundamentals/devsecops">
      DevSecOps

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
          <div class="">
              <span class="d-block h4 color-fg-default my-1" id="solutions-resources-heading">Resources</span>
            <ul class="list-style-none f5" aria-labelledby="solutions-resources-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Learning Pathways&quot;,&quot;label&quot;:&quot;ref_cta:Learning Pathways;&quot;}" href="https://resources.github.com/learn/pathways">
      Learning Pathways

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to White papers, Ebooks, Webinars&quot;,&quot;label&quot;:&quot;ref_cta:White papers, Ebooks, Webinars;&quot;}" href="https://resources.github.com/">
      White papers, Ebooks, Webinars

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Customer Stories&quot;,&quot;label&quot;:&quot;ref_cta:Customer Stories;&quot;}" href="https://github.com/customer-stories">
      Customer Stories

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" target="_blank" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Solutions&quot;,&quot;action&quot;:&quot;click to go to Partners&quot;,&quot;label&quot;:&quot;ref_cta:Partners;&quot;}" href="https://partner.github.com/">
      Partners

    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link-external HeaderMenu-external-icon color-fg-subtle">
    <path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path>
</svg>
</a></li>

            </ul>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
      <button type="button" class="HeaderMenu-link border-0 width-full width-lg-auto px-0 px-lg-2 py-3 py-lg-2 no-wrap d-flex flex-items-center flex-justify-between js-details-target" aria-expanded="false" fdprocessedid="t74c3d">
        Open Source
        <svg opacity="0.5" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down HeaderMenu-icon ml-1">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
      </button>
      <div class="HeaderMenu-dropdown dropdown-menu rounded m-0 p-0 py-2 py-lg-4 position-relative position-lg-absolute left-0 left-lg-n3 px-lg-4">
          <div class="border-bottom pb-3 mb-3">
            <ul class="list-style-none f5">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to GitHub Sponsors&quot;,&quot;label&quot;:&quot;ref_cta:GitHub Sponsors;&quot;}" href="https://github.com/sponsors">
      
      <div>
        <div class="color-fg-default h4">GitHub Sponsors</div>
        Fund open source developers
      </div>

    
</a></li>

            </ul>
          </div>
          <div class="border-bottom pb-3 mb-3">
            <ul class="list-style-none f5">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary d-flex flex-items-center" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to The ReadME Project&quot;,&quot;label&quot;:&quot;ref_cta:The ReadME Project;&quot;}" href="https://github.com/readme">
      
      <div>
        <div class="color-fg-default h4">The ReadME Project</div>
        GitHub community articles
      </div>

    
</a></li>

            </ul>
          </div>
          <div class="">
              <span class="d-block h4 color-fg-default my-1" id="open-source-repositories-heading">Repositories</span>
            <ul class="list-style-none f5" aria-labelledby="open-source-repositories-heading">
                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to Topics&quot;,&quot;label&quot;:&quot;ref_cta:Topics;&quot;}" href="https://github.com/topics">
      Topics

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to Trending&quot;,&quot;label&quot;:&quot;ref_cta:Trending;&quot;}" href="https://github.com/trending">
      Trending

    
</a></li>

                <li>
  <a class="HeaderMenu-dropdown-link lh-condensed d-block no-underline position-relative py-2 Link--secondary" data-analytics-event="{&quot;category&quot;:&quot;Header dropdown (logged out), Open Source&quot;,&quot;action&quot;:&quot;click to go to Collections&quot;,&quot;label&quot;:&quot;ref_cta:Collections;&quot;}" href="https://github.com/collections">
      Collections

    
</a></li>

            </ul>
          </div>
      </div>
</li>


                <li class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item">
    <a class="HeaderMenu-link no-underline px-0 px-lg-2 py-3 py-lg-2 d-block d-lg-inline-block" data-analytics-event="{&quot;category&quot;:&quot;Header menu top item (logged out)&quot;,&quot;action&quot;:&quot;click to go to Pricing&quot;,&quot;label&quot;:&quot;ref_cta:Pricing;&quot;}" href="https://github.com/pricing">Pricing</a>
</li>

            </ul>
          </nav>

        <div class="d-lg-flex flex-items-center mb-3 mb-lg-0 text-center text-lg-left ml-3" style="">
                


<qbsearch-input class="search-input" data-scope="repo:anweasha/Pharmacy_Management_System" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="8qvlGjWrBi32LgKlOwEYMyAMwnIo5rHQvO-XgbeCqbWMG1aUwG6hWh9RfPfd1h490ItoKShN4UK_WOY4HuJutg" data-max-custom-scopes="10" data-header-redesign-enabled="false" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="anweasha/Pharmacy_Management_System" data-current-org="" data-current-owner="anweasha" data-logged-in="false" data-copilot-chat-enabled="false" data-blackbird-indexed-repo-csrf="&lt;input type=&quot;hidden&quot; value=&quot;BbMvnzT3DMsb-xzVHHYyvDtO2Cn7yNH0QI0lKkrkK_H28R2UHpKYZOG2gwg2_F446Nes8OOXflI4VnnyQbrGKQ&quot; data-csrf=&quot;true&quot; /&gt;" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center mr-4 rounded" data-action="click:qbsearch-input#searchInputContainerClicked">
      <button type="button" class="header-search-button placeholder input-button form-control d-flex flex-1 flex-self-stretch flex-items-center no-wrap width-full py-0 pl-2 pr-0 text-left border-0 box-shadow-none" data-target="qbsearch-input.inputButton" placeholder="Search or jump to..." data-hotkey="s,/" autocapitalize="off" data-action="click:qbsearch-input#handleExpand" fdprocessedid="hpq12f">
        <div class="mr-2 color-fg-muted">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <span class="flex-1" data-target="qbsearch-input.inputButtonText">Search or jump to...</span>
          <div class="d-flex" data-target="qbsearch-input.hotkeyIndicator">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>

          </div>
      </button>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-large Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-fixed width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/anweasha/Pharmacy_Management_System/blob/main/main.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-261a2921-8645-4a8e-ad29-fc7e3b9e9213" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-261a2921-8645-4a8e-ad29-fc7e3b9e9213" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="uHLrdJoNlFfA_fSrlY4ATczVank78T-rOkUHjjT7VExYAoOycrAKqfKi43Au9XysTLb2AYk4soNQF5a_GT9rIQ">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="4OvumakH1LkziZ03c7m7boIbGvtJmu4T9VnGFz-WQJ95Ls7tC_Wz59EYsNN5ZKGtXX1bxJXNRnvmV18h7n3qrg">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="G-qNt-8kl7NOTz_03nwleBp-TAza6Tt55RGIijkOkeKhMMrl5sgXpvIBGJlrxSVYCvdyUg1fV0ZZtKeQrfpmvg" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="Zpm--hWLSydZ-BhGl7UeWMOaryho62lnXyPJ39NSx1necwcf-JUyCb2X5_sMyhgXUYYmgh2NlEsGAXFjZBrGAg" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


          <div class="position-relative mr-lg-3 d-lg-inline-block">
            <a href="https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fanweasha%2FPharmacy_Management_System%2Fblob%2Fmain%2Fdrug_data.db" class="HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="e9ddb64bc836d847d4e5bdb94ec70a1c232cec97dc5070cb6e681b5137d66e9c" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
              Sign in
            </a>
          </div>

            <a href="https://github.com/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&amp;source=header-repo&amp;source_repo=anweasha%2FPharmacy_Management_System" class="HeaderMenu-link HeaderMenu-link--sign-up flex-shrink-0 d-none d-lg-inline-block no-underline border color-border-default rounded px-2 py-1" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="e9ddb64bc836d847d4e5bdb94ec70a1c232cec97dc5070cb6e681b5137d66e9c" data-analytics-event="{&quot;category&quot;:&quot;Sign up&quot;,&quot;action&quot;:&quot;click to sign up for account&quot;,&quot;label&quot;:&quot;ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show;ref_cta:Sign up;ref_loc:header logged out&quot;}">
              Sign up
            </a>
        </div>
      </div>
    </div>
  </div>
</header>

      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/anweasha/Pharmacy_Management_System/blob/main/main.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/anweasha/Pharmacy_Management_System/blob/main/main.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/anweasha/Pharmacy_Management_System/blob/main/main.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-ee0e31dc-3a9c-4a27-adf7-2cb2dc548d42" aria-labelledby="tooltip-96f12490-e21f-4929-b696-b6a8da98a9f0" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-96f12490-e21f-4929-b696-b6a8da98a9f0" for="icon-button-ee0e31dc-3a9c-4a27-adf7-2cb2dc548d42" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">





  <template class="js-flash-template"></template>
</div>


    
    <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template></include-fragment>





  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






  
  <div id="repository-container-header" class="pt-3 hide-full-screen" style="background-color: var(--page-header-bgColor, var(--color-page-header-bg));" data-turbo-replace="">

      <div class="d-flex flex-wrap flex-justify-end mb-3  px-3 px-md-4 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit mr-3">
            
  <div class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked color-fg-muted mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
    
    <span class="author flex-self-stretch" itemprop="author">
      <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/anweasha/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/anweasha">
        anweasha
</a>    </span>
    <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
    <strong itemprop="name" class="mr-2 flex-self-stretch">
      <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" href="https://github.com/anweasha/Pharmacy_Management_System">Pharmacy_Management_System</a>
    </strong>

    <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
  </div>
    <span class="text-small lh-condensed-ultra no-wrap mt-1" data-repository-hovercards-enabled="">
      forked from <a data-hovercard-type="repository" data-hovercard-url="/Aditimittal2809/Pharmacy_Management_System/hovercard" class="Link--inTextBlock" href="https://github.com/Aditimittal2809/Pharmacy_Management_System">Aditimittal2809/Pharmacy_Management_System</a>
    </span>


        </div>

        <div id="repository-details-container" data-turbo-replace="">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      

  <li>
            <a href="https://github.com/login?return_to=%2Fanweasha%2FPharmacy_Management_System" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="a277b6ba77befb94149f3cf05ed62c0605cbe5b2e4a06f7817dd77cf84d860d8" aria-label="You must be signed in to change notification settings" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell mr-2">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>Notifications
</a>
  </li>

  <li>
          <a icon="repo-forked" id="fork-button" href="https://github.com/login?return_to=%2Fanweasha%2FPharmacy_Management_System" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:488082647,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="0ea37206666ea12cfaa9384b18dd9ce1b3dd24ed0f370e69d011fd61c055aef8" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
    <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="5" data-view-component="true" class="Counter">5</span>
</a>
  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <a href="https://github.com/login?return_to=%2Fanweasha%2FPharmacy_Management_System" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:488082647,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ce7009848faafa4c24a2d58a2518325ecd168441aed508ef6516116092faa70d" aria-label="You must be signed in to star a repository" data-view-component="true" class="tooltipped tooltipped-s btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star v-align-text-bottom d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="16 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="16" data-view-component="true" class="Counter js-social-count">16</span>
</a>        <button aria-label="You must be signed in to add this repository to a list" type="button" disabled="disabled" data-view-component="true" class="btn-sm btn BtnGroup-item px-2">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button></div>
  </li>

    <li>
        

    </li>
</ul>

        </div>
      </div>

        <div id="responsive-meta-container" data-turbo-replace="">
</div>


          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/anweasha/Pharmacy_Management_System" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /anweasha/Pharmacy_Management_System" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/anweasha/Pharmacy_Management_System/pulls" data-tab-item="i1pull-requests-tab" data-selected-links="repo_pulls checks /anweasha/Pharmacy_Management_System/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/anweasha/Pharmacy_Management_System/actions" data-tab-item="i2actions-tab" data-selected-links="repo_actions /anweasha/Pharmacy_Management_System/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/anweasha/Pharmacy_Management_System/projects" data-tab-item="i3projects-tab" data-selected-links="repo_projects new_repo_project repo_project /anweasha/Pharmacy_Management_System/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/anweasha/Pharmacy_Management_System/security" data-tab-item="i4security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /anweasha/Pharmacy_Management_System/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/anweasha/Pharmacy_Management_System/pulse" data-tab-item="i5insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /anweasha/Pharmacy_Management_System/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-button" popovertarget="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-overlay" aria-controls="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-list" aria-haspopup="true" aria-labelledby="tooltip-b212e924-7788-4bba-b47e-29f8feed0902" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-b212e924-7788-4bba-b47e-29f8feed0902" for="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position id="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-overlay" anchor="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-button" id="action-menu-16f074df-2ec0-4792-a9df-f91a5b01f53d-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-5b8ca476-d50e-453e-9412-ad41e6847b16" href="https://github.com/anweasha/Pharmacy_Management_System" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span></a>
  
</li>
        <li hidden="" data-menu-item="i1pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-d8037028-ccb3-4a40-aeae-646bcfb6e1a5" href="https://github.com/anweasha/Pharmacy_Management_System/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
</li>
        <li hidden="" data-menu-item="i2actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-45be6e1b-45ff-4658-8fc4-43bcd655ff66" href="https://github.com/anweasha/Pharmacy_Management_System/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span></a>
  
</li>
        <li hidden="" data-menu-item="i3projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-cac040d0-980d-483e-90e7-7cb1878bd5b7" href="https://github.com/anweasha/Pharmacy_Management_System/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
</li>
        <li hidden="" data-menu-item="i4security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-95849981-3e18-4d37-8c76-844f106e5e19" href="https://github.com/anweasha/Pharmacy_Management_System/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span></a>
  
</li>
        <li hidden="" data-menu-item="i5insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-217a151a-e291-4e6c-ac58-15edcf479e2e" href="https://github.com/anweasha/Pharmacy_Management_System/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span></a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>

  </div>

  



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
    



    
      
    





<react-app app-name="react-code-view" initial-path="/anweasha/Pharmacy_Management_System/blob/main/drug_data.db" style="min-height: calc(100vh - 64px)" data-ssr="false" data-lazy="false" data-alternate="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":false,"fileTree":{"":{"items":[{"name":"images","path":"images","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"drug_data.db","path":"drug_data.db","contentType":"file"},{"name":"drugdatabase.sql","path":"drugdatabase.sql","contentType":"file"},{"name":"main.py","path":"main.py","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":2.8794939999999998,"foldersToFetch":[],"repo":{"id":488082647,"defaultBranch":"main","name":"Pharmacy_Management_System","ownerLogin":"anweasha","currentUserCanPush":false,"isFork":true,"isEmpty":false,"createdAt":"2022-05-03T10:29:22.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/86158020?v=4","public":true,"private":false,"isOrgOwned":false},"codeLineWrapEnabled":false,"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1651553968.8350542","canEdit":false,"refType":"branch","currentOid":"6354f9c617f17cfb46021cc97c3aedde68721c99"},"path":"drug_data.db","currentUser":null,"blob":{"rawLines":null,"stylingDirectives":null,"colorizedLines":null,"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/anweasha/Pharmacy_Management_System/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"drug_data.db","displayUrl":"https://github.com/anweasha/Pharmacy_Management_System/blob/main/drug_data.db?raw=true","headerInfo":{"blobSize":"28 KB","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"onBranch":true,"shortPath":"c98bd6b","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fanweasha%2FPharmacy_Management_System%2Fblob%2Fmain%2Fdrug_data.db","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":null,"truncatedSloc":null},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":null,"languageID":null,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/anweasha/Pharmacy_Management_System/blob/main/drug_data.db","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/anweasha/Pharmacy_Management_System/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/anweasha/Pharmacy_Management_System/raw/main/drug_data.db","renderImageOrRaw":true,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":false,"workflowRedirectUrl":null,"symbols":null},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/anweasha/Pharmacy_Management_System/branches":{"post":"vbn7UVyiR_qbEiiJOfyws-0xYZQM_A4fVjUnSwaFPWWCNukoiP_EpAczk1pgTK8OopytzfyaL_FpCHqDDBVG-Q"},"/repos/preferences":{"post":"JS4UHImTv8OTKajxBrKvwk-IlwZfyS-Ht0_tmSMb6E4CkCRdvP2SefBC8BuXrlq7zkvHiw4YFHyqAq4NrIw5EQ"}}},"title":"Pharmacy_Management_System/drug_data.db at main · anweasha/Pharmacy_Management_System","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-a007d7f370d6.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-d0f0ff069004.js","githubDevUrl":null,"enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":false,"copilot_conversational_ux_embedding_update":false,"copilot_smell_icebreaker_ux":true,"copilot_workspace":false}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish">    <button hidden="" data-testid="header-permalink-button" data-hotkey="y,Shift+Y" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div class="Box-sc-g0xbh4-0 fSWWem" style="--sticky-pane-height: calc(100vh - (max(36.60000228881836px, 0px)));"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 xEgty"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div class="Box-sc-g0xbh4-0 gNdDUH" style="--pane-width: 320px;"><div class="Box-sc-g0xbh4-0"><div id="repos-file-tree" class="Box-sc-g0xbh4-0 jyDQiw"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 jUriTl"><span role="tooltip" aria-label="Collapse file tree" id="expand-button-file-tree-button" class="Tooltip__TooltipBase-sc-17tf59c-0 gNgnVl tooltipped-se"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-labelledby="expand-button-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" data-hotkey="Control+b" class="types__StyledButton-sc-ws60qy-0 dWnuhe" data-no-visuals="true" fdprocessedid="e0mjf"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button></span><button hidden="" data-testid="" data-hotkey="Control+b" data-hotkey-scope="read-only-cursor-text-area"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Files</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-repos-header-ref-selector" aria-haspopup="true" tabindex="0" data-hotkey="w" aria-label="main branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 fruYDV react-repos-tree-pane-ref-selector width-full ref-selector-class" fdprocessedid="fg8l4"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 iPGYsi"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk ref-selector-button-text-container"><span class="Text-sc-17v1xeu-0 bOMzPg">&nbsp;main</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey="w" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 jahcnb"><button data-component="IconButton" type="button" aria-label="Search this repository" data-hotkey="/" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jIEvFL" fdprocessedid="4i0qia"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div><div class="Box-sc-g0xbh4-0 jRttMj"><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 cXNreu jbzqwE TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value="" fdprocessedid="49gijp"><span class="TextInput-icon"></span></span></div><button hidden="" data-testid="" data-hotkey="t,Shift+T" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="t,Shift+T"></button><div class="Box-sc-g0xbh4-0 bYLCoz"><div><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 erWCJP"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 TIGQC"><li class="PRIVATE_TreeView-item" tabindex="0" id="images-item" role="treeitem" aria-labelledby=":r20:" aria-describedby=":r21: :r22:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r20:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r21:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>images</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="README.md-item" role="treeitem" aria-labelledby=":r23:" aria-describedby=":r24: :r25:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r23:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r24:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="drug_data.db-item" role="treeitem" aria-labelledby=":r26:" aria-describedby=":r27: :r28:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r26:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r27:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>drug_data.db</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="drugdatabase.sql-item" role="treeitem" aria-labelledby=":r29:" aria-describedby=":r2a: :r2b:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r29:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r2a:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>drugdatabase.sql</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="main.py-item" role="treeitem" aria-labelledby=":r2c:" aria-describedby=":r2d: :r2e:" aria-level="1" aria-selected="true" aria-current="true"><div class="PRIVATE_TreeView-item-container" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r2c:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r2d:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>main.py</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 gMNHHu"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="577" aria-valuenow="0" aria-valuetext="Pane width 0 pixels" tabindex="0" class="Box-sc-g0xbh4-0 fjdBNx"></div></div></div></div><div class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 eIgvIk"><div class="Box-sc-g0xbh4-0 eVFfWF container"><div class="px-3 pt-3 pb-0" id="StickyHeader"><div class="Box-sc-g0xbh4-0 fywjmm"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 kszRgZ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 ipyMWB" href="https://github.com/anweasha/Pharmacy_Management_System/tree/main">Pharmacy_Management_System</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fIsVJr">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">main.py</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 ivbpoP" fdprocessedid="e7agji"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="react-code-view-header-element--wide"><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hviaoI"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 jXTShb js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button-nav-menu-wide" id=":r2j:" aria-haspopup="true" tabindex="0" data-no-visuals="true" fdprocessedid="zdsbq"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div><div class="react-code-view-header-element--narrow"><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 hviaoI"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 jXTShb js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button-nav-menu-narrow" id=":r2l:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 hVZtwF react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 cMYnca"></div>   </div><div class="Box-sc-g0xbh4-0 hVZtwF">   <button hidden="" data-testid="" data-hotkey="r,Shift+R" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="Box-sc-g0xbh4-0 jQCQnS"><div class="Box-sc-g0xbh4-0 eYedVD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="Box-sc-g0xbh4-0 drtGBr"><div class="Box-sc-g0xbh4-0 eScEiW"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hLLhje"><a href="https://github.com/VijayRavichander" data-testid="avatar-icon-link" data-hovercard-url="/users/VijayRavichander/hovercard" class="Link__StyledLink-sc-14289xe-0 dheQRw"><img alt="VijayRavichander" size="20" src="./main_files/58650933" data-testid="github-avatar" aria-label="VijayRavichander" height="20" width="20" class="Avatar__StyledAvatar-sc-2lv0r8-0 kYMvPL"></a><a href="https://github.com/anweasha/Pharmacy_Management_System/commits?author=VijayRavichander" aria-label="commits by VijayRavichander" data-hovercard-url="/users/VijayRavichander/hovercard" class="Link__StyledLink-sc-14289xe-0 XuJeD">VijayRavichander</a></div><span class=""></span></div><div class="Box-sc-g0xbh4-0 fqNQBl react-last-commit-message"><div class="Box-sc-g0xbh4-0 jEKUjt Truncate"><span class="Text-sc-17v1xeu-0 gPDEWA Truncate-text" data-testid="latest-commit-html"><a href="https://github.com/anweasha/Pharmacy_Management_System/commit/339dd79b0594da235009eab4f4e06e5476cced61" class="Link--secondary" data-pjax="true" data-hovercard-url="/anweasha/Pharmacy_Management_System/commit/339dd79b0594da235009eab4f4e06e5476cced61/hovercard">Add files via upload</a></span></div></div><span class="Text-sc-17v1xeu-0 bESgln react-last-commit-summary-timestamp"><relative-time class="sc-bcXHqe" tense="past" datetime="2022-04-23T09:01:27.000Z" title="Apr 23, 2022, 2:31 PM GMT+5:30"><template shadowrootmode="open">2 years ago</template>Apr 23, 2022</relative-time></span></div><div data-testid="latest-commit-details" class="Box-sc-g0xbh4-0 lhFvfi"><span class="Text-sc-17v1xeu-0 bESgln react-last-commit-oid-timestamp"><a class="Link__StyledLink-sc-14289xe-0 dheQRw Link--secondary" aria-label="Commit 339dd79" href="https://github.com/anweasha/Pharmacy_Management_System/commit/339dd79b0594da235009eab4f4e06e5476cced61">339dd79</a>&nbsp;·&nbsp;<relative-time class="sc-bcXHqe" tense="past" datetime="2022-04-23T09:01:27.000Z" title="Apr 23, 2022, 2:31 PM GMT+5:30"><template shadowrootmode="open">2 years ago</template>Apr 23, 2022</relative-time></span><span class="Text-sc-17v1xeu-0 bESgln react-last-commit-timestamp"><relative-time class="sc-bcXHqe" tense="past" datetime="2022-04-23T09:01:27.000Z" title="Apr 23, 2022, 2:31 PM GMT+5:30"><template shadowrootmode="open">2 years ago</template>Apr 23, 2022</relative-time></span></div><div class="Box-sc-g0xbh4-0 jGfYmh"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">History</h2><a class="types__StyledButton-sc-ws60qy-0 fAkXQN react-last-commit-history-group" href="https://github.com/anweasha/Pharmacy_Management_System/commits/main/main.py" data-size="small"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text"><span class="Text-sc-17v1xeu-0 dALsKK">History</span></span></span></a><div class="Box-sc-g0xbh4-0 bqgLjk"><button data-component="IconButton" type="button" aria-label="Open commit details" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iGsLPX"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button></div><span role="tooltip" aria-label="Commit history" id=":r2n:" class="Tooltip__TooltipBase-sc-17tf59c-0 gNgnVl tooltipped-n"><a class="types__StyledButton-sc-ws60qy-0 fAkXQN react-last-commit-history-icon" href="https://github.com/anweasha/Pharmacy_Management_System/commits/main/main.py"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div><div class="Box-sc-g0xbh4-0 iJmJly"><div class="Box-sc-g0xbh4-0 jACbi container"><div class="Box-sc-g0xbh4-0 gIJuDf react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 BnySK text-mono"><div title="10.9 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">320 lines (242 loc) · 10.9 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 VHzRk react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 ePiodO"><div class="Box-sc-g0xbh4-0 react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 kQJlnf"><div class="Box-sc-g0xbh4-0 gJICKO"><div class="Box-sc-g0xbh4-0 iZJewz"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 ipyMWB" href="https://github.com/anweasha/Pharmacy_Management_System/tree/main">Pharmacy_Management_System</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 cYjMDB">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 jAEDJk">main.py</h1></div></div><button type="button" data-size="small" class="types__StyledButton-sc-ws60qy-0 gfKkfV" style="--button-color: fg.default;"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 jfjHXm"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 bfkNRF"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 huxtnT"><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" data-hotkey="Control+/ Control+c" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 dAjliH" fdprocessedid="oko4x0o"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 gMPsNT"><button aria-current="false" data-hotkey="b,Shift+B,Control+/ Control+b" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 fIktcg" fdprocessedid="eahw8q"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey="Control+/ Control+c" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 BnySK text-mono"><div title="10.9 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">320 lines (242 loc) · 10.9 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 iBylDf"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><div class="Box-sc-g0xbh4-0 kSGBPx react-blob-header-edit-and-raw-actions"><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><a href="https://github.com/anweasha/Pharmacy_Management_System/raw/main/main.py" data-testid="raw-button" data-hotkey="Control+/ Control+r" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 dTgfec"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" data-hotkey="Control+Shift+C" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 pyyxt" fdprocessedid="s8lvar"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" id=":r2p:" class="Tooltip__TooltipBase-sc-17tf59c-0 gNgnVl tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" data-hotkey="Control+Shift+S" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 fmvlPZ" fdprocessedid="qtp4qd"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey="Control+/ Control+r" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey="Control+Shift+C" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey="Control+Shift+S" data-hotkey-scope="read-only-cursor-text-area"></button><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><span role="tooltip" aria-label="You must be signed in to make or propose changes" id=":r2q:" class="Tooltip__TooltipBase-sc-17tf59c-0 gNgnVl tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Edit file" class="types__StyledButton-sc-ws60qy-0 bwSTmS btn" aria-disabled="true" data-size="small" data-no-visuals="true" fdprocessedid="4gtrjt"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></button></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" id=":r2r:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 pyyxt" fdprocessedid="8kd06i"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div></div><span role="tooltip" aria-label="Open symbols panel" id=":r32:" class="Tooltip__TooltipBase-sc-17tf59c-0 gNgnVl tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Symbols" aria-pressed="false" aria-expanded="false" aria-controls="symbols-pane" class="types__StyledButton-sc-ws60qy-0 bcQZPI" data-hotkey="Control+i" data-testid="symbols-button" id="symbols-button" data-size="small" data-no-visuals="true" fdprocessedid="qode3c"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button></span><div class="Box-sc-g0xbh4-0 react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" class="types__StyledButton-sc-ws60qy-0 dGDIQc js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":r2t:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div></div></div><div class="Box-sc-g0xbh4-0 ytOJl"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 jWnGGx"><div class="Box-sc-g0xbh4-0 TCenl"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div class="Box-sc-g0xbh4-0 eRkHwF"><div class="Box-sc-g0xbh4-0 cVawVl"><div class="Box-sc-g0xbh4-0 gZCGFC"><div aria-hidden="true" data-testid="navigation-cursor" class="Box-sc-g0xbh4-0 code-navigation-cursor" style="top: 0px; left: 92px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Control+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><textarea id="read-only-cursor-text-area" data-testid="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 8; outline: none; overflow: auto hidden; height: 6420px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">import streamlit as st
import pandas as pd
from PIL import Image
#from drug_db import *
import random

## SQL DATABASE CODE
import sqlite3


conn = sqlite3.connect("drug_data.db",check_same_thread=False)
c = conn.cursor()

def cust_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Customers(
                    C_Name VARCHAR(50) NOT NULL,
                    C_Password VARCHAR(50) NOT NULL,
                    C_Email VARCHAR(50) PRIMARY KEY NOT NULL, 
                    C_State VARCHAR(50) NOT NULL,
                    C_Number VARCHAR(50) NOT NULL 
                    )''')
    print('Customer Table create Successfully')

def customer_add_data(Cname,Cpass, Cemail, Cstate,Cnumber):
    c.execute('''INSERT INTO Customers (C_Name,C_Password,C_Email, C_State, C_Number) VALUES(?,?,?,?,?)''', (Cname,Cpass,  Cemail, Cstate,Cnumber))
    conn.commit()

def customer_view_all_data():
    c.execute('SELECT * FROM Customers')
    customer_data = c.fetchall()
    return customer_data
def customer_update(Cemail,Cnumber):
    c.execute(''' UPDATE Customers SET C_Number = ? WHERE C_Email = ?''', (Cnumber,Cemail,))
    conn.commit()
    print("Updating")
def customer_delete(Cemail):
    c.execute(''' DELETE FROM Customers WHERE C_Email = ?''', (Cemail,))
    conn.commit()

def drug_update(Duse, Did):
    c.execute(''' UPDATE Drugs SET D_Use = ? WHERE D_id = ?''', (Duse,Did))
    conn.commit()
def drug_delete(Did):
    c.execute(''' DELETE FROM Drugs WHERE D_id = ?''', (Did,))
    conn.commit()

def drug_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Drugs(
                D_Name VARCHAR(50) NOT NULL,
                D_ExpDate DATE NOT NULL, 
                D_Use VARCHAR(50) NOT NULL,
                D_Qty INT NOT NULL, 
                D_id INT PRIMARY KEY NOT NULL)
                ''')
    print('DRUG Table create Successfully')

def drug_add_data(Dname, Dexpdate, Duse, Dqty, Did):
    c.execute('''INSERT INTO Drugs (D_Name, D_Expdate, D_Use, D_Qty, D_id) VALUES(?,?,?,?,?)''', (Dname, Dexpdate, Duse, Dqty, Did))
    conn.commit()

def drug_view_all_data():
    c.execute('SELECT * FROM Drugs')
    drug_data = c.fetchall()
    return drug_data

def order_create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
                O_Name VARCHAR(100) NOT NULL,
                O_Items VARCHAR(100) NOT NULL,
                O_Qty VARCHAR(100) NOT NULL,
                O_id VARCHAR(100) PRIMARY KEY NOT NULL)
    ''')

def order_delete(Oid):
    c.execute(''' DELETE FROM Orders WHERE O_id = ?''', (Oid,))

def order_add_data(O_Name,O_Items,O_Qty,O_id):
    c.execute('''INSERT INTO Orders (O_Name, O_Items,O_Qty, O_id) VALUES(?,?,?,?)''',
              (O_Name,O_Items,O_Qty,O_id))
    conn.commit()


def order_view_data(customername):
    c.execute('SELECT * FROM ORDERS Where O_Name == ?',(customername,))
    order_data = c.fetchall()
    return order_data

def order_view_all_data():
    c.execute('SELECT * FROM ORDERS')
    order_all_data = c.fetchall()
    return order_all_data






#__________________________________________________________________________________







def admin():


    st.title("Pharmacy Database Dashboard")
    menu = ["Drugs", "Customers", "Orders", "About"]
    choice = st.sidebar.selectbox("Menu", menu)



    ## DRUGS
    if choice == "Drugs":

        menu = ["Add", "View", "Update", "Delete"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":

            st.subheader("Add Drugs")

            col1, col2 = st.columns(2)

            with col1:
                drug_name = st.text_area("Enter the Drug Name")
                drug_expiry = st.date_input("Expiry Date of Drug (YYYY-MM-DD)")
                drug_mainuse = st.text_area("When to Use")
            with col2:
                drug_quantity = st.text_area("Enter the quantity")
                drug_id = st.text_area("Enter the Drug id (example:#D1)")

            if st.button("Add Drug"):
                drug_add_data(drug_name,drug_expiry,drug_mainuse,drug_quantity,drug_id)
                st.success("Successfully Added Data")
        if choice == "View":
            st.subheader("Drug Details")
            drug_result = drug_view_all_data()
            #st.write(drug_result)
            with st.expander("View All Drug Data"):
                drug_clean_df = pd.DataFrame(drug_result, columns=["Name", "Expiry Date", "Use", "Quantity", "ID"])
                st.dataframe(drug_clean_df)
            with st.expander("View Drug Quantity"):
                drug_name_quantity_df = drug_clean_df[['Name','Quantity']]
                #drug_name_quantity_df = drug_name_quantity_df.reset_index()
                st.dataframe(drug_name_quantity_df)
        if choice == 'Update':
            st.subheader("Update Drug Details")
            d_id = st.text_area("Drug ID")
            d_use = st.text_area("Drug Use")
            if st.button(label='Update'):
                drug_update(d_use,d_id)

        if choice == 'Delete':
            st.subheader("Delete Drugs")
            did = st.text_area("Drug ID")
            if st.button(label="Delete"):
                drug_delete(did)



    ## CUSTOMERS
    elif choice == "Customers":

        menu = ["View", "Update", "Delete"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "View":
            st.subheader("Customer Details")
            cust_result = customer_view_all_data()
            #st.write(cust_result)
            with st.expander("View All Customer Data"):
                cust_clean_df = pd.DataFrame(cust_result, columns=["Name", "Password","Email-ID" ,"Area", "Number"])
                st.dataframe(cust_clean_df)

        if choice == 'Update':
            st.subheader("Update Customer Details")
            cust_email = st.text_area("Email")
            cust_number = st.text_area("Phone Number")
            if st.button(label='Update'):
                customer_update(cust_email,cust_number)

        if choice == 'Delete':
            st.subheader("Delete Customer")
            cust_email = st.text_area("Email")
            if st.button(label="Delete"):
                customer_delete(cust_email)

    elif choice == "Orders":

        menu = ["View"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "View":
            st.subheader("Order Details")
            order_result = order_view_all_data()
            #st.write(cust_result)
            with st.expander("View All Order Data"):
                order_clean_df = pd.DataFrame(order_result, columns=["Name", "Items","Qty" ,"ID"])
                st.dataframe(order_clean_df)
    elif choice == "About":
        st.subheader("DBMS Mini Project")
        st.subheader("By Aditi (226), Anweasha (235) &amp; Vijay (239)")


def getauthenicate(username, password):
    #print("Auth")
    c.execute('SELECT C_Password FROM Customers WHERE C_Name = ?', (username,))
    cust_password = c.fetchall()
    #print(cust_password[0][0], "Outside password")
    #print(password, "Parameter password")
    if cust_password[0][0] == password:
        #print("Inside password")
        return True
    else:
        return False


###################################################################


def customer(username, password):
    if getauthenicate(username, password):
        print("In Customer")
        st.title("Welcome to Pharmacy Store")

        st.subheader("Your Order Details")
        order_result = order_view_data(username)
        # st.write(cust_result)
        with st.expander("View All Order Data"):
            order_clean_df = pd.DataFrame(order_result, columns=["Name", "Items", "Qty", "ID"])
            st.dataframe(order_clean_df)

        drug_result = drug_view_all_data()
        print(drug_result)


        st.subheader("Drug: "+drug_result[0][0])
        img = Image.open('images/dolo650.jpg')
        st.image(img, width=100, caption="Rs. 15/-")
        dolo650 = st.slider(label="Quantity",min_value=0, max_value=5, key= 1)
        st.info("When to USE: " + str(drug_result[0][2]))


        st.subheader("Drug: " + drug_result[1][0])
        img = Image.open('images/strepsils.JPG')
        st.image(img, width=100 , caption="Rs. 10/-")
        strepsils = st.slider(label="Quantity",min_value=0, max_value=5, key= 2)
        st.info("When to USE: " + str(drug_result[1][2]))

        st.subheader("Drug: " + drug_result[2][0])
        img = Image.open('images/vicks.JPG')
        st.image(img, width=100, caption="Rs. 65/-")
        vicks = st.slider(label="Quantity",min_value=0, max_value=5, key=3)
        st.info("When to USE: " + str(drug_result[2][2]))



        if st.button(label="Buy now"):
            O_items = ""

            if int(dolo650) &gt; 0:
                O_items += "Dolo-650,"
            if int(strepsils) &gt; 0:
                O_items += "Strepsils,"
            if int(vicks) &gt; 0:
                O_items += "Vicks"
            O_Qty = str(dolo650)+str(',') + str(strepsils) + str(",") + str(vicks)

            O_id = username + "#O" + str(random.randint(0,1000000))
            #order_add_data(O_Name, O_Items,O_Qty, O_id):
            order_add_data(username, O_items, O_Qty, O_id)








if __name__ == '__main__':
    drug_create_table()
    cust_create_table()
    order_create_table()

    menu = ["Login", "SignUp","Admin"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Login":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox(label="Login"):
            customer(username, password)

    elif choice == "SignUp":
        st.subheader("Create New Account")
        cust_name = st.text_input("Name")
        cust_password = st.text_input("Password", type='password', key=1000)
        cust_password1 = st.text_input("Confirm Password", type='password', key=1001)
        col1, col2, col3 = st.columns(3)

        with col1:
            cust_email = st.text_area("Email ID")
        with col2:
            cust_area = st.text_area("State")
        with col3:
            cust_number = st.text_area("Phone Number")

        if st.button("Signup"):
            if (cust_password == cust_password1):
                customer_add_data(cust_name,cust_password,cust_email, cust_area, cust_number,)
                st.success("Account Created!")
                st.info("Go to Login Menu to login")
            else:
                st.warning('Password dont match')
    elif choice == "Admin":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        # if st.sidebar.button("Login"):
        if username == 'admin' and password == 'admin':
            admin()</textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 cXpbTk"><div tabindex="0" class="Box-sc-g0xbh4-0 hHjsH"><div class="Box-sc-g0xbh4-0 VkLKX react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-testid="code-lines-container" data-paste-markdown-skip="true" data-hpc="true" style="height: 6400px;"><div class="react-line-numbers" style="pointer-events: auto; height: 6400px; position: relative; z-index: 2;"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(20px);">2</div><div data-line-number="3" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(40px);">3</div><div data-line-number="4" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(60px);">4</div><div data-line-number="5" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(80px);">5</div><div data-line-number="6" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(100px);">6</div><div data-line-number="7" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(120px);">7</div><div data-line-number="8" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(140px);">8</div><div data-line-number="9" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(160px);">9</div><div data-line-number="10" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(180px);">10</div><div data-line-number="11" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(200px);">11</div><div data-line-number="12" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(220px);">12</div><div data-line-number="13" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(240px);">13</div><div data-line-number="14" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(260px);">14<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="15" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(280px);">15</div><div data-line-number="16" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(300px);">16</div><div data-line-number="17" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(320px);">17</div><div data-line-number="18" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(340px);">18</div><div data-line-number="19" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(360px);">19</div><div data-line-number="20" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(380px);">20</div><div data-line-number="21" class="child-of-line-13  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(400px);">21</div><div data-line-number="22" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(420px);">22</div><div data-line-number="23" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(440px);">23</div><div data-line-number="24" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(460px);">24</div><div data-line-number="25" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(480px);">25</div><div data-line-number="26" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(500px);">26</div><div data-line-number="27" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(520px);">27</div><div data-line-number="28" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(540px);">28</div><div data-line-number="29" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(560px);">29</div><div data-line-number="30" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(580px);">30</div><div data-line-number="31" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(600px);">31</div><div data-line-number="32" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(620px);">32</div><div data-line-number="33" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(640px);">33</div><div data-line-number="34" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(660px);">34</div><div data-line-number="35" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(680px);">35</div><div data-line-number="36" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(700px);">36</div><div data-line-number="37" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(720px);">37</div><div data-line-number="38" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(740px);">38</div><div data-line-number="39" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(760px);">39</div><div data-line-number="40" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(780px);">40</div><div data-line-number="41" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(800px);">41</div><div data-line-number="42" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(820px);">42</div><div data-line-number="43" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(840px);">43</div><div data-line-number="44" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(860px);">44</div><div data-line-number="45" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(880px);">45</div><div data-line-number="46" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(900px);">46</div><div data-line-number="47" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(920px);">47<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="48" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(940px);">48</div><div data-line-number="49" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(960px);">49</div><div data-line-number="50" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(980px);">50</div><div data-line-number="51" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1000px);">51</div><div data-line-number="52" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1020px);">52</div><div data-line-number="53" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1040px);">53</div><div data-line-number="54" class="child-of-line-46  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1060px);">54</div><div data-line-number="55" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1080px);">55</div><div data-line-number="56" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1100px);">56</div><div data-line-number="57" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1120px);">57</div><div data-line-number="58" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1140px);">58</div><div data-line-number="59" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1160px);">59</div><div data-line-number="60" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1180px);">60</div><div data-line-number="61" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1200px);">61</div><div data-line-number="62" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1220px);">62</div><div data-line-number="63" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1240px);">63</div><div data-line-number="64" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1260px);">64</div><div data-line-number="65" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1280px);">65</div><div data-line-number="66" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1300px);">66<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="67" class="child-of-line-65  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1320px);">67</div><div data-line-number="68" class="child-of-line-65  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1340px);">68</div><div data-line-number="69" class="child-of-line-65  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1360px);">69</div><div data-line-number="70" class="child-of-line-65  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1380px);">70</div><div data-line-number="71" class="child-of-line-65  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1400px);">71</div><div data-line-number="72" class="child-of-line-65  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1420px);">72</div><div data-line-number="73" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1440px);">73</div><div data-line-number="74" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1460px);">74</div><div data-line-number="75" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1480px);">75</div><div data-line-number="76" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1500px);">76</div><div data-line-number="77" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1520px);">77</div><div data-line-number="78" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1540px);">78</div><div data-line-number="79" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1560px);">79</div><div data-line-number="80" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1580px);">80</div><div data-line-number="81" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1600px);">81</div><div data-line-number="82" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1620px);">82</div><div data-line-number="83" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1640px);">83</div><div data-line-number="84" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1660px);">84</div><div data-line-number="85" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1680px);">85</div><div data-line-number="86" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1700px);">86</div><div data-line-number="87" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1720px);">87</div><div data-line-number="88" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1740px);">88</div><div data-line-number="89" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1760px);">89</div><div data-line-number="90" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1780px);">90</div><div data-line-number="91" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1800px);">91</div><div data-line-number="92" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1820px);">92</div><div data-line-number="93" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1840px);">93</div><div data-line-number="94" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1860px);">94</div><div data-line-number="95" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1880px);">95</div><div data-line-number="96" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1900px);">96</div><div data-line-number="97" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1920px);">97</div><div data-line-number="98" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1940px);">98</div><div data-line-number="99" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1960px);">99</div><div data-line-number="100" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1980px);">100</div><div data-line-number="101" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2000px);">101</div><div data-line-number="102" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2020px);">102</div><div data-line-number="103" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2040px);">103</div><div data-line-number="104" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2060px);">104</div><div data-line-number="105" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2080px);">105</div><div data-line-number="106" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2100px);">106</div><div data-line-number="107" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2120px);">107<span class="Box-sc-g0xbh4-0 hXUKEK"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 cXzIIR"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="108" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2140px);">108</div><div data-line-number="109" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2160px);">109</div><div data-line-number="110" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2180px);">110</div><div data-line-number="111" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2200px);">111</div><div data-line-number="112" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2220px);">112</div><div data-line-number="113" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2240px);">113</div><div data-line-number="114" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2260px);">114</div><div data-line-number="115" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2280px);">115</div><div data-line-number="116" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2300px);">116</div><div data-line-number="117" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2320px);">117</div><div data-line-number="118" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2340px);">118</div><div data-line-number="119" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2360px);">119</div><div data-line-number="120" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2380px);">120</div><div data-line-number="121" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2400px);">121</div><div data-line-number="122" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2420px);">122</div><div data-line-number="123" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2440px);">123</div><div data-line-number="124" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2460px);">124</div><div data-line-number="125" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2480px);">125</div><div data-line-number="126" class="child-of-line-106  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2500px);">126</div><div data-line-number="247" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4920px);">247</div><div data-line-number="248" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4940px);">248</div><div data-line-number="249" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4960px);">249</div><div data-line-number="250" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4980px);">250</div><div data-line-number="251" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5000px);">251</div><div data-line-number="252" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5020px);">252</div><div data-line-number="253" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5040px);">253</div><div data-line-number="254" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5060px);">254</div><div data-line-number="255" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5080px);">255</div><div data-line-number="256" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5100px);">256</div><div data-line-number="257" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5120px);">257</div><div data-line-number="258" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5140px);">258</div><div data-line-number="259" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5160px);">259</div><div data-line-number="260" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5180px);">260</div><div data-line-number="261" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5200px);">261</div><div data-line-number="262" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5220px);">262</div><div data-line-number="263" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5240px);">263</div><div data-line-number="264" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5260px);">264</div><div data-line-number="265" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5280px);">265</div><div data-line-number="266" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5300px);">266</div><div data-line-number="267" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5320px);">267</div><div data-line-number="268" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5340px);">268</div><div data-line-number="269" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5360px);">269</div><div data-line-number="270" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5380px);">270</div><div data-line-number="271" class="child-of-line-221  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5400px);">271</div><div data-line-number="272" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5420px);">272</div><div data-line-number="273" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5440px);">273</div><div data-line-number="274" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5460px);">274</div><div data-line-number="275" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5480px);">275</div><div data-line-number="276" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5500px);">276</div><div data-line-number="277" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5520px);">277</div><div data-line-number="278" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5540px);">278</div><div data-line-number="279" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5560px);">279</div><div data-line-number="280" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5580px);">280</div><div data-line-number="281" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5600px);">281</div><div data-line-number="282" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5620px);">282</div><div data-line-number="283" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5640px);">283</div><div data-line-number="284" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5660px);">284</div><div data-line-number="285" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5680px);">285</div><div data-line-number="286" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5700px);">286</div><div data-line-number="287" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5720px);">287</div><div data-line-number="288" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5740px);">288</div><div data-line-number="289" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5760px);">289</div><div data-line-number="290" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5780px);">290</div><div data-line-number="291" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5800px);">291</div><div data-line-number="292" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5820px);">292</div><div data-line-number="293" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5840px);">293</div><div data-line-number="294" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5860px);">294</div><div data-line-number="295" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5880px);">295</div><div data-line-number="296" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5900px);">296</div><div data-line-number="297" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5920px);">297</div><div data-line-number="298" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5940px);">298</div><div data-line-number="299" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5960px);">299</div><div data-line-number="300" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(5980px);">300</div><div data-line-number="301" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6000px);">301</div><div data-line-number="302" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6020px);">302</div><div data-line-number="303" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6040px);">303</div><div data-line-number="304" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6060px);">304</div><div data-line-number="305" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6080px);">305</div><div data-line-number="306" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6100px);">306</div><div data-line-number="307" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6120px);">307</div><div data-line-number="308" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6140px);">308</div><div data-line-number="309" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6160px);">309</div><div data-line-number="310" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6180px);">310</div><div data-line-number="311" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6200px);">311</div><div data-line-number="312" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6220px);">312</div><div data-line-number="313" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6240px);">313</div><div data-line-number="314" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6260px);">314</div><div data-line-number="315" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6280px);">315</div><div data-line-number="316" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6300px);">316</div><div data-line-number="317" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6320px);">317</div><div data-line-number="318" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6340px);">318</div><div data-line-number="319" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6360px);">319</div><div data-line-number="320" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(6380px);">320</div></div><div class="react-code-lines" style="height: 6400px;"><div data-key="0" class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC1" class="react-file-line html-div" data-testid="code-cell" data-line-number="1" inert="inert" style="position: relative;"><span class="pl-k">import</span> <span class="pl-s1">streamlit</span> <span class="pl-k">as</span> <span class="pl-s1">st</span></div></div></div><div data-key="1" class="react-code-text react-code-line-contents virtual" style="transform: translateY(20px); min-height: auto;"><div><div id="LC2" class="react-file-line html-div" data-testid="code-cell" data-line-number="2" inert="inert" style="position: relative;"><span class="pl-k">import</span> <span class="pl-s1">pandas</span> <span class="pl-k">as</span> <span class="pl-s1">pd</span></div></div></div><div data-key="2" class="react-code-text react-code-line-contents virtual" style="transform: translateY(40px); min-height: auto;"><div><div id="LC3" class="react-file-line html-div" data-testid="code-cell" data-line-number="3" inert="inert" style="position: relative;"><span class="pl-k">from</span> <span class="pl-v">PIL</span> <span class="pl-k">import</span> <span class="pl-v">Image</span></div></div></div><div data-key="3" class="react-code-text react-code-line-contents virtual" style="transform: translateY(60px); min-height: auto;"><div><div id="LC4" class="react-file-line html-div" data-testid="code-cell" data-line-number="4" inert="inert" style="position: relative;"><span class="pl-c">#from drug_db import *</span></div></div></div><div data-key="4" class="react-code-text react-code-line-contents virtual" style="transform: translateY(80px); min-height: auto;"><div><div id="LC5" class="react-file-line html-div" data-testid="code-cell" data-line-number="5" inert="inert" style="position: relative;"><span class="pl-k">import</span> <span class="pl-s1">random</span></div></div></div><div data-key="5" class="react-code-text react-code-line-contents virtual" style="transform: translateY(100px); min-height: auto;"><div><div id="LC6" class="react-file-line html-div" data-testid="code-cell" data-line-number="6" inert="inert" style="position: relative;">
</div></div></div><div data-key="6" class="react-code-text react-code-line-contents virtual" style="transform: translateY(120px); min-height: auto;"><div><div id="LC7" class="react-file-line html-div" data-testid="code-cell" data-line-number="7" inert="inert" style="position: relative;"><span class="pl-c">## SQL DATABASE CODE</span></div></div></div><div data-key="7" class="react-code-text react-code-line-contents virtual" style="transform: translateY(140px); min-height: auto;"><div><div id="LC8" class="react-file-line html-div" data-testid="code-cell" data-line-number="8" inert="inert" style="position: relative;"><span class="pl-k">import</span> <span class="pl-s1">sqlite3</span></div></div></div><div data-key="8" class="react-code-text react-code-line-contents virtual" style="transform: translateY(160px); min-height: auto;"><div><div id="LC9" class="react-file-line html-div" data-testid="code-cell" data-line-number="9" inert="inert" style="position: relative;">
</div></div></div><div data-key="9" class="react-code-text react-code-line-contents virtual" style="transform: translateY(180px); min-height: auto;"><div><div id="LC10" class="react-file-line html-div" data-testid="code-cell" data-line-number="10" inert="inert" style="position: relative;">
</div></div></div><div data-key="10" class="react-code-text react-code-line-contents virtual" style="transform: translateY(200px); min-height: auto;"><div><div id="LC11" class="react-file-line html-div" data-testid="code-cell" data-line-number="11" inert="inert" style="position: relative;"><span class="pl-s1">conn</span> <span class="pl-c1">=</span> <span class="pl-s1">sqlite3</span>.<span class="pl-en">connect</span>(<span class="pl-s">"drug_data.db"</span>,<span class="pl-s1">check_same_thread</span><span class="pl-c1">=</span><span class="pl-c1">False</span>)</div></div></div><div data-key="11" class="react-code-text react-code-line-contents virtual" style="transform: translateY(220px); min-height: auto;"><div><div id="LC12" class="react-file-line html-div" data-testid="code-cell" data-line-number="12" inert="inert" style="position: relative;"><span class="pl-s1">c</span> <span class="pl-c1">=</span> <span class="pl-s1">conn</span>.<span class="pl-en">cursor</span>()</div></div></div><div data-key="12" class="react-code-text react-code-line-contents virtual" style="transform: translateY(240px); min-height: auto;"><div><div id="LC13" class="react-file-line html-div" data-testid="code-cell" data-line-number="13" inert="inert" style="position: relative;">
</div></div></div><div data-key="13" class="react-code-text react-code-line-contents virtual" style="transform: translateY(260px); min-height: auto;"><div><div id="LC14" class="react-file-line html-div" data-testid="code-cell" data-line-number="14" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">cust_create_table</span>():</div></div></div><div data-key="14" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(280px); min-height: auto;"><div><div id="LC15" class="react-file-line html-div" data-testid="code-cell" data-line-number="15" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'''CREATE TABLE IF NOT EXISTS Customers(</span></div></div></div><div data-key="15" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(300px); min-height: auto;"><div><div id="LC16" class="react-file-line html-div" data-testid="code-cell" data-line-number="16" inert="inert" style="position: relative;"><span class="pl-s">                    C_Name VARCHAR(50) NOT NULL,</span></div></div></div><div data-key="16" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(320px); min-height: auto;"><div><div id="LC17" class="react-file-line html-div" data-testid="code-cell" data-line-number="17" inert="inert" style="position: relative;"><span class="pl-s">                    C_Password VARCHAR(50) NOT NULL,</span></div></div></div><div data-key="17" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(340px); min-height: auto;"><div><div id="LC18" class="react-file-line html-div" data-testid="code-cell" data-line-number="18" inert="inert" style="position: relative;"><span class="pl-s">                    C_Email VARCHAR(50) PRIMARY KEY NOT NULL, </span></div></div></div><div data-key="18" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(360px); min-height: auto;"><div><div id="LC19" class="react-file-line html-div" data-testid="code-cell" data-line-number="19" inert="inert" style="position: relative;"><span class="pl-s">                    C_State VARCHAR(50) NOT NULL,</span></div></div></div><div data-key="19" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(380px); min-height: auto;"><div><div id="LC20" class="react-file-line html-div" data-testid="code-cell" data-line-number="20" inert="inert" style="position: relative;"><span class="pl-s">                    C_Number VARCHAR(50) NOT NULL </span></div></div></div><div data-key="20" class="child-of-line-13  react-code-text react-code-line-contents virtual" style="transform: translateY(400px); min-height: auto;"><div><div id="LC21" class="react-file-line html-div" data-testid="code-cell" data-line-number="21" inert="inert" style="position: relative;"><span class="pl-s">                    )'''</span>)</div></div></div><div data-key="21" class="react-code-text react-code-line-contents virtual" style="transform: translateY(420px); min-height: auto;"><div><div id="LC22" class="react-file-line html-div" data-testid="code-cell" data-line-number="22" inert="inert" style="position: relative;">    <span class="pl-en">print</span>(<span class="pl-s">'Customer Table create Successfully'</span>)</div></div></div><div data-key="22" class="react-code-text react-code-line-contents virtual" style="transform: translateY(440px); min-height: auto;"><div><div id="LC23" class="react-file-line html-div" data-testid="code-cell" data-line-number="23" inert="inert" style="position: relative;">
</div></div></div><div data-key="23" class="react-code-text react-code-line-contents virtual" style="transform: translateY(460px); min-height: auto;"><div><div id="LC24" class="react-file-line html-div" data-testid="code-cell" data-line-number="24" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">customer_add_data</span>(<span class="pl-v">Cname</span>,<span class="pl-v">Cpass</span>, <span class="pl-v">Cemail</span>, <span class="pl-v">Cstate</span>,<span class="pl-v">Cnumber</span>):</div></div></div><div data-key="24" class="react-code-text react-code-line-contents virtual" style="transform: translateY(480px); min-height: auto;"><div><div id="LC25" class="react-file-line html-div" data-testid="code-cell" data-line-number="25" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'''INSERT INTO Customers (C_Name,C_Password,C_Email, C_State, C_Number) VALUES(?,?,?,?,?)'''</span>, (<span class="pl-v">Cname</span>,<span class="pl-v">Cpass</span>,  <span class="pl-v">Cemail</span>, <span class="pl-v">Cstate</span>,<span class="pl-v">Cnumber</span>))</div></div></div><div data-key="25" class="react-code-text react-code-line-contents virtual" style="transform: translateY(500px); min-height: auto;"><div><div id="LC26" class="react-file-line html-div" data-testid="code-cell" data-line-number="26" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="26" class="react-code-text react-code-line-contents virtual" style="transform: translateY(520px); min-height: auto;"><div><div id="LC27" class="react-file-line html-div" data-testid="code-cell" data-line-number="27" inert="inert" style="position: relative;">
</div></div></div><div data-key="27" class="react-code-text react-code-line-contents virtual" style="transform: translateY(540px); min-height: auto;"><div><div id="LC28" class="react-file-line html-div" data-testid="code-cell" data-line-number="28" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">customer_view_all_data</span>():</div></div></div><div data-key="28" class="react-code-text react-code-line-contents virtual" style="transform: translateY(560px); min-height: auto;"><div><div id="LC29" class="react-file-line html-div" data-testid="code-cell" data-line-number="29" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'SELECT * FROM Customers'</span>)</div></div></div><div data-key="29" class="react-code-text react-code-line-contents virtual" style="transform: translateY(580px); min-height: auto;"><div><div id="LC30" class="react-file-line html-div" data-testid="code-cell" data-line-number="30" inert="inert" style="position: relative;">    <span class="pl-s1">customer_data</span> <span class="pl-c1">=</span> <span class="pl-s1">c</span>.<span class="pl-en">fetchall</span>()</div></div></div><div data-key="30" class="react-code-text react-code-line-contents virtual" style="transform: translateY(600px); min-height: auto;"><div><div id="LC31" class="react-file-line html-div" data-testid="code-cell" data-line-number="31" inert="inert" style="position: relative;">    <span class="pl-k">return</span> <span class="pl-s1">customer_data</span></div></div></div><div data-key="31" class="react-code-text react-code-line-contents virtual" style="transform: translateY(620px); min-height: auto;"><div><div id="LC32" class="react-file-line html-div" data-testid="code-cell" data-line-number="32" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">customer_update</span>(<span class="pl-v">Cemail</span>,<span class="pl-v">Cnumber</span>):</div></div></div><div data-key="32" class="react-code-text react-code-line-contents virtual" style="transform: translateY(640px); min-height: auto;"><div><div id="LC33" class="react-file-line html-div" data-testid="code-cell" data-line-number="33" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">''' UPDATE Customers SET C_Number = ? WHERE C_Email = ?'''</span>, (<span class="pl-v">Cnumber</span>,<span class="pl-v">Cemail</span>,))</div></div></div><div data-key="33" class="react-code-text react-code-line-contents virtual" style="transform: translateY(660px); min-height: auto;"><div><div id="LC34" class="react-file-line html-div" data-testid="code-cell" data-line-number="34" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="34" class="react-code-text react-code-line-contents virtual" style="transform: translateY(680px); min-height: auto;"><div><div id="LC35" class="react-file-line html-div" data-testid="code-cell" data-line-number="35" inert="inert" style="position: relative;">    <span class="pl-en">print</span>(<span class="pl-s">"Updating"</span>)</div></div></div><div data-key="35" class="react-code-text react-code-line-contents virtual" style="transform: translateY(700px); min-height: auto;"><div><div id="LC36" class="react-file-line html-div" data-testid="code-cell" data-line-number="36" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">customer_delete</span>(<span class="pl-v">Cemail</span>):</div></div></div><div data-key="36" class="react-code-text react-code-line-contents virtual" style="transform: translateY(720px); min-height: auto;"><div><div id="LC37" class="react-file-line html-div" data-testid="code-cell" data-line-number="37" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">''' DELETE FROM Customers WHERE C_Email = ?'''</span>, (<span class="pl-v">Cemail</span>,))</div></div></div><div data-key="37" class="react-code-text react-code-line-contents virtual" style="transform: translateY(740px); min-height: auto;"><div><div id="LC38" class="react-file-line html-div" data-testid="code-cell" data-line-number="38" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="38" class="react-code-text react-code-line-contents virtual" style="transform: translateY(760px); min-height: auto;"><div><div id="LC39" class="react-file-line html-div" data-testid="code-cell" data-line-number="39" inert="inert" style="position: relative;">
</div></div></div><div data-key="39" class="react-code-text react-code-line-contents virtual" style="transform: translateY(780px); min-height: auto;"><div><div id="LC40" class="react-file-line html-div" data-testid="code-cell" data-line-number="40" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">drug_update</span>(<span class="pl-v">Duse</span>, <span class="pl-v">Did</span>):</div></div></div><div data-key="40" class="react-code-text react-code-line-contents virtual" style="transform: translateY(800px); min-height: auto;"><div><div id="LC41" class="react-file-line html-div" data-testid="code-cell" data-line-number="41" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">''' UPDATE Drugs SET D_Use = ? WHERE D_id = ?'''</span>, (<span class="pl-v">Duse</span>,<span class="pl-v">Did</span>))</div></div></div><div data-key="41" class="react-code-text react-code-line-contents virtual" style="transform: translateY(820px); min-height: auto;"><div><div id="LC42" class="react-file-line html-div" data-testid="code-cell" data-line-number="42" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="42" class="react-code-text react-code-line-contents virtual" style="transform: translateY(840px); min-height: auto;"><div><div id="LC43" class="react-file-line html-div" data-testid="code-cell" data-line-number="43" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">drug_delete</span>(<span class="pl-v">Did</span>):</div></div></div><div data-key="43" class="react-code-text react-code-line-contents virtual" style="transform: translateY(860px); min-height: auto;"><div><div id="LC44" class="react-file-line html-div" data-testid="code-cell" data-line-number="44" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">''' DELETE FROM Drugs WHERE D_id = ?'''</span>, (<span class="pl-v">Did</span>,))</div></div></div><div data-key="44" class="react-code-text react-code-line-contents virtual" style="transform: translateY(880px); min-height: auto;"><div><div id="LC45" class="react-file-line html-div" data-testid="code-cell" data-line-number="45" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="45" class="react-code-text react-code-line-contents virtual" style="transform: translateY(900px); min-height: auto;"><div><div id="LC46" class="react-file-line html-div" data-testid="code-cell" data-line-number="46" inert="inert" style="position: relative;">
</div></div></div><div data-key="46" class="react-code-text react-code-line-contents virtual" style="transform: translateY(920px); min-height: auto;"><div><div id="LC47" class="react-file-line html-div" data-testid="code-cell" data-line-number="47" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">drug_create_table</span>():</div></div></div><div data-key="47" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(940px); min-height: auto;"><div><div id="LC48" class="react-file-line html-div" data-testid="code-cell" data-line-number="48" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'''CREATE TABLE IF NOT EXISTS Drugs(</span></div></div></div><div data-key="48" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(960px); min-height: auto;"><div><div id="LC49" class="react-file-line html-div" data-testid="code-cell" data-line-number="49" inert="inert" style="position: relative;"><span class="pl-s">                D_Name VARCHAR(50) NOT NULL,</span></div></div></div><div data-key="49" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(980px); min-height: auto;"><div><div id="LC50" class="react-file-line html-div" data-testid="code-cell" data-line-number="50" inert="inert" style="position: relative;"><span class="pl-s">                D_ExpDate DATE NOT NULL, </span></div></div></div><div data-key="50" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(1000px); min-height: auto;"><div><div id="LC51" class="react-file-line html-div" data-testid="code-cell" data-line-number="51" inert="inert" style="position: relative;"><span class="pl-s">                D_Use VARCHAR(50) NOT NULL,</span></div></div></div><div data-key="51" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(1020px); min-height: auto;"><div><div id="LC52" class="react-file-line html-div" data-testid="code-cell" data-line-number="52" inert="inert" style="position: relative;"><span class="pl-s">                D_Qty INT NOT NULL, </span></div></div></div><div data-key="52" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(1040px); min-height: auto;"><div><div id="LC53" class="react-file-line html-div" data-testid="code-cell" data-line-number="53" inert="inert" style="position: relative;"><span class="pl-s">                D_id INT PRIMARY KEY NOT NULL)</span></div></div></div><div data-key="53" class="child-of-line-46  react-code-text react-code-line-contents virtual" style="transform: translateY(1060px); min-height: auto;"><div><div id="LC54" class="react-file-line html-div" data-testid="code-cell" data-line-number="54" inert="inert" style="position: relative;"><span class="pl-s">                '''</span>)</div></div></div><div data-key="54" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1080px); min-height: auto;"><div><div id="LC55" class="react-file-line html-div" data-testid="code-cell" data-line-number="55" inert="inert" style="position: relative;">    <span class="pl-en">print</span>(<span class="pl-s">'DRUG Table create Successfully'</span>)</div></div></div><div data-key="55" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1100px); min-height: auto;"><div><div id="LC56" class="react-file-line html-div" data-testid="code-cell" data-line-number="56" inert="inert" style="position: relative;">
</div></div></div><div data-key="56" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1120px); min-height: auto;"><div><div id="LC57" class="react-file-line html-div" data-testid="code-cell" data-line-number="57" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">drug_add_data</span>(<span class="pl-v">Dname</span>, <span class="pl-v">Dexpdate</span>, <span class="pl-v">Duse</span>, <span class="pl-v">Dqty</span>, <span class="pl-v">Did</span>):</div></div></div><div data-key="57" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1140px); min-height: auto;"><div><div id="LC58" class="react-file-line html-div" data-testid="code-cell" data-line-number="58" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'''INSERT INTO Drugs (D_Name, D_Expdate, D_Use, D_Qty, D_id) VALUES(?,?,?,?,?)'''</span>, (<span class="pl-v">Dname</span>, <span class="pl-v">Dexpdate</span>, <span class="pl-v">Duse</span>, <span class="pl-v">Dqty</span>, <span class="pl-v">Did</span>))</div></div></div><div data-key="58" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1160px); min-height: auto;"><div><div id="LC59" class="react-file-line html-div" data-testid="code-cell" data-line-number="59" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="59" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1180px); min-height: auto;"><div><div id="LC60" class="react-file-line html-div" data-testid="code-cell" data-line-number="60" inert="inert" style="position: relative;">
</div></div></div><div data-key="60" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1200px); min-height: auto;"><div><div id="LC61" class="react-file-line html-div" data-testid="code-cell" data-line-number="61" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">drug_view_all_data</span>():</div></div></div><div data-key="61" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1220px); min-height: auto;"><div><div id="LC62" class="react-file-line html-div" data-testid="code-cell" data-line-number="62" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'SELECT * FROM Drugs'</span>)</div></div></div><div data-key="62" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1240px); min-height: auto;"><div><div id="LC63" class="react-file-line html-div" data-testid="code-cell" data-line-number="63" inert="inert" style="position: relative;">    <span class="pl-s1">drug_data</span> <span class="pl-c1">=</span> <span class="pl-s1">c</span>.<span class="pl-en">fetchall</span>()</div></div></div><div data-key="63" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1260px); min-height: auto;"><div><div id="LC64" class="react-file-line html-div" data-testid="code-cell" data-line-number="64" inert="inert" style="position: relative;">    <span class="pl-k">return</span> <span class="pl-s1">drug_data</span></div></div></div><div data-key="64" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1280px); min-height: auto;"><div><div id="LC65" class="react-file-line html-div" data-testid="code-cell" data-line-number="65" inert="inert" style="position: relative;">
</div></div></div><div data-key="65" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1300px); min-height: auto;"><div><div id="LC66" class="react-file-line html-div" data-testid="code-cell" data-line-number="66" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">order_create_table</span>():</div></div></div><div data-key="66" class="child-of-line-65  react-code-text react-code-line-contents virtual" style="transform: translateY(1320px); min-height: auto;"><div><div id="LC67" class="react-file-line html-div" data-testid="code-cell" data-line-number="67" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'''</span></div></div></div><div data-key="67" class="child-of-line-65  react-code-text react-code-line-contents virtual" style="transform: translateY(1340px); min-height: auto;"><div><div id="LC68" class="react-file-line html-div" data-testid="code-cell" data-line-number="68" inert="inert" style="position: relative;"><span class="pl-s">        CREATE TABLE IF NOT EXISTS Orders(</span></div></div></div><div data-key="68" class="child-of-line-65  react-code-text react-code-line-contents virtual" style="transform: translateY(1360px); min-height: auto;"><div><div id="LC69" class="react-file-line html-div" data-testid="code-cell" data-line-number="69" inert="inert" style="position: relative;"><span class="pl-s">                O_Name VARCHAR(100) NOT NULL,</span></div></div></div><div data-key="69" class="child-of-line-65  react-code-text react-code-line-contents virtual" style="transform: translateY(1380px); min-height: auto;"><div><div id="LC70" class="react-file-line html-div" data-testid="code-cell" data-line-number="70" inert="inert" style="position: relative;"><span class="pl-s">                O_Items VARCHAR(100) NOT NULL,</span></div></div></div><div data-key="70" class="child-of-line-65  react-code-text react-code-line-contents virtual" style="transform: translateY(1400px); min-height: auto;"><div><div id="LC71" class="react-file-line html-div" data-testid="code-cell" data-line-number="71" inert="inert" style="position: relative;"><span class="pl-s">                O_Qty VARCHAR(100) NOT NULL,</span></div></div></div><div data-key="71" class="child-of-line-65  react-code-text react-code-line-contents virtual" style="transform: translateY(1420px); min-height: auto;"><div><div id="LC72" class="react-file-line html-div" data-testid="code-cell" data-line-number="72" inert="inert" style="position: relative;"><span class="pl-s">                O_id VARCHAR(100) PRIMARY KEY NOT NULL)</span></div></div></div><div data-key="72" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1440px); min-height: auto;"><div><div id="LC73" class="react-file-line html-div" data-testid="code-cell" data-line-number="73" inert="inert" style="position: relative;"><span class="pl-s">    '''</span>)</div></div></div><div data-key="73" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1460px); min-height: auto;"><div><div id="LC74" class="react-file-line html-div" data-testid="code-cell" data-line-number="74" inert="inert" style="position: relative;">
</div></div></div><div data-key="74" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1480px); min-height: auto;"><div><div id="LC75" class="react-file-line html-div" data-testid="code-cell" data-line-number="75" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">order_delete</span>(<span class="pl-v">Oid</span>):</div></div></div><div data-key="75" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1500px); min-height: auto;"><div><div id="LC76" class="react-file-line html-div" data-testid="code-cell" data-line-number="76" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">''' DELETE FROM Orders WHERE O_id = ?'''</span>, (<span class="pl-v">Oid</span>,))</div></div></div><div data-key="76" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1520px); min-height: auto;"><div><div id="LC77" class="react-file-line html-div" data-testid="code-cell" data-line-number="77" inert="inert" style="position: relative;">
</div></div></div><div data-key="77" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1540px); min-height: auto;"><div><div id="LC78" class="react-file-line html-div" data-testid="code-cell" data-line-number="78" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">order_add_data</span>(<span class="pl-v">O_Name</span>,<span class="pl-v">O_Items</span>,<span class="pl-v">O_Qty</span>,<span class="pl-v">O_id</span>):</div></div></div><div data-key="78" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1560px); min-height: auto;"><div><div id="LC79" class="react-file-line html-div" data-testid="code-cell" data-line-number="79" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'''INSERT INTO Orders (O_Name, O_Items,O_Qty, O_id) VALUES(?,?,?,?)'''</span>,</div></div></div><div data-key="79" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1580px); min-height: auto;"><div><div id="LC80" class="react-file-line html-div" data-testid="code-cell" data-line-number="80" inert="inert" style="position: relative;">              (<span class="pl-v">O_Name</span>,<span class="pl-v">O_Items</span>,<span class="pl-v">O_Qty</span>,<span class="pl-v">O_id</span>))</div></div></div><div data-key="80" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1600px); min-height: auto;"><div><div id="LC81" class="react-file-line html-div" data-testid="code-cell" data-line-number="81" inert="inert" style="position: relative;">    <span class="pl-s1">conn</span>.<span class="pl-en">commit</span>()</div></div></div><div data-key="81" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1620px); min-height: auto;"><div><div id="LC82" class="react-file-line html-div" data-testid="code-cell" data-line-number="82" inert="inert" style="position: relative;">
</div></div></div><div data-key="82" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1640px); min-height: auto;"><div><div id="LC83" class="react-file-line html-div" data-testid="code-cell" data-line-number="83" inert="inert" style="position: relative;">
</div></div></div><div data-key="83" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1660px); min-height: auto;"><div><div id="LC84" class="react-file-line html-div" data-testid="code-cell" data-line-number="84" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">order_view_data</span>(<span class="pl-s1">customername</span>):</div></div></div><div data-key="84" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1680px); min-height: auto;"><div><div id="LC85" class="react-file-line html-div" data-testid="code-cell" data-line-number="85" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'SELECT * FROM ORDERS Where O_Name == ?'</span>,(<span class="pl-s1">customername</span>,))</div></div></div><div data-key="85" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1700px); min-height: auto;"><div><div id="LC86" class="react-file-line html-div" data-testid="code-cell" data-line-number="86" inert="inert" style="position: relative;">    <span class="pl-s1">order_data</span> <span class="pl-c1">=</span> <span class="pl-s1">c</span>.<span class="pl-en">fetchall</span>()</div></div></div><div data-key="86" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1720px); min-height: auto;"><div><div id="LC87" class="react-file-line html-div" data-testid="code-cell" data-line-number="87" inert="inert" style="position: relative;">    <span class="pl-k">return</span> <span class="pl-s1">order_data</span></div></div></div><div data-key="87" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1740px); min-height: auto;"><div><div id="LC88" class="react-file-line html-div" data-testid="code-cell" data-line-number="88" inert="inert" style="position: relative;">
</div></div></div><div data-key="88" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1760px); min-height: auto;"><div><div id="LC89" class="react-file-line html-div" data-testid="code-cell" data-line-number="89" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">order_view_all_data</span>():</div></div></div><div data-key="89" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1780px); min-height: auto;"><div><div id="LC90" class="react-file-line html-div" data-testid="code-cell" data-line-number="90" inert="inert" style="position: relative;">    <span class="pl-s1">c</span>.<span class="pl-en">execute</span>(<span class="pl-s">'SELECT * FROM ORDERS'</span>)</div></div></div><div data-key="90" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1800px); min-height: auto;"><div><div id="LC91" class="react-file-line html-div" data-testid="code-cell" data-line-number="91" inert="inert" style="position: relative;">    <span class="pl-s1">order_all_data</span> <span class="pl-c1">=</span> <span class="pl-s1">c</span>.<span class="pl-en">fetchall</span>()</div></div></div><div data-key="91" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1820px); min-height: auto;"><div><div id="LC92" class="react-file-line html-div" data-testid="code-cell" data-line-number="92" inert="inert" style="position: relative;">    <span class="pl-k">return</span> <span class="pl-s1">order_all_data</span></div></div></div><div data-key="92" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1840px); min-height: auto;"><div><div id="LC93" class="react-file-line html-div" data-testid="code-cell" data-line-number="93" inert="inert" style="position: relative;">
</div></div></div><div data-key="93" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1860px); min-height: auto;"><div><div id="LC94" class="react-file-line html-div" data-testid="code-cell" data-line-number="94" inert="inert" style="position: relative;">
</div></div></div><div data-key="94" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1880px); min-height: auto;"><div><div id="LC95" class="react-file-line html-div" data-testid="code-cell" data-line-number="95" inert="inert" style="position: relative;">
</div></div></div><div data-key="95" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1900px); min-height: auto;"><div><div id="LC96" class="react-file-line html-div" data-testid="code-cell" data-line-number="96" inert="inert" style="position: relative;">
</div></div></div><div data-key="96" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1920px); min-height: auto;"><div><div id="LC97" class="react-file-line html-div" data-testid="code-cell" data-line-number="97" inert="inert" style="position: relative;">
</div></div></div><div data-key="97" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1940px); min-height: auto;"><div><div id="LC98" class="react-file-line html-div" data-testid="code-cell" data-line-number="98" inert="inert" style="position: relative;">
</div></div></div><div data-key="98" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1960px); min-height: auto;"><div><div id="LC99" class="react-file-line html-div" data-testid="code-cell" data-line-number="99" inert="inert" style="position: relative;"><span class="pl-c">#__________________________________________________________________________________</span></div></div></div><div data-key="99" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1980px); min-height: auto;"><div><div id="LC100" class="react-file-line html-div" data-testid="code-cell" data-line-number="100" inert="inert" style="position: relative;">
</div></div></div><div data-key="100" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2000px); min-height: auto;"><div><div id="LC101" class="react-file-line html-div" data-testid="code-cell" data-line-number="101" inert="inert" style="position: relative;">
</div></div></div><div data-key="101" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2020px); min-height: auto;"><div><div id="LC102" class="react-file-line html-div" data-testid="code-cell" data-line-number="102" inert="inert" style="position: relative;">
</div></div></div><div data-key="102" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2040px); min-height: auto;"><div><div id="LC103" class="react-file-line html-div" data-testid="code-cell" data-line-number="103" inert="inert" style="position: relative;">
</div></div></div><div data-key="103" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2060px); min-height: auto;"><div><div id="LC104" class="react-file-line html-div" data-testid="code-cell" data-line-number="104" inert="inert" style="position: relative;">
</div></div></div><div data-key="104" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2080px); min-height: auto;"><div><div id="LC105" class="react-file-line html-div" data-testid="code-cell" data-line-number="105" inert="inert" style="position: relative;">
</div></div></div><div data-key="105" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2100px); min-height: auto;"><div><div id="LC106" class="react-file-line html-div" data-testid="code-cell" data-line-number="106" inert="inert" style="position: relative;">
</div></div></div><div data-key="106" class="react-code-text react-code-line-contents virtual" style="transform: translateY(2120px); min-height: auto;"><div><div id="LC107" class="react-file-line html-div" data-testid="code-cell" data-line-number="107" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">admin</span>():</div></div></div><div data-key="107" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2140px); min-height: auto;"><div><div id="LC108" class="react-file-line html-div" data-testid="code-cell" data-line-number="108" inert="inert" style="position: relative;">
</div></div></div><div data-key="108" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2160px); min-height: auto;"><div><div id="LC109" class="react-file-line html-div" data-testid="code-cell" data-line-number="109" inert="inert" style="position: relative;">
</div></div></div><div data-key="109" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2180px); min-height: auto;"><div><div id="LC110" class="react-file-line html-div" data-testid="code-cell" data-line-number="110" inert="inert" style="position: relative;">    <span class="pl-s1">st</span>.<span class="pl-en">title</span>(<span class="pl-s">"Pharmacy Database Dashboard"</span>)</div></div></div><div data-key="110" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2200px); min-height: auto;"><div><div id="LC111" class="react-file-line html-div" data-testid="code-cell" data-line-number="111" inert="inert" style="position: relative;">    <span class="pl-s1">menu</span> <span class="pl-c1">=</span> [<span class="pl-s">"Drugs"</span>, <span class="pl-s">"Customers"</span>, <span class="pl-s">"Orders"</span>, <span class="pl-s">"About"</span>]</div></div></div><div data-key="111" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2220px); min-height: auto;"><div><div id="LC112" class="react-file-line html-div" data-testid="code-cell" data-line-number="112" inert="inert" style="position: relative;">    <span class="pl-s1">choice</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">selectbox</span>(<span class="pl-s">"Menu"</span>, <span class="pl-s1">menu</span>)</div></div></div><div data-key="112" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2240px); min-height: auto;"><div><div id="LC113" class="react-file-line html-div" data-testid="code-cell" data-line-number="113" inert="inert" style="position: relative;">
</div></div></div><div data-key="113" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2260px); min-height: auto;"><div><div id="LC114" class="react-file-line html-div" data-testid="code-cell" data-line-number="114" inert="inert" style="position: relative;">
</div></div></div><div data-key="114" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2280px); min-height: auto;"><div><div id="LC115" class="react-file-line html-div" data-testid="code-cell" data-line-number="115" inert="inert" style="position: relative;">
</div></div></div><div data-key="115" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2300px); min-height: auto;"><div><div id="LC116" class="react-file-line html-div" data-testid="code-cell" data-line-number="116" inert="inert" style="position: relative;">    <span class="pl-c">## DRUGS</span></div></div></div><div data-key="116" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2320px); min-height: auto;"><div><div id="LC117" class="react-file-line html-div" data-testid="code-cell" data-line-number="117" inert="inert" style="position: relative;">    <span class="pl-k">if</span> <span class="pl-s1">choice</span> <span class="pl-c1">==</span> <span class="pl-s">"Drugs"</span>:</div></div></div><div data-key="117" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2340px); min-height: auto;"><div><div id="LC118" class="react-file-line html-div" data-testid="code-cell" data-line-number="118" inert="inert" style="position: relative;">
</div></div></div><div data-key="118" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2360px); min-height: auto;"><div><div id="LC119" class="react-file-line html-div" data-testid="code-cell" data-line-number="119" inert="inert" style="position: relative;">        <span class="pl-s1">menu</span> <span class="pl-c1">=</span> [<span class="pl-s">"Add"</span>, <span class="pl-s">"View"</span>, <span class="pl-s">"Update"</span>, <span class="pl-s">"Delete"</span>]</div></div></div><div data-key="119" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2380px); min-height: auto;"><div><div id="LC120" class="react-file-line html-div" data-testid="code-cell" data-line-number="120" inert="inert" style="position: relative;">        <span class="pl-s1">choice</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">selectbox</span>(<span class="pl-s">"Menu"</span>, <span class="pl-s1">menu</span>)</div></div></div><div data-key="120" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2400px); min-height: auto;"><div><div id="LC121" class="react-file-line html-div" data-testid="code-cell" data-line-number="121" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-s1">choice</span> <span class="pl-c1">==</span> <span class="pl-s">"Add"</span>:</div></div></div><div data-key="121" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2420px); min-height: auto;"><div><div id="LC122" class="react-file-line html-div" data-testid="code-cell" data-line-number="122" inert="inert" style="position: relative;">
</div></div></div><div data-key="122" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2440px); min-height: auto;"><div><div id="LC123" class="react-file-line html-div" data-testid="code-cell" data-line-number="123" inert="inert" style="position: relative;">            <span class="pl-s1">st</span>.<span class="pl-en">subheader</span>(<span class="pl-s">"Add Drugs"</span>)</div></div></div><div data-key="123" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2460px); min-height: auto;"><div><div id="LC124" class="react-file-line html-div" data-testid="code-cell" data-line-number="124" inert="inert" style="position: relative;">
</div></div></div><div data-key="124" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2480px); min-height: auto;"><div><div id="LC125" class="react-file-line html-div" data-testid="code-cell" data-line-number="125" inert="inert" style="position: relative;">            <span class="pl-s1">col1</span>, <span class="pl-s1">col2</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">columns</span>(<span class="pl-c1">2</span>)</div></div></div><div data-key="125" class="child-of-line-106  react-code-text react-code-line-contents virtual" style="transform: translateY(2500px); min-height: auto;"><div><div id="LC126" class="react-file-line html-div" data-testid="code-cell" data-line-number="126" inert="inert" style="position: relative;">
</div></div></div><div data-key="246" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(4920px); min-height: auto;"><div><div id="LC247" class="react-file-line html-div" data-testid="code-cell" data-line-number="247" inert="inert" style="position: relative;">        <span class="pl-s1">st</span>.<span class="pl-en">image</span>(<span class="pl-s1">img</span>, <span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">100</span> , <span class="pl-s1">caption</span><span class="pl-c1">=</span><span class="pl-s">"Rs. 10/-"</span>)</div></div></div><div data-key="247" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(4940px); min-height: auto;"><div><div id="LC248" class="react-file-line html-div" data-testid="code-cell" data-line-number="248" inert="inert" style="position: relative;">        <span class="pl-s1">strepsils</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">slider</span>(<span class="pl-s1">label</span><span class="pl-c1">=</span><span class="pl-s">"Quantity"</span>,<span class="pl-s1">min_value</span><span class="pl-c1">=</span><span class="pl-c1">0</span>, <span class="pl-s1">max_value</span><span class="pl-c1">=</span><span class="pl-c1">5</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span> <span class="pl-c1">2</span>)</div></div></div><div data-key="248" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(4960px); min-height: auto;"><div><div id="LC249" class="react-file-line html-div" data-testid="code-cell" data-line-number="249" inert="inert" style="position: relative;">        <span class="pl-s1">st</span>.<span class="pl-en">info</span>(<span class="pl-s">"When to USE: "</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">drug_result</span>[<span class="pl-c1">1</span>][<span class="pl-c1">2</span>]))</div></div></div><div data-key="249" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(4980px); min-height: auto;"><div><div id="LC250" class="react-file-line html-div" data-testid="code-cell" data-line-number="250" inert="inert" style="position: relative;">
</div></div></div><div data-key="250" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5000px); min-height: auto;"><div><div id="LC251" class="react-file-line html-div" data-testid="code-cell" data-line-number="251" inert="inert" style="position: relative;">        <span class="pl-s1">st</span>.<span class="pl-en">subheader</span>(<span class="pl-s">"Drug: "</span> <span class="pl-c1">+</span> <span class="pl-s1">drug_result</span>[<span class="pl-c1">2</span>][<span class="pl-c1">0</span>])</div></div></div><div data-key="251" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5020px); min-height: auto;"><div><div id="LC252" class="react-file-line html-div" data-testid="code-cell" data-line-number="252" inert="inert" style="position: relative;">        <span class="pl-s1">img</span> <span class="pl-c1">=</span> <span class="pl-v">Image</span>.<span class="pl-en">open</span>(<span class="pl-s">'images/vicks.JPG'</span>)</div></div></div><div data-key="252" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5040px); min-height: auto;"><div><div id="LC253" class="react-file-line html-div" data-testid="code-cell" data-line-number="253" inert="inert" style="position: relative;">        <span class="pl-s1">st</span>.<span class="pl-en">image</span>(<span class="pl-s1">img</span>, <span class="pl-s1">width</span><span class="pl-c1">=</span><span class="pl-c1">100</span>, <span class="pl-s1">caption</span><span class="pl-c1">=</span><span class="pl-s">"Rs. 65/-"</span>)</div></div></div><div data-key="253" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5060px); min-height: auto;"><div><div id="LC254" class="react-file-line html-div" data-testid="code-cell" data-line-number="254" inert="inert" style="position: relative;">        <span class="pl-s1">vicks</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">slider</span>(<span class="pl-s1">label</span><span class="pl-c1">=</span><span class="pl-s">"Quantity"</span>,<span class="pl-s1">min_value</span><span class="pl-c1">=</span><span class="pl-c1">0</span>, <span class="pl-s1">max_value</span><span class="pl-c1">=</span><span class="pl-c1">5</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-c1">3</span>)</div></div></div><div data-key="254" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5080px); min-height: auto;"><div><div id="LC255" class="react-file-line html-div" data-testid="code-cell" data-line-number="255" inert="inert" style="position: relative;">        <span class="pl-s1">st</span>.<span class="pl-en">info</span>(<span class="pl-s">"When to USE: "</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">drug_result</span>[<span class="pl-c1">2</span>][<span class="pl-c1">2</span>]))</div></div></div><div data-key="255" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5100px); min-height: auto;"><div><div id="LC256" class="react-file-line html-div" data-testid="code-cell" data-line-number="256" inert="inert" style="position: relative;">
</div></div></div><div data-key="256" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5120px); min-height: auto;"><div><div id="LC257" class="react-file-line html-div" data-testid="code-cell" data-line-number="257" inert="inert" style="position: relative;">
</div></div></div><div data-key="257" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5140px); min-height: auto;"><div><div id="LC258" class="react-file-line html-div" data-testid="code-cell" data-line-number="258" inert="inert" style="position: relative;">
</div></div></div><div data-key="258" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5160px); min-height: auto;"><div><div id="LC259" class="react-file-line html-div" data-testid="code-cell" data-line-number="259" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-s1">st</span>.<span class="pl-en">button</span>(<span class="pl-s1">label</span><span class="pl-c1">=</span><span class="pl-s">"Buy now"</span>):</div></div></div><div data-key="259" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5180px); min-height: auto;"><div><div id="LC260" class="react-file-line html-div" data-testid="code-cell" data-line-number="260" inert="inert" style="position: relative;">            <span class="pl-v">O_items</span> <span class="pl-c1">=</span> <span class="pl-s">""</span></div></div></div><div data-key="260" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5200px); min-height: auto;"><div><div id="LC261" class="react-file-line html-div" data-testid="code-cell" data-line-number="261" inert="inert" style="position: relative;">
</div></div></div><div data-key="261" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5220px); min-height: auto;"><div><div id="LC262" class="react-file-line html-div" data-testid="code-cell" data-line-number="262" inert="inert" style="position: relative;">            <span class="pl-k">if</span> <span class="pl-en">int</span>(<span class="pl-s1">dolo650</span>) <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span>:</div></div></div><div data-key="262" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5240px); min-height: auto;"><div><div id="LC263" class="react-file-line html-div" data-testid="code-cell" data-line-number="263" inert="inert" style="position: relative;">                <span class="pl-v">O_items</span> <span class="pl-c1">+=</span> <span class="pl-s">"Dolo-650,"</span></div></div></div><div data-key="263" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5260px); min-height: auto;"><div><div id="LC264" class="react-file-line html-div" data-testid="code-cell" data-line-number="264" inert="inert" style="position: relative;">            <span class="pl-k">if</span> <span class="pl-en">int</span>(<span class="pl-s1">strepsils</span>) <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span>:</div></div></div><div data-key="264" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5280px); min-height: auto;"><div><div id="LC265" class="react-file-line html-div" data-testid="code-cell" data-line-number="265" inert="inert" style="position: relative;">                <span class="pl-v">O_items</span> <span class="pl-c1">+=</span> <span class="pl-s">"Strepsils,"</span></div></div></div><div data-key="265" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5300px); min-height: auto;"><div><div id="LC266" class="react-file-line html-div" data-testid="code-cell" data-line-number="266" inert="inert" style="position: relative;">            <span class="pl-k">if</span> <span class="pl-en">int</span>(<span class="pl-s1">vicks</span>) <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span>:</div></div></div><div data-key="266" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5320px); min-height: auto;"><div><div id="LC267" class="react-file-line html-div" data-testid="code-cell" data-line-number="267" inert="inert" style="position: relative;">                <span class="pl-v">O_items</span> <span class="pl-c1">+=</span> <span class="pl-s">"Vicks"</span></div></div></div><div data-key="267" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5340px); min-height: auto;"><div><div id="LC268" class="react-file-line html-div" data-testid="code-cell" data-line-number="268" inert="inert" style="position: relative;">            <span class="pl-v">O_Qty</span> <span class="pl-c1">=</span> <span class="pl-en">str</span>(<span class="pl-s1">dolo650</span>)<span class="pl-c1">+</span><span class="pl-en">str</span>(<span class="pl-s">','</span>) <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">strepsils</span>) <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s">","</span>) <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">vicks</span>)</div></div></div><div data-key="268" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5360px); min-height: auto;"><div><div id="LC269" class="react-file-line html-div" data-testid="code-cell" data-line-number="269" inert="inert" style="position: relative;">
</div></div></div><div data-key="269" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5380px); min-height: auto;"><div><div id="LC270" class="react-file-line html-div" data-testid="code-cell" data-line-number="270" inert="inert" style="position: relative;">            <span class="pl-v">O_id</span> <span class="pl-c1">=</span> <span class="pl-s1">username</span> <span class="pl-c1">+</span> <span class="pl-s">"#O"</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">0</span>,<span class="pl-c1">1000000</span>))</div></div></div><div data-key="270" class="child-of-line-221  react-code-text react-code-line-contents virtual" style="transform: translateY(5400px); min-height: auto;"><div><div id="LC271" class="react-file-line html-div" data-testid="code-cell" data-line-number="271" inert="inert" style="position: relative;">            <span class="pl-c">#order_add_data(O_Name, O_Items,O_Qty, O_id):</span></div></div></div><div data-key="271" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5420px); min-height: auto;"><div><div id="LC272" class="react-file-line html-div" data-testid="code-cell" data-line-number="272" inert="inert" style="position: relative;">            <span class="pl-en">order_add_data</span>(<span class="pl-s1">username</span>, <span class="pl-v">O_items</span>, <span class="pl-v">O_Qty</span>, <span class="pl-v">O_id</span>)</div></div></div><div data-key="272" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5440px); min-height: auto;"><div><div id="LC273" class="react-file-line html-div" data-testid="code-cell" data-line-number="273" inert="inert" style="position: relative;">
</div></div></div><div data-key="273" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5460px); min-height: auto;"><div><div id="LC274" class="react-file-line html-div" data-testid="code-cell" data-line-number="274" inert="inert" style="position: relative;">
</div></div></div><div data-key="274" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5480px); min-height: auto;"><div><div id="LC275" class="react-file-line html-div" data-testid="code-cell" data-line-number="275" inert="inert" style="position: relative;">
</div></div></div><div data-key="275" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5500px); min-height: auto;"><div><div id="LC276" class="react-file-line html-div" data-testid="code-cell" data-line-number="276" inert="inert" style="position: relative;">
</div></div></div><div data-key="276" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5520px); min-height: auto;"><div><div id="LC277" class="react-file-line html-div" data-testid="code-cell" data-line-number="277" inert="inert" style="position: relative;">
</div></div></div><div data-key="277" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5540px); min-height: auto;"><div><div id="LC278" class="react-file-line html-div" data-testid="code-cell" data-line-number="278" inert="inert" style="position: relative;">
</div></div></div><div data-key="278" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5560px); min-height: auto;"><div><div id="LC279" class="react-file-line html-div" data-testid="code-cell" data-line-number="279" inert="inert" style="position: relative;">
</div></div></div><div data-key="279" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5580px); min-height: auto;"><div><div id="LC280" class="react-file-line html-div" data-testid="code-cell" data-line-number="280" inert="inert" style="position: relative;">
</div></div></div><div data-key="280" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5600px); min-height: auto;"><div><div id="LC281" class="react-file-line html-div" data-testid="code-cell" data-line-number="281" inert="inert" style="position: relative;"><span class="pl-k">if</span> <span class="pl-s1">__name__</span> <span class="pl-c1">==</span> <span class="pl-s">'__main__'</span>:</div></div></div><div data-key="281" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5620px); min-height: auto;"><div><div id="LC282" class="react-file-line html-div" data-testid="code-cell" data-line-number="282" inert="inert" style="position: relative;">    <span class="pl-en">drug_create_table</span>()</div></div></div><div data-key="282" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5640px); min-height: auto;"><div><div id="LC283" class="react-file-line html-div" data-testid="code-cell" data-line-number="283" inert="inert" style="position: relative;">    <span class="pl-en">cust_create_table</span>()</div></div></div><div data-key="283" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5660px); min-height: auto;"><div><div id="LC284" class="react-file-line html-div" data-testid="code-cell" data-line-number="284" inert="inert" style="position: relative;">    <span class="pl-en">order_create_table</span>()</div></div></div><div data-key="284" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5680px); min-height: auto;"><div><div id="LC285" class="react-file-line html-div" data-testid="code-cell" data-line-number="285" inert="inert" style="position: relative;">
</div></div></div><div data-key="285" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5700px); min-height: auto;"><div><div id="LC286" class="react-file-line html-div" data-testid="code-cell" data-line-number="286" inert="inert" style="position: relative;">    <span class="pl-s1">menu</span> <span class="pl-c1">=</span> [<span class="pl-s">"Login"</span>, <span class="pl-s">"SignUp"</span>,<span class="pl-s">"Admin"</span>]</div></div></div><div data-key="286" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5720px); min-height: auto;"><div><div id="LC287" class="react-file-line html-div" data-testid="code-cell" data-line-number="287" inert="inert" style="position: relative;">    <span class="pl-s1">choice</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">selectbox</span>(<span class="pl-s">"Menu"</span>, <span class="pl-s1">menu</span>)</div></div></div><div data-key="287" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5740px); min-height: auto;"><div><div id="LC288" class="react-file-line html-div" data-testid="code-cell" data-line-number="288" inert="inert" style="position: relative;">    <span class="pl-k">if</span> <span class="pl-s1">choice</span> <span class="pl-c1">==</span> <span class="pl-s">"Login"</span>:</div></div></div><div data-key="288" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5760px); min-height: auto;"><div><div id="LC289" class="react-file-line html-div" data-testid="code-cell" data-line-number="289" inert="inert" style="position: relative;">        <span class="pl-s1">username</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"User Name"</span>)</div></div></div><div data-key="289" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5780px); min-height: auto;"><div><div id="LC290" class="react-file-line html-div" data-testid="code-cell" data-line-number="290" inert="inert" style="position: relative;">        <span class="pl-s1">password</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"Password"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s">'password'</span>)</div></div></div><div data-key="290" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5800px); min-height: auto;"><div><div id="LC291" class="react-file-line html-div" data-testid="code-cell" data-line-number="291" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">checkbox</span>(<span class="pl-s1">label</span><span class="pl-c1">=</span><span class="pl-s">"Login"</span>):</div></div></div><div data-key="291" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5820px); min-height: auto;"><div><div id="LC292" class="react-file-line html-div" data-testid="code-cell" data-line-number="292" inert="inert" style="position: relative;">            <span class="pl-en">customer</span>(<span class="pl-s1">username</span>, <span class="pl-s1">password</span>)</div></div></div><div data-key="292" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5840px); min-height: auto;"><div><div id="LC293" class="react-file-line html-div" data-testid="code-cell" data-line-number="293" inert="inert" style="position: relative;">
</div></div></div><div data-key="293" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5860px); min-height: auto;"><div><div id="LC294" class="react-file-line html-div" data-testid="code-cell" data-line-number="294" inert="inert" style="position: relative;">    <span class="pl-k">elif</span> <span class="pl-s1">choice</span> <span class="pl-c1">==</span> <span class="pl-s">"SignUp"</span>:</div></div></div><div data-key="294" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5880px); min-height: auto;"><div><div id="LC295" class="react-file-line html-div" data-testid="code-cell" data-line-number="295" inert="inert" style="position: relative;">        <span class="pl-s1">st</span>.<span class="pl-en">subheader</span>(<span class="pl-s">"Create New Account"</span>)</div></div></div><div data-key="295" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5900px); min-height: auto;"><div><div id="LC296" class="react-file-line html-div" data-testid="code-cell" data-line-number="296" inert="inert" style="position: relative;">        <span class="pl-s1">cust_name</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"Name"</span>)</div></div></div><div data-key="296" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5920px); min-height: auto;"><div><div id="LC297" class="react-file-line html-div" data-testid="code-cell" data-line-number="297" inert="inert" style="position: relative;">        <span class="pl-s1">cust_password</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"Password"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s">'password'</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-c1">1000</span>)</div></div></div><div data-key="297" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5940px); min-height: auto;"><div><div id="LC298" class="react-file-line html-div" data-testid="code-cell" data-line-number="298" inert="inert" style="position: relative;">        <span class="pl-s1">cust_password1</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"Confirm Password"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s">'password'</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-c1">1001</span>)</div></div></div><div data-key="298" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5960px); min-height: auto;"><div><div id="LC299" class="react-file-line html-div" data-testid="code-cell" data-line-number="299" inert="inert" style="position: relative;">        <span class="pl-s1">col1</span>, <span class="pl-s1">col2</span>, <span class="pl-s1">col3</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">columns</span>(<span class="pl-c1">3</span>)</div></div></div><div data-key="299" class="react-code-text react-code-line-contents virtual" style="transform: translateY(5980px); min-height: auto;"><div><div id="LC300" class="react-file-line html-div" data-testid="code-cell" data-line-number="300" inert="inert" style="position: relative;">
</div></div></div><div data-key="300" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6000px); min-height: auto;"><div><div id="LC301" class="react-file-line html-div" data-testid="code-cell" data-line-number="301" inert="inert" style="position: relative;">        <span class="pl-k">with</span> <span class="pl-s1">col1</span>:</div></div></div><div data-key="301" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6020px); min-height: auto;"><div><div id="LC302" class="react-file-line html-div" data-testid="code-cell" data-line-number="302" inert="inert" style="position: relative;">            <span class="pl-s1">cust_email</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">text_area</span>(<span class="pl-s">"Email ID"</span>)</div></div></div><div data-key="302" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6040px); min-height: auto;"><div><div id="LC303" class="react-file-line html-div" data-testid="code-cell" data-line-number="303" inert="inert" style="position: relative;">        <span class="pl-k">with</span> <span class="pl-s1">col2</span>:</div></div></div><div data-key="303" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6060px); min-height: auto;"><div><div id="LC304" class="react-file-line html-div" data-testid="code-cell" data-line-number="304" inert="inert" style="position: relative;">            <span class="pl-s1">cust_area</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">text_area</span>(<span class="pl-s">"State"</span>)</div></div></div><div data-key="304" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6080px); min-height: auto;"><div><div id="LC305" class="react-file-line html-div" data-testid="code-cell" data-line-number="305" inert="inert" style="position: relative;">        <span class="pl-k">with</span> <span class="pl-s1">col3</span>:</div></div></div><div data-key="305" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6100px); min-height: auto;"><div><div id="LC306" class="react-file-line html-div" data-testid="code-cell" data-line-number="306" inert="inert" style="position: relative;">            <span class="pl-s1">cust_number</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-en">text_area</span>(<span class="pl-s">"Phone Number"</span>)</div></div></div><div data-key="306" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6120px); min-height: auto;"><div><div id="LC307" class="react-file-line html-div" data-testid="code-cell" data-line-number="307" inert="inert" style="position: relative;">
</div></div></div><div data-key="307" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6140px); min-height: auto;"><div><div id="LC308" class="react-file-line html-div" data-testid="code-cell" data-line-number="308" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-s1">st</span>.<span class="pl-en">button</span>(<span class="pl-s">"Signup"</span>):</div></div></div><div data-key="308" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6160px); min-height: auto;"><div><div id="LC309" class="react-file-line html-div" data-testid="code-cell" data-line-number="309" inert="inert" style="position: relative;">            <span class="pl-k">if</span> (<span class="pl-s1">cust_password</span> <span class="pl-c1">==</span> <span class="pl-s1">cust_password1</span>):</div></div></div><div data-key="309" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6180px); min-height: auto;"><div><div id="LC310" class="react-file-line html-div" data-testid="code-cell" data-line-number="310" inert="inert" style="position: relative;">                <span class="pl-en">customer_add_data</span>(<span class="pl-s1">cust_name</span>,<span class="pl-s1">cust_password</span>,<span class="pl-s1">cust_email</span>, <span class="pl-s1">cust_area</span>, <span class="pl-s1">cust_number</span>,)</div></div></div><div data-key="310" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6200px); min-height: auto;"><div><div id="LC311" class="react-file-line html-div" data-testid="code-cell" data-line-number="311" inert="inert" style="position: relative;">                <span class="pl-s1">st</span>.<span class="pl-en">success</span>(<span class="pl-s">"Account Created!"</span>)</div></div></div><div data-key="311" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6220px); min-height: auto;"><div><div id="LC312" class="react-file-line html-div" data-testid="code-cell" data-line-number="312" inert="inert" style="position: relative;">                <span class="pl-s1">st</span>.<span class="pl-en">info</span>(<span class="pl-s">"Go to Login Menu to login"</span>)</div></div></div><div data-key="312" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6240px); min-height: auto;"><div><div id="LC313" class="react-file-line html-div" data-testid="code-cell" data-line-number="313" inert="inert" style="position: relative;">            <span class="pl-k">else</span>:</div></div></div><div data-key="313" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6260px); min-height: auto;"><div><div id="LC314" class="react-file-line html-div" data-testid="code-cell" data-line-number="314" inert="inert" style="position: relative;">                <span class="pl-s1">st</span>.<span class="pl-en">warning</span>(<span class="pl-s">'Password dont match'</span>)</div></div></div><div data-key="314" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6280px); min-height: auto;"><div><div id="LC315" class="react-file-line html-div" data-testid="code-cell" data-line-number="315" inert="inert" style="position: relative;">    <span class="pl-k">elif</span> <span class="pl-s1">choice</span> <span class="pl-c1">==</span> <span class="pl-s">"Admin"</span>:</div></div></div><div data-key="315" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6300px); min-height: auto;"><div><div id="LC316" class="react-file-line html-div" data-testid="code-cell" data-line-number="316" inert="inert" style="position: relative;">        <span class="pl-s1">username</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"User Name"</span>)</div></div></div><div data-key="316" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6320px); min-height: auto;"><div><div id="LC317" class="react-file-line html-div" data-testid="code-cell" data-line-number="317" inert="inert" style="position: relative;">        <span class="pl-s1">password</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-s1">sidebar</span>.<span class="pl-en">text_input</span>(<span class="pl-s">"Password"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s">'password'</span>)</div></div></div><div data-key="317" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6340px); min-height: auto;"><div><div id="LC318" class="react-file-line html-div" data-testid="code-cell" data-line-number="318" inert="inert" style="position: relative;">        <span class="pl-c"># if st.sidebar.button("Login"):</span></div></div></div><div data-key="318" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6360px); min-height: auto;"><div><div id="LC319" class="react-file-line html-div" data-testid="code-cell" data-line-number="319" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-s1">username</span> <span class="pl-c1">==</span> <span class="pl-s">'admin'</span> <span class="pl-c1">and</span> <span class="pl-s1">password</span> <span class="pl-c1">==</span> <span class="pl-s">'admin'</span>:</div></div></div><div data-key="319" class="react-code-text react-code-line-contents virtual" style="transform: translateY(6380px); min-height: auto;"><div><div id="LC320" class="react-file-line html-div" data-testid="code-cell" data-line-number="320" inert="inert" style="position: relative;">            <span class="pl-en">admin</span>()</div></div></div></div><button hidden="" data-hotkey="Control+a"></button></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div></div>   </div></div></div><div class="Box-sc-g0xbh4-0"></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey="Control+F6,Control+Shift+F6" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div>    <script type="application/json" id="__PRIMER_DATA_:r1u:__">{"resolvedServerColorMode":"day"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mr-3">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" fdprocessedid="vo3qa">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mr-3">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" fdprocessedid="oqb428">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none; top: 7.60001px; left: 201.819px; z-index: 100;" tabindex="0">
  <div class="Popover-message Popover-message--large Box color-shadow-large Popover-message--bottom-left" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>




    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" aria-atomic="true">Pharmacy_Management_System/main.py at main · anweasha/Pharmacy_Management_System · GitHub</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only" aria-live="assertive" aria-atomic="true"></div>
  


<span id="PING_IFRAME_FORM_DETECTION" style="display: none;"></span><div class="sr-only" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive">&nbsp;</div></body></html>