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
<img src="https://cdn4.telesco.pe/file/K0qX30OC7phT48fjn7687RXAAkWzZ5LKuOEqJIEpCmAfdIUlc4TihmqTWyXaq2zxDKMtgiysQVxvbv3GY0TNS8lTU048qiWxy3APzN0ASFkr8vN8u9FO9xqNifZzTpT4sB410sFEQ5L27rP4z1Wu9VV__hikT3MInoTZp0vxQPFcEG69L_W2rJmzMAHrUyUa1YtXeAFPDdXeaGhTjZbLq5ZIdSQmGshYjwykIMBfCQnHhVZGRJIT8CI8leXoUffyYAmPwpGfoGvwM555n1HMHBIKks51_g9nDWMLlrUErFwaTdFlyDibr30ka3uSTGz_i1hQFp_6pRdDD5Yrr5MlkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 482K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-31391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNJf6sfpS92APfFuJS-w44BR8VP1OGNUU0HQlE23ycGVNbOdjw1t8DS3Jo2fsv6XnSv-eDmkdLiPdnfNmPNkPSuccF2EMNTO3sJ0rWX12rSmsoBh4UwiIA_EndGwer6D7Y0THdELQkC9zECJNv70BS3bzcuS2xgWnYmMyu08lTK7lKmzpFlWoz7ZZNFpk9pyQ6M5omtxkB0j1W7WcvrQVkv-H2rpe3Sur0B8kDRkJEZUMAffElbwt43xYTWbFEapW4iIK8TbKn7btir7cH7wIg2QCzTu5a3tdxel6FveIka2twVMFIKI239bDe1MDm1Enw1XpVQL2ULi5t67XMjGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/31391" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYhYbUj5WY_-v3yVRjDco09ZN5SWw1MUXNoA_ulgcoXiiHAA2HMmmAmL1J4OzCTNps7aQLTKXUwoCefP9qdPa9uBkl8CaAtaqp3rksqiLeT1tKGRDtNgicN3wTu6OzeuHpZjKZ5XN6Xs6RgwpQ9YvJMC4eVPGI5G3u5Ac-GUpO3G3KsTDO4ysz0FpIhXiih-Fs7rYv-qkPuX9rVo-OIDxwRdCqUtTgty55wNe6Pmh4ytSOCQk4O6LJOIFBoNMuAjIJE5TaA_A3ITmnKxjaL8UOA5tVrm4f5Afq-yVKfZ4P7T9iePMybiGU7FGWPmXZ_Ngg7bUyW0DfQEDfVG-4ZLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه‌دوست‌داشتنی‌ترین‌زوج تاریخ فوتبالم از هم جدا شدن و خانوم ویرجینیا باید فعلا تنهایی سه تا بچه قد و نیم‌قدشو بزرگ کنه تو ۲۷ سالگی.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/persiana_Soccer/31390" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDfBAZpuNzK0t43UuDox-jSqwl_m-nv5L2Mq9FBW1kPvcMAjKHnTiptzxf2YSy0FMe-59plE-8vL5WWmwhzba7UbIZrCpYweB6XpWWddd-IKq8plCxNYJXJEDuqWNBb8zrHdgnKAplvxVwGTOvwBwumyx96-iGMeL4MG5qSZvGuljX9PfEUBSxvqoQICatGyrixwW0q1GWe5HEnb97mlFhBO1WL-L0ZV2dEbanI1k-NTJBBINPfHLXjuOvL50AD3Kp7-H-CbFirhpB5_Otnb_y5qsZ1mtnVexzT_Wy9QbQvtLCFDxCwVHfNn8UiS2uHFw3XSBOUpzRUKAaBIO_t1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/31389" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/31388" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKq61jINopELUXGBxDTISaX9T1uV-8nambs7clmQBkGzSUpdYOUplmMv-36x1lkNoCxsmGBxIwBSeIhTesT5an4a0EKotS2bfT9xN-3EyhMrywX1qnw6z0YDiaHUskmLjXpOg1UfjU3ET_Lzi9Cc4bHEW9Yk8PB2aCHoqPrIIcGNzK-puDMX4k_PdBlKrPhiuvdk2U0RnSvECkFtcRr52sG5GfIjD_K8xam2OTu15ZOzwTU28dv_35y4Je3JYtXDeaN7EzDbzmDx-IjfrziBeczs5_90YypRT9YNyw15BQTfAnJuyInzzFrkq9Rk3MJHBT9o_l9XPu3nDc9OaAbZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/31387" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ee700462.mp4?token=gFTxqvLjIT22sqdWcLERu1EQ-mN5I4uqWPyGnc8OeXWs6I4iy-XrPereSnX2pXfXmN2iAjfk3OLjkLLhP16-3d5uW7b62VmEYSDgBWU1xshf2DXDJAVCnWg92aZAcCAhQpnWtzbTtrqvgfGccDIcWpMJtZ0dqFPcwDxoyyXyFa0hGd4i6LquUN_GrUzeLZXAOsKratfb-YqsmGd-LZgu2Ec5J_7DcKE7Qx9ajIp4I3MSCDA41wNhkFRXRkV8SrQIThUr8gtge0wae6wB4ppITkuKrL-79VAgqcwR1Gm8ymsRT2Uq4zhyfcsem2KW6tJjTjifYi5wUYLoQPWxN1Ohs48R66y7c5CsSQX829PV1HphKH_5iBqnqIsdAW26mt8frmFX9XRMGLrBcrFNeusw6nA77boLAcirKVEMYxu7T44cW4gIbhDaGNrCkwaZPzuzi46AXeYLGmdwwEOMpbHcDFwFuxng59GuyQJ6LFzUPUYNEEby7Nckqd5LaEupXc7NV8zOsbdpW7PEAFLVMqk5F83SMEEav5bnoTCfNcNxTw589zmj_3gbDniyrWnztQwhVCJPb0ICtIzkwRmEySCZt0ffNzAYQUC7ZmXyEANqxznkyXgTKYi-eIc6HANh8WIf7OpbHI46Dl54bXSMb8bO9ju9OS8VZmPNa0UhcaNmCs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ee700462.mp4?token=gFTxqvLjIT22sqdWcLERu1EQ-mN5I4uqWPyGnc8OeXWs6I4iy-XrPereSnX2pXfXmN2iAjfk3OLjkLLhP16-3d5uW7b62VmEYSDgBWU1xshf2DXDJAVCnWg92aZAcCAhQpnWtzbTtrqvgfGccDIcWpMJtZ0dqFPcwDxoyyXyFa0hGd4i6LquUN_GrUzeLZXAOsKratfb-YqsmGd-LZgu2Ec5J_7DcKE7Qx9ajIp4I3MSCDA41wNhkFRXRkV8SrQIThUr8gtge0wae6wB4ppITkuKrL-79VAgqcwR1Gm8ymsRT2Uq4zhyfcsem2KW6tJjTjifYi5wUYLoQPWxN1Ohs48R66y7c5CsSQX829PV1HphKH_5iBqnqIsdAW26mt8frmFX9XRMGLrBcrFNeusw6nA77boLAcirKVEMYxu7T44cW4gIbhDaGNrCkwaZPzuzi46AXeYLGmdwwEOMpbHcDFwFuxng59GuyQJ6LFzUPUYNEEby7Nckqd5LaEupXc7NV8zOsbdpW7PEAFLVMqk5F83SMEEav5bnoTCfNcNxTw589zmj_3gbDniyrWnztQwhVCJPb0ICtIzkwRmEySCZt0ffNzAYQUC7ZmXyEANqxznkyXgTKYi-eIc6HANh8WIf7OpbHI46Dl54bXSMb8bO9ju9OS8VZmPNa0UhcaNmCs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی از آنالیز عملکرد پرسپولیسِ مهدی تارتار در بازی این هفته سرخ‌ها مقابل صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/31386" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEbEa-DKVmmBv1PmRmnWFwWOHWl94OiKTB0_yIXatFpUKkhduUc_MO_TplA6NCMJyg2681vCzQEAabnPeLUceF5M9PrMZTzaz7emYrbhOmxlnJCtZJCkKdEt3tkHHXfQGym3tISN_v_TfE4msdLXGO6Cy7qMqQxGDSPfEw7HrYqQ588uVn1TpWZHMfMY-UV5B0_LllXHM-TgaV87S1auKJHcxwAmcmfDyttnYwfsBP6jxLOtHdcmR-WdRA_pxHoD3PsAQeZ5PuQF4uNpkCBYInA-ci_qFAxCpqtuCH6IuB0Ax_-nHgLyZ5v4fKfrdcdIh7Ref9QyJKvT1FZYGhxigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/31385" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdMgB2y9tfSDjYusP7FYuNa_2fzSUvz5L1jXBQpDHNzj6J0fDQVSBxNWwzXr_ktZ44zxAE3nClfCvujxkzIBs_EvcDdmO2VY9uL9g9gHHJBReqFjRIFOHE_p91BDtsb7ElQGMVSHVGlYyD8N1RxEKiWDfi8iE4dZSEOlF3h2rjM-o0K3u3V_kDEQGca06LoscOhXNBun3V9ZMupZj-KGNg3rc-2m_z6lh7NmMIcFSBJSbnv6_d4ThcQyhwF_bnCFZXa6mdyHdPbH1nDtuCT2AMWw8hL6rap5sLMNkopnc8Y-lzGP0jA_xHEiynKiU_33sgOetcAegzVwFT8E4duiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/31384" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p50v5y-5Xacos4wyHivoP2uNRyfivJqyx_9cgKLWf4o1B5wfpfNB8gwCMoe2xUajyv6SdKOelbwPV2Nj6ic0t5nsXw4gdIIxenerW5nLpcUh5GTNGTQi8Y3mBeZc34hXmy5nxdt7OE0as3WhUXz3QoZ_XxmrZ5q2hGn40mMpWjK9nf6TnMkDB1QKUM4I3pmMskCQ1TcbcQYgCMXRPc7gGK1IfFPRMhi3UbKWXLFFVON1jw5WVpmyBwW8OR5xsDLnI47_JB6ECLdXsUf-2BIGiS1thiNvXch77DFR7zDdQLhza-qsX38bssLMqGUlqd8mFu8qHJsfO9Lw_T7VPQvUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/31383" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAj3zkHFHSdgMlbqGMHRGGJ71gqvzyiBNJIwIifJLxLQKknql0aWdd97SX8wxMRVujcU1Nc4UGsryvC7VBSitlGY5ROBuuirL94Jsq9CDdTxFZdUmlYXjrEd2xL9XZRBCu4c357pxj8KO8sgYBZEmJd6YC4XUzqC3qq_DpdqWcqvxP5iq8cbM9WQtt2XQt83_gqAQBXRl_mUQvN2ScemUQEonwIMkQGYv9EfbdzN-9-wIlQRbQSoXIq_q13Iok5opBJzxzRWHD5ObCs3a8CBpfc3xq0DqBHusAKu_roVeB1KGnYIso5jIgBzCvuPYNr1RRaDCW8BRFKcz2rtzZrgEryM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAj3zkHFHSdgMlbqGMHRGGJ71gqvzyiBNJIwIifJLxLQKknql0aWdd97SX8wxMRVujcU1Nc4UGsryvC7VBSitlGY5ROBuuirL94Jsq9CDdTxFZdUmlYXjrEd2xL9XZRBCu4c357pxj8KO8sgYBZEmJd6YC4XUzqC3qq_DpdqWcqvxP5iq8cbM9WQtt2XQt83_gqAQBXRl_mUQvN2ScemUQEonwIMkQGYv9EfbdzN-9-wIlQRbQSoXIq_q13Iok5opBJzxzRWHD5ObCs3a8CBpfc3xq0DqBHusAKu_roVeB1KGnYIso5jIgBzCvuPYNr1RRaDCW8BRFKcz2rtzZrgEryM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
g19
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/31382" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkqRG-9xHptV1emuld1gs6gHQQM3FILB5BgW-dPsTt05uR_u7sOMXPvC1gbETbERlnL9c0F1hbFTfDXWPHyPfNgYmbkOYM05sYC7scGWq9_1H4j-QRyXdOk0mH1GsmcQXlmmAmt3SNkDXyxd69eT5i51olW3njV3b-ORmdahl11W6fV32L9wFgIIaP7Bs3qQdLL99IV7-cQsJEXfHp6vVhtn7I0HjlMflF4FRi0SGXVJNw683jfR-Xr8gk5tgmPLzRLurNaj6J64PnGs_ybr_cZLbhVIKDYeV2lakJEr7NXmGii1efrQDk7OwU1MUUZzJPFDTv7LSB8yTYSTasiS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ زهرا گونش ستاره تیم‌ والیبال واکیف‌ بانک ترکیه باز هم نامزد بهترین بازیکن ماه لیگ ترکیه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/31381" target="_blank">📅 19:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaGEWJdkCEJDGytyD1L3voFeQl-gT1f5xIAVEhtD9Bqz9ncLr4LqIPN0-Tc0vKAE4fAmoK9HbJeLRwvy4zYxoU4ei6VIlCF4ywsl1SoX2zcauLQbez4bRaxO3hnLYwtpq0gE170sfaIo45jfZKciKwi8v2VNe97k7QaxDF4lOrV4DcvizZaHMqdj9J07bJHWVoz3zIe28lIejkxiqMNogF8_VxhYLdfghU3nuKhXBnDJe8IsCpbdUODo9uclfu2uiUdeW9Ql0zpDpggOOnjKHXH3bTnJsEiXWb3EvtOXTkmATVZdX-yVGFxeilFTLn1EqrBHwoH6W8RAj1eu4BjVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سریع‌ترین بازیکنان تاریخ فوتبال برای رسیدن به 100 گل در5لیگ‌معتبراروپا؛ CR7 همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/31380" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8eyR7FllEW5wTwPhRnhml3zSMo7DQ1VP9iO6Q0w1KJE6bPrwf1gDNl9MKMKIsIlsU1eiIiP1GQBzCd_VjDKvfyd8Ges_NN59o_fR-fwFzBx08QwbbPVe0KEY_5VDN3qBdK4dRzaVJKEYuc9QJMOLZmlZtlxkPm5zZyQ-sBKcNVGEYVDWK2BfSX-U-Rd1oGOc0BRqHS6st6fzZrgqUBJCX0Pkprh49kwLPhkSQvVnouRIU_PBYD3jjXmJCP4hmIRqqMfk6MYUWgi07FT2aXwrxKjNUAvyfamG1a_aBhMEFdDBJQtCpOOLsdpBle6iikadXaMippKDxHgnCZ254ux_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگار تیم اینترمیلان هستن که افشاگری کرده وگفته مائورو ایکاردی زمانیکه در این تیم و با وندا در رابطه‌بود دوبار درخواست.رابطه جنسی با من داشته که هر دو بار دست رد به سینه او زدم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31379" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKoaSLooqoU2oPKDRh_sbUHVxRolFzPTlBLjuuc0dMNx8EGyRt-7XhtWFw9U4aVcr83q32CW0AintqauwbXXdc9yUFOAxs0yIME2x4Q1RKXHEu2rGNTOHcF1BFeAyf5ggxQu1LSTzH4aJtxBGDW8_niHj0uR6Fx0OMpDQXf4k1cI8ioLlfmGS3oC6M8hyY_VTCRz62AY1rvxCAIDfU7PkmNRkcsIUPB7GaNxM5b6ujc-XVmIl2Mfcci5qYKx-05DMQUEbe4j0Ua_jouU6iIOhwLxON5oKVnpnCQn5bOWcK47v1G0PWNPDCVnBBCQfo_r26Sac7hi3k4TmvNtn2JwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیپ‌واستایل‌تمام"بگی"عیسی الکثیر مهاجم سابق پرسپولیس که تا آستانه یاغی شدن هم پیش رفت در اکران فیلم سینمایی ما که اخیر ساخته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/31378" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP1Xv_Ak9cGnQkmrYpl4yn6V3pcDoDWte9XsUxwVX8ZoarUi-wttvQV4kDwfCToVpPrZhENkEPQTWGo-L-cULUFkNoNsgMIWYFyFOUtvq5YyU05dXXUGQIu0jNHDBsl8y6B9aZF7k5_DdjX1Ri5u2lTtvgUKZ8K208JJ0dQ4d3TyqOj_BFi8rCnugDt-qh_nLWdcl4JzY604TfdOwfNVXgDsMQPVY1yplmUtX-TCOzLzzQkorXoxXzudKb36FcthoMJQMse93juqj3GOGAJpKCny0TDpmLnyQ6PkeYDNXNCBQwo2wDGDkMa95G63wZaYxnNn2Ozf1-6M4rxND3HvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/31377" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G50O3DRLtIH-HUGYFuSbcLTzY3gb1w85D5rbheuu5rplzt193AjrqacsTfrrbFbwCrxMi7-8cTJcvzy6-O8YpwA6QJfYhXCG7VeA_weOiWtFG2suFX2nd_xoOpCaPhWr9h8W9fM5XKebq4eyFE9pG7wQQfeG4jQaSryOHw7OLj4Eb9UxinyTTKKz7OLSF3cM7nhnXXuP-OD_GmpqotnTYbqhKw8pCnG28_8E8u-ojiBYp4DVqJLIRrpsxuspCEjcOJPS6fFYt1gP1eE59RHRtmc1hnG-wWSrgO_uQcpgvDHiYoVXHZ12YSE9sjprrKPuE4LWuLrn_18lk7HJ_SbumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/31376" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REkprrum3pXvUGRiF9l_iIbwYlpA0QczPi61CPdMI_5ivO2r7Y3yIgw8MRw72DFz8mrbUZlvQRF96K_a7cOiUxaGqK4E29tOKnhOrA-Z8mzlh4z82K4GAC865HNIl39qKK8de19pP0v_XiXhIBp8S97xnwyWjI-13s6zP6Du9zQskjbcgiUf-Z9uOnxrt0niHST67m2VO59lrQzskrPmgTlI6-IIGxEJRFpYvWA-N8cKjy61v92PUgDRzeW3gJu0c642cnZEpSA4Kkdscx3hxPkAJXmXxme5kdtBSbVyTdKs3SJGUZpnigUeasdfyFF4WuRbU6by5ASF1vH4Dq-YzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب تیم منتخب هفته‌هشتم رقابت‌های لیگ از نگاه‌سایت‌متریکا براساس بیشترین نمره در هر پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/31375" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB51KmheiSB7uxT-4CIlER3YR_G6KNMbU58hOfnAeN4EJDbVtvj47KlmzdJUEtMWEoAL8e7aQhpjh8LxIgsYigaoYNPXYyy7JTiDvzLVktUKFWQZUti8R7sK6IhQoqlu3UxX9b3iMAH4HChEGFUTS7sLTAISSSLsZHtKzTyEiHmud2sL2eQIhHMPZKXuGcJHJbgn90TJXp8t2K554PYsOeO9cGS9foh04dOx6fKlJdXrlvCLmyhcXTnaCpWEx3xFKB5Fqk26z_SjWJHNvFot1vTx9nLMevWQvfZuGauhxLyjHoaz194__4RMtARiurRj54mJI6JhqIt2CK3jhvQmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته ششم سری‌آ؛
تقابل شاگردان گاسپرینی و سسک فابرگاس در ایستگاه ششم برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/31374" target="_blank">📅 16:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31373">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwij_VzuFrPs4tjydVjJnGHUzybHFFpFs43d5dkKr3iey56FGpm82wUJWqJk4qHEVWdCTV7wSesUmO_tNDRzXG7_WC27frL7K8xz7LX76KBYe6M9vGf-PDyRS954UHH4yjf7mmbMDlExgCP2-tgr8ACBOFRwYJGp2GhXP1tTpeaQXjtIvCFJ78mtl8wYuS1u7VKI-MTdTXhXJnzOpj15QblxEdasXpAYjrpPn7zRk2IU1138aOre-ufTGF9FU8RcOK3yxs22CeJfgpXz1Jdw9xgR4i0bYrc82VFLxFzGhtuyZBLL0EZAZiIKD87s-76vOQtRia-BdmfVGrPyI74zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهراب بختیاری زاده پیشنهاد حضور در کادرفنی استقلال رو به پژمان‌منتظری کاپیتان‌سابق‌آبی‌ها داده. منتظری گفته بزودی جواب این پیشنهاد رو میده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31373" target="_blank">📅 15:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31372">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrSw4aXtgBLqUAJrWOsacK8yPgt0vje165gHIAUhj08yOPEpf1yTQ9XSXY_qmUPQq7lTwnVYI2JFD7Maibt4nppzZbVb9UGH9-8KF0K7LNL7K-Z0zLuk5pnO9dVEPSKFrLki0WNnm8UJLqctcLDx0KnBOVRjS3k_97Z0-0MytAmljZfgK307jvZUJuScYT78tEwiLLpWRBr0zSZ_YIRxuLv9eWILNwyAyHTYCx9BH__tAyFmR_I6G2gxs9H8sDjPJBU2MV0h7K5TOGvNY_-n7p7fS0oMMy_lGySzss5rk_kk8KiGn835-yDeCqGsJfeXonXSoYty8Vw8kYk1wg63QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/31372" target="_blank">📅 15:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31371">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLwwgfTNoOrCen8PXoSV7vso5GgF9GO4BHY1aZDZcRMqcgya-zCMWqc5pVXBnSxfiVatJdvu8pgdE3_qQZEkF4PSgrht-hmniRw2JorNx9ZkKUqiNxTSZep525faXWrcK_CJB32GLuZU7vOCtCyVlKyUtG2GoZvvqeq8G_JsVrkxicq2AvV9Rzh_jEzQAPu5Q1_APjS9JxLaVyoSRXyKfvLb-3K3EIRFteHGhQa7E57vwi2MiY-KEQ5kWdSX82aZq-lDQENNZGcHSj3edvv_myc65vW29021_cl6V3jQak82vSYlZwAIsljTKFa66IPj4TYLw1vJ4OrCj4S6rJAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/31371" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31370">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
ویدیویی از پاس‌ های تماشایی پل پوگبا در مستطیل‌سبزکه‌منجر به گلزنی هم‌تیمی هاش میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/31370" target="_blank">📅 14:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31369">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azbJqf7em49RGQ4pZYiU1ZryBZBM96PGiY-iUAb0dHulImsEBoJE8HElA5EhFO4-Sggoca9ay_qN7BU0hLmmNx_oju47KutJ9wLRokFqmV-eD20VcKdk6ilTwnySHuLgpCL28HFXip9ktJVkSVcC_vXk-arMDEartm4YP-dr2nJNaGVgSsQ8Q1F41yrFWYeE7hISphb3Jo3utGd8SjvjqKKmAObn_OUkvQr4SNdzfu-8W1CMVWYDuixnWxeZe_-M4nly1gDOWoy1Ykezq245V5IFEK63PKfsOtLmNGM7Z_FKM8c3nKozpjN4XbU-KCY_A7JiHvSGVCy_95y8DICdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/31369" target="_blank">📅 14:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31368">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3XmSRhTt7zzhuHzFPwVBXVH0chTYeQiK3JvTVc8pO1YJoAEk6US1vml3qpqGnn96xfO9jm0AJ-9c3iaDAUqwbjvdiE7K34rgJhI5Bly9tIouPM4fP3hhxExFf2zJ6dkT3QKiqb4B70q92_Zm0dccaTnzAdjKIYFfkNfSP76IamcmFIUd8LXHm2L4-zZS9jtRzXgDoHylQpeAg2wRgTyVgMCQJAC4kcOLiFcfpXi5YxqotQMxoy7IKeLsiMCI2DhTz39wTFT3XvaMMHWr24mJnA-D8T2Jag_JKCgcHa8gOryS0aE94tOYep9XK9HRSw7-mmMY4pTSvJOswlMxc9ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار شبکه DAZN ایتالیا و از طرفداران تیم آث میلان که گفته روسونری با روبن آموریم به جایی نخواهد رسید و باید او رو از این تیم کنار بزارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/31368" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31367">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Odhq2xI7vEz2EHHN4dQfWjXzJauepUIjp6fToiJ-hkBxcOJ0GNOwl4AYq-MRQb00fwczAB2YA7e9bsIE95DWs8r7Nq1mm9JBznJyLwS5ggraBVOgkmaQ6SYQKaUUtvOM2FU5ivIluM3FOgsJm7Z36BHc6w0LUOX1GUWo7haatrmRSbDsAnGUOWWvFt2hhAbRZVz_1BYtJmoO_KhPCCXxZFhjLzcZScI6QyrGd9UDRYliN5rjpapVuQjEmC5n-fZaCKpnDH86mkwBKE47fV-UeJ2smQPxmFt1MHP7zpy9nOJEEIY3EL1mvR1JqW3cN2unxyMaCLcLSH-mhZpgnF4wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ساکت الهامی سرمربی پیکان قبل بازی با شمس آذر: من‌دیگه‌اون‌ادم‌سابق نیست و دیگه دست به زن ندارم. ساکت الهامی در بازی دیروز با شمس آذر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31367" target="_blank">📅 13:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31366">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv57vaI7ZRX1aVsI1qDse5wH3U1v_2Zn7nZ06sRJ2ijcbz2Ws2DuVvZ_5hWPvqDksId6yAZ7mtQ3o_-FmkJo0Jc0vd1d7ot5tjmBTAWr5e5OBb8HTphBjTD_Eh2iG8vnRSl4c8v5Nod-wQtcuGwVKRzmtOXzFWrr702-UgugP5lm1tzk3WO3Y2bgepCfta5DKojvG_XORUM5yLYsNLwimZ8pXMv3HmaUIvyTIqMR2lgNW4H-Wjqw4n7hQNvShsap_9YA-0nbmkt4dAtRSJWQ9_oj_nGRqPTtUdvjreZuZRzNpVwkIHJ0Uyt_b5AL66JbLvK5P2ichipCFT50Xf97cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31366" target="_blank">📅 13:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31365">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31365" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31364">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/31364" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31363">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOfrKsBGQAJohauRuSSm3epkY2-Plotp_sn2M2ZjCU7vZvcWfwVNVir5YSH5WJg-TbeIWYIrNFWUSTMjb1AAb75_jTp_6MoCtJVESyYjQaGfd6uj9aJaAvQ5s8JxAg4iLf3es1ZXCc6QClJjtQV0lSNYxlJ0ITBTFg18WmUvNvgYE7r2SQV_ydbP8MfTHzgg-AFwL3qUOxSEq0zQasUgQod_Mb-unF3DjlRjHCrOmndvnvGPY-3TbyCKMK1Sl7y0bkrRRiuRB8L3DCFts3dRWgcPNB0fcQal-9jRb37gv3tcPjff7m0PfLtdFAY8kY_tzMj2XtU5uLv8aH0pgfFoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/31363" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31362">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31362" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31361">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=RtLg969Z1pnC__gaYU-9kMbARXoNKOoz1F1aPmmn5EeAFyO-1Dhmaeg37EKsLPWCcZ2SWkGRZ0UAG7ZXnz8o4y7h7USC7EsfTTz-iv6KnzONuIc45cOE6ZbYBfatYIfRjXHzfIh9lVBQAJX5Wmip-m9ptTDdJWURs5I9cvYDjzfgqij8_hF6ZYhNZZ1c6BmgtwbgT6zmZi71zvLvjwTBtR7R0descoXB4igAGuT1ETzmXm5NPtIqn7yr6bgp97ws8C9wJdUi_mGM7pi6vnlG2AjTiXekzmMFAFqOIqzcTGrVH5dNwrqRBVno5t75k7k5y14Y83k_GVb7RNmZbJR5mB2MwvXkYlwO3Mh-jdxWATfh5Xp275QoYY-9GXnaAi3xvQqsc1Hi281itkrDNESy7btqERArUg2dgxU96DpdNjw6EF0LDd2Fbe8vFNh94ip9RXsTUVRqnw0thO9Y0BaB6TVem3zGTfXlaJtiRGyChA30-cIAX26YVyJF0xDcCw8SZxQ0DDH4uIBPgHgvn51FUecQaVU-jhYOC5jiCSdOQe-QbhcwJvUUZQVazXje8xA1WH4eDrU1gTHnQXcLoEmyVk6PMNiTgR3Kl9exxKntCnKlpiCxD31qMFzkX9LnChMcOGddssYKQYo0Mk-k8-icDJi-9P-XcZyz7JFIkzb-GrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=RtLg969Z1pnC__gaYU-9kMbARXoNKOoz1F1aPmmn5EeAFyO-1Dhmaeg37EKsLPWCcZ2SWkGRZ0UAG7ZXnz8o4y7h7USC7EsfTTz-iv6KnzONuIc45cOE6ZbYBfatYIfRjXHzfIh9lVBQAJX5Wmip-m9ptTDdJWURs5I9cvYDjzfgqij8_hF6ZYhNZZ1c6BmgtwbgT6zmZi71zvLvjwTBtR7R0descoXB4igAGuT1ETzmXm5NPtIqn7yr6bgp97ws8C9wJdUi_mGM7pi6vnlG2AjTiXekzmMFAFqOIqzcTGrVH5dNwrqRBVno5t75k7k5y14Y83k_GVb7RNmZbJR5mB2MwvXkYlwO3Mh-jdxWATfh5Xp275QoYY-9GXnaAi3xvQqsc1Hi281itkrDNESy7btqERArUg2dgxU96DpdNjw6EF0LDd2Fbe8vFNh94ip9RXsTUVRqnw0thO9Y0BaB6TVem3zGTfXlaJtiRGyChA30-cIAX26YVyJF0xDcCw8SZxQ0DDH4uIBPgHgvn51FUecQaVU-jhYOC5jiCSdOQe-QbhcwJvUUZQVazXje8xA1WH4eDrU1gTHnQXcLoEmyVk6PMNiTgR3Kl9exxKntCnKlpiCxD31qMFzkX9LnChMcOGddssYKQYo0Mk-k8-icDJi-9P-XcZyz7JFIkzb-GrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌فوق‌العاده زیبا از جشن فارغ التحصیلی دانشجویان رشته علوم ورزشی دانشگاه شهر اهواز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31361" target="_blank">📅 12:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31360">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31360" target="_blank">📅 12:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31359">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCFGSjjgQYPQJa30EAR1mhtxrVlK2Hm4qH_veOhEZEltw6GhgY00MmJibk3NNNqYjmIAGJbYCzOMJpTw9exggze1ZAHvLFKCHKJsNazgiu6wXTQPz6Cxdxqx2eYhYN-w1F7xYD8wxLoUnvhQhCGiaF99BvUXFiN6qzIxX6c9UaPvLMHU6Hvt-wduucil6Ql4VxAQXshcDdfl3pkY7p7FGa2l863qL2-Td_s1jPByYP06Wnbc_ryx2PvTYrmIvrFk2zTQEJm7Fb8XvrFF7mBFQWgWM77xwS-JQIICQ56Mtt-_Wj9aLTB-xDViZ20u3BKsBAoau3qmf10LWCtCDMPXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس هیات‌مدیره استقلال: با علیرضا بیرانوند هیچ مذاکره‌ای نداشتیم اما درآینده هرچیزی ممکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31359" target="_blank">📅 11:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31358">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brqjCc11o80F6rrZQnIXIRB6T7gaoDAafn4WwmaGMrGBEdWL-_gXbq37kLmAjGH3dYLoHZvbFq5b1STcUXBFPsEHPNOJ52S62iBs747BbEH-DIx6xGnQya0nPLJi4ZK2lRClZXo-o9dO-hG-AI9jUQ8Em6x_M6KcyPPW5vqF0QE897OgAlLoUT8ETShZRDIx6dgxwrIXZOUyVxd0jWNcC-VnIzoUGjDotfiZq1mqZ8VXhGddVsofKg3eDLxG_l6GA47AK0GtsvVUdt__n3cpYP7eEfA9KhLmJoZcPRaMoE7LLij6Pt77HJXKssT2I-ChAb854Dmes_-LTWMSzk8Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31358" target="_blank">📅 09:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz-R4MT0Zmdcx_0a4mmjYB08kZXyRlzUpPOJATEEcFkvI2jX1412DXcQBX-qIqDekgEBSSSHweTjfUDyZRxFPSFpwo5fsjhHZDCbCBMLOSQrdCBFrsravDy-TmA5uIP0LZpN_pjUKLVE1Ui0NCRZPwXpmyRo8TF4zCTNcrQDcxuKU05dwpoa516-f7qh_Bsyg-xS2LYWy-JZ0sQhZz3d5sCIPwoLwo_CEFFXO-asxGXS6ID6n2HbUoz-pJVNZs1GpsvX5vShiMlEhTZxenU2ruj4uryfjcP5DAVPTSeQ3CeKJZ-HktcFjSf5Yq--KYTIxEORTL9nlBpw_JapLvXJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSGVwhhNtISP6TA_Yv9saJyK00G6BDazDvV_d8YlUrEpIUd2-JCRJlpATtYEUfkCgHjWYE0ZtYxc6KiCrKhuG4tzCqVRHMI1F54p8TV7jjTaMomuOUiE3GARhlIC7LX-_Ic_WunNPoKIcXWdFXBkaRHhan0pQK2IkiCuL51s6S-p8e8B6m88a4X6I1DCzea4QMENRAN_yFqeVmAdtjRqMUkNdQ2HDERmtRZDDc0NZJV0jezNlPsu5Az5PgLF70CuXugYP7bTSBGVPrDafUmXoZS1asDF6cQy33Hgw1ItwdqjJdGbpzQ41g6B6x4FTy3L-jn5fP_q08liwTMcdm7crA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
دبل‌تماشایی‌ومحشر لیونل مسی فوق ستاره 39 ساله آرژانتینی اینترمیامی در بازی بامداد امروز این تیم در لیگ MLS؛ تعداد گل‌های لئو مسی در کل دوران‌حرفه‌ایش به 934 رسید و برای58امین بار از سوفااسکور نمره کامل 10 از 10 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31356" target="_blank">📅 09:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7APGhvw7yJUJsuFxVgs2BUvHMnhdCT9U6xhviyy4jN_VVw--Q23EKgIQoJTnThYVjWGP7ptDOSeRy2nxmd1axa3_81xaE9xqoc9ulUm5md44rDRYMEbRVCwztGOyac21g5aCbnjbiCPeMpVrJYPMHDsm5Z0Hlc3hSvl-gtkqQyjfEUDK6jne_Jxq5gDJ_a34yOsPSKWCIpCmBHBF9Z5yjIIlFnVgiSMfQXDFW24cdBO3iA9TqHevQ7AHWsPT76-_eBQERRft85Io3E_KxkqsaTKb5YC9ESX2tc10Z7Iwkl_M9JB-Ead41Oyyy6Sd_J8FmNxCjt5FTX2BstJhYT5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بارسا فلیک تو این‌فصل: 9 بازی. 0 مساوی. 0 باخت. 9 برد. 39 گل زده. میانگین 4.3 گل در هر بازی. بهترین خط حمله دنیا. صدر جدول لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31355" target="_blank">📅 09:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31353" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uARpoEdfT2TN-2vn-E8TpA7VufnDdAAXGa1ixWEzBIQnTKSgsF93D66uaYqvHWoU3w6s2fxLym-N4VBi194RdvH6oa_gyAmrrT7F_kxWyWCO61y12Fj5Ep2bjrsGngqxYNphd3hrR3nSfN_JR-qnqo3yYPAA4rJ5RipS9slYRsyY9tSQqydf5QVi7y54Jpw1a6JtbqCv7JST218y3JVva0asYpF-Zn20m3tyhn9aV4XRXdWM9tVpGbO_oTgHGUEeFd1VqmouWLR9yRzdkF3aj8mQqm_TjDYgB1PKKgviRXLaVVBnEQunx--fixk18urqZFcmQIaI1ZWtImT1A8SB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31352" target="_blank">📅 08:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8zj70A_6nWf_2HyZzCpOuwZv6ZJhYJWOln2gK_Q1Y8UgqWalr_ytOHCHNihqQVQjNipaQqgkD7Vj6VyX-VxhC6Sw5grfmuaSPzLSiNgbhROI3_A69zp4JHbTpNsMYxMXdSLyWBGBJrpprbVwv3ICC2dU3U0q9JnnehEsmtmyXL3ItvLMDmNMzSaBhMkCCdfLUV-IcewLEQf1QGO9jPI3Ru4bVVHk8OhphEK6vwWPexrWDfIqHJJM-0CQGrcCJG5Lm5ktB00btf4pBGWzwFWRsxczWcmJVuHkZShkyR5FjChT23AnElguMc7ZlnQmck1KClk3OA9a80f_GLvnsYD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد خانگی بارسلونا و رئال مادرید تا دومین تساوی بایرنی‌ها در این فصل
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31351" target="_blank">📅 08:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOw5ihv2tbZ3LRVRNlij5Afspm5NCvvJUqKXjGlg_fxeZWI74QDbEwVsPdg0SgT7qV2ZeeZ5AzTR552zdrG5rHyffjqgbI1Cbdj4dzALORQeYxwdlXO0gUHx_7HYqIRSLeRLDMordM92FTliV0U863embXRlU7vXXMbOrSO7qBFcDtwEMYWUA2grM3_6mOAdQb0zV1nmG1lswFaaLUckWjcy2hgvDH2CaShI1CvbBRTr6av12n4L0H2zJvitUOuQz9hLJA6bQvHlpov4OXRkiYS_iOR479sIp1xXrQ80Z9Og-ugWsQzXz5xdycW18pKOPymA47so0d9JrmsW4rztfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjlswvNJA08FMHvKiV2hC5W2Wwrsr--7k2BioRlrR83UYnoXIDf5bOo7yJVKEkSEzYduaiyig76MFEQUs5isIYzMlsfff39JMP0-Ms3U9k8ilzvnDT1Ntq7ul6FYX3AlPv745UpipQAs-OgINwQheg7SH5JtEChqud3-cF92YtrdpPTTxljLs-NXNqy5au2ztRtIgaE3z1jd-XPNczi1xPtHb0wyEUzoteL2LMCzEP0PiXX19GQ6hILF8d830yNZ4a1Cno9u-kN561jf5sWaR7XGjth27F3kbgZJPmDxNse-n-V6aQ1q41l27O-RHTJZC2BqxY0QoUIUWCMDzQ1evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBSl0aridxtgGJ61Tp6kpwEVRkJgKq2akRGJOAc5X_y-aSEbYi_0ly3kLNAa2w39IUHzWPHHZq_1rfPND7eskHS26Jh8J55eItITY_-hlAMUc40MKolqrVusRjHFkQfxCetJU6sImcKSlsFA58iOXi738U0YGqi7Parn68iRCv6fuD4vZuwPafKAteyEPfOUO9uqeOb1TO4Bkpp4P64MvEYTm-09ij0Sxl_tq52KaI51DtHcZ9DpovvA2vvfC7kiAunqlLlcdDR-QFJsVzBDdkzv1JJG4CaqHtKroOQ7iD_PeZgLbymRJb_REL8eJD9qJgU_pejkGl3x_QeVNNDW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEW-F1teniccTQIalmSv8yC0vYyTis3LBV_MOst-veO1pp7pio5p5XUheLVywL-XadFOTxyPRZOFUtG9aeQc1h_0QVIuKQmfvRlwiJiLdqMQOCFmnD2loEPzxjymYmgOyhGuegsKrhxD6avALF6_3bDcCYqUrs42BfCtEUf32PePNsmiRgBUX2SSx_kYVnvB0xlLXDhidQDbXTCE5jKf1pJMWBMsTiZyt0y-vp5eGMmCk_sxhAnWYzHaxD77egoM7X7hC4sO7tf3S-UZ572TMI9_RXfRUkdD9ck45z9MW2g5T-4gHBwE8GdEqlkIUQi8-7nbQ-uEaG8kphIjbQeThQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPYc5wEgA8pyr1AzLxStS_xFKdQVrcxM7-wNAXZAIcbLUqBsabVyc8gJVMTkAJ_D6d8vWQ-nmh4vxCu37zoh7hD4dppjFFOeDG-lXFDNVXv5L2z2bc-c39HyV7zHEACN3qKsROunnS265ZcfJk0PAqZeKwee1EFhr6kmf0Y6bzouGbk4qc-zbek4N1q0cDIPPwnY-43NEpZpLihiBwtIrZKS5sEXuYYQRUc0Ec9olemsyCNYLKpPAlcIs4yWzoeraFG1zDmVBLI7gzacFGom47ezjjo2--fGadF9WRaZs5oUs3IRVA6HNxucRvOdU4yYi-Eg1C5O4TmQ78dky-E1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7d_8F873D22FTR5MsjGScirmierkq-x-seShaTJCbn2y4uGif2LAF_lJ6iq5K-tAGkSok0AB88SQVcl3wEJmsUOQTssM1pHmBdi5V84nX_yz2mSuUIxuYn7_XsLX32MkMTldoh22vsSvWw71drBG48b1SA_5lrhtmYHn_aZw0Nal2MtujjKE5Kx3wl9DJrO_NCGtNfoyPXzWP_BtAzZoHGPwek7boYpZn5gHmamC-gUPbieXV8AB2MDtTeUKiYqzcRVYBFFTU61Kmxzj4y-N6QDgxC55ZHiVBe1tVBQza-TYsn2f5mZMEx0ioGQwYFsT3x2DO8cLwPep4Q-zwr5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNzj9ZOPvwWNnBoTATxzksWN0rkZe0odskkVtx4ru3i9oyf0MFRRH5PMcnCVe3TVl0Q7YkszfiuBoFaRHYO36ju3fzdF-3lQ9_cRds-PAzYr_PCbTC-zhmgiXADTCLHC62eCosTBZh7lkzIsDsrne8IjE6108tkL0f3kI13bIn_bg6aeGlgsqqLly1zcYnYCbESQmg5qfmhJLSbUcLPWzbppnboqCpHGDN8wzg2h4fJ-t6K9qUgq6wUsrH3iImnvm-YftCKz4_y3y5LBsy174kc_D--SITrdD7xULk0DM-54GUDjyt0XmGAH-Xch82-Hpy7gd5FxjADKmoxWWkmvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgfZbFlSPPs4WtAPWjgRnH6gv0UO3zk5hYg0VKxnnU2cvO6ka3N6DMZPvCzItUv1_jOBxv0NqouR5vNd0XQqfSwoCxSIpBmxJpnj1wn3MOhL2iZRRJadCNskOLEph3WG4kxteVNidxQU_MM7rwyP-AYoO3fEVBkt2K6sd4HZqz0dT6336UKO5iCb4VhuCvZ1j2FGJoDdYj5d5lrDKQVCrU0ZJlHO9Qa7lZlDKONAkmufh1jkBrxh3k_uSYXjmSQmIR5_0LsJIiMso_-C4QXLz4NgpO2-spC6fviXM44p1MfM0fdyyphP7uFVfRr-tKwH1eWK1rFEFo8nCKHWfso9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=HE9d7j71rXsBYhudouH0FfqjmCOG_EHiaoFavX-y7EJ429uciwWiZ1u0TYZdSaSZkEPOYoHDXwAOp-TFhzW2OUXGW_OOLgCnlfA9GZ7oeH1RGXwvQqsQLbcQFBFzW3zJhC0UpsvNlgRYo72G_zImQilDa5LqKwbdGgx1hjIu9PVxZgbbLwwwqkoOW9I0wKbcmLaUGOrCtCwTtt8_JU7oRN5wqkkn8ZyyaF10hLv_Bn3L5z7XB_UVrUgo1IpgpKQTanlvYjTfFYDt9-KXOzaA0uYvSU7ztE4NAUm7CTl5k43RfD-vaMgZrcw4IdhJlGdRkprSW9YDt7JVSafMaY4ctI-v4WAH59e0JvEtkGg6aO1aYencA4JnsuXkmtQg5H9BS3bhP-JVyn1AC9OR2uOOWMUWzVojP7p3mYS8BFWIm-LrAvPKrZHOgWhT3nyqiJcbzsjuRevY0i2_kCjfptqjzFcDnWQr5nmRPCi5Exr5sSQdY10NCYYSjaNsD3w5H7_1Em9DX6jW6lJxy_jTv1bP3ozeT9XZkD7mN7fqepG-lYK2ZiJi6Bsw3CmVsuBkApa9kYLb2QKqjD7lcEkxj43E2fQd_a2dw2_mVGugpHkddJWflniWMGQcTzCeNr6lBk5hjjC7GMWTKfB8XnyYryt_Y7a16V8DvRshaQnovzO08nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=HE9d7j71rXsBYhudouH0FfqjmCOG_EHiaoFavX-y7EJ429uciwWiZ1u0TYZdSaSZkEPOYoHDXwAOp-TFhzW2OUXGW_OOLgCnlfA9GZ7oeH1RGXwvQqsQLbcQFBFzW3zJhC0UpsvNlgRYo72G_zImQilDa5LqKwbdGgx1hjIu9PVxZgbbLwwwqkoOW9I0wKbcmLaUGOrCtCwTtt8_JU7oRN5wqkkn8ZyyaF10hLv_Bn3L5z7XB_UVrUgo1IpgpKQTanlvYjTfFYDt9-KXOzaA0uYvSU7ztE4NAUm7CTl5k43RfD-vaMgZrcw4IdhJlGdRkprSW9YDt7JVSafMaY4ctI-v4WAH59e0JvEtkGg6aO1aYencA4JnsuXkmtQg5H9BS3bhP-JVyn1AC9OR2uOOWMUWzVojP7p3mYS8BFWIm-LrAvPKrZHOgWhT3nyqiJcbzsjuRevY0i2_kCjfptqjzFcDnWQr5nmRPCi5Exr5sSQdY10NCYYSjaNsD3w5H7_1Em9DX6jW6lJxy_jTv1bP3ozeT9XZkD7mN7fqepG-lYK2ZiJi6Bsw3CmVsuBkApa9kYLb2QKqjD7lcEkxj43E2fQd_a2dw2_mVGugpHkddJWflniWMGQcTzCeNr6lBk5hjjC7GMWTKfB8XnyYryt_Y7a16V8DvRshaQnovzO08nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sb18aoKLwRH_WIY_mPjqOTl7DmEQhB3gy4HDkFX925itDjNxDk_8zY-l81EVJkco5PgAEdZu70WK9uobZBWy6HjVsRzz4dbHX9SswJ3Wv9jbT7z-QzStgf5LX2OWD5DRUIK6o4Tu5swWXLwZdtSWw3ReGfRoiNqHolGRR8XcHbcg8Fh35vdHknoYs4H3cFsFcZiXEEphZgveKlnND5mbCb30dfAv6uHJl4nvFgnnMEe0Epc-OHIv3lI7tqdfx70QmyZ5RkCWJvp8G8UQ9K1QXTAlxdfUxkEHu3Thl1v3sN77cWMgCV8AAcgdKRKt0Y4LHC0mDALIWi8MDc5ZOWBGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PefgGrqE9DDBvQzwiAigKUF28ZNjnkJQfUGbkXabUIQXLQd3gFaCDW_sCJSTBAKEoTwA82Y1sMoIJFlwvnf3pNCW82MYXTE3aDufCVAMz_yHausIw_-YKXSlkSt6FG6K6532b4iNXJwU7Do-_l6xDyem2KeOX5kyq5TBReVQ4zx1K2sGv5pg41kUvgSV5GeDzr7s9Ia98dEXhxlhM4txdTgenq_cmgAIyDbLxsOed3gNdssNjfKM931uoDbIoqD6olMw8u_fKpNoeM6RJRq6RFrsUoSvFeFsIZFZ5gH57zxOo8-hAlzti7SCLoaQ-DzwgGJ_RbhxmKWXvVaKSOayrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OP627deA5ieN48QV9a5hhw5TG0ozQHGyD6MT0mO6qWG3TePJzVcYsuPHHBraK4xTN6Jd-JxASRkHE-sjWdqpTfn-Bf4jonOxS9-Q4028uVnGuOAg1iFJXKGNpFHBMKe47VJyfgjoBK60066U47TLZMUm0e06j2-5vMeoliy_5_9SzlVPln3rKY26sQcVehTwNbzEnz3z6tBflEe8rt_nDQvDweldjxATIUz6RDaZwYQYJ9D-Qtm2xPIiXpzpx3Dvoe1EIFa9FO2pu27xCjRkoXLLP2dgJTEiYl90ywX8Rvym6lF_UwvWg4pjcdHr6u7mlEox-IMZe-ByXcBJ2Z5R7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHQPWTULFMB_mHw2q5zI_WEVPvFRvqFbHTVYrygqB_KpILH5HI6bEzIaWUtv07GDbo04SkVMjAri3XhFHrhp5NHoBpjywGT17Nx4L-e2DUmuNPh44jjcdmEsg9BMPdZ9eX11fcsrWbaHcz53Bo4BybDwcFAKXZa4w-QhWJ_49jZFsUR6e4j85X9ljoKC5Kw2mUTCw-Gx0nVSou8UGFApWKZt762YE8VqltSMVmKw_zcq4m_7wDVu4LiSpQtlW8eImz_x5u3PFzEY69z5TP7GS1RxfZd0kkU9TkAO4YtyzCXgUD9Y4cHETwX5yrCqYgro0mVP4MQfspp-aHhDkP44nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuNtpUim5SjmtoCZ3ZmJ8Ra-6FSfDQ1jNbgPdtZ_W6i4kbvRFCLf-zWptlgtnt-HIWAffLQi_RRnDOUaEaYBRQJCBD8j10WOQE0taCqm873PjfQQkWouxv5Mjp4S-9NVKFXQ4h_t5sE7umCVIJgIhpxvnBlYr91jLiwg8JiHLdwtIffeXFnO8ptYzSrxmbVgZhsyz_OVAAzgvYKfgGjsryWTRK2qESj0ClvJlaKM2Mh2yrgbpbNaBmBiK0244fU5lKAV8hMuXwmjIBw5AkLKaEqv8Uq1tjAI2gVRatv9ic9ErMOcbcgV8HU7VIDxblgX3VqFU5qClEahT5QIwhuXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbE-9VscMOCcIWt0ICIo95X2V2I6tSg_WBxyAjl5zIuh2q5_G64uPdCvhmIGm6-t4pp0ZXrfqf3MWAXPHOuRYep7Va_UKiZNkaI_7ToictIs_OafmvEPq8LjsAVHMwOSgkTRaeaK6Q5IoJslLhJaScJzWd3zjqZuCWnhS8yjcy9uL-bIlfDr5RW4cMZQUuAuRG32spRFO62QrnXfpRnBVEFw60uDsU1GuH-aHYjEWaNBHbV-kkN8-SmTRd0sHJep_3lqaP5nX6EwYmEIeUFZQQEYm376QrBYBgGsTGxs9Le8xGUkRUsGEI-wEDmSrqPqARJuam15xc4bCb0x4wBirw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=jCal7mt4qv_PNno7pgFu0ax7x_bBcH4UHiPd9FMaQB_0-kAJWnIrpWeIbnOvCAUd6RMrsLNc_T0o7j5qp2ftO-WsFaeY7_iSNp3uByPY_2H08gL9faE8KwBuWSz3UUJIysy6Ongwxp23ukiURPMpL8UuIp3xjryiCPse8cWidVmRRWfW9-6S9uavYUnjOpuAc-We8efmEVWAd171B0ug_gbjLfcDABTelwRDprDyh6WLdd1aOs7DNnjXWGZ1MWbqTg3CxxQf5qj4wwyQKHAhsUXUpEvUOOSlN9xZZwwMcyxV8KbBvFYim4xqYwNlEQ9to8G0hbzE6ghRO4gwjIH05AqfGRdrBVHUtZvEcmHDC_JTynkSWlrc-WlMTVPL46IeRrrALVAkH0aBOWsX_S2QAEdirDcIK5eJk4Yn8O2HXP8bqmchxQ3ttWzylEOAJuPf0tIrE5dORCT-aUfYC08vNpGYa2TlPj53_Jtj-XYj_CWRosmqv3Nli5hIyhY4MMgxmc1E9BTgQneAVetnYyGTLBFrkcFW8rhP_HdlXtM-ufHyOqDtJsNvLCz-UnOn6jXlswHLS1lBRq46Y0gzzTGcNhOUcJuaWtJCWlA99ykA3mdnup9B6EbXki2F06S0MxlhOJfVrv1hVFiBdjxIWbrrRcOijulQsbxWIJ6_aARpgtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=jCal7mt4qv_PNno7pgFu0ax7x_bBcH4UHiPd9FMaQB_0-kAJWnIrpWeIbnOvCAUd6RMrsLNc_T0o7j5qp2ftO-WsFaeY7_iSNp3uByPY_2H08gL9faE8KwBuWSz3UUJIysy6Ongwxp23ukiURPMpL8UuIp3xjryiCPse8cWidVmRRWfW9-6S9uavYUnjOpuAc-We8efmEVWAd171B0ug_gbjLfcDABTelwRDprDyh6WLdd1aOs7DNnjXWGZ1MWbqTg3CxxQf5qj4wwyQKHAhsUXUpEvUOOSlN9xZZwwMcyxV8KbBvFYim4xqYwNlEQ9to8G0hbzE6ghRO4gwjIH05AqfGRdrBVHUtZvEcmHDC_JTynkSWlrc-WlMTVPL46IeRrrALVAkH0aBOWsX_S2QAEdirDcIK5eJk4Yn8O2HXP8bqmchxQ3ttWzylEOAJuPf0tIrE5dORCT-aUfYC08vNpGYa2TlPj53_Jtj-XYj_CWRosmqv3Nli5hIyhY4MMgxmc1E9BTgQneAVetnYyGTLBFrkcFW8rhP_HdlXtM-ufHyOqDtJsNvLCz-UnOn6jXlswHLS1lBRq46Y0gzzTGcNhOUcJuaWtJCWlA99ykA3mdnup9B6EbXki2F06S0MxlhOJfVrv1hVFiBdjxIWbrrRcOijulQsbxWIJ6_aARpgtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31331" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO6-ZVM86NeTKvkD6vgrttx-M_Ww8YFVFl-BSgf131R7denm3ksmRUgDEc5g7-hbjdp37Moe56xWV2xdW3aBMsTYNeCC46_f0dVexydMP1P1wh3K3_A61ytyAd3xbXd9MhfdbIEbbVhZzrCdEyzNjY1MbwJZomqtR9-av_Uszq9vfJPNa4_DQjs4Wsph8jhwYZ-fVNLsXQo8uGeYaLYpIonJsbltJWL3hnUuC1WuOejgDeNY0QOrLiDSoHNo99Orj5DiZ3uOdvBvmdXPWrZ7oMREW-74UdpRqFfZ4_q8dsf3VnDPZCRXH0SXKvnychoDeo_L6ZSZYmpS8QArQL4UWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YR6GX3f5z42UGAY93qehaYttFXrAtbBby7iNB4JFLYLPb9YGi3VM79435gAAvV6yJA3YXm_CygadGxn_oBQQWeGWeoGm4o4lRzmQxt3H41kUn6GY4BI44qSaOfGwfD_IMe4K0T31nJWb4bTSvhfGVDM6oXHGLmmTtfL6BNI8TeUPKk-O1aCKLROC4ywNb66dczsFyfssjCRXbjR9nnNc2dpFLYJRfL6sNYAkTUffHNHCmkuSwXnDH9059AuYcdA4BXMAM2klQee-AHMi2WA7yTZJScyVhHwaqNBtjUSDA912zApVppByiDQfDNT6o4UgJkz1U1kEK7AuOFlRy_HEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6kw7T75zGyR7oZ0aJmiCHpNFe9j8ajc-b9vEY15dff7XtONrA6WeUswKKsj0yRHC336XWVsZ91FvkTYJ9TP4DFvAgzWrTAzo4DsqCkbvy_NyiGBFwX8u_xVU7fmT2z4aDIkBRH4ifrYktrexcVXNxGCnjWww9A3bBSFpzL-PpEdBSm42NGoUF5GoVG3seCPD5rBR0pQOyOJSJsxLOHjiiTacHsxU899oGkJm90D0jZC_sSMswm5tecy06G2fu0opCSvMnD6E7zyrYhBNzCc2ykjKJe2KX9UGT2kqwBfGaF1uq-qGNsxsskBhlpvSyqxrG0yxcjk9BYfgMkT-a1p_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGZx19T0BIgRvpK6kVlH333ahpUjcVWKJA1iHZU5YZGB1yuY1MV3zcvZemWNRJCia_rUPiJS4eMCvHToMsX987Q7K_9ra0msN2lhG4yBAk_kZuo6fyGzDFfKYkB73JoivF4S1TF38XP6S8tiBLhXV_QoiO2Dkxtf2KEMbRAjigdK9PxjWswVCPchz6fBIEdX1TnZC_U7uV30B1wYurxdTB4OvRwahzM8YeirKpDxjHKohW1LAA136V7GHeiirrrINwNNQjVsKxvuOPgntjVsTrWKzw-6wstN32bXLkE11Kdnez0VgqdPy6vjrC2F8IxtV8a7WhJLUCkTCAbX6TbfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boSyyyAvClwp4tmNHY9iECUIpZqV8MZI0CPo579scytndAx95jQxh-x2XvpSquqAeLc49kJbtQc5ZTkpOHVQ6sdvUzoDvVBJU98CibquioWVT2Ibk4vQ9-Vy_lqxbzjdcXsO1EADn1rsy46zkhrEC9p6iUnaCqO1Kf4JLi41XUVFglMntXSKiTXu73Db2akz435VyKaGGzdlevfFy8LQVu7IXP-MFpVjIwPj4DnyL3dE5UHBa2ElpLT-oy8n8gmUeRYOUDwPaiWp55KyzRORtkGDbVmUDB8GGKnItteljuX9C5GyRgsKtooF1am3UtaBFFrA_R0L5q18NjiOlGmOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOpl3WKDOUXLSlNFLDz4YfiCTMC_RGoy_fF_xAWWzJuCE6DIqP_Z1Ub8GsYnkfyKt5IBO-p0FJRDqCJf33lp9EYLM_a6PgTdmndyZP2lymAB1P6t9f_MIp054vZ9Iq1FGPy7fKqV4o0QFsgVBlTJaDBPqCxh5nnbwzs7JqGrkAjQHvNDHX0mW4Oy-oarimp_FUT8jn7MYtrhQN49RRbvT_G3MwRz_kadnszAr9D_Mp3E9qzcoRmBiv3EXI_pJ5UbUxpB7RYxxbwbE6F6_VMhn7sByCj_fnDzPjfI1m_HqXyh58xj3vXLPyANM2zLDrSLzCpA8PGHszrqXOT3apwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=h8HYw9b8-pFOuvYCGDjzyWW1BSXuxu3DHFs1jOvNhhOg7i_x_bGx4vDz6l2lirQ6H5IH6dc1ikTQRSCaHYUjxe9y5_OckuYXYq6gaGAEsMUYpryIBkbcQHz3rBkciGP5EP4IdO36Ew5oijUQQ3DNojOFoxnvzseGknC22rKa2BlzZN41kzf7iiliAGUhtv3HgMV1op_IVyBRkIIcazuB8boj9OrW2290Arn-3PIMpJiexo4l1qTxDDRhNWTkjNwmtJ5tnI-SSxz2N-ANjRlAySRuUlxfDwYsGdYcaWz4nRMXd4wRregwcoh4l5kO4NPMJPbMMuIQU_dzko5hFLGRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=h8HYw9b8-pFOuvYCGDjzyWW1BSXuxu3DHFs1jOvNhhOg7i_x_bGx4vDz6l2lirQ6H5IH6dc1ikTQRSCaHYUjxe9y5_OckuYXYq6gaGAEsMUYpryIBkbcQHz3rBkciGP5EP4IdO36Ew5oijUQQ3DNojOFoxnvzseGknC22rKa2BlzZN41kzf7iiliAGUhtv3HgMV1op_IVyBRkIIcazuB8boj9OrW2290Arn-3PIMpJiexo4l1qTxDDRhNWTkjNwmtJ5tnI-SSxz2N-ANjRlAySRuUlxfDwYsGdYcaWz4nRMXd4wRregwcoh4l5kO4NPMJPbMMuIQU_dzko5hFLGRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiyguPnSvMQBp1sOl7QYh1eDRtFfqzbZZ4_VRZ2_6XzByQeQAgMObTE6C_1wJykQePyxww4Mf-N9Ps7GXSu0OiMWzmyE7X3X6JnvN3Qle9-KdUfQfwkOB4QgSod9XrvcYRUvJ5cOTn3NvB-u4BuCnYZ83ks3G6mCpln4r1PEg5RkE2rDXRf8SJ_EmgC5Ae6cttqznPGkWi7yugRNMz7zS-MAQn3bUlulCBQ4Do2UYk0gj2F6lVeusCJ9l-iDik5byfaDkspZiv1SnpJVpYIwn3S49l4ZOalnk6IYiEj_w3F5oKZUEMicp8-czGYL-0HLmvE3Ot4ffnDAyo2mXXbEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4fF9qbg8sUXEu5GWQVm-imxL5GcQ6lBW8ZcxC23EUzKy00Qzf03MGVrkfKG-jV4nOgJZM179uK5QWPp_7a8i3kThAUGCaUKI9oKMNn2INH_i7dlWPnzK8cA9JJa7X_BLwNJyI8cWdb7i_a6Rp0eHGmlZNfXTszroabY-dk33wvFhAO-9O4i-QeOD-hJzedpc6sIcYZwfgdUWJfurcjv8YeZWYXfrGmebFYZOlnQcrvmORU0yco6T5_QjAwo3x3NYDO8jMQUQ843_gxHPzs6-A8qYS9qEA-WmIj8OxGiGnJbzeBcI6_Vtw2TOnKJh5SmhcU-HOlcfhCnoWNZyaDAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=gFedebBb0oFEwEPjbZoB8RQcnoNet9wqPcaBe4XYv2aMPPV1pQ31kfF0fkD1Qs0-vTh1JlSkJHlMTuRZIxx4jswikIKqoCuHMo_hSO87aNPHoZIc87Z17aLS_cMwb3K3Qq6NA5z5b-ZUvZFV-h4pQAESCQXGXZC9YTArgRgH4n_cQ5rm3tsLM4eyV5WWAZX4leUJGNKTtowdaranzJHs8hmAidzNi7XnOO48RLNZpcksN5imz6xegVA0MY_hGKapgFHvpIBtJsMUjUv60F7adB1_zskIMddbiCVLEbQJIjmschAWHN8b0Q_neClAbfIPGjLjO1M1Yq54pxa3y_ZAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=gFedebBb0oFEwEPjbZoB8RQcnoNet9wqPcaBe4XYv2aMPPV1pQ31kfF0fkD1Qs0-vTh1JlSkJHlMTuRZIxx4jswikIKqoCuHMo_hSO87aNPHoZIc87Z17aLS_cMwb3K3Qq6NA5z5b-ZUvZFV-h4pQAESCQXGXZC9YTArgRgH4n_cQ5rm3tsLM4eyV5WWAZX4leUJGNKTtowdaranzJHs8hmAidzNi7XnOO48RLNZpcksN5imz6xegVA0MY_hGKapgFHvpIBtJsMUjUv60F7adB1_zskIMddbiCVLEbQJIjmschAWHN8b0Q_neClAbfIPGjLjO1M1Yq54pxa3y_ZAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
واکنش‌ابوطالب‌حسینی به صحبت‌های اخیر ساکت الهامی سرمربی سابق نساجی که گفته بود در زمان حضور دراین‌تیم در رقابت‌های لیگ برتر حدود 10 روز در زندان‌های ساری تمرین میکردند.
🤯
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=JPYmv3b_CXiCZj75HadtG4DHC8m4VVuH1MEO2sLQLdEC7I4dset0DlKH2L9Fo1RuIQyaTvtGknmxsFhnsXV6nzQpYY2naj7eZUCLjgZRkBxwpA3Kf0LUN-XxNlm1HA02_V_TYLQWiDgT6p45PQgtH2tdtjN4pkeh3gWOto6AIUpasekUbv2t9v6xR9IEkh5OphEtRUIunDuYwDlavZbq0VYoyT6kKPl417nc9ynA1RWxjmnYG9Xd9iaTaW1FjCAXM7FnvnjU5KeszbaX32tNsZ5qo_1SnWbctIVOX5gb2HXVUQ_AfaNLfAx7I-oM_DWtRI4Hb2oyNKeHGrq2_qNvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=JPYmv3b_CXiCZj75HadtG4DHC8m4VVuH1MEO2sLQLdEC7I4dset0DlKH2L9Fo1RuIQyaTvtGknmxsFhnsXV6nzQpYY2naj7eZUCLjgZRkBxwpA3Kf0LUN-XxNlm1HA02_V_TYLQWiDgT6p45PQgtH2tdtjN4pkeh3gWOto6AIUpasekUbv2t9v6xR9IEkh5OphEtRUIunDuYwDlavZbq0VYoyT6kKPl417nc9ynA1RWxjmnYG9Xd9iaTaW1FjCAXM7FnvnjU5KeszbaX32tNsZ5qo_1SnWbctIVOX5gb2HXVUQ_AfaNLfAx7I-oM_DWtRI4Hb2oyNKeHGrq2_qNvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZllbpG2GLb2s8gsUDm1zMwYy6Jq4I5k-dPuOkgLDS4EsqnHwh0SpCSoXMKcbv9CsxE7-Jc3YafgHFWICo8td48D17H_kfycpvi64IU7vy-NRcKSUNK7a5yuCr73lVvvvFSvB53hpaUb2iLUtvThj9KSCmb4GAlU43XBP78dUf2btnpTgFrQieyYcnaUBmv1TM1PK7_hb2LHYJFXzYbsOhRL_yGb4VWkF9venW0FeVSv8NQhuuyEP8oLboei9MdkbN2riR_zjZy1Ku_sdXv9aq5MHGoGNcpYbtARrMDnCNaCsHI1vlIEIJHQ3kHmx9JKATEQ-mQGgrEZ_ThNZf7ifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfW7PVuRHkItCKioSGoVZwPcPKU9gdxuRb4H2VPnzvBgzd1_y4K1_ZQxisfjjRgCwHP0c93JX9lu2r_yDm8UC6j6nHZfa30DRzEVB-fMCZWK166YarFb_Enm0qjcU6RsC87HLXKYO7WVl--QjE8YqkY9k65JZeBWNRC7bB1O5PTHib8El2veytKdBVSuFrltFspkur7_OM5Wjd7E02thW85ygwnxDHI5LYnpyZY2LKNMKSAmLIZBoG8n8bCSUWEsI0cPsSToDqgfICXf4UI3ZklDAoMbOoSbzEewBUIFsnMl59MZqzAE158iYk9n47KbIuhajovsmPV66V3UdLxNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJFQxRfzfxqwt3TEm_R0zhDgwfHOlGeCvQbmKLMoWssZw4Yemm2x9M19Fn5dCpTqeSeklwyWlM-uGpRQkUNmdOFJ0xAZHdYoqJNaWKgQiPv-Ts89lN_60hyqD-WX7N0b6cSVXRAn1_fJ6Al5xvzjkT7zNBxgf2oW2iRi7hyDCYREthmkLLUWl4UfSx_oPlCyBZa-84_epllWTNFfq8JQMyLN-xdJJwBxWkrUvo2UIq0qK4TY1eaRqLXKGgkxGkNzbPq-ljRWqyzxiOooZYhmC1zG1iFA0rieGgu3wxk7d6-u6oGNhBqi6h1Zv-Ml9WmG3e88MQE8BEyXzbM6Hb0BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzfOXtU8s6bPvrcaGM1LBBNEl9XvV1NKMVAZF2rn64b83zspdfRzp4mmjPRSQ-0Sgr6eJGATAh7XCwyFNO8V1OVcrCGLH2i4eMQ2sKAI3LwfD2-CmHiSFIOtmuV7GjFz3j6-HvWgWr1rJH01-y-Nikn4ZfBGK4r_O4LB0Ol7z9L01yzM4bxWPU_CIYYbfYNsf1SaWXgQccSwBSe9SlMZlouR_Ys6-cCxCcof7_ya1D1L4aFuveCu6stb_4dqw514dmnfJj6eWgH50N7PaMrfAdHdcHphhRg8Mews3h69MPIYSoKdyCZsvet-46zVVHuSyJJ8qa87ZUu1T96njz2GEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPkSPJ2_vKu-hTziC9f4-W1rpDRb51PHeltc37J-cWejfD3EF9P-9ri3HlkxyqcmzBfYp_oAROne3kMfVAw-0uGtHa2BWhx2lcN80BuxXP6BF7km6L2X3_MnzSYemHxkr2As9AW7HgzYp_pzm7tdL7SWw1Kr8xdFUrOtoU8c98vveM7jp-2StNs74uukgtjemuiAC8ZKO78gZ_3XHe01ozjtdO5ynNHYsjBi2RejNewcgwLDkKW3_RHd7x3TebnFjJCnIB1jmTqESHIn1-S9Lj9x9wDW00e7vN7-S259p2Z0fJ9fypLGZvg5POvnQSUuQk9WKLeVCAzzL0WdI4wLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu5zonfbqDUF8wugv-vTVsp1Li9Q4cLtyBGZHEyOM7u8K_dOcjTy6udQnA1_mn12izWQesNxBxuwaDfglOgXM8QY2gN-4zMNegZjUmvY7hDlWZlOb6DjVZnq4xlGaM8gnDurqkbXlfgrRS6Z293VB5WVw9B5J8thvFB2I-CGZNbA1_nGxgA61ovjZ6rWYIev5tAC_lYnaFQTmAj-podRJCfBUJTB1UTiRUA8henPwH300JcGKyv7fxx647m2HrcOLkALjCtqRCjowFJtbIrMs1tjxXyMLCz60RXEI44lbM86YiT94U8ftv1LSvvNZDVuAV4AwJCMWbLjXbFp0X63KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uerSx3c02RAbPnbQeumzy8cVS5PBRvF_Ynb26r9mYhlcvK5BSzLXdy7LENHozkiMeL8EG9NLdTx1mABgfGsuKj8dSEGzQinMynqmJklNYG1ST0U3Vycjjms73taZsVN3nPrenHyHHUkIubiSKJx4h9mkDeRB-X8dFGN6ykg4kKEDkmr-Z6by6W6Bz_PhzMUOb0DKBAYrq5sZq7mf_M_h7LCgic3218E-yJjmiItZ32AwA1pWWF7EoLyJXBnuVBM0uf2YAGk_GlJIFrfpLUKSNMSD5PH7WhzcYceSAi8j0TjBj78brpAfOSnkMrR0WU_7r4Kv8CE7_MOGIoi2F5zlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk-eb5678NwEyM13eeDw0XsIqxsSmT6AL30vfh5xLX__Ls8lma-jcs8aof_MSE28vOySHJM06FtZ_bPXN2HHPXC-ptCf7hW-yrP5GbVdpnEk6aSyiK5D7oKzY63Ix2HBIP47H3G7GfJHlalM6Su-El2z0wqd1k4qdZehvtsEVg2c07YBOKcIcCIj8Zn28wvjTane9zmHsUHXFdRYhRafdnUJITMpy3HxyFFrDERhPJBVdZISQpet1Gu8LB0ugYqOzO82n13tpXY5j9utOf9RLyzD7a5-UH4c-0t0If2pKsTXrf7VKYTKawdirMgn839LP685KgBFPjKaWhDeGTRLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3JQcdF4btYAEmkJ3lAg4kEdsuYs0hzu9KTsvFdcE6iFWnPCmtFZ3uy8bR4JQdGdToVZArABMM92jeJ403OwXY3LvqrT_C1bd6PNzT7F4Asp3dO7JgJwR_0rJwvpAeBqlP6DUIIAqZdY3CDgmBigk6IyTLWgXXd4uVOJwpboNh-XqBqSrLOBtLjFGjzAJvSvN5N48_im62qCt4CK6pGW3ZYUIeyJhF3tnfNeYLd2g8VeuN9wGOAiKikeEr_XksZbgI32deMWjB4u_W2mmpzReNhGR2hHrBx6u0S4AL_sLFSF-bRoTl2pQOzP7pyqo4QddbJSzj3F7gclhE3aGdBvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkCm_NTaA6XpDXKeH3Um6euNC67dR_5Q7rOTuaBagKKsW5Op_NtOFxXoQMBSkSiEO04OmapqvDcRWespfQS-QgSMATljFqu_9TBHDLh4czXebjVJQlzanYCAVk5uFfp0q9ToZcE6YFnnXtIep92vp4Rlf4ZP_68NTNIg4OAuO4lPYCn6lixNR3ydOM0reonNxRmpqN9sgtlUnJLy8OkcePqE6VqUDhYzJ02VD3oZEt9jSRn7LFV-fmgivhOmqRUIt7PzbmNjroh40Agy1BiN_1Jze-JAnN60sGNsTgQUQEHgHldVsTMpkXXkI_0YNB0PzMJjFLC1gxOtYG-xemIoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUpaY4XpyAwvo7mazKukylFsWpgvajprZ9L-ATO4M3pVd5vxNj1EzOVJgKALU5bqfYtyRfqvZR4VXO-1RJLpT73MGT6z4FDwMnWkhF4Exss7oUV4CpLpZ-QatKRzozg7gXHZiSm1QKcQZbcUUhF-F3uP7OywlRlNT0qFeXyNYhSxFD-oSOeoY38EC3NxJm8EzBjsbRZqwgqJGAeO8LQhEhozWIcBndGf1NOBvXmx2rRWDttELD8kbsAKmPlmfThw1zLpMAi5rpNVSUAcX8nmmCNtBh3Lo21jcbcEx35cElwz7M6Pi6TCgY4P8FAAIKNL0xuvqVb21e_keJB7M5IHFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln0Nws_FdH_93ujh4mj_dNlBFDXvhO4cH_7KJ3gWuR_O_W3lT-OelUx3lOKcXsL85Evk7Bo56ASiibQ4yOoW68AE965seALsFJ8AHi1j6aCwYeayhPttgeUyFsoiuBVI6JyBcJlV4xg3paGmONp3sn-J8RPdC14_TIDoSeOS1kN1ksIQWfnUVxdzLDaP6G8bFGX66S8GEauJyZuBgzNm4DhdwnUUumV6Odu-OvLxthE5te_JuZRWeIMGpLRSrUbg95K__td8sjXgNSbdM2ImG61sz4Y5njvWH7bPtazcEadMlKDQIwbcST9yRxThMRsq_OFhwdbDegdBmxH2Je1Dsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-GHbmQHjaUa1tknotmdwfblgMKmkYfkZTqHdyvuWdrjA7N77Y4R3ZeK0VazNkiDP2E6bwE19kguYaU8dICP0tVWHRDCWpc4CMIRl5y1MarSPh-Soxh_AKrfOrZVrbU0foDYMvtT0h4rPGDArQr8Xpy-pXkXrfjVnPrMf7RcSm6aGhkndb1At-1X05S1uELdPlXudra8RN0D_cfjkWvOcA0T7xNq_sJIjdBomCDM7XhGBN-y8K5kGI57gMv6SVB8KSxcXJwfSjB7416kaijy49gO7u53hQbuXzZ5IJQy_j_pu-isaPHp7-UCDIP_iz_p1PH8nKWk1DGFJ00Vxv_yaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmKUtibzJ71ELZjRNd3rQJjERh4aEiCDSIkqqXcLmN5W0mvORtp0m1fXk0WwPGRcLVf9OnZhCNOh6SShGeBRc6rQ5i5lcUMfkmkVGsalyYrXjIRmhMon6RO3bLoKRRZgv0kmZARyoxLmtjW124r1CU30eKVIr5lW46an3wOABRI4_ZEJvwsPNeq9fmvzwDaodT8GXVqRjIyPr_XuqCfU4i1X33-vKBJqKAiuD3Umdwc0c04397WDRkDgzOITDQL7lvvSf1OM8bHYKrHh0GRpnFlfZHQ3T1EEjLRN2zOWGmp9dpTO9ydPbiIPhxtFhawRcmZ3rv4kmuKLlLvEVjk6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwMoGHEaaz_dG65koJBjihA9Ik34nB26zEQu-FjdcwUlOy9BJbURCDtT_s5_6Vji6nJcNif8Ow3NcHFeoGCp8Gub3xoiWVSLoRmAp8SRgacoEHeuWYMrBsNreGKosBFMY1ZrEXCDLWablSGvMzQxxMUkW0WwX-0ANLuyANPQDoE24MnFZQzMyvuocUTEt7ZVAevdv9CyHVuQhuctVyFRdDNlVX3Xh69bnRbF_-hz3c9kiF5_fMIbbmqWyl_m-D-ROPkzuec9IDD16XaKUYDi41HVaa8ZLctWUZpFQulHxEefly3CfNcGb_cBhzk8rkALF6pDWBqgQpej6rCjgT0_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYcUTmnBTng5ssu7UjOHKN4PpGQ21TxyZ184dxLuqEZAWQfVnmyRsnU0cJQ3cAQAgrXj1M4glEysx_JV3njGOizcI2Fs20YdJQIx7_ikt1jG3b4dttJJipxXlif66e5Ga_kBYEJswo6mxMoQbOp66GNhtknPHpODVh4O1ne-J-K_Q8ub_CvIKmueOpRjwBG5suJzEhw68lXVFu1L698U0gsC0JUWmHyg2tkBtb5KS10PuBofjt_nqY7R78DlYrHfr68T5tWhP7nE9cJHqJtx2mOOFNi6-HbQgcCmBBCcIlO-YxMwrX-1BFRGWH6bBR181zw-den2tONXBIqDOQ-O4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAp10R0iL1oNkcUA-6oueqBmRni7cUncnYPK4MwOwMb9Tq6f1MF3Aod81_34DCLCUgPYiS5nnntJtq5ifVoFdSNG85PCHRgG-0Z2zSy20B2mECIBWbfWVcdBbJ2G-rjQB0FgO3A20McjV2jTq-6gm5b6Gs8EQ0cjdFlMHw7pvwzMciJ0WkJtIA0Y5GNQnZ0ULFQhvMzimLqwpDOCNDoRGqfu9kAVDq3kBStloLZ74MY5xOPvIk2eI7cHQGUCrXCpeaa_g5PJgiUhhO8Q-wuhdUrc0U-xR_ufY8sjCDk69bRJ51ecOAg25KlcrlEcORO3U6m2cDsdUA9CUK0WnAfBUHNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAp10R0iL1oNkcUA-6oueqBmRni7cUncnYPK4MwOwMb9Tq6f1MF3Aod81_34DCLCUgPYiS5nnntJtq5ifVoFdSNG85PCHRgG-0Z2zSy20B2mECIBWbfWVcdBbJ2G-rjQB0FgO3A20McjV2jTq-6gm5b6Gs8EQ0cjdFlMHw7pvwzMciJ0WkJtIA0Y5GNQnZ0ULFQhvMzimLqwpDOCNDoRGqfu9kAVDq3kBStloLZ74MY5xOPvIk2eI7cHQGUCrXCpeaa_g5PJgiUhhO8Q-wuhdUrc0U-xR_ufY8sjCDk69bRJ51ecOAg25KlcrlEcORO3U6m2cDsdUA9CUK0WnAfBUHNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRJfAhRsxCgVgjqjfcn5ozCt0q0Lt3GaquDNkjn_0F3yisUCdkKy1xEmcvcFJBynaA-v-FBfIsQZo33kiF5-nhs3d38nmIW3beqYx5L-QFT2fl0PVANJV0DqGbAjnRltqddMucGY5z-YlHJ1UqD-7kVnV379udcUwpsHbU0hf8XUQMrAwR88VttrgNyOCya1VDpnNhLyd7gh3OyvwpD1MSP_FJHfs3oh5USA77T8G8K2tnmwF_M5ofpNoG74lACmUNNZZsIMxHaY5DsJ0Wfj-4u1h1X8-GazcF9wlJxdhTxcvNZIs48xxx3bNDfB5SAY9H2gVkW4wEgPGfkld6y23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3TyIiQk9YDKlXltOvM2PWFM0iX_O5EIWHH9ib-aVeJsqDcnx1o_ndUQ_hJnTdW_sYVEadNGDygQMYgND-SbK35B4ragEB9EvYKtS5VQNlQtit2ATLgYxWfbRni1lNKusFeKkKmF_X8Nah5EbRplWnrzfIHaIYGR4JatzZq_x-RRP-BM3KB-7H26jRYpvUanLgqmggKkQUWw7kTCYaOyQ6YcQ-1lCZQCBrzs5nKlkaUgb8xH9DlDUKHjOpJHAy_-ZazGAliji6xYppNVf0qWkcnNlBTO_847LTjbPsm0J1cl8MY8QsmT9aROQf4bP5es6-3HqEt6ycja5EXOYUvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVPV6dCPwaa33FX1LBWHoFohno1ml9stxyzjPPl4yopa-8xGcG0-UtCh-zYxNMnyB5-6uxqHASjYxZZtu3covELvNVAOWknjbnll1CXnXijh2bhJinxL_S7GjhXsO97PrFRg-8NYXOz_1ahVe6syURlEUyibTPU6_W5JcxiCnckU5PkMfMcIbjiOsyhBvEGRsR_4NnIW-T2XJUxxgaKyZgu_ubwqis9i8XBbvSwyW_ZSw76pnly_gCUBA8HN5s1GTNQPW7HKj453gjCdFSdIZQzMXJOIfvT0QRrs_G3_kVNa_kdhRv7U4z7f01k4x8_LSfS9EybL8qy6oqMPlQjrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opGrPhXcJapNUpx45R4LRw9gqQBG6KmbG8wK6ddciuJ39XCPyblIreSDD5-9tXi5C3V1WLuIOksIfDopi5BiNb2zcro-zaFXsDiOnHEZWrryO1o0sYbcRImL8pRO5U-NjgLl0BesVRTKWibXYmJmjvq-DdW8tO0VbZ3lx3abDra2lIT_99DlxequA6g0Mt1xwh-lQ9qIZnPC9_sga2KArdhoZ4nAs_1u6nI0j-KUFI44rGXSpQqEoFDrKUSOurS9dkZjOSPHOSp-ulFKxv-BqVLBTA8Yl8msg1IYIudLXvJCD5bPQdM-QHB-pLhHGnGuFJibIpqSjwUd84PLPCyD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLz550NyN4gwsG19nilQY6eooQZxmhfOIZ1-1JxY-8fSL7yP28Y3wOhXiXi6C5PvtA4klQdBq1PzTEdce83k_7JU0x0SOHJjLjU79DxbRFUMBFmfaIfvBvN-jemNkRUYZhgSu2pkgcgON_H7lA7B4rPMV1hl16jWlsXDEoF5v_Hh1juRuqE8YUt5NNsIB6_qp8l9ZUc4wuqQe5OG5h5Wycyawab8aUzYGWWbe1Cjuf1PTCFBqwORf6c3DjyzxJxF7snzXtfq7O-7fCvYhmUWawF3YMKyLQnm-mAWDHZ6JBqpsLbetpR3Nhu-wdnDlYiYbgNqH32-FOFg_TMsnv5ApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSXbKJCYNGu__eMHunb9hm97l487i2rLL6kAyvahVRnnrVjxB9NDylJs-osJoX91Oq2_05IUF_E78F6MrhPfELvXElEf5qQdlT6yYQg-HSOc83dMymooZKfvbzo3aRj49qAi-lP6qFAQKH_uI0gRfzyBvvqP4cdA6_klg-pu9kDv2OJtxek7SyQp6w8uQkLsJc7kvHx0rXnzuXJ7xIwnWCFzT0bZgFG6vAVXKYYTi1l01alLQEARr1IyMZN3WKziGKVwEdGTm3kXC45BbFE7JVi6qJsPxbYk-r1_ANRT__Ug7aPKxPnOT8yIxJojaZT93M8mPOV4rYBzVeOals4loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_KFX89WamHOtoYYD57jTY2Q3hmbJbjlLaow7IQfGtvXnWrUYUz-92aMF28G1g7PsWT9tWhR5mCrYaqnLcFSgDu7gKpkjTVh4kjbGPxUVV4YtvHwSn1Ok8JpSRyi0_hOl_6Qqrp7tvf-SwNIkBUOxtQKgU7GXUWrqgk-HoKkZCFd5s-3JQ4zNnWLFGO8YJS_IyqHltuNryxjzVEPfNhwchpoW3_ui8pSP7ZOXWGMvBBFypM-q6dAxZWPRrOuQSANHYEw-wNOHLaVR-ARKkRelzpNS1kqEo259I-sAyxBX_H_6Jq8m2844-ajqQGM512v_77HKmsKAczj-fhFCK7IuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxr-lRGecdCzykRn7Voz0I_gP9R1X5_2DePTR99WWQ5AtKs3EX7YfPDQYrp2kTFrTd5WB94X5IMFRxAg6L-U7AkrTaP9EKvW2TecaCYY62KcEks2z7jK952BaxLHxZcAVK7YVdsYo6iIebulx5NRsZvgYleRI7oJl95UUkZgoeWOr0rvCsXLV-emKpkwYhrLxAsQB1tdlO-hjsIei20KZKvgI9C8y98G3ArUpUiNBA9TpVmNwWJfa4ccEIc6WLnC6vE0twoS3t-aGmgwB1thzlQGodF_wtbTKd0x3HcPW-0rWGDA_PrSobsUDJ9dtUJKY7CxHQzOTlWx7R4ddPCuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eagSFCPST5LghWMQLwpUte6HhdFO4Tks0oh9yhD-2d53medgE-5gmJggSTSd1eoTwyeDCuGKVNPq3ezvFuqNnJsOSpTg3PN1S6B_zD_NvaCSMDBCaySw9XicsWsexm9XyG9Jo0J3ZJWm7ZiSC1xMo1GUYUYtr7ffVta682ME7KQe3DMM_aeNfxnrAxT-paqPQkbV14e5FSoOv5295BGnGt42eQqfj7V217WDn5HDlHuCl9LMJO8UCoczkk5CSmgmdFfDakxcL9R6KoC_2GDoqq7kMuOVvXVE2Jfe6ine5iDDNbi6ODK_Ancqd8Lz2MIcUmHyeruY5Yh-7V_GSgUfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBF5KtT2XDTb98XmNXMyutD2NAnxcgNBRkp-6wea0rFOEwpKHbYWwoX5k6G4u89ydkUaljPjbnQsmYbEpq8PDHYVm7yRhkva11lYzvVZzt6XAYSROqRw9dV58gEbnjKKJmWcadly3mz9uaISFdeUEJ_4zJfPredbzemBalxSMRr9KeSSz1Y276U1YVKOdb8qe_cfsUeY4F_cr-_MnKzDrmiXo06q9lSclSbO367CjJD_k9IlyGXlIB2DUtcmrPyiaSRip3yx3cW-OdonDMPYqL966DeX2wqUghV3hdeeNKrc5q87uJmSxiD9NI4qQBktX6hZHXwpcY76NhYNj5F8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyWm60vMyUAgz__Mr_oOXwKk0fWK11nAChSuiaO1X-WhE44hXJAYVA4QjiUQ6ZJDjXBaxUbCYqzUXDbQwfxF58iSRsUYrVxv4BS9E7u_ud3X-6TCNTQjOLTsqVTrf2szG9zJMqrnoUA90E7YX4SFN2WRdfW7F4aGulsWo1N85JZlocxmXhU7IoprdcU-USZDIub_kTpvPFYHUGYAPWZ1Rzi-sX7s2_LINC5iKUPZltm0L54V2z5g3CYcIKDs_wyPmKW9YPkzWT9qj6ho5YzGwASrhaitQiEdA3Fvp7OjrZnXAZ2VwSLvF3-9seR77vCYNjEyZHHwL6i6YCqKRDxJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na0tDcqejceCGha9ITQS-TdRtXJ5wo26PCe7meigQpNtoEA6tKB1b2IPJ0k_KSJxi0jVsufYciuNV8SB9qD0kinaYWzJZF1DO2BcxeYYHxWrE6LdiwdM_YkGdoNXnnF6SgmfxgxTnxDE1CxavCCEuUxs-lebK8LXy-p3oUnrB50t9Efk2He5AzVaTRw2noNX9ZapM3RVnLnDYWp3KS0TaRENxJFf4ymZlZ8TjV6MdwH4icYGqxEHW8oNJCMvIr_n8A2gLuUVHZwJxoUeGHrD-78s8s0_f6TMt2L5LJZsslWCqwdpL18TPBAYDlYyU4Q2wWfllK2vhlgjQ5hYvU5Tiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1k2dLeTQ7R9D_N2yZqrH_WbLC1JilK32G0vQaQIRmf5T5XTCliT8trlRsaARZVnLiT8NCpmirTVBOxvTyuccRrdlYF4arnNnf-80RPHaDaV6au5Np81SkixxkxR--fmULj3Wz0Su8eaSOcL5snEZXFwjfcCAruLwHyXyF_mnDKlPqeP4Zj1CjKsnl-2qsUIStQwEKujpbP8Dcd3sXKJ_jmegj1_KoUTU2XHPl0PUPm-WcRX4o9O3qzJwiLCXAUemHK0DTHyGKSuNTDYnvU5mWcRDAoa3NLSDc2ft1Fz-Uw2E20QdCZrM8uAHZPrQZBXDDg-rKBgdpy3CM2gFeaX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rB1l-mVZ6c4IDBOlzPEAjSjnIYUppeSEezCEBBvdEQt1a5VCFzx4f88BYedTU0-7bo7YivyJZVGcnDmrmeAyfIAv_HRhcPr2w5mQ2myCjxKgZnSR-gCqlbVLfIknfGQ1rhmzKst-vKxFNRSEvHA23OYQlBRZtEZRjSJguPxlWLPQb8y_5U-gUKbUciT4EPyrAoc9uPC9-ajxMSPhcmFULkLhJzz4xpEFYXaW6S6qsK6YJqMfKdgnHO-XUxnhgn1OBq09TYy7JM5sm1GbFmbWymKtMocHwbCYPBhK6SBZYy5F05Gh99tgYbMJvH4H5h9C6QpIHvqr2WnAV0T-jL5B0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4RaNXLwpU8n-m_MHVcXNYDal0-IPbG1aNk6HiFBUPz-QVtnQfImeQSg8sgCZInDtvX3-ydhzMfHaaeTw2rWMX4pKpxmv0o4hBH8KT5Dh5XuuePxX9bpL5-xNvYSr-YFZpkjYniLydNdYGyB-VDyl4ZnB7nYcusDVyJwKuiE9c0_MPB2zGzr-UuyMuk-h3Zz1NfxB3bDC_dZKhG9YeLAQvLy1tdqwW8Tprz9R5XN8qFdv5nElPumwa03RtYeNxZcVJMIiGY57xwHwailJjmi-w4NgQBO_dsYaXpPWi2lwJ8E7GrRT0aDouSawle9h7F16ektCkuT_A4TAwhMPcjn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaLvuPN3URxd5uUI7Hg3R_nUIoJWVvp-Z-XwwjIKj0pi7accOGMiV_Alt4_sgANHJbpE263vqJhA03XC-n2UV0AKlus1IfS2qKsv2fc8fFyGk0hoKnsxQj-tMYwDaQYwIl80QP6bAhIDWdNaBp1WXxHCJr1JrDXZ1wEVY9JC3xaWIY1JwdBDxu3BU8JrEXsTCdihPWHnt07cOkpISmVGhWd2jKRq3EX2yPqHU4toKmC6rIo0NvxqILg9trjcOJ-qAhZRa4qgEsPZodSgjpw8aoFs6NNjrY8UTId6DeIkyPySTcUkwCGEH1INGKkQctmcWoOWSPf9tuhX940NwLevwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
