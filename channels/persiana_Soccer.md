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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 604K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 22:22:38</div>
<hr>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWG7zQne2TXr6K8oPo3GgxVmQWTgIPKaO5hP1Xf2utPRL7FT6PMz8er-iroLvgQeQWS0dkt4XvBCHXCBarDrEGfWyijJFxvupS4RlRQOvJQxHKX6BZMdci7uKPkQFzb8nxRGCq8-nA-FxGMZRlbX8DUUsDydIYoKFLQg4vIGPbbo3shDqUpMDtjOE53BwOcwcmIfx-MUf_To4WuiwWk8_nA_dCnVEItgtx87iBdsls-xTgXebvqdSh0uGqtjuZ8SL8NdyPCW7H-jn9e_Kddfd56veyRwbmtaUsHJUUCxJRoBJ4qj0IhJoTQZqxF29LFbc-6GFlHfUZefiudmVABrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWTjKH0ews5z3dQj7QMfhvoQP9Vf9BCoO3785wgvWzG0i2ggTGDBQ1GgGAps4kun1l_8uiEcDyQWKdZIMEEdoLzIJS1JMwLajEorKUaPG38L_-JNIa8Vc_4ArIQfOc5KBD0Be3XTo5_HdUwWuTB5KAGFL0zP1Q9NbuAOaGX03TvUeytXr5ua7ObKKWycU7gvtG-vgSRbR58X-QdyMn3RQZhimTjQUQ8exqjJtwM5u9DwUU-KUeaqGLa33m-t6J8gGXwYZinwsxmwepsI_H5FHGecWJRdUocAAgLkQkhzVDk3Rg06isjep_eMV67HOFh07JKvONFDyHh1XdrDvKopmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMIFOfH4Ummqqud_YBRfq0AiFDlGbA7RzWqA2MxFlK-5jDie6gokfT3VgxxLWFGyo-Hu3NZym_co3yKzoSEJa0ETLeAuEVThhCh25NpkYR85No9-v_-ycjQsmfP253qcJEtx4ytcgX9Yt-k9bfO1yM-Q09OyOH5bi7QZg2H8g0YEvMQm9Jh5dyOPO26990RzT9IGXfhokbC7rEiyZwLzkamh5HiMUr3pfcDvZxpuC6t29yJtfMbwTVLEHz9g3WZxUP9GcTeIEMWpavkOYTXUscTBmFJ8tahWrWHiYFyTyntQ0eqmIqfza2f-rMv-UE9aArM4TrCfIf_7V1tu_dQVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhrSL4OT7akFezOOV20GpJWTOFYBa3Lsrd1PrtOOYNqTmqvksoxcreEoUPLp81lFkesoQnZiLxIpKyhv01unkIldYtRFIYi_CreErjDVgetEARo94OVb5QD2geOxAkBumhYxA7Gl-53_9xFNoDlYocnk0EJPznETJn-PtnKqXBZqxCxPJExXzNJ9XdN2E3BaWK_uQkzHWlwd-4MMGT44WLVVe2fMwdy6mUyP4UfONuNEPeX3uKrwCeiAq_oUVdaTBAaefzfzBtSOiKyMMkpCmxEg20Nym4QgH2QASvpvcMltuedn4p2mkee0WTjN2X9tRn1ngCWtC4yrEjRr6BIdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ku-_dxBuhLq5DvlllfNNeARH_2Ar_-CLfZnL97Cg5GZlRiL_fE7-m-yuVe_q6c6_5lT_9N2yx8x8WfYJCfRI4MF18scL3qu67wLKoRQ_W0cNvbfwsS7cJel7NjdeGKQb9ihTEQCIZxuXByTsaup5gjqfoDyW32DzAaPv1vFiqNlm0HhwFp7FHzrBI_ZCwWFKeozFXAcCSCeJeShGgODFA7jmXUNSILioBD3pCMr6JBPls63JBseMMzSVnI6F4pzm_jf14_EJpjne_7-l3X-CFMwX_S85VgSwXqk9yZZPaJIXdX0oa_MfgpcleydbNh4NHmP2L1oSIaP_QJTYY-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvVEWFuLH8InWb6Nk7Dg2xLyqqBDz--E3jYsLff1HfDtilUdne6QfG6u2eNe0MvIYnVN0AsCOPDUQuPH_U31Tov8EZCbRRBA4nZ_jwI5d6B1y7y5AV4vST_HDNPatzTR_iya-cOlOEe1Y4tORUZKTLuZ1wDff8ck7cQu7QVY4A3jehfCVw0BjmUsQZaMCWImyXaLEQK_vCLdQqX9cQ0M9Va-jjKxENYws5day0rtGEAFzrtXsckq2FxaocMJG6ln52_qoEFiL-CIHTPxpjxItmVi8fiLjgh1WE9KyHlfeYWK6KQ3-Va7VBtU3w0hGS9FGopSPI9rlltqzmyrZUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae0WFtqXEQH8ATlgGVZTyYg8kRXyVg5paG46yY98OBTM_EHUq8RILux8Ax5YlEqKzAREJjMeOYeUgjt4JL0A8FaTL462X3DxGSksW9TZvvJQlwdbkLyV1gvld7TLVqM699tSWDhXqcVXqty95LN4id0wfbaNknecUBqutuC92IvCpWq5IeGENJjR5-fG9vSijPhkrqA9bAe7KDyDvrJ4ECwfHYFD7mqp6zS7vK49eBav7jJ28AH54WK0fgGEsS5zIuTZqeCIgIVUnh2oXg2DT9Nl8cGXCgBFq8VT-YW_a137x5FxQDCk4bluc3SxLw1SvpTy61QN_PArXO_TsGXiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqNNqJ-WfZt15tf3MARfJENv6BbL7ToEJ-0b37mMfJBDjH4bnOf2gYa2v6mOZSevLf4M583BbdyGd2OMDRWETnh3AApbMX21txyUGVnRDR4E_TR8lO_nbqlb8UlEGYWpovF77s-QKLmDItgPKsG-gIaS1t_BNwTmXpuZLniZVN7p_SanQEmrh0QERglaWtsntvA5zQZH2KHZMUn42n0OQiz-Ny9L6MmLNF1Xa7IScHd5SiJtOQYj4iysrsTER6_CTGH9-UBWXb6FmZssVT32SDwsnO0yWvLC5W8HxqJNQA2fKPmvm9d1nVAvTVm-dny8o5-qVMxWHKz6IGp7S-4aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2xnGxvkg2RWH4DocOJQ2TgifWu9ZTGlwfMPKX0MLVx6vQEYgP69OheG01D0Dd_0sDRNLY5qPIZ8gC_oIS7Z50SIT0Cs6k-P6cav9QsDtGFZ5SZ4YvEfF4L30yn37EhbgOeSlmaOl6_nlmwVLUrK_0IhCR4KnK24AC0F7Dwss4Tmp_BX7sf8Yrg3me1XSpLetb6zIzeX_srO0NaaHaITEleCKZXHBjx-LFBr-invMlxcoaEq_lYB1O1hDjwWIGRaBW5jjtUp_976JBwB47tpwyPuVZQKCgkMsIW1aXef983ApEuY_VxqWGmjrjKhCzhhlxEBtxuc7ome1zsLbV9Xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHpDm9Vh3l7igt7JojxSRt1jGy_GiyotKYxuoxmljyEpsvDHyqosun_fDlJ2OzkEqEndEHVFcWcoxgMbuE7ZzM-oCRYV12LcFuq8DtlQRy6kDSyJqieVlUKRUOPpPwODu6gbnDPBxlqC4bQjwsNDqOYjGyALxBM43u0OKbYd9yOQW4ZTj8SEHJr6AFqGWiEUwniZpdYxQns_yOIkUuZVz2gUyoOQ7YlwwlCWuie1H0MM2m2Ozad6E3hROtY0uXRsVjkUNQZ6LgwTEFSLBc63yHEPumS7hkZEKhF1mW2vIZaii_nQpS3V3f8EPS5H8cj7n45TGpWp0J2wBAXKU-GPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc8CAtxEjgo1r2AVbxYEAfLgTPe9EMnl87sBBbFck7YhS0YI67j2bFqjhayrWvsdGrcMAsWiLYc9plw3G4L-cO2lXvk0aX_DckHEs1mKHC4ZzgM3aMKvlsIJYYdPg2LvatvOp720filq50knsRcoCS9p5wSTNjUJhtFTJnGDEVmeY7OTehQGDNoFEEutH0I3osjI-_gtwpaXps6qLoW63w76o_ISwuT2CIcTbi7QEUk4CCoaVv1LE5QLlog8AeyAz2d_8s5AG_qgVUeORi0hInXAInheVYBef5W4OEKGM4MiE4TTpeVmOA2sYZOMksLukaQi77f3Vx9Vvz9obulV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQS1zVIj1VWgHvShiywc1gnpg-mvBDsF0pmSNneq1z3vNHOaQ6e90sORi90xWQRw1CGjYpLhsA2JYM9PNI67ZcOYApee5aR0wc4lKVQYC73gYIuex7fm2SM2W4Ey2KAxl7LfWD7FMWM3-mZhEitTrpuwbwALdkEIu5siLnjSvo8lfgKDqLEV_3GB4h86i3EeGt2JMixryIJq1V_8Z83FRQv93s_lfMABNAN-36cZ2yjk3G4cWoLgTMprtXEOhTio_UCvo-EtT8tlmL7G1cghFKgHUFAR0n1uxrbwiyplXLA_G8xg20n12MfBK9khi6vG0E0v_GSRSX5pAXfJ5FRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF4IFcE0RDf5RVkJtVqrXVLV_vAkeZGJhd0GqtR90uqERC-2IjX_Av2ae7DNQBPp4vAgr8DRN5gHXELHvZf3KPcShZbKupQKc3y3tum7dbTcROLc8eKh90MmiFgSiJXiWoxqaRNb4eV0F2XkQtqXpj8PuooVx-1STJW4B0do6VEGvIORP-0Igcm6z-xoSFMh06pBfJF7G43sJ2xUdPvGXhDKIvt20GNRpcVfQIVyftEii7_wDQyUaLDegqVuCCNjYnu1F212TbGGjj4p3L77_M7YbqfvXLIUz_mx3_6z5mml5S4naK3ORcqE9KZKgf-6mssr1uK-b6baWvJiXyYSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/26625" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag9Zo2borfYRA5NtMqaRY9rWREmp4xKuuF8hcEOdPrsB5Y_6aIr80R1n8jrvRFdWoyUKMfvmF43edJpk0JThM2SdbUtgiAyPiKY93ZgSbTUQBiuDpKbzIPshtCDRA4kPwMEGmJmHr2VUugEM7qpp1fdbxMOrwhy7Zykcx-lSeaHd0SKoUuhOLecgF_CCTNThylW3n8Ycos95saHy2JAlGz9syCAOHlyTsVlCC__Bes77Ea8xVVMqyEoKVrtqI5H5Z3izD2jI5j55wKPsLt9XxiqpVQCtFX1XZ_IinG2uQ9bFu6sK2ZJbnqVQbGuxcLrYVaEiyZjk_m4ZReWImThoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAPTjzae1IcCUl3Nj17IXKk25bvtUCb4w9MgUlleUSfk4Rin6cq_d7gR_yXKXHgWythCPL8xWaSbV9nSbnrIusQ2a05_0Rq0rJ4zXCcCd9gg1w03Vzwu93-W4Ehim1yg6AxCKqiDCpFnLpVZMvlGMwHzvvXh3v9Vx5O2CBCLjz16QobdcXLKjxcaQSI2QLTz_H_wS87qtBhphULIxtR6Ha8KuD3jDjLYHfuI6wYlqZ-fKTXoCYdGophxXJSkvww1YIdNBFrdM8_QJvbfjk_HbubaduTyCs_zNJZrbTF6kwmaDQ1k5Cs-ufvAUYjDDRS5bX3EajiakJhfO7EVifQNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1o0hkAGDlKcjGAjm4TJQcHCS9hR92cbuCECoJOJf1t7vhO8DnCh2Jm1CJap7ZLihllT3Jqdz_8kKtD-jcOo4my1pCjeUASuV7KpFALFnOE0h3f3n5BvecH6haxmv21yZtiI0qpaz8NIW2S0PXWgn6GEwkvepLobI2K-Su--upDXZalSn8OWSO2c4NlMLh2WKWRpwULNT7aZtZcnrhg1gjYG0wGq7DZZX86hKxDTDLEbfImZB5JfTOx9KIHnwaoXGy5eVu4hkF0lknYl8-2I5AQdYDqMx5BDSCMVcLOhdJP167qM35MJFS6liSET2PMrU0feRDBMXhk-ld_dvS6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HevWY4EdI9t1ofsfo5QwqlGIKpVyMQ4jZAKpcy7z1ZyV96jqo9bMPYl4SF1vPp3ca0KUSRYrXnxaWvNUvRAEHY46UYeqYpcr66FGPQ7NreeIlzEC8IQ97ZoREafENzoUQ97DKmbGCWVFN35fb9CsyVEEvSW3jjDHMW9NeC6-CI1IMDsGAXFn6GjVBBPZlXpnLCF54G4vBBfu2Z4CwVl-fAhN60eHuNeE-z7jc5Ztx1WzHMTrR75Y8CP7zTIzvaeA7gGVF_qtCfNqXhNBhh4_f98bmwD1WkNbYhTAjqDjVmKVgH_TeOO4URwUCtAFWN-L5mocBV9k03LG2TNvYQTlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6KoovFOQEwCzSzAtGqxkUhlvPADPxmeQ9Wa7tWo-Hi4arAJJr9nuwsC4z9kwTY7_Hy1w2uyD9UtJMnoaNPaNK6DWOT3pIQbsMbAjDOQLJMTo7r5-TevWZjHFqI-fDzoZ-P5r6YeiiXe3x_ofVULOCo4_l0a8AQvwyd9r44PC0170xU7m1TzR_0YIPC2-vgp3pCtWpPMWSDv6CL6KLO_mMgTNjMRJy6FdNATVQyyQ9A5jhRn3q4bEjC_Dj5m7y3iSmIqnIxlJlhFa6l8ftHZrq3oY5e9uhsUQRMcjHE_MzBonw82TMx0vtIm9hUm_5jPJZeuvPaxOWi0iUzQZFGfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m47grzWkPYPft66UbBbhMSNMu5BLZ-z25hGx12uk-9P5h6BIjb32GeU7btvBwkVG8lArgKPjlt2tYFAtkUbFF82Nt9a2yylzN43hyl4Zm5f50boy-1wFLY29KVia1G_zWjSW4aDDuGrnOYxaj14D6cUhFo_AkIzbxDY1r2c4942uQJgNKoZfW6p64whlrYB3HYZFIz3y-R1gzqbkaeXHS6WRdGi9LIORVEF83Pe07O57JnuoGZ_FTXVdJkPXdgvkmh0qVJ21ggd1WSobJggBxZP0kR7II1sxu3enGKvxcuKlRYj2sdTENINwR2u3L-2CA_JzTPw-Qxi3Hn0O28aEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3C65bpnQDvO2-8yghxpTZiAJLu2-JFtuWIncY4a3B87lJUl4c5ZUbiqnpOq35XpSy37Lz9Pr_Bh-3VnOD93DEBPzGMbevNDqdu0caUaQKpfRanzaXHQ0sqh-xaN7tn9cUzvjNjYTQy1tplEn-2wt0o_4X0wWB9YZmeQV9j1B_ibdft97IVuZUhsxT-BtdowNlp0--9ctfO2Yv8Tsc0u7WjKoTaUaLtqMxD7e4fORtPkGelBA2P5Z-wfKQnDYlcCqCCcja9i-7OehE2nuzFCahrYMxymRLN2zvWU0sUGzGFokBM9ALyJEA412tR7rHFYsDw3xkw8vkxy2aD2dWgzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6C032dX3A0m8V2t0N0P5ar5YJwkR8pjwYMXH3TADPq_KmuDWKYwWZbEwJK3zhSPGdahwJyTMMAQd5aNFgVfzcj9Ylo9HnvwnEWwdVaUSNap2JHE-UfkSIJGeHZXr-JhYsLLWc-0n6EvJCtovFnFvCWeUap78RWfZy18qChEnACEZjn8Ddi8YucRutN-E_HkJT-hs2oieGV2tZW0PocFqpQ8UTxpByaMJxyj3LRMpk4T79Si32aZmuRlpdLzP8jkm2i7rOff-A4lPQdGUrd45ojN2wYkyZiQPL3ryrmVHrP5HNNKOQo2we3IHazlaug2nQbLPY1Aa79lTkbHuHwTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5EDdSDYeyp5EC80AZoqMCsmjVwNcgPvkt6QH4tKi7By1FSpTsE9PyfDUOPQKWZbX0hyXewYhYD57W5Y4rXPyEjTULY3uKg-gc2PkXijHjTq8GWMxEqfEvjYHMggxP1QDSBY3K0rn9U9Yo5jDm4NxUZGMl0-JCaX0soN5hYE0FZiZ64MB9vA6LajzFedplyJbdGmHfTbv-J0Qt0PW5EzoCcH9RuknE7D04q8eq7_X0MeD_3ukShVVE7JNW6zzSQvS84hIk8Nbjn5POEm1JeTP_ElpsLanKFmW0tJubh6uJGMdTTnQlFF5O9XGdCJOp0ZQSac0Lx730oJtUm4F_-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ORqeEggHrIJXkj-0TWGRl23g_CKcjx2nXuFHA0v_4e01Q3racpbrxaEEkjhOuG-sOUk9VzbmvEXPWvVall66JRKZc8Zzx_bqRxMlfSOudZZp3mIqHK1e5bgG9RLuaR67LQ47n7vPIUeA12MYmdYZhMdJruB6xjscaoGd2N02KkyBVGmXyFwXrsymnJupJwm9zMLI02_LaII_j-fF-0EF3GdX8ucrD49wXdENZ5aTXNvYYxWEtaqnx5hbncKtOQmx_G2ptEpXJrFF5TrO8NkwbhSgpcCiKZefhqyUl9PznojkmN8R0hiJPc0syrqZg-j7TB8miz0mDm3OC_p9VfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJWwgR8EJolmuAlDRWREtAk3BK_mRhyUTzMTgFdkThE9_gKngU43qBHMKrj-0zyjyWd6ftCLlJX3aHWIVHf5-DbVAC4YzZThgDpu2yQI_psHXQjlRd6CmpwEC8HFfZvvuCmCqCskBGFniyUvTTtjpAcugJPyZXpR9X9azl7wzuAa8s0qdtA7voy-ch7huM-Oalwi7KoNgmB60rp9rmu1pGik4N6bK_PiyK5TPYIQF3CkxnfNf9D5ExrYgeL8icWF_rxhbeagDchPrnQw5l44iLvTjQnY6vXFHenPVRyqao0ca8Ug9jXx4O-ORdoIUjuOtB-Nk9kB7rHhYJc-grItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esrgE2-IfiZhg-XvHPQbyBqfbQwRVrffh6PgP2k1eOekn6D770b8jtRzxZW_VUZsxMHuhEMCw3lxq3PNQXlonDYyesfzeAdJhk-rjyTTmC7le5adBDqubVRfDU35f90SRX6cBGEOY2WWb6boWlao3LhN009AXh-XfmB4PbhcwdnCDEasUQSEPA2szCLcgJxgnIjVN2NLKOT3vNfbPXLHz0gUmB_XzhwIMao7BOGy9jjd5gf7nO51PBH_gEEDoR9nVgEsEt4nC6wa-PS6pvvbFhDpvTpkGQHAdCst4Q5XW26wtuPs0WadTjpqBb8L1ij4LdCbLDjVsbHkYijJv2OOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwkTNWfCjXt2ccv_AAkJUhF963HyogEzS-Gh6aKoPtc8b9S_19SoBa7xgYGFFItBk5qXMzGbMH3xJnZhB73VV4Q4s6qoRwijYqtt-HRy91W-023jliBCu7XS1bVcUedWexKYeqQRZ9RZKz8r1emLX-7fbQi7gfV0_SUC7Ad_JKDfhqVnXOcZ8Q00qcpNbI-k7vvw5B4J6t1jjlCDpH3eFp_Kh-U5dUcbhfALsIXO-YGGCFOhbnZlfvFou2N1_TTuUnGqd6KGD1IxVrmVet-YTNrmiBFH4QzkKaqu_VGv5GuiQ-oWF0M1RoASRcyljtYfRM47w6PTp2TPL9qalO_03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmG6wYVxSR2htEfFgNP8cxVYLAcAaj4yu-JuG0qrQe4xdTAhzPMgGh7MNCyFGRM9A4NR8pJeuVKKTKV2RTksdX9vcY6JJKcen6g-XKwCCO5e-G97pSfRye_c_NBgDBv2-E_Bw4pccOBuvo5v-mbEwID6UGcMe0t6--PjyhYSIonhQbk_TZftVKVHpDPEj5ySlmywj2-BqHKYy_L1dJ02a-awNEpvRAWe1wy71EyxUcBo2GbWgVA20eVxub4Re33MazgFTql4q374IEANa149TMKcykwgLMufk9mECoonhdfoJ6bdNCpV0Kxh3l88F3RIXJd9ehSRP-SnYXIZRz_9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4u3hrE-OMlRXPWZSYScVWsgO07VkLeZ6UpKUau2NVDZIXNKo8Jtvij8kjmciRnj0UWwSzSGORgxaKT6e2s8bV2rhX_tr_FtvgvOEXyJA0ZIIwF9P8eIc94LdCxyglIOpftjrz2Um9srG0a87Hppc2Sr2inYFf-ftwOwFTRpegVcZRqIQOe-CBC6pUSVe2kdQJkUG-Mw2AFLLd5hv5oyBuW_IDLsXDNxVCWcKnNWdgri3DcUTOaSI6SRRuAluCJoRanshxAjU6Il1qYSAq8kNpa-IwLGD3TEk6yHd4kowW1a9aSpKBXOl3gORO8SqQsWmmS6mXt9xu4ajVzSN5ULvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op0_QB1M1MW-jYAnNwRtWFdZ3NrVU8vtd8-Hv4Yx2utANCNjlS8_bNVwcL_5cSpItwPYMsCwUAwpbLFPekN1zRWciQbz2IEwYK2sVO71Vz5IFurcN14njASgGipfqNOmRGLkbUYK06jT2JA-3B7WQh1OVQM21uNFXtIpc9WxItkCz67Hp-S5HdkjVeq-6M9Hl7Qb6oMkmi9bOhjapIcQyKG9JZ4TSRPzns_REIG6LaFoP_BfYyd7nhJ1I7S-mVmyFoBKNOnn85DnCNZPmXKaMOPQghwPvsfkXogtNokjJSnCecTAq7r9_4Qj6Eaov8IeRd_V7o0gIti9AQwvqz7UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhL7amLJ1lvI_1mzGBDcvHwVF-L_CigGowdnKXA2iB8k7-yj8NK8OB5bgsS7gjfFvZy1eTSXg1l0blAw7k1zftrQd47_QzB4t_DoyCL-snH5APMxFxdBoaF_zr0kZnMwYO7W2hHnQyijlEqQkVEe4xaYBS9a6H6i58x7lZRvgKhOQ23J1K9r3PU_IK3wny8aJMpkohlHg0QJsLBiDlELwH2pBGqHgvx3qQT3XrSL_ZYgXPY9EVtuEASKpKzGvkIhjbXkKSRc2-qGk_EPxvk5e4YctDfkRXpZK3iLixqzoXrAx5367j_mzAerNj8NdKJWR3dQijGybrYc9PDXsJG16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfWbxd5Jpjy4cXY3Jl5rEc8siEmeYnwGLWL4GdbophzwNVtCKUybhhGv963IhhtiE5oTWm8Jmt6aMAu_xxGsjQH9dx6JTAEel4sLgJWKjn9tKprL1mAHyvS0Fy-YWkfgj6AYHChAg8XV-6ADaBeOa4Dg9ddNVa9I2wLY2MA8hje-4GBjiZPM58oT24KxQ8EOXXm-cm7aHTOD-XdEBeO58ns3DoJjw7_D5QdsxU9KteRHC_5TeVSsFWc2Mmn-Z9SmKDZc3nyAdtY_6Ydqv3EFhVPPSy_fv2qoM1xd9B2N-7XPje6vfGfnCSqtDjoQpabFrpfauU6Eppmet-aVooh9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jfor7dh7YiENEq4GfCZbtvIjv8EHFH8EWCX57uWHDigRD7pJBHiY2guy7EvO95cY5HqAp4mm5btL1Z-cyOrSDN52jQK_8m3Gao_P2K7w_eK2YJEZjaC00ITOcGbW2wXFoydVx3vfyQgsuj8XclO9GCFzsylmuagZelBWBp8liFOErz_Kxt3rkeqcnC2I7cnkrtUjdYGMjrxRVk3UG_0TkJaAnF3d7tStApQWtHAiEhWxqTti3U1e2gcQwaUXJUJU0I2CiNLapzNIwsn4D4CpWZQfUHkAD1YUOibyA9Wuhn8cctnmqDCtiD2rJnCmOix7d_ITt9Y7J6m16dUvZkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLJq2QsWI-7ASYu3QAifBVtfc_W6gc1ArF4C6trmOtYIGjSvxmBqBE0sUFGmqPfJXT9RJZaFX2WsoYoQmN0zPrHvQnwcssGSnBPYYhGcp_4526uUt3WxYWXac1KjQNXZxzEn6ifBksc5wN4Ky7OtExEo7uhhVZ-AfcjCLomnz8q1hJ76Pv8DY1bRnoSojqtrfk7h2G5ZekoU8oZzdT5bbyFo-TO6mdq10GFyQBbba2kQaZka_NGIbRU5lwuupihCa5eIYf_oS2Om-6M3qA4YyeY37T8rtoVP_GHhUNqpw5dIykugeh3BU6JT-j_NmmHCkBhA7S8SyB7KLk9hAHjrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLXHisLts73Dc6cMQnrOpMqb6yUQ1Y16A8NHWfmx3b6g4kziikAlE8mzYNTtck721SGuZjFndLb3GWemhD9OTiEWpILJ2WtT2YYMdNWamc91cq-wFmY_7YYVJZ426kf2cfs5-XI1F3NcbtIJF9wF5SZ7caYCf72LCn2K_4TK2phh24tGNAvkgJsYOmIZeaBkG0feFafYysK_cZ0fu4Np_cCl9chMcDJwL-zjaGgZNp10u6MwCjAkjj9Hb4niwioeEfUNUPUz2z0hwuyZEuELHGt-j0LQblgSWDGb_6BRQK9qzjJTAt7SPJXee_-0fGmkINaq06RytG6_rC2CvuVzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26598" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRGFiju7CblIhMu-sOJqUPd_A6AWP_3hPkPup7y0Yr2w9eldUX4gHy4CsDxuNdoZqC-XkkoRk9FNslkL0v510wjlBZmoyxCZUF8xZcJoE-wzDmm25MukvdKwHOxMnNbw3O_piGhk8T2-ymkK6PWV3QiK0RVTQ4cErijHlzae9R_p744H-qskbqIxseeh2cvHNGmxInTDANnN4Vc9XBKRlki895n40bvqSYGYPnGLPSIhyvE3mGkhVFDFXYYsMcVBh9xLSw0ufmJBkg-GjC9YqoMsYBRw2QkIY1_jFv5vj2fjG1gWwRaA0onaXTVql2S62j_vxOu1OAvVUM8ULzAalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=ODMdA1xhyXFGRe2-qNXyfo1h0jDkFi_mSb4fkrs5ymLVzHZOG4E52BJfpYU0GoAQgzA2jd81u4ICeoGJY6XVKzsu74Q92oUAhr0ksZwCH-zaLam6mRHQbPdLSa3mlFFfYQ_7A5XDbxccrVzNkHCMiH4Zd53PKP5LKFU8dHqBGUbcZJlo8BQ2VpoLQ66wLVVwZlucE6CnKABNIBsAJLeGHbupETuyx7ZY1HI2ku2yM7lAB3-VZIg7lfwlSxagetxFK_ATpYjUfStx45lnDOecCzJclgwuhbbeRrrjgxmYdr20z-3Bh0L89biXBImvczfSaVIMy8DxzvSvvn1hwxd5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=ODMdA1xhyXFGRe2-qNXyfo1h0jDkFi_mSb4fkrs5ymLVzHZOG4E52BJfpYU0GoAQgzA2jd81u4ICeoGJY6XVKzsu74Q92oUAhr0ksZwCH-zaLam6mRHQbPdLSa3mlFFfYQ_7A5XDbxccrVzNkHCMiH4Zd53PKP5LKFU8dHqBGUbcZJlo8BQ2VpoLQ66wLVVwZlucE6CnKABNIBsAJLeGHbupETuyx7ZY1HI2ku2yM7lAB3-VZIg7lfwlSxagetxFK_ATpYjUfStx45lnDOecCzJclgwuhbbeRrrjgxmYdr20z-3Bh0L89biXBImvczfSaVIMy8DxzvSvvn1hwxd5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE_Kga1oPA-6Bk3hf5tDyGJOcKN8A-EPh_Q004APJOjhY5gXsrUuTSYDjU2wSIAJRX-wspUfn9JFi0eB_-ipPhHCQXmnFw99y1cuRI-KV_8m32wjXT3pxG_vFzfrFTO2lJ5kvO0Q3wpwUE8vJqpcO7pdSVsfQxKymo7iMG4CxBg3i2qW6TJkvWwF265Ou-2rGqswGV_aqrqORvqzuU5W3ZFB3HpWduxPun1Av8pRWVa5Dyt79yLt3xvPWXvRTS-Nz_I0OXjzCVR-HV1Ca-RUH6E1nCpoH4T0QeuXaMaOLnAPEi5fJa_obRcHx2Gz3zDDD9bcCEMT03SK7BQQf2b56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNzb5BaNi37MqkpfcFqUqJxxuwvQ8xRmyjJVn5IAz11J-5kBagrmfUNU8KYimqg5KDUI3yjaBz0WedHS2waS5Jo7jcayTbY2yqIC3bJCWnDgFD2xPdpPisXb-QAIVFMA6-pK6TCS2CuhNMaa1gTLGQ8QYRepxskfmlxUx7EIYNq9IWDB21cT8__Hc4rjrVf5cJDET57tEvreAnRykTsjAztQYLQ5k6qhchvTBhee2mNBo9s8dBrioY_13OllQh9qSGwLxLjbUrkczfIJhdVAIA9e11KrSp7Y_RLDfbwZpZUA78QHhtCHt99X4Wcuud1IxOZHrT172jUj2s-RCC6rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIr-_G1HKjyHabJnlc4DKmVb06eTyXGsb6RTH0roASYCxH_SI1fbwWAyMyDd5qKg4iMtu0_urEKcDTt8TCqewOuD1_3KfOsv-KmoP_kOXiNMwCAs7XIfoS3f3qJ3Pgz4ZOl_jTS-lmA12b523qHYcYNHSnoaMgeijF3hVKGVaBzO6MwjpbjEybn2F-ttwP99PivuRF7-ype91qU35lEDux7UjC6cvYXu684Wa3_rlfpq42LYPDHselWA8Sod-ydjfBYAKVyt_bMMGvrjaHnLkWXOPm_SroBmKKApo8CIgWCGSa075CiQlG-ihiK3rZXYqbO1i9-CoDDjMT0CICx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFXJjXJQtT1n1Xvh1N9GKTvA10VMpd1GXDLLJw-UU-afr3fwZWk68jEvdiBwBPZ8ImtroLTgH1ISfwHBwsdkd4_4e8eYXaVT140aO9CHUeIqBS7BD_nJIyUe1DNoMYQsjshJljjZPqCVbP1opeYuMzQkyoFjG9n-48-8HvJFzQJIcwdF9W73zufaYNv3jZsDbiQOlljPQPno_G5Odby-t4DICfcEO58MEZbICFzCsvVOtha3CEwkbb6IsUXbVcg2R6HifYRKn2SNqFqQliLKckoC-GRrqYAPQmMNhLBxCSdErllDjZWjfaI5LzLkNOk6btO-0xS1lvEgnVCOnm9dcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIB67Z9OyTovz7hx9yKpkp7mjp1roK_faHVYUX7G_ttNynjmSYs5orUNhykRpDjJlwojzvBYJEqdc1fAGFplb7vq1jElGKMJuod5AUGY0tSh_ErcpwxIhUVotYJHECypd0R60-fih6JbCS-2Ii-TOhv_m86rR376wUc2iYYG9gp-wT_Z3t4kEFbuDuCLxh4uVRQqYo8cQ-8n1sbzQMMUeeQqAKCMdvmd_mX5m4rV5YS2BkmM9SnVUsQ1ufH_6FiUKf27_CSaQ1f8ZsKgZ4RHVdlrBZN0dcaqkNKUobIrkPuN7rV4a5czpc-YFC7JFz3-MiR-Jb3o_b37VkEyXBu-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqqNxGoDu9yYl4UMIPPaf5NA524HEyH1NUT7QzEumCsgUbpNqGeCFv0dnw7ZVX-nqYxaYmZQ0gwriEIjRhYGJr3VI2ENk3x_3-tzX2fUw17ilGxrwUcerccFLtH_e4_g6narXUFiAhc5i1Lroo0mydx_qlRFpTonYV5FuaQesbURU8XxuCadnvCAsMACBfEHw4Lizwh41ygE8siHwRH3xDxYWgFoScPEW2zMg2Svn4xxujMC7RKzb-Egpy_CUriToUxd7_pLGnNXdsdL7A5HWAOLDeSFAzChLBCJjN18P_VbIBhE8to6Kc-KPcYXHJTWQdXj-1xo4QWJ3N5E_nBGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlCyZvWq4A7f5zl3dXKjwjibT1VaY7fq-IIZUa2rrnMEzDjarAMv7M0h2UwF5UkOlywB1AjJe6ZB9RWI_1jJ18nuRYAB3shQW2pu9sKWYjMxCk2z11xLjG2ukLbBVCvgX3Nn8GybxKKZUs95U5Guqciarw_yhocs8lZ0HnYAQ1rofbqc_-YeVk1MSnSBfHQlLDYvQ-WRim8w0CB0Ig1HLdk-CrAAe-AFBa96giqk6_554M-jokmesigAv9N_NdV-8u6OSkuc0UEeQR7hM9iuOu7LvFUg3mUestL1MzPk9Xs012OXbHTBNfhwWVRwEU7FMyV5unHxlYIDwIF0Y0_VcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=Uney7bGw43_Wza6UvZu3bEsED16I54JW2GMdADg3kvKvgvcarNP627Rvmqq_pbfVnfIDlggY0KXWHSiO4BKUc8rZsba0-R9S44uBpIKqoKm_2hDrhh9qesLLh9FPOCMD0phvtZRvZtqfy7bppbEGxvwq7iJzS3-yHVo-ooe0oEV2rqeMSfa8Uff-JhE2xgIr_8DcIL0PQCNVwyXXSs0DqNFHPxMCM3vsCoZbUM7fgk47yxVb6v5zL1ebbpob0NnMB07I-TnV-YUCchVSIXvOODqALTo_K4VXdkgvUEWbO_48UV9yxLlJL5mXcHXJNeEZqXro_BpHwRTw97AA0AKg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=Uney7bGw43_Wza6UvZu3bEsED16I54JW2GMdADg3kvKvgvcarNP627Rvmqq_pbfVnfIDlggY0KXWHSiO4BKUc8rZsba0-R9S44uBpIKqoKm_2hDrhh9qesLLh9FPOCMD0phvtZRvZtqfy7bppbEGxvwq7iJzS3-yHVo-ooe0oEV2rqeMSfa8Uff-JhE2xgIr_8DcIL0PQCNVwyXXSs0DqNFHPxMCM3vsCoZbUM7fgk47yxVb6v5zL1ebbpob0NnMB07I-TnV-YUCchVSIXvOODqALTo_K4VXdkgvUEWbO_48UV9yxLlJL5mXcHXJNeEZqXro_BpHwRTw97AA0AKg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIkjzBLuWfkNoGEhrdUM_9KVtztOcYrDo6nh0PIvYYKB17kj9XNrxh4y3vaC-sUJbOLhRpHJFtYHd9-KpgH6fytOOj77tqQgbUWSyLQ6vMyWVWtCPYEuvipBq9oduGrP5hVX3o6TJSH1fpQsF9d6Uz9rCM9NyUjyW8BOxJSbx93vslblGqKi6PTEfESZsNYlYbh9BVI8wSY7p2-LccHJ4i-mzmnBY-2unKyk3QjKFyueE--yWop2nx7XliqBk1EAYWq27F8jUWllPcFrrFHucuh0ENcBNVZuXFAli59D1Kq94gQSsMkWj2HA93FkHQAb7VEozWYYr5FbpvCTUGoqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAApBguPSNPkByoQgQSHzNqBMPS1rmqRTvAghSsR1ElNlvn6F-KpCzaWLzgyapgGBpwid_F1PU65zKhl3UKLt2yJicgAsvqZsRA8wjvvSGOSqMT7NIBv-VUrryy-sXwmLN2ziOxwA3trai2Gj_855IQ9ykLiJFHKMrkv0u_3Wuds0L-GBuRTHpO9V1TZx1uQoYwn3RgFDmkWy-gM2f5eAeVTVJQl3iIDIi-2vZQb2jjV-g2r5FTMqz74Pd_WpOpWiT4gMf7v8N7AwpcU45WF8BHnQiZvOtjMUO7Z0vw34EUPgWUne0bbIz-_S2Bl202IVSH-XGxmOmv4EpYgxilYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gn4slbkAMH1r51wmtOGecOo1LGpuy8WxeoRMjQ7xAxe-xT8KTZmtPrsC8yGh9BUpWf3o6E-SVAzO_rCVF1tLAU6HpMWBYIIT0-ssMSF4FcCLHdTuEnFR2z3XhV9eILaqITR_vM6h6uisnMhqHQPck_587WylRoiVgKVgN6AWNOB8SXAhT9wixugdkIXfOKgH4kaZpiNaSRgPkbvhl8hJm6FlQNkMM45vz5L5wu9YEwOvKUWjYAdyaW84Y8HyMDo4mG2CfCf3xdMam8K2LqKsqsEBBBzdLwcsOc63m8LKPNyNBYxC6UnEv70NJsNTpBVOz1zVdCg2joM1M1hw5XHM2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-vFg8GlLNNenkMFERvFHJP_gXROJPV1kazeTXy9No_VLY9AhQS8P5YBoJBJ0myDNoXjuK-saapejG-AxeG5MjHejL-SWsM7JMCQpi37edBwUCugbQa0btAMjk6slQdwXyCTm_IynSC5WlbTI6nHkgsCQdOpSFZlwDMNwWJCwWc8YI7HYKGWrFFCkXc-dWN_AZDEeCXxX02evPtyQgzcH0mlEWnS4H17TPPgwW4T_ANW370dkb5ye_fr0RGQfGdKToLUwJax456IydKOleeZ8xztUeWkPu4xRXIOXebF_i7BhNcvIC5HOLSs4DrPj7cpJh7FgDslxNcc99vfomybgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXLWU7HW5OFzRRF8KuFAVLDGSo5eG2KJlsjQ65gFBb-Yu-elGuC5H37on0V_zBaC1s1Eed4CPYcOLBd6E82BoqPGpK2confccYd2RbhhQY7ECSnceI5jqaumL02k3eeAfI1rFKQV6-HA63lMqhcV0BYg9KMb_jvxtN35udGzrdfw0NkfcqWOX8K0sjKEmLP2ljyWGpsqzUpA_lpHuTN1Bcz4taWxGXTt97Bicd5NvMvvrcC2XJXzyKF_YJw-oA9jL2_FEHlArN2o7MmAHOjjdNrJPXDluLtwm4yUKGuVLWPoxgNnbqfPMkplFEQmbh4HSpvSj-bf9vyXQ4JXVTRVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MucWvmbXmMi5OffkfciWwNJl2Ac_Iv-8VLvmW_3JAvL9AgdMsc2EDRXYUcIgiNi7znQxm9atNzitCQByQHqAM4LwPCb_wgA0TQUXCFbHgmaE7h9xlPEm87TowbTKL2MwJOKEP2Q9YKP3SvNRrGMAMU_HVILwVNNck_7uw6OtOcN1BSRvcQiXJNp1BM1PPJsDC5qFl-fld7GeugtflJVmhnBneuFD0Ydcd43TtVxYaCvhWeGnIcqVOng5ZRtewxK4P5AQjL926KJJJDjz2gJqq6Msgnh1pKe6lblWUqz8KYu7Kn1nzOkj5MtiIAD5sV4ZRUSO1abliAfhduwigBZxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru5zDeQDAjqJmkMreacd4UBiyuvT_AHJtEAJJiNtAUCeiuuK7HxwnoEk_brQ9m02KR3PgnXnjQolIGkjtHUJRAbfFrrTHUQc5xi22ILu3AyMnApcsh4XsRFEHDZ48zZhF6nFxShP8Ajd5LrJNlfzBWsunh6-gZc1jkNLu9AkE0r2dUbJPDp744kUOxnt2KYT0quIlJ2PWrsq4CeYMiiqHHNQoHHYzd91bsdxiW_5X3XwIXQXIHGlzPxIiWaR7MCGl35n29Qn7j-h8UAPhfP1eY87W19dBqC2pDsMh_8T_TbK9SeLLI3fo1WbGw8RkBs20BzLUOPBqYNSNDEKcrJTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsGPrQz-8MvPg9-_4wY9fU7F-eLO32_pQ6ffcRI6E8qgeK6OSuiIcOMHHSUwr8OoWwCk2isLHEunfqFnCMDBjrOodlGIsKaSBnDcE4J630FpjR9ZObBKYsnov2UCCtSCjdtxf4Gkqm4F6xOrmSBS-6GStd6PaYwtq6-a9e-zdDSBVCDavE4jMeUAbkbKR40Z4zpf2Qo4wCWuu88xjbRg7FCc2tVHyVtfeJ2kKH54aYx1JdJ6z9ckir1Yttc0uW_WyxglZS5y7yAGwsvmhCN6E5ZA_tmNc_D3UY34Qyn9cTRkpnAwTWTxzDA7rY858mMhDfRszvSYQTy-sMn_hwkT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tppabMElpnF_2Y7rRLoWuqQeLcDUfte6gtDLnsxfDeeXvEScXejspHE1l4w2bZ2BypZsg4K_vJ83NpR6cBBUp5_gBf_dGcqgCTIGhGUM-fBjg0jWAuEQAlMOJCM2Y0NGSFw2waRVXXnubh_TL6PflK-nf8hNgcMNs2rAZoMB6j8gmqHb7Nkg7e_wXB6gXIbQeP17AteNDml5K4vIHrkCauoYQqOXzaJ0HaCTPpvTHTkxInxCT1molBly6ee0R2GFR-8CMb6giHRW9eKTnN9Go6PYfPkrkrgCJzIRTlNWodBRduiiJa8TZnOiYLN6QC2G0iz-WVrGTR8s1A-kDGceZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=iJMsWdI9Guf5HLzfkSTI4cMW3Mop7x5Zg5pRh3zORnzb4y_Q0na7LSuxvlBeU0R97JRd9gFHan6HzcfPc49JpATx7lRXpqtTYk3oH-BgUg-ZqRWz1xNTdwnnkyHd8IZHZE81xwhoUnXDWGyhxr0CNiWgLzXOKNUmrsC7oj4F6Z2No-eA2sZjLHM3yYrHdJHBD02iqHVLpiRFsSTyhK3CRhV8R9mwcET6SBQisuCYj3wvQIZH5vv_E_6Jw_Ly975ZD2XMp5pfi2aiyfbyCY5iAFjceAdDCHBl89Iii-ylqDqxP7c-bGlS_7NhhU_Wurab4Yqjfp3PMJxrhAJaiF173Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=iJMsWdI9Guf5HLzfkSTI4cMW3Mop7x5Zg5pRh3zORnzb4y_Q0na7LSuxvlBeU0R97JRd9gFHan6HzcfPc49JpATx7lRXpqtTYk3oH-BgUg-ZqRWz1xNTdwnnkyHd8IZHZE81xwhoUnXDWGyhxr0CNiWgLzXOKNUmrsC7oj4F6Z2No-eA2sZjLHM3yYrHdJHBD02iqHVLpiRFsSTyhK3CRhV8R9mwcET6SBQisuCYj3wvQIZH5vv_E_6Jw_Ly975ZD2XMp5pfi2aiyfbyCY5iAFjceAdDCHBl89Iii-ylqDqxP7c-bGlS_7NhhU_Wurab4Yqjfp3PMJxrhAJaiF173Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK0yQo-iBv_bEUN-VC7fsAAf_QI7auzIBbezgnT-57sLe9_EuGfkvgn2C31SLdgcT3VDpIixlUOFIbSuyHH4Imej_grRScRu1ES-23qaVYO3oNnLIIpMWn6WoQyJaqF-nk6_6JQUH1zcbTMEHbS2QpNIzmKNfHMnAQdmnI1SZyV279Y5OknQYerKF7gMwr4gYTv8lewl2aKq_hcH9W_esn09_TyIQjGrOvaY9xtb7S33yozOnKhssJoAo8TV06qKiDaoph4HoQzwp_3Ku6GUXZ3fmqZEr3dTG1Vyd_uxUeWj64pANReZbSwTsqxaGfTIeed1hwI4zdjbaPBOZ3ymng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGj03t3uSHLj_EM01E09Gb5P1pi47BQlTh7Fgyp6Y0zs8lR1crWaqOjif5-PNf7e6_UTfAnrp-deSXK8XpThqqLQtuhSKUFDpRnP4bKy7SRlizeEYAHqoaqin96aUdqooJ2vYOVNagZXZO7BswQXeWIa5N5RDzxPHsP2zkv2-UN1KFN2hxp8quLL6WjcNR3M_qoVFBFliY0zn65G2n8w9vJ8Yp2U-CFhCk99mQ_ZtV10HG4zBjCLxJZorpmbIku86QKRS0sZKpWpHiPcyfqmduoPsBqR-w8xCMBFfQth_NTjwQNTvyJLKIozQ9E-KgqJBrOpvdqI5LCR88HqCZWlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmBrR424OKVS2P7pVaZjmOEGv-i_ipQ3l_ECuOuIgKQOoJR5_sznTUrjtsD2sZMOBO89EpKLvAgB7hjz3V_qj5iMt18uDmoqEGAfesmyT7IQOa8B6gB_Bf_FATlhVLKXHUSlne3S-6jzKy9N6YmJwJ9b3_24jWqnE8ce4lCSWtVLaypfCRp3wlodye8yKyyO_FGA9dg6kFjGKketI5c4iAaJon4V4xpPuXAH5sSS-xL-LrlZ5HxnGuW17dsEP60f3-ObIrSweYdDQBPZqaagkBtkW2TZZNByfi7b5-C_ieRY6qA0ij12Zp8VzPhDp1v7lrMJauPkwbb1KXfwEJiEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbOa9oIPzXUaFTgBVPWEG6slvY-f3IXiKVroi-IJ-6YP471HatS1ZOVFHGIRWWEbJiex3-P2Jz6llz7zsfh_fLqsnUD44_JUlhySDxkk4u3y3cTIMCQwsndD5pAwGjyrdJGD1IRVVbNC9h-uSYNpY3KSraeURRn5PuNRhE7eHrmqipMA5HmHtR-FwLNKsqIK2ky64xrwz4pib6E5UD-Age6R1-914P0AbF6hjCBGTX_a_dPj9snhu8QpLCFzKFH-TNJQR8TjvQaPn_cVy-_wEM7I-RNrqdKraoS5iHLPqnj2jbkA1r_Yd0mPLVaCct5jLexhDa1ehlXC8ssXyqMBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR1BwKzfb7Aeu31bTzarKFHm7ThShI9F_gpseh0oaw0vs3Qvo54VkVJQCbeMq11MZJP3BfW-CyiZYHjzUxvLEDnzji02gGrT3YqlgqsoqBUO1L6mW1fBLjanbsZITmaB65vioH1ngkkwxBYu9H_u1lqsk9wHg6a7jAf5dqCAIwAP5tlPULg6YoCX4NiSMl47DEVbw3dIH0fswfwylOn2RERLt5zOapjNgannM80pctUedQXSVplKy0avfKnAiRjA8NUh_Ul3RZHk9-mLJjlez7JP_aqzOqDYGcAEiwVZeO44pOnoOEWrAgEVGiqqI8-eLsNX62-H_WlB50Djng1zHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X307KaIsdjJVw_eJZmJM8nhnS9lpL7ZH1-PvrBN4aGFJNhWhnAEZ0hTe3WatbmD4eZ-k02aBXcclsf6Kw-3RbQsj0PL0d6IRs3k8bie9DPPbq2l4CVdya4natmxW0lsH0cS-K9QQsJ29ggBDIitkhNWLS8SAyFpg0iOPsghHj5PK1jyqNV9J08XG_ZjIhXGn5IGtLFFVFx4yOgfJTYj5RwzqbEO4nrEcJne2wCMhRaqdika5z58-e6qYkarxqnkRMpbWpPs6GWFpx82bqdmBEZ_vYxTpPlAO2FMnrNnxjvgjdvnQt1oSkSl-h2uxzw_Ft7DfbIW5X-QBA5sQa1ymLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxumeIffzkhHHQbR7l-m-TmOQb3BB7jo9hj6Mup6RwLGj54XVjdvizXYeN9h3FlMTQWk0FOup00KYjq8hFj1sKIFzkoBFRr2CNjL8K_grYH0bBIuTmC7Pfm-mKd0xGSjrf8JnhBPXIyuog9DSS3LXrDlcTvg2P2t5p89OZlV_IZstApvytLhlh5U5IblRUKpyUe5Q8h0ZQe08C_9WE_fjaSiFAj5NPyeoW5lGzAjCdFJECkxxVbFSAM5g7e9AV7vBBC1PU2zXTacy-fJglbadrmcJ572aW96cMSMahqqQzdIOlKC9LXQ_ECAwj61IZg1n1rP-FT_dUVU2UThml_W9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV16SxLg-5x6n0veKsCrZjaYWXT1Gi8JRPWCofHmH0FKOxJQD6rZkONERUTEd6BlRWoqPQ5vagA3_nYXnBIwilPpcO9eiDwobKte40nii1uxgOMqFbI0uULT4VNm3bzVE4ouKcFJ0VP3dHnXCx2KxG-sI0zN4oVvPe-3GcX22l3kpyFAq2qSCn67VlqZEw6-57s1GvTBDaVda0nXonaNPDaqvF8YdAMa9UmeMv2nRhWYltTBrzy6EObKWV28NMR5Wjm7-cH5KIgw8Wz7pfwLwWzBNKMZfw-Z8JpOvsoLPp2UvxwVko2OTBMv_leZw0OOVFeW3BgOLBUhnjfa5666JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnBdKRV4243wSrM4dswFrcMuX56IA3lU-CLsBIieYpv51AMEfpnESY3xBk3oPRMwhPS1GY4micpBJN456kZLpx2ug1nDderiI3tQ-kKaAaPIFhVH5kYFM7g9tnu1IjqE3ujtfvHGm_oOoU8IePLTfekx53SN3FvaArimQNNQBLd0I2qnqxPm-wnRkm-VdDkkV4a4ZUJauMSHnU1CMpxjur8LMYqeiXgU2LSJzGzhtdhnLV_55x-n3mumeJgpcbgOrRIWRq-vE7jcPMIDIrKfl0mBH7nPI4Z3OIgdupLxpslnmlj5L0hPbs7qD5AcAehhRvEY9Ltk8ifmTSl_dpxFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdpsaNsphT3zMYCQibQKqsrPDxEFHUE36vt5dNuNE_FjJyST9tkSpLzqKS9CqhFRrOs12i-PZ4_ZJbM_Eo9BUGp8rNvfB0LJoRw8H6wOHlrUtu-eJJqeL9LvDyA6dPWWGXSH1EDZLCFu4_cGVECcQeDG8R6qX_SIggXLKTLPGey9Chk8JVqUyZ0mnRyGfKVx7_Nu_G5GWQiINHNjhmObGbrejqWalGIwYONKXOrVTn7Azarve_DH-VrEYI2iI2yBaFaHqR62w0DpNciYBGM1eoKNTP6xnQ-ijDxULNmJW3XalxPXB-ctolFJn__kVw7nWqP1lMZ8kiWLyUPqlUHInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=YHuVwlzuy9dZg7RHCrk5RhGZNeFkg1J1cqRErGmFnVP0kupHxArvOFYELq_yE890084hCmDUHoHWVyDkCJNNuRg9FJF_n8lslIvHrJ4zzJVk1UOLHETAMWBr-J8M4RbbjV-WyZbNOZBZCq2rjUMfwP3zVtNxa3FIaDbqeJPDV8eApCTBK3tapZiMS3o6kbjida65bQWpdr1gqYY5KzLk1jl7OeCxPN1tx5JVNw_GO6jxqs3bHjY_DYXJUUNIs3Zf_l7f7vSYaoNhbA2NiQkc0WIeUAuKtbQw30d2RZwyJqHKfJsoVMlfYTBqNp75iMroOMtpl0nuDLPqq5SIg2D6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=YHuVwlzuy9dZg7RHCrk5RhGZNeFkg1J1cqRErGmFnVP0kupHxArvOFYELq_yE890084hCmDUHoHWVyDkCJNNuRg9FJF_n8lslIvHrJ4zzJVk1UOLHETAMWBr-J8M4RbbjV-WyZbNOZBZCq2rjUMfwP3zVtNxa3FIaDbqeJPDV8eApCTBK3tapZiMS3o6kbjida65bQWpdr1gqYY5KzLk1jl7OeCxPN1tx5JVNw_GO6jxqs3bHjY_DYXJUUNIs3Zf_l7f7vSYaoNhbA2NiQkc0WIeUAuKtbQw30d2RZwyJqHKfJsoVMlfYTBqNp75iMroOMtpl0nuDLPqq5SIg2D6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnqQyqlsPYHCMDbchYDbEdjwaBZjgCeTWxO-FR46g9ocrWVld4D_herVHIadhZIJIWG5dcbhu5KnzBFl4m8uu8JWGE6_-dYcTgnA0VyBaQM64YdQZhXrb0Fo6O-iCXtkrJU9VLs0UXZuuA8okVdITHblN5U67QOolATE4qoCPVCrLoPtKVgxZOiQkQRALaj7wLM-zq0azPOsHHgXzXX9He7V8KFYdRX0d7eP-SuNgIrTVX9dB99XS9DAsl_gTSyJ-25Hnn7HPvZ8BWWsZMtHOAoFhd1ddZWEXyHXZpj2O2ihhz2BHhyFjVj4NKL7cOPdn2Y2tYA4-ldi5Oax2hmqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=teIpKE7YhGCEF9txSFBqPeTYQsqqtLpaK7h8x4Q677Zawhh3R9n8x1Qg-oYL_ZtFvIgkn0SYJspP2wIrYx9e9HBxvXuoSt1A3UXkfH41zovyDg4VPV5eEEIiQ3w60maJH1j1ICCq4Qq6j-aubXL12j5gkIzSVFxSNMAARqERkhDmWptJD5gbWOIUi-YxMm94j_UQuUnRNHv7tPRCDO85OPZ9Iq5nzQqMgpSWfwn_hHpRsrxqZa1JLksEZ0CrC6wwuE8KnIqzJ5mpiJIGwFTRLGh0w3qYA5V_6AbKtgftwdH91v6BTXSuPVCdwxY7thv9PIgt3k-iGqlvt9t4DT45hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=teIpKE7YhGCEF9txSFBqPeTYQsqqtLpaK7h8x4Q677Zawhh3R9n8x1Qg-oYL_ZtFvIgkn0SYJspP2wIrYx9e9HBxvXuoSt1A3UXkfH41zovyDg4VPV5eEEIiQ3w60maJH1j1ICCq4Qq6j-aubXL12j5gkIzSVFxSNMAARqERkhDmWptJD5gbWOIUi-YxMm94j_UQuUnRNHv7tPRCDO85OPZ9Iq5nzQqMgpSWfwn_hHpRsrxqZa1JLksEZ0CrC6wwuE8KnIqzJ5mpiJIGwFTRLGh0w3qYA5V_6AbKtgftwdH91v6BTXSuPVCdwxY7thv9PIgt3k-iGqlvt9t4DT45hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVZaRIfExHH8eeFXCewOtqDSG6-W-EizR1CH9CaYHCSm-Z3lwzTWomUeivIknvamqbbkZZHiHhPwz51J7Ho5-Wro9orsMXxK753Btzvi2B5ZDQ3yc-_z6CH-yVltEGjRifOGtO8yJydGTdKVPYfw_-w6JQqB89aBJmN9MGJWbafh-lrCbhBmTRmpnEAfkWmrtA6PoFUZqtghBZ0PoJHjoitK_BtXCnu8OcEJZ3mOZoNqRU29vzEI9R4_l7EV7J3adVDSE4Ac985ETLkwOYiGmBayqBV5bLvJqomtKqy7TdSXDXJW4ymDE4ijXEYF0oGiAXpEjH4AwimrjL1gAVbDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWPxh_5yeTif2UPlqndBEqH-CLPPlbLp215yH0500FlMD-T0HWbKGInznNl-rEHN3KDgXV_Ew69hNj_GZLYqmZpysfk-j0OW1vwC5a9Q5gM3nGqVGD9_-v73NsfwKf8NYk4ailwt5WkS-9HfyHlynGjI91usvThrwAty8jm7jbQVJc65ppQlfyYVQzxKvhrzeFTxsk8k8sqczsvbVLvEkW2nEDqk__KQSG_cTJmxyVcTXSVWLb1QkevWL3NgGZvuoPP-KT7Ar67JRyZfVJc-3ONbrBjTVJZAQgGiawU4hK7VpiJHwohYubAqCNBsLCb0Zl3iWmNKTCMe_0ZHmvRdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEHapdEL9sec_cOYY0PgD_LgRo88m7norriM0HDWRdRB9O_ZD1u50C8nipX2oMPBwX2FTJ0wwb-XlL7I1mccFKUob7E3fHrfHN5S_0fRrIgr5UTMu1Sy779aXMNiBD9sQ94AXO6GKUXD6qpMgXpN2hYAmqdXQsxuGQNTMf10Cp74IDXlVCKki9BUflG8OJYAt3y9zJKQSz-Yx9FxfaEB-AZ5d3WfLe5pYzjFUgqC_qp7pLooHRCJ66mxEqzOeENXvjbooWGJVMxtV9QcLJzZG6ewpw7wC1xEVWbScuO_IQ81272JIGANgKbYBCIho2fVw1y4J6zWpKf1WtDtPht_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJw_fsQSSCuPC9xK5oojmtHWL2-AmHv9TRkXudC3TSKQW4v8OT8RU20tYOTBlBOS5V17czK2tw-39QRjTSws_IKsK94vJr66T_rc21A7vpoTv09Hh6EFh5gtSLvCcWenwo5Kit7Hv1b651OfmUVLLg3Q1kAPOJl5c5GHjF7JxjWT9dXvpyLdMm8_ufWy5sm_BsRZfMXSybegu_qWzKRiTBSItyNSSAjOS7dv9Pyd0JEiRl_xRjROt6pBsALVAaK23bwGc293_qt5xajvTGXq2OFLSiXYfQEPlTM560sQ1okUsmvGohz6MkyDNRqI9RE8gI4XStESWT5iZNjEqcWZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTpWHsEcnhhkIhz2DFGUfVC9ryfpzxGPoP6bdCbKKPL-RTFcFrF1ojs_SRDhgs_lOsGEkU45W-0g1h2j4rhyG9zllF7G_dbff7C1m6gHO9H2yLrbAnzoZYdmapTozm10WHxVLLWxHLgG_g0Q-9hwmXOVRo9sBz5ELJTIfaOTIUEGWp83FjtiGdQys7g_utBuirD6RgOaUaOjhBP9IFVFJ_V7NKDWDToqGmYbUlQnyd4lALVPrL3dRusEZtKrUfPrBEfoMlBALoC5SL9WuNMJMxV9nQ7GQPURg38EH1rYrp51HSpitVrqDz_by8PqIq7kRbR03uf7Fy2YIpxpu-3cUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vofhkmTowedCkTlrNBAAdcrqqCpqE7VAiW8bEp1s11TkPa9sqQnNzwk6L2zsbAbJF5pOH7Edx5PUrLlPdAi17Q1AF_LdkGPCmOW2rK-E1B7-ctXK-w_IgR_Y20sl7Z_-TuxdFfY6PxCpQKLWWNb5klNoxQxwNvRbcPdpn23c5hS3nHUwKpTW4f9JkpnTulVka81YjWaZNtc2fDuyEA3plBoLUgJCRO_59qdqjAg40oTLA5TxFSyj6tabi3TCdln2nLbwEToyL3rFWpL5V21U0LWzk6ADwYhJD8HEbNOLIXty3W2E0IAW3bK0m-zI6snjHez2F4bGbo5RTMsMeE309A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=tE_vbrMa3RPTGqEdBDviTFSLXw6kHIpvk2FzWJe4YWv3XWE8pY44dbkiSenkpRgLLjQIZs4f_UQk8rUwde4LYvIDn2MDZPNG0i761XItyxaIwiWFaIV0b1tcnrgZOlPNHV7Aq_IlhnNemnNyGfLsD7pfNlJ4M_M8kTQZEwuRhHX_CduOfpaGSJCRAG6XImPCgUASsJoP41ToWgBEgRX6chGIPdzejyjQ9o5X23g2FdGNOWdBNRcA47eYoR6neFm64VY_PwgMCK1-uQwKStSkYTYp4RnJNY-3mN098Z6KtEq2eESK3CKxhVz-Io7sAgRWmqeX7bNmcV22gjG2lrQkdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=tE_vbrMa3RPTGqEdBDviTFSLXw6kHIpvk2FzWJe4YWv3XWE8pY44dbkiSenkpRgLLjQIZs4f_UQk8rUwde4LYvIDn2MDZPNG0i761XItyxaIwiWFaIV0b1tcnrgZOlPNHV7Aq_IlhnNemnNyGfLsD7pfNlJ4M_M8kTQZEwuRhHX_CduOfpaGSJCRAG6XImPCgUASsJoP41ToWgBEgRX6chGIPdzejyjQ9o5X23g2FdGNOWdBNRcA47eYoR6neFm64VY_PwgMCK1-uQwKStSkYTYp4RnJNY-3mN098Z6KtEq2eESK3CKxhVz-Io7sAgRWmqeX7bNmcV22gjG2lrQkdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=OAihTKZbRzSEgQ6Mb5x4LUHZrVUPSBaZap0wRxm5lKKTuHrN--ucDXwpblSBk7e5J9Cau8jOIQxqXf0HbNGSUM7Mv8KhOjPTvG5A5oFv9Q1GtIht7w_7V3nMtl1sYzFuZ4aVa_J06MJj3-QHHPGDtefZSwS79G0ehozsUETvh9llfevQBYv7M0tKxifMc9QoFpfS9_vLVzkqD-5Hj8cdZ49zoecwFdZXFw-Vo-jp87vfOCqr3RO5VEoHaGLFKpxiPrpe2J_ceqs6yT8cCsIAzJ0rAbWLh8yim193syh3XV1T98nCjzLItXWqCLkZD0RuXMlVV2bIYRnmQzGfNlUUJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=OAihTKZbRzSEgQ6Mb5x4LUHZrVUPSBaZap0wRxm5lKKTuHrN--ucDXwpblSBk7e5J9Cau8jOIQxqXf0HbNGSUM7Mv8KhOjPTvG5A5oFv9Q1GtIht7w_7V3nMtl1sYzFuZ4aVa_J06MJj3-QHHPGDtefZSwS79G0ehozsUETvh9llfevQBYv7M0tKxifMc9QoFpfS9_vLVzkqD-5Hj8cdZ49zoecwFdZXFw-Vo-jp87vfOCqr3RO5VEoHaGLFKpxiPrpe2J_ceqs6yT8cCsIAzJ0rAbWLh8yim193syh3XV1T98nCjzLItXWqCLkZD0RuXMlVV2bIYRnmQzGfNlUUJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBnMT5GIMHpcs0lnbvtuzVphPZevuVfzzmxnbfEYG8Kvy6TRcxMkquE8Q1KbRsPjqtB8CsaPZwYgp1gNoRSRddppFQADhOFU0U8sQ_rIZVEOclTmsYo225ki2eN123M7T5w9I-6TcNujFYgiEu-SlwxDfZkwXmrnY9V5k9NFsmxOejZEZISSGJRdwJvEaTWOKqjjCRqn_AhGaqyeUygQjzJxFyVbD9DsIpNx1YRPku8Gyfas4gT3DxiCWYWmXA9PyBDZHOrFqVdXMD66maAiyXk5ZuzzaJZegNiX841OInz8Yo-umReQnujt9eMN1vvcp77GZ5zgMNGsdMIcCR3HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=gT6_0DXNmBRQBQ5sxpf9cMd81InwKWJRkeb1AgmCq7dG0DY94ov5LsQYRTjytFFguU_f-SPQGjC-Kg1rgl5Ujc1-bR7V6y1xORJixMdmenEFreb2w31fe6drpFjXih8pUoNSK8QWtjhssL-Wfk6CAMgdHGLk9aVgr29T39IOgTfVkwUReb8FLrDVr5mW1eWmTz7-TvugAywOVeulKO9EHWstIAx3V4oxYIuHoPyXV4VWhpHg8KIOv26YYEXji09HYKBPlIlY4pfPx36RsF2Yl0lkEmqKnbcHkQeQiJqQeEWTAf8nkyeBr-TuNScLY5u1b3EUIdiJ0c2CzvB2l5ToP1EG73Y4K4-wLq9NrMPQm9YnqqgJfP4s5MsaHY1zvIEFFYf5vAUlftOiN83u6r7dU0wx8Q4LiFdDT9FsdYa51iF3HrlQx9ZKGG4ZUyFo-Nf1X2rHynlZV68K5mPdZruC3QqYbow4ppYTEF3kockN07iRMD9GANay-Dux_btOe2f_gHbd1zO1o8xr3RYv-FsDAshh954SLYjgRLZW2Auq_RS8tXgPqZiZGMc4PejsoT21vmFXFJhoL4qOLHH60V6XjII3a_s02mBMdi0B9yIELFUMHtppkmiaS0WplvyROLwdgIN5nYzmu3z1cxsNG-xe3TC2t6-eGwTLS0toWrBCd08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=gT6_0DXNmBRQBQ5sxpf9cMd81InwKWJRkeb1AgmCq7dG0DY94ov5LsQYRTjytFFguU_f-SPQGjC-Kg1rgl5Ujc1-bR7V6y1xORJixMdmenEFreb2w31fe6drpFjXih8pUoNSK8QWtjhssL-Wfk6CAMgdHGLk9aVgr29T39IOgTfVkwUReb8FLrDVr5mW1eWmTz7-TvugAywOVeulKO9EHWstIAx3V4oxYIuHoPyXV4VWhpHg8KIOv26YYEXji09HYKBPlIlY4pfPx36RsF2Yl0lkEmqKnbcHkQeQiJqQeEWTAf8nkyeBr-TuNScLY5u1b3EUIdiJ0c2CzvB2l5ToP1EG73Y4K4-wLq9NrMPQm9YnqqgJfP4s5MsaHY1zvIEFFYf5vAUlftOiN83u6r7dU0wx8Q4LiFdDT9FsdYa51iF3HrlQx9ZKGG4ZUyFo-Nf1X2rHynlZV68K5mPdZruC3QqYbow4ppYTEF3kockN07iRMD9GANay-Dux_btOe2f_gHbd1zO1o8xr3RYv-FsDAshh954SLYjgRLZW2Auq_RS8tXgPqZiZGMc4PejsoT21vmFXFJhoL4qOLHH60V6XjII3a_s02mBMdi0B9yIELFUMHtppkmiaS0WplvyROLwdgIN5nYzmu3z1cxsNG-xe3TC2t6-eGwTLS0toWrBCd08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSR_bMOiDBxsQIpXYp-icN8ezQNJpCE5U6cfNGZef3XUpCz0fxL6M3ha1ozR6kXxeRBBxCgjGZTq7b7dvUopOkHTxiAdMFPqc8YdLOcnpZd7ePKFqwn1lNt5WgG1QPAjrWUH__qIG7nHXOu3eERaRCpARkR8z1EJsiQ02LW84zn_tMerSUpfqo8NZ6HwJEdQpw9CUiqVRneCsaEHh2o1hx1nA7vs22KuPoDUBi6vd6EqBIUCaEY_TDPP_rPlk3z6nn9CtNIdEjF9vS2izaksbXXMv_76PSG6HShxNCovScvqCf2nR0makbGXBD1UHNPPmLbYYe1b9KGXmsrW5jfVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ5Ts0wUYvIMzr-9oPhL0ywNWF1XMMI3qlnOXDWRpsrZXJ-EvwaVRRP3CB9Pp4PKE_TOwgg9VIKYSYqcSKzIqQpIyyyUzXlHfULVhMjADFaRPtrxU2-jtEJlk6s0KeGShXNqYxb7IAcoV8p7szBo9sOQ9JBLZNn1WrEwJP26NxdLKtgchgRKf5z0262HTGQPOCEaBwNuQFOPcnj0lJx0mueZUYmNqONFcGVrBhcmHpSNTa6RggJTY5pBlgO6y5Z-WsZumHSZK71l6WlBgIisrFe8Hjq6Brmi3FEruat92AHXRw3oe8_k7qS4NlTilhCq1HthZnXJXbYc6fgR1Kie3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgyTWePfOxmEbhhxFBHlGPxo-tD27C-Bk8cZozpBjwdr-4cYxxUzFsiZocTGABmWDzsCKnLAjksz80dR4Wx4MNElhA5eubO-UfKlt1Y3TbdnsOziC6c9ffNeEwPyCrOs4618MnfBmLrVY-EbZPuy5eLhlz-8_XHuz6bjGaqp8G-U9FWOZzm55eOqdkn8fGT9hrj1s7ZxUjwMrZzxpmDA3w8JNG6V5FmLoLLCf0gDIcy-f0DktQYURAT-0Vb40VaG_iHGz0d5R5vtQSu5vBEGYOnmzg0_qLI57EHvrKLrZbXOIuRZBKMmTbt6n6CH3SyBBJ7mV5kmHq6RpWUz77-hAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=g9cDCPM9_LMBRTVOFOEmaVp5sUeshPsO6duWH4ZQp9dkx2orni6Sb3JMg9W2NCBB2r_BDt3Q9-QDWrQv5kagIh5OEK8gJeYlsTUWOhFWDi_1cFgdy1VS7V4wnAUNSG_bcEfuURpoBEnlovlwWSxKVAcU3I6eGR11raVRuK5qAuzzVzhzVGg4oyh-dBAfXusUlWd8lemrXsGg0eYZnfPVlUyoD5byxj0JwQwjwTtgXqUQwtTnSbO9iTnAxs-I3aSJ6igt27FSh8I2MEzZOuaDKh84iTkWzAjPTRYSIX0QGl1mUmQTNFXwieE0eaZMHvLEK6DNGVO_mVPTISAAKprIVFEZfB4mbTlFSVTGDioEEbfi3c_on7fwZnGwMOyiLFMQH7gvXDOSC-1K2meNgeJqQOrEooVJBVWv6zkT3Y7t9-rOrg2JIkWA4NWlLIgCKoytJkfik4o7gTREF-A9tBO7s2Oo4n01N-ukE29nDGW0u4Fwdh7TYToBLzJnycVUvv7xUiEgdoIFcu-kPA53v5HV_KkvkALE-Tphx7aNqcF7hNtCzOHqLgdBVYtvJi7j0sgaoKTRTNvcdqZ45iV2qALGA7cM_Us5fMZczXhOIxWrOqis8mTYhNSzhHKVoY6pHsn6XbJAWVa-qQxYBkTVP7tXD4EYf1_ErvpRvcigQcbnF1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=g9cDCPM9_LMBRTVOFOEmaVp5sUeshPsO6duWH4ZQp9dkx2orni6Sb3JMg9W2NCBB2r_BDt3Q9-QDWrQv5kagIh5OEK8gJeYlsTUWOhFWDi_1cFgdy1VS7V4wnAUNSG_bcEfuURpoBEnlovlwWSxKVAcU3I6eGR11raVRuK5qAuzzVzhzVGg4oyh-dBAfXusUlWd8lemrXsGg0eYZnfPVlUyoD5byxj0JwQwjwTtgXqUQwtTnSbO9iTnAxs-I3aSJ6igt27FSh8I2MEzZOuaDKh84iTkWzAjPTRYSIX0QGl1mUmQTNFXwieE0eaZMHvLEK6DNGVO_mVPTISAAKprIVFEZfB4mbTlFSVTGDioEEbfi3c_on7fwZnGwMOyiLFMQH7gvXDOSC-1K2meNgeJqQOrEooVJBVWv6zkT3Y7t9-rOrg2JIkWA4NWlLIgCKoytJkfik4o7gTREF-A9tBO7s2Oo4n01N-ukE29nDGW0u4Fwdh7TYToBLzJnycVUvv7xUiEgdoIFcu-kPA53v5HV_KkvkALE-Tphx7aNqcF7hNtCzOHqLgdBVYtvJi7j0sgaoKTRTNvcdqZ45iV2qALGA7cM_Us5fMZczXhOIxWrOqis8mTYhNSzhHKVoY6pHsn6XbJAWVa-qQxYBkTVP7tXD4EYf1_ErvpRvcigQcbnF1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuLFJYm8nffDnowuXQZwLA49fuD1N78uNRPahTFxPkkdLtLf-FM6qRccXJVDjaqQF5ptHewCR-UgHN2KE5YxUo0s8WwJRYtuNhln1NOrr_zgpi6iwqYjKJppeEn1MmfpkaL5S9nYSlocGQMTTszrt0ZX2GyG0bZprbphtkA8cf1jxgmyYHok_vfh_gsq5zvO276djo83DEw0gbEyLDTWo7am1rPcdYdVZquggYNwEs_MVSHSc5zE5iL2GFdd5jHQ_aK4JnLqcT8LSlPPOGNifA10Ue6kH9JYNT_OoRS8A75TCEktroX7QhHbxWpd2h7xIY58TTTgbYXxSSbvwikH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoZ3f5C35BYg3R72QpfkUYje5I-UWhyUZV_t9Em2TVYDKD94HVffgPiW62qkKJfqHX3BGmuiLCVxhSTOjjd4M9A3NqH60QVchNMyaADcPL7yrhyNDu4WONRrOVAAazdhzUobUJmduMtAHuSD4cz7A1vWHrABtBv60ZsHtDANgv4eMxrkZsompqOsTBNOj5Hb3l7AboL4HQvYDIzKbWQL4PCQKSdrP-3tRuA1k_hlGbaYND2Q9fxBiurIvNwm5Fb-b3-Lu_eoM89u3zLYvNGxmhCCEBWtEVuqLAP4XPjRhGfSr38Xx0oyMZjBj5flvzcWt_Y4JLqAEXV3xuefsaxdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBwRKp6v4rhBfGQF6-fc0Mn47k1e-bQ99sHtlo7P-ULObiOXpZBaHxNBAlT6itpL6dV0KjKOFd1DXAzw6hGYdu30Fv_wPq4sd4ZT19rcEY7LHu-YuGDOdbJZmNC0V029UGI0CUTivGjd7qUkThw57YEDDSS_0dDEb4Ne_0zQCS3nV0AcYFEpy2NFfyMfKXuHRmlyXhDaW-S2YYkCkhq3Coil0xFCn6OFz55vWPNETeH0HXJbqumdZWZbg56C2_JodDOs7TuXX1cDGbaKmcR8vOGau0vVtpJBxGpPU9ciDUFFQZO3d6WHZ10z3VnkvsvIbKpvT3XJdS5D3vptNhCSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlmIIeNpMytIVDc5fSkV_l8R0Z2s56D96_Ud7QsEfeoYPqYU18VOyAZxQoWFxVblB1VXhuf-sr1ffC75_eU2SxSl56aVvtg87DnYIyQsgIxaP5Sw0cv486-fVaGuphbB5fF1bTPZMNGVPWyqtSZuZIMG7kj7LYetZME9PGbRyLQ_iqDqpuz9xvcW1f3jcUlfaK6Wpf1PKuZom2IZ9Mgo3AbB3TfttoTxwvJs9dsj5elN7saKdMJAALRIv1AGeBVC49e9ElPg49QFn9McDjZA8qzDXNnmiiyQG5kafhl-S5J9DJ17rlsPsvny2u41Y2MUAj5H6-vC_NxTomquUocjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5AiiXCFq-qXgxQ93zzMJkMk2k_nmGzoyjOaXpPL1Nn30zbYw3r4d9X6Y92v_Yd5TfHlhzX6uvTfxYbNDydLJ-270gtIJTE3RQDjLaVQRw4rxuR4OIZElAg6jUF81sFCD1T54SJ5owlEQvDFLrXxZyhvmb8CpJMSWyxHW_IWvR0T_lmq-7IgSI09W640gIo8YpH7YnVZAxxSOWL0KAY9Dg71w190NTrfeSs-EDrQXpLBRb16DwXnkoxuPZTxG1bDRPvGF9h2hFlYB6Dj1RGtJZw9FE-o_d9Ih7Fzbns0m-r8MgzV2F_kTo2xnnQa1mUteAlZZNXTN8iAEVyErOukew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=lBWk02O9fnrMGpfq8F2IV1eSdfek4zBbjffc4h_kRsnKllKPSsjGlUf8IbI70YWqpqot-tAhObfF633N4zgXi18PK8i7-54gNouGVEfr7kRmO1-IHUDKJhI1aDdv8l_b1hvUHHkhhhDL-lE_dIKZHSYfzb-Z2ade10P8ibXLlKj4SDcJ-x1U6ApPUhR0unuVsJU-uTKpYEjV1ezD9MC8z5ne4U-rTdw9788WTOvgqURphhkdiltP3MaaC3SFvUFP7GKBPQHGOcnQDP6RgEev7u0LlBBK9Fy0HFQH34FONAodo5qwh77T1ZxbxWgOUgU6nNFm0KQEWfeMl4w5p5-DAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=lBWk02O9fnrMGpfq8F2IV1eSdfek4zBbjffc4h_kRsnKllKPSsjGlUf8IbI70YWqpqot-tAhObfF633N4zgXi18PK8i7-54gNouGVEfr7kRmO1-IHUDKJhI1aDdv8l_b1hvUHHkhhhDL-lE_dIKZHSYfzb-Z2ade10P8ibXLlKj4SDcJ-x1U6ApPUhR0unuVsJU-uTKpYEjV1ezD9MC8z5ne4U-rTdw9788WTOvgqURphhkdiltP3MaaC3SFvUFP7GKBPQHGOcnQDP6RgEev7u0LlBBK9Fy0HFQH34FONAodo5qwh77T1ZxbxWgOUgU6nNFm0KQEWfeMl4w5p5-DAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNRAXWhF6xtW5-z-Sxp_k6i4g3UjnbIXaBT9v_ECp7TpwzSTE_Ke_p_kMuQAkfRyfCJWzPE2yXIGpBqMxIJ9gPlQk65m1NkbMkfRgfz7jEPZfCZO9BU9VruAaaa35JT6yYQaDztn1jbfjdcQjktpIZ-ArwIBlmNbszvGuDPcLp8UdaA1gmEZdi5ifQxzNfk-sYfOZ8xvyIV3cduyj7LN1HsboNh5aSAUaLoF-HV3vvdBYrf2dMFEpvmtFueDzxHy4s-jPEnAAU8Wl_4NQKlpiaTATtmgeAptTy9yyOIeLoM07UqPZWucYj0NB3ge4JrKDgEEkqznZ59xFwJNQPZM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgaY-5cK0nqbrAEwg4upe0ftT2ccp70uCH_5A90TcYURAPScrkOgp56VZ4EFsfe2Qas1E5hnwJiHo0Ji_HwKNWjuIia6PJjwlCD8YcOmoCH3i5HItjb6Z_7GfjkddeW3o8EUPWRNz-yCA3Mmrs6uz_KXIjA5r-eWdHHHfOEEA_cNk8-MDrvohJr-lCJWFlf53xi5V9VX9NW8Xn3PI8DiVA2HBJ2u90oMB4Lp2-sO6l0THVfD7WKgxKZwm-YKec89gyWxkaun_sfP-PJ-6zQ_67s7wlhU_yky_I0YY35yj-4NhNNlKAgKn6ecCyB19NvfRipaQDlNo6JZfD_kFsf9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUZj9I6v_F5ymRNnqrOPNsozF72WNwuBCDciIAwKOLBCrGo-sGSPnvpWdz8ueQ_xoyqOdt5cLrass1c3lVHTYC7OAM-nQRDUeuYCJMfjfreRtrl0jG8SdOiFJ0w8bdZZizD3MXGDgyFCIiwonV63aFLluylbe6PryqLky3C608tgDK1z-txtVx0XbPmVWE0KCfcTs3RzTwXtg5VoheT2n0WKKAtJHYLJBZy54Jv26LR4oyTxaD9F6BBrLZaJtzp8iDmYMsP0Wqnp0BdfTJ7EiLSRN5u-QNt-GuLKMuq18Kq6uuGxCtcSDKlSuwSOa8ZskDaFUx4uglcw-zJd5OXeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGM1MipHzMc6N9pgVLL4eh8gXmWrIDYhPppJfXmxt_wUJ1TehZr8-MqxbajR4219bJnpQHEZhTd04jOwG1PcjUucRN5rlQwdD8rx4FgBuwk20VYp2sq-tf7IKNIbhZ-KBPhBk2Zl66tTsYNFYZMfPwcv2RRfiPT6e_CSJuNln3r6256ysZeNm53D-zu9NGSWcFXeUKu1kJ0h-LEpqj992LsqLPr51N3w_FAxH8F8uqeh9P2lCok2tROvK1cGJUnmP9aRMkeiARcRyoCF3hmuvisMpwYQ6gAypQTQaFWfLXxqUUtUgx0AQ4RbJ_jWBlOJmqGtwRefVExhIQCt_vOymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0_eXT0V_m_pcc2F8WUhvXPNl8rWREmmmDbHpXbQAKybmfjbKimfVSUVPqIm18KUXxMnVl33tEwBmg4m5yvOkK6UCFJ975u-P4Sbc2IsGzsjpnQvCsY7pVFulp6H7fDeugXpn4JzHZMDC6HHyF2uvvLYWyusYhATVVQe_8gXACOlWblwNmpUdacvhmL63UpL_q7DVKPd2R9AUpBPlu6OGO7oqBAehjyaXOeDYPKPOP5ykyDzooRm7RhGyJ-oj65CVZtDeH823D4PbiTgLNAl7ybTtSroj9_ShhBM93kQ9T2h3IXXMsPojCjay2Xu1M41rmPbNWk07hA-tgyBYXLlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=TmrHL3BV6RwCQI4OW1Tp_YmeRT_jXlO2Ku6Z0Z5cvCleRthut3vZzoO3fJ4IYkl6Ha1mWNU0ZKl4OZ6j9jvOrHnHcNfMA4n4Z83K66jnkqw21mBcFMRbtQSiSH-ZQVpRBjXaLlU4E1_5kXfHwdVOEy4b1q2QDSZxYiFs-t7IuZzfAjcbGJ6i83_xtdtPCiyjSUZG39muZWC_owFx3oCN4k8HHubwGNnKVBjia1GEfkQoxCQNdvF5tSPSy6LcuKMCdLJZaFwXiyublPqU6TEMa_Kv1-0acJvr7qjoBc4hAue7DWAorXhodClj49ZI_IHWyGY4s9ADEwlEaIZL58XU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=TmrHL3BV6RwCQI4OW1Tp_YmeRT_jXlO2Ku6Z0Z5cvCleRthut3vZzoO3fJ4IYkl6Ha1mWNU0ZKl4OZ6j9jvOrHnHcNfMA4n4Z83K66jnkqw21mBcFMRbtQSiSH-ZQVpRBjXaLlU4E1_5kXfHwdVOEy4b1q2QDSZxYiFs-t7IuZzfAjcbGJ6i83_xtdtPCiyjSUZG39muZWC_owFx3oCN4k8HHubwGNnKVBjia1GEfkQoxCQNdvF5tSPSy6LcuKMCdLJZaFwXiyublPqU6TEMa_Kv1-0acJvr7qjoBc4hAue7DWAorXhodClj49ZI_IHWyGY4s9ADEwlEaIZL58XU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
