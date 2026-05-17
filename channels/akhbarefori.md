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
<img src="https://cdn4.telesco.pe/file/BH5E-dUd-WW-7ytskn_GF3xtuhInPFbmfSyRK71mnm8TjkcVVxTYhhtxF4aNjGRAqbhaRdOZPmbO6enerQDrqgdWmBePPvQY3HZhgdDBUX8jtwXu3BhVbCXlQf34zQsHnF4haykmaNrPDaW8hST-1lx1SRt1IGEfQHMbEQwXxzDkiA8MkAbRUKLNxdxXuTo8erI5VbsMqWIRz1dIsR62Ny0Ud3HOwpfL30aqA-bfjbABa9xR-_EzzZRWL80ovIU4_vPl033mpG3VLfcgwxjNEDBcIcbTDBRHxexhzVwi2oPSR9aasAuXGUtUNNanS7r_gVATz8tOOZaL58CdwMaYXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 01:42:18</div>
<hr>

<div class="tg-post" id="msg-652742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
هیچ جایگزینی برای تنگه هرمز وجود ندارد
🔹
کشورهای عربی حاشیه خلیج فارس به دنبال مختل شدن صادرات نفت‌ و گازشان به دنبال مسیرهای جایگزین خط لوله برای تنگه هرمز هستند.
🔹
این راهکارها پرهزینه، ناکافی و در برابر حملات هوایی آسیب‌پذیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/akhbarefori/652742" target="_blank">📅 01:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پروژه استراتوس؛ معادل انفجار ۲۳ بمب اتمی در بیابان یوتای آمریکا!
🔹
یک ابر مرکز داده به نام «پروژه استراتوس» در آمریکا، آنقدر انرژی می‌بلعد و گرما پس می‌دهد که هر ۲۴ ساعت، معادل ۲۳ بمب اتم گرما وارد محیط می‌شود. این پروژه‌ عظیم تا ۹ گیگاوات برق مصرف می‌کند.
🔹
پروژه با ژنراتورهای گازی مستقل کار می‌کند، بنابراین این گرما در یک نقطه متمرکز می‌ماند. گویی یک آتشفشان تکنولوژیک در دل کویر روشن شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/akhbarefori/652741" target="_blank">📅 00:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuXYYAXauC8RBBIqB3YyVCjB7BSU5qUWs8iraYJ8GVQcmYy_uRahn23u4YaSqk4YKg8RX4r5LY7wn-yEzOi0xGvJl814-pX752XzIDpnc-_DhMEePC20aTqD7xfDAA29LhIRAAn4krT5QDgeKh6-IWnypbwnq4NcmbUF-FdFgRc0E0O7j4aaKQZHCIa92SYFLxtlRUjak8MZ1k5h9JYqyvzoRIH45MstBxugF4EtusJVsVClOrWh1CIVv7GH-odR3q2hHuqScWi_XCFo-lUg5PezWFHEx3KLftvf4qQgi2qg_exc9btlPxa9Z1R13PKwY6SYl_yukWuc2q-HQJxnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بغداد: اجازه نمی‌دهیم عراق سکویی برای حمله به کشورهای دیگر شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652740" target="_blank">📅 00:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSBoRTEpiqBtjLVEJ7kp6wKpCgaUEs-_iorOq6ZQUrT032mmhD83U4znh40JPCdAdOIOffndzICDBxCvjyw9FA0XHo-LzdtIEU6GUF-F09033hCh4MuA75jaiWbmlGC8chMs1bww7cn8VkaIo0HJzUDN_3UoRhDnfBr0zHL0cOPusEVgzRAAYXYOFSQbnnGpTLQngGwrIe3mrtc1wPGwP-bSgfRyKCP7lr6Vc2ISm-FV05UFa1YmLfGI7nhfGTVsfyEsdUnJ4cb1u6Vp_L-VH8EROIWIudTs6dcPQOC08wHv9zVHT0_F8kDc2HIeMg29eknDNc0u2Uz5l6sjYrqbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ft_4ABr6IcehCRy5y5RqiX9RU4KPPMOwg7pKyhxcrRqVLzJsuh-Ue-2zkpV_aywxedgE-UvsuzDNSA1X0dZoAq1xxzVIJIhF9M4UdmFxiWpNDFKLKOCJM394nrfUvzkHI4_AxAOM0BQEjnvCpWvqdCnBOM0ItZUakJq7TnM8YN5RC5GbkVpdSOePesLtnq7gFqWzvtfdKLgtfmHdPKojVFx0AZbZgjDmDQkh8Aps-0nni269VG5D20QWtAEv7QcylPtvl1p4PmgE74AbhgNMEAlu7HnqUW1uSKRqD609b29mu3el119YI7NkJDqrCgXSYUccQ64hc5UEQ4Atpb6NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFG8IO76F-jhMg2C_f35LOl0qXL7-0H0xfd2XKFLxVJE6Yiq-G6PUv_J-yTPyhmAOLDV1bRethiAWZlvppXhMjH4XA74LA0-mla1id7Ne4G5a2exHyZghtBj-4MjI74HAsu0P3_Jv0JWtEmLIlENc8lqAWHyckpl2e2dmKPoZop-0_tYnXVAFT9cQvyRyFaoEHuZeb5bhOKY0sJ0QImLw-ChUewMMD_8x8EHnuE1OppVMkgyQ97KiwbeMb27B5rXTLTnWG_061E44bccRGSPQLPB4x-bI3uGX2KCTgIFBiLqhhqQhkAcqLnZeOKvd3BiZhjx9EAEAnUBV1ixfJASUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OETyh0cr7BZQK3i6JHl9pZCSSmEOkplq871mM9ef_ggRe3QXL8QOsRARvQYGW5rHRtM_MTfxBt8gbQ-IOmIUWkoh306JzGAfMD0MOL1jDfwz8VZuO0xzSDMaHmCwn7HaGAf8zS4MKC974_ohzmnmLErQrr_HsEloc5gQtsjeqmWNGwkVXx_mKYeAKH1ghhDuY2EzkpLAOFZ-8O0WiuDavxg_1KDIhrcRfSzuHlVyvM0KYqljVlfcwMMbHd6kQBWbG7gpwNOILaAcPa07SElj3yYGkS4jE28CIa2bZ6Sc_BW86MQIOFqw4V8kjz5i56XkCDHWmXnVWXnYz1oSkCJXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fu5HhHSJ19QkGTaSuSYI22BsOxFiK2p2eKyT3BgZ6ehiF27QpJqWd7YGHY4HKAXP67dipl-3IvdMGVQqS8NhByyN06OFo7aF64cSRvaFSu3j0NLh8l7Og8Nc1b2RsL29Jw5m5K5_7V2NUpNzZK6X_K4FiMITFquDF6nxFuQUp0hbDQJsrmtA47SgUQYXq0rv81eDb5QV3kVsEsZbzcb9zuvQ5l3vp7z9-SmDzkik3R-5g8s40CXANcWT2inx3VcM7ahjmAXo4h_ozm6xGcJ_CPk4DFR-bEA9X_DcvH3nfFu7HU7kKTV5L_JpPHCKG1r5QuNIv2AOLKJLMWRDLEj0jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تنگه هرمز می‌تواند آمریکا را به توافق بکشاند؟
🔹
ادامه بسته‌ ماندن تنگه هرمز در پی تنش میان ایران و آمریکا، به‌عنوان بزرگ‌ترین تهدید عرضه نفت در دهه اخیر مطرح شده است.
🔹
مؤسسه Continuum Economics با بررسی سه سناریو بر اساس مدت اختلال و واکنش جهانی، احتمال مصالحه میان ایران و آمریکا را ۸۰ درصد برآورد کرده است. نتایج این داده‌ها را در این اسلایدها ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/652735" target="_blank">📅 00:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
از خبرها و تحلیل‌های جنجالی امروز غافل نمانید
🔹
🔹
خبرهای لحظه به لحظه از تحولات منطقه | ترامپ تهدید کرد، جنگ نزدیک است!
👇
khabarfoori.com/fa/tiny/news-3215612
🔹
اموال این بلاگرها و سلبریتی ها توقیف شد + لیست
👇
khabarfoori.com/fa/tiny/news-3215517
🔹
جنگ سوم ایران و آمریکا چگونه خواهد بود | از تداوم ترور تا نبرد بزرگ در خلیج فارس
👇
khabarfoori.com/fa/tiny/news-3215690
🔹
ماجرای حمله پهپادی امروز به امارات چه بود؟
👇
khabarfoori.com/fa/tiny/news-3215668
🔹
تحلیل آخرین قیمت‌ها در بازار | مورد عجیب ریزش طلا و گرانی پوشک
👇
khabarfoori.com/fa/tiny/news-3215805
🔹
در آپارات خبرفوری، ویدئوهای خبرساز را ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/652734" target="_blank">📅 00:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdqL9ZQhFmmXHOoz3A8UQzY9ExBbZM4fseYg5xsPigV6sOqwYs409DVbP6OHFr1_ffMWO0XFA_XY4lZ1saEDkoxwZY_YM_5FU0_h-zz5j4b1SmhFLJ_TjgVdLJa7KnXgy5dnMdqgkarEulb6dFCOxbuPthNAhcIvjb17QOHSW5HHSiSaQ67sM1Vtv7bSuPHjIy3UnUHl4HYUjjoTQPbyIQZOXoe8oGwN9i4ShFKXhxWtNegCzCNjA6zbcd_uaS7rlRVUEI78Ejg-_aSREl6bOpRg4cxvbhhTXTFsKJjYtBd0yt4rm7VBZgnCvItVqTX_srvpTWWE6gvyE7nrOgU-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عربستان در حمله پهپادی از عراق
🔹
سرلشکر ترکی المالکی، سخنگوی وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح امروز یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شد.
🔹
المالکی اظهار داشت که عربستان حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند و علیه هرگونه تلاشی برای تعدی به حاکمیت و امنیت این کشور، اقدامات عملیاتی اتخاذ خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/652733" target="_blank">📅 23:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWaXesvT_2iPQrzL_P_14iOmQYc3NNgfR6ChKv0FJAXzUDZCswvKWylc-pNzlWVRcDzCy6iAVX7fyDkgIS8FPBpKSV-V_BWNY5iVUSuBE5bFIzxoJxF7Do8qRNHDOJhkOmMeJJSx6ufJe5f6XMJWaigM1XwexI_TARGwYnnxg-AvHDcFPjDHdMdvZzaty_XV1-pz7m_azEuw_B-rMQUc-DMYImJ0UpLT_ilFo8DlRtW6KZ1UCmwsolpmZ8hz72jxBApFvWE-Gp75BAVyzeW8W59nd_w1k0StzaLIEhpOqyja9kHi6cqP0BAYWuSnyxdE9hr9-W29g2d19B_tPO2QhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالانه تنها نیم درصد به جمعیت کشور اضافه می‌شود/ تعداد ولادت‌ها به کمتر از ۹۰۰ هزار نفر رسید
🔹
سعیدی، رئیس مرکز جوانی جمعیت وزارت بهداشت: شاخص TFR یا باروری کل که مربوط به تعداد موالید در خانم‌های در سن فرزندآوری است، رو به کاهش است. زمانی در دهه ۶۰، به ازای هر خانم در سن فرزندآوری حدوداً ۶.۵ فرزند به دنیا می‌آمد. الان این عدد به حدود ۱.۴ فرزند رسیده است.
🔹
آمار ولادت‌ها به زیر یک میلیون نفر رسیده و در سال ۱۴۰۴ حدود ۸۹۲ هزار ولادت نوزاد ایرانی در کشور ثبت شد.
🔹
سالانه حدود نیم درصد به جمعیت کشور اضافه می‌شود. به عبارت دیگر، سالانه حدود ۹۰۰ هزار ولادت داریم و حدود ۴۵۰ هزار فوت.
🔹
با ادامه یافتن این روند، اگر تعداد مرگ از تعداد ولادت‌ها پیشی بگیرد، رشد جمعیت ما منفی می‌شود.
🔹
در سال‌های گذشته میانگین سن ازدواج به ۱۸ تا ۱۹ سال رسیده بود اما اکنون این عدد به حدود ۲۸ تا ۳۲ سال رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652732" target="_blank">📅 23:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8aTCkU-vjBxKyGK4EriR4eYxNdBA0RQ0nTWYAIuy3Gm_UnZqfb8dFU7UpWOxRoX5xh9kYxxF-2_LcEmHLfTXXw_W7fuFhtqVRZYpvTYwbHRskiMkPvab-VxNkAh_uuH_dxnaQaKF9wY36Z4IMm29hOo9M5sEuVm9UA_YbhUOy7XqxUblgoS6EswZBQvvFVFC7_8cbKq20hWTr0tAerwKFg45g1UFw-amJwWplSxJb2t3Q8FM70xkGr2gavcPV59P-O2qzjikh3_zDj9uvMoxOlBJGjlPWs2UA0TyYmUdwVkEGdgEgLwKzdLT1tuKBrYdlLZTA2WrK10ghhVCIYRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه قطری: اگر جنگ باعث ناامنی کشورهای خلیج فارس می‌شود، چرا آمریکا در منطقه حضور دارد؟
دوحه نیوز:
🔹
آمریکا پس از این جنگ بیشتر به یک بار اضافی تبدیل می‌شود تا یک حامی. کشورهای خلیج فارس می‌توانند برای دیپلماسی بیشتر تلاش کنند، اما ایالات متحده متقاعد نشده است که این جنگ به اتحادهای خودش آسیب می‌رساند.
🔹
اگر آمریکا متوقف شود، اسرائیل فوراً متوقف خواهد شد. این تحولات، کشورهای منطقه را به دنبال‌کردن تضمین‌های امنیتی بلندمدت و تلاش بیشتر برای دیپلماسی سوق داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/akhbarefori/652731" target="_blank">📅 23:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Etvc_R6dWoY27378MfwMonzdhLO9dBK1U-sB0KAHAh85_VNhBXeQDuxR1hUCoDQooUXENSUoK5-93IEjNr-_IXVSB7ViRTZlgnc5Rpd0R9NUUy3Z9dqJL79y37GCeAA966fj79VSy9h5iId1YhJAB-psh__4c7nIfxg9pxz5oAg9JWSPPTa69KdEVU3tMo8ghZLv6nAStIrIYUVPyWsOhUclGARpZuIzvbVtws3zKgMLwhJ8AvVJheY5Ho5QQkzPA5glDMP1DWXaoVoGlqwMMm_3yuQoVpHROVfKgd_rWV_51arAuQEIkQ7E3TsaKFSL4xA1k0gjQww0dhCwDKtFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6J0u89QmvnJhRwA0ocOFX0t80Mc77HUDAcnjRWzbIICwAFXmCzCGx6uQw1UExO5zbsYJjlVaqvV3m55DUjUpMutJxu5aliFzpjHLMM4-uQLykoqRN10ErD9I4qTihSAMpHp6-mDwybst_Ivjx-QpQ-oLfsVzzry19CszCe1JhkfpzUlYO4kDQvmWbCgPSCCDOYBNkFAcQRX2NQ_MRzNC607CDzmTe6qX16zBpfNXpesdC9jG6kOM2A031wbGiwHTol5K0PxsqGDfGjVLl_2ZKmyBoApov5O3HXoBZHNOgdxWAMozZtxfLPXL-XS1hAbR4vDRJC4uwn_SEFopVLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irdhWLaptuQ9NdS31MjLWS2kKFgvVX1N374-QgSTJNO9RwNCNNOyFtgbO__Sn0BaTfxo5PtBU91AOZgtSke_S1lyX-p2IiaSiG3qfQeJLU0u3eBdnUVzeZb-Yu2PJemvpJqa8PsqYDBT-KMk2mqZWODtVLojr27OxsixcU1VrxEre7trg4Ij3geviUJRoe8Ykq7XtJS53LA9N64vo178UWa3jCjt48ZY4yq2o6fpxff_hzjSbP6fRnVwOw1zeANAPivR_nLeFND7ZcBOWuGVfvrI593D3g4GHaFY-M3USVtpx2FaknZLzmGry_XOBbndVEY_mouaKjYy0KbqX-7zDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec6544557.mp4?token=cuSceOeYKUwqtaFDXc6Nu10epcLtldHLMrnYlo7O0UBvA-Tf4bdV_M9vvUPzMOqpu_1gXOWVvopUygWg03qCVpVJJd0gTNnZLZ9o46PQrP64bT6ssq8oHCU4HhMSIRWp0_vMOSIsGcKvPixG93QCgdjxamHiZIgHnJWWNhCBEqEAQUmhmpua91PJCgNgCvfPTWKw82L0vFWvZJzvzWadI05wkDaA1lXQ6g2zOefvPiG5NRUJLaqjC54NgX3Ym4mQgN1uTA0LBsbbmbHvShSr838ULRQwijJh3gDKaoIG-Swsa4Eg1awvRSDOYo1d5xls10Y70ywtFiBsyjuHuk0TgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec6544557.mp4?token=cuSceOeYKUwqtaFDXc6Nu10epcLtldHLMrnYlo7O0UBvA-Tf4bdV_M9vvUPzMOqpu_1gXOWVvopUygWg03qCVpVJJd0gTNnZLZ9o46PQrP64bT6ssq8oHCU4HhMSIRWp0_vMOSIsGcKvPixG93QCgdjxamHiZIgHnJWWNhCBEqEAQUmhmpua91PJCgNgCvfPTWKw82L0vFWvZJzvzWadI05wkDaA1lXQ6g2zOefvPiG5NRUJLaqjC54NgX3Ym4mQgN1uTA0LBsbbmbHvShSr838ULRQwijJh3gDKaoIG-Swsa4Eg1awvRSDOYo1d5xls10Y70ywtFiBsyjuHuk0TgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی درباره انهدام یک پهپاد آمریکایی در یمن
🔹
برخی رسانه‌ها با انتشار تصاویری، از انهدام یک فروند پهپاد MQ۹ ارتش آمریکا در آسمان استان مارب به دست نیروهای مسلح یمن خبر می‌دهند‌.
🔹
نیروهای مسلح یمن هنوز بیانیه‌ای در این باره صادر نکرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/652727" target="_blank">📅 23:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تکنیک اقتصادی روسیه در جنگ برای نجات بورس مسکو
🔹
خبرهای رسیده حکایت از این دارد که بورس تهران بعد از بزرگترین تعطیلی خود قرار است سه‌شنبه باز شود.
🔹
تجربه بورس مسکو در ایام جنگ روسیه و اوکراین می‌تواند برای ایران درس‌آموز باشد. اما روسیه در جنگ برای بورس چه کرد؟
🔹
در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/652726" target="_blank">📅 23:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652725">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y443M5wRR90sjCU2cmKWypBwbGk5tVZ7wQcQfvLqtNRn02oOVerMHgxgrEvLfGdHEl8SX7263YyDzfdk3wdUg-_2RcGNjjpJc2qsIYhrKOnkeZooylRW0x9p7zUpKS66f3zo1p1S6cAE6jlIUVIr5ZZRzAyzG57PDMQZvWxbgTWejjyFEIZRVd-Fc-OywQBishGqmLS5PAdS0ozVE6crlwXfF_jJSWxRQnXuWT4k5S_LxN12C27VK4XrqNWc2MBDy7Usu8bkSpm_dVB1oRi1cj7it79MwEo4NmjmOO9J8_EkqJ_jynCyHqDE7Dbugqdu3qdkQzDt1EfMPKTSjUcurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از چین تعهد گرفت که از ایران حمایت مادی نکند!
جیمیسون گریر، نماینده ارشد تجاری ترامپ به ای‌بی‌سی نیوز:
🔹
وقتی رئیس‌جمهور به آنجا رفت، نرفت که از آنها بخواهد در تنگه هرمز اقدامی انجام دهند. او بسیار متمرکز بر این بود که اطمینان حاصل کند آنها از ایران حمایت مادی نمی‌کنند. این تعهدی است که او به دست آورد و تأیید کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/652725" target="_blank">📅 23:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652724">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f594291402.mp4?token=s3SRIpvVeKpES_agXRtlCFqEcwsI6Hn3f8FtwDdDec_TmZ5p-ufgnY0j3TV_YpE2S-z35NPMZbh1j6qWLF-1ssAU147x1iZ1CDiLeNVOzX9VJClYn9xISwF44GEnmjaEs6-F7Ebycxc1gTUf99kJcqNAAL89l_PQctDjTmpcBmZ3KW9o9fSdufJMMFI3XjMqU7x5gstbQiMhEkkQrT6Jtld2OVh_3h4VPlWoGa2efPLkDBc-jb8GKqVYqlu3raS4GyRebG0nba_L8iGh5eT_adH20kPnZ39dpaht_CZWIlXmkZI-XkJJW5vRDLqp8J8HDOCI1KFX8Nc7KyDsSz2y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f594291402.mp4?token=s3SRIpvVeKpES_agXRtlCFqEcwsI6Hn3f8FtwDdDec_TmZ5p-ufgnY0j3TV_YpE2S-z35NPMZbh1j6qWLF-1ssAU147x1iZ1CDiLeNVOzX9VJClYn9xISwF44GEnmjaEs6-F7Ebycxc1gTUf99kJcqNAAL89l_PQctDjTmpcBmZ3KW9o9fSdufJMMFI3XjMqU7x5gstbQiMhEkkQrT6Jtld2OVh_3h4VPlWoGa2efPLkDBc-jb8GKqVYqlu3raS4GyRebG0nba_L8iGh5eT_adH20kPnZ39dpaht_CZWIlXmkZI-XkJJW5vRDLqp8J8HDOCI1KFX8Nc7KyDsSz2y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: فتوای حرام بودن بمب هسته‌ای رهبر انقلاب  تغییر نکرده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/652724" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652723">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1FB4Aqc_rQLatN8fjcJ5GIFs1_fP4NbetYANr5E2IGu1GXjJD62BZIV6uYAAA6jn1xDy3JOGlJQTslaF7_-irwmDH3oz5JIlyDUzfyaVV3m-A1MquTvzJSxj4ArG9BtmCazpVOcxL2ucimCSCDDS9wQ8CkCOUY_KxrfRKjM7gKmnm_9uwvTWtnpq1uFdzBJXpBq7EqnS-mN_8qYDnIDOQLI7cChoV_PX4rE9fmxmVhnN4RRAw5sfKnDOKOUt_S--PpVzY0Lug78hXJIGTwqRC1irrCn6EadJ9LJxgT1X0qjIraEADMNAuJUAADBLO6jPSRmKVKvnF2V-juJ9D3ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشان ملی «روابط عمومی برتر ایران» به ایرانسل تعلق گرفت
🔹
همزمان با روز روابط عمومی، سیزدهمین دوره «جشنواره ستارگان روابط‌ عمومی ایران»، ۲۷ اردیبهشت‌ماه، برای ششمین سال متوالی از ایرانسل تقدیر کرد.
🔹
در مراسم پایانی این جشنواره که با حضور جمعی از فعالان ارتباطی ایرانی و بین‌المللی در سالن همایش‌های کتابخانه ملی ایران برگزار شد.
🔹
در این رویداد، نشان ویژه «ستاره ارتباطی مدیر ارشد»، با کسب بالاترین امتیازهای لازم از ارزیابی‌های تخصصی و به دلیل شخصیت و منش ارتباطی، روحیه تعاملی و نقش تعیین‌کننده در بهبود ارتباط با ذی‌نفعان و نگاه تعالی‌جویانه به حوزه ارتباطات، روابط عمومی، رسانه و افکار عمومی، به مهندس محمدحسین سلیمانیان مدیرعامل ایرانسل اعطا شد.
🔹
همچنین روابط عمومی ایرانسل، بر اساس رأی هیئت داوران و به دلیل درخشش در عرصه‌های مختلف ارتباطی، به‌ویژه مدیریت هوشمند خوشنامی سازمان، موفق شد لوح سپاس و نشان ویژه ستاره ملی «روابط عمومی برتر ایران» را دریافت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/652723" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652722">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درویش: خسارت جزایر مرجانی اطراف جزایر هنگام، هرمز، و کیش در اثر بمباران‌های جنگ محسوس است
محمد درویش، فعال محیط زیست در
#گفتگو
با خبرفوری:
🔹
شاهد وجود لاشه‌های ماهی و آبزیان در سطح آب نبودیم اما خسارت جزایر مرجانی اطراف هنگام، هرمز، کیش در اثر این بمباران‌ها محسوس است و روی کیفیت غذای آن منطقه اثر می گذارد.
🔹
معاونت دریایی سازمان حفاظت محیط زیست باید موضع گیری شفاف کند و بگوید چه حدی از آلودگی، خلیج فارس را دربرگرفته، چه میزان خطرناک است، کدام جزایر ما در معرض آسیب است.
🔹
نزدیک به ۲۰۰ شناور و کشتی‌های مختلف در خلیج فارس و دریای عمان غرق شده است که محموله ها و مشتقات شیمیایی، محموله‌ها و مهمات آنها زیر آب رفته است و می تواند سبب آلودگی شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/akhbarefori/652722" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652721">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سرلشکر رضایی: ایران در دیپلماسی و مذاکره جدی است اما در برخورد با متجاوز، جدی‌تر است
🔹
آمریکاست که الان باید خودش را ثابت کند.
🔹
انگشت نیروهای مسلح ما روی ماشه است و همزمان دیپلماسی هم ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/652721" target="_blank">📅 23:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652720">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
برنامه جدید وزارت اقتصاد برای تغییر مسیرهای تجاری کشور/ مسیر جایگزین معرفی شد
🔹
در شرایطی که طی هفته‌های اخیر روند واردات کالا از برخی بنادر جنوبی کشور با کندی مواجه شده، دولت بامحوریت وزارت اقتصاد برنامه جدیدی را برای بازطراحی مسیرهای تجاری و وارداتی کشور در دستور کار قرار داده است.
🔹
برنامه‌ای که بر اساس آن بخشی از واردات از بنادر جنوبی به بنادر شمالی و مرزهای زمینی منتقل می‌شود تا روند تأمین کالا بدون وقفه ادامه یابد و بازار با کمبود مواجه نشود.
🔹
بر اساس اعلام وزارت امور اقتصادی و دارایی، این تصمیم با هدف افزایش تاب‌آوری اقتصادی، جلوگیری از ایجاد گلوگاه در زنجیره تأمین و استفاده حداکثری از ظرفیت‌های جایگزین حمل‌ونقل اتخاذ شده است.
🔹
در هم ین راستا، هماهنگی‌های گسترده‌ای با کشورهای همسایه برای تسهیل ترانزیت، حمل‌ونقل و ورود کالا انجام شده و کارگروه‌های ویژه‌ای نیز در سطح ملی و استانی تشکیل شده‌اند./ خبرآنلاین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/652720" target="_blank">📅 23:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652719">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای رسانه صهیونی: امریکا به امارات پیشنهاد داده جزیره لاوان را تصرف کند!
جورزالم‌پست:
🔹
گزارش‌ها حاکی از آن است که دولت ترامپ امارات را تشویق می‌کند تا درگیر مستقیم در جنگ علیه ایران شود. برخی مقامات به ابوظبی پیشنهاد می‌کنند جزیره لاوان ایران را تصرف کند.
🔹
یک مقام اسبق ارشد امنیتی دولت ترامپ گفت که استفاده از نیروهای امارات، از قرار گرفتن نیروهای آمریکایی در خط آتش جلوگیری می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/652719" target="_blank">📅 23:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652718">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e3688043.mp4?token=tiuGYwqTr1F5WcJ-RlLqRZGBlInIvInReBW7-JIkajfsARUZzZ17ylyeEmn-eUobpCGVBAvMv0PubBy6DLC2SN9haVp373SA4s_-E96QINMrPbEGu1V82w7fmDK9TLr2QJWJ-F64oE32jfStC5QmX5Dfy-p42h9zqCLO7VfLrpT1anvdWZTwKEMI1H4i2Paz1hIoGtPFTYXsZBoxqZrZPoPaQSQQS08RjtmFGRMxA7NhEnz84tnd1CODFH26V_2AKxqkTxWLvtMF0GQ-bFPLfs0lDs_dR7ybcBVGlR9D2tmBjFZHEll5DQUcBSmh1KNzJVRoFvG5oPPCe2ne77PmcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e3688043.mp4?token=tiuGYwqTr1F5WcJ-RlLqRZGBlInIvInReBW7-JIkajfsARUZzZ17ylyeEmn-eUobpCGVBAvMv0PubBy6DLC2SN9haVp373SA4s_-E96QINMrPbEGu1V82w7fmDK9TLr2QJWJ-F64oE32jfStC5QmX5Dfy-p42h9zqCLO7VfLrpT1anvdWZTwKEMI1H4i2Paz1hIoGtPFTYXsZBoxqZrZPoPaQSQQS08RjtmFGRMxA7NhEnz84tnd1CODFH26V_2AKxqkTxWLvtMF0GQ-bFPLfs0lDs_dR7ybcBVGlR9D2tmBjFZHEll5DQUcBSmh1KNzJVRoFvG5oPPCe2ne77PmcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست بیمه بیکاری به اوج رسید!
🔹
عددهای این ویدئو خبر نیست، واقعیت‌های این روزهاست که از پی آمار می‌آید.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/652718" target="_blank">📅 22:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652717">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv6E68S-2YZ-7Qhq-U5LMXin8E-3ATefImQv5yYdiE4iarkHAU_OTkPVrde3wk8AE6avPWUrmY6LByLZ1XJly86R7SNRzxMeuPIiJCJiurb92_6FxydB0R2hy3ugMWFEO_4kDaOBM6jEDgRRY56aUNcwKFIxOtHDeFmBtHjTNqQS-xUbEfAjpJjnAA45aCdVZ3IY4ME1osID08ylVky_ySYE4PXZ4XSKy5WwwoN_WvCIoXCoSUryjIzNJM1j3L-IYpFBc-TBgMMdUwHu5g3UAoqfJCtbPrsvToQOdBvCQOypUVWC261kCbUAmh7CTaLyyZaiS1HGcaEEsevpUnpY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف چند دقیقه، آلودگی چند صد ساله…طبیعت، سطل زباله‌ ما نیست…  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/652717" target="_blank">📅 22:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ef0u9Bg_nRfZMcj2O3638FV6vxWBPnDhEd3pFZzsycA6ak1mVFaSlyTLvbD0CfjcseInzRKHjYITUgOfwsHIzjRbK0I6lEL3SBaT2AkNhBFtc-Jw5zAU4efCBLiEv9mcmFr56fG9kNIVVTKusiPMEOYJEB00fg0g1WGIGdCTPpRhcjiPHin_wo8fdHKKB4kJaWGuIS4f2S5o1lisPO-oDQjEu8Em0u0MRMEz_8f_KBJm4D-JMTnFFQ1HFEEMNeZz6hRLy8TDWu06IEaDN3Pr3M2OrYZvCu-g_V9ubL4IDnYfZqsX1kmzcB03Z1Mp7jHEsGMxK-I5xJ925l365eDRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QG4Zcx0JiOCoz5nxM4DXmR3WDvlZGu90JTU7EM5fXPKi7zn2fnuIo-yKeJsCTJHVOEl_Q-VndSpN3gmCfrz7CkZTWg4xEk5nZsHMxdBkm60OKkopbwVA38vJp5p3Qf1dE5xmVWHGXQQRk4k-s-rmXG5nP20iX0yVnS03opVzN5zykFPOj0Ts2FOl_mlxUJwrGSpqvfkwG-ElIdm1lLS0u96Ty0dBpMcg9D1gz-eHfABrT48JTMxoK4Z7w4v7fE9nTHLMR-1F3oXr7D-G4DKXzi5em3Q4ZkFzUu-MgV5xw0MeuTWhZsetZSP6G2YMB-obSbeRTp5A85o2_ujcI4xlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCIb4fjAgGts9IkrBHFjj38FwDz135MRZc4LzxylBNy8s3435GzYFaPpU-VRe0GXK10637OzZH_Rt1zQgBS8nd_5aF7PRjjye_HiBH0d2gZ1hONvtLMPSTQoplhn5-I7GhMU95iZAS3S7XvDeekEPPMJyXJqDJOoijz6xqYVl6SbL36ekykWIfcDZmgAtXESL5-odguzHbRKS_NQjkifzqfpFbuY0J9xfGS83LVKb0xfbuDsvUAqVzcXUMNihk6-cMRsF8Z0f_qyNFAkrzK2rfKuPpfd8vWQ-HkgiCd4KMZ9BagDRJsAAFZQCs2L8SdvBJRcZDxpa46ep8PGWjycsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6128f73793.mp4?token=Ssq2dscCkB8GdnW9qbEh1o0beJQg1iIUpsL-y3Br0XXhi0Bwh08WqanLlRP4WV9TO30DdDG5jozCBqGZADlYmqXVK_kmoGnUkytLTHoiwraUQv6ONnLLf5JmFRcU6FdEOvdGBzE0XOrd-jncNf1BiVvgjoU7gkt605EhBePcPZAydjL3ipVsADHtZ6mV4MSVK8tDcPDhdpXkucqeZT35BkHpsQbqsJOY1-H0DOGZ7Vwxo-ggYzJc4fSrVpLAUtNgasVLJ5IZaNLsFYlHL2ir2iptcstcbST8rq0jy2sTyuvfLj4MIxqJ1gRSiidBvWRaj456w0Lwq_U5-aIbH9jerg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6128f73793.mp4?token=Ssq2dscCkB8GdnW9qbEh1o0beJQg1iIUpsL-y3Br0XXhi0Bwh08WqanLlRP4WV9TO30DdDG5jozCBqGZADlYmqXVK_kmoGnUkytLTHoiwraUQv6ONnLLf5JmFRcU6FdEOvdGBzE0XOrd-jncNf1BiVvgjoU7gkt605EhBePcPZAydjL3ipVsADHtZ6mV4MSVK8tDcPDhdpXkucqeZT35BkHpsQbqsJOY1-H0DOGZ7Vwxo-ggYzJc4fSrVpLAUtNgasVLJ5IZaNLsFYlHL2ir2iptcstcbST8rq0jy2sTyuvfLj4MIxqJ1gRSiidBvWRaj456w0Lwq_U5-aIbH9jerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوری| برخورد دو جنگنده نیروی دریایی آمریکا در آسمان
🔹
در جریان نمایش هوایی Gunfighter Skies
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/652713" target="_blank">📅 22:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
قیمت های عجیب و غریب در بازار میوه/ یک کیلوگرم انگور ۵ میلیون تومان!
🔹
این روزها بازار میوه با قیمت های عجیبی روبه رو شده است، به‌طوری که در یک سوپرمیوه در خیابان فرشته، هر کیلوگرم انگور یاقوتی بنفش را تا ۵ میلیون تومان و زردآلو را تا نزدیک به دو میلیون تومان عرضه می کنند.
شرح ماجرا را در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3215722</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/akhbarefori/652712" target="_blank">📅 22:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975f8b4c2d.mp4?token=lunYJEmRxBOXbXq6xxZZT1ZeI9CdPE2tKG0r_rTTZloTWbT1wRBVAnwcgXZwXpAC11c3GQRmbiCZRKkaJzyae1FRoj_QsXVozqkhYRO4FTv56LStkk6-E56SImyylw3xObrRxgYAf9B_v9mTURyp-f5C7KuTaNre4-yKPS64nDF81ZeRMnqktAx3p7dEEsO4v9ffYRdnFWUJZC4wLu7WSafiqa4SOY3WeKeHs-p-eb8PN27uKNkgy6Hgvr5K-yi1D9rJ_x3erJr0SS8iZMB2xbg2DFrARsbZ9oaFFAh3ViLvzoqVhkSBdCT9ypDag1sPRkdvim_UHf2Eb809x5x-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975f8b4c2d.mp4?token=lunYJEmRxBOXbXq6xxZZT1ZeI9CdPE2tKG0r_rTTZloTWbT1wRBVAnwcgXZwXpAC11c3GQRmbiCZRKkaJzyae1FRoj_QsXVozqkhYRO4FTv56LStkk6-E56SImyylw3xObrRxgYAf9B_v9mTURyp-f5C7KuTaNre4-yKPS64nDF81ZeRMnqktAx3p7dEEsO4v9ffYRdnFWUJZC4wLu7WSafiqa4SOY3WeKeHs-p-eb8PN27uKNkgy6Hgvr5K-yi1D9rJ_x3erJr0SS8iZMB2xbg2DFrARsbZ9oaFFAh3ViLvzoqVhkSBdCT9ypDag1sPRkdvim_UHf2Eb809x5x-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نه‌تنها «هنوز زنده‌ایم»، بلکه دست‌های دلاوران نیروهای مسلح ایرانمان هم هنوز روی ماشه است. مردم هم هنوز در میدانِ خیابان‌‌اند، روحیه‌ها و همدلی ملّی‌مان هم همچنان در قلّه است. ما اینجاییم تا اگر پدوفیلیِ جنگ‌معاش و متوهم دوباره غلطی کرد، به او و نیابتی‌های کوتوله‌اش در حاشیهٔ جنوبی خلیج فارسمان و در سراسر منطقه درس تاریخی بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/652711" target="_blank">📅 22:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
برنامه جدید وزارت اقتصاد برای تغییر مسیرهای تجاری کشور/ مسیر جایگزین معرفی شد
🔹
در شرایطی که طی هفته‌های اخیر روند واردات کالا از برخی بنادر جنوبی کشور با کندی مواجه شده، دولت بامحوریت وزارت اقتصاد برنامه جدیدی را برای بازطراحی مسیرهای تجاری و وارداتی کشور در دستور کار قرار داده است.
🔹
برنامه‌ای که بر اساس آن بخشی از واردات از بنادر جنوبی به بنادر شمالی و مرزهای زمینی منتقل می‌شود تا روند تأمین کالا بدون وقفه ادامه یابد و بازار با کمبود مواجه نشود.
🔹
بر اساس اعلام وزارت امور اقتصادی و دارایی، این تصمیم با هدف افزایش تاب‌آوری اقتصادی، جلوگیری از ایجاد گلوگاه در زنجیره تأمین و استفاده حداکثری از ظرفیت‌های جایگزین حمل‌ونقل اتخاذ شده است.
🔹
در هم ین راستا، هماهنگی‌های گسترده‌ای با کشورهای همسایه برای تسهیل ترانزیت، حمل‌ونقل و ورود کالا انجام شده و کارگروه‌های ویژه‌ای نیز در سطح ملی و استانی تشکیل شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/akhbarefori/652710" target="_blank">📅 22:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f895fd79a.mp4?token=lcsySV6oAypeCuw9kC16WS-2CNBCKN7UaQrd-6lMfKHL1VdNE7k9gc-WjxLNWHJphB1Z4pCC9_zNSEDcG7Gim-YBt9Cbtee0KA525Kh0G5AEgG6ehyBqQVyyUBmhHtdKh-cnH-1Z08aMQscJZZDZOtYAyw6GI7sFoyuUM0VsMu0UXneQfGoVX3nZ5qSnPn14zoZuFlnrgre96ZzeT1Xauz7mQiXNcKNJjfoqFcnIOqiHaKk7cxePVXdtEst30Ffk0EbGxav2ZcsJ2MrGJYrikG7WRfzBZja2pg6xB0h7TXIvaCisUFA6GdN39MfHNItZ9gUxg8AFA5h9zI5-7e2dT5_2Pr5ihHbNwuEVeSK4EaikcNAa1Zwur5fWaV-sxm6ht0N8jfkN7-LNZDa9ULravctOBe9x3_k0WBLrLgKLSIiti8nhRrate35AKaRCgWEOMl5bY15ZWEq-YARNdoJ_h-FR3HXF_qOVJeAd4T07tc9RZPSIKWgg-X6Nr5U3edD42t63ttxtsZHg-4YcjqWao60IZG3EE92jomesxQDbLCgUXwPOVTYcmwbm-kDNsMpq08MPNwvfnQGb_a6RlKwn8ILormmzwWfSSIpnf8xzLMnndMtBVP5fgMv4bVweFKko8-VQvEs7YKNRmWphCassz23i7vW-Ql8BS7qPkLBGq-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f895fd79a.mp4?token=lcsySV6oAypeCuw9kC16WS-2CNBCKN7UaQrd-6lMfKHL1VdNE7k9gc-WjxLNWHJphB1Z4pCC9_zNSEDcG7Gim-YBt9Cbtee0KA525Kh0G5AEgG6ehyBqQVyyUBmhHtdKh-cnH-1Z08aMQscJZZDZOtYAyw6GI7sFoyuUM0VsMu0UXneQfGoVX3nZ5qSnPn14zoZuFlnrgre96ZzeT1Xauz7mQiXNcKNJjfoqFcnIOqiHaKk7cxePVXdtEst30Ffk0EbGxav2ZcsJ2MrGJYrikG7WRfzBZja2pg6xB0h7TXIvaCisUFA6GdN39MfHNItZ9gUxg8AFA5h9zI5-7e2dT5_2Pr5ihHbNwuEVeSK4EaikcNAa1Zwur5fWaV-sxm6ht0N8jfkN7-LNZDa9ULravctOBe9x3_k0WBLrLgKLSIiti8nhRrate35AKaRCgWEOMl5bY15ZWEq-YARNdoJ_h-FR3HXF_qOVJeAd4T07tc9RZPSIKWgg-X6Nr5U3edD42t63ttxtsZHg-4YcjqWao60IZG3EE92jomesxQDbLCgUXwPOVTYcmwbm-kDNsMpq08MPNwvfnQGb_a6RlKwn8ILormmzwWfSSIpnf8xzLMnndMtBVP5fgMv4bVweFKko8-VQvEs7YKNRmWphCassz23i7vW-Ql8BS7qPkLBGq-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: محاصرهٔ دریایی آمریکا را می‌شکنیم
🔹
صبر ما حدی دارد و نیروهای مسلح درحال آماده‌کردن خودش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/652709" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
کاخ سفید: ترامپ و همتای چینی به توافق رسیدند که ایران نباید به سلاح هسته‌ای دست یابد
🔹
ترامپ و همتای چینی توافق کردند هیچ کشوری نباید برای تنگه هرمز عوارض دریافت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/652708" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
محسن رضایی: در جریان باز کردن تنگه هرمز، ارتش و سپاه جلوی آمریکایی‌ها ایستادند و یکی از ۳ ناو آمریکا با شلیک موشک‌های ما آسیب جدی دید که صدایش را در نمی‌آورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/652707" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee0743e80.mp4?token=JeVdekkJgM9JMJRp9M0gv0_hi5YNsDFW3rtsdKp6XTaDwRBZPeTGg3DqXeXI2z_V-IZZ_HHq7ktLxvSTqHhjT4zrFByBgHSqNz9ZiOMbwKzKNAqL3qV2HsKcI8qXioy6aYmMmpuNqK0InBO-izrho_Vz2m9M_77M05UjqdEDP24EeFSp5y4FOWJCHMjF02JRrmPs-WLJYFMQHc3YFvF5Pnazy-DLN91EVcwC6C0QSSQ1ykM9GXDqT5doqXPTQPOQ16vDNoYOUhceBYbo8skSDFdZzgdLu1oXj3TucGLCrmdNe_nCJzL0TkMhwyS7ieqDn1Kji3JFan1uldbrAzpqamXOdtI0xm3qQoQ463DO4Y7Y1Nzi5FQvCXz5vj8VHISFQWphgVGdW7KM74bVNI8tF8XrsrsymnNUQSJN16pLkTvkzFT0QTTRc5Bj7Xa-hrim23QaZAWtKrS9pr5fo2Tcm7cbbuq6yhed23hwhYyh2BG5UcXRRLSsNqh-mqkRYWi6GWMxXVjihV4Z5b3qfdDgsto6A3Mza4ydO9nuc0Khsdvex5ylxYdZsy9saPE7VamXzes9g6pEz2wU06OswCVaUhf1pn6ovnv2oPoXVGCJ5DJEAwvheCUAyMycoCh3ZtBAeZ_0jaWciIG0fL5gM5iXFhyT6esDRjujvbGTham1rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee0743e80.mp4?token=JeVdekkJgM9JMJRp9M0gv0_hi5YNsDFW3rtsdKp6XTaDwRBZPeTGg3DqXeXI2z_V-IZZ_HHq7ktLxvSTqHhjT4zrFByBgHSqNz9ZiOMbwKzKNAqL3qV2HsKcI8qXioy6aYmMmpuNqK0InBO-izrho_Vz2m9M_77M05UjqdEDP24EeFSp5y4FOWJCHMjF02JRrmPs-WLJYFMQHc3YFvF5Pnazy-DLN91EVcwC6C0QSSQ1ykM9GXDqT5doqXPTQPOQ16vDNoYOUhceBYbo8skSDFdZzgdLu1oXj3TucGLCrmdNe_nCJzL0TkMhwyS7ieqDn1Kji3JFan1uldbrAzpqamXOdtI0xm3qQoQ463DO4Y7Y1Nzi5FQvCXz5vj8VHISFQWphgVGdW7KM74bVNI8tF8XrsrsymnNUQSJN16pLkTvkzFT0QTTRc5Bj7Xa-hrim23QaZAWtKrS9pr5fo2Tcm7cbbuq6yhed23hwhYyh2BG5UcXRRLSsNqh-mqkRYWi6GWMxXVjihV4Z5b3qfdDgsto6A3Mza4ydO9nuc0Khsdvex5ylxYdZsy9saPE7VamXzes9g6pEz2wU06OswCVaUhf1pn6ovnv2oPoXVGCJ5DJEAwvheCUAyMycoCh3ZtBAeZ_0jaWciIG0fL5gM5iXFhyT6esDRjujvbGTham1rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز برای تجارت باز است؛ نه برای لشکرکشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/652706" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da680f7fe.mp4?token=pni4eQS9DOAIt_ulhrwOADA-POyr6ooLXu24jYEnQd7967dhGA-zOCvscRb6O8hOOeOQvfiB7q6XBOG7mpov9TJc7XC6kU9wihicFg_OmC7Y2LX1-n6HCuNAJ16IXOinlwckAVMG4DutTLE_hwscc4YKf_v8oCPixls-dYWG56zSl5HOusf9_AMc8xt9n0dH7-WVpfHrNA1xIpQdpAWSrLMHm8QfiM8gqMTQlGo5gdxiyh2tOa2p2D--rZGkJ2AcqEHNFyF5yqwEpRIWAr6tVr8pArxDGEhocAwymKq9apd60_4xPu6MNIgn6MVNSkDjxDWHx8AYx7UIMGvTLwRX3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da680f7fe.mp4?token=pni4eQS9DOAIt_ulhrwOADA-POyr6ooLXu24jYEnQd7967dhGA-zOCvscRb6O8hOOeOQvfiB7q6XBOG7mpov9TJc7XC6kU9wihicFg_OmC7Y2LX1-n6HCuNAJ16IXOinlwckAVMG4DutTLE_hwscc4YKf_v8oCPixls-dYWG56zSl5HOusf9_AMc8xt9n0dH7-WVpfHrNA1xIpQdpAWSrLMHm8QfiM8gqMTQlGo5gdxiyh2tOa2p2D--rZGkJ2AcqEHNFyF5yqwEpRIWAr6tVr8pArxDGEhocAwymKq9apd60_4xPu6MNIgn6MVNSkDjxDWHx8AYx7UIMGvTLwRX3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری و کشته شدن ۱۶۶ سارق مسلح در ایام جنگ
🔹
رادان: همانطور که قول داده بودیم در ایام جنگ با سارقین مماشات نداشته باشیم، تا امروز ۱۶۶ نفر از سارقین مسلح و حرفه‌ای که در برابر پلیس مقاومت کردند به ضرب گلوله زمینگیر و دستگیر شدند و تعدادی از آن‌ها کشته شدند و ۱۰۰ قبضه سلاح نیز از آن‌ها کشف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/652705" target="_blank">📅 22:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2o1AC3DKohWdjAAkyIYzXtX2DL-FBbQnKVvrIf9_r6zHWg-lKYl20xIGLcupLatwi6W2MMgrgfdCb4PLHcE7BEX7OJDNip_4QPbQu0YWZiEvlWTFe11JegNBRShFugQaT6OzY2SSfzdlQR2RTMxvwCdzzAWYXP68DPXRP5t99f5lGI3CgaRSIZroqDkM1Tk_sJP-S2_ZqMaMFUyzzGlxSaI0Hhoe_8J722nU_qa0yZ55z3RFC3f00iaIQRim5G5d2W3TvR9TbxIvmKAh1BD-13vOKiTpDPAEhxVAP6pQi1ydc0f5PwPck1VywWiE_vz4KrjV38WV3Zsrcz-Nqbs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN: ایران می‌تواند با تهدید کابل‌های اینترنتی زیر دریا در تنگه هرمز شرکت‌های فناوری مانند گوگل و متا را ملزم به رعایت قوانین خود کند
🔹
ایران با الهام از محاصره موفقیت‌آمیز تنگه هرمز در طول جنگ، اکنون شریان‌های پنهان اقتصاد جهانی، یعنی کابل‌های اینترنت زیردریایی، را هدف قرار داده تا از غول‌های فناوری جهان حق عبور دریافت کند.
🔹
تهران در نظر دارد شرکت‌های بزرگ فناوری مانند گوگل، مایکروسافت، متا و آمازون را مجبور به پایبندی به قوانین خود کرده و از شرکت‌های کابل‌های زیردریایی حق لیسانس دریافت کند.
🔹
با اینکه اپراتورهای بین‌المللی به دلیل ریسک‌های امنیتی تلاش کرده‌اند کابل‌ها را در بخش عمانی تنگه هرمز متمرکز کنند، اما به گفته مؤسسه پژوهشی «تلی‌جئوگرافی»، دو کابل کلیدی دقیقاً از آب‌های سرزمینی ایران عبور می‌کنند.
🔹
کارشناسان هشدار می‌دهند که هرگونه آسیب عمدی به این زیرساخت‌ها، می‌تواند یک «فاجعه دیجیتال زنجیره‌ای» ایجاد کند که بیش از همه کشورهای عرب خلیج فارس، را تحت تأثیر قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/652704" target="_blank">📅 22:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8MQeC_5XkaiYLKdsukoT1e-Uy5PPLK1tiIeFtp0xU82QCHmHGsMIPVkuqfUhFxolp88_AjfdhzHINH8ruhigT1VqV6ZlMTrmDkycFOzKQ6v9F00C9scTNn6xLKvxf_RR0tN6h_hN5JoZ8lyVm6MoFmTTs4AbGjtSWkiNiC7Zvw-WPtM2BVPmPU9a183f70TVIr6yE1hGTeOrdAcJoz3NhJ_nAs0uvfw6uJMmsbtgtpdWd2USLhFqUxHrStRIxa2wAS4iya7EItxS1mnOhy42PFlCdMkc6ophqmvUSv_c8CarEWRkG7i0sOTp6sZlkQC58u1BqZBs-B75u-0uMvG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاف تلگرامیِ «العربیه»؛ پیام اتاق فرمانِ رسانهٔ سعودی به کارمندانش: تا می‌توانید به جنگ روانی علیه ایران مهمات برسانید
🔹
«تا اینجا چند تا آکسیوس و ترامپ کار کردیم. آکسیوس‌ها رو فتونیوز کنید!» ادمینِ «العربیه»، رسانهٔ نزدیک به اسرائیل، این فرمانِ صادرشده از مدیران به کارمندان را به‌اشتباه در کانال عمومی‌اش پست کرده. البته این نکته، چیز پنهانی نبود؛ دو روز پیش هم که کانال العربیه سعی کرد در ادامهٔ فعالیت‌های رسانه‌ایِ ضدمقاومتش نقل‌قولی از نخست‌وزیر لبنان را با تنظیم خاصی پوشش دهد، نظر مردم غزه درباره فعالیت‌‌هایشان و اسمی که روی این رسانه سعودی گذاشته‌اند را مرور کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/akhbarefori/652703" target="_blank">📅 21:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2f385bca.mp4?token=ACSYPTLtEm0n6o2PM_p1_M0i-VZ38nnPV86TlEc0pQQ4Bi7OmVcWxgESOJDIj7-Hgaa0r5HEKwLaAbuT9YhASLYo8re3nWj0rKQ2ZmZPS9QFzXk06JvVL0k8qu4Oub2QJaFbg-M5tj-B7kYnmYR44o57GzouyTf5vo7sR8SJlYPy2CmR7b2f8Z6DasnJu2PDt1cjI9lEOKQ-VLyVwgxbfjPN_HOAahRHjTiU3wp_H4yNGKyjk92w0Mi_dz_Y_0hRozpqkyer5p3ZaMCfNLl6wy7AKBkN-7QzqpyRUDXSqM2e7CXfOnbB5rD_9uzMYeql7KdIEDrj_3v36uxTT2fsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2f385bca.mp4?token=ACSYPTLtEm0n6o2PM_p1_M0i-VZ38nnPV86TlEc0pQQ4Bi7OmVcWxgESOJDIj7-Hgaa0r5HEKwLaAbuT9YhASLYo8re3nWj0rKQ2ZmZPS9QFzXk06JvVL0k8qu4Oub2QJaFbg-M5tj-B7kYnmYR44o57GzouyTf5vo7sR8SJlYPy2CmR7b2f8Z6DasnJu2PDt1cjI9lEOKQ-VLyVwgxbfjPN_HOAahRHjTiU3wp_H4yNGKyjk92w0Mi_dz_Y_0hRozpqkyer5p3ZaMCfNLl6wy7AKBkN-7QzqpyRUDXSqM2e7CXfOnbB5rD_9uzMYeql7KdIEDrj_3v36uxTT2fsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هماهنگی با سپاه، لازمه عبور از تنگه هرمز
🔹
نمایی از مسیر اقتدار و نقشه تنگه هرمز که نیروی دریایی سپاه مسیر امن آن‌را هم برای ورود و هم برای خروج به جامعه دریانوردی در سراسر جهان‌ معرفی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/652702" target="_blank">📅 21:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f344W5MaEUFse79uQENlh8lx6_CCmMXVGBSBOTGvG2j7mtT-BEPT7D55JfvbqClF-TLI3cmZ2nZRc8TPGqZ5QoWuwB6b16X9ggJK7cNT-iHi1O2C6R_KrM9eTYlPfm7y-usgQCCk7g03UfbgNSTA914vo9FL54coFQJ6Vz6__j6c6rRmqDLHOYj8YTfoa_PQKyDmvBywnanEqIRv_wEMnbbPyL_2zZMukPAcGioi9KcMWny_KTXy8Tg67IvWALqA5GD4onkaJRRA24sD9n57rdwiWNrZM8tOgYmtzc1VfLFgOA6GGZIFEavofxJuwS-bLrDuiQMqAvdfO4aC4Qmb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مشکوک در باب المندب و توقف چندساعته دریانوردی
🔹
طبق اخبار واصله از منابع موثق شب گذشته در دریای سرخ و ورودی باب المندب انفجار مهیب و مشکوکی رخ داد که تا ساعت ها تردد کشتی ها از این تنگه را بدلیل ترس از انفجار های بعدی متوقف نمود.
🔹
تا کنون هیچ گروهی مسئولیت این انفجار را به عهده نگرفته است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/akhbarefori/652701" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96c671aef0.mp4?token=GgHGa8ffNlCHHGZq8tBbpDI64TYrHmyLNfVUFOE8HNbnUv0O49jt716182S6pjVaGdhM2-cqXTeDbFQB6sRqymX8YWFqK5JGOgRbNEMiDazZ1f3KaodcVvzvoBif9mOmXUvqFxCcU2s3qFLXhVYAjDbzlDBQd2mH8uOzkAUgFWr8SEiKUxN-bMRof53Sl-ZTfi0QMfhZ0VDMs6jzhBUB-Gk0iL3WEvzRPXAmFchV-Dcr-BcPO-_Y0z3gTpvuf4JsUMwlhsz336-KPstjTdvHZjiPiHmIesGVzb0wXr6nnIYr_EeAX1YueZgp3N_pWHgykwwiqt96pPdgupjWC-mIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96c671aef0.mp4?token=GgHGa8ffNlCHHGZq8tBbpDI64TYrHmyLNfVUFOE8HNbnUv0O49jt716182S6pjVaGdhM2-cqXTeDbFQB6sRqymX8YWFqK5JGOgRbNEMiDazZ1f3KaodcVvzvoBif9mOmXUvqFxCcU2s3qFLXhVYAjDbzlDBQd2mH8uOzkAUgFWr8SEiKUxN-bMRof53Sl-ZTfi0QMfhZ0VDMs6jzhBUB-Gk0iL3WEvzRPXAmFchV-Dcr-BcPO-_Y0z3gTpvuf4JsUMwlhsz336-KPstjTdvHZjiPiHmIesGVzb0wXr6nnIYr_EeAX1YueZgp3N_pWHgykwwiqt96pPdgupjWC-mIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رادان: از آغاز جنگ تا به الان بالغ بر ۶ هزار و ۵۰۰ نفر از وطن‌فروشان و جواسیس دستگیر شدند که ۵۶۷ نفر از آن‌ها موارد ویژه مرتبط با نفاق، اشرار و گروهک‌های ضدانقلاب بودند
🔹
دستگیری سربازان دشمن و وطن‌فروشان در اغتشاشات دی ماه همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/652700" target="_blank">📅 21:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib3FxWBqzVDfBcoHTV5Mk52qLxsfeG4IqyxanME5sKh9V4DA94ck9ESUdgVmZvy9iKldHPN4RL4FiJNsJv0d1rnyJ3k3vpSHd6E7eSBDwtVcZKZuQg619gW5WqWp02XNTBGKo_vTqv2Lj1tgToMqgmtHNhTHegMLu0_SL_2ljLvjDF354O2gEG-N8VAKhgk877BNAqZ13FeqdWCaVzp7MwCSN8lMkvnLe8KeeIXEb-VMdzcxL9omLHgeL6pbd2xfwMhBmrIvYfqXfLGUV-YDIv3jkzb4-4rs5-NrFY66q88TqD3b_reAGFGXg7vxhG8wVxXR5i2Ci0dABT56_Wra8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی: هیچ قدرتی نظامی نمی‌تواند تنگه هرمز را باز کند
🔹
سخنگوی کمیسیون امنیت ملی با اشاره به اینکه آمریکا دلیل اصلی اوضاع کنونی در تنگه هرمز است، گفت که هیچ قدرت نظامی در جهان نمی‌تواند بدون موافقت ایران، این تنگه را باز کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/652699" target="_blank">📅 21:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652698">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q46Hj9rMpPkiZj1IPyH4foKrq9zCLNiR16OigFpm1FNeGKtyzFu1ao45mV-yaFde6cyQJxV-FyR6B8q6r6npZ9XW09H4cQWBzbLCdfDupaK9Pp3nv3LNlsF1NC9FLWT7-PZXbV9sGhqZn8MTlIlLcDezO40wl4nKPJZKfadXGDdN7bOApfZJIKfIpwfrcLN9DMGG13IOY92XyXFlIGpjTp91nomfRCHGim5DKl_hHGawZkyZchPbraPf8POjpeTaFXFfGFaQiyvjcA3ZTkNRX-PASXAEuPoMjbNaGJ2aOfq5xqVt_pmufJF_DcmU1efIwGx4sRkHsZZKHTdZt8LiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مافیای گروگان‌گیر
🔹
اقتصاد ایران در برخی موارد در گروگان مافیای ذینفع است. گروه‌هایی که نه از سر ناچاری، که به خاطر حفظ منافع کلان خود، تصمیم‌سازی ملی را فلج کرده‌اند. هر طرح ساختاری که به سودای بی‌حدومرزشان لطمه بزند، با وتوی پنهانشان نقش بر آب می‌شود. مهمترین مصداق؛ قانون مالیات بر خانه‌های خالی و سوداگری و سفته‌بازی در بازارهای غیرمولد مسکن، خودرو، طلا و ارز است که زمین‌گیر شده یا به خوبی اجرا نمی‌شود. یا مافیای فیلترشکن که به جای شفافیت، از بی‌قانونی ارتزاق می‌کند. در این شرایط، مهمترین وظیفه قوه قضاییه نه شعار، که برخورد قاطع با این گروگان‌گیران اقتصاد است. ملت در گروِ تصمیم شماست.
🔹
هفتصدوپنجاه‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/akhbarefori/652698" target="_blank">📅 21:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN4LchX0_UQlzKUnkS5XkUH6tgQ8iqCCPSnYwv5iaLDYUrlQKPcI2alzstjR4Vysk22BFWS1vWyOYctPCWsQ4Yh_-XfEuczO3h_Bcdn5JIUUjHjm4Z1cqivXHTUKGkzrah7vzPjzVFVVPp8HEeVA40VziNstNmYDAHckTpvCe1qEVypafM2p54O00MQnN9tjkyJEEmC91btRmR3bEoim3c810RkdLMnM3G-G9yHt5RoLJbcsvZ48KTscvQULF4_WN7ITEOIooswuQ9k80FswrKlpambjcpi64I8WrqA6ZSrKJzy8bWQgHY-NKlzOVKIpFh9-vZrC1dbdS46wfJ6ViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای نقش وزیر جنگ آمریکا در کشتار کودکان میناب
🔹
وبگاه آمریکایی اینترسپت نوشته است:
🔹
گزارش افشاگرانه بازرس کل وزارت جنگ آمریکا افشا کرد که هگزت عمداً جان غیرنظامیان را به خطر انداخته است.
🔹
این گزارش نشان می‌دهد که پنتاگون هیچ‌یک از اقدامات الزامی برای کاهش آسیب به غیرنظامیان را اجرا نکرده است.
🔹
دیدبان ارشد پنتاگون در گزارشش اعلام کرده که کاهش شدید بودجه و نیروهای «اداره کاهش آسیب به غیرنظامیان» در دوران پیت هگزت (وزیر جنگ آمریکا) توانایی این کشور در حفاظت از غیرنظامیان در مناطق جنگی را عملاً از بین برده است.
🔹
بر اساس آمار سازمان «ایروارز»، ارتش آمریکا در دور دوم ریاست‌جمهوری ترامپ بیش از ۲,۰۰۰ غیرنظامی را در سراسر جهان، از ونزوئلا و یمن تا ایران و سومالی، به قتل رسانده است.
🔹
در جریان جنگ با ایران، تحقیقات نظامی افشا کرد که بر خلاف ادعای ترامپ، حمله به مدرسه ابتدایی «شجره طیبه» در میناب که منجر به کشته شدن بیش از ۱۵۰ غیرنظامی (عمدتاً کودکان) شد، توسط آمریکا انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/652697" target="_blank">📅 21:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui1uExhZOay5nvB-RmCP90Eql5MP-YXi69nMDgo7IENP1E0nUS08ucgDWt_RCfnLS3pyH_t_jMyY0LuL7r2fTKeZoPkoABvGWzLDYg1OOSdNxdwBxFEVgtQebT0RsRWbcVglxbY3jVbRra-c8V2EYl0VwvSGpmjLrUmn2Mb94U_LAOt-uwiwqP5iRGsC-HEz3GunpJQC5tGDjWViqM14CCacnptXPBt-wyfgqUkcRtmYu69v-siTP1XuipAzCAs0PNZpBL6rgLmr60RFJYJBgfbMKlfokmRb8Qy35Y6aS8zEjR-qlwcVDA23Qz0K9SfTCkwFFZo3iVug-PWPGkAA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار وزیر نیرو به پرمصرف‌های برق
🔹
مشترکانی که بیش از سهمیه خود، برق مصرف کنند، با جریمه قطع برق رو‌به‌رو خواهند شد.
🔹
مجوزهای لازم برای قطع برق مشترکانی که مطابق الگو مصرف نمی‌کنند از نهادهای مربوطه گرفته شده است.
🔹
اگر مشترکان، ۱۰ درصد مصرف برق خود را در مقایسه با سال قبل کاهش دهند، روی قبض برق آن‌ها ۲۰ درصد تخفیف اعمال می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/652696" target="_blank">📅 20:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652695">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ترامپ به Axios :
🔹
«وقت در حال تمام شدن است برای ایران»
🔹
و هشدار داد که اگر ایران پیشنهاد بهتری برای توافق ندهد «آنها ضربه بسیار سخت‌تری خواهند خورد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/652695" target="_blank">📅 20:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8468cec1.mp4?token=dP9EPEnbLW6on9Q4iLD96z-Q9Zd6WLUiajV0why9YAnIIMYBWYbBoAq6OMPNsyKFjgfT-mUiTL6S_KXiymhg-omi3hTtYBodrXNhIeu7Imb7o4kP2l5jmKVol_2FqyDwn-En3SfsJJwY9ZV7V8cKVxl47JJeVmPDTA1im8oZy0045O7YM5r0dX3On4hd26vocq-uLP0_d9uOK5RceoVObIlScZQOkppLBYjSbjm897Azdckp0qh3E58I0HUzc9D0z9M6RZVS4dZ3FpC2I8ROgXMUPQP013WfcyfBWo5MQv7rpcfdskKrsa_H3LdbjkheKe5z4jxJQQC1tgkOeJpQZJZVL_jo7fNajAt5dT71TtKJbRMC75GbxvNakpfAICf51klfVgUedo_Y7XiEmFVjvYWXhjoXMqmTzQuHDgKxvJ2VfWnkhV8zvbopv9jE9Bfc27CjSCJsvOw5zTl3A3CLu5ZLcCs4LjiAcS7Q-8MdUvhzFKg8nVzpees6QXcyz4qLcxDu4r9j3uzDWsP2i8ZjeN0H9OyslK0m4Nu7Vy4ATYqDp0NBHhlnEWjt4YQd4LcQUU4U0a2jsdOqmQeMJ9xAPELAga-nIWsc8urXXpr9FSF26IkPu4NcypCVWa68M_ufUfi2Ojv2ip1FrnP_8jzJ_ixFBtrupHPSoPWUVn6Rb08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8468cec1.mp4?token=dP9EPEnbLW6on9Q4iLD96z-Q9Zd6WLUiajV0why9YAnIIMYBWYbBoAq6OMPNsyKFjgfT-mUiTL6S_KXiymhg-omi3hTtYBodrXNhIeu7Imb7o4kP2l5jmKVol_2FqyDwn-En3SfsJJwY9ZV7V8cKVxl47JJeVmPDTA1im8oZy0045O7YM5r0dX3On4hd26vocq-uLP0_d9uOK5RceoVObIlScZQOkppLBYjSbjm897Azdckp0qh3E58I0HUzc9D0z9M6RZVS4dZ3FpC2I8ROgXMUPQP013WfcyfBWo5MQv7rpcfdskKrsa_H3LdbjkheKe5z4jxJQQC1tgkOeJpQZJZVL_jo7fNajAt5dT71TtKJbRMC75GbxvNakpfAICf51klfVgUedo_Y7XiEmFVjvYWXhjoXMqmTzQuHDgKxvJ2VfWnkhV8zvbopv9jE9Bfc27CjSCJsvOw5zTl3A3CLu5ZLcCs4LjiAcS7Q-8MdUvhzFKg8nVzpees6QXcyz4qLcxDu4r9j3uzDWsP2i8ZjeN0H9OyslK0m4Nu7Vy4ATYqDp0NBHhlnEWjt4YQd4LcQUU4U0a2jsdOqmQeMJ9xAPELAga-nIWsc8urXXpr9FSF26IkPu4NcypCVWa68M_ufUfi2Ojv2ip1FrnP_8jzJ_ixFBtrupHPSoPWUVn6Rb08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«باب‌المندب؛ دروازه‌ای که اگر بسته شود، هیچ جایگزینی ندارد»
🔹
از جهش یک‌شبه قیمت نفت تا شبح قحطی در کمین ملت‌ها؛ این همان کابوسی است که جهان در لحظه‌ای که تنگه باب‌المندب به طور کامل بسته شود، با آن روبرو خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/652694" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
یدیعوت آحارونوت، به نقل از یک منبع اسرائیلی: اسرائیل در حال آماده‌سازی برای کنترل ناوگان آزادی است که هفته گذشته از ترکیه حرکت کرده و به سمت نوار غزه می‌رود
🔹
ما کنترل کشتی‌های ناوگان آزادی را به دست خواهیم گرفت و شرکت‌کنندگان را به زندانی شناور منتقل خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/652693" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhqTtRUtOowOOhORgqG26NV-eY-FN_VUxMMZ5OQ1sIs96XkYP_OSWmQWviWcX3DN2rlU1_9VUs5VdeeHbAySBS7oTXF7POp05djk6Ew2wDKJ6DANiyJJqIPtEr4wXjloHshq2ndoFRprNEdf_YuoqDL5o2v8jUOVnf4tgYoMRVW-tgJpzNDOaIg7DR-6Zgk4Y1AVQEGFqhw60UmGhVeKL4wfNDk0obIrrROAvfE3YykJv12mVYkiBxAxEcTFCu1rR6EG_vilT3rm-25MdO8kvlyaR-DSDuCxvuMaLg5Dyto8B5gGWhEtOmSJAxDlFBZK-6_X80U5FjMvlGOcuqJfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در مصاحبه با رسانه صهیونیستی: ایرانی‌ها باید بترسند
🔹
در ادامه یاوه‌گویی‌های ترامپ درباره ایران، رئیس‌جمهور آمریکا مدعی شد: به نظر من ایرانی‌ها باید از آنچه در حال حاضر در جریان است بترسند.
🔹
به نظرم ایرانی‌ها باید از من برحذر باشند.
🔹
این اظهارات در حالی مطرح می‌شود که رئیس‌جمهور آمریکا ساعتی پیش با نخست‌وزیر رژیم صهیونیستی به صورت تلفنی گفت‌وگو کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/652692" target="_blank">📅 20:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dveduCql-OuG5slZbUvUftepDIa5Z6PkbGW5uiS0gm0vPYaRALZmfoY3xmDa3CUJqkNek7iuFevfGH7mXIBvPvz2--zYw_2ss8O6BrE3lnSOvyMQWASC6VfgHCEDuhKHKVoWA4J5AiacavrCRyv8bQB1XU29rGHgqO6_2HMMQ_Ysikal0qop5huPxUUbZf3EmlARWwGoqWHXxVl1ioRbAhMDhslVyzS3G066cPTOWPSvbzVFn7IOVwdM8xgJZcjlCFz3BbTnMkwc26syQYnNobUv8ShPQgoNOVpnqkuUB9cy1J9uFlaMx4qzUEDMXal0qUiOUxubOBSA4-onjnWtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6n_LN0x2MJKBnEiWOWDF6gyefDrbDfVYrjrpdEYMurlc9qRwz6g6JxTUMm6hemz6KYQ7t9MUn8dsvsNBtQ5k-7ltKWBvXYxpOjl16o1hZjh8bqUY35iB5IYUspC0IyTwfsTGv7NAOb4YT0Splx886YHOdgTfdVu6k4R3kgB-VC8DBK2tVyLnueHdgyUFkZV6ezJ9XOklGbqsacXE4S7PwHGR_1UhxVcayrbGbv0VbVl3d_U-xl_xks7-m7wmqdclA7d2-aW_ZdNxFfLyk6TFuwh_UXp5rj-02gaBhzbrHkC7ObT6ZqxNo0W2CEXulRjmp2397quolzllQ1F6slemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxuVIlLE0tG_uyMUpdLo92EcvckG2SvkREIJzKmWSirfyD5iKBmeT8a4VmqaefspFs5rvM3-8aLZhJ3hMzejd6y0frdCRRgG2shIk2Xk1OrNm-ENYv29wr0hu1Bze-Y43Ov62lWVSKsgRZnkJlBRY9MeKPk1V9wvaXZZJvnZHrUJU3Pb4oxv8AttKQVi-WVNmBF_upR3bEptgLdFt5ufqT1tCS5HTwEKe8njipNz3CM1aYyxExzyjtFzwEinQFSEP3fps8NZDm_oqgjKuOQDadHRhLrlxAu7UZBS1C8-1v-2POSLpPHIbl_RTNW8ZyeNpQ3mEwFdb504k8slj50cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBL9zV1Dq1GvC9fPeyVzorGEmgqshVXWoTym9-XI6_xYcKyGsE0YSG-rkkzXE1KSWbRz7_TD58L2pwc3FwkScnC7LPwLLNmF_OSe7GbaBP0nrKnYrOLMxy6FgHQyUXEZVDkgELbWSMu60P5uxOswuzGlkr0QFtehgPFJrF7wTyQVnoLcj6oTZwDpM2OhhBBhTzIY8nT6iQNxmMgS4LDQ6vjMjxkjRMvRzfy14UA8pv4sYC0IxIvFhbCoToq1-K2VNVKl9uoyaV1zbGW79jaQzAQwq6zTTcONQzxqN0INGDu-bHqRyxisgI1buCEL88FtQGKxsbKTVxlsQxMMbxhTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCNtPDjOJEB9VrLHcas9daYCOEMKOBeuIrwh2dpk9Mxk7JwCAM9O3D-YVZoTqCoTUxpf0r73hSV18ukDz5F2ErR6SC7-0BOBRdE0qmwW15hqeATGWuI5x2onkqNmcwl8FubuC93WLP0XJd58baXSht9dJOFTexnAnwdU_fApZo2uJpk5IWetqkXH7OGP10MSpWab4n2SWhTfo1BN2FE6bcyqcHbKwLm4rqxRRNWFR7fMY-PNXagoOzqRWhqMUIV0Jgl3ciF45k92K85dPaF3VZAJo3ur_UgcNImSzPmFTfCGTWTqMwh-hvw8m8WKMzb0c7HX-6dj-IcBT5wsts8zGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blT1a2S7_kW7nG94DdQyJRgq5vljDpTMLygpsaWBSF0KiwDbhrQ8l-nnCiSiGwhoxVjXeaiZilwgMbpEVO-FEokD-jAgDGJYcgrXAeP0WCXVoKsOqr9BGz16PfEkOizP_hCv3UvoaguNhu6pdxmBZfjk3EHO6Y1dLkg85jHdxebyFXts__yB5TyGA8cdck8eSUa-WknPUwtsDFo3ZTSQEUEMVSwRMaI7FVhOZ8YSqp3pN2-dykX62O1RxNVX5Q-PiuInpCVlszjPT0sAta4eeR_ef_zb-ZxLKHgTN6MbuTg6GxGPh78ugyVK398yYvuBOfp_J-Cv4P4aZPa-YWjxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzqDA8j9nfoBbLjqZdSiPSwm3mf9gT3AxN7Ququp_xPDY_FoaW47CGs_Kr8Y2QWAgTNkcE58s9wZZgINQQtqhrlHoki-YUmJdIYda5ruWWwwRmfkv5pEe9IME4ocIE7Cvbmj0wnT24SsKEtyqgvrzwpjqpDeXBLjcMa1N4cXCPV00CERjgLfXJO4EsnyFBaUxJyXtfzyait03JLklUFiThhZb0Wcs52A2S5uBv7kNYKwAkjoqdwF5tL5QlnJFNIEI3Yj3Mz1o80VumBQntPz-8_eEtQH60qTBA0hrS6MDznMeNbAYuwvnx81A8CwUBQEcBuNfYEweVg5kzJtNzCbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f20vMxA6TN3ShitdJCOwy1nnvidbDicvpJs2Aa4PqLTBxsMyN19z2vKopQ6qx1bMUY3OyQWMV_mdARfHFU-ka3Wlh4kor8quzyhnM88nsKa7qUBJl4NASDOEWS4349p1MMTQhtJyoa3GVZGqBIZgQf36O-lwnXbcjHCYgpBISdbZ4dP5eTiZHe6J4o7MaS5iF63lDyI65rG7pN4Shh10yxp1LKOc55o_00eyRsokRC4Z7ZbCo164QIEHVGT6Ly8DmlotPhzMAIBxaxraxfG3zm8njST5_6LhiOuMvZJwA3vKbQKQbyPDDIjxBkXwRpNDozOv_031JF4uv-oILW7udQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk8q0XybYjzgGuTs_551MqtLwpRRUdHn1DhEMNfo-4O26P5ytl51uHDVV0-LUvn7FaBBD73S_3nNjYdd97f0gSllknexsvGJYEqoZFPcBSCWaeEl4_xV4dckaHgYY9_x31V3RYTjlWQl8xVquzI-xjlvSevw5tajihvCt5VlygvR2abEYhraNFif1i-1YB2mmTAFiB1d9sg1zR7ZUAgStaVrnqpOW-BPJDwOqVaaGioVX3DdFLZCLliZRoco-lzDJ8N0eoQQ111kRLUFogVAN24hxOBxxq57AxhLo-x3omQkAlDGUI-tK5hVTMixTMiijuTFIVi7LYjAUe_ryB-P5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjsLRF4zQPEx7xp6c9U4A4lEau3TJIHDAK4rJgojJc-UlU_j6Uoysy-FVcKsi0eI1mo-v1P3_4UDxIS9uIWrtFdXWIeDXh4F4mgCZa3muv8kIU_tdIu2MOz24StbG15CDhmpZbbD9rhA5bk5I_P8352IsX9m3_9h6BaiwiCnj22ya_4ebjznfR1FWTgnftN7fyOeKXEctEjZ79i5JgG3WFf7uVhGmtiBGLvefHGzqMfBSre1SJugFs92OrLhtI2BktxakoiEzRAJgPTmqUg_vyUJOitH8XwkPOV75RMLpIZJt2k6A7tMQn9LP8Y2D8KE6er8UWb1lPKNlHlgoQ7RKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/652682" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652681">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDvDKRhCESP-daiu8XWVxVyiUdBoZhFHaqy8i1MASWWl8zRu-Jm36LATpCI_6DfCV_Y30Ui0hCI2ujeLng1-5voxW5xC2rNjHMNxmxJxjStOpW6visCZuQ3DME0l1f3nLEVFkWcBYnKonC9q9Rma_cTpBHToy5OEwjeh6zfzQOG2MKGkwldoHgoC9fcUp7I9RGkpqMwB4sNad22QFrYuxFeMGGKKOKrrxbwjcizjjCxzvNawrKPrJu_bAa4OZso6-JbPaNytmfw7N_1AMNrqNIWMOF_-hSzOM8hSWYAik9y196oHmJVpohepxmUICQB_VNHSlAPYIVwzQT7zh_e-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست با دامن شدن فیلترشکن فروش ها به رسانه های معاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/akhbarefori/652681" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652680">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSqjkbmdDlFsvE0rWchlsBNiCU8vRMgDcTdX4z-P9IgbZ09ZwqVRcnplyLikPHeU3RDplqkp7yco8KrfpkI3OwwqYoO8gmqlzi2zfrrYDdxPFzeRmIzArhe7JpnZtUJaxS0aCRnYywbpWc1HyimCkgM09F1EHZjrqa3H1AAEaBOhLvgtaTr1_IqZ_pQ6c2tkpUuZOQg54nHpAwlP1GKSP-weGb8Zv_kBHtqIXNEKMbNqyM7v4pJaky7f6spd4Dwv3pftR-1_xDIqEN_ogpRmRtLCiAXelR38GU1baHOrT9uMWyDAV9E46CDkHqTfKK_NKLkKIa8IOjUZ_7wc4ibiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان بارندگی کشور در ۶ سال اخیر؛ امسال رکورد شکست!
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/652680" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652679">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1650f70a.mp4?token=ahuZn1hp9g1bGUzUCt6mh_680eBVwh7kbBwmETVsWfjGske52ObNyo4hpjfDTpSWw09FvV6t_FIKMi_Rt_HiziO-i2iRCm-LzC8LXk9KOYE_tMqU-Si3KGWtBEIaiJdN2z5pVv5xaAPgmDCKL8UQ0FVkk9p-4lTLBlYzMF21LN5nCq1459VxtIF62XBIPK8nW7aMm_WMH5wWSURoQMYw47vHuLG21gHG7rptCvrTML6kqVsrCCFePrh_PfCFkreyj17Tte26ZxCjVmGbhO50-l0-DA9bpxfnwJ9QB8O5f38sU29GSO66d_UmAHiFYmu_D-kRGWvlCfSONx0LBs8StLpOKeUFLqv0fBz-7Abm55WYYI6o_9Czubn5rEHM7DJiYWDqw6WhN2irjxqsL_ZuVi2GdiHW8v4eNNopd_V57-BwyFTSzfggwSeILwyrga37c0yNDgknK3C5eHD-lCm1Y20bU-bs6i_tMxuuXIkCX5seT7rQsVqSoCK2jzPFSs1idrEEK5anTNeha6i2YxiwC8xEFoCRpI7dvC5r2YE9ulZtAm8bJTmqvTnj3S7oWXWTOk6o3E2ee_gRZC9Q7nmlB1AO2gfqFYxs2UAtCiFb76M-TNoVSc2KR-X45MAZgX0yVUF6c70eIIHrIUT-oeStJLkYhKxrDKBTvUI1K45e5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1650f70a.mp4?token=ahuZn1hp9g1bGUzUCt6mh_680eBVwh7kbBwmETVsWfjGske52ObNyo4hpjfDTpSWw09FvV6t_FIKMi_Rt_HiziO-i2iRCm-LzC8LXk9KOYE_tMqU-Si3KGWtBEIaiJdN2z5pVv5xaAPgmDCKL8UQ0FVkk9p-4lTLBlYzMF21LN5nCq1459VxtIF62XBIPK8nW7aMm_WMH5wWSURoQMYw47vHuLG21gHG7rptCvrTML6kqVsrCCFePrh_PfCFkreyj17Tte26ZxCjVmGbhO50-l0-DA9bpxfnwJ9QB8O5f38sU29GSO66d_UmAHiFYmu_D-kRGWvlCfSONx0LBs8StLpOKeUFLqv0fBz-7Abm55WYYI6o_9Czubn5rEHM7DJiYWDqw6WhN2irjxqsL_ZuVi2GdiHW8v4eNNopd_V57-BwyFTSzfggwSeILwyrga37c0yNDgknK3C5eHD-lCm1Y20bU-bs6i_tMxuuXIkCX5seT7rQsVqSoCK2jzPFSs1idrEEK5anTNeha6i2YxiwC8xEFoCRpI7dvC5r2YE9ulZtAm8bJTmqvTnj3S7oWXWTOk6o3E2ee_gRZC9Q7nmlB1AO2gfqFYxs2UAtCiFb76M-TNoVSc2KR-X45MAZgX0yVUF6c70eIIHrIUT-oeStJLkYhKxrDKBTvUI1K45e5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده پیشین فرانسه در سازمان ملل: با ازسرگیری حملات آمریکا و اسرائیل، ایران وادار به تسلیم نمی‌شود
🔹
ژرار آرو، نماینده پیشین فرانسه در سازمان ملل: آمریکایی‌ها و اسرائیلی‌ها ۴۰ روز دست به حمله زدند، اما نتوانستند ایران را به زانو درآورند. دلیلی ندارد که با ازسرگیری حملات آمریکا و اسرائیل، ایران وادار به تسلیم شود.
🔹
بر خلاف ادعای ترامپ، ایرانی‌ها توانمندی‌های نظامی و ابزار لازم برای پاسخ تلافی‌جویانه را حفظ کرده‌اند. اگر آمریکایی‌ها دست به حمله نظامی بزنند، این اقدام نشان‌دهنده ضعف و بی‌برنامگی آن‌ها برای خروج از بن‌بست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/akhbarefori/652679" target="_blank">📅 20:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652678">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5sl9Xje9AMm48cKXPmks-tZyK6QJ8XvoeJXupo9WGa4_Yy14sh4dcqalp3PSiOy0JNQ3wRhT-k4YwkQx7cax6vlWIj9MxeUICBCVJGcHNyEnhRJGRSJEgNWVi1GTrwfSAIXb6kPEx1zbpOgj4z5BP_gF-x9EZeeazGYntUlDcIT2O4AZ-dYmsR_5TT5LAE8Nt2GbJBbNc9AvAUDvQ4R51a16heG1U4ljYwZ8Wu3dVEaNRfyWH70ckBdUSOPvzUAGW7MJ9pVAUtA9umvUdioRGuB2SlcHSqDAsdefOXS9DLJcq8VJA1C5sCmmJ8Uo9HXv8UghZAnB5IQw7FuxUpzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح عربستان برای ایجاد «قانون هلسینکی خلیج فارس»
میدل ایست مانیتور:
🔹
عربستان در حال مطرح کردن ترتیباتی مشابه «قانون هلسینکی خلیج فارس» با ایران است. این توافق فقط یک قرارداد سعودی-ایرانی نخواهد بود، بلکه به خلیج فارس و اتحادیه اروپا گسترش می‌یابد.
🔹
هدف آن تثبیت عدم تجاوز، عادی‌سازی ساختاری اقتصادی و مکانیسم‌های نظارت و اجراست. اما توافق عدم تجاوز خلیج فارس-اتحادیه اروپا-ایران بدون آمریکا، یک خلأ خطرناک ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/652678" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652677">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba03a97bef.mp4?token=wB2ZaL00oz2IIpG2VaJD7fzhKqEXCE1n9L4OJ7rWytM-XFqA6QsIyiJ0zk-I2AweNVZaaztpoYr93jxs9PEPQ1D0GBDHo1iTyVfav_D12ZtP_jkwo9z_zD1gJhWIc80m78RAPtS2lxbzVbE0BirHLgCmOUa-0uxC6avGcdmjfeUa9yq1guMO5kn86Fqkdtz-ykeCkBI-DkkXlWQ9h1Cvqr6yPWFZxywU4FowgycsS5IbRwhQy7E85fPFbEG5H-FmWne1IYNqxELo4vSzyFxUmEB8Xzbj9k9qngNbXqxosieH2uzm8Q8HhNRXtUtYu2boHjAvwDdAkExmB7vGHKC8PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba03a97bef.mp4?token=wB2ZaL00oz2IIpG2VaJD7fzhKqEXCE1n9L4OJ7rWytM-XFqA6QsIyiJ0zk-I2AweNVZaaztpoYr93jxs9PEPQ1D0GBDHo1iTyVfav_D12ZtP_jkwo9z_zD1gJhWIc80m78RAPtS2lxbzVbE0BirHLgCmOUa-0uxC6avGcdmjfeUa9yq1guMO5kn86Fqkdtz-ykeCkBI-DkkXlWQ9h1Cvqr6yPWFZxywU4FowgycsS5IbRwhQy7E85fPFbEG5H-FmWne1IYNqxELo4vSzyFxUmEB8Xzbj9k9qngNbXqxosieH2uzm8Q8HhNRXtUtYu2boHjAvwDdAkExmB7vGHKC8PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفوذ دستگاه اطلاعاتی ایران در قلب نیروی هوایی رژیم صهیونیستی؛ اطلاعات فوق حسّاس در اختیار مأموران اطلاعاتی ایران!
🔹
گزارش ویژه شبکه عبری «کان» رژیم صهیونیستی: دستگاه اطلاعاتی ایران توانسته به نهادهای امنیتی اسرائیل نفوذ کند و اسرائیلی‌های بیشتری را برای خیانت جذب کند!
🔹
پس از پایگاه هوایی «تل‌نوف»، این‌بار پایگاه حیفا تحت نفوذ دستگاه اطلاعاتی ایران قرار گرفته است؛ اکنون اطلاعات و موقعیت‌های جنگنده‌های اسرائیل در اختیار مأموران ایرانی است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/652677" target="_blank">📅 20:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652676">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال تغییر ساعت رسمی کشور
علی بابایی، رئیس کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
موضوع تغییر ساعت رسمی کشور از طرف دولت است و در مجلس بررسی شده است.
🔹
لایحه اصلاح ساعت رسمی در نوبت صحن قرار دارد تا تصویب شود و در روند حفظ انرژی در کشور موثر است.
🔹
تغییر ساعت اداری به جای ساعت رسمی کشور، تاثیری ندارد و ساعات اداری تغییر نمی‌کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/akhbarefori/652676" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652675">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
خرید ۳۰۰ پهپاد رزمی توسط کوبا
🔹
بر اساس اطلاعات طبقه‌بندی‌شده‌ای که به دست وبگاه اکسیوس رسیده است، کوبا بیش از ۳۰۰ پهپاد رزمی خریداری کرده است.
🔹
گفته می‌شود کوبا از این پهپادها برای حمله محتمل به پایگاه آمریکا در خلیج گوانتانامو و کشتی‌های نظامی آمریکا استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/652675" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652674">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای رسانه اماراتی از استراتژی اسرائیل برای جنگ با ایران
صدای امارات:
🔹
استراتژی فعلی اسرائیل نابودی کامل ایران را هدف قرار نمی‌دهد. بلکه بر انجام «حملات دردناک و قاطع» علیه تأسیسات ایران تمرکز دارد.
🔹
این حملات برای شکستن خطوط قرمز تهران و مجبور کردن رهبری ایران به بازگشت به میز مذاکره ظرف چند روز پس از شروع حمله کافی خواهد بود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/652674" target="_blank">📅 19:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652673">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi2Y9goDCTKjGe3FcHvoYo4aOlHmBlVP8y6SaBffSskgPahr_-SEulA6iG7ijAIjgOjIAk55p2wF0r6XZIbo8_US4QbyNaNVkj3xWZoR7_XFCHWhdXkrgzjgTqb6INYyLTS3tN6j21ct4NQX-k0ZeFOg-rHPyebbmgotZpMU7ehrTiDh4uC3cGvMc-gZ9UGt1zZon8qLwSAHTt8-s0hDCgTolz4OgF2Qa4d2h1cSEHaf23fzJgje_tEHTZP-BQPs6VLZwEORj3ucC8rSs_0jGALm-6eRGxpFJTJ9hS0CqC3z5wl59Dfj86RdQWV6KIIIO1xFBNVXVQDyHLHTOoFKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون حمایت از خانواده مجلس: میزان اعتبار وام ازدواج و فرزندآوری در بودجه امسال ۷۴ درصد رشد یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/652673" target="_blank">📅 19:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652672">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9362afbca8.mp4?token=BMUTM5YlBuSNTiwoiFOgpNr-Ue6drhQFQmHINe90m9HTSIUwfUTwE6-UulaHUJmdcw7M3Irq2Qm9GZeM6TXXitzavl6M6l4xBghG1P-AseFVbolRDif5YbqcZ2wZceGduJriha2EHTgmewj73xiIK75E-N361lNk_FHKQ4M6puPJasm_19BVaF-ZoyIhAc8-r55U37LvMhNUseAZ1zq2-zuRixuNEFSa5HW49_HqIf3Nq5mnwhdtwJW_5O4CTFOeasyWKu-b_tqSAfQulNB56V9kvVtXE8SgQNvvGKx-Qq6HgY9LU0YjQDNrAYfsuaf8HEnRp8Aehf31voEaIxu_lDUnH4I3TK9BjVit5RT9PiaB-9TdV_9Hjwn2TRadwJmEnpBAhCHb7eJ5RmVBf0_rZ_6CB9HJt2sjIRgXA1I9QXHBdSRLi6cHGERM-TAVKMW4_6knguGa0FkazdVmZuphxT0HErHZnay9Fzptrkoad7gpmSk3o6bEzwTlIlJAAUja-3SvqA5PoAkIVbiJKVZD3YEGHo3wLk1a8LrGo0XcH3v3YRp-T81c9Vl3gotyS51tGH1rsL4QE1Yr-XGnBHTMUWLNybBsd-fj3B3vvxKxfilwGonWolHpbuZRJd1RDJ48FSP5b2zWS6Cd_VaWspUEWxg6abrC1_XKEotwjyBYRb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9362afbca8.mp4?token=BMUTM5YlBuSNTiwoiFOgpNr-Ue6drhQFQmHINe90m9HTSIUwfUTwE6-UulaHUJmdcw7M3Irq2Qm9GZeM6TXXitzavl6M6l4xBghG1P-AseFVbolRDif5YbqcZ2wZceGduJriha2EHTgmewj73xiIK75E-N361lNk_FHKQ4M6puPJasm_19BVaF-ZoyIhAc8-r55U37LvMhNUseAZ1zq2-zuRixuNEFSa5HW49_HqIf3Nq5mnwhdtwJW_5O4CTFOeasyWKu-b_tqSAfQulNB56V9kvVtXE8SgQNvvGKx-Qq6HgY9LU0YjQDNrAYfsuaf8HEnRp8Aehf31voEaIxu_lDUnH4I3TK9BjVit5RT9PiaB-9TdV_9Hjwn2TRadwJmEnpBAhCHb7eJ5RmVBf0_rZ_6CB9HJt2sjIRgXA1I9QXHBdSRLi6cHGERM-TAVKMW4_6knguGa0FkazdVmZuphxT0HErHZnay9Fzptrkoad7gpmSk3o6bEzwTlIlJAAUja-3SvqA5PoAkIVbiJKVZD3YEGHo3wLk1a8LrGo0XcH3v3YRp-T81c9Vl3gotyS51tGH1rsL4QE1Yr-XGnBHTMUWLNybBsd-fj3B3vvxKxfilwGonWolHpbuZRJd1RDJ48FSP5b2zWS6Cd_VaWspUEWxg6abrC1_XKEotwjyBYRb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسه میناب؛ تصادف نبود، الگو بود!
🔹
در این ویدئو حقایقی را خواهید شنید که هیچ رسانه بین‌المللی جرات بیان آن را نداشته است.
🔹
این حقیقت یک واقعیت تاسف‌برانگیز است.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/652672" target="_blank">📅 19:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652671">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5394e22d.mp4?token=LcIpbvNfe11eWFBXqrnMtv6nJv5e0w4Njks06KR1pocvXgE2dWedjtYzXjLVVoRwqQ7e_KyyFhsaEitelZYoiw8l0gQAGLOWF_Ba6kn5wG6XzQCJ0LkZH2PLctfdRLFSzdjLfSWVBBY7a9Nb29p85qEb6EVmoA3oyx-_NP8xUi5AlJfYlq9xOrLnMd4ch9btvbh7JIURlMhjy4KF3ZS7uedgyf8NVyVj4D5bk-KTdvpeO_kcVgULh_cpPNbmSa0V9Lkry_R31_WmPBwuaApQK1OOVakWdSQA0by8F5ZKGYu3uVpH1lPln28mUHs5YaxWCeKGOkEPP0d5n5WsOBtHEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5394e22d.mp4?token=LcIpbvNfe11eWFBXqrnMtv6nJv5e0w4Njks06KR1pocvXgE2dWedjtYzXjLVVoRwqQ7e_KyyFhsaEitelZYoiw8l0gQAGLOWF_Ba6kn5wG6XzQCJ0LkZH2PLctfdRLFSzdjLfSWVBBY7a9Nb29p85qEb6EVmoA3oyx-_NP8xUi5AlJfYlq9xOrLnMd4ch9btvbh7JIURlMhjy4KF3ZS7uedgyf8NVyVj4D5bk-KTdvpeO_kcVgULh_cpPNbmSa0V9Lkry_R31_WmPBwuaApQK1OOVakWdSQA0by8F5ZKGYu3uVpH1lPln28mUHs5YaxWCeKGOkEPP0d5n5WsOBtHEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی رهبر شهید انقلاب در سال ۱۳۵۹ از افزایش قدرت نظامی ایران
🔹
عطاءالله مهاجرانی: در ۴۰ روزی که کشور درحال جنگ بود، هماهنگی مهمی میان میدان، خیابان و دیپلماسی بود که این هماهنگی همان آرمان رهبر شهید انقلاب بود.
🔹
یک هفته پس از سقوط خرمشهر، هنگامی که جلسه‌ای در کمیسیون دفاع در حال برگزاری بود و فرماندهان وقت از ناراحتی سقوط خرمشهر گریه می‌کردند، رهبر شهید انقلاب گفت: جوانان ما ۳۵ روز مقاومت کردند و حتی سلاح کافی برای دفاع از شهر نداشتند، اما به روزی خواهیم رسید که دشمن خیال حمله به ایران را نخواهد کرد و اگر هم حمله‌ای کند پشیمان خواهد شد.
🔹
ایران به نقطه‌ای که رهبر شهید انقلاب فرموده بود رسید؛ کشورهای زیادی ترامپ را برای حمله به ایران سرزنش می‌کنند.
🔹
ان‌شاءالله جنگ پایان پیدا می‌کند و کشور را با سرمایه اجتماعی، سیاسی و ایمانی بهتر از قبل خواهیم ساخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/652671" target="_blank">📅 19:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652670">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeZg8COUDp-oPaVKBh6zTKKcqD_wV9yCwQ5O3iZMTgZc7VnkeyS-14dwDYkDdm8UvNHGl9MBRtUd4cuuzHalPLe0vmRsLk8VwFO7akxzJ2fcyAHss4jJZsaKa7v_mQMYCnZbC8ot8l-6nLRMsoMCKsdvPhsEUQlPTz9jtmMUHNZ7imhBO3gg3A28f5IKEqnZUDOwpsvyn_xqMW_gked_OUQuG2LT5fhH_9d9U5xXZVnxBP6uTEFiVG52anXe-yuqk5L3LlnLfxJqCbzESF_mD3_bBW9U6ofPZdmj2PP5XiBq8tTlJUUeLToDPtjq_dEGSQ3bmjTiwUpUs9HjCkEi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتخاب‌های کوچک ما، آینده‌ زمین را می‌سازند
🔹
با کنار گذاشتن لیوان‌ها و نی‌های پلاستیکی، می‌توانیم هم از طعم طبیعی نوشیدنی لذت ببریم و هم سهمی در حفظ محیط‌زیست داشته باشیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/652670" target="_blank">📅 19:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2664909396.mp4?token=UZu83mhNEcyYEjX0MDBu4bU7xCGb6FXcWYjTcuB-KiHzt_tEoS14VS45oPjIqMXqCzv1StCCv2gZ3y9fAPPX4gLWiNxhaSe__-1Od8WOwTiBxf0-3PQFC9OXJjaD4Xr9zQEXeq4AUAsG4JduvZa3JrDpwIAHUzFlkh3m86yfPBi5YoE1xFXFC9kVQaOTESKwoXvTadT6bhFttI-smj2r3FrUACr9YnnlsqA0ubX9cqdEsZ30Mfpdxv7KzVNMyq1BoUR71btJgAeuMshDYKXW3rHkLsf8ELCs1Y8WV-_VDa9K20G2WhIn-nqJVo2hXPn-ci6rqosTzTyezs4wqKhOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2664909396.mp4?token=UZu83mhNEcyYEjX0MDBu4bU7xCGb6FXcWYjTcuB-KiHzt_tEoS14VS45oPjIqMXqCzv1StCCv2gZ3y9fAPPX4gLWiNxhaSe__-1Od8WOwTiBxf0-3PQFC9OXJjaD4Xr9zQEXeq4AUAsG4JduvZa3JrDpwIAHUzFlkh3m86yfPBi5YoE1xFXFC9kVQaOTESKwoXvTadT6bhFttI-smj2r3FrUACr9YnnlsqA0ubX9cqdEsZ30Mfpdxv7KzVNMyq1BoUR71btJgAeuMshDYKXW3rHkLsf8ELCs1Y8WV-_VDa9K20G2WhIn-nqJVo2hXPn-ci6rqosTzTyezs4wqKhOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: گمان نمی‌کردم قدرت موشکی ایران این‌قدر بالا باشد
🔹
باید پدیدۀ شهرهای موشکی را به‌عنوان امکانات درجه اول درنظر بگیریم. ما باید در کشور شهرهایی داشته باشیم که تمام امکانات حکومتی در آن پیش‌بینی شود که در صورت حمله به امکانات‌مان گزینه داشته باشیم.
🔹
باید برای مردم هم پناهگاه بسازیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/652669" target="_blank">📅 19:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiDx0qHlEIIDl7L3jUQ2FsfoDuHSdcgLknQv3MKX9NdJ9L0hJ-kVkHW2jG7TPQ9tG2UMd6TMl8Y7CEtrEX44JpBnGY2dPyZCY9wswr-GwxY2CO0ytL5cimLwKIrVK7FsiQNCE2Ql3tfpMK6Ie7LGza3nm-GFipU4oct7BMe_S6AMrbVJfKHrQvLZNnAkObsvRimCN-oltxC_sFGiXbGbEcS4atIu4bs0-NN-ttmELlZeOi2fcOVn2myyV43TDx-C6PGen-6ss6KFSKLbyTnjMtjxuDwHbSSbOVO89cy-L1knjWfkKe40wSArbrhfKfw_GWEuztGNzkQ57Zu0zh2oPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز بزرگداشت خیام؛
«خیام را با صدای شما روایت می‌کنیم...»
🎙
🔹
مخاطبین عزیز خبرفوری، برای شرکت در این فراخوان کافیست یک پیام صوتی حدود ۱۵ ثانیه‌ای ضبط کنید و از حس‌وحال آرامگاه خیام، خاطره‌تان از اشعار او، یا تأثیری که رباعیات و اندیشه‌های خیام بر زندگی شما داشته است برای ما بگویید.
🔹
همچنین می‌توانید یکی از رباعیات موردعلاقه‌تان را بخوانید و روایت خود از جهان‌بینی و سبک زندگی خیام را با الوفوری به اشتراک بگذارید.
همین حالا اقدام کنید
👇
@Ertebat_baforii
@Alo_Fori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/652668" target="_blank">📅 19:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
کوثری:دشمن قادر به مقابله با موشک‌های بسیار قوی و پهپادهای اثرگذار ما نیست
🔹
عضو کمیسیون امنیت ملی مجلس: شهید نصیرزاده به دلیل عشق و علاقه خالصانه به کار و نیز تجربه بسیار بالا در نیروی هوایی ارتش و جانشینی ستاد کل نیروهای مسلح، تسلط تخصصی کامل بر مسائل دفاعی داشت.
🔹
در مدت هشت، نه ماه فعالیت این شهید، به ویژه پس از جنگ ۱۲ روزه، کارهای بسیار بزرگی انجام شد که موجب شد نیروهای مسلح دستشان پر باشد تا در برابر جرثومه‌های فساد استکبار جهانی و صهیونیسم بین‌الملل عرض اندام کنند.
🔹
دشمن قادر به مقابله با موشک‌های بسیار قوی و پهپادهای اثرگذار ما نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/652667" target="_blank">📅 19:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652666">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc542899c9.mp4?token=sGYAr3S90-JXcaafGGUQRHL0cI_JEKMJDh1OoUIo5HOyNwz_wbVvt2VLi8lv3752ZGx64Yr2aWmhUI7o6cl5kzpDs7I7RExuunz2GU25C1vt5r_uIs1fwiyziaJktUxP2b5O3-ESf5O-ZvHkFnsryWixKys5gWSE0cyYYiIDSbXeAiRNhrgXvsw1aApyvfyrOydf_aDJgIq7tN6kblne-a-5qk-UgDiFjxG9ISwI2V8vLXjkK5B9M10PatBXAeA3YVSvMBFm9wnsVEgcb_hzqBGHo2GBHULQaX1kVYEIgDF1B23nlIS_AQ5G6SnZZfe_BsQaP0DiCZzVIwW2725w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc542899c9.mp4?token=sGYAr3S90-JXcaafGGUQRHL0cI_JEKMJDh1OoUIo5HOyNwz_wbVvt2VLi8lv3752ZGx64Yr2aWmhUI7o6cl5kzpDs7I7RExuunz2GU25C1vt5r_uIs1fwiyziaJktUxP2b5O3-ESf5O-ZvHkFnsryWixKys5gWSE0cyYYiIDSbXeAiRNhrgXvsw1aApyvfyrOydf_aDJgIq7tN6kblne-a-5qk-UgDiFjxG9ISwI2V8vLXjkK5B9M10PatBXAeA3YVSvMBFm9wnsVEgcb_hzqBGHo2GBHULQaX1kVYEIgDF1B23nlIS_AQ5G6SnZZfe_BsQaP0DiCZzVIwW2725w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات دو طرح بزرگ حمایتی از سهامداران خرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/652666" target="_blank">📅 18:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652665">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiNDEGYcalW3nf-PzYkDDZJDNyU5XOttzKo0bywwasf1K7NXNiIrSVVsMXS_qTQKwjYQF8Zqj8jR-P0i8YpJQV9ZAz1RuPm7pCfqUgX16ex-X2sF-BQPHsOGBQxCd4wS6zIrhduUOM2_xipQI14gDrgvLYaIu2SwCWNTlfdkY2hR4u9VDzVA7rIf6m12EVQ12BjZfLdYI__rPmOO_5z19b_pd9WmZ59MUyoyO7eANM5Q3LW7-qTESfQ2fjRkiWSMkVlzoVYbPiK6iKheaCwzTjurlJol7bN6UU_y8efqq0LuNabdOD8janap6Pb99ekV4HOazv212QJVmuF9vHSgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر| هشدار درباره عملیات غیرموجه علیه کشورهای منطقه و انتساب آن به ایران
🔹
یک مقام آگاه نظامی: ایران همه کشورهای منطقه را از افتادن در این دام رژیم صهیونیستی برحذر می‌دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/652665" target="_blank">📅 18:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
یک مقام آگاه نظامی: دشمن شکست خورده آمریکایی صهیونی که به خاطر تجاوز غیرقانونی و جنایات بی حد در انزوای بین المللی قرار گرفته است تلاش می کند با انجام عملیاتهای غیرموجه علیه کشورهای منطقه و نسبت دادن آن به جمهوری اسلامی ایران خود را از باتلاق خودساخته برهاند و از بن بستی که قرار گرفته خارج کند
🔹
جمهوری اسلامی ایران طرف پیروز در مقابل تجاوزات بوده و این توطئه صهیونیستی را محکوم می کند و همه ی اطراف را نسبت به افتادن در تله دشمن و هر گونه رفتار یا گفتارو نسنجیده برحذر می‌دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/652664" target="_blank">📅 18:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwbKKN7JqnakIVCZXE9SbqjTfYse3sul5fG6FgrZ9xsR4e_y7-_6rfXWm6Fzhcec2p1K4ulFmbDj6LEXkrlYR0PV1urf1cO_RHHG7Ph0O3dCfIiIdOi8lDii2eGn7wBYGGgZWZUAYtCGT4InEfe4Isi04ZArz1Bi5MNQ3r2NkMxC02prbmQ9JpGxJTgfSLgfJ14d9GeSvqW2iMFnQ64Y_2d6WJ_sjMW9ikfSI0NzpyBjCHvhq1D64ne-3ZiKBhRW7R1jLD94phZWKDkaeCAlAKHmy6fgjD6bh4FdJ2SU3733J8_CP5rW-qlwQWipWQAvLBXecuG1MLoCUN0nS34ceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا شرایط ایران را بپذیرد یا تسلیم موشک های ما شود
🔹
سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی ایران را بپذیرد و تسلیم دیپلمات های ما شود و یا اینکه ایران از موضع قدرت با آن مذاکره خواهد کرد و باید تسلیم موشک های ما شود
🔹
از هیچ یک از شروط خود کوتاه نخواهیم آمد و آنها باید با تسلیم دیپلمات‌های ما بشوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/652663" target="_blank">📅 18:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5fBsUeJNpHmuvGcYCTC91AEfxHFUpd-Vq1duWuJFxilLsQH5Jqo-a0OGUTSJpY-OMKTWwQhtWCtyi_jiPA7JfK-kXnaxQGepL6FRK13a5VVaWCg3jNRbSG0SngVc7iiTIhbKVbQnqyiPwbqDenOrlJVZSGJJiEDaVsW34CGSIQGPtQ2FT9JJElwj1PLr6XWuiu-oHz86qQGCvql4gLJrIilOV23F5DcAEs-aKFyx3GDX7Xeqg6H0TTA7StQ30aPMcnmAy2bMW7kJPRt-j-vkGGFHnqiffDbdrVX--K4TYbOJPt6mcTL_XQMfWo3qL1Jwn5dkA_17kwKU7LYxjO6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تلاش ناموفق امارات برای ترغیب عربستان و قطر به حمله مشترک به ایران | ابوظبی در انتظار جزا
🔹
بر اساس گزارشی از رسانه امارات متحده عربی تلاش کرده بود عربستان سعودی و قطر را متقاعد کند تا در واکنش به حملات ایران به کشورهای حوزه خلیج فارس، یک عملیات نظامی مشترک علیه تهران انجام دهند؛ اما این پیشنهاد با مخالفت رهبران منطقه روبه‌رو شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215653</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/652662" target="_blank">📅 18:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnhxoaWTpNTOIZ65jrMXbsAfNF01cYSns1EgIvtOL9JYiCQveTfD0hswtrzOX-5uHo_qHPjCTXNINkYArPf-2ADu-ZqCUgAUA59eq9xFxXwldvKbNMhq3cEy5CMPCIXIWCyAoevJWH0RP9LdiF7mGnEyqBTjKlrMRUNLnSh8B1Df3v6M6C_WigsV92ZT_ilJWvMhsfGiAG-7HK2VEZ2gdwhLW0xXnexSWjqdLfBKAVSFrz1tyRu_zG8OU1199wkrQirG8uDQNWoOJ-lxzZH6Af251alhJvD-iL3WS9C9J1iW9jiqBd79V-U7UeqjchbRqTIvlzgT9vADu_FUqf4UlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام: ناو تهاجمی آبی-خاکی تریپولی در محاصره ایران مشارکت دارد
🔹
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که از آغاز محاصره دریایی علیه ایران، تاکنون مسیر ۸۱ کشتی تجاری تغییر داده شده و ۴ فروند نیز از کار انداخته شده است.
🔹
سنتکام روز یکشنبه با اعلام این آمار افزود که ناو تهاجمی آبی-خاکی «تریپولی» نیز در اجرای این محاصره دریایی مشارکت دارد. هدف از این اقدامات، اطمینان از تبعیت کشتی‌ها از مقررات اعلام‌شده و تشدید فشارهای دریایی علیه جمهوری اسلامی ایران عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/652661" target="_blank">📅 18:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وزارت دفاع امارات: امروز یک پهپاد ناشناس به محوطهٔ داخلی نیروگاه هسته‌ای «براکه» در منطقه «الظفره» اصابت کرد
🔹
تحقیقات برای شناسایی منشأ این حملات در جریان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/652660" target="_blank">📅 17:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0Y_63gY96mS131PrF4LXorcy0-H1umSZucQoavQh8TEtCzqyvKRNzghHSnQUgZPJSMe1JXUPST5R1CcoIUE2_JQ_q3WoIR9rpWG0OdsW3ZAg_CzVcI9YtlJ15i2MbRqmVQIeFNS20udpq7w2uL4lkUwqosPyXx4WMXvfDNRvb-XYkxlNtFJ0TGKsCw1nbQKWVEAAI9yocQLjzh1tuNgPwEfeEWUZHeOqTlkBShan5VS6H3j9YoYz25cKzKq_7gFXnx6rVFHh1ai8GwbiAQDbek5qBjIjMCg8XeprAmiMEwIjvF56QgGS4XlUSYCZw3De7-brZADbbiDe57SkH_Ubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان عصر امروز با قالیباف رئیس مجلس دیدار و گفت‌وگو کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652659" target="_blank">📅 16:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFT_-s1Gvi15Y7VYhHHzfWh8519ko_Mhn05oWoja3x_c27Qqlw9rIKaqto4cdWhsbmG3_b8CIxEUcphMKON4G7xvRnOKYjUHoMhHqxG3kEX9k_BRP12q-ivGLrf3bxYkchDqpGuffsB8wlUhFJ9YX--uOdqLDKV31oEMvHcMCbtZ2Q5BqPm8_YxRKuh1qT5tOICUZ7bEQHXKdLiOQY-r5d_TQWMvsK07St27kOVzdWXvKE38OK-zB-igAK5ToFtVENEWLe49HoM9TFYQn___dipiOG23Vrks4SgRMDokf8pOkvZS5vrolNQhW1oVkd6VQr7EV3nK1u_Sb3BY6fyiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور رهبر انقلاب در امور بین‌الملل: به‌زودی واشنگتن باید با فانوس به‌دنبال بقایای اعتبار خود در غرب آسیا بگردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652658" target="_blank">📅 16:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4968d388ca.mp4?token=IY04IDbu8dltodbyXYyCJDz8qTzVgQJKDdOOguoMzOOsuNlZ6KgBoqF9e1QAxu4bAGSIwOBrQjRcywjwCSwgP9UBRwwZqRkoxVY04GQzBoqywVQSVPsDVHZlIyTlw-1wGVeuLoPd7NQJQ9colzsEvNcn62Fr3GEfItAxcUr1gsdwzGzBaNt7HY1l6HPFi7ofZ1JUyKERoZr2PeDN5MIB3XBMBSGMjKIRDhJaQc-rT6J5AbQVcDHS7rtyc0m7ZfNWxE-Sx6Ja4g08OdajE3H9z6gL5OM1Kqq4JlrCrGcSoF8QrONWWjEPc9f6kpeP0PUvj7IcUhDanS2YofoAJpQg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4968d388ca.mp4?token=IY04IDbu8dltodbyXYyCJDz8qTzVgQJKDdOOguoMzOOsuNlZ6KgBoqF9e1QAxu4bAGSIwOBrQjRcywjwCSwgP9UBRwwZqRkoxVY04GQzBoqywVQSVPsDVHZlIyTlw-1wGVeuLoPd7NQJQ9colzsEvNcn62Fr3GEfItAxcUr1gsdwzGzBaNt7HY1l6HPFi7ofZ1JUyKERoZr2PeDN5MIB3XBMBSGMjKIRDhJaQc-rT6J5AbQVcDHS7rtyc0m7ZfNWxE-Sx6Ja4g08OdajE3H9z6gL5OM1Kqq4JlrCrGcSoF8QrONWWjEPc9f6kpeP0PUvj7IcUhDanS2YofoAJpQg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تصویرِ جامعه‌ای است که پیش از هر جنگی، قافیه را به خودش باخته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/652657" target="_blank">📅 16:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652656">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPZfBfH6M_z7pHZZantMlXy8bPM8Nk-uMhxX3gCappUVcvvNUU6av48jVFCvFSPFsld20JjG1wmudbXW3lAJnwZIrsmPwS3fvqwY69NMn9RqS0eroIp5IDavIvZlkzBhGbO4cW-jccaRP53D8vwExGQSPswSnM6zmZAS7ObyLTyRycNGpwLbUVzUlbPGLTylPKei1Nkdk2Fs5bgFvbABo44HID8BEkNL02wOYqVrGNyyApH_2Uoj0j6ts3x6ToYYQm7CSsQMnQAAbmmuZ1Va5MkceoY8HJyNoioqksUgeVzqv8pIL08y5aMUZO0v_Ug5s6DRQBKkQGryvL5fxTweSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو درباره ایران با ترامپ گفت‌وگو می‌کند
🔹
نخست وزیر رژیم صهیونیستی ضمن تکرار ادعاهای قبلی خود علیه گروههای مقاومت، مدعی شد که در قبال ایران، آماده هر احتمالی هست.
🔹
بنیامین نتانیاهو امروز خبر داد که درباره جمهوری اسلامی ایران با دونالد ترامپ رئیس جمهور آمریکا گفت‌وگو خواهد کرد.
🔹
وی در بخش دیگر اظهارات خود به ترور «عزالدین الحداد» فرمانده شهید حماس پرداخت و مدعی شد: «همه مهندسان ۷ اکتبر (عملیات طوفان الاقصی) از بین خواهند رفت؛ ما به پایان مأموریت بسیار نزدیک هستیم».
🔹
نتانیاهو در ادامه به ناتوانی ارتش اسرائیل در برابر حملات حزب الله به ویژه پهپادهای انتحاری اذعان کرد و گفت: «شش سال پیش، در جلسه کابینه، در مورد تهدید پهپادها هشدار دادم و آن را خطری می‌دانستم که می‌تواند در عملیات ترور و در میادین نبرد استفاده شود.
🔹
با وجود اینکه دولت لبنان در تلاش است به «صلح جامع و فراگیر» با اسرائیل دست پیدا کند، نتانیاهو گفت: ما بر مناطق وسیعی در جنوب لبنان مسلط شده‌ایم و آن را پاکسازی می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/652656" target="_blank">📅 16:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652655">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Jyhhrqleuz217x6ervLcxaRWAOi1V64nuT4Q59aHESEZ6YFWL1KGq57_X9cMuuhPxw8EhcCW93Ieb9KN8HWtUOyGdSd5XFSiqcUiOyrfCPhXHvBKufvIV9UfQxe5ZQj-VRCyQ85BeGZQ4cVN8KfF26v9ww_nytW3i6IW8omZ8M48Zfmk9AIYBcHG-v6CgFKksKYVAvhcvGv56_8CSAh1dq9x4g5iiOtjHjictEragAhWjNVWX0TULvBrJ5XKsUg54ZzENG1scjbzr3kUg6Zur4bjmaUVuiba44tzPf0mmZjCMOMPd8L1J7h-pYHhX2_Xxyp3kE-fg3sIUDceTyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ سوم ایران و آمریکا چگونه خواهد بود/ از تداوم ترور تا نبرد بزرگ در خلیج فارس
🔹
هم ایران و هم آمریکا برای ضربه زدن به طرف مقابل، برنامه های ویژه ای دارند. این برنامه ها باید طوری باشد که طرف مقابل در کوتاه ترین زمان، بیشترین ضربه را ببیند. ایران احتمالا در جنگ پیش رو، اهداف مهم اسرائیل و کشورهای عربی متحد آمریکا را هدف قرار دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3215690</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/652655" target="_blank">📅 16:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652654">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
افشای دومین پایگاه اسرائیل در عراق
🔹
روزنامه نیویورک تایمز آمریکا از وجود ۲ موضع نظامی سری اسرائیلی در صحرای غربی عراق(در نزدیکی مرز سوریه) خبر داد.
🔹
این پایگاه نظامی در سال ۲۰۲۵ برای حمایت از عملیات نظامی (تجاوز تروریستی نظامی) علیه ایران به کار رفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/652654" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAMS5MoQHqXrzHj_VsWQ1Ji3hpXCWthu7m8UkaoJJZg4dj4uhJ6gP9EFslXo0CToERHYOUGZvoODxSkWHH1Ymk-u62nGl8--bsjNLyB9qXmVuaLd-SJOiP9KV858G_xMzyBUMIByZygjQJlA28lD4d44LHY-iH_JJkZhe3ExGuhnOoTw356CLFvuCukld7pukA-5MOs8p5Gxm1Ay_MWyApXaEJr_K251-nHr0L2VXbWChNrN7BNVhkz3shFhKjPAvA7za3y5qfwJhIG3Xj6KSVGWQ74_m-5-8E-fMod2YVOIX5IjjAOKCAS11HSZOJnQ6Ck45zfbbV5bJ0PdbFbMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور برزیل: من با جنگ آمریکا علیه ایران مخالفم و ترامپ هم می‌داند
🔹
داسیلوا: ترامپ می‌داند که من با جنگ علیه ایران و مداخله در ونزوئلا مخالفم و نسل‌کشی در فلسطین را هم محکوم می‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/652653" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae38MHtYdFyBMdEYzg2FfMF6cAfWDraY02JIUwjuBAHN3RgkWCnp11XgrhW8RMsC69xLqFXpHdKeHt262JBE_LrHrwJGyVdE_QtJc7c1BLsyxyLnV2F2eQ-SZDHvG5PmUW-56PPrKdb96c_aWn8H5aU28HEMaUtYvo5scwj6yCsm3llhs1R69pqkJ5dPGHKsZvdvbSpvl0n024FlZdctkAhRfVXHyC8gcMkkmOtpxwBpDiCvWqQQSEhbX92NodRv7lFTnQynTK24PPEoAA6Pxp_jXEjOw4y6kaAxcdz-5nHnsg8ZuJpdAJU59XehD2_7t0Ft7BsgL6DN2v4rMwx9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاکستان خواستار آتش‌بس فوری در غزه شد
🔹
رئیس‌جمهور پاکستان: خواستار آتش‌بس فوری و پایدار در غزه هستیم. رژیم صهیونیستی باید پاسخ‌گوی جنایت‌های خود باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/652652" target="_blank">📅 15:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_GvDLDmnaRCC5LsyMRk_Pk7FAHErPWbJsoJRo4ITME-qhdAJDHY3YZeOpewvD3kvQiIEwha7o2T5f5aHcZpH2gdymbwDaSYZFTwxJPNutt5_RN-D3Jh7Ij02Hm8DJ8h_QFAVF7f7O_O3ZWy6bbbvxLNoDC63QLo3W1fNO7q4AfC6E2PvdPCT__sCtnIjqwzphBZQFRTYxpgcryvVYh6WeKTapn4ci5MuH4EQC3I-O1fgKIzPNzYG2yPFP8_XwgEKNc43U8uCB3Jdsz3Rmoja4lEJ_dqUZRkGrG_1ZphZec8dQKJwLU3D7dI09qNWreBB2-kMthBFqQHlGau3YbFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین تماس تلفنی نتانیاهو با ترامپ پس از سفر چین رئیس جمهور آمریکا
🔹
بنیامین نتانیاهو نخست وزیر رژیم صهیونیستی با اشاره به اینکه امروز تلفنی با رئیس جمهور آمریکا در سایه تحولات و تشدید تنش در منطقه و پس از سفر اخیر ترامپ به چین، گفتگو می کند به حملات پهپادی حزب الله نیز اذعان و ادعاهایی درباره ایران و غزه نیز مطرح کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/652651" target="_blank">📅 15:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652650">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb8a1582d.mp4?token=Lb1ZFer1BzGRHYkC5pFKgfEGTPjkltWClZ7Qxr7bol5cYBCJmAeVuPw1ix2Z4894Brbxx8v5_TDZ43msyOCBPWC0lMA-xP1tPEzAE9q1k4UTs_mhiDesOFD641qVS7ZRTRgW0mX4kIrMOqqm6aPxKsTkjLIZWvrsBLIyOpG9QPAMWvHgKWBFWFwg2SS7P9abQOGg4lZwAqtdb_BwmmuF8LdbMbylGWehvOw1W3XM9_RZOXcR6eFDiiSAFdqSFC0dkXD6wrexf-C6Vcc74H3gT162xl3vlnv1UwOscKpQ2N2XSpHl0DBzqz_8kIx_rvngxxSrFZkjmzbBiaUjRXJEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb8a1582d.mp4?token=Lb1ZFer1BzGRHYkC5pFKgfEGTPjkltWClZ7Qxr7bol5cYBCJmAeVuPw1ix2Z4894Brbxx8v5_TDZ43msyOCBPWC0lMA-xP1tPEzAE9q1k4UTs_mhiDesOFD641qVS7ZRTRgW0mX4kIrMOqqm6aPxKsTkjLIZWvrsBLIyOpG9QPAMWvHgKWBFWFwg2SS7P9abQOGg4lZwAqtdb_BwmmuF8LdbMbylGWehvOw1W3XM9_RZOXcR6eFDiiSAFdqSFC0dkXD6wrexf-C6Vcc74H3gT162xl3vlnv1UwOscKpQ2N2XSpHl0DBzqz_8kIx_rvngxxSrFZkjmzbBiaUjRXJEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجهیزات ارتباطی صهیونیست‌ها هم از حملات دقیق حزب‌الله در امان نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/652650" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b9dba7fe.mp4?token=JLGnqA5oUz4dzjNCj108PCiS-JxiZJbzwFzhgAoK5Goi61eq_udJxsxFEMmBbWwy6B-PL0Q2a_kyRWwzPjFyITbohi4y5yaz6hD36n3wlUcDD_fstteCtf9qwocNKbWhGxYpndInQce-6o-toDT8w-AsyH8mug1dwM1ORHyuINg0zv0VaN7whCE_Mx-11QwpZ0KJ2GNzcfNv3_skne-xAobTaO0-htrWOOI4dopf8IvxqNWxJnkhZERqaGPhz8bKkDjMoJZ_YS5zxVaqD75qgNDZcIGiSxaBiwGPvrGmheg7VeOoNwCJeynpRS58OiF1OnZ9LOp7G_dTaDIypO2AADmuMdmXrndJtcw4_M-2nSGIUC5pfUlxTvJAq7zL8XOjPkySA4LmPQml9AJA7Iyikkf_BqgAVrP6oE112wqwr2xqKVPmql_HkIZxYtTI-_hdLvoy62-Rb2GHvdLjwc2wKRVayvoTG1Gfc6v40zqJ60BCzCUiPbKOnC2ox7aES2LJvKV8bpo1h9yTaea2WeL4R5d7zrrS14wbs3nAh1U3ys0CTTVfP2-prJM9Gn37YL1Xk6qb1oH8s7uxN3IsYoS01jQV8T8p0BkqLcSfSXExhfG5Wb6AhU0JD164H3rbC6nAD27tuK8HabPfJBkqR4iopXUgHehWPmrowqgWB8EGDwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b9dba7fe.mp4?token=JLGnqA5oUz4dzjNCj108PCiS-JxiZJbzwFzhgAoK5Goi61eq_udJxsxFEMmBbWwy6B-PL0Q2a_kyRWwzPjFyITbohi4y5yaz6hD36n3wlUcDD_fstteCtf9qwocNKbWhGxYpndInQce-6o-toDT8w-AsyH8mug1dwM1ORHyuINg0zv0VaN7whCE_Mx-11QwpZ0KJ2GNzcfNv3_skne-xAobTaO0-htrWOOI4dopf8IvxqNWxJnkhZERqaGPhz8bKkDjMoJZ_YS5zxVaqD75qgNDZcIGiSxaBiwGPvrGmheg7VeOoNwCJeynpRS58OiF1OnZ9LOp7G_dTaDIypO2AADmuMdmXrndJtcw4_M-2nSGIUC5pfUlxTvJAq7zL8XOjPkySA4LmPQml9AJA7Iyikkf_BqgAVrP6oE112wqwr2xqKVPmql_HkIZxYtTI-_hdLvoy62-Rb2GHvdLjwc2wKRVayvoTG1Gfc6v40zqJ60BCzCUiPbKOnC2ox7aES2LJvKV8bpo1h9yTaea2WeL4R5d7zrrS14wbs3nAh1U3ys0CTTVfP2-prJM9Gn37YL1Xk6qb1oH8s7uxN3IsYoS01jQV8T8p0BkqLcSfSXExhfG5Wb6AhU0JD164H3rbC6nAD27tuK8HabPfJBkqR4iopXUgHehWPmrowqgWB8EGDwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروش فوری ویلا جنگلی چلک ( نوشهر )
💰
قیمت ۲۰میلیارد اقساطی
📱
09128402035
📱
09115046100
🏕️
ویلا مدرن لاکچری
🔥
فول هوشمند ، داخل شهرک
🔥
✅
متراژ زمین ۵۵۰متر
✅
متراژ بنا ۶۵۰متر تریبلکس
✅
۵ خوابه (مستر)
✅
شهرک با گیت نگهبانی
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
💰
قیمت ۲۰ميليارد اقساطی
⭐
اقساط بدون بهره
⭐
- تماس جهت بازدید :
🆔
شناسه:
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/652649" target="_blank">📅 15:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2c60a4a7.mp4?token=Fu8KdMSf1xYcBBf8aySdGICRw1ONG1fHjWBZs1ekNQa1tYXA2xDrvxLkeYg3X9QXinYyFPKEvbYW-tMY8pmPPZBLDSQ4kBtBIm95dQ_I5hM3-CTgDPiEW6MjJblufEBLfHCHDfTzG51vOappycW0GAUMYlNi7L3WpF_zqSDWxgxRUzuCTVpZ1hmbN9xH95DuW8g51iZhCjdvmj4vhGtFbF6ASvKIXVMKg0dHUt61Ly3N-IZeVazv7qhxKoQ82gC-9aI7rhVLr6LaUvCAltp3L1__XxrxW57U_pHTdMVD-lxf6e01iOcB_bylsEGE8dSeFUX_e64V2GcUS64AU_CN4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2c60a4a7.mp4?token=Fu8KdMSf1xYcBBf8aySdGICRw1ONG1fHjWBZs1ekNQa1tYXA2xDrvxLkeYg3X9QXinYyFPKEvbYW-tMY8pmPPZBLDSQ4kBtBIm95dQ_I5hM3-CTgDPiEW6MjJblufEBLfHCHDfTzG51vOappycW0GAUMYlNi7L3WpF_zqSDWxgxRUzuCTVpZ1hmbN9xH95DuW8g51iZhCjdvmj4vhGtFbF6ASvKIXVMKg0dHUt61Ly3N-IZeVazv7qhxKoQ82gC-9aI7rhVLr6LaUvCAltp3L1__XxrxW57U_pHTdMVD-lxf6e01iOcB_bylsEGE8dSeFUX_e64V2GcUS64AU_CN4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید مجلس شورای اسلامی به نظارت بر قیمت‌ها و جلوگیری از گرانی‌ها در دومین جلسه بر خط مجلس شورای اسلامی
🔹
آقای حاجی بابایی نایب رئیس مجلس در نطق پیش از دستور خود کاهش فشارهای اقتصادی مردم و نیز ایستادگی در برابر زیادی خواهی های آمریکا را از مهم‌ترین اولویت‌های کشور عنوان کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/652648" target="_blank">📅 14:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652647">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
متیو هو، دیپلمات سابق آمریکایی: اگر آمریکا جنگ دیگری را با ایران آغاز کند، بعد از آن دوباره مجبور می‌شود جنگ را متوقف کند چون ذخایر تسلیحاتی‌اش تمام می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/652647" target="_blank">📅 14:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d33189aaa.mp4?token=vzLl758i-j8hrdeC3DgbdCzuNHkPE-wxiLNA9WeigN5t3mVvI3mi3iWdqs7-hVRarmAy1-2cjqHBSziqM9Ildu0hR-TYWpol3wBbWLCyuZTjnaZqrA6fopfm2SFBt3do10Rd_GLefhEyZ9BrXsi1LTy6VtQ_KB2R1QwSaDIbKp0atKpUGxBwCbRt_6ucy8SeLC-yQ5ib9MWc6CqbP1Jt6Br-8m63fIiP0vfHaGc4XFguDvTQahvGBDInLPoNCgkxP-JyObQJrXXvc1k0wVccp-yW3KlDppQ0v8haQBEgoyZVuxJ-2Vp1bjbokFdmVvDB0LW8Wvs0uTBZlXlVymrL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d33189aaa.mp4?token=vzLl758i-j8hrdeC3DgbdCzuNHkPE-wxiLNA9WeigN5t3mVvI3mi3iWdqs7-hVRarmAy1-2cjqHBSziqM9Ildu0hR-TYWpol3wBbWLCyuZTjnaZqrA6fopfm2SFBt3do10Rd_GLefhEyZ9BrXsi1LTy6VtQ_KB2R1QwSaDIbKp0atKpUGxBwCbRt_6ucy8SeLC-yQ5ib9MWc6CqbP1Jt6Br-8m63fIiP0vfHaGc4XFguDvTQahvGBDInLPoNCgkxP-JyObQJrXXvc1k0wVccp-yW3KlDppQ0v8haQBEgoyZVuxJ-2Vp1bjbokFdmVvDB0LW8Wvs0uTBZlXlVymrL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: باید در کالاهای اساسی به‌ویژه گندم خودکفا باشیم
🔹
این راهبرد الان برنامۀ قطعی سالانه دولت شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/652646" target="_blank">📅 14:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652644">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldFhYfoLuvDfAeFG-6JOv-aOmdlkYO8OluKjyXImEi7tuBrGeEEqnPtXJq3E1uZ2eLuY2_yrRkS-kDRT5TpDPIyLt1zp65y1F61XYJS_c0eGttPKWFMRgixtpjj4A0iulW1EK0QPDRRdB5t9d34CAOCVRRODFo9pvWDsDIG2BztC0QB7aJ3v2tZ87IeoHFbMBxyxVJra477wLYTmnITtJ4rR2nuEV-0tOJXgrnbuSuyQd3U3vG7wgGRG52SkIZ4HPJJBSCLB9Qp6Vw1TcGH_m2Iy5cenB_hN7QAe9n14bkkhjIHjJwQY3WHqpbRybHe21iK2zhRO3mcGInxenD897Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTL8-1izfuveLSUGTQlwHdTt6RKQZD62UI-UPR3LwBEBRRfGFEwjLMggQGFz4Eeri2J2is-WZ-HVpKxxDDnaArTI_VWyAOhRFd_WuGp6n5ql7lrQPGI7UBfNwWL1azprOTVF2zd0F0LNFhiyE6kaIgz_AMN2vbIMr4Z3Aft5eVEz8lCE2XdNNmDPxzQhITYhBwEazZe_WGBgAULj9XSp9_H4u9WNK6pCxo1qrG86PxKK-iMFlJHVE6qVgtDg6kaovP_3q8HeL4sTez6uM3EU3A9h4dUCuQmEakyTDvsWNp778hCZZSKVW1Mp2SwfiuxrjM5OrNMpZqADn3Zq5Ip0Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عاملان شهادت یک پلیس در ملارد دستگیر شدند
🔹
فرمانده انتظامی ملارد: ۲ نفر از سارقان خودرو و منزل که در جریان اغتشاشات دی‌ماه در شهادت سرهنگ دهقان مشارکت داشتند، ‌دستگیر شدند؛ در بازرسی از مخفیگاه آنان ۲ خودرو نیز کشف و توقیف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/652644" target="_blank">📅 14:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652643">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAHa3wwZ7cpk5TI5eiI9vRFDKw4AknnqbDEo9-diOtkRbEIDA4_wD4mPjkoQTC0RJa8ePo4zrPApBBrS_K4rX7asTOix8gjvfmnjDrpZWZNia2lmNJ1zcar5ebgqL6FASIcemU0MmZ0ZDpdR15dqMkryi4kw3Y7IFe7YddfLbsBq6oxQ2GQVvEHYSed5bq3ispCKwU4K97q3CYuY8g5tiFH8QYEy3xuBQ85z9lrLAwEVTzflhpY5kmTPzWvbfA8qcP8KBI1LAi2vLAYzoTDqL3DqLJ695UxLgultga6OIFVKBMX-Pbx5Ke7hURqDcTyRKkuSwj0RLQLQngPibt260w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اتحادیه اروپا: بمباران تاسیسات انرژی ایران، راه‌حل نیست
🔹
مسئول سیاست خارجی اتحادیه اروپا کایا کالاس امروز در نشستی، اوضاع در خاورمیانه را خطرناک توصیف کرد و گفت «همه ما امیدواریم تنش بین آمریکا و ایران کاهش یابد».
🔹
او در اشاره به احتمال ازسرگیری حملات آمریکا و اسرائیل علیه ایران و تهدید متجاوزان به هدف قرار دادن زیرساخت‌های غیرنظامی ایران، گفت که «بمباران تاسیسات انرژی در ایران مشکل را حل نخواهد کرد و برعکس ممکن است مسائل را پیچیده‌تر کند».
🔹
کالاس به افزایش قیمت انرژی ناشی از جنگ‌افروزی آمریکا و اسرائیل علیه ایران و پیامدهای آن هم اشاره کرد، اما مدعی شد که این موضوع، تأثیر قابل‌توجهی بر کشورهای اروپایی نداشته است.
🔹
این مقام اروپایی همچنین دفاع مشروع ایران در جریان جنگ اخیر را تهدید معرفی کرد و مدعی شد که برنامه موشکی ایران برای کشورهای همسایه تهدید محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/652643" target="_blank">📅 14:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652642">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a833cedb09.mp4?token=e7Bf9Av8jOfG9eXwxbkoTl1MwWG8MzAeTDD5pt26Wq-dON4pePSNOr7L1WDbROiNnT9g45KK3w-5qe5Fs7cIRRkLlKnqqEWh3xPDOyPdvvDoSTmJZYxx0Vij2QeNyOFUSiVK8f4P_58ZyR0hZLM80VN4WHguUR2AwiMqrnAhkWqYeDhsggXDfn2hpuWnISeq3kEK6P4YEb3Pd9cah0neJtndlE1aJhQyhKlCLyu72R_LQwpscC-dO1g6yfiLqDRI72uIMNpuhhmhbVg60sXmTiM9s5V3YoAE2UDUaL_-DMsBjIvAVlYNjtsNpQ_8q8oo3bZQnyXRGA-0gVfZ1vVYFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a833cedb09.mp4?token=e7Bf9Av8jOfG9eXwxbkoTl1MwWG8MzAeTDD5pt26Wq-dON4pePSNOr7L1WDbROiNnT9g45KK3w-5qe5Fs7cIRRkLlKnqqEWh3xPDOyPdvvDoSTmJZYxx0Vij2QeNyOFUSiVK8f4P_58ZyR0hZLM80VN4WHguUR2AwiMqrnAhkWqYeDhsggXDfn2hpuWnISeq3kEK6P4YEb3Pd9cah0neJtndlE1aJhQyhKlCLyu72R_LQwpscC-dO1g6yfiLqDRI72uIMNpuhhmhbVg60sXmTiM9s5V3YoAE2UDUaL_-DMsBjIvAVlYNjtsNpQ_8q8oo3bZQnyXRGA-0gVfZ1vVYFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کالابرگ و بیمه بیکاران؛ دستورکار دومین جلسه برخط مجلس
🔹
نمایندگان مجلس در دومین جلسه‌ی صحنْ در سال جدید بر ضرورت مهارگرانی‌ها و افزایش قدرت خرید مردم تاکید کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/652642" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652641">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عارف: راهبرد دولت تأمین پایدار کالاهای اساسی و جلوگیری از گران‌فروشی است
🔹
معاون اول رئیس‌جمهور با تأکید بر ضرورت مقابله با گران‌فروشی، گفت: راهبرد اصلی دولت که در تمام جلسات اقتصادی دنبال می‌شود، تأمین پایدار کالاهای اساسی و جلوگیری از گران‌فروشی است؛ البته بخشی از دلایل گرانی کالاها به مسائل بین‌المللی بازمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/652641" target="_blank">📅 14:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652640">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1273915b99.mp4?token=GwTeSjrh_pzjg7bOZEMT9EBDbPyTZt0v6ORBt3M5vcidagVcg5mse-6DxdVhJ9OkEJpLlM0dRneL1_msKctDJjjyZe4BdKG4J2X2UdPrXewC34s7emx34bHfs8bBluaLwGJiI_4IZIJlVOStqlHZ-BgptHJW8KGTv7C-kDFS6TtWx3gbtz8UtkUdyHpcF43NvzB0shgnp2Hvrua8OuVG3phJc_O_B7zs0cPJX3JQ56BpaMOgYW5ABteZFaJUE7uajkR0d1XieECGfMhBJHjoiEejha70brRXzhQUglDfynGaERaHWs0Z6ylqdlGCrrLzoyu9jR7fPPbIJIIkNmvSwRdjSvXQPZbaSsYUprKa0k7twDZmKj226DAEOCtKHauksgW84IUhJlmLgThGRIIJuYN9JynP-9f4OVd1e7rPhFUdBX6QnF8JguDyx3q1gtBxLr2Ra4nNsIHcnTfSRsugk0NK2SO7LEU4NS65dCyUAEyQ0idnG-E0CxNOLSn2gEDQ89SPL_YvXTxxk0tq3n44hntLJZH_4AzJrbKz6PMS1NVCy8HwmVo4ZzcykLKiA_pG24OioMLyBKqTd2osJ95k9LKDPnc-ELtZSC3juO_dBpjk1XkZ8D1xU1TRpvER23_pyddBNLvwAuXihXw__CVFUUtLnN0LQaVqMSqry_BItZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1273915b99.mp4?token=GwTeSjrh_pzjg7bOZEMT9EBDbPyTZt0v6ORBt3M5vcidagVcg5mse-6DxdVhJ9OkEJpLlM0dRneL1_msKctDJjjyZe4BdKG4J2X2UdPrXewC34s7emx34bHfs8bBluaLwGJiI_4IZIJlVOStqlHZ-BgptHJW8KGTv7C-kDFS6TtWx3gbtz8UtkUdyHpcF43NvzB0shgnp2Hvrua8OuVG3phJc_O_B7zs0cPJX3JQ56BpaMOgYW5ABteZFaJUE7uajkR0d1XieECGfMhBJHjoiEejha70brRXzhQUglDfynGaERaHWs0Z6ylqdlGCrrLzoyu9jR7fPPbIJIIkNmvSwRdjSvXQPZbaSsYUprKa0k7twDZmKj226DAEOCtKHauksgW84IUhJlmLgThGRIIJuYN9JynP-9f4OVd1e7rPhFUdBX6QnF8JguDyx3q1gtBxLr2Ra4nNsIHcnTfSRsugk0NK2SO7LEU4NS65dCyUAEyQ0idnG-E0CxNOLSn2gEDQ89SPL_YvXTxxk0tq3n44hntLJZH_4AzJrbKz6PMS1NVCy8HwmVo4ZzcykLKiA_pG24OioMLyBKqTd2osJ95k9LKDPnc-ELtZSC3juO_dBpjk1XkZ8D1xU1TRpvER23_pyddBNLvwAuXihXw__CVFUUtLnN0LQaVqMSqry_BItZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس کونز، سناتور آمریکایی: ایران همچنان تعداد زیادی پهپاد مرگبار در اختیار دارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/652640" target="_blank">📅 14:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652639">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
امارات اعلام کرد: آتش‌سوزی ناشی از حمله پهپادی به یک ژنراتور برق در نزدیکی تاسیسات هسته‌ای براکه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652639" target="_blank">📅 13:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652638">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وقوع چند انفجار در ابوظبی
🔹
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652638" target="_blank">📅 13:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8891bbc2f6.mp4?token=XwMYwS-k4C5DE5CcR4I6rGQteY3FesW93OaIdJ-nRVdlDkp0WTGdg4GeF1-9KS2irndXNW4uBW9E-_weCqIEps7a9KC0Da_JPUGakWiu8vrhwcI6JYVLg45ae7x9jWK6gUONFxQKlE2FmWEH2PB__jVIO1nb34NrIvJhG2_wLZgKZBJVkOJWO6JoVC4BPUfI320L4F-mkeqawfPpLuiu8uUcQLsP7AZzUgii0XjeIqMAgDTxwEzkE_ZMK7dVnnZOWdb1CCRAjQSoJ00qjmmTy5rR_abLTHG3yVwkNZymM7Gh94CUqZXrFtLd9zjo82ebGWdI5mghfm9rXMcgobw3djzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8891bbc2f6.mp4?token=XwMYwS-k4C5DE5CcR4I6rGQteY3FesW93OaIdJ-nRVdlDkp0WTGdg4GeF1-9KS2irndXNW4uBW9E-_weCqIEps7a9KC0Da_JPUGakWiu8vrhwcI6JYVLg45ae7x9jWK6gUONFxQKlE2FmWEH2PB__jVIO1nb34NrIvJhG2_wLZgKZBJVkOJWO6JoVC4BPUfI320L4F-mkeqawfPpLuiu8uUcQLsP7AZzUgii0XjeIqMAgDTxwEzkE_ZMK7dVnnZOWdb1CCRAjQSoJ00qjmmTy5rR_abLTHG3yVwkNZymM7Gh94CUqZXrFtLd9zjo82ebGWdI5mghfm9rXMcgobw3djzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: اگر دشمن به نفت ما حمله کند کاری می‌کنیم دیگر هیچ کشور دنیا به نفت این منطقه دسترسی نداشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652636" target="_blank">📅 13:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تغییر ساعت رسمی متناسب با فصول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/akhbarefori/652635" target="_blank">📅 13:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652634">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMMEq9iAen0K7Vxin429kl8tVDvrna5LJ5e0Xotp_Gix_WBEJrWljknHmCS85mq0WyQ9VVkQuOPh1FUn62dmse4h9QtgvNLkLWJp9geDRp7LiITk67puVxcnGjBSHoIGKNCZ-H1y8gncpDuUsFF2RDVrSmjpzxXfR45hh9VNBoPsu6AyoWKCFJO7i-o7NPt352xpEpOiaF_je-LDKLGPxk374RRfZHDnFHCoGPFj6h9N0n85P80ibpOZnW-IJG1VGxkRex2rHX_YElkk0G5hdVyEyaoR6b9M5k7blD9_2I3Y0tNHU9h2HTyxSbi3SFe5f5nksOTeXODT3wyrU0AWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیاتی از جلسۀ غیرعلنی مجلس با موضوع کالابرگ
🔹
نادری، نماینده مجلس: جلسۀ غیرعلنی با حضور بیش از  ۲۰۰ نماینده به‌صورت مجازی برگزار شد.
🔹
محور جلسه کالابرگ و بیمه بود. آمارهای ارائه شده از سوی وزیر رفاه قانع‌کننده نبود.
🔹
وعده‌های مکرر میدری و دولت برای افزایش رقم کالابرگ هم محقق نشده که مورد انتقاد نمایندگان است.
🔹
وزیر رفاه، وزیر کم‌کاری است. تعدیل کارگران در وزراتخانه‌ها مورد انتقاد نمایندگان بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/652634" target="_blank">📅 13:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652633">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تخصیص ۳۹ همت اعتبار برای مقابله با تنش آبی در ۱۰ استان کشور
🔹
مدیرعامل شرکت آبفا با بیان اینکه هم اکنون ۱۰ استان کشور با تنش آبی مواجه هستند، بر ضرورت مشارکت شهروندان در مدیریت مصرف آب تاکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/652633" target="_blank">📅 13:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652632">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7m5jikm5RSYZ-Gdl3OlSddk-bgWWuNloxvmKxpnJFa1z_ST0v-uJouAWfaEQ2WfW-yEBYPfOhjSXwF8PitQ9x7L2H5eW8udfNuDnmScx1fyuXeukCx921bY7-riQDuAOOwA8CdKS30Fpzx6j3NCwysKo07jkLmtopWzU7f8-SlwaVyqbwz2ezfiqmgaskg2RyJiNPDFQrtydVAelwIrkvajbRPCuKznTg_J_-tBSV4tkwOzs8WncM4ZhsfTa44l99RHupVu9rKVj03_ONVIoFDRXO_BB_3IUTDLhyjGLCNFYsn0fP7liejbdlzmnv8mzbhSsJR4aBCnPjH-Gb1vWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتبار مرحله نخست طرح «یسنا» برای خانوارهای دارای کودکان چندقلوی زیر دو سال واریز شد
🔹
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی: اعتبار یسنا برای خرید رایگان سبد غذایی و پوشک کودک در قالب کالابرگ الکترونیکی اختصاص یافته است
🔹
بیش از ۵۶ هزار کودک چندقلوی زیر دو سال در این مرحله مشمول دریافت حمایت شده‌اند
🔹
خانوارهای دارای فرزند دو قلو و بیشتر می‌توانند تا سقف ۱۵ میلیون ریال از این اعتبار استفاده کنند
🔹
سبد حمایتی شامل اقلام غذایی مورد تأیید وزارت بهداشت و پوشک رایگان است
🔹
خرید اقلام از طریق فروشگاه‌های طرف قرارداد طرح کالابرگ الکترونیکی در سراسر کشور انجام می‌شود
🔹
مهلت استفاده از اعتبار این طرح تا پایان خردادماه سال جاری اعلام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/akhbarefori/652632" target="_blank">📅 13:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652631">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa048e618.mp4?token=Q0ASw0rmY7dE35B_wh4l6B_Wr36QDBvJeP0c3AJWq8vq5DByRFbp1tJHA2bfC58QXXXwxRW50eGfIScL_sQEMXNK34hkmtDz7N30hf49JeTQrRcd8vgFk8_lbq_zwWnpa-ZW1gLEbjWugqhFX2CtRw1G21SXkMwR-Gb5iPjmdWTLL9vHRQqpkmDcZqoFJ77eM6JOuDe-MDBvEBmP8XHZs3K1s_XlHv6f3t7R3lYtbAwu-UL0-P6LM9a_GmHKNfopLdxqcQCbIT96NfljRsNUosLzfq4JQNzRL0uYIo-rAJ6dqjqm3rDaj6qXE_TRILm6zY7ZwM9PfPN1EpOGnqd5-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa048e618.mp4?token=Q0ASw0rmY7dE35B_wh4l6B_Wr36QDBvJeP0c3AJWq8vq5DByRFbp1tJHA2bfC58QXXXwxRW50eGfIScL_sQEMXNK34hkmtDz7N30hf49JeTQrRcd8vgFk8_lbq_zwWnpa-ZW1gLEbjWugqhFX2CtRw1G21SXkMwR-Gb5iPjmdWTLL9vHRQqpkmDcZqoFJ77eM6JOuDe-MDBvEBmP8XHZs3K1s_XlHv6f3t7R3lYtbAwu-UL0-P6LM9a_GmHKNfopLdxqcQCbIT96NfljRsNUosLzfq4JQNzRL0uYIo-rAJ6dqjqm3rDaj6qXE_TRILm6zY7ZwM9PfPN1EpOGnqd5-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: تنگه هرمز برای ما از بمب اتم هم مهم‌تر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/652631" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652630">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5hffVB532H3DBfuodztkiFDJhT5wzV4L_dsTVoxTX9hFQwFVmA1LIPrC_PVn-mZ1YMy-VygnOW73Qaw0874kOvnC8DIhSBrLgf_uvOqtWOgT4PsMC2fBL32Ql9XqBIvkC4QlPj-J12KpBTsGXhaOJ3Utp6-gjZf0K_j8-LlJGdG-AmgAnfbo43cDcFX3fMyzdCZGUOBn7xE1oczIP5PoXyoEblfn-RBmMOhSIzJkrKuPnuH0-RJmc6wFta-2S5pXhXBUPMEAmkh-Z_lDOQbgiaOFOnKmHAAlqm3IUPQBdzaTGuIU_56frBgMEziZy35x3HW1c0XTlYb-AupsOMhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیوان لاهه برای ۵ مقام اسرائیلی دیگر حکم بازداشت صادر کرد
🔹
روزنامه اسرائیلی هاآرتص امروز گزارش داد که دیوان کیفری بین‌المللی (ICC) حکم بازداشت مخفیانه‌ علیه پنج مقام اسرائیلی شامل سه سیاستمدار و دو پرسنل نظامی، صادر کرده است.
🔹
هنوز دادگاه لاهه به این گزارش واکنشی نشان نداده و در صورت تأیید، تعداد مقام‌های اسرائیلی که از سوی دیوان کیفری بین‌المللی با دستگیری مواجه هستند، به هفت نفر می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/652630" target="_blank">📅 13:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa941b0615.mp4?token=ZGz8y6uker8jT9wRYkeBeuqkzkgQPVU0513B_y5hev4t0utZCvC4BAkVN0-6R-oOyvDbQc5HBC4YcEjJxSMEq6MruN5JMuB2nPz-EYHj7DKL8ADqu5evaw5qiYhux7-DmJask3p0ejJVJiygZVA9X86IC1mZQcSlL9Y6b3gIRyJsdy9-A0rMPX5-P_1Ove7KyZBerbybY3F6lNc7PiyDdOk48LJr4HdsObTKUXaOUqRsLyEO9biLuO7BeCo0t6TCSykhhi3Hg6Dxpcy2ShASGmCgi-CJvcyVXhY89ZUV6dKCGV6sLeaYQZ5JwXKHyXq5Ne8vF9D3jp4Vi6BHQF5j7qX6GDmsQ41C7BdxhxyNg3HzHXYqcbTSWD-tXarLIscTFf-6b7UzN7DgNGC4D9g-W9qm0YOPQS-s7tfmzWrorEm8JBEZvA8bzeV4mzdLUoPDUzhvJCoUGbBv5C_ztEzTecoJwcfGulhh9vyk7Rlg0ajP-6mO4cCBgvvAvlMer-hmliSIzXWggOdsXlyMSimMq_QtBb7ZMoku24MaXhAf1XSJzysaS8MQXw-9s3tUV5WB0jIhAWvGcAKmTCP5uBkwsb1iNWyeFCHMrPvSIA6-0GHoBaDx4mr4SSzmgiPTNMRZ8cCnJBwn6xiROiXDVR5AVYKk-Q_tARzDgSCVlcYmtnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa941b0615.mp4?token=ZGz8y6uker8jT9wRYkeBeuqkzkgQPVU0513B_y5hev4t0utZCvC4BAkVN0-6R-oOyvDbQc5HBC4YcEjJxSMEq6MruN5JMuB2nPz-EYHj7DKL8ADqu5evaw5qiYhux7-DmJask3p0ejJVJiygZVA9X86IC1mZQcSlL9Y6b3gIRyJsdy9-A0rMPX5-P_1Ove7KyZBerbybY3F6lNc7PiyDdOk48LJr4HdsObTKUXaOUqRsLyEO9biLuO7BeCo0t6TCSykhhi3Hg6Dxpcy2ShASGmCgi-CJvcyVXhY89ZUV6dKCGV6sLeaYQZ5JwXKHyXq5Ne8vF9D3jp4Vi6BHQF5j7qX6GDmsQ41C7BdxhxyNg3HzHXYqcbTSWD-tXarLIscTFf-6b7UzN7DgNGC4D9g-W9qm0YOPQS-s7tfmzWrorEm8JBEZvA8bzeV4mzdLUoPDUzhvJCoUGbBv5C_ztEzTecoJwcfGulhh9vyk7Rlg0ajP-6mO4cCBgvvAvlMer-hmliSIzXWggOdsXlyMSimMq_QtBb7ZMoku24MaXhAf1XSJzysaS8MQXw-9s3tUV5WB0jIhAWvGcAKmTCP5uBkwsb1iNWyeFCHMrPvSIA6-0GHoBaDx4mr4SSzmgiPTNMRZ8cCnJBwn6xiROiXDVR5AVYKk-Q_tARzDgSCVlcYmtnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بابایی، نائب رئیس مجلس: اگر به تاسیسات نفتی ایران حمله شود به تمام تاسیسات نفتی کشورهای دوست و دشمن در منطقه حمله می کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/652628" target="_blank">📅 12:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610d8b6046.mp4?token=YwRh83OoRBhuit0tzO5xPDa82AVJrUrabtFliGG3xwB3zdSIu5l2hL7gwrzeYiSyE0ukGFeQzVFSEl22efgY82RQ31mIawFcVHZwSbH2ni86uUwy_SZ7sQLngUhrtlYhgw-Rs8ylEkAJG7POZNBgohCjLBS14L6HrEwY0zGnhalPGwNGlmgQFSVRMqQB7yVlW-qxsiNi6mFlKeINh-zT-te_Y0p2d548VSFL1xEKL3gI29AaZio_jFp1TpwFhbA0v2rod9Udb27pbNByeybc9GWPUgwMiN7lAhqgINGr2Y3vwBwztMD28Yim6NFJfrP0KBbMytNVhIh0CvbnVthoozYbt1tDUeLTHboHPSqQFlTAK4X8Vbg3U7DVhTKsLPaXy5tUusbiHlzQRk2rspgZhW-Wtew1zyU79fOeUTN6bnDSUb-oc1lpfrIzz-CRMhKcSOUiwxf4O6nwoWKzo261RdWqFHVCLh9wmyzoCkEf9RPviAJlCJKis9yM3EszulsQxnbphk1DDWr50PQOQoYHtV4cH7qT53jCBz-Tkv6Tf2JtWbga7UKgbpEnCK6g0FGhi8t5bd2kAl7t82bHrKuTTps-CgH2cR9obsvCfQzcp6BRnJYmOn2Y-m55xKcb5Epll_KEk5sfJAgFjlB13bwg5HYpRf3FUdKefnvSiVvPtKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610d8b6046.mp4?token=YwRh83OoRBhuit0tzO5xPDa82AVJrUrabtFliGG3xwB3zdSIu5l2hL7gwrzeYiSyE0ukGFeQzVFSEl22efgY82RQ31mIawFcVHZwSbH2ni86uUwy_SZ7sQLngUhrtlYhgw-Rs8ylEkAJG7POZNBgohCjLBS14L6HrEwY0zGnhalPGwNGlmgQFSVRMqQB7yVlW-qxsiNi6mFlKeINh-zT-te_Y0p2d548VSFL1xEKL3gI29AaZio_jFp1TpwFhbA0v2rod9Udb27pbNByeybc9GWPUgwMiN7lAhqgINGr2Y3vwBwztMD28Yim6NFJfrP0KBbMytNVhIh0CvbnVthoozYbt1tDUeLTHboHPSqQFlTAK4X8Vbg3U7DVhTKsLPaXy5tUusbiHlzQRk2rspgZhW-Wtew1zyU79fOeUTN6bnDSUb-oc1lpfrIzz-CRMhKcSOUiwxf4O6nwoWKzo261RdWqFHVCLh9wmyzoCkEf9RPviAJlCJKis9yM3EszulsQxnbphk1DDWr50PQOQoYHtV4cH7qT53jCBz-Tkv6Tf2JtWbga7UKgbpEnCK6g0FGhi8t5bd2kAl7t82bHrKuTTps-CgH2cR9obsvCfQzcp6BRnJYmOn2Y-m55xKcb5Epll_KEk5sfJAgFjlB13bwg5HYpRf3FUdKefnvSiVvPtKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس مورفی، سناتور آمریکایی: تنگه هرمز قبل از شروع جنگ باز بود، حالا داریم سعی می‌کنیم مشکلی را حل کنیم که خودمون به وجود آوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/652627" target="_blank">📅 12:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36779bca6.mp4?token=mqGWQGzUMh15_BZqpO5VP81_HTg9AuQdoQyZ9xoC7_t8edPmjIgfeeoadwbVuHZLWz7e386qY9H9MW1t35pDwudkmn5r_BlLp_aTF-UltK9FItovc05qyXTj7UPoMVb6sXq_FHFki46ZKSQlaZX1HLho5MOxi1w4J2kFe45VB5ed3sio525tq0Bo7QH8rYbj571AesRYgIBOTNkL8z6-1-bHuR1juCzU2inyVBbnlW-OmlPs7_VVae2xJoYCOt8YKzXQKSQzaKLxwjCc6k7ApqPGbg2FMSAKx_cz6mmFIpz6vHgMyKQoeNHBBTuqh7GS1Dhw2RJ-Mgu9z4ud5t7ZZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36779bca6.mp4?token=mqGWQGzUMh15_BZqpO5VP81_HTg9AuQdoQyZ9xoC7_t8edPmjIgfeeoadwbVuHZLWz7e386qY9H9MW1t35pDwudkmn5r_BlLp_aTF-UltK9FItovc05qyXTj7UPoMVb6sXq_FHFki46ZKSQlaZX1HLho5MOxi1w4J2kFe45VB5ed3sio525tq0Bo7QH8rYbj571AesRYgIBOTNkL8z6-1-bHuR1juCzU2inyVBbnlW-OmlPs7_VVae2xJoYCOt8YKzXQKSQzaKLxwjCc6k7ApqPGbg2FMSAKx_cz6mmFIpz6vHgMyKQoeNHBBTuqh7GS1Dhw2RJ-Mgu9z4ud5t7ZZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بابایی، نائب رئیس مجلس: اگر دشمن به نفت ما حمله کند کاری می‌کنیم دیگر هیچ کشور دنیا به نفت این منطقه دسترسی نداشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/652626" target="_blank">📅 12:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
وداع جانسوز همسر شهید مهدی سعادتی با فرزند شهیدش محمدحسین سعادتی
🔹
شهید سرهنگ دوم مهدی سعادتی، شهید محمدحسین سعادتی، شهیده زهرا قاسمی، شهیده آذر لطفی و شهیده مهیار محمدی در حمله هوایی دشمنان آمریکایی صهیونیستی به منطقه مسکونی در محله محسن‌آباد خمین به درجه رفیع شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/652625" target="_blank">📅 12:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تجاوز رژیم صهیونیستی به خاک سوریه
🔹
منابع محلی سوریه خبر دادند که یک گشتی رژیم اشغالگر صهیونیستی وارد جاده «الاصبح مزرعه الفتیان» در استان قنیطره شد.
🔹
منابع مذکور افزودند که اشغاگران مانع دسترسی دامداران محلی به زمین‌های خود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/652624" target="_blank">📅 12:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q68HOBa4iHHouSaBfKtp4l2YLFMy0xKAqztGVIGCtRTzy96HXb_lx7FDipWBPQix6c3q2NnOzkqwb8DIIfHLFJnjwkDnOFrXOpopzqVU05XSUzhgP4SDglc33T1ME8iYYStqNIcMbpNksxyfdHnbul6XLmHScl3EzJwNbR65SfW9F9IDUOO2_x7mxRcmBDgN1yKgmCdrdqa1bci73DkNqgrz5y3yoHQ57hAkqp6_U4Pq7IiJXNrairMuej4KUuv6M6J37zQ07xXhqZnQHZllsPkAMaYINKSzAEZyIJiDY5nky4SnqKgJsmp9eUlRCAQOLvHmdiyzlrejbqf6kjoTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: سرنوشت ملت فلسطین به دست فلسطینیان رقم خواهد خورد
🔹
رئیس مجلس در پی شهادت فرمانده گردان عزالدین قسام: در زمانی که با وعده‌های دروغین، آتش‌بس در غزه حاکم بود، «عزالدین الحداد»  فرمانده گردان عزالدین قسام با همسر و دخترش به شهادت رسید.
🔹
وعده الهی غیرقابل تغییر است.
🔹
با ادامه خط مقاومت سرنوشت ملت و سرزمین فلسطین به دست فلسطینیان رقم خواهد خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/652623" target="_blank">📅 12:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تکرار حماقت آمریکایی‌ها، پیامدی جز دریافت ضربات کوبنده‌تر درپی ندارد
🔹
«سردار شکارچی»سخنگوی ارشد نیروهای مسلح: تکرار هرگونه حماقت برای جبران بی‌آبرویی آمریکا در جنگ تحمیلی سوم علیه ایران، پیامدی جز دریافت ضربات کوبنده‌تر و شدیدتر برای آن کشور به‌دنبال نخواهد داشت.
🔹
رئیس‌جمهور مستأصل آمریکا باید بداند در صورت عملی شدن تهدیدها و تجاوز مجدد به ایران اسلامی، دارایی‌ها و ارتش مضمحل آن کشور با سناریوهای جدید، هجومی، غافلگیرکننده و طوفانی روبه‌رو خواهند شد و در باتلاق خودساخته‌ای که نتیجه سیاست‌های ماجراجویانه همان رئیس‌جمهور است، فرو خواهند رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/652622" target="_blank">📅 12:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5z1Q8FRTw8eQhqyTDxmdDCYc3TzkPYZ-KujqVs02XkUxnZDEtwKkN-bQBSRtn2EFsf4j4xaJuxDiPpt8sd4NyQ6d-fY0Yjh_1_tBKE9sXDh9a2oBsfVoscNivvx32_t2BLtOLxzTu38cDrCq49WOxRcTMB1vci69fNSGXn8dV_OFkx69cSh6XDVRpS33CopV8bKJ5jucr42DGvUOFXGl116rVqjzcTI8X0K5v3evfRjahw_LQJah8up3IgC9CDAM49D5Vs96MRIjS9l_xW1II7aidcLuigHUcPra9FtynJON7vUWlkSZG1lLL8pz63dSTFWtym1uYKv6dZBruH7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارشگر ویژه سازمان ملل نسبت به شکنجه گسترده فلسطینیان هشدار داد
🔹
فرانچسکا آلبانزه هشدار داد رژیم اسرائیل از شکنجه علیه بازداشت‌شدگان فلسطینی در زندان‌ها استفاده می‌کند و در سطحی وسیع‌تر کل جمعیت فلسطینی در سرزمین‌های اشغالی را از طریق محاصره، جابه‌جایی اجباری و محدودیت کمک‌های انسانی تحت شکنجه قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/akhbarefori/652621" target="_blank">📅 12:16 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
