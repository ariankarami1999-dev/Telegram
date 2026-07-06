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
<img src="https://cdn4.telesco.pe/file/sjqaU07aHJT9aIsxjjxmbgbBhJdB-Z006c3Zp3ZZgNKvtpaZhAokryx4QHvxAa6PRAPcD8PmnMjyf1ilKG1CyIt5n4Ky8eD3QmoIcswgBypGEgLczJv3vCdYJmv6vhCaBQIfprnkBq0rAoCxtvLyZvDQt2yek-xybhzhNWxbPHchMk3_Vj485bh5RD9g0U4f5VLpTrDwQeLW0fixQYCDUhDiWJ-gxUeVOpaPp56QgvCIYxcZtWUQ9QrHZV7fm8niKkqsHUWUfhFhr1da2dPzsAxGaC7eVh1mtc4X1zWihxlO8w7J7L-uESNrSgMnqOXeVfWtVRJ53mGtbmUTCXlvIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 01:22:22</div>
<hr>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up-Fq7812k6gyJifo6kWmAQdMraZaNEAdAc0DXDhL3m2t8nUnu4VJ538H61hsCWzeI7uOKaD90UK01ivUI98RK-pnX-E6jcHSou9YXmh8VsdR1kGApPVROqL3JXz4QMIcB1fjKzb2nAHGPbzvAQMYhVHz91xJarxRNcgYhmSRxXk9ZewrGJarN7AbNUWmC146WGZ73u-rolQkawunBm_mbk_pN6zovK3B6NUO-gFpYQ2oO4_sXM_DjEdngDtJxo2bQzCzfEGezDbDrJfpR-HCUIs1jhtEy2h4Ke0TBlqiZ_kXgpbPPjsMQpnpYxL8fhcgt7Zmku1hymrvDQiO0e_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiOBNdlHcj2u7by0c4i4-lxjxQ63elvO7pHn28CxBpMxmkSdBgm70TGz9Fl9yWgWHr7xr6wzhBTtuezc94YEZ5WkDFHJXW4bnr5xogobq8Em1sYHqL9JVFeLLtTljoxu1iarqdS712jB9FVNWXsX4UM4jIqWM_FQ8GIBMl6L4jg9kZHPeCsXNGDkEWctlfAbZasGa9atOUPtsyddS5a570zWXU-b6AuaenMOsiNIPOtoOHQR82x8sDJeltZZeelVtqm4-z4HKEaZ_pKA7Zxnw4oLgJcjhEel9qfwOlExMSb4jcC00gi96D0yE932DCfKuer5lw7iXjdthyGwz1uZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx5Qb9zl5O4UgLEiUTLGlPe7aIhNfDDKTPlOFD1C7yut57YZChNF6MX6DlMQaKQIh88d57ArC1kjCRaxnaYVl3qB0CKXdr66WmYfuLqu0GNv8CcPX5kBshsX_kllVDtKm9oiszDQGXDjKJrHlvMfZ3r7uljsuLG8GWJ5xt9WrhAw46uqh5FBjFAqQ6JkcHCW3mFl3Y_Lznwj8hjhtiRC0BcoOBimLwGn5aaHZT4faHdp-NoI9KXU4FzVnTn7gCnUJhY2_7WNMqSoNnIhvkezld8ndB14UqzYg9dDV5EeAAT46w3huUqcggMDn_sPotLOyNEXogqj3cEalqFho0REcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwuoRGQ8XfDkuN1d18gpw_DS8HnHachji7PD10S8iPVpPPS1Wvp3ZI1AlU_7b0b8Qd0U2Cg8LwLJc_mtDt6MiiNpbiIJzmacEVtXj-q9OD1eWYVkRHlBul1BkYrzHPXqrilzrs7SMXn_nSg08WOmDx45_QkPw2xN25_AFtQGYHcbDVfbfTPa9lC8eVngXs3SQyH9D3vgGvQLTJWF55jAkO7PkinjRdwkZUh2pu-VykblquACTyhTP5khd2r-Xa85tvgOoft_alzEoIecwRKyHW-x5m5-DdTmWFAvYci28OYr1EFTOIloshI7PZWlqyhRYG5r43AelrEJmnTzfiLO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh48so0K2zxAF92UvjML3Lm_sbCCZX08Jh7k2inLmnga1p2Fz3Zln1sptFsnKPE5ofTDpSiI89mEAsKOJrnkcHnMjtwqeNXW2-UdLSjv_d5qLGw2pspAkb1ZLFZhRp3U-ouePyRsfmlKV219X-fyWc7dXZk9Q8pxXMbeHEA2XWxT4KygYNRIKBsBMHVSG-Zz3g5dosWmjHYwFM3-RwCQymUGHNIvo3-30u4r6jwKMJ1Uy1FTQIjG8RlopZ7XIPeNCsrU3Z-jsGUfPrQFO6wvK6QnbS1aPrvlDcp5TMg7MpHQW_qehFXUniP1FN5W_fcmkY_0Mik7ifya0mGoSD-LWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=ET8mNNLNjC9IENJS4XskEtpl3g4MFtivP3HPUza3qKW4BGpRMiIrFhMee3OU43_Jzrmym29Av0cpW80Zl6JL5ZfCPFQLUjIkA_hgSM5cQ_aoQWovBpoAJUQ7VDKuewHo7V8TWsTTfcW61AvO7-bDjMGNxbjDuoH7wsTr5NaM4C9uGcNOyaIaKO2SMfjn4Z9yIotuSs-99aO1aH-xiuTu0y6WdjUyh0JgQnRTD_rKG_L3QmUZmrCVIJOYWnkVkuRP1oBecZc1J3laks4DgxhFfa-4vi4ahu_WUzy9kWPIAji0UTlbnOBEyZ5H6lFRl0dt4x94HwuGZcLm9lEHgavOTnd4W-n4QfZSbYZMswOL2815O-C4N3dRBRa3gT-ZhfP6f_7rTGqDoo90IFYJxj_SDdMNefdvr0kUGXDfIjPN1uOmo7nJnsjLSXWe9wfq7FFpBySOYa-hlPMZXETBZs9Vi01Kf0R3s1KX4yq82f3XDjraLMgltVtz7R3kiNqssV82wdHd6vGZkOtLBa2qjlAK6ghtOp2QGiszzmmjEr3FiVUOUpeJF0MroI5n2Z7K_gMcin3bxcQI5yxMfONCtl5-c1V9Oa-dZl4WRovl2TQcIGzK3uiTBH0VL3SUgtr0cciQ7bQLMoVu12MMh7jXeUoFd-XFBrlC0KPD4oHle5a_al0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2U-riMSKWoIlRspRuPqV8_nuLGmqgOE3VoK_PUdX5IDaT2o7XPbMHtWfHTz5PMILZz10Swzdmf57_kU8OSLoeZwgqmZEmygzw4_BqPU-aSKgSxX4pHqs36MHcgifAjRYPMzLkD6eqMu95_N04Es-fUspf0-lfPTk0ADvL3RDL-oHQc1Iqpcj-8ewgGB245_ABNtdh9DEVS6mgzOCh9TWsYmTEpJ7I_9NqfuVGyyl7fXyI6bhSx8AKK-R_JkGqtAl3-rDYyrfp4B5HxLWID9L7JtZ94WTzFojENpAiNINs2qrmcXihP9G7arICo_fLb7nGDySFPvxQ83D9hGMj1KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpgapNDk4n1WjNxr1ivqpRwQBetlG9VzsWg6bkcrM9cgsX4nFZClwYx_FrW3tEKQvDPTPj3Cte2nHh4UJAfIQ5g_WOhQtL8iFkDvEPDQ9UkPw9bC79RXuR38CWZARTulLUsgWSffu6M-pUR0gJfn4Iw1odAqHbC5ajANhx4b5c4_4vf6H673ZukEq451iNhaB4gsSnE9RG-R0NH4KZp1h1t538dM0FyPIQZUxGQ5bie9jSi6l7OSA2xI6defsTV9Ls-SWGOrsTe7ICaWpKC56DEezK-5Zn_RdDiDv42Prh3h12UmJShGlULLHGA0qckCYMqVwsihySly8iFZp-wuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyS4o7qKc4ylwLjniCk2y1CqoQQqNkap_SI-pdwCdqNyeAysYXRtT_dkEJyEq39KKbk0lO0WpKQMdmzTIKrlOhPYSRsoRtAMB_J2R5EFN8Ee1ivimSgXlFaKfPJ6Hmks4devIjN8jcEUTA-P-1MNxZUY9E32zclV6BdagikTliS20b0_ujpm6oYa7R6HYYTkm0IWB0bTC1nsWrXOYVl8azIuMh8lD8zrR77bJbOZT5w9fBTQAQLxxPnRdzT01rkDlcChVJn1wZeI4JvBKQIMAbkWi1S-7xiCbGN0cnWjxgUc7eLAY3jy3y_Mlc6NT9cT6ng1mb4sBywRZAkPOrP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=fCM8z1mxUVhkhL6YQf2K7J9OfrHA7cQk3l2TYEGhd-6wbF4bT-711AqSnItR5-OZrVl1GEVYChzSVdq1Y2KgClwzftRTp51eWSHgKvyLJpdOKAJo8EAJg3VgqoJJ_P0DMXarASSV25Yxbvy4O5Q-WWdE5Z1Xt-5EycyjCDYm9FjPhJeKDDtrjZ1JCy7CYV_8-tksMHXaqn-px10jzDAc8lhkhQXQJTTstyA4cic4jcYmaulbim0Ev2a1ytO95h4h9EMzRBSjtfmkSrxhBXpP_5htkV7XAZVcv-ejDB1cE_R1geDYOVhA6Lrqot4GJUwHXIoaKTVGqoHbnpv6NOHFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=mlPjf8VlEV7wxPpuxA5aZw9RA7CJHjrXBmr_CdcQQoDWInqjYEQq_mPL9t_1VEevjLRceIHvR9mCabbYCLGrkU8qpToEskv7jpESnV7Owrly-ZwTR0gLzFtYziRM_Vbnj0V9S-OyYrxpUEgz5b_Ejy_lb-GjipvfZ01K1BjyplNKXePV1CB8crNIKAa3Rygox9ehuG9qja0GnLtK1bFac4EsajzP5Ve-QElZv7RV0uNBwwBrhbAsamQsp5aa5gH_U32jSJ6yg92EiqzlnfRriv2LGtcCvFFA7Htycmw-5caXmbGBel7cWzzCdvw0r0O6L55dSAEA86YKlLAL52NnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMFpoZQE1CvEid2riFMllOiCyRovhKkdHOhdhVafbf-UR7tLZybiPeC1K1q0mnC_LH6PL7J1hJhxsgucbAvBJiW-IBCo28jfa-o1fylEG2eXg-no4_HIknHtildjlpeWd9Zm5D_l2t1Y1nU587BLiGjBrxfIKp_E_LoIt0fH0sgww6qbYtarUTfGiQBRhnrGP3nPceJ_9pV0tj_Izb6Lu4I4_4xIyhR363PH-xafUCCZg13j_klccdEwryrxkQcvN1-xNj9_Z374nyaS5JK83CzNp9XPYx9VBz6Xzl7JCnpf4yjm3Tqa4gXQh-ieWrwASzRi-R7Lyk7zOKDZ10qKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=c9GMR45GIWEa2zHEQ1Zg3qIxkYfQA9M_GaUVrEn8prtLtEX0upDU7xrOs_yfuuyuzphFxUSf82Ei-DMTPYJ4Vt0jIjqqEyhsfG4McDyzwFobNVOfEqEdMawY-sApiIl-ZuyvAEFpy6vTyxzLYzRw5RPNn8_c0QEP84p7FvKZW6l6j8Mf7lDbxJFddDnDGamjKadrlWDVBJIM4_2GI5Iz63Cp-FPrxr6KDqmq9rk7fmGzXRbooq4L7pAmNM-09R_Kxz7Tu4Gxtyw_ZS-VGp0UQcsDb5SenfK7jSPecX07sHAcokDM6lTl4fYbY1Bz0EZVbjz0_na9Ig2nwo5SY2F-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=c9GMR45GIWEa2zHEQ1Zg3qIxkYfQA9M_GaUVrEn8prtLtEX0upDU7xrOs_yfuuyuzphFxUSf82Ei-DMTPYJ4Vt0jIjqqEyhsfG4McDyzwFobNVOfEqEdMawY-sApiIl-ZuyvAEFpy6vTyxzLYzRw5RPNn8_c0QEP84p7FvKZW6l6j8Mf7lDbxJFddDnDGamjKadrlWDVBJIM4_2GI5Iz63Cp-FPrxr6KDqmq9rk7fmGzXRbooq4L7pAmNM-09R_Kxz7Tu4Gxtyw_ZS-VGp0UQcsDb5SenfK7jSPecX07sHAcokDM6lTl4fYbY1Bz0EZVbjz0_na9Ig2nwo5SY2F-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=GVMr9EfI_9D7b6sxi3MpPi50Pys0Y9zE6inJRkxermCc1IDFUlW4Q0czIo_tgxskeg42wNdNrgAM4zYVj647Bh4U3sr7xnYm90BP-VeFd3_AyqT8z_0306qqz8xhQqmOxheajseiu4FIZ4DucxU9z-Cun4tW_Sv4Hlq8aa-IgE9HfXKM7Jb-8pPKO1vzeU3lRGawA4051-y4QPdPkV2NM2L7869QAaVqMOPdY2GzApQUlDWS-88A6gbjOTKhpAc0PQQSrVZI0yAS3s8uoQVkYrvrrs9qWQU4O02hVDye7z3M0KfoNjiDKoPaETj02F0EJQ9bzySvpJ8BhJALtxIzDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=GVMr9EfI_9D7b6sxi3MpPi50Pys0Y9zE6inJRkxermCc1IDFUlW4Q0czIo_tgxskeg42wNdNrgAM4zYVj647Bh4U3sr7xnYm90BP-VeFd3_AyqT8z_0306qqz8xhQqmOxheajseiu4FIZ4DucxU9z-Cun4tW_Sv4Hlq8aa-IgE9HfXKM7Jb-8pPKO1vzeU3lRGawA4051-y4QPdPkV2NM2L7869QAaVqMOPdY2GzApQUlDWS-88A6gbjOTKhpAc0PQQSrVZI0yAS3s8uoQVkYrvrrs9qWQU4O02hVDye7z3M0KfoNjiDKoPaETj02F0EJQ9bzySvpJ8BhJALtxIzDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=CYlZ20nlB25n0Axl5VaNkCjUz5Y9QtiFdaJjLfCbEQXKbD6hGhAKxT67wSMZqDNMaRs1WW63i2zr4VWUHAcxUr-JTz8kmGJq-55G3Z7WhXo7Vxaf2ElV9997t-mlh4hKWJ5DZZ95wkM5cvk4azIpOSBlBzv7WnTE8MB1Cipge2Gmm8mFH3GgOBDKQkWIJpzG6s5A4mF0oGOSzSdvL0t6SN-5uqQU8Kx5dA5LgLIwzs4j78jaoiP64ye7YHlRTXV4FTG95kBtlPgRPajYOteLV2Gzt4MiGLP3yEi9l9Q63sVR-15wKbsG_BMl8HE0Oe6WSSP6jkhH1CPVR6ARl1Qtzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=CYlZ20nlB25n0Axl5VaNkCjUz5Y9QtiFdaJjLfCbEQXKbD6hGhAKxT67wSMZqDNMaRs1WW63i2zr4VWUHAcxUr-JTz8kmGJq-55G3Z7WhXo7Vxaf2ElV9997t-mlh4hKWJ5DZZ95wkM5cvk4azIpOSBlBzv7WnTE8MB1Cipge2Gmm8mFH3GgOBDKQkWIJpzG6s5A4mF0oGOSzSdvL0t6SN-5uqQU8Kx5dA5LgLIwzs4j78jaoiP64ye7YHlRTXV4FTG95kBtlPgRPajYOteLV2Gzt4MiGLP3yEi9l9Q63sVR-15wKbsG_BMl8HE0Oe6WSSP6jkhH1CPVR6ARl1Qtzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=g6AXA7xIx6xjNWcAcIR_TdWHh3Kua2fT0_Yyc9vCLfFMCe3mqRgHU9P2U50_tYGgm8NJJwzzs9dH95JVnSJ8eACZl4hwC9Qdd4TfBORKFfqjbrwL0f0iY1P99GEMFhnzskmlzOYxa0cL8x6ILqLNJf4q49ar5K7cHrC-pzNmtmLQNry6xP84lo3zbJlY_ec417fTRshC9d2WYwHSqDJ_O7cZK1XA7bDzGr97-g9znlZ-civmOdEfPlbbOOHOT6NNsn6XBpOCWhDwHRcB6DOgTE67w_pgrkxfHO08x2m4TTSN9mvkE1291_SdreqLmShHZVC0YoBfl_Ka3HRB7dmgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=g6AXA7xIx6xjNWcAcIR_TdWHh3Kua2fT0_Yyc9vCLfFMCe3mqRgHU9P2U50_tYGgm8NJJwzzs9dH95JVnSJ8eACZl4hwC9Qdd4TfBORKFfqjbrwL0f0iY1P99GEMFhnzskmlzOYxa0cL8x6ILqLNJf4q49ar5K7cHrC-pzNmtmLQNry6xP84lo3zbJlY_ec417fTRshC9d2WYwHSqDJ_O7cZK1XA7bDzGr97-g9znlZ-civmOdEfPlbbOOHOT6NNsn6XBpOCWhDwHRcB6DOgTE67w_pgrkxfHO08x2m4TTSN9mvkE1291_SdreqLmShHZVC0YoBfl_Ka3HRB7dmgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWF0AS8BstjTTF67PHhrBxBVtk_EAvwCaAxAtou03RIjrjBhaSFXrCj_HuMTj7tqwYEqRioWQ06pNXNA0ZUDxEJFZGb57py8xsagn3SRWbYvqyNxqzbGBYW66naUGGcrMLRNCPn7kjGkll1u9jNKrk8TJpNtAnWaDiu-e_JV6OdzVM_jRGanRXzBEXBth2lZ9lQkRtAHHHg3T75dxMd01myYDJE7rQ615yuJrK7vDiOReQm5yVbZANHThWLQuRoUaeb8ZacGFW75JdGO4w7UUv2ntdb4PEof45h3-YIDbN0SqMyF_UDmY4HTWBjwyBgU9qNMcDH4VJX0bllC7l51KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1qjeBc-aZ5z_N_1JBGtMqWe3AyH7pljGMDZKjNY4ylWgXnC4lLHRE59C81Hp254bwLI5ff9vcgg4duOVfYa1ecIPS-400A1ZNYC63yp6h6MLTtYoUKYYtYFKcCdAlrmghdGPDo1XGLvzGlhHyGhUjL0VASGgOOasEQjwGpy-qq2bLFdlWeQaNTQwBJm09b_Y69lmlzApS34KwKrJYn4brnCPwi_qOpnbbtGoBd0b7ej-tpM_zl7cK2gsg2Hr3ydOrN62qgFINvDGKZaB1tOuS8mlRPP8jkmv6DWdKF9xiydQ7cB_zhsrAogF12vct3e_umyJ3Ml03PmCoKBTDjnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNkhCA6SzWcD24_2CjxSt6AepNRq3pPf80cQXwMQvWiLphsUEOYnkxe3ycphWKqgA7IS6Nkb4TIVwjzZ-JuwwyWBAzZdYGG9DfBM6YAP7Dk7IaezRhHGNbDh5b8IymW_vBEkSyFXs-9A4ruWfWCDIuGcavT0ycu_w0_LXN8SrOsMPXy-Vu9UEwfV4scaEvzZ6Vy0s3Qz-Uc08PFkMWBIlfOG1EwiPemuP_f0LTnyh38eE2eJKuiWbNcJxjfsah0YTXvmEWEm6g4b3Qopk17vshJvj6qNuvHr-HC3yuT50fWyf5vIxBYpMlNsr2JFIRIWbLIsVQ4BmTWnvhXH5U-UYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc3Da3LnFizlXKFiv-onf98jRkytMGHUmVHIaRb-y3fLUZUchb_hIxS2nzEkDyNrGTRqrpWNh1VGYMb5DQDy0F6UbNVQTXSaKjF8OqH4svU5M5NR4YSRNq0PIQWng1YkFG5TxiGuR7M7GZKVSQPr1kIwGFM-y8Q1MnlHGk48R_Ril99bnVDoQMk1yn5POKx4cqTVaFHfxNVQaB9HIw0m2iz2XYudPaAeh9aCIDQGuv18d78hGMnrvbEcBVUX08cIhWRGR-NGrNUtD1L2rwMfxgVLD2qEbtOZpCX5nX4kawmi0hpOp2nBBbzND53N2qglTEi7vHEzAoX3_lXOvGjcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1XjDZutpHHwu3gk7umoxoY_eI0b1dsoT97tJlMluy1dzVrCZJGOvd9utBqM9Ze0AHBWZVoBPKaSBx1a5g77bKXbdFKo1CU1BGxtB4Qjrlw-R-hImUnLkLtZ2fgC-Kf2HkKbVMZp1FF2qS4wAeE92G48oU27XGGKFWHoMtNtLl_Ppo9EQvvjKimsb9uRKx7k_w3d_KDrunqjczXuUa1bV9C0Rt6AmmbUp81APel7prTzUhuMA3WkadSqaEGMHHQRbZ7ntYDlmnUT50T52RazB6exyUPdI7SNwWc6Ox0XuNjYL2nQgM7v_bo9ELzam5_bX0SGPjRd0SbDiQJjUPUaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-K-ewotwmCaLBiOCGJhAowcghbsURQiaJdzjcMyLzYPgQ8dfge5Z2rB5aBA4RWB39W17rBk4X_vsoRSNNf8xhktctVqv2OGYhQB_7kcxEgD4rTrmOHIdnVApvbrpKcv4mwNLAwtRuaKKSQxPYR_IHu-XJIiBH_sBAdUJX5e0HFAdNBRBh12g6MLbkoCfp1X7GNzhlB0BNpk5aPF1-i3sKoYU7NZR1YRJqKfG0SOqX_vTafLJF0RKtXIKA2eZL4KAOaUrSXV__8Rc1eCbEQLKR8IgKEmh5V0hOjBlnC5nzB2Ro8dm7X3C0ArLh1U-YaxvSg3Bi6K_dsmvZBHyh3S6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnoU3dus74yu87TjIzkVBZZNgF3ynnjzxGne98WqbdRSB5yK2mrXu8p2degYpCiTK8Wf4Nosf0m9glIUX4cw9ZNnKiV3XBhmD-rRq6lxycI6TtfPGnbC4-I_UkUUhsostIIEHrbCkWUL3s2w1awKz5TGJMdq0pjmtlcYdO1UIwTGsN2B44-v-4Jsds_vjJ1rhfrJvU62rLyiJ1uLe-lXA00wRgjQe-iSwme3jXdly1-7kU-bBbXlaeH-0lnoCSGqekflJF_HlugYXcX1wNTOwUVSCcZzrOUvY7rqdbV0QIVCK_xO6ymxAKHJisN5stQzNmHPYgM764zIl47lHCXKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSi0FNVpvTh1o7ZpNf8Bi7CAW7Mz2pAuIsvIjkTVLF7nZa9UnOx0FiDGyObhjuAaAOsC5bySk4XalCt7IImh3JRMDRGOEWYkHaQtYwSSPFWOLNOqzW8KuAVtA2DokBdirpjEfFQDIndrPWMRLrc8K10SkdUNoTQiUHj43IgJsJ6qq0-byHMANchxSTB-D72V4-fIfImyqOfBlOF0kaG_pa-MysYnYQBR5Rvo8wDRE8_jfowbZoACEXV6rtpuNo5vzkwHA71dvqf2MUeaeJga6MSiDhusoOovzKG-u2eJ2vUdnc3UAIE-qcCr7nZUA0zJrLxhtHNbns5DW0F64gOeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVihA6TwmqhEqQ-YmFzjJIvVL0XzaudskoBWeQmQcMfzeJpwYxjFO1yh1vZ2BMYW_BiFR5SKUQObr8CKgVZL5Zyo1-du2wntUblpiphns8wvbb5Lgv5t43CrPt3ziniCofZsL-GkWpXhMg1Qxgk7Nhxm2GiOltxEsYaHOCJFT9kVYtcd4gVE5wRXpr__RjCqzjNTXNlHXSJLP7uJdi3gakx1sbGMd35Ar-igAKq0KOhltKkqOuFd8Nhxb29yolCkSedgIKjrsA__ZInNUm7dPNKT77KB2YEPksdBHcMP9_V49j6pa-vZg7wUBXt4Ws7f-KK6gjChrcabo3_yVtYymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucXGet6Zftv7jqURuwVfKJX717KBkmU1c-ijP34hcPavXo5znc8VlLZraN3oA1HbxhiLZTBhkPv-7WTgbprZLDycLyPwQcMaHxrdGMODLow49Ea78ojxda38L19-jNNx3tBBz035XRto4PYpwll3Y05brIXaUxSWOzMQQ92b9uhroPeA7SsUtHUkomKsX6Rf2PebnX5gigihjXzKVJzQ6JjUYxt5E8rc4aF4wEIomqRMh_oEoVVBj8ZmWBzKFha2c_QeKFXyRAmx8Q6VUhwBmWHkkmwFzHC29WGYov7P_WE435TxkrhJ4h_5q5_KO-dADqG8uXpG0TfceNdJ9N_PHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS4dA179bwTzFLcXa4RgfdIT8X_C9Y6xz52ze6CyfhjXvaOi_o0iPj7dAZe9KyBeAvYX2AEsUFS0IXk895FY_K7b1ac1Wb7tqkWa0kGuKfUFTx-Z--hz-c3hLMq7noA5m0tlXHDX9wr_JMKmuWv6FdLZZqJVP0ykGERBjqyFJL_b-RL_kRNDp3PfzH9lAyW3hivrWXEg94tw0x4gWt5M_I5NscVXEp40Siy_zrxkOaCr81b7NxkPCFHdx6dRgUfrOPgguWQsCGvTOzuwTJkHTmtFReDAALVbk5XLW4ToB-NLMDaDG_e5GMw6sU-LwX4s3DyqhaptHu5CGbcvg89Drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp8ah7T7Obcj62s2LIbwpL78zEw9jjCq3IEE-kvw7JejGAoG--LQXl0jox0jdND1AK94t8E8i34YkbCGwv9Q9y-uUMiNqBfHFcVm_ld4L_wbnTfF__xRXnxn9K_s4ijsLSctE_OPImMs1eUuHW4g1s6lMhHDiBTzvhDLbrur-ar244RrMnzOVWDGSLcYnsbCzGVEeET3aA6Q7n9oApfvY0z43kkql5QKXbSe-RJJep-yZbGLXWX0oFd84hApKFQmXc_3qcIYbfcfvKWMpgM9wBCYEHe8XRfPeLFVW5LGaqUbfP9vC6bhE8roo_6GE6Sz7HCHgXm-b0zCTayMaKLQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=uiT-dYsjQulFxfYJQR0kJVkevgLUtQHtgjIzsflskX0wPQp7v7JeOqfarZerd-Ozr62Tx-yF37zCQ9qbAKZbc7n1PZR2XjG4gUzdFwZ69hBfqD8PONBxBKFDQFVQyqSMxrKO8B6atxbZ6U5KZZIEQZ1KG2uq9UAKbrq_HLWV6gzhOoqglsYA90XbNHZpKvq8j6bDZQsFc0NEse_SRJ561IXO5XrjJVMWZXSzBXPVPOtmovnFFT011UThV3qoxrrtidx3lqghw7ft9HomX0TODkqxcgXOUyQ3a51KP1NAVuLamntf3Y00urZ8KHy8S8zIN5AduuH4ay_pR5-94oC0vGSrYt99fLDs0Fu2Y0iIKORpCFeYWLASFdXyUH2lXv_b9CczdpiaNqG9PAO2kusbLRy6SZks1hUPr-zM5CDeMmqEal6u_UVAU1UeNzqamUHvTnMGCvfT5UFdUlR21K2DFE3r_2z7vNKuLOKagAu6Dh76GYqa9Y2mTCoCguH8ZeyMfHLSIYx4hVMHxDwCfxLEWgDFEbS7vLivKafZuYzNHX2z5NFkcSfO0CdDeyp_q9I9b6_U5JWCrUh2CjvTY27EMghYKptVzs8zy5YvmQsjGcy7FNUBGOLsQF5j2w5t9rih5IgkEIUYTmdjW2-aMn7V4OFwwhCfk53ctQ0mi_NWa38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=uiT-dYsjQulFxfYJQR0kJVkevgLUtQHtgjIzsflskX0wPQp7v7JeOqfarZerd-Ozr62Tx-yF37zCQ9qbAKZbc7n1PZR2XjG4gUzdFwZ69hBfqD8PONBxBKFDQFVQyqSMxrKO8B6atxbZ6U5KZZIEQZ1KG2uq9UAKbrq_HLWV6gzhOoqglsYA90XbNHZpKvq8j6bDZQsFc0NEse_SRJ561IXO5XrjJVMWZXSzBXPVPOtmovnFFT011UThV3qoxrrtidx3lqghw7ft9HomX0TODkqxcgXOUyQ3a51KP1NAVuLamntf3Y00urZ8KHy8S8zIN5AduuH4ay_pR5-94oC0vGSrYt99fLDs0Fu2Y0iIKORpCFeYWLASFdXyUH2lXv_b9CczdpiaNqG9PAO2kusbLRy6SZks1hUPr-zM5CDeMmqEal6u_UVAU1UeNzqamUHvTnMGCvfT5UFdUlR21K2DFE3r_2z7vNKuLOKagAu6Dh76GYqa9Y2mTCoCguH8ZeyMfHLSIYx4hVMHxDwCfxLEWgDFEbS7vLivKafZuYzNHX2z5NFkcSfO0CdDeyp_q9I9b6_U5JWCrUh2CjvTY27EMghYKptVzs8zy5YvmQsjGcy7FNUBGOLsQF5j2w5t9rih5IgkEIUYTmdjW2-aMn7V4OFwwhCfk53ctQ0mi_NWa38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IThtvQl5cCzxzO834BTa25ktKO6Il7O_B8IvqwjhyI-SvLWu96vtS22WGVlRkn7-A0Zn5VyJZRZhEkMCqwBJWjXeAT_CoA8r27ZDMHUGCaf-ddGwuqs5rp2_r-fNtSsEWgnvGpsbEejZc5wCr-qQDCr8uJU-G57lANZw-8ovDzJpMGlEXopNAsQYcEvmK2Y6RjBHVhm0KzMGL1o8B1pq1gNmDw-2Ci7otWk0JJBwm_ZdeONrS7imNA0qECxv7osNsnzQYFEJz3cTvQPzQ-923JIFQQWHkXLQiPvkaZpjpzygqMEC1hNRvxg7VL7yTKM3SHmJkYftconXD-rQwG0_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB3uyqSzd2sSTMQap2hNUf6LqLLuHbE_uGYzaPGINdTRrBeT1SizEB7uw1_19FOFR16l88CHR1N9VhI-sBmYdjyCa-vCdkK4Mz4oavpabYuCKPCq1xkRSUCDU8eSOFYMcSruEz36J90HP2MldLqbP5PSh894IdH83mZ8X2GQC2_SpvIJKWONb09jJNn0vbeaHbX46OQ9gdt2Mn9x1qpfCK2IERcYeglt-5BUtVvRyT8Ui5lOtP8tNPN_r53yr6WoZVtt6BGKy0n0NvNljMWff_qAKvElh4FJTuvKZsy-sFJKKaMsF0NHCCgMBO11TuU2On6dHSVkxnYpZjtGwrAngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRfpXQ0ZuCbnWTy8v5cMfnvxZ9a5OAlqe1QdKEsNIhd2YKCV5Xmu2giUzf5_50HCyu9k1sKJbRLhM5rSkm80AT-yTbJnI03_KmT6CzinmAMb97JGhNUeDEW_B6DfmEYQIXzZWa5u28PuFGgra5xpS0cLi1azT_fX_kmCt5bmHNn6mmmceypOqZSq5-jc_KmP2KdZ8WDPFXsd1NN3aD5QZtDBrakpA8RYop0pLXeR2IxPJlig2i4IFbtIW2QSNYyoMUOYutEscbSlSspRJuNsGt3gkD72BcTejphAt7ID123q6dWwgKhQn7AbWtWhJu2j0kRzwfdclnni0yKIbUVL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ2tmITmFiGcrhZ_kbJGtiLGHsfKHp_q5dXi18nDZEh2xRAeNJE8rFoXxTtwqsVlyvjVi5CXm00JousUwmj4E7sOXUFVufI6FN6HDxZ2j3peswHEDtARNgubKvTzLOJ_YiUrhao_2qmO8ffD5RzSzWTANrle07owh1w_I0Ma71XzRgUMlny_gXXPXg_FtKlHECXzTU0uNKMxJjED7zLg4-Aq5AnzZFQYr50E0IG6x3ILUIzUWwUHJmZsrUELkEDhfqrJZgfA5PvgadlF4jwMXlo4lRSyMGsakAro0T6pSm2md83woldJCqjyBTnsrWnhSKj9m8aMRjjESlJYbAjepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMIjLLCbNZYrIxIDDyvIqwcOd5NFnSgvEm6PAka0QU01bEJ_OnHizMFKd8QtURlhAMU9xYgsIFXkIE1Rl89I4DLwQYlL6szxUIL611IfMuCFiguIq5LmsO-G-1o8_YYw6eRL8lYSjogT0vEJQy6_OWcCn9zkkkwOnvAmhycZUwXtGKAmDfGZoJWlPeCgiebCdTl67CiFwPd83RWCEI4GjWYmHBWU-pDLTzCrdtEBnzFEGv19HtveZ56u7pU28MS9BN3BBk0dDvIlNal23gv11X9PCFJGcyLMpg8eZY6Q-i5Dn-CpGrwjLuMjE6M99eAmSvzS-clI-tKaqZJqD83fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLUNFuRaR_2EvPmU0LyH0_Wn88mQU2x61s5oakIMfGvXkgQwXE360kL-ikW6TKnCns8V6egKLUSV_VXuC8fT-LrLIRyA2mKuc6aiRRQkzylLUQeJ-HznpzqfnCa6z_n-gnOVCiRq9Dv0A5cdhXZ7QkWI6rj3sIeTDov4o-Os-XOdJTfM3cnY6w1VCZ6eFPm0RnMcmuoWJ41FtAC3HShbIvlBfNNrD8_5mzvwHdftEPmHnw9fU9BTi2dOk29Q1CTDXfraBxf0qbBbCNUvxj5uwn3deZOAZHPq9NFSFzILEw6DgheCta9ocyYdgCMY_9lZOUnXs25CL36mp361GoIXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=kLwFkAqd7kB8nn4WR90cu5wGTMXbmdvrKjDdlxrvhQIwWqGlSxEaOD5T-fjzW8VvMeAbWZqgcV1HrJej494BVWo24KtKTIHcJcS64E18kNz-S7TzexRjYywmlGVaSJhpz2kIGYz_uLqpu9s4CO_Rh18sgUm-OEB5L06q-elj4REGoCSsTjc8LuebQdhHSFIyk094Z9h1fxcwiC7fqLbwtaQZzg7W7-6_Tlpq8S98fp803EJOd2fj9FIE5xUx6z6nzekUmPpZM8UtRd_KPWrCt0MR2UX2MWdaAdrAt4nZFakby2nqMV9F9wgbLo0cD5jGas80y3Xt4F7JBK_sppbApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=kLwFkAqd7kB8nn4WR90cu5wGTMXbmdvrKjDdlxrvhQIwWqGlSxEaOD5T-fjzW8VvMeAbWZqgcV1HrJej494BVWo24KtKTIHcJcS64E18kNz-S7TzexRjYywmlGVaSJhpz2kIGYz_uLqpu9s4CO_Rh18sgUm-OEB5L06q-elj4REGoCSsTjc8LuebQdhHSFIyk094Z9h1fxcwiC7fqLbwtaQZzg7W7-6_Tlpq8S98fp803EJOd2fj9FIE5xUx6z6nzekUmPpZM8UtRd_KPWrCt0MR2UX2MWdaAdrAt4nZFakby2nqMV9F9wgbLo0cD5jGas80y3Xt4F7JBK_sppbApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=VUAVOaKRlNqcRSLOJnmaW73x-VmMK6hUPOoV8XB3zxeiB2V9I09pGBhl5W95fodqhb3CiC6APWkT_LQU97hI_vDcmvd3eacwK7nWaLkxGXqr9MBBg7e817dGxPAfoHdh63wJkDn0E2_LoNfteWuc51ASAjoUBXe5CiRwjrOfnZbYHHQUUeBS2hxYas8OQDqLk4g6xp2y3_AKsxyGnVgBgHDlTggoOTj49lgKXvBa_21SZ6arowDF9HpLTs6ODl-ZoKtzi64LeIm5ei_yj5WFcElo-Yt3pD-BlqLqCg_lry60OYRLZ75XZNe9ziK9iUd9fdN7sOsL2W6ZNlH60X6EMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=VUAVOaKRlNqcRSLOJnmaW73x-VmMK6hUPOoV8XB3zxeiB2V9I09pGBhl5W95fodqhb3CiC6APWkT_LQU97hI_vDcmvd3eacwK7nWaLkxGXqr9MBBg7e817dGxPAfoHdh63wJkDn0E2_LoNfteWuc51ASAjoUBXe5CiRwjrOfnZbYHHQUUeBS2hxYas8OQDqLk4g6xp2y3_AKsxyGnVgBgHDlTggoOTj49lgKXvBa_21SZ6arowDF9HpLTs6ODl-ZoKtzi64LeIm5ei_yj5WFcElo-Yt3pD-BlqLqCg_lry60OYRLZ75XZNe9ziK9iUd9fdN7sOsL2W6ZNlH60X6EMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV7P4QNaIha2rkNjiuu0YiKpYSxZ2NfKMurenvveAFr65FIiAWws5_8go0x_yqapROJ2WmmoGg6hQRhEozML4Bo1uMWAv7-PVrSUyVNZZwsV2bEZJ9KTAruF1KuYukiVr2Gg9LF363y6ht7kBJRymbVmnqXQ_9ue2yJU_Zg3GO7owiIDu5ly_rA5UQIVjqXlGc4aQolWo2j1CUESu7XNrmOieoq1pXHiqJ2XJLWmW5UsfP039gzDb-7v5pcaK39Ooar3qM4V_9L1PhxMVk27KqonREPFS6ImCkqpfc8m5cTt1kI3VMYp2PfDTohML39jagd672a59xHhg_ksd2HwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avhvreq0oMNlREN-35Z4W57gKw4Yj95D7hd4yZiewl9HQWOOv78sSylhshfdGtg5YI06jtVq1HT_pJuSqx6iHSuqPQ2rZ8b43hXlQcrhaADVzQV1LW-PilCZOE0rKHMAslfz_0fu8mQeyLHjUtvwzXUvTzFlKRRMJlFOZfybqI0qVfejwh1ojPqEKVQg_TMRJ_wHVpqIZhmgC6TjAGYj_5166_-6-qmKpuG_qmnAVHh8pn0V2NXZVjvJic0x-UIxL4EHiWmonOhEq8OtlQnfh1sjoeqHHgBceF9jLTofhEe9GdtHtYSGaGj57VyYoHHsl1Md6RxFhOnzdEDk9BHGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=mf68pu2zSNq3BrNKNY7nJrfV8lNcb_egV8zpOLEOnP4LKiM8AoAv2U74ntv5ze13xV0_aRDQ2xfoF5oszZeSbnYBX4LcYt7Ecdwo5IrKwTyXwiTxWaAjHLuDq2lkRjXro76u_s_ZNEanSh3eiPvQzvEJkjhqNQcyRZU8YFvXiNDne_Si-hBJccWLeUEWg0MtF2-yGygNyo2v3keSZF14O0juBUrW2oD4j1hZG7b8vqK660ODBrOTOCVbyI8Zk5lIz5GIj4PITRZd753VJ7fSO6PRcDs6e9j-ceL-z8nubrwUajdmtPiUmZHUYBDq5wUt3bdHgBw2qcJ9L6-vDb0TWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=mf68pu2zSNq3BrNKNY7nJrfV8lNcb_egV8zpOLEOnP4LKiM8AoAv2U74ntv5ze13xV0_aRDQ2xfoF5oszZeSbnYBX4LcYt7Ecdwo5IrKwTyXwiTxWaAjHLuDq2lkRjXro76u_s_ZNEanSh3eiPvQzvEJkjhqNQcyRZU8YFvXiNDne_Si-hBJccWLeUEWg0MtF2-yGygNyo2v3keSZF14O0juBUrW2oD4j1hZG7b8vqK660ODBrOTOCVbyI8Zk5lIz5GIj4PITRZd753VJ7fSO6PRcDs6e9j-ceL-z8nubrwUajdmtPiUmZHUYBDq5wUt3bdHgBw2qcJ9L6-vDb0TWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYF0KVKA_IJAe79RBONk5OHDqoZ527a1ZmrJftctla33rhFCutyfeOD9c-SfU2dmnlRDuHkRVn_wUtoRNm2KroBBwNk1uvJH3i8b4QFK0HRNvFYUWu2ZhtoV1SDEWFb1CC0XGStckJzvGKUBoDaYCBqXr2OVGQkaI6hp1WPF14Okzh0scqIhAyPdwe7RBMEMwPScQJM2Ib_epFmaUOcqHnYNPiTNfncp21IWyMa2y9ixZsoCSAoDxM-FsZalfO2cFI0t7lAvD2TPWLDMOyUZJZlLqX-bhn4xK_8llXmFfoqzMGdoaV1vp30PdnQtqhioWpTX1JjWEM2ayBumVuA0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzvhqfaqui7I5pmCtixEa34uaFUVC28DDwjmofzQwdnQb5_Tl0yc86M2ae7-nXj_Oyk2EMXsK-FjEuhbiTrU66Qz6KSI5e1VtVU6cojJm-o1PqXE3pjQmn2VwTy9JiO3WDFTV7wGhPsfhN96GhuRqD3zLi4znOjRairYR8P9l0uvm5QjZ7JUsKppJbbq9qvSvJivz0M0Nr6-zsjbQKqP3kHIP6s-HyCu1aclDvKadCreIS21X_VWVTWB9OXN2XuOVdt3zxGV0ymXzCuk1XU17AHgOljpBKeViNKU0i3BnZUogrm0A-lXMOshiH5VEkNyd1oFLtb_RKK5Vq_uMIdcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
