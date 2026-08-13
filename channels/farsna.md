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
<img src="https://cdn4.telesco.pe/file/fz8SIakvDtTlD21BhKiZwZ2DhdMOYIcnwH0qbxhmMTIiC8H0bOBLNuZas7Fq926DEt6wEnarDE1_tBUXeqoCpaXwjT0pDbS6eNoVhUz_wD5ozPOzhFYhjdLPJ2nW8OXF-fjDcQs0_E2nsHzSBpsufL-Z4Dew-9BshYKRoej0YAyCFT-UlKzp8EVBjsYeDRML3PF2huEZ76m18hyWMXlKkF7iybvn1HdC-eRZPqJyFMZppYBeKYDultYbEBccrtcDItgpvjgrulR7DahQHItVHFbMGwKuF4iXNAk6vOZXTSIv8nSsxNrymlIrgxrDb2qnIoHjm6W_5Siyb1MZ8-tGxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 00:02:12</div>
<hr>

<div class="tg-post" id="msg-455949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KByeIsohPwF374Ax5LnVa8pTui2JdxZzgf-8iim2qGfN0bzx7Hj16H3WsNSgTYmFpfxL270UbQpaGk_6HzaGletVXBxa0PN7B-Y7YvCPYj7-0BzBhLhwT6GNviAT9xrf_1uvKkl2laU3sva9CzFMcIOAVslsYUHCB9rJ9kqTYepHou-bYTSUndi9Nzu7eEDXuWnuT-UpaXd_ET-3FdOvINSPB3pzaGapvWy-iJcbag-0NeItQQwHj27MMr9kt2_f6Ai3wupOrLx19yWn0i4NBmcHyGdVqR-ADD2SicuK2GwcfuCd8ZqQKMDLA3I2UV8AmAztHV0bdnytYBIy7P22VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌فشانی در تاریکی
🔹
در سال سیزدهم بعثت، سران قریش که از گسترش اسلام در یثرب (مدینه) به تنگ آمده بودند، در «دارالندوه» گرد هم آمدند. طرح آنان، نقشه‌ای شوم و حساب‌شده بود: از هر قبیله جوانی انتخاب شود تا همگی دسته‌جمعی به خانه پیامبر(ص) هجوم ببرند و او را در خواب بکشند. با این کار، خون پیامبر میان تمام قبایل تقسیم می‌شد و خاندان بنی‌هاشم توان جنگ با همه قبایل را نداشتند و مجبور به پذیرش دیه می‌شدند.
🔹
چون وحی بر پیامبر نازل شد و او را از این توطئه آگاه ساخت، فرمان هجرت به یثرب صادر شد. اما خروج پیامبر از خانه، نیازمند پوششی بود تا ردپای خروجش پنهان بماند.
🔹
پیامبر راز را با علی(ع) در میان گذاشت و از او خواست تا آن شب در بسترش بخوابد و روانداز سبزِ او را بر سر بکشد. علی(ع) بی‌تردید و تنها با یک پرسش گفت: «ای رسول خدا، اگر من آنجا بخوابم، جان شما سالم می‌ماند؟» و پس از شنیدن پاسخ مثبت، پیشنهاد را با جان و دل پذیرفت.
🔹
با تاریک شدن هوا، کمین‌کنندگان قریش خانه را محاصره کردند. آنان از روزنه‌ها نگاه می‌کردند و کسی را می‌دیدند که با روانداز سبزِ پیامبر خفته است؛ پس آسوده‌خاطر منتظر سپیده‌دم ماندند تا طبق نقشه حمله کنند.
🔹
در این میان، پیامبر(ص) با استفاده از تاریکی شب و غفلت مهاجمان، از خانه خارج شد و به سمت غار ثور حرکت کرد.
🔹
با طلوع سپیده‌دم، مردان قریش با شمشیرهای کشیده به درون خانه یورش بردند. اما وقتی پارچه از روی صورت کسی‌که خوابیده کنار زده شد، به‌جای پیامبر، با علی(ع) مواجه شدند که آرام و بی‌باک برپاست! نقشه قریش نقش بر آب شد و پیامبر فرصت کافی برای دور شدن از مکه را پیدا کرد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 340 · <a href="https://t.me/farsna/455949" target="_blank">📅 00:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f485f9a09f.mp4?token=ItgqkJA9tzzVCScHtOsccA5M8enc-RRV_cx8nt3v5e97CX3PMp37YTYLwWPZHzH1weAJ1NAcsq_EJSyC6huJZxMRhJNLFpYWsReF3BGbMXayqqw85t0hiT1LKX3q7JxFJMLwOpSyvQBvfa1Efdq1N_j5pRJalLJMGU4waMpQX4WSBDzYW8Qa-_LNM42FAI8Yn5wnpQ5Nlon24JOMFEzlWixzGhTXwWzkV98jN_M4t0PUqzOzDXWZjGfVEiLhv-vTrMI01evBAJoOo-d77KEaQqW7YPPrXi29ZbiRd_VMboS-9NUCr4KsutSeqPfjt5GOuPp_0h3FvCjVcPjzuVX3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f485f9a09f.mp4?token=ItgqkJA9tzzVCScHtOsccA5M8enc-RRV_cx8nt3v5e97CX3PMp37YTYLwWPZHzH1weAJ1NAcsq_EJSyC6huJZxMRhJNLFpYWsReF3BGbMXayqqw85t0hiT1LKX3q7JxFJMLwOpSyvQBvfa1Efdq1N_j5pRJalLJMGU4waMpQX4WSBDzYW8Qa-_LNM42FAI8Yn5wnpQ5Nlon24JOMFEzlWixzGhTXwWzkV98jN_M4t0PUqzOzDXWZjGfVEiLhv-vTrMI01evBAJoOo-d77KEaQqW7YPPrXi29ZbiRd_VMboS-9NUCr4KsutSeqPfjt5GOuPp_0h3FvCjVcPjzuVX3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانۀ ۱۶۶ کاشمری‌ها در شام شهادت حضرت رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/455948" target="_blank">📅 23:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: ۲۰ درصدِ ناترازی تولید و مصرف بنزین به‌خاطر ترافیک، خودروهای تک‌سرنشین و یک‌سرخالی‌بودن خودروهای باری است.  @Farsna</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/455947" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1754162d0.mp4?token=Wky3C3o0qvesTqDbIO8ZM0ZnEkF85wiIfZyr-UkEFq6hhTirWoPURljmmPWhNhO8hXi5ggAYczDZYVesNsaJCWOsJbZa4jI3bhDVdSNsZcMEAbR7tWDhvBvclkljS0DBGyPNpimzwfxxcKL6O0aCjfXl9Je2QuoSLStUxOLx7WKWz3hwp2mncqFn64xD0DsXedq4xCbM1vgliiqUKxk9angVo9CaD_vIyIVj5btG5NMXigMXQ2a7JAVSOR_zcYaTKmwDwWMmZHoNw7mM580L3BCgoLfOyAO_JYNsk0iTMfFM7sCIeyTMZUVhtIvqfLK9hcXSKQnI3nE0QReNKZakm4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1754162d0.mp4?token=Wky3C3o0qvesTqDbIO8ZM0ZnEkF85wiIfZyr-UkEFq6hhTirWoPURljmmPWhNhO8hXi5ggAYczDZYVesNsaJCWOsJbZa4jI3bhDVdSNsZcMEAbR7tWDhvBvclkljS0DBGyPNpimzwfxxcKL6O0aCjfXl9Je2QuoSLStUxOLx7WKWz3hwp2mncqFn64xD0DsXedq4xCbM1vgliiqUKxk9angVo9CaD_vIyIVj5btG5NMXigMXQ2a7JAVSOR_zcYaTKmwDwWMmZHoNw7mM580L3BCgoLfOyAO_JYNsk0iTMfFM7sCIeyTMZUVhtIvqfLK9hcXSKQnI3nE0QReNKZakm4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: دلیل ۵۰ درصد شکاف بین تولید و مصرف بنزین، خودروهای داخلی هستند
🔹
شاید در دولت هیچ‌کس مثل من از این خودروها آسیب نخورده است. این خودروها جز مصرف زیاد بنزین، ده‌ها مشکل دیگر دارند. @Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/455946" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa53a50025.mp4?token=XGAMIcIZnYwPjcdxMWRWHg26YSet6RtgYh7wTPlhBD0wRRaYVfHfpPSH42O3SyLw1_McfPHiGcgsEscHHCiSUYPNqKFV-qqBfJaKHPRyvrsty-02oetDMcc7-_tR3ursaSoepxz9h39gVeL1BBmnQUWSbMbmLCpMzr4672gu1XqcmOVX2_acIihFdOD2LllKCIeDY0A1gyC9wrx_3Yz1hkzUUiPlBv8JBtxQxyb-y4UPMSL9zDJLzz3xFd_lKIqjo5NCRyvMPmBBpcT9h4zxWHOhSlLMo2V73qtSjWYgB4yyv8IlNi-Dmxj2UxMZ2zmMsFFr2sjqufr3uigWVHGWng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa53a50025.mp4?token=XGAMIcIZnYwPjcdxMWRWHg26YSet6RtgYh7wTPlhBD0wRRaYVfHfpPSH42O3SyLw1_McfPHiGcgsEscHHCiSUYPNqKFV-qqBfJaKHPRyvrsty-02oetDMcc7-_tR3ursaSoepxz9h39gVeL1BBmnQUWSbMbmLCpMzr4672gu1XqcmOVX2_acIihFdOD2LllKCIeDY0A1gyC9wrx_3Yz1hkzUUiPlBv8JBtxQxyb-y4UPMSL9zDJLzz3xFd_lKIqjo5NCRyvMPmBBpcT9h4zxWHOhSlLMo2V73qtSjWYgB4yyv8IlNi-Dmxj2UxMZ2zmMsFFr2sjqufr3uigWVHGWng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: مصرف بنزین در کشور ما نسبت به دیگر کشورها روزانه ۷۰-۸۰ میلیون لیتر بیشتر است
🔹
مصرف بهینۀ بنزین در ایران باید روزانه ۵۰-۶۰ میلیون لیتر باشد نه ۱۳۵ میلیون لیتر.
🔹
باید کاری کنیم تقاضای مصرف بنزین کنترل شود. @Farsna</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/455945" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3ea8fac05.mp4?token=nZs1Ye6gzyk7fHNx1xXrtX1qEk0vBKBH87QilUbwJVHx85Y0jtvzBJuUfV_5A8e3P05BG8H04lHfEN4HjjZakCoDjyFkIqzxjMhaLArwpzBJks3Ph_-kAXPOBkLRQuPCvjELLLSd8fN-_85MpLIWCJ1xPIxtjOQ6SaWdq709UJE-pXz6wR2jLFYzO83xhYHeEtwOvll79Z7SP3D8Wusuk6VVcgigc64X2PmfHKmCukRO9IOPoKoZWT-P8A9IERstQNzxftedFT-NG0X5RedOtjif50AouoOipS75x4iQPlpoAmGWFkG1oqNX6cMlJRpcuyRLXAprFL0pXsgoxsqBSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3ea8fac05.mp4?token=nZs1Ye6gzyk7fHNx1xXrtX1qEk0vBKBH87QilUbwJVHx85Y0jtvzBJuUfV_5A8e3P05BG8H04lHfEN4HjjZakCoDjyFkIqzxjMhaLArwpzBJks3Ph_-kAXPOBkLRQuPCvjELLLSd8fN-_85MpLIWCJ1xPIxtjOQ6SaWdq709UJE-pXz6wR2jLFYzO83xhYHeEtwOvll79Z7SP3D8Wusuk6VVcgigc64X2PmfHKmCukRO9IOPoKoZWT-P8A9IERstQNzxftedFT-NG0X5RedOtjif50AouoOipS75x4iQPlpoAmGWFkG1oqNX6cMlJRpcuyRLXAprFL0pXsgoxsqBSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا می‌شود شکاف بین تولید و مصرف بنزین را با بالابردن تولید جبران کرد؟
🔹
رئیس سازمان بهینه‌سازی: بالابردن تولید نیاز به سرمایه‌گذاری ۱۳ تا ۳۰ میلیارد دلاری دارد که این رقم وجود ندارد.
🔹
اگر بر فرض این کار هم انجام شود، باید روزانه  ۸۶۰ هزار تا ۱.۴ میلیون…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/455944" target="_blank">📅 23:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-hLyjXhTt5dPP7G3m-eOL6MqihWafawYEIvBzQJK7cT6Kl_FjPx8P846Xp0CJoUT9bFkvCiCMcDzQgzf0hsqAdkWqKVOjVJRQx9tCjz-_XdAX2i9nn9QH37eUncS5S8GMX9z8skQqQaj6rdxAT75sN-OPV5BQSgQvZgLhK8K-AY47EX5hmeY-KCJeG4lF4fBvP5TvC2QokZwp8mKNXZdON0D1jHlaAIs-y-UbP4iCi9oEE23fYT_z8J3CWnLOsotNfkgzXhpsLoEpRz6Yc04hLHnNNznowHUkSWBPy2tT6aEDp_ThbsSw-FYD3zNd5h3-pSidI8f9AjLBO_wsSv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله مروی: وحدت و انسجام، مسیر عزت و استقلال ملت ایران است
🔹
تولیت آستان قدس در مراسم خطبه‌خوانی شهادت امام رضا(ع): وحدت، اتحاد و اعتماد به دست‌اندرکاران کشور، مسیر عزت، عظمت، شکوه و استقلال ملت ایران است.
🔹
ایجاد یأس، بدبینی و شبهه در ذهن مردم، جز خدمت به دشمن هیچ اثری ندارد؛ همان‌گونه که بزک کردن و بی‌خطر نشان دادن دشمن نیز مردود است.
🔹
ملت ایران در برابر سختی‌ها و جنایات دشمن نه‌تنها متزلزل نشدند، بلکه عزم و استقامتش بیشتر شد.
🔹
زائر امام رضا(ع) باید با افزایش معرفت و تبعیت از آموزه‌های حضرت، زیارت را به فرصتی برای اصلاح و تطبیق زندگی خود با سیره امام تبدیل کند.
@Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/455943" target="_blank">📅 23:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b698d3c57e.mp4?token=BdrSZoFCYzvoZlyNjsKi0tHLL4ep8MCajzxULEKpSQvhzuDLXY4n0liJlPefT-FjC1VqOOcFbo7gdFmi5mpG5zxtTvkoBrdqtVyERnOihuRlHqlmOIQhbjo-dCUZuOyp0mGJIlSDM0fBcTb2Pb8ojRK_J57sLuCySIjSywrngrOCngmoglDogf6aVYQOkh6CW2sN-2_XQCD8CHcL-q20bl2ZwrCOSm3bxhDNwJBAscg-_g1kU1UGPdZiyaCZbnG04Zn3iAdhaHaZhPhe81fis8GYjxt2q9PMq_SOopIugeYNDcnxps5CuQL6MoJ1Sq8tt022JdwT3HyXkfF09Prxxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b698d3c57e.mp4?token=BdrSZoFCYzvoZlyNjsKi0tHLL4ep8MCajzxULEKpSQvhzuDLXY4n0liJlPefT-FjC1VqOOcFbo7gdFmi5mpG5zxtTvkoBrdqtVyERnOihuRlHqlmOIQhbjo-dCUZuOyp0mGJIlSDM0fBcTb2Pb8ojRK_J57sLuCySIjSywrngrOCngmoglDogf6aVYQOkh6CW2sN-2_XQCD8CHcL-q20bl2ZwrCOSm3bxhDNwJBAscg-_g1kU1UGPdZiyaCZbnG04Zn3iAdhaHaZhPhe81fis8GYjxt2q9PMq_SOopIugeYNDcnxps5CuQL6MoJ1Sq8tt022JdwT3HyXkfF09Prxxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخشش رعدوبرق در آسمان اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/455942" target="_blank">📅 23:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d076f9c2f.mp4?token=l81tia890HPaubGWmaTCuRR8czpDg9fluVvP_zjJG6NQrrfGmgZxJoB3wouII3JaHid0YZtPkOnBudygcjeyVMx8X8fKbJLjSsZMPx6TtrZjp27vJSoLIsaRhIZz1wBjb01ZoMROTgspKxOCuzCwtdPGHRfFe4XUxurUhKk_r3kaelgONcq9Hqez_Kpl5K1bxmPEBW5DMqZbrLPtFE3hEMfMkOHVMBiPYQcKbzS3YZhFDkTNrgdUNqJYD_QuZUMvNI6FQYA4SHC-GiQjg3NThrpk4kRwH5gkp-ly_ZuaVU213MK8EhITD_J6Qf3KvCiRW-fZH_1ujfAbzrPh8F7K3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d076f9c2f.mp4?token=l81tia890HPaubGWmaTCuRR8czpDg9fluVvP_zjJG6NQrrfGmgZxJoB3wouII3JaHid0YZtPkOnBudygcjeyVMx8X8fKbJLjSsZMPx6TtrZjp27vJSoLIsaRhIZz1wBjb01ZoMROTgspKxOCuzCwtdPGHRfFe4XUxurUhKk_r3kaelgONcq9Hqez_Kpl5K1bxmPEBW5DMqZbrLPtFE3hEMfMkOHVMBiPYQcKbzS3YZhFDkTNrgdUNqJYD_QuZUMvNI6FQYA4SHC-GiQjg3NThrpk4kRwH5gkp-ly_ZuaVU213MK8EhITD_J6Qf3KvCiRW-fZH_1ujfAbzrPh8F7K3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: طبق پیش‌بینی‌ها با روند مصرف فعلی، شکاف بین تولید و مصرف بنزین تا پایان سال ۱۴۰۸ به ۴۳ تا ۷۰ میلیون لیتر خواهد رسید.  @Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/455941" target="_blank">📅 23:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06279d848.mp4?token=O-Yl60YXS9svfe70uSiSWunO6e-_xhIPkplQW-FfKjQm4N3jxkGWyAVz2uXADyZfD1Q_HfGX_eCbwd7R5A4ogh37-2CVe3cGnlQBDPo_-aJphQjaa8PtLrUPdqYyMWyAWv_u7UF05yi4R6vVrhV1sgmBVtgAPb08pCUlI5NoVVDBcg-8RlhSP2F5BYqGcTGc9LniCVyGlnVRFuQ6uZy3fbOSlYXV22Z2Gf5T4-51u23LyDGDMyoUSz4zsda6DB3hpukzrvEYzH2javWg2mHYbRP6LzQ0S-j98KW-NhUyxkSKdPcTRQh0ZbaMQJhWlbVvttzZ_ivN0uVN1QtEb_f4gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06279d848.mp4?token=O-Yl60YXS9svfe70uSiSWunO6e-_xhIPkplQW-FfKjQm4N3jxkGWyAVz2uXADyZfD1Q_HfGX_eCbwd7R5A4ogh37-2CVe3cGnlQBDPo_-aJphQjaa8PtLrUPdqYyMWyAWv_u7UF05yi4R6vVrhV1sgmBVtgAPb08pCUlI5NoVVDBcg-8RlhSP2F5BYqGcTGc9LniCVyGlnVRFuQ6uZy3fbOSlYXV22Z2Gf5T4-51u23LyDGDMyoUSz4zsda6DB3hpukzrvEYzH2javWg2mHYbRP6LzQ0S-j98KW-NhUyxkSKdPcTRQh0ZbaMQJhWlbVvttzZ_ivN0uVN1QtEb_f4gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: طبق برآوردها مصرف روزانۀ بنزین تا پایان سال به ۱۳۹ تا ۱۴۴ میلیون لیتر خواهد رسید اما همچنان عدد تولید روزانه‌مان روی ۱۲۱ میلیون لیتر خواهد ماند.  @Farsna</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/455940" target="_blank">📅 22:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86b8b765b.mp4?token=tCLDuVRCQrBAjyx3YrPLhLCN1QFVePGEqBNTOJrkQLorQPDd1DeTfuQC5Am1CyNRlbcFJGK-sIroKsuooK9G304e1_o1AXDyUAg4PlWqwpe-j-ZLUFVY7hsBhsCoo0X4iwZvCGF9ooJyD94Ee4is9PIdiTMlv03_lCObLLzo5x29pRqMcblns0Eh5O2OeakssbWw9Cu1SNkoL2Qo-mANpmNmE2ayscYzmTGD8bdC_jP8pCOF4TI6gmMnKfbAhJCwTi0KowYBluvO6fc_4MXdELhl_WZOIFuDHdVp--u3g_yBdCMU0EhPf-6cCDhxLFL_N5X9hPkAKMW9UXUfsT69_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86b8b765b.mp4?token=tCLDuVRCQrBAjyx3YrPLhLCN1QFVePGEqBNTOJrkQLorQPDd1DeTfuQC5Am1CyNRlbcFJGK-sIroKsuooK9G304e1_o1AXDyUAg4PlWqwpe-j-ZLUFVY7hsBhsCoo0X4iwZvCGF9ooJyD94Ee4is9PIdiTMlv03_lCObLLzo5x29pRqMcblns0Eh5O2OeakssbWw9Cu1SNkoL2Qo-mANpmNmE2ayscYzmTGD8bdC_jP8pCOF4TI6gmMnKfbAhJCwTi0KowYBluvO6fc_4MXdELhl_WZOIFuDHdVp--u3g_yBdCMU0EhPf-6cCDhxLFL_N5X9hPkAKMW9UXUfsT69_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: مصرف روزانۀ بنزین ۱۳۵ میلیون لیتر است
🔹
تولید داخلی ما ۱۲۱ میلیون لیتر است و میزان واردات تقریبا ۱۴ میلیون لیتر است. یکی از اهداف دولت این است که واردات صفر شود و پول آن به اولویت‌های بالاتر مثل دارو و کالاهای اساسی تخصیص داده شود.…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/455939" target="_blank">📅 22:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92fc6d9a8.mp4?token=bxVz1SJTZTQdVm_khSsH-NgKXQCZcBzdMfEfw4sSfRtG8aKPVvULuUOFMC4ZE7S7KSVyY8yfpA8ndbgmUejRYAVgAcGvN99GxI0iwKybg4HlwOZA8-wiQRWS0olSv-STgRdjQ18PVBQ3lfn0Nfn9YEth7Q0Gf6jw1Ulh4GphkMjrpzp7JY25Hi-K0tjvSt9u91SnjKJQlU4-sLC-zYD7GCr29XwBoix0ELq-iC2SrFDymj446zZgx2R7qPE-x8Sc6L9ijRIZifn_VEgLWFJmvr9Chvn9sT2-3dpcIw82iavgp042r3jgV0G_n-qalS37ronNearf6cBqxgUldwQkM2oDp0YOpwd3tcgttDPiOxUyMej33b_HeLtIAlsiQpZ3fWpR8uhwVMBlZltig7qWduIs5oD8P1ijsipJ9FG7DwVgHiTqIsOea_tFG-x-J0jaWrownLFe-k1HqB3lxeD-0ED5ilPVbz6SR3HUgJRts_bYoKL8Jsb7V8XH1Et9jwCF_fEPT2a-IGvqL0TlDK9iGQY3GiAglLaZFWLC5uYwa_FbPaHlKEAdy9fOFLYomtPQVACDopW5hV8qf5KtvG-jhLUTC7kjaek8i2avwDGSH2pDscD9KqxJpFMOeVqkSFIdp1F_spe-lNjjgWwSKWA9tzDMageKA81S9QbS5McgLVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92fc6d9a8.mp4?token=bxVz1SJTZTQdVm_khSsH-NgKXQCZcBzdMfEfw4sSfRtG8aKPVvULuUOFMC4ZE7S7KSVyY8yfpA8ndbgmUejRYAVgAcGvN99GxI0iwKybg4HlwOZA8-wiQRWS0olSv-STgRdjQ18PVBQ3lfn0Nfn9YEth7Q0Gf6jw1Ulh4GphkMjrpzp7JY25Hi-K0tjvSt9u91SnjKJQlU4-sLC-zYD7GCr29XwBoix0ELq-iC2SrFDymj446zZgx2R7qPE-x8Sc6L9ijRIZifn_VEgLWFJmvr9Chvn9sT2-3dpcIw82iavgp042r3jgV0G_n-qalS37ronNearf6cBqxgUldwQkM2oDp0YOpwd3tcgttDPiOxUyMej33b_HeLtIAlsiQpZ3fWpR8uhwVMBlZltig7qWduIs5oD8P1ijsipJ9FG7DwVgHiTqIsOea_tFG-x-J0jaWrownLFe-k1HqB3lxeD-0ED5ilPVbz6SR3HUgJRts_bYoKL8Jsb7V8XH1Et9jwCF_fEPT2a-IGvqL0TlDK9iGQY3GiAglLaZFWLC5uYwa_FbPaHlKEAdy9fOFLYomtPQVACDopW5hV8qf5KtvG-jhLUTC7kjaek8i2avwDGSH2pDscD9KqxJpFMOeVqkSFIdp1F_spe-lNjjgWwSKWA9tzDMageKA81S9QbS5McgLVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است
🔹
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، چند هفته قبل از اجرا آن را به مردم توضیح می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/455938" target="_blank">📅 22:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np-Ajr6GG9j3OF06X6vSHQhVN5GAGuxrRadQAql9TrTEnsPDTT9qJjxQ9HoHa_cYlJC24EZCLZyKGl3TnEC3JALZhHZ1PVj05Wl58u3_7o2LRe2TdcsStO4IaHrpHQTKr0oS99c9YbnX1CLkWzgqn1pWucPPjXOgaSseHxse2hb4UMqpcZ4EvxDHbhBynb3uDL7dX0phskondUhzaVpeKIv9Q2_DMVU92hFL0vzJk-G5-ZRxYAY0PZp5Yj2l3rtuRjn6i6MsuQSc8zK1t5rG_EYswRvNG02yZkmnPjbooNhZyJeaJVjoXqXsyJ3YPTu0OEMYQEWb28_vnsP17u4Ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهرم راهبردی ایران در خزر که نباید از دست برود
🔹
با توجه به فشارهای ایجادشده بر مسیرهای دریایی جنوب، اهمیت بنادر شمالی و اتصال ایران به روسیه، آسیای مرکزی و کریدور شمال-جنوب بیش از گذشته شده است.
🔹
بنادر شمالی می‌توانند هم در تأمین کالاهای اساسی و هم در صادرات و ترانزیت کالا به اوراسیا نقش مهمی ایفا کنند.
🔹
هر تصمیمی دربارۀ چارچوب حقوقی این پهنۀ آبی باید با معیار میزان تأمین منافع اقتصادی، تجاری، کریدوری و امنیتی ایران سنجیده شود.
🖼
اما سؤال اینجاست:
رژیم حقوقی خزر چگونه می‌تواند بر این ظرفیت راهبردی ایران اثر بگذارد؟
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/455937" target="_blank">📅 22:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/deafdaed1d.mp4?token=Gabr7OgM4aXU0AZdBctkqAe25pB6j1PHs5nz6oJyowTORZVxVX5IgtxIfwfCyeJ_IhEVVEMxA3F03inmqKmf5hQTxSLR2Y0AaC3X58CeduHjdLNmWUWx1jfhY9ZqV84H51S6Duj9OQyi-6U9WRy1Rv_XFL4WMxnUv_9sBfqOYW8kPXs9_AriIVFxd-N9vSer-oFnlpf0NCbj3xiakBelldU9LultIkcz97Ef319IJYSGdOB3jYi6YTNft2c1C0rU6BUuo9o6JxS3GG14uWv4Urc_nJWL7HjOuN2kzQnl5ZEKX0Pj5v0-5XYAOoNBEiyToVJEhZ3_rkcBWFcYLF7jog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/deafdaed1d.mp4?token=Gabr7OgM4aXU0AZdBctkqAe25pB6j1PHs5nz6oJyowTORZVxVX5IgtxIfwfCyeJ_IhEVVEMxA3F03inmqKmf5hQTxSLR2Y0AaC3X58CeduHjdLNmWUWx1jfhY9ZqV84H51S6Duj9OQyi-6U9WRy1Rv_XFL4WMxnUv_9sBfqOYW8kPXs9_AriIVFxd-N9vSer-oFnlpf0NCbj3xiakBelldU9LultIkcz97Ef319IJYSGdOB3jYi6YTNft2c1C0rU6BUuo9o6JxS3GG14uWv4Urc_nJWL7HjOuN2kzQnl5ZEKX0Pj5v0-5XYAOoNBEiyToVJEhZ3_rkcBWFcYLF7jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدرت‌نمایی دوباره در «مردان آهنین»؛ رکوردشکنی در رقابتی نفس‌گیر / لحظه‌ای پرفشار که به خون‌ریزی شرکت‌کننده منجر شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/455936" target="_blank">📅 22:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0oyT9K56qPu4WbTFPhx7w-vXontaF2RJJyztCeBJQ45wwTHEMkBBBlHoMFYbiyd9S2lPH5YLEeq42YOtXfo_ibcpndn53FhldubRs4ZG9EcIe9vs1Sm_EDIrBxW5492IQ_F506j-Coex4Knz0_Z8dCO4V-kOefkZnp19Z-QRuQhyDlzCUfOpG4mvg7QR_7iF2bX0L_wz7fgSZmfkl0QtJdvkcOhb8veBi6wbHiTu3nZvaSFz5S5s4S0m3N2DgrFwyi2DcACF_1We2YCBh9cawaz-839Tjn0zjJp1MXYeeg9JNg-6Cziq55Ks_A0XE6OIPfSkcNxQKYcUnVPEqw9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
فروش فوق‌العاده کوییک R-S پارس‌خودرو
شرایط فروش فوق‌العاده کوییک R-S با استاندارد ۸۵گانه، رینگ فولادی و ترمز SBR اعلام شد.
🔹
نوع طرح: عادی (از محل مازاد ظرفیت طرح جوانی جمعیت)
🔹
رنگ خودرو: سفید – مشکی
🔹
موعد تحویل: ۹۰ روز پس از پذیرش
🔹
مبلغ پیش‌پرداخت علی‌الحساب: ۱۰,۱۲۱,۴۳۰,۰۰۰ ریال
🔹
زمان ثبت‌نام: از ساعت ۱۰ صبح یکشنبه ۲۵ مرداد ۱۴۰۵ تا پایان ۲۷ مرداد ۱۴۰۵
🔹
سامانه ثبت‌نام:
saipa.iranecar.com
📌
متقاضیان می‌توانند در بازه زمانی تعیین‌شده با مراجعه به سامانه فروش اینترنتی سایپا نسبت به ثبت درخواست اقدام کنند.
✅
با ما همراه باشید در شبکه‌های اجتماعی ایتا، تلگرام و بله:
🆔
@parskhodro_pk</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/455935" target="_blank">📅 22:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/455934" target="_blank">📅 22:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79716cfdc9.mp4?token=Ei694gFIm02CylzeSNlgQW9BmTev1d_aMH6bCw7ClBTE3qX_OYUhFl7mVBQTLkgklhwnmPO4ok8zmOquy2rOm66a69oW90FfMiGh9VbfpbOy0xHHbi37UbwPZPRv2_FRD3G-V1FjF9j8tboWMZUzuh2yeyFHb_Tt7t0RigZuy52F0nd8OfNLRaAafuck3CVtkbq8EkGLxhQ4bxEcOydLH0RC2UWY9wwJxlNA9uT6AAKNmyYF-fPbM1ofqYfKd7ZAXR8HtewN38H1Df_ilaCn2HBz2v6OIbI0n_OYMvx27IPVj6x-H80-Fqg5iJDj0zwt5sE69qvx7Zb0TV_EYhyOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79716cfdc9.mp4?token=Ei694gFIm02CylzeSNlgQW9BmTev1d_aMH6bCw7ClBTE3qX_OYUhFl7mVBQTLkgklhwnmPO4ok8zmOquy2rOm66a69oW90FfMiGh9VbfpbOy0xHHbi37UbwPZPRv2_FRD3G-V1FjF9j8tboWMZUzuh2yeyFHb_Tt7t0RigZuy52F0nd8OfNLRaAafuck3CVtkbq8EkGLxhQ4bxEcOydLH0RC2UWY9wwJxlNA9uT6AAKNmyYF-fPbM1ofqYfKd7ZAXR8HtewN38H1Df_ilaCn2HBz2v6OIbI0n_OYMvx27IPVj6x-H80-Fqg5iJDj0zwt5sE69qvx7Zb0TV_EYhyOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: تا الان هیچ تصمیمی در دولت برای تغییر نرخ بنزین و سازوکار تخصیص فعلی بنزین گرفته نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/455933" target="_blank">📅 22:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkaUJJ22iPwCgYl36qnLsUmaT9ci9xcjK9w8s96-sxj5kuM1NDiBnuhcnPF-bKfRalSWtdOpBkqiaR5SMXiATgoEUkKdaYDziIYXZwim1a24jtB_ILYBvB11EnIKYJiVCqBAhgkCWAKV3e1O4srbU5riJo1NXJDituph1vctd5Ynk0hF3o72lHh4YkCkAPLdLcBXK338hyXIHhbU1aDai-lc9UiIshPl0zEDWNFLLlixaJG_eJFUOd0kzdWTaoBFDmAeOASRJZRotvmp-o3aly2buAhNMmPen2rCTDNJ2K6U2dRg1PJG4SX2JDr886yW4NR2sIf6mIttZRZd2e1_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علما و مراجع تقلید در دیدار با رئیس سازمان بسیج چه گفتند
🔸
آیت‌الله مکارم شیرازی: بسیج شجره طیبه‌ای است که مردم و کشور در طول سال‌ها از ثمرات آن بهره‌مند شده‌اند.
🔹
آیت‌الله سبحانی: ثبت‌نام ده‌ها میلیونی «جانفدا» تنها یک عدد نیست؛ نشانه‌ای از ظرفیتی عظیم است که می‌تواند بسیج را از یک تشکیلات به یک فرهنگ فراگیر ملی تبدیل کند.
🔸
آیت‌الله سعیدی: بسیج باید کاری کند تا شادابی و نشاط در جامعه بیشتر دیده شود.
🔹
آیت‌الله اجاق‌نژاد: مسجد می‌تواند حلقه اتصال مردم و میدان نقش‌آفرینی آنان باشد
🔸
آیت‌الله حسینی بوشهری: ریشه بخشی از پیشرفت ایران در همان روحیه‌ای است که نامش «بسیجی» است؛ روحیه‌ای که از جهاد، مسئولیت‌پذیری و حضور فعال مردم شکل گرفته است
🔹
آیت‌الله خاتمی: انتصابات اخیر فرماندهی معظم کل قوا، نشانه‌ای از شکل‌گیری یک آرایش تازه برای مقابله با دشمن است؛ آرایشی که باید امید دشمن را به یأس تبدیل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/455932" target="_blank">📅 22:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f6611c4b.mp4?token=WEWdbEhmvJf0avxM2zZYflg-crR43H15fdtcRc-k5s4jt2FvFpCekKBlF5I-J5tvMDQ6gatYFWQCDNTWOeoZ7Wyix_jlkFT9ZX2uHEmvCIFWFRZBosN-qCsg27P0JF580kkuonjMAmWb8q8Y4hkv1iOJyXRtYasAzuBnd-QoiE4Ctj1ikK-0533SXGh7X1rPAd8Y7jhPPRv8dgz2RtliZ4Cbj8MHTubkBGyqhON4fyYo20MGf9MB0q2s3QdQmuLJQrhBPTi3u6eObGgSrwu5WxouXu1dk-0k7qX5y2XbBepIm2joLkTzvrlWSaPBwno6MIMmZUig1g3NanqFiWUECw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f6611c4b.mp4?token=WEWdbEhmvJf0avxM2zZYflg-crR43H15fdtcRc-k5s4jt2FvFpCekKBlF5I-J5tvMDQ6gatYFWQCDNTWOeoZ7Wyix_jlkFT9ZX2uHEmvCIFWFRZBosN-qCsg27P0JF580kkuonjMAmWb8q8Y4hkv1iOJyXRtYasAzuBnd-QoiE4Ctj1ikK-0533SXGh7X1rPAd8Y7jhPPRv8dgz2RtliZ4Cbj8MHTubkBGyqhON4fyYo20MGf9MB0q2s3QdQmuLJQrhBPTi3u6eObGgSrwu5WxouXu1dk-0k7qX5y2XbBepIm2joLkTzvrlWSaPBwno6MIMmZUig1g3NanqFiWUECw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
🔹
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/455931" target="_blank">📅 22:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0OQ0vMc746vgGW_suOW7H1svdt53nfqi64KYtBbMt6HZF35eZNa3zMObEo1HOk2qNfN_V3r5EdB35KF2Eu-3a7aDfBezFTnjvpskGdf4FGe42Ikqk85LoJ6AKiGO0NPTZvAGz_Uy7PYZAoulMGIFLodt748LIgn3FCnxcyOTkvESvrQovzY3DWYDJBWXXTIr67YEMMlkewO6BbtgzaxOz4KeMfdphixQ2R_patbbA3_YJYiWmkpqgYgTaCpJBhVP9uVuVIAQtOLsKc29PKJeoLpF0lLrJACm1JnJw0Fa3aMhRtwXEYWeogv3csis0mj5H4tl-je7pSktbtALTLnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا نخستین روز ماه ربیع‌الاول است
🔹
براساس گزارش ستاد استهلال دفتر رهبر انقلاب، ماه صفر ۲۹ روزه است و آغاز ماه ربیع‌الاول ۱۴۴۸ روز جمعه ۲۳ مردادماه خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/455930" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e928a011af.mp4?token=XPtqGMxmi26IFYeEYZVtWugb0flL5ro6qY0lEpmt9WDMAG13DjH8Wij-sUpq4_6Xn27HaWDvjgjYnzDaYeJO0fJ1BXG-Gd0ZkjDKTuE-CqwWsy2nQvgRzuZPLtffgjjOFVKJMbPldvkcXTqXwG68sTQHJv47EMTu92NvBV-y3ry7_4m7U8Z8DEafcREdDBpUKH3UGfB5PmYoHvVshuaUjVon7xrdej3Skmbo8Ah2TVXOfRyyifQvdLkRd7hYVq6zss-qg9mfdzPFtAbPW43ipvvSbouM7WcSvE5_TxD1Z5Gl5IIlKc9Q9zxqg8k2aFRJyf-8k12Xokeive9KO_ZJiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e928a011af.mp4?token=XPtqGMxmi26IFYeEYZVtWugb0flL5ro6qY0lEpmt9WDMAG13DjH8Wij-sUpq4_6Xn27HaWDvjgjYnzDaYeJO0fJ1BXG-Gd0ZkjDKTuE-CqwWsy2nQvgRzuZPLtffgjjOFVKJMbPldvkcXTqXwG68sTQHJv47EMTu92NvBV-y3ry7_4m7U8Z8DEafcREdDBpUKH3UGfB5PmYoHvVshuaUjVon7xrdej3Skmbo8Ah2TVXOfRyyifQvdLkRd7hYVq6zss-qg9mfdzPFtAbPW43ipvvSbouM7WcSvE5_TxD1Z5Gl5IIlKc9Q9zxqg8k2aFRJyf-8k12Xokeive9KO_ZJiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز پرباران در راه ایران
🔹
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔹
النینو که با گرم شدن غیرعادی آب اقیانوس آرام شناخته می‌شود، معمولاً…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/455929" target="_blank">📅 21:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۱۷.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/455924" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۱۶.pdf</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/455924" target="_blank">📅 21:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96f74ca48.mp4?token=PLhn4mzYxRUV9ziL-vYiUzQNd3iSlnSthtL_1NyyL4ATVy0vK0W6PQ80AaiJ9D4vwUsu3MPA0lzGIrCTcecA1K48YwLjkddkrufq0dRY3Bie3vRbVq2gz8BcOdKzjSQZ5pn7P_GT5Gw3LYISVl7VQnYj3GOZ7WNC2xguO27iXATQVxm6Cf2MciBrg1Y26saFsRbEJBq8bkJSGW-_nMTqJypk-LxBRuHFXzgi9wbW9XlL5J-Y9OZ0xSImJYty-ZokOGLWxonC1YhnoeVxlH3kCIZDPMpn6r40RlPoH0Ftm8WE_AInHvvoqT97tQQ3V5aERN_IPQVaHHn5NQzyKtyOiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96f74ca48.mp4?token=PLhn4mzYxRUV9ziL-vYiUzQNd3iSlnSthtL_1NyyL4ATVy0vK0W6PQ80AaiJ9D4vwUsu3MPA0lzGIrCTcecA1K48YwLjkddkrufq0dRY3Bie3vRbVq2gz8BcOdKzjSQZ5pn7P_GT5Gw3LYISVl7VQnYj3GOZ7WNC2xguO27iXATQVxm6Cf2MciBrg1Y26saFsRbEJBq8bkJSGW-_nMTqJypk-LxBRuHFXzgi9wbW9XlL5J-Y9OZ0xSImJYty-ZokOGLWxonC1YhnoeVxlH3kCIZDPMpn6r40RlPoH0Ftm8WE_AInHvvoqT97tQQ3V5aERN_IPQVaHHn5NQzyKtyOiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون تعارف با قاضی دهه‌شصتی که مداح اهل‌بیت است  @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/455923" target="_blank">📅 21:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59be13619b.mp4?token=L1frTCG6A14FEWNVanCn-jPlhxBip4Zh_T-u2XcY686SxVqv-pCXZ633f4vk5tjDtmU4ICMmNHACSlCpGVRyO06fUVVNeZ73i8b71XM59gFOQxrAcDE9I56q20YQ1XCgu3pIqh7QHvZJ5UEHxHKpBbJL5W41arV6LUbUfn1PrXx-Z3DPV1nUMeQv_pGs-thxVaLNyqxETRzYcyj2zWuyDKcr_bVD4-sw0pNcKEORGmBQfLEjddIkdM7c2Mez91fJTZHvFCBeVfy7eQJd1UNy5867h0-Y_ZDQGa5yDOhW0MDmG4VzBaARtHP487ZUCL9EFJnoAnS0vVbochN5iuxSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59be13619b.mp4?token=L1frTCG6A14FEWNVanCn-jPlhxBip4Zh_T-u2XcY686SxVqv-pCXZ633f4vk5tjDtmU4ICMmNHACSlCpGVRyO06fUVVNeZ73i8b71XM59gFOQxrAcDE9I56q20YQ1XCgu3pIqh7QHvZJ5UEHxHKpBbJL5W41arV6LUbUfn1PrXx-Z3DPV1nUMeQv_pGs-thxVaLNyqxETRzYcyj2zWuyDKcr_bVD4-sw0pNcKEORGmBQfLEjddIkdM7c2Mez91fJTZHvFCBeVfy7eQJd1UNy5867h0-Y_ZDQGa5yDOhW0MDmG4VzBaARtHP487ZUCL9EFJnoAnS0vVbochN5iuxSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش فایننشال‌تایمز از حق قانونی ایران در تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/455922" target="_blank">📅 21:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5aadfdeb.mp4?token=sV_un6kzWA8mUZHnfFPczPMGBJk9PtwYEZFr68aptxWIf7OKMNMD6Ymp-dU9jzDCkYDzfWU3KoSHoPjrB68cLNmGgpWOmwnz9Nj6M07-47akXz73AxFguPQkS_xtvsI-oZh2E9E3qBTJvcbPjsx10__F0GFtLoviX4l3AqKXWQy2cSYseZuZqqjQ8eL0I-DqATHttR1bsAxb0w6Gf5F0v4pj6vElzvXtq4br9xntuY-M-4ygFeGH87YaLWN7SUArYl--rxl-aKbP6z2Mj-HXoWd_THcgl-ZiUFBUDtL931jHD1FhN_QBtRtC1pxvi28V4GQn0WpRnirGiZVUzOUUElWYRGZPfyIF3BmfMCOk67n-alQJjULE6uZymL7YpUrJPgQV7dP0RuqjgmaUJRAr5e1cbZB17ZkLQjkdiVedW6Ip_re5HtfRp-ctAtW-bPLMD369mqEqeVqNItwD1MUmV3f0lgt3jCBS-Kujh9rsrxTOIIKzJhNxnpuS_EBQ7TqfE6sa1nw_96B5CZxdpxFgYyZoKKPjm5ntp0CGTQ71bgqiLHN9Ja9xvAbaIvBYLBADwN1_Z6ddDSr7YXmmsCkwhq1PvAW15lxFs1YSnR_h-Ab8IgvxiT5UZm3wWB_wQkJgYq5IYdKNW0HoaPYLG41ZoAT2KmExaCotBX8araSltvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5aadfdeb.mp4?token=sV_un6kzWA8mUZHnfFPczPMGBJk9PtwYEZFr68aptxWIf7OKMNMD6Ymp-dU9jzDCkYDzfWU3KoSHoPjrB68cLNmGgpWOmwnz9Nj6M07-47akXz73AxFguPQkS_xtvsI-oZh2E9E3qBTJvcbPjsx10__F0GFtLoviX4l3AqKXWQy2cSYseZuZqqjQ8eL0I-DqATHttR1bsAxb0w6Gf5F0v4pj6vElzvXtq4br9xntuY-M-4ygFeGH87YaLWN7SUArYl--rxl-aKbP6z2Mj-HXoWd_THcgl-ZiUFBUDtL931jHD1FhN_QBtRtC1pxvi28V4GQn0WpRnirGiZVUzOUUElWYRGZPfyIF3BmfMCOk67n-alQJjULE6uZymL7YpUrJPgQV7dP0RuqjgmaUJRAr5e1cbZB17ZkLQjkdiVedW6Ip_re5HtfRp-ctAtW-bPLMD369mqEqeVqNItwD1MUmV3f0lgt3jCBS-Kujh9rsrxTOIIKzJhNxnpuS_EBQ7TqfE6sa1nw_96B5CZxdpxFgYyZoKKPjm5ntp0CGTQ71bgqiLHN9Ja9xvAbaIvBYLBADwN1_Z6ddDSr7YXmmsCkwhq1PvAW15lxFs1YSnR_h-Ab8IgvxiT5UZm3wWB_wQkJgYq5IYdKNW0HoaPYLG41ZoAT2KmExaCotBX8araSltvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون تعارف با قاضی دهه‌شصتی که مداح اهل‌بیت است
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/455921" target="_blank">📅 21:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8e93792f.mp4?token=MqJ7eKUAffcwiJrkytGRFfkolFIFeU5pOM14b_UpyEONu44eZ__Il8IDHI2LGISSwc18pcaWy5Gad5CglB4-0bNh15TJuNPTwD8GmaQlP6jVzTlr_zLEjUB3lsUi3XwKr_llwdx8PuWTq7Ppf6A87O5lR8OD_l3R7IZemYGOGpwbHLBgfC_PqlxfYjS5bsITpX_JW4gOcyax6jpemxaIl2Iq10juN-SlQ2RUZ3KKuyZFPFkbqf_CBCX2l03_BK3mojeyMN9BbT1SqzkWqpMKarR297Er449Bo2yhRQs706685jlukyav44k853jqKMy7fPeDKhv5wf0-RXj-SSIlWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8e93792f.mp4?token=MqJ7eKUAffcwiJrkytGRFfkolFIFeU5pOM14b_UpyEONu44eZ__Il8IDHI2LGISSwc18pcaWy5Gad5CglB4-0bNh15TJuNPTwD8GmaQlP6jVzTlr_zLEjUB3lsUi3XwKr_llwdx8PuWTq7Ppf6A87O5lR8OD_l3R7IZemYGOGpwbHLBgfC_PqlxfYjS5bsITpX_JW4gOcyax6jpemxaIl2Iq10juN-SlQ2RUZ3KKuyZFPFkbqf_CBCX2l03_BK3mojeyMN9BbT1SqzkWqpMKarR297Er449Bo2yhRQs706685jlukyav44k853jqKMy7fPeDKhv5wf0-RXj-SSIlWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر میراث فرهنگی: برای حفاظت از آثار تاریخی کشور از پهپاد استفاده خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/455920" target="_blank">📅 21:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d296da6f6.mp4?token=mpDYx_pbTNv2cX9Fa1WiROfLS1BKgFPDHa047P5ThhsxwrQp9NqvjxSXFta9490_VCt3l0oRBLJiFVLm5mKXRNRlZjeyi0EiykWp2t9aUjlvQMDzkSSMDCE2nWNEZgtJIQU8KlrvbyHCgZBVYJAzkzWNMtxcyaPGg983ST3U3j9_WbZog2JQNizCUysWrWrNxwmEC7dDd94EFvySOdGtdp-NxXchGr4q6mvEEePHr_oMWw0UBDfP3rK0M0gCqiLSG1pWll0qOC5xdLOdnOdKhUIDH5E0GKcsLJbTeRQzMH3LIvwOaLiPfPZ2LVwUFr8iZqZEOaJEh78Znb_XCHTQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d296da6f6.mp4?token=mpDYx_pbTNv2cX9Fa1WiROfLS1BKgFPDHa047P5ThhsxwrQp9NqvjxSXFta9490_VCt3l0oRBLJiFVLm5mKXRNRlZjeyi0EiykWp2t9aUjlvQMDzkSSMDCE2nWNEZgtJIQU8KlrvbyHCgZBVYJAzkzWNMtxcyaPGg983ST3U3j9_WbZog2JQNizCUysWrWrNxwmEC7dDd94EFvySOdGtdp-NxXchGr4q6mvEEePHr_oMWw0UBDfP3rK0M0gCqiLSG1pWll0qOC5xdLOdnOdKhUIDH5E0GKcsLJbTeRQzMH3LIvwOaLiPfPZ2LVwUFr8iZqZEOaJEh78Znb_XCHTQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر روی لینک پیامک‌های جعلی ابلاغیه و برنده‌شدن جایزه کلیک کنید، درگیر اینجا خواهید شد
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/455919" target="_blank">📅 20:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb3b61d3e.mp4?token=hzhiw0I99IVnXAqar-DkqClBs2UGpdAyO3MTLGWvgiolfEFAhRAvSszrvxZyuoeLt8uPka3eQdXqYyrKlfCY2pVSxMt2Ih38EG3Mn8K6wMuayE0Bq5mJcmgdJ5gyyiT3jPtPkudyYxK2WWh4YZhkTGMHbWqb1N-gTFe8ltVC7plBBRV2U-rVcqzPNRoIEWlc5mzviknoZVBj-23ynlbrcgHigF3BXgkwEFa1j_pe1Ykgymcw65IrYHz8lUb5Bcub7vAJEt1i793fHczg5Bl0LkoFkbH6HEr-1x9_Ko2sR7wqBnD9vYAupWo2BEuUFWisPUzaCrl2xAD4FzilM0VrgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb3b61d3e.mp4?token=hzhiw0I99IVnXAqar-DkqClBs2UGpdAyO3MTLGWvgiolfEFAhRAvSszrvxZyuoeLt8uPka3eQdXqYyrKlfCY2pVSxMt2Ih38EG3Mn8K6wMuayE0Bq5mJcmgdJ5gyyiT3jPtPkudyYxK2WWh4YZhkTGMHbWqb1N-gTFe8ltVC7plBBRV2U-rVcqzPNRoIEWlc5mzviknoZVBj-23ynlbrcgHigF3BXgkwEFa1j_pe1Ykgymcw65IrYHz8lUb5Bcub7vAJEt1i793fHczg5Bl0LkoFkbH6HEr-1x9_Ko2sR7wqBnD9vYAupWo2BEuUFWisPUzaCrl2xAD4FzilM0VrgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی منتشرنشده از دیدارهای صمیمانۀ خانواده‌های شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/455918" target="_blank">📅 20:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUA2qdMSm80vS1xaZKMMPVMrz4FacMZTV6sHFj1NbF4BQYeMFJojn5Db3UuWn_kj5A31bWuaL8jvU7wgUvcqKeroVA1d6r5FVd0LBM1hINuPkzzpEKsuhkgIiiiXwxdHPKaF8dlRjqG7cvTR3OPGk2laAwwjftYgfJhza-HSDt7EgJnOYg3_5UgiJ5MoHjt4Ho6Ftl_1gmvhQNE7FnMCilkutaOKUYuvkki_BYvouvVFI5nvp4RqcUsGtcEhnciMuntJ5pGlo4EnynXAIt_ZmR3elA7zm45f8iccejXuGM2ERAd6Jq9syx1RKBlauOJYldMxLNj27gLtwSCYll56FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعۀ بزرگ دربارۀ پرسپولیس
🔹
طی روزهای اخیر شایعاتی دربارۀ راه‌اندازی تیم «ب» پرسپولیس و حتی انتخاب سرمربی این تیم مطرح شده اما پیگیری‌ها از باشگاه نشان می‌دهد تا این لحظه تصمیم نهایی در این خصوص گرفته نشده است.
🔹
با وجود مطرح‌شدن بحث حضور تیم دوم پرسپولیس در لیگ دسته اول، این پروژه هنوز وارد مرحلۀ اجرایی نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/455917" target="_blank">📅 20:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813cb5c9e.mp4?token=Uidb_k51BB_duXQl4OvU7eQ9T_ZzTbbPK5klTlfQZkVCMfTjWsw1apIa-4zn1Gb-DyWeca0Sv10Xi84RfIYsot0NK-TvK9evHOHaJCsso056qRuEpD_09sX4YJgUcsmxRhQmcoXTED8SxSYAlH9igtl5zNJkhZTsiHPD2hEXT0obsU0pvBoGyDWB6Hf7f_s6oEgBtzGi3hfkfW3qquiRDHLur0IorxTKzY03cV1DMIetcND0p5T5Ml4Cvgbh-rsj51TJYRsDwHAf8toiWKxWb7oDSbPHjiA2A59txbygKxe20cKAEZLUoYCSubc8ty2ravBQQyZcRumh8pWNtCN7Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813cb5c9e.mp4?token=Uidb_k51BB_duXQl4OvU7eQ9T_ZzTbbPK5klTlfQZkVCMfTjWsw1apIa-4zn1Gb-DyWeca0Sv10Xi84RfIYsot0NK-TvK9evHOHaJCsso056qRuEpD_09sX4YJgUcsmxRhQmcoXTED8SxSYAlH9igtl5zNJkhZTsiHPD2hEXT0obsU0pvBoGyDWB6Hf7f_s6oEgBtzGi3hfkfW3qquiRDHLur0IorxTKzY03cV1DMIetcND0p5T5Ml4Cvgbh-rsj51TJYRsDwHAf8toiWKxWb7oDSbPHjiA2A59txbygKxe20cKAEZLUoYCSubc8ty2ravBQQyZcRumh8pWNtCN7Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
شام غریبان امام هشتمین است
◾️
مرثیه‌خوانش حضرت روح‌الامین است
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/455916" target="_blank">📅 20:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14394ebcc1.mp4?token=vaEIRI-CiJVRCXJCE3izrDJWAA1q9tzB4XdkOOn5OU4cToJTx4idaJuDqpEkYimahRyLgcNm97gbKBfo3nkt82Rrxe6uYVHR-rfURVJOKCqv8RAMfS4DBBtBE-vN9dAq26eF6tpfv_SBHvETsIIOQ7cXMEWOsksDMP34reP-UUcAcTms1gR4slsK-dF-gyC_N45m4XQrq6sR6tro9c_Tie6N0gTesvYRG9hpubXYFkafPH6ps0VWJjyBj0yP5O-GznFfjKr6fmZBw8TgdqTiMc56CwHfB4wkCy5tN5vUSQqVZzebEFlD4AxgcKHz-Dy6hgvsRYYq7SmvYpkpiWsJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14394ebcc1.mp4?token=vaEIRI-CiJVRCXJCE3izrDJWAA1q9tzB4XdkOOn5OU4cToJTx4idaJuDqpEkYimahRyLgcNm97gbKBfo3nkt82Rrxe6uYVHR-rfURVJOKCqv8RAMfS4DBBtBE-vN9dAq26eF6tpfv_SBHvETsIIOQ7cXMEWOsksDMP34reP-UUcAcTms1gR4slsK-dF-gyC_N45m4XQrq6sR6tro9c_Tie6N0gTesvYRG9hpubXYFkafPH6ps0VWJjyBj0yP5O-GznFfjKr6fmZBw8TgdqTiMc56CwHfB4wkCy5tN5vUSQqVZzebEFlD4AxgcKHz-Dy6hgvsRYYq7SmvYpkpiWsJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا کنوانسیون خزر خطرناک است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/455915" target="_blank">📅 20:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojs3b38NZXjM9AkFYB0YdIxtfZHrVOE4JXSmwpL_v0rpv36VDxJHbu8B5qEpchi30psL8roGEvKRXgyiqyJMRf7Y3cT6hniBBW6JQl5bj6gXZlhC86ssK5mDvh5pFEaU_TpYezyTF_lB-mIrdVYT1ZIw-mygZDEv1dh1bKiJehI_ib3kfFRBM97G5pRZX51VZ-0lxd0NTHPvOcCQs405exag5L9P0-dquCq7F6_baRQaBvWht3KgRHhhRXGsVr1an3ouE9Y8cuWuwJ_GlTwMHrtdTLpDiYy8nBMdYXYUWw6YebD-aEQOvY7kFFu63dMJPJ3B52vYlsN_KuYdx1CZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: یک‌چهارم پهپادهای MQ-9 آمریکا در جنگ با ایران نابود شد
🔹
واشنگتن‌پست به‌نقل از ۳ مقام آمریکایی: ارتش آمریکا در جریان جنگ با ایران دست‌کم ۴۵ فروند پهپاد MQ-9 ریپر از دست داده که می‌شود معادل حدود ۲۵ درصد ناوگان این پهپادها.
🔹
ارزش هر فروند MQ-9، بسته به تجهیزات و تسلیحات، بین ۳۰ تا ۵۰ میلیون دلار است.
🔹
این پهپادها به‌ویژه در اطراف تنگه هرمز به‌شدت استفاده شدند و برای ایران و گروه‌های مقاومت اهداف نسبتاً آسانی بوده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/455914" target="_blank">📅 20:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHw3ivcQBQ_1PBJOnPy5Vfk1S2UwnPsC0Sp9aqlA_o5aWjUeO8IuHxqx8R8W06WjqugKWtzwWe7AHVhJR_JcDfYFs7VFSMARrx2Krc5o0LcNPbyoPNwF_1S_1BY9Ow4Obl_NW8wFIh_JsSzDRwZ89aAbN0Y148VufjsN98WTyndMg9SMybAyrxPqKJm15sEONPhJImmyW9xBDyFzlSAf6WMiVreQIicTNgjnKDGBDpy0Ps_A1_vesUDxb-ieoovFEs9p7fTNeFRmoEJOW70hcUEWYMU6DPlsVKqMcSE03L2t0banTqlP0_OmEqVpthvyxmtCzV8rgTtprSWVIPHFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGWcXTFh918O7WZhszaPAbjly81qLO1jMP9L53BLZRS3e812-A7XsdOb1v_68MnRCf2MhiACZLbovisPSvbv5ApDqQwHVMX38Y6WEVJVcOGRCaFAbQAhIOZ2fPitKheouRm-7IjhOT336q7RoZ4-SXsC7K4DiHGG7TDbSFjeX0usPJ246OzZIc8Gz-xxLlcO0dYPDuRFbZgST_thz45STW6AagRFseo5_zFOpVMldVx6_BB9O-qPNFeS1l2_Wa1E7KaJgUNLdIPbp1kpJ0xZiLxNhC_osMxeyb6tOfKXDvo7SA8YI9Gzbk2LdlsZDdxlGSEAzvxiqPfhll3Vz7PPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qr51EEZOmVUJJnbHb0QQz0ATqt97iicpWGznmsaClkmHm_85dujgPCC9_UXxKVR_5oXUJ6__39JaiMeC0zGpP9ZkRqIpWbsrutwmLFW2y6G0ra_dJB2iapYiYRr838dCa-D15YNhfnXAADfGWK4Jpm0rj1KlzaEQMRsj-_pE8H3xHZvTcewNyMYfT25eFQkBzzqBHC6dfF5dq5_MRcQU3J8jhLesYt6XNhNNVTbSCvhM7indJuWHo1bSKPoH13pspdN-qMa5jXpegIcGQ6Yyr5nwD04_YmxN_hbdpOOOKuHZmYD2Xgw2rfijZc5xj0-QDarp29NXvgryewQZogKmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBoNwoHs6RIgBeXEaXb2Wn2gZ8Nm5PU26ZsHhQKKLqYIJSEQ6N9myT9us5q5_WoilZ_cU7ef9v__B8Yl-tHL9PcsyRBJZ2ynW40ybZlCfp5xoS87wg-z-C7nC8VpaMSs7DBCtwbSCwuzFupGwMadzhzeJmADEOtlmgatANpy67ve3m1us2h6TljWnR_gnEzrWHwtNwla1VCj3tTwAk5c98ucJT8hezFe2OVwVd_HKSP-vwqzFtSp2WSC3-t4aIx7DABMjMt7i1BIbcgXbNJicHPAuvY9hQ5j8zkpNFPxF2JvF4sxuIzzxljDSmjYW2A5TGIl0H6qtuES56ht75ucfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید از ضربات ایران بر ستون فقرات آمریکا
🔹
امارات:
رادار راهبردی TPS-57 در پایگاه الظفره
🔹
امارات:
واحد فشرده‌سازی گاز پالایشگاه حبشان
🔸
بحرین:
مرکز داده پشتیبانی‌کننده اطلاعات ارتش آمریکا
🔸
امارات:
واحد کربن صنایع آلومینیوم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/455910" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP3RBy1JgjrUkwY43PXECWLO9Scshn4rPI3A_9Uz-zvDzp_soJeuHAgROABZuqtzg_5dvGsGpglnu4URuWZ8wTYPGemQYjpjeiihi2FkSff7tPQ3BkWPPMkWlRu9lz0LsHWHA-PtmWQeCX-gKsSrXyzQ7tnyOxUAMSYui6TL9RZ-pg2q5R3q8aLFId0JDxBtaoVOSWxNpLiEXhyYfm6nDMGSFfzifdR8l2dpYZnuiNf_44AKPRKcSWn7mSC8RJ0SyehtBx_rQdqamHsWmUVg0XrkH3Uh7rjlI_P9qk9bOnQM-gPqukm9vlrSeFBsQq6fK701DmDncMzhYyZz31861Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال بازنشسته آمریکایی: پهپادها و جنگنده‌های ایرانی دمار از روزگارمان درآوردند
🔹
ژنرال بازنشسته نیروی هوایی آمریکا، گلن ون‌هرک، در نشست سالانه سمپوزیوم دفاع موشکی و فضایی در هانتسویل، آلاباما، با ادعان به شکست سامانه‌های پدافندی این کشور در برابر حملات هوایی…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/455909" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455907">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">حملات یمن به پالایشگاه آرامکو در «جیزان» عربستان
🔹
یک منبع نظامی یمن خبر داد نیروهای مسلح این کشور، پالایشگاه شرکت آرامکو در منطقه «جیزان» را هدف قرار داد.
🔸
این منبع با اشاره به اینکه عملیات مذکور به دو پهپاد صورت گرفته، تأکید کرد که این پهپادها در نهایت دقت، به هدف خود اصابت کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/455907" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455906">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c120c1ec00.mp4?token=LEaDGvJC9tjgwamaIh7pLVVpIiq0mrwrIYPdxJjBcrMTNzTL2wOdWSEldwd-pPwPgi0wr_eHcJkWktrxUTQRJDkjKYcwpR-Qt1XwgxP9LFMCYwHtURtd-L5GAq68_gQNDGEQk9CKRbKX_RMBgjWZm4hwnS08XnmQkDhV5S0_8l3QLGU0ahwiLKKOLoEx1gkoJPSFSNcrqrSVPPbTNXVB7la4MjLZpb9uALShMA5iy5dJ8d3kyVy2MFBxckna0QZfX1wVd__a7TCGRg06y-4iaqE_ybekrI5wP8h2YyggTcVQc7N1q6aJfyjk_5d64exwxlzGkuIHX8_7m4Q1Y3ajtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c120c1ec00.mp4?token=LEaDGvJC9tjgwamaIh7pLVVpIiq0mrwrIYPdxJjBcrMTNzTL2wOdWSEldwd-pPwPgi0wr_eHcJkWktrxUTQRJDkjKYcwpR-Qt1XwgxP9LFMCYwHtURtd-L5GAq68_gQNDGEQk9CKRbKX_RMBgjWZm4hwnS08XnmQkDhV5S0_8l3QLGU0ahwiLKKOLoEx1gkoJPSFSNcrqrSVPPbTNXVB7la4MjLZpb9uALShMA5iy5dJ8d3kyVy2MFBxckna0QZfX1wVd__a7TCGRg06y-4iaqE_ybekrI5wP8h2YyggTcVQc7N1q6aJfyjk_5d64exwxlzGkuIHX8_7m4Q1Y3ajtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعویض ضریح امام رضا(ع) با حضور رهبر شهید در سال ۱۳۷۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455906" target="_blank">📅 19:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455905">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea128868b4.mp4?token=s3Dl9pHpgY21Vo29F89rNbmyXFFqO3R7JgFja54njagsK9WaNKf9jUOGl541OOYz5KBhIbGwFy7WEAWCpZJqWAwFkL2XJNkj2w720FnYbisNEtM_hn8klzObzQdxOSrYHIh72RjYs0NYZS5NiazUcHkQWRHVQ-NH4hJLAQHuiWO6fv5LvlM0b17aZd2PCVduKXvC3QbLRd4BWJxmceYeldZoHthIJvPfVS4i45Jehg5o2T4xC5_JVNlpzHUwprhPm1uNywtYJ5UHLH_emECM6t4mTSQHgV7-sjJe445ws7XOvPEUbZTklRn6Mr58XWIGYcr0wgFYjohtlWKNSQG5O2ppFu9-0buGFmNEeFCli_7_iTrBU7YupVxRixhRSLsv8diNW46BNd20kE0lC_N3MFebzndrL6SjcxTkHxnVBToddjVSShJKywXTs57K8l_tH_5Gs1zO5CZ-pIXUJFYMpbr6E7vx6GtC_TmBOx9IYFr8ElocUvEmUwdzDjCnUY7Jp39nQmNqUDXxXnF3mRj2MZCNIRrWLMiBATXQIAFTXZo0bFWU9xkKkWhtcap0P9OpG_g5Cop0-yK1rYM3byxRa-W_qpA98uM6_kUcZLyNH9VTYSa_P_Es3629TBSmrg8T-lddyObQMjZmWLxJ28Hg29Tto3F1W2A9Gr5a6GrbBA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea128868b4.mp4?token=s3Dl9pHpgY21Vo29F89rNbmyXFFqO3R7JgFja54njagsK9WaNKf9jUOGl541OOYz5KBhIbGwFy7WEAWCpZJqWAwFkL2XJNkj2w720FnYbisNEtM_hn8klzObzQdxOSrYHIh72RjYs0NYZS5NiazUcHkQWRHVQ-NH4hJLAQHuiWO6fv5LvlM0b17aZd2PCVduKXvC3QbLRd4BWJxmceYeldZoHthIJvPfVS4i45Jehg5o2T4xC5_JVNlpzHUwprhPm1uNywtYJ5UHLH_emECM6t4mTSQHgV7-sjJe445ws7XOvPEUbZTklRn6Mr58XWIGYcr0wgFYjohtlWKNSQG5O2ppFu9-0buGFmNEeFCli_7_iTrBU7YupVxRixhRSLsv8diNW46BNd20kE0lC_N3MFebzndrL6SjcxTkHxnVBToddjVSShJKywXTs57K8l_tH_5Gs1zO5CZ-pIXUJFYMpbr6E7vx6GtC_TmBOx9IYFr8ElocUvEmUwdzDjCnUY7Jp39nQmNqUDXxXnF3mRj2MZCNIRrWLMiBATXQIAFTXZo0bFWU9xkKkWhtcap0P9OpG_g5Cop0-yK1rYM3byxRa-W_qpA98uM6_kUcZLyNH9VTYSa_P_Es3629TBSmrg8T-lddyObQMjZmWLxJ28Hg29Tto3F1W2A9Gr5a6GrbBA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشنهاد ایران برای ایجاد کریدور مالی مستقل بریکس
🔹
رئیس‌کل بانک مرکزی جمهوری اسلامی ایران در دومین روز نشست‌های مالی بریکس در هند، بر ضرورت ایجاد کریدور مالی اختصاصی بریکس و اتصال شبکه‌های پرداخت ملی کشورهای عضو تأکید کرد.
🔹
او گفت توسعه همکاری‌های مالی بریکس باید از گفت‌وگوهای کلی فراتر رود و به ایجاد زیرساخت‌های عملیاتی، امن و پایدار برای پرداخت‌ها و تسویه‌های فرامرزی منجر شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455905" target="_blank">📅 18:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jK24239riro14MZGuBv99WVBDdG-OPdd_2yr0Qww6WGmWa-IXo5WSEP7ZlHc2F6D62xia5XLYEzHJRcGC7KegE2r7gkNGjI_zNmm1tKOiYCo75uKIRMnhaupexfi9ub9t8U2hexEtGq2C83PWzfKn2kDiQmREPerRDhFDRYpy6_ID_FgvwMVayJgO9goCjWNbG3324QgSCAvKqUA9mlLKVe0BObwCSIn89AJvINvSIMvYp47etdH0nxlSyxfpstgzSMXU_XsgW2H6x17df-xchWHCxlTI_m_QrcUuhos_WhRFCpxgvP4hiMXGyaMrJXG8vHiAuWg-WlaaE-e6yjoNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiIbu5QUpy9LLmeYaZF93N8AxaK0yQw73mmbLi4oqLXkGl4Cr-kE-AJ7fFeGKeqEF-vUeinIweqMt_v0S2vE2FVUXh7V4eBM4J_FO5Oe1VXMkbES8WYtNILq9J2Y4Vmt73b1T-T9AQuzH8-zKpmdreCKIS4ZJreD22K9caz73a1lzj1_9x364RBc2NNY1BXUrroPqtIlg1ma4tMN6bCLCnEjSV7Ej474xvAbuFWQf-LKNyC7FukTYY9Ak7YFJowwm0r7EWjL-lV3wdJQxvioHcJ6zEMP7I9Dpr4SxVHnPBFPY5BBiNBOZiLYQk0rX1otnmMS4-KfFF7El71kTIfEIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESYjDlBoSgXTOHX5WsrPgZHkoJCiWdApPrjsN1lqC8IE1O22u65cOqd9VDOm3NjhRP12dbD10oGZ7CbpPuPw9S9YEXvsqnCwJHUQDWlo8wb3ZXWLZdvZHTD6l3WAqDEGmx2mjEtHqsczp0VX3IIFQHfhDg3Kf3uohC_XgM_vxVftuuSbZvOaqyqGwzEA1XgQX7Ct82x7jsMElsizPBLQmGmOvYICYCXgt0Z7WfZORWJ7r90RCfzw0zcofB1tasLd68DcjGXG-uTLlga-zkpaJb7_LsbeWIiQZIkBzJVit0tTnlRcB-Uw1OU9NeVzy_aTbetOPPlVgrp2ByclM8xxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-kbtXrTrUoL6qwmWTHoQO9Ku4-aL01QD_gE4L7E1K0R9f-LbHv4cfKAfH0ncCOrs0RyZ7qtS8-_zcIr5pn6HOTurFrXpgNB3M0pCBCURkjGeJEY7xRM3aSYQU0becELsl7fG1MYk1gunSF_wCnMnFjenkor4ZmY0wZ015uTWmHWabDIsL0lmIWPnxEN2Ww2mSK5CeliohDPJTBbms5WZ4XRljld6nwlhYw_k0Q97WCH_Eniw3vxaTUtqrkGR3KnvMjwdCkmQmPDkDPU5RTk8OTvmmPpuwb7du9imU4PY9jXmklRf3NK_M98VnoUOyak5Po0T96ZHwozgeauVWJ8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXBiHeru6nvJCIajSxL_l6h9coasOoxOOLcCZ1RIiDKGwy8xj9ZL0M6TWOELr0nhHXeJCNZQS0LmM6flpFTslloymWsjJ3Kw31QVreIn49RB7pif3mPW-uDR86slwEim15tT04n3Y86Nm3U82NNXDHUBZZfgQgM4SRzvHCta02XYIK164nEC-qiznr21CgnB9DvbTJoPi2ELPk4pIksXRyOuZEXGUx7WTOTY3NRwPph-KiLm7gwlQCH2uqfRBkLkRg7R1BrR5QgRV-jZ3iVvg3Duv3pfbygG1zC7x_UuAceI9vR9PZuHXpTKnKdYt-Y5Z9afgztvAM5knLtxH68DbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5AsbLS0tYWtQi7-BUVUFVgd7C_G_a9gSZu6ebyov80viKG3wH827JSmde23r--3ENs1kshn4XZlpsIvSXQsToHs7WNcdrYMsUmZL8PbcnqSZ7QpenGFCE9fIw77UJtiQJtZoRvbp-rViQeyC3MAmoVpA_MsIgYlfNDPfnywF9OUbTluq-fETbqsSa0DoENsytFHWW29bC2t_x4vNnTjVIT2Z1pXz7-ONmQdbXMUo4O54Z3LndKd1ZzynqIzAC3TjdT4sDnjx6PJoUnvZj1PdRaojkHWBPu2ah3-PiKPaWEDC4A4aY8HvV2URCHuKJHeaKuwM4Wojq6ywoTSnOXWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4tax67aRsG6S2NLR5XhHYnZseEl6KnNh1MOySF4Vd1AiKEFnQupj-pBSnyNNvAK2XJFoEEYYJ9gEzh5fVlnIOqjYjvXESj2ybOUE8yY-8bNpxYif_zYsJGdjoPbJ_sbK5Mf9KP-o3ezLyJiKiungZGoyq_hSEhGi17HcFwQ2d8BJjaORpScsevVzs5iOQd3cv8VuzoVY3jM8yxntz17W4BXnfyohQO5qPb5YUaPHPiqHxJEq0uPb1PfpaY9i0Y8_kgrbISWgLHYDXrTB_0sCStfJ38F-uSzZb-bn8AHWFUSNlrEm2UbLO14DaBNZk_Bd8lY_e0vGUc38xqWTMRkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfWS2ZB1H_QaU3kbqVotorOV4RHrd2AWMGsKqPrtztoqADSTt6uEWBebWptE1jrJpN9RUWm7DMhZHqj_-bLy1OKWeWGBXO4uMWteSokrcFCzuoyMreHDKc9z-MW3xJh97kqKp5aPa9Pu6x6_64ZJDTinaOV9YexsUegePX0M8durXjnpC6yeafVYbzfs1in720eF9CH2BZftYmUX1WB1mqrxOY7BHhDfwOe1DYqOTauifmIobBI65d4Dk6IAl5qIvLE64QKINcHPMECmTNfsEadJuAfmsbooA5vxGWA1H5DxkR1qLto0Dm07bsXYynH-D9p4rTPhw7pYMoN7IaTBNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور زائران در جوار مزار رهبر شهید انقلاب در رواق دارالذکر در روز شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/455897" target="_blank">📅 18:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d9e5e0f4.mp4?token=Nv6pCj_fqu9wW3vAqGP0Ej2G81TTOoh52q0zXjBannQgTRYsG_dEMO-dk6QQDi17eve8TRPbDN3L4u6trrhNuFY7ZdBMhq_02odvP5dLRjc2AP2pK6ZcsAb3wwZq-1KmlaCQfYSgw1Zd4NKbMjaf9Q84KnW9rvfOMaCRYzlSFPl59-aM_ULyKP-SjuPrKaigqWdhZFNsWmnG1re-FIt0mOlpaOkt0YERv4p1MkQulid1sqsmWBDHwV4q1UY9b35VN0x8u1JS0Xejs8LqhUwmIgwWzG00gkDjib1trIGp58Rn4kp3IFqPWpz_IjwYZBtMPjavWe_efrRy8IVRjmnrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d9e5e0f4.mp4?token=Nv6pCj_fqu9wW3vAqGP0Ej2G81TTOoh52q0zXjBannQgTRYsG_dEMO-dk6QQDi17eve8TRPbDN3L4u6trrhNuFY7ZdBMhq_02odvP5dLRjc2AP2pK6ZcsAb3wwZq-1KmlaCQfYSgw1Zd4NKbMjaf9Q84KnW9rvfOMaCRYzlSFPl59-aM_ULyKP-SjuPrKaigqWdhZFNsWmnG1re-FIt0mOlpaOkt0YERv4p1MkQulid1sqsmWBDHwV4q1UY9b35VN0x8u1JS0Xejs8LqhUwmIgwWzG00gkDjib1trIGp58Rn4kp3IFqPWpz_IjwYZBtMPjavWe_efrRy8IVRjmnrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجرۀ متفاوتی به حضور و سخنرانی رهبر شهید انقلاب در مراسم عزاداری سال گذشته شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/455896" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d0d497a6.mp4?token=Bl_Jb-qHWPUBIeaJDEZEjq3wP8tpq-K7UINM9DW2EWIJsGIhmYwd8wfMfJLBnD82lQNwPfJCSAg6Q3bthIK52buhtSXjBNkWhkRTN6CDRBXuQYA5L4HopoJ0gbFLaeRHXzJcfuCkfjNX7buX1XYb9cBKJoN4qJcARgonDBslMlubWJGUf1vwJN5Yehb_nDYRnWx1hC6MadL0XBBni3qJYKPeBXsqHhX8rSJq80sbDGgdHzIMkDfuuZpGluWVwlP4bhmAR_4M9yUWLFLy1puuot33TOvVoCxjywFZ2AkPBMMr48DIwIzRvAYqsBbS2ZcMQbgGvFaYTc2UpDLCXn2LvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d0d497a6.mp4?token=Bl_Jb-qHWPUBIeaJDEZEjq3wP8tpq-K7UINM9DW2EWIJsGIhmYwd8wfMfJLBnD82lQNwPfJCSAg6Q3bthIK52buhtSXjBNkWhkRTN6CDRBXuQYA5L4HopoJ0gbFLaeRHXzJcfuCkfjNX7buX1XYb9cBKJoN4qJcARgonDBslMlubWJGUf1vwJN5Yehb_nDYRnWx1hC6MadL0XBBni3qJYKPeBXsqHhX8rSJq80sbDGgdHzIMkDfuuZpGluWVwlP4bhmAR_4M9yUWLFLy1puuot33TOvVoCxjywFZ2AkPBMMr48DIwIzRvAYqsBbS2ZcMQbgGvFaYTc2UpDLCXn2LvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لبیک لبیک یا امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/455895" target="_blank">📅 18:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtTNHgqOLjeezC-G4QZEFLTCpyxgJT-8uwI2GeTkQO-5OqXwOyd118AlQz0t1rAZevDE0sonkX2PIAknAbpOz0JyTIjAoLB5-cxGRgo7y8xw5Alg-Z8ektDP8ED5EQ4mF0r7GVIajYbEyDYolhqSGT6jyZJmZn1cxy3QraBlQjr_rIU4bf-2IGkBU1e8SsaFr8QlREQEuDciFxVg7K7CpvPU-JTiqErUrHwBq5U6bOHAU_KpdsQbDS3Unv2kX8eGc1EkCE6fUucEoQLSfngDnbHdNKkqKFuihBJ4eI74_bHcevau3yHlToOG4sUCzx88ZfzhD5KPPmsTWqyR5wg-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت آلودگی نفتی سواحل قشم از زبان رئیس سازمان محیط‌زیست
🔹
آلودگی از ۳ روز پیش وارد سواحل قشم شده و مناطق سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام را درگیر کرده است. هم‌زمان عملیات مهار و پاک‌سازی با استفاده از شناور، تجهیزات تخصصی و بوم‌های حائل درحال انجام است.
🔹
رئیس سازمان محیط‌زیست در این‌باره می‌گوید: «آلودگی نفتی سواحل جنوب قشم تنها یک نمونه از آلودگی‌های گسترده‌ای است که طی چند دهه گذشته زیست‌بوم دریایی منطقه را تخریب کرده.
🔹
چه کسی مسئول جبران خسارات وارده است؟ کشورهای مصرف‌کنندۀ انرژی صادراتی از منطقه ما یا طرف‌های مجاور این منطقه را جولانگاه عملیات نظامی کرده‌اند؟»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/455894" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab8d69ef8.mp4?token=abdkMAN-3GY85EEkesnJ89_FNzUhjlywTIF6NpWrmV3oNebSK4qLI16_YLC5uqvZI3o6E7Pl2lIrg-ce9ZYk4qLbM0-W8yr_iNmmwoy-Ky_C5eh9muJ094CYExeVd9NIhsbDshNBQeTKGYrUpdRNbK_GJ_GP5IZN_qusFgGN410hciWfFUTaEE3eU5FSFvsE2gVETTdK6hG6W_WpxkjLYsp54dZc0Yyy_iQW6oe4s3KMJgRd12WoqCpoeOSpdQhp4gZWkrgV1EJEnk4rRhGlNoJ40UGOfFIEdmPtnJKZhQeHGJwotrxepNitWYuRJBDEBHyer00pE81_anbFMSoHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab8d69ef8.mp4?token=abdkMAN-3GY85EEkesnJ89_FNzUhjlywTIF6NpWrmV3oNebSK4qLI16_YLC5uqvZI3o6E7Pl2lIrg-ce9ZYk4qLbM0-W8yr_iNmmwoy-Ky_C5eh9muJ094CYExeVd9NIhsbDshNBQeTKGYrUpdRNbK_GJ_GP5IZN_qusFgGN410hciWfFUTaEE3eU5FSFvsE2gVETTdK6hG6W_WpxkjLYsp54dZc0Yyy_iQW6oe4s3KMJgRd12WoqCpoeOSpdQhp4gZWkrgV1EJEnk4rRhGlNoJ40UGOfFIEdmPtnJKZhQeHGJwotrxepNitWYuRJBDEBHyer00pE81_anbFMSoHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در کارخانۀ مهمات‌سازی ایتالیا
🔹
رسانه‌های ایتالیایی از وقوع انفجار و آتش‌سوزی در یک کارخانه تولید مهمات در جنوب رم خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/455893" target="_blank">📅 18:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD-4jnwC6cIXUZFiw4a2QXp4Y6finpHmfyqMBEb5IWJ4YHyqXnUyP__qOI_kq3uBGy32WW7KK2guXnV6H7QgAGEvsL3ZUA7n635OJi6ca-Z_DklmAMFE2NfF_TYRLd6R5Sx7jbQuOpe_bosi7Wz8j4ztY0KrOXWwMgI2sm7F1zS40E7PJwAlbHZGY9cJHdPgJXKUZtJmimXRzITfWqbvOnNh1vjg5IGMBkMBghflTDYwrX-V5qvJOEO3pixE_rDfiI5Ho2dY-Mmio6VoVjJRLUCk-U5ZH02qP76pIKM00-1tvaVlopjpQj2JeAkAbj1i14zP5GlWWUNwQw-VuH_wVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جلیلی: دشمن که شکست خورد، تازه وقت ابتکار است.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/455892" target="_blank">📅 18:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bf8e9f37.mp4?token=PKX99IQPoz53hhJlFYIakZb07I_O7yl_PhXZXWbyesKrhPjg2NrFycQsFAvq84suU1UZ8jXbdk-mne_7txiw_I_M02KaunYVeYCK5GE51GvLKi9EvdYrY_Wj9DeTtUeYxFMnZ41Us7TfFGgUaHDhQgRPDPo9LTk4N8bbpSn9zyQKbENX--MEJNlltdg-MvsXABWPCmF-J-1oazdTjsOAOYttAHco9tDW6xDICt1v0ppD3cKky4VLvBuF0IWZtdx9c15tev0mSUUJz-N1_jnri4SUwq3E7aNdZgBhAXdJXUPaRWTB9wMsYiBlnQ4SFZtpdzmQqv1UPK2J8Dch9a3eCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bf8e9f37.mp4?token=PKX99IQPoz53hhJlFYIakZb07I_O7yl_PhXZXWbyesKrhPjg2NrFycQsFAvq84suU1UZ8jXbdk-mne_7txiw_I_M02KaunYVeYCK5GE51GvLKi9EvdYrY_Wj9DeTtUeYxFMnZ41Us7TfFGgUaHDhQgRPDPo9LTk4N8bbpSn9zyQKbENX--MEJNlltdg-MvsXABWPCmF-J-1oazdTjsOAOYttAHco9tDW6xDICt1v0ppD3cKky4VLvBuF0IWZtdx9c15tev0mSUUJz-N1_jnri4SUwq3E7aNdZgBhAXdJXUPaRWTB9wMsYiBlnQ4SFZtpdzmQqv1UPK2J8Dch9a3eCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی در برنامۀ سمت خدا: فرعون‌ها با ایجاد مافیا و فساد، راه را بر آدم‌های سالم می‌بندند اما این به معنای شکست نیست
🔹
ملت امام حسین(ع) با ایستادن حول محور ولایت، می‌توانند خشم و ترس مستکبران را برانگیزند.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/455891" target="_blank">📅 18:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZhQ2dxew2MC-5IBEtcTuwwlow24oYdirJ44MbwHU2NR0CuiLtyC8KeSDCp4yYnWIxREUNZzqL42bASdosT8-VpMSo1X2g4a0PauevaJAdo2BmC4H-Vjt5HUrts62wzDvwjSJvvNTl3OdnLz4meFKz9wGEm9JwhjFsGtcgCjp8FsMm3CG55jw_nXxXElYsAr3k1-k4kUOD4c4FjmwQYIscxTfIamN0TC099BP36EuPE8JuEZ9wkCuOlEMnN2ieE_iC4K0_2QyxCC-T_KrkHJeYTWZD11o-i0jbO634zDfCskZ8y2OH2hZUR0_vV6xFZSTmHvSwzViHjNhlOvJtF7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس صداوسیما: تولید رسمی سریال موسی کلیم‌الله این هفته آغاز خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/455890" target="_blank">📅 17:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htuaJlnI40UrjsG0sA_--aybQSOWOmRcb5I8loi1FUR2BpJByDZAPzMIMLeyWGunefzgh0TFqFEpO-h6nZstJ0axutnk4wNzaXzvrg5SBLjb27zCask1LwMK1iJEW0XW4oobS0tfCckLHJuDtAl3zEh0YTmOCseYJxye-2U2kQ-TyLv-wwYa_e7YsRiUDZ3I4FPky7QLoBgnCKzuYsrFGHhWw_0M9DDX_8mpjAkB_xqEYYhE9PuxidLNMpG-IgxD8UmpV3aFt-lvCc58R1r6BOnzc1xjpp-wvGIubupvTmX9o-RGhR6iqPfjg1xcikuX698xsHTwpCsb5HN9vNBghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای عملیات تهاجمی پرقدرت علیه دشمن</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/455889" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455888">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbbm8NQ-cLLvqXijWrf05H8ChWnz0ohyvAHeNdBBRlTMLns5_grgosFDKTYmKt62Q8-K0UP06PJbvIp0DXRfF7JPBsd5NSc9cVxMK3LN63RRZPzs3GhgoHyZ5E8yBKVBpaGYYaO-aPjUrp8DzdWYy3HVtjEV0G9APhdCoPrFtxrYvMODC5FsmnwYewbtW5rqjTO7CR_Q0nPMxQ_jZLhFMfhohtK7sKTC0OvWdGLf-YMVaKyZV0EB9mc1IgnPT_08-DcZWMV7pOi_gJTjPTao2OuB4bFi09upyVVxnQtxYLSSoEFWxdsgzpbnh4XnVheP7mXzPsqi3Wsoh5E7YcT4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای ظریف پای برجام و کنوانسیون خزر
🔹
اگر درنظر بگیریم که نقش طیف اصلاح‌طلبان در برجام و پرونده هسته‌ای‌ ایران تا چه میزان پررنگ است، عمده مسائل مرتبط با کنوانسیون خزر نیز با یک درجه پایین‌تر به این طیف مرتبط است.
🔹
اولین مذاکرات پیرامون تعیین رژیم حقوقی دریای خزر در دولت خاتمی صورت گرفت و نهایتا امضای کنوانسیون اکتائو در دولت روحانی بود. حالا هم که دولت پزشکیان لایحه الحاق ایران به این کنوانسیون را برای تصویب به مجلس فرستاده است.
🔹
اما lمحمدجواد ظریف نقش عمده‌ای در مذاکرات کنوانسیون خزر در اکتائوی قزاقستان داشت و اصلا امضای او به‌عنوان وزیرخارجه پای کنوانسیونی است که به‌تازگی از سوی دولت برای تصویب به مجلس ارسال شده.
🔹
در روزهای اخیر درحالی‌که رسانه‌های عموما اصلاح‌طلب با آب‌وتاب فیلم صحبت‌های ظریف در رد شائبۀ سهم ۵۰ درصدی ایران در دریای خزر را منتشر می‌کنند، خاطرات بد مردم ایران از برجام و آن همه هیاهو برای «هیچ» این تردید را ایجاد کرده که مبادا آش کنوانسیون خزر به همان شوری برجام باشد، کمااینکه آشپز هر دو نیز یکی است!
🖼
اما آیا خاطرات برجام تکرار می‌شود؟
اینجا
بخوانید
عکس: محسن ونایی
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/455888" target="_blank">📅 17:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455887">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1014712f2.mp4?token=MbzQUCzdHYCO8hbE3OMDrWx2sCC7rXJVM1vqe8SOHKdIJn5QV6TqsXCyYF7BNoowQK92rPLje5jyr4rt8_vN2BAWJOuMw48ouj3muvul9e-BGjAZ3HjeEoahk02kF9oPkQPlxdQdXS2wOFvMZnCHfo4PtuHNug5Fa8q73kQ3RRIdx3CLb4458CFgOZdGJE4qzkn-Gm4SgwAX2I7xzUVl_qyxfSo7o5gU96V-_uWHxDF2CfDNYnNH3pXxEqcomZwkXuXF_7QKlc4Wwno_vXAwuesrxoehLo-EmCpl61aU5Hnv6NsPK7YBzfGYn3RkKKHeVDVIxN1fQ1zD4oz_14Qzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1014712f2.mp4?token=MbzQUCzdHYCO8hbE3OMDrWx2sCC7rXJVM1vqe8SOHKdIJn5QV6TqsXCyYF7BNoowQK92rPLje5jyr4rt8_vN2BAWJOuMw48ouj3muvul9e-BGjAZ3HjeEoahk02kF9oPkQPlxdQdXS2wOFvMZnCHfo4PtuHNug5Fa8q73kQ3RRIdx3CLb4458CFgOZdGJE4qzkn-Gm4SgwAX2I7xzUVl_qyxfSo7o5gU96V-_uWHxDF2CfDNYnNH3pXxEqcomZwkXuXF_7QKlc4Wwno_vXAwuesrxoehLo-EmCpl61aU5Hnv6NsPK7YBzfGYn3RkKKHeVDVIxN1fQ1zD4oz_14Qzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در کشتی‌سازی چین
🔹
درپی آتش‌سوزی یک کشتی در کارخانه کشتی‌سازی شهر فوان در استان فوجیان چین، انفجار شدیدی رخ داد که تاکنون دست‌کم ۱۰ زخمی بر جای گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/455887" target="_blank">📅 17:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455886">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc4OaqNGE0oqyCeWTVa0E3CPiF8YNufaDliWb7YUREYYkHFxk5KZ5GgoyaVQ8kk0jcNCZRSgim9or_Id04qgW3opA7LhtXwVXnr9pRYqYRyx4mAfvm7hDYgluc0QnuG0SxZ-y3s04cP7xX6sDvKQaflMILssE4XgodhumJOsYLQ0KcDg6Cs59rVZn6wESKSXVfFESAHLsJ2Bk_LsIRYd1k_Q_CyxSvbSZQCefNx5BiGqmFe2QwC38LqlXY2u3xjvjXyV1f8zaH5zVt9mOFam6sH1VCc9VYxKfYqLMcGt3B9-Iv3LkuYF39g_8u4KWEVKY4wHuh_02zbgszJVp1OPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش الحدث از ضربات انصارالله به مزدوران سعودی
🔹
شبکهٔ سعودی الحدث: درجریان عملیات امروز انصارالله در منطقهٔ العبر، ۲ نفر کشته و ۱۵ نفر زخمی شدند.
🔸
پیش از این نیز یک منبع امنیتی یمنی امروز گزارش داده بود که درگیری میان نیروی دریایی وابسته به دولت مستعفی یمن و شناورهای انفجاری انصارالله در ساحل غربی رخ داده که منجر به انفجار ۲ شناور شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/455886" target="_blank">📅 17:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jv7obRQUNE-ifk8fPswHuk6BY0wivss2TLMt3ZuNoKa1oqLUUIibJ3p3fm-q4l_mrqxtlMbxdBDWk-NpA4AsLcZMLRCU4tzqH33fxeS5s3IRIu4UWjLyceZaQKgcYMR33VDuByWhiLXvvRR2T_5S6ihzjLyJKL4gyCxnCM5nhCSgUfs8kvObn-2pXSEqpJpD1lh9I35ElfFCUhqH39slo6NtKyi5NetbskehrpZBrp7BFwV5L1WdFqDEbEzFs3ddDJMHXDa1_FuJjNUXM-cSkDoKlLuZ8eHtUXx4R5MxwjuhZye43jWapgWZLg-Y4PWVp34rdi6wMEXHVjDGKZjnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Piu6md5zE56KoyW_8AlTqtfXDphFXo5mrXbQcSzgg9Hc80zDbEBWQ3B3ZJ7rWbeBsdQ3oxcTZDPPdgCBaQOeyuAn_z5kJavQaLI5unEdCgDAdQYcDM19P-Ps_3Yb7oDJY5Xy9mM5dNU0mXONZhSDWe5WJPfDsHg0EtB_D_fKv1TrI9LMOyUarglB6jgF1ncJFuvU3cXwL22qHozOl57zVaEAzRnuCikhI-noSiw_CS9EPyx0PPZwENmz5PbuFiIGCdJ7Chr4KjuJD0q9psGG3iORRlbs-tSbXkSeD7Agr39EuBZzymdzV8UORmfPvbOP4IgubJhPB1LVOuGavVsSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMR4KpKNrk49EQ-hlUPFjAcxh_rtUbOsBnho3X5Cn8xe5LJ4F8st5mnmRKlNtDu99bGHlCT7aQ0_C-Ua4QmzPZ2mf_Sx--1fEuTmnDPdVpxWNRYgvotuPITEDEQr0VGUt2fLyDM7AG8y5tK5CcfGoM4G20eAB1dr3JV5G20jeNjiDrwx1b_RLNpsOOWqe9agkmj8UcID8JpXi8NQyc9Jv_h97x-Qjdu8Jc0GCVo15EPelDB8y8NaIkxEhu_DmfvYV2It3TZPjz2ITgLd_85mIBsG6SLYjmryclEz8B5sqyR2Iuv7sPzgnyBjUtSIG3o2yebAkN1SLCIjOxK6u7PGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxXtoeJNn7hpbroLtzqRMThbfVL_OWC2rUaYpZTCsEV7FOG3vD9zKLP_0nkI7jSVs5J3yhjoUi2oUegGCNLNzl2BiPLtvbLs9HYLJrlH707RU7ChjrHGOTMFzDUjAkJETinaREq_7nJitZqE69H41NLXv-Qwm7OXxhsCSwHei9AmrSyu4LtQRrnER75WIS7zyi-ZLryPppmPisSjOCzPZVPkh-SowDu0zTRiVVxgeecgXim6Y-wtmQ5l77xk9Xj7QZD0wO_PtfF5kEXOh48updrUzHgQ_uu-iEVDqx9C-qx8cAtUgH0aaV7q-LyfZX0CCvPr5bDD1WaHFolMuHlq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRe3qyu7m1c-p1jyomy8F9z_dHIbh5xt77lP0id374157fAcPb-t07JENmTirtPRR5jQhdEvopZk9KZlrpNWmQC4wi2gWVGLOuWGHrxZDcsDZIueiuwhLGM91QQuaO1WTZMh33vEB5keb3p7qe44QPYEdd_gep3hCl3xZLfW-s34Unhj0CvsDhYsgriOwjarMnHqoGzRhgJZS2QfwcOout71UJIf_pitg5MC1WAz4GgI2CU7rKHB1he3lSJBCmvNOPWiN2qGKv6KSQm66oJ00c6MKuUvvo-9NWmxB-vJZ0dzVMUjq1tYucEfjbO33AXp9cTsn9L0SZFeDYVVXmJjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cx0y7_-FaTgd92kDhY2cRxJyG3R5Wyy1zqBIx7Eeqtnoqhitt6dJjy_tGLilyxNhih4cfYbSjpQp2QrVbrUltbbBQtQ2S2-XCIsyj7A9f3IwX72WxLAWfLe3upKZhEsV-Q6F3D286I-_1VLpSnjSrAalakjd0BDqJPaKmeQig7bhsRBLfjNJuxplK2jmEjyvnjr2j_BTcC4jEzwY5ZnGDszmj9cmBIG_XDGnBYAbWjfBfGZDQlZe54N6_wDUeFuLAuT-gqshPEHaT1ecKDmYAlS2SV55drxTwF_Uxkfdo3tN_C0d5WoFX6Q89HLCRP2HTjy03FUMb_TzuGN5u3qbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krow-iIheicwE84P7b0HbUI-Izuec_ZuvKw1PXgFWEyqsbjuTilpwuQhCG6lWVBzFv09iEbcy9HzcGmcXCT-cZUKJMJUYA-u7DnVKBFHu_1zkR6OrphvwH0e9Okr9Uh3sl8-_gtONHYrOunyvsINdLBEfOuN1xR_PomrROziblYsEe7Mi19AV-gAaJlpD6qL1Bd8gbqm7YuFx1kW8NctJBCFeUTnLfkwJd6Zv9bSaQ8VYp2md59_cMmZCapCRV3qhWx5wFKpE8-Bb2ngPvQdFIsV_0HP61bXF-24IXNBv7deWmkOpXczKn9YPRgZuehxhtk6CG2zzEga59DRvykZmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
این‌جا تبرک‌خانهٔ امام‌ رضاست
عکس:
ایمان جنتی و محمدجواد مشهدی
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/455879" target="_blank">📅 16:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704533da75.mp4?token=QJx46blTSviSR5fAvZhphPls6N_QxoddXSJqgyN3X5m8ACr92LOTTOo1mKlf16JXlQgt3IFqZothRGaCnDEkeCPwTQX0TkCSYZOnSGKynlgnFDK2aNxFRd8PiA7Ubv9ogYiPpqo5F16Sv39VP6l0tRIsjuRLew5kmiMOk1Vl0_CslvzSo0e5VwY-WCMgYb8fTIho1-OJ479xzTB00kKAu0LoqGy_0VxHAZKHNTTtpHSLWrzRdwIPqHGWq52j79g5pkNHNFOQYcaX7OPg-inqx9IAr_CZU3kpyhODI4MuzqEekc5SR5D-B4UtMImEsNzcDaHkpSP7V9P-W4hyzK7IwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704533da75.mp4?token=QJx46blTSviSR5fAvZhphPls6N_QxoddXSJqgyN3X5m8ACr92LOTTOo1mKlf16JXlQgt3IFqZothRGaCnDEkeCPwTQX0TkCSYZOnSGKynlgnFDK2aNxFRd8PiA7Ubv9ogYiPpqo5F16Sv39VP6l0tRIsjuRLew5kmiMOk1Vl0_CslvzSo0e5VwY-WCMgYb8fTIho1-OJ479xzTB00kKAu0LoqGy_0VxHAZKHNTTtpHSLWrzRdwIPqHGWq52j79g5pkNHNFOQYcaX7OPg-inqx9IAr_CZU3kpyhODI4MuzqEekc5SR5D-B4UtMImEsNzcDaHkpSP7V9P-W4hyzK7IwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقام پیشین آمریکایی: در بن‌بست ایران گیر افتاده‌ایم
🔹
مقام پیشین وزارت خارجه آمریکا تاکید کرده که رئیس‌جمهور این کشور گزینه‌های مناسبی در قبال ایران ندارد و در یک «بن‌بست» گیر افتاده است.
🔹
«هدر کانلی» عضو ارشد مؤسسه امریکن اینترپرایز و معاون پیشین وزیر خارجه آمریکا در امور اروپا و اوراسیا که با شبکه بلومبرگ گفت‌وگو می‌کرد، در پاسخ به این پرسش که با مواضع متناقض ترامپ درباره مذاکره و همزمان مطالبه امتیاز برای آمریکایی‌های کشته‌شده چه باید کرد و روند کنونی در چه مرحله‌ای قرار دارد، گفت: «ما گیر کرده‌ایم. در دو هفته گذشته در همین وضعیت گیر کرده‌ایم. رئیس‌جمهور گزینه‌های خوبی ندارد.»
🔗
شرح کامل این گفت‌وگو را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/455878" target="_blank">📅 16:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455877">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d4ebc018.mp4?token=lwIqZtxJMLmf_L8eVjhryp-7wpnvtHGf6OBtXVp4SAy8-b5m-UyQ9b10HPlVIdpmkdpe1kVBuPKJfwX1ou7DnTEaPW81o6Lsd0hYIvcbP91sIj0dl-XvduUHXWFYDXLv0UoFFceAcGmRmlhDHA_ogtpCH1AL8q2y8Id3jDfOqJtoI9YTIIszQW1HkeeYM5feU0pkj81Br05sYwpIoYjHBPNIxDwBboxD-aeRTa1XDwtc9vwbECJJw7iwMfpteLn6WjG0XurThtMjcARWTMHNU5M4jk5ixahcynMkZtDBvTApXN0cyOoP8pzSbVXX2LBMdnYlE7vBdS9wnFWuLnQwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d4ebc018.mp4?token=lwIqZtxJMLmf_L8eVjhryp-7wpnvtHGf6OBtXVp4SAy8-b5m-UyQ9b10HPlVIdpmkdpe1kVBuPKJfwX1ou7DnTEaPW81o6Lsd0hYIvcbP91sIj0dl-XvduUHXWFYDXLv0UoFFceAcGmRmlhDHA_ogtpCH1AL8q2y8Id3jDfOqJtoI9YTIIszQW1HkeeYM5feU0pkj81Br05sYwpIoYjHBPNIxDwBboxD-aeRTa1XDwtc9vwbECJJw7iwMfpteLn6WjG0XurThtMjcARWTMHNU5M4jk5ixahcynMkZtDBvTApXN0cyOoP8pzSbVXX2LBMdnYlE7vBdS9wnFWuLnQwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانه‌های ضدانقلاب آب‌بندی شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/455877" target="_blank">📅 16:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
یک شهید در حملهٔ پهپادی اسرائیل به غزه
🔹
منابع خبری گزارش دادند اسرائیل یک خودرو را در منطقهٔ «الشیخ عجلین» در جنوب غرب شهر غزه هدف قرار داد که در این حمله یک نفر شهید و چند نفر دیگر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/455876" target="_blank">📅 16:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff3c4526a.mp4?token=Kr8U8QRDdqpSlmQRYMegLOD-9b6Bk2TMot1qT2-gUeFcEbKIG-w-lLUb7bd14YbTiL9301mR4t3Ga9qDg-gQLLXzUqMkJPQy7LWK2WLLQ1LXD-y-mjBcEsqDIjkm3LbH8qJn5s9LmelHVuhV6fkTsNjtDWIWEG1AN0EKoPXkd7HNm6DjGiEQ4iGsvix9mrBKw_Pf3VYls9zABfIC0H9z3SgLBryzIqGwDOdbhwjCSgt7XHL6hD3WE4Jl8R-bnGUHKKkC3tLvZiiDrsSj5aI-EONuqdFo-ZcTODocXYQFJ0rCVJCWYxZZrqdS6Hvwv0s_I5Xx6P5F0eGyVoArAB1d-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff3c4526a.mp4?token=Kr8U8QRDdqpSlmQRYMegLOD-9b6Bk2TMot1qT2-gUeFcEbKIG-w-lLUb7bd14YbTiL9301mR4t3Ga9qDg-gQLLXzUqMkJPQy7LWK2WLLQ1LXD-y-mjBcEsqDIjkm3LbH8qJn5s9LmelHVuhV6fkTsNjtDWIWEG1AN0EKoPXkd7HNm6DjGiEQ4iGsvix9mrBKw_Pf3VYls9zABfIC0H9z3SgLBryzIqGwDOdbhwjCSgt7XHL6hD3WE4Jl8R-bnGUHKKkC3tLvZiiDrsSj5aI-EONuqdFo-ZcTODocXYQFJ0rCVJCWYxZZrqdS6Hvwv0s_I5Xx6P5F0eGyVoArAB1d-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طعمه کردن خبرنگاران در ماجرای فرار ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/455875" target="_blank">📅 16:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جاده چالوس و آزادراه تهران-شمال یک طرفه شد
🔹
مدیرکل راهداری البرز: تردد کلیهٔ وسایل نقلیه در جاده چالوس و آزادراه تهران – شمال مسیر (جنوب به شمال) تا اطلاع بعدی ممنوع است.
🔹
ترافیک در جاده چالوس مسیر (جنوب به شمال) حدفاصل بیلقان تا پورکان و مسیر (شمال به جنوب ) حدفاصل ماسال تا مکارود سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/455874" target="_blank">📅 16:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc49227da.mp4?token=QIBKbwOasiOaCxUYr_clj8bzdo1Gs-VmhXql7RvB6h7niYu4RBUftOiWmfXo4-XJcVhQ2vu6mrBA9Lgsf6skpoCnDQL5FNHkahqzztCz9aRG3fr3-9XtlgDDOAVPb-A8rCgqqoLkoefkorzu_xMgo3SAk0iY6i_U0JQDyn1JM5zM-CFY3oFlNC5LiR0bt_cG6wnbHBxMVpRtm-uyZ5vsduU--IBdVZ8NTynJDFOhbSJeCK0DPfhZ1pfg-xA39t1FR9gkZUlwEKR92KCTFBNAahIMpCzoUoerR3LhjlDotjDv_RrQbEI1fmdzwINsAVaRembMVt9PBePDQfIQIdntKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc49227da.mp4?token=QIBKbwOasiOaCxUYr_clj8bzdo1Gs-VmhXql7RvB6h7niYu4RBUftOiWmfXo4-XJcVhQ2vu6mrBA9Lgsf6skpoCnDQL5FNHkahqzztCz9aRG3fr3-9XtlgDDOAVPb-A8rCgqqoLkoefkorzu_xMgo3SAk0iY6i_U0JQDyn1JM5zM-CFY3oFlNC5LiR0bt_cG6wnbHBxMVpRtm-uyZ5vsduU--IBdVZ8NTynJDFOhbSJeCK0DPfhZ1pfg-xA39t1FR9gkZUlwEKR92KCTFBNAahIMpCzoUoerR3LhjlDotjDv_RrQbEI1fmdzwINsAVaRembMVt9PBePDQfIQIdntKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هت‌تریک طلایی وزنه‌بردار ایرانی با شکستن رکورد دنیا
🔹
حمیدرضا زارعی، ملی‌پوش وزنه‌برداری کشورمان در دستهٔ ۹۵ کیلوگرم جوانان، در رقابت‌های قهرمانی آسیا در کسب طلا هت‌تریک کرد و رکورد دنیا را شکست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/455873" target="_blank">📅 16:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e9fda238.mp4?token=IMAr14nGiHP9C75Zvg5K-CiVgKUmGhFh8Fk87_ov7MPrwVOR5z5WeVCPM3lnE5Q9KggQf8W9ejd-rxzfWI85jb4jfDZYsCXHnezIJSA0KjAZ0yeuNq3xo4dey2Eu-gYkkfHxByROE6-UxXDWeJpQiDFM_kO4d6Jyoqjk2S7eWuPHrLUpsj3hUdsNOMl8rxv7xy1F71ThdiTWdHlNrfhFkv790yLkkhoTHKRhwZW7RGfK1gI6CM3I3lC-76aLyfQK2L-yTfX4M9K4I9u30d5fPWexF2GA7ZnWGfz7cu-X3Y6_lh1oJqjZkFM0bi0R1EHKr8Kn9vHX-Q0aYp7GkaWGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e9fda238.mp4?token=IMAr14nGiHP9C75Zvg5K-CiVgKUmGhFh8Fk87_ov7MPrwVOR5z5WeVCPM3lnE5Q9KggQf8W9ejd-rxzfWI85jb4jfDZYsCXHnezIJSA0KjAZ0yeuNq3xo4dey2Eu-gYkkfHxByROE6-UxXDWeJpQiDFM_kO4d6Jyoqjk2S7eWuPHrLUpsj3hUdsNOMl8rxv7xy1F71ThdiTWdHlNrfhFkv790yLkkhoTHKRhwZW7RGfK1gI6CM3I3lC-76aLyfQK2L-yTfX4M9K4I9u30d5fPWexF2GA7ZnWGfz7cu-X3Y6_lh1oJqjZkFM0bi0R1EHKr8Kn9vHX-Q0aYp7GkaWGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان وظیفهٔ فراجا: مهلت مشمولان فارغ‌التحصیل غیرغایب برای شرکت در آزمون سراسری تا پایان آبان تمدید شد
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/455872" target="_blank">📅 15:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b50fef7d.mp4?token=s8DeTrwmBkJycR2ltG0AylWKH3FktgT2peTDhkeIZN26-A1iQVErFjLNz-ExndDyDhYhJhNP1GIlc17S85eo0GAkZTwE3B1MSULv0gbqPx1ZPZx90cno4LapXzsojvOEsAg8zzJ-atmq4BsPj8llqC2wjscs4edexePwHqFYMrHO6t-6UzYSMrIBlJVrTN1KK-4rDpgbiBF_C9f9GEaOLxQOz0ZzYpRmGuIBWU8rpwH1iadmkoi8G9r1BUN3Yq-OD24c7t43tc9MWBlqtV0Ws1YeUQkMeUeJvU_R9Mg_jUgbf2xqrKVnZP8h1bCAzley0QJx1oFc-zUOmCdIoD_Zwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b50fef7d.mp4?token=s8DeTrwmBkJycR2ltG0AylWKH3FktgT2peTDhkeIZN26-A1iQVErFjLNz-ExndDyDhYhJhNP1GIlc17S85eo0GAkZTwE3B1MSULv0gbqPx1ZPZx90cno4LapXzsojvOEsAg8zzJ-atmq4BsPj8llqC2wjscs4edexePwHqFYMrHO6t-6UzYSMrIBlJVrTN1KK-4rDpgbiBF_C9f9GEaOLxQOz0ZzYpRmGuIBWU8rpwH1iadmkoi8G9r1BUN3Yq-OD24c7t43tc9MWBlqtV0Ws1YeUQkMeUeJvU_R9Mg_jUgbf2xqrKVnZP8h1bCAzley0QJx1oFc-zUOmCdIoD_Zwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: هیچ کشتی بدون اجازهٔ ایران امکان تردد از تنگهٔ هرمز را ندارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/455871" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpDJEZCkY8Xpg-5l65GWNzUTkScuPsqA505nvUCrYG8rSQyAEH8fkKgVk2m87XD6KKirk7fYrJuJ2Ms8eTQVTy6imZSNrOjyCO8DE7JmJF13uoTuueiFNae0cdl7961Q5p27kK9MUfYdzpHxNcCxYslgKDDq61-pAA1Ckw20xFMYYynJ3bK-FNyDUqzvy40ovJNYXF70Vv_mEFC_QETErCDGIWyww7SvbXYvWrLiOlX3svklajPUTcNBEPq4AI3Pbm-F2D9i4y2JBrPdjW4GO6YgWbrT4pg9uZcsXWvptijIqzTod1tC7V3tIIk_kDeCAWVPqSZPEp7aglHJTIhWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دلنوشتهٔ خاص مهران غفوریان؛ خوشحالم زادهٔ خاکی هستم که امام رضا دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/455870" target="_blank">📅 15:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67b734a3e.mp4?token=JIptjvU3G8LgMFBWRNF_IJ-XlnMUcFUKFxZvKuBq0Gz_8FMQmOnPA78CRQHVJfNjWfC_57_Jn6hG5wnUtoLEgKbpuY3kDVKMz204Qk874qIihb4ey5QU5lMYm2Sj_cYDZo9qeCbvuoZUz22BCAZ0QOBc6WHNSbsgDMEPWyS993RuKbM8Sx9MOqsoeGBLtniYfrwd-NO8kl2Gz8FHlmmjfSzZg6Ou0vfOYHxoDI2plRLTRXM7UcMnfw2o6PSmgP7bk7kV0sbDZMipwLa3atdkkZDgSpQqyBb02wpvbpB-fKs73v6ZoFz6kJN2ydDQZFPevAA-RuS-L-Z8lUplO26EZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67b734a3e.mp4?token=JIptjvU3G8LgMFBWRNF_IJ-XlnMUcFUKFxZvKuBq0Gz_8FMQmOnPA78CRQHVJfNjWfC_57_Jn6hG5wnUtoLEgKbpuY3kDVKMz204Qk874qIihb4ey5QU5lMYm2Sj_cYDZo9qeCbvuoZUz22BCAZ0QOBc6WHNSbsgDMEPWyS993RuKbM8Sx9MOqsoeGBLtniYfrwd-NO8kl2Gz8FHlmmjfSzZg6Ou0vfOYHxoDI2plRLTRXM7UcMnfw2o6PSmgP7bk7kV0sbDZMipwLa3atdkkZDgSpQqyBb02wpvbpB-fKs73v6ZoFz6kJN2ydDQZFPevAA-RuS-L-Z8lUplO26EZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعا مدارس امسال با رنگ‌وبوی عشق به رهبر شهید آغاز می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/455869" target="_blank">📅 15:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOuMnBg40yypmuYrUaGeLr7bB_5FCUSoErFTuXXVVLatq7F4LhH9eT34E4meW6_sw0E6zM5CajWj4PhQNdHqTeKmgZrn7BRiG30QUT-Aj0emgGvCH_95msuvOVIaMSJ8WDtZfOrPsEV4C1LW6qCMWbbr5PsqGi2j8F4OJaI0iMdI-cY5EPA8ynP1pL0OSmiyXwDTYzF_KSPduqIjOGD3W4KMk4K87E3JJmbciq_o7w8BDRPQrAw4U_TKuPmV8i_8SNurH6TTxunnSMSk2PBpaUMZPtUQ2QpoTOedLcz2pVGTr3BxU0L_o4zB_YE50SVjI1X4TjLHntHbVuktFUnthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکسازی آلودگی نفتی قشم به مراحل پایانی رسید
🔹
مدیرکل حفاظت محیط زیست هرمزگان:  آلودگی نفتی دریایی و ساحلی در برخی نقاط جزیرهٔ قشم مدیریت شده و عملیات جمع‌آوری آلودگی‌ها اکنون در مراحل نهایی قرار دارد.
🔹
با تلاش نیروهای حاضر در منطقه، آلودگی‌های مشاهده‌شده در جنوب جزیرهٔ قشم تا غروب روز چهارشنبه تقریباً به‌طور کامل جمع‌آوری شد و بخش قابل توجهی از سواحل آلوده پاکسازی شده است.
🔹
پایش سواحل و مناطق دریایی همچنان ادامه دارد تا در صورت مشاهده لکه‌ها یا بقایای نفتی، اقدامات لازم برای جمع‌آوری و پاکسازی آنها انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/455868" target="_blank">📅 15:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سفر هیأت امنیتی بلندپایهٔ عراق به عربستان سعودی
🔹
بغداد الیوم: یک هیأت بلندپایه امنیتی عراق به ریاست رئیس دفتر فرماندهٔ کل نیروهای مسلح، به منظور بررسی شماری از پرونده‌های امنیتی و موضوعات مشترک وارد عربستان سعودی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/455867" target="_blank">📅 15:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455866">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
کارشناس بین‌الملل: تصویب لایحه خزر به تمامیت ارضی کشور خدشه وارد می‌کند
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/455866" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d921022c6b.mp4?token=bn-D8hgVUzx4mNg6rtFTTi0MGmmRDq3cuOFcuDigGKI5k7ftNVzoGa8y3yVHVrphQmAj-7fB9UpBl_sDPu2_U3bIVwg2bbQGbdx_D_xeKiJ1kw_D_ptvhaQe9e1k6esPS2pApLWYR2n6PirZUezlPNUynnnQ4LNur5ue33I9uqTqIpMT7goWTLzypD-TfsXVCDcZm3bKB_vGXL3ZY-n71fu47m5ekHVQKj90VMtBVxowRi_HWSSOPF-D-VqMO63gGYIxRL71S8YUk37VF4dalr0ObhD3Y58QGuI2tz_vO1MHyydQbzPrXOk0kJMk_MzFQjGGAqg-_5EMZ5bBTymVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d921022c6b.mp4?token=bn-D8hgVUzx4mNg6rtFTTi0MGmmRDq3cuOFcuDigGKI5k7ftNVzoGa8y3yVHVrphQmAj-7fB9UpBl_sDPu2_U3bIVwg2bbQGbdx_D_xeKiJ1kw_D_ptvhaQe9e1k6esPS2pApLWYR2n6PirZUezlPNUynnnQ4LNur5ue33I9uqTqIpMT7goWTLzypD-TfsXVCDcZm3bKB_vGXL3ZY-n71fu47m5ekHVQKj90VMtBVxowRi_HWSSOPF-D-VqMO63gGYIxRL71S8YUk37VF4dalr0ObhD3Y58QGuI2tz_vO1MHyydQbzPrXOk0kJMk_MzFQjGGAqg-_5EMZ5bBTymVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم شاهچراغ(ع) در سوگ برادر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/455865" target="_blank">📅 15:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e9ad1f54.mp4?token=Mo7Dxt0vtYWLbeaNnu2B8jk0MBNSWTv_5TFFlyALB8TZmMEAvkxrqzDdqj0qvrMOU7l6p8WSSm92EcMM3ip5B3NGNSA-5_KjYin7xmf5v92ZybeMNzmCiwNf1fpg_VS2-HuTe18LlnVR1JICK6-tyFDAthcX_WO8huL9aw2qo_7HMOgq0uqDLheZ3W09wASZugGCZP5o1dVJE1dBfXe0JVCcbttiBsdajIhbyAxlAClew-48vxv8omLpzfdEffUegykSE7_NdDUkimuFsrIty2KvKLAKg9x0inavJMvjekF1yeQ7wQjzKv5vY22oKu2jOUvzgYmfMwafkniTr7yclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e9ad1f54.mp4?token=Mo7Dxt0vtYWLbeaNnu2B8jk0MBNSWTv_5TFFlyALB8TZmMEAvkxrqzDdqj0qvrMOU7l6p8WSSm92EcMM3ip5B3NGNSA-5_KjYin7xmf5v92ZybeMNzmCiwNf1fpg_VS2-HuTe18LlnVR1JICK6-tyFDAthcX_WO8huL9aw2qo_7HMOgq0uqDLheZ3W09wASZugGCZP5o1dVJE1dBfXe0JVCcbttiBsdajIhbyAxlAClew-48vxv8omLpzfdEffUegykSE7_NdDUkimuFsrIty2KvKLAKg9x0inavJMvjekF1yeQ7wQjzKv5vY22oKu2jOUvzgYmfMwafkniTr7yclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهدید صریح وزیر جنگ آمریکا: حملهٔ نظامی به کوبا روی میز است
🔹
پیت هگزث: اگر کوبا مطابق با ارادهٔ آمریکا پیش نرود، از گزینهٔ نظامی علیه این کشور استفاده خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/455864" target="_blank">📅 14:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8843ee8d8.mp4?token=ODj-sg_WmfnxejxjvIOPds0Z_x6IDT_j57ynnXvG0wWmCdDuTUIguOrR83lG3Z4IBpNXDSugqrqFCPaL1H1Xf6_pMH1SpZuoRzvhMAZr70VQ66m0cCDvW-wbM1a_sPjHVzktM7vybuixte3BcGe6qME9eTr6s3v6TrcVb57GDxNLTCh4CY1TwE2Ry3uuLSLlOAxgCLqKxBrGUToU294ruOfnLpCOAdGG38MSn3hDYaPAKqDI_fGinqqmHslPiyzT1df5aNx2fxLw_XT7YSrZEFuxWXk6K1y8IWF7EHxpkLECZ8ErWe2ZFblV54JVMBfiNZXPzWrBYodf1JDg2Mfm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8843ee8d8.mp4?token=ODj-sg_WmfnxejxjvIOPds0Z_x6IDT_j57ynnXvG0wWmCdDuTUIguOrR83lG3Z4IBpNXDSugqrqFCPaL1H1Xf6_pMH1SpZuoRzvhMAZr70VQ66m0cCDvW-wbM1a_sPjHVzktM7vybuixte3BcGe6qME9eTr6s3v6TrcVb57GDxNLTCh4CY1TwE2Ry3uuLSLlOAxgCLqKxBrGUToU294ruOfnLpCOAdGG38MSn3hDYaPAKqDI_fGinqqmHslPiyzT1df5aNx2fxLw_XT7YSrZEFuxWXk6K1y8IWF7EHxpkLECZ8ErWe2ZFblV54JVMBfiNZXPzWrBYodf1JDg2Mfm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: شهید نائینی سنگر فرهنگ را به سنگر جنگ گره زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/455862" target="_blank">📅 14:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e8c1f37a.mp4?token=kx5SWWCYPRx7vFrggRicUY_FOg2yI43wZsfjo6gQiSRoxDPJ0T2yU7Q-XntNA5tJHsRG7TxiHUpoOEDRbPElUysQybLaOcZTMRNgb_o2Bx9foKChwIyhXELFl_vQg1oYFJUgw0PXBHWguWWvU2bajjNWDlBB_U1QSz6-1E50081rXFPBgdN-wEOmusLHdmI940aKt50lneLk2hZU_rMhQg63ByQ3SqmdpA6z_HF7WRYQD1vf29o7kuajLyGO5iU0tK466LkLqXtxejw6g5iI5eLSt_saMORq7yQrd0nLLbMfTK0hwZPzEFZO2q7nNCSYClqns3YGz4jcCNypilrRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e8c1f37a.mp4?token=kx5SWWCYPRx7vFrggRicUY_FOg2yI43wZsfjo6gQiSRoxDPJ0T2yU7Q-XntNA5tJHsRG7TxiHUpoOEDRbPElUysQybLaOcZTMRNgb_o2Bx9foKChwIyhXELFl_vQg1oYFJUgw0PXBHWguWWvU2bajjNWDlBB_U1QSz6-1E50081rXFPBgdN-wEOmusLHdmI940aKt50lneLk2hZU_rMhQg63ByQ3SqmdpA6z_HF7WRYQD1vf29o7kuajLyGO5iU0tK466LkLqXtxejw6g5iI5eLSt_saMORq7yQrd0nLLbMfTK0hwZPzEFZO2q7nNCSYClqns3YGz4jcCNypilrRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آهویی که سپیده دم شهادت امام‌رضا(ع) به خانهٔ یک روستایی پناه آورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/455861" target="_blank">📅 14:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
تیزر مستند «دیدار آخر»
🔹
مستند «دیدار آخر» به تهیه کنندگی و کارگردانی هادی نعمت‌اللهی و محصول مرکز مستند سوره به روایت تشییع آقای شهید ایران در تهران می‌پردازد.
پنجشنبه ۲۲ مرداد
ساعت ۲۲:۳۰ شبکه دو سیما</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/455860" target="_blank">📅 14:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/455859" target="_blank">📅 14:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455858">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/455858" target="_blank">📅 14:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxVjt2GYknQCTfLNT6W8ATpSOuIzw48AtFjWRM5xpyQqlh02KNPNOunMkgmVpwK8qm0W_H0kdNoxhZ0nm0j96qpyE9M9FLrJCMqRCOjgcw8WGR-w4WtQIKyf2FGWB7OJRK0wDrkAUp74-YUgDg-fDRPqpOIFbRzCDARE84JAL9eB7OplnZAsJ_o3Ln1jHvNPvSRbRRFr4iceTYU76HPFs4ir_79uGYwZpJHh8hD0SAJYZE7tuFXHlz5loUVGxIZzocNL8oI_EqFnoSFyRT611t1bsJiCloCzQ_ySpByin6d5JRHEvM9kpZ-yIpojU_lKqEY7wRCqyJ1Mo57MBcVEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس حساب سخنگوی نیروهای مسلح یمن را بست
🔹
پلتفرم آمریکایی ایکس، حساب سرتیپ یحیی سریع را مسدود کرد تا شاید بتواند صدای عملیات‌های پیشدستانه انصارالله در معادله «محاصره در برابر محاصره» را خاموش کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455857" target="_blank">📅 14:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455856">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37df6d9d9b.mp4?token=l-h8e_3VMKeGjdV6Bi-Axwdy06MYAtfP_0LHhx4W7raktSogAbyh7yKL0u-0N_hMyi66Kheh9RGKs8lpBsb5FBQ0wQcWEs9oSqOYckSFOJaM7sXqJMR-EJhMRUqMexRDVP-NfKTpPdutgTVNzCcKXU8fPfu86vFUOKuXCqZRfHpTuI4wq9PaNIGEtMqDTgn5uoelAMXgB-7J_P_C8ZdvElOZdarr9T2571vlGGwZS59pNiR1CyyJZ9vnCHXL255iOoLIe2iwlVhHygTpXPhM_N_l5j471rB76f0ZoaRTDdcW9qmljUp7GZ15kv1LSVuW4-_72lwCaLD-RMD46emyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37df6d9d9b.mp4?token=l-h8e_3VMKeGjdV6Bi-Axwdy06MYAtfP_0LHhx4W7raktSogAbyh7yKL0u-0N_hMyi66Kheh9RGKs8lpBsb5FBQ0wQcWEs9oSqOYckSFOJaM7sXqJMR-EJhMRUqMexRDVP-NfKTpPdutgTVNzCcKXU8fPfu86vFUOKuXCqZRfHpTuI4wq9PaNIGEtMqDTgn5uoelAMXgB-7J_P_C8ZdvElOZdarr9T2571vlGGwZS59pNiR1CyyJZ9vnCHXL255iOoLIe2iwlVhHygTpXPhM_N_l5j471rB76f0ZoaRTDdcW9qmljUp7GZ15kv1LSVuW4-_72lwCaLD-RMD46emyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک باند ۴ نفرهٔ سازمان یافته</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/455856" target="_blank">📅 14:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455855">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ec95bfe2.mp4?token=cAt3KdtjFDQ6EQM1viGqd0InClDwB_bEzrcwKC3vyFoNUKVutdYExaxPCBc4LguaqK8-skSvCwr8GEdazGbNAv4jyBVwTzCXHHpp68-SIB1zS4oux1T977r7V8AyaW3GINh2eOuGt8cCG4BUflR4GISTbvHRN-0TLuYKoeCxZiqL0cHm04GUMLzMAa3SCB55ZiioUI_wUYakdIfxHxHPK1IJcso96iDvnUrKpEds_lV0eACu2fCKY046AZMhrV9fbw3HZm3F4Truu3hHxJMRsYPSt-ZKfzsuMhmq1sJJHrANj7NchT0w66yUsR7noH08dlk-_902mjwpKLcOEQHSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ec95bfe2.mp4?token=cAt3KdtjFDQ6EQM1viGqd0InClDwB_bEzrcwKC3vyFoNUKVutdYExaxPCBc4LguaqK8-skSvCwr8GEdazGbNAv4jyBVwTzCXHHpp68-SIB1zS4oux1T977r7V8AyaW3GINh2eOuGt8cCG4BUflR4GISTbvHRN-0TLuYKoeCxZiqL0cHm04GUMLzMAa3SCB55ZiioUI_wUYakdIfxHxHPK1IJcso96iDvnUrKpEds_lV0eACu2fCKY046AZMhrV9fbw3HZm3F4Truu3hHxJMRsYPSt-ZKfzsuMhmq1sJJHrANj7NchT0w66yUsR7noH08dlk-_902mjwpKLcOEQHSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری خیابانی آستارایی‌ها در سالروز شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/455855" target="_blank">📅 14:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455854">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceefa4e9f.mp4?token=MzjfkLMiMZWxxwQ4RsC8hiE0nXNM0lvtZy0URXAYYUZM6JWWrsL2b6JjBr_xV-w_QBoKQMO5NR14wDsyukUr8zsGhfLb-Hb1DA4jdinLo50ZaRq8BQsvow6esa32Wlc7Typn7dUE5gjXpOEYJXRkf88CSyJYkQ0lJQ23zmK1Bf-oeSICCzi8Sr_vApFHBBxS5Z5JRSBl8oo-TWRTEhbKOXCZ_Vq0sD0GPEr5yL63UEHvsgclARQp-Dnp80nUycvSYAZOLKZZp605Bs6KcP_drXr1K8kjTqG1oBpfefZagz0gLqdJ1zZ6jDhoHdBLbaSrp6hBX5btTLwc46-7sjFyvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceefa4e9f.mp4?token=MzjfkLMiMZWxxwQ4RsC8hiE0nXNM0lvtZy0URXAYYUZM6JWWrsL2b6JjBr_xV-w_QBoKQMO5NR14wDsyukUr8zsGhfLb-Hb1DA4jdinLo50ZaRq8BQsvow6esa32Wlc7Typn7dUE5gjXpOEYJXRkf88CSyJYkQ0lJQ23zmK1Bf-oeSICCzi8Sr_vApFHBBxS5Z5JRSBl8oo-TWRTEhbKOXCZ_Vq0sD0GPEr5yL63UEHvsgclARQp-Dnp80nUycvSYAZOLKZZp605Bs6KcP_drXr1K8kjTqG1oBpfefZagz0gLqdJ1zZ6jDhoHdBLbaSrp6hBX5btTLwc46-7sjFyvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام ۲ هسته‌ٔ عملیاتی گروهک تروریستی-تکفیری با دستگیری ۴ تروریست و کشته شدن ۲ تن از آنان در جنوب‌شرق کشور
🔹
ادارۀ کل اطلاعات سیستان و بلوچستان: ۲ هسته‌ٔ سازمان یافته وارداتی دیگر از گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونی…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455854" target="_blank">📅 13:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455853">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHoAkR2-v3Nq4hCyXoPJyMXs-Q4DxCkcy0c7Fw5c6bv-EeHkLwHM9345SEfYsZyC-MgJliRkaeHCqIMeIGY87DW9ZgON22BRwLDbkKxbd2Gg_KMIpCoFlLs0gH_IFH4A-MxF8JV3QAuQCI8IxhF_fWvPk0kiZVCFLkVTY7fJOu7vG5Vojg75zjZMJby3TOIoQief2NzUib3ZOkeg5g4kzknYG67NGtd3HZwkxW4nN2plKhLtS8WoX75lcjT4XWFQL10dN6B62Sfe_djnluaON0e-tAPO7mgbGgjqAHjK69_7_IU7gRHhW-kiiVGKO0rGFKA31nLWDdKN7AYesgLVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال بازنشسته آمریکایی: پهپادها و جنگنده‌های ایرانی دمار از روزگارمان درآوردند
🔹
ژنرال بازنشسته نیروی هوایی آمریکا، گلن ون‌هرک، در نشست سالانه سمپوزیوم دفاع موشکی و فضایی در هانتسویل، آلاباما، با ادعان به شکست سامانه‌های پدافندی این کشور در برابر حملات هوایی ایران، گفت: «صادقانه بگویم، پهپادها و سایر وسایل هوافضایی از جمله سه فروند اف-۵ که از ایران بلند شدند و در ارتفاع پایین به پایگاه هوایی ما حمله کرده و بمب ریختند، دمار از روزگار ما درآوردند.»
🔹
این ژنرال ارشد بازنشسته که در پنل تخصصی مقابله با پهپادها سخن می‌گفت، بیان داشت: «این برای من به عنوان یک خلبان بسیار شرم‌آور است که بگویم چنین اتفاقی افتاده است. این اولین بار در چند دهه اخیر است که نیروهای آمریکایی هدف چنین حمله‌ای قرار می‌گیرند.»
🔹
به گزارش پایگاه خبری «وار زون»، این حملات در حالی رخ داده‌اند که در کنار حسگرهای مرتبط با سامانه‌های پدافند هوایی مختلف از جمله پاتریوت و هواپیماهای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) در آسمان، ارتش آمریکا سال‌ها زمان گذاشته است تا یک شبکه یکپارچه‌تر پدافند هوایی و موشکی را با همکاری متحدان و شرکای خود در سراسر خاورمیانه توسعه بدهد.
🔹
این پایگاه خبری در ادامه می‌نویسد: «ایران در روزهای ابتدایی این درگیری به‌طور فعال رادارهای پدافند هوایی و موشکی منطقه را هدف قرار داده بود؛ موضوعی که به گفته کارشناسان نظامی، خود به‌تنهایی زنگ خطر جداگانه‌ای برای نیروهای آمریکایی محسوب می‌شود.»
🔹
در ادامه این گزارش آمده است: «این مسئله این پرسش را مطرح می‌کند که ایران برای پشتیبانی از این عملیات چه توانمندی‌های دیگری را به میدان آورده است؟ نیروهای ایرانی ممکن است برای هموار کردن مسیر حمله، حملات موشکی و پهپادی گسترده‌تری را علیه حسگرها، مراکز فرماندهی و کنترل و دیگر مواضع انجام داده باشند. همچنین احتمال استفاده از جنگ الکترونیک، حملات سایبری و انواع مختلف عملیات فریب نیز وجود دارد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/455853" target="_blank">📅 13:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455852">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انهدام ۲ هسته‌ٔ عملیاتی گروهک تروریستی-تکفیری با دستگیری ۴ تروریست و کشته شدن ۲ تن از آنان در جنوب‌شرق کشور
🔹
ادارۀ کل اطلاعات سیستان و بلوچستان: ۲ هسته‌ٔ سازمان یافته وارداتی دیگر از گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونی به هنگام ورود به کشور شناسایی و پیش از هرگونه اقدام ایذایی، در سلسله عملیات‌های نیروهای اطلاعاتی استان در شهرستان خاش، تعداد ۴ نفر از تروریست‌ها دستگیر و ۲ نفر دیگر در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🔹
این ۲ هسته‌ٔ عملیاتی آموزش دیده وارداتی مزدور دشمن آمریکایی-صهیونیستی قصد اجرای پروژه دشمن در ناامن سازی استان و ضربه به زیرساخت‌های اقتصادی جنوب استان را داشتند که قبل از هرگونه اقدام، شناسایی و متلاشی شدند.
🔹
همچنین یک باند ۴ نفرهٔ سازمان یافته شرارت و مخل نظم و امنیت عمومی در شهرستان زاهدان که درصدد ربایش شهروندان این شهر و باجگیری از خانواده آنان بود، در تور اطلاعاتی سربازان گمنام امام زمان(عج) قرار گرفته و به همراه مقادیری سلاح و تجهیزات دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/455852" target="_blank">📅 13:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988b13041b.mp4?token=LxyCCBAOA8J4mt9LTK1v5DnMvsvmLPShgdbPZbgOW2jv-bDtbSjvA7ZTB1uStIwOqwnZzkvSmuzBqNX4rRWvnWs6q01Y3oi4FQOKPpnsVA0r3ZUR9fTAbZO5p9tYryWQ6Hd_m1fqaTlUhR9KaXNWMQBhEfZcgR9exzhBcTFAR4zcGAewm1iOV2ONwD2L-qtJVauqqdxEgzLGCn493BiiIVABx8tVyd-NttRbwgebSdLuzexPBkVg6PcW6hz3grr4Ct9VaWnskN_ndbpk8-bvkazYbHzvjMIS952fxL2DxganCOv0RCjkulsdcTatLSHIK4aPJiAq4qyhx4BxSS28og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988b13041b.mp4?token=LxyCCBAOA8J4mt9LTK1v5DnMvsvmLPShgdbPZbgOW2jv-bDtbSjvA7ZTB1uStIwOqwnZzkvSmuzBqNX4rRWvnWs6q01Y3oi4FQOKPpnsVA0r3ZUR9fTAbZO5p9tYryWQ6Hd_m1fqaTlUhR9KaXNWMQBhEfZcgR9exzhBcTFAR4zcGAewm1iOV2ONwD2L-qtJVauqqdxEgzLGCn493BiiIVABx8tVyd-NttRbwgebSdLuzexPBkVg6PcW6hz3grr4Ct9VaWnskN_ndbpk8-bvkazYbHzvjMIS952fxL2DxganCOv0RCjkulsdcTatLSHIK4aPJiAq4qyhx4BxSS28og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم نهبندان خراسان‌جنوبی در سوگ شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/455851" target="_blank">📅 13:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljiRCg72t6ikgZjrB36I-1dQm9OBmT5BGY1FDQ85RsMQUvx4mLars6c0IATIwiJHV7MrsEcSefbQJYwEPAbsENRiJ8D2EbqQBDUiM3FgKAZyI7sEtO8AVW3-27zn-SxH7u1ya3EzY0UDuxTO6EOnQEX-i8PLeBTNWeLM3eaZH0BS-CHWSfgojlWDeyZ4pf8GMWWKgFoIChiWi5dfyoE7K7tnU7Q-_wEiT0ffBHXVmcj6wsgDnwPdHW-l3BQNNP-eaurt67bdWRHEF4WAxO2pRNBl07oQ30A089NxrRagxLlx1KaK_rh90hbC2fTnzX4g7KLvH24aQbWgfqNdnYb0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JG03kG2CFpsSw9O0U9gFvQhiiEQtv6AeWhkvMl66QfFOcQnqVdxcAUSw12uAydlj6lpRd95XlhYX0WRBcr85sDWsUVS7S_TQDpOuh5PZHHxnR-P3e1JNbOPPWM7nkhRrlmJS9BZqbkvSdey_qS-wqzEPniFqNmP8fBsq228mpIHul44RJjEjr3zah4Qk9u_1Baz5ARpDCzBmhjrCczq_WP24Sa4L_bhG29oVnGpIfak47DlyscBdcwIHq6jEwBFteM_wfPdKuUzKrYXdyQbh2hKXMesjutlveB3se3htBZKvf64-AX8nQPClfgAzeo7iz0jcCCwtU_Zu2vlBh5f4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmMxMRMxFjB8pG4NRGDPIP4v6VuV0mp0FqoEyOub1At_3usEa8NluyzzRCMrMObhL4E7jkA-DSIr8ZOzS4kXTMmZSKiiasf57UGX9A8d33gI93tYl6BZJ-XtD_u-GZaLjZIThMj-E9PqMdFGSwKm6vPk1VPCpwqLRHm51jGtAV9D4kBorcJq85p_zGC0Sc0g7-Ih11klvlrniPcs9WKTf1_3UoNN8crD5JawYNEzVV7t6fQHeUv9HmoSVGfzWYdTPQBtYVmenvNx41ZEO68VWRtf03s66Fk_nWHz5nAX9y6luQmprLvuzkdb52It8V92xgtcm_VOUy5fg6bLKvOZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2sIXXQZMeT4RUmS6JAL5ddgaS6UUebQDqFXMt28MAtiXLc_gEuv1YY-mYaAnx5v9PIgdZv9vFTHpK0RX5WrdrpKInAXkX4IryQwQOSCIpXQTLf98BLeSEBfC1SHyG-nRlVNLkAkHMalDn8Y4rJuUlKgyTP2JjZE6SN_M_rJ3q-hbNkulFKFYjtQwhb_ybwX2pCfVtTYwNG8cI6M1drVOlXtP4dzphP3U3hC-pAxMK7_Z6Sx81eKIVcL2VBUtr8lA6WF9SyjF6i5jx9cOHKG08MQ_IhC3iRHcXWYiDaSZ1xGMiiSoRANXDGaZcsA6xAZoJRymLmu7Ee4NC_sorPdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvoyBngm1pwJuXfHIwcRsGQXStT3mriXnJqTQmkv4s7SUbklecsaK_FQt5OfEmlKUJFHTe7fERXK-xnwLd9RL9FeciwVN8bZ-tdHeFM8EnjreLOROrCWqFyMaMNtwkdUbEtLZihPOTkv9FqCGMPQtTWNG7da7vtxUNYTjeMkP6wAJgv3yUu1sOc_bscGlDeijqTuKy9aBc6HzB9rrRuoIsrr_vh8dobqkeqq_uumpE0o7x8H4BDuFChMZLHG83eHqvPIIzn8HhqhVDHdUijDPZleTRFoAMFlZYu9EvuAg-ho8_JB3WGuk5cjAtYy6Hfjh9iWbl48MvE7pAAoCF3fdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQpGb27tV2L5dA5qYuzAbVmots9Unq6p8FWZ3IAVAu11h1x5tQgw5kEJNp8UcmBCndh07Clz5UNSZjM0qddBaPIiNtSrQao7MUZucm5uBibyYLuhpFeVK7QqxZnTyUVwp2GrLIyURi0PQ0EcDglMt9BbfSM9jJ-bK8_-xIOsxjaWbbfwbWufOtlYZ92iQxq6eOiN8g2aYF_0LSOKXAeaBbnGPzLTF-Hoc-srLdVyEJJb0d0DjaiPeCBxhw4RrIAwx0jFqOzZkjRMeqOvY0V6fKH-rInF6-rLD9GJTah5Naz2IxOrwjIIEg6UYYgwTkYR5YEB9MnE8oYYXpdGDCqtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVAC8qm4bv_yitBG5cJrXyCq3ySlrIBaAWz-XWkxHdIVbqeZWJC4EDk55Wf3WsL_mHt2H0yGPHq_MK_weavGuMCFT0Qi-F_IhEBgoZiuyg4TErO_ycWXpEAbERe3BgfbKzIrB4n9yfeNwN940ESL4FCZSeqfueto_G1H711ysJvOrxbzfAoKJCLzgdc-ouXl2kgANGMB1QQTZirpL84wbsfS1JJ0ggXJmjIuANypI2zzHkapCDsX0TZ9l5ep0NonNt25FVd-Lb8aYoFcIZhl3XP9X4iXf5Vs-oBCxpKc-IKWtION-Av_Zzwfd0F1g4mfARQc1ptf-DQ1iCr3b7JwqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تبریز غرق در ماتم شهادت امام رضا(ع)
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/455844" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712bc5e595.mp4?token=QrDJ_exdTRihlsCud69mhYmpCbOD4ye5uUwM-u2zRM_wvJxioCQ1wPHjbHzJ9RoVcQdn5cH-1Hja33OfwAX6n_d5J7VcTMXOpWEGrXK4qJoT_H8n1jnWkbndX-wKr-ju0u5JaSujXLEau4MEBVXaR6js_Il8IrJUWiNmedqjLOQDrTjCvhxYLuqv_XwZ2UTyzRCkxhDIVeDpMWnTYHm6KawE9-MhjT4qdNVLEMguAYYO9lk8MwTbgR1mN6jZxc9JQ3a_0NuT7OKVBBtdvfYNxjUBogjohOg_RzhHM9ofz7fO74U5_sk36I1bLT8V9vqEyV0JUXd8q4R5xsvb8ilhojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712bc5e595.mp4?token=QrDJ_exdTRihlsCud69mhYmpCbOD4ye5uUwM-u2zRM_wvJxioCQ1wPHjbHzJ9RoVcQdn5cH-1Hja33OfwAX6n_d5J7VcTMXOpWEGrXK4qJoT_H8n1jnWkbndX-wKr-ju0u5JaSujXLEau4MEBVXaR6js_Il8IrJUWiNmedqjLOQDrTjCvhxYLuqv_XwZ2UTyzRCkxhDIVeDpMWnTYHm6KawE9-MhjT4qdNVLEMguAYYO9lk8MwTbgR1mN6jZxc9JQ3a_0NuT7OKVBBtdvfYNxjUBogjohOg_RzhHM9ofz7fO74U5_sk36I1bLT8V9vqEyV0JUXd8q4R5xsvb8ilhojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطعهٔ موسیقی «به رَسم کِرام» با غزلی از رهبر شهید در نجوای با امام رضا‌(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/455843" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c5432f7b.mp4?token=F9TA-_exaZ4DQ43MQCHTXMMVNiCbx_Xl6i3biANqttG6zsdH-FmNMtAkwBrSabskjg9Uy5fOvz_8ZqoQKcWnItQ1kFVcJGu7zTMamubAzVtCwYhlsNGXmNpPAY26WGodze8Wkauhe187bXMpEL72s8X27u6j2X2eFBK9cmFH2hY7gdCzgzn4pbhfliQCleEbHlpMRxrPcWgbGPv-vW42K0NrF-0hN5--Z7VJ3vNfEaTl46lpojb79lTzl-i4TsLawRGVkQ1hE4gCEUJcZqhbqjhuXe-QiZ798YTyytJdjFkF7QBa2Sw55skaT94c-t_71SFaqgKpGQzYZf0ySE2Mkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c5432f7b.mp4?token=F9TA-_exaZ4DQ43MQCHTXMMVNiCbx_Xl6i3biANqttG6zsdH-FmNMtAkwBrSabskjg9Uy5fOvz_8ZqoQKcWnItQ1kFVcJGu7zTMamubAzVtCwYhlsNGXmNpPAY26WGodze8Wkauhe187bXMpEL72s8X27u6j2X2eFBK9cmFH2hY7gdCzgzn4pbhfliQCleEbHlpMRxrPcWgbGPv-vW42K0NrF-0hN5--Z7VJ3vNfEaTl46lpojb79lTzl-i4TsLawRGVkQ1hE4gCEUJcZqhbqjhuXe-QiZ798YTyytJdjFkF7QBa2Sw55skaT94c-t_71SFaqgKpGQzYZf0ySE2Mkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمزمهٔ صلوات خاصه حضرت علی‌‌بن‌موسی‌الرضا(ع) توسط رهبر شهید انقلاب در حرم‌رضوی
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/455842" target="_blank">📅 12:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlBRIrKOWxo0j7nsbkHB52FkScmQqdmcGjTeAa3Cei-VZ8f19qT1J_ergw8GKkXbAt5iY44BAPNebAX14xB6a9e-9geMYuRA-VVHr0UHS19959ItVdWfeZrjLUfgsbxbyQGKpf6sZN0r84OzhHMaoCT1r_YoOQzBNZFm1a7JLNiLs0ZKL5yUhZrXdciuVeo8Wo5lTOXPMiVbX95lYHn_AICSOFGX910wYT-M7b6HK6ucjylMeeYRUTn3Qz5g3cH_UHvhZcR87Ize_UKLzf2zI3HOX0NCA057yO2cnhEJs2N5EkcHd9lTyYJFAuerXyXWbm1kWcxDM738arsr7qTr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVXwB1FHcJFcLAWMBfu0KN_KEoxojtJy5pEnHn0Y0mbff0b_xpVeQDAH4QFKmV2HaYogwOsM2O9mKwC8gafnDbyx2OLGQegfNTw68n-2eTB948b5EIi39CEGBeGzoqzAU_3V8bKKz9g5imDeEqT6zHR5P_EOpaciiC_-J0fu-i3k5MDpv3thU2MqQKKbfdUC7PzXM1YrnDKDjJ4Hk4lGX6ZV_9-_Ig43qOIeKG7yfuYJMZIvkdWVsa_PhbbGrk_W2FocaKT74WxtwyZkcX1uO2tp1C0uprMFUyOIDzy16X3NvYxuXRjzuBMyqgOOLgL_vIckc9cuWLfhPY1b6krvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR1I9cG0S_fDtOAhrMzafoxG_zNi8vMWoAFq9CIy8K80XXG3B0QjHSJ0gRmUQO720r0T2SqpK7jmiBwj_JJXJQiTWraw83N56ywcTBOBg6G13SPibLO1gyVA2B8aU2HZvYdV7AMohvtkxrw81lKYCdPIhiY5haXDj0JS-bUW1AIShsoO-V5AWPoe4E5LmWqA4RGwVonz513eNt3AlQaggd6j75i8T13LVJygGHUP48pE-GPXHNtli2K3W5FeNcuBOtZaSwKO2JHfpbCNAai1zoFLgTpXKJ9zWnUnwYYbUHyRBOOtfBzSbYmsXgfVKzjOcc_s1JlUNQFA46MQ1A6iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNnCuSWtSNwBRZsyotoU9wBOlYysHvpMr9rbpQK21j0cw0yOFDJpwNepG0lj2EVp9dcVm0ZHpmdcQhuUvd32KBjKIp8D9Jov9Ax3ojyOsnrXkFo58MnkuFGXbkYh7KUFK-2ivKK5saN7GTgrc-34dpgQLNXSjA_-Nt67UDfYr-M9JLHPSoEZpSv7h_47oAgxQ_-RLLz9aBT453h9GVZsuIkHUpufds1t3XIJSQ2RGWMfzDkXQPCB-h8wxBcOerm05DkllvrIMQMAFA3qx0jxaJm03yQ-gUXln6q3LAJv5U6Su9tPiKJXEWvcRmKgks2jZCAkc8cn7MxmFSA-SCAXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0RceKuJ3JIBcnYG-iyEk3XJ9C-yZMeWeac7klKPmfOK5VaOicz8CVQD8oDpTwx_EIO1G29Vfkg42TKDg-DVmR8pQ_EVLepdl4Y8NcXHPbqhLDyPGpAQURVv1OQ71bi-USo-jJpNDptfRsjO-5Q3cX-ac0iyjNBoz2G4cz-t01gs7-uY56WnIeJoANEDMGmtasSW83iGPpLKpjrho7IN225xyo6FNLql1f-rFc1dxGlFhKxTDtLIHKBcDYS8RAQHGmE8E7ZMFUvyRLaHGlTRDQMDN-M61DwpJ2FnENyesZs0uKzLVLlnlT3jVQTdxvQU0pR7u_2l5xcCU7qYIfXJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXN_2YJs6DjzWxRjRD2YI_gWmPhy9itRgsIhOyI844kR6JsQTPPhkz2ZgRd_QJb1cFdoIoshrkslhtXILZSlCvOBJoH6bXm-PN9iX7hGyxwW0Y7BZGfsaxPt8xYP3XrFMtKrgwSdjH3aUI03JPwHY1hdwNsbUxUBfvxtkodWf4MaloAsVUe71ehL_R6tGUZ1K4oHAHnCRIJnKnaDQWWh5daYGXmlbzRjAuvHPjggjfWC0TfW8Ic0wgi6gk9XdQowB_joC6xwv2kWBcdANQsUT-2q7DRad_LhAPfWpqmxvZUb-tK9fkqwZ77lis67QTguR6ZQlIjJPxjZ72exySr-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1SDSao7KGwiEBteMKSWvZQRZPlerblvpqckWj1hbsb1Tdu6jYq5qoGECq_g33CAMKAQVk0lHDEZ8kK03z4nKdR9r15KFUUiRKsIqqPn1rPcBLR4ToAbXINDWKS44U6fJxUtZ_jwj5-Uf-8Zx9veiCgl18F_Br6Bd7gS8hXZn_YAXPnLQUyOvdcA0EMSxQnGOBHlTndkhtJN-dzJGlafiZnYIxjqz-Lln0asg1o8Sl-JX54dJAioLmiP-X9Y8Vibv9e_9x7w_5UcDGMEDHylymtnZLBOGbJFVqy89ndQYAZcIJQjftGKzHrxArrl_Pj6o5YAA_rMlDyhWLcxvQg46g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین نخل‌برداری یزدی‌ها در مشهدالرضا
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/455835" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636abc426c.mp4?token=DuSOW35qF4E4Xu9g2-eW91SN2-AuWwSaRCCcqjOJRQOM_E3fFqJR5Lf27Hlt7uutrf5L3vEYlEYKa2PyIUNQrtNbFEWptH0mVCisGBioScOSiHcWqNZCJ55t8LYQRGUjVnRiiLnwn3WLLwWHYwF5sDpUhFTLaF8H5LNfOn-MoQI8mKRwPUKtWQiGSQg6OcddcErkGYj02sSp3KGS7ugt4mU70SCfnFLE8h6HwoqTBS0rvXz3q9epz5VdAvp9fYzI8X9QjSzuwHKapJ9hLGwvHT_HLw4KxtvVCE16s1_C1rHDZQk-1u1qE1LHjcdqXHb3mrMJZJneIND1hHsB8Vp-LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636abc426c.mp4?token=DuSOW35qF4E4Xu9g2-eW91SN2-AuWwSaRCCcqjOJRQOM_E3fFqJR5Lf27Hlt7uutrf5L3vEYlEYKa2PyIUNQrtNbFEWptH0mVCisGBioScOSiHcWqNZCJ55t8LYQRGUjVnRiiLnwn3WLLwWHYwF5sDpUhFTLaF8H5LNfOn-MoQI8mKRwPUKtWQiGSQg6OcddcErkGYj02sSp3KGS7ugt4mU70SCfnFLE8h6HwoqTBS0rvXz3q9epz5VdAvp9fYzI8X9QjSzuwHKapJ9hLGwvHT_HLw4KxtvVCE16s1_C1rHDZQk-1u1qE1LHjcdqXHb3mrMJZJneIND1hHsB8Vp-LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرازهایی از زیارت امین‌الله که سال گذشته در روز شهادت امام رضا(ع) در حسینیهٔ امام خمینی باحضور رهبر شهید قرائت شد
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/455834" target="_blank">📅 12:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM2e-8RWnQl_6T7u38Woh5HDDuVVUVwj9mOC4Ip4DBLw1nWXuVSH5a-9pwvwtAhsg5OOlTHvlBIpox2fkOtSMjLkilR070qSJcpQfrUvQtJEYbbYcNXQlK6Mli16VR-ny3g41aviOtfHKEqJtKchDcrBpCQ8xMpEe-1U16XrSJ_aAvT9IKnVCi9aNELNTiTEsWVzys87H05CU5ftqHxHnluwRFj51aZ-CI8H-1c1QkYvlKnaDjNm-_fgtRwrmguwPNllF9T4Lh5ki2PZwmji_PvjMXZnit2ywgaHwKeiXjLKJ8X5sLV7sl-pt1MQ7RJJzlCOVy3HUCZZQ5pDznA_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی:سازمان ملل در حال مرگ تدریجی است
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی: من خطر فروپاشی یا نابودی فوری و ناگهانی سازمان ملل را نمی‌بینم. فکر می‌کنم موضوع بیشتر به نوعی مرگ تدریجی شبیه است.
🔹
سازمان ملل در حال از دست دادن اهمیت و اعتبار خود است و سهم قابل‌توجهی در حل بحران‌های جدید یا جنگ‌های بین‌دولتی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/455833" target="_blank">📅 12:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h66gv1R1a6u41K6Nx3yAzfbCaHu_RbU09bjy1F-Xj-UATVMhERKGHq0PkRSrS7JwP2Jlz3MT6Zownsk8TZJKT7dRv57YS3TUuzcuBIhd2VORuMGe4tLTSLI3qccKsT4owvhx7MK73zu7fTLO9iR2kp0pumAr3911utp9ygkNG6F6CLsDA9T-TkUg60msHaKox9-9k_hSa8yUQ8YFuMdKXi_IwtVwBc-nnWIoJ0RBIjl38ZICAoQccTLwtzg55szjxYi_lyrDoHdxEsjM87JDnXO-8XQ36xUe227zOURiNVyQibG_Iz_HuRWs_QNF8Op5tnKg_HenOD-QYgKqEbW34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار سنایی‌راد: در جنگ احتمالی آینده تهاجمی‌تر از قبل عمل خواهیم کرد
🔹
معاون سیاسی دفتر عقیدتی ـ سیاسی فرماندهٔ کل قوا: دشمن تصور می‌کند با ایجاد اختلاف داخلی و فشار اقتصادی می‌تواند حوادثی مشابه دی‌ماه را تکرار کند و در همین راستا اقداماتی انجام می‌دهد، اما تاکنون محاسبات آن‌ها محقق نشده است.
🔹
امروز نیز اتحاد مقدس مردم ایران زیر پرچم «الله اکبر» و «لا اله الا الله» شکل گرفته و باید این اتحاد را حفظ کنیم.
🔹
در داخل کشور باید به این موضوع توجه داشته باشیم که اتحاد مقدس، هم سفارش رهبر شهید و هم انتظار و مطالبهٔ رهبر معظم انقلاب اسلامی است و به امید خدا، با وجود اختلاف سلیقه‌ها و تفاوت دیدگاه‌های سیاسی، هرجا پای دشمن در میان باشد، وحدت و اتحاد مردم تقویت خواهد شد.
🔹
به عنوان یک سرباز کوچک عرض می‌کنم که مردم هیچ نگرانی نسبت به توان دفاعی کشور در برابر دشمن نداشته باشند. ما در جنگ اخیر ایستادیم و به اذن خداوند، در جنگ احتمالی آینده محکم‌تر و تهاجمی‌تر خواهیم ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/455832" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394ce654c.mp4?token=EfC658pIr7bw50Uir24oMEtgY_-3jIdxjtMJzzbioee-E-1htkdmjru2RCMmfsYUvhLq_yO2GhATmBVdm3XjkFno-u35775510LHeVrooEgHlH72eRTsq0uQ5xtE-HwdimmCUPrrxOjci6QOfdEc0SAknAMO2IOwfyxL0D-2Lrx2QGXVJCZvQuz0qsEB1_y-mRdUWzp6htw4xegHuUusUtXCP43Vmu_NhCxLt--6IaF7en6IWC_LZi8AC3jRI3ibpmxGcz8s3YabSuj21peXpvQJcp1kaG2463rrIJ7713BIa-_pkrn1kkD1Bv1B6_yTzoohZCyS11fDafmdq_F7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394ce654c.mp4?token=EfC658pIr7bw50Uir24oMEtgY_-3jIdxjtMJzzbioee-E-1htkdmjru2RCMmfsYUvhLq_yO2GhATmBVdm3XjkFno-u35775510LHeVrooEgHlH72eRTsq0uQ5xtE-HwdimmCUPrrxOjci6QOfdEc0SAknAMO2IOwfyxL0D-2Lrx2QGXVJCZvQuz0qsEB1_y-mRdUWzp6htw4xegHuUusUtXCP43Vmu_NhCxLt--6IaF7en6IWC_LZi8AC3jRI3ibpmxGcz8s3YabSuj21peXpvQJcp1kaG2463rrIJ7713BIa-_pkrn1kkD1Bv1B6_yTzoohZCyS11fDafmdq_F7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان قلدری شرور اجیرشده با شلیک پلیس
🔹
در پی انتشار ویدئویی از صحنه شرارت و قدرت‌نمایی فردی با سلاح سرد در فضای مجازی که در آن متهم با استفاده از قمه به یکی از شهروندان حمله کرده بود، تیم‌های عملیاتی پلیس اطلاعات تهران بزرگ بلافاصله وارد عمل شده و متهم را دستگیرکردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/455831" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa4cf399.mp4?token=qTH2Zqa7fxSue37ZpKfffWN1aIuCyYPHtvhtw6L0BYGP76QW4gVoCyDsNGJtlhfsWeL3mMq_xxh8yoc40dlHt9abET2RwUvpYYK0rJEa0dmaRC3UwhdV0YOSvob9-P9aTWJNVMAaG1rfhdL-4JPGYMMC3Fki-0BBsaDV4RPYmKYhBwX7eCxDNpIJ7IFDogODCWzqUZdfWLU3ien4fXEgiLiKUpUR7-bcVAsS2--6rm0vJfq8yyKXjYdcG4Co9IFHw21OjTzjJmQJxx4N4YzKV8YZVbF8aMXOl0d3_kiLUM-xTbzOkIcJTRhfbsiTWQhhXyXfymhPFk_Ie8GUmUAx50HQ2eDHv9Mxtvp3zqGXidvzf31mkp-6jmVD2PzF3Sr8mOQeywYry14U4zvH3TW1af39FX_lwUsz1O_TsmhsJmGDSJSyWk35buvE_OxnmheEYJ3qsV9YAshPirefbd8vH23IRlUObgNPBja0Xt367NXouBtarRuy_lVgq9lgIQu2zWmZX0bjhBg7P9wj48KH9B7k81JNNP_onSTZ2ufzkwzcF5-nB7zIB8W1HE0iYxirG5qjpnGux6mx44uD9GkgXHL7FMzANFeAs1Nf9w-SOlrjEUY19hNqTwrMKRK1LrnccxidQMYEHOZtu9T5rbOYfFPtpfWd7lh7fNrmCn_3fW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa4cf399.mp4?token=qTH2Zqa7fxSue37ZpKfffWN1aIuCyYPHtvhtw6L0BYGP76QW4gVoCyDsNGJtlhfsWeL3mMq_xxh8yoc40dlHt9abET2RwUvpYYK0rJEa0dmaRC3UwhdV0YOSvob9-P9aTWJNVMAaG1rfhdL-4JPGYMMC3Fki-0BBsaDV4RPYmKYhBwX7eCxDNpIJ7IFDogODCWzqUZdfWLU3ien4fXEgiLiKUpUR7-bcVAsS2--6rm0vJfq8yyKXjYdcG4Co9IFHw21OjTzjJmQJxx4N4YzKV8YZVbF8aMXOl0d3_kiLUM-xTbzOkIcJTRhfbsiTWQhhXyXfymhPFk_Ie8GUmUAx50HQ2eDHv9Mxtvp3zqGXidvzf31mkp-6jmVD2PzF3Sr8mOQeywYry14U4zvH3TW1af39FX_lwUsz1O_TsmhsJmGDSJSyWk35buvE_OxnmheEYJ3qsV9YAshPirefbd8vH23IRlUObgNPBja0Xt367NXouBtarRuy_lVgq9lgIQu2zWmZX0bjhBg7P9wj48KH9B7k81JNNP_onSTZ2ufzkwzcF5-nB7zIB8W1HE0iYxirG5qjpnGux6mx44uD9GkgXHL7FMzANFeAs1Nf9w-SOlrjEUY19hNqTwrMKRK1LrnccxidQMYEHOZtu9T5rbOYfFPtpfWd7lh7fNrmCn_3fW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم‌رضوی در سالروز شهادت امام هشتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/455830" target="_blank">📅 12:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBYC-eeCkwUtnRuvKu9xd93V8DQYrsiHGrzpdD0qhjBGdlvsuAWAVpnckX6bRCOiN-j-BZS9W_g9O34SXPvJm4PoJ0AU0iEmPspZqV2_5LDcwwm0L30Sg99S9__UJ1xXoPZNTJ0J1lI7CH-kqV7S2RSAomzlX7UlK5rIZHCa4KAoKl5lxENEFOB7FVfKQlbMS03Z_mEOpTOywibttnRL2OaCKP_OSnTBpoMna4y5Wg6iftW8RzFyR-j92O2m92UzDWT7xubpeFJMz-n6njIL2OHthatcnfyKhsfxpQ8LEc7xb0HME9FQzWGNsI96FP48UpnfEkURXNsZfcbdVhvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران: بلندی‌های جولان بخشی جدایی‌ناپذیر سرزمین سوریه است
🔹
وزارت امور‌خارجه: ایران لفاظی‌های نخست‌وزیر جنایت پیشه رژیم صهیونیستی مبنی بر تعلق همیشگی بلندی‌های جولان سوریه به این رژیم و نیز نفی کشور مستقل فلسطین را به شدت محکوم می‌کند.
🔹
اساساً سرکرده باند جنایتکار و مافیایی حاکم بر سرزمین اشغال شده فلسطین در جایگاهی نیست که راجع به تشکیل دولت مستقل فلسطینی اظهارنظر کند، چرا که سرزمین فلسطین متعلق به مردم فلسطین است و توهمات نژادپرستانه رژیم نسل‌کش صهیونیستی نمی‌تواند این واقعیت را تغییر دهد.
🔹
علاوه بر این بلندی‌های جولان بخشی جدایی ناپذیر از سرزمین سوریه است و جاه‌طلبی‌های استعماری یک موجودیت غاصب و اشغالگر نمی‌تواند واقعیت‌های حقوقی و تاریخی آن را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/455829" target="_blank">📅 12:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riaxsymK0rLrtD0Qclf3AThWrRVzfB0Zb6fTWPSfCi-dKZitdKC8PcI50vuby1t63F1nO6A6KixSygOlZCJ8Y0YPaEStHD6cOnLdnXhWEZ2qwunqW9lvyC1AI0HmJ-XzFi9zh4TrtH2mPboScQSpzaL4UfW9CLDQ7euwheTdYwW7bD-v5iMmLaZcVXxvbvOTZNT0HmwDPByZi0eCNfM_8eqxxS5Pj2ZH-Hwmdi-rhwpRaY9x1oUPwRdNfulsHJmsS7TkpL4Mvm-ISwcYw3bVmtlzFGAlzbd3P8Roh54E1fQzkeLZdByl1XPbvYXfbEB_GQnY6-CkgXLeu_1LZTUaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQF0ykdx_7yRNCToQDNIudJUK4HL2ADS89k34BMhYY9v6Q5_jegmEdpg1R9RkcKZjniAWVBIj0WL12CbB-9kguWPUZIYu5os3HrvO7cIjoeF8Of3wckKxYkHNQz5Hf72oAKGAt8LWmpZrxWALRDHTsygScOxzKZq8L4LfICMgJX-eXYEUpbbYnst_0MEYeADMqxgqbGfz6hAdB6iuBZ1UvjNYS3lZNPceRKhzmo7LMxq5NJ6Eu_Qj13APw7XLUET3_5YbMeXdmd76AUiHP_uBDkceSYgZQkIQuv22P_h6KTcKF7k7M3mYqKM4Lvt05YJywaff3xhOyzWDtMuu9X__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnBWiOYDelEugyHq1ySFatA-Nzymkihcy1Mg5gRxJePoBezTvE3YX5pocss7M3OLOv0eyuWi1I7DSkpWPzzILnXDFBmoYezvI7Au-Q2ertDPxjwz_NIMAcCEcgXYCi65_Abil9aB0m8I0wpzffcv0LPkz-D9CrLDtKdnuLUvM-tlLyCCAoijgPTOtFp1RHG6OPlgtKWiEI347SJSsV7Yq2k0X7qHGWHbq6OIsXgmtPNuF7rHLymShi_dTOE71lzlcdqd2ASMm0qMsG-OoTYZCz3MX7y-KnVNSDQQKjLV_E1kasCfXF88IbwF2jKmZj4tFpeOrlt6G6rb2fvQtKQ85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvolG8wI64P8XtfNkgeyoYosYh1g1_j1CcokIYUwXdmRtcxbkU6cBrqNITikxM-SBV2BkTAgJ9xubdE_VzkhnLmhouerq9PEUXQjn5O9QeNse0KsJbSdpKByh1en_AWh5MUGH9Un6g7nVIDFmyz072yejDSEz3LfCxWA1sl25i_HDhLBu1W2Y096iUAmaChbKas8r_2JezD4pRkWx0oWoX3W-jQg22pG6iBxc0NTn8WrX7u8VkY0BfEQ7S13tbLm5Neh3MnEVQB1Bo753RN8K3vaZaDcbxtxnP72Vl8fqXXkDMCFBPw6gsQXWf-_gmLIEg-WzcuBlcnfdBvO2M2INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFu93nnxAaBtKKn-UxARgEkWbLOPhUcpSujPpl1qwUY6ykVwkvhJy4L9hbNrhgjGRX6BeMfMxeGuHC8lILm_RPJAxlkyj_DfrbxToqznFaJbsh09PY9QfCjgAovV6oL3-ewRcXSSO8YqbZRSFg_qc_YXUp2i2dMprc9O8vx3PQHJ_mQACgJj-SAgrrSUQHoRQu1b9pQb59o61F3DTiCRs7MjwssNvqMT1NQzCa1jTK6UIKzA24bdpKM_ApU2kh7wQ62arVzRmFWFDCmlN6UTMravxFBjENRygmeOTYLYl6O-y3lPpJ08jUwSdZYopQdGVnRN8z_w-hqyDRO1KfhplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Edb0RRjx1ttYblbF03DW6LPuE74uyvTrHtr2oE4nLWhvFMCPSaVYVAI_nvVR1OCgjZQSoRDoAyzvlt9-KieskLI6Ww5XrdEzvmz4t3FONBGYGoPAScVu-CQDs-4RaQEBlvs4ABKUQZz7n5NSvVsA03rpxhLaL6IOghXyWmn8E-NXb67YjtjX9Aly7-clkjD7P8XQr1I4N9SejuQaV90ZuiIfjWnflikIklehJZxZdAtEqBworfVlk3CPTYgECe-yjN-k66o7myQbx81GGMPmDihPqbG7Wqp8knFwgdZAjX-WG8TyWNRl16XJeXZ-7oDbxAh_oaBWQZXUbRuUKThXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul0tqzTlhKGkxtPOCFnC5OS-J0FUP0PwnqCjcSIfiiv-LCU1WkNcci7QlBh9kI0FyanjHN_gNy80XXoQLwWlk804UYZIxEIWzq_LACSZBqU847uUBFTp42ZnQw_oeUYWyE3K1OukSWbM7zvRKQWZzzeoM7XqFSGAeAwZ5HJ6TcisQ9otMlHlDOnGV5iQx1HH2CAh-2wKZuQfRZDmnEAPLmoH98IsuSkhJ7M7DlBV9PqqQo-KPAnv46JgCe9KoeFkYfdT6XocouLva3-pCizK9GRLV-TL3PDCnqiivmklSOOJqkYJpZgSnpbatxCyrPjFTZ9gm-nSkgSwjXZid3AXKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سالروز شهادت امام رضا(ع) در حرم‌رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/455822" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961b8b3a3.mp4?token=CXMzzwDrqTP4BBxQFORhsPCFgjMZTqlI7uA0zYybNmLVDK1QJKso03Sz4mamYBwVGubjA9WnM4W5BpQdG5XReeWSzOR5Dda65cH69n17X4cIeJ3fsJDYWnWphK8K_ErsD7CLTEgbDP6ApZ7b8kbEvNPuKvSdK026vhJWbQNgVEX82lenNYeH9UdchHyasbA0ykx4oq6zNjRiWV8GpUoyFPWJCApwp7hBu-SgupxraZ0tFPmfREGSt0C7019GOF-y0psqDGPOWImdFoS1Kd5_1W1V0tmzquF7dwBjNTg5AfcGgaBYEOhojaKNlBexZFk5n_jNH_xBfw8FCi6tKMWs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961b8b3a3.mp4?token=CXMzzwDrqTP4BBxQFORhsPCFgjMZTqlI7uA0zYybNmLVDK1QJKso03Sz4mamYBwVGubjA9WnM4W5BpQdG5XReeWSzOR5Dda65cH69n17X4cIeJ3fsJDYWnWphK8K_ErsD7CLTEgbDP6ApZ7b8kbEvNPuKvSdK026vhJWbQNgVEX82lenNYeH9UdchHyasbA0ykx4oq6zNjRiWV8GpUoyFPWJCApwp7hBu-SgupxraZ0tFPmfREGSt0C7019GOF-y0psqDGPOWImdFoS1Kd5_1W1V0tmzquF7dwBjNTg5AfcGgaBYEOhojaKNlBexZFk5n_jNH_xBfw8FCi6tKMWs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیغ مجمع تشخیص بر گردن بانک مرکزی
🔹
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص:  بررسی سیاست‌های پولی و بانکی در مجمع تشخیص در حالی بررسی است؛ هدف این سیاست‌ها، اصلاح ساختار نظام بانکی و به حداقل رساندن آثار منفی ناترازی بانک‌ها و عملکرد بازار پول است.
🔹
گزارش کمیسیون اقتصادی پس از طی فرآیندی طولانی به صحن مجمع رسید و چند بند آن نیز به تصویب رسید، اما به دلیل شرایط خاص و ضرورت‌های موجود، امکان ادامه بررسی جلسات فراهم نشد.
🔹
استقلال بانک مرکزی و اصلاح ساختار نظام بانکی از محورهای مهم این سیاست‌ها است، همچنین با توجه به تحولات نظام‌های پرداخت در جهان و شرایط تحریمی ایران، باید مشخص شود کشور چگونه می‌تواند از ظرفیت رمزارزها در نظام پرداخت استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/455821" target="_blank">📅 11:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4fVby-hm42jvdW8Olb5bv7RqnSphlpXzqMwstuoixUQdMKWGZhoQbJQAaZZIIlYc6emj6WVlqPaTyeVnNVukjELQ-qcEK51DZiWWqwMmznYIVu-KJoCAX9Cv0mKO3N5p7w9LQQ69xPhmayeQkFfW_waPIJuMHT_R7OF1pq7NG_OPH4JgfaFR5Z2XI3G9Ckfl6cu80E88A5GY3Pzll_5M9lnQwkb-AS2STW0J5DyRs7GTnPvAEXy3DU4-UtzPFHHMCXKalhvYDJEj7ZKSfd6gJ4Rma-TfRwmHv7CCM58RIUAhL8zwlGuhzYe9zGfNkv_YeWnEVyIAdGkg8Uio03Tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طمع ترامپ برای درآمدزایی از تروث
سوشال برایش دردسرساز شد
🔹
دونالد ترامپ به دلیل راه‌اندازی سرویس اشتراکی که تا ۱۰۰ هزار دلار در ماه برای دسترسی زودهنگام به پست‌های او و مقامات ارشد دولت در تروث سوشال هزینه می‌گیرد، با شکایت جدیدی مواجه شده است.
🔹
شاکیان این پرونده، نشریه اینترسپت و بنیاد آزادی مطبوعات هستند که در دادگاه فدرال ناحیه جنوبی نیویورک علیه ترامپ، دو دستیار او و دفتر اجرایی رئیس‌جمهور شکایت کرده‌اند.
🔹
این شکایت، سرویس «تروث ای‌پی‌آی» را هدف قرار داده است؛ سرویسی پولی که اول آگوست توسط شرکت مالک تروث سوشال راه‌اندازی شد. شاکیان این سازوکار را «بی‌سابقه، فسادآمیز و خلاف قانون اساسی» خوانده‌اند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/455820" target="_blank">📅 11:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=SkJCkKZrgTJyiHLVUb_Kd9Apq8uORgVhG2iJ6IbPHIx3m4zPsYHMcrfnYCW0TPEwL6lntYheM9vc2EagymzW3E5t-31TuILINrL8vbD7txpRbcaf4AJhlZNFi1exfH4BdzVUOFvv8xr6Aqn5T5vk3fKafxVOvvZm51j5euIXeQvvTYaUD06O-2nIglV54GXIy1x7ltHSEYhWjYizvPHDnwFWYzfjiZF9eX4D3Dswac4Uii2s04XpN1RG5udWTayRU6f5XuEBxgRqPaVF59XNFMtYOBIKpHVcHc3RFWVms8vaCRjdSk0gYXzAT8v6ggj6bJi43zHflHBZ8JZDiv6d6Fakq7QtK0pEQxuItyj-YACS3Cy68CFrexJX-051rtP6A4_JVX1oSXUVjxZx9tPCjlKk0QXCy4rq3opWByrqEMKWd9JEG5d83kMw2uYimuY-17ckDNf09puBvZwyIvLScXNZptlOAQtLld3jvyYM_TYWwmM0IetjPT5vcviwTDkCJsxtcWMx-iMvfdUu_JQM0LS9vcU1YCVTaDC3g0GXidSPOSTb869vPgyCfsi9qSA-6H7oTief7TDMnQRfk38O437buMPaPD3sle-eYgJM2bxujGg74pyY2X5O9etzWNcL1sUKF_G1Z6gHy6oZ9Ywh6PiMsZnBFb3ohm2YZHuwHII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=SkJCkKZrgTJyiHLVUb_Kd9Apq8uORgVhG2iJ6IbPHIx3m4zPsYHMcrfnYCW0TPEwL6lntYheM9vc2EagymzW3E5t-31TuILINrL8vbD7txpRbcaf4AJhlZNFi1exfH4BdzVUOFvv8xr6Aqn5T5vk3fKafxVOvvZm51j5euIXeQvvTYaUD06O-2nIglV54GXIy1x7ltHSEYhWjYizvPHDnwFWYzfjiZF9eX4D3Dswac4Uii2s04XpN1RG5udWTayRU6f5XuEBxgRqPaVF59XNFMtYOBIKpHVcHc3RFWVms8vaCRjdSk0gYXzAT8v6ggj6bJi43zHflHBZ8JZDiv6d6Fakq7QtK0pEQxuItyj-YACS3Cy68CFrexJX-051rtP6A4_JVX1oSXUVjxZx9tPCjlKk0QXCy4rq3opWByrqEMKWd9JEG5d83kMw2uYimuY-17ckDNf09puBvZwyIvLScXNZptlOAQtLld3jvyYM_TYWwmM0IetjPT5vcviwTDkCJsxtcWMx-iMvfdUu_JQM0LS9vcU1YCVTaDC3g0GXidSPOSTb869vPgyCfsi9qSA-6H7oTief7TDMnQRfk38O437buMPaPD3sle-eYgJM2bxujGg74pyY2X5O9etzWNcL1sUKF_G1Z6gHy6oZ9Ywh6PiMsZnBFb3ohm2YZHuwHII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از آلودگی نفتی در سواحل جنوبی قشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/455819" target="_blank">📅 11:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5dTax459NLjdsc44tq0BVzS35nOHV8fxSz4bdnUUY_dNKpHhRI8VvXRU8u5wyVVRi9ExWEp_6GetxAxok8mtfi89xkuNas8GwiRvKaS8FO9uMtZYw8jlcBbLXZPR8u07i1wBlm_CwMPeyxz_rOPdYnyzATQRKAlnTqQ7H5FFYweBqTksuiQK_fi1HBHcjzGK2HSS4eUyDkNWRRWC28_nEwNqavr2oQQ-WsfAyGq78InmqTPxgHYqzFlanEn4JfNYqx91GCtBabDydLi9qqlTThB6scOS7mjF3iMk5QGDt3-XmXJhDXGWw4sVbuJ56R-e38QL_8r-UQSjsGRhUzt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آمریکا در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی بزرگی شده است
🔹
آمریکا مدت‌هاست که به دلیل ضعف اطلاعاتی، دچار اشتباهات محاسباتی مکرر می‌شود. جنگ علیه ایران نمونه‌ای روشن از آن است. اکنون نیز در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی حتی بزرگ‌تری شده است.
🔹
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باشید.
🔹
الله بزرگ است، بزرگ‌تر از هر قدرتی بر روی زمین. ما بر الله توکل داریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/455818" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
آمدم ای شاه پناهم بده
🔹
نوحه‌خوانی در حرم‌رضوی به‌مناسبت شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/455817" target="_blank">📅 11:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دستگیری ۱۵ حفار غیرمجاز و کشف ۲ تُن سنگ طلادار
🔹
فرمانده انتظامی کلیبر آذربایجان‌شرقی از اجرای چند عملیات هدفمند علیه حفاران غیرمجاز و قاچاقچیان سنگ معدنی طلا خبر داد.
در این عملیات‌ها:
🔸
۱۵ حفار غیرمجاز دستگیر شدند.
🔸
بیش از ۲ تُن سنگ معدنی طلا کشف شد.
🔸
یک وانت نیسان و ۸ موتورسیکلت توقیف شد.
🔸
۳ موتور برق، ۲ دژبر و یک بالابر نیز توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/455816" target="_blank">📅 11:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrgHHIiX0YXm6padaQc5gdkPaMBdi3DrOqZLAXo8ctILJUvD2suQn-f1Y7fQsRFEQn6fu3X0V1NMKQqjuq5SZLOs3dUUb2jyk9xrCkMn02zChSWWgsJcxx96hFHWOAKyKQWmYAqSN4uM7CuI6QT-AMoFnf7VkiHJEpspAPlmiGpSP4iiEWkNXNzYv78wCBh5vC_g9o6wYFmhZFGOuTL5FHW40bZbEVMNeSzjW7r3WCSDWcoSD-cgHSBw3cfA3sSproAvvSeyj9hpSmQ-D_PMHyAPYE9ePbMo3lSVY2VL6U9jBxGCR-narMF0gQH0ln84c9x6qIx7ylqdnNzCQMJMyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙️
گام موثر بانک صادرات ایران در حمایت از اشتغال/ اعطای تسهیلات به بخش صنعت ۷۲ درصد رشد کرد
🔹
بانک صادرات ایران با اعطای بیش از ۷۲۰ هزار میلیارد ریال تسهیلات به بخش صنعت در پایان بهار ۱۴۰۵، به نقش‌آفرینی موثر در حمایت از واحدهای تولیدی و افزایش اشتغال پرداخت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/455815" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioLQsq9fQf7fMLShzVy2ZO7_FFrSyoUkGhVsdN6sumyHUve0P1x7Lxz7M5Ik3saZC4CJQUhmTuYFfs2zLI6RYGmwbZfkRRdeDS8PTRzaIkWuVFBepLb_3GD5hx9yhzJ9QpcL1D4VzjufrUisgdIptOqoRfkrYUsZpMY690N7zpZD46d_1SkYvregAgbyFg0YIyJ7Sr6eiurThszVMOchC6FO5R9-4G9Yo6LoAhqYVwT6BGHfigs1VsqKJ2ZCcjHF62oWxaD1H8JkcIXpuuLCdvuFkdDS7bhRLtTD5Dn-eAIwcVEk8MHJFXFgYW1cErsyQJrooQeZGOfB7MU_xO5k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ فروشگاه آنلاین مذهبی که ارزش یک‌بار دیدن را دارند
۱.
فروشگاه موکب‌آرت
۲.
فروشگاه پوشاک معراج
۳.
فروشگاه ربیع
۴.
فروشگاه ماهد
۵.
فروشگاه مغیث
اگر به دنبال تجربه‌ای متفاوت در خرید محصولات فرهنگی، مذهبی و ایرانی هستید،
این ۵ مجموعه
می‌توانند نقطه شروع خوبی برای شما باشند.</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/455814" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/455813" target="_blank">📅 11:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cf91335c.mp4?token=ltAVCHAXbkBGf6QeVH0aCTZqU2OwkxqWNynuJf85sfhvMDoBZiQ6DAWmdqcZYhwkhhML04kiYsjRJ65uj4P4QJc1C7cxAU56srYWrqX32C9FU-SfUSdN7x5PY9Hnkn9alNt3V_0m2SQUtI01P9gDIYIwRiWl2NUVtqsgtUspdc-yJ-f3lHcLgDQgLUb4foqVDJ6TZGqjTNdILvuQ-tFtuRyyFmEi--iezJVSrsGORpbcABSh4aH86jASnn-MgMWIy_GWh_uRoBXI87dWJ5F9d_O6PDWQA5U6fLoXCJdVoq14mKVruvoyMcija5qb5bgpLmgIMiLmL9JE7WCjirEcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cf91335c.mp4?token=ltAVCHAXbkBGf6QeVH0aCTZqU2OwkxqWNynuJf85sfhvMDoBZiQ6DAWmdqcZYhwkhhML04kiYsjRJ65uj4P4QJc1C7cxAU56srYWrqX32C9FU-SfUSdN7x5PY9Hnkn9alNt3V_0m2SQUtI01P9gDIYIwRiWl2NUVtqsgtUspdc-yJ-f3lHcLgDQgLUb4foqVDJ6TZGqjTNdILvuQ-tFtuRyyFmEi--iezJVSrsGORpbcABSh4aH86jASnn-MgMWIy_GWh_uRoBXI87dWJ5F9d_O6PDWQA5U6fLoXCJdVoq14mKVruvoyMcija5qb5bgpLmgIMiLmL9JE7WCjirEcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریکی تاراگونای اسپانیا در لحظهٔ خورشیدگرفتگی کامل
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/455812" target="_blank">📅 10:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF-4M0ieQYqjfm-_DW2CBNcwFNz0e65NuEsg8wX34Mi7L-5OWA7sFWvN_m8VKX5mJOYRAfx8U_XTi7qHuRLco6TZ78RCm6epffQld3abQkKZ7062nJ7emUzEnfelIMCCWlmct5s1u9dsnjFqVGa9s96PV143iGPVKEAgONQymsQ5XpI-xipzVt7EbsJOmkCtfRJY53Ae1847v6FJmP2B8cErNc6krpyDYxKHjPWq4QHV4veEKQGFswHEBPBy3CCkKFdgCPXsXfYgXoscrcpGNECY4lvh8Lv4PCQshzxX3wwBJq_mOV4J22-5FcWhMdcntScF17bjvemkXOBIpqOHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزیدی: عراق پایگاه تجاوز به همسایگان نمی‌شود
🔹
نخست‌وزیر و فرمانده کل نیروهای مسلح عراق در بازدید شبانه از مرکز عملیات پدافند هوایی، با تاکید بر نقش محوری عراق در امنیت منطقه، اعلام کرد که خاک و حریم هوایی این کشور هرگز پایگاه تجاوز به همسایگان نخواهد بود.
🔹
علی فالح الزیدی همچنین بر تأمین تمامی نیازمندی‌های پدافند هوایی، ارتقای سطح رزمی و فناوری، و فراهم‌سازی مقدمات ایجاد سامانه‌ای پیشرفته برای حفاظت از حریم هوایی عراق تاکید کرد و گفت: «آسمان و حاکمیت عراق، نمادی است که اجازه نخواهیم داد حریم آن نقض شود یا امنیت آن از سوی هر قدرتی مورد تعرض قرار گیرد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/455811" target="_blank">📅 10:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31a9e4389.mp4?token=s50FX8gimS6_u-c5nNJ03ircAFV4fUMFSDhwga1MDnvZlIZiFTKezhtvo0s9wR_SNonb-eBQILwSpgRiAWGPOMziBkruae6ESnP5vsccFkpgp3o5x7IINgifbbfHXgVL8BMP6V6vOxpvi3BUXPw9woSAGVbDYXnjlTujcUYU5HfNw4_-jJUv2yPUNNi5FmBi6vVu4DjFF9MdzKUJqTWj7QDj9dt5bwlPX1BnQE3j2myLtVTWhrTdrrLfNdHwCBUCzOZVuNVZwGDXH7azXFjZxT3GcpqEanTwyMgMTyjKs7CykVJvzIzbjpHySi10e7pg6L8FYSN_tsh8bxVvv3tc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31a9e4389.mp4?token=s50FX8gimS6_u-c5nNJ03ircAFV4fUMFSDhwga1MDnvZlIZiFTKezhtvo0s9wR_SNonb-eBQILwSpgRiAWGPOMziBkruae6ESnP5vsccFkpgp3o5x7IINgifbbfHXgVL8BMP6V6vOxpvi3BUXPw9woSAGVbDYXnjlTujcUYU5HfNw4_-jJUv2yPUNNi5FmBi6vVu4DjFF9MdzKUJqTWj7QDj9dt5bwlPX1BnQE3j2myLtVTWhrTdrrLfNdHwCBUCzOZVuNVZwGDXH7azXFjZxT3GcpqEanTwyMgMTyjKs7CykVJvzIzbjpHySi10e7pg6L8FYSN_tsh8bxVvv3tc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستهٔ عزاداری خادمان و زائران در حرم بانوی کرامت برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/455810" target="_blank">📅 10:32 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
