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
<img src="https://cdn4.telesco.pe/file/GeJG2unAENGvcz9OFwsX0HPiYyaeOUDDtriiKi_zw1Tq0WOEtcKTXmoHmIf_QbF3YNkhTk3YTUnIGtmc-P43N__Vnbr7TGMEYh1xK_sBj-e_x4EWo5mS_9e639Nw0SeFewdKgS9KxplIlGEs5TltdtNmryNB5A-DWbRikEq69ydkl2wiV6FDomKnlllKPUK5dobBiPyhreM2oqqKVNQ1hP6oXnPq5zMP-OUV-yQpOpmJ0bLH5_PmpRA-XjajV3R2bj_-UXBnulEJgA79j17HjMTMBvEiSP8_eL0PhroF_2JzAYDB5jN6iSli4xWMpFpL0gUarWPhMC_L_3C1Koc6iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 12:33:18</div>
<hr>

<div class="tg-post" id="msg-682766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=KZKLVvRIwIUPP18ozg2UyJfEVHX9qS4rz5hxh7SuFQXtoC2Av8C0EwIpQBG8dxpE9noEvnuegLSRzJI79DUpOfiM6NQwSQfvv3SHfASYBCxFb83Vcz9eMnU6u6ATKGyRlnASRxmZo3pplq8ZEYvgF3-rZlwRd7MR38lSPEZw1tgrdpWCllOIEqDRVJp3zkdgi4mxeHocrY9hKHD7LHmlrIeP0fmGDrPMSsTTD7H7vrdFA6Vu7OQHDcVTQY2o0PdsCEAjUcECJWi91nlHTB1fjvivj6UALfI3fmdnMTizZ--emo5wSV0TZHM8hjUVjx0k9h1RYDao9-H2KQvxOHwcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=KZKLVvRIwIUPP18ozg2UyJfEVHX9qS4rz5hxh7SuFQXtoC2Av8C0EwIpQBG8dxpE9noEvnuegLSRzJI79DUpOfiM6NQwSQfvv3SHfASYBCxFb83Vcz9eMnU6u6ATKGyRlnASRxmZo3pplq8ZEYvgF3-rZlwRd7MR38lSPEZw1tgrdpWCllOIEqDRVJp3zkdgi4mxeHocrY9hKHD7LHmlrIeP0fmGDrPMSsTTD7H7vrdFA6Vu7OQHDcVTQY2o0PdsCEAjUcECJWi91nlHTB1fjvivj6UALfI3fmdnMTizZ--emo5wSV0TZHM8hjUVjx0k9h1RYDao9-H2KQvxOHwcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردبیر پیشین نشریۀ خلیج‌تایمز: کشورهای منطقۀ خلیج فارس از ترس موشک‌ها و پهپادها، به تعامل با ایران روی آورده‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/682766" target="_blank">📅 12:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJoa2J2W7fPbAjlbWClF32YbgxuzjQxYSFjAdJQovZxPKUDiV5jg2dLcywdrwYUyUg-yxLfsOmGaq6cDhqI5Ma3qVJdk9zsK0qdH9h5mhBciVrmHwf4kBiv4o_4sOq2p8TZFji639-Hat5BYmdiDWF1iGRpUMoiLH3ohkBEcFbVymPexTxqOjyGBw5Y0UY43TSlRi5FYNx7_ug4ZPyxF9_W7M-Q-gPY8dN_E1KYZqM8CApb0Z36AjwDct9Eowiitj255RU4l-_W8AJjbigX3Eoiybq9rLcsVpphNYrA63nZYci7N65iq-kHAepdBixhHn_NnNOfUNpYjPFx8Y278xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/682765" target="_blank">📅 12:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2f7760b8.mp4?token=blGbn9C-GxmGVFeu5HwaDLpehi1ezg2jlBsr_RBnvQPxgaEiztAEYjRa1sy_PJZoJTgvDwGDRJJrxHvSxoI-PcyxvoyeOfhSIpEXwzKvJYGzVkDlgP9aXp56nzMoA8QN-NO1zT_580ueXzKqCTG61o97IVOtOEki5jeaX2wkUnJeNFYmsf5xfpCrfXQi9kGiK-9dGaLPPslIN4BKp-OoRCQPgjfVZO_lc1JFs9IrfKyFF0niiuBF-DGLyxuiblXIV1QWoG9XPhyJwg6O7NxeFzm6jhDyQbOuMgUH_v9pmmaUnJGjF5yrnqyQwImBVBBLpYP0DS0rVme8XcGHNY7iyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2f7760b8.mp4?token=blGbn9C-GxmGVFeu5HwaDLpehi1ezg2jlBsr_RBnvQPxgaEiztAEYjRa1sy_PJZoJTgvDwGDRJJrxHvSxoI-PcyxvoyeOfhSIpEXwzKvJYGzVkDlgP9aXp56nzMoA8QN-NO1zT_580ueXzKqCTG61o97IVOtOEki5jeaX2wkUnJeNFYmsf5xfpCrfXQi9kGiK-9dGaLPPslIN4BKp-OoRCQPgjfVZO_lc1JFs9IrfKyFF0niiuBF-DGLyxuiblXIV1QWoG9XPhyJwg6O7NxeFzm6jhDyQbOuMgUH_v9pmmaUnJGjF5yrnqyQwImBVBBLpYP0DS0rVme8XcGHNY7iyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از زبان ‌علم بشنوید چرا بین خانم‌ها و اقایان این‌قدر تفاوت رفتاری وجود داره؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/682764" target="_blank">📅 12:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3XEaFqI4fhAECdMlUeeiWjozo-sOAfzo-1Q8Tj_DLhk2gT0en6eLYrRQqpqDzMx6wK8YOAz0GWzG3QIZw309RVTBFMqJEw7L_momW0cY-PlKeJDwAHBur2lI71VFVG_Y_MGDPQgKqX9tu7yiVVtiua9MasJ02hyPV5uS_5YXz1j5nqdkdBXi_0qZm41oB7Abt7ITOa8UX3ds0fanmhTAaq3aNh7BHjmqWyhA-GZCzEVQ0wRRcQybKNgVxCNsQUWWtR_m7QqWOQecTiWdL89Ui2CNSFmtWdLwv0P7kHUCqS86uQzgiBOnCzSUB4ASVorhFI7TajiupabLzGILczczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴۰ لغت کاربردی که اگر بلد باشی سطح زبانت B1 هست
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/682763" target="_blank">📅 12:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2XeStgCsV0Wd14EgHqcP5CvmVwtuR6Po12FvBR3TnZ_a6fEn8hcGcyIX9LrO1WD4UBK1Kpt40ZzsS489tkXpGjXkRjFqODUZ2Qkpy8rBVCEFv20wrO_21vF9FUmdwDY7TK0SOLn8QhZ4_8jzdQ9Kl4V5qxAC6jbzmvLoOjzyjVPIyUHb0mJf4jDYeBdDI6crJLL5bQPDX-H5fdOnLuu4vQHoZf6CjgJ_fpXscuVNHcCnRspNj6lc25ArUylz1gC2iaot5epamSFaPEif8Wu3m3s27JHuXzGuBFoc9CJMq3b1f-UiPRnJjX_GLz00K8Ezi0dYH64vr8Q2WhMq1kenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
تا 70% تخفیف در جشنواره mono!
👠
صندل، کفش، کیف، البسه، اکسسوری زنانه و مردانه
‼️
امکان استفاده از تخفیف بیشتر فقط در ۳ روز پایانی مرداد ماه:
💰
1000000 تومان تخفیف بیشتر با اسنپ پی در خرید آنلاین: PAYCVCCK
💰
500000 تومان تخفیف بیشتر با دیجی پی در خرید حضوری: DEAKJM
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
‌
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/682762" target="_blank">📅 12:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=d9pX6wRe_FLsyS1uBeAqMfiLExiVUV7spSWFi-EurnL_4iz_Cfz2TpZ2b7zZy8jAwo9PxHc7TSu01FIyBcDmaOlGfM25SIBgqgU1LNUvWtq0Ph8r67_YRU_hq_p07Pt2sFwjhc-GO6KnIshopU5CTZTdTtQ_ty6QFohJkXT91uW0lv_xcTS1ml2kaM5wNp5UJd92bE-IO5KMK92jiK2l44YvZRTEJwvn9HUZqOXMIPxYfwf074P3c1Q_UV8UkFwENnQS-eCr4HP_K6SHISdIoiOdOZ2loEbKln5P5L1p2dKDfyKYNSb5ZvtD0SDYPjSZfJF4qO0m9YYQHle9kUNCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=d9pX6wRe_FLsyS1uBeAqMfiLExiVUV7spSWFi-EurnL_4iz_Cfz2TpZ2b7zZy8jAwo9PxHc7TSu01FIyBcDmaOlGfM25SIBgqgU1LNUvWtq0Ph8r67_YRU_hq_p07Pt2sFwjhc-GO6KnIshopU5CTZTdTtQ_ty6QFohJkXT91uW0lv_xcTS1ml2kaM5wNp5UJd92bE-IO5KMK92jiK2l44YvZRTEJwvn9HUZqOXMIPxYfwf074P3c1Q_UV8UkFwENnQS-eCr4HP_K6SHISdIoiOdOZ2loEbKln5P5L1p2dKDfyKYNSb5ZvtD0SDYPjSZfJF4qO0m9YYQHle9kUNCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزهٔ مقاومت: اهمیت اصلی علی‌الطاهر لبنان، علاوه‌بر موقعیت جغرافیایی، به تأسیسات استراتژیک آن برمی‌گردد/ در میدان نظامی درگیری‌ها لحظه‌ای ادامه دارد و حزب‌الله همچنان با تمام توان درحال مقابله با دشمن صهیونیستی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/682761" target="_blank">📅 11:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4e744901.mp4?token=JH1fOn4fZdcZxBn_6yGWFHiXA4wJpjsQeKnE3NtY_AhJ9589LLFab0NGDlg8W5G-fopgAqelGC_BaYprNsoAbuchPKypwPkKba9c6xVDDNd3OWuNez1OC51Z680BjPEbVokVE3IY12BnqB-UR8uFYTaAkBA8VhoHSiluRi0JZs71Pq50LCa3_539eCSzI5O3_z_dqqgecF_UpVDJ5esyQHuogFPy4hPw9P3WPqreViKoGVo1QQv5c34vhTl0OAwlsdQir39oqmiqQPE9IpxbyDPUHEq42g4229YoKb6ExbWl-xjxww3-TJwDmB11QprlhuEH-wjkaFFvtSPT22EFxxPdP3T0azfpSIVpB4p16JpL7z3F-0iVgmcsinjZIRUXl11Ek7UVPG2IB03vBiHdwPHd7JSXzYI2g0jwEa-xMeeg-9QoS1RR1S7DEZ8j0UTRf3-r86KI88TDUBHBgBQlKLfIxAeNXF1j8i1EPKLcBic0duGHcIOLwn69nBa1B3qtjfKkhfK_uAzyt5pgufzvKnyf8xJ9h_gvfHPzny4Ux2ATTH2ZS0_el6tBt262TfPWyaLhy7vqYKziSyJyuILrr_EFSQ2q_s53ruWpU9DcG3JS3-AM8n8gqgXTucI9Up7-RhPmCc1fjawIwk5acpdGY7MsTVu45uJVg7ImvIl2X7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4e744901.mp4?token=JH1fOn4fZdcZxBn_6yGWFHiXA4wJpjsQeKnE3NtY_AhJ9589LLFab0NGDlg8W5G-fopgAqelGC_BaYprNsoAbuchPKypwPkKba9c6xVDDNd3OWuNez1OC51Z680BjPEbVokVE3IY12BnqB-UR8uFYTaAkBA8VhoHSiluRi0JZs71Pq50LCa3_539eCSzI5O3_z_dqqgecF_UpVDJ5esyQHuogFPy4hPw9P3WPqreViKoGVo1QQv5c34vhTl0OAwlsdQir39oqmiqQPE9IpxbyDPUHEq42g4229YoKb6ExbWl-xjxww3-TJwDmB11QprlhuEH-wjkaFFvtSPT22EFxxPdP3T0azfpSIVpB4p16JpL7z3F-0iVgmcsinjZIRUXl11Ek7UVPG2IB03vBiHdwPHd7JSXzYI2g0jwEa-xMeeg-9QoS1RR1S7DEZ8j0UTRf3-r86KI88TDUBHBgBQlKLfIxAeNXF1j8i1EPKLcBic0duGHcIOLwn69nBa1B3qtjfKkhfK_uAzyt5pgufzvKnyf8xJ9h_gvfHPzny4Ux2ATTH2ZS0_el6tBt262TfPWyaLhy7vqYKziSyJyuILrr_EFSQ2q_s53ruWpU9DcG3JS3-AM8n8gqgXTucI9Up7-RhPmCc1fjawIwk5acpdGY7MsTVu45uJVg7ImvIl2X7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین در سال ۱۹۱۷
🔹
فیلمی تاریخی از چین که در سال ۱۹۱۷ میلادی ضبط شده و تصویری از این کشور در بیش از یک قرن پیش ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/akhbarefori/682760" target="_blank">📅 11:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682758">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای «الحدث» به نقل از منابع آگاه: ترامپ دستور داده است مذاکرات با ایران برای چند هفته متوقف شود و احتمال تمدید این توقف نیز وجود دارد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/682758" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682757">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترس از ایران، بازی اسرائیل در عربستان را لغو کرد
🔹
مسابقات «جام ملت‌های ورزش‌های الکترونیکی» که قرار بود در ریاض برگزار شود، به‌دلیل شرایط امنیتی منطقه تا سال ۲۰۲۷ به تعویق افتاد.
🔹
این تصمیم در حالی گرفته شد که قرار بود اسرائیل برای نخستین‌بار تیمی را به یک رویداد ورزشی در عربستان اعزام کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/682757" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682756">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe6b7f22ee.mp4?token=NzgyUQ0nx0hppyltYoDPwBOAvW5Xiw0eDjOcllMAgVG5hz5mHCCRjsQWr6nfhlSVglDNNT2uXmg2LO1_Bv7Z2OY1rtjV7GhaBQWC--Ahx6vy9exPp2S9dvqnP5BKKMemc090KshTj-RJO2eKV0CFFAmWWG_ZfvHNUYTjtGTbW1GX2pqD0M_UKKkkDbmjJ3ScTnTwR45sWKqyMLu4GAnS2Z1KZMgtNlZEDVAY5pkVBaftniQVTnM1HKLcP2ZhRD4K7KwOHl5eoIE46IpWIRuw75gHTT1EyMNEDApbTG2tnGNAQ3U3fRrRTzQs_OfcxxNOccg-_l1uDywKTub88jQEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe6b7f22ee.mp4?token=NzgyUQ0nx0hppyltYoDPwBOAvW5Xiw0eDjOcllMAgVG5hz5mHCCRjsQWr6nfhlSVglDNNT2uXmg2LO1_Bv7Z2OY1rtjV7GhaBQWC--Ahx6vy9exPp2S9dvqnP5BKKMemc090KshTj-RJO2eKV0CFFAmWWG_ZfvHNUYTjtGTbW1GX2pqD0M_UKKkkDbmjJ3ScTnTwR45sWKqyMLu4GAnS2Z1KZMgtNlZEDVAY5pkVBaftniQVTnM1HKLcP2ZhRD4K7KwOHl5eoIE46IpWIRuw75gHTT1EyMNEDApbTG2tnGNAQ3U3fRrRTzQs_OfcxxNOccg-_l1uDywKTub88jQEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر شیشه عسل، حاصل میلیون‌ها گل
🐝
🌸
🔹
هر زنبور در طول عمرش حدود یک قاشق غذاخوری عسل تولید می‌کند؛ برای تهیه یک شیشه ۲۸۰ گرمی، حدود ۶۸۳ زنبور روی بیش از ۱.۱ میلیون گل می‌نشینند و مجموعاً حدود ۵۲ هزار کیلومتر پرواز می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/682756" target="_blank">📅 11:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682755">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597578ac3e.mp4?token=FTqG4-VOLxihAaXXyDqlMUuesecVKLPOwjZWspXCw71JaYhbI1v8SLP_4uf_XNBOxSfmi4-pGzlSK92alr8IDNyZORrgSG6_KPJJcpC0UVG-JJyzYORAmG_8G1mM8bqCbuGwub3myNYKMDZeg6PGmln8dcfdDBXOaLndx1QMbb7UJLMpiiZQey_iE05PiMbQBOkDs19Zy6skdp_aZN8D8XGuOCD_YCdTU1k-x-XK7gGRAOJPVIyLW5xC86N5xtip9MwYqedjzJxRtMe07QQYsYWxNd8yEgiGAMHDSfZlF-DDCDY8PNSm2vGBsFim9LTx15IE2IXFiUHF6KNH3Gdamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597578ac3e.mp4?token=FTqG4-VOLxihAaXXyDqlMUuesecVKLPOwjZWspXCw71JaYhbI1v8SLP_4uf_XNBOxSfmi4-pGzlSK92alr8IDNyZORrgSG6_KPJJcpC0UVG-JJyzYORAmG_8G1mM8bqCbuGwub3myNYKMDZeg6PGmln8dcfdDBXOaLndx1QMbb7UJLMpiiZQey_iE05PiMbQBOkDs19Zy6skdp_aZN8D8XGuOCD_YCdTU1k-x-XK7gGRAOJPVIyLW5xC86N5xtip9MwYqedjzJxRtMe07QQYsYWxNd8yEgiGAMHDSfZlF-DDCDY8PNSm2vGBsFim9LTx15IE2IXFiUHF6KNH3Gdamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود غلیظ جنوب تهران ناشی از آتش‌سوزی ۲ تانکر بود
روابط عمومی پالایشگاه تهران:
🔹
حادثه برای دو تانکر هنگام بارگیری نفت سفید رخ داده و آتش‌سوزی در کوتاه‌ترین زمان مهار شده است؛ این حادثه یک مصدوم سطحی داشت و تلفات جانی نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/682755" target="_blank">📅 11:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682754">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بدهی عمومی آمریکا برای نخستین بار در تاریخ رسماً از مرز ۴۰ تریلیون دلار گذشت!
🔹
داده‌های وزارت خزانه‌داری آمریکا نشان می‌دهد که رقم بدهی داخلی دولت این کشور از زمان دوره اول ریاست جمهوری «دونالد ترامپ» در سال ۲۰۱۷، دو برابر شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/682754" target="_blank">📅 11:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اجاره در مناطق لوکس تهران؛ ماهی معادل ۲۰۰ میلیون تومان
🔹
براساس قیمت‌های پیشنهادی موجران، مستأجران برای اجاره آپارتمان‌های ۱۰ تا ۲۵ سال ساخت در مناطق گران‌قیمت تهران، به‌طور میانگین باید حدود ۴ میلیارد تومان ودیعه و ماهانه ۷۸ میلیون تومان اجاره پرداخت کنند.
🔹
با تبدیل ودیعه به اجاره، هزینه کل سکونت در چنین واحدهایی به حدود ۲۰۰ میلیون تومان در ماه می‌رسد؛ رقمی که فاصله بازار مسکن لوکس با توان مالی بخش بزرگی از خانوارها را بیش از پیش نشان می‌دهد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/682753" target="_blank">📅 11:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو کمیسیون امنیت ملی: بهترین واکنش به تشدید جنگ اقتصادی توسط ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است.
🔹
تکذیب حمله به دادگستری بهبهان؛ فیلم منتشر‌ شده‌ قدیمی است.
🔹
وزیر دفاع کره جنوبی: برآورد سئول از زرادخانه اتمی کره شمالی بین ۸۰ تا ۱۲۰ کلاهک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/682752" target="_blank">📅 11:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apbdh9HOwDg5tygzl10U6ufYh-rP6W3yElIP1ktsVLXJ1z6YgisO_RTu03cj14j6FMbwXjXKI5ztbymknOGTg-OtS6y3jleeC8mUyCRpEt_5nRxR9mZLEthhpbDID3uVy-4jxLGRAxkYboYGr1BePaHsiDAiWUnanPNQmhCirbDwnpa8sg_tZ_I-7NYL0lPWYkWPUJATyZF-mE-ihhYzgXQzuGUzazRTElMcfsEFDJiimfvSbEQmZARKfJyLUTQfuefa57WF7ajUQIngIcXIW_AjoplSNG1P-RcsWpp58f-AjtkNA8tH0cmQPUEyPpWp0sfyJoWB1NU6ksGRhwjZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/682751" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682750">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAth-MXOnQ4hyy2mk7D9zGt8CgESjmjzJUA3nLV3VrkupROxVTXKXWwuNCGjkgefszcDK3b7wO1IuYRX-k-O-nNJGB7IZqqmxqUzyHJeiBBYmJXenJH1Knv6C1MD_V5w4HHSSi_oGU3Fi9HX15VxY7f7Ib67w3LslqVXSbFuD_oaaLfW-1pjFtmp9YIMuw56kxQBqEJ3XnpPNPANsIZmVgK2ePQuW8_5YDdBIPAW0WLtEj1O2A2wQ3HviuehwEjOn_l_vOY_--tsv_tYn6Iw2vQZnckglcnlNZmB7nikR9ZSVGaxlezFvZXxu_ecjZn1Fq6k0dHovuQSgXODpBGxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی تماشایی از خلیج گواتر، سیستان و بلوچستان
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/682750" target="_blank">📅 10:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682749">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede4a3da96.mp4?token=Z6z5HNs8EkJRLV9m3zYpbKVDx4E-tpwgha4ROZJGzYvrDjClCZb4ggwZ9UIq4NDA-pfIesRd_FBB7WkGCmkNQGkYh0wDVqlYD2Md8rMqlBcRH9D8aJrNfD5x5kO7As6iazd5T4EKyWZV-jnV7OC_3Wu5eLqOYixYZsOEWfvy4cuTzLeBV15YtT0xEGx915JLc9gQ1MLwPjP0qvuXfBiSyiPh-GXj2mED0evYVNkwR9COcbDcQGxIDXtulkSWYXCkzotWWiDP4gtr44PvBg4NN24Tnxtb_wAKe_-SKtvfFBYruZXDWWkMXq4B5NuIFtlhMrJf4917C0cOLKoqsMpsAWZ5_yNoRA6QDT2AmKILqz9ENE9fxm6eJS_lRVwE3xKKHDJMFORWMaAw3N9WH5hAOm_CdeVopqzy5cnQ0d-y48mSDS4DySnZKjk3atoAtL7dhPjsvkxVa9e_bv9A6zozGnQhDJaa7pq7XbE2fKibUJN6yfuYpSYaVtDheoyuaT_wcQaFGTfXUuak8uthrrOPbm1r9YrMtoi3Bs223QGNsSGDn8wLk5Bq967CAg0XWihFxnCyanWKob-S94wVkTbDRCLyV8XnpKr3OzJt2FkSSgrW_4jGVEspHtYcrFiv5gJu-3NGeA4RTF6OxCsWmTDXdLypan-uUFj6YNIlOTs7Yjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede4a3da96.mp4?token=Z6z5HNs8EkJRLV9m3zYpbKVDx4E-tpwgha4ROZJGzYvrDjClCZb4ggwZ9UIq4NDA-pfIesRd_FBB7WkGCmkNQGkYh0wDVqlYD2Md8rMqlBcRH9D8aJrNfD5x5kO7As6iazd5T4EKyWZV-jnV7OC_3Wu5eLqOYixYZsOEWfvy4cuTzLeBV15YtT0xEGx915JLc9gQ1MLwPjP0qvuXfBiSyiPh-GXj2mED0evYVNkwR9COcbDcQGxIDXtulkSWYXCkzotWWiDP4gtr44PvBg4NN24Tnxtb_wAKe_-SKtvfFBYruZXDWWkMXq4B5NuIFtlhMrJf4917C0cOLKoqsMpsAWZ5_yNoRA6QDT2AmKILqz9ENE9fxm6eJS_lRVwE3xKKHDJMFORWMaAw3N9WH5hAOm_CdeVopqzy5cnQ0d-y48mSDS4DySnZKjk3atoAtL7dhPjsvkxVa9e_bv9A6zozGnQhDJaa7pq7XbE2fKibUJN6yfuYpSYaVtDheoyuaT_wcQaFGTfXUuak8uthrrOPbm1r9YrMtoi3Bs223QGNsSGDn8wLk5Bq967CAg0XWihFxnCyanWKob-S94wVkTbDRCLyV8XnpKr3OzJt2FkSSgrW_4jGVEspHtYcrFiv5gJu-3NGeA4RTF6OxCsWmTDXdLypan-uUFj6YNIlOTs7Yjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظرتون چرا امروز یه روز خاص هست
⁉️
🔹
چرا امروز همه باید حواسمون به مصرف برق باشه
⁉️
🔹
چرا امروز چند ساعت بیشتر از روزای دیگه مصرف برق رو مدیرت کنیم ؟
🤝
همدلی امروز ما
✍
آرامش فردای فرزندان عزیزمون رو رقم میزنه
برای آینده آنها، امروز با آنها همدلی کنیم.
❤️
قرارمون همدلیه
🫶
📚
#کنکور
♥️
#قرار_همدلی
⚡️
#مدیریت_مصرف_برق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682749" target="_blank">📅 10:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682747">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/682747" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b404884170.mp4?token=EnMT2hlRbyT3zRCcVqxPrE4CRiBrbfCIK2fxIi3Lj2-IOgm-yyAyxpkC768g0G22Q_sLvzsjc5CNwAZwwAj3XyPsmwzWxdJf_I_5L2oHl7YugKGwPrvTDpd20ldPRrMbbwXBYtoFLh4Gz6KQNnecwKcaL87K1QINIe1cMFQZjBH3QFsjmCHFd1wVin6_r5m-cskI1wkftom25zoYWUifFE6igirmERRgTsjFTHVZRFN0Ws4XNSgCTiElMdi4YA4X-o3NOf4iXsUqo7DSVLOmUhmzfdrA2AL3B9CsyyHlOQVCMjJZnZQUPP1vZq6Y-nNzkMfWc80tKHSVz0FKhqy1ApZEAj1LJdYHJF2KxaI52stUSPNTmmCDFjZp3b3tMs2gINy6qpcxSnyGpz2HdfDflrVs2UAmJeBGsHN_vGuBLmiVZvc8HRA8n1Lbq5N397CFrjrv0q69D7za3PaaZPNyCE9Qdl94R4mV21PG4YzUWl_bZwvopJl7hBguzqy8RqSPWXfTdfJYhYzWGgYLXQnPJSeJo3pRTLsm9Nz88i5FaFf_kRImW6SeDVvYLb955B_22NhZ6Bmt_r6Bu96Cdno0dueqw4QuW0PysU02cA2TiPj39iyw_llbM1skoDgf36avkfhFitOmpcVQnXHmj21azZ7pLFBGdrj6g--BPupXR1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b404884170.mp4?token=EnMT2hlRbyT3zRCcVqxPrE4CRiBrbfCIK2fxIi3Lj2-IOgm-yyAyxpkC768g0G22Q_sLvzsjc5CNwAZwwAj3XyPsmwzWxdJf_I_5L2oHl7YugKGwPrvTDpd20ldPRrMbbwXBYtoFLh4Gz6KQNnecwKcaL87K1QINIe1cMFQZjBH3QFsjmCHFd1wVin6_r5m-cskI1wkftom25zoYWUifFE6igirmERRgTsjFTHVZRFN0Ws4XNSgCTiElMdi4YA4X-o3NOf4iXsUqo7DSVLOmUhmzfdrA2AL3B9CsyyHlOQVCMjJZnZQUPP1vZq6Y-nNzkMfWc80tKHSVz0FKhqy1ApZEAj1LJdYHJF2KxaI52stUSPNTmmCDFjZp3b3tMs2gINy6qpcxSnyGpz2HdfDflrVs2UAmJeBGsHN_vGuBLmiVZvc8HRA8n1Lbq5N397CFrjrv0q69D7za3PaaZPNyCE9Qdl94R4mV21PG4YzUWl_bZwvopJl7hBguzqy8RqSPWXfTdfJYhYzWGgYLXQnPJSeJo3pRTLsm9Nz88i5FaFf_kRImW6SeDVvYLb955B_22NhZ6Bmt_r6Bu96Cdno0dueqw4QuW0PysU02cA2TiPj39iyw_llbM1skoDgf36avkfhFitOmpcVQnXHmj21azZ7pLFBGdrj6g--BPupXR1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درمان غیرتهاجمی لرزش پارکینسون با اولتراسوند
🧠
🔹
یک بیمار ۷۲ ساله مبتلا به پارکینسون پس از سال‌ها لرزش شدید، با روش اولتراسوند متمرکز و بدون باز کردن جمجمه، در چند دقیقه بهبود چشمگیری پیدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/682745" target="_blank">📅 10:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی سپاه: با وقوع جنگ جدید، تسلیحات مخرب‌تری به کار می‌گیریم
سردار محبی:
🔹
قدرت تخریب سر‌های جنگی به‌کار رفته در موشک‌های سپاه بسیار فراتر از نمونه‌های استفاده‌ شده در جنگ‌های پیشین است و اگر جنگی آغاز شود، تسلیحات ما در تمامی ابعاد با گذشته کاملاً متفاوت خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/682744" target="_blank">📅 10:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c23aGKpAJ0lshfmNpDRHN1SrWntX4w8uYepWPFDLwGVdCraNxQNKQnk4yBaa6Mt1NoHYnE3ln2ZcaEHBL34jYg-RzFyd6FdGm7BQw2Wj4qRyiDruK9FF3B81MzIWKHyqbCq72imheAH6gDXG0ItGwRZktfhgz18WcbwvyPy2qFRkjJge6epLPb1Dx3Y93liO7Ts0oDdIt-OopxAu2qvO5UvMTHedcCDJtysvlVAnLWYvy4XpFh1ikQ37eg6mIggZJ-297W6CjULzaRab3A2kQSemQkoeC6bHqG4RJuUGF4uPp7DUsPLRvWy9oD10Xh_EML464zUW42S_2LZ-OsAz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/682743" target="_blank">📅 10:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج نهایی کنکور و آزمون پذیرش دانشجو معلم نیمه دوم آبان اعلام می‌شود.
🔹
قالیباف با مشاور امنیت ملی عراق دیدار و گفتگو کرد.
🔹
سپاه اصفهان: امروز صدای انفجار در محدوده جنوب این شهر شنیده می‌شود.
🔹
وزیر جنگ رژیم صهیونیستی: اردوغان ترکیه را به ماجراجویی‌های خطرناک در سوریه می‌کشاند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/682742" target="_blank">📅 10:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9NWij8E4KuWTSPUhYFWwHuQSDNNNF8sy5lYQ8m37OBo7dh4FHgEvFEMnl68WHxdn3IKb0BZ8ODTgA7zgr4UuLZMPUhce8hTBNsJGrix43mZTeq6uuSQbODI05tGWxR0FxpV13sE1ZWxRZwAQD21uEzJseb82WLJ2WkGAF7PdUbXQiPIhYgkIyCTDJX5N7QX2GRz9dBomchNv9gYrFh1eG7Tg-XWfbPsQkfu21XtwckqSRetDHyoQ1WQnlFFXeLYstsff6AYkZRDvRjRW9L16EFTdOjKp6_OXuLj6Vc3s0vHR_mQMF1rxTSH0nyaur6ubdf9268WADQs2gGfC4-HRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند
🔹
آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/682741" target="_blank">📅 10:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffdc10f45.mp4?token=uUl6p_XRXKa1hHRtnP6lOlmXv90pZZ5ky8Lqs2d5Qo0SzqYsbei2BwDmrcktgtrGGmUGY6CBj8tgC49PeLcWt8i5CuncbsnyjyJX5e4PfxtLMCKPiKyBMbH_IROkVXzjvVB9S8Dwhq13AAiKGxumXSG1bZJ-17bbEpRwQgU6v_Hf-t4NrulpXa3ovLsT7MZtB5NB75u1pcH5w3mX1boBf_KPvc3I1VjTqo0vkfP6eL3WpSNdRo1Iip4GsgNITZEKuuc6TwCzhQVeNkOCeGbzBeeJEL1rHykD310_F0hRihs0diPMnSmSoijffNZwZZJ721nh5ckh1luFPAdRgpqtCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffdc10f45.mp4?token=uUl6p_XRXKa1hHRtnP6lOlmXv90pZZ5ky8Lqs2d5Qo0SzqYsbei2BwDmrcktgtrGGmUGY6CBj8tgC49PeLcWt8i5CuncbsnyjyJX5e4PfxtLMCKPiKyBMbH_IROkVXzjvVB9S8Dwhq13AAiKGxumXSG1bZJ-17bbEpRwQgU6v_Hf-t4NrulpXa3ovLsT7MZtB5NB75u1pcH5w3mX1boBf_KPvc3I1VjTqo0vkfP6eL3WpSNdRo1Iip4GsgNITZEKuuc6TwCzhQVeNkOCeGbzBeeJEL1rHykD310_F0hRihs0diPMnSmSoijffNZwZZJ721nh5ckh1luFPAdRgpqtCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین با عطر این دمپختک باقالی بریم به خونه مامان‌بزرگ‌هامون
😍
مواد لازم:
🔹
۲ پیمانه برنج ساده
🔹
۱ پیمانه برنج دودی
🔹
دو پیمانه باقالی زرد
🔹
۱۰۰ گرم کره
🔹
۲ قاشق روغن مایع
🔹
۲ قاشق پیاز سرخ شده
🔹
نمک فلفل زردچوبه
🔹
۲ پیمانه آب قلم
🔹
۴ پیمانه آب آشامیدنی #آشپزی
🇮🇷
…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/682740" target="_blank">📅 10:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIY5l6_q6ceCTgi6qh_dKMB0vgxdnl2m-wKCgLNLMfCdwJunF7FIdQYKRLN8-_7bJX2gH4KDX_LYmQMw36K0_8YRwsOZlPhB-fwgGKXJrTho0N8WZMHt82XMulBe6yqHiUkZmcjXYv4S6ZpswgSfo9fUsAKaVtEn_x2P3gvAGVhVFrxfBDzhIq9-19I0q2g1Qo560f1YDXyiADm5Qf4YOhHuLBTQUkN7jrMtMRno-fchUnOFnLailNxCJGaMWbxG1mer3oABZzFtQNuqLCXW4anNHCi8l91UZIhBiqZCR7fPP3ZKC9wu7fDIS0w9xA8i4soQS4cuLrWKiE_4ZIHmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۵ گیاه که می‌توانید از یک برگ تکثیر کنید
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/682737" target="_blank">📅 09:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682736">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xji5Fb-YqzSSzI66fYOZab60RW5LSKPK9qdG-XaMheQXF1mXjkG2fLYGv8B05RXkxveaPpbqd78-Vft596cW9SCucfYn-WsRhcru-oYwlgl3jIiJY81hrUQVth-047Tuz2CpLf_NQPht3RRx3yqAQ7zcHK4X86gjntyLBsFT37RV1HyUth1ZVg6CRm04wUX1GC3jQ5qyg_RMJvUViTbTYLLOytdr3R9U3C-YWbDYqteAtyMXuDVrQg7GdUTrvTrbziwjZovbixUTBjhFKhdKTX-HecwCIlakGdoVL-_3MEl8vVIBPJl39PUEhLHEw4dUVCdlbDrcYpFV8ZtkgrcqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682736" target="_blank">📅 09:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682735">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1IDDbLLPr-G3DKuhQvLZt3FvA9ndCsZRFPhMsyfNEGt-oZzGnZdjhXa9T8cuXDt-hMhV9jA4cJyqH1yvVSHIpc-IXTJR_C8l535aaOm2qVG-n2yuEKf4ww0TGyAttGtgB5nPQKZYss_8E4w_QwmRf7S7OUDTKnRH5w6OPEqdNSjHygkh9yrDHhFjCqIMrL3Wyy5JjZsVGGEa-RF_FV8cM1-TCF7OB6VIsiHGIp91F9AlVF9Wenbrd0OC_xLVyvJUrGOy2YGVutT6CR1krlSkyYW1LLiadhsfOj-SaBNoFN59_vjM2x-LLseDfwEWsq6xH01PCGKSd79-iKkWz7Ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جهان ۲۶ درخت وجود دارند که عمرشان بیش از میلاد مسیح است؛ یکی از این درختان سرو ابرکوه یزد با قدمت ۴ هزار سال است
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/682735" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682734">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd9558ed7.mp4?token=uKu-TttrGM2OojXDuNh2p49q-XIq5kA_RKApqV6pDu_aUinFlstXxUo6xPKChC31AfUql55BJ-NGmIKV4LkBnywelgUaoVZkhkWNH8FCF-k4AZkzGgl2knSNYcslBKjqpci3Pbf3CLlQHGFgbZt6PuKCSjErG-ZZNs3YOU9CAW3v3Hh1ZM8gYo2tpSfmmokRoVUVOeudZ2jS-y_1qNxFcQhwsTkXooi7kL6nTJQFGeDDVtQJGbW8Q8bLz8K-qhfpKb_A7F381JXayuzOBegVwnuVn9WY8I_KSDw9mU6--anC3_qdClz4kuxB87lQghSmxpwZdd9zvtSMv24chAUEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd9558ed7.mp4?token=uKu-TttrGM2OojXDuNh2p49q-XIq5kA_RKApqV6pDu_aUinFlstXxUo6xPKChC31AfUql55BJ-NGmIKV4LkBnywelgUaoVZkhkWNH8FCF-k4AZkzGgl2knSNYcslBKjqpci3Pbf3CLlQHGFgbZt6PuKCSjErG-ZZNs3YOU9CAW3v3Hh1ZM8gYo2tpSfmmokRoVUVOeudZ2jS-y_1qNxFcQhwsTkXooi7kL6nTJQFGeDDVtQJGbW8Q8bLz8K-qhfpKb_A7F381JXayuzOBegVwnuVn9WY8I_KSDw9mU6--anC3_qdClz4kuxB87lQghSmxpwZdd9zvtSMv24chAUEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ملوانان ناو آمریکایی خودکشی می‌کنند؟
🔹
وضعیت بحرانی ناو آمریکایی پس از ماه‌ها حضور در جنگ با ایران که اخیرا مجبور شدن بهش پایان ماموریت بدن!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/682734" target="_blank">📅 09:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUPPSzH9yuin69oX4AKBlj8RB-3ZqBIes-7g40CRgW3mHtp-KAy5WRBBCCdv4Dw0lcJDdFgWVuSIvAgRiXlamWd04en7SZ1k2_OHcc3Gh6wI5b4sduGqM81LQHbKy0R_CX7dxUOJ20ivGd6FlniVfSVCDs7ux9_UzQNhx6_cZi4qCUnT2FD-fpLvyZvdEYuYXPXuBOxUlt_Y7TWBo6-0tUAdVAw418rHA6yJsE4HoxzEVLHybx28OcaAshmYEAibUDy_4Q7Pzb6-sW-aC_92tFpCNAj7gfiMLQ8260x3yIF50FgVnaZ0ED2T6IXpjwKoUUY-MD9EjMcgC21PF64gqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حکم اعدام تبعه خارجی دخیل در جنایت میدان علیخانی اصفهان اجرا شد
🔹
قائم حسینی، تبعه خارجی و از عناصر دخیل در جنایت میدان علیخانی اصفهان که منجر به شهادت مظلومانه چهار نیروی فراجا شد، پس از رسیدگی به پرونده و تأیید حکم در دیوان عالی کشور، به جرم کشیدن سلاح و ایجاد رعب و وحشت، ایجاد ناامنی عمومی و ناامنی در حد وسیع، اقدام علیه تمامیت جسمانی افراد و امنیت ملی به نحوی که موجب اخلال شدید در نظم عمومی شده بود، پس از طی روال قانونی به دار مجازات آویخته شد.
🔹
قائم حسینی به پیکر شهید نیروی انتظامی لگد زده بود و جهیزیۀ نوعروسان خیریه امیرالمؤمنین (ع) را به آتش‌ کشیده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/682733" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مقام ارشد امنیتی ایران: محاصره دریایی آمریکا، تجاوز نظامی به زیرساخت ایران تلقی می‌شود/ محدودیت تجارت نفت و کالا در انتظار کشورهای منطقه
اسپوتنیک به نقل از یک مقام ارشد امنیتی ایران:
🔹
محاصره دریایی آمریکا یک اقدام تجاوزکارانه است؛ نسبت به واکنش منطقه‌ای ایران هشدار می‌دهیم.
🔹
اعمال محدودیت برای ورود کالا به ایران یا افزایش فشارهای اقتصادی در شرایطی که محاصره دریایی آمریکا به مثابه اقدام تجاوزکارانه علیه ایران ادامه دارد، از سوی تهران به‌عنوان تجاوز نظامی به زیرساخت‌های کشور تلقی شده و موجب واکنشی خواهد شد که پیامدهای آن متوجه کل منطقه به‌ویژه همدستان و شرکای امنیتی و تجاری آمریکا خواهد بود.
🔹
جمهوری اسلامی ایران تحمل نخواهد کرد که کشورهای منطقه که به انحای مختلف در بروز وضعیت فعلی نقش و تقصیر داشته‌اند آزادانه به تجارت نفت و کالا ادامه دهند و ملت ایران به‌ناحق مورد فشار، تحریم و محاصره قرار داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/682731" target="_blank">📅 09:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
زمان اعلام نتایج نهایی آزمون ارشد اعلام شد
رئیس سازمان سنجش:
🔹
نتایج نهایی آزمون کارشناسی ارشد اواخر هفته آینده بر روی سایت سازمان سنجش آموزش کشور قرار می‌گیرد.
🔹
پذیرفته شدگان آزمون کارشناسی ارشد سال ۱۴۰۵ از اوایل آبان ماه سال جاری در کلاس های درس دانشگاه ها حضور خواهند یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/682730" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند
🔹
آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/682729" target="_blank">📅 09:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682728">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
میزان تاثیر معدل و سهم آزمون در کنکور ۱۴۰۵
رئیس سازمان سنجش
:
🔹
در سه گروه آزمایشی اصلی، ۶۰ درصد نمره کل متقاضیان از سوابق تحصیلی و ۴۰ درصد از نمره آزمون سراسری محاسبه می‌شود.
🔹
سهم سوابق تحصیلی پایه یازدهم در سال جاری به صورت مثبت اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/682728" target="_blank">📅 08:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC8kEWtLNq7oe8z67w10I3qOV1xnKUaoh1pDxBILHmWTc7K8BisSm1FL9AQMDBlrc14iCa9OndonOpuzg5U9m62x0It4oRV5mq9o-ut2GjHy98_IcYufcTAhJaFrtI9m1g2JIXIZ9Zy73hn74CC9A1eg5n6dls-axm67EL1fZSKbAuHofbpN4zegGz0PqaZ91iTFI9VTt8LLIsLQ3OmuwD0M8xfdYsBpBaFJTFcY-_vGoVq33WtuZw-QXVnbqqzu-Jlz1xo2kn4m6--zQ_NcGbfkhZdrXI6gGsKu7Q-cnKNXKgezPH3Gg-6bmDNdDTtwTSHftoeHZHIuHy3KZQdfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل ارزشیابی پیشرفت تحصیلی تربیتی و برنامه آزمون‌های شهریورماه ۱۴۰۵ اعلام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682726" target="_blank">📅 08:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/081eab3852.mp4?token=mvrF_yiDps9G7_9PlumorQ9nxN6VSAuYJnnGkcE911zbICKhQGFsoge2LiHPkfCVfdDUrMRXix8D4nliFE2SCdw3MfjDwVmahN2hPae4zFvdPXvggFOsIX2OAo65HxYB8b8OEIlND0yjbLb3oGddNVF2SgnHTp5OtIpoxnj6nKuodMS6_2nUNZUQ4YAhNsaMYLJ5_RGMSjb-LfI2q89sCJN7iWbdfhmp_PJ-o5e1ichmjrEf_Jv37uIKzrZshCX37KA_DFBpBPA59T2NGr7wVLcPuRsowVfJIpOSpUOVCTF-gpu5Etwi9J4jJQKDgqNYT0EJAbIBTOAvfMOJJYXmwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/081eab3852.mp4?token=mvrF_yiDps9G7_9PlumorQ9nxN6VSAuYJnnGkcE911zbICKhQGFsoge2LiHPkfCVfdDUrMRXix8D4nliFE2SCdw3MfjDwVmahN2hPae4zFvdPXvggFOsIX2OAo65HxYB8b8OEIlND0yjbLb3oGddNVF2SgnHTp5OtIpoxnj6nKuodMS6_2nUNZUQ4YAhNsaMYLJ5_RGMSjb-LfI2q89sCJN7iWbdfhmp_PJ-o5e1ichmjrEf_Jv37uIKzrZshCX37KA_DFBpBPA59T2NGr7wVLcPuRsowVfJIpOSpUOVCTF-gpu5Etwi9J4jJQKDgqNYT0EJAbIBTOAvfMOJJYXmwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بندر چینی در گوانگ‌ژو؛ باربران مجازی کشتی‌ها را از راه دور با ۵G تخلیه می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682725" target="_blank">📅 08:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df29aeb07.mp4?token=QvFypjhaX-1Eq599OBTVdLpA36N2pSNAmOrFkNc7fYucM0D4edRBJI0d1Bcefc4mhHeRRBn4NIf9BYPZpDnJUUboaI5D3ZcJe5KHadKHi0Q11Kil_dEEKAfDk8dLmO9nWnQkJTya4mdB-MdZBRw6qSycxMC29zKmxwJXu3MLXf9e8lCVPfItV2dlFJ_e9TmPR2QGkyHQj1O58oXrZ_sD8WtESqNpOC0UjqV8Pffi2UjmO_oFlSAfjcqbj4GFKmGIhsLbqf0jlz5qWaas9pJj0fQeZ0RQ04aZCeE_Ctotr7Fin-LbOetmKmIgTpwLgXh_DaqIlfcYbtJuQJcCquzCbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df29aeb07.mp4?token=QvFypjhaX-1Eq599OBTVdLpA36N2pSNAmOrFkNc7fYucM0D4edRBJI0d1Bcefc4mhHeRRBn4NIf9BYPZpDnJUUboaI5D3ZcJe5KHadKHi0Q11Kil_dEEKAfDk8dLmO9nWnQkJTya4mdB-MdZBRw6qSycxMC29zKmxwJXu3MLXf9e8lCVPfItV2dlFJ_e9TmPR2QGkyHQj1O58oXrZ_sD8WtESqNpOC0UjqV8Pffi2UjmO_oFlSAfjcqbj4GFKmGIhsLbqf0jlz5qWaas9pJj0fQeZ0RQ04aZCeE_Ctotr7Fin-LbOetmKmIgTpwLgXh_DaqIlfcYbtJuQJcCquzCbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند
🔹
آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682724" target="_blank">📅 08:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آزمون سراسری سال ۱۴۰۵ تا دقایقی دیگر آغاز می‌شود
🔹
امروز داوطلبان گروه آزمایشی علوم تجربی در آزمون سراسری حاضر شدند در این آزمون ۴۵۱۵۲۲ داوطلب شرکت کردند که در این آزمون ۶۹ درصد خانم و ۳۱ درصد آقا هستند.
🔹
همچنین بعد از ظهر امروز آزمون سراسری زبان‌های خارجی…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/682723" target="_blank">📅 08:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682721">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa0d09f26.mp4?token=vEvIZ9Mti-V_IyuIbLA1AfjdU8ClWVkR7nYrJutK6OdgSXo-HdC5-22NDkjn0jIM2eQmmBAX6WoOkngtBy6JRRqDAli6cRcHfy5FBQbp_Pwt41cj9On1Y58rEMkBdbZw9EEPuGO3I9UhehhjFBsvdVPvyxY6aDkH_vhM60_rIG9jYdD-z12kmRggn9kH0TPqOx-JaIjrmVUUSQKNcsGXCY2vXEaQv3n8GJVYC8wwhZHeHCpjDqulB9N4qMbybiAYEyothEVWEwlZjWGJwWP_TigT814a5sAeJJbcYsAOaxfE-B4dq-EX7J4giLPBymm3N3LgUpWixIPbokilrkbD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa0d09f26.mp4?token=vEvIZ9Mti-V_IyuIbLA1AfjdU8ClWVkR7nYrJutK6OdgSXo-HdC5-22NDkjn0jIM2eQmmBAX6WoOkngtBy6JRRqDAli6cRcHfy5FBQbp_Pwt41cj9On1Y58rEMkBdbZw9EEPuGO3I9UhehhjFBsvdVPvyxY6aDkH_vhM60_rIG9jYdD-z12kmRggn9kH0TPqOx-JaIjrmVUUSQKNcsGXCY2vXEaQv3n8GJVYC8wwhZHeHCpjDqulB9N4qMbybiAYEyothEVWEwlZjWGJwWP_TigT814a5sAeJJbcYsAOaxfE-B4dq-EX7J4giLPBymm3N3LgUpWixIPbokilrkbD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این چند حرکت رو توی خونه با استمرار انجام بده و تغییر رو ببین
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/682721" target="_blank">📅 08:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682720">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
کارشناس چینی: در جنگ فیل‌ها، سبزه پامال می‌شود
کارشناس چینی:
🔹
برخی کشورهای منطقه در ماجرای جنگ با ایران مصداق بارز این ضرب‌المثل هستند که «در جنگ فیل‌ها، سبزه پامال می‌شود».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/682720" target="_blank">📅 07:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682717">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آزمون سراسری سال ۱۴۰۵ تا دقایقی دیگر آغاز می‌شود
🔹
امروز داوطلبان گروه آزمایشی علوم تجربی در آزمون سراسری حاضر شدند در این آزمون ۴۵۱۵۲۲ داوطلب شرکت کردند که در این آزمون ۶۹ درصد خانم و ۳۱ درصد آقا هستند.
🔹
همچنین بعد از ظهر امروز آزمون سراسری زبان‌های خارجی برگزار می‌شود در این آزمون ۹۰۱۷۳ داوطلب شرکت می‌کنند که ۶۹ درصد اون‌ها هم خانم و ۳۱ درصد آقا هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/682717" target="_blank">📅 07:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682716">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcWXASBLWvaW6C2yXJLG4k5hiJYA6K8q2NUO1aPjqeCa7PkGxRdOI98QzIYo-ZGZ79fqOQgWnPwwkhA67LNbxGdd2neX-ex5JaO7rtQ1onZwY5Bz2XElnE9ch2Js2FcWVB8fNeMMMV2SbkkGD8Q5VFGAz_zTklGEjnXkNBymbI7QYhx8flfw1m2c6CQcrGiKDi5BHh80-MAbfUP9ZcZRe5oBxY6ey6Aol4-Ok7IN3mHeMyIyR4z4O_ymvOY-vp1F6cH5OVGUmR5IZ8fe46a_ijwayUteoPx4uWx22Te51jtx7SjbRSbBAtVtkz7txckukaHFhQN511r2joS4vPOEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۹ مرداد ماه
۷ ربیع‌الأول ۱۴۴۸
۲۰ آگوست ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/682716" target="_blank">📅 07:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682715">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muSula1_bj5ad10DiunjrVQYOXxlrPGKlS-rtP4ttjteHkrxLsO15FgK7q1lCCSP8yQY4kx5WCtXONfFp_Vgn-frLDmymcTZeS-pq4cZiBEHdhsEjlVEGPNjnYyxQ8gbDGe_PG2O1KktSjR7OsU0u8KVFCiFDhJOb05lZaOL2z6wpDgRp7z7Eb3I9t--h3MQ4zEMBnRsNGDG1j3A36YaoHjilOAitwrcaeKJ-G9GFC8kGC7dIRowHGsXJqFMInqhVayGHXU6KMQPayGrq60iXvsymO8nZkZ-BHV_Awhg2TKsmACmdci0bHFDY0_uV0bfz0kUNsMgCDYatmilTKsTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز توی سوپرمارکت دیجی‌کالا آتیش‌بازی تخفیف به راهه!
🔥
➗
کد تخفیف ۵۰۰ هزار تومانی
➕
تا
۹۹٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
با
ارسال رایگان
و زیر
۴۵ دقیقه‌
🔥
هرچی برای خونه‌ات میخوایی از  کالاهای
سوپرمارکتی و نان تا پروتئین و میوه
، با تخفیف ویژه موجوده!
🛒
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
DET555
⏰
فقط امروز
⏰
بزن بریم خرید از سوپرمارکت دیجی‌کالا
👇
dgka.me/ATTISHBAZI
dgka.me/ATTISHBAZI</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/682715" target="_blank">📅 03:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LajcW-5vxOyBJYKg5Eeb0z_oI20LXcWh0ezeJ5d8-XBItfUz31ZzqhoXR1o8FD6A9K7Lo2tBGMzGX3H5HCoLW5z-tXv-_1ziW_OnC8Tzwud4HCBrTGhFuyTUlihcrG27d7GWnYm9WePluHnVdRfjBqPLADTLCTmh9At_ZRmt9aIEGWTSDk7c32TnmvyE5lcc3BDo959ogHfN0bTg849VMx7XRCKQbogUFbm7CVEhuE17LquSAJeOo1_rPBhy0R69Cpglczk87AKgL-WG0dDklHCMegVSBeITb7Ng6ADV5YVX0ONDVS3Tb8Yg_XrNeUeUcWa2uvrv3ekuBgOUB-tEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد
رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز اعلام می‌کنم که سنگین‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد.
🔹
این یک جنگ اقتصادی و انزوایی در مقیاسی بی‌سابقه خواهد بود.
🔹
امروز همچنین اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی بسیار سنگین روبه‌رو خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/682713" target="_blank">📅 02:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c1ae5df3.mp4?token=bc0pvqDFIWO9_gysrqHpBiV633rtjo2CQO9yaXp1kBYS2MvaSAFMuJbCUrMe3gf3ynEF3sECVj6LS6j0sTPim7zwTy-da-wWl9eGaSS8sNdGzhDlQ7YNPyPrzMoKjDyfyzNwx06iXtvnZOzcYNGpKmWb6T6EjDupubTvzMJMrXLsRpOUkEx-jFB4gw0YY2rk8vi4EUp4hLoaIqECry1fiVjc1_c5xtwHhTxlkw-ujGQKj34ZxCzWR2DH3C-i22Mid_aOpWRs-cT97koirvLSM6fJBfFhWsC0ccCNAR6JZ_2mBeH9r_9eDwkWG82OUyv_j0Hjlw894VFkRuKOWXLT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c1ae5df3.mp4?token=bc0pvqDFIWO9_gysrqHpBiV633rtjo2CQO9yaXp1kBYS2MvaSAFMuJbCUrMe3gf3ynEF3sECVj6LS6j0sTPim7zwTy-da-wWl9eGaSS8sNdGzhDlQ7YNPyPrzMoKjDyfyzNwx06iXtvnZOzcYNGpKmWb6T6EjDupubTvzMJMrXLsRpOUkEx-jFB4gw0YY2rk8vi4EUp4hLoaIqECry1fiVjc1_c5xtwHhTxlkw-ujGQKj34ZxCzWR2DH3C-i22Mid_aOpWRs-cT97koirvLSM6fJBfFhWsC0ccCNAR6JZ_2mBeH9r_9eDwkWG82OUyv_j0Hjlw894VFkRuKOWXLT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات موشکی روسیه به پایتخت اوکراین
🔹
رسانه‌های اوکراینی بامداد پنجشنبه از وقوع چندین انفجار قدرتمند در کی‌یف خبر دادند.
🔹
گفته می‌شود حداقل ۱۵ موشک بالستیک و هایپرسونیک شامل اسکندر و زیرکان به‌طور همزمان از چندین منطقه روسیه شلیک شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/682710" target="_blank">📅 01:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL5dZiPA_fsoopmMPNNDmTrX8Lh3x4U47vQh6LCAtc-4K0YjUEvJYxZzbfI_QEowJqw-zu3zDpe9e2eptB3cf3MbNUmCA5NuJUTFODJZsm_cxmKhfMPwv72wiCdhlg4zZGwkNbS4HM7ZUhqf8x8zMM8k0PrjWl838vl2JMSXDt1z5iIrcQ17US1SVuMSR5_ejMVhOakprOamoafoReea9keDy09Zy31j4OpsW0smQxjSqjQH2dWsGlzlnZAjXhdW5nhS-ZY1DYK23glmG3GAJ4iNgxcrTwE1lCoO8-Ga5w3QVpXEd4dhKaCW6tXIqWEvCyoV0g08Wtt0mcVlzYEsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکایی‌ها واشنگتن را پیروز جنگ می‌دانند یا تهران را؟
🔹
آخرین نظرسنجی اکونومیست/یوگاو نشان می‌دهد ۲۷ درصد آمریکا را پیروز می‌دانند، در مقابل ۲۲ درصد ایران. در حالی که ۳۵ درصد معتقدند فعلاً هیچ‌کدام برتری ندارند.
🔹
۵۴ درصد جمهوری‌خواهان معتقدند آمریکا در حال پیروزی است، در حالی که این رقم میان دموکرات‌ها تنها ۹ درصد است.
🔹
در مقابل، فقط ۳ درصد جمهوری‌خواهان ایران را پیروز می‌دانند این رقم میان دموکرات‌ها به ۳۴ درصد می‌رسد. همچنین ۲۵ درصد جمهوری‌خواهان و ۴۴ درصد دموکرات‌ها معتقدند هیچ‌کدام از دو کشور فعلاً در جنگ برتری ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/682708" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Od40Z0AtopeKzNh3g_Ha3tXoOifv_gaMpnIJYYAHn35yakVRpjvWJwSfK3_rPVi5WpyBCYViVLAj_t2n7rqnvKUnqMj7DezH-G24yy7wAiyHJpA2V2Qq3wsPKYxi0W-6_w08SLyrFPZZPGERNGpjOFaEhHL1LAmdrUVPnrFWTNyNGKZbeRHvu7T7-3Z0gurFWpXCV4MG5k44lgO8T6f4fpJ11pI-dfZm7Ry8PfsrEcIwnXjRb4Yt7Z7r6JvB9ynJIELP4jtaYutEqkuPqMFS98h_Z91NNAzt3fctdae2yhp8jNx1JXqYLXXSxyrCBBKDDuzGig-8lOugFN0WkEMonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfeTANbjBY1P7-MObHDytvc0uA-W_x2Lk3sjatqWQErcl7RGMh06Rgjaa8cQWx93lKGS65ACsFTKs-fsCS3pyLaMvY9ZvTkDdlz4UrU8RXb-jfOM-9YIqsj-0zzwEgujDjndjePCLrxccgFW1ybsloDlHsWoFCrSXJ9WRVwr_jJczRpWVxUfq36vLfZE0mWqleSfuIPeqHWw-mRSY0Gru6jubgfTy2CzlwwPKPhda5HiucqDak078chRX4NGZNt6bl3fdRRedEV-PZDoLhiYsXRd86tFYL92MgVaEIKQTsYAd3OFx6P8PceZ471a8RvSepnu63jWbK8DmKn2g5_s3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCa3lIZapG-wJk0s8iWgf3azNrJxmldZTJ6TgvqG4GFmT9CjM6SwDRf4ZJXxfTFUdq9RYR9AbbLcrcHRf5XVjMbt2eR_EHCYL_9j6nV6EcWorb63QLAbyscYHnsZzb0fZNWc5nckkL9F8Lgkbv-MOunwfP6aNRUdJmdMYhakOVDPvjX0VSBid3p4kntwrCyLIVOBnrAjggq9U3t75JtQDR10g-a_wUhH9NKKxmjEMOFlcSKoQ1ohrDyOOWMKxr46knJAJS5cp5VTqE6Cs0dvMRUVqHhouwCv2Sdjy5jFzAhG41B80wEHaZlcfm7zWpbGYjQDZLuc7JZhddKMMoOYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAmXGCfuBJfu6kOjB0idaj64YhW3z38OHuZtE4kTEVs1Dx51tCEU8ll5KHFzJletqHnyIx0SRoQBxcX6Sy-vSbRrWk3nc5a0kjIXxk4XSL8FOV8pIZ415MnghMOwhdhMqTCtJUgXdYSyY03LP-5OZZhbnJVXMhrDxze8DZ7gMhaiLObghOBKTKgBaKRcYp65cAzgaCUxF4jnOilyIivTIFctS0ZA-BBnrc2QmiuzTqEmUeILT10WzCoRnSlgbZGx4pYwtItEfumSvjKfoMn9KMUH5q4yBPbgW43_FfMu3MIzISwQoN8dOB8_vsW27gSN5WrvC_tTDQWSGJZkJuENzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9qdIk9-TUfv482AKcgzKdlpw_dF8JMba0xHNtVutKQVQNpyrmWAaVsLkwiBCgziqc-H-bv3TXgTpnUVpYeTUiO8cp9s7cq1LPnUQFe6aYAoJb2wCojawN86pau9uB0himEyNFVgVGdZu6c8IhX67FLco_Dh2HRja2zeioAl8isuU8m2p0ERMmadUqxaXIE4Q9zDmK_tRHNF791PH7wbUizM9gg8ulqAi-eT-uSs5IymVi8w8ZP7x_0EVSkICFVUeZLl0-G46wFA-DBKbQI9uMEpV5xIj0gnjveaxYItyBlkarFaxApsui0UFTCWiqQHPbLeqMnqZ-5emXP8ZYhf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-o9JfanO1V5uCq8k_O6YvcUj6Y77uam6Z-uFkc03hNjV7nCkrhIPxkJ7ZP6BVgZoFiW2db3DFVisBG5gGNbYKDsgQ5oDmGwdIIsQbFG6UOx5D0-qR7QYVU4TG-1g-2Fwd96D5UKCfCeMQm_cKE66E-lC8u08OKller5GMfymDF-f1i-5HawVRio3eeSsaKukf9bf-6xIpXrQflVDFcn5ZzImg0phJTftg44uiKyOz0VYc5nyTeL7Kql1N4u4pwyCFRdP3d7tWx5JzqPX4tOi9npgsErAIOIjpMxrXS1XeFFn5inarNguwhdYMou_dJPUojX8v6UXhtEkgN9Z10sFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نقشه جدید اروپا در جنگ ایران و آمریکا
🔹
اروپا در جنگ میان آمریکا و ایران کجا ایستاد؟ اگر جنگ جدیدی شکل بگیرد، اروپا چه نقشی خواهد داشت؟ پشت خروج ناوها، واگذاری پایگاه‌ها و تحرکات دیپلماتیک، آرایش متفاوتی در  اروپا در حال شکل‌گیری است.
🔹
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/682702" target="_blank">📅 00:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGHcG-NNfI9wZlpSFnQXrugOUbFgUyCHVugUHJHEJm7qxsCFnCe_xCf0wjRPpjmrLz6Qn_GGpXdwC0_8kjDiG58UTxxXHpot9H9P0WpuRxKgTimysNHq388db08elAtanU94y7C1cKhb_ELKqS3VewuMmaJjyvMya0iMMcyT5KS6w01G_G4f9Q7-hPKWJKitvqCZEPiyPFM6gXFhe6Q1PtP7D78LZ3qPcYCzZpsI8oK-nfstfwqgKVul63mX-O3T5hkSRPRPu8fAT9lx6AjqeVYfpR1qB93iWWdtFKF_740c3vLXx2D3bbqI5cS_bJZF65FSObq71LjnLtUTkvrNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روبرتو کارلوس شایعات مربوط به مسلمان شدن خود را تکذیب کرد
اسطوره فوتبال برزیل:
🔹
من برای دین اسلام احترام زیادی قائلم و دیدن اینکه همسرم نماز می‌خواند، بسیار عالی است.
🔹
اما شایعاتی که در مورد مسلمان شدن من منتشر شده، نادرست هستند.
🔹
کارلوس به تازگی با زنی مسلمان ازدواج کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/682701" target="_blank">📅 00:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69147ef19a.mp4?token=vthOo5rPxyHcHYpHVSQprskYeBBf8ni7UPvBplyXzdqjvTTffrX-826eRqyS986wF7jr1gSw-JBmcXNa1GjYKNrCcfsk_OSkAdhCGkiJK1hh5Q6e5zFNLIKU76HjR1kCJhLHZVcrMlyG6FxCATWpNdXdH6p2qnjIStZZ10_VwNqlXQlbTNe70P_DpnhVMO143MdpiPKL2gmzas_QlEzct6LRH42ICMqjBbr7KkdHwKJBWW6z681C-YSBB7LZVRiQ4M11RDDyO-4SrrYrjECApniGCK0IfW2QcrVGQhLbm2JGJhlEJn_X8jfODqCxNRKxzNcUam_3Dnx92a-PgewZmk4nG_hB3b3nUFB_2AZIa-z3u-ikInzUEor91cGcrM1YVIy-la7eHxnUdjtTrmLHG8yDPenDyh-PdceLgcY51M5XrJX9vNIbefcwu4F2h9ROiCxy5e1uwFFAH8uSOAS1Q9wxD5md2fEP03yoCADyyAtu6RXCFqRNNt6UgQq6IETVZai_vNNx5TYF1S5DPXN_eMObx1Vizhf2WzCmlneWejiStleSbOLqryvlkf60SVV0hgXUF9ziqCyQdq4w7xeDRrdPny4fup-mmZBPeRYceh6ZkirZh0SnzKUYiP-yIvpJH4WTFIvSXnZM8j--ph71UbVScH6qKMUeo_ouqPTV5zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69147ef19a.mp4?token=vthOo5rPxyHcHYpHVSQprskYeBBf8ni7UPvBplyXzdqjvTTffrX-826eRqyS986wF7jr1gSw-JBmcXNa1GjYKNrCcfsk_OSkAdhCGkiJK1hh5Q6e5zFNLIKU76HjR1kCJhLHZVcrMlyG6FxCATWpNdXdH6p2qnjIStZZ10_VwNqlXQlbTNe70P_DpnhVMO143MdpiPKL2gmzas_QlEzct6LRH42ICMqjBbr7KkdHwKJBWW6z681C-YSBB7LZVRiQ4M11RDDyO-4SrrYrjECApniGCK0IfW2QcrVGQhLbm2JGJhlEJn_X8jfODqCxNRKxzNcUam_3Dnx92a-PgewZmk4nG_hB3b3nUFB_2AZIa-z3u-ikInzUEor91cGcrM1YVIy-la7eHxnUdjtTrmLHG8yDPenDyh-PdceLgcY51M5XrJX9vNIbefcwu4F2h9ROiCxy5e1uwFFAH8uSOAS1Q9wxD5md2fEP03yoCADyyAtu6RXCFqRNNt6UgQq6IETVZai_vNNx5TYF1S5DPXN_eMObx1Vizhf2WzCmlneWejiStleSbOLqryvlkf60SVV0hgXUF9ziqCyQdq4w7xeDRrdPny4fup-mmZBPeRYceh6ZkirZh0SnzKUYiP-yIvpJH4WTFIvSXnZM8j--ph71UbVScH6qKMUeo_ouqPTV5zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گره فوق العاده عالی برای بستن کیسه‌های پلاستیکی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/682700" target="_blank">📅 00:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac1dmVeYFCkhuzZFhQm6YVxwsHY566Qlz3RNqINIp9kxgMyZszjyElMG_4bw4HcneykIPhd0MyIz1ZiOj0L3i-MOxCy2w43ylf44rHcuuU7g5fmVyIsocVVZBIE8uvs5H8wgmXhNT0p4PWMKm8zYDGtkJKBsu8ADrCMMJAbVrikz-ciiakWM7QgpiEYrFZZ0eq1Uw1YaCejLcGnLoXgB5owcw804NiQ9KZtBcaxVFkvVHni_XzV4wsVK40f0AxsN7h0OnnG6jlxLkMexPLj9kzOJlF4W7op3LOCKS8Cxsj6L5fGy9SaEW3a5jrvraavoUq0amEYaEaPBq55sGe4xKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدهی عمومی آمریکا برای نخستین بار در تاریخ رسماً از مرز ۴۰ تریلیون دلار گذشت!
🔹
داده‌های وزارت خزانه‌داری آمریکا نشان می‌دهد که رقم بدهی داخلی دولت این کشور از زمان دوره اول ریاست جمهوری «دونالد ترامپ» در سال ۲۰۱۷، دو برابر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/682699" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682698">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBE74-0axrxFwM0lzv3glvGmeuLIk-0N2S1yhfE42kBZrwbXAGGkFBdAbE9GI80KyKQaOQjRoF9FaHF8hOdqVrbVvTlUpBiHu3HBpAJ52mD5Aweh1CCutg0Ir-C94xVvp3aPbU_DgnFR-p2bZz-Bduf051MWFnskTs7hzA_6XtRym46KAZRNhuv-dVKtaV2g252oo3j5NqL4MDQtA568JB9NZuEcNUgHAOgeBPMlSk_BxQVct2AiAZbEunGPeMLWFAWYwS7BZzD8SEfMObCpJSJkiogyfF2ga5vBL4u9gS1vQiTQ1pRrgLhgm_TGT_pfDL4U739UWE8hdpMna76Hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنگ دندان فقط یک موضوع زیبایی نیست؛ دندان‌ها با رنگشان هشدار می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/682698" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQWLcW47erbirY_eMkfDcClnmVGDBwMC0j71UebAJOGRSsxGo5BPotk1V-JwUj-3BrXpG-cPqZIS-be_BaxP1hstSEpicyiEStQTraa8gC9cSdRZad4OlsBvZ7rrIi9veIudbJnTGvC5HALZMHBiA1iCqe12gBm91oeEgDW7fYK2WlXZcqgVbJkjCiL8l5HCV2SlUrBLSp84lSbvVTbZZApmFmZsY4ofjZ2ALDaQ-etCrgXlXslWTAZOar5IsFXFFcwQaznmzvxrvkZP3A-GWvDsd8oxVReMriE8iab7-tBvZi4LQ-8FJENBkdo6tLZSQL2DStl-HdrovKd7mKr5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی‌های مناسب تولید محتوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/682696" target="_blank">📅 00:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
شکایت جمهوری آذربایجان از شبکه سی‌ان‌ان
وبگاه واشنگتن اگزمینر:
🔹
جمهوری آذربایجان از شبکه خبری سی‌ان‌ان به دلیل انتشار گزارشی جنجالی مبنی بر اینکه رژیم اسرائیل تیم‌های پهپادی و کماندویی را از خاک خود علیه ایران به کار گرفت، شکایت کرد.
🔹
در ماه ژوئن، سی‌ان‌ان گزارشی منتشر کرد که در آن ادعا شده بود ده‌ها مأمور موساد و کماندوهای رژیم صهیونیستی از یک پایگاه مخفی در جنوب جمهوری آذربایجان فعالیت می‌کنند و از طریق آن مأموریت‌های جمع‌آوری اطلاعات و حتی ترور با پهپاد را انجام می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/682695" target="_blank">📅 00:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تغییر نگاه مردم ایران به طلا: طلاسازان بی‌ چاره شدند
عباداله محمدولی، عضو هیئت مدیره اتحادیه فروشندگان طلا در
#گفتگو
با خبرفوری:
🔹
به جای اینکه فقط به ذخایر طلا فکر کنیم باید به سمت تقویت تولید برویم و چیزی که می‌تواند جایگاه طلا را در اقتصاد تقویت کند تولید، فعال شدن کسب‌وکارها، ایجاد اشتغال پایدار و ورود ارز به کشور است.
🔹
امروز حدود ۹۰ درصد مردم طلا را با نگاه سرمایه‌گذاری خریداری می‌کنند و فقط حدود ۱۰ درصد برای زینت و مصنوعات طلا خرید انجام می‌دهند و همین تغییر نگاه باعث شده تولیدکنندگان مصنوعات طلا با کاهش تقاضا مواجه شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/682694" target="_blank">📅 00:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjhuL_EZFW4lrzOp7aksYywefyZtv73ihzdEZzqd3wkw6O528HsZPqUlhBZVXkm1uoENC3TVUSKhMm-UmJgyrEKLRUI7Z6DG19lTtFIyu9LskwitH5p4otZcCVsW_mzN8BDeGAk9OOsKvAHbtsMrwqfgpsEE8Mn41K2o1jrFibsvoCHM8DbQx9gN_EAy-3kUgogYWyICdY7szKmjs8v-L3VbhM7CRswe_F_h1BelT3glLNYMfhEiP4hFOYf7Ot2oH7GwJUWb2zXrnVohSHY9AkkxJ1H0tDg_1kEkDwesXdHgp9i-oqNsNzT3SSgmHQf6ga0Jwc87eI-iAsXduziShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انس طلا به ۴۵۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/682691" target="_blank">📅 00:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0xL5Tusm5ICIczvZkTOpgcmNnml4WmD5L8-kfFy3NVruLhS3GYiivbTjapDfaJaFbrJ-1OwzbMOymPCwsmsFQzMAKdvVctTBGAr99E273DzenBUCfnZ5Gj0QKLX8MEatBud8rKR3jDQePkkLckcP1GZvFz7drzgnvcd65vjKuBOR5w9vspEc2uUw85kKVDOVIbrhLFM074qdcCapZAJApdRAXdFpIzjr-UcLO5prxCPGSHIQtKMDN_CpF9kuiY5xUvkjWRBMuLgZXAz8lIBr7mckU53oDUaCjK7HcoCk1vc-T7EB9glF8-5mKgy-KWJXrK2sgxGqQe-sYzFvLnM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/682690" target="_blank">📅 00:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682689">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381825a269.mp4?token=S5hSQn3xz8Tcb-nMKXQpnMPen-UnJyzHiTOFplXeFLfGzCHH_g-J3hOU-ujNbCkD8mwMIPb2kr2LxId4KmkLAqAJRNIofs2-fWCu8S1WRvzrK1HiaXi2iDHUaOPqy5OX962mlQ2D5oMgWLe6PGfr37-gIskHnMfuHGhftSpAPrCEfrK8b2TVrYv-LlcdJpPHV-0o9q_AGWJ--5v3Au0BZN1KSouOnEfOQAPPJ3wMfc7p1cHWWVGXrakk-eGEkS0rHACc6OF-fiuNPNYfTJ9iAAepW1CoMWhaTE5wtMi7Ly0kQRw0HpLH4ogVWCMcMGZa1dct3Ojk29vq_q7oev4zRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381825a269.mp4?token=S5hSQn3xz8Tcb-nMKXQpnMPen-UnJyzHiTOFplXeFLfGzCHH_g-J3hOU-ujNbCkD8mwMIPb2kr2LxId4KmkLAqAJRNIofs2-fWCu8S1WRvzrK1HiaXi2iDHUaOPqy5OX962mlQ2D5oMgWLe6PGfr37-gIskHnMfuHGhftSpAPrCEfrK8b2TVrYv-LlcdJpPHV-0o9q_AGWJ--5v3Au0BZN1KSouOnEfOQAPPJ3wMfc7p1cHWWVGXrakk-eGEkS0rHACc6OF-fiuNPNYfTJ9iAAepW1CoMWhaTE5wtMi7Ly0kQRw0HpLH4ogVWCMcMGZa1dct3Ojk29vq_q7oev4zRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمب خبری هانتر بایدن: ترامپ از خون و ویرانی در غزه و ایران پول می‌سازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/682689" target="_blank">📅 23:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
جان بولتون: عمان مشکوک است
جان بولتون در گفتگو با پایگاه خبری هیل:
🔹
تهدید جدید ترامپ علیه عمان نشانه‌ای از این است که او در دریا گم شده و نمی‌داند در بحبوحه این درگیری چه کار کند.
🔹
عمان «انتخاب مشکوکی» برای میانجیگری در این مذاکرات است. ترامپ استراتژیک فکر نمی‌کند. او دامنه توجه کوتاهی دارد و ما تا حد زیادی به همین دلیل در جایی هستیم که اکنون هستیم./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/682688" target="_blank">📅 23:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7eYixVcR6igr9aJUfc-YgKn2c79o4T8ZvReI2FvBgWSp4-224BBKdzkTemwENgbNVvLZKeBjhHTB4ZvIznzYUn16rBKAYGoUP9zYP82gvJMm8zJV_1LmC02XxclgcSxMAG9SKdT214bH6ZhfcWNV3qpAl8Nur6330ejLb0QYUCzooK634CZp8Y58a6fQzEjJiZJuUCDO0rxzYYjyflwRW92eV427Mwyyyyfz3rgXQ5N--OePUBH1LC3qrXm4VynFhWM0MZ6ssugQ5zyTVJ3G-dWCmjV7TrwZicqKocHcCBJPaR0M66BzJUjZgutw7bOv5hU5qWahJbeWpXumYAhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سمت دشمن
🔹
امارات در ادامه هم‌سویی خود با آمریکا و اسرائیل، تمامی مبادلات تجاری و معاملات مالی با ایران را تا اطلاع ثانوی به حالت تعلیق درآورده است. این تصمیم به گفته منابع اماراتی، پس از ادعای شناسایی دو موشک بالستیک ایرانی که مسیرهای کشتیرانی را هدف قرار داده بودند، اعلام شده است.
🔹
هشتصدوسی‌‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/682687" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1w3EPpmRFvXhgqStpKKCt1yQcC7Ga7kxB_n1fsWX6Sst1HyszxMzZn4z5yHvgfAUoE7VQlblHj2JHMMEPwfKsQGcVXOhTNlKiIQqBeim_5U9YHslO8Wex87jIK9sFu0u4LjLJxcJ-m48vqk-zCpakPX3ZWCGQwUVCLDJPAMZvhArASheby6PaM6C-A0EwaYAAk0NBEbIzCMuLfEzN8M11gkABXbjq3tIod1wCpYfMHmaZ0Wd4orjV0r8Ea1ZF1rheY81nEVXAnyrYgKZD7DbSDhxatL59RF0eb0aplIwxQwtV7wm3KKJty__TSZZ_bu6IdtHXZDzF8gjw3GXNq0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرسودگی ناوگان آمریکا؛ فرصتی تبلیغاتی برای چین در اقیانوس آرام
🔹
به گزارش «اسرائیل هیوم»، ادامه جنگ با ایران فشار زیادی بر نیروی دریایی آمریکا وارد کرده است. ناو هواپیمابر «آبراهام لینکلن» پس از بیش از ۲۵۰ روز حضور پیاپی در دریا، با کمبود غذا، مشکلات آب و فاضلاب و نگرانی‌های فزاینده درباره سلامت روان خدمه روبه‌رو شده است.
🔹
آمریکا برای مدتی نیز هیچ ناو هواپیمابری در اقیانوس آرام نداشت؛ زیرا ناوهایش به خاورمیانه منتقل شده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/682686" target="_blank">📅 23:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpRq4GaLaqRCZKrwUb9BOdsTXnvinIouwdRDHCCsE6rdio5ztmy0RgJW9uw5UwHWLtw0m14v8bS5XFd3YNuSf1KwWvUpLn5qOC5IpCD0xrVhYcWwKGNXhb2jUGhzDFEEbWKRXWrB20xH1AFCW04HbnHLscMlG-QCAOiHsp23ZUTbYte9HQ2oTI2dreFRq6ksth2qH9XkLa8NPE1xX_hgR2NF2MPEFeU05LpU7L8goU_Gy7ku6XRCKF_5NX5mM4kIUAL-FPDiLgayHQu64pXUPQViJk0U9vXWWDxro8YkKwWKW82HAWYZg-VZV6Oi2ARfzaSfiQG9vLTZTn6TA6RfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و آمریکا در آستانه کدام جنگ؟ / ۵ سناریو درباره آینده رویارویی تهران و واشنگتن
🔹
شش ماه پس از آغاز درگیری، جنگی که قرار بود کوتاه و تعیین‌کننده باشد، به یک بن‌بست فرسایشی تبدیل شده است؛ تنگه هرمز به مرکز ثقل بحران بدل شده و هم‌زمان با عقب‌نشینی دیپلماسی، خطر یک محاسبه اشتباه می‌تواند جنگ را وارد مرحله‌ای کاملاً تازه کند.
گزارش کامل را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239054</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682685" target="_blank">📅 23:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9840899c49.mp4?token=Suux_QfGp4rJ6G84NBYeFeJrO7SDJJXLmlMalDYybDC1baofwILwaVB__Xidq_ngkDyJComvK30WfyvbMGqs5Yqo4WhLcfbUwj6dsS24RDaGWpTvc5ifnfBhCJLnwXHfdHJlwo4u7Vp_eTkOQjJziaLxnZzvoO2VsJccTpjiyYSRqOz8z7uycrD69rdaE4ZzKDRQcg1MnU7xlj3DewJ63spK_zK4xmtlhAQSdMJ7bgcmZDDnLRHtd_4LwrBmwrx11CFqnl0av_RCcM3-k0MWa0T3uklQv6cTHcSliCV-9CJvGzF8Ya3pyCLrIQcYL_pOxBuFh8jL4T5zXFAogAQw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9840899c49.mp4?token=Suux_QfGp4rJ6G84NBYeFeJrO7SDJJXLmlMalDYybDC1baofwILwaVB__Xidq_ngkDyJComvK30WfyvbMGqs5Yqo4WhLcfbUwj6dsS24RDaGWpTvc5ifnfBhCJLnwXHfdHJlwo4u7Vp_eTkOQjJziaLxnZzvoO2VsJccTpjiyYSRqOz8z7uycrD69rdaE4ZzKDRQcg1MnU7xlj3DewJ63spK_zK4xmtlhAQSdMJ7bgcmZDDnLRHtd_4LwrBmwrx11CFqnl0av_RCcM3-k0MWa0T3uklQv6cTHcSliCV-9CJvGzF8Ya3pyCLrIQcYL_pOxBuFh8jL4T5zXFAogAQw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با بطری‌های دور ریختنی گلدان‌های جالب و زیبا بسازید
🪴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/682684" target="_blank">📅 23:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون بهداشت: مافیا خود ما هستیم
عمر علیپور اقدم، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
اگر دارویی در کشور پیدا نمی‌شود اما همان دارو در بازار سیاه مانند ناصرخسرو وجود دارد باید پاسخ داده شود که این داروها از چه مسیری خارج می‌شوند و چرا در داروخانه‌های معتبر به دست مردم نمی‌رسند.
🔹
ما همه مسلمانیم و نباید دروغ بگوییم مافیا خود ما هستیم و باید ریشه مشکل را پیدا کنیم و ببینیم داروها از کجا ناپدید می‌شوند و چگونه سر از بازار آزاد درمی‌آورند.
🔹
وقتی دارویی در داروخانه‌های معتبر نیست اما در بازار آزاد پیدا می‌شود یعنی یک جای کار در زنجیره تأمین و توزیع دارو می‌لنگد و باید مسیر خروج داروها بررسی شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/682683" target="_blank">📅 23:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ترامپ باز هم درباره هرمز به تناقض‌گویی افتاد
🔹
ترامپ متوهم که در داخل آمریکا به دلیل افزایش قیمت بنزین در نتیجه جنگ علیه ایران مورد انتقاد قرار گرفته اظهارات ضد و نقیض خود درباره تنگه هرمز را تکرار کرد.
🔹
او از یک طرف مدعی شد که تنگه هرمز الان باز است و…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/682682" target="_blank">📅 23:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ژنرال نزدیک به نتانیاهو: اسرائیل برای حمله پیش‌دستانه احتمالی به ایران آماده می‌شود
ادعای میدل‌ایست‌مانیتور:
🔹
سرلشکر اوزی دایان از نزدیکان نتانیاهو گفته که اسرائیل در حال جنگیدن برای "بقای خود" است.
🔹
او هشدار داد که این کشور نمی‌تواند به طور کامل برای مقابله با مسئله ایران بر امریکا تکیه کند.
🔹
دایان گفت که اسرائیل خود را برای امکان انجام یک حمله پیش‌دستانه علیه ایران آماده می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/682681" target="_blank">📅 23:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9b4d4640.mp4?token=kXjZl31E3eVvLlRm3MWTTavQxAKIHj7IIl3AW19oW0rYBg_liIjJyrz9Bn7b_WdLsc8clAj72wvjf2i-6dk59lBMj3Dmsu_xMDYhKOPV1dz41hUvexTiuyZVZ19tTFwGG_Pys90oFWUFs46Reu3Oxy04NHqaRX1vvL1XQV1gmbv3_5XZ6V6dOuhT7fuII0ALti7t1MzCWl6bSkQ6I_l90GMx8sPaAhETQx2iuKsmyWRyshQ01Luok2xMvSWrVroMF2_Gh8PsvZ2CD2tFba_kYeGqrKtAO2iII3WkBuJ5LJeF5XxKEhfAn2AxiVGK203vV1o8MR1vBRFU03ZjJBJMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9b4d4640.mp4?token=kXjZl31E3eVvLlRm3MWTTavQxAKIHj7IIl3AW19oW0rYBg_liIjJyrz9Bn7b_WdLsc8clAj72wvjf2i-6dk59lBMj3Dmsu_xMDYhKOPV1dz41hUvexTiuyZVZ19tTFwGG_Pys90oFWUFs46Reu3Oxy04NHqaRX1vvL1XQV1gmbv3_5XZ6V6dOuhT7fuII0ALti7t1MzCWl6bSkQ6I_l90GMx8sPaAhETQx2iuKsmyWRyshQ01Luok2xMvSWrVroMF2_Gh8PsvZ2CD2tFba_kYeGqrKtAO2iII3WkBuJ5LJeF5XxKEhfAn2AxiVGK203vV1o8MR1vBRFU03ZjJBJMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بخش عمده‌ای از تورم مربوط به تخلفات بانک‌ها است
🔹
به‌هیچ‌وجه در قبال بانک‌های ناتراز مماشات نخواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/682680" target="_blank">📅 23:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ed8453ff.mp4?token=T22vh9p-6ti2XFoEPB-8U-FFvd5SW4ZdUn0prAMEXadiKqfRmJSL23YWar87ftKcNG1rxNt88ZutWW31jueY-DjwmXe9p89V4Z-F65gTEpRVVBWX5Ey7oqLXYqGO6yKXivSlO3ivcN08f0egEFKJtnrsdYWfPnKC1RHImzoX5oNt46tFpljIpE3YsN_J59jSeFhN3E0ZMPRie8Ea78bXcc43CtAf5K8awCSzxpMxAO3ITEdEI6-NavJXIqk6tedbLviXprlt5Lu0HjUtFVGdIbAAkxUa6E76Z4XUc2rQlxjtX0VgRg3M8A3AK2Zh7N0WGJRa7O57lqlfMoPLItKCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ed8453ff.mp4?token=T22vh9p-6ti2XFoEPB-8U-FFvd5SW4ZdUn0prAMEXadiKqfRmJSL23YWar87ftKcNG1rxNt88ZutWW31jueY-DjwmXe9p89V4Z-F65gTEpRVVBWX5Ey7oqLXYqGO6yKXivSlO3ivcN08f0egEFKJtnrsdYWfPnKC1RHImzoX5oNt46tFpljIpE3YsN_J59jSeFhN3E0ZMPRie8Ea78bXcc43CtAf5K8awCSzxpMxAO3ITEdEI6-NavJXIqk6tedbLviXprlt5Lu0HjUtFVGdIbAAkxUa6E76Z4XUc2rQlxjtX0VgRg3M8A3AK2Zh7N0WGJRa7O57lqlfMoPLItKCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادت کوچک غلطی که اگر به صورت نادرست هم انجام شود به لثه‌های شما آسیب می‌رساند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/682679" target="_blank">📅 23:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a488bd8cda.mp4?token=HZv0z13-dh2CwQdtM5ZyExqa6oLawzJr_HnJo8pQUIaf84CYg7ovRytbBWf0lGQaW3OZCUM-cavQ0VcgVJnhGlJ9mIS-czw0WaFZhxOYD7HYJgB6b-ujuEomXPgnJQbid98-bUm613JLYJWp1-47RqrMf2W1fCv2EcnwYnn-8QqBQKuzbDPIFmBaHNyqSFoBkbWMCbrMcL3whp2pKdBTsBoqWHN2-HaloKt23qWZi_s8lJdcWbq-_Z5zkupn73N9e9xE6FAnhUT36PgXq4l8KaUxuhirREFA9hUFBd-HKEiKZ3ZUngwltwVC-4wKmBfpmJYcVIdp2jYFPlBcsAX-yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a488bd8cda.mp4?token=HZv0z13-dh2CwQdtM5ZyExqa6oLawzJr_HnJo8pQUIaf84CYg7ovRytbBWf0lGQaW3OZCUM-cavQ0VcgVJnhGlJ9mIS-czw0WaFZhxOYD7HYJgB6b-ujuEomXPgnJQbid98-bUm613JLYJWp1-47RqrMf2W1fCv2EcnwYnn-8QqBQKuzbDPIFmBaHNyqSFoBkbWMCbrMcL3whp2pKdBTsBoqWHN2-HaloKt23qWZi_s8lJdcWbq-_Z5zkupn73N9e9xE6FAnhUT36PgXq4l8KaUxuhirREFA9hUFBd-HKEiKZ3ZUngwltwVC-4wKmBfpmJYcVIdp2jYFPlBcsAX-yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از قانون نبوغ تا ترامپ نادان!  ترامپ: من قانون "نابغه" را امضا کردم اسم آن را به افتخار خودم گذاشتم
🔹
من نمی‌خواستم از اسم خودم استفاده کنم، بنابراین فقط آن را "قانون نابغه" نامیدم. #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682678" target="_blank">📅 23:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
همتی: بسیاری از همسایگان ما حتی جرئت عکس گرفتن با ایران را ندارند
رئیس کل بانک مرکزی:
🔹
بسیاری از کشورهای همسایه می‌گویند حتی برای نشستن، فیلم گرفتن یا عکس گرفتن با ما تحت فشار قرار می‌گیرند.
🔹
جمهوری اسلامی یک‌تنه در برابر استکبار ایستاده و این ایستادگی در جهان بازتاب گسترده‌ای داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/682677" target="_blank">📅 23:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g33BY0nRDUYOt10gidWnV1IuCVP-5_bEF-_LTIW4A9CMDXXjoai-1JE1aFNiweBWe4awffOL8fZR77Ii_dTz-I0txypnw5kgEDd5AhCBx_pNQ-2BHMQ5bK9JHyee_aADaH8J_rvOHDgycosNtTvFzbftMboPoT8q2ShvBFM2NwhbbDpZwhM19T3Vm5m7z6Rf_WB1m_ahXFf49i0QseZOy1mej54kQh6BzKhQsAFEba4xz4LEysLWjT0Q5vZz256Nu9G0S5wPdpsiu1bEY9m10QBcnp4Vzy2cF-Ypgbsq0M3sXrjXi5a_JJCceY33eWv-ly6J4bY2VXHZ9ckIW5k5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بایدها و نبایدهای شب قبل کنکور که لازمه حتما بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/682676" target="_blank">📅 23:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمریکا واقعاً می‌تواند وارد جنگ زمینی با ایران شود؟
🔹
پشت تهدیدهای واشنگتن، یک سناریو مطرح شده؛ اما ورود زمینی می‌تواند برای ترامپ از یک عملیات نظامی، به یک کابوس سیاسی تبدیل شود.
🔹
چرا حتی بخشی از جمهوری‌خواهان هم با این گزینه مخالف‌اند؟ پاسخ، معادلات جنگ را عجیب‌تر می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/682675" target="_blank">📅 23:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بازار کار کوچک‌تر شد؛ ۶۱۱ هزار بیمه‌شده و ۷۷۰ هزار شاغل کم شدند
🔹
گزارش مرکز پژوهش‌های اتاق ایران نشان می‌دهد بازار کار در سال ۱۴۰۴ تحت تأثیر جنگ، بحران‌های اجتماعی و اختلال اینترنت با فشارهای جدی روبه‌رو شده است.
🔹
تعداد شاغلان از بهار تا زمستان ۷۷۰ هزار نفر کاهش یافته و بیش از یک میلیون و ۳۵۸ هزار نفر از بازار کار خارج شده‌اند. همچنین شمار بیمه‌شدگان ۶۱۱ هزار نفر کمتر شده است.
🔹
در همین حال، افزایش اشتغال ناقص و رشد ۱۲ درصدی کارگاه‌های یک‌نفره در کنار کاهش بنگاه‌های کوچک و متوسط، نشانه‌ای از تغییر نگران‌کننده در ساختار اشتغال ایران است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/682673" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=P7ulKC-dVgqZlnryGieb4C2TsNv9_jB022qbSc8IaCgXXltyyhj8JAUBJhuhISxgKYqAJ6UK3VQLFR-HtWWnYEiJW1pLNk87HebmZvnHA6d9R4cfFfuQv019XeX2T4yHEMWBs9yA6e9f6JiCYHIGmpm8pkP4MhTUYEYbrFJzmdwRdHtxtxXRBQurtYspmMaesFBeiDMqQT3x81kGQRqnihCGd384R8Gby1DiPKAtISHoYNpzT0slnp9h-bZVFFi88-QTyQHan1rn9YVHFg-9V2q96XwJ183dE1xwxz56mcA4tZ1_LhMU0pvJRfhtlf0QDSQg2D0Rwt-aiX2tbnRcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=P7ulKC-dVgqZlnryGieb4C2TsNv9_jB022qbSc8IaCgXXltyyhj8JAUBJhuhISxgKYqAJ6UK3VQLFR-HtWWnYEiJW1pLNk87HebmZvnHA6d9R4cfFfuQv019XeX2T4yHEMWBs9yA6e9f6JiCYHIGmpm8pkP4MhTUYEYbrFJzmdwRdHtxtxXRBQurtYspmMaesFBeiDMqQT3x81kGQRqnihCGd384R8Gby1DiPKAtISHoYNpzT0slnp9h-bZVFFi88-QTyQHan1rn9YVHFg-9V2q96XwJ183dE1xwxz56mcA4tZ1_LhMU0pvJRfhtlf0QDSQg2D0Rwt-aiX2tbnRcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بخش عمده‌ای از تورم مربوط به تخلفات بانک‌ها است
🔹
به‌هیچ‌وجه در قبال بانک‌های ناتراز مماشات نخواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/682672" target="_blank">📅 23:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
همتی: بانک مرکزی هیچ برنامه‌ای برای تغییر نرخ سود بانکی ندارد
رئیس کل بانک مرکزی:
🔹
افزایش نرخ سود بانکی نیازمند الزامات ساختاری است که در حال حاضر به‌دلیل ناترازی جدی شبکه بانکی کشور فراهم نیست.
🔹
بانک مرکزی در کوتاه‌مدت هیچ تصمیمی برای تغییر نرخ سود بانکی ندارد و روند سیاست‌گذاری موجود را ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/682671" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051dde39f2.mp4?token=oTJ7E7xO1vOgHfdn3ScEEvK0kLsw_M-dHNDfT8xWWb8QVf5JFuuATYDdiAzuJIon3SS1UQ3PeHaBc2rnEEMWe6GHCfUAVICvAiLlMuTXhRLnIBZuso36PO54OCTgJMVfFTxnLP_bkB1VBxYk8Nrv2jjMYmsYEUUDmZLh2XBky2tv6ugtq0kgaiQG6tFVPpq7pM5SGqAx6OIzMT9SKWxGR5LNut4RlG2u0K_r9wWerj5JbO6FbjN7AGMfwMBl8mTRKQEBq8zIxcKASCez8hbI3GlkOScYPjwA-9LLBm5uOd04ytY4RZVq9VEOfoN4i-hULWyJXj3doOwQu1x4s1-Ghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051dde39f2.mp4?token=oTJ7E7xO1vOgHfdn3ScEEvK0kLsw_M-dHNDfT8xWWb8QVf5JFuuATYDdiAzuJIon3SS1UQ3PeHaBc2rnEEMWe6GHCfUAVICvAiLlMuTXhRLnIBZuso36PO54OCTgJMVfFTxnLP_bkB1VBxYk8Nrv2jjMYmsYEUUDmZLh2XBky2tv6ugtq0kgaiQG6tFVPpq7pM5SGqAx6OIzMT9SKWxGR5LNut4RlG2u0K_r9wWerj5JbO6FbjN7AGMfwMBl8mTRKQEBq8zIxcKASCez8hbI3GlkOScYPjwA-9LLBm5uOd04ytY4RZVq9VEOfoN4i-hULWyJXj3doOwQu1x4s1-Ghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از قانون نبوغ تا ترامپ نادان!
ترامپ: من قانون "نابغه" را امضا کردم اسم آن را به افتخار خودم گذاشتم
🔹
من نمی‌خواستم از اسم خودم استفاده کنم، بنابراین فقط آن را "قانون نابغه" نامیدم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/682670" target="_blank">📅 22:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
همتی، رئیس‌کل بانک‌مرکزی: کالابرگ باید ۲۳ درصد افزایش یابد و به ۱ میلیون و ۲۳۰ هزار تومان برسد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/682669" target="_blank">📅 22:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98f856478.mp4?token=fLXXNNisfcsMEIWlFEGoiSNVFXD0YQwEmfOPDGbm8Pj-pjKBn69zt0kVZsoFBwTa-Ppig0pp_Sn6RL-tQ8-VsDd1ngfaZrjetihfJIWjzocMsSUDAzeC_XiIfE6cHRsjyW5haTEYcBAf1xtBZ-D4_4utniPZq1IZ_uMAlYju1WKcH_XIENnihGqWExPzuSW2o78wg1Y6TnYFLq8FRS2_U1iDTwmbMiW-SELIfHnzP8HEIUUN1Dn9L8b0VmKecnr380DMHI7eS__p3vYMR7KE3kmLa-X3T4BbEF4t9oQYGKD7-E5vbhFhq2H-JbcgouYgit2bk7IymJ3zLLHkzu1N-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98f856478.mp4?token=fLXXNNisfcsMEIWlFEGoiSNVFXD0YQwEmfOPDGbm8Pj-pjKBn69zt0kVZsoFBwTa-Ppig0pp_Sn6RL-tQ8-VsDd1ngfaZrjetihfJIWjzocMsSUDAzeC_XiIfE6cHRsjyW5haTEYcBAf1xtBZ-D4_4utniPZq1IZ_uMAlYju1WKcH_XIENnihGqWExPzuSW2o78wg1Y6TnYFLq8FRS2_U1iDTwmbMiW-SELIfHnzP8HEIUUN1Dn9L8b0VmKecnr380DMHI7eS__p3vYMR7KE3kmLa-X3T4BbEF4t9oQYGKD7-E5vbhFhq2H-JbcgouYgit2bk7IymJ3zLLHkzu1N-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک Y2 Zhuque-3 ساخت چین بازیابی مبتنی بر زمین را برای اولین بار تکمیل کرد و راه را برای موشک‌های قابل استفاده مجدد چه در دریا و چه در خشکی و هزینه‌های پایین‌تر هموار ساخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/682668" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVcpCikZKFJfdFBv_XISZt0YZEukm8ySw3wjBU4_OdJgfJnwD7tq2mUh4GzHj7ZekICQsLU1ZKSv47tSvJRr2ZCBu4H1yv8H7psbiN4IKyEkD9pDhzMU0LyB9hzPNV5QoSfUP762BCvJJVECc65xaBQEQ_mtp1WJY80B-42IXGtFgjta-4096opX-wvySfhKv2NfenWzGXEm7RU3Aj_eunLfeYzxysNIQmM7bVcmXlEIMP3ayUvBNOD1M4K5AywaXZgmMD6VbWuSOg8x1E0FVyivCiU6Jw3hu0dH6h4zQH4UV7g_LxKUh0eAB6ij8BK7J9UyWWN2qLjpT87aEZy5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آناتولی: عراق از ایران خواست تنگه را به روی آنها باز کند
ادعای آناتولی:
🔹
عراق از ایران درخواست بررسی ویژه در مورد صادرات نفت از طریق تنگه هرمز کرد. این درخواست در جلسه‌ای در بغداد بین روسای پارلمان دو کشور مطرح شد.
🔹
عراق همچنان در میان کشورهایی است که بیشترین تأثیر را از تحولات منطقه‌ای می‌پذیرند و بر اهمیت روابط دوجانبه عمیق‌تر و همکاری فزاینده بین بغداد و تهران تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/682667" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da6b7d5420.mp4?token=azPsQl9kpNhaVZ48b0Cuw5uMX2TczLAxGko0hG3HvUo-c9x5GAl_S_Bgh7rHOnsr0of954jBn8LUI75KPBrFMLqXy3BvahpggrZvsmgeU65YFbofgMBPbIQJilAhE6x9Mqhjz1iOkXcQENh1q3qN_8oFxoXBaKf0tR7TP1fK0sstkLuqHJhK6ogetrWOysEbdk0fZlS84lw1xQoo276HsApGd4OINDOyPju-jtBVZaqNH2FiYU5H0vRYUwjWppjn63OJwW-cp7AiedBE1SQxUl8CS_uDYkR1hI58dBGdu440OKDX_PMVcnVqxbbbx6LJTXLU0syPptt4AapIdKB_wTDDVuTxW9VYrDYCuetAvZzpY7hOAMLvlL_Jixlc29HRjib5OuWVY_lWGhwJhBd-6lu1-hDIM2AAAljjzeDBYgSRHAakEwbUwrhFZhGjcLaNW_0OAh7W9wFD5YRPTUuWNAa2BNILDmNvppy9xaQu7w4DdE_2f0wSNg-XER_0qyvd9stJDWmVtZIzNYsybCQ-OzGaIr2AmGT9bHakIkCIJa7JhOmkwBT3NfQgtQEoXgVodCImAKaOPmHUErGY0BotYyp6V-yKDUzFHPc_v6pbrNjjebR1fHhLcHIssFzz0rOnhg01Tq0SXbkpBDkJXns9A-rylvZj81GN2IjqKNi3sC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da6b7d5420.mp4?token=azPsQl9kpNhaVZ48b0Cuw5uMX2TczLAxGko0hG3HvUo-c9x5GAl_S_Bgh7rHOnsr0of954jBn8LUI75KPBrFMLqXy3BvahpggrZvsmgeU65YFbofgMBPbIQJilAhE6x9Mqhjz1iOkXcQENh1q3qN_8oFxoXBaKf0tR7TP1fK0sstkLuqHJhK6ogetrWOysEbdk0fZlS84lw1xQoo276HsApGd4OINDOyPju-jtBVZaqNH2FiYU5H0vRYUwjWppjn63OJwW-cp7AiedBE1SQxUl8CS_uDYkR1hI58dBGdu440OKDX_PMVcnVqxbbbx6LJTXLU0syPptt4AapIdKB_wTDDVuTxW9VYrDYCuetAvZzpY7hOAMLvlL_Jixlc29HRjib5OuWVY_lWGhwJhBd-6lu1-hDIM2AAAljjzeDBYgSRHAakEwbUwrhFZhGjcLaNW_0OAh7W9wFD5YRPTUuWNAa2BNILDmNvppy9xaQu7w4DdE_2f0wSNg-XER_0qyvd9stJDWmVtZIzNYsybCQ-OzGaIr2AmGT9bHakIkCIJa7JhOmkwBT3NfQgtQEoXgVodCImAKaOPmHUErGY0BotYyp6V-yKDUzFHPc_v6pbrNjjebR1fHhLcHIssFzz0rOnhg01Tq0SXbkpBDkJXns9A-rylvZj81GN2IjqKNi3sC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی، رئیس‌کل بانک‌مرکزی: کالابرگ باید ۲۳ درصد افزایش یابد و به ۱ میلیون و ۲۳۰ هزار تومان برسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/682666" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cd10c07b.mp4?token=pcBNpevbmTgE0DER7fCt7WHHMsiA9UAsagbo1BHmTqIlENapVB_2M12fRvyh9C-phoGhisYKJHUWEZplskgtSI5NL1urTs4EThPcJqw3G4TpPvjqiDrxbm2eGrd-7w2AFmGT_lMLCtTOuMcD4gnkCo6z9qc8py2HpHSdqhtGbO9SYEj3oQsx1yHhfih3X6lPbuOG3f43kfALLZtpmJfyhs7qs8L3aM5GjdIyuG39cEkZPl___bnIb4HlJ5IkSW46UE9qz6qhFGyjTeA8wahikGaksZuVkpVzvLwlNe64B0tdUYufCtyWqKY2fZby86C_6O1uzvPj52NgOS-Dn0fokzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cd10c07b.mp4?token=pcBNpevbmTgE0DER7fCt7WHHMsiA9UAsagbo1BHmTqIlENapVB_2M12fRvyh9C-phoGhisYKJHUWEZplskgtSI5NL1urTs4EThPcJqw3G4TpPvjqiDrxbm2eGrd-7w2AFmGT_lMLCtTOuMcD4gnkCo6z9qc8py2HpHSdqhtGbO9SYEj3oQsx1yHhfih3X6lPbuOG3f43kfALLZtpmJfyhs7qs8L3aM5GjdIyuG39cEkZPl___bnIb4HlJ5IkSW46UE9qz6qhFGyjTeA8wahikGaksZuVkpVzvLwlNe64B0tdUYufCtyWqKY2fZby86C_6O1uzvPj52NgOS-Dn0fokzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جعبه‌های کاغذی ساده در چین که به کسب‌وکار بسته‌بندی لوکس تبدیل شده
🔹
این جعبه‌ها در چند ثانیه تا می‌شوند و به کیسه هدیه‌ای شیک تبدیل می‌شوند. ساختشان کمتر از ۱ دلار هزینه دارد، اما می‌توانند ۱۰ تا ۲۰ برابر بیشتر فروخته شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/682661" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0026d21b5.mp4?token=QpedyB-q9E1xQD1HaS8iWpYiUJK7Qqq20RGNcZDOIknjYePAQC5VpLwg3gwgVg7G37-BjxbtBwzWYz1cyQ64MhlF1lXfdIzh12-dM7oYMKuKu7-v4kdrUVstUNgmEFtBwCjpt_uZrJUuMwcikljGSaCqOi_A7D7rswGg2mnGBHimJbHhcOdzvcz9VbY7HauBW9_pQDsEb1pV4n_isUpbui35lqi8QGmMF3bm-EECua8hnrOjaqVbc_g6I2SC61KWN1MOwbjhYpsJaO8aV68bM5c_2b4x8yz1rqolETQt26pUn_TvUXi_lAdnhqsGiYKXB5wL7pUFr0Q4mOLPW_c3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0026d21b5.mp4?token=QpedyB-q9E1xQD1HaS8iWpYiUJK7Qqq20RGNcZDOIknjYePAQC5VpLwg3gwgVg7G37-BjxbtBwzWYz1cyQ64MhlF1lXfdIzh12-dM7oYMKuKu7-v4kdrUVstUNgmEFtBwCjpt_uZrJUuMwcikljGSaCqOi_A7D7rswGg2mnGBHimJbHhcOdzvcz9VbY7HauBW9_pQDsEb1pV4n_isUpbui35lqi8QGmMF3bm-EECua8hnrOjaqVbc_g6I2SC61KWN1MOwbjhYpsJaO8aV68bM5c_2b4x8yz1rqolETQt26pUn_TvUXi_lAdnhqsGiYKXB5wL7pUFr0Q4mOLPW_c3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیشنهاد ایجاد کریدور مالی در بریکس را ارائه کردیم/ باید وابستگی به ارزهای دیگر کاهش یابد   رئیس کل بانک مرکزی:
🔹
اگر بریکس بتواند ایده‌های خود را به مرحله عمل برساند، ظرفیت‌های قابل توجهی خواهد داشت و به آینده آن امیدوارم.
🔹
پیش از جنگ ۱۲ میلیارد دلار…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/682660" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687bb05d6.mp4?token=nq6nN-ZPXs88gMEjGXw343ONFoLyFD6pPp-r5nTH3bUttx4uNsIeCQ_iu02Ulu-eLcX1DjRO0ZTRUhbRROgCq6HAC1c2TaCUtYmB_maaZHLADg5WahEzK7MwXWVNIIO0ojGpdwdsrO1ufqI_X5QS8fqvmHaBkTb7c_FZm-Gu6djPmFvspPxc699MFy6V8h4qpC_tJtP1zCf5IxvESz_yuvDq-C-yVplrdJjTGm1lKV6sf81cTq_piYELdVxpHBJzY6vFpvyWE-JMBUYaG9r9xNYD0gTXXdqy97yknZoBz_qOMVvQ6p50O22YevCb5yJCo8OQss04YDOVGPI-x-igcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687bb05d6.mp4?token=nq6nN-ZPXs88gMEjGXw343ONFoLyFD6pPp-r5nTH3bUttx4uNsIeCQ_iu02Ulu-eLcX1DjRO0ZTRUhbRROgCq6HAC1c2TaCUtYmB_maaZHLADg5WahEzK7MwXWVNIIO0ojGpdwdsrO1ufqI_X5QS8fqvmHaBkTb7c_FZm-Gu6djPmFvspPxc699MFy6V8h4qpC_tJtP1zCf5IxvESz_yuvDq-C-yVplrdJjTGm1lKV6sf81cTq_piYELdVxpHBJzY6vFpvyWE-JMBUYaG9r9xNYD0gTXXdqy97yknZoBz_qOMVvQ6p50O22YevCb5yJCo8OQss04YDOVGPI-x-igcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیشنهاد ایجاد کریدور مالی در بریکس را ارائه کردیم/ باید وابستگی به ارزهای دیگر کاهش یابد
رئیس کل بانک مرکزی:
🔹
اگر بریکس بتواند ایده‌های خود را به مرحله عمل برساند، ظرفیت‌های قابل توجهی خواهد داشت و به آینده آن امیدوارم.
🔹
پیش از جنگ ۱۲ میلیارد دلار صادرات به عراق داشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/682659" target="_blank">📅 22:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پازوکی، اقتصاددان: اسرائیل و رقبای منطقه‌ای خواستار انزوای ایران هستند
مهدی پازوکی، اقتصاددان در
#گفت‌وگو
با خبرفوری:
🔹
شانس دوبار در خانه ما را زد. یک‌بار پیش از انقلاب که درآمد نفت بالا رفت و شاه با کنارزدن تکنوکرات‌ها، زمینه سقوط خودش را فراهم کرد. یک‌بار هم بعد از انقلاب که برنامه چهارم را کنار زدند.
🔹
در برنامه چهارم، تعامل با جامعه جهانی در چارچوب منافع ملی دیده شده بود، اما هر بار از تعامل حرف زدیم، گفتند وابستگی است. من صراحتاً می‌گویم تعامل اقتصادی ایران با جهان به نفع ملت ایران است.
🔹
اگر انضباط مالی، پولی و اداری را حاکم کنیم و از جوانان تحصیل‌کرده استفاده کنیم، می‌توانیم آقای منطقه شویم؛ نه اینکه نهادهای دولتی محل دفتر و دکان افراد بی‌دانش باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/682657" target="_blank">📅 22:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17dd06b49a.mp4?token=W1l0FZhBK5cCvVWw0QN8qAHBg7X0BbxNkUad6iLEm8gEcAzxEN5vqKOSKt7S9vs1qMYvoIvCMnIpKkwWJ6xluLT_mT1ehF9h_8Y5KTiMKcE5tr1542iMaR6Bve69ssFZEbrbR7ehSXalBvqOgEmpAw5nG_D4bT7z9CpdXYMLWZtg0EHbV_SXHx6njqbWDYf3J2Q1aky-yMayEPHqI0lx90Uc9ras0O4cx2X3lwUp8U0vJ4-QNKp5rTh4jcwviKhN5KL5DEgABzup8CkCZYQ2J9EhSwtpP91xWvqhyoyNhEIibl7qXkAoBliNi9QJlq44_RDcQCrK81zooKhzQUzHFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17dd06b49a.mp4?token=W1l0FZhBK5cCvVWw0QN8qAHBg7X0BbxNkUad6iLEm8gEcAzxEN5vqKOSKt7S9vs1qMYvoIvCMnIpKkwWJ6xluLT_mT1ehF9h_8Y5KTiMKcE5tr1542iMaR6Bve69ssFZEbrbR7ehSXalBvqOgEmpAw5nG_D4bT7z9CpdXYMLWZtg0EHbV_SXHx6njqbWDYf3J2Q1aky-yMayEPHqI0lx90Uc9ras0O4cx2X3lwUp8U0vJ4-QNKp5rTh4jcwviKhN5KL5DEgABzup8CkCZYQ2J9EhSwtpP91xWvqhyoyNhEIibl7qXkAoBliNi9QJlq44_RDcQCrK81zooKhzQUzHFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: مشکلات بانکی ایران و عراق طی هفته‌های آینده برطرف می‌شود
🔹
عراق صدور ضمانت‌نامه برای پیمانکاران ایرانی را پذیرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/682656" target="_blank">📅 22:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2770ae392f.mp4?token=Ah5sY2ToZJy27xuV4RFkGhCY3ZM1dL9SSOPS6pyL7oNJwzsahpElKNEY9U57WRtcM92X2HpyFOubrqblVpFHuBq9CNlqEh0VjHp93m0Xu02gndwgRn40Gl5k2t1OO8HybvugRlRPJVXqExu6_seRH4S9OpF2vLNK5Tjn00Yt5D7otLw4DKhB21I-dGzXRUwRv_eA35KND-_5fo9bvLPFKG2o-XbYsKOWfNJOS_tScHh0SzB1R8Aa99-LYc2ZEMuDibeRQDaRzvdggI8iJjHf2-EP73A_ITcHqHZhLE-rhJHiMnVmi79fynaHXJUaG2SPOAoGPH8ZFuXos9qeHrBP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2770ae392f.mp4?token=Ah5sY2ToZJy27xuV4RFkGhCY3ZM1dL9SSOPS6pyL7oNJwzsahpElKNEY9U57WRtcM92X2HpyFOubrqblVpFHuBq9CNlqEh0VjHp93m0Xu02gndwgRn40Gl5k2t1OO8HybvugRlRPJVXqExu6_seRH4S9OpF2vLNK5Tjn00Yt5D7otLw4DKhB21I-dGzXRUwRv_eA35KND-_5fo9bvLPFKG2o-XbYsKOWfNJOS_tScHh0SzB1R8Aa99-LYc2ZEMuDibeRQDaRzvdggI8iJjHf2-EP73A_ITcHqHZhLE-rhJHiMnVmi79fynaHXJUaG2SPOAoGPH8ZFuXos9qeHrBP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از لپ‌تاپ دوربین‌دار شیائومی با قابلیت‌های عجیب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/682655" target="_blank">📅 22:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a5db559.mp4?token=kdK9_AYN4NS2qCrQHlwrnGlDLOiG3uoncBMu4bZJmJw9cpZqDP3mrftQW4ZojaQCDUv0gzzOXxcpp8ogWbcFjo4_NXzKHMN4tF0ux1gQrNCYoLUe2GIHl_lHxze-9s5qExPrTKOe4EOGlMqN8GsNMQoU8WjPht7lMgHQ6Y2j6j0SySOEWCgbTp6AfosOtWSZsRzX5SfhjnmBrVSG4HndlblZvP2PYxC5Lp_lvehNF5GakEQHvmYfUwvdtNkIckm_rqCJlHouBWSiML-v8CG9mEvFSaGwoLXuRGvDA4HeEot8uTcFev8ZbcohmTnMf4qFBVB0CMELAoOELmWJ2ufYyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a5db559.mp4?token=kdK9_AYN4NS2qCrQHlwrnGlDLOiG3uoncBMu4bZJmJw9cpZqDP3mrftQW4ZojaQCDUv0gzzOXxcpp8ogWbcFjo4_NXzKHMN4tF0ux1gQrNCYoLUe2GIHl_lHxze-9s5qExPrTKOe4EOGlMqN8GsNMQoU8WjPht7lMgHQ6Y2j6j0SySOEWCgbTp6AfosOtWSZsRzX5SfhjnmBrVSG4HndlblZvP2PYxC5Lp_lvehNF5GakEQHvmYfUwvdtNkIckm_rqCJlHouBWSiML-v8CG9mEvFSaGwoLXuRGvDA4HeEot8uTcFev8ZbcohmTnMf4qFBVB0CMELAoOELmWJ2ufYyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/682654" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6jvkRQ43MdVBvppeEHkRCBlFkdlkcSLm_tVuin9NUBfYmEWM4A-k7TWt3gbYWprVTDhtfxz_GApuQckJs2isKki1XvevQADX3gX9Zjpast67vnEOcr0qvxmgSVJ00DT1yLU5hsvu9Y07R2AEFEuF-kjdEZfPrqJjVXTDizJVgousVZzsCBC_RO2G6FT8eGhxjFYLlghyT7ux6b-IjDm8x4m0XovsjSfpxXaVjILYkRWVtBel0X89jJgi4HIGCOrg_X2cvGtskTqsTTLnkz7npRyb24Cw9G81GUkcZ9udUjBSBmQ_OQ-hJ9_zgYE3yNQYzeTG6oicYCMXOd35Lccmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ مورد از عجیب‌ترین لحظات ترامپ در مورد جنگ ایران | از «ایران توافق کرده» تا «هرمز مال ماست»
🔹
این هفته، دونالد ترامپ، در حالی که جنگ ایران وارد ششمین ماه خود شده، مجموعه‌ای از اظهارات جنجالی و گاه متناقض را مطرح کرده است؛ از تهدید به جنگ با یک کشور دیگر خاورمیانه گرفته تا پیشنهاد تبدیل تنگه هرمز به قلمرو آمریکا و حتی ادعایی که با پیام‌های رسمی دولتش درباره مذاکرات با ایران در تضاد بود. و این تازه تا روز سه‌شنبه ادامه داشته است.
ترجمه گزارش سی‌ان‌ان را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3238948</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/682653" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682648">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxxqSUG5t4RjwjRvZnBHGCZT26XldzWGHSoL5ph-Nw5dUmUD2GOv0EbKqi2OpFzWpfXOfUqF09IZJdaBzB00u_3w6gSZMLfbaP9A3FugXVrBRh5G2RTXowLb3vYb7BFONSWdbYYnuw3JQXeFqN_jMTRe6hFs7qUNVlDb-kMQQ0PYuyOD3_1MXNB0GpUofe_eIgquy3D8bkmwM6_srFeOETAWDRs-rkDBqCxTJ4YvxoYg_xfMoQVq4eD5pck8mZ8MGrcePhgBHb3IQWc76H-hsc6bJE9lrEDlNggjWIq-d5gS6AAB9ojji6YPPLomriUlGmHXJQbYZrjb6MAk9Rkyeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ietaZ3uqGw9Se-Jk0cYYQn19Lke-3tAykQD4r4dKXiUyXBMfVBsx599HYInufxUsFwx2ogVCaCfQEqiT4p8xCCZzmRCeEZuZEq7Csuy1tc2K6Yjyy8oc4fEhvaion-iFfq-D7rW-i1mOL00IbD2KOdxcSELz64T-3TNIb7W_2hNZsVlsLWppTdc3l4JhFlQOrFjXIqdNSldQeaz-jbDoxaM-2qtXEotWNIMvAzPKAdjtAEKESppbf20ttilRqPLXRZlHuQmqKYSAgkKQVoG7CByRZiQ-4KAnPHo-FtG6N--yCk-lf4dkAZEZlvU_NkVINCYLf10psTT6vCCqnAaNKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b991cf3af0.mp4?token=adR4V_0liKv2GBat-25wREl1q2_Mur9WJomFsFyU2vA0HczRcoZlLSAwLiEN7pSpdndKAf1C15T37PnbPZtJgk3BYnV7_nEfTbRwaT9IIIP0g1no5e-oLsltyd0tiXOAZ1P9Dppyqm5a5Prse3tpnoiboCYtIRYrxoAArAmcsx2cUdYqNiA8QihxcIoklgf4E6hxKgiAt2U392YK4uGpygikJkSdyuk2WaL0TIqNdw76jkOEun15nxofuYUjHdZRNrmeBiAVuXyG7N2h5F7DgAS1ySK7fo_vSpuLyejCvjwP1H9prjAzoRS_zI-5jUp3mzWqXbBTan-c-QhcAhL2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b991cf3af0.mp4?token=adR4V_0liKv2GBat-25wREl1q2_Mur9WJomFsFyU2vA0HczRcoZlLSAwLiEN7pSpdndKAf1C15T37PnbPZtJgk3BYnV7_nEfTbRwaT9IIIP0g1no5e-oLsltyd0tiXOAZ1P9Dppyqm5a5Prse3tpnoiboCYtIRYrxoAArAmcsx2cUdYqNiA8QihxcIoklgf4E6hxKgiAt2U392YK4uGpygikJkSdyuk2WaL0TIqNdw76jkOEun15nxofuYUjHdZRNrmeBiAVuXyG7N2h5F7DgAS1ySK7fo_vSpuLyejCvjwP1H9prjAzoRS_zI-5jUp3mzWqXbBTan-c-QhcAhL2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎀
از یک پارچه ساده تا یک کسب‌وکار خانگی
🔹
این بار در
#چرخ_زندگی
رفتیم سراغ یک ایده خلاقانه و کم‌هزینه؛ دوخت کش موهای دست‌دوز.
🔹
با چند وسیله ساده مثل پارچه، کش، نخ و کمی خلاقیت می‌شود محصولی زیبا ساخت و قدم اول یک کسب‌وکار خانگی را برداشت.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/682648" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682647">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
وحشت اسرائیل از حمله پیش دستانه ایران
👇
khabarfoori.com/fa/tiny/news-3238761
🔹
جابه‌جایی ۹ مدیر عالی رتبه در قوه قضائیه
👇
khabarfoori.com/fa/tiny/news-3238863
🔹
حمله پهپادی به کامیون‌های ایرانی در نزدیکی مرز روسیه و بلاروس
👇
khabarfoori.com/fa/tiny/news-3238978
🔹
همسر اکبر عبدی دستور تخریب مزار شوهرش را صادر کرد
👇
khabarfoori.com/fa/tiny/news-3238910
🔹
احتمال حمله آمریکا به ایران در شرایط کنونی چقدر است؟
👇
khabarfoori.com/fa/tiny/news-3238769
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/682647" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682646">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goBGpJMI3m4yKkJwX1zQR1x3E9Z58WOhBxtO9QRmRRAND6SrN3kZ2TdwHvUCMRGibZChFZibOW23V8QcBJuwp1P44on9x3kngo45CuXwM9W-_TuZb6ULNnOZlvKNzMGQRNE8uUr5Q2c-0icMf01yj6ugkeBtoZwwgvzkpIcCeouh-wGAYvjQBWRGgyh5i9zcxxu5a_pcQIZ882gJEPk5R1_aDUGF0iWl_hqmEy5hO2ESAOtM4ZSGJcO2ImA03C8VxiGEGsQP5zNVwDkeRtLVpmmwGqkaWLWd7dCIp286KHTodgHQDT2WeHJCB_MhhcvLxJW2Qh_gdJbZvkTmWw363w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دنیا جای ماندن نیست؛ دل‌بستنِ بیش از حد به آن، آرامش را از انسان می‌گیرد
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که دنیا برای هیچ‌کس خانه‌ای همیشگی نیست. آنچه می‌ماند، اعمال و انتخاب‌های ماست؛ پس بهتر است دل را به چیزی نبندیم که دیر یا زود باید از آن…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/682646" target="_blank">📅 22:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682645">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4cf96a80.mp4?token=PyBZCNCKakKMMDbIgJWLGHoJk6OfUxfA31ksnAXRc3o5pFYvQcnsiU9dNs2kFB1S5n2X4SkCg6z6gtHtKGlg15ZaOBKV-pSkB-SKX95yujBcTySQz1JzrzCn-yzPCOifOALISRIjL6pHJsqKWPheO3Cp0Q7UFtFJOBLwx28gT3EYcw01R9T4cMcrP-LOUkIoF79xYnsPopw6Ho2DFgSQ01sF5XJybFxIz5ietlUMgINQN1QOuc-zQyu2ENjkJrpN7Sm2OD8AkHvdfkAVqiqktLQ68jX9iyi6pfa2lnJzgFZk5pDUJRPWxl4pTlgxosVt0sbCMfOPLvvCjKAGDmeJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4cf96a80.mp4?token=PyBZCNCKakKMMDbIgJWLGHoJk6OfUxfA31ksnAXRc3o5pFYvQcnsiU9dNs2kFB1S5n2X4SkCg6z6gtHtKGlg15ZaOBKV-pSkB-SKX95yujBcTySQz1JzrzCn-yzPCOifOALISRIjL6pHJsqKWPheO3Cp0Q7UFtFJOBLwx28gT3EYcw01R9T4cMcrP-LOUkIoF79xYnsPopw6Ho2DFgSQ01sF5XJybFxIz5ietlUMgINQN1QOuc-zQyu2ENjkJrpN7Sm2OD8AkHvdfkAVqiqktLQ68jX9iyi6pfa2lnJzgFZk5pDUJRPWxl4pTlgxosVt0sbCMfOPLvvCjKAGDmeJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک سرک کشیدن، به شلیک مرگبار ختم شد
🔹
یک لحظه کنجکاوی، صحنه‌ای غیرمنتظره و پرتنش را رقم می‌زند؛ اتفاقی که ترامپ حتی کنترلش را از دست می‌دهد....
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/682645" target="_blank">📅 22:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682643">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSXlG6GW5xu_aAYQhYlM_HraVSotG6W4W1dsIw_QFF_M64w9-ry_NBtv8ja2FPtUwZpg2XINkkuOmC9V14EEwo45fOT8JsRAM-9jnxpMS8S2eOmPdZGtjpTL_pndlcZ65f1h-Yh4T68YDM7Jd5HpAaOMKyUupBw2NN7Fg-3KT07AEOc9btyRKoA8-nI7CEZzFhMooi7SAewV4PhQGnCzk---MrSHefCXnpov_N1FVzSG9FT_E0k1kgNrz7jSdscFxlW4OkLyfg8KDIgNPhdKPGSVkaDBWHZT5e1EVAeDnx8tyHECx_wnV1o64Mn-C08rCC19-KEXdP5kOICKWm-QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a1b218a4.mp4?token=cuxCWocOMP3Nnb3XNzqQKhhoshk8ydaFHEMCAf4U0Z1uqbAdnikRXVCB7Pzyv2JoxpAnANjSimC4WoVBn4s7YCYYOG-BavjcaXptCnalokY71D3R0EndoHKmn1UujUZ7iJt4am_gqh5qAUC1J0Q0mlPIBF9mxubLfVDo0wdMx7fLrNM0yidA6QPxA0wN0NkSScnBg-PP5by6ARZHE3HtrEfLpMTOHWW36Ad5vSxFEL619jQBIUXlIzO2KJo8Crs93QM6tGzK7d_7XsbsNVjpINr6rKn7ax96AtEPyVyJzAedDmMlUCLxR72SFi-KoaYd-wBMGtSXa-LUAXRUuBpzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a1b218a4.mp4?token=cuxCWocOMP3Nnb3XNzqQKhhoshk8ydaFHEMCAf4U0Z1uqbAdnikRXVCB7Pzyv2JoxpAnANjSimC4WoVBn4s7YCYYOG-BavjcaXptCnalokY71D3R0EndoHKmn1UujUZ7iJt4am_gqh5qAUC1J0Q0mlPIBF9mxubLfVDo0wdMx7fLrNM0yidA6QPxA0wN0NkSScnBg-PP5by6ARZHE3HtrEfLpMTOHWW36Ad5vSxFEL619jQBIUXlIzO2KJo8Crs93QM6tGzK7d_7XsbsNVjpINr6rKn7ax96AtEPyVyJzAedDmMlUCLxR72SFi-KoaYd-wBMGtSXa-LUAXRUuBpzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصاره همه سخنرانی‌های ترامپ در مورد ایران
🔹
سفارت ایران در غنا با انتشار ویدیویی طنزآمیز، تناقض‌گویی‌های پی‌درپی ترامپ درباره ایران را به تصویر کشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/682643" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682642">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAutonovin.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6jrLDkuej53adJrwhzPamEed_32A3aVDXC7u-GZa76Q_7xzB37-6ERl0fIMiJgdYA_POTKjIgcdVWbJZF-VQggjYF6LJbrJ92v-5TBEnaSuIUIFu2q7NiYo1lLMHZ-4QlXKpgu0uKK6gaKmXtpN_ZYub9tw5p1QAy6U9vN6NQ9AlPD05ScMuVs85IhDXSKxslENUYKXOZJW_k2ikiYWIZVPLkcLFVIX9Hyub0iM3mMA0P9-E273TbBjB5ewnHA4HQJ0TsUKsy0j6UyS6fsDKpR-1DMD9uKmI1KmKAWduqHRsq_YElQkBcVNoaZCmpKrTqo9ZH8uqMbKMV8UFGGfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آخرین فرصت خرید خودروهای وارداتی اعلام شد
🔹
متقاضیان تا پایان روز دوشنبه ۲ شهریور ۱۴۰۵ فرصت دارند حساب خود را نزد بانک‌های اعلام‌شده در پلتفرم اتونوین وکالتی کرده و ۵۰۰ میلیون تومان مسدود کنند.
🔹
همچنین تا پایان روز سه‌شنبه ۳ شهریور ۱۴۰۵ امکان ثبت‌نام و انتخاب خودروی موردنظر در این طرح فراهم است.
🚘
برندهای عرضه‌شده در این طرح:
Toyota | Nissan | Mazda | Volkswagen | Volvo | BYD
🌐
ثبت‌نام و انتخاب خودرو:
Autonovin.ir</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/682642" target="_blank">📅 21:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682641">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-lTFi7EfbVsX3BpP1hTQ_oiVO54WheRUO7SrkSQc1X_JRZgu42apsQ-RhDTbzbUa3oVVzprmKrnAsbRK6ZwAsBRyVwZkbPfzVbEu0leAGyBsmAPVdSPvkFi97uLJ-8S6PcO1qcSQZGD9D42Ou5JF4HzJMeGw4ZGgCIZUgnuiJylK-IDGiOk0jp5Cl0NkM7axe9g3PTLz8EQowGmsnXXtT3TNW3kDaruKGjaY_Cs7e_pqPopRkaIfk2cYfmt8Ys-TmTZjRXeZ-EMFNnc2123EEhIxdkcqIPp7RpwqRsjsnEywVgI0_2MzqjKlCFFzlICh0J51BRX_J-yLJk2YMkiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل فولاد خوزستان: بازگشت به تولید در کمتر از ۲۵ روز
🔹
امین ابراهیمی، مدیرعامل فولاد خوزستان، با اشاره به حضور کارکنان و بازنشستگان از نخستین ساعات حادثه گفت: «اقدامات فوری کارکنان در ساعات نخست، از جمله ایمن‌سازی تأسیسات و قطع جریان گاز، از بروز خسارت‌های بیشتر جلوگیری کرد.» این حضور خودجوش نشان داد سرمایه انسانی این مجموعه، مهم‌ترین دارایی آن در لحظات بحرانی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/682641" target="_blank">📅 21:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682640">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ0xwKXIp-eLJMAPOrqk9HzuE0Q3FvkfcBI6gMGuY4JujCJT1Jb4d9h5ChkNb4LzYFm5JIquIIx8exPxmUQ06Qv3WgsQCxSj03JfNcgfzALbZPooZpX1oeKb2zQw3kf8pm_TVqEi_PrdUGL8A9e-eC89oh-ZDKcGK8e9YfH5C3DmmYVZqAHPBfuDKcDWc-gck7QzwRe0GosFjfSP122GwrDDMhu_64DM9rjXTDjY5M34gvbr065d5lw4CzBXks40vYc1HKY5GghDDt8E8tmn3zJwTHicRC_RakAanPv8vaz4mOzpUDS7EkJWRxEJ55wjHswmbLKkIoTQaEc8-SAmTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز کنکور نزدیکه، این چند نکته ساده رو از شب قبل جدی بگیرید تا با آرامش و انرژی بیشتری سر جلسه حاضر بشید
🔹
کنکوری‌های عزیز؛ انشاءالله برین و با کلی خبرهای خوب برگردین؛ خدا شاهد تمام تلاش و زحماتتون هست و رهاتون نمی‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/682640" target="_blank">📅 21:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682631">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e3a6112e.mp4?token=SkTU7H-NIID6aWzUSVg24xFO9-nEOUQIBEoOu0AijPB2lEqZN-5mPh-X-ytDuXWyOtKwsljVLKC51sdXMewZn8QTlpHxwdSDKZKvoUs-fiFqoz5Z4I-GLfTwPq3fAwB1Foa9gip4JRL90ch1jr0YX-JI3O7CUNsWAKj8Yi-0Z3p7ozhtZpML6Ruj7RIy9smjsubRB2SzbA2Ors6r3W8kkXEZsLzitiu9kVLDHm2GKsrztUpkF8JTc1JuAT95b8vOCjJvPk0gFmVrL9WQRP7Tim2YMF3g9sB6IzNmOGqvsaSGfi95SB0fQGVMHat_wVC9V78V40JDJaNxjG2F-aI37YsJwHQjC6sK4o8ewnX7_zkxpO_IdAd9wDkWpmNsrAsW3GEpbt8l-Q3PGOPwHs7zeChbtASmO4eQbd9U81J290tuuiaYPhwPHGASyOjO5u9AM15lKyYJH7RPXPktNeleKIbinl0gbsWvsmer_935CywBWoDHy_ZNeMEi2nx0R2Z2cfaK518FVLhiP2JlWbQXc7NRefzbEWOvmtugpt57csnLAZu94KYhXhWYnGPXe6HTgyZT3MUhqdw4HPkJSq-6269jSTUUP77AybhSp7SLTswqOVIA1RgPFBZB4qXpyEq9sf7rLh1p6klAMi2uMugZKCzTvbI5pg1KJXbouNBX244" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e3a6112e.mp4?token=SkTU7H-NIID6aWzUSVg24xFO9-nEOUQIBEoOu0AijPB2lEqZN-5mPh-X-ytDuXWyOtKwsljVLKC51sdXMewZn8QTlpHxwdSDKZKvoUs-fiFqoz5Z4I-GLfTwPq3fAwB1Foa9gip4JRL90ch1jr0YX-JI3O7CUNsWAKj8Yi-0Z3p7ozhtZpML6Ruj7RIy9smjsubRB2SzbA2Ors6r3W8kkXEZsLzitiu9kVLDHm2GKsrztUpkF8JTc1JuAT95b8vOCjJvPk0gFmVrL9WQRP7Tim2YMF3g9sB6IzNmOGqvsaSGfi95SB0fQGVMHat_wVC9V78V40JDJaNxjG2F-aI37YsJwHQjC6sK4o8ewnX7_zkxpO_IdAd9wDkWpmNsrAsW3GEpbt8l-Q3PGOPwHs7zeChbtASmO4eQbd9U81J290tuuiaYPhwPHGASyOjO5u9AM15lKyYJH7RPXPktNeleKIbinl0gbsWvsmer_935CywBWoDHy_ZNeMEi2nx0R2Z2cfaK518FVLhiP2JlWbQXc7NRefzbEWOvmtugpt57csnLAZu94KYhXhWYnGPXe6HTgyZT3MUhqdw4HPkJSq-6269jSTUUP77AybhSp7SLTswqOVIA1RgPFBZB4qXpyEq9sf7rLh1p6klAMi2uMugZKCzTvbI5pg1KJXbouNBX244" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه پدرانه رهبر شهید به جوانان و نوجوانان کشور: از کنکور نترسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/682631" target="_blank">📅 21:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxZMQbAdrjedR0wHsFrm-Y8AHgMFj9Kr1WKZfM-On0L3D9KxfzEAuqWQwnaal_CqL0Stj-rnbXmsEoWzMrHGoPQnFxn2gJPkEUB4Crtt8OXXfkFYJFKenuKsvSh-XfHidd5JhPyzzojAkhDbZfv-IK3ulglF2maK8RXmGv0SkL0bwcOvrQktxCtEKf-ZrHLlQhCoxcnKgHI5ElLRJsAC9MwQK0Jehi3Qd3dOfUXjveqU0JCLEh0zLvFsAFGjPH9naw1mNCT7lYb7s69pAYbDvhk2t9QlB-6eevS1tOgMV-q1ajdP8qBwz00hKPHYxqJHMjVy_jIuuvRiUMU-uJQRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس معناداری که قاليباف منتشر کرد
🔹
رئیس مجلس با انتشار تصویری در اکانت خود به زیاده‌خواهی آمریکایی‌ها در خلیج فارس واکنش نشان داد.
🔹
این تصویر که قابی از نقشه خلیج‌فارس و تنگه هرمز را نشان می‌دهد، به‌نوعی بیانگر تسلط ایرانی‌ها بر تنگۀ هرمز و خلیج‌فارس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/682629" target="_blank">📅 21:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRDcBGnqkSgBv5tFHdraDDIfwgcjLokrvZd2QcN_GMP4ued3L1v5HOireifcBViC5mtzubZIDlz61GRLaj42-PLJdhXKo5RK0kfRc3tIivHu4ZwZ8TcltcTIotjAGC18Ue8J1JfWGEmZQ1MI3NwzTjI_4CTFofv02c4o8pIP9IECI_5TmmuTIkD5mRjSYbvg-uDxcASxDPnwwqHjwkqkgXtXbQVaXHmUsAI30iLtFJMjcFsqryv75U8EHlIwlBws8pUkivvwcQI8AUCYv-ttgJ1ut2saf7XP_nDxTXvtbcmfNLOCYAul07-wFARv-2KM4qDy0g_ptTWC11LpoezIGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۳ سال پس از یک خیانت به مردم / پشت پرده حادثه ای که باعث جنگ ایران و آمریکا تا امروز شد
🔹
چرا ۲۸ مرداد رخ داد؟ آیا این حادثه ضروری بود یا امکانی؟ آیا اگر مصدق و شاه اقدامات مرتکب شده را مرتکب نمی شدند، این کودتا رخ می داد؟
داستان روزی را بخوانید که آمریکا را از چشم ایرانی‌ها انداخت
👇
khabarfoori.com/fa/tiny/news-3238697</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/682627" target="_blank">📅 21:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اقدام غیراخلاقی برخی شرکت‌های پیمانکاری: مزایای کارگران را به عنوان سود خودشان دریافت می‌کنند
هاشم خنفری پورجعفری، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بین یک میلیون و ۳۰۰ هزار تا یک میلیون و ۵۰۰ هزار نیروی شرکتی پیمانکاری در کشور داریم که بخشی از آنها از طریق شرکت‌های پیمانکاری با دستگاه‌های دولتی همکاری می‌کنند و ساماندهی وضعیت آنها در حال پیگیری است.
🔹
شرکت‌های پیمانکاری حداقل حدود ۱۰ درصد از مزایای نیروهای شرکتی را به عنوان سود خود دریافت می‌کنند و این مبلغ می‌تواند به جای واسطه‌ها به رفاهیات و مزایای کارگران اختصاص پیدا کند.
🔹
در برخی قراردادها پیمانکار برای اینکه در مناقصه برنده شود قیمت پایین‌تری پیشنهاد می‌دهد و بعد مجبور می‌شود از مزایا، اضافه‌کاری و رفاهیات کارگران کم کند تا قرارداد برایش صرفه اقتصادی داشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/682625" target="_blank">📅 21:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d27502e1.mp4?token=IYnRWi1ZZxNRo8aNtirULQzCKyXmGIfco9BArnmEpkiHoKNcB8r0QoMOP3gfS9QyOu3I6lzxVuH8Om_g2aTbFqfbOrTA_WqiH7F2ys3_kCwMCMaET22fo8SbMkNDl3wH3ExCBtUrJ1GI17A-J5ByHxffHAZ53eD08VdHDvRwevDZGXdE5Zrx2GEAAo9Ez1Xf7LngMXgCP4JHxTOV9oHpgmAs9LfCE8RJPc9ivr87T1cP_noRIbPbFqzUtxy62hoEjmT8EverUpo-iFTj48LHSLpLugvK3Ziy-TgHd5tURXnylhmBteK6m_SwzApUOnB-IUYz1fYlY5dGwp-idr9Nng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d27502e1.mp4?token=IYnRWi1ZZxNRo8aNtirULQzCKyXmGIfco9BArnmEpkiHoKNcB8r0QoMOP3gfS9QyOu3I6lzxVuH8Om_g2aTbFqfbOrTA_WqiH7F2ys3_kCwMCMaET22fo8SbMkNDl3wH3ExCBtUrJ1GI17A-J5ByHxffHAZ53eD08VdHDvRwevDZGXdE5Zrx2GEAAo9Ez1Xf7LngMXgCP4JHxTOV9oHpgmAs9LfCE8RJPc9ivr87T1cP_noRIbPbFqzUtxy62hoEjmT8EverUpo-iFTj48LHSLpLugvK3Ziy-TgHd5tURXnylhmBteK6m_SwzApUOnB-IUYz1fYlY5dGwp-idr9Nng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مارشال‌های آمریکا از بالکن به پایین حین تمرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/682624" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baXxBzg8LtfYFVJ0m9CdaKa60LfgCQZeIXLl6F4CjdSe-LPUOObS6vGXqa50MMEyA9g6M33kd703NLwYDsPh3SUkwmSU8CTbrvy1x2KGYxzKUGpXF67TE7tyhvtvz9QhkHN5uRdEjmYsiLnejkgBHGfOB1Y4kV_FKwdlmT4HOR-QL0LrDgL4-CEIPH55fuxSOgJyLBqCOeF5cxPVdBGxofLkto4iRkGaLJ6DOuHXYeD1sTxYymRHYoUmL3uuMYF22WgRy5gOBoW8LyzM-fFOjhqRNUTgPZ7aKaf-qaMnkRxajlFTWlFkd0QK4wAlaCWbyfq256O5Mh_lCwj8Hhud3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ‌عجیب ارزش بیت‌کوین
🔹
فقط در ۵۰ دقیقه  ۴,۴۰۰ دلار جهش کرد و برای اولین بار در بیش از ۲ ماه گذشته به سقف ۶۹,۷۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/682622" target="_blank">📅 20:52 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
