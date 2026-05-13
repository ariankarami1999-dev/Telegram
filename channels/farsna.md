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
<img src="https://cdn4.telesco.pe/file/EU0qUAghnO4Nz-5Bwf5oc6xFADnAG4o0k5BqW9-n-DUKMU7oYf8y_rbC0uH7okxaUCkKGgfbkOF5h6WBXCcanQRUXstxcc9OXFyxer2KegUlMcRcvYGUoH43KjNp8a5kY8xQ1ULpvP0m2TbWHA7cRcIRoWbS4rXF4ymE-5odQHLKz96J06n6lGb3G2uyvbOE4QX7MYppOsFCA-IS0_gfEqv6tvHA8cUaSAwQKbnY9BC8LgX_n1Omw2YZeTtTb9e7ZrC2gl2SUvCj88cNj6V136eXdgm8OEql3ZItgmwFU081C-mt7PNDQbB-oQ50_J59SCB4qopMYxvBFXMoefjKJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 20:07:55</div>
<hr>

<div class="tg-post" id="msg-435405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p573izjdRFOzhClmXQiYsv-0DGw4MYG-Xljm5Oph1cbXlMlXzpxvbTX41YOBx0NnftddZUlFNrdvm_W7j5Fb1sHs_eqsRW17J5V8QAo6XcA5t7n1s6wU9HN8-uHjVuP-TRAwzUFzTSCSHEPuMLrbp3lvY2L-0p0TBJ1JDILlgWiKzhV3obw25io5CU6TkxEi9lUWu5hrdi6s4ERT2pzPNGvFC5ZkTGZUzst3L5UWG69POdrMAaVRl4nlgv2Se5WlmsJqCNGg01q5Nk252a9Ox7e7kD4xn4m5IVux_Sy7e0wup61RJxdWf2KK_M5hGkfBnO_afSKHdCNP5yTRbVCVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزارت خارجه ادعای کویت دربارۀ ۴ شهروند ایرانی را رد کرد
🔹
وزارت امورخارجه: اقدام ناشایست دولت کویت در بازداشت ۴ مامور ایرانی که براساس اختلال در ناوبری وارد آب‌های سرزمینی کویت شده بودند را محکوم می‌کنیم.
🔹
اتباع ایرانی بازداشت‌شده باید مطابق قوانین بین‌المللی…</div>
<div class="tg-footer">👁️ 61 · <a href="https://t.me/farsna/435405" target="_blank">📅 20:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e9154898.mp4?token=rJqDkC8tV57Q09-yoKb9lFMVSsVvKQfArtW1EL3h6_57b3wDGY6xyniKdKtHO842mMxfsFwreoPZ9S5OEj-OaNu6R9Z2KqQANQxH4jfmT5Bdz8zaAc_Wl3JDK29U22z6qSEYeJpONrKvroWU2hDDatf9oDUzIRkEgrNxnsseG3CazzuVDOXJBcEOVgy81NkOQxn8Lcuq9A5xTB8yu3AoKdM2--Sk5R23hXxjD20w-VxEendriwlWsB0os6RiY7NkYR-p1F7hI6QZpteU0xMloEOSq18BY0LUuZl6np_s1326B8ssDWq5SQ9uot73m5zMmoDYZWBq_6ggyOtwnDmpC3Ef8uebUV5geep-xKVoZ2_gGP5LLqQSOI6OVC5aKuwFp6QYcNUvaiPmFA9qbJ28SM3YQ0f4ScK6GIJDKzmn7hxOw9NBnB6wqeukLF1teWQgWI5pDec4mZA9_Z4D_OtNSKtf1ku6Np9OUcYsPQPiR2jXGC5VWI30PZXhnzlW06yjcueH9QOMmNoa77vOngLKjsm9ku_FWa09jFe13nCuUeBisvPAd1QWPAMeahoMPSLIV7FGqcoAzRl28KHn2oJMh8qZzt-C00O8CniSidAb9FuIqf5EmB9r3O9Js8wSDcmSyhrys9Io4eHR1TwodHveoFdVFoc4sreCgSNL0QigcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e9154898.mp4?token=rJqDkC8tV57Q09-yoKb9lFMVSsVvKQfArtW1EL3h6_57b3wDGY6xyniKdKtHO842mMxfsFwreoPZ9S5OEj-OaNu6R9Z2KqQANQxH4jfmT5Bdz8zaAc_Wl3JDK29U22z6qSEYeJpONrKvroWU2hDDatf9oDUzIRkEgrNxnsseG3CazzuVDOXJBcEOVgy81NkOQxn8Lcuq9A5xTB8yu3AoKdM2--Sk5R23hXxjD20w-VxEendriwlWsB0os6RiY7NkYR-p1F7hI6QZpteU0xMloEOSq18BY0LUuZl6np_s1326B8ssDWq5SQ9uot73m5zMmoDYZWBq_6ggyOtwnDmpC3Ef8uebUV5geep-xKVoZ2_gGP5LLqQSOI6OVC5aKuwFp6QYcNUvaiPmFA9qbJ28SM3YQ0f4ScK6GIJDKzmn7hxOw9NBnB6wqeukLF1teWQgWI5pDec4mZA9_Z4D_OtNSKtf1ku6Np9OUcYsPQPiR2jXGC5VWI30PZXhnzlW06yjcueH9QOMmNoa77vOngLKjsm9ku_FWa09jFe13nCuUeBisvPAd1QWPAMeahoMPSLIV7FGqcoAzRl28KHn2oJMh8qZzt-C00O8CniSidAb9FuIqf5EmB9r3O9Js8wSDcmSyhrys9Io4eHR1TwodHveoFdVFoc4sreCgSNL0QigcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آیین ملی شاهنامه و هویت ایرانی  عکس: زینب حمزه لویی @Farsna</div>
<div class="tg-footer">👁️ 302 · <a href="https://t.me/farsna/435403" target="_blank">📅 20:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
امتحانات حضوری دبستان‌های استان تهران لغو شد
🔹
مدیرکل آموزش‌وپرورش شهرستان‌های تهران: ارزشیابی نهایی حضوری برای دانش‌آموزان دبستانی منتفی است و نمرۀ نهایی براساس عملکرد مستمر کلاسی توسط معلم و تأیید مدیر مدرسه اعلام می‌‎شود.
@Farsna</div>
<div class="tg-footer">👁️ 452 · <a href="https://t.me/farsna/435402" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0098b7a4ad.mp4?token=XtNpdMVU30sL1a8CSFTm-F8mMAtQcnXvLIR3uAwTizJFjGZtf6S6HiAEcNLL1WKfNMrUZ9yd2jQKpkkIBGY_uTRTSn2WPpqKh4_xzsmF6ERuLnh-A-Nr5O6a9NzvQ8F8oWsUTBjGDOoXkp7jWcTyJu7n7QzKrXanfP4CmbMEtDXNRO1BLVK5f5GehNemaf4F7ToGYvC3TmemxmIAlf_he_dD1ny8dZvhuQIZWFXy4K8W_rKrvsPkrXqaJrbUwCnfziavwEBb9UFKK8jr4X40eSk4UhsIXxCLMsia5ks6oQAcRrcxJJZQeS2VIMNmPXu_oRfGxt6OzB_Wqnjp2esiLk8YVPLAS2tFXNyi9cLD9xQC1D0R10ZJsx63AJpLrUwVZ4OWVjgHatFNzrO6kQjqNHQ3ioNa529Ru9cMiiq_lzJr53tc3AN_n3yLddt_b9gRCybhwhMLpKc9Ol-PXToKdf3mUsqo8DyFsptHhn-NGJkZuIO96jWUgNSMGQnkp7cSayI-QxOLFV_oP-6Y3BRMacs4bac1iTSJPQ4KaOEAblBvmkb34HjK9XjnwGmpMs52R87vGODJIlayt3V3XAkGSNteos63BC68LoKqxczW8RHcYosXeXl15ffHre5cC5Lv2JzE7mZ4cpdHF1ioM7P9H3YMcrPUM550rfPtWpHvwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0098b7a4ad.mp4?token=XtNpdMVU30sL1a8CSFTm-F8mMAtQcnXvLIR3uAwTizJFjGZtf6S6HiAEcNLL1WKfNMrUZ9yd2jQKpkkIBGY_uTRTSn2WPpqKh4_xzsmF6ERuLnh-A-Nr5O6a9NzvQ8F8oWsUTBjGDOoXkp7jWcTyJu7n7QzKrXanfP4CmbMEtDXNRO1BLVK5f5GehNemaf4F7ToGYvC3TmemxmIAlf_he_dD1ny8dZvhuQIZWFXy4K8W_rKrvsPkrXqaJrbUwCnfziavwEBb9UFKK8jr4X40eSk4UhsIXxCLMsia5ks6oQAcRrcxJJZQeS2VIMNmPXu_oRfGxt6OzB_Wqnjp2esiLk8YVPLAS2tFXNyi9cLD9xQC1D0R10ZJsx63AJpLrUwVZ4OWVjgHatFNzrO6kQjqNHQ3ioNa529Ru9cMiiq_lzJr53tc3AN_n3yLddt_b9gRCybhwhMLpKc9Ol-PXToKdf3mUsqo8DyFsptHhn-NGJkZuIO96jWUgNSMGQnkp7cSayI-QxOLFV_oP-6Y3BRMacs4bac1iTSJPQ4KaOEAblBvmkb34HjK9XjnwGmpMs52R87vGODJIlayt3V3XAkGSNteos63BC68LoKqxczW8RHcYosXeXl15ffHre5cC5Lv2JzE7mZ4cpdHF1ioM7P9H3YMcrPUM550rfPtWpHvwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن تکلیف فرشته‌های کوار فارس در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/farsna/435401" target="_blank">📅 19:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حزب‌الله: سربازان صهیونیست‌ را در کمین گرفتار کردیم
🔹
رزمندگان مقاومت موفق شدند با استفاده از تسلیحات مناسب، خودروی زرهی دشمن را به‌صورت مستقیم مورد اصابت قرار دهند و آن را منهدم کنند.
🔹
پس از انهدام خودروی پیش‌رو، یک لودر نظامی که درحال بازگشایی مسیر بود، هدف قرار گرفت که منجر به توقف کامل تحرکات دشمن در این محور شد.
🔹
درپی این درگیری، نیروی هوایی دشمن تلاش کرد با اعزام بالگردهای امدادی و پهپادهای مسلح، مجروحان خود را تخلیه و از عقب‌نشینی نیروهای تحت محاصره پشتیبانی کند، اما با آتش پدافندی مقاومت مواجه شد.
@Farsna</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/farsna/435400" target="_blank">📅 19:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b211685ea.mp4?token=XsDdJr32f1I_XhbtnGTV8N9XlaWXncqkVGleEmysyjo0YwkT_9_wUOSYkYGf1piJeSnNf7KuFKPVaMbV3xGird_ZbpVSSOIS5Xro4K84BVarUlO-Iutembh2hmsKWorLfbw7hXaWQUQ1j8C1Oq2U6AAMnq-8KU_41Eqhq-3xCLFgLssc7jDRs7hAYjZq0L7LAY6Bhp_tep-RpdkdTJG7p2XYCBhtTduYB_15DeAW5Ral0ZldmOeW0GbXYbdnVJ7lABb0XzqR3LjLTHv7bcaV76uWgQ1ndXsnkQXq8h53-sxGY14y8rqTZ3T2rN1CJ4t222I4Cfh7s1yVzdXMgpYlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b211685ea.mp4?token=XsDdJr32f1I_XhbtnGTV8N9XlaWXncqkVGleEmysyjo0YwkT_9_wUOSYkYGf1piJeSnNf7KuFKPVaMbV3xGird_ZbpVSSOIS5Xro4K84BVarUlO-Iutembh2hmsKWorLfbw7hXaWQUQ1j8C1Oq2U6AAMnq-8KU_41Eqhq-3xCLFgLssc7jDRs7hAYjZq0L7LAY6Bhp_tep-RpdkdTJG7p2XYCBhtTduYB_15DeAW5Ral0ZldmOeW0GbXYbdnVJ7lABb0XzqR3LjLTHv7bcaV76uWgQ1ndXsnkQXq8h53-sxGY14y8rqTZ3T2rN1CJ4t222I4Cfh7s1yVzdXMgpYlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در مخازن نفت شهر «مرسین» ترکیه
🔹
این آتش‌سوزی تاکنون یک کشته داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/farsna/435399" target="_blank">📅 19:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1ca7b77d.mov?token=oEvsBCrNTUTkPk6Qd2i2tFtZiMREqofL7-ncfqOs_RvJW6L2OenV2ZC6oy0twati7kjgqswTP2dscBtd6bV_mlM64InC0ky4AvBcVmvOumiTir17PSq9P7qmM6s8hEM-UdhyJ4Rn57YvsJv_LQOOxw-VWwlK1ADvGRn8Ga8ijXE13e1V8c3zbMnM6tT_im26Zndr90SCT7LnJ43480fC0as4hKgKfBqnsP7zkvumER-EUL1HCumsl21Ivz1WJeCnjSU5WsTlbaKGqla_dr_zMNrZjjOxJ7AEed5HsCkiluUjHPJ37Zio0X2Aw1TsEA8JyzmKEfc6dJ3rhL_6qNtRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1ca7b77d.mov?token=oEvsBCrNTUTkPk6Qd2i2tFtZiMREqofL7-ncfqOs_RvJW6L2OenV2ZC6oy0twati7kjgqswTP2dscBtd6bV_mlM64InC0ky4AvBcVmvOumiTir17PSq9P7qmM6s8hEM-UdhyJ4Rn57YvsJv_LQOOxw-VWwlK1ADvGRn8Ga8ijXE13e1V8c3zbMnM6tT_im26Zndr90SCT7LnJ43480fC0as4hKgKfBqnsP7zkvumER-EUL1HCumsl21Ivz1WJeCnjSU5WsTlbaKGqla_dr_zMNrZjjOxJ7AEed5HsCkiluUjHPJ37Zio0X2Aw1TsEA8JyzmKEfc6dJ3rhL_6qNtRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی برای شرکت در نشست وزرای خارجهٔ کشورهای بریکس راهی هند شد.  @Farsna</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/farsna/435398" target="_blank">📅 19:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
آشنا: سوییس که به ظاهر آرام‌ترین کشور جهان است، قوی‌ترین پناهگاه‌های اتمی را دارد
🔹
ما بعد از جنگ ۸ساله نباید پناهگاه‌ها را از دست می‌دادیم و باید آن‌ها را توسعه می‌دادیم. @Farsna</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/435397" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435390">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVSR9xcokH8XtIHWVu3ROWG6J7Er1h0x2yRfhYtTinz5_R31j4qaEo6SUWsRuydXevkYG21rQH75faNGoEoxHcWB4qs41Nc0jlFSMPm0fqSNsK4CjtsNEZuGWE-7ORUplF5YPE6ng7quA7EvkJGJ3842Ln3umbZose_tr0UVxhlcGjSi6HAA9LmGYlZ7Q86tShyN9k8hArlJZNNWDNlEnKuRaf4GUfr4JzbkudWQ_Xv9s8cnPkJCvNFNqFyqJ-KDADsq0QigM8hDrGtyxh08z5NIfX3R3ECvrWH8DMht0mfryD5x9YSJFp4LjZaSOmPxjkSn101rYgdaWtoCLODLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzF2_cPGIC79LcehKDQrvaugF-urgy5oJ9Fr3w6J1i0826GOvEV6mV-ITpW6WG44-uYWcSSU7aox0IK8cG5ItVs_iqNhkxY0sNrbRwaXofuBsbjz0jAeu0-E9fXn69_kM2HYD2aCH8tUvwQ2pY3RE_HI69UR35TTE4RRcIvokr0fQOtOqZBgfgn4FXkQMks8sVdnVM0ZZM0uu4_R9kWtRDos0RZSs5g00K5CRHfdt3oiFeXXvJlnzr95t9XXCsrLX_g_-YSHuwG2tHfAS-l6PKHF5arqAmsQN0h24liUqZusCkoOlA-MDnqCiv9MYoy6fVNiT500Q1l8GGLAWCuZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4fDYPvWd52bJE3NdVEqWz1ZC5dwgZZJCJ0T6_oJ8pa-NfyXj80JrEptO7F2QHPX9IGSE2G_rANf1HyIiRQshEjqzX5Dn8xIbodxvyFa60HhEviZz7sQqaM2_ewu1wwgNSpUtfp8f1I3mdGFUbii5Cn9hPrLED8RBJafZq8yNYvHcN0hnMjBYMqE12A5FMtCDr5qkiyrFzeZDO9zgV8a6jzJSXFdvJT81lPct7YVciXy9ZgbmKtN72U0Z_PoDUD0Qh9DPQ4psmjlIMFRQ3VLZ2FiJXP06EtSeuz4npMfNLlBBKJ0eL6UEXUL4fdJGFfCY7vIh3IFBbN35zmRl0236w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDtl-maz2WOXxj5yFLIhN2OwwVyQZlznR1E8T-Ol_IZVgEbw72VA2o_XpmWL7hcTtedlkXrIRzJ1roWZnD_qUrIlJWmPotytMDwPEIdDieU961_B1lHpmSpYeq1vOo6QaSDgKLrC6qBxNEpoTlL_cO0HRmT83QXrXEMkI5cybicKzFFdyZ5KQIhFEo9T62qhV7uG85RqRT3udzxppEIffwcGOV0TeC07I1KOBY_7Gp5f6Hveb72_GQBL-rlThX50FJfwk5qViIEgCSKSiixSzTLBmf0T2NcwvzTwgxAAo9zWrZAWrmAwkMgTDIx09AvKBoCNIUqlG14iJBooWhzqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOjx-NW5S6aoZvW5htelhk4edIKNWZA32Ilj2IJhyR4iKPmaTanFeBj7WXSuOQFSfUz9lEBs4tOOwCWdB1JSGaSOyMNUxoPXKrMnBWTeqftPOLFJkUQgfxaym2Ak7AbVOLnmEdXPACa3FDYsS83asPJiM_H48rlR6wchmmdusKskNmfA1DJrx_qcuxJ_taen5pJUONr0zfaQTKekbXK3n9Qiy_Ya1xxgle_kLE0u9s9ACfyLr64TtxzpfOLnsen1mBaTkyQdk_xJamxZ18cXkRjAMKjTxcosKP9qMpUSjOHvUx3rHmf6upYyfH58zWht3LdGEPf2_wQ5a1izF5yKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVjfAtBMajmHvh0zyMMV2Yl7DePJ-vi5ndo_yXibJXEio1Oz73HcSsDZbMa-A3F2j0DOTzz5jMMNRhMES9Y9PELIgefCU1Cpgq8ZxAa3Nnsf1kViguIR8b0jrU3-w7cUz5Rv46qPRyEp_hQ-9jOR0XH3hEZolTvl7Qfvf_6K8ho3vt1v-pJvgp354m2TDLXr_A9P08pqbC1KVdykQPCpEjfC5tS2Jz4fEOVMY2rhGbtEznZDiswbB4569D414SvbDYfgI3n3wwRn2BAlky1-u0__o3SibGV5G3VQiwFV3TM33n51aLBvd0XZ2YSgPtRn-lu7MmiWJHwUMElMWOX-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUw4FU6iVQmwQBEBEEnT9O62wCwgi8fYz2n8H5Y6E0JsSmcb_gsGrzd029_EVyLY8Pqliqu6ch6IQv2AwxJ-y0Er4fb5WpcX247C8JDPIoAkdSssX2MFndZLwKg8uDFcbfpK1tmSVVeOE8OSS0ANhx-9yX1yaXx8kQrxgcQiKL_sRT8-Nd90Grb2zJfn5DbPKZSLn1XL_ndxxXQ8RiwNcGk7saIUxUa-ibf2rv6uFPAzSLYpFur7-1RK-mZ42bSR7p3V-1_5dIR2ocQMVvlBXDLHp5hUVw-2c2szjjGgI4TIli6ccmJPfS4fC4iSZeHNIwXA81zJJ5DuLhEwaEzFNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین ملی شاهنامه و هویت ایرانی
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/435390" target="_blank">📅 19:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwN5xsPt-OKyO0mfx5QldbtS0wI7581ODZuQVfaXpagFX9GcBAR3RXo2zPUH_yaDXddSwGM1NXeWEqtzd9hKODWkA4pD0iDYUG5Dsc9uysoGw3VaMmzpWD-F3wDhZL8-5gsevluOHiPDWfxzM1vTZilNTt8-h40BKrCR3tki9417iRg8kP6bn0dIvR4oEt2quIA5UMG2xlGEfk4Qf3p9A5qy5yOB2gvUBjuWKEPYsY1bA-1dOaB-Wf6DJ5wNnDfepokqmySgpoHQSTH-rQ88BD8jxSpYg33q5qU0OTPAbki1qxQ14_3tREUcqSuUuViFm9l5mAsgkrS_jvj-h76zYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات آمریکایی: اعراب بین ایران و اسرائیل یکی را انتخاب کنند
🔹
سفیر آمریکا در اراضی اشغالی خطاب به کشورهای عربی حاشیه خلیج فارس گفته میان اسرائیل و ایران «یک طرف را انتخاب کنید. کدام طرف را انتخاب می‌کنید؟»
🔹
مایک هاکبی ادعا کرده که اسرائیل «دشمن طبیعی» آن‌ها نیست و حتی مدعی شد که اسرائیل قصد نابودی آن‌ها را ندارد و «نمی‌خواهد سرزمینشان» را تصاحب کند.
🔹
این در حالی است که بسیاری از سیاستمداران صهیونیستی به طرح رژیم برای اشغالگری‌های بیشتر و پیگیری پروژه «اسرائیل بزرگ» اذعان کرده‌اند،‌ طرحی که شامل چندین کشور عربی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/435389" target="_blank">📅 19:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ab33e4c.mp4?token=mmT5hNlDDx1b_s1ai-x3R2jdD5zFmM5ALGx-8FX0vZ5aKHnSCKxwkkBYU2Mfalv0ui6eoGLc57Nt31JatIv2J9lzeJrlBe10DrQFwaES_NpaOPn8ezZR8EGsSnzZFatirEA8d_c-63vlxsh-61ZcLxCOS5URELOf2uOza0kXFUGmj5gaYjMChwtAFHZfAxFg002fDQU2njTVABqr805_JopajAR77Q3jJY2HxJLvlhGVd9wzp6bRykMPYdEV-uEodzblIdxGmyAauU8DIP533CT7D33LvYV87PJz7o06119lqItCZj0sP_oQt_3qjk9XG-bx-fB8qyAUMB2Wvegd3wpFn83INl-8KB9EUk5JUqhglQw4u9PCfk7rxdwj2qbeCfLr-79WNZwRFMW4VDM-Gn8VG_FufNHqBUnsx4pW9hil_5tRmihmuPdUXAbTQC6xYOj69tgGwxe6CIQMPkexAbFLBEEKNzoddHD2o0rd1aP8Akthg8AyhxmYOiqA2YEwaIenOy2KbCCRz_RBJ-UnBDBj1Gcyb-C5MlR3O3EnTmsKcPERbAhltV8h7zfAhFYHuXXvODl0dr61bHiove5HTuiKh12NI6icNPwkZRAYpJrzVfVTVhOxZqxPET8EbSEjvNeJuLMM-6KtwmT8wcgzvQKAcHvVvPK2DWL9Iri41IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ab33e4c.mp4?token=mmT5hNlDDx1b_s1ai-x3R2jdD5zFmM5ALGx-8FX0vZ5aKHnSCKxwkkBYU2Mfalv0ui6eoGLc57Nt31JatIv2J9lzeJrlBe10DrQFwaES_NpaOPn8ezZR8EGsSnzZFatirEA8d_c-63vlxsh-61ZcLxCOS5URELOf2uOza0kXFUGmj5gaYjMChwtAFHZfAxFg002fDQU2njTVABqr805_JopajAR77Q3jJY2HxJLvlhGVd9wzp6bRykMPYdEV-uEodzblIdxGmyAauU8DIP533CT7D33LvYV87PJz7o06119lqItCZj0sP_oQt_3qjk9XG-bx-fB8qyAUMB2Wvegd3wpFn83INl-8KB9EUk5JUqhglQw4u9PCfk7rxdwj2qbeCfLr-79WNZwRFMW4VDM-Gn8VG_FufNHqBUnsx4pW9hil_5tRmihmuPdUXAbTQC6xYOj69tgGwxe6CIQMPkexAbFLBEEKNzoddHD2o0rd1aP8Akthg8AyhxmYOiqA2YEwaIenOy2KbCCRz_RBJ-UnBDBj1Gcyb-C5MlR3O3EnTmsKcPERbAhltV8h7zfAhFYHuXXvODl0dr61bHiove5HTuiKh12NI6icNPwkZRAYpJrzVfVTVhOxZqxPET8EbSEjvNeJuLMM-6KtwmT8wcgzvQKAcHvVvPK2DWL9Iri41IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دنیا به ترامپ می‌خندد
🔸
وقتی ترامپ می‌گوید «ایرانی‌ها دیگر نمی‌خندند»؛ اصفهانی‌ها جواب او را این چنین می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/farsna/435388" target="_blank">📅 19:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435387">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357902fec0.mp4?token=DkDA5j6HMd1E16jOf_ruI47D84zu6dZrrY4nykBpP7wAJFBQWJk6RyYO2Ag57Gfq9SCtNjVPCpaQK5glvLe7yG16l9DtAmpZRYH6bseaIngNOzreACXNAIiPdsrWzSGIWpOQQxnlDQu2lUVoTmtVuwTnpkNsYinHUfpcizQ92Pm0NUfCqLpiSgGQy_CYcUBWqbwj2RqhUJXKy5nUmjG29oKbrJ4I1jtnHZ6XKf9oAadAVefugkQstrIH-2iLDzXhrtr72aICADQ46z7yzczutmzTe8RNDlvUbkAKOj8qwOdIsSk-msGr4SSGFKmEmuiwvKrV-Bwuh78Dr2DdSyocLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357902fec0.mp4?token=DkDA5j6HMd1E16jOf_ruI47D84zu6dZrrY4nykBpP7wAJFBQWJk6RyYO2Ag57Gfq9SCtNjVPCpaQK5glvLe7yG16l9DtAmpZRYH6bseaIngNOzreACXNAIiPdsrWzSGIWpOQQxnlDQu2lUVoTmtVuwTnpkNsYinHUfpcizQ92Pm0NUfCqLpiSgGQy_CYcUBWqbwj2RqhUJXKy5nUmjG29oKbrJ4I1jtnHZ6XKf9oAadAVefugkQstrIH-2iLDzXhrtr72aICADQ46z7yzczutmzTe8RNDlvUbkAKOj8qwOdIsSk-msGr4SSGFKmEmuiwvKrV-Bwuh78Dr2DdSyocLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: در جنگ ایرانی‌ها فهمیدند عجب چیزهایی دارند
🔹
وقتی پل B1 را زدند ناگهان ایرانی‌ها توجه کردند که ما چه پُلی داریم.
🔹
وقتی مدرسۀ میناب را زدند متوجه می‌شوید که در مینابی که ته ایران است هم مدرسۀ کپری نداریم.
🔹
در جنگ است که شما می‌بینید شبکۀ برق‌تان را…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/435387" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435386">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86a5b68eb.mp4?token=eferSD8bKm_252u625C4-GPx2BmHFf29b2dhw3IzQQ4-3haaMTeTInJj7Zr1w63vgxU8Zy559M_dZJAE5TxbaYI_SzRvCdBnwaYyn0S7Ev_kK4v0sEPRmk4djTtj2PwXlVFnXm1whKraBjpdZIuvfTqCCuv1L0wwlJBK9-i789Tw0wHSHR7U5xpi5aggZ68mDfZfMIyvtvMksKdx7QX2kLcBdq-EwmfJzyqgQ0Cjg36cCZpjcELk1R2qdeKx4lXjzKJWhljdOmTV0fVIL8pDvF8JJsNMC_znh6zhOJoYm71HHH8TXTKjbhVNXUrSck8KssnVSQ4bUY-TWX-_Jx6aSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86a5b68eb.mp4?token=eferSD8bKm_252u625C4-GPx2BmHFf29b2dhw3IzQQ4-3haaMTeTInJj7Zr1w63vgxU8Zy559M_dZJAE5TxbaYI_SzRvCdBnwaYyn0S7Ev_kK4v0sEPRmk4djTtj2PwXlVFnXm1whKraBjpdZIuvfTqCCuv1L0wwlJBK9-i789Tw0wHSHR7U5xpi5aggZ68mDfZfMIyvtvMksKdx7QX2kLcBdq-EwmfJzyqgQ0Cjg36cCZpjcELk1R2qdeKx4lXjzKJWhljdOmTV0fVIL8pDvF8JJsNMC_znh6zhOJoYm71HHH8TXTKjbhVNXUrSck8KssnVSQ4bUY-TWX-_Jx6aSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگترین اتاق فرار دنیا کجاست؟
@Farsna</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/435386" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435385">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c03f1b81d.mp4?token=XypNkQwAsPaUG6iw4lRcbvvGrnPaFVl4bLRrXEr2Q5f_psfkJLYiRAkQSr3_OmFjSafNbRXwbhrDAN36zmllqe0DzkAMez3hV1BvYaxOePtsTxveC9jyrHTu-WlJIudoBac82STjDLpSJAuVx0zW6HdRoxUp9dbhwqGwRMgNLOIAydFn4t1TWkM23lhO9Xx3-RfHiFeWm6XH6FVISJBuMH3SXcMeZc3GR7ObThiQkbImeFW7y4Zevk5-1HFJ8HS1XSCYsN3bZt0c5b8yGYTzkAZjC9i7YE1WDMC03_QP9x3eLGYbwZ_Res3mASTeQe0PDbGm07zPcgriHMUYWh2u5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c03f1b81d.mp4?token=XypNkQwAsPaUG6iw4lRcbvvGrnPaFVl4bLRrXEr2Q5f_psfkJLYiRAkQSr3_OmFjSafNbRXwbhrDAN36zmllqe0DzkAMez3hV1BvYaxOePtsTxveC9jyrHTu-WlJIudoBac82STjDLpSJAuVx0zW6HdRoxUp9dbhwqGwRMgNLOIAydFn4t1TWkM23lhO9Xx3-RfHiFeWm6XH6FVISJBuMH3SXcMeZc3GR7ObThiQkbImeFW7y4Zevk5-1HFJ8HS1XSCYsN3bZt0c5b8yGYTzkAZjC9i7YE1WDMC03_QP9x3eLGYbwZ_Res3mASTeQe0PDbGm07zPcgriHMUYWh2u5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیوارنگاره میدان انقلاب با تصویری از ملی‌پوشان فوتبال
@Sportfars</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/farsna/435385" target="_blank">📅 19:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435384">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e2c0d3d.mp4?token=n2tznFyQXI2NcUfoA-g7FW08jOvvsGm5CLKKC2PLKel0cajp23AkAnCGacUQSnc9SSmAua8pLBw3mTEUiyt-umIIFoQMOp7S0jphktFTBCbK05520Vr133DWHsKgiGwgxYW_nrth0PMQHsJkxhOTVU9nTaY_mFQQAajUCGtnnGkAC1Ewvl4lzwlqrN4G8WZi9j8cDuXr9pgb2zkEFlHdpgJZ10Rpz-EN9zMivhRYy4r_SU6QUotgvf3jN1Jk4FscwAX2GNXZBfeFqPTgcwntvz8TUPNEtuF7Zk4zrKUqLEB53JYMkXz7qRcOqhIkKd3EBH3N3E-v_KWqGN_qZYRzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e2c0d3d.mp4?token=n2tznFyQXI2NcUfoA-g7FW08jOvvsGm5CLKKC2PLKel0cajp23AkAnCGacUQSnc9SSmAua8pLBw3mTEUiyt-umIIFoQMOp7S0jphktFTBCbK05520Vr133DWHsKgiGwgxYW_nrth0PMQHsJkxhOTVU9nTaY_mFQQAajUCGtnnGkAC1Ewvl4lzwlqrN4G8WZi9j8cDuXr9pgb2zkEFlHdpgJZ10Rpz-EN9zMivhRYy4r_SU6QUotgvf3jN1Jk4FscwAX2GNXZBfeFqPTgcwntvz8TUPNEtuF7Zk4zrKUqLEB53JYMkXz7qRcOqhIkKd3EBH3N3E-v_KWqGN_qZYRzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: الگوی توسعۀ ایران کاملا نشان می‌دهد دولت همواره نسبت به گسترش خدمات عمومی به دورترین و محروم‌ترین نقاط توجه ویژه داشته است
🔹
ایران تقریبا به تعداد تمام استان‌هایش فرودگاه دارد. اگر الگوی توسعۀ ایران چیز دیگر بود می‌گفت تمام پول این فرودگاه‌ها را در…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/435384" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435383">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBwS9sXbCuTvH4KGR8yE7PHOYVvnFq8Pt08k6RiTngZvQzxWG7sSYc-0je7DAPwS1zNWcIsYxq2mYKKO42jc_cdbXbyU_Po-igAX_O3r9Rh4g1oxqFbgHNQ2-5Pwe-JrhkkbHfKpGL2gAtG1r32Ee2w0M--7Ts8kYHN7-OHgXbTp_zF9xqqnzprT1wKAACAFxkQDMyGVR3r2G3WDQ7zTGFmdiUgJYjkiwYxD6SBjjmTZr4Z5ltIVFeS6ByI7RSXqMLu9xdI4j1InVIWijoBOeTQZey5RNnmSL35ipT6Pf1O1u11XguDviZTq1e3wmBjoXZGPEm4vKX7F6g7hfykew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: تابستان خاموشی نخواهیم داشت
🔹
عباس علی‌آبادی وزیر نیرو: با همکاری مردم و افزایش ظرفیت تولید، وضعیت امسال از سال گذشته به مراتب بهتر خواهد بود و امید است تابستان بدون خاموشی سپری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/435383" target="_blank">📅 19:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435382">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f423d72.mp4?token=LUqHBuy1-OA33T6j14zIAkAXvbk3hTy-uJ3HsBVYsc7mQrr_ECkTH_4531tBsQQf-xV_56xkM-jhYgKrByZiRE3xZ2ltCXlX3Gu5x3W4loOI0Wdv_wSoGNJ00cDrl2KpzTmKRgrPcv6wPBoBkEGnq0gTCaEuLYNCEng5tCrWadZKtuCBEt-OpF3ARMd4v6caKIJzmfA0k5kwiR6EF2-5EuGBI41loMkf7MjBUV76NTjXD7vEbMdWt7zjkoaXx-5VkzygB1N0OKGrJ2lvDtF0apVm0z5_0k_CCq5tf5zo-3Wxh_pLwxZtpOrBET6NjPje1JlEUxSUNKj8ur64sN4dYhkL5xqnZq7ABhoUFRlmLWhb3GG8sLz_AwugK38Grqwx5uB1ZxxzZZYRdUBL3k2wCR3ROkAsjpr0vZ-u_SoZ8de4BgAHv_7yxxOAiTirs0VpzRCXW-4Fs-ZaMEU6VN4mqBZsyknpO75wOLtH5GyMqGnuq127-hq_4Vxgh1PV0aAWuRmq8Z_y68K5DkvaxEgPxeyVbMtAh_KC6ormvCC0EmJVv_1sO7O53xJqGI2PlGUnpQhdtLWYOkjif6jhwF6H7CQetoMC8_WuYeroGX697q9xnQd9ritsr0o9IKwQvzqvQALP3VDxzCZZdCZinMidNSy5-5ntjvJiJj_6sA8aDeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f423d72.mp4?token=LUqHBuy1-OA33T6j14zIAkAXvbk3hTy-uJ3HsBVYsc7mQrr_ECkTH_4531tBsQQf-xV_56xkM-jhYgKrByZiRE3xZ2ltCXlX3Gu5x3W4loOI0Wdv_wSoGNJ00cDrl2KpzTmKRgrPcv6wPBoBkEGnq0gTCaEuLYNCEng5tCrWadZKtuCBEt-OpF3ARMd4v6caKIJzmfA0k5kwiR6EF2-5EuGBI41loMkf7MjBUV76NTjXD7vEbMdWt7zjkoaXx-5VkzygB1N0OKGrJ2lvDtF0apVm0z5_0k_CCq5tf5zo-3Wxh_pLwxZtpOrBET6NjPje1JlEUxSUNKj8ur64sN4dYhkL5xqnZq7ABhoUFRlmLWhb3GG8sLz_AwugK38Grqwx5uB1ZxxzZZYRdUBL3k2wCR3ROkAsjpr0vZ-u_SoZ8de4BgAHv_7yxxOAiTirs0VpzRCXW-4Fs-ZaMEU6VN4mqBZsyknpO75wOLtH5GyMqGnuq127-hq_4Vxgh1PV0aAWuRmq8Z_y68K5DkvaxEgPxeyVbMtAh_KC6ormvCC0EmJVv_1sO7O53xJqGI2PlGUnpQhdtLWYOkjif6jhwF6H7CQetoMC8_WuYeroGX697q9xnQd9ritsr0o9IKwQvzqvQALP3VDxzCZZdCZinMidNSy5-5ntjvJiJj_6sA8aDeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: ایران هنوز شگفتی‌هایی برای دشمن دارد
🔹
ایران ظرفیت عبور از چالش فعلی را دارد. برای توان نظامی ایران، ۴۷ سال زحمت کشیده شده است. به‌نظر من هیچ‌کس نمی‌داند ایران چقدر قدرت دارد.
🔹
اگر قرار است مستقل باشیم آخرش اسلحه‌ها حرف می‌زنند. @Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/435382" target="_blank">📅 19:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435381">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b50003c3.mp4?token=vJuV8-La7nAKuVcfXF1-BHL1jzTrMmoRNm2aDaIxeXFR12nDuaD68W8Wy7buOWEcGBgr_EqfUF5EwGMNOpEidEBFtPV3H8jkPr321mXOSCYovOfjrDs8e_gOsMUY5q_oUJpKzB2gFPJuEspt121W7bpkt8KvJfIrDXbNeCRY0qU_8iGcRrNSix3IV5LeSXe5LdAR1LeBqCuE0IgRD5EQqm6KztyTzDD0FAHNABKXz7XRYcHXlZ91P0Zo-n9yeGoSrk5dJXW5xk8FqB0XxvqY9PaasHG3cphVSEbbHlZzuUMjV_j2lqzOWAy1YnPYGfkJK6Dl9I0lvatDd_7eW-rMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b50003c3.mp4?token=vJuV8-La7nAKuVcfXF1-BHL1jzTrMmoRNm2aDaIxeXFR12nDuaD68W8Wy7buOWEcGBgr_EqfUF5EwGMNOpEidEBFtPV3H8jkPr321mXOSCYovOfjrDs8e_gOsMUY5q_oUJpKzB2gFPJuEspt121W7bpkt8KvJfIrDXbNeCRY0qU_8iGcRrNSix3IV5LeSXe5LdAR1LeBqCuE0IgRD5EQqm6KztyTzDD0FAHNABKXz7XRYcHXlZ91P0Zo-n9yeGoSrk5dJXW5xk8FqB0XxvqY9PaasHG3cphVSEbbHlZzuUMjV_j2lqzOWAy1YnPYGfkJK6Dl9I0lvatDd_7eW-rMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
فنجان اول اسپرسو با آشنا  گفت‌و‌گو با حسام‌الدین آشنا را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/435381" target="_blank">📅 18:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435380">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Live stream finished (4 seconds)</div>
<div class="tg-footer"><a href="https://t.me/farsna/435380" target="_blank">📅 18:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOI-R_HJfqXW2SZysTCHfqs-QIUQpRrsZfKWrkffuOX_bbouyXtbemEVT_rYOBuh_IPt1xMzGKfAC7JXI0nzqAFR3LnrLD_NBXg74HkOI1rfbbcWhyAl1qtAyaBRSl0LGkQjLK9a6jq1u7V6VyKNI6paH-tjIm-Qjbx7cYf_C-b1BzStUG1gKHVPZjZkex_nCMFeUbGUPyKrMKjgNy7_O3ranA6bYwxoEQTOKMewRHi7BBbWJ30f26hWUEV7jvHSYgTgbmM3ztOHVV2Qilj0gCjsVxszbpPGxXJXVRacVSLap8mZKWsNk_TR8ba-3u0K9QjoHoj61GpVUzujCdKPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به تیم ملی فوتبال: برای نام ایران بجنگید
🔹
رئیس‌جمهور در جمع اعضای تیم ملی فوتبال: آنچه برای ما اهمیت دارد، مجاهدت صادقانه، تلاش مسئولانه و به‌کارگیری همه ظرفیت‌ها برای سربلندی ایران عزیز است.
🔹
نتیجه، محصول اراده، تدبیر، تلاش و البته مشیت الهی خواهد…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/435377" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4NV2ABFagMJbnt06TsibSJtJz2M2_UtqNKn71-nbvOuWsD_YI6EtFIsyXLsB2maO3Esgh7tqLkJVYnBKvzJZW30EB8oPMfIT6MOmf8zVf0Z7wKxHDBud17Kl9eqH40zIqT8vwbKmVXbpnzvhkUS-IMxvp_6mo4942BLOkIKgDTPvNMrTZP1cybEnvDvB8e_jLqbza6wIjnVfGCHL6QCEtnD5GtkbpS0x6ram-swtCzxbcJMnBQRr00Ghx6GFfBiR_s7E-CuIAQDBKfGoPq_WQfSSSVIOJwp4f5aMEdVq8FpE3Tf9pBHj-Z4R9XzfRqeVa-rRVq3_GWZGQDR7nq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به تیم ملی فوتبال: برای نام ایران بجنگید
🔹
رئیس‌جمهور در جمع اعضای تیم ملی فوتبال: آنچه برای ما اهمیت دارد، مجاهدت صادقانه، تلاش مسئولانه و به‌کارگیری همه ظرفیت‌ها برای سربلندی ایران عزیز است.
🔹
نتیجه، محصول اراده، تدبیر، تلاش و البته مشیت الهی خواهد بود؛ اما آنچه ملت ایران از فرزندان خود انتظار دارد، ایستادن شرافتمندانه و جنگیدن با همه توان در میدان رقابت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/435376" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv3kZBASh6Ppz_c7kyG6Vi1he58Bflrkd82Ip71SSJqxxZrGAf8m59DhC-k4t-Ab7DcnAvt_Qm3IF7nGveTAMPoLlO39MTxKow-zWqCfwnylerF6PuMTncA-1xYLkQpiSwsYwtkUJ_TPMerPG644k3mgUJ-N4DBL4-xaS4Ak-w3-hIqxHEpvWQVi0GcVuxJc5w6MEe256J_y9Ojz-w0FmwNUbizd4l2gt51Cl1QZ_VGcIyufK7AKK9NdpKtZXmmkmb52Texp5Sq98jfBf1-lbHfChtlaQDf98vBGoJGdViXKmeO4jlfR-UhZHrqdA5ghirY0IXm5QmGVGX2u1MSaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
فنجان اول اسپرسو با آشنا
گفت‌و‌گو با حسام‌الدین آشنا را هم‌اکنون در
سایت
،
ایتا
،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/435375" target="_blank">📅 18:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-34.pdf</div>
  <div class="tg-doc-extra">2.3 MB</div>
