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
<img src="https://cdn4.telesco.pe/file/rQNdqqN80ZKSCt3IXlYdWn7zfGYBrB0hq3I-H4bHCHVKAUw1aF27P1T9qfGf-v3Yf_6xZ5VfXE2hcD8bYsMPklkOgiusBDA_APl3qLQTthPVYZLa9P_QDHaQrSYBJIWw-JxgfIPJGg0oEuwtwS9LoxdgTSV5143CNRg6s2VrgBbENl3RbL8RcESBkgUK2IX3Wrgvi-CeCZkS8gPywoQOjzZoOXyhEEZRcXfmoJagDs3f1zNOAu8K-g-VaYviL1-MEHvXQjsKQF_kuZgwZI_RJURb41jyb6ZUzmTFy4X57KpeVf94NKzqaSpfSDgTKVGsMFr5SkAYb0EnT9AyZpFH5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 115K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-70803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=YJNGbJjGg0tIdBBbmjUL2i5t8Un7q8U91COyMjZCso22g76XUzVZsSTuHJNkwDNjd-miZi8mtBXb8m092qGgBeecHR7AXZD5M-_k_7W_1g9edwOERsofHxlR9a_KQKRHp2QfFcb39TqaGoNhAjxu0Zb2QpINQH4tOmWjadrRvJIlKbQFnWTNpZ1m3zx0qc8dXrLC8uZdhvv2955vXh8Q9_LpWsGlwW2gHAePHjeXG423AskRhnye7disG0xXuXUqVPpz9dhsU3wneGzTkoFGVLQcjx61RQkpu8TsSk3uc7bfZG4yybluby5FKwfbevBOaWNjGXszf60ECAzxAHhHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=YJNGbJjGg0tIdBBbmjUL2i5t8Un7q8U91COyMjZCso22g76XUzVZsSTuHJNkwDNjd-miZi8mtBXb8m092qGgBeecHR7AXZD5M-_k_7W_1g9edwOERsofHxlR9a_KQKRHp2QfFcb39TqaGoNhAjxu0Zb2QpINQH4tOmWjadrRvJIlKbQFnWTNpZ1m3zx0qc8dXrLC8uZdhvv2955vXh8Q9_LpWsGlwW2gHAePHjeXG423AskRhnye7disG0xXuXUqVPpz9dhsU3wneGzTkoFGVLQcjx61RQkpu8TsSk3uc7bfZG4yybluby5FKwfbevBOaWNjGXszf60ECAzxAHhHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حرفای وایرال شده رحمان و رحیم پایتخت درباره ازدواج :
ازدواج نباید دوقلو باشن چون ممکنه این وسط اشتباه بگیریم اونارو
آقا کاره دیگه یهو دیدی در رفت دیگه نشد جمع بکنی
سارا و نیکا هم خب اون زمان تازه بچه بودن کلا نمیشد
@News_Hut</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/news_hut/70803" target="_blank">📅 17:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=Tmm1XQB6JUKK33MEUHL_jQY4FJmt6ipfNaUi9cFPTfdCjVQSwmtIrfn_WTlAHVOXgISgV6AEPAsvxNDbJKRLRMu2wGkir9TP8P6AFr_sxkOToB1YyEmYJpiEtRJjzrhZZ0PTN3K_gt1J9it6uzObuLsBx9I3EfwFYbeRaShHUUU-XrnKyJP319OBoPec6E-ZEEnTm8uyQWIyKNNtW2geUpsOlRtylbGq_36Uib27-mP0XOzM-LAW33c7nte2S2VKpkzCigmHgGnML9HzNpRJpiKqsken7oZ_-bn_-yadqpVDECeIvLap9B30VgeWpbsLTWdc6LPrMtk11tMRQHH9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=Tmm1XQB6JUKK33MEUHL_jQY4FJmt6ipfNaUi9cFPTfdCjVQSwmtIrfn_WTlAHVOXgISgV6AEPAsvxNDbJKRLRMu2wGkir9TP8P6AFr_sxkOToB1YyEmYJpiEtRJjzrhZZ0PTN3K_gt1J9it6uzObuLsBx9I3EfwFYbeRaShHUUU-XrnKyJP319OBoPec6E-ZEEnTm8uyQWIyKNNtW2geUpsOlRtylbGq_36Uib27-mP0XOzM-LAW33c7nte2S2VKpkzCigmHgGnML9HzNpRJpiKqsken7oZ_-bn_-yadqpVDECeIvLap9B30VgeWpbsLTWdc6LPrMtk11tMRQHH9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صادق الحسینی کارشناس اقتصاد :
کیفیت بنزین رو جوری پایین آوردن که تا ۳ ماه آینده تعداد زیادی از خودروها قراره تعمیرگاه صف بکشن و موتور تعمیر کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/news_hut/70802" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=mJE1Q_VBkgSE8LmvLTpifMEZFw9-CGUC3wrC4mO_uDYtgN1KbttDahUyiz9hEa-mkCl-gIbNetM7JeYbTwoSg7Y5o4DIp9GKS4bqY7FynGQF6kHs48-wYuVGi2absq5Vt-vd2ChdQs9WHEUv47ztXgjSe9ZiQO7qPV_au_WnmBEyXI08qICTeo__CpChoeOI4NAdYS5rTpLYhbiQeoJjMlI9GBDxmeW3JUshAZT7UpPIBOgk7MHTdCujo0U7dCF58p8xwRzM7bFOGFmy7UhMrf0SWCySavmSrcFFlPmZDMnptBgAU806vED9z6_pOWJgC9r9W2jp7lPRMGb_NmDWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=mJE1Q_VBkgSE8LmvLTpifMEZFw9-CGUC3wrC4mO_uDYtgN1KbttDahUyiz9hEa-mkCl-gIbNetM7JeYbTwoSg7Y5o4DIp9GKS4bqY7FynGQF6kHs48-wYuVGi2absq5Vt-vd2ChdQs9WHEUv47ztXgjSe9ZiQO7qPV_au_WnmBEyXI08qICTeo__CpChoeOI4NAdYS5rTpLYhbiQeoJjMlI9GBDxmeW3JUshAZT7UpPIBOgk7MHTdCujo0U7dCF58p8xwRzM7bFOGFmy7UhMrf0SWCySavmSrcFFlPmZDMnptBgAU806vED9z6_pOWJgC9r9W2jp7lPRMGb_NmDWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
پایین کشیدن تصویر مجتبی خامنه‌ای در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/70801" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=n23kQk9q8b5_p-ggS6RgBhlxRmM6tAvh1VWa9YNPAzWW-vl_JIF7N0n2M-g85-LJFUIL-KE20BbsBwvJ3IG3CikHG1eC6vFiH4Bn6lob7c_1LXCKVZgwGVgBeD59my0D4j03aIDdofFeUG-gtbrBLj8oB-HRychP6UP0NcRr_NHIcAK3yotIFEUOf03kzqGDjraOXQe4IRW0-1BbU6bC01n8NOrAuJgzwFGc6GsNvfAa2esMLyNJsaTpBFDaY1CBZusv1c0NqlrRNgofWkcGMfGoAg98HMY_m6joAF3kNC7f7x3Bj2cLx-Nu1WwlOUgVo_8st52Oato3ZvdueE53aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=n23kQk9q8b5_p-ggS6RgBhlxRmM6tAvh1VWa9YNPAzWW-vl_JIF7N0n2M-g85-LJFUIL-KE20BbsBwvJ3IG3CikHG1eC6vFiH4Bn6lob7c_1LXCKVZgwGVgBeD59my0D4j03aIDdofFeUG-gtbrBLj8oB-HRychP6UP0NcRr_NHIcAK3yotIFEUOf03kzqGDjraOXQe4IRW0-1BbU6bC01n8NOrAuJgzwFGc6GsNvfAa2esMLyNJsaTpBFDaY1CBZusv1c0NqlrRNgofWkcGMfGoAg98HMY_m6joAF3kNC7f7x3Bj2cLx-Nu1WwlOUgVo_8st52Oato3ZvdueE53aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دوربین مخفی و تلاش این خانم برای اینکه جلوی خفتگیر رو بگیره خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/news_hut/70800" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=jnac81io6PCdICXbo_as17vFmG7XEIETduUzNOW0pdErUbGVj5i7vh7LG8n9iWgzwkEwbBgmR9QOQV-WuG2JVv47zaXbRBrtXVglen8mykozSO8VVwwUuh8Gcv-SWyfXisKnyffoocw0OPvyXojBuSUIMWWMp0LzZeJf5KvsgZH0yjhqc7AsjaHyfqbVm7JdPR6GSzIvmKt8HwyX0DyuM4_SN4NQHiyVrtG67SEYliYkdUbSLANgvfNT3BGaYrxxm8oQYs9TQ0wzXpeJmdaUbgpMFoOEtYUOx4sbJVNBr-swNPIk-ArgsbVmnU0me8scs66E4twTU7g24CjtivHYMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=jnac81io6PCdICXbo_as17vFmG7XEIETduUzNOW0pdErUbGVj5i7vh7LG8n9iWgzwkEwbBgmR9QOQV-WuG2JVv47zaXbRBrtXVglen8mykozSO8VVwwUuh8Gcv-SWyfXisKnyffoocw0OPvyXojBuSUIMWWMp0LzZeJf5KvsgZH0yjhqc7AsjaHyfqbVm7JdPR6GSzIvmKt8HwyX0DyuM4_SN4NQHiyVrtG67SEYliYkdUbSLANgvfNT3BGaYrxxm8oQYs9TQ0wzXpeJmdaUbgpMFoOEtYUOx4sbJVNBr-swNPIk-ArgsbVmnU0me8scs66E4twTU7g24CjtivHYMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره کسایی که میگن تحریم هیچ اثری نداره:
نمی‌دونم چی به اینا باید بگم فقط همین رو میگم که عقلم خوب چیزیه.
@News_Hut</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/news_hut/70799" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=vpz5D95RO-T5_FIskplM5NH3F6j7KtZOkOuja69WBwKxXgN3t5fCM1Oe0mbzDhECa9EJ86tnhsR1FkWldM3bOVEVvuUxDmDe8H9O3Cy3CEN7Tphrzdz8ZBWR3b1nWtnu7X_Xif-Q8eLDARM11hNz1ToraP_c5EzXJ3SZVhVjOxB0Ut_XaqvOyIy1dbf_jae3UvwPwuAM-7qwN_1RBasJ2lw1b_iUvMjqoL66mjEIfYe8efDuXg_LPael5umKXsLG8rahWRTglJ2wenyNn_TdgzgQH_bqMBArl5nPSztvYK6PnlDr-VoLpLM65RQShwTmDN0TQrkDBcvasA1CESD4T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=vpz5D95RO-T5_FIskplM5NH3F6j7KtZOkOuja69WBwKxXgN3t5fCM1Oe0mbzDhECa9EJ86tnhsR1FkWldM3bOVEVvuUxDmDe8H9O3Cy3CEN7Tphrzdz8ZBWR3b1nWtnu7X_Xif-Q8eLDARM11hNz1ToraP_c5EzXJ3SZVhVjOxB0Ut_XaqvOyIy1dbf_jae3UvwPwuAM-7qwN_1RBasJ2lw1b_iUvMjqoL66mjEIfYe8efDuXg_LPael5umKXsLG8rahWRTglJ2wenyNn_TdgzgQH_bqMBArl5nPSztvYK6PnlDr-VoLpLM65RQShwTmDN0TQrkDBcvasA1CESD4T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنلاین شاپ های اینستاگرام برای ویو دست به هرکاری میزنن
مثلا این ویدیو با ترفند شیک باسن باعث شد میلیونی ویو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/70798" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=g0IbxOH6PqfyiZYeEl6SUrV38Pl_Mlef2NtvtFcK0u5iiD7BAR20CVdBzKIR5DQf1_6mEasQaIBGmlAlxXuIe4Yn2JnOYKJ0afJs0UMxa7INysft0PNpPHND4znPiTrNx9ZKIUQhJL_TuCeuKbN4bF3LB4UJvahJDFPTB_eL53sg8c2c0Em9yF8OWZEZpY3VeeVN6gZ7g5cHkkEGOrtfMPE4zkfW8xhu0q2hWimwy5I1BcSlD7e7lAUpdQiXYjZVFCaROkFhZ7iii3CS_80Qo-eyF6VsbUINCquC9jvj0WOQnhnQf-a03TlgAL3SXwxmqaam6vrATkzl_jxVqgfvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=g0IbxOH6PqfyiZYeEl6SUrV38Pl_Mlef2NtvtFcK0u5iiD7BAR20CVdBzKIR5DQf1_6mEasQaIBGmlAlxXuIe4Yn2JnOYKJ0afJs0UMxa7INysft0PNpPHND4znPiTrNx9ZKIUQhJL_TuCeuKbN4bF3LB4UJvahJDFPTB_eL53sg8c2c0Em9yF8OWZEZpY3VeeVN6gZ7g5cHkkEGOrtfMPE4zkfW8xhu0q2hWimwy5I1BcSlD7e7lAUpdQiXYjZVFCaROkFhZ7iii3CS_80Qo-eyF6VsbUINCquC9jvj0WOQnhnQf-a03TlgAL3SXwxmqaam6vrATkzl_jxVqgfvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
آیفون 17 پرو از ارتفاع ۳۰ کیلومتری سقوط کرد و سالم موند!
آیفون 17 پرو رو با قاب محافظ
RhinoShield AirX
از یه بالن، از ارتفاع
۳۰ هزار و ۶۰۷ متری
زمین ول کردن!
باورکردنی نیست، ولی گوشی بعد از این سقوط وحشتناک
کاملاً سالم موند
و حتی یه آسیب جدی هم ندید.
🔥
🏆
این اتفاق توسط
گینس
به‌عنوان «بلندترین سقوط تلفن همراه درون قاب محافظ روی عوارض طبیعی زمین» ثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/70797" target="_blank">📅 14:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6McSo-8PtZpHJ-A1ZtLIxRgL33Wlb1_4StXbKEkUA7WichndMnjvErctHwZUMGooWtFzkD0pNzlU3ABY6-c5jSJ3aSOuDdp7hF0Y30FqMkow2TI6HOlmEOzmo3zQ36an7ZGKm4O1MByAxlYLYCKBuE48gBKI5ngcehKGGBA5IQBU6Di_haEbUseig4vVakYpsHuIaIV4hzCPA7hX304eD5uLbd45Bv0qHzaS6RsmZvepxWAvgqm0d9bU9vD7EAKrW1x5bzNrW6U0kiaAL1EOVUpu_BWX0TRZ40Mp6dcLjOciXeTbSkpPuS_gdZ-Za_SE6ysTF6Kj5cJ5YkGcgHDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تصویر ماهواره‌ای از بقایای شناورهای غرق‌شدۀ جمهوری اسلامی:
تصویر ماهواره‌ای تازه،بقایای ناوچه‌های جماران،نقدی و بایندر را نشان می‌دهد که در حملات اخیر آمریکا طی جنگ ۴۰روزه غرق شدند.
در این تصویر همچنین بقایای احتمالی یک شناور کلاس دلوار و دو شناور گشتی کلاس هندیجان دیده می‌شود.
محوطۀ پیرامونی نیز آثار گستردۀ تخریب ناشی از حملات را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/70796" target="_blank">📅 13:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=Qrau8TfGGJgy2PNibwtgf37NDoKneVIP4HsjhoWcz5040MRVpWvEEvse4uhJxuyB5ykhOK4dIX0oAm1I6KQnTfpxpk6E60q0dRzzwOlIPgemQxVJsy2_yFJoAvFHUHQRJ0pquStk50FyqgPJpKroFEQICV6I9iVp7ubrQdofXThgUzCQF_3o6LQervCZ5-sHzaeX0ezYAd10y6cA0c2WBUuyNqZg7eVv7LYBDijZgjQNjAiIP7mACggrghkYydlbseqMYP-P4DO3V3I_gkqPNQSpGYh5yim8dOt6wqxMEgPsL3crjGq7FgTXyU24FqQbCV0MuJfqNnFSUd08Ic-AUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=Qrau8TfGGJgy2PNibwtgf37NDoKneVIP4HsjhoWcz5040MRVpWvEEvse4uhJxuyB5ykhOK4dIX0oAm1I6KQnTfpxpk6E60q0dRzzwOlIPgemQxVJsy2_yFJoAvFHUHQRJ0pquStk50FyqgPJpKroFEQICV6I9iVp7ubrQdofXThgUzCQF_3o6LQervCZ5-sHzaeX0ezYAd10y6cA0c2WBUuyNqZg7eVv7LYBDijZgjQNjAiIP7mACggrghkYydlbseqMYP-P4DO3V3I_gkqPNQSpGYh5yim8dOt6wqxMEgPsL3crjGq7FgTXyU24FqQbCV0MuJfqNnFSUd08Ic-AUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
تاکر کارلسن، تحلیلگر آمریکایی:
در نشست‌های پنتاگون درباره نحوه واکنش به ایران، گزینه استفاده از سلاح‌های هسته‌ای تاکتیکی بررسی شده است.
روسیه، آمریکا و اسرائیل در حال بازنگری در دکترین‌های هسته‌ای خود هستند و آمریکا نیز این موضوع را بررسی می‌کند.
سلاح‌های هسته‌ای تاکتیکی با وجود قدرت انفجاری کمتر، همچنان تسلیحات هسته‌ای محسوب می‌شوند و استفاده از آنها علیه اهدافی در ایران در پنتاگون مورد بحث قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70795" target="_blank">📅 12:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=XQsDE4OOWMFb1YfMPOIp1C-sWSLsl3vCXZs0nIZbwk4D4B1VzsCcWRU7Oa2r96JODzCE1UHvvSYP-jAKvz0cd94RNfuXowDASSVVdcZjbEgACDPbIFXHyiU0JQPOiK8v0zObOEklvB7XCzQM_nU-xZrN5DYOL_ftWSfHJdc6p4TWQKRqLoAMq0sVqc3zXNN_BLYOKsYfrUtt8V4oA6Lg2-nN_nRsJabCGOLFZJslpOx-duE2VNWpn3KsvRWb6QSkiNKMvvwdVGTRIf7eN_4WdhzcMejoqdrIWbAPSnBIpVG6XoShNVaZdf8IlLjohhx1_MBEN1Z84PmOFQ4TRJw18A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=XQsDE4OOWMFb1YfMPOIp1C-sWSLsl3vCXZs0nIZbwk4D4B1VzsCcWRU7Oa2r96JODzCE1UHvvSYP-jAKvz0cd94RNfuXowDASSVVdcZjbEgACDPbIFXHyiU0JQPOiK8v0zObOEklvB7XCzQM_nU-xZrN5DYOL_ftWSfHJdc6p4TWQKRqLoAMq0sVqc3zXNN_BLYOKsYfrUtt8V4oA6Lg2-nN_nRsJabCGOLFZJslpOx-duE2VNWpn3KsvRWb6QSkiNKMvvwdVGTRIf7eN_4WdhzcMejoqdrIWbAPSnBIpVG6XoShNVaZdf8IlLjohhx1_MBEN1Z84PmOFQ4TRJw18A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/70794" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70793" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70793" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIjb2v405HS-AzlUEX7M3Pxx83KHUYiXyGPcY1l2pKlXW8S4UhrJqb3z5VMhkjuIS5hkpj1EQXD6T2nSk-MuXPH4KAhcXQO6ouMZPEiU87-HeE8yHig0rTZoA2HjgvRFT1xI8uQLDuvXKv5KK3OZL6UMnXLR-s58hd88e-q3kmpl0Q6iq6BngN1-WlqVIoN_LDFNKpE9kicz9ewQGLJg8b17GFSCfN3gzfnl-cWrJfOzfexySERfhzJKEBxCVjDke-cze1ek7kDMONc_qJpwf6LzPeZdPZiIQSa_CzjC3Ujh8BSBylMztLKawK6axIGTI3ZkZyLy3qeKjhcukOE5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70792" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=mvMrSL7pAiYqfDzyxhfuAAG2obs7aqrU8C23zT31klY7QRTKtR8wF07wY0ytMiUJOq4hnfpgU63kraOzIK-MlJaUeRJ9RLAzlfWEak3pGQ47ep4phVpHAgP5bE_b9tXQykmD6xM7q6M5AuRRD8oBcULLMmBB6fxD25qDFiVsGxrIqoMnKHnK2vG8m2jrO-VIxi2P42Xc1RwpBqErCYlKhU8JL-aKaEa052QaNPqfvy9bRdMk45dvuBupG7DwZin7f7uqv64ykW1Lt26MtIn41BtPPkaaSCicDRk3MyCRo_7YnFQbADVHjkWHg_IpVl66TFZV30EU4DJ34AwLz-suGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=mvMrSL7pAiYqfDzyxhfuAAG2obs7aqrU8C23zT31klY7QRTKtR8wF07wY0ytMiUJOq4hnfpgU63kraOzIK-MlJaUeRJ9RLAzlfWEak3pGQ47ep4phVpHAgP5bE_b9tXQykmD6xM7q6M5AuRRD8oBcULLMmBB6fxD25qDFiVsGxrIqoMnKHnK2vG8m2jrO-VIxi2P42Xc1RwpBqErCYlKhU8JL-aKaEa052QaNPqfvy9bRdMk45dvuBupG7DwZin7f7uqv64ykW1Lt26MtIn41BtPPkaaSCicDRk3MyCRo_7YnFQbADVHjkWHg_IpVl66TFZV30EU4DJ34AwLz-suGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که کلینیک بیماری زنان داره تعریف میکنه که یه خانم 56 ساله بهش مراجعه کرده و گفته که همسر 67ساله‌ام از وقتی بازنشست شده، روزی چندبار باهام رابطه داره؛
قسمت عجیب ماجرا اینجاست که جدیدا یه فانتزی‌ای پیدا کرده که میگه سرت رو بکن تو ماشین لباسشویی تا از پشت باهات رابطه داشته باشم!!
الانم این خانم سوزش شدید پیدا کرده و مجبور شده موضوع رو به پسرش بگه تا اون بره باباش رو از خر شیطون بیاره پایین...
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/70791" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70787">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=Bw_NARW9pNde85uxA-3Qb2V9Sbb5ps6VF3F-Qpwt5_lEIImhhU5XwxChL0uuwMPJtIo_7l-xVNRDw9Hm5dQhwKhTvSwHDtW87n_x0Vp4NqLXXyRT5zFlV7kDzigoWEdFLU1HB1_CJFkk8eOGTL6SntRL-o6wn6sETOsH3WkRGeosBnNRRpeBeZHu5-6htugHK1mcdgDqKQpK-30qH_KLkvkHgD1RPBtOdfUzcPZzI2TzRJUWd5I5yM4u8dRcGIgS4cPev_e3vLZDpTMOVkDLmF8KH2Hs7Zw6oVvHyck4oUdxGQi5klShQJMJCdBoYSw6vY4qgjSyi-om7MlNy6ct-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=Bw_NARW9pNde85uxA-3Qb2V9Sbb5ps6VF3F-Qpwt5_lEIImhhU5XwxChL0uuwMPJtIo_7l-xVNRDw9Hm5dQhwKhTvSwHDtW87n_x0Vp4NqLXXyRT5zFlV7kDzigoWEdFLU1HB1_CJFkk8eOGTL6SntRL-o6wn6sETOsH3WkRGeosBnNRRpeBeZHu5-6htugHK1mcdgDqKQpK-30qH_KLkvkHgD1RPBtOdfUzcPZzI2TzRJUWd5I5yM4u8dRcGIgS4cPev_e3vLZDpTMOVkDLmF8KH2Hs7Zw6oVvHyck4oUdxGQi5klShQJMJCdBoYSw6vY4qgjSyi-om7MlNy6ct-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار شد که حسابی سر و صدا کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/70787" target="_blank">📅 11:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70782">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=KGkKh1bva2o0mCAeEYAwNLcvAVPmJcC21O35cWLflY0RWt9UTCRzNcdFTgoD5Ly207XTCHfTzST4Zq9WcsEGVpoOHM9lK-geOy5Z0EjA0crqsfFDFzbIBjF1xq5TlOruURi1fmhFRc6AODZg9VYOQy3tECZ-ifvC9KaWA7LL4aeyPXG1px1POSVcadSHwnC1_L206yFkN5xg3HGBwCtrJU8mXsUFvKR2Jkh07_hbztnyWheYvygXCaVD8uCqrcJ9nxrTKjMSB58hhJ41jhwYiAy2utOP56No8Vw6xq3XetU_pvYZLzuk5zb7rjqGnBTc4TzaNRPGTnpC2znzfqkRcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=KGkKh1bva2o0mCAeEYAwNLcvAVPmJcC21O35cWLflY0RWt9UTCRzNcdFTgoD5Ly207XTCHfTzST4Zq9WcsEGVpoOHM9lK-geOy5Z0EjA0crqsfFDFzbIBjF1xq5TlOruURi1fmhFRc6AODZg9VYOQy3tECZ-ifvC9KaWA7LL4aeyPXG1px1POSVcadSHwnC1_L206yFkN5xg3HGBwCtrJU8mXsUFvKR2Jkh07_hbztnyWheYvygXCaVD8uCqrcJ9nxrTKjMSB58hhJ41jhwYiAy2utOP56No8Vw6xq3XetU_pvYZLzuk5zb7rjqGnBTc4TzaNRPGTnpC2znzfqkRcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇳🇵
🇨🇳
ویدیو اختصاصی جدیدی که توسط نیویورک تایمز به دست آمده و تأیید شده است، واضح‌ترین تصویر از ریزش کوه لانگتانگ لیرونگ در ۲۶ آگوست را که باعث سیل فاجعه‌بار نپال-تبت شد، ارائه می‌دهد.
کوهنوردان قبل از اینکه یخ، سنگ و آوار به دره فرو بروند و ابری از گرد و غبار عظیم را به هوا بلند کنند، صدای ترک بزرگی را شنیدند.
فیلم دیگری، آوارهایی را که بلافاصله پس از ریزش به سمت پایین تپه حرکت می‌کنند، به تصویر می‌کشد - آغاز فاجعه‌ای که جوامع پایین‌دست را ویران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/70782" target="_blank">📅 11:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70780">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4pY0HV0xCjzx-XjuxA0dGyE0I3960cID8NjZO6b59lzHcLOXyBndyJUt0OrxtQ99E0FVZCXLTChLHZIZeZKWdRCkEYuaxAVnTlpM4L5PYyNjqyPyBEVAMqI10KCdwSSnlKb5m7TLFe_1EjqVYSQSy9rw_ZR_2MDFzoa2wiK7R8uUa-DzambnZk8I_Z1h0OUR9TVUvGjRYOi02Jjv2yKxfeIOrfmvF1Dn5mXo2pj6CiuO-ZM4cW3t1VoiyoCthhYhKZFno39IbligvssbqKjjtFCPMIpYz5YjVR2ppgZQOpQRHBTnnpr_UP2oLECh-1AiViR_Q46tVyQljaFfoF9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCL2wMIX3NyTXHItXz4G5qYHDTw6UjATcDqSNQXGquC3O-lbZykaL3yJzKnJcohbPKNDvMU1bYdcEzNBgx4KIzlg36LwEa7bh480CPEFklwffYqG0f34TxHaX8HvHhg_BHCwIV4o8mbpfLDcG0Fz8EJOLRMxaHn1kHrHsA49I1dcgc6c1yuPU-6z5KAQ-rORd6TY7WUL-VHP8P8Gl12r0W3XGCFR8mEfrk-LMQf1iKsCuhtf-atIyWPxEV2tIqvkfhJB-fyiOY3THa4ecmMr96LokyQupuC8jQWhnPFdQHXAI2sXe8pq2XCFkwEvUHfojb4S2JUEvr1Yhf0PjirW9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
استوری یوسف، پسر مسعود پزشکیان:
مسائل رو ناموسی نکنید که هیچکس نتونه درباره‌اش حرف بزنه!
اگه تو غنی‌سازی منفعت داریم، دنبال کنیم و اگه نداریم، متوقفش کنیم.
اگه تو داشتن توان موشکی و پهپادی منافع داریم، دنبال کنیم و اگه نداریم، دست برداریم.
اگه بریم سمت هسته‌ای، دیگه فقط آمریکا و اسرائیل نمیان سراغ‌مون و اونوقت یه اجماع جهانی علیه ایران شکل می‌گیره.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70780" target="_blank">📅 10:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70779">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ffa3e78b.mp4?token=BOPFxTu4-b4VQbi_Il8Syz8bAEIvI8t1SWfQtyw6wnLvEnG-EakqK5IQVjBYrJVbGIJWb7PA4SvEdwCr_l6YP7ZXju4eeGIODJcrer3ARV5cmQC0UEkVpEq5zaHE9vRF3V3iFIw3bw6UtExGIOup3PIHXqNmJpGX-Xp40bdFnCRrFLHqQufALyhj0aKyZjStm4uwBGPAzK6rZJ8x47hJxqMDqPyJLZyF5SLjOlQbIQoFsw_zRIDeIZ7YaKsxqgpVoXH6IGXEAPlYGAn8-v3yM8uNrh78GpQ8w6xhUSp3wrbUI_JlCwu540g1skfkdu73xVmyj6GmY9RvrZubxKA0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ffa3e78b.mp4?token=BOPFxTu4-b4VQbi_Il8Syz8bAEIvI8t1SWfQtyw6wnLvEnG-EakqK5IQVjBYrJVbGIJWb7PA4SvEdwCr_l6YP7ZXju4eeGIODJcrer3ARV5cmQC0UEkVpEq5zaHE9vRF3V3iFIw3bw6UtExGIOup3PIHXqNmJpGX-Xp40bdFnCRrFLHqQufALyhj0aKyZjStm4uwBGPAzK6rZJ8x47hJxqMDqPyJLZyF5SLjOlQbIQoFsw_zRIDeIZ7YaKsxqgpVoXH6IGXEAPlYGAn8-v3yM8uNrh78GpQ8w6xhUSp3wrbUI_JlCwu540g1skfkdu73xVmyj6GmY9RvrZubxKA0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت بندر شهید رجایی بندرعباس، بزرگترین و مهمترین بندر تجاری کشور بعد از محاصره دریایی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70779" target="_blank">📅 10:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70778">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6d1be5bb.mp4?token=vudi89ZgRKt-svhNLP0-N8BYnhuklFtE5p0ihBQfhosC33L-Adk-bp6W2TgVhHpsUBHJ1XqhP1zZuB10ZB1hSK5dVqMBxoxhdpE3zdHwWSYGfnXLtMTNbasQ_bQWO7Xj4bloXmj8d-5dhV24uSAHilufcpzZ3CF7U-pfL0Dj4fkUf8SLkl1zG_CiT6uQNSBn8BQsZwg0GzDqqsDuas6y427qr7sXPTmPAizFrm0ZAHXtKqdBJIGCgmUFbFS3BA27ONLO-Lm1FnEUPrOTWXJX5yUl3RfppTBjYp3_X0oYFlRhRMJ2xx69Bl8unZY2HUDmdFjiRsFHWw3y-wvj4-iaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6d1be5bb.mp4?token=vudi89ZgRKt-svhNLP0-N8BYnhuklFtE5p0ihBQfhosC33L-Adk-bp6W2TgVhHpsUBHJ1XqhP1zZuB10ZB1hSK5dVqMBxoxhdpE3zdHwWSYGfnXLtMTNbasQ_bQWO7Xj4bloXmj8d-5dhV24uSAHilufcpzZ3CF7U-pfL0Dj4fkUf8SLkl1zG_CiT6uQNSBn8BQsZwg0GzDqqsDuas6y427qr7sXPTmPAizFrm0ZAHXtKqdBJIGCgmUFbFS3BA27ONLO-Lm1FnEUPrOTWXJX5yUl3RfppTBjYp3_X0oYFlRhRMJ2xx69Bl8unZY2HUDmdFjiRsFHWw3y-wvj4-iaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان بعد از بیانیه مجتبی خامنه‌ای که گفت ضعف های کشور رو علنی نگید
داره پرقدرت به حرفش عمل میکنه و اومده گفته:
صداوسیما هی‌‌ میگه‌ آمریکا تورمش ۲ درصد رفته بالا؛ خب‌ بابا مال ما ۱۰۰ درصد رفته بالا.
همه چیز به تحریم و واردات ربط داره.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70778" target="_blank">📅 09:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70777">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=ABQITD3MaXBelgpSkw7k6OjgXkOgNEYxD5J33UcnN-y_s-OmH_Y2HRQ8W3jeGtsx5nEVs5C4QT5RlHZ0aTNQX3dKLlXQoNdC1KCEb6NivLxMuexc88ihxHJ4xVATI66rcFrxI81YwE79muB_sZX9uaBdu_4NRrmWLw7D_XVdK9VsUjXgUFcL7DSxPFUnMHVY4Rqlxjz99U3i0IGdJBtjM_dY7oV_LCD0cmE_f_is6tiLKtWuHXpyk-wYkC9xZsQDuGDjtFNDjuhtjchbbN4HaVUfa0pjIMyx5NfsBvqm1o5mnuaRewRMZE0zI-ZAQySc1HjdMiWLNsGYc_zXUgsckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=ABQITD3MaXBelgpSkw7k6OjgXkOgNEYxD5J33UcnN-y_s-OmH_Y2HRQ8W3jeGtsx5nEVs5C4QT5RlHZ0aTNQX3dKLlXQoNdC1KCEb6NivLxMuexc88ihxHJ4xVATI66rcFrxI81YwE79muB_sZX9uaBdu_4NRrmWLw7D_XVdK9VsUjXgUFcL7DSxPFUnMHVY4Rqlxjz99U3i0IGdJBtjM_dY7oV_LCD0cmE_f_is6tiLKtWuHXpyk-wYkC9xZsQDuGDjtFNDjuhtjchbbN4HaVUfa0pjIMyx5NfsBvqm1o5mnuaRewRMZE0zI-ZAQySc1HjdMiWLNsGYc_zXUgsckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات اولیه حمله پشم ریزون آمریکا و اسراییل به انبارهای نفت تهران در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70777" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70776">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omV3GI9ZIjtikfuWNHWXGsFTHrwBTnARDxs98zHk1Ty9FvzTYDzzFJMbFliGuLDJ5DLQuZVfMZ-ex5xMHFGLA4ez3F00QOdSfNahWNsDdZ4g5Z2O0YlxMWJy4wHMDNqSgqyQJ1e1OJthCunIHHW9gyfsl0uiKojRvXoqPvs7Gjokyfs0s_h39bcJBomQfsU7YM8SGlwYOtHMya6Nt-4xNShcWUwdX5ZlAAyhZs-lN9T9UZalySBLAbVVsPhbhj065kvjzjwOOxabAKW_tkkiHVAIOdB3tvFpG6duGfGwOgaPpKnIHUJti0kahleqOVJo2B2XaHvIfwYorYfjd9eghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70776" target="_blank">📅 01:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70775">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26b389410.mp4?token=mnuw4metfeUqQ119oe68fzVYJQsW3rz0idYFdlgf18DVhdJiFutR_Q7cDJ_IvKQH0afg9BQ9zKLn7KgsgSld9cip4mXUT9Sdf-B6w0yar5pHQdJLpbEphW3S13iigij9_yqkudDlbzIjezJ3iv45m-dS-MF21uXv5KhSLn3phH-zpCZv7y44dG0aPQUt9IICuTA1gl0OR0W5OaKQlZxCL_4EhQFZU_C2YmSKv62SgIzDusNFz9BETz8yBqJOa91vCSJqvud_-oYb0GApmtbMMNPDrNSlpdcwon3UoLlriQIjVmkKXMPKXLZYFrJzz9fGejymzXEa8wqIR7CNBNg6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26b389410.mp4?token=mnuw4metfeUqQ119oe68fzVYJQsW3rz0idYFdlgf18DVhdJiFutR_Q7cDJ_IvKQH0afg9BQ9zKLn7KgsgSld9cip4mXUT9Sdf-B6w0yar5pHQdJLpbEphW3S13iigij9_yqkudDlbzIjezJ3iv45m-dS-MF21uXv5KhSLn3phH-zpCZv7y44dG0aPQUt9IICuTA1gl0OR0W5OaKQlZxCL_4EhQFZU_C2YmSKv62SgIzDusNFz9BETz8yBqJOa91vCSJqvud_-oYb0GApmtbMMNPDrNSlpdcwon3UoLlriQIjVmkKXMPKXLZYFrJzz9fGejymzXEa8wqIR7CNBNg6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپِ هوش مصنوعی، تابلوی «دریاچه انتاریو» را با تابلوی «دریاچه آمریکا» جایگزین می‌کند و سپس با آهنگ «YMCA» شروع به رقصیدن می‌کند
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70775" target="_blank">📅 01:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70774">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6d62ZQw0XC4RAjUlwqA9OdmWLwsPS-8vYuW8a0c70jnlrqXuwoA3fyuy4fKFuxn09YLEYf1IrlVNwyHntu2FiDAG4Itv0oYpPh6KMgx8XF4LTivteAu3JH6E-PxmlBs9tKYRiXvLhHPP6wQ35XajwJEvv2QovS6iIflkjkcFy8TQiQINHXc6qpPYgSJpiXtk68tyWtW7NcWNaAfgBwoYqmquY12frz-XqW4nyXMj9ptij2Bwbvd_UibMu1gILs1-wJUHfqDa_UavGcTHeVinu6wFyWnrDK4VGIayEk3Pe_HhfKmG4zoEtRFiu6Wdg_zapv3-LV9XFG2KldVe9h_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
باراک راوید:
دو مقام اسرائیلی می‌گویند که تصمیم به بستن تنگه هرمز توسط فرمانده وقت نیروی دریایی سپاه پاسداران انقلاب اسلامی، سردار علیرضا تنگسیری، اتخاذ شد.
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه را می‌بندد و هشدار داد که به نفت‌کش‌هایی که قصد عبور از آن را داشته باشند، حمله خواهد کرد.
اما به گفته مقامات اسرائیلی و آمریکایی، تنگسیری در پشت پرده دستوری صادر کرد که تنش را به‌شدت تشدید کرد: استقرار مین‌های دریایی در «طرح تفکیک ترافیک» (TSS) که مسیر اصلی کشتیرانی بین‌المللی در این تنگه محسوب می‌شود.
تنگسیری سه هفته بعد در جریان یک حمله هوایی اسرائیل در بندرعباس کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70774" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70773">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=t_l4dJIDLpz7yEz3N2jEndvsW9dwexBBtMosIDCL7ZSqfH9cUN3FTxXt28p7gP6Bonott0G05pGQH_NKRHxlFXIffxEXUMNtvG-Q3RJgDznHSSJNXGnubfupmceAVjWGC83_tK1yJaPp6-IsEJfcJ1Ok1VyUIdO7uBisiWpLj-8_tp_9y4gEnWx_lyr30bPvzdzz9CDdBWEZTatEqbhOE4jNecXBzPS7POMobJjjfTaT-WYtdf4PuhA_gUeya8nDQnGUz0fe_UOMxa0HL4c8RuFCvg1q3M6_pZkZqhPNvv-kjDFcc9ceY-4CP_mQxEueXjQemwm3hqqIJJWQpXG75w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=t_l4dJIDLpz7yEz3N2jEndvsW9dwexBBtMosIDCL7ZSqfH9cUN3FTxXt28p7gP6Bonott0G05pGQH_NKRHxlFXIffxEXUMNtvG-Q3RJgDznHSSJNXGnubfupmceAVjWGC83_tK1yJaPp6-IsEJfcJ1Ok1VyUIdO7uBisiWpLj-8_tp_9y4gEnWx_lyr30bPvzdzz9CDdBWEZTatEqbhOE4jNecXBzPS7POMobJjjfTaT-WYtdf4PuhA_gUeya8nDQnGUz0fe_UOMxa0HL4c8RuFCvg1q3M6_pZkZqhPNvv-kjDFcc9ceY-4CP_mQxEueXjQemwm3hqqIJJWQpXG75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارتی شوگر مامی ها توی ولنجک تهران
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70773" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70772">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051d44837a.mp4?token=I-qIIDuX97UUPiKOMgbXuP3XXPCe2EohFSQAUa4Ys98Z0ZXuvPJfEDWWZyXBIm7MoXqfqpawKnFS5MdRy4TE5C4BbfWr7XnFSlblxHShwuuj7wKtqbKcvIj14hBuI9Nad0uPKcEK-V2VVzaPLsdbGkTnbJgaXLh1N5z0lj3GyCBvujXZXzmPZ3JRcH5Bzx35NSitsvZBTHCmEvUNUA_9VLBhU3avj93SvXnVSj-FAl8xDIRFqruDqdAnFN_wjfWHjALoo9NCE6lh_hsOyob3KZ0dD7Iu15kDAOGi6D9GWNVi3BDE9jSAk9-YXNp56ZIcySAzBtgjnqzS_Yy8-YwqS8ABett-izhmLU_bRQJUrfT8RYKu1Dh_32HdvuUFWjr3QQHWYpXK55oG6xfVKvVbrwTqOskdNaXLHg2kAH2F5X51w-33wFSlydCJ4D7SDbQWgA3ILjo90HdPIM6vwm0I2_2SlT1jJDgdlZaO5UI0eJn5eWecRcx_s6DWgBXtY4Hh73TGfgQ-7CNuqbdIO-E6fu1VJJwKeLNoaMHpP7-i4-Ohh1_twN9OcGPSyiBuY65bD2KWXmxzN6BAkLWjmLLa2M0pdP_u4BGjG704eSlPacQdO60tJG_8BxXIQ4vPmTrSNSs8bld_mZorBJIk5gLl6uJre44NsWtTW5Yz90yv6i0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051d44837a.mp4?token=I-qIIDuX97UUPiKOMgbXuP3XXPCe2EohFSQAUa4Ys98Z0ZXuvPJfEDWWZyXBIm7MoXqfqpawKnFS5MdRy4TE5C4BbfWr7XnFSlblxHShwuuj7wKtqbKcvIj14hBuI9Nad0uPKcEK-V2VVzaPLsdbGkTnbJgaXLh1N5z0lj3GyCBvujXZXzmPZ3JRcH5Bzx35NSitsvZBTHCmEvUNUA_9VLBhU3avj93SvXnVSj-FAl8xDIRFqruDqdAnFN_wjfWHjALoo9NCE6lh_hsOyob3KZ0dD7Iu15kDAOGi6D9GWNVi3BDE9jSAk9-YXNp56ZIcySAzBtgjnqzS_Yy8-YwqS8ABett-izhmLU_bRQJUrfT8RYKu1Dh_32HdvuUFWjr3QQHWYpXK55oG6xfVKvVbrwTqOskdNaXLHg2kAH2F5X51w-33wFSlydCJ4D7SDbQWgA3ILjo90HdPIM6vwm0I2_2SlT1jJDgdlZaO5UI0eJn5eWecRcx_s6DWgBXtY4Hh73TGfgQ-7CNuqbdIO-E6fu1VJJwKeLNoaMHpP7-i4-Ohh1_twN9OcGPSyiBuY65bD2KWXmxzN6BAkLWjmLLa2M0pdP_u4BGjG704eSlPacQdO60tJG_8BxXIQ4vPmTrSNSs8bld_mZorBJIk5gLl6uJre44NsWtTW5Yz90yv6i0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصویری که صداوسیما و رسانه های داخلی از آمریکا نشون میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70772" target="_blank">📅 23:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=oLGr8mhesmHElgWMqF5t0p3sOenRIRnGfoR0WyRRokur24qu0cUeXR-QvUdfZHdSqNcK8T3XgvOcO3H4462H4Ejd6A5DnbAoDdBVK9yhK4ofhLmuT3Ib6BH-VkRPtSaChRxzpH2iIM3ufV2AXJLkw3TC5yzUWOQ1MNlL491EKR9_FzpQU0hktlGUQN8Z3JtZNHXa5zM3twHW1Fs6BVPrE37WNkmRf_WhLwAfV6XHOF7VNOcJalEslESriWie5wCZj8qYlTfnjXGLz1h2lsOYy4frp2FUBSxIqBhewICc808yGh_40w7vMVcPKatPKStp278L_4RgdJTNVFhd6VYq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=oLGr8mhesmHElgWMqF5t0p3sOenRIRnGfoR0WyRRokur24qu0cUeXR-QvUdfZHdSqNcK8T3XgvOcO3H4462H4Ejd6A5DnbAoDdBVK9yhK4ofhLmuT3Ib6BH-VkRPtSaChRxzpH2iIM3ufV2AXJLkw3TC5yzUWOQ1MNlL491EKR9_FzpQU0hktlGUQN8Z3JtZNHXa5zM3twHW1Fs6BVPrE37WNkmRf_WhLwAfV6XHOF7VNOcJalEslESriWie5wCZj8qYlTfnjXGLz1h2lsOYy4frp2FUBSxIqBhewICc808yGh_40w7vMVcPKatPKStp278L_4RgdJTNVFhd6VYq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
«میزان، رأی ملت است»؛ اما ظاهراً نه همیشه!
🎙
روح‌الله خمینی در سال ۱۳۵۸:
«میزان، رأی ملت است» و حتی اگر اکثریت مردم اشتباه کنند، باید به رأی آنان احترام گذاشت.
اما چندی بعد، در سال ۱۳۶۰:
«میزان، آرای ملت است»؛ «البته مسائل اگر مسائل اسلامی باشد، اگر در رای هم مخالف باشید، باید تو سرتان زد!»
🇮🇷
🎙
سال ها بعد علی خامنه‌ای در پاسخ به پیشنهاد رفراندوم در ایران گفت:
«این چه حرف بی‌خودی است؟ مگر همه مردم قدرت تحلیل مسائل سیاسی را دارند؟»
⁉️
اما همین رفراندوم را برای فلسطین و دیگر کشورها تجویز می‌کند تا خواست مردم مشخص شود!
پس چگونه است که مردم دیگر کشورها قدرت تحلیل مسائل سیاسی دارند، اما مردم ایران ندارند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70771" target="_blank">📅 23:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70770">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=dExJF8HobVewYiMaGluERn3zjE0BuWsQKLQsoBYNg4CIxR_fXlOSPANkP171-f4EKHNfELWrnORaqrwBkkq1AHfJFlBx1yKCrTKz4nwzekvz4HFNBl9Vw4wPrpHG9t_2b53mxuB95ShMoiVJc44s2jK6UUd0x5xHErttdwYW00okvfvDXAOdj31Dek050Xwkzqwh1vnxhfsE-L2b5uAlm_mHBIvlTBbrB61iRgOeISF-eerD748M0nHN8D0QEZtS0xLTq6Rk-lXGlvzfGJkD0oeFlXtSma45dKTQFa5ks5D7aQMoXbyU3JB_Q0L9OYnivUh4784yPbQ1a8KtZzIqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=dExJF8HobVewYiMaGluERn3zjE0BuWsQKLQsoBYNg4CIxR_fXlOSPANkP171-f4EKHNfELWrnORaqrwBkkq1AHfJFlBx1yKCrTKz4nwzekvz4HFNBl9Vw4wPrpHG9t_2b53mxuB95ShMoiVJc44s2jK6UUd0x5xHErttdwYW00okvfvDXAOdj31Dek050Xwkzqwh1vnxhfsE-L2b5uAlm_mHBIvlTBbrB61iRgOeISF-eerD748M0nHN8D0QEZtS0xLTq6Rk-lXGlvzfGJkD0oeFlXtSma45dKTQFa5ks5D7aQMoXbyU3JB_Q0L9OYnivUh4784yPbQ1a8KtZzIqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر رفته دکتر و میگه وسواس شدید دارم و نمیتونم برم دستشویی چون چندشم میشه!
برای همین دستمال کاغذی برمیدارم، تو اتاقم لای دستمال کاغذی پی‌پی میکنم و بعد از یه هفته که جمع شد، میندازم سطل آشغال
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70770" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=hZjYkdn0aMVgqUk8n2x4DsgZACcMtsuXX_j4x7RjvdDKDmxz3DhOtZ_tMm2MpLG163is7U_-5z6DEaN8Obk435kKRblvKIdcQr-TuwqGRDXG9s1ljJksYWYOtoxPgJCoWU28mDm-qkQF8zQWqMCcd-f9r0rxZp7kEKDzDn4AuAQfre-bd5RuDd33GpkDYhymnaZw0tKn2rCbEwYlBU49YyCywOMQ6lsZOuezuPlu4Ilgm8leJg018h7WgxFOmZ6T0dd-h6xo6UM2tHCSgflAvN4BmlUuP59E6tbnNMaFdF7ilnJQDU0gCUBkg6WVY_7VXDjLvlLcSqFpyGPzmMkzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=hZjYkdn0aMVgqUk8n2x4DsgZACcMtsuXX_j4x7RjvdDKDmxz3DhOtZ_tMm2MpLG163is7U_-5z6DEaN8Obk435kKRblvKIdcQr-TuwqGRDXG9s1ljJksYWYOtoxPgJCoWU28mDm-qkQF8zQWqMCcd-f9r0rxZp7kEKDzDn4AuAQfre-bd5RuDd33GpkDYhymnaZw0tKn2rCbEwYlBU49YyCywOMQ6lsZOuezuPlu4Ilgm8leJg018h7WgxFOmZ6T0dd-h6xo6UM2tHCSgflAvN4BmlUuP59E6tbnNMaFdF7ilnJQDU0gCUBkg6WVY_7VXDjLvlLcSqFpyGPzmMkzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سخنرانی یه اخوند در خیابونای قم برای در و دیوار.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70769" target="_blank">📅 21:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=emSTQtoGQckbfhFHbFnP3yVrCja0J_fMTYumOXviB_SuKapLiA0wyLB_Bqin0tyHe5IOLm3ZJCSY0DYo0-IABsi3pUi3Y3_sHQ3sHn-H7K8XyXZWMXC9Wdy796pFEiLoOlIxQNpQJqffe3dj0UIH04cN4OQO8BE4C2jWU9z2mWLBBdqR08ATgOmqPx24DiFlh83IQMjwKETzMVIk6eyl89RIPyIWK_tclx2VWbwNTBOfLTEmOR8ARUWZWmfg1drWUZAHa1sZaqb6bF6T5iQ8K0dT8oPvajO8tIKJV9LT6DbSNNdH2jJRzigEMhfJuBlVJ8QB-y6TaMro4e9GYATssQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=emSTQtoGQckbfhFHbFnP3yVrCja0J_fMTYumOXviB_SuKapLiA0wyLB_Bqin0tyHe5IOLm3ZJCSY0DYo0-IABsi3pUi3Y3_sHQ3sHn-H7K8XyXZWMXC9Wdy796pFEiLoOlIxQNpQJqffe3dj0UIH04cN4OQO8BE4C2jWU9z2mWLBBdqR08ATgOmqPx24DiFlh83IQMjwKETzMVIk6eyl89RIPyIWK_tclx2VWbwNTBOfLTEmOR8ARUWZWmfg1drWUZAHa1sZaqb6bF6T5iQ8K0dT8oPvajO8tIKJV9LT6DbSNNdH2jJRzigEMhfJuBlVJ8QB-y6TaMro4e9GYATssQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صدا و سیما:
تو رو به خدا تورو به ۱۲۴ هزار پیغمبرتورو به همه اهل بیت باور کنیم که ما تو جنگ پیروز شدیم
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70768" target="_blank">📅 21:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBj865gsflqa4IqXDbyRlwXmzQCEVf4Otd1hUVFf-b5_fAKw_CBo0avl0HXgtmiPckdvPlJ6Ic21Qz94pvY9nzKaXEaVDfcKqnV4OnqbLMLwrjlSyjn-nrOCDUhqV83Rf1duzBFnQ4ykm0Zr1sre0YD4tmr-heMbM_qiJMvrgtMrd2VmADgeFauiluCFFNc3TkG8m7mq8XpkKMxEvKKjeHPi9gcFKbypSwTUfWSle15B88AFSJ5XwN2xl9pcWc3i8JAuCchIWO5dOOvKXwqPjDYeYx1KLU0e2UenOUzDAd9bhrD7i4F0YT6Uagx3OSr1RhNxcCwgyGlsYD74JF6k7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
دیس قالیباف به بسنت:
دروغگو، دروغگو، شلوارش آتش گرفته.
برای ۱۳۰ دلار واقعی، به کارمندتان بگویید که آمار مودیز را که ۱۳۰+ میلیارد دلار هزینه جنگ را نشان می‌دهد، بکشد
از دیگری بپرسید که خیابان جین چقدر از ۱۳۰ میلیون دلار فروش استقراضی نفت را فقط در یک دور معاملات آتی برای شما سوزانده است.
دروغگو، دروغگو، بازده (اوراق خزانه‌داری آمریکا)آتش گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70767" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=AINPyO9M5vh2O0qT6MzdhAlfVyfWuvqaZHAMITDJyTeWJ3u7T9xRpvCynm6thXlRWUWidYfw3rwOMNG-9x7Aqxr2XYk3_b2BE76c8QXH285PDp_pqxuolgc_8A42vzjCtIXhGlWmy_SnqMqh8AHv_fySBLMGYzqjB9Bx7yfyPy76agt2dAWTqOukEh5MJPzl-WLffA5G5_wAc3bIjj_89y9IgZkAwk56QSmT8rYaPStiF7IOL763DAHUN4ZiKWOUjGSuK0BitpM55GZD4dnDWJiacXteL7j6gzA2EMI13ecAiot7vNe9m1AfQXzSr5TD7423yaPs_1gS4BmiEvcwL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=AINPyO9M5vh2O0qT6MzdhAlfVyfWuvqaZHAMITDJyTeWJ3u7T9xRpvCynm6thXlRWUWidYfw3rwOMNG-9x7Aqxr2XYk3_b2BE76c8QXH285PDp_pqxuolgc_8A42vzjCtIXhGlWmy_SnqMqh8AHv_fySBLMGYzqjB9Bx7yfyPy76agt2dAWTqOukEh5MJPzl-WLffA5G5_wAc3bIjj_89y9IgZkAwk56QSmT8rYaPStiF7IOL763DAHUN4ZiKWOUjGSuK0BitpM55GZD4dnDWJiacXteL7j6gzA2EMI13ecAiot7vNe9m1AfQXzSr5TD7423yaPs_1gS4BmiEvcwL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
دریاچه آمریکا توسط «اردک های دونالد» محافظت می‌شود
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70766" target="_blank">📅 19:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
صف ترسناک و طولانی ده کیلومتری یه پمپ بنزین توی سیستان و بلوچستان!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70765" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70764" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlhNy2G3ilJckP15Shzj9qfb7MeJAu7Uwujto7HVidxmV8G_UJooBJqG39yyUzpz-bR_t5fimk9eo-m37xdTEo9GRAb0eQShznxVeX3y7LWy0jt_JV-9ERVcQ4SM4lwtPUuShmTus3uH4ObxcEPZuXx67tfzDNoXiuYi84_fV-hSZoq8GctQ9fN8ASz2DPcDvP8urBXp6ydUgOcV_P6cRWAEZFGLT8GoXdoQUTazX9TwbesoynIq9TyV0n5w4o-_mOndQZdbetRubCaB_nO9P0zz81yKjN4XejjY469cg-ssSc9ED4Dm4VuVhTm001EPPDgwqrZctU6BA9McP6ELSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70763" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70762">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنفرانس خبری علیرضا منصوریان در عراق که سوژه رسانه ها شده
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70762" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70761">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
رقص ایرانیان در شهر وان ترکیه؛
هزاران ایرانی برای خرید، دسترسی به مشروبات الکلی و تجربه تفریحات شبانه مختلط — که در کشور خودشان امکان‌پذیر نیست — به شهر وان در شرق ترکیه سفر می‌کنند؛ شهری که تنها یک‌ونیم ساعت با مرز فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70761" target="_blank">📅 18:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=bTvugyXVo2r_ejgHkxyEBzyI9Sx3dC8-NzShjfQzhiGBEpBdxpR_ARlhdYIxKclIPltnlwazUhNSwvLBQsAu9KCrlx1w8TjNuiZieZ5Y0M7EFjbcxcelyM08bIXNNaBc-_gzKNQQ_LQFuIKUHcfdwAP-IQWArh2dL5e5VJBnQv7heNhj_ve4c16-pBW4j-StxBcKWZ2G7O6ftgClQuo_OgX3oRFNglnpWKBCXWGWx21KRgEb6gCZgPfzlJLCheb5onys3sqk80zyG2P2SK5Zgw41IU2frPYYvyJcxUn9_lHC8yuhY7dvIHQ6R97tmUwlWtDBU_KuT8kcG5CxbwGmjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=bTvugyXVo2r_ejgHkxyEBzyI9Sx3dC8-NzShjfQzhiGBEpBdxpR_ARlhdYIxKclIPltnlwazUhNSwvLBQsAu9KCrlx1w8TjNuiZieZ5Y0M7EFjbcxcelyM08bIXNNaBc-_gzKNQQ_LQFuIKUHcfdwAP-IQWArh2dL5e5VJBnQv7heNhj_ve4c16-pBW4j-StxBcKWZ2G7O6ftgClQuo_OgX3oRFNglnpWKBCXWGWx21KRgEb6gCZgPfzlJLCheb5onys3sqk80zyG2P2SK5Zgw41IU2frPYYvyJcxUn9_lHC8yuhY7dvIHQ6R97tmUwlWtDBU_KuT8kcG5CxbwGmjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر داشت چالش ضبط می‌کرد که دو نفری باهم برن غذا بخورن، تا اینکه یه خانم دکتر خورد به تورش و آخرش این شکلی با دعوا تموم شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70759" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=H8fJ4W0trOST4pLoEiEFGZQE2-SZjNSRwX5JjWCi2a0q2LHenrB9zqLHxkIqyyOnXUY32nH6sL8Uj5ibUPUZAB2V9XucZpigHu5zBZF--mN1lyYFu12CsIeWDHtGX_Yl9Cr6HMEGlqvLtTDeOef0Rzehy165eIkImAVEnOpGuuAFj4agsMCbap-lOmN3ncsNIfUEhb949lNm2ep_9vl4MFrPSoW5eqvMef2R7m2sFkMXFcPm3t6ACflREl1BCMje5y4VN1fmAXjh1UadXZU9uH7Qi_gH14eBKp2SysXqYMQC0OUU1UO4s5sZi5X8wmutTnBVlBDmW5DKyasMOBTGHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=H8fJ4W0trOST4pLoEiEFGZQE2-SZjNSRwX5JjWCi2a0q2LHenrB9zqLHxkIqyyOnXUY32nH6sL8Uj5ibUPUZAB2V9XucZpigHu5zBZF--mN1lyYFu12CsIeWDHtGX_Yl9Cr6HMEGlqvLtTDeOef0Rzehy165eIkImAVEnOpGuuAFj4agsMCbap-lOmN3ncsNIfUEhb949lNm2ep_9vl4MFrPSoW5eqvMef2R7m2sFkMXFcPm3t6ACflREl1BCMje5y4VN1fmAXjh1UadXZU9uH7Qi_gH14eBKp2SysXqYMQC0OUU1UO4s5sZi5X8wmutTnBVlBDmW5DKyasMOBTGHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:
ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود.
امروز همان پوشک ۸۶۵ هزار تومان است.
باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70758" target="_blank">📅 17:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=tUqOt-3pTB_s7d3_pCruMt0B4jT_8Mg3bZEIUH8b1NWcki1heFod9nOoFFkwibCzLjctHr4-CIx_ImAICLvjjLpjMWrYEQMhM0VT3gW8h5OcBrty9xa-4YCg4HlkDiHsLuUlEyMT1m40N-Hs0fLmDv9VyPFyxKhYg1WYxAckehpfpt0Chwoct28_cx68apI2C_WjiQi59cpMGhn1HTG-gShnhxAYeltJyIDg1DhyEcCfZ-3JVA5kXZk1Qeh2pVRuKKI9FK8_ktFUIZ9JdFmWt1YnP8zOdELw_yyQBSE5nPuOTm6X9fdTHAyH4Ig434dG31pcDQtLucVRcKlcZBDUAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=tUqOt-3pTB_s7d3_pCruMt0B4jT_8Mg3bZEIUH8b1NWcki1heFod9nOoFFkwibCzLjctHr4-CIx_ImAICLvjjLpjMWrYEQMhM0VT3gW8h5OcBrty9xa-4YCg4HlkDiHsLuUlEyMT1m40N-Hs0fLmDv9VyPFyxKhYg1WYxAckehpfpt0Chwoct28_cx68apI2C_WjiQi59cpMGhn1HTG-gShnhxAYeltJyIDg1DhyEcCfZ-3JVA5kXZk1Qeh2pVRuKKI9FK8_ktFUIZ9JdFmWt1YnP8zOdELw_yyQBSE5nPuOTm6X9fdTHAyH4Ig434dG31pcDQtLucVRcKlcZBDUAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💀
این ویدیو از سرعت تایپ مسی شدیدا داره تو رسانه ها وایرال میشه
حالا جدا از سرعت تایپش فکرشو بکن لیونل مسی با ثروت تخمینی 1.1 میلیارد دلاری گوشی ای که دستشه آیفون15 هستش
بعد یه‌سری جوونای ایرانی با هزارتا قسط و قرض و بدبختی میرن آیفون17 میخرن و تو چشم همدیگه میکنن
از یه طرف هم بعضی دخترا میان میگن پسری که آیفون17 نداره کنسله و ...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70757" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=hzSrBM4ph_AD3N89LvREd-nFnZl0FXWKIdWAcZaxqEXX15rThyY3GjiaxLFObjh4YnP97fBxT7OF0OTbqtau7dylM-QGg7rUXOZyVh8AA5UWNZq0MjG7TuMkaUg0jorCixk3vPgh2ftDVFtYhHW3LSIqoGesuPI48J7qWA93_tyVVSYphXy8Yj_caPPsrH54jrpB1SA531MzVKn78JQfRHgzXAQx1jipaXbajS4CI2KElutwSUpCf86e6FD7JLYXJAhVLanll1H2nVHl3i4_PHiiJ9URQDCCSeG978qU-zdZT2Mev4Owh9N7ALKhZl2A7hI5wiMY_eZ5KGxcQdxgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=hzSrBM4ph_AD3N89LvREd-nFnZl0FXWKIdWAcZaxqEXX15rThyY3GjiaxLFObjh4YnP97fBxT7OF0OTbqtau7dylM-QGg7rUXOZyVh8AA5UWNZq0MjG7TuMkaUg0jorCixk3vPgh2ftDVFtYhHW3LSIqoGesuPI48J7qWA93_tyVVSYphXy8Yj_caPPsrH54jrpB1SA531MzVKn78JQfRHgzXAQx1jipaXbajS4CI2KElutwSUpCf86e6FD7JLYXJAhVLanll1H2nVHl3i4_PHiiJ9URQDCCSeG978qU-zdZT2Mev4Owh9N7ALKhZl2A7hI5wiMY_eZ5KGxcQdxgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار در گفتگو با شاهنشاه آریامهر:
آمریکا و بریتانیا نیز، که احساس می‌کنند رژیم شما غیردموکراتیک است. شما چگونه به آن پاسخ می‌دهید؟
❤️
شاهنشاه آریامهر:
خب، من به آن پاسخ می‌دهم و می‌گویم که رژیم شما دموکراتیک‌تر از ما نیست، زیرا به نام دموکراسی، شما کارهایی را انجام می‌دهید که ما از آن‌ها وحشت داریم.
هیچ برابری بین مردم شما وجود ندارد.
تفاوت بیشتری در سطح زندگی و ثروت بین مردم شما نسبت به مردم ما وجود دارد.
🎙
خبرنگار:
آیا اینطور است؟
❤️
محمدرضا شاه:
فقط ببینید چند میلیاردر دارید و چند فقیر.
در اینجا، ثروت کشور، حداقل ما پنج قلم مواد غذایی را یارانه می‌دهیم
تمام آموزش رایگان است.
در سراسر دانشگاه، ما حتی به دانشجویان پول توجیبی می‌دهیم.
🎙
خبرنگار:
خب، اجازه دهید به شما بگویم که آقای کالاهان (نخست‌وزیر بریتانیا) مانند شما در یک دفتر کار نمی‌کند. شما چگونه به آن پاسخ می‌دهید؟
❤️
محمدرضا شاه:
آقای کالاهان نخست وزیر است.
من شاه شاهان کشوری هستم که دو هزار و پانصد سال سلطنت دارد، اما این کاخ را نمی‌توان با کاخ باکینگهام مقایسه کرد.
قیمت کاخ باکینگهام صد برابر بیشتر از قیمت این یکی است.
در گذشته، شما، بریتانیایی‌ها و دیگران که در اینجا نفوذ داشتید، می‌توانستید نخست وزیران را به دلخواه خود تغییر دهید و در امور داخلی ما دخالت کنید.
آیا برای آن زمان از دست رفته متاسف هستید؟ آیا همان چیز را می‌خواهید، دخالت در امور داخلی ما؟
ما به شما اجازه نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70756" target="_blank">📅 15:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70755">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1PkKsxapeNu2CTRUDDNN7shMccSPSEc42cA-3LKFiAj6FEN1_pINleI1biLjnnSfSroNo-1mGua3rG5PMg2Z41fb8P4CrKL8zlfFpBvwmjr_mr8aC_ntEVNWgTwN3apYLlhdPUsv4ec4uu7fAJQ4hJmf9ahyIm8GgrpkoGlEQyKNwR1hzvDOOjEtnfU2Nvsw_nITf-sA-Qf-amsFCqyn_Uy8Nb4N3dxlmeoA9e0psz-uXE07rq87cZw9P3_axUehDyo53tUBi55TLhcrmiUJkpwH32tSXC_iA0r1K4aaZYSZWDu1t58LE52H3kFtgy_NFq56XZh6zws1xv9MGMUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
اطلاعات ما حاکی از تلاش‌های گسترده برای دستکاری بازارهای انرژی است.
عناصری در دولت آمریکا با بهره‌گیری از رسانه‌های ساده‌لوح، سعی دارند برای منافع شخصی بر قیمت‌ها تأثیر بگذارند و رئیس‌جمهور آمریکا را همچنان درگیر جنگی بازنده نگه دارند.
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه، بر طبل جنگ می‌کوبند.
این مصرف‌کنندگان آمریکایی هستند که پیامدهای واقعی این وضعیت را با تمام وجود حس می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70755" target="_blank">📅 15:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70754">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQS7cPFiVJuGf1Z6J_hX02PhYeAEbi5O15vGP0ewykMAlaWeNTRdP2bGtrXFyVYS0xrTtnlRQPvkFtTtsLSWHW7Odyi8MV3Fczeqxm4eQNrn8o5P5XjuumqPz74qRIpvcMKbU6yTGttqRm4XDWapDEp0xyeo3NkHHP57khXSeKGkIwSrZpJbATaJjBoug4i1_H2FIV5cQgC5NkwnHtsQc5yHJR4M1HxHfm7VAewLR7C7fhfcyHSTVkM39SYehh9hxeWv9rOA6f295iiReKd4Ttfw2QfNbFuZCqvVH7H2O4XriW33xuqpxK2tFEry6bgJnn0N8LJC_wdFGzeYNSg60TTU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQS7cPFiVJuGf1Z6J_hX02PhYeAEbi5O15vGP0ewykMAlaWeNTRdP2bGtrXFyVYS0xrTtnlRQPvkFtTtsLSWHW7Odyi8MV3Fczeqxm4eQNrn8o5P5XjuumqPz74qRIpvcMKbU6yTGttqRm4XDWapDEp0xyeo3NkHHP57khXSeKGkIwSrZpJbATaJjBoug4i1_H2FIV5cQgC5NkwnHtsQc5yHJR4M1HxHfm7VAewLR7C7fhfcyHSTVkM39SYehh9hxeWv9rOA6f295iiReKd4Ttfw2QfNbFuZCqvVH7H2O4XriW33xuqpxK2tFEry6bgJnn0N8LJC_wdFGzeYNSg60TTU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
مراد ویسی:
۱۵ هزار میلیارد برای شیر مدارس «نبود» — ۱۵۰ هزار میلیارد برای خانه‌سازی حزب‌الله لبنان «بود».
بودجه شیر مدارس بچه‌های ایرانی قطع شد. عددش ۱۵ هزار میلیارد تومان بود؛ گفتند نداریم.
در همان حال، ده برابر آن — ۱۵۰ هزار میلیارد تومان — برای ساختن خانه برای اعضای حزب‌الله لبنان پرداخت شد.
وقتی می‌گوییم اینها ایرانی نیستند، عرق ایرانی ندارند، بعضی‌ها معترض می‌شوند. اما ایرانی بودن به این نیست که در مشهد و تهران و کرمانشاه و اهواز و کرمان به دنیا آمده باشی.
وقتی پول شیر مدرسه را نمی‌دهی و ده برابرش را به بیرون از مرز می‌فرستی، معلوم است که منافع ایران برایت مهم نیست.
بازنشسته معوقه‌اش را نمی‌گیرد.
گندم‌کار طلبش را نمی‌گیرد.
پرستار اضافه‌کارش را نمی‌گیرد.
بچه مدرسه‌ای شیرش را نمی‌گیرد.
اما بودجه هزار حوزه علمیه سر جایش است.
اینها حکومت نکرده‌اند؛ منصب حکومت را اشغال کرده‌اند. اشغالگرند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70754" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70753">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=hC1x8Nd-T6oiDbJIHv1Q25UdfD2QM6mhiSJTHnyN3neX7jctbtgwjfqb_v9TDjybxXrQAAe8E7NByE7E4S3UEXNMp45NorsUWByPuIznMfiwaM51y3rSQZZfpCvkCdU20F1oyIzElRYGcDJZVbi7Ppz3wwpui9xVEMk59RSbqlX5KR-myce_cqVnZEsgrfMtmjt-DJpb4Sb-HQy6fAy92sXtKUf-Rwk4R64Q5huUj9tIUjWTI-X_MyEj0QcCGRDOXR6YY-0s9s6nBWdTZphAt0nqDVpJoTFbUC9XN1RmuP4iWuJMs1idYXMn5rZud3hSDM2NVXDm7vrd8Iec-646o4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=hC1x8Nd-T6oiDbJIHv1Q25UdfD2QM6mhiSJTHnyN3neX7jctbtgwjfqb_v9TDjybxXrQAAe8E7NByE7E4S3UEXNMp45NorsUWByPuIznMfiwaM51y3rSQZZfpCvkCdU20F1oyIzElRYGcDJZVbi7Ppz3wwpui9xVEMk59RSbqlX5KR-myce_cqVnZEsgrfMtmjt-DJpb4Sb-HQy6fAy92sXtKUf-Rwk4R64Q5huUj9tIUjWTI-X_MyEj0QcCGRDOXR6YY-0s9s6nBWdTZphAt0nqDVpJoTFbUC9XN1RmuP4iWuJMs1idYXMn5rZud3hSDM2NVXDm7vrd8Iec-646o4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از شیرجه زدن تو استخر یه پیرزن دزفولی 85 ساله در بانمک ترین شکل ممکن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70753" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70752">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu-cDaU6iOcW13YpnTJlyGM7pN4ekQINLbnh6pJdVwnGrOtw07-jZMq57OFb12hi0A-6Xf5CrsgY9AHPUBYb_dunjKSZTw7nmb8Luq-Ho6ZEsSgkV-hkttLKlswpF3r44s3cmqxr9yne3UGowFWCQ1gfTLXTvHbwEs2fnpOUxh76MDq2PvnpmYzt3vGPA7lkX__vtRMy47TuakyYYKcToXj6zpb7GoIc_AK7HkF5IiXiqyaxlkBLbzDT-PWH6fc9zQ10l8uZHXQ7UJ-QSbL_H4vUN2vRLvGKVfP_RvRAYetFQiwK1QpKrAlNeXIXxMY8Jvsol0xv2inYdqNQPCYKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بنر یک عرزشی در تجمعات شبانه:
آمدیم امام زمان را بیاوریم
مجتبی خامنه ای رهبرمان را هم به غیبت بردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70752" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70751">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=CI6H0iHlzv1u31kccjH3wRWadFkpj6mJiyGh8pTj-ATY24c7p5TAd5KqO4oWm1F5aDRtZTlsrlrLgcTG_Et36dGA0T1RWef7LZDYKyxuL1oxHx0Ta24W3pxD7OwBZr8YUYtTuR0SixqaJKqIY8RMI21kXoluJ8qLTPEV9hRi7sepbJkgtClFsNS_s-mSOemqC3NQchYupdCC5RCfob9I_wz_zT9WXYyBduFSK8S5uz9TFwDdz-eF5myhooI_luCcApe-IaAPqv0ahaja07Vg_Zva65W4zMAsLKX77gVCVb01-PBiVKB05NMc0Oxzj_WP-Xgrb6ZYm-u4pAu1-TDc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=CI6H0iHlzv1u31kccjH3wRWadFkpj6mJiyGh8pTj-ATY24c7p5TAd5KqO4oWm1F5aDRtZTlsrlrLgcTG_Et36dGA0T1RWef7LZDYKyxuL1oxHx0Ta24W3pxD7OwBZr8YUYtTuR0SixqaJKqIY8RMI21kXoluJ8qLTPEV9hRi7sepbJkgtClFsNS_s-mSOemqC3NQchYupdCC5RCfob9I_wz_zT9WXYyBduFSK8S5uz9TFwDdz-eF5myhooI_luCcApe-IaAPqv0ahaja07Vg_Zva65W4zMAsLKX77gVCVb01-PBiVKB05NMc0Oxzj_WP-Xgrb6ZYm-u4pAu1-TDc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجتبی خامنه‌ای:‌
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
🇮🇷
پزشکیان بعد اینکه مجتبی خامنه‌ای گفت "دولت نباید ضعف‌ها رو علنی کنه" :
واقعیت اینه که ما پول نداریم، درآمدمون کمتر و مشکلات‌مون بیشتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70751" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70750">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVbj2_xG_LLf8qTo33diQRYbJbMvXoJpCM-F8b0Q9_3R7WvEm-Al8fam1jxycQW1XsYlwlbro9v2RPTCgDfO8ZS6iCYhEq57Iz-QJO0GHVL4RWEgvSxVDjqn39XM1qFfbigMxUbQdhWUwbu_QzJu15DG1pW5Y3VkdEvTn2uWrQkD1-12d_NrXrIKLLjLiNkvpuaxLcANnajQheRBu6ObD8qcXVdXh7yI0SxYX-lJjO7if5KUIWXpBQMLhBOwfXxUFUBuoZviUoT9XvNHSN63C1rFE4o1pKahI4V58zCLF3Av9mar6MItrIEC_FgN3HcPIlAvjIrRt0Z_klwZuJ0iPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
گلدمن ساکس:
صادرات نفت خلیج فارس به سطح ۱۵ تا ۱۶ میلیون بشکه در روز بازگشته است که حدود دو‌سومِ میزانِ پیش از جنگ محسوب می‌شود.
نفتکش‌ها به‌طور فزاینده‌ای با خاموش کردن سیستم‌های ردیابی («رفتن به حالت نامرئی») و استفاده از روش انتقال نفت از کشتی به کشتی، سعی در دور زدن اختلالات دارند؛ اقدامی که به کاهش قیمت نفت از بیش از ۱۲۰ دلار در ماه آوریل به حدود ۸۹ دلار کمک کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70750" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70748">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=MJ7N9T9g3oRBlTHR3nhILE4jsOuVQnnUx3N1r1E6Ha2KrS2kc0ca8JKEIiSbFzxJuhnCF3zBjn-pSdFGNmKy_BkPjMncWyBweQ1_zdJIC5pJlfnkm2dWdFUvQg6zXv95IeFNXlB6YgSk_rurOG6CPT4F2Y-oOIa55E5FRDcYcN4p5BSW77Rx1PT83gQ3ImllmGXQwfw8ieCf6bMwSnTNSYj4aXt3KPBPX7B1x5mfy_oaKVbSsuhX0pofuXzet6DHK6-2hvVBuFrWo-7DMml7242sTcpdExVP8SljAKr55aVANP3TPwVSiyp-ppa8n3XWz42eQR1VsFqEEgTbOdjpoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=MJ7N9T9g3oRBlTHR3nhILE4jsOuVQnnUx3N1r1E6Ha2KrS2kc0ca8JKEIiSbFzxJuhnCF3zBjn-pSdFGNmKy_BkPjMncWyBweQ1_zdJIC5pJlfnkm2dWdFUvQg6zXv95IeFNXlB6YgSk_rurOG6CPT4F2Y-oOIa55E5FRDcYcN4p5BSW77Rx1PT83gQ3ImllmGXQwfw8ieCf6bMwSnTNSYj4aXt3KPBPX7B1x5mfy_oaKVbSsuhX0pofuXzet6DHK6-2hvVBuFrWo-7DMml7242sTcpdExVP8SljAKr55aVANP3TPwVSiyp-ppa8n3XWz42eQR1VsFqEEgTbOdjpoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روزی هست که اکسپلور تحت سیطره این بانوی بلوند ایرانیه؛
و خیلی‌ها از ایشون با عنوان "قرمه سبزی جاافتاده" یاد کردن...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70748" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70747">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70747" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70746">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k__yYk2EmbCXG1mjKzGJrLVkuiHjiDCDA_kg8Jwv9R_amLrz_givQGpUhAgGZ0tIUAZJ69j6g9j11wz20B7Frz2YdtE_kgCOVMULiq0qhsPYi4L6GSvrxZtFB8abWqg4822vBfQFRAJcuV3gjlEoqdACL-vyn0s9pAlVw3z4ptMy6EOavEsg_EWI10bSTzWH7U1Ri1SW7VnCqA4wXoH3NH7ma2T593fqBJwV-Yff09humUmNwT4jLjIqEpg43BC-1b10R9PQNfPwWsebFSA6Qunz0Evk1lgHkTyXhZsXaT1ioa7JIR8jTveTfROF9bXJW2yZHjJCRS4eZvXlhPgHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70746" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70745">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=EJtTHe7L02qWYwQH1VFEB20D5Ej1NLbE2KEiSZkSk4ofEdnk1pLaR7USBpKlErPSukdXCvBXR5-xrzB8_ewyXeWEoU8kBbkKFqKYvC8wWVKeeWdxEgdO31xBS_pC23VkSmpm9aIJmLGBBHRYJGIfvyoN1bDUPF-2waj4ntDrT-Z-khBg_Wv9EDcNAu2o8bUUlIKSi60ir9PKw9TBCJ8QUBzZoneqAAOP2uhtqO-1ZkE6IjSV1snfe6fWQdIWPXRILDhTllAd5eeeLKu_9iBN7wFHQvl2vKLwrLgZLeRBu9eM5uxc5OpPb8rto50JryTYFnq6E_x6ZasLaGOHMiq1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=EJtTHe7L02qWYwQH1VFEB20D5Ej1NLbE2KEiSZkSk4ofEdnk1pLaR7USBpKlErPSukdXCvBXR5-xrzB8_ewyXeWEoU8kBbkKFqKYvC8wWVKeeWdxEgdO31xBS_pC23VkSmpm9aIJmLGBBHRYJGIfvyoN1bDUPF-2waj4ntDrT-Z-khBg_Wv9EDcNAu2o8bUUlIKSi60ir9PKw9TBCJ8QUBzZoneqAAOP2uhtqO-1ZkE6IjSV1snfe6fWQdIWPXRILDhTllAd5eeeLKu_9iBN7wFHQvl2vKLwrLgZLeRBu9eM5uxc5OpPb8rto50JryTYFnq6E_x6ZasLaGOHMiq1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شعرخوانی محسن نامجو درباره علی خامنه‌ای و جمهوری اسلامی، شهریور ۱۴۰۱:
یک روز مار صدسرتان می‌رود به گا
آئین خوک‌پرورتان می‌رود به گا
سیدعلی اصغرتان می‌رود به گا
سیخ و سنگ سرورتان می‌رود به گا
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70745" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70744">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OagWVC6iVK7XYua4MBK57wSexmRQ_yp3AqYBCQTQKEEa-Jhjibtas5bhbvOg623PHw8s8K_vFMfVIpsy0GDgnI_4Ie_gvu0TAP6eEsyZcIAB-87RMHvOXKFhSdIklG5VHALVzAB5tChdE-0TuTNrkUdM3O9HGxAs4fYmCk_GA7TgQB_vGMWpooqVk4thi_HlgnZ2sDp8oi3pyRczWgIlIfI2fu9lsUd9hHorUMusXS45sEyUIHLcohmgvb5L3ZiXOGkeIo89mqtpcBVmgs5tllsTpq93WW9fN8ecydP9s91kpoBuGgaujgNVmQnZwf2NFE685v1tGEY3YKgqM9oP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:
به گفته مقامات آمریکایی، ایالات متحده مقادیر زیادی موشک و سامانه دفاع هوایی را برای جنگ با ایران به خاورمیانه منتقل کرده و برخی از ذخایر خود در اروپا و آسیا را در سطح بسیار پایینی نگه داشته است.
به گفته مقامات آمریکایی، پاتریوت، ATACMS و سایر سلاح‌های دقیق به شدت تخلیه شده‌اند، در حالی که رهگیرهای THAAD و سیستم‌های ضد پهپاد نیز به منطقه منتقل شده‌اند. تکمیل موجودی انبارها می‌تواند سال‌ها طول بکشد.
این کمبودها، فرماندهان آمریکایی را مجبور به تنظیم برنامه‌های احتمالی کرده و نگرانی‌هایی را در مورد توانایی واشنگتن برای پاسخ همزمان به حمله احتمالی چین به تایوان یا تهدید روسیه علیه ناتو ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70744" target="_blank">📅 11:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70743">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Y4nOvvHQdy8ZkPx80CnyyfMjLUcbuO0wnO43Y4T8xcLwJQ6CEPSmbj7OJnZkNO1Ogc9K4GpUhuY08FTzplDsOvXz1TvLmkIyJ04RPvTRCMmHCbw764DVs4gOI5ycQ2VM6o7wFywEmKoUoadXwV7z6ZFIE8zDSZp7PWMnYK778A0Qxbp2fWXT0Nbi0zjeVOE_EUg1SbS-SfjKdEu1LRNUGV82Uovz74wMxVyZKpRM_voy48-KjumbIQww8dPq8ZFryNErNhgm6k4woVdTrqNJDFNYL8gyfblOPorT8sJs38hoRy4opX-ncnzfQ2Y4OGtYdlJQIQKg-fJ_UtgANNECNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Y4nOvvHQdy8ZkPx80CnyyfMjLUcbuO0wnO43Y4T8xcLwJQ6CEPSmbj7OJnZkNO1Ogc9K4GpUhuY08FTzplDsOvXz1TvLmkIyJ04RPvTRCMmHCbw764DVs4gOI5ycQ2VM6o7wFywEmKoUoadXwV7z6ZFIE8zDSZp7PWMnYK778A0Qxbp2fWXT0Nbi0zjeVOE_EUg1SbS-SfjKdEu1LRNUGV82Uovz74wMxVyZKpRM_voy48-KjumbIQww8dPq8ZFryNErNhgm6k4woVdTrqNJDFNYL8gyfblOPorT8sJs38hoRy4opX-ncnzfQ2Y4OGtYdlJQIQKg-fJ_UtgANNECNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک دختر ۱۶ساله رفته تست بارداری گرفته و تستش مثبت شده:
فقط لرزش پاهاشو ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70743" target="_blank">📅 11:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70742">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=D5ftbIN9Uvtet-sO7tpl_BAsDzRHVX1ADTY0_Lpyrl54OLJB2D355cHPd5pwGxA8t9J7HAu4n1tVHBAvmMxLV5HFlLkf_Saw_MwpNN4NdyerTYuyxH3dA4vI8WiS3LQwGu8Huv6oXFuhWYfmXmwvmxmFmTa_CY5Nw--T2Zp5MozdwS8o6DNuv_d7aNVho_3dXHHkOKq-5fYHTnKQlW7EwJZNcbC8aBSrHvk5qSktGbhbJFnXkIJWXQWZcpQCmFb2CpCQTr5zy7bDKzzcOZQw36MokdbMcAP_0FmL_TnN6XUx4-vHzm2xHNdu9H4nNMnT4IMPZFPJwunLiAxsoNs4UzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=D5ftbIN9Uvtet-sO7tpl_BAsDzRHVX1ADTY0_Lpyrl54OLJB2D355cHPd5pwGxA8t9J7HAu4n1tVHBAvmMxLV5HFlLkf_Saw_MwpNN4NdyerTYuyxH3dA4vI8WiS3LQwGu8Huv6oXFuhWYfmXmwvmxmFmTa_CY5Nw--T2Zp5MozdwS8o6DNuv_d7aNVho_3dXHHkOKq-5fYHTnKQlW7EwJZNcbC8aBSrHvk5qSktGbhbJFnXkIJWXQWZcpQCmFb2CpCQTr5zy7bDKzzcOZQw36MokdbMcAP_0FmL_TnN6XUx4-vHzm2xHNdu9H4nNMnT4IMPZFPJwunLiAxsoNs4UzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آیسان اسلامی درباره شاهزاده رضا پهلوی:
طرف میاد میگه این که نمیتونه تو ایران نبوده د آخه خارکصه برای مسافرت که نرفته پدرشو کشتید
میخاید برگرده ایران بکنن زندان مثل تتلو عکس بزنیم آزادش کنید؟
سیاست مدار نباید مهربون باشه که انقد حرف بهش بگن
خارکصه ها خامنه‌ای رو دیدید؟؟ کسی خایه نمیکرد بهش پخ بگه بعد میاین انتقاد میکنید؟
خامنه ای خار روحانی خاتمی احمدی نژاد رفسنجانی (پدرنظام رو گایید)
خب دیدین که با رای دادن نمیتونین جلو اینا باشین چرا پس ۵۰ هزار کشته دادیم ما
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70742" target="_blank">📅 10:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70741">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=HDfkGbSamYa3q-HLsayN3UvJyGMYwf2bo02Vsl8JYj-QivzfG1wFon50wAWwUhHNoXJVvdxlIp9hvQWOFiapoJGFZ-yT4etyQNYy6ZhCoxNE9nVuH9dDoMkm8a7WkGafPfXw96RuDYzSYqAxjunSBj7XG4MBaNYGOZj_FslCOIXi7DSAItq96hGIwvq_cIx5kQ08X7bXo_XxGanfqnX6naoYDWX7_zEDAJz6Jdil2RxTN87pMG0-14v4AaAt_dVMgSd3Xxps55NEZBseuOskErQKVpBmScG8nofXPDgzEE-gDz5IHrapkv0iHwmGCU1ACcj-980uVLXpQuLVdz2x1o6TXhk20dXnZfu2sLdflePCgAIQgdPJO3OJoC7BH6kYx6UCMT18jPvdTVMoiBMkMdKpPVUQgOw4bIPvSKMJxQuT_J_-GjHKUMAf4O3uJmx0_jTdvaUiA9y0LObAFAJlsfkvFc6dRUZ7GUasXaPnZy_DRt9np4EvDmp6nwq1BCf9ahNrEL501lNObodG757ggVQfeC7P5ztxfSW9z37F0ZjSj344Zkk60HzHEuR4_ooEEj98ZirspS6YluEeWGzaVY1_RTdOGh5Cqkyst4Lab2pYRdLzgtPeqtDzb-1y03htFhvP2q0HfFg8ieJ4A1TwlxaIvm4iPNw7ULhH66J4nkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=HDfkGbSamYa3q-HLsayN3UvJyGMYwf2bo02Vsl8JYj-QivzfG1wFon50wAWwUhHNoXJVvdxlIp9hvQWOFiapoJGFZ-yT4etyQNYy6ZhCoxNE9nVuH9dDoMkm8a7WkGafPfXw96RuDYzSYqAxjunSBj7XG4MBaNYGOZj_FslCOIXi7DSAItq96hGIwvq_cIx5kQ08X7bXo_XxGanfqnX6naoYDWX7_zEDAJz6Jdil2RxTN87pMG0-14v4AaAt_dVMgSd3Xxps55NEZBseuOskErQKVpBmScG8nofXPDgzEE-gDz5IHrapkv0iHwmGCU1ACcj-980uVLXpQuLVdz2x1o6TXhk20dXnZfu2sLdflePCgAIQgdPJO3OJoC7BH6kYx6UCMT18jPvdTVMoiBMkMdKpPVUQgOw4bIPvSKMJxQuT_J_-GjHKUMAf4O3uJmx0_jTdvaUiA9y0LObAFAJlsfkvFc6dRUZ7GUasXaPnZy_DRt9np4EvDmp6nwq1BCf9ahNrEL501lNObodG757ggVQfeC7P5ztxfSW9z37F0ZjSj344Zkk60HzHEuR4_ooEEj98ZirspS6YluEeWGzaVY1_RTdOGh5Cqkyst4Lab2pYRdLzgtPeqtDzb-1y03htFhvP2q0HfFg8ieJ4A1TwlxaIvm4iPNw7ULhH66J4nkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
این ویدیو تو اینستاگرام فارسی از شدت طبیعی بودنش شمارو وارد طبیعت میکنه و یادتون میره که این فقط یه کلیپ:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70741" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70740">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=s1GZkCQfZQyhMwzhsCwXZeLTyXrBwgt4YvPedGXmj3NORLC8GxxchMwMHSYmYztms2szU548T94ACRg1Ifntc_Dn_MMElUmmsff5ZPUqQiFK3bQdcgZoH5Zwgb-U_CMZZRAmOrgEDsCX9re5mzOp3YUgdp9Jt8PRNj8LxM6e__1C8zlbwAQeIhVAnUsc3fDWkLZfMd6MQvBqRL4G5cjakGr7uMc_XIj736nehoiFuLH2cgq6fHcX637XEBxjnKyGkAU4otFYwbUuo_gdttS78JHFk1gPIHh_8tcM2hBbo9az9wqLx3obvftwHltdzzBIFkdNCQbWSmVxZjpn30zuFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=s1GZkCQfZQyhMwzhsCwXZeLTyXrBwgt4YvPedGXmj3NORLC8GxxchMwMHSYmYztms2szU548T94ACRg1Ifntc_Dn_MMElUmmsff5ZPUqQiFK3bQdcgZoH5Zwgb-U_CMZZRAmOrgEDsCX9re5mzOp3YUgdp9Jt8PRNj8LxM6e__1C8zlbwAQeIhVAnUsc3fDWkLZfMd6MQvBqRL4G5cjakGr7uMc_XIj736nehoiFuLH2cgq6fHcX637XEBxjnKyGkAU4otFYwbUuo_gdttS78JHFk1gPIHh_8tcM2hBbo9az9wqLx3obvftwHltdzzBIFkdNCQbWSmVxZjpn30zuFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال‌ شده از گلایه‌های مالی یه ستوان سومِ نیروی انتظامی:
تا صبح میرم گشت‌زنی و حقوق خالص من 21 تومنه!
با این حقوق حتی غذای خانواده هم نمی‌تونم تا آخرماه تأمین کنم.
به هرکی هم می‌گیم جواب میده که دست ما نیست.
من نه ضد نظامم نه هیچی، آقا به فکر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70740" target="_blank">📅 09:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70739">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCboOqbbA6HIEvh-KL-HKGusrjtU2LW1jdeiZO2Bpk3_l3UsR9g9d1rGhftNygU_ISzKoUK07KuVRO0UfYj1Go5HhgHS_4xcIuFnRML6-OIrvD6jg2DwiPe4yL09IbCIpeLPmseQIAH4BhXIQQfNvJgGytDDh9aMqWnCR36ZiFJTw5QL987j52pMRLEWMOwSfcRrTCbtZjS1YJpZXQAHgmxc53BCXwM12TtuN12FEl_Feq1lLMxWkuka0ssz_x3AeVXTjXp3nNfCreLpMUmPlhRkBd5ISNrTD6iNNrEvo5WMLVfn_5iLP-m3167aiBb-95Hro5MhhseFy-6i-huRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
باراک راوید:
بیش از ۲۰۰ شیء شبیه به مین از مسیر اصلی این تنگه پاکسازی شده است.
مقامات آمریکایی می‌گویند تنها ۱۱ مورد از آن‌ها مین واقعی بودند و تعداد اندکی نیز به شکل اصولی کار گذاشته شده بودند.
تنگه هرمز باز است و آمریکا در «نبرد هرمز»دست بالاتر را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70739" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNO5hdDg9T5AdRqPbRkUzWxqH0eWcMBPIeMIFi5SFzxOCnhRzryylvqKDYGlM5aW0gHo7hhtNCEBrcmv8hWJnhNYzrOOONCpjzeNJQiGB92AgqZd79KuzGziiIacQQr1j6Ff4a5oX3pvJ9eQr8PA1NKN5HadwWW0gwdsKb6vwOPMb2Qh-NAjHkq-I9ySdT3rCiqxEZp75B3r07XTSJHaxvcihwvQAuer5vLEn4PVRedJ-Y9dySdsxS56R2DcEgp_Da4kASuMK_JKP3UCJKua7cxJyX8rVtr2NLg4rQ8cMIwxdTp5iikQBth1YSsx32BkeR9dq4acBm32p3v3CaMqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70735">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owfll3_Odd1AnMpIl6H5Euif90ruprKtBsIOnw0W-hdvEilts43UE1lp1jt6fv16Uu2gAtQ3-iOGtMXC5-OZnme00ybwwkXQ5G_-OzgVO7QGVOtSDs_Pt0whYYqESFdTaWkyESio3N3WA1LZt_JlpyCvI6haHq6rj-_mX4ehi0Q0T14rPjC_5sUvBl5Q5o6emEZq7EihHTs7gCriyyfpBrGVYgre2MLb4jKMHM7U8X2PfbQaUGQuw0GWmg-EX-uasctGI8cDE-nAAM1NKQVORUJ1HlrcgYUu7greeACibIUQExJgWR7sZwyoNJ5XJin781wCa3yAj0S04BBtMwzFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مجری:
غیر از قرآن و نهج‌البلاغه، کتاب دیگری هم مطالعه می‌کنید؟
🇮🇷
پزشکیان
تا دلتان بخواهد. فکر می‌کنید همه حرف‌هایی که می‌زنم، فقط از همین منابع است؟
🎙
مجری:
آخرین کتابی که مطالعه کردید، چه بود؟
🇮🇷
پزشکیان:
آخرین کتابی که خواندم «فراجامعه» نویسنده آمریکایی بود.مگر می‌شود کتاب نخواند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70735" target="_blank">📅 01:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70734">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=MSdYImx-40Qx7Y1tZIcJZQgRA0GnfnLbSWBwtG4ePAMsbHt3xzeu2spD1ag37cUuI3xNmKoKKxr0WSGGTnFh0bYffWm9JsVY9hIYlk-xHaexNL9FIZUAaGRQV4RiD7DXXt54EGecz9l0gDkDhLZM351VPIaRWgUIGMq6KWsR6LZUPqu9w4HjrIz56nLD0GU1HF4c-owNhQyp5D_G_l9Lu1BcwKc4qzwUxA5x0Fm5pyG0_-eCqKAeoqKBVBcoPjNE0tf1ASadpkyrAjNWOdaBAeGhzH28G_B4aW2a4fi1DEC4CZDruji10rTB83ZkfVf9Qs81vp31ViYObLcdCqzfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=MSdYImx-40Qx7Y1tZIcJZQgRA0GnfnLbSWBwtG4ePAMsbHt3xzeu2spD1ag37cUuI3xNmKoKKxr0WSGGTnFh0bYffWm9JsVY9hIYlk-xHaexNL9FIZUAaGRQV4RiD7DXXt54EGecz9l0gDkDhLZM351VPIaRWgUIGMq6KWsR6LZUPqu9w4HjrIz56nLD0GU1HF4c-owNhQyp5D_G_l9Lu1BcwKc4qzwUxA5x0Fm5pyG0_-eCqKAeoqKBVBcoPjNE0tf1ASadpkyrAjNWOdaBAeGhzH28G_B4aW2a4fi1DEC4CZDruji10rTB83ZkfVf9Qs81vp31ViYObLcdCqzfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مسعود پزشکیان:
«زمانی که حتی پیش از وقوع هرگونه درگیری، با کسری بودجه ۱۵۰۰ هزار میلیارد ریالی مواجه بودیم... آیا این صرفاً ناشی از سوءمدیریت است؟ آیا این بدان معناست که مردم تورم را احساس نمی‌کنند؟»
«بدیهی است که ما در زمینه معیشت مردم مشکلاتی داریم. روشن است که... باید تا کنون میزان طرح کالابرگ الکترونیک را افزایش می‌دادیم. ما در برابر مردم شرمنده‌ایم.»
🇮🇷
پزشکیان:
«در این شرایط جنگ‌گونه و در این وضعیت اقتصادی
بگذارید بگویند
:
"من می‌توانم با همین شرایط و محدودیت‌ها مشکل را حل کنم"؛ آنگاه من دستشان را می‌بوسم.»
«نه اینکه به من بگویند "پول و منابع در اختیارم بگذار تا مشکل را حل کنم"
خب، اگر من پول داشتم که خودم حل میکردم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70734" target="_blank">📅 00:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70733">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bolGOO1OcbAizgh13eyxI9Fc9iVvKzyjswj6E5b5EimzM8KtNViJH8h9nHVw6j1PsHfrpLD4-Pgtc-okNQvizcwIzRCsq5yqwp7Fx1z5KLONtVsT1F4jX8_igDvgU2S9AJOOw8XwIQPJC_LgBMCA0-Ee2S5qP0fWqPQNjoT4uU_WPMCXSOqET02vqvcUrKNQmGnUrI3qUjE0Wsue32pZuBb_1hWjN1D-nzg2MDes9QVVCXfBI0xueF_HXBFNhpMc3BVuweLKQPUW-1-2odqt26gz8hazncxUyFhqUeUqBD0y0_iwGDX0sLeIIbRgj12tL2QojONlPLMSCgY3IYE7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇫
برای اولین بار تور افغانستان گردی برای مردم ایران موجود شد.
قیمت تور ۷ روزه‌، ناقابل ۵۰ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70733" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70732">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=j9d7iwDXhUquNB_4xSBXzzzlg1LZY7AAQwFJpFgyRdn3rW8OYu78LFRgkpHrN04RvLWFjjZ20XNNrFwSNNTwR27ALCDDw3uImU1wdPfWl6JgNFlb7IwtC8Dw8NcSX9bkM_aKYdIgjGTSX3CSHsPMSlvuJFRk9qclMw37ra9DMWVQ9isKlmLavQGAg_dGO1N96DkffWBWs_6TWtoyCEho7WU0O9VsqU4gJ3PansdGXqRcjQ--c4AFmpReTGHSGHP1Cufxyb6naEeHIz84spip-DYAcWo4GhMbA_OkWLlQ9dIgS2t2eDxs8ZHbTIYXRdc7_cey8WLvb_cE7tviLtrNWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=j9d7iwDXhUquNB_4xSBXzzzlg1LZY7AAQwFJpFgyRdn3rW8OYu78LFRgkpHrN04RvLWFjjZ20XNNrFwSNNTwR27ALCDDw3uImU1wdPfWl6JgNFlb7IwtC8Dw8NcSX9bkM_aKYdIgjGTSX3CSHsPMSlvuJFRk9qclMw37ra9DMWVQ9isKlmLavQGAg_dGO1N96DkffWBWs_6TWtoyCEho7WU0O9VsqU4gJ3PansdGXqRcjQ--c4AFmpReTGHSGHP1Cufxyb6naEeHIz84spip-DYAcWo4GhMbA_OkWLlQ9dIgS2t2eDxs8ZHbTIYXRdc7_cey8WLvb_cE7tviLtrNWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
بنزین لیتری ۱۰ هزار تومان !
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70732" target="_blank">📅 23:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=QKS1i-XqUzR3b7RwZYb51nOcg74VKR1WJW_j9jeGgxgxc7td9l-q8tsvbU4wJIL5yoGHqolEqkbrhenMMpVGVPKyU-gkfOY6p7e8tHFvgGKhIWiSsF0UkijVEZhA_M9GIzbgH4_BjEFlfEFaiJ8qugtNBoOlrF33gRVaMcXyFXKYhU2MK6BluJ52-cnI5aBntI2pXYQmIJicawqyEIe3P1BCvYYZis749_hGkF-aDmllmjc1N6PiWMXvcQNqURkuk8Os0wO-_iVDhyC51lE2QVdgYGwMJm0CsqHX7_RQI216WxOZkcf8HzZ2TIXv7coLxsjaYhNVxjcgN5PDvBpcrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=QKS1i-XqUzR3b7RwZYb51nOcg74VKR1WJW_j9jeGgxgxc7td9l-q8tsvbU4wJIL5yoGHqolEqkbrhenMMpVGVPKyU-gkfOY6p7e8tHFvgGKhIWiSsF0UkijVEZhA_M9GIzbgH4_BjEFlfEFaiJ8qugtNBoOlrF33gRVaMcXyFXKYhU2MK6BluJ52-cnI5aBntI2pXYQmIJicawqyEIe3P1BCvYYZis749_hGkF-aDmllmjc1N6PiWMXvcQNqURkuk8Os0wO-_iVDhyC51lE2QVdgYGwMJm0CsqHX7_RQI216WxOZkcf8HzZ2TIXv7coLxsjaYhNVxjcgN5PDvBpcrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای انتحاری اوکراینی از نوع «شاهد» به پایگاه هوایی «انگلس-۲» در روسیه حمله کردند؛ پایگاهی که میزبان بمب‌افکن‌های راهبردی نیروی هوافضای روسیه (VKS) است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70730" target="_blank">📅 23:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZBF84lXp8IzmPdUjxVdCQOKmJjKzCmazseZCrfIyLm4PfXMFzLFrkCQ1qGyfbTEBW1xVRIe3ozk2pACEeVDrd_92YK1A9wtJgWSvAoB2uSU2ZcqZ2ErvZnBKmu2AeiDAOMpaVYRe7Ne9qIiUXrppHoQnPGFOtPBswQ1IJ0wuvNSQHUnzi4rWlEKChIC0VeXssPVV40z6ibZ1JievDl80LvQe_w6uN-GM30NVhpwkF-_nb9tRmDINJzr5f_iyPbS0RGMndkBI4Ut3_Eb6uMw-npyK6d8rE_8m0TRdIDNp40qVe5-8sxpwZlTqR951ruNKwucUQPNse6K5mXziQj_XgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZBF84lXp8IzmPdUjxVdCQOKmJjKzCmazseZCrfIyLm4PfXMFzLFrkCQ1qGyfbTEBW1xVRIe3ozk2pACEeVDrd_92YK1A9wtJgWSvAoB2uSU2ZcqZ2ErvZnBKmu2AeiDAOMpaVYRe7Ne9qIiUXrppHoQnPGFOtPBswQ1IJ0wuvNSQHUnzi4rWlEKChIC0VeXssPVV40z6ibZ1JievDl80LvQe_w6uN-GM30NVhpwkF-_nb9tRmDINJzr5f_iyPbS0RGMndkBI4Ut3_Eb6uMw-npyK6d8rE_8m0TRdIDNp40qVe5-8sxpwZlTqR951ruNKwucUQPNse6K5mXziQj_XgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبتای یه مداح؛
روزی بود یه میلیون حسابم داشتم رفتم ده میلیون چیز میز خریدم تازه پونصد هم حسابم موند
خاک تو سر مسئولی که چوب میندازه لای چرخ اداره این مملکت
اصلا دلار بشه یه میلیارد رزق ما دست خداس نه دلار
دلار ۲۰۰ تومنی هزار تومنی ۱۰۰ تومنی همش یه عدده مهم نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70729" target="_blank">📅 22:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
چندین موشک ضد کشتی از سیریک به طرف تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70728" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70727">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=a9nn6lgLkj74DpaMOXPA-8mI5_IBI2L8pj8BWEoT4WAZbO3Q1OFTPMPEdkdyquCDZ15b9WUGNzp0RVQe-5iYz5qSE53kHzBezLIlghXz1dc_TcBseCHsC5CbtdJ93ykHsvJh4nBMBl-RuicKNbnR7dKHP0BoC4A-dg5YxOpaZV0O1Rcw3LfrxSFbKOBeV4XT2c0bBzSCv10nAkMubhyQ8S9fGkXIhy5LYeOoBnLyhfzMcjykOtt6BgGl53t818K3HJTKCxWzAcJnI0huQiU7PG3aOJEIxJfuM1dGan7bzcYLCRAJ37Le31hvWVhF0ILTujNJ8DGoajfviKnuvHyl4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=a9nn6lgLkj74DpaMOXPA-8mI5_IBI2L8pj8BWEoT4WAZbO3Q1OFTPMPEdkdyquCDZ15b9WUGNzp0RVQe-5iYz5qSE53kHzBezLIlghXz1dc_TcBseCHsC5CbtdJ93ykHsvJh4nBMBl-RuicKNbnR7dKHP0BoC4A-dg5YxOpaZV0O1Rcw3LfrxSFbKOBeV4XT2c0bBzSCv10nAkMubhyQ8S9fGkXIhy5LYeOoBnLyhfzMcjykOtt6BgGl53t818K3HJTKCxWzAcJnI0huQiU7PG3aOJEIxJfuM1dGan7bzcYLCRAJ37Le31hvWVhF0ILTujNJ8DGoajfviKnuvHyl4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجید شریفی:
جایگاه کره‌شمالی با جایگاه ایران اصلاً قابل مقایسه نیست
اگر ایران سمت سلاح اتمی برود، همین چین هم شما را تحریم خواهد کرد
مطمئن باشید به اندازه‌ای که روس ها مخالف اتمی شدن ایران هستند، آمریکایی ها مخالف نیستند؛ این را مطمئن باشید
بازی مناسبات قدرت است، بحث دوستی و اینجور چیزها نیست
به محض اینکه اعلام کنید سلاح هسته‌ای داشته باشیم، مطمئن باشید با تمام قوا حمله خواهند کرد، هیچ حد و مرز اخلاقی را رعایت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70727" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Wp-ecZfzuHFl7B53yQNyxRlT5oiJIX-jNjUZuUz4j8a3qp-L939WQgbyp-5eHCx_GE63VFf4i-Za2KFADqQitUOcsNUuGPPSr0JbKZ8OZ-ba-iZqtYHw7qMPeMEt0SjeXSYfULBCv8vD7HTFevlcYKUjIrY0S48bA2ICgFq1KW8Xd-klRkOt6UKaBvsZ1pUYQsO8JgNRqDeKanwCaPD2FRdwbZZ5VsZUB3S4M_v_8rEmzFWYg8jZFpDF5-1OEjJZpF0rk2l2xPty3T9nBe4dCtptxnq0RdZV-DYKKwznTY7V3QwCgYZyRnb7xlWPThluAHH6AGHnRFOPVNGR3Ncz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Wp-ecZfzuHFl7B53yQNyxRlT5oiJIX-jNjUZuUz4j8a3qp-L939WQgbyp-5eHCx_GE63VFf4i-Za2KFADqQitUOcsNUuGPPSr0JbKZ8OZ-ba-iZqtYHw7qMPeMEt0SjeXSYfULBCv8vD7HTFevlcYKUjIrY0S48bA2ICgFq1KW8Xd-klRkOt6UKaBvsZ1pUYQsO8JgNRqDeKanwCaPD2FRdwbZZ5VsZUB3S4M_v_8rEmzFWYg8jZFpDF5-1OEjJZpF0rk2l2xPty3T9nBe4dCtptxnq0RdZV-DYKKwznTY7V3QwCgYZyRnb7xlWPThluAHH6AGHnRFOPVNGR3Ncz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بعد از حذف شدن سوریه از کشورهای حامیِ تروریسم؛
احمد الشرع، رئیس‌جمهور سوریه، به یکی از فروشگاه‌های دمشق رفت و اولین تراکنش پرداخت با ویزاکارت(کارت بین‌المللی )رو انجام‌ داد...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70726" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70725">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=T8iKlOUPgq6kfona4Qsd6EjEHyUPZKjUKkmZAdnV5ZsKVsxJxeUd3DRHaSJDZ-kfoI-8jMP7THpYLEL2AUeD_wl5QhjWUHf2XeihNKgrLUsjTFqhIlAXlyTOBrMC49jfCQxDCSH6mKn1GlnW0BnZgFSTRLLsHD07seyv4AgCyk2pWjdYhutXBIaJp-rL41pINjcY5fH_aLIEbkwock-6iFXkvDY77YW5T1zoeo-tfEzAlQVJXSCBoYlWS43SIqmwqFEKgC34XesTLArKa0LIDFv5pY-utEDFW7zD8sItzr6Ue0S3-3RWfQfGpYS5jlUFVw5Dv4jH-rCeFp0fWt4A9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=T8iKlOUPgq6kfona4Qsd6EjEHyUPZKjUKkmZAdnV5ZsKVsxJxeUd3DRHaSJDZ-kfoI-8jMP7THpYLEL2AUeD_wl5QhjWUHf2XeihNKgrLUsjTFqhIlAXlyTOBrMC49jfCQxDCSH6mKn1GlnW0BnZgFSTRLLsHD07seyv4AgCyk2pWjdYhutXBIaJp-rL41pINjcY5fH_aLIEbkwock-6iFXkvDY77YW5T1zoeo-tfEzAlQVJXSCBoYlWS43SIqmwqFEKgC34XesTLArKa0LIDFv5pY-utEDFW7zD8sItzr6Ue0S3-3RWfQfGpYS5jlUFVw5Dv4jH-rCeFp0fWt4A9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇵
ویدیویی دیگر از آنچه در نپال رخ داد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70725" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70724">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouZmRCP3rhEOMuPfX1deZ8UHtzXX9QwcJKQBLZcuJ2G4MiRLUcIzJ-v3LezP42Cowj2AbCmyKlKgtDrnKzhe-ATqCSAMl402sIH8oLjU7P9W4Zuizz1crBfhWlVBClYWDP-Wzsg4ripsrZSdXnrw_WjLOXzHlgDiTU73wzDTjZW2OyvglmgyWDe4p3kWgQViAlR7AB44uV0iQE9vkqNkPf1sklzux8oN141j20IyeHxlamRFXBLx_g5pVAoSKik4qaj8vgOzfvDZy_9rL3hWJ11aTFi_CJmXeJug-xlYHAzI66ZApSWA9eF40ET3ujG9q1YtxRSa6Wc42u7CpCw5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داد که تمامی شریان‌های حیاتی اقتصادی باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید ناشی از رژیم ایران پایان دهد.
ما همچنین هشدار دادیم که حامیان و تسهیل‌کنندگان فعالیت‌های ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی بهره‌مند باشند.
بانک «مصر» (Banque Misr) در امارات تصمیم گرفت این واقعیت را به بهایی گزاف و از طریق تجربه‌ای دشوار دریابد؛ و امروز، ما نخستین گام را برای پاسخگو کردن این بانک در قبال حمایت‌های مستمر و فاحش آن از رژیم ایران برمی‌داریم.
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای جرایم مالی وزارت خزانه‌داری آمریکا (FinCEN) مقرراتی را پیشنهاد کرد که دسترسی «بانک مصر» (شعبه امارات) به خدمات بانکداری کارگزاری با مؤسسات مالی ایالات متحده را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری، «رضا محمد تأیدی» — مدیر شعبه دبی بانک ملی — و همچنین یک شرکت پوششی مستقر در هنگ‌کنگ را که در پولشویی وجوه برای یک صرافی ایرانیِ تحت تحریم نقش داشته است، تحریم کرد.
🔴
«عملیات طرد اقتصادی» در حال قطع آخرین شریان‌های حیاتی مالی است که رژیم ایران را سرپا نگه داشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70724" target="_blank">📅 19:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70723">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEvBJ9p-KjietcexcOSmyAU_UbaX_8yedCFM99cBcK8pdKtYUf66ZDSl5Kf0Ge2YqsU8imWqxZF6zeQHhbpFoVIt-riBAlI1ewuzErtHclUr4HogQ_NyCiV5WxDG86IYui4oB2Z6gir_eNkDk5azpz60H-iwvKoDSTb4sjRs_NwaqhfI3C6QmDKwvVwfGTHmW78yweR2hIPbXgBDOC7X4ROGrOGn8miwW_dX0duHdw71BVegnb4Va4SSlO2u77QH9mmKnl2VkhFobcyYOTXYvaOJD0PctiQ2wQhePVKBxgwICgjriB1bGNdyKR_L54VUSdQkzyE7X-1QK883AhuqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ: دیگر خبری از آن آدمِ مهربان نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70723" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=B2QaUSTI7t5lO8l3JJXJa3gX7uQiv8nwYmEcwAy3P571HXNyukBnYYDpUHsj8vq5MnXEXkSgfQxJUQ_6zdbQayWPeeEkW77eXdKvLA2T9FjwkM159kiQfWjYEZujw2ZwZcmtYdFM7pDMcaMoDriQioqYGOonJkupk5kUmSHqISFBG7OzgnaIIidxs1wIg3KMNhTAjQDW4MU3ce_M6gpd-8zzW5Apao-vEBxq5pjPtLt8puxxF7EOI-FlyQc5_BMazpOygQHdeJrzkW7_dbpAkDudgOGOAkZ_zSf4SWdUmMm04S-a4fb0F8nBC2KqJGV4UB5Q2TW1VUYI4DNCq7vDxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=B2QaUSTI7t5lO8l3JJXJa3gX7uQiv8nwYmEcwAy3P571HXNyukBnYYDpUHsj8vq5MnXEXkSgfQxJUQ_6zdbQayWPeeEkW77eXdKvLA2T9FjwkM159kiQfWjYEZujw2ZwZcmtYdFM7pDMcaMoDriQioqYGOonJkupk5kUmSHqISFBG7OzgnaIIidxs1wIg3KMNhTAjQDW4MU3ce_M6gpd-8zzW5Apao-vEBxq5pjPtLt8puxxF7EOI-FlyQc5_BMazpOygQHdeJrzkW7_dbpAkDudgOGOAkZ_zSf4SWdUmMm04S-a4fb0F8nBC2KqJGV4UB5Q2TW1VUYI4DNCq7vDxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دوربین مخفی ضبط میکنن از رفتار جامعه با دخترها و پسرها؛
وقتی دختره بنزین میخاد صدنفر برا کمک بهش می ایستن
ولی وقتی پسره درخواست بنزین میکنه حتی یه نفرم حاضر به کمک نمیشه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70722" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70721" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g54GCwHO45JSetG5LRPy47quLgt4ORW7IFmg7s8MS9TiW9MB_ZFnM25hCHlX-8T6v6YYWZW3Q65N8SCc4GexYKFpMAvBWSZp8KOovSf2GPHvsd4Eh9ogv8pZk_UWW_mW-E2yxKe9CH6H4m3qUpFZwqVvLjDH432mqpr9EqXNhddvIp0_FV1gK9mdzf2p86Zu1Xj9DDaeXTWwG4auJ8PjBp4jmL7nd22AWzqPuu7OLKucnTH2JWr0AieTELODm5C6Idx5EavAPAUO5Nw3WdD8Vkt7d3qkwJ7ySJU96CYaM2iG6p-ey47DpZ5h_fAG1rSr2twh6A8aTbibVpS1T2p8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70720" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=Hyazl-pspKlTBgJ-XwbVM1x4N4c5I1y1SMM_AENLJG0WLh_Im07uypFLQQQL0SdXjUSWABukEWT54kExS8GugezsOqEHlofHVdcMg9VacGREXiZD0QqumDL9juu-jeLdPCLonhiG9DO-Onuw19DzUnL_yN_zVW7YMFqEx7pQ27tDrc4FjjgWAcuULkj_s2pH7fBX6qDYpL2NbnHqmU5fMYwPrnfwCvkTC4cRLnU_pME0tjeXXiuOt7tkV5Zck5_3RsSPSsCBZjUqS8JJoH0lcfutO28lrYf13MLyD6m1bXK8dcoKzf0NKMUHvTvN678R8i9SZRflXWAivBe82-rZHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=Hyazl-pspKlTBgJ-XwbVM1x4N4c5I1y1SMM_AENLJG0WLh_Im07uypFLQQQL0SdXjUSWABukEWT54kExS8GugezsOqEHlofHVdcMg9VacGREXiZD0QqumDL9juu-jeLdPCLonhiG9DO-Onuw19DzUnL_yN_zVW7YMFqEx7pQ27tDrc4FjjgWAcuULkj_s2pH7fBX6qDYpL2NbnHqmU5fMYwPrnfwCvkTC4cRLnU_pME0tjeXXiuOt7tkV5Zck5_3RsSPSsCBZjUqS8JJoH0lcfutO28lrYf13MLyD6m1bXK8dcoKzf0NKMUHvTvN678R8i9SZRflXWAivBe82-rZHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری خطاب به آخوند:
یه چیزی بگم باورتون میشه؟وقت تموم شد.
🙁
واکنش آخوند:
خوووبه؛اگه اینجوریه که من دیگه اصلا نمیام اینجا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70718" target="_blank">📅 18:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55129dd199.mp4?token=r_G2bzUeHXE1YTctfk-R9KUVSeFVNGQBRBbYRd_IXH7-egm6PyqB2uv4rX63a_yEGMicP0ffLDAQi9-0XVUSGFkgzAZi1daZibzx6WfSNdaUdd4gMJWlq2rTmTv_l-BITewuc7px3IjcH5D7a7SFihssSUeIyMg7X9Z0iCMk81UxS1dkim5Oj1txr2UBLHRNa1LyCZGntgWY20IOLgUXggUEZ5uxcOJSiD0m51TLGyXrlLqrItLA-X63RkMOGdfjtxHlCd3ytVHL8ama8jKLFTs8aNUpqS7pztF2ovyTL1EvEGDArkO7PalIMyhQSdylmq9YtuVkgSNu7xPURpCguw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55129dd199.mp4?token=r_G2bzUeHXE1YTctfk-R9KUVSeFVNGQBRBbYRd_IXH7-egm6PyqB2uv4rX63a_yEGMicP0ffLDAQi9-0XVUSGFkgzAZi1daZibzx6WfSNdaUdd4gMJWlq2rTmTv_l-BITewuc7px3IjcH5D7a7SFihssSUeIyMg7X9Z0iCMk81UxS1dkim5Oj1txr2UBLHRNa1LyCZGntgWY20IOLgUXggUEZ5uxcOJSiD0m51TLGyXrlLqrItLA-X63RkMOGdfjtxHlCd3ytVHL8ama8jKLFTs8aNUpqS7pztF2ovyTL1EvEGDArkO7PalIMyhQSdylmq9YtuVkgSNu7xPURpCguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چرا یهودیان بهترین بی‌سیم‌ها و شرکت های اینتل و راکال رو دارن؟
⏺
مهدی طائب؛ کارشناس مذهبی: چون حضرت موسی یادشون داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70717" target="_blank">📅 18:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508daa856a.mp4?token=q5ykcqvnYgcXOLnE9aaKCBvBxqQv9JMZGz2ldLyvNQzn5fvK8JnyFZizBAcXrtrqhLweu5AE55qE1z8TZLD8xgt74YXZUH9r5HTpvNFe4JeuWRZC-jI3FdEO9Oit-GLEwz7XpqRx6RaKH8Nz4ndSDXLSxleGjIpVQ-R1cL_v8AobAEBR9q2ZPS6NRGHkuh86CT-ZWE2q5gCELIXHmqVDwW0yCcHjH1RlGzB8pS9k80A4rTmkauqykqHC2KoVpF7ivW8YPCqhSa3htA_Ke25O8falxH4c_1MWdQ0xVlv9iWT5lb1NsrFbAuFEqLG7XCh87VRnfyGDSd7IIhQM4MrSFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508daa856a.mp4?token=q5ykcqvnYgcXOLnE9aaKCBvBxqQv9JMZGz2ldLyvNQzn5fvK8JnyFZizBAcXrtrqhLweu5AE55qE1z8TZLD8xgt74YXZUH9r5HTpvNFe4JeuWRZC-jI3FdEO9Oit-GLEwz7XpqRx6RaKH8Nz4ndSDXLSxleGjIpVQ-R1cL_v8AobAEBR9q2ZPS6NRGHkuh86CT-ZWE2q5gCELIXHmqVDwW0yCcHjH1RlGzB8pS9k80A4rTmkauqykqHC2KoVpF7ivW8YPCqhSa3htA_Ke25O8falxH4c_1MWdQ0xVlv9iWT5lb1NsrFbAuFEqLG7XCh87VRnfyGDSd7IIhQM4MrSFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشماتون بریزه؛ یه پسری داشت توی خیابون قدم میزد که یه پیرزن رندوم برگشت بهش گفت: تا حالا کون کردی؟ دوس دارم منو از کون دار بزنی، حشرم بدجوری زده بالا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70716" target="_blank">📅 17:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=QsBnFuiVWPSNAb9DXOH8Sq6a4n0-zEcoUx7MH4fA-7Xl_z9lXI8LOJLPXhprICD_77FzZ_Hywe0hMGDqTvvRtpxszxRkovDXk7xH_9zHxx_9VUjgOoSroSnyctLlGH_QuP0DhbASdWP540yZaN4dVSTWd-j1C1pbr3iHYUHZHjk1aDsHy-iNRv5lhtX1E0qWBrfTQXdO--qJkHduEVhGlwd5DjwMHvTS7NbYhgJWb4bqK8BfbqaBBVCoXStXAhKA6WDY5UGWyrwEgyw67X5ZataUDzihGgVhwJcMhfi_qzfNJu1aheTl_hTpe5l4BY2CaA_VjBD6pZiBU7Kig-AarQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=QsBnFuiVWPSNAb9DXOH8Sq6a4n0-zEcoUx7MH4fA-7Xl_z9lXI8LOJLPXhprICD_77FzZ_Hywe0hMGDqTvvRtpxszxRkovDXk7xH_9zHxx_9VUjgOoSroSnyctLlGH_QuP0DhbASdWP540yZaN4dVSTWd-j1C1pbr3iHYUHZHjk1aDsHy-iNRv5lhtX1E0qWBrfTQXdO--qJkHduEVhGlwd5DjwMHvTS7NbYhgJWb4bqK8BfbqaBBVCoXStXAhKA6WDY5UGWyrwEgyw67X5ZataUDzihGgVhwJcMhfi_qzfNJu1aheTl_hTpe5l4BY2CaA_VjBD6pZiBU7Kig-AarQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=I58a4EwQUIIwfxB6xXwrIf_MuVYP6ExjE9CWiDSoTwiw9CAvPxK-24bV65OOe1ETP4O2V4S_NAGRcQUrGU6u9nXA2YrFebTH_wOPVKLrEuTRem2zoBcmOAbkUCgmz7ZP_aJbw4XUwBsoFrTfZe5Qb2Tk0gHNF0lRxlnXSn5aSiZpKOUZpefgzxgsZwFUQNKc9PUbLFaftkLDyFXgkJ5YmIxw1lcaCutb5YqFGVdDk2IMB04xuDWIQln8Bc6Iou_81i-WMYj9qcbkE8cRWhrsGb54WpZn48e87CNGXrovXJ70muQD4u2SfHJK2GLky0t-HRr7BPXgPXJBRcA_wNbyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=I58a4EwQUIIwfxB6xXwrIf_MuVYP6ExjE9CWiDSoTwiw9CAvPxK-24bV65OOe1ETP4O2V4S_NAGRcQUrGU6u9nXA2YrFebTH_wOPVKLrEuTRem2zoBcmOAbkUCgmz7ZP_aJbw4XUwBsoFrTfZe5Qb2Tk0gHNF0lRxlnXSn5aSiZpKOUZpefgzxgsZwFUQNKc9PUbLFaftkLDyFXgkJ5YmIxw1lcaCutb5YqFGVdDk2IMB04xuDWIQln8Bc6Iou_81i-WMYj9qcbkE8cRWhrsGb54WpZn48e87CNGXrovXJ70muQD4u2SfHJK2GLky0t-HRr7BPXgPXJBRcA_wNbyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1L0Dc2PBHZV8TIVKqSjfjq3WaJhUrkS30U3O3oStNiufcIBU2aLN20jcQZeQLQuY04nPNusSUIbsQ8bb1N5aYkk18jx-aVvUp1JB_X8mtNlX5Mv6Bqp7bFZHmn6j0pR_rC2z5vbkD9BHKc-NXiSFdPiRcSaWNO9sLBbZNzfT80Lkg06uEUbmkr-WH-1F3IwOiH_14316Xo2vNJ0qjU4rfFd1aKHhmjzxuJzSS_C7sOVjsUBv58KHaAmI9oTpLczInPxBkwKhyCROi9r6Ez87lmoAqV6XBA5LcKWgBk4j7Zhfd9SS3R9vj2vdZOmnK1m2Yb2BXXB88O6QejUhngpBWPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1L0Dc2PBHZV8TIVKqSjfjq3WaJhUrkS30U3O3oStNiufcIBU2aLN20jcQZeQLQuY04nPNusSUIbsQ8bb1N5aYkk18jx-aVvUp1JB_X8mtNlX5Mv6Bqp7bFZHmn6j0pR_rC2z5vbkD9BHKc-NXiSFdPiRcSaWNO9sLBbZNzfT80Lkg06uEUbmkr-WH-1F3IwOiH_14316Xo2vNJ0qjU4rfFd1aKHhmjzxuJzSS_C7sOVjsUBv58KHaAmI9oTpLczInPxBkwKhyCROi9r6Ez87lmoAqV6XBA5LcKWgBk4j7Zhfd9SS3R9vj2vdZOmnK1m2Yb2BXXB88O6QejUhngpBWPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=Wkm3oNIcYqufpLv2Vknlv2qAuO8i4fGaDaVLwjnuFw06Qgt17UDavCiHo3fTF0BtdxSgJP4f04OjJsy_tsLUzPECOs_WmjcT4Q2yhSO6cmY1uitMxgOlbu5029ciO1KMQhcTcZpSi2ZMJyBRkMAuruQvaOm_roXfr0V2bNCsudmTQpGq7hmiezq3-Tqk9_tmYSbGa59Iu7At7KwTYprCsXbxwRKjl1NxCUMu9SEuWQHzZrLZaKyeWaqCFjtWiYuZFEqv8WvglgesQ3A7ppiV85VrSQzGMKDuEQTzz2w7RKHbQwkzq-pA__ICRZ5mh5Kd5nzey2-sT6ONx82czY6RGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=Wkm3oNIcYqufpLv2Vknlv2qAuO8i4fGaDaVLwjnuFw06Qgt17UDavCiHo3fTF0BtdxSgJP4f04OjJsy_tsLUzPECOs_WmjcT4Q2yhSO6cmY1uitMxgOlbu5029ciO1KMQhcTcZpSi2ZMJyBRkMAuruQvaOm_roXfr0V2bNCsudmTQpGq7hmiezq3-Tqk9_tmYSbGa59Iu7At7KwTYprCsXbxwRKjl1NxCUMu9SEuWQHzZrLZaKyeWaqCFjtWiYuZFEqv8WvglgesQ3A7ppiV85VrSQzGMKDuEQTzz2w7RKHbQwkzq-pA__ICRZ5mh5Kd5nzey2-sT6ONx82czY6RGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=ft25g30fsVTNHAZ99477EMes1xpo4QgGAK0pdK-TnPjfms_ZfbtL690g3oG5KS9FnDvDyd6FDUdu1ewAsfpRSTuuf2hkYCDdC8YJD6SALKZk6zY9zZmcmE9xdrT3xiKmsyY8J9D34aQ_1oK-qkTxJ9CLhHOMl8WNmyLRFIvGyswR6f9kLdduXGix2JJdRwyHGhLZRMoCDrMxGjwfNWYsNsImXnhdJ9lwAQbcuYwDIag_rek7svkCNWPyQVEKT_UaDKPx5SwIOuXog18OEX0LP6ohfmuMZNIj-E0-x13e0oQ6D2-pCLtaSbq3wEQBm-_vn8olrNN8waCYQxwplxfgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=ft25g30fsVTNHAZ99477EMes1xpo4QgGAK0pdK-TnPjfms_ZfbtL690g3oG5KS9FnDvDyd6FDUdu1ewAsfpRSTuuf2hkYCDdC8YJD6SALKZk6zY9zZmcmE9xdrT3xiKmsyY8J9D34aQ_1oK-qkTxJ9CLhHOMl8WNmyLRFIvGyswR6f9kLdduXGix2JJdRwyHGhLZRMoCDrMxGjwfNWYsNsImXnhdJ9lwAQbcuYwDIag_rek7svkCNWPyQVEKT_UaDKPx5SwIOuXog18OEX0LP6ohfmuMZNIj-E0-x13e0oQ6D2-pCLtaSbq3wEQBm-_vn8olrNN8waCYQxwplxfgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmpJjkZydkEsagrQQO489cRRaeOFC_FC508B7_7cZIDZU2zuwqI0HPRoIdt-3RdjszJ3SJvnayT06w0hOT5J-t2H58KJnRFW-xQAyJLLeQZpnAp-7rYM7BMdJ4fPgVSeTfHsXOeBki99tjeeZrQ3mZ78hRuLPbM7ISyTuqreNKB1rjJdE1aSGeRHoZWy2ZuWgcDw9CWqhdaA0THUVdlPD-vPAiBWMlLLxQ1JIjaGuL749FS7i36NbiZHkyftVVjy2UQYtOeoqi0HWGrW5EG-K7Ksbs6p8rFLTl0BzR-h97-YbPSkkmJVJr1svkpRE33VBJepN2SyRNLP9aKOuRFYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=eyOmz79xwC60l_dY3Hmz7SVRusrCALZBpuRs6XrYeqsXWMd1AkuaodjG6OJISN4n4QnS_jDLf2Ya2WLMVlyEx-Gxymjuiznq3_i3jFnF2xbKn9oAXWn87V9Z9XwJhiQYgPErqXPElQHfPqS1GkDAdDthGV8ZGbslcWt21ZaYNjLVep5q8uxyAfur9HXhvUqAYnIlihHM9tGkw4M-EoDK5ZRuIdyTxHCeJNMKKneHjaMEOXJsqWu_MGYb_jyKZgvYcJZB5KU2WwNEXmHvx8H2uozmEvqZT8ZIticC4mZQCslwim_iDkIVL40JW95pliederzCgDdO7aiMSjvBLFGtUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=eyOmz79xwC60l_dY3Hmz7SVRusrCALZBpuRs6XrYeqsXWMd1AkuaodjG6OJISN4n4QnS_jDLf2Ya2WLMVlyEx-Gxymjuiznq3_i3jFnF2xbKn9oAXWn87V9Z9XwJhiQYgPErqXPElQHfPqS1GkDAdDthGV8ZGbslcWt21ZaYNjLVep5q8uxyAfur9HXhvUqAYnIlihHM9tGkw4M-EoDK5ZRuIdyTxHCeJNMKKneHjaMEOXJsqWu_MGYb_jyKZgvYcJZB5KU2WwNEXmHvx8H2uozmEvqZT8ZIticC4mZQCslwim_iDkIVL40JW95pliederzCgDdO7aiMSjvBLFGtUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbodV8gEkue4r-8GSHkdYDlaj6be-5K-efHFLx5lojtvPTJwZJeFC4qAh8uHs65OdqCHrr9qz6A9ExoINSeLF0B76ljOLd8sQVOlNtA-LGkCbxJfsNGO8foUTcHyAhg4ceJW3R-DprJ_eOp1FWrN_9kkA3eqGDh9ots5DQCXgX7ig5UvN-RnXC2IE8pyPtF0cji1EKimuHJJGlM1sSrkJp0DX1-_JOGT3YscZqwjHAkH7A7TFS-9eEaJoonexzLf0f6SwHTsZlFouSE5JTHa89w7Ynejc8ADTSrbUV1QAU3nRBT_3HHrVMQu5egUvgAHM5A-uyiEpfUwlR0Yaw7FHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGte2ms8NllLkw1rvg90nAUajwBzRFP5Z19P4u15lwgEWAvopbe68ntMkvVHoa9G_9BArQ4fVftdmxILKQ4Agzm2K26gmLmFAJb_VOML50iXWY7XdhtNquWCZpMTCWT5V4SIIu2MS-brSzMeBaSo_1ko64DMbsI2reUJYVIiFt5q1lhK4dcJN2Cz6ENJCPAeuY1HzrUH-RZ0nRk9eINkdkMSDIymtj_wFhAYP_z1Kicp-sf6CNDF3WtU-0dYlw_etAT70z7ryNq6CAzhd5edl7nwTdX4Whc0cARu-LolrIJl8S6QFZ_JINiuW82AnwnhUaskWeQVElCC3wCXHqbIkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQLNxcWJqU0cAFXpmSEKe1HaAaBYiWCsWHfP4te2Tc1p3u7_uLZNJ7iGYFwywLhu_2TITTl-L94boCTFy5GD7yTq9YCNcQlt5_ipVi42KajI7kmBLUtoXiqMmr7ccmTmx-AZJyQv5OsjZyRzjhPWm4ceXV9akvPX9cMezc_Bx4_B2gC3B922-rXkcTzxWjlue-1GmUKfWyZ_lLMpcsQ7yxDB0usucf_zWVEWKOnk0w26ScWMGoi8ctyFCH0NtboGwBPOQuggPpyTWFQMvHcTnfD3nRM1bleJgnORj2Fc4Cr0vlTqZ5noblf7TIwCwtQh-zBzljLvCjE5jmKXhRGhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e6WUAfNcipkCLROnOj5MVxd5uC765-7zvpKuLMoZnEh6QJvvEMwC5Gu2h-2t0t5pSSPb_zn7K9tozanMZ6y8QYBGFJA4hsiN_-LkD42qqBE5RhYBxIKcPvt1YhrlKarV1mRcLDQsvJcXCLOQZF0prjYoAN822lwCCA977a23x3RT_mN7fUYmacYLWsDZzpk_bnoZqyX-LrssvSkBRtyA1MVoh5IIr7KrvzI9INvTP1Y0QR30w-u2tKJj5t9D7YBESiEZEmVnR4S5UgrvjbUi1gIoeWe_HjsSWVQvnl8OYAZu06hdM3LbHFRObvbfb3Y3afHlvDGeVB_vsuxCJ_NfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gUPPmKmacwYd-YpGj0Q8HormhpzCyWU3fgM1YvHFjGV2Inb76tMRIHp08fZUZ6R9x1tlgqzwqBw_5Q04rbImagFEadC2GM8VVa07Kv9a5IRtMcS8Dx_GF8_LO8aWppLyY49wCGuASUdWZz28U0JTJ9kItVHc3gVdTV7Pyv90j_yrx0FvZlKRrl0EEZgw6fKZMLg9ZEJOzWNYP75XZhJzzUTf9wzj1P7e70CcqPQ6_yKAJcG9oIj-dOAObsuctHby51gSSAj_UHxcrbdtoQ8U7hJFhKH7OMrQGvYbGciEZGal48z2760JFE3pa7b6B5FqKhtXiTfZKH14EM-Arq71xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6cX7RTgbY_Ndrfpcb2l35wTJ6JKoPWVKO942MG6Aj5WDYt9dTxIl1CU2CGAOjnTb6tqA3yI7uXNv3qk7z-zMDDp8yNjbtAl8y_HGqbG3s1uFv8-YzB5Lke70_6kIcplWYNDi2sJB8uXcSWEUJE76a-yOYk6Kjy4KdngJzj9mDyP5Z2cL-7wYETYaieCvCEGYK5nJXdBzyRVv3vXT4yg5zDIY8NRt_Pqvj0Lf4OTxj6VKn9G4Sn9OPVheU7sR7Eu1WDx71TOtiIa2aH3rB0bGFET_vIRV-6LTYf7yW3cdGF2NjNAsgi3HiwlU0ReFkW0KaoO11ctCZwUzNFJlote6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=m9JV9-ukzF6lS1Gas1nNd1AvDyMTNuQ7T5ysXHSPFf6cPZCjbYokDNdrNLNQxkf2QJhwhVXm_Rr6Rxo2jJC-OtQBFWNYze_XvmBfMnOs22fKv1M7SWtqeIkWrnL2jTCB_xOViawC8WFiOpGphBSnW6SRC4LTrZEcVZj2tYXaAW9MhS_diRvM1rd0OibSyqnsuxwiLdtzDQO23QnAXOY9wtGQQjV-Bkknjgsca2vWaV5DmsliY9OOOB5gHT6LJ5Wubz7czBMYrPqI71H7_-XJmfi4kkD1BqCVF2S8Mt7WmU0lB30owfJgIZMJZf7Clx1bCGT6zjNh_IL2MGmJMrKLJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=m9JV9-ukzF6lS1Gas1nNd1AvDyMTNuQ7T5ysXHSPFf6cPZCjbYokDNdrNLNQxkf2QJhwhVXm_Rr6Rxo2jJC-OtQBFWNYze_XvmBfMnOs22fKv1M7SWtqeIkWrnL2jTCB_xOViawC8WFiOpGphBSnW6SRC4LTrZEcVZj2tYXaAW9MhS_diRvM1rd0OibSyqnsuxwiLdtzDQO23QnAXOY9wtGQQjV-Bkknjgsca2vWaV5DmsliY9OOOB5gHT6LJ5Wubz7czBMYrPqI71H7_-XJmfi4kkD1BqCVF2S8Mt7WmU0lB30owfJgIZMJZf7Clx1bCGT6zjNh_IL2MGmJMrKLJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=D4gU5EV-Gg7B6RMrKBLeY69uFAKQS3VcLKEMa92PHNVWT2k-FLdbsUorf4XViQikxlJDmQKgHuFU1IqCPak30Ngkz4pc6Urhil0EyNr9EcPLZfztjseUOklmAThSrTlJou-tM7fEZTiv8VXrIREv9f7k0lwGn6Ca_K4OaFHDzg9fC4p2hU9z3u3CElBvfa9pD5QXgGpve0K4otF0iO6u6iUf-PsKBHwJUzBoXggblQSmyvclZeCwEs1ikDA5-Bww8sMG77Zx-tznls8UmP-CHDX_EsPPY9UDH1Xmtz3sTMX_8q_g8HXb_EorJ5MH_Z2JSs91huJCB0x-nobg2r8eiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=D4gU5EV-Gg7B6RMrKBLeY69uFAKQS3VcLKEMa92PHNVWT2k-FLdbsUorf4XViQikxlJDmQKgHuFU1IqCPak30Ngkz4pc6Urhil0EyNr9EcPLZfztjseUOklmAThSrTlJou-tM7fEZTiv8VXrIREv9f7k0lwGn6Ca_K4OaFHDzg9fC4p2hU9z3u3CElBvfa9pD5QXgGpve0K4otF0iO6u6iUf-PsKBHwJUzBoXggblQSmyvclZeCwEs1ikDA5-Bww8sMG77Zx-tznls8UmP-CHDX_EsPPY9UDH1Xmtz3sTMX_8q_g8HXb_EorJ5MH_Z2JSs91huJCB0x-nobg2r8eiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmGFCCO1XztqqxOVuOEl72Qvjwoth39ixO_g5yznj6Eq0yWm5n-NAS4zdmdnkZzJN87H860UdRIGvDmJBMglOOd7LhZ5SJjlf6IMqToQRBlWEftphb85NMF0BgQYnUL2NM5XbQPhO8fENf8NNcGO_HfHI915rAGmea9L5hNM3k-e3ORj6q9a5lkSZqftHKqt-eYql-C0tHHWP3mTZVcwxj0CHCAHAGnl_WedMUucBI1qL5q1cZoIEZfguVvs4vAv0BJ6OuXY60iJe8gw4az0H3srTwiNw-x-6yKSdNLihTDcjCrsteSe_0pbBVahECKPdymEHvZuQR827K8QKr90yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=lgLfnvaa67pQg0xqg2cB9X_43s6jQgWkUbi5qHiSNekY6FDoctagy0qKCSMZZyloySh94CxbAIyRktSs1t_SekxgQqp7391e0rGP9nc4ZXATwQjdxZDQTLWb7HHYDJuNvu7gk20e1BZlYdzLUMYmCPLVaJhxZJeFFk-kLgehkwVLsfnI758blfAFoVKTdXzkwrNMyt0C23h__7uoQGSUlILw6pD1ENfjA-hru76EcQ9R74f-EzF4oiKioqwshMN1kkSDe3oh5qWg6Owgvu9t8ku8p6qZ51fvWUJ48e0rRVeOpbM9yAPrrKGgBLM0Y4Cd7SP6uDYDmS1gJEvGf1NbKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=lgLfnvaa67pQg0xqg2cB9X_43s6jQgWkUbi5qHiSNekY6FDoctagy0qKCSMZZyloySh94CxbAIyRktSs1t_SekxgQqp7391e0rGP9nc4ZXATwQjdxZDQTLWb7HHYDJuNvu7gk20e1BZlYdzLUMYmCPLVaJhxZJeFFk-kLgehkwVLsfnI758blfAFoVKTdXzkwrNMyt0C23h__7uoQGSUlILw6pD1ENfjA-hru76EcQ9R74f-EzF4oiKioqwshMN1kkSDe3oh5qWg6Owgvu9t8ku8p6qZ51fvWUJ48e0rRVeOpbM9yAPrrKGgBLM0Y4Cd7SP6uDYDmS1gJEvGf1NbKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=A-fWAXRRBqThzuvk9T_hdQJx-CvGXCkP3Zw5-rz-Z3MBHPTAI5_h45Qx7X0ssT5G87IvCP7Er0p-4u8hBS593Hbx9ky8CUyncf9BnY59MRWqmw4aL6EaoGHPax-3IxfShnnVEUYvd0Y3efMUtc8dvfP5at-m3_FjzWBlmIjcoxDptoeigh76suP6n1xi6kwB9K-mAEh8dIkZJnVaynnwbgTfDKqD5GmAcIuK1zodGto6cgddpmGAWRxxFQfWFudzdp_SoFgZhMEqK6N0z5Q-vBjG-bkWgdSCy2-TPUJGi7WxWOM8bMM0j2VW5UyRG3vUcLRWPIboElVWSx-_KyRJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=A-fWAXRRBqThzuvk9T_hdQJx-CvGXCkP3Zw5-rz-Z3MBHPTAI5_h45Qx7X0ssT5G87IvCP7Er0p-4u8hBS593Hbx9ky8CUyncf9BnY59MRWqmw4aL6EaoGHPax-3IxfShnnVEUYvd0Y3efMUtc8dvfP5at-m3_FjzWBlmIjcoxDptoeigh76suP6n1xi6kwB9K-mAEh8dIkZJnVaynnwbgTfDKqD5GmAcIuK1zodGto6cgddpmGAWRxxFQfWFudzdp_SoFgZhMEqK6N0z5Q-vBjG-bkWgdSCy2-TPUJGi7WxWOM8bMM0j2VW5UyRG3vUcLRWPIboElVWSx-_KyRJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gtz1RXaURFI945dqvEKFkhF0I35kE2VyzwtoRtBSGBghErSXgL3HKkK96Fq0-KPKP0XBCQadAinKWnZ_iRyLLjb44rGCxVX8B-rdO6QearyaQCMKPuJLasBivCq6YlG9YAaWHI14H7qi7fdmA-i4RoHZIKSubtLgxQlRnxh4U-afnhU2JdiD2kjFu_GFTkOJS8zVSvHZHOLCDfY8WDhq-c1pEfAdJas63eBd9fpBPfiU2kKgUWO-xSkRPwM2KTHsDlGobNnNDZxIHNZHHHrlhHiC2j4S3OtLz8NPnMRMjNUkuOZSJ8xKQ2fMEPmaP62d1pPbWhGNYi8TB-w5pV8gtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Adj-UfuDUiT58_jqIT4h3t1lh_8Eaq2qw0qtail6Two4ozaB590uC2siudE4yzcgByDOztmn15HV49WFvK2AiGLfTO3kSlEyzTYIY6rX9k_tYiJCIkpL24iUQF6Ve6rQPhun6k20dY725Fo-E6lXkhuLgjLe-ITrEyXoociTMvPyvpcpjJfHl9Dm-p510Kz9Z2QSTMoUpXkvoB2FFGVBFRilx3R9gmEUeHJtbMUt9V_TmwOOXmTZDxzMlekslv3bnoEqoTcQTNhi3wTNBkup6HlcyEwUYkckG4ltLg5FmVZksV_7jdHw0jd3EcnMUOBxriJUQlxwWXL1PDa7fejbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbdDBMPvASx97JD7a2wQqr3Aj5ud-PFdsaCusqqoXfi6wOD_mbE7asq18yr-Du1vuqlD6D2tyzhzUWPLC3IkT7R-Dvv__tUJCmeTOCb7Besui-Q9a-taa0c9LbtrUh6DgpAGkJMKbY22w1PnujY2OXmnRZK5va0IqqsQ0Fulmi9bn_fyfuvLZn90iPY-l-2FdkIKPXUfqZr-uuGPugh6KTKZG9W6nkIxxspcP71yry3H1IRV78T69u7jttHjYukY9d9-QudOZ5A4pP1g_vF5QqIlZ1SOB5FvGF_OWbfFpwyHnRqlG-z6QaOi-FlL-787xv56-IiI2u0wYGHIs2s4-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-7IKXn8aH_Q22Ti4kFBzjzlHOPn8NTmaR71O127JQG37ywJr0p9rXLp8Go8mkyuMvKJKAp855UeQohTfOd3cqKqRYwXZNpJm2YV9NbsNKZwnlIveAVMAayMdSL6zj9kqyH5F7pSOghvAd1Qq84fYBqGT_lWFJjlAfuR5EdavoPjNn218MfEfaHlGfmDpZGbNVqgGsS6sDJfJfpMwbLuny3E6fSkJDFuaOQ73_gRDbZKvOTg84MCtrMdBuytisf5HJkxcxrLljlDto56Ob3pdDhGiutouBAbV9FC6LGWrkqoWfGGmSd6gi8Wgvtq_ah6NsMCBa9aXREvKcT_unfjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
