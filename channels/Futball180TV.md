<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/S6hPPIUn8MKcCYJO4BYRBwmt2v8WL5tK-MeO3XvnJx6VXGmIvKs73K6whbguU45t3uC89LWRsADwWvhGCLvr-7UXzcgLgAY26Cv3fZl8rO4s8Y2RSHR-pviQ0uHwKQ24M16uI8EBod3zuKEw23BJvuCbYsvLEC8Oz95XDSFfFhTrLDRed85sCpNOeGHRDSuw8mgFPPwe-VHSaEdQwspRcHstzsXps6fnDbgFvoHJGpoJPLbDTsHmp3ypAalHeLnji-Eia74lpPvizKkh1LKuqSh1PTI1U9YmV85Gsv_IoUZghVoSvgHnPbBt8mRAhkZY4VC7I_5CKtrSfj9PKr1hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 555K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-101202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUZEnfTFwAsBcKEPuEiBOxR_AJ-sfEMursOrVyLeSrt8ab-48xRE_r6XY5_2oAGibPxcKd0Q1PAWONmTFzcQ0m--6OJCznfeTi1gii2pErGaAvpJMCQTQRqu6VLjijc5-PXYt1ikngNab_fjpiUevGAYz2-41wWXIM4YKB8RFwfdpWDF0QlWKGgnh_qx1Z0dRk4GSxUfVn3uhZgsFmAeIgv4_ZJYEl1AisQMdkMnsbuHawSuefY-UxRbSWGsJus0u7P4JFvyiF7X8OqeYuQwuZ_jTapv675Z24qKnwczMMRTgeqsHmJqx0IRtm2P-vQqEBUzXXxtX2kIGQ92SERt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم برای بهترین هافبک فعلی دنیا
🫡
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/101202" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101201">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1P9KyN5zLMzj0jWyJ2xEC45TgWfvxUvFydaJsbMinnlo5FC5nO4ITdMcw7qt53b3VEHAy1OQoNvW73qBK8Z4rYSSncrF5Ot2rDQD3NL3WgOkufvMFf5NH9yVe2PBopa0swicNyysS4JMYczcuiJw4Huf_jzLofiR_vQU3VN84a4EPBgJreMhQeT1NRb7aulvz4KeJ02pXocCO3L2wOXpmOF5iMWQuQQWi4Fht-LPvP669N3plFc783WPNbH4nPWKnc8VWREptH78KLha5_yP8VVc28ylNhCP16A2YEuhEKoaNtCamOs606vlLxIz6VRjYmK2QkOSYlXm1MH3K7vmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
🔻
فران تورس: وقتی مسی در تیم حریف حضور دارد، طبیعتا نسبت به حضورش احساس استرس و نگرانی می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/101201" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پادشاه تاجشو داد به شاهزاده و الان قراره تموم دنیا براش زانو بزنن
اولین توپ طلا در سن ۱۹ سالگی به به
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/101200" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw8OOyIgM4MxSYWSydlJGEeI4N-7VPFApmJ-7T8jeGxwxdAV-cOLYJVvRMk9gabFsc8GIaHUwgaJm6U9fj-XR6TNgUGWAHGVT4jmyfWwErBBHXDeG_EFzarv5xD5FqkmdYvqmZccWe-kCgqi_9UMplRcrsDluyo0sRVfhKLsV8Mw7sesOzeLnykHtwXuw7T9litBzY5HeR-J2jhq-lLg6myg5PVSzvbrz-eJvtrrx0BXUG_3XlnBO5tU0rd-dA1PzIIt686hp0Pa53fu1vsW4cSPRZT1OBFPmY5DcaH4LWP4lGuNiQ9odw8UQaD5IsIwZ0Caa2NhKOXbJpYzy2kc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
وضعیت تهران هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/101199" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101198">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEce8fV6KidkroASx9UizBaS7HmIWoSCOvfWXcRHoyl-fU-sioglSYpcrX8Y4ZqlEIFeCMsEmGTwuIHcf3R4VDalAOEWgsBSreRiGp12dlTp87wNj_451GksDanc-etoe134g9SfgWtdc0NHmi3shIJ-BqWgIF0Dcp4EPF7fSDkt-nPM2YiVIb_GtzfXPVAqihRm4eTa7ekwCwTQGxRKSAEJ35r-Lo8tuPHPMv6OMvZ51n5MiPs3-X99Ha45uJebHLX_PfT__ll7YzyGuSrEnHuiZ9M_rg8sJoSU152p566r3VSUbVivQNVEP4zpXdV6v8_SFltt1GusSAjhJlA41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
پاردس که وسط بازی باید اخراج میشد، بعد سوت پایان بازی قرمز گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/101198" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0oc8VBJEHyji6okHqR-N0QZ7XMh-cLUP5X2EK2ySnR0BuDqIXrd1fPDY6dYQaYeHbr4Whhmyx0cfzQKSvZobMu-W9JYoJID9I1A43s9cTHLajSfytSmZORnaZWLPNazJ6HGpOxezfltIJhNLx1pxT2QvL1L2s0e1kV2Ly0qL30tZUwpc3N-jt7Bb73W124EaR9UqySnb3JcN7gRSmPUWjvqdWSXXNaLfTAN7XzoQ25aGH7reCKFGfYmxPWTtVISjf_ckDZSwr2xWSykLOcd_iausILGtfApGL8qroNgcPJyJ4XrZWWtEEWexlzIVPO9BaCstaTla_38Xa2_QhhIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
پاردس که وسط بازی باید اخراج میشد، بعد سوت پایان بازی قرمز گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/101197" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndo6LGSMksoLD4Oj6Gb-TNBJ-1cj_zZvcIsjxDpZC1tR876MGpxBma2mYDHi2zc4oV7Wu6xdPvEvAGnmiWmHC1XalcNAhQSY9SQ6ZC3mPxxAhJ-h9mxS0eVB8Kwke1kSfxkgLtL4bPYKQMASzzHVRoorEQUvneG2a7RpuajrBX4h2xeP-uCjLB4y23hmFMTMPeNFeKXEI0fEvjgxuOtlSGthT6fLkrBD8jia9jpS0G6amovuwBbs0YiCU4p46KJ-ixVZrecgkzuUxUV5a0wHgpvJt8fxeDybNYrztOsPAG5PSsIGU-2Uy9kZhxTnZgBWLTCaEDonjNQTBrj5a44ImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلداری یامال به مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/101196" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL5x9DMXZbQuSlw1dJR_R5A8DVAsYvsXA4U_l9JqaR6_zVT2EI_GgmUk0iQG4Dp49DKYejeJaB89v6tUeeK1c6p12ZezpvhHOY-KULCpRIztK5JCEtYT6fJ-20UTT_QDsEFPgPZETCV7m8oXX_xglq91pzgv0XjXFBekxwSZRTM3tAEN96dzvLSC124Qo3cF6U2HFqkaWew4m4MInlf7VUs3l5Le7NMQynbqLrztuvdFvHrLLp2RROq2keL-w_CSEbae_BiDG5I9H9qWGioZ0yenF6yBuHYVXb1JMEc-qwuADYUJmayDReg1jch7L9iCpfTQ7hUEWwgypWEGSpH2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اشک‌های اسطوره رودری پس از قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101195" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101194">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqDrSHav7zFFxsYahLxikYgyNKK7DFpi5HViHFs4YsHKJOPd6PQKpzGaE4KMYuRFOEJ20dzXmEGvx3QNvK1I10QhBm18qQco_dCUBUWxj2Hy0_dQfDLW3fakS8ImesCnH4VrRgMn8HK3jEBKSOtz9Gt7Cgjg-Lp7tyth1XWMK6AoTvLqKvwFL0tm1IcUk6XQ89O6AOnNc2U7o-15KcidYig-Z8C30akVtI5r8GJXio0Lu7wIKpjJEnXyGx_gWwJET-NuX-6oW7pkj5M66bNB3RIz137S3oSG2eS1XJXBiwyzqKpAwoCosPKxs3Cr309bi4SYA87rCl7GASCMxWPt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
پوستر جالب ESPN برای فران‌تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/101194" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNHl6s4lt21CGErFv-6-Na6554-heTV1b5pOyBymaxkASd9Zc5Q97q0y14Iwf-IS4-eR6QyYcZg3X4NX07Sy1zaNKFKhCYG6HxmXk6mAiTg1NYPDTF1vXycrKz-vlIM9KllgrfWAgvlhiKQ9j-Ak3ayYyEV1Bgclf1sYri9zKr26rjkLhxT-mrqvo3RA91lcCh1P_FxirJJ5Gax5I_EFBjGaME4M9F35j1dKAn6Ldkqw04lBrzjkGTReMRt35yCNOav3vSmbVrchOBJR_HATHr24UX5RYwP5nRlwBxNRNJ3K9GAqshbEZgYlWrWqs87eE5nP0Tull4yW5FB0I4FGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/101193" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWPmNzHNZV8MdiI7BQBmLPWCdPkahNYtzr2UgiCtTr70dkU9chh3WiuqQkj6RXq9ll7Kt2Ia29w1ob5Sh2exqrBLE4NOEl5Fs2soRtoCkDlVfYBMBuRij3W3urU3_7Xnh9MlEUP9e0A1btVIPWn-Asp6mst7vUXriMrlq11U5YW-LgLv8I9sQdmkvhBxqfQl5xkVcugthzxTzRyK-avfFc6mODUC-0UoeL0gp0afVBttw0klY92X-a1_pX4M8ka2_wW3wz6-uTMrA1O2Iowwofe1mzfbpMsrIG8UfE7_Lv14YyG-b-y_D3cKq6bpHYFEGa2arp3UPsjkSwWxUlg3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufR9HrrIkFw4l7_TVQEyNkSMH0prMTUiObJnCVZE9ysws2Hv60XO4XPyaGv9b8g98XSgAQicuv4eEcHape3Ql4ptFhnjMGpp4_cd45qhWDyQ-eM4_EgtdQey8A301509fUfjhlT2KyfoyODcmwrsRm_L8pz5JOWdqCH6Zdh_kLjQi1G-RsljCTI_OFwpayku6s4vWzrKXGEzyBLHZpkqSVRSHQkCDK_R6ivLE1lHoilfPPPdCvocse4Es2iTyCNwIVJSL_1Fvww_x4goesAcZ6S1uKWA45Po0Ijs5zPiAIH5pm_1wo8b5zr3FZYYoQcpiWIcNY4tBElFJn_zaLwW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjEcC7k7ptI3nnMZqGYZEwoIO4R-rTt_rWiTxWtcrywVGKpw9NyFQZsQ-03kPC4qp65_fzQK853F9LhfgmZFYPV9w9UGGHpGtolPLBolsB6ETDVuSiM02ZrgF076U5R0q1pACSd8coNtGYp1fhgig0bBh1kFQlg9RCBx-LqJYhvXPHIXV-vMUx-msISgOC1wMeuvBtWw4lD7y8tnCXxtMG-jfnATsR3Zq-nI2I4Wdd2X0b_-vn2EV2JwQ3NI3iZTs648Pqtsdi_yCGqA3QlsQwHOR6nDj9Q4bRhM6rZ56a0rMBhT0khH9yp9bE6L5WKuqQsN3j9S7Yj-ZztnPNJE1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🔥
اسپانیا برای دومین بار در تاریخ خود پس از 16 سال قهرمان جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/101189" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSv6lEnymRkCOBIap6PlaXYXhTV4DUfyCh0zlX0RWsY_TS79iTUlyNgAP0FxE4-E3FIN9JUClT1AqnTzvznq5EXFFtXOX1o6akfRrQ9dfzmZrRoE15APUySYNzRoR2wWpfwHeUF7u8NczNkqnBVdTj3yPTzKy8X8Qmu43Xny6JJ7y5TTDNCORv9dRsOQFL7pYblsqcZfz_GDEn0Nvg-O2pbEmms4Req2H40xzv1Y2dFSe84FPyFgjMmac7C2HapGSL76kH9sQwgx6gzKPJpPYxLCdhbn86JmGCwshmI5Eg9E6I98X77ukyT9TQjQ630IWM1drCcwBlIWcekATyvZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو پس از پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/101188" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101187">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUG7VgHMiZdyRfeR7kgcxA99kfBcnYNdG2OzvjN_5K0eVCBWMnnjYTChzqRFbgcTT2LHdhDir8iPJW4_2kQ8LnptA-UpHWq_qsZzyroXhlOExMCOSrRoS_NG7aF8bdXCbVTCselXk4OIid9Z3GL3sML-aiVU-R1svoti65CY0GdI6zYn2QbDvWRGuOB5G8jXIJoRF1GcgGYNQPHC6KJWF67yQ3heB7LbWGtKWvMGqyhcC1aHbZV_6opSWqYP1D9o1ZKAN07w1W9kE_2JW9PsdT3278o_-1jeyMlFNQNt0NtydWBF3qEigZFL3yuuv8xCEvx1GoseiNLap_cnLc-oLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
و در نهایت Last dance اسطوره مسی در جام جهانی اینگونه به پایان رسید...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/101187" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b4743485.mp4?token=Wl_n_tY2hapBUUQAVqzEY9zPOn1D3oNOn-Kra136B64m4VQJCuWmcLjJsFy6Yg2vE2copZ574MiGOjh0T5MTUef0d59OIq-deIjxNRwIlKlOV6Bm3rV-Qd5VX9qFkxHuuWg0D_xjf3JU5DhU84SkFkkAa5RL-Aw_sgKsE903Pbcg6b_rEK4ShurOmPdZJ-ooMK7AmD9I81fpmDxJA6KH7NCrCfT3ju9SATGXIdNk1CY-QNJ-gtzdsFVW1aZLP2jdLitmfWUNddqIxEI7S6wBgqDkDdBG_x0_doqUAXZj-Qvfn_rv4LfjKMZvcZTEdoH49HnqRsR0U6IemeOD4UG2XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b4743485.mp4?token=Wl_n_tY2hapBUUQAVqzEY9zPOn1D3oNOn-Kra136B64m4VQJCuWmcLjJsFy6Yg2vE2copZ574MiGOjh0T5MTUef0d59OIq-deIjxNRwIlKlOV6Bm3rV-Qd5VX9qFkxHuuWg0D_xjf3JU5DhU84SkFkkAa5RL-Aw_sgKsE903Pbcg6b_rEK4ShurOmPdZJ-ooMK7AmD9I81fpmDxJA6KH7NCrCfT3ju9SATGXIdNk1CY-QNJ-gtzdsFVW1aZLP2jdLitmfWUNddqIxEI7S6wBgqDkDdBG_x0_doqUAXZj-Qvfn_rv4LfjKMZvcZTEdoH49HnqRsR0U6IemeOD4UG2XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رونالدو امشب که صدای گریه‌های جورجینا رو می‌شنوه و می‌گیره می‌خوابه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/101186" target="_blank">📅 01:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_27CigGfB6xPztKIWu6AJ3ndkkOxN4FtViPlFEzMCsyyJbZXPTVm1MKDWuGPQ3NVz32SQHtfr7GWQs97oO8eh45kP-XojtzH5bKjY6ZtMW4pRStHrAToog7a7c3FbxiBICGapKVIuhgK3C1JE85MaxRKdiru_H3NHbtPUgUmvdvyXCEN7FJcXuVO-kraEkNKMxwAQgAnMc7r2NzWvMMab6t3ajGCUoCap-Y9rMjivqY55xRt_jjJLCD88suUyReVFWX2nhVxgHV-zt8t-RTDZSJGkkOSm8W2kTVAkCtdXEDcFhldgURfJKDVIfkaQ9SXtApbDNUWd6OMKLcbVPrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو پس از پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/101185" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSJECG6VSO6NDS_pz-uLqQex_NlaGF8oogtNIQ1yeTL5Ua6gi0OFL9ksCmKpx8mmD6NhGa9P6C9tZoPqjoAurjE1zXa4yK_dTSdW8i5wmZEMZbr3jDR_SrIbnNj_p5Tbry8lcJ3yfoEJlmVX9Zo-mEsyjsmok284AxVThcuGH_tmULZWmxAB9b2sVjAMs2gZVMWm8lpzaGmjV1LmBniJpiwqVrs0t9gQ4d7zsisF_mFgGemKq-6emkfZeVfvkJ6Dw0ZIgHPyaTW0d6cMUkts_EmNNNe8CQotXGT9TjX2q38P6Yi55WhcsjmF5YX0f71SmnLz5Wdza70XSPpZ5SfWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#رسمی
| امباپه به عنوان آقای گل جام‌جهانی انتخاب شد و کفش طلای جام جهانی رو به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101184" target="_blank">📅 01:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLhxLRK558tNKeVs5Z7HpvYjJMIDahvkklMtIuXBmxS3gPC1iZNjwjgrxiS4I_9ADKkXgEmn8EwCr-oPVykhkJVdX1UNSXxkPI7vuDn2VP04HAeoPwVFAjMMHk1A4VaTOeUrrpbqGnAkNiMZ5VuST8dbEGNr6xq0o_9GBRLVvsffsXLa0cl_GUsUU9BeRiQ4dfpTYIjKvCgn8yHiLc03Z5k47Jq1EzD_QpBaKwZWsk7JF0WEYYYzUnXnoO4IzjTFp2rY2Vfcm5bDQE_mvmhXsZryX13JKkfe4fqZaxhr3RfjQvCfF7IDJmAjf2rFd2cYgR0InEsIbmWx1Zi_rogNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تیم‌ملی اسپانیا قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101183" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101182">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۱۰ ثانیهههههه</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/101182" target="_blank">📅 01:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کمتر از یک دقیقهههههه</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/101181" target="_blank">📅 01:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101180">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تازه بازی جون گرفته</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101180" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوباره کرنر</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101179" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101178">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">5 دقیقه وقت اضافههههه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101178" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101177">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آرژانتین داشتت میزدددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101177" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101176">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101176" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101175">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دقیقه 119</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101175" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101174">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy-UDw6TVm0UCR6xiq2c1gvx-Rq8_7Zh_M72VQaT4n-KmYJ2_8KPCx0sVHbMhFt7B2K4wIzYRw4vhwKc0zy3WFQOdaj0jxPNE1Hg3M6PvOC2qNhQ-wGcK-Fyae4sVMM-k1CWBuN6T1lbJ3F7BUe5m-jX0Ki2KGK_rziQVUiWhskXK378Lv8MvQ0jf7XXClkg4yMUPWjRwh4LEcdsPiWFdpECczMVoz06bB2o0O9cfhF2Ha7DF4Y7K6DpWElcnQg0_fYN9smTuXeOaXu1wOqM5UkVgKkFXuWLvz60hD7vCvoE_4mZtCmeHubPcct4GHAipNr_WtALisOUHRyK9zW2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بعد از گل اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101174" target="_blank">📅 01:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101173">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نذاشتن بخندی رئیس</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/101173" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101172">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تورس داشت دبل میکرد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/101172" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دومییییی ولی آفسایددددد</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/101171" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رد شد دد</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101170" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گللللل دوم</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101169" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58290e7a3e.mp4?token=EkMjRtvSeR8GTFB-2SvlqYiU2FFSjptD3yvRhEDRc7FHP_vcVQfntGM_gTi4onoQQjdPkAALzPX-31nVKX3U5KqLCIBuovEeDN-pbfHJxjJHHxrBUIQ3wQHUqv9_NdR3BeM7pKuXd22os2VlzZargv-VZyFKAzk1XgwJax7Lpf8C5Tz_Nzdbzm91uKJ_YWhJNP-pfXZYGpaWeXXBG87roH-_8WFyuQ_K0t4CP0b2o4sW8sL12EAW8Lng2GqlnQ2Whr8xn6tgs1me94ExuTxnBSwgAC-k_zL6jvMFeDjUNbEsQbiB67ik-djKoztqiKBxzk0Ndu3JrVEvpikunsdPdSroB_Rtpgueqd5cjukHJYNK46_08gfFyEUdbURBUSvIbjStS0dhosSqjDkq5qMsFiUvmaamMmbMInH8KwhcBaFVWqGg-aiH8qB0lGwxl91SEjPkIoOX-WNzftjzmOfjkiNcAVwort9e3xbF_p-r1a_JWyfkru6p8FqQoLSBcI9KDs3Ikz1eZgSFZ9Z-WQjoZSXz8c_M9rrx95G4mThYFyO7dtpqdv7uf4YzfAaHWFV2XtW7W_IO-Sme4Y0RBHY2XJ-aMkK4sRFt2E9KhXdNIW0KNo4Hjh_H4SGkH2-Rz3SlV60VshVs4rMDix7gAd3E1jkgkTQNoTgRwQEcOdRJ_is" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58290e7a3e.mp4?token=EkMjRtvSeR8GTFB-2SvlqYiU2FFSjptD3yvRhEDRc7FHP_vcVQfntGM_gTi4onoQQjdPkAALzPX-31nVKX3U5KqLCIBuovEeDN-pbfHJxjJHHxrBUIQ3wQHUqv9_NdR3BeM7pKuXd22os2VlzZargv-VZyFKAzk1XgwJax7Lpf8C5Tz_Nzdbzm91uKJ_YWhJNP-pfXZYGpaWeXXBG87roH-_8WFyuQ_K0t4CP0b2o4sW8sL12EAW8Lng2GqlnQ2Whr8xn6tgs1me94ExuTxnBSwgAC-k_zL6jvMFeDjUNbEsQbiB67ik-djKoztqiKBxzk0Ndu3JrVEvpikunsdPdSroB_Rtpgueqd5cjukHJYNK46_08gfFyEUdbURBUSvIbjStS0dhosSqjDkq5qMsFiUvmaamMmbMInH8KwhcBaFVWqGg-aiH8qB0lGwxl91SEjPkIoOX-WNzftjzmOfjkiNcAVwort9e3xbF_p-r1a_JWyfkru6p8FqQoLSBcI9KDs3Ikz1eZgSFZ9Z-WQjoZSXz8c_M9rrx95G4mThYFyO7dtpqdv7uf4YzfAaHWFV2XtW7W_IO-Sme4Y0RBHY2XJ-aMkK4sRFt2E9KhXdNIW0KNo4Hjh_H4SGkH2-Rz3SlV60VshVs4rMDix7gAd3E1jkgkTQNoTgRwQEcOdRJ_is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101168" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcAT2cgRhsXcDB04FoSZH6TGa2sCF3vCrtl6lFPd7dxDLJrlhwfLCYMxSMr31eD6le1AQSICEh1kgpXOJ9y8_uJx-ckM8lXosEI6xm0bFhollBZeQ5FlG0tg9vRKge6WDictw5v6A5uglPAnkAX3IVEWQvU3bwpNIA7earP458_6-L5F9TPBudIZByVMJCxMt-FGnMD_uSrETyOlY_yEGQdpK6lcJBJQfh2DfGtl-uydYdmsCxdLdmXHm4T_e5H-w5NY0vghTj75KjMculc016lpFI0YQhJOFnMa25vAa6yMC-I8GsJqMBDAC1d2n5x_JIkVNQeW6Jekvdrf4ESpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کن کوسه گل قهرمانیتو توی جام‌جهانی بزنه.</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101167" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حقش بود اسپانیا</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/101166" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فران تورسسسسسسس</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101165" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسپانیا زدددددددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101164" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسپانیاااا</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101163" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101162" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گللللللللللل
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/101161" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شروع نیمه دوم وقتای اضافه</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/101160" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پایان نیمه اول وقت‌های اضافه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101159" target="_blank">📅 01:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سه دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101158" target="_blank">📅 01:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همینو اگه برای اسپانیا خطا نمی‌گرفت تا آخر بازی مغز ما رو مورد عنایت قرار میدادید.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101157" target="_blank">📅 01:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خطا بود دیگه بیناموس</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101156" target="_blank">📅 01:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نزدیک بود بزنهههه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101155" target="_blank">📅 01:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پشمامممم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101154" target="_blank">📅 01:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwNJ34rNW6sWUp4q4zePQiPv22EK8cwcYEJlV-JDcw9lsNhVHF8TwDWkRCytnM4Qpap1Ad3TGt9RB-EDw9pL9utZn1ITKKewt5sz9sbCXqL6A7F5jAltqfysmt8ue5wIKXK3-ym6Ey0wkWnssYybXhUA6-JnZZzhHqtm1-JjvZFrNf9pX_18qj-D2A_5pjUcB-CY6hfW5Uw6AU2LQ01dKuVj9V7_VJ6QkjPtUdaF5XNyvoMFFQKjmsiT5LhhEW6QF6XjNaDdsfAx4AiMkqsJ88CL_5DcUYYKPiJ7nUrFt9uP-0BWknvC3gGFSY8wILGM969FIDwNWTkd_AxShJVQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101153" target="_blank">📅 00:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پاشو لگد کرد دیگه هی میگن خطا نبود خطا نبود.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/101152" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسپانیااااا گللللللللللللل زد ولی رد شد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101151" target="_blank">📅 00:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رد شددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101150" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/101149" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مارتینز نمی‌خواد گل بخوره</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101148" target="_blank">📅 00:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پشمااااااام</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101147" target="_blank">📅 00:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سوپررررر سیووووو</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101146" target="_blank">📅 00:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101145" target="_blank">📅 00:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4u4MyKJWaBJLHuJMs9cQ1iaH97UwHUxgufr3V7nkJzX2Q6j2iOiSbrC6WQdtWA2Ngo1KsghkFDFvDvNX6fygfBha8ooLr07DYIHSEzOI3CszOQ9JpNbafbUXmEJzJ89Woonkr6W2Bdup5EP3NbtZCDf89tQrl73TrGkJQw4Bfy_YdERdz1IJ3KeNAUdFtPg6rU5vEOoHvEnb0y7zD-BOVCu1zqNLzYtmXm2y9tFk0FDrj8Cf3ZRX1atOune4XVuSzp17srC44z_fDOsUrzCnWBnnubqsa_JB4_1xhWZm5kmmcCXrckOTJfgzE8y7HQ7MpCLVjAFE1UvDgwGclYoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار پرتغال تو بازی با اسپانیا تو همین مراحل حذفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101144" target="_blank">📅 00:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بریم وقت های اضافه اول</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101143" target="_blank">📅 00:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUPvY2mrD6aQwlaig7gIuwfWB2hD1GYF9iRlVfzjp8_EwiMBVhlD9YhSw47IM8FclQWixPjT3M-qlyo9fsVXIJqDkdPXdNcb2DqpOlqWY6jD4jvxw-5l-C5I8LJtGJVXOXjw3GM8IHt7E7EIDGlpP212eLEToQvQ3KXSA87rFR5CtIjdXxEAvlDa9G2SzkmWdL2WZEQ_dEivfoFzCdiefTziiQBk1a8lwKb5Dssu_2hFLIxYxl0aCsa8jmuKGKEk4NoUYMwyC9tSJd4g3l6eQGkaaCEwbyDyJPRThnmS-m0YS6PD-F0P82AlpbJDepnqw_Ba119UUolYj1GeARQ8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین رسماً تو قوطی بود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101142" target="_blank">📅 00:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار و خبر ورزشی فوتبال سه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_V7C7kYmCk9W1YfjqhoeMT8-Iso5-XcG2Dn1-QW7RT3VBO3TYAXjSNDyP23hk-oNjfGT7maHwkSGz5fOtTgfRhnCaV2pUqlu85ugIcfVKSNR0x7nqiyBdCACcwF3k4OdT9xeQqaZ1S5Sxjr-2K75rcxTS4ubriiqF61T40RaQDxPQEFaYkFK0LnWQun7e2wdKDPUJDale3rS5IRCpqWxwHJO2QbrdYg3W11yOgMVcWlGvphYZYIV0UybRNlPt-yJE744IwsQ1Wym2qiYvdhz7AYqz9y1c1KR6Kj5uTsO27hAg7rMYtzN_J-ReSkxLBwRz4jQZ_3JBY-iCkiUWt2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پشماممممم
😐
😐
😳
امشب تو ورزشگاه یه آرژانتینی جوگیر شده و کل
میمی
هارو انداخته بیروونن
🔞
📹
ویدئو گذاشتم بات چنل‌مشکلی پیش نیاد
👇
👇
👇
دانلود بدون سانسور ویدئو</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101141" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
بازی راهی وقت اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101139" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چه خوشگلللل گرفتتتتتت امی مارتینز</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101138" target="_blank">📅 00:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چچچه شووووتی زد یامال</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101137" target="_blank">📅 00:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگگل نشددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101136" target="_blank">📅 00:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خطای خوووش جا واسه اسپانیاااا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101135" target="_blank">📅 00:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مسی: کوکوریا جلو دهنشو گرررفته</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101134" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101133">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انزو رفت بیرون</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101133" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آرژانتین ده نفررررررره شدددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101132" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انزوووو اخراج شد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101131" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اخرااااج</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101130" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مارتینز گرررررفت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101129" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101128">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXuJFhxb95JuYyB_IKg5hTTvwcjbPYqKBLZowtO2a0lF7meCbR8n_iQkRafVtVuw5334HXzJUeb6ujJF_VLmFGyT4Hbe50fNoM1Y0h_XkxrqvK-a72DjG7qyhjCI1dm_XKB04fN7tJSXIqm7MaOkpc2woN4HPZt99q_dvyWgJECqblVOiXF6lQbjb4TivP6lnGTSYv7-_2VXxz6k9b1df8JWQOA_KfZkWbICYDVuysWmh5iVp5ZkvDomD731xFOfqv3sD_aihedIiZA1Pf3ObuLoeCV9aJZGO8FBSRudGe4gLbxdcxQxXxgqgPFoNltLwmJTkpH2VDYQzJOLUKSupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101128" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پا شد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101127" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101126">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسی افتادههه رو زمین</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101126" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101125">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اوههههه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101125" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101124">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۴ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101124" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101123">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به به چه قابی دارن نشون میدن</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101123" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101122">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آرژانتین واقعا هیچی نبوده</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101122" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101121">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کرنرررر</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101121" target="_blank">📅 00:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101120">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101120" target="_blank">📅 00:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101119">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">زرد واسه انزو</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101119" target="_blank">📅 00:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101118">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چییییییی گرفت مارتینزززز</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101118" target="_blank">📅 00:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101117">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101117" target="_blank">📅 00:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101116">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عجب شاهکاریه امی مارتینز</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101116" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101115">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">واااااای پشمام</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101115" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101114">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بازمممممم گرفتتتت</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101114" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101113">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پدری هم زد وسط دستای امی مارتینز</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101113" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101112">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101112" target="_blank">📅 00:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیکو ویلیامز و مرینو اومدن
بائنا و اولمو رفتن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101111" target="_blank">📅 00:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مرینو اومد تا کارو تموم کنه</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101110" target="_blank">📅 00:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سیمئونه رید تو حمله آرژانتین</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101109" target="_blank">📅 00:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آرژانتین هیچی نداشته و صفر شوت و ایکس جی صفر فاجعه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101108" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بازمممممم گرفت مارتینز</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101107" target="_blank">📅 00:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101106" target="_blank">📅 00:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">واقعا سگیییی دفاع میکنن آرژانتینیا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/101105" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسپانیا سنگیییین فشار میاره</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101104" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101103" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اویارزابال و رویز بیرون رفتن تورس و و پدری اومدن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101102" target="_blank">📅 00:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خطای خووووش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101101" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خطای خووووش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101100" target="_blank">📅 00:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101099">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چه دفاعیییی میکنه آرژانتین</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101099" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