</div>
<a href="https://t.me/farsna/435374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۳۳.pdf</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/435374" target="_blank">📅 18:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JftG4Z9lf5WPnCr7ZUyWkk-9KiyTpdjYfoQJoNQxzhmfHwUTxewg8wXohfGQXDAZmdBdwMIVydTE9iCPwDqHIuVoWS2IrcbL_XZE8DPzsV7WCuDBlClY-UQfvWO5DsxyoYhnyPMpYtVG76mxHnvY2sGiNWFjY3SC6A5Dn1moAd20szTcTU3hirEJ_CGJ2Det9exwmpVncbpsJl0MVKdd-5Y7xkxiM5qnMW1ddunG32TJ2F7xOwaIsnRuTsouzUUaukvbw6RAf2XsPkbB8RUWQl-igEMfCfE2pXfgm4o4imJQT-r6CYSVK-7TWpT1_AGtxrfdd_zC4ayZDf0xvoCW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک سرباز صهیونیست را شکار کرد  @Farsna</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/435373" target="_blank">📅 18:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/435372" target="_blank">📅 18:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435369">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Zl-zm9Z2jcXY_P1YSpNS53zcVOEn-FmHl59D6Ki2jY88m_d4E2HaG_1dg5TDs1bv-Jj7dqGT7tX8EL2Sn1DylS4v9z0XR0QzJFFRUQgnJzqLGqDVFuDc7dbbJlo-t-0pWRC2RH-dYr7Ap-WtL4DQrISurSMxjfCx8nVXrvbmcFpb-1ybR1dbP3bOME0mi3vcUbZ_o7klMxgHuyshvU0Sz8ztJP4xDroVJM0M9296ic9YBEtmcGw_zxu6YE_-c0u5dWuQcSy8QpTJjzymE-UZJsPYNk5trSks2krF-wZDxiNsxX32QdB_gb2RIk-TMcRjGl_Nstfze-EPC02yQZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: تأثیر جنگ ایران، برای صنعت هوایی در ابعاد بحران کروناست
🔹
اندرو لوبنبرگ، تحلیلگر خطوط هوایی در بارکلیز، می‌گوید: گرانی سرسام‌آور سوخت جت فشار زیادی به شرکت‌های هواپیمایی وارد کرده است. بحران فعلی مانند «کوویدِ بعدی» است. ورشکستگی‌ها، ادغام‌ شرکت‌‌ها و بازنشستگی سریع‌ هواپیماهای قدیمی در راه است.
🔹
احتمالاً دوران سفرهای هوایی ارزان‌قیمت درحال نزدیک‌شدن به پایان خود است. بسیاری در این صنعت اکنون در این فکر هستند که پس از تعطیلی شرکت هواپیمایی «اسپیریت» آمریکا، کدام شرکت ممکن است بعدی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/435369" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435368">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIKVEVScLBb3IFaGiGLmZ3n2arovLfhsyi-WXA2MCEHMTBQptUfkc0yrBWpcMJ4aoeZ56L_nDbOo6djvXFdeMQEApki2iead5wCsmsR6jkYNbFVuJHIL6GfBkb7A7ZJXdMMpnO98jEeGawPRXOMhS-zY20eKUoFP8CPwaYBleVHtUVk43XAyE-7BwZUHNi7QEU7qqDfhcW_AryKx2GVvSFNiriWFMzzoTjujj0VmCMJTt6rIPzPNnare11gGxBEYxFCRD8FSWzy-NwBgpxcAqPhcMdQMgkrGy18Yhg_8HBskNO-nWknTwj5qHTMLpn88sn_zzQ_q5Bxr5QG4ajlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت خود را از بازار برق بیرون می‌کشد
🔹
سندی به رویت خبرنگار فارس رسیده که مشخص می‌کند، مشترکان برق با مصرف بالای ۱۵۰ کیلووات شامل بخش‌های خانگی، صنعتی و کشاورزی از تاریخ ۲۲ تیر باید برق خود را به جای دولت از بورس انرژی خریداری کنند.
🔹
پیشتر برنامه هفتم توسعه دولت را مکلف به خروج از بازار برق کرده بود؛ از سال آینده دامنه خرید و فروش برق در بورس برای مشترکان بالای ۳۰ کیلووات نیز برقرار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/435368" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b553572d.mp4?token=fxPeANqfBnrVsEMEYS1qWKhUXBIP2oMgIohucw1GmbtYLDmPUjtNywUMjF_RSGVtdbEDzjAPmFNus8jvb1i3ClPY7DA3IjufCCZc3YBQieQjD6dfuDDhFOPefGj6IDniJMIGiybIhQfCtqYnvHSNa59iQQUFKvetHwB4Et15_kZbCyRz5Q1MOUP0nOZy7J2-uMbIkMnwpu_TnQj-km13eDbDy7R-uCsfKCPxYTge-Cf0XkhueN7gaQ0BuSQMWXgLJEXvM7rF-8zSJ1XMRZ2lF5M-353VZZ_tQv0hha1j5dcxZZw73zmaIW_wIQeMllLKleWSGqDSGTbQssa_wFwJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b553572d.mp4?token=fxPeANqfBnrVsEMEYS1qWKhUXBIP2oMgIohucw1GmbtYLDmPUjtNywUMjF_RSGVtdbEDzjAPmFNus8jvb1i3ClPY7DA3IjufCCZc3YBQieQjD6dfuDDhFOPefGj6IDniJMIGiybIhQfCtqYnvHSNa59iQQUFKvetHwB4Et15_kZbCyRz5Q1MOUP0nOZy7J2-uMbIkMnwpu_TnQj-km13eDbDy7R-uCsfKCPxYTge-Cf0XkhueN7gaQ0BuSQMWXgLJEXvM7rF-8zSJ1XMRZ2lF5M-353VZZ_tQv0hha1j5dcxZZw73zmaIW_wIQeMllLKleWSGqDSGTbQssa_wFwJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامه سمت خدا:  آمریکایی‌ها می‌گویند ما می‌دانیم ایرانی‌ها چه تجهیزاتی دارند و راه مقابله با آن را هم می‌دانیم اما بازهم نمی‌توانیم در مقابل ایران مقاومت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/435366" target="_blank">📅 17:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bfe83fff2.mp4?token=SPWX8FSzRJ9eQAeqMqQNjacPSELJ9ZaS_7Kv_7MjSxeeOFkUZXmyMGz9cDxtixVpU6iJ0eJMt5phkLxiXpo8Td07M6RLmwTFnrftTTU1sz9PtfWzNhjJB_UzuhWd9_E3xpfaetd0Xk-QAeYorr-TSl34bmvXAoleqVCqzjzzj1Gl9pWqCpyT_K2Ok3lsfa_Pp2-9pEHopTTWBzZhqp-P8eIR5APejktO8SdY8BFj0XyKUv6hJetJJPHFXVQKjo4YiCmDpmXDNNLlsgpHiDxxvIqZqqtj7FBuVOYQyG4TkrFKh1iy1X9IUCGk2XCd9thDx9mL9RU68rIbJVcvwzWh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bfe83fff2.mp4?token=SPWX8FSzRJ9eQAeqMqQNjacPSELJ9ZaS_7Kv_7MjSxeeOFkUZXmyMGz9cDxtixVpU6iJ0eJMt5phkLxiXpo8Td07M6RLmwTFnrftTTU1sz9PtfWzNhjJB_UzuhWd9_E3xpfaetd0Xk-QAeYorr-TSl34bmvXAoleqVCqzjzzj1Gl9pWqCpyT_K2Ok3lsfa_Pp2-9pEHopTTWBzZhqp-P8eIR5APejktO8SdY8BFj0XyKUv6hJetJJPHFXVQKjo4YiCmDpmXDNNLlsgpHiDxxvIqZqqtj7FBuVOYQyG4TkrFKh1iy1X9IUCGk2XCd9thDx9mL9RU68rIbJVcvwzWh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک سرباز صهیونیست را شکار کرد
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/435365" target="_blank">📅 17:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef4869e61.mp4?token=Sgqg26lMZKJDki617Of4ytai1WsdQecer932goZhBEpumhLUJ4E2Vg9MLFkgufoLaFZIw-L1PDY1bXpPxJLjCDwtVJgOr1hVoSf7HVubO1V_-wiQ4BIB0skiVk6u073xuu3GXsK6z3h7IEX_cBl73KmXNYVjcgOef-uFhmbhETBNwG1uQG-bsJztIVTJPhgxV53UxZt9VSZ4XgMMpHivpUsb_b6kGnDmATEOaJvHpgf9ewqWjGkkj7Sfcx0JD-YV66Mxj4MzGJCZKsudwJitGMjZF9LZ6c4YSC6pl6ImS1iNGbdPoxDuQhvkNNTmQ5unMBN23XdRxLCRtqekepCshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef4869e61.mp4?token=Sgqg26lMZKJDki617Of4ytai1WsdQecer932goZhBEpumhLUJ4E2Vg9MLFkgufoLaFZIw-L1PDY1bXpPxJLjCDwtVJgOr1hVoSf7HVubO1V_-wiQ4BIB0skiVk6u073xuu3GXsK6z3h7IEX_cBl73KmXNYVjcgOef-uFhmbhETBNwG1uQG-bsJztIVTJPhgxV53UxZt9VSZ4XgMMpHivpUsb_b6kGnDmATEOaJvHpgf9ewqWjGkkj7Sfcx0JD-YV66Mxj4MzGJCZKsudwJitGMjZF9LZ6c4YSC6pl6ImS1iNGbdPoxDuQhvkNNTmQ5unMBN23XdRxLCRtqekepCshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهرهٔ رسانه‌ای پرنفوذ اروپا: با افتخار صهیونیست‌ غیریهودی هستم
🔹
ماتیاس دوپنر، مالک پایگاه‌های خبری پولیتیکو و بیزنس اینسایدر، عضو هیئت‌مدیره نتفلیکس و عضو کمیتهٔ اجرایی کنفرانس بیلدربرگ: صهیونیسم نژادپرستی نیست، بلکه ضدیت با صهیونیسم نژادپرستی است.
🔹
من با تمام وجود، از روی اعتقاد و با اشتیاق، یک صهیونیست غیریهودی هستم. اسرائیل تنها دموکراسی منطقه و سرپل ارزش‌های غربی است.
🔹
اسرائیل با وجود همه مسائل، سرزمین آزادی و مدارا، و سرزمین دفاع مقتدرانه و موفقیت‌آمیز از ارزش‌های ماست.
@Farsna</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/435364" target="_blank">📅 17:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812709ce3.mp4?token=Rb7QqJC3Tca7BJLR6cVO6NV2tts8jw2RzE-xqbA8eSU-_wudALMTgP7WrGQgwRKLx93vFUW8KbSVSm2EA6LUbZC4beYsBGOdw_Eb5eTIIITMQMYHzmtVUDL3ecL8lhHGcmJZuP-0HXcCbU3VyOo_hvUtGtWgclXBpyA_Z1w-U0ilkZReIu9hw9SqkKlGAGKF7ShcLZzZeZ6yT3Rn7x8KPQu8Il-Gz2VZu345QA5M7zXER3i82yQTaSx3pj9WyGbMPTyWsaQbRGOYWhZjLZdtx0I6QXcdVUU6P9zkkQBdT4Ip-wRIaDyinAFOWXtz2saMEvnsCuAUADuYFWKNDfY48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812709ce3.mp4?token=Rb7QqJC3Tca7BJLR6cVO6NV2tts8jw2RzE-xqbA8eSU-_wudALMTgP7WrGQgwRKLx93vFUW8KbSVSm2EA6LUbZC4beYsBGOdw_Eb5eTIIITMQMYHzmtVUDL3ecL8lhHGcmJZuP-0HXcCbU3VyOo_hvUtGtWgclXBpyA_Z1w-U0ilkZReIu9hw9SqkKlGAGKF7ShcLZzZeZ6yT3Rn7x8KPQu8Il-Gz2VZu345QA5M7zXER3i82yQTaSx3pj9WyGbMPTyWsaQbRGOYWhZjLZdtx0I6QXcdVUU6P9zkkQBdT4Ip-wRIaDyinAFOWXtz2saMEvnsCuAUADuYFWKNDfY48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره همرزم فرمانده شهید یگان فاتحین از آخرین دیدار با شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/435363" target="_blank">📅 17:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnsfQ-21nQGx4oVqdRRAgtfbKdt-wJRkYXNOkvUyGHfVQpxWqnR7p8IeinHqDYn4vkoKQnXfQMhfTsNA2Jv0Jk4ivBBqWlLbIk6_c_LxPSZa-ehK2R264Q5trnjOVypLmWeqi7O2b4cn9KfdxWFKxT-WVEPBR4TSOZJKEZAUgzlP772hzS2UJ-A_jPtAlTtoDCq2R-EQHn05W0-f55TPS6SbKSQhfalLQhrSMzuAP_8cgpM3AtUaHICoOXaqR2Ejt8g7Z7vAP1JxAgaFpVUisCvRXPzBoReFHmvk_o_WcgEX9JkZQf4kRSEdBDwkMtvCB5xrUVDcJpgmKgaBfJ5fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO3IRCWe0mpl_7-M-UfmPL0F_6ccfAOVTligy1cEamW_-RyX59Vf0ZLG55-zXpqniySbD8RKm5nqR76BwJ7fw-WjB4s7_2VZ0N3WkSXw-p2w6WxcFB6RcumXOz1-QQ_yhfu764BF3PiYN4A_AL6a4tfg5bZC0SE1mdcSjMMa9nnTGHemNAFRsF0cTnrwjlnfLXqfH3pSa1Ot01_mM7Ig2YkwZCWam0P_PmDpfok-A1WqiEJwrm-j1Qhzdh3lIlIQOhjNE0wVu2UPzt1WNVDOx4sHgkckxdQoR4v7-LiPSCDimgHToXeZ3NB6HGE53agNXXsyIrmx-b8ijrKoIOtong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmQe3xul7Vk87gXQtjxbX4UJsiU--IizsTRwfmnSLW7C-8BX1Z5pYR3B6y7abajYo0KD8hyHdO1BOUfy5R-MQiTCHl2Lijb3RR2pAc7W7Jv0tz35Thxa2q3OhNRK8xncWpsbWYu3SazTFkNbABUXWSOeplHuXE8lYSwvzbwVtNsWKslpaqP3EKHCx1L5Mea7X-Weru_CsSMSOgQqSFSYNAYufOZIt-76mq1HcZ__4IxO6H7GV0fSW1dhP_M31zxCF6m7k1-bZcN1rvx8lSuJgIj-C-w7z-bLi6e4Ivw_zJsIWJjrMi28u1DvwYw_kfCfG_Z0CyRBYWRIArcVxeo9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AelfQai14Ze5c9lZCBDY5p6p0OSgLyvTtsiWI-ceq5cLg1Se4YaiTkre52n1HhUTtHgoF9oIC6UN_CeTN5I5Nz0d76gwYJ5f7ewSNg6g6hD26I6hxjQFnlWJFN2nsPjJ8oxQX3GuNg3LLSDIuU5vEbzJH6Hm3bpUnmNGIrEAMmyqEnuCu4Lad3h_91u00Vc4x-mIe6ElUK_b9QST91vCWJaXt6bMZr_MDIoo1mdccoEgM1e-DZyG7mej_b89f86HNWXrm4pWqtbBOpPK-KfZu2Mcjp71bneUuUficYJ2DYSIHmFgXPoaNxYLzLvp8KcPgR32wUWO3UqLjOn0CyY-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9lt9lzDCZizHgrcpLOJPp9-qlCP5YcFNwSTEHkmBWJuLXTQyxR5KkAklBz03xJVwj2H7YH8EWSuf37CB3xKKd-3VA1rwXuXrcJPGWagdIdDf-oQtlkiepkSrEI5y1xceaposRj1M2U--4hpnm2C-x9DX-_3RKuedSob8SzvoTqAb2pd-pXud_UWvILTaJ16FjmlHIjC_B8oCpUVnOSvDyKhlWDKZTrEMeD3u7Idb-LAOUb_bmx02NZJUIjnj1GfLn5w6C7JRjIxRPV0eHd8iz7bV6Xo6cboDsN-e1IOdkDwZb24ll2P6rLO0l1NVgakawvd4btd5Dvg7sLWTyOx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvrKA4vxYoZfz-ArRrsGsXYu3KmXWKPzDQJBN23MS0JMVBZWrwd8bUpETJbRVKbs5nAtZkHZHvCJYdQAimiPwhtuzoTEEeh8pV_KNQ9H6JYPH4XVjfSYDemmalNAX5dXqh_H9--AIze13AtAgMd8KANfLQDaaqUp-xpy_O7mjUWmbFal3MzRKh9WOOGUIj-lYai5x7NALArkeAztb8ZO4_a4EJsaHqk0_FrQpBy7ii6rQsQsA4k24z3TBfGXY9lu06EBRhxD1DLgqXoFGfG5mVMv9lQUWwWFS7c-X_lbg9-2N_oDdAJrv6Jj6sv29Nw5b8r2TWgFhz77Tkm0UMPHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk9nS7-f1HKkQjR7f5re_i5GNiBEzwqixnmMt_BnVbe47kqeZMTygwaUI_B88Cyy5OZ-U2u-dC53D_bme2hIoPqnivUmpy9iqni8UA_cch2tcUrDrrBebprR_9hJSkCxqI30DSFfkQ7mbcBR9FUhx0VW8hgxh3lsNBwPvouougc-bjQ49PJNLUl0yl05xrjY7-iIatzDsdgCSIa0iHOjg6hEuEx5yna0jdykQHJH4I0WUCsdDSVh28Izct0BpweDFUBdy5QpimY8PbCtN-HT0mWDzmR9u3ug6L3X3b6YmrH6R9P7fq2QmZiLXsoOtu8IwERJ5dzN0yF24o-_QCQM6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سلام شهید؛ آئین گرامیداشت شهدای جنگ رمضان
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/435356" target="_blank">📅 17:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYJSudKGM_psCpMmW9308MDIqOgkLeC1JR_eAu9AmdQe_wHsmVVws18_XieJUsWbchNGW1CSIuW50nI6Slva4QhoDLa3ZuqmcOcNtbIwSrtZ6niQd3PS5EJNZ9ML4YHA5Sk-nZps_YJSYE6YXtdrYd4frWLIYx740YbzSBic5RmynDNCIbqpqvX1UBVdKjITuzQy4GdKNJDiyTY4W3A29Sw7ZCk-pFd0Fa2NTXv_I5QVFzl9olCDiLBnJ9IHSjg80J8rcyxEDAm1253pJ4yr5dLS4PGv9ONQuwaoSmV5DiK3-i3NYX6XQV82Ok_7uN9nmvsHxW5O4ZBqpwSa-3QUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر آب سدهای کشور به ۶۵ درصد رسید
🔹
طبق جدیدترین آمارهای وزارت نیرو، میزان پر شدگی سدهای کشور در حال حاضر به ۶۵ درصد رسیده و حجم آب موجود سدها نسبت به سال گذشته ۲۴ درصد افزایش دارد.
🔹
با این حال در مناطق پرجمعیت مانند تهران، البرز، مشهد، خراسان‌شمالی و مرکزی همچنان باید رعایت مدیریت آب و صرفه‌جویی در دستور کار قرار گیرد تا از شرایط کم‌آبی در تابستان بتوانیم به سلامت عبور کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/435355" target="_blank">📅 17:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7JwZTSRdVxAhsImnB8UPyPdASfnu2i7EHB03FNkbjEm7qQcCU3OsS8E8Hf7szbkYB-HbqtpLCfQfi69-I7ZGxz9fIeUv8Tx2h7raLuSarW95n3uP-AARVtA_DQm8XiG1vaOtlFAD5YBPGadYwwxkTYq11qb5N4i0TXISivLwGZgRMRl4i-IN-kKHJoJYvaRjUtNufXLlclxZU-ag6WP6n54FvPeJIQCMNQZHpBNsIOffyGaIDSmWBMirL40jk5ZXuYGmXuH-nh4cWz4hxetVfrbxwsMvS30Hs-_s_beMuRbG_LjLIgPORZ40zM5igMO1Schq0k41tqPwhzJtMo2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمزگانی‌ها روزانه به ۱۵ کشتی در تنگهٔ هرمز خدمات می‌دهند
🔹
به گفتهٔ مسئولان بنادر و دریانوردی هرمزگان با همکاری مردم محلی روزانه به ۱۰ تا ۱۵ کشتی معطل‌مانده در تنگهٔ هرمز خدمات‌رسانی متنوع می‌شود.
🔹
این خدمات شامل تامین آب، سوخت، نیازهای درمانی و دارویی، نیازهای فنی و تعمیراتی سیار و... است.
🔹
۴ لنگرگاه در منطقهٔ پیرامونی بندرعباس و قشم وجود دارد که زیر نظر سازمان بنادر و دریانوردی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farsna/435354" target="_blank">📅 17:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331e0b7936.mp4?token=CAxlv0fqr6nC7xl60bv2boyyutl3jIyCrdRIq2foINJw1RFt7shA0J3PoUQiltLJbOQR5ol9STBDdILRJ6j9YKSIPB_g-Yhy0vgU4fZTBqNSCZrKA-nhw6srsJNFY4VXvk2uK14hBOi4xP579s2YgvfZJCv2kZnmvnIbP2G3ZE2MUYosVG8NSWFdYZSI_PSFGLbTb2cN1dou5s-D9cJv2clgiIHHBr1V4Zy8skwqhcncJHwE6HoR3VuHgluNiw8OxWO6SdKU7g8UF_qHlOGAm9V-OyD-qBXoOv2Gkdew2k1aUXBmXRl4kbDoKlaWRcbX1K549WkTdGwrE4-Esd8CbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331e0b7936.mp4?token=CAxlv0fqr6nC7xl60bv2boyyutl3jIyCrdRIq2foINJw1RFt7shA0J3PoUQiltLJbOQR5ol9STBDdILRJ6j9YKSIPB_g-Yhy0vgU4fZTBqNSCZrKA-nhw6srsJNFY4VXvk2uK14hBOi4xP579s2YgvfZJCv2kZnmvnIbP2G3ZE2MUYosVG8NSWFdYZSI_PSFGLbTb2cN1dou5s-D9cJv2clgiIHHBr1V4Zy8skwqhcncJHwE6HoR3VuHgluNiw8OxWO6SdKU7g8UF_qHlOGAm9V-OyD-qBXoOv2Gkdew2k1aUXBmXRl4kbDoKlaWRcbX1K549WkTdGwrE4-Esd8CbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تشخیص پیکرهای تکه‌تکه‌شدهٔ کودکان میناب توسط مادرانشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/435353" target="_blank">📅 16:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJOYjoN48jZWtyS0qJ4cCQCvlzGS71E1zgwMDtF1zRxMHpnWZT8_mtsS2wBwzZOnkMcoQNmH_ZSnzZT74PzSc8DwxvZ7ayknwYv6UDmtl6O5CGQ7K5pBjWIlcTekfwC6sm9bAjFR9uFMDSjiWiqOdogIT8iovieytwZVxdPvPJoweJTo4gYuM5GJpP8Ra3nInL_QLGoYOU9F97MGVoWvi2b5lRqcD1AOvysAdIB7RCYKX3EjCmeY4c34uSKfNaOPZ0Qn3fXGEHqmlZKmfo6az-IOmQNhIzsNS6blaMV-MX5-KD7gqLOiWXkowfVQ7GxFxs4eRpdvMzftCMKj_sB9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgBdRXFc_UebOQS6nC0sVRPN54Yq0STNTeNKA1r5CDqHjKQFRDjot5KetIQFqTrLboXS7js0qFLWugvI6ENMSdMWzx-A7Br_Q1DeIfkIB5PVgz6K5ZyEAxgVrlVm_tM8HsBzC69m8Rk1nIxE21JiTqehllawlCEgF0VYjq_4k3i7l-Deow67Kom0ZLTfbSTTqBESZMFKgeKyBUCnr8vD2MRciyRjEseIjlBy8XET6rOjN3FXDmqWK1baLmHTTRlv9Q8ng7Pa8VO40hc6uHzUckLTBdeiWid9LLfKduruOfgty2j2wSjiJoihdJzZI4BM5iOmP-oj3w4kVZ4oadEgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9r9oPNCIbt2PXeDB1c7-MvHO7eOnf-67UZhJY6FCo2rF9eTzSwf4Y_4OfRs7jKN9IJPv_5Ne9pbb3u9qBGIHWmCar1Fvqdg56bQjlS4Tzf9axQIM7TAm4c1TFQOyuRAXYxrjjvxg21I7c05Puu7gH0C2DKF6Sr3SAH2dUzoMRPKVNVXNkFA8AWlQdiY-qMtCzQkHfgAv6SL_KH_1LdGJv0hp0R683Va6CfYu1VC3F65nEVTzGT3guKp_hGOtDs9bXznYl5tUgiukia83ra-OFd0me8Izlj6cVhedy5Xobpc0zIEICwUb-4RzQAZ02qkG0QL1XZDiolJ2OQbU5AzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqk_0Lmzs-J1PunKEqzySKGZdvoBFFexOkwdNTBglhhixg6AtdTwxB7HfPOwjgjCvNxrJmeNvHqge8QZ7CFOzpAHIyZ7aFBC4ProP1E1XoJJP-euwx5iSyobxiVIGCjvfvnh2kzQsiSexJf1T79izKluLVdKoz_utmW-87vZdoCQhrlyHKAqt4XlQTrmY5EsAnR9Z5GKpo1_zw--FHum6V-a7wo8WUmsjvYHzIE5zSvpVjUlgL0mn45WbPDbNvwkjjTc0rXAD4Fr0bTtllgbFcic-KC6-1BUllQiBPq9y5xb-XWVf83kSR3PuwgafThw2Mr0ddIX90Glj1EKpFn-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDhomIRnu3ovdOeQPs60TEfgQyPctlVsg6rJsPlUzS2895wFZcWPVS8c6c9pY81npIbQW16E-Y1CVWwqI9JrEM5MzeVgjOXix4VosCmxQPyTiSiQHuI_q8YevIXzGMkAunP82DqsZbGMB85j4DvBOm79dB3XpAGBknjOYLopzL3bI0dJal60GBDJSZoQgwkp8RSJkvFLKzvuiOK2kEXo6ib1gHnUZp09JB-4AtcoXY80X506-lND19tFzkxY7Vx0eqA0d9RTMCeDuKEU8tsQYRGxFnUNl6b-_0pPgm0QVoT_P9hUCRkN4uH5GJ2PV75QVAExrP-atFCm-DD06oiV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/subLx05rcjrmASf-WWDj4EWg9ufpQusnkyXUniLdgs5bLOQRmpr8AfB6wD1XD_WwnFsBxxWFvgi9uB4G8CQjJboGz3iHXoiBgkC_TDu7iTAxUpcZseDEJ-bT43zE-usy-5vnjK_etNwrnTJ6Zz3UEqWC_hi-816FIstzO23W4MoaydvpQTrxGc0WFGk0ckBz2D8ZG1vXg-FMZSCdtPrXap2w60DMg-zwv6WPvTfwonlPekMFKeTirVv-9kpZxeBJELcDbBryb6_Y0xV_vc8dNCPLYI-Hxy6IZ-Cm1RHDg5Zy2_pfGFAjtqO9o2-Fu3n1b5yqMLCHGFPIu6opypFEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r23x5l8GWwVjM22moy-I-tRMgcUGKjVz4_43HGXjdxoU5_jKK6jxcY-lHZArXiUUgdBD8d80INOOlEubF_bp7V7m-1enJtsJzrwLnXPQ1Yre5MPvhNzbxfz0M1GbvyT7Nzr3dagqPTK8BWKbmTZJpW6b5SBztlDrNmI1wPDGpGCqZGtgm1y9xkv7B3Eb4c6Iaf-1vkXLJU4mIRnlOhgNpBHWH-4faADjIghBeGQhGI9svua-acdhOtzywmlDXkkTp_7Vt-lRzOe-rW0LoJlfiKOkpKuOgRyRKaxYImLffn-MxNQPmgF1bPeMRXhCAkVL-aijGZ6BnlyYr2qClbb2NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری هفتمین نمایشگاه مجازی کتاب تهران
🔹
نشست خبری هفتمین دوره نمایشگاه مجازی کتاب تهران امروز با حضور قائم‌مقام نمایشگاه کتاب تهران در خانه کتاب برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/435346" target="_blank">📅 16:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9393913bb.mp4?token=R12u27Y-bTiGVpHuc3LAXDUfoQ2qJLbDYmJwNbklf3ft_hwLhfmm-haITaf1KgpvUahQM5GcI4AtQ46hsVHCbwvzlEcNEPbO6mQ7N1fx08g7iL6-ouRl87ba8moboamyhj89yxumeY6HFVQPS0YDMQk3qWnKlL-Bzcm8C1QdAJVRMfmVUgwnG6qw3IDQ2Wg7KCPjgMHYaNd1CDxTLoItP4olnB4Qmg-B00Iw2OjqhouQ5i_knH3vGLmKnnCcEwqtfDlF3QhpfanVUz9WmXZrhQv4VRUNx5PtGbwMZadAq1y0ecjWC5vBfL3YxIYYc8sdCOZ_lFxFBzBNdxNQcdTiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9393913bb.mp4?token=R12u27Y-bTiGVpHuc3LAXDUfoQ2qJLbDYmJwNbklf3ft_hwLhfmm-haITaf1KgpvUahQM5GcI4AtQ46hsVHCbwvzlEcNEPbO6mQ7N1fx08g7iL6-ouRl87ba8moboamyhj89yxumeY6HFVQPS0YDMQk3qWnKlL-Bzcm8C1QdAJVRMfmVUgwnG6qw3IDQ2Wg7KCPjgMHYaNd1CDxTLoItP4olnB4Qmg-B00Iw2OjqhouQ5i_knH3vGLmKnnCcEwqtfDlF3QhpfanVUz9WmXZrhQv4VRUNx5PtGbwMZadAq1y0ecjWC5vBfL3YxIYYc8sdCOZ_lFxFBzBNdxNQcdTiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ سلاح مهم شیطان که با آن بر مردم مسلط می‌شود
صحبت‌های شنیدنی حجت‌الاسلام رفیعی در برنامه سمت خدا
@Farsna</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/435345" target="_blank">📅 16:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV3rEMz4P8eZTf0Qzp84oOjecNJeAHLGZMF9nNn_JX2C_xgGKtfdnEOFCsCYIZa8UQJ5ET_dznPZnVgOyl4azX3JFH2cq-4OPivK_i3n_0uPEE8X-W4qFzGuNVLskytNkm3fwrNDSYl-wcP1YUZOsII-PrgTApL_AHynAgRxoctI-r8xTK3_iIFcS_Qz7cZl0wslSTFHoIKZphGCO_q6QnEkljnfVtxKBRX__lNmRvKF_T0Gk3flryY38b6PpXFhxa5KD4OywX_tM9ej-HSARQFPvhCE3GAfW4UIsIU8yAEe24MBMg3Wgo3rCwgJRvAhBxEaap4uFA2XcqyPnFrpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر نقشه انتخاباتی؛ حربه جمهوری‌خواهان برای فرار از شکست
🔹
جنگ ایران، جمهوری‌خواهان را در شرایط بسیار دشواری قرار داده و احتمال پیروزی آن‌ها در انتخابات میان‌دوره کنگره را کاهش داده است. اکنون آن‌ها در صدد هستند تا با «بازطراحی نقشه انتخاباتی»، ضعف کاهش محبوبیت در میان مردم آمریکا را پوشش دهند و بر دموکرات‌ها پیروز شوند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/435344" target="_blank">📅 16:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما از ایران سپاسگزاریم که به‌خاطر حمایت از حقوق ما در خاک، عزت و کرامت، سختی‌های بسیاری را به جان خریده است. @Farsna</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/435343" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435342">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: دشمن صهیونیست راهی جز ناامیدی، توقف تجاوز، عقب‌نشینی از خاک اشغال‌شدهٔ لبنان، آزادی اسرا و دست‌کشیدن از بهانه‌جویی برای جنگ نخواهد داشت.
🔸
دشمن با تجاوز و جنایت‌هایش نه به ثبات می‌رسد و نه آینده‌ای خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/435342" target="_blank">📅 16:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dae014c5c.mp4?token=C2WmbQpItF8rLtcCXexeFfnbtZEku6X_2LG6VSP_AfMEXJzOO83ctNkXSxj8-eRxRzgoOlvdnjeDVHuJDfmDDFq5rA4wjxEt7TU_21Spvmd4lwWi1hRwb1URcz0pqDKj7I9nRdVFwDlJL-s9uVriM5c9-vhNbbkUswlGSZWKJlyqhyOxK151xQ2n1KyCZUlJwhl0tJ6hnroeWyddYOVWoWT9R61l6l40bSZQmdlP4_9I1Yv2TPcKQ5fFltO4OREowgNu9SIZLXtvKC3bQkhQxVzsR_BwVjL9PJv5DnJoK6i68qFVer67xf8LvOWLYNQah1A-HMfGq9ugI3ttguoERg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dae014c5c.mp4?token=C2WmbQpItF8rLtcCXexeFfnbtZEku6X_2LG6VSP_AfMEXJzOO83ctNkXSxj8-eRxRzgoOlvdnjeDVHuJDfmDDFq5rA4wjxEt7TU_21Spvmd4lwWi1hRwb1URcz0pqDKj7I9nRdVFwDlJL-s9uVriM5c9-vhNbbkUswlGSZWKJlyqhyOxK151xQ2n1KyCZUlJwhl0tJ6hnroeWyddYOVWoWT9R61l6l40bSZQmdlP4_9I1Yv2TPcKQ5fFltO4OREowgNu9SIZLXtvKC3bQkhQxVzsR_BwVjL9PJv5DnJoK6i68qFVer67xf8LvOWLYNQah1A-HMfGq9ugI3ttguoERg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در سنای فیلیپین
🔹
همزمان با تشدید تنش‌ها بر سر دستگیری یک سناتور ارشد، صدای تیراندازی در داخل سنای فیلیپین شنیده شد.
🔹
شاهدان عینی از شنیده شدن صدای تیراندازی‌های متعدد خبر دادند که باعث شد روزنامه‌نگاران و دیگران به دنبال پناهگاه بگردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/435340" target="_blank">📅 16:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: دشمن صهیونیست راهی جز ناامیدی، توقف تجاوز، عقب‌نشینی از خاک اشغال‌شدهٔ لبنان، آزادی اسرا و دست‌کشیدن از بهانه‌جویی برای جنگ نخواهد داشت.
🔸
دشمن با تجاوز و جنایت‌هایش نه به ثبات می‌رسد و نه آینده‌ای خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/435339" target="_blank">📅 16:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_zHvZrm_WrYTYkPwFLsWgjWWMK75kWH0Ib1oNNKWEci54lbqC_W8K1uI4z-RV7IhCJqyLtaokZABSUgeDr_JHsnxeCD84Y7_vU_Ddhk6D6cYc27q2r2qRjDAeuERPTzV3Oaubj6-XlSPyqWpGy2IV1hRqG99txBIyaZ-zKnsJ4-WtSuRrINnSYyfhmiVLwWFHbcoqVfS1wfqS6aZvBsu86EVf5zS5_vI5kC8OjL8u-k7LbNb8ya5Yt5Eo0OTV3K-_yrNQg6LVScK86VTLXLbyWHnvUGBRsFp2YwAmao4jkt-CNAmmsrok6XzVsgzfqEW1z-MG2qLsLiesED6X5BEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم توقیف اموال باشگاه استقلال
🔹
ساعدی‌فر، مالک برند پوشاک ورزشی «مجید» به‌دلیل دریافت‌نکردن مطالبات خود از استقلال در زمان تولید لباس‌های این باشگاه، از آبی‌ها شکایت کرده و علاوه‌بر دریافت حکم دادگاه، دستور توقیف اموال را هم گرفته است.
🔹
همچنین طبق شنیده‌ها دسترسی به حساب‌های رسمی باشگاه با مشکل مواجه شده و مشخص نیست تراکنش مالی استقلال دقیقا از چه مسیری انجام می‌شود.
🔹
آخرین پیگیری‌ها نشان می‌دهد که باشگاه استقلال هنوز اقدامی برای پرداخت بدهی خود انجام نداده و همین موضوع باعث شده تا هر ماه حدود ۷۰۰ میلیون تومان جریمه به مطالبات ساعدی‌فر اضافه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/435338" target="_blank">📅 16:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB_Cgiz-6f4qk9qZvhYgXUGpuu1uFAfy4zjQlvjxSxwdwv8xWQM9VGUB9Hh3mLwN7RlQBBOZu3JhAJqDOiXgzLqN7jmkYmBZS6N9D9p-7Fqxe2WqO9Ab1YnAtrPeLEygaX4TOMnYakc9t1jSpkgRJ-fOQwabtQCKOYFdaqQ_pAnqT_bFmDx788aakZRe4KBjIpqliwp7a56uqRqDEp4rI6bZOUa9XFaUDNA2uuN1FZFHuGPwKgiG-KvFkjK2EhMdX1ue33AYKbyduWqhDRjGsc09xYBOomWsNsyJDLK_CxuY3VTxfx1hH8hIrsK61cGDGDhqUc2ZOtmySLM0qam4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: عراقچی برای شرکت در نشست وزرای خارجهٔ بریکس به هند سفر می‌کند.
🔸
نشست وزرای خارجهٔ کشورهای عضو بریکس پنجشنبه و جمعه در دهلی‌نو برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/435337" target="_blank">📅 16:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=kwVlSXKoGlC3DPHEF5V8KvVck7Gjr2-JPcm5muXi7bRR7eCmWpC733iXwpevfQWC07QWGE6seVph-G0encJpvXSzY2EM_8bwHCIzWnX05_GkKk6v8bbVPO6t5ihakSi7M_xvn0b6dxdrvmq_OlOnjVdXLwdL82CD6k8Dc4OOnCIkbor8WSQ7H9vxJdPVIl-IBc0KUkhPfq8_fuiZ1VK8nRgkmjioZM3_RrVXJcHqQ-2fpTtNp4wFXXmJ1_Q78BAFvzvQcuzm-SILV_HLjDIeWKZXkNK1qVWv30sC1L8S-TFAqmzRiZ_fufMsaMgcfMHKF9rtkaR0GMevklPL7zentw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09bfe31db3.mp4?token=kwVlSXKoGlC3DPHEF5V8KvVck7Gjr2-JPcm5muXi7bRR7eCmWpC733iXwpevfQWC07QWGE6seVph-G0encJpvXSzY2EM_8bwHCIzWnX05_GkKk6v8bbVPO6t5ihakSi7M_xvn0b6dxdrvmq_OlOnjVdXLwdL82CD6k8Dc4OOnCIkbor8WSQ7H9vxJdPVIl-IBc0KUkhPfq8_fuiZ1VK8nRgkmjioZM3_RrVXJcHqQ-2fpTtNp4wFXXmJ1_Q78BAFvzvQcuzm-SILV_HLjDIeWKZXkNK1qVWv30sC1L8S-TFAqmzRiZ_fufMsaMgcfMHKF9rtkaR0GMevklPL7zentw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی: امیدواریم ترامپ در چین موضوع پایان‌دادن به جنگ اوکراین را مطرح کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/435336" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a66b75.mp4?token=cUi8eskNfSH0zrZnUqmUeNVkOo5XH3bdALZb896_vfkk99vcLkJy66Zd06CULRnUUIBh7P9SYgJS0Mbm4ACB1ow7POLcQHeilcVcNT0TErymCATs3X7mmKJzwbtF7SEqA31dXt4VG9C9yJxozSpyQ1vGP7NaKbmoj_g2xHUuieDLkeGp-fFOmQE-Co_yLpHHEqZvHSFFNjYeyjVwoa-JNoe2JoytQqBDilcS0dhy7uXn7v1RKRueZFyx9aLM181BTaccn9UA2t_t65KxgjfVGnCyUFh2XjPNXsBLwVamY52XEX4VN_ND5dR1Bi1fhziHfe7uUmHV6iqwwb_g-40yiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a66b75.mp4?token=cUi8eskNfSH0zrZnUqmUeNVkOo5XH3bdALZb896_vfkk99vcLkJy66Zd06CULRnUUIBh7P9SYgJS0Mbm4ACB1ow7POLcQHeilcVcNT0TErymCATs3X7mmKJzwbtF7SEqA31dXt4VG9C9yJxozSpyQ1vGP7NaKbmoj_g2xHUuieDLkeGp-fFOmQE-Co_yLpHHEqZvHSFFNjYeyjVwoa-JNoe2JoytQqBDilcS0dhy7uXn7v1RKRueZFyx9aLM181BTaccn9UA2t_t65KxgjfVGnCyUFh2XjPNXsBLwVamY52XEX4VN_ND5dR1Bi1fhziHfe7uUmHV6iqwwb_g-40yiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ روش درآمدزایی از کابل‌های کف تنگهٔ هرمز
🔹
رئیس اندیشکده اقتصاد دانش‌بنیان در گفت‌وگو با فارس: کابل‌های فیبر نوری به‌عنوان کالایی ارزشمند از آب‌های ایران و عمان عبور می‌کنند.
🔹
تجربهٔ جهانی نشان می‌دهد کشورهای ساحلی از طریق شرکت‌های عبوردهنده، منابع درآمدی متنوعی از جمله مالیات، هزینه حفاظت از محیط زیست، گارد ساحلی، تعمیر و نگهداری کابل‌ها دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/435335" target="_blank">📅 16:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD2CQQgcAZ-rHFJza4AaezmmDa9xU5VVKzSFUgMwKACwClzyXgjG3F38XlifX-Cc5gySkZGgJBVZOXMXWM3P8dyGRQjfOlYuYU39QyIaEQMYTfvr94Wt0hSKNFXSRz0SkbawrCtbonHTLHdikZdJfvvP1dKyq2NVX6E-87ChVe0k_V3_zSv02-_V4DhYjrORpqvjGhH9rlA7YkqOIVuTrklm8yZ7ZR0GqWYNxhRHVNWSDhE7aw2v5tYXErRqz8x83V99q49N0CMU7h0EeHSX2sO2rP7aLR6D-FDhPYjrzI3qy-82mcC0RUxBf5VheAH6P1qQ-tjRCjtB7C5p7duJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیست و دومین نشست شورای عالی مدیران با حضور سرپرست و اعضای هیئت‌مدیره برگزار شد/تاکيد اسکندری بر توسعه بانکداری هوشمند و حمایت از تولید ملی در بانک صادرات ایران
بیست و دومین نشست شورای عالی مدیران بانک صادرات ایران با هدف بررسی شاخص‌های عملکردی سال ۱۴۰۴ و تشریح مهم‌ترین اهداف و راهکارها در مسیر توسعه خدمات مالی و بانکی برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/435334" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435331">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUVnlpRsEnAwRJ-0q13brkvVj67N3SR7ioUMjohiFxwRJ8bh9WW2io7vAt-jOg1-zQJYR95rw-BedH0fzPNvohollxYoJ7ndh0rge79a-PnypplR2VirUs54kde0BZlrkyMh-7yY6l2O0ze0ZIQhnK894EiWnDXLvvUveJ8sIPx6TknHdZ0LWHkFCM_2ECzki17Ae8V3Mn_yAwhQkk_tfoOnPIhaJwi3hy354JxejDLL7VoYCi9R-wgA25rkwGlL_38q5N2xP6eWTp6ESR2cbI4k6kmzvzglIZXVBZWYHjsZVyvxKFogA3cqgkIK_I14iDvbO58vgN0zenG2_mHdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIclVuG8Tgz49SnDQOtFVH72POFmZkycgMXu4qxTklgKSsX5civhvyDU7jC4NBOZ2VtJlLyBbDOs0F2Hly410fa9CW0PPBhLKsuhcyVoRaIcWLRazYj48fjtqMZIFznGr00BSho-BMr53F6BA2AuL8W3CfWZ2qeM89PHNrEu4je-Y5vvD4OV5C3zRMacVFHD5pduSmn6qinSQqAEtrnIm7IBtCg8jVbArQvXdjlLyCKMlaVBtiF1y6f4sn2xOiQCt2dSGxbPEcM3CRCYGhpzV074q_-TpW5yfBzFBgKL73Hi_ihOl-fzbFhvyVrVLLCR9uN8p9a_Ceadf4nqdujXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTbFP46ozcNqMKW8IQdi_R96FwSFjnFGSyPjSag-iCgGH9-ZBr9eoMc-EvkNfp5UET2PAM_UBLexw_EThxQ3fN_DLcPQA5C7VGud4kDzh5C8b4i-AiSnGnB2xTwWabeXm_NJ1wxb8SoeJdboMMToniAvribgvhg0RxEW6WjIwYPka5ELRNx6OeDsfclOOyTZpaDB3cX2qF_6x8gtpOB983Wc2llvZbiriOyspeJfdrV-VqudL68sE5GtFIkBr6iyPFPwwxnCvR57RtMMX_rmiqo1Tzi1RGUUA54YvDwaFOzuAEJmF2WkysT4DshWI9rk2LbJPJ8Iyb3Xl6DwfRjU2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
رونمایی رسانه مس ایران با حضور وزیر صمت؛
🔰
«عصر مس»؛ روایت آغاز شد
🔻
شماره نخستِ دوره تازه مجله الکترونیک «عصر مس» با حضور وزیر صنعت، معدن و تجارت، مدیرعامل شرکت ملی صنایع مس ایران و جمعی از مسئولان کشور، رونمایی شد؛ رسانه‌ای روایی و چندرسانه‌ای که با نگاهی تازه، روایت صنعت مس ایران را بازخوانی می‌کند.
🔹
آیین رونماییِ نخستین شماره دوره تازه مجله الکترونیک «عصر مس»، امروز ۲۱اردیبهشت‌ماه در حاشیه افتتاح نمایشگاه «معدن و معنا» و با حضور سیدمحمد اتابک وزیر صنعت، معدن و تجارت، دکتر سیدمصطفی فیض مدیرعامل شرکت ملی صنایع مس ایران و جمعی از مدیران و مسئولان برگزار شد.
🔹
«عصر مس» در دوره تازه خود با رویکردی نو در روایت‌گری رسانه‌ای، می‌کوشد تصویری زنده‌تر و عمیق‌تر از صنعت مس ایران ارائه دهد.
ادامه خبر در مس‌پرس
👇
👇
👇
https://mespress.ir/x6QG
◀️
شماره نخست دوره تازه مجله الکترونیک «عصر مس» را ازطریق لینک زیر دریافت کنید:
https://media.mespress.ir/d/2026/05/11/0/15374.pdf?ts=1778489262000
@mespress_ir</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/435331" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435330">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/435330" target="_blank">📅 16:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435329">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYdsSYVogPPVTF2Ro57rTOSTgVwB0vj4IvHSLz6mBa_RUHfrYWOgtM5oxiIzBh_ZGjLggLfMCt4o-MzE8blBHKc0XC83RAsCt45qY9EDhYLbmFDvyJhLFMYz-rdDDDjsvbd9o7HW-jyAdcCRGUvR05xS8ogolQrFGg3lQsTpDf8h3w5BvALGNwxxO8BicwysMavIkIJDIWC3BajAiy_pJQKXwIbfGGB_I_k1McQ-pMypbDi0wGFhNEE7raOnltT-rJUCZ_90zXFTfr5WjvALtZJ1QmziqwjvZtuxHLNwqgXbj4vEKEyALDnIHXiJWpDGyntQ8HAmsLw1TCq_rZkm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش از ۴۰۰ تن برنج احتکارشده در مازندران
🔹
فرمانده انتظامی مازندران: درپی بازرسی از یک انبار در بابل، بیش از ۴۰۸ تُن برنج احتکارشده به ارزش تقریبی ۱۴۷ میلیارد تومان کشف و یک متهم دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/435329" target="_blank">📅 15:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435328">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoTdt1rbOqwbIBIiqlRnjs9FDxsxSwgIDeNBFmBS1839ubaLeIElmD6mHheaxaw_XL-kko1fFwNdVAhwvFJ6FX1BKMssE6kllqbsB7mzompySLvvwaTcXz_7T2AGMmo2ovFxSEQQoiBuY00UVfVYrhZ3rQ877Th2iqHE7haxUB7V5OyjHaK4OkNB9h1iVlfnjDWXyvLuGRguPFgDjGzn1vBzIgSUoH6ELs4NQ8wqohO8FFEuFrersOWhmKEPF4BahohrEvANJs2dZsGWDkCSIg5i3sl-RmRB-mMTQ8NrNYYRudA0apvluDEsvet3ZCS4_FrP7fezHqNeGPQes0rQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حبس پول توسط بانک‌ها صدای وزارت صمت را هم درآورد
🔹
با وجود اینکه بانک‌ها بزرگترین دارندگان پول و دارایی در ایران هستند، اما عمکلرد سلیقه‌ای در تخصیص منابع و استفاده برای خرید ملک و تامین مالی شرکت‌های زیرمجموعهٔ خود، بسیاری از مردم را شاکی کرده است.
🔹
کسب اطلاع فارس نشان می‌دهد، حتی بانک‌ها برای بازسازی خسارات جنگ نیز ورود جدی نخواهند داشت. یک مقام در وزارت صمت می‌گوید که «امیدی به بانک‌ها برای تامین مالی بازسازی‌ها نداریم.»
🔹
بانک‌ها در شرایط جنگی هیچ وامی حتی وام‌های خرد ازدواج و فرزندآوری را پرداخت نمی‌کردند؛ با این حال در همان زمان برای عدم بازپرداخت اقساط جریمه هم گرفته بودند که با پیگیری‌ نهادهای بالادستی قرار است به حساب مشتریان بازگردانند.
🔹
ضعف نظارت بانک مرکزی و غلبهٔ نگاه بنگاه‌داری به بانکداری در بانک‌ها منابع بانک‌ها را به‌سمت فعالیت‌های غیرمولد سوق داده است.
🔹
تخصصی‌کردن بانک‌ها و تقسیم‌بندی آن‌ها به توسعه‌ای، تجاری، تخصصی، جامع، قرض‌الحسنه و پس‌انداز مسکن و نیز کاهش محدودیت در کنترل ترازنامه برای بانک‌هایی که در پروژه‌های تولیدی مشارکت کنند، از جمله راهکارهای بانک مرکزی برای خروج بانک‌ها از بنگاه‌داری و هدایت منابع به‌سمت تولید است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/435328" target="_blank">📅 15:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435327">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کشف ۳ بمب انفجاری از یک تیم تروریستی
🔹
فرمانده مرزبانی فراجا: با هوشیاری مرزبانان در کنترل و مراقبت از مرزهای کشور، ۶۶۷ کیلوگرم انواع مواد مخدر به همراه ۴ قبضه سلاح و ۳ بمب انفجاری از قاچاقچیان قبل از ورود به کشور کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/435327" target="_blank">📅 15:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435326">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa69c5177b.mp4?token=srq8EdBMOVRLiLKBJ271O3ucbEz4aZTFsV1FZK5ebo0R9aNPE1j2qdH_amiQI20lP6iLM8wWbZcSEuJcguDaXDDu3kUnVTjPT2L5tkogcgrFbL98MBEg2Fua0P-OLLlB6gYbWj393D-R-LZ56vBuB5guBCtSl7CkEBeXHfp-L59CtUGw7u9wgxzQK7uLFhQ7MZEq4xaiajoerwjCRX3EW6Ej47pSYmLas8uxqnAaSKJ5l9t3uB2Mep06uL7gHHsR3hgVQfPy293MWiEMWapbCWNCZtEKc_tuVIQE32M-TAvAHA9dIU9RJ9pHW8VLHB9QpkiL1k9hMt2oI_m3OgIGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa69c5177b.mp4?token=srq8EdBMOVRLiLKBJ271O3ucbEz4aZTFsV1FZK5ebo0R9aNPE1j2qdH_amiQI20lP6iLM8wWbZcSEuJcguDaXDDu3kUnVTjPT2L5tkogcgrFbL98MBEg2Fua0P-OLLlB6gYbWj393D-R-LZ56vBuB5guBCtSl7CkEBeXHfp-L59CtUGw7u9wgxzQK7uLFhQ7MZEq4xaiajoerwjCRX3EW6Ej47pSYmLas8uxqnAaSKJ5l9t3uB2Mep06uL7gHHsR3hgVQfPy293MWiEMWapbCWNCZtEKc_tuVIQE32M-TAvAHA9dIU9RJ9pHW8VLHB9QpkiL1k9hMt2oI_m3OgIGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستور کار ترامپ در سفر به چین؛ ایران محور اصلی
🔹
بلومبرگ گزارش داد که ترامپ قصد دارد در سفر به چین، شی جین‌پینگ را در ارتباط با فروش تسلیحات و خرید نفت از ایران تحت فشار قرار دهد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/435326" target="_blank">📅 15:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435325">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0EMtyDDNqm5aDAh8Xys5MUAhr1u0XGndPIP9ABhNdMXrkxzZ7VKwx6il4FzgQfgN0o7US1h8DJEfVDPCxXBoWwz4DMbi6iLnFoJEspneRCLq67dY9uJJBrRYeLJ3uYqA_doRvtBcmfUQz10vIJpLbxtzolIO9eqMS5BB1NWlW6wg_QDm24K4J3yo4SNAiF2RhgpfmuS0eCCYV5B7D5pJQ1eieS9iSi6CkqNnNM3nCIfQTHhgTVT4wKEJgKSftecCCvF0eZkQ224kdekNX0C34kk8aCNBJ_bTrNCoxYYgyScf4_7sewkSae61tJ9vAIYIsmyY1e59sFNBxEd02Vchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها معادل ۲ سد لتیان آب پس‌انداز کردند
🔹
کاهش ۲۵ لیتری سرانه مصرف روزانه آب توسط ۱۵ میلیون شهروند تهرانی در سال گذشته، به صرفه‌جویی ۱۳۶ میلیون مترمکعبی در پایتخت منجر شد؛ این رقم معادل ۲ برابر ظرفیت مخزن ۷۰ میلیون مترمکعبی سد لتیان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/435325" target="_blank">📅 15:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzgh8DHLI9kwJ1Jy4Ilm0WEdFgP02S-OfDxvXvrAf6S6uSLo9HtIz2UTyymaZO8A_crrOBGvNaLHW8KS94qlk1F33grOSJOwkFIWiy35n4MdLrFeFnCxktCGBxxgeff2ZXKCoIUm3pxEJauNDdOnETm1fcN6ijHeix7lcGLIE1BKZvWD4aFSikYteXW2ZlEzxbidciIvRblqqXiwfYhqbi_itSo-v6XouhyRcLWhBDUemmTt-p0SrxhmNdHtoMfj9p9ODcXpzoHNgZVe7f9_M6DUkYFimJ7S0r5-jUbRuKQRV-qwGT-pJaLLScrjmiHxhhKlRIS9D4icEm_TAmIuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اپوزیسیون اسرائیل: روند انحلال کنست را آغاز می‌کنیم
🔹
یائیر لاپید در شبکه ایکس نوشت: «با همکاری سایر جناح‌های اپوزیسیون، اخیراً تمام لوایح پیشنهادی را از دستورکار کنست (پارلمان رژیم اشغالگر) خارج کرده‌ایم. در غیاب اکثریت، ائتلاف قادر به تصویب حتی قوانین خود نیست. این وضعیت کنستِ در حال فروپاشی است.
🔹
همانطور که این هفته ذکر کردم، کنست از کار افتاده است و ما از هفته آینده روند انحلال آن را آغاز خواهیم کرد و در مسیر اصلاح اسرائیل گام برخواهیم داشت.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435324" target="_blank">📅 15:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435323">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsxR7Dv_QdIX4Lj0i2fxHd_nZRWKiVeRXz3LiuT1ndSWwwY3e4C5CX9OV9xPpSNrl_b1V6yZBpHEgvukr6cDh_x1_0ED_5pYwLYBg0g863L_dwmhU1qz1SOnaax9NlSha9O5m_L1RhIK2cbapamYeDIN_oF_1F7XvEwi_3hiHe_R9C7EEboX8f8KSEAnD3miS-jVhwnMkn1vUiTmJgNIvEZoXQ_pb0CthkUlmGByouGyV2L0hdEJYl7_VxEXeGaGtvbFx-bIQnX_JxaDCuTBSIGEaG7ax9qXF-2gJfKUOOb2sep2YOQ8d8dY1o5jJpVVv_oAlF-GtBXpnWZr0KcP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ بسته‌های چیپس ژاپنی از بسته‌بودن تنگهٔ هرمز پرید
🔹
شرکت Calbee ژاپن که تولیدکنندهٔ چیپس سیب‌زمینی و غلات است، اعلام کرد که به‌دلیل کاهش موجودی جوهرهای رنگی که پس‌از جنگ ایران ایجاد شده، بسته‌بندی محصولاتش را به سیاه و سفید تغییر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/435323" target="_blank">📅 15:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBcoMw3kRtirfledOj-woaFErvrpLSl3Cl-3SprfV6n9RRjmJ04g3C-Pa0dy1A1FEegeg2U6x7Q8ZjBLzDVvhDrqzFxTboyWEnl7TgNamIVReclzB3JZ6vpVI-KWelhzqCIn71EjLV4rgp9btuzGUTZ9YuoCQ3AeMJCE8Kpc0qaLmJcXf1ZYNq--YpKP6x_LdOE93EZsxXWRg90-2hF-PLyUfbwTRfIwWdqUz_x71uzcrP3afynvY6jGtgUS4w2jB489KwqQXDXAzLOSP4ubOd2oQuCiNAPUk9MgkLumddegN4cZdNdYaT-ouJaZbbh4e7vz23IjcG4v9R8yJfgbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز روزانه ۱۵ میلیون بشکه نفت جهان را کم کرد
🔹
جدیدترین داده‌های بین‌المللی نشان می‌دهد حجم تولید ناخواسته متوقف‌شده نفت جهان با جهشی چشمگیر از ۱۲.۹ میلیون بشکه در روز در ماه مارس به ۱۵.۸ میلیون بشکه در آوریل افزایش یافته است.
🔸
این آمار که از پایگاه‌های معتبر انرژی گردآوری شده، بیانگر تأثیر عمیق درگیری‌های اخیر در منطقهٔ خلیج فارس بر بازارهای جهانی انرژی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435322" target="_blank">📅 15:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN0f51ETNAqu145wUoaNpPPSgO7F0xfZXOzrp6JKMgZs5Lfy_SMAtROpV-HGxL-K41ZdMnR1zm30f5ZtWxrWxZLLe3zqD4HhsPX1Inixqc-iVff-H-5-YsM4fLHPDx-TMe6OztHvfFN0uwVHV5bPywsQpG838y4aYQ4xAmAf88bdjyyZlskadqqJaZwtLF8NRnvmY10BViNl4225YLgORHou0_jd8leDDpwgDfQiBdfRycpxg_ZmY8y1sUBZ4wrZTK7uwOc5IIpszMO9KLqHQGFidiLYn3godyeCvch6-FRz7v17jPVeWzgOUEJwALXz4_WbsCTtIlcTL4xvaCHpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بازروایی انیمیشنی از رسوایی پدافند آمریکا در مقابل جنگنده ایرانی و طرح یک پرسش؛ چه رسوایی‌های دیگری همچنان افشا نشده‌اند؟
🔹
ویدئوی منتشر شده توسط شبکه راشا تودی داستان تحقیر پدافند چندلایه پایگاه آمریکا در کویت در مقابل جنگنده اف-۵ ایرانی را که روز شنبه…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/435321" target="_blank">📅 14:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852c5d7e70.mp4?token=jmlI-9lzbqq6lifI86S7nxQA_b1LruVKDilR-DRm4b10XGfnfZeIgls6gGRZ-dgff-_N6CVCEt4tJpckgI7XuT6ZJiH-rL2ONT542a6FDw0PpT7LFj-sDRFWJa5-l4fnk_6sYeDGAnVmZ5buCHuOVIFec2-LLyiLypBNTM9OlBcEePlPFqTGU-AYHBwCQHbgolOgTBDP13rLkX_U5eEuiyiD5loQ9HSsFq_NewrAHPAm9C4e5tJNvkrvSguJnjkLSZ2j6WJR2HlEwR96K6jgmt2BDFfPBDnYy6Oiu8Xk2p6eK5nvnmQ7Z7Ko3Mclzv_yTfkQnGhwWOqYrfg4WFuAvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852c5d7e70.mp4?token=jmlI-9lzbqq6lifI86S7nxQA_b1LruVKDilR-DRm4b10XGfnfZeIgls6gGRZ-dgff-_N6CVCEt4tJpckgI7XuT6ZJiH-rL2ONT542a6FDw0PpT7LFj-sDRFWJa5-l4fnk_6sYeDGAnVmZ5buCHuOVIFec2-LLyiLypBNTM9OlBcEePlPFqTGU-AYHBwCQHbgolOgTBDP13rLkX_U5eEuiyiD5loQ9HSsFq_NewrAHPAm9C4e5tJNvkrvSguJnjkLSZ2j6WJR2HlEwR96K6jgmt2BDFfPBDnYy6Oiu8Xk2p6eK5nvnmQ7Z7Ko3Mclzv_yTfkQnGhwWOqYrfg4WFuAvjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش سپاه تهران بزرگ با رمز «لبیک یا خامنه‌ای» برگزار شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/435320" target="_blank">📅 14:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3hP3dpNgqn1402_TMuY41pLbk7WxevDVEtZiK8YMBtbcb7G5UxRlFYJYwUq9MOND1tT9pGm8uKyQRfPA23BkB6ClHCjGTT2pBMFOWK4zSxul4HuwMDpTLG4O5wzLKJYILDhx_4OoeaSjwnHDhPz8fpb7UZ6qr_3oWDyXxgz8LfuMBHnfqBghCzMo01CywoXwp0j36Kx1cQC55WsA3dJQIQuT4xe6RpzvT6F7yvTlwxOmBT57GoULVQCLcyB1ZRbeRFpsQxRYHHgZNJz2feBRXLUAX5hBsAf6OfJloslpTBhLSI6BdFmHAwM6ziQ6XZ5e779FA7dNzNjrRTrhlyuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای سفر مخفیانهٔ رئیس موساد به امارات
🔹
وال‌استریت‌ژورنال به نقل از منابع آگاه گزارش کرد که بارنیا، رئیس موساد، در زمان جنگ علیه ایران، دست‌کم دو بار برای هماهنگی عملیات‌ها علیه ایران به امارات سفر کرده است.
🔹
براساس این گزارش، هدف از دیدارهای بارنیا، همگام‌سازی تبادل اطلاعات و برنامه‌ریزی تهاجم علیه ایران بوده است.
🔹
وال‌استریت‌ژرونال همچنین گزارش کرده که «نقش ابوظبی در جنگ با ایران فراتر از هماهنگی اطلاعاتی بود» و فاش کرد که «امارات به‌طور مخفیانه حملات نظامی مستقلی را علیه ایران انجام داده و تنها کشوری به‌جز آمریکا و اسرائیل است که دست به چنین اقدامی زده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435319" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جادهٔ چالوس یک‌طرفه شد
🔹
پلیس‌راه البرز: به دلیل ایجاد ترافیک سنگین در جادهٔ چالوس و آزادراه تهران–شمال، تردد تمامی وسایل نقلیه از سمت چالوس به تهران (شمال به جنوب) به‌صورت مقطعی ممنوع خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435318" target="_blank">📅 14:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isyZxBWAe0sTFclGRmQFAUQ2BgwxWT11pOlDPw8rxe2nBSExazTbO31IxDL-SlTeboW9DuijLLsAotI8OOlfckQ34-8dOhOlWHTRVFINarRkT93305LuGdg8KTQT6iSFmFzpHD6cNd1jucbQmSQILc6pasSc-Yfuv2ZxVGSier-ucZrL3nu1Or3UdJO5ssi64trWLYboVk0rN_MMm7Lt2Y8eygeiCRKHd5L9aMQ3SWKLx5_Ag9N_dcjLmu__SXg7hMgxM4dFdCELbFkQ2ybyaX924X-LHQ-b7CvRxngAVie-ghZKaoSIS55KGQOeuOUewpwWpWRqBVXho_w2dwLpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷۰۰ تُن روغن احتکاری در بروجن
🔹
فرمانده انتظامی چهارمحال‌وبختیاری: درپی بازرسی از یک انبار در بروجن، ۷۰۰ تُن روغن خوراکی احتکاری به ارزش تقریبی ۹۹۳ میلیارد تومان کشف و یک متهم دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/435317" target="_blank">📅 14:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435315">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV5smzqZcbvfcc1vfGgDRZNP0_peNSGy9RLL8VQbwMOfuBhY5vyqZXjOJ79KfX9allDCf9XRecdK7e6k_LXFaPPZWrnPlC_9O60CSkdAZp3vJHnhCmmcKaoIXzf179py87cKij229Iv8WKbg4nFqMFH0PNJc82DHOxhBaDWOwfsJfUWJeF2RJXgplKJBHjxDFdgcp8DaBhlEKp-2E9QN0RWolsKv8n2DEw9rT9XMzJNWRqdz9eUa7UslWldRKq8AgdL-ZT6ZCBJrEgvb0gYfvFOVHkCzUGFkcLE4K6Ddh2P_AzGj2LpKBeygyUAwZPD0pQaVUKFfCsPmy8Muy5Nhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: وظیفهٔ ما این است که با همه وجود در کنار مردم باشیم
🔹
با قدردانی از نیروهای جانفدای وزارت جهادکشاورزی از دورترین روستاهای مرزی تا پایتخت و وزیر محترم که از ابتدای جنگ رمضان پای کار معیشت مردم عزیز ایران بوده‌اند، می‌خواهم تمام توانشان را برای کنترل قیمت‌ها به‌کار ببندند.
@Farsna</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/435315" target="_blank">📅 14:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435314">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AliVFXyBcLophbejZqE57Ym6aA2A0lqDE_zhP1g384B0DrzICvQ4eAFxmAQ-bxedhqQQKN08TxMV4yd4NbFSV8hd0AYHjAAWExbGRK028pTchuWV5JgOzMPipvS_CAqTNKpq-hHkzWqsPY-2eLzOTVuUz8piw81BjIp8dag8Cz7Nhg58lDELXlN7qFzw24IcrPIxfzWnFXD3tx6gcIDactkcXpc1J_yHq0jElXFBubFkFb25D_wq2g45QWNWJD3IAs3KzuMk1dpcT71ri7s8flOF7zzK9heEFu92l-UcYQnZZoaSFV_JWSqQmgCb4WhRdOL2cg4ak-es-FhesAlH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت اکبر عبدی از زبان ده‌نمکی
🔹
مسعود ده‌نمکی، کارگردان سینما در گفتگو با فارس: اکبر عبدی یک یا دو مورد سکته خفیف داشت و در حال حاضر به دلیل عوارض قبلی در آی‌سی‌یو است و وضعیتش تثبیت نشده است.
🔹
آقای عبدی چند روزی هم در خواب مصنوعی بود و امیدواریم که با تلاش پزشکان بهتر شود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/435314" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435313">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توقیف اموال ۲۴ فرد مرتبط با دشمن
🔹
رئیس دادگستری هرمزگان: اموال ۲۴ نفر از عناصر خارج از کشور که با شبکه‌های معاند دشمن همکاری داشته‌اند، شناسایی و طبق روال قانونی توقیف شده‌است.‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/435313" target="_blank">📅 14:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnKGi1nKSBfsdfJSKF8qDtrCvkvugXbJcVYUd-8wLRVVxi2-O_RTL83pSSFxxXbx9egqumgTVRp-jiE7NuaccYyOneETSQQ0odGGs2BOetimT_kV2sgkLmXbvbTw9FvKnG_-g4l6SNof2FaMd62jmH1Ou3CKEanm0lEWRWcURLwY_VJctYT0_nC3KvAu2JUnHK6Yun09O28__0CHqTIyzODjdbBvdmP-m4XyGZmC2upRD7d8fNbHAJUGDb2qTmxtbg8Pn5GL5jhrB_QmliOmU_0BERyHmMdBfgKqGcfqtjVaTf0UxuRBt3SQvmmUZsrCiIXD2COesi0TIB6suD2wGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wuf2Jfca8pORNtQ7XRXHiCvU0Wzd3Ai2uWB3NEWH4pE52LK-N7GyZeAwFNhKL3CViNNrAuUP6rRJveU96HjQnVEzimsLIHL3njsiYdWp3qrbDD6PFrA9ularANP00lwagdoscEfYgMo20Nk4cx_bcwsMCG68SN4ySGqE9BLagrRTyGmJ2btwKqBmR9VRPUpGW2b0RTn5Kva1Kel-43R2dTfPi09JYWDoeOw13IFcpJ40dk7bV7JkWhoBnXRn4WuIwZXSQ5qc4d0FDDz3FUuJlCgZDfpVEiOMVj1-vDd0w4ed-V_ro9xdlhiXp45Kfcn1BvhknBWJbKs3g4cf7HgvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laG_DbSSYUvMExeSHeOeyXgtFc2eEX-iEM5fJmpVnCszhN05S2XklOQGckuoO3SDdyPOtSLL_cIENUAhMDUex9SeiT6DH_p905akC1CL10b3hKkP1gF73sTzqeqxn_r67QOFFqpPGzt7_XiPkUGk87G3nyqpG64PGWuvNir0Gq13VnSl3OmtGm64EB8XYwDOyNVjWSWMhzchLXDh9Gqxer7CM-5k9J-6r0emMaRlJHOxSaxPL0-hL00IhHAZzk3TwI8o6MTbGteNI06mxA8NyLfyK8VqKOinEFPOlH5IqZKCx5xW8NqEOtZqDCTTqH7dl7XUiH-d2ROqGdCGhBZ7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDOyuCXF-eWUxIS1eCC2veXFn-sLW49xBdWLAsK9PMqMM5QJjjQyWvKy9hjGqbUTcp9AGboaDBUnJCGY3zzmeePowI7kigK1UHyIVb-1A_kK8xe0ASQ0PNjPR89z1Q65z5RilAoi8P3_Hf04aBhflNMsJg1McoFca18jXZzYObaUQ4HaLugp9W4u-H5NJkQ15L_wRbgjdytH8HBuDIGCCzYg7caVU81kGuDaDl4Y7PfeZRYlWRJAJNkyck6qP9yXPowkjqt-FoqC3WLppILi7s7EXWOXLrjhZY2MLkl5PHIhhbo-4zN5krTT_CztaS-USwnq_K2r2lpF9CRMNwWk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ED-wxZDG5aUuU4drYsHEuo6FdZMzUQLX3dEZmhObxLawl2iKGMvwuqBrPNyDttcFOcwG-DtKCDU0GKMCY98VesY1_HhU68pDMT4vIO4nJ80ONdiJ3Fopq9u9htomtDpxqLChrE1u_O2mTIyGP2fj6g0LYzXtM5effSJko9GJ6PZgxeOng1hy1Cy8dF_cZJGmeYZwxEN53_eqkmsSuMfpg-qGMo3cFS55DbqkzD92YWblg-GfqVUmAkc38UBHJT0vjhu1Tqp_uBjCxfb-t78qdBwrlnbdAeHNDNIGVkFjJECE83D3nP3kcKDEzQwLLJ6T4YEORAd8o4sviM08ZU6QPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgGwFPdCiLOeFT9sJc_Xj5bGf6nwPT1cURnI-d8Zpbw40KZlu0Rv2qk0xWQBxDwpim4O5v-hazhdWGn8b8dlJw8ZfJb1Kj4F1fK2WxbPOqNReufPnOb6YsD-OGYW2fYnHVGnMCZGpGyuJ1epG3kUlewn1bMvExOFwOo-nu4s9mrjrTCOl58-ui4FByZsP8O8oNXbtbSmBzXbdK2MeKwynQTrJ5hSmvAImuL7sZ1TFZa-jn901hrukN80xaxqtPfa_ZRyFSn1s9WYWqVDmAM4o_lShQoJgGtvrNAgyrxACmBvnNotPEDDpPMhSuQumd22sxRyO906-ZAqf4Fkl5JC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/havT2bM7H_SMo7lhOctfJNmd6tamyLVTcDQHsIm3Rk_o6AmwJgNzY1a4gpB9sx8YIoTAJFi5ryeq0peLC1vLPdkudwuBwqRfyUsGQ4hww4M4VSMKUQFF-U0sHeV6dSjLIfHk5hRBPdrk0EqXP1AmayJlSTvkLiJZqINZvx0vTXAodA_G33vBtlgLUV-GP_FygoHQCSa2s-bWPGoTHyuGUCwr-9xrRw_uFJqw2pcLoX2OrKIJix5SfBf6R3nA_XD-y0qWezPxT_lN_L1BE-TT19dfL7xVAJ5jNjBjXn04MtonX1IxCjYbKiDqcJp2Rg8rpY0JNdKfd-L0ditEZXySSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzdSDaldtV9Gj0qgcrYt7GH2f2SEW83koqiz4bMvNIrT7Q7mxbQUQlgVAy8TrCKbtiBCj6tkgpjblNof6OkwnU8y_mN1dl1zCLYQJ_39dxal2hpm3J2qFN1rw6GbvLQs596scuoJOQFYWYuVWJg7g2pLcnLjp8zzB0e6aSTnZbz0dtHBhlAEe7YXINORtVAC2bxe4XfTKMlZ4aynUgWWTrlOcIVK6LV7gzjA67jLYlW1S4GBjzy8fDbqRA6vF4Z_YFU7CEoKLXZ-KR0AQy49g93k_4n5zuee6U3Mpex1NIOBdpjFZzKHoXH4uXl3ATH1JzXBY2WQSESgiPx2Krnstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgUMbEI7UHXUBnadUtCntQwujnHZV10fsPNXzl9vRdsvrqk_DbDzblZSlOnAX58hMjNurO720-8KEafqD7pg8aPtDRKRCafhYAyqZzFmQpwUtgFRwNwmQvZMfok6bAKUIZelVr6yoGIUKK9Wd55td2f64bwPA9O2LobT0JapotTh2Ejzk6nYplM7GqgZ-HG5u0qVJaMD-3FDrS7ZfVmjmyxkUKwha5hThtaI2vc3ClmO_C5EB5-j3kBt6BZvSsMV2DokdHGUBVN9fDnzOGnEi8fFLZIcuUMiu6qOSjGXg5ka-6zBvzY_3GOih6qyLK0sRRz4mD6FY-gwqP64LgXRpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از تنگهٔ همیشه هرمز
🔹
بیش از ۱۵۰۰ کشتی خارجی در دو سوی تنگهٔ هرمز منتظر دریافت مجوز از سوی جمهوری اسلامی ایران برای عبور هستند.
عکس:
معصومه کمالی
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/435304" target="_blank">📅 13:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbvmy9A-6TmMQhwmvxhY-T9WcEfRvFB4U_Sw2Ol-LlVWZh9l9QKQfpXPYA2tlaMt0RJDJ7K4zB79SPIAio47xW-T9vLGrXo171UIZl07yAh1T6KPxVFK0mPma8HJCzodWM1jrW1vSSO06lDcjp2MfCs3uSXCH4D_4X7jZoJM7f2EUDUgoHnXcvzWM-JLGSh6bDzcZ_umSdF1N63Mvi0_0TanxzJHJ_kjDOCT61pGCUb8lVMrJc-uQoCnEaK7pVBW20gm8Q8xPDfW8NIsr4Phmx9EnJqG1UAYSdwJNWHSJpP5cShHgPDWYODHtvJAmsD7HDwa025DVoZz07DU8jrfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کارگروه آرد و نان اتاق اصناف: نان گران نشده است
🔹
قیمت‌های جدید نرخ نان که در فضای مجازی دست به دست می‌شود اشتباه است و نرخ جدیدی برای نان تصویب نشده است.
🔹
از دیروز فهرست قیمت‌های جدید نان در فضای مجازی می‌چرخد و حتی در خیابان‌ها مردم از افزایش قیمت از امروز خبر می‌دادند.
🔹
هفتهٔ گذشته بررسی هزینه‌ها طبق روال سالانه به سازمان حمایت از مصرف‌کنندگان و تولیدکنندگان ارسال شده و آنها هنوز تصمیم جدیدی ابلاغ نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435303" target="_blank">📅 13:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b50a2f5c5.mp4?token=sUanGdkpCoTCi3z0_dDyKSSJ4DBqVXirwe-FnTzb-2Cx1StgCep8ut7I1TByr383w8_2T-8LlPMDUVN1AsgjVg3RMMGS8XtJyI2TMcxPLgybd41GeiM4KbCLD9NREsgPI94U2q6pqPhYNrCh316GtF_ZvkiiaSyE2Vdf0q-eJsu5W75P74kQ7RKbmqUQ86cRMCgpWvxqTSw9BQZaqEoyd84SG31e8PKGoQQAmQIC5uxIhUxk6CF3zD3qyXMl0TWxNvQsFDxR0rUdp4fC0rpEFpYaHieSjkdUT1HH0p2Mi_JuxfnI-3gVcWlFPgQD5rBLnrr8Gd10GmJ9f4HJ9FVnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b50a2f5c5.mp4?token=sUanGdkpCoTCi3z0_dDyKSSJ4DBqVXirwe-FnTzb-2Cx1StgCep8ut7I1TByr383w8_2T-8LlPMDUVN1AsgjVg3RMMGS8XtJyI2TMcxPLgybd41GeiM4KbCLD9NREsgPI94U2q6pqPhYNrCh316GtF_ZvkiiaSyE2Vdf0q-eJsu5W75P74kQ7RKbmqUQ86cRMCgpWvxqTSw9BQZaqEoyd84SG31e8PKGoQQAmQIC5uxIhUxk6CF3zD3qyXMl0TWxNvQsFDxR0rUdp4fC0rpEFpYaHieSjkdUT1HH0p2Mi_JuxfnI-3gVcWlFPgQD5rBLnrr8Gd10GmJ9f4HJ9FVnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از انهدام تانک مرکاوای ارتش صهیونیستی را منتشر کرد
🔹
مقاومت اسلامی لبنان همچنین از انجام ۷ عملیات موشکی و پهپادی علیه مواضع ارتش صهیونیستی تا ظهر امروز خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435302" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXp-6zI5Y3t7qvuZyjsz5AjO9VT1Gns62XroUAykXUhOk0lZ4NXnaH5gbAyIEImsq4Fd2VlIzXCrwrD4Z4MD5_IKTPG46dHy7ApwwoO5OG1MuGl9sqVEy1pORldzEHsKIkS9C1mri3zOY_KxQ5fAOkEagiMXBZhT27wpSPqnA1CJC5yNYBbowk5pBkK6l_P3kcRgOnRWAoC9PSBhwzeesMdH9mn4Hh1URVrxzyML0MXjnQdo_dp8vGb90AskGhSRXzweGBbemg0Plf5QrdT_gx9gPZxxZ4Sv457nqO2MHIBFwLZ0GdOl56TpEiiGcYHoGrmeYJ55F2HIeGYfMYxmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدوین ۶ بستهٔ حمایتی برای بازسازی فولاد و پتروشیمی
🔹
وزیر اقتصاد: دولت پس از جنگ ۱۲ روزه و پیش از جنگ ۴۰ روزه، برنامهٔ جامع حکمرانی اقتصادی در بحران را تدوین و اختیارات را به وزرا و استانداران تفویض کرد.
🔹
با شروع جنگ، اتاق عملیات ویژه تشکیل شد و خدمات بانکی، بیمه، گمرک و ترخیص کالا بدون وقفه ادامه یافت.
🔹
همچنین حقوق کارکنان و بازنشستگان ۱۰ روز پیش‌ازموعد پرداخت شد و وصول مالیات‌ها با استمهال و بخشودگی همراه گشت.
🔹
بیمهٔ جنگ برای کامیون‌داران در نظر گرفته شد و با تأمین کالا، از التهاب بازار جلوگیری گردید. ستاد بازسازی فعال شده و خسارت‌های زیرساخت‌های اقتصادی مستندسازی شد.
🔹
در نهایت ۶ بستهٔ حمایتی شامل تسهیلات ترجیحی، اعتبار مالیاتی و انتشار اوراق برای بازسازی صنایع بزرگ و کوچک، مشروط به حفظ اشتغال طراحی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/435301" target="_blank">📅 13:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c9b569181.mp4?token=QJA_vfmVElubfzLTjElvt7_6_iCphnvDb_Wm5nWi3uBFR95Y9vWCLtISz6Ik8fmeiVRrqc88nvthpC8rhWZWO10nhEhV7ZK9b4EGzSQNMWHDkAj0UUs-ZNcYWGxYXLKb-4W-C8t7yndx4HFn_89qTMtR5kFTr8lz58LSZNRW91FiNiuA6RAw9q3-Sq2m_diLiJoS7FL2_LeqVwfnuiS5G7DXh91jcyE6dkrnljF-mK0_-32xk1RGdFjMGuZBW5ulG-ZBsux0Hsmma2Y86gLRFDPHJX7z3_P2X_43U3OsXiWr2cGOIm31gbulvCxBhlUFzY3MrZDhDyS0JiAhDXjNCywrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c9b569181.mp4?token=QJA_vfmVElubfzLTjElvt7_6_iCphnvDb_Wm5nWi3uBFR95Y9vWCLtISz6Ik8fmeiVRrqc88nvthpC8rhWZWO10nhEhV7ZK9b4EGzSQNMWHDkAj0UUs-ZNcYWGxYXLKb-4W-C8t7yndx4HFn_89qTMtR5kFTr8lz58LSZNRW91FiNiuA6RAw9q3-Sq2m_diLiJoS7FL2_LeqVwfnuiS5G7DXh91jcyE6dkrnljF-mK0_-32xk1RGdFjMGuZBW5ulG-ZBsux0Hsmma2Y86gLRFDPHJX7z3_P2X_43U3OsXiWr2cGOIm31gbulvCxBhlUFzY3MrZDhDyS0JiAhDXjNCywrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اجتماع دوقلوهای شیرازی در هفتادوسومین شب اقتدار  عکس: احمدرضا مداح @Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/435300" target="_blank">📅 13:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907dfc0cea.mp4?token=oPDJi_LSw8pNwLNqgoWwKexEMyk7qCF-hpB6rOjNqGwglh1Pm0enlBJEY6DAs125sajwJAji2ueSiWzmrPOdXUeCxoo29NAVbrJvB8sRMRIVYqUCiZBlPOhJLlnH7eEdUs-aHcbYp90cZc3OEgrmCq1DcrjbHZcwYEFwVDuEj-KTcmuydWkGrUYfIbZWQptXuZICxZ15Mr0tWNQFDeVVesTgTUockgmm3YDpRnP16mKRkvq3Rf5HSIbU_HSUOiA0NM0rzSBEOEZhSQ8PoZpUssTKHQ533tFsK2U7FC3YOfy2IDkCYR7g_c21VvI26axr20d_mWgJ3pds3sW46ePl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907dfc0cea.mp4?token=oPDJi_LSw8pNwLNqgoWwKexEMyk7qCF-hpB6rOjNqGwglh1Pm0enlBJEY6DAs125sajwJAji2ueSiWzmrPOdXUeCxoo29NAVbrJvB8sRMRIVYqUCiZBlPOhJLlnH7eEdUs-aHcbYp90cZc3OEgrmCq1DcrjbHZcwYEFwVDuEj-KTcmuydWkGrUYfIbZWQptXuZICxZ15Mr0tWNQFDeVVesTgTUockgmm3YDpRnP16mKRkvq3Rf5HSIbU_HSUOiA0NM0rzSBEOEZhSQ8PoZpUssTKHQ533tFsK2U7FC3YOfy2IDkCYR7g_c21VvI26axr20d_mWgJ3pds3sW46ePl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار ابن‌الرضا سرپرست وزارت دفاع شد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: ‏با حکم پزشکیان، سردار پاسدار سیدمجید ابن‌الرضا به عنوان سرپرست وزارت دفاع منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435299" target="_blank">📅 13:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3f7c8fb7.mp4?token=G4VUSBaBpDynbZCs2c5xnaU-jtaK6RS1T0WoCJih0GqI638SmPdpaocvcYDttJnpNh_rNLjTqDBpMDrTxrbYcfpzvuFnildyL8BgD1bMNj7TseKYFmFSlmBWWOv18-RCWkL15XmF9SXuSFAqdxsQabcIAup7lj-NsDx-WZefyeIyV4rtZgM2IXLb7rGuPuEMKZEvX5WweFeWS9mF7hIZUj1FS-OXNMnDI9uZdm0jakiGGPl5P9P8L2t_N5o8we-wPYQ1qFdSRl567su38LDFGCh-WbpxdCf1FMywdIJqaMq3sMH-TZc9jgvR58JLXM27qmJWn6f1wvAtmn0bJHHPu6a8kMHoqi4M5VUZaZWpI6dNfORubQC2ke7hMHpl7ru3EpXCZjDaBpah9d-CCdvw9QQ_WAvm_A06vhi97zz4EfOWbKcf2JLS0bsrqswzA8xGboLbf8Zebm1SHVJjFAsZv0yoWIMMBOUDErKeT9wmRkRElaZxfvMRa8T9quLXYV5abaWAWfN-YL9OnXAI631vGnBWr42fqmgO2YPlLjT4TAYDheeabGnPSzy0K4esxmE3DoTk9hwFl7KO6tBaY_vHgUgHYANgsvsgKcSZhGOHVu9DEonAd1dj0b3_93KmEv-P7gDps7hizxAhwAsVvBCEesa2kWwvjJ5RwGCzv3g_Wts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3f7c8fb7.mp4?token=G4VUSBaBpDynbZCs2c5xnaU-jtaK6RS1T0WoCJih0GqI638SmPdpaocvcYDttJnpNh_rNLjTqDBpMDrTxrbYcfpzvuFnildyL8BgD1bMNj7TseKYFmFSlmBWWOv18-RCWkL15XmF9SXuSFAqdxsQabcIAup7lj-NsDx-WZefyeIyV4rtZgM2IXLb7rGuPuEMKZEvX5WweFeWS9mF7hIZUj1FS-OXNMnDI9uZdm0jakiGGPl5P9P8L2t_N5o8we-wPYQ1qFdSRl567su38LDFGCh-WbpxdCf1FMywdIJqaMq3sMH-TZc9jgvR58JLXM27qmJWn6f1wvAtmn0bJHHPu6a8kMHoqi4M5VUZaZWpI6dNfORubQC2ke7hMHpl7ru3EpXCZjDaBpah9d-CCdvw9QQ_WAvm_A06vhi97zz4EfOWbKcf2JLS0bsrqswzA8xGboLbf8Zebm1SHVJjFAsZv0yoWIMMBOUDErKeT9wmRkRElaZxfvMRa8T9quLXYV5abaWAWfN-YL9OnXAI631vGnBWr42fqmgO2YPlLjT4TAYDheeabGnPSzy0K4esxmE3DoTk9hwFl7KO6tBaY_vHgUgHYANgsvsgKcSZhGOHVu9DEonAd1dj0b3_93KmEv-P7gDps7hizxAhwAsVvBCEesa2kWwvjJ5RwGCzv3g_Wts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه آیت‌الله بهجت ۳۰ سال پیش دربارۀ رهبر شهید انقلاب پیش‌بینی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435298" target="_blank">📅 12:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsld1YkgTx8jspM5HbBbefUHv-vVOwpi0IIJJRfbquGdEiBpGYgXxqIVHlieHUoVydAEq7DoAmzxmFf-zx_pilgjEZr5ZE-2Xsx7iO1BxPOWCmC89bt4OSOpmxiWXeMa-vHZBBSxXOUVWBf7NeIKpQcM7MxvqAcfGSIPueHul1dJ6DGN7uUnPoH4-r9jf-CYdyGJD3Qyzib7rcDsXJVGsLmHYUsvvr6WzBoh4CPzNn8a6AwX57sJRqolYWhFEXyWKvVlrmft0-xyGTdwO9W3iJ6I4I6CD2i2P6KBHhqA11GOm0gIkDIeVe53g9Nh18eX784n-3uW0h9RtUyxIkLaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت اربعین شهادت سردار سیدیزدان میر
🔹
مراسم پاسداشت چهلمین روز شهادت فرماندهٔ گمنام جبههٔ مقاومت اسلامی سردار سرتيپ پاسدار شهید سیدیزدان میر (حاج اصغر باقری) و شهیده دکتر فاطمه‌سادات میر، جمعه از ساعت ۱۷ تا ۱۸:۳۰ در مسجد شهید بهشتی تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/435297" target="_blank">📅 12:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9v4bG0UF93QRNqbRzNVIsqn6eDgdqmLjk1P4cqkd7pxRmKxBOIjUVxJJr1cjizoTVslLFEkg2SSKa5Q0ctkujOqUY1L0S1cZDQypWDVqLC94uRT3PiNuTzUAv3Kf8uFDuXW8BVNAySD7TPvviCYLML89rU2EXXg5tmY-fq5puUns6whLi5fJHrbtKXsDa2ofsJkKBorejFxr-QUeiocWpH2Oba7kTC6d3pKHx_0m4mPBXGzmhTMiHjCMC_caqPKmRQEQYjJ-yEhbJQFB1Zy76cIEocWxrtuNPNX7h1xqSOYv5aDgPkb4iDOfXgb16M-0uo3og2cbqUbO3M-wA8iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای مجلس و مرغداران بر سر مقصر گرانی
🔹
نایب رئیس کمیسیون اصل ۹۰ مجلس، وزارت جهاد کشاورزی را دربارهٔ گرانی مرغ مقصر دانست که با وجود نهادهٔ کافی، جوجه‌ریزی کمتری در فروردین انجام شد و تولید را کم کرد و قیمت‌ها تا ۳۹۰ هزار تومان در هر کیلو بالا رفت.
🔹
این درحالی‌ست که اتحادیهٔ مرغداران، کمبود و گرانی ۵ برابری نهاده‌ها، خوراک،‌ واکسن و دارو را مانع جوجه‌ریزی اعلام کرده که تولید با هزینهٔ گران برای آنها صرفی نداشت.
🔹
بر اساس آمار اتحادیهٔ مرغداران، جوجه‌ریزی مرغداری‌های کشور در فروردین ۱۰۶ و در اردیبهشت ۱۲۶ میلیون قطعه است که این میزان افزایش جوجه‌ریزی ۴۲ هزار تن تولید مرغ را بیشتر می‌کند و نیاز ۱۷ میلیون نفر را در ماه بیشتر از ماه قبل تامین خواهد کرد.
عکس: علی‌حامد حق‌دوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/435296" target="_blank">📅 12:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75236b936a.mp4?token=GaSJcHqSoZHVUfFEsbH-bdULutEMlOECyU4P4XN_cccDUMH-vzK2QcQbBnBkxcgWoDzVWxUs6oL-7LwKNUI693dQqhID7luooZECfjBIFvqxUO2m1Jbgm25ZODLm7dwHqNkJII9C57H91WURULVFnOHcTioNh1lwbHZtBjd31_ZFQCyLtLyFoAW_kCnhp8tbFBbD4dKfC2ONew70x7JZ-0dV07d5YgD5ZjOL0TJ1K9RIp790zd_VrQx7-q18DOyhzwFdkxFzPUns98BOV40ttGCzR63oi8fVACa4tTQk_nPeickp2BetYYGMpSaZ6pONADh2P5GRns7di22-E96QSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75236b936a.mp4?token=GaSJcHqSoZHVUfFEsbH-bdULutEMlOECyU4P4XN_cccDUMH-vzK2QcQbBnBkxcgWoDzVWxUs6oL-7LwKNUI693dQqhID7luooZECfjBIFvqxUO2m1Jbgm25ZODLm7dwHqNkJII9C57H91WURULVFnOHcTioNh1lwbHZtBjd31_ZFQCyLtLyFoAW_kCnhp8tbFBbD4dKfC2ONew70x7JZ-0dV07d5YgD5ZjOL0TJ1K9RIp790zd_VrQx7-q18DOyhzwFdkxFzPUns98BOV40ttGCzR63oi8fVACa4tTQk_nPeickp2BetYYGMpSaZ6pONADh2P5GRns7di22-E96QSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: نگاه چین و روسیه به قدرت ایران ارتقا یافته
🔹
امروز حرف از رد شدن از ابرقدرتی ایران، شعار نیست و دشمنان ما هم به این نتیجه رسیده‌اند، تا جایی که لحن دشمنان و حتی کشورهای حوزه خلیج فارس تغییر کرده است.
🔹
هیچ کشوری یک‌طرفه با ما تعامل نخواهد داشت و کشورها…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/435295" target="_blank">📅 12:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b5381a13.mp4?token=NuGzedqRsTrMuyUHxq0u9FnPuREeTtImFISVf7I_5cNoD6W0HmwfmMm0jJGUnXmHxBnie0knY55LAla37Nqlh4QHEpYEoGTMmB-Nlt2txoqW7F0L_1D2WWA_Tgr_5JNE5JDdVtIoSQqK1Yv3jjnYkbeVWJB2ABb3mlqkQZGN5iIEVeMvS3Vpm-1HAMq-XBCwCjgYJhbUDWBVOW5ZVtD4mwSqYU_ffGbC_7H1MdeoFiOokk_BlkgqKZd-bMF46voplu2YV5F4_E7cNqRWJCLsuB0I1cotLLebECcJnKPnyl0-ZfRotdlF0I8FnzlzbvbFc_g7OuQZOrCNosxHp1Bg3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b5381a13.mp4?token=NuGzedqRsTrMuyUHxq0u9FnPuREeTtImFISVf7I_5cNoD6W0HmwfmMm0jJGUnXmHxBnie0knY55LAla37Nqlh4QHEpYEoGTMmB-Nlt2txoqW7F0L_1D2WWA_Tgr_5JNE5JDdVtIoSQqK1Yv3jjnYkbeVWJB2ABb3mlqkQZGN5iIEVeMvS3Vpm-1HAMq-XBCwCjgYJhbUDWBVOW5ZVtD4mwSqYU_ffGbC_7H1MdeoFiOokk_BlkgqKZd-bMF46voplu2YV5F4_E7cNqRWJCLsuB0I1cotLLebECcJnKPnyl0-ZfRotdlF0I8FnzlzbvbFc_g7OuQZOrCNosxHp1Bg3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور در دورهٔ اصلاحات: مدال افتخار موشکی‌شدن ایران را باید به سینهٔ رهبر شهید زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/435294" target="_blank">📅 11:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
بازی تو وسط ممنوع، بر بی‌طرفا لعنت
🔹
نوحۀ حماسی نوشه‌ور در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435293" target="_blank">📅 11:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مدیرعامل یک مؤسسهٔ‌ مالی با ۱۳ هزار شاکی دستگیر شد
🔹
دادستان مرکز استان کهگیلویه‌وبویراحمد از بازداشت مدیرعامل یک مؤسسهٔ مالی به‌اتهام کلاهبرداری و فعالیت غیرمجاز خبر داد و گفت: در این پرونده بیش از ۱۳ هزار نفر مال‌باخته شناسایی شده است.
🔹
این مؤسسه در ابتدا مجوز بانک مرکزی را داشته اما از سال ۱۴۰۲ بدون تمدید یا دریافت مجوز به فعالیت خود ادامه داده و این تخلف با گزارش پرداخت‌های گزینشی احراز شده است.
🔹
براساس نظریهٔ اولیهٔ کارشناس رسمی، ماندهٔ اصل سپرده‌ها حدود ۱۶۵ میلیارد تومان و مانده تسهیلات پرداختی در اختیار اشخاص حدود ۸۵ میلیارد تومان براورد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/435292" target="_blank">📅 11:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435291">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3d84ad80.mp4?token=UBoZjlJXY5WN8Hkp3JusQoai2emT8flj6R8-QB3FVE77fy2KVse5nrHgUD_IXzMWkc5rCKMRu3YCzhqvcIw75vJjqjXmQw3c9WLMxI4uWjYDN6EbMKRaJWC2UfOAbFkSlyBqBkOUyr0yOyvUxVaTEx3CxM2NxCOmUYsZ7LL603G81lga63EuFNRV0Dm4CN0j2Gfg8MQowSwT2Q77iFzGb1KJEZ8u0WlY3KWs1kmoWDpcILROC0C6Tv1l_eRqnrvhw9OzEB1Pm8QqOsvvdL6-cuEpOtkfvMPSDlPfewMPxwKOEHzUZWpg4U8sWYO3dV31WiTm_2DCNhjIGBZOBiEFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3d84ad80.mp4?token=UBoZjlJXY5WN8Hkp3JusQoai2emT8flj6R8-QB3FVE77fy2KVse5nrHgUD_IXzMWkc5rCKMRu3YCzhqvcIw75vJjqjXmQw3c9WLMxI4uWjYDN6EbMKRaJWC2UfOAbFkSlyBqBkOUyr0yOyvUxVaTEx3CxM2NxCOmUYsZ7LL603G81lga63EuFNRV0Dm4CN0j2Gfg8MQowSwT2Q77iFzGb1KJEZ8u0WlY3KWs1kmoWDpcILROC0C6Tv1l_eRqnrvhw9OzEB1Pm8QqOsvvdL6-cuEpOtkfvMPSDlPfewMPxwKOEHzUZWpg4U8sWYO3dV31WiTm_2DCNhjIGBZOBiEFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شابلون‌زدن شبانه یک خانم در خیابان‌های تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/435291" target="_blank">📅 11:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGbaNbDl0BZj2qes-MlIaiPMymj97c3WfN6tyvm1CEvc4U6l4befEZsys9V1sbFI5pVMtXicGtWu4E8OPRBGBBXDKTbDBYVbJ1lMG4jWXHnQThY-amgVf1CWah8j7s8d2MoKXrDjymfOxg1MjorlXI9Vsre_6lsh2V99WlgVAorZjoEOTTnaDooyMMBtAd0m9chqRaac8NwHkcfbRSM0mAzQ7FuYM8EOzfjJjK32R5YoluWYXPISmRHAjpTFF3_jDL7StN0XJ8Rzm9Zp5G3YU5rUGl5UBRrYfZMGnvgQwdcurdqK2G8wacHQZGujrTuXSd7kwclERU8KM9HYmJBAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: هزینه جنگ ایران یک تریلیون دلار است نه ۲۹ میلیارد
🔹
سی‌ان‌ان در گزارشی به نقل از متخصصان ادعای پنتاگون درباره هزینه ۲۹ میلیارد دلاری جنگ ایران را زیر سوال برد و از هزینه یک تریلیون دلاری سخن گفت.
🔹
«لیندا بیلمز»، کارشناس سیاست‌گذاری عمومی در مدرسه کندی هاروارد در یادداشتی نوشت: «جنگ‌ها همیشه بیش از آنچه انتظار می‌رود هزینه دارند. در طول تاریخ، کسانی که وارد جنگ می‌شوند تمایل دارند نسبت به هزینه و مدت زمان آن خوش‌بین باشند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/435290" target="_blank">📅 11:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIYt1pUtkvtOCsvGMdR69UXCMQHB-xMR-NYDAIcKMpmO9NcTNqxhsviv25VY8SDAWFlubRUrs8HsoqxQ4UcoTp8sDBx7jkibQ1Upgd1Bz4Miltz3gWxayATa0PXR1MZw01FgOGBDfku_WHg6baMZCWa3wtKlZsxF4vjFFzzuD3uKNpB-LnQjHlKBoK-oX2W9tqTcNsJH0sPUp6tI_AXOKJYXrLr5HSFU9xF9rIfxGIprzSbVKt8GMkB5pa6oCd7k4UnX-ullNzXA_VQ_P_FlFtn_DQVPhPpOJlnRJpb1acAYDeyGDCc2Tag2oPK9uaqbrIE_l_HvXUN7K-ODPUDc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUsqcxO8J4HTBMa8wMdtu_D51z-23zaz4W7soBRnZ75IhvdgGyrjpN8xAI2lB0KPVqYqWcgRl1xV_F-gDdVMck2r48T7f7XmZxSk_Vi1Sk5e9k5PSihrm_vA2vTUlnIAziBtnqZ6CmUsnzvdu3-eDhWvmJCDMhpUV7gXHtv64w2NlDxU4Z-Qq0SmpNkIIFOa4v8rN32jT04mMqIH_QaN1n4gK9GWw9EcUECOnuFEW9-BfmUpq_4NTfKRi6IfBqTakOJR_z7AxYCbm37uwlktf5dSztWFMUUDqUF6P5453OZ9GDL-fQnXNX9MwriWi4X2ilPLXxBWFjXmqqUJorq8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNW63pcrNYORXgbxiJ9k12YpJgvDrCvQCRHH2XCUHgGDwi_WsKayLJ_j4n8qaPUoev0-r2go2cCIyB74VHPWFF50dA9K6yiwcYqHfr-xCFD_3uoxYihmOA720AX2qHveeRzxy2LKveyjwaP9L9QhHnlCVAYM_mBR9rPjcQq0wrsGywcrBHwoy2dpfbY5H3bSfftl4ovTBRmv75erHbSF3K3hojbVcbYA2vWk6sGMJDGO3-3v0Fs4pyiWSaFUW18cTFLONff6kSiJsPlMXDUS1dihRj3jVd9QuE9Yx5TE5IusZ5ZPjklamnj1XkfFUHxXnHFrGORnB0Oz1HuSIMIQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNcM1OFMGXrqEE8mmK-eIPZ5kVjQZZe8M-7Ne5eN_5FwOuGhbhl2KBCfY3BqmepHGrlo4NTquSEPElvQekgF3A7-x3wN3gNlwJaciuoE7RczY2Nhno2UTVAl2rqOpoY_33q0IJzYMNr6CnYLERhNGPxgmE0R9etb1W0e23LvUt-L2HtOt2X25q42wVYyWGe_Cd9Ew6qTM3Ommr3lbVRdgOtYkrR9cNUxZfNW12oS1xxIm5xVxNV5CW7b3GXGgoMjt63eLNxd3VW-VrbUNuxcRmHBwAE_R9bs9PBBjyuqV1lEfIEm6AH-S8JNY4Uhj6cdu1Pa9E1CyKNdsNWwC4rZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDoqzLbBxAJtdAWRQ2dfoXnC-gFiwlt2jeUpaLN8JLZ38g3dz9Zo3GAoHrfJtE4_CF1_uem69t4_LsmYF2kqvBKLlPzctet3wNyFWcqUxsHHD_PWczqSfOjiNaY2a4YpACkdLyMYtG2cDI_nsLsEegFmQn1xpU-20NhpVVFxLb6i4HYHVvvztMBAutHsO_VI1K-D2-gfGV_57ajrj2cvOenxAmeoYPGgTvq2X49BRWGEXGsKvTXU1_37C5cNIQ19VsiE5rfvBF7-dWVNjbGJVtJiwflmZUam8dv_9PUNP3I8xJfL99CqDVKZmEInXZdme08OIWMHFmLSpnChhzXUHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتشار فهرستی از وطن‌فروشان خارج‌نشین توسط گروه علاج
🔹
براساس اعلام گروه علاج این افراد از حملات رئیس‌جمهور آمریکا به ایران تشکر کرده و نسبت به جان باختن برخی هموطنان ابراز شادمانی کرده‌اند.
🔹
علاج خواستار اقداماتی از جمله توقیف اموال، تعلیق خدمات کنسولی و سلب تابعیت این افراد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435285" target="_blank">📅 11:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR0CEnlLZJ1tXmSr1qI4GFNhvpEXP-BX18jIhPHpOnNzuSHzg11cvI5n0LCfrcbh_Pl81vzerX8IYlvY7MES7SRT5wr1HqUVFM2HLzNnpGmgzSr54-laWV49mOnG2I9Ij_krxwDtzi8-GPkB7kc6YgN27UJhdfZ006u37zs4ft4LbU5wPexYRzO6jMpkHzf0-nsimiToBoRJ9b_6jpiLVZVHFgI-srQfFYKwjUHDCPnya2PAwVXGiehpOiCJC-RhIg6KGi1AZaR6rTSPkvsAz1kVlp1qm2XD53UnxqFej_IO6hzbeFmYmuUjvJvxVmyIyzdn29y-SaOXEQA7Ma2f_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمار ۴۰ روز جنایات آمریکا و اسرائیل در ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/435284" target="_blank">📅 11:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c18fec5dd.mp4?token=QangHcAaCr87dYh8lwqxftGKw2n4bg4NqL9tDC_bOhhJuj3PLNkMhex8q6Q520pTIKJ7rb-cmriRkWjiyQEmrFhvnyTDBwHbQrhGII-S2fTZMCWzUtAWHgAa2nYqEsgU-kCFU1uRwg8lvLmeSHGYi2VgxuD3AfR3fvpM_cVkRVsWeDGS8Xs5RTbUuCb3vWaZ39OoXx2XZ5b-n2co192L1phtiUJakOYNpZpAz4v4aHBaJFUmNu9pYLneJhY-360QX4degwB9_FCXbKWJ5W2KYiLl8U9uT1hnPacKaLF8ThH5lDTjEBDCOe4KBIVZETHGt2ndwahmhco3v6TuEAfbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c18fec5dd.mp4?token=QangHcAaCr87dYh8lwqxftGKw2n4bg4NqL9tDC_bOhhJuj3PLNkMhex8q6Q520pTIKJ7rb-cmriRkWjiyQEmrFhvnyTDBwHbQrhGII-S2fTZMCWzUtAWHgAa2nYqEsgU-kCFU1uRwg8lvLmeSHGYi2VgxuD3AfR3fvpM_cVkRVsWeDGS8Xs5RTbUuCb3vWaZ39OoXx2XZ5b-n2co192L1phtiUJakOYNpZpAz4v4aHBaJFUmNu9pYLneJhY-360QX4degwB9_FCXbKWJ5W2KYiLl8U9uT1hnPacKaLF8ThH5lDTjEBDCOe4KBIVZETHGt2ndwahmhco3v6TuEAfbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسماعیلی: رهبر شهید تقریباً همۀ فیلم‌های مطرح کشور را می‌دیدند
🔹
وزیر ارشاد دولت سیزدهم: رهبر شهید انقلاب تقریباً همۀ فیلم‌های مطرح داخل کشور را وقت می‌گذاشتند و تماشا می‌کردند.
🔹
به‌عنوان نمونه، پس از برگزاری جشنواره‌های فجر، گزارش‌ها جمع‌بندی و از دفتر رهبری توصیه‌های ایشان ابلاغ می‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/435283" target="_blank">📅 11:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83703317f.mp4?token=WQP-I9LXSB2Jh6-sv85VeY0yF0fee-54I4AFqg35yDfzR_lX14d9O6DTBwRQWdVXxZJoS1Shrmz7yciG-lq_J0TV2LJ0epWD_7OIPa8M5GUlWaujIoT7K-NZERsTXr9EG-j43_O6c2MzDj-keWCUCcivp6gKXVLovHgOJ7u5Fj77blHbpHk6xAYcXmXPVe2AhkuFSKbjA460lkchTkf2vl_lfdVc3puboQHCimE_qeb9XIt06wCI8cYh-h3QysVRvTkkR09962nM0gkNwNxzUQ8E8RgIkofMlrVCrA9pVcY17dcrU1-iSP9N_iqtQ9IhaVtGbvR0CrCP3IM5D0wKOmecufu4aF4P8_uUYGF568VlXs8GcH1g7LMJSlV_MWNVFb9uFMavjY8fu5SwabpclRta37umfTzDzXJzI6ho_kEGkmLBmocr2FldxXF20SiI4JkM-GtuqP9nlw25RX8GUtSnfXVpYxA4n8LyLiqoIxn7AIZVYsJBUQA7GUNs8plHqnDYMKCocAPMiveTiOqHSFTRve9A_nmWto4XPVlusLLVUvcbhAmv6ZgmrkwaDBJo1VqnauGtOR0I5i2dmpa1EPSVE1YrcWyB2fV_mHGGhz6Mv0FV9WJiftALS85dzYDyFM90DysI-LgWKbIbKYNhvlswXbjTl5tdgQrVbVLAq60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83703317f.mp4?token=WQP-I9LXSB2Jh6-sv85VeY0yF0fee-54I4AFqg35yDfzR_lX14d9O6DTBwRQWdVXxZJoS1Shrmz7yciG-lq_J0TV2LJ0epWD_7OIPa8M5GUlWaujIoT7K-NZERsTXr9EG-j43_O6c2MzDj-keWCUCcivp6gKXVLovHgOJ7u5Fj77blHbpHk6xAYcXmXPVe2AhkuFSKbjA460lkchTkf2vl_lfdVc3puboQHCimE_qeb9XIt06wCI8cYh-h3QysVRvTkkR09962nM0gkNwNxzUQ8E8RgIkofMlrVCrA9pVcY17dcrU1-iSP9N_iqtQ9IhaVtGbvR0CrCP3IM5D0wKOmecufu4aF4P8_uUYGF568VlXs8GcH1g7LMJSlV_MWNVFb9uFMavjY8fu5SwabpclRta37umfTzDzXJzI6ho_kEGkmLBmocr2FldxXF20SiI4JkM-GtuqP9nlw25RX8GUtSnfXVpYxA4n8LyLiqoIxn7AIZVYsJBUQA7GUNs8plHqnDYMKCocAPMiveTiOqHSFTRve9A_nmWto4XPVlusLLVUvcbhAmv6ZgmrkwaDBJo1VqnauGtOR0I5i2dmpa1EPSVE1YrcWyB2fV_mHGGhz6Mv0FV9WJiftALS85dzYDyFM90DysI-LgWKbIbKYNhvlswXbjTl5tdgQrVbVLAq60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی دیگر از لگو انیمیشن ایرانی؛ تاریخ واقعی را اینجا پیدا کنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/435282" target="_blank">📅 10:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3c4G78Tf_unWa6_YYkuyJ9dblNmi3J4rFDAWTKIR6YtRwQBEHhdGeMy4NrmX98tN4Vd1HnJR1_P6K_lo0jCmw9JIRCk0CtgWb1abUWsQqm4c6rccVf9gciDJHG3JXmMUh276itCFjdRjdCIkqU1JgDXi7eqF1x8sp_V3PzvPGZNqf3YO2LFDCmvva9YIz4Ff6Jy0aw1PA6Fc3tzyWnTyU0GoAe3DBFchGAuZi5Cm8RRzT4h3fwo9En4gotp4JTeNkTLdYwl-N76hIYCbJemUTIP0kXtQ0CowgbLeym14F5OiyR3mtDCCVgkz_96QVgyPoe20mzcbP2m3sGDNVyRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt4rQCc8DSSMimvoYsI4AqMTepzyZFOg0JnjdUWlbJd4AfCAFhYnj9sUZSJTPbsHWHWt_Xxk7S1cvRujQOIoRIApKW3JwOK_gin9sY9Re9CsGGwMUN7MNQPXqtbXazc3A_F_yaJvF7IOECQQlaHAzjxi1IlMggmMTSkDZh1lgwnUyjYblgvH3W7qs7yww-6KVV5B3o-re5YYMwGb4Dv47Kiu6wTlIdkONTSvctnXg-bu43tocwljaEiy-WDSmC7Efd07e9A5IW9RdmZv-nTO6qzjxKylt_NfVmVp1ZYj1gOTteZYxrxDkBfWni_toEdSKNXtnkFO0bw22lKeE3vLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qe6eqPB7euy-0TUjCHHDgLUGvSm8v8yr1MhV4AKQHgHILc0QuyNqfkV7h10vgTA4JDfDn1MsNl6TnoxiPqm-Kq8E64mpt87RJTT2dcV_xPC5hQxX_0WH2Dd5g8uOoI1OJ1dNMfs8egT_ZIUI_PXriWDuZG7tAiVX3JPvbtYGgiE37euMoxpj7KVIVzsaqSggoeRhE2en0UTOOFXUxFr7myIds-Q5SlFCMbuwmMQZsDkzcxbiuL3ioUUlNoIAYoYTVveHeh9Wm7bXvxrTSOdglzv-n4Mt2G7ANqryaycUv_LKtPY0SyJTQ13ymfptg7AfvqRLjN5M_mD-tvnYu6D28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkxRvO75movTjeOOqmSfEsdJTZjGwJGCo-JvXsRn-nUuvBoaWpiHNAon-pMhv6i90gUFF3A7N4g4s4ZN5MOYFhJYaEVhP82JT1mwXIOFCJnfgKHdjz0jKNg0ZVNP1EbTwOiwhIZbbzV-bcyUBx5u8wTzAXK1ka9MfpR98cdXnVS7gBgnOa2Q27jeRmxmIQxPyBswVwvF-kGcamZPz-WHEXg_EmHsAvd9dOIibgxAgq7L_MqGdXryfLZuQQD9u2ozPOTvoFmUB2XTOaUBgsFDx-Omymf6X8PCBKMG1gdPxPEbJG21OfNv37t2RARk3ycyDTNhl-vh523N6ClsBApDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz77DkEqNa7YrzOVbFLId6aS4MUvtobEkuwgiGhne7oRUDXZpV4kHf7JxzAgY_a1L49TycRcEfMHIiw-30E5is6a9L7cNBg2pRptQTtHAH8eqZEKpzE18Spf1qWs5jxlOaPx43oLb5APd6ibF5eaDdGydn8AP-avNPznLlh28WzdLyFrc_eFffxKXSrXnFGqx-3ibk5kaf3PU-hvYXx1J9YQ_tcHmb6duxJxZghxOcNQqttXcufixWO5uS7s4CbUQ_Cko8hmOIa-NBRWCALmoZSuDweFluS0d_v4CWs02ipQg7qLYSExz9Tyqa1eVG5cHRuwX8vxuSofC2NHuJTsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeGHUjepnq1C3ILcCLVgGc-ygp8xI-o-1Jbs6FosdtaP_CF5y36G8NOLRe7fyC-FC7GPxlYvhmTfnDjA9JVWdy_ncOYIcoRPGXR5EF3HPgE0qMa2ChjcPRhbTR0h0BdHHxRR8IbMG-tY0mWLsPe6q8rsorLU-7Jd8E4S7c0ivgYvjhow_W-9L3kxNNpGMHT-X8Fiolhv5ZXiVok67nbD7sfdiqyfJl1MUS1HLP6uLgoW-njpb4-ZAGXSL1AVPmP9OBBhu4i3_TPipFG3N2ryutLeS9M4eIl4muoLUNSyG_7-duybjLdf3LrfvmEDI-IRIN5agEkQjPMCgKdw9nSolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQGLcY8NRlxBjakxcZIAxbpvFHMy69VDTlFOi6fxDpAoBeM3nbmHeqDkXiIwUlTElvqKQERQlTFvFhHdhuTHkiC960s8qs0wBZha_nXuZS577MMKy6hw_9AE8eNHTgJxo1DB4t6NnOmCNkJLYjF2qQu43-rW7j3JcI7NC6Lkug1PQGQ5RQTUNP3sYvtsEPP9bN-HNfiZgd5gU6-K6DGTnqkj6VH8X1q8Uq_E0tUj0zXEQRdIFQ1IrXTzaxGco8q1uQ80wy3_m-o1kJQCe9vUUBjoqL2mJVjEqanlD8Zx6f6RrgUnwdefvbswBwKapU3qJ1g5XFgL90yVKzM3A3Lpxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع دوقلوهای شیرازی در هفتادوسومین شب اقتدار
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435275" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">کلانتری: رضا کیانیان از ژاپن پولی نگرفته است
🔹
رئیس سابق سازمان محیط‌زیست در گفت‌وگو با فارس: رضا کیانیان پولی از جایکا نگرفته که به من بدهد، اگر گرفته اثبات کند.
🔹
اصلا او از جایگاه جایکا اطلاعی ندارد و آنها پول به فرد نمی‌دهند، خواستم شکایت کنم اما دیدم از روی بی‌اطلاعی این حرف‌ها را می‌گوید و یا شاید ‌دنبال بزرگ کردن خودش است.
🔸
رضا کیانیان، بازیگر سینما پیش‌تر اعلام کرده: سازمان ملل از طریق دولت ژاپن سه میلیون دلار( معادل هزینۀ آبیاری بارانی یک میلیون هکتار) به‌ حساب او واریز کرده و او این مبلغ را به عیسی کلانتری تحویل داده اما از سرنوشت این پول بی‌اطلاع است.
@farseconomy
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/435274" target="_blank">📅 10:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e702dbb501.mp4?token=QTiSZEkKzI4pN5VYutDLAcJBItXXyJRGfal1r1gTmUuszgRQHqTCfI4fE7GnB2uQMNVI3H0fXMf0D9ENIfbMDfu1KDxQFqKv_Hd4M8rBIOsfY5FVA2YNQ0KJVQX5GtvfGaBKxbehOCDT6JmWAop0lPYstvT5z4Wa8PjQJMg_-6wkBEozTOEyodv4cHPrZOoGOibwMoJ3EC0969Eqmmc0XShFZNKvdqrUDzAz3RH-HOk02Q8DlUwfTKsZiLgR6HOQYJ_htwUOeFIlYNp1qaQszDTpA7O6ngd5bLD8kMd_sHksa7f95NEwfkFwb_iZYBY0c3cb7y0lDroooED-hoodNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e702dbb501.mp4?token=QTiSZEkKzI4pN5VYutDLAcJBItXXyJRGfal1r1gTmUuszgRQHqTCfI4fE7GnB2uQMNVI3H0fXMf0D9ENIfbMDfu1KDxQFqKv_Hd4M8rBIOsfY5FVA2YNQ0KJVQX5GtvfGaBKxbehOCDT6JmWAop0lPYstvT5z4Wa8PjQJMg_-6wkBEozTOEyodv4cHPrZOoGOibwMoJ3EC0969Eqmmc0XShFZNKvdqrUDzAz3RH-HOk02Q8DlUwfTKsZiLgR6HOQYJ_htwUOeFIlYNp1qaQszDTpA7O6ngd5bLD8kMd_sHksa7f95NEwfkFwb_iZYBY0c3cb7y0lDroooED-hoodNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی فوتبال از میدان انقلاب به جام جهانی بدرقه می‌شود
🔹
معاون امنیتی استانداری تهران: در حمایت از تیم ملی فوتبال کشورمان برای حضور در بازی‌های جام جهانی، آیین بدرقه چهارشنبه‌شب ۲۳ اردیبهشت همزمان با اجتماع ملت غیور ایران در میدان انقلاب اسلامی برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435273" target="_blank">📅 10:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5acc6517.mp4?token=SjdfP36TO0rzcLeA5OvyrDUKjNdJKbQCiY4_A3my1MHpKwznNkuQ6upa8Q5HhCGkrT9OjKH6i6yYxp73C2DIcvMmOO4aZKY0FF7nEaes1b0QZ2m3dzJJYah5dERZEBr4nFHqteWQKrhR2fJ2rEqHtVbv33ciPYjU0oYUiWv1gR5YxGxVMttciVWUHvdGHzkLVzVn_JlP1hckZ_JIEjKKU_KCOwl2rvHt_AFlqJPShD7I43IPmZuKwYvYcMtrS334et_tL35lR7wk8ZcBUpeSjSMqablEBTFwVwJMOCEmaY306zfHr9rYDg4hU3pFh9GQAjepg7P6XliHc4QiPykz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5acc6517.mp4?token=SjdfP36TO0rzcLeA5OvyrDUKjNdJKbQCiY4_A3my1MHpKwznNkuQ6upa8Q5HhCGkrT9OjKH6i6yYxp73C2DIcvMmOO4aZKY0FF7nEaes1b0QZ2m3dzJJYah5dERZEBr4nFHqteWQKrhR2fJ2rEqHtVbv33ciPYjU0oYUiWv1gR5YxGxVMttciVWUHvdGHzkLVzVn_JlP1hckZ_JIEjKKU_KCOwl2rvHt_AFlqJPShD7I43IPmZuKwYvYcMtrS334et_tL35lR7wk8ZcBUpeSjSMqablEBTFwVwJMOCEmaY306zfHr9rYDg4hU3pFh9GQAjepg7P6XliHc4QiPykz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان افرشته، جاسوس موساد اعدام شد
🔹
احسان افرشته، فرزند مصطفی که به اتهام جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شده بود پس از طی فرآیند کامل آیین دادرسی کیفری و تایید و ابرام حکم در دیوان عالی کشور بامداد امروز به سزای اعمالش رسید…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435272" target="_blank">📅 10:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccj6ZheJYmEE6_vLx7tqSnr3wUpnYGG6TDAfxHAp1aNCO3Giv7JfSUx9_dGW2CVDyhQK1C8YIDSw0MdS4UInCUqgiMRpkSTm8Hoj2jlBPWMErqyAT5N6iX3dpFciCjCKO_HtlcqGxkhLs4Uk0Rd15b6EZOoOW9l3PmRwgjqWpFGsINEJYMZUCGgB94AAxWtQ7SR_RREDIV3ELx4VzgWs8fk7zE64sTrQQqU7mZrLX9EJW9WLv7P7NVAYl5TQUut_Yji3nxe9VRTnHjhlLWKZXMSy4tJJBRKslZchxmicTjUp9Ov4owJs80odxxfqZFIRa1CnIsm6T1maociXo-KAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماموریت ویژۀ رئیس‌جمهور به معاون اول در سِمت جدید
🔹
پزشکیان نظر به ضرورت فوری استقرار حکمرانی یکپارچه، منسجم و کارآمد در فضای مجازی عارف را با حفظ سمت به‌عنوان رئیس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب کرد.
🔹
رئیس‌جمهور همچنین «تدوین و اجرای نقشۀ راه جامع تحول در حکمرانی فضای مجازی»، «بازآرایی ساختارهای تصمیم‌سازی و تصمیم‌گیری از جمله ساماندهی و ارتقای کارآمدی دبیرخانه شورای‌عالی و مرکز ملی فضای مجازی» و نیز «استقرار نظام نظارت راهبردی و پایش مستمر عملکرد دستگاه‌ها در این حوزه» را از جمله مأموریت‌های محوله به عارف در این سمت برشمرده است.
🔹
در حکم پزشکیان آمده: کلیۀ وزارتخانه‌ها، دستگاه‌های اجرایی، نهادها و سازمان‌های عمومی و حاکمیتی، موظف به همکاری کامل و مؤثر با این ستاد در چارچوب قوانین و مقررات و اجرای دقیق هماهنگی‌ها و تصمیمات ابلاغی می‌باشند.
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/435271" target="_blank">📅 10:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435264">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-gojYoXcgc_1dgnzNq2ff4xGt0hBnD8KMPrR9x2f3Wih1J6d4d8CjktqrEt2nnT7VScOyLJjZyYiNh1K2HVbtyyjPYMWRrwx0LbMET4xAYxjCgo_sDB3lqfB_83fOnQ8fu_sgpd1bMUiS3IZC_OTcAp19ll6MHKn1UzAHnO6--kprkPswOZ4GiBXaq-DlXdtB3KcGa5zf5Jb3U8zZdrHC7vWwJeu43vL7quMxQFOuLiNs1jfe8h-a7FED0uvkoANBBn73uyWEc0141Qpcdvxkd34MUuVrNsZd8DBq-pZjF-QhDqHpZzk1M69p0ncH0AOmkC1WW8LWyLP4W9MWZtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md4Pd8u65uZs3ZKUZaLZRnmyTnhLC0NwehHtLX6h8t3ieAmz2eB6p0C7roz5UcNU22pGtSwYW4_dxvUYies5gkLCCeZ9oyCFeRCAUrNCF5SRARUYydgO-8skBKEnjly_S2coOulaTHMjAzcsFdF7xRSofZznqUyLZlIR5xykCuxf2X_EdbpDFI5IIxVqvf62dCxfu0gmkr1MIDyB4FtG_7hiboKTrzGQPY_zyZy3kO-uhU83dLmnEO3ZeDddmmomKAydqyi9YpHzHOeh_0NiQVu7WvYiGaT9TGrjGLbPQYU2aHGrc7PF55412vQC-ELoumCw7ZI-iHVJ2P5_nnU6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOvXGBl3JGimByHtySuLAZm_4FYnKN6lPxxejt33gOdx6kxLOjHEuuAxDsy8xx69InGn9AMj1wrkAEyFa1aw8WWTvzkp4vhrBg66NJnUoCI7IhJDj52EsrrG77ndxpqFu-HzY8klLLHUDpTCxja1vLE-YlSb0NvZpdGsHJHQln9NJw3mc76KxBxSQ_GRxhs955p-CcZaHOc5qSXO5luQOZGUMMcRRFUyPj-CopXnfhcMCSPOdH2Jm9FLq2eLkn4NDnHtMZ5BwJ1MKh7yqznuLL2IDaMAZbXD2xJG1J0TKdqGEbs6Uf-P7kbb04bxIQaiXCSU61F001-B-SzN6PhN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWqOf3gmYJC5PLO1ckCHo7gRT9vgn-xxBrFS5-jEFI3tC7WfI-KgaRnhRsZ_3tBYmC65tWOoq1ViIenG5-0My7_86l2pTJ11ks_wUzd1HQtUg-cAq-dP-L6JgJfzGju2S8YqYN0gHqTQLE3X9OD1D4it0CfeK0XArH65V-z3BgXb8fD-SetEjku92FN8SxTU88DuH30lA-vXZw3nWLjK-AdiXqnzz-2qZhWBbh02XNi1ybRVheHr2r-zGzpHqGKSJTyKXqB1YnamXRypfVY_wVBoROzO2c4bpy3lgZ7P5-O0qKwPQYPxG0GxPbvZaHFSIFQiiWt_nt3MmtRCpSme8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7-fp1Y8vDVyihkYY3VVAuMB-66T5szHZv5jErmsik2eubZODUYlzUHSpIzVTIklmoLkRzUtL2HCW9Bx9mRXKPDbUQgqMkJxX-48VaOLCqXRa7E7D_DcHlbqc_Yjhi_0UWbdNzxMCQR1I5jPrCBtHi6loPvFg7xOIXbr6Lsi70M8hCh03kMLaM3vNhy5VKnIVQYCJPn_6Ts-AUNjQSXv-6za4TFnLMht5uUeRVWiS7-j9Jb1tjDyuP62Tx63BzeWgbKSqSxlWhodi0tDNjm9Dsr1G0L0wx8WWp8J1Guj29pBlWwgh5v9FxpQK_isdpN0B9BKGDVK4XA-YpcaNDYH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDwm49O66_SggFQCMC--BZeIUN7z1gDKHEM9lRouQoXd6nEnaStkMkEjU9UScME7Am-IMvMuVaJoU55kKyEiJSl_odoZMeCoITVrOOhfqbb04wzlW_8nwGQmU9s1NJjHdIo64WlgECsmZSUACMf2KxyaFige59TowSJiCh-1-OfXDEpKtG6IbFj5Vvo31gBh_GbjhyOBO2mTCH3_2RvQvIhNEWNBQuuJpzom-YUZnZdUts8-sVzjS9Qn9uZP6uhigZClTUiBxzToFFk3C-eVwQMB6kdhIwcgT_-UPxzY9avXc-KUQ1PSBznDeHwy8clAroPOkA1RBt329v015cHQ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور اعضای تیم ملی کشتی آزاد در چایخانۀ امام رضا (ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/435264" target="_blank">📅 09:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
ویژه برنامۀ سپاه تهران برای گرامیداشت شهدا
🔹
معاون فرهنگی سپاه محمد رسول‌‌الله تهران: در میادین برنامه‌ریزی انجام داده‌ایم که براساس آن، هر شب به‌نام یک شهید تمثالش در تمامی میادین نصب می‌شود.
🔹
در میادین سیرۀ زندگی شهید، اقداماتی که انجام داده و دستاوردهایی که به‌دست آورده، برای مردم بیان خواهد شد.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/435263" target="_blank">📅 09:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435262">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcba5805d.mp4?token=NRJRx1IQenAbAtE2TrvY8UbzMC1GTa6SB8kJVb2WO2qkL5WgkPeCqhwFaxhAiIQdIJG_UDqCU5ZoUvGqmuQ3kTqVGIp98fNT2ThkH8Z0XayeL_2uRLG2pnkozoNxHEDaQ2-gbu40fAG96uyqW2UAL8XWP0kTfIl-7WZ_AM_eFk0kyfxHzuf8tjl_0ml_B6vYZIYSAg0O8vD9n35L1Pg3m04OG0pq1x-kKiKIU6s2Ol_H47TLjCXOEwtXSeFn6tTjsz3FEdjsek_9YuBNKUW8gSZH1c0Fc1tlVeFymplWoSFZ_OH34eWszfhNJZJtst2jftsXI_TveRfSDTFvADFtwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcba5805d.mp4?token=NRJRx1IQenAbAtE2TrvY8UbzMC1GTa6SB8kJVb2WO2qkL5WgkPeCqhwFaxhAiIQdIJG_UDqCU5ZoUvGqmuQ3kTqVGIp98fNT2ThkH8Z0XayeL_2uRLG2pnkozoNxHEDaQ2-gbu40fAG96uyqW2UAL8XWP0kTfIl-7WZ_AM_eFk0kyfxHzuf8tjl_0ml_B6vYZIYSAg0O8vD9n35L1Pg3m04OG0pq1x-kKiKIU6s2Ol_H47TLjCXOEwtXSeFn6tTjsz3FEdjsek_9YuBNKUW8gSZH1c0Fc1tlVeFymplWoSFZ_OH34eWszfhNJZJtst2jftsXI_TveRfSDTFvADFtwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد زنی در صورت پهلوی در واشنگتن: شرم بر شما
🔹
یک زن معترض به جنگ آمریکا علیه ایران در جریان نشست روز گذشته نشریه آمریکایی پولتیکو و کارخانه اسلحه‌سازی لاکهید در واشنگتن، که رضا پهلوی در آن سخنرانی می‌کرد، فریاد زد «شرم بر شما!»
🔹
وی در حالیکه فریاد می‌زد، خطاب به پهلوی گفت «شما کجا بودید وقتی مردم ما داشتند فرزندانشان را از زیر آوار بمب‌هایی که شما به کشورمان دعوت کرده‌اید بیرون می‌کشیدند؟ چطور می‌توانید بگویید «مردم من! ایران من!» و بعد‌ آنها را دعوت به بمباران مردم کنید؟ شرم بر شما!»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/435262" target="_blank">📅 08:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4-iRZXcBpTuJNClaT2S4fcY9dC73DlNnWxxhvCHLojhpv_a63_lKuSnnmdpedsdUuUj5DvWtZ10txvWsVMBKRx8n-TWht9rrMD93co1Y8_9jodgk8fnP0JE--lGTlWNBNUi36_tR1CrstWsc22yL2asxcu26v4Z5sAHsYi1BQZSTMs3z1Tb0sDFlz7CwJ7xoYS3rcNJRRJnDlBUDNhLi5nNAiraRr7n3jdCBnrSjrqMasliZw0QHO8SHbWOdijvpOKxU3xuyYU3Px8i2WNzHXPCbPR-DpyM2I57KBc4zViUKUziQYfDkkoE3yEsz31rRRtu2Wsb7VYhmP2CcIVkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhNmHbh_AKIa9Rn0g8vyMMLU8c5xZFcG2iESANsZG41Sgaaz8ux7sqONuwoUQKXHjGncnWUYZ4dBr-vZ6MurL_5aNcCruamlZAsQq-WNHoUDhr4tU8Drfqjj0bmcrQ4jHDBUCyZZsa4zkns4SWtifbSxU4MrTCI4PJ50SlYLZ188NVlIkXNX2qsLE_l0U5cS3lGHOuLpk8e9Wlz_JHrGMX7zB4SmwMpUNebZBFBK6YjaUpgugclLDuERbil6YhkIWiSuYPHkoC3qForDU8qBDzLw1bE80xcP5KaQY2BPc2jDxp6nklRN6QlyyBD_St-aryQgRWKzGLiRkVU1DrUN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-3dZeiD63yDSQQxVXdZKiHT7tddx0SuUkEQ9rthOcGOqlE4EVE4-Gitn2C13hJ0xJ5JYl1huI1ZQ8KP3jybumgs040r7XTc0a-Xgn8r8lFTeD5EzIvSLdqtHDC4l2yyHz_3kqNEGLyQGxn6KiSXFYzNTOq5Z7m1Aaid2u43Bs-BkBnNZ1Y5j6CHkDUW3wy95VsVHfd1bGbRH920_mvKpZwx2Vkg_vKbKi7dduPe-XgK7J8yG8z6pPnJDj6K6Pst6E-JIMsCLecc_wDaXq4ciQKQS-7nRQRRMDHmXm17NxMFRyH8t3d-tQg0AhG8vI-PDiScfrw-Q3zCkDs5mDj2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYj2ACSJgLY0I_YbVck3s8RB0jKzxD3mlWpVNwAsA_bFdpfbBtyeRjT8bk_ibqP6nDWArB6vDDrpxxZ-pLOvtSUIn5nXbaGA7LcNQ8p_-2KTP7HwVhHk3NVgqftLNgf49MG4a4_gNiGIM6Xx6J9GNsV16cMkEKNLdkHASok3A3dG7oFA6ix2o9UNZUeHRebsrj93ZxRazuq9XH3obPoKnHuYyRahY9GL79xS-pFMb338pmfsI7XO9-DEiU0hvpILuYiQp32g0HDCxxueLTKXWlNTyt0NSwqF-kJmr7t9dU8k8r9tKrdVL7k5Sabo8z3Xn4kslZiv6kQ6uoeT9StwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpSz-Jq_-9H5YoMiAyzCLkmUVMvIrs5-NM8p-seA3I2H8xdlw2h9OfLTxzh82DqLV_E5NGC8Kj-7a4kyv_DvJCCEf2TCiE_eypRT5p9oUAuW8YIwF2pioEwBMT8PYHL_7p6pdsR-ycqd1AZ8cGnltNtWJdP0uIqBZAVHQJzaG2Lv-dfToymmzq8bT8LpQGTH6qJTnmqh9KwLeRXJQdxkvDsaaTv8myXOZV14ftZ2udYYdh3B0JX9CyJ1Gg7M___20XLAYerYrII56pgV9yn1fPnI3bbEqoft4Y9bEOawqLmnufiCZIQHbzN2xmfmkqxtewBffFuGbI__ubO_F_oFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdEsOr6u7_LZanSOhRU-mGGbMsJRJvXkB_9g4evGkb915Ekz1GUF2jFLFGNvUTYdeg0jbjsLfgsiutKrCCmkFEm1kbp8WDB_zce32j8gZn7Iwzp8EOVx-a2xErIkQMuP7cdnvJqhFkBCb59h2hATcxBQSnOZuHwLSNt1hDYw-rv625Afedbssq1u50JPQdNe_cjNYEtJYzSKkYI8cadQHPcbV4aDvOPZ3Wz-OgsIq_-860CTiS6hxYINT4QykF017i3vcjV8cmVZWH6x4XnvDBXqvvcN2Gz25kxHpGIvUVbjsXrNk2hARbvYweNLCjS4o7jbIV2o_JC3u49zq0hkHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احسان افرشته، جاسوس موساد اعدام شد
🔹
احسان افرشته، فرزند مصطفی که به اتهام جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شده بود پس از طی فرآیند کامل آیین دادرسی کیفری و تایید و ابرام حکم در دیوان عالی کشور بامداد امروز به سزای اعمالش رسید و به دار مجازات آویخته شد.
🔹
او از بدو ارتباط با اولین افسر موساد چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند. افرشته در ابتدا در پوشش راننده تاکسی اینترنتی دستورات افسران موساد را اجرا می‌کرد.
🔹
افرشته در طول همکاری با رژیم صهیونیستی به زبان‌های انگلیسی، فرانسه و عبری مسلط شده و نام سازمانی او نزد سرویس موساد «جیمز» بوده است.
🔹
محکوم در طول همکاری خود با موساد حداقل ماهانه ۴ الی ۵ پست الکترونیک فارغ از تماس‌های صوتی و... با افسران اطلاعاتی موساد داشته و بیش از ۳۰۰ پیام بین آنها رد و بدل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/435256" target="_blank">📅 08:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSb25O97mVisVf6nq02ok2xSkoXpEmW3VkuBfQmhDmkXgUGP9zds-fQA9Hw0gkQrLACF3w3Gz-k-sC_6YdOpsv3da9rzpCQzLkQMOoVk9-M7j6i1PsT2-d0jttl2J92oWj_CsOVGU8BwhhTR8vlYS9h48eAefTmFTPo6u1H1Q-eyyZ-DEtuyNqOXLwhmm0QCg1I6xTHki0ZMdlM0uS49viYNxr5zQ8w852OegU-8lbVJLeBBQmp5Z01NYXgN529I9F8kSDBENf6CUJ16h0ulogNpV-S3ix3d_tahpREc2xB4EMXIXQ8jgs-R4WGwoVNGAIAyz_Diqip-fUjsSn7A5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت ۳۰ میلیون تنی که محاصره را دور می‌زند
🔹
در حالی که تنگۀ هرمز به گلوگاه تحریم‌های آمریکایی تبدیل شده، دریای خزر به خط مقدم تاب‌آوری اقتصادی ایران بدل شده است.
🔹
استاندار گیلان می‌گوید که بنادر شمالی ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند؛ رقمی که معادل کل نیاز وارداتی کشور در سال گذشته است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/435255" target="_blank">📅 07:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیش‌بینی رگبار و رعدوبرق در ۱۸ استان
🔹
هواشناسی: امروز چهارشنبه در برخی مناطق استان‌های آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان، مازندران، ارتفاعات گلستان و سمنان، کردستان، زنجان، قزوین، البرز، تهران، قم، همدان، مرکزی و برخی نقاط واقع در جنوب خراسان رضوی، شمال خراسان جنوبی و شرق یزد، رگبار و رعدوبرق و وزش باد شدید موقت، گاهی همراه با گردوخاک و در نقاط مستعد بارش تگرگ پیش‌بینی می‌شود.
🔸
امروز آسمان تهران قسمتی نیمه ابری همراه با وزش باد، گاهی افزایش ابر، وزش باد شدید و رگبار و رعدوبرق است.
🔹
جمعه با ورود سامانۀ بارشی جدید از شمال‌غرب و غرب کشور، بارش در این مناطق آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/435254" target="_blank">📅 07:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎥
روایت مجری ثریا از مدافعان هرمز: در گرمایی که تحملش دشوار است، رزمندگان ما ۲۴ ساعته در جزیرۀ هرمز از وطن پاسداری می‌کنند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/435253" target="_blank">📅 07:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmOyVAwA90vNZ--pvCaYhCfMCWZjg0TMe9mzR0hBk9F0CgSUitxXBFASodrThQW6XL7AdPwggmzxBatwlbHqF4tbPBAecXTm7GFylvt-3tpqqrl2HvWtriYPbV4QVEbnkAfdgYY7M459Xrxgl15Smhntp7aD8gR98QNksNWskk9APNjFx6UfRBpy2VVoqMs7--txy4oFqStw7AD5JO_OBi7i0q6cHQVODOUyQlZHYjp_qlE3HuOkohGgt15LDv-w8_gJLHnYINMjOwF8rx6F5pjiLQahpvhmu7sDFXB77v3O2pyP715PW75ndQALQGHSsAYrRiRCsQay3sNngG6o0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: انبار کالاهای اساسی تا ۶ ماه آینده پر است
🔹
معاون خدمات شهری: مردم اطمینان داشته باشند که با تأمین گسترده کالا در ۳۱۵ میدان میوه‌وتره‌بار، تا شش‌ماه آینده هیچ کمبودی در کالاهای اساسی نخواهیم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/435252" target="_blank">📅 06:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXwno-A4gYg3yhBN_3VlqXbl8ctHfXdjYmtBCUH9y2YXqLfMsuXM1Y6HMjMpHyyRFkr8Oj9vVaN3Ig7bCSyFtU8ETcQgcRzzvipyjxrhf6483s5a11IVTSO3gf7SltAYD7YWk1n7ofjAilWkCDQqkoFy7XNFT8Y3c7p_Rfsb63gq6ebe_ikNIq86GyLjghSiR2-5-h6wT8nwhy6w9Stp0OOfibh8XwjB9_PTqbIaYMTCQ8cujuiYTawKv1d0eZG0EmaluoS_iHh2zRz8CCeS8hlBuUYJAZnlDF0-zrnu1Xb1wqZhg9HtkVELPKRtaDoJaTOraGlp4_bESyMI8FocHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف خبر توافقی مهم از سایت دولت آمریکا
🔹
وزارت بازرگانی آمریکا صفحه مربوط به توافق خود با شرکت‌های گوگل، مایکروسافت و ایکس‌ای‌آی برای آزمایش امنیتی مدل‌های جدید هوش مصنوعی را از وب‌سایت خود حذف کرده است.
🔹
لینکی که پیش‌تر جزئیات این همکاری را توضیح می‌داد، اکنون به صفحه «یافت نشد» هدایت می‌شود و بعداً به سایت «مرکز استانداردها و نوآوری هوش مصنوعی» منتقل شده است.
🔹
طبق این توافق که چند روز پیش اعلام شده بود، شرکت‌های فناوری قرار بود مدل‌های پیشرفته خود را پیش از عرضه عمومی در اختیار دولت قرار دهند تا از نظر خطرات و آسیب‌پذیری‌های امنیتی بررسی شوند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/435251" target="_blank">📅 06:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o93HJNhd73YuNh21LSNzMYb7UXMaTZyj2U6vq3No-pty-oFOSl3DF5XQnfd53aedDR5YWgYSMPR7dskpj4z0U5Q-XuMGp5Ep67XEhVL80keqB4ihvp_wbZazQYFhcOfrUTCyOOqp5QMa4o-9HOPmhL5Hgm3m-6Qz1khIPkANQ9s7EDJu-4T2mnqw2NCy9LmAJFjRgMIMQ15lz9JdtL-UCyMZs2TzhWDlVK9Cekha1eYrWA2OPW-Ref4ZpRh0-6WEX2940wFmREmzwhWNRzpRA91Ov_tRlZxYKhM0pvYlUCPCfkBinYHkv5hFJUhJAI9cGuH7RvkgSQcV2Djv6dou0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای مسدود شدن شبانۀ تونل‌های پایتخت چیست؟
🔹
در ماه‌های اخیر بارها اخباری از مسدود شدن شبانۀ تونل‌های تهران در رسانه‌ها منتشر شده و دلیل بسته شدن شبانه تونل‌های پایتخت سؤال بسیاری از شهروندان تهرانی است.
🔹
مدیرعامل شرکت کنترل ترافیک تهران می‌گوید: انسدادهای موقت تونل‌های شهری عمدتاً با هدف انجام عملیات فنی، نگهداری و ارتقای ایمنی زیرساخت‌های ترافیکی انجام می‌شود تا عملکرد تجهیزات حیاتی این تونل‌ها در سطح مطلوب حفظ شود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/435250" target="_blank">📅 05:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2k_GZFeeM5x51cRer4C4efZgeAI0kRix4MIgUikon5P6O8x-cARrHKqp2bRt5hAn0rrMCZxMSfq0mLJAD5tb2j5JIZY_uTqhNE_G7Y-LwiqAjOtNMdG5Y7Tsh11p4j2FXx2VWBQ_9Su-Ov5kKFzhx0EdRODA-fhrzucjWUN_7xkZ942JlsN1wukrZVK_MbcS4bDu1tm6Ed5quTLPYRvVwbE_nLL6b2GVk-RaBmspF9ob_BBr-2j8GDaCw-qe1vS799C0pCQogQ-va_6t7ljC__KEbbiX4ANzKK1lVTVYLklt_KEJa_-_YUSb5nRzvV8b-VUQAv3bg3IH7_g4NaFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: پاکستان میانجی‌گری بین آمریکا و ایران را تشدید کند
🔹
وزیر خارجۀ چین در گفت‌وگو با همتای پاکستانی خود، بر تداوم حمایت پکن از میانجی‌گری بین آمریکا و ایران، و مشارکت در این روند تاکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/435249" target="_blank">📅 05:17 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
