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
<img src="https://cdn4.telesco.pe/file/h-gvLBS3_WEOir7T1VuDkCGEwFaLuWplxFamZpQnQkgUs3Y228_R8MX40yoMwgHyDhewFVjaHssF5gJKvYBuyLft2g0HGO3oqRB_s8QY1cR7d6V0XCWC7Qzj6mCSI8KnlK4L4k-bp_LdOgjThIQtyZl1nG9HtCLekHpTAt-BM3Ai3YpWw77XK3Of3jTOj-wF_gQ-0uVHzTUnfrtnyHc7NrCRw4tqaQRIXeQHOJVdskspMHehlho6OH5PgfwWltzwv3RLXqc7T6Fmb9T6-s_cxs16P_60lrYZOlZgi2md6SulGr_C3Dp1J05vzSs50l3WxSIJlKNlEodCUAT5lN6QsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 179K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 18:20:33</div>
<hr>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh_G3P5tCxtTnnAxbgbAoLI_yNTu65ryFvhy6-64rUaKpHZFYRdYkHWM3HOxZHmF5BbhRSBrjSa-td7IsCKZJc-DzzKVIgWY_uB4Q_AVEwitfRXhBZ8wlgrGwerd8vhvx5YtxIXk8kHJ5UWMDYYjPqlWtqoek2hxaWWxnmD7Bt0m1HP2h9EYugHeJyNVqDwvgOP1r_2KaV-f-uwHbg3d9qsHv3HKWhh9h6LZuiHlfnnfvyhNZ5X9nlG-CFveNqz7abc8gqR5FXK6vONl3UwuAV5ykkn68OKFkGFetiHNBIhlZ3lFf6Wrl06JuI_jvxvh_1znQGxVuyqd2HGFla5ELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoxC0d5ktucUyN7nU89A5vK18vYkgZbORvhSEodWxhV5ZZlLV5nbf-wJoQTZUmpZdpUHLrUQcoBBTo81ex6cOiW-DWfq2mnp5_NEszaSGXN9Y2MIfkcq_t8jjng54CmgkJ6NLdCFgW8-wwXDB8Rubi4KigSHDvGir6awZBLAOF8VcMULkiTqb7Pt0ED_okdbgiLG-_fEDL20_yZTF3xgHhM-ZwDB3s34xztwOGcmOJ57WxvSd0Y1vAsdqKbFR8CziZN4-eKrDzD_jtBPZBJgh0oO3x3gcVUOnflrQ3G6GC2AHs5ZHGxddeDfworC-aea_T2r-OREI6Abgb1TJVUBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌ترکیب پاری‌سن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4_0gv3ZHLoQ4zmVDyoBsibeTnVmDrQSkXloj_PbwML00isB2UGLpWU2cTKFMqiVGtKf7I_vcKrgd8zioN7jAeEHYDbVNVRRnfqXQL-oWvJ9QU0oSQUbAO4gk43bdhq5TBH5ujD97oD6wofBtb01kJtlK2PbT9UiPDZ8WVymDYFjJXaZvDV9igJLkfpCi-FtsdIXp6Ey8FiXGXOqH3gqXRdaLFNInLrAacv6jwmbwX4k5jDhzKpJ2_AgJvmLCrhJrANKGuNa8QSYGA8oQ5rL7Qzy1R4pgiSIb73qhLNhnMcf0hxZSvRjCIODS1ujidEmp8xNSFGHCqSLDfGlnolyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6GgJGt--H982H2SB2Xpjh-Z3zwBpa5oM9NHYLhZSmupwDPuix5lMPG814AN9d09BAYO82KWzABYCt3R3r1bMG3ay4cRkTYAUgchQGBHNhjbsVy6oBSvJPo3ybURtU-o86v3fmci64mANXSkZOXGSMnC0mYa9dWZYJvPSsF6fV832GMpyQ5cY-QYKYG3BfpRajoY9y8g4NEEQySfUtAM3UH3J0jmiCv70xKRPgN5tg_umvT3I29xfI46vgO2W326SDuJ9qEAkjhps1Em1M-h49SAu9to0LLfgyUyyfXRe_DnbWHJ76IdP7Z0wMPsybPvETi6nboePbj21PNieOb4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATWwUcNBah5L6F9Ui5qiLrdhFbmFiFEaQlJl0_eYiuZUvLEcqXPC-q56amIBneYIkhoydTBrAfd_2mzrge-6Rw4owUyZS_x6z3dZU1Y19IdhxD7JOxujUFP55lJK71UOGlpWhhnjSr9JhJBfhOyOjohP_4QPyNSs7SFsMUUfJPxOIWmEEsb-b5xylkLeGjEvTvc3gKNRpafho3WsPh_fODfFd5QnK2VxvnKGuX9Wuoy1KCwoML0RSFt3EDLo0onz7M5CeqFL3KhJbQ2hXsszXbK4U2PlIGvD1g0brqlwCVqDUjqpmFLxXFEJWi3N6TDFp_fpIK2PvKZLNcSaQBI5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSvGjygDAp4449rJEQW5fI8nqGJvMzSu6Zwa3okYa7VPaqFaNnUxOoFZCs1VwHlxAQiY2uaikTV_j4swllpbkKemU8ceFMVEZLNnxKfBCHjn1ruXzFbyLshXNISdnX2X-dOFRvMP_NjOlyFjcKj51cWGQGHuNbPeiJXzFP-HUXvKwd2jBR-sgzQu8U0D_CSoISnOPTPE9UxL0N8vN333woyxK7qcmx3UDgtlfb_peg_VkZe96KDJPeiIUNnNV1yGaGsicn4a7ZXCURx_HR7UmhGOH_GbA27Cla8nMWoktJeTMf9kcUzgFV4ZKID5Y4KQdILjNLoSNJTX2eJAsnbK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=TVrK46o9JczB8i2CXvAQxCJXwQU1MRayrmCBKDv6PTtyIDzLnxP7tzo5UI6tfY96TA8UgF6NVFysiDf7j1f-TumNvuWn7ad3ISB7m80EmT6NWjU2mfn2LGeld40OgLwckrgbCN1U-EzDi2WuoRVmoLJq1eues5ZXopd6elsGM3uXLNfxBMewYWBkdnKmYTWSxl5jJc8ZzZu-abSHDlxMTj2VH9gLiUh4NuoioT9UI0gvfLXc4l78yvUtCyd3MgiWw1SDMj64LBxLL-l8slpHAioWEv4ivULZT0IoX6DZhgwVPS7B94DDqCVP3C8abLK_OMt1YoPRaGWRIpxiY_UVbphO3UQcMZRBvhanELAH6ELuMyqxBo2srRF-J4gYpPORsbH4se5RJwUsWzjHh4LDHjMKKD3NehPN4wPpCCLArrmsJRYrBJ9wXqLnvKqEEZpKWbPSGiohRUa8Y1B05KH1qe4V9FTvwUN7rvLhglbBnpfhRaOAQRdJkm2z5gPyTLGihCTejdn3PNYuMIakUVb-OUS3z3jLhOBE9yshGz23BvVi3IOECRuo2W4v7mizrp5WHB094AlVPog3vzAYiG4usO6EfXC35Xbz9iam4LRG-TB88h5p-GOpvHa_Qk89zG4EphGum5T8VPqOxVE8vkvsf35R-OTAkAVyvvd6MT3K9MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=TVrK46o9JczB8i2CXvAQxCJXwQU1MRayrmCBKDv6PTtyIDzLnxP7tzo5UI6tfY96TA8UgF6NVFysiDf7j1f-TumNvuWn7ad3ISB7m80EmT6NWjU2mfn2LGeld40OgLwckrgbCN1U-EzDi2WuoRVmoLJq1eues5ZXopd6elsGM3uXLNfxBMewYWBkdnKmYTWSxl5jJc8ZzZu-abSHDlxMTj2VH9gLiUh4NuoioT9UI0gvfLXc4l78yvUtCyd3MgiWw1SDMj64LBxLL-l8slpHAioWEv4ivULZT0IoX6DZhgwVPS7B94DDqCVP3C8abLK_OMt1YoPRaGWRIpxiY_UVbphO3UQcMZRBvhanELAH6ELuMyqxBo2srRF-J4gYpPORsbH4se5RJwUsWzjHh4LDHjMKKD3NehPN4wPpCCLArrmsJRYrBJ9wXqLnvKqEEZpKWbPSGiohRUa8Y1B05KH1qe4V9FTvwUN7rvLhglbBnpfhRaOAQRdJkm2z5gPyTLGihCTejdn3PNYuMIakUVb-OUS3z3jLhOBE9yshGz23BvVi3IOECRuo2W4v7mizrp5WHB094AlVPog3vzAYiG4usO6EfXC35Xbz9iam4LRG-TB88h5p-GOpvHa_Qk89zG4EphGum5T8VPqOxVE8vkvsf35R-OTAkAVyvvd6MT3K9MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDXDNySxefPQf5ya4bJWPWltq_6fBrG1dz9ugCEux-9Llr7ZGNHgROD3xGc5uuNNcc-ufoeJC1R66ntajX_efL7RVqsGyVVhNxePWwLgjS8KnQ6CR112ogI8mYwI1hY9MeoD6bUu8p2_hzYwN-14Z-JzKhIpux1DbWcq7P6gqYNsnWZMIH9F_obRJ78piv62LlOSqA-ZQmiTdpJZl1Qa-MMdEFKft7IAqPpie-YmgZ60pIxiPnI8T_2xeRZT_oCSQ7NapfEDo7h27pIQlgLHKNg3DbavtTcM0zKkJqM_MfxT1-pNsIAZREsDn4daEal_3GBi_B2Y1VzwvUVyB33m4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4wiCrvO4MB_h-u25CsXKYKTtpah5zo59BdJrYlfv6gaOgVXJx6LSwZvoUGL9AwpZAs4poS4ZoeUfzHhC2j8a4unGZnj05FnUVN64I21fcNKl6hLoL0r0a3z1UW6zvsNyT9TVxdvKUQ6IyWJ7kqC0MEH4jMrL4ex7XtaF2vKiSUelmW84SbrT0nKQ9eordXYtdLhyX2QQOFt5tgGRbxQgpQrgxL61sO6rd0XWtyZkurdlNB53lAn90R14E41WvliZg7KP48o2hSqLKVG4ak8xQiqBKwHH9I-LywLWSiVfRwpWo41nZUn9-J7uD1TxnzPlkCz7qGMhTREu0P9b5r8AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyVZ3brrj52Fkr6XAXJ2QPB5J6jZh6vtgWN_ctMidwtt_z6FdIbe9cEsXzVDhJ8oM5YydOhNJPO5BHYV0k9mODZEyGK-Mfs66tmGH8RtFKLyEDFXL8PlvoXDqQpH-UTBoKBxzjS4h_S4Pg_Y59s0M18TlnoRLTRfgoyVdOyyNxIb7hpigVS347jLOjaB4Xgjqw5A7-sC6fYeTnWCLh45gUgKB7ih4pxPgrmk4TmUcSe5T2uURzyQMGWdc_XbiRG2Qc1yK9CxQCwIMo3XrPKEC9CJ3u9CZ5Pl9ka8wuwu57Crn3cSIpOFTmwvQdvn0ZU1ckkJtQHDhcn2uqrjwJiq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=hidJ0j3SckPYEEv0_QvQb3xw9FgefpRHWKsPBxIJadSzOpxzVbd9Abrh1k94xh7UswOUWg9VQ_gBhhw4NEbzPUN7QK-CbDS5pdJ95Sh9iO08gnVzRlPjRh3Fgx8av9Q56DR12aNwT9Mnd5AOQzKgvff_tRT5BGoHzPzqpjI8kl5GGOLa9tf46qiysZ9laley3U1FFI1fUh8JN1cz9BOUnOQK0JKAC7btYqLqfRnuM1Gd4U2k1zJAX6V7y4iJX3WSXupFeuga6WeHYwfPtZ0SKe7vqKS2_Ybl-tLzV-kYWNtTUxte8lu8khXBpUGGvNBJLgJk_-Y-9LKHUcGajtCkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=hidJ0j3SckPYEEv0_QvQb3xw9FgefpRHWKsPBxIJadSzOpxzVbd9Abrh1k94xh7UswOUWg9VQ_gBhhw4NEbzPUN7QK-CbDS5pdJ95Sh9iO08gnVzRlPjRh3Fgx8av9Q56DR12aNwT9Mnd5AOQzKgvff_tRT5BGoHzPzqpjI8kl5GGOLa9tf46qiysZ9laley3U1FFI1fUh8JN1cz9BOUnOQK0JKAC7btYqLqfRnuM1Gd4U2k1zJAX6V7y4iJX3WSXupFeuga6WeHYwfPtZ0SKe7vqKS2_Ybl-tLzV-kYWNtTUxte8lu8khXBpUGGvNBJLgJk_-Y-9LKHUcGajtCkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4TMCG43B5R0YD_9dHWkWZg1KO5v8O4OZlqIELYgUSiL9fawZh8snx23KcmRjguEb66mBvECB4TS_Nd3uOaWzaxNj4TJ2KRp5sWopEikcwOLHI-AlZ_8R8q6ZCCm1rWpQWpwqohggVCMuKhk19lH1TIOF6oNOkd4yN8jO-QgEf5RLhPPS00QTVqtbOtG4SdIQuCX2oKrzaJ98DoeDiE47Sd2yV-V82p8O1oY7lRWL0BkZbVLV7LVsd3OIsaw1c3ngnZUSRMYa9_E2AfrgCQX9w7T5YJ2K9vYUJhtt4n8W-pVeT7p-CvbtWwOI_Fqzff2IXr-6Fd1X0Dg_Kdqsa-6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvzQxe5BEwUDwSZuhgjqCwKNl8DpMKj6N4Er33mgQqOCBSc3KpjCzdR87KsOlmPVn3_UjSudZ9LDtYoPr0_ljj-06NRQczYvVV_-5Svpjn2Tk5WUlknhW4jdsw13UcUTEQP8Ms8RhpEDNiExKT1nBu9RmGowZqrIr6COhsCNQG2cwTR3et_SUN1WANJ0ZyQLTpiXuXjtf2H9xwP1k8PeYJ5ECjmj--GR-KkTU1WYjGssYhiXJd_0w_gnI6ZLZyCyt4-vd_O-XvFzpiz6gSEND9KMxs8qsz2oljVKXRZ00st6QhZOXsJvXz2lAsV2RWgzvyE8htkkpqQa1vQ2E9Xa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFcS1uqV6sUBTRBBdl6_OPZrayAS7JtEVfFmZ__mjImhRRWCodZcm4YyyAZIlwvfD7qKRG2PTO8Qv-9QXP-oeqlSPJn1w15W_nQdgygCJVXmywc9Awb8OAs0-n0T1LL9nvq8__PrDvjUvwims7SHJZSLMEaOqUx0Al8HICR9GYH2UtO8mZjm3uYTnbbQlNDLnujdYyw272bvh8f2mrvjaNdwSbBFUvBy2SxBRFSKDmLwo10KYm1x0fmjDUTI02NGpd9g6dmmyois__hO48O-oHSralqaP9-4SvZ0cemIiIOHppREPrtsiyg_6gAkJd5UWZxlw6eBimFLqu9afe7n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzJ4bmUsr8PB5yC5tJZGh8bYErnfsm9uKKORBwlejmLkUxt2-MKrDso87AT3sD3igkG7ocWGV1QJov7lG7ave2K2J5MOjSDNOwV4nAbxjsaMJCgmkcACiHbCcyI741-7KhQJgMZxrWWkyvkexN3bBbtnPAXeIuO9cjmXe8kpRJEVvlyFLcFhOvQ_wisTGN5tTzWsJS2_7CwMH-bs6xnXvn5cimYmRMbgrHgprGfl-PvZSlLJsnFv-USCFxQv6-IHkjNsJyXyzugytiqlM8735YTbQj2zUUYEMg1BS6THy2Qvf68UxKq0MjNp-T4ei1IgG8VpBj1lx3t47kD_YRph4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRhdZaqYvOwCFAwiFePERFG5ZyEm4hv95xS_rTkgxRVR4JC2yxjOsVTwKGsKnUURlcPw7dbKX7CU2aIMGRl3wTZ1R4-Xd4HjHhVk0eQIXFEyHN-KU_xbtd0fv7yvZ-7rjs6B8eoEEhSIe915VjHSsPBa3cmbLzvvRUkz9DqNU6Oscf6mWcTUD_S6i4AfkwoKd7YTT6ZJg1TkF_uHKyOTDuGJvhNgkynJz9cuIYa4Qsvi5sazNyw86I-o4MsUCdnHKTRJzfq_4DXvkL1bop4I-KKRfmfEtG5VXvKnZOruLV4fIWPl3M4UZEfCrWQL5Rt7f7hE8ESfR4dbkFX8TDtl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkK9XxkCrgd2eEsWxN8RqeM_Dv7T2omqsZCMmOOhsYuDGSSswbJjmBYukPgxTqnnmstLSqDhBydLm9xkGdesIdAyDaSgRkg34sLoLrHlDfHBx0LwMsYN7OkUd8EQ8cYNDuTgjO5UxCvtU8eUxhfy7EFWGVlgi2xxCLp3mhkcsgEcWGr4cKRv1V_mdxOjT6-_rEx8lPPiprOwKz9qB7VIwXWEfB2pHT-YKhgdIaTRzqGBJRBJshaKbP6_DsEE9fsWerdzJ4MivsMkuA1Cj3snzl5PLIAFGo8UB7ylSvpGXRN5cbf0-jeaEQkMdGOnxOaJROgrb7Nf8e1uEb-zuPDWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDR0526y7zAjg7woTf5dIRqxl8XR_Cs1gwZGRr4Lq4vdXngZEKMRorb8GLO4zSTQPN9aknrexuj953XqINOvUVWHwW9hWbGA9481s7zRfm3NRlg_EgI-9LbybnwabpLqVORBBc-O8n05mPtEdZ3R09qpJGSFVJ4dEhwEyBjnCzzjhfSwAqCr-hBBhlDr8pO3VLGEQnuWnb9Fvb9laATb9ukVh9XsWEEfVgDccWQd18t1d5sjteyU7gJ-VBOKy_9kPdBi2NRsWkXJuuMOt0MbfYFygQOxtTPa2FpKpPIOPv7gxZFmmWmOOehk84OYv32cJekFVhSO3KUKuFmUYbhAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRMV7MWI8Bi8WAxgqJm59O4bVTzxUAB7Q6AUXuzDgXGGV4qNAXgsXNFV9a_Xq1u18GSCCPnmWnKbSZipH93toWk9o4U-42k-LSoB9PtmwvSvI90mFstH-zdIy9Cc_y6emZsUmbh3Xyt_xuoYjMK0Ddq4l24m5PRRCcdRCfr4X3AVnExPZ2jZZq-qg24M2VaFilC57ZwFUndSHwDdPVSaKmliKIpB6_wKt_rvHanuSo4wbrYBuw_o0GnImgUSUaM9mjTepMUKFz7xZgYWzpQwpIhQ6TluZxTYEs11i7fPZ9VyW59_rYysZABV46Zl0t6BWcelJ16UreRWJGxuo5LROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAGOMxsnODGEJDxfIyeVVFI2bpNPQlSBkaygnzKdfbvFkanuLFf8xkaPe59VqBbd8_FX9-KWKcgs8nl-tZnYQpcRbIBOzcqDQ8R56znsVzlARlaa2l_02Yci20A0DSjfah5EYL5CCbo5Mkwpkff9GPViat42atvAgIZm_7ZGfZ4T8l55GDU1ZRhOpsf3HPVn8DlmKIsfLPbmkvU7eX5VhAKmUiBnJExsUfiYO2OGPoFsHUdrzNzznQbk3Y8WKGPxKHXlgs0qQQFelLi6LX4b3TuZmHRwa2JamkuxE_n4Am0R7kUnhdo3GqYm2-Xi0c_gL8WilA2QJ0SO_jrmeskJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq5LRxrL-oqcgsfvOPA_cG_DeXguvlBGgoywzVcQELdKYRh6q-r9LdRpGtQ9_2bPOGqHMgK5bPR2s8NYIX3EP6dnUAU4QUXOxOFy0pc8MdcNtLsurqV-QOsjvfa-kruGZvYSAytYdSKI2YfjSYI6uMdNamPdiPxEhJsGmF-EOP3qCpICHKQWZ6lEb3HFwkuwJYqHbFQB2Sgqdi2U0rkJ1UHw0nFGAN_SWCCJgpfwBuXeYUIwTl2RMVNnh5AmUyEpqPUz-Lz4MSqRy1St8eMwwm35bzpSAWIY-G-fzP1n0sqE-Ygocebuzmlnf84oivCIU6-dHQQdRNtRCCl4Hmv1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjYwUAdXiXV5p1lyfXx5y0YU0DvjW4tWXfj84tT4QehDw97ymgAkWE764scUUITdnfP5MnFhMoZSiWVEw21yuBxdOeSTRTrYgnZjNtPmpP6YzcHPoBG2EOYoYUk70njPIknXR3ijWrjWKo5WvVz3DyAgcdci17PxlenyAGnwMN062-eT6qcfw9OTbi-0y0JmP1NR2WVll85nRe89m94AhJ5OkIKT5F8aktpQ1e2S7AwVwM3K8wTjJStXlEwk_lZXAkZAuYl5PHRNUx_v6B6twTTAF_avbrmbeivIXvrS4anXg0XI-ORjTYJuD5YNJUTm8ulQM8lxq1nZRatr8LXPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdhZe88b6eiFbQOF0CG9lYjchIGziQVCsqERUK9xArP2_banclm2NwSIWbPcM-_L1l9js38tITbcfyYSTwMPI-wYm6BhPLPRkCbVbTGKXtIj-dKBi3X-X3ScFbdRxTii_twwACRt7KKPp_IFjVP5m5AM005D4q2ORZCI0Af_o4GAOOndHVa8ur6jDWBNkx3_BJzshbKnMqCSSBOBIeHnvTipoRg_qTQvfj8deh6ho5U5LfyuoNoI-vSo3IwzIJ41qr5mkhk_ttDECEHl8MxSEbMR6PY_-pCDp2RQy6V_H73ZxskEISUICLpEk6C0ckymWZ-tKzEs5YA0ZDcH7Hn9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpIgsBnyA0erTLs_DegSucNbtGUNsC89TFAICn7oaAwq0AlmtvSHepjg4fcKPL4xMi0lX7DWYZOVw7i3B7ZO0leMAk6RHGc-jX7CBna-kJhJ0syOZVrTUseDZqoM-lTDqzMT1BzKBnRBm8IoEEyvRk3bmXo3w2ed5x2R20Fgpz4XGFGyInt8xZOSL8-UiA1MpnOhS361Ymn7X8JLvioVhKbmkqmLxwDEOe4Rx3IhVhL2p7673lcXYYdozeo-c8Nte6FEzsIMlVmoqHozUJnjf0I_zexZ_Fb27dBHIflwxL8q4M4EWGT889ZRpP15HTAlBm6CcvUkYg9eHZnw7pix1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTK39JZnPlACyBJ0j-7UDNygvhd9a185IN_jSdJOt-PqtoiDN4NiSiQqi9JS37gru55Igq5QITa-pyxUwXblVyHSVvCQaluwFlcl6PO0ybdQeP8dLhFkLIJ4Y_2vsKtpCLMkTN3JouNAS-0pwvF7tXyzm26GP6z_qxqOsLHFTQXahz4gvbVfy_wNJZVRtPh1qC0EE6bHq3_56Lud-gP09NG48_UodIunVwyewo46eAGuxP2cY9fzUk1v_UriBbGqJc4IMgX0ME92eYuHyTPyqUNLuPRbw7jfyE2xckFZHFkhqrQjbEhTZgUI1qQxDQzfKfBZMkuFBj0phszIL2JE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OocCeQCDrfVxd2KUE_fyBh9QsZpTKwfKBFfHM4olN39H0VUsf6PPGrtiCcWg50PF5aCOWBNW4508luMd7l5wBOwYb5g_98do4k3fw8x9fkbdluhDDVIX_OZd66HkG7rogMYXLqw5IZ2mzSK31hCoGHRLiS6OkrCt0W3v8pmW5SwoUzaBoaq-1QbLe1dPrmp12dpTmyl3dtuIlFt6iuljxyq7RZ3rHFtSS94N9PRH3QO6KyBOlRFKebj23XJzOQGZ4sNrgEpCV9c2UaxWL7x386mWzR23mSp1Hbj6gOV2ybjKTK9moc_B0mBt9zftFtZuIePL5todQT3SyBbgrZ3j3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfU_9t8iP74dFWmAKbEwklE4rKvCHf_7JyAZwhOj4QaPcCSHpSpxggwsWWPyyHWN-FXn4fHCsyfJ30lw8-lavjzEusvaFJv9_7ZCWTuAx_lcnkDBKJnmtsAuXNkREL9Gxd8WZtNQ7Y1gon_Ymyse0rVM_SDoSHieTACbmFUC8ZiHIiT-PfWqWkap62ppT08euwhIZwss9K_OO9F0pCnf79GMtU3pgrpGJuXVgJNbgSJSWPjFzZEq0BwZI840zHp6u4CC5-uz1bLvNi1KTUyqM9yjZqpLPr4l8fgp1iqRjqNIf5yD0OBJ-MWHZ4benqZmODHCKTQvJCs6jbfFRd11FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au0spLpXee-AaAOi2PCdRzFsbrsxpHY4eaD9J1TMowI2fOeIlmonM4br-Xzjk2Vto7xAbWfRbO4jTGSJjt8VUxWu3Gd-5POYDyQgK9yiESAYF-qVRs_Cm0q7RrH3r1jNwE00Ulop0sM7-Vk7_SLwyDG7EZkOMpgqJCwZbdmt2OQuVubetaYSAc1MtNV0jl215kxS95RO6LnIvcgUPVDR35Yp853LC0EqQm91SpFaNp41RZ_Tdn3rzeyVsYs2o6RhhrSkR8MNjt470BOD8C0MIQAm3YQ4Om8UiqkVRkpMjcWxEvtnsVn5vk1q5wBiF8IccoKlpTW9XHYENfIZWXCpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq6uqzFim3ws79eY1kPfmE2E0PGBhBQXAEZMlFzCdq43PNnuTOqYniV5G9UR4BWKBrOy3NHcokWtPQ9fWGECxhw_ZGkynpkNU0hI8WF_-KpFukvkHhRwJ-ta6j4UjlNJqx-pZLFYilkiR7omOdEe5Uo7FFd_f2iWioPb76fNh6ZKDXsNKyT4-rneUDtylYLY6tMIM15bqg84ykk-48itMxOCo5g8lqYNh7GK56WxwOsJEDwQHlIBbJvOhF7em7Lod1LiTMK6e4dr1vpQNYbUW6VrM9zfitEc5zvFkWOl5F5_S3gbuq8Oq0JrsCtwD4IttkeMg0CnB04dTnruuJJQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2yAwI6HyB4Zw8VI-wfVauz3_fqFVh73hFFYCYcLXd07xNMUqWMkc2SaK4IcL37j2nC2hZBJmofT1_Grr18n0P-vL-nXOuQvM-xunN5UUqkGQvD8JqsMJwFwM-wrQDHuagEjfVsAx-RSgyi_YZoCbK1yky_o238wRtsvtjzdOGEFvMAslKFPrXLcljSpGYoP5P_vmwJvcA2LwXwbnhbip37CdStBGGC9Rs7a_shcwRrwRNRXLGr2A1KVOMbVrLr9AxAZIGq7REQT4u0p_dvLwbeA7V-9W_WDWo5LCfpybsoUfZ3CnQNyG-97EY9gIrqT6j4Y59zhECncVnui-dsG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
فینال لیگ قهرمانان رو
#رایگان
پیش بینی کن!
🎯
با ثبت نام در این لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r9
📱
@winro_io</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22455" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=dCk5isdks51yFmYoFDuUbDPZH4p-e6DYssPyDadSbDNM46DBeb3vIKxqIhaP-EqwQc5Xgm81af1W3nV2_lP549JlSadO4rQ60g11Yex7uGn48s1YVHSRRA_UqAdPL-gZ2jYVXf-3fc3Y02hoLhMyk1FiURe_sibC-RE6WPbJHG4wX67h_p57sETMLm1cgMF_47TIOEEDHKo3AoX0NmTpP3Wazb9lQk8_bRkc3Bsm_aZarPta30uJJKH6eGrQDCQo6F1k6irNblSvl1qQ_Y6wk8oLjJFC_4pG09W3MQh8slDiB7tl8cnmoGDeAyTXKIm5_MZj1ch0RW-BYHMSj2OEln7dUPTyN9wLCiJO7F-u_3b-6Rety5UdVWGK1sG6QipoZwIWFHdm_xRWx2wN-kJk4G2Q62-3fGMSq3zADzAY6bmVwsa8AQRY-jNEgJKEe99oS1NAMRph5RXHmcqUHn9PWKltN_HERJF4Ffmj6zDq0dWY_TELNOGHzZGtu77aCadKSf_DeYRT41JtHt_I0qerexIiKBEqfck0rSVPUYHZofKoG4r7PCDPP8I8NOSaZGjDBM97u36VopglL6C6kwG6ZXOKZqqpfmU_vqwbJMbZGLwHA_v3_565iklphf_SIbfgLklS5NeUmKD9k4XwMIryntX_lVtGTYTYVmGZzs1Xlq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=dCk5isdks51yFmYoFDuUbDPZH4p-e6DYssPyDadSbDNM46DBeb3vIKxqIhaP-EqwQc5Xgm81af1W3nV2_lP549JlSadO4rQ60g11Yex7uGn48s1YVHSRRA_UqAdPL-gZ2jYVXf-3fc3Y02hoLhMyk1FiURe_sibC-RE6WPbJHG4wX67h_p57sETMLm1cgMF_47TIOEEDHKo3AoX0NmTpP3Wazb9lQk8_bRkc3Bsm_aZarPta30uJJKH6eGrQDCQo6F1k6irNblSvl1qQ_Y6wk8oLjJFC_4pG09W3MQh8slDiB7tl8cnmoGDeAyTXKIm5_MZj1ch0RW-BYHMSj2OEln7dUPTyN9wLCiJO7F-u_3b-6Rety5UdVWGK1sG6QipoZwIWFHdm_xRWx2wN-kJk4G2Q62-3fGMSq3zADzAY6bmVwsa8AQRY-jNEgJKEe99oS1NAMRph5RXHmcqUHn9PWKltN_HERJF4Ffmj6zDq0dWY_TELNOGHzZGtu77aCadKSf_DeYRT41JtHt_I0qerexIiKBEqfck0rSVPUYHZofKoG4r7PCDPP8I8NOSaZGjDBM97u36VopglL6C6kwG6ZXOKZqqpfmU_vqwbJMbZGLwHA_v3_565iklphf_SIbfgLklS5NeUmKD9k4XwMIryntX_lVtGTYTYVmGZzs1Xlq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=X4QtD4EOw1OUUpnhUngjtYz97_G7ZBDlc-nMRa3thVGmlAxuRhcan-D2DTqB2Htg9V2b4Bn3EeNbsDfsCR_HtY-xiH2Ta7Y09xaF2vEM1Ot3DiFGmiQtSaeJdbgSqDji52Oo6riHxQ7UzA17XVScTKcBh2_rU8vEHvk5Xikp4_JmHDmjJ0NF4_JMORPfy5Vi8cB8utRqsi6LnmlFTuOOP_a6peBCfkpJm65C5EbALXbuB5qxNc8A5qujBDDnAXEH6ao5BAb2ee0Sr3YffrSGsIZu0xAakPM8qXRouYlJKZG-GNw30eNwynhK6Kd7dcvlHVrLSErADXlMGmefMheK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=X4QtD4EOw1OUUpnhUngjtYz97_G7ZBDlc-nMRa3thVGmlAxuRhcan-D2DTqB2Htg9V2b4Bn3EeNbsDfsCR_HtY-xiH2Ta7Y09xaF2vEM1Ot3DiFGmiQtSaeJdbgSqDji52Oo6riHxQ7UzA17XVScTKcBh2_rU8vEHvk5Xikp4_JmHDmjJ0NF4_JMORPfy5Vi8cB8utRqsi6LnmlFTuOOP_a6peBCfkpJm65C5EbALXbuB5qxNc8A5qujBDDnAXEH6ao5BAb2ee0Sr3YffrSGsIZu0xAakPM8qXRouYlJKZG-GNw30eNwynhK6Kd7dcvlHVrLSErADXlMGmefMheK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeP0IiXNth1VGaH_bSd71MlqkQY4lG766PZDtxnZr4aA6s96JWsPDDcadM6R9ZTuiGXwnUswExrQrdejHppmuTXVxBPgQrxQdiwsXW9H7iv5NqHtLDdyDSNKMYcIu03jC0Q3No-GqGXsZqVzbNW5xbW18yZYJWNLFYfUv3uGQVQKGaQQm4jmHnvww2jZWkeyqCnyleBq7krShf61RcnR59bsZ80ukRRnNyaTINblWra47XIJWNsE0_JNHBon2U-vS1nCSCDspkMfQ-DBF74tLUE_qsy_O1w-0OO8PhR-6w1NQzEm6Zmohpox6YwG6Z33ZvLqeCVpk9qTv7z3rjnQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkwUTfyxclzSwA1EQhuwfW9K1gLtUx3n0iOntRZbVRn2I4nvut9td74aJPGUyt6JrvslqC8HwuJKfHG_TijPHzVSsYp8wj0X3yYGvJSl0OHGhELLon4te_3hRN57gulKQv50K5YIZheFcKlGxFsF_-ZHvpK6AlPqYjacQYwwwM4IMM9YYDYOGOUbmj4O2L_SQ6WLC9r1_LO0eKVJso-Tjz9WH4B0zxjsHu8jCPFwIeebIAtdhXmvklnnF4I5i9CesAeoR1TL7Rn763wXAZfjZC6vw2kp8R4eh_KU6ER6DshEtfRj090UOLb4jrAY7JVlivF0IP0ohbSCHiuCQS4WQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slsRlnx5akXn2EDuC3GUAG5qjQ7Jlyv0geISS1P3yaSV_nNv5myPcnEkU-h3rfVSjwqoFCX11Mo43EOaaFLg8gMRm_2gkWN_Ofq1iOciojHGqzeicZdOaMT3ANU9gqKyhjhmWsG-i24ZERhis2hFtpXwSRblDky5XcLy8of1ba3xAVFcQviKu5sqaIC_BeQCQzbmEIJNkBgkXbSZhfyOinGB6PO7M4jVXIfCuPhmU3bHR59SxXiNmtYMlGGg32Ds_G_I7YnmkopzqsKTnzelrqaz1eLxfiBVE-pLnynPLsDtwWkNS_iQ_wSaA2LTGoQEE1hNQLPAnzY4obvd2i6ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3s9Cgh0ZPmZzSVbSmi62KjJ0r2vHDHU3AFi7b2eo53ewWdUkO6vMGykDqT_Sjzs8EPddJ6k1Im_3tOtDdu9uPYJ5AxVqc5dPkQZrNDHogi20fLTtDyf-1E4MPeWCkpb_K4eLEcrYv4ZawBAZdfSuWL1vTd3AVE6seX2A-nal25UgvyD1HYzed7KH-wvUHy6ae72X_nPyGPWC4UACFTm6709FMtwIlXpUqS30b-Hbp548dxo0d_i7ct78mBEXCzOwegEXUSfnRFeB_CgdSQZZ1iIQXVnpQa6cGd5h3dinL87wrWzWhzCWYcOv0wduIaSWaznwXm_YU1gpXv1l8QwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnLteNg5L9iuYm67FiZpzyIOsbORAnO_-AC_8U6G-GEjC7BunmralIlXbplYs6uPfSpoMlnX-kHqTGXBOq24srDLqoqgtPSxEopMyI_-3QpFMULe50-Hzuo-TjMquBWVutOqILtIHHxuo8VZul3enaCrA2ZM7gIjtHQaDmSh3BWv25OKMPwOPjuUZNoMvI7snvYxT1uXXu0fiy3-v7pLWn2Xh0XtPsBFZmd3dXfFx8VAKIlMJWdObkdeviS7o8of6iaprI0nzs3GEtO28wrsUYJEGp6_ngeKGu5xJV_CFW9tcul37zeeqLTAGwUkZd3BPD4xniWlk_GqYtWoy1r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA2mk9HvN7oyNhScsCeoZj5Sz1SnxZarDAbjvtopEIxlo0zMxSA0HTY8laK1G6EtDrvqbUKpadx_ul8whBxO57D-6EQUfoK-wCfSGLUBFWH0JQ5fOGLZmzoREYYR4jHGecVfghQPX5kGARAFI_YTMqDJNy3ObRLkW1iqapRJNGlsLX6PEfQjvj_ZIQn6HrDMuw9_mRXJuoA6p1ikvSAHVp0jXQDNY-K5W4sgdtR_9vYiCcdW99oId-9jMYU_kuVfqZut7VMl0o_2FzDkwRg0XMzhrvSMYZDlZY0tZAHE62dEP3YCH7Lz2DE_jkyGEvKI-na1sylOYLCsJxSYKtzDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeCC26haCesUo6rx1Zas6nmmw3EdZ-ziy-LKk1bK6oHY3NL00Ha5hF-wJLfkomDcNY1L9qY4Caze_EN9J6TsMd36VjYK7fLAa1VEp7XbpBgXvSO5cE7GiYsbmFCPhoSaGNJ2d0YFLFWBNgd7F1OD04PGDQN_ZfKzSgRgI4U9srOxrk9_hAPtNgAHaN1eC0WrcNvRx4XMFSnTAaBnyZSXad6KHLSBpnm0r4T7ir7j_O1TDy-W22x9BZxQWApeBQ0bP4dq9S9cW_FVolV6OsHiWFeUo7NYrp0PzpbtJrQwwBTcH0GwBgdD-Emvx7KDxbsgWEsFJv9eam54130rPLr0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFgabF-o-udtLH9D3hIAEO4yW1Y7djEIEtKnUrUnUlV1nLgYmULJ9Ey3OnqItMVsv7PRgF3I4Js2-vB-0i4uvF2HKGiuX5EDRgGyfHarz8Ol-UG84nbneA1cKX2e1zzKkTm00dP-W7dTDIWqM3_3NWdDWmW3P9elQkIxdc8b5e92IUR4Xh2Tua5AziSKXV6XCIKIpiQL9Ak84PUn7bN6GrF4YwbmHyDfp_7rY3TP0F4YsVs2MTttsft9tmJ1GOK2ptzTN-HvVV2ib-uVIyjj-TUPT7Nj5P8NNuyOKnoCk3yHJXAPv-IQBDSK-mz4DEPqQyVQaiJZ6Zzuzulgwc95Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFjgOX9vVHATKSfkTvyOQzgJeWVAoiz9cZkl_Igks6QjMQBVtHV9IOfHdSau8qOptJEtGe8EVZfk_FQz5gDbn_0Rg5Uu_dWdlSF5mkc5w5IC_pgD0S9h-PMDNYndKBeUiPrz6ydsAEA-SySOAibO2LvNA0EOzY8w-8ECBY-4X3nockSD1-eFvadctLOdFqCsJ0k25Qs7pjO3-XmF6ypP5OKl6KgjLybG8J8wbLHjIyAgoC6WXtMFz-okdHVw0wVoVw3anssOoAL7afHA9OH6MxOdBz-4NKv_kSleb1UsxdHK8GILpFGUEcZ5ElF70TKgsEUy6HAJPGb7vuO4xTRMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5-kIeNbmdSinS6dkBCcLlQS0gm3_migVkQu8nCAQR50v1LS2jQi0QH-yKc5QzHs7mo1N9xc9_5fVagcsfFdKEh4Bwcw40lhSYoFIh1hTiUcgXvKRfkZ9GrIIYuu_VTLzP-SK8D1-9Yj2K4-ecz_Yj85_2w7hu8k-U3I36rahZya-NAsUe4gWNrLmdzQhWCepkC5wYJ-R80tGifknCUBUklBvhQ1DRg8tNomGWaV-WZQMErLrw-If7u94eXIJ_Fee3pNUow3GD3AGn9rJR1bKKxbbu5L80gWqUi7uEiiJW69Si-rNbSszVSCB0daIid_IXFzqTov8VM9n9Z1JQ_auQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqZ4Y0Re7FDNAgRwYzr_I56nZqO0r5laKkLICS3_sCJrystS2cOBdRWJ9WvVITa8MaQ-E-NczQyiwuQLkWeY_S2VU_fY1Ot4Fu7yOVjDwKp_5ERu_o-_XmNeRdyzYvINBSrR2fSxPxelNp6sVzildayIH_XijaMBkdxR3CiNPl0uo4FYCJYFj8u1Z4VMJ-nGG2k7BAd_iMdbBR6tcXzrizvmbpjTbu5bEaWXa0heOh94s9RQXaXs99vsBrQdZjUPVv64k5MxEJpIHMKXC-PDgnAz5rW32T36MIJFPHEt37gtfHG59q5yebG-KMHtmnnPxWM6WLKpNJ1jSAluDoctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFdYq--zN2A8X_GTd7cT_8cra7rBrnjpu-Vb0p3RzbHlTXLFGl858acrfHYbw8OBgXsUwRzf87LuH4SlFUZH_4oDKxG8YpmigV8CiPkc6-Ws8_0imPp3J5vM4yJf3_IyppLiT_ZWA-ccw3LSkuxP-ZXw_nw3Nh52AOtnSLc0mJoKAuv-g8oxnkMDRdBpDI4nc6ISP3jQpLMCPHorTxu2b57iisYR1rFS99jq_IEUT9jlqe8aiHBCUr_6XcxYeDwGverJhk-Vy0EtISVpy-9Em2hI0CC-3Ewh2lyLOR45H2yCDafXo4wtmXEW08IR-2K7ZNRC847s8qIR8_GOyVknxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQoBa07U8HfBO4QgxGvbxG7fW2sJDbHd81LhExvU7up-LG4hPVcR5_H9pfcH14kS0OgZ0IiHPH5IyDpkKb5dd9iYxetQlrr-FYQf-oCOG-OrrKYHFz0XMb21TDICWVURSi-pE9lbFdKOv0c_pzJaeYszc0DaCn8HEep5nyGRPmMIKoZSLteHjb6aXP8-WAb559WABKp7ly9Tzim8-Tl-eXAgf6sDhgrYI-f_VyKjDu3bdRivQ5vbtgkfuM4r87RjegEU-MReLSrMAOoudMmq252l7vEx1uysbVe1bQ6EWKis5JaM0ZTEEVTfb2UXzyA-wmHzhhqdMDaE2CNwPiq2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvUA3bUdoQclWT06kc2FOSKlGNDdchNnYw8a-C7qeDeEsj9sPdHlv7lCzHri50fKpc9ASLIa9UB2DE6eX5OqNLaPaJJWR6s-XGv3Gv0cZMwMu8n2_RQX8cAWjB2waF28iC81oro3dkknQ5gTOeYac6onPV3b_nGoE_WE6WtbbKW7pgJMlPOBnvmDiNDsjPOqQ9NrBsvT9VX2ELD1cZmxr-ujhoa2xSpk72EnPRXdyeROte5CRQBnWMKnmNb5wxmnGp-yFT7s4sIEtHke8JMBHLPgdx5P2FSAFCjV71xZyVjRnhyWkqR4CQoactgBq_GUxCH4YZBsNnW1nzgWEafKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLe9HHHzXIf7HHqQhHzxub-Ucyc8pq1SZB3B0hOhJuFn3sLaXtj-U91F-vg9uHeAXm4pVwNsOX0yDcwrt0_yi0GAHK7JQwnn-NOwKYoRIwgK3FT9On4MGa6T4MXEgRBg0_BOF-I85rPmlNw3KuOWg8K1Lp3dCflbgezq5YPqTyc7x3geYBB8NL2r1PGrtoOXGG0XuUUFdMeSFXBdndoFDj-1ffEWHOzawpxDPfFKC11se0BtEXk87wHG54KQsBaHCQYLVrKz2g_STVC2VAosQaYKFYxeoENT5RST0k3YVqG52MKFUj-__jYf1jgBmlTyBt63wotksSMlrBEHtJ9q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsmUc8ASK_LoDByDy3lJwG8YhGxtHKHECPI3PVsMCYN9AavSdY1ieFS9siGuOHJ3Ael_c--qcTUBD8X9oEFUEyyLpvwqNu7lKO1KovI5278_djizPzyDMC_fXSeys3UMPYXrpPfiwgk79e8IK16BC383wEa9FtvLopk1QxvQuRiFl7aPpuwu7b0-fTeyIEocdSyiWzMpi9gM9jjG7kgAupacDe8wdxUiDxp254QBhDIY9SmoAjwSchxTTYB5USrlK70w8wWD8G5QvFRm1XDy7EqTI2whRMeA-RVMENH9h0qPGJJcW6bEvm60bEXklD3A2XoGr9aNYQtaWyfijiKvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEZo9PHlWohEYpSK7Wnprllzl4p9ZmeYXQsQ39Zk03wGkTOan8GmrPiQPYONfcrwpB4aNYDZ3c7VsCH2UggZ0y1R96uRlg-ireRiBqrUVM6PbqfDlmA0DNf-EEVIxu2orqtP22AmCzq5ISzSLDfinvpUPC9T4Rdk9j2eKZ3PybPUJGT78-fQrnSWSJz6HT7WLmmu1HqLOlsamslcTZgIuqCy1wn4odcJ599YoFzAtXDdeOUqVFa9aZE7LRr1WPjm56S7Gu4fAfsRJXKpfZMrtxxZgyM3x9ia-R0Ysf69IiXJrieW6wSAx8-O15je90k1zylEq4ZzUkB439XokBOewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxO9g1lQnI_ZhnhZvDAHTY84wm_hhd4A2M5Ky5zYGsDS96ESo4kdM5uz2006svz2g-fAjOSR-cjPbx5qeMbD61l9gmC8ToI6RyXWR1Lc7n5VCBFkpTKbPmcAOa3uJdnTZ75yJxHhUTb7_7oe5VZTGCm53n_ZpSh0zZGeQbT52lwW5WxnjvRrzcTacppNUZjkHbUo4--e4YE4HQJ9xZm6W1vwvJxhFLQDZoPldLJx02YAYXHTfreQOri7digZSznw_piCaFCoN1hhOM3tW1TCrk2TAgDvNaCTvDdBuBYJB9SonO_AXMqJRw3pyKCkdbgTP1cXqYphf0ahv_Cw1x7T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=fZXKfz2ba1_nQE7po6p0ft1JPQfOxq-uCqSyZdvCfGfItBzllbx1iFaHhcVjxMgLyomICv2j_fnbj3TOw4hUJJaIXgagsrO58ggYlMGeMnDZu3skLhsD3auW-Vug7SbFL7PKNZHC-v6JhwR-wOhh0ULWGiCfPNSM4QkKEKCYOpNvNfVPO7bnGCQNrSGEl99ICReyChIStAPntgI-rN50h7SQxE8bjZ5KUn2LzXZGtBK5gqwiO42IJZaJl0_mrc_T4EOoZX4hDTjKyTjgDkuieNEEBnSXQn7Ds7GXKK568tvD73maxHg22tKOSi4cZuZN23js8-GoCKjTmGQ7a_YYYYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=fZXKfz2ba1_nQE7po6p0ft1JPQfOxq-uCqSyZdvCfGfItBzllbx1iFaHhcVjxMgLyomICv2j_fnbj3TOw4hUJJaIXgagsrO58ggYlMGeMnDZu3skLhsD3auW-Vug7SbFL7PKNZHC-v6JhwR-wOhh0ULWGiCfPNSM4QkKEKCYOpNvNfVPO7bnGCQNrSGEl99ICReyChIStAPntgI-rN50h7SQxE8bjZ5KUn2LzXZGtBK5gqwiO42IJZaJl0_mrc_T4EOoZX4hDTjKyTjgDkuieNEEBnSXQn7Ds7GXKK568tvD73maxHg22tKOSi4cZuZN23js8-GoCKjTmGQ7a_YYYYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULLWAL18ulGadl0So73rAT3UqWjKdYRDsCObnclAYNW8i7d9sQsO1WfAyscpwDshf6ejeMwTr5oRbnatrLUV0prj0uze1jww-IIA9xpQtUh3pUNyz9orgirQDRBUP1GqG6tIWiqihPtHDReXfIwcvckHP0oPFdDsqYpWZwVZZrFye3At4akzWkN-4v-uAWDosyDpb3uHIBJdCOn8TrhbEJmG9FY7Ru3KPZfwvNdxXYLp7sSCw7jUH3pNTuDeAzihKQyqWnLbqkw-ffnM86SZwvUws6eZou_ZgNh96qa7IQeF6xOHzkSqib7HH-U5l7X7HVYYH7CrFaENiJBBVtZ6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HgQXXMi0u_CNxuI29JMvjOfA8TLuueiGh3g9NV9iJOSZWpXFbs1MOwWnnPUKUjmVcycffKYhmPrl3eXTNWQ1SzOnof8RR0cYu3U8mICei4Cz2-RpENrq92y_ocX3ipZ1lrxrfTHrKmry8CP6Z1866j8bn-c8RB9ORqZ2MIkHb-eqP431IfJ0G2buO_TrGsgJt_1cuXM9k2RVL6eF7qIPwkKeANverVSg_tJPQbrtojqLMkkenGa7Oc-qutZftGzTIgEXKgrl_OQCPL_L0YFg7QDv6KLjQc7qHyBgzIbW7ZbFM2pAJx_uzaQZ9LRddVfGQKEMDz3kw7vgHui_oC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DffSOTOuOpmmgRb5PAbqwzglYWphIal_IEGUXPHihShiT-ZFVBbDOuxt_53XyAiuTsVD4Fh--FiRqN8mBqpIQ2lqeCLsVmifOsy3aAtpNEA87T7G5qtTqgLy0Na4DXX0KuSppi8aRNY_yyNR_n7FCKBfPfLRtxvdC2UE2x39_EOo73n0TIlecG_siABhzdCH3LeKIvFwUzwH3SowkVrjIJFkfuoBdihVOc5Ll_iNQtZazkN0vMtGgZHhI65q4hISR2LgIls_iMMQbNOzy6_0Z4CyYEuoRRg4b_smYICPJKp7BynQf-2EGfwOzoaaSpa4ermdmM3LmFdF-TONoNmkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNrc8VpSfvi6oC3GTVBuwBds3uhZJ1dnba9pJntx4rhCNbaMdPWIk8YuJVztVpABxn8Equ4HCGyMFWNG94BNUE1_jFLwKKLFuNzVs32kzOE0vk3p67786dM254-yGYqQlBhNmVJSoc89KHMAkvq46JHRd-IqrkTR_d-ey92Anxwvkge_eNE_ufvry9xKNGGsrIbUvRI4z3mrR1xjwXWhQnU3xkHwSkVJpAen_lEq_3d_eT0HzAgWYPRcgDgSMVo1uY6lgwZiyGd5TqrfvnUSyqtTXAjueQ6CZiXbMjYemp6BxJQSlg1e9WIR9-KLRjV9kpHzKbgGtx2NB19qFt4mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVlWjZUGXi4u1FvgireEcVPNpJZtUnfnK510o5eaSgxM9yv1ksQC6HJkhuxqGgGyKyOD4QBOOnfZgRHY9ADgjJbNwK9aZEgxuqSKt3npNe4NvdtdRFR0nrw4UiXohcyF6jH8-U6_f2iVqnzQVKeb4K_QEKG7lUnI8VG-UYP65wJP1K6RH1KdVA8Kfs8YdDtL_lH17dYzLBCF5h9PEG_l2L1rfJd8OPut55qBeYcDaPFer8tjlEQHO_ahVtmZuIESucD4yb4PUFih6EKEyDQIQ5p5GgX5bxr7g07Viuioact7gpuZUo40jmiHDjWe_CpniU1_NFxG69AemRFoVzmtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHwYoQZAd3Tx7xuNAYsxncaKWCueMyNuhPp-weRmbAxu1TvqeldxAx2LEh-g0E6xPaENB_gxT3KEPw0H3cCIMOpwoj1XopTiknnqUWiSMElNwlxvo_E_IzNyWFOgbmMWtjznwGDrNUjWS7z5JBmDgVBHxjbtSQv6saECi5QgSmnAPxK5NSbC93pnFgqDzM8TOwXGudJo2uLN8kXIUuPtkeyhPQj18Co7yn5Xi5O1viZ2pyod80jRrABMTUheewjNu2hBeyB_qpDmrqUgNRXq6EHHriOdmTtpoVYis_Cd1Eu9iRUtZcBufSIySTxPYH6Sbz56ID5AEFoiEgKSVF7n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anS5GSe16TF1SSmiIxDVSHJALKSN_572Jr_Asg0jPsFSvNG3KVSPsafPQ8voC5a_V1vmfxqE6_3sUNaxIuN9iSRq1Ph-IuHmmOGdELa0rLW26qNEYTNRDkHkVz5OvlKfNm801xPpd_At6byILhsHPSaFQU4-nMpVLG8Z0WpfeRsRe8VfkFt37lLfOk1QKbW0jhs94zO1F0rraeWnO7JrK9MichujVCkYd6sOPP26oEBCGZHjOx7Cd9QcFRH2-2diGyeWbpx2jrMqxqnAIZQAL18YnM5tR8_GsZTfArbFLNJuRpwtmWP5MWbt5iR8Vcs3iN29ANeH87Tdsyep8KGpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9lIIQ7fXX5wAx8BieFVslvsk8tnsY4grAoCXEcDMkq-MRu-k10cW-_bqw_ET6vxmFOtIV9uLlKiUnfQiI_ccl4PBGkxHZPRulhnUQ-AyWogvwvGuR4i1KyBLSamqj0x0jxetnG87hYjVrIZwCx2dq9jYRY0zl7qP62Bpaueai92mAhnbIfOrNqhCToNi6x-NsVindG9IiyLzIi-MVbop_XFSbzRKaZFfA1l2oQI2ppfByrag1dhoB8J94PEcrrQzhkVZyrX1YPtatb0kvQQJhmYNO7vVqWSyFtE5DMKSMc8YwjMGWCERSMxOHnbiVmcigT9lutKbN47gnjmMglD-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSxZQ2n1_0NU4QfUA9gPgrqP2FYGxXYxeEulLJMHhelS4lgiekHA9CYsJisfdynarxja0u2YJ_-TFBWfx97KFltlA_vDrzzxo5Sxc-XWBT0KTnCz9cy9LtQHlAHf4SM2L4sbr_uiHl9JjXLYOvz0teG_r4cOzduJCvCWw_GNVTv8GKJVkvbf6gdFHTETQUl_RsZbLUu14IEgMZ7dKErkqJgH3AtVGLqaHZuoDXGoV5mDKOqqbW7ICkwf12ws2xPH9FdW3akGBK2zNKeTTICSPytLxjiomlHZ0df3vx88sX-w2_w1uCfbzvouV76vrhC95Af9PHDrHsZ2AYMcB4o37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs_LxIZjuTdsGkk-qa1t3vRmDKR5WGsxzXFgV5GqQdieKe6OzLkV3tvGT77MKmfCRTGnvL0rLzqNgjouOhzSfY1QMoW_y_0clMno-fLiQgkqH9Jx1duFxW7tycgQc2sVNE0Kk572gbsOq2F9xrnHMCRFiSxAQDyEbgvkI8AxU1xKbs0rgniVkyWMZVdlGTF6AsttYUaPLWQGjXLFX21b1y8BZ8EUmjYM8u-NUHB-fYRCjlMNQXHKpRgxRCriPw-wU4F7kp2_3lxODjnHNNz8eNtvgG8NswSEzxDIkqCvNBQHP9hWzYdDcnSH7J1_j2VZ5gKpftczonBCZGiIUnGOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-Y5HQ0yiXL0iJSMH-aBhi0yVbKRb3gr8-BDhcwnsVhFZfLx8FYGPadw7G3MOBpgA69y2lSyIfFWWnbFPvn0vaoI2c54kV_QFy0PCFuB_6g8SWJUF3ZdnYU5jTwNUpodj5L7CD4ErUaowK3LW56KYSyMXJsvHTP4IXivpQknKQdbusIOgI4SfIKajF-L3w9Qxj25rvdSLbqRNyhjeCdV3tSb9lmZmzrGfPyYXi-gLe3Zc3vbfcfkHGKDhmMQtmv8Coi5SMh2FUDtojXqO2U77tkiIlT-mx_yqIOW5DqS-yWllwbUs2dWZZd8vZ8XAALCRy0Ud69M-pwOITToUBzVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FymW7nBNuy2AeE1r2qEm894ngxqJ8QA73sE516fMNyTYi7o_4-7ze7qBde0yZ6r6a3Xv2pep1sdRfR0J2vTUcVcLkW8o64UclNIMLvyQLSQN4chTxOoJxI7vLY99tA72vk9tWM0zhNXqEQS0isnMf_-594YaStG5_9vA2QdgEV5LcVP3UYqGhOa6kGDVj08zGq7IrYKZiyu1QsQRjT94PD3vaJrzbpe-wTLDOeEaV7bLx4SSRPa5fztGGfUmYshHv1AOYnPcsfyxx-zC4gJHWvGIl4lsQ-9DkQzzAu_bunN8cjrzgDwMoGzt-YTOojF65I3pQ7pwPl1tXMb_6JATdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=EXGPeqPVJeuhizYSQcNr9MfyaBn4gbZ1UA3g2VY4r1PXK5G30QH3tM9PO-bxI5G9U3pWnoyX2GWamRqn1vbz5HFByOOJl2i-QPFHwPpLYCDkNzWbRIZoZ9FuUanrD9okkLJs-sGO-MMu1hLHy05ddTiUCaGpLAYLQ-AP_gOb-eTdI8F2XFy7tTLqrfbaqlQSqHHsGphOAadC78Sy5aKJhrg2P9B0y0X3Vzt7sltDQOTtwFZ0E1Av2R7lJgGKlkHglHiQ-5fjVoL_aSVdcUC-YyXVGh68aSrQqhaCG1dTb6SE-1B6zQ0ScSeUVumAiroZH4ii-PwYpTOLcSD4oS4uuxQpAG2wuIrbNmR0a529cSXNNqfHazdFC4xNj0wict2X8lMUtCUZeTj7AETL78sAoaZ3Cn6UJU14rkBwwYR9xFQ3eYCwI2QqIvRhWfX7LwkblaetRnl07mIdLxw5RAZQ43tNMkcxpBfPGNVjvkXuBfowaLc-J1rkJPebt4InWHVgJdFwmTmAWJ35juVGFsdBM1OciMRzsm6DNOxW2fL0lQCQh6QQH55BN1nN95hUKxwr1y4WffqIMRZP0WNomzOe8quLVX_p78xnd90v7Fi-EgStsfCOUK-GiobPIogmPp1v6pL5kVspf8M9RnF9dybLEwpTMvFwE5hQ8fLmEwL0DQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=EXGPeqPVJeuhizYSQcNr9MfyaBn4gbZ1UA3g2VY4r1PXK5G30QH3tM9PO-bxI5G9U3pWnoyX2GWamRqn1vbz5HFByOOJl2i-QPFHwPpLYCDkNzWbRIZoZ9FuUanrD9okkLJs-sGO-MMu1hLHy05ddTiUCaGpLAYLQ-AP_gOb-eTdI8F2XFy7tTLqrfbaqlQSqHHsGphOAadC78Sy5aKJhrg2P9B0y0X3Vzt7sltDQOTtwFZ0E1Av2R7lJgGKlkHglHiQ-5fjVoL_aSVdcUC-YyXVGh68aSrQqhaCG1dTb6SE-1B6zQ0ScSeUVumAiroZH4ii-PwYpTOLcSD4oS4uuxQpAG2wuIrbNmR0a529cSXNNqfHazdFC4xNj0wict2X8lMUtCUZeTj7AETL78sAoaZ3Cn6UJU14rkBwwYR9xFQ3eYCwI2QqIvRhWfX7LwkblaetRnl07mIdLxw5RAZQ43tNMkcxpBfPGNVjvkXuBfowaLc-J1rkJPebt4InWHVgJdFwmTmAWJ35juVGFsdBM1OciMRzsm6DNOxW2fL0lQCQh6QQH55BN1nN95hUKxwr1y4WffqIMRZP0WNomzOe8quLVX_p78xnd90v7Fi-EgStsfCOUK-GiobPIogmPp1v6pL5kVspf8M9RnF9dybLEwpTMvFwE5hQ8fLmEwL0DQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=jxA-hKFQdas3mcuJGOJ_D9o0Nk2rlgHvjsK0_NYh5uFhc4X6ZuY3yTM60dsTkcIMStJJXunXcKgbtLSp7fhL8QUBtJQXApyls2WyEmOq1Ges0xzx9sZe-Y9HnqIrU0dEdBVWssAfBPAuQaQ7sbC2lNdlIIScb9Ivkf5nBWPVDR8wiqyTodeeVn-lo7lyo4ag9YoTe49i9WgV5d5wtK39wwFUEq5g4dy1_CgVnK2p2S4WQlz3dO_Z1SD-TmKMnwfgHdy8tgqDkNBfhyvUmjBQxTfbhAjXQaDLiYhKaIXkAs_T8QmqzWRJkc5dm1TNpgoTYgKa2BbgJKZZNkNTxLs1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=jxA-hKFQdas3mcuJGOJ_D9o0Nk2rlgHvjsK0_NYh5uFhc4X6ZuY3yTM60dsTkcIMStJJXunXcKgbtLSp7fhL8QUBtJQXApyls2WyEmOq1Ges0xzx9sZe-Y9HnqIrU0dEdBVWssAfBPAuQaQ7sbC2lNdlIIScb9Ivkf5nBWPVDR8wiqyTodeeVn-lo7lyo4ag9YoTe49i9WgV5d5wtK39wwFUEq5g4dy1_CgVnK2p2S4WQlz3dO_Z1SD-TmKMnwfgHdy8tgqDkNBfhyvUmjBQxTfbhAjXQaDLiYhKaIXkAs_T8QmqzWRJkc5dm1TNpgoTYgKa2BbgJKZZNkNTxLs1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2ozVETuLpNPBGhSAizrIMDqId8oiUOACEbVPkI-AcDljFBBd1HdsO_-DUiEbC7Q_0EJZ9mrqZxfcdWERrMJgxg8vnON72JQVRbYNOgwax6jlEiIYDXv04PIRCA0PfEeLJG3dnfNgPG4KLXp49bALSU17tp8gvtW8cZoCpR1g0Z7kypiZpAM2EXLR7wB1Z_7SyLAd4iOfLqLup4LRBukwXO1j8uYqJBe68lCLlTF-iKL_wBYLyojqN0RWS3xLotm8ZqqKALgIfw7TTxDXJvYV9aMeABB2qpI581Eo2peLfN5omgatG_kC0GWgurnVLNfASo7qYcGvM129KKv5x22yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKVn51VZk2dxjbourLvUHzHRHzVkokca1JCgSJXBRqlCE3zk_KDCY4UV4zc5bmSIVyWAurMnJ9zgEdUSI1J9pfZKPwEs21Fa01pAy_fq-9e9povVhDrCm5y0QHrlCNs62XeQl2lCEoutxpndLdbRaC3xNyCqFiyhm9tOYeyqTNgBh4yVLQt33H41EFYrPWOrOldCshbLnycAWZOyabIMISawf3uVwcm1xdorgorCAxHBhSJ9OSoxiz3TTW6rJd7wlgkytzRungcceX4NeIvDACcRrkqw-IBDLkxoS5QmKV-Py6QdNLMHurVZduVTCzXIR9Kupyxsq2GnigrLbTXadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEJHkv8wGoJCXx2Zy5t-gr059m74e5lHTaRAfdXGSOP6wK-NGvqywmMqUYGNgl8X5AAoJEQ3ADASuHKoqZRmSOs5ama02GJ1N2y5FMQ_N0rOm8UCxaMP3rx97d9GrBnEjVU2UCPUjXvvIM1tzUmHMJiAgC1fXfi4zLcVrM1EeGbSEGn_3f2SMNfxp-s8X8z4lqADbpuUPYBgvIgx3tm9D7td6DFNFUPnU5gHjh3n57wwD1zhU9YREz1q-ia8dBhezVKzahy9EJfz6FqvzwzSzdmQ_OmFGEw0hluunl6UcgCA3CcOtPFda-0nWZ94Ku5bqcdlvvao899ZYvNeFO_u5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX5O9lDb9NUB8M8_SN2U20vkMenYly4Qqyi1P9NdAd1KVjjv25CIlsK5y3Ay_Ple5JQR7b4SF1hb6QwrjI1lG9Defg4B39SyxNfTLe9VV8BkUFvrMNrIE0FoCl7NQkLi-xpwHTwnEODZrddQCkCaSbWVjKKNIvbfQvkJSalb3-JWiX3a2UsyAtI94duq6gdEEHJ69yuTc6ttaAogGTrhRSsCyAJytGJuigeUOke6NioATF_5HVnaggYErEnwPX2Q-9za6xYRuSj5CDjz9m3G2rd7N9mOAhDE8w6n_xg8kz2VyKyJqHL_l4c3uKsXNL8TM-q0DnWNGEZerBjMg5yBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXC2GR-xd3hH7gr4m0zmsUNohfUv9M4qxWwA7Gi3x_9HfSaaglWIaFXMvsiziIfmJhiptdayrfSgDP3cPmtnJhuhW2L_R2ROz5kMutI6stQsfFxoKwA9A7y5OekdS076w6kJRalD-XD07fkrMCmwEnRsgVjPQSCxZhIPpqZ4okyB_rG8YuuzM9VwDibvE7TQwV4qN4ufta3_JKHiPHtmMHDcxiew8OlsQ77xdatg1ssDy8HiyImsxV7p-tcRPvXRJOwhNwiEjxYAbUiPp3OhHJV_c-SVD6G6BRg6yTGFOrptC03z1KgZIRpTH_JUxJufwprplePlhdyRu1gYGwexOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBSEVPcg27-EB-AYW0BkKRFrDIEnjoXWheGddjM-C5keEH0j7ZsUft6j7Ps6rK7_VPcpJwSirQVf20rGCQnqz_VW8b_fGjZDimWm0sYXiCMpcARvADkG8qVa8LXFh5yqxxDG6x8EvGT-G2oFXkZTx-7jRFDrE_f3T8B32Z4kZkQ28IfMgpTrUGwdE0oXCR9ymOmUpFiTVuLT79EeYiNH0QvyE3af4MBmMgNXVUUXwula0UBFQiwg-C4iJ36W0dpnf8LvEon-D4lay06Kwobekf3zVTHeY026_cUAUBWSS-WZap8IvOwjH_nVRJ7zW1vkiru8LClkeRyBFyonqicftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUYXvFf-oldJ19On1rc2Ip7pUwk7TAwgRWZH3PjTyaYFcYjEKn7LnXSQ9evOBh4v4kEYdCH2DsII9cB0xBDoVqqYzmU1YswKISigj5Dij7Lxez17S-XgPtUbmzhIf4wOdvwmCpKYIJ_5H9J1sgSsTzL1z5YZt4XyYstst6O7xNvbQS-tl4HqwA_fYE2Lr55yAGYrt5nFMo_dYIPXhseGlmaHfw0j2kN8bXuEnT3GHnFjpVFrDxHUDrhgesl9MzYprrEHTJRiMAiifkETXhpQP8wsLwV9noaY_huawqFN1i0GuwZ1mAy_a4QNBeDdAckUz2cf65Ri6fboZnVwAWSAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDAUlc4VpZgkIlnNEIzyAXd2gE18bZm7IvxK6G-GMFFdYX21bspdycbGIVpTOfRRGikk9uOBG34gWB5gRCBuKzJDfdAh6XVFy-DgeWnSEOJeE3jJgMz7c7p_qTfpiMBXXOTeEj8J_3ChSBg2larjioTHF-NSYIBbNihiKIsAA-1sS4Ys6Ud-h8hMYwr-7DarFBvcr5qXaEMAgCkkhL-uKMEqAWRsbPq11JfR9KeOALCEELm4pmQHj3WMvKsz1G8fz_MnfmuFH_aBN4aHg9aX_WjBTFy8c7W5e7xBd1udkAPeLpBlvkmkRiY2rDgG1ZQPnoZ_NO73OamDWGXPebJdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVF0vjNvKRp_9jwMMUksYK11mDfNh1_eMVOjxLcGS3islHFjbpyXb3ZV3PaYU4KBYXfP2LP_4-yoibYtKM9Uw4wjG9dYl3C6oYskW1DeVOHX8W7Kb3RPySt-VRkl35_PXDmTNHkmJr8P2XcITznqiVOFFFb7vpKWRn8aWRlSBBb_Z7EiWRJ8VBWoXKrqICMXA1qEj7p93DYn9b6Z3SlFppCzxtYNUOzLGN0hwnEvRrBXB_Ec3Q88wa3pYQxrpSDYBfPwGvAqm7vdvdXZUtbewtOIBy1j1TJPIB6ZAcqMDAIom4hZybN5RL0BTDlyg-uyKtOY_NOPGZRQ84KXxlNewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=KQS0a9VOXCdSNftxPAFxg2iaHFcNg9EROMPefH2v_LgccJIc0NyKqdvjXtyz107jNGRp_kipP-kzOhc9QlIUybSlGbOq2d3SjHyB6rDP1IiUQEy9SEZS4BjRUgv1BMzxVfaodJtn5EXToq5XFSFjlAzaj7DCGnf1uVXmrqHaD5C-PpYnzLYnmc2A7uE3h_MM3IwiKg55h_az_dSeiSDdBW1Au1h66KGxNWbtCNdTnKwzyv37x4VbwPuaI4szXJcdVTQ5AaLS4NnjAoKjSk7_6IR1GWPDtQBSo0jx3ua2r1pKFdONPjA-1Gz2dNvd2m0pSlHWiNyf5VW9KCAZlpdbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=KQS0a9VOXCdSNftxPAFxg2iaHFcNg9EROMPefH2v_LgccJIc0NyKqdvjXtyz107jNGRp_kipP-kzOhc9QlIUybSlGbOq2d3SjHyB6rDP1IiUQEy9SEZS4BjRUgv1BMzxVfaodJtn5EXToq5XFSFjlAzaj7DCGnf1uVXmrqHaD5C-PpYnzLYnmc2A7uE3h_MM3IwiKg55h_az_dSeiSDdBW1Au1h66KGxNWbtCNdTnKwzyv37x4VbwPuaI4szXJcdVTQ5AaLS4NnjAoKjSk7_6IR1GWPDtQBSo0jx3ua2r1pKFdONPjA-1Gz2dNvd2m0pSlHWiNyf5VW9KCAZlpdbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbV4qV5cojnbYRIn3oHRob3MN4Qt7tI1NfyMoUr1azWhycwxiwaen4vVvyhMmIrszpch_vV9nyayutr5IC0S5c4HG2z3454uDn3iqTe8dp1qzXdMGoPioaC_jToC34XgVsAde5wuWbrBoJGkrKPXGbnMqVRNA7EuQ4d4Uz1fKfHqNl6D8fh40JPHDtp9BYLh9uOzIrQFM6KztNkwNCgnadu5rgP7P5HgTQfPjwBmeRYB_DXUtymiF8Nvz9WEtXHi3u5lHdk4UkE-1sIYXf8TktpEXUHGsfAtk4OpFaqHcP5To3tJ1FB6bumZDLB9ytMejlwO-J9gXxNakxYXovu50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=YFLQGddug2gud1ZfhRveyCjbVmWbSjm0htr28XCr59VZE9dNyQN2HrRehqicECy2JbmXJPEkq4J4Z0b-mRb_DV9b53hQFZYsrt8EADfN1ShYafJZWgYNad-u58lYP7Rtqx5NqVJHh9p397jixVLeSF_vmhDRdf3R7tIA0hN5Dn_QVeBG83SLUuHYj4iQ8JLFiPFmeN8iyXV9E-PNb_NUn907qRc0ud1A3H79OD6UR6M2jc0RhCf0GDosUmubHB2EfsPPhMx9ihWZ6OT3O0AmAUfM52Q7fvFbzauWU5qS2mB4sauppVyOT6Osf8keo85Js8qSKJ90o1A6p0F-jC4SAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=YFLQGddug2gud1ZfhRveyCjbVmWbSjm0htr28XCr59VZE9dNyQN2HrRehqicECy2JbmXJPEkq4J4Z0b-mRb_DV9b53hQFZYsrt8EADfN1ShYafJZWgYNad-u58lYP7Rtqx5NqVJHh9p397jixVLeSF_vmhDRdf3R7tIA0hN5Dn_QVeBG83SLUuHYj4iQ8JLFiPFmeN8iyXV9E-PNb_NUn907qRc0ud1A3H79OD6UR6M2jc0RhCf0GDosUmubHB2EfsPPhMx9ihWZ6OT3O0AmAUfM52Q7fvFbzauWU5qS2mB4sauppVyOT6Osf8keo85Js8qSKJ90o1A6p0F-jC4SAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWIw5aRBE6Jx56gpw5wqIDbYkVa_3udOxP4Pk1ByoFQ35A55nDHda5kb7lqbwKx3gTJEaygHkfAJhNc1M6Y3s1ACF63v9NISjVRX2eSO4aCwI_QLqZSVqE3DdssdYuOA9fkHUcKrmBy9UZyIBbzJM6VsKWrm0jEZ6U6Ct1YBCzTLUzII-2_IPTijmatGzu9dOv22inXEe3pR3DyUB46Wsja5CkM4BWYpIhQ-ozAujqI1kS-V4r04D8aVXVi1ACt75pRkr-Ptg4MwcFX7cE3pdAYy0AShwt9GBORuesI8-gEeD3jxYk8ycCJQJHK9JuP_n2p5C0P1vwrmB3Jvk_UI6TZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWIw5aRBE6Jx56gpw5wqIDbYkVa_3udOxP4Pk1ByoFQ35A55nDHda5kb7lqbwKx3gTJEaygHkfAJhNc1M6Y3s1ACF63v9NISjVRX2eSO4aCwI_QLqZSVqE3DdssdYuOA9fkHUcKrmBy9UZyIBbzJM6VsKWrm0jEZ6U6Ct1YBCzTLUzII-2_IPTijmatGzu9dOv22inXEe3pR3DyUB46Wsja5CkM4BWYpIhQ-ozAujqI1kS-V4r04D8aVXVi1ACt75pRkr-Ptg4MwcFX7cE3pdAYy0AShwt9GBORuesI8-gEeD3jxYk8ycCJQJHK9JuP_n2p5C0P1vwrmB3Jvk_UI6TZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBcJBUd4-PcSsoZIB2l7zPypJ8QDgmqka_lPg9gNfR48YBYswp0UW1ZyNs5r48Eenj6zaBtPCLgKEZwYpd580tTG1_YEIdnZLU_wFjLlLodFOYEdYZIOTOmZjI5Y3vqjGV06CHMz3fb6bBFBjS1ssT4BGRxREquXSC-ZNdSK8cb83Sd43wihGQY5ZjfBUjYQF6VCCj1LQ569ubc8CK_LkZ0FrIJV2DULJ1jynQhD9mhADklBDmFL_g8EuFb0cDfL4lYO8KNEHN2iKqJ5ZsZCk6osv4iPtjnuTfyRpUu83SSyM5SvZilkdsLZKcNzFpn5kiQNlylLjA4eXfq8-T1Cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqYaeEs6JgnyKN3I3e_piUrLF4KyEPsgMH1M-P9RJYJuBlxZ5fQmHa0wfBYkhMfBF4uGFVT6I47KNSiE2JQRiYBdT0COiJzbSjDKmH2C5YF_vrtnskOM2HTB1O-sk-txEOQJdjowtnsCMU0_0Rf0e_GvxqO2WLtvarOggcN__YLwFIPJorEFWgyCS4BajzoxbmN7ZoPF3IdZnrQGdK_mhAL1P7RC7p3-BLj440zUduDowWCe5tXgl5JLJsTAuQrS-7RpkkH001taXt0wpQy-AmRJgadlrkC5fM4e7ZKc7FnXVbPdI9dUYCu9yKLXA0rPLOIA8gz1St9b5R6G9rw0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf0bdoF0o0ZAmNUHI1o98QJuR5PbXUAvr2pu8yJi9xsfMC7ImtoniLdOJUhzwku-c4ymtnCqlHrFxhqY2u8MpO9pqW6eqdocj4qFvsRIqcojxf5baCZjtB_xJKha81dxD9-Y5Qr4RL9I1DqlCAfyo3Ggn-ukOCwb9sOMVHHGTC_p-JADCydUt0oWkCwYxyKJDWmZ40tDxDr2mJEHPxDL-5fM04HTVTv6tn0cn-HPC_nbuFl8O4gXjJ43iQ_lT63nznlN3jKKApbx_d5Hq0A7EOHOhfIHlAvPhw8bkjbVVl8P8suPuVGuczLnb-6OiXLHnEwRyDXYgEGdKaQkzYg45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmFj2SemPv0rve1mFAerDuWnIJ-FJTYCb9to8HpUc80-wudWhGRkYVF4h27cwnseKPPvrP2MkCnrXrCtjW4xNdfUTHZJ2tOozIoB0R1PCGze-H4EJC6SM5s7zD1T909BmG5GnkgRr1DyowrbJg_1wX61uj-t8ayP7MnY2OD97mYtZ4_tUncGPVh4l3KdwZUCrRcw0JzmEaL79-CVoHiLlp4g1YXN2JXYXJ3npmp4oxYU5zgy6MlOl3fJnLC_rgNhgUk_b7Wnmw0yX1en2HxE-TMcLXIFgoPXW-6uebRMK1hUUl26zIClD3mhFuqa7RC8_HcpmX4o_tf3cItfTbDXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4dLjuHHJLa5ZpKFkmgLn3BB2CpFWw12vG2snvmHdZQXgsy5ByLOgyf6DWLaPc7vurdrG60_NRRXPzukmKpEO78ZLvdT6pn0IoRyxObI8mi_Th7M9Kqs8_LUY9Am6rm66oSJjj8WVMbPs_tzE0CkUu_MRsGB_HdMuUv5ZwtLm2GYfK-C3v1jpX5gtQnXFJ-E6Lko3ORjFh7EVZT-8d3VNslPfwGTz9pKe3XjrYPZJO8GFqllfvSiuT9khxZ2a8bG-QFmUXv6oOUhwLT9oAGtdQg3hg17XM7DardSWzVZBDC1dIaTrLvWdW1bRnfuiA6RG4z3cmb2fzo_RzU6FZbkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ6OZSRQJAvX7490fBEZhz7O1aWUL9Kxge_5ziIk1h3oqiitLRUdgnuQ4CnsAgd7i4hezHht5dgpTw6gQjinRKiXV8y8Xj2yvtQcJi7NvA7Xl_yDS0DjEdtdV3DkmpgTKt41MioDyA5MKHax516yXQ1EmsG07y58cDVUQavcKhzsPY-WHNnYCLdLLWfyl5flYpmUF-QJEm1O722YSrqwwkxg2ojQ4vtEeKZyyb4hr_APqHJjA1hv5oOfjVW_QZFDE9h-uUuOgJLem1tZazSCDpBhXnZJzNZ8evTq4BTE2lpZd_TRYsRl3bU0VuqBh5ZuPuND8KNukCYA83r9VUd4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=XJivS4vS_7CcJ9iSv1dmy092MvL61SY_zuZTQ7NVoqfWPuC-WWX0or-Vx6TO7rZtpeYPdIFOFW3pyGbZKZ3r_qo3wCeTdQMltsPy-4fekh_FZ4lojbOgU43UaR5vCUwNjuSng4x6QmpIRE4_S4Nsal4j3o_IWQ-UP6dbglQEkMhXP0vEW1VhAfweB_inqBMnvszrbUjLPGZQD58oVn61Y6asLLXP4dV1_aK3RuPJn9NlXPMZ9ti9HMXrPRO8i1ALEqwO7LgYeRlGh_qpn32ztIYTycjq580rc4iTVUSM94TQCmQkIfsbZWwoSlPhD5s55TJ-uQCZd_2tPLDV3F5x8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=XJivS4vS_7CcJ9iSv1dmy092MvL61SY_zuZTQ7NVoqfWPuC-WWX0or-Vx6TO7rZtpeYPdIFOFW3pyGbZKZ3r_qo3wCeTdQMltsPy-4fekh_FZ4lojbOgU43UaR5vCUwNjuSng4x6QmpIRE4_S4Nsal4j3o_IWQ-UP6dbglQEkMhXP0vEW1VhAfweB_inqBMnvszrbUjLPGZQD58oVn61Y6asLLXP4dV1_aK3RuPJn9NlXPMZ9ti9HMXrPRO8i1ALEqwO7LgYeRlGh_qpn32ztIYTycjq580rc4iTVUSM94TQCmQkIfsbZWwoSlPhD5s55TJ-uQCZd_2tPLDV3F5x8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=KcAWI3I380NuPfpnegxc4K2WC3U4txfcRoZAaQpGfc2eCPTYkQUdlArLwCgolX7QMjUoaWaIuf_FO_plXxAyu7ZWZjbMPBzKwppsW4k4Owlf_gi27v9oCVAvw_O8gunKDChCYUr8fswTfC3h8jztQ8bwTrdwtjwbC0JAxL0JEgGjBAdUPmKX1cUL6LNO4UpiM4Jqe6RWCRCPmfmWuq02f1It_aR7wQznvfU8vIiCVRAhmRCtvGdUMX8A7mLR5unWcAu_OHqIIgBkSuKY2uiRb_25Nr5lomQY2ykEtKQJMLLJubpvf64ZsTW3FYC8tgnACSHP1Qtt_NTmb5b4QNH0HjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=KcAWI3I380NuPfpnegxc4K2WC3U4txfcRoZAaQpGfc2eCPTYkQUdlArLwCgolX7QMjUoaWaIuf_FO_plXxAyu7ZWZjbMPBzKwppsW4k4Owlf_gi27v9oCVAvw_O8gunKDChCYUr8fswTfC3h8jztQ8bwTrdwtjwbC0JAxL0JEgGjBAdUPmKX1cUL6LNO4UpiM4Jqe6RWCRCPmfmWuq02f1It_aR7wQznvfU8vIiCVRAhmRCtvGdUMX8A7mLR5unWcAu_OHqIIgBkSuKY2uiRb_25Nr5lomQY2ykEtKQJMLLJubpvf64ZsTW3FYC8tgnACSHP1Qtt_NTmb5b4QNH0HjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqFb4EBL3ehvRXJAixod40nUmyVAPl2Q8fLSV6xIaU87-hlJdS-vZWz1dvvOC0zIFRyR-0KqIZhfoVyhPzdJsFgr8resCCCdU9xQrknnaheeBB30rY2K3ej88wG_N8rtc5OD2O_LNACgq_Yd0kJl-NXVD0RDSD2CYUo5nfEDjQ1MUVCHDQrqJAEM9ThFhzYQl6bOElX5PmdBtv2SMKfnqnZ-vcE5bEbELc7Yg8OnX1E8PLrG7u_ZqO-vA5a_1Vl24yWyXzkL1w3b3T6u3CCsjSc-BDiBKqvmFnwEx3MbzNLUzLkuA98FOfR3W3o38oBGXBAlgvpn87sFNQTeryBUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REYSIUr848hrtgq0-MCBq8pQUtw3q64wcduC_MFf-cO7iEjW0HWrWtfCAaJULP1H-RSKJiXr8zxuhZ_YRZwQU3DpDiLtJZKA6DGXjNj6EjTBtaNeGInS8kjkUvi6m1vbwUINt8yMKqBkPoX4gFCtu0b3iCCA9bNkJpW1-uhvVXt068S3RR8loX1q5NvXa_zpOqPbBqthNvdLwV7FYT2J1saBpk0K9mS-gBX5-Wbtbqk4g2-cKSXR9TUq2LS70U8VZjt-TAKwUhYKWpPLTrp4UWPO15DKkd9_8jevVS0cbpshKt770YllVT7i-CrLtnYA0W_jqwiHRT1uRtRLy7zHmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyDr9VYd3Gmx8uBH6D_u_MVCwRgv-hxOhDSGDCOBfRXxpmlBRxT32yBkV8lR0v2N4LfkXdFJ5TXAN9G8565fEyIOmHof0OJsnauEs2PWHB7Da1cuyXt4RMUaDdgC-J0LqlQWjtcQdzoQUAn7WJlQn8wFTze_roJG3CKyQNtFBsHOzV5IwNvTXfdSUsCwmlNssx02iJ-zMJ9Nnyx1fWP61XNULRjG74h4ssH7JsoHJC99epcTSxSb0gt0YANhLdtD1bKq6QCAvBqrHWiZ17kI5aLPXAS8rb99I_kgq1RkTZMqkKSuEuqfw-7x5_uKkjXisrvNPYGu_xiducJV3Oiq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOf6OB8j03WaKLfvDaSWFvMCkopvikSh1rRDEHd3taLywhPbj-uOscqz5KzMSfwP59u2bbfUSTDqOBytm_M2mE1C_pM1Fn_HNvFL-yySxJUpQyASbF9nVyb6Yh1uE1oKjWCEBmuGlx4ryY_EpJnQP2EsETZWmaiQFSgECehGgS5P8kt7NVVQVCwh7S3nAmuu3X_C0J6HNEKkFNXklAVE_g84QVlRLvfYBN7r5tvo4coU7h_gOd_2YrdFIj41TGyiOjcSgFR8qHx8mo7WDmyvQiRLpPhPOvOGjk0mpmM4DmJZV3Nr_2Mq6Md-QoWpqYUjkMWkj8zhDmQeW_9TsOF6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F48mSAqdxESH_csNTzT1qL7i_JRKtbftottO9rCKXRoZewxNr7PFYc5yyI0z4UxZxjsb6boMH6-HXgpnRF55lyft_la291fMUPlr6lgQdr09PHZZS5rrG8At8v5a2YyP2slXc3uekLw2synXYZwaoRgi4JHtU3UNkTFAd7TzdsvzFoTcKiZE7yATIqKJilTpoN1MrCv1qdHFjZ1vB59EQX-Lu4CdFlQeG84cYRv-80lf_X4TMoggH0cVGY-FNzIEqzG_AhKscHddYwIPH6EI64YTmfUOtRhUOFZXwW4-KD96wgtN9ohACe0H9FdLVHiUpT8WKcpCidmt6sotIRgmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=kvOePPd-Ui5cCMMFhIVo28vYaZ7klgy26jUvIXQLs8Kx0vc5ZMXKR0kSsDsELLHqJdEtUGMCc3IPdLl-BrHgiivNbqWmAfyX6SPILl-DxzV8dTmomAEME5er-DkDhVu2oDg7Y6BHFMWyZsgXoN7BljHk4tpQIuNNpqCi-Kjz8VO8BaBaehy6cBukkdd4mhbEqvPIqlTCKLyNQLEVsbOBbgsYWOp7YZpMy8n59OZbW9LClXqyP62zuWltnt-0D5ddTNH3fP61C-zhE5CvWWr9bo250rGrDJgfADTLRn7OBPvy3L_pRej7zcASmW1WTYvFQdEhlkTJrspK-VyvtPnaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=kvOePPd-Ui5cCMMFhIVo28vYaZ7klgy26jUvIXQLs8Kx0vc5ZMXKR0kSsDsELLHqJdEtUGMCc3IPdLl-BrHgiivNbqWmAfyX6SPILl-DxzV8dTmomAEME5er-DkDhVu2oDg7Y6BHFMWyZsgXoN7BljHk4tpQIuNNpqCi-Kjz8VO8BaBaehy6cBukkdd4mhbEqvPIqlTCKLyNQLEVsbOBbgsYWOp7YZpMy8n59OZbW9LClXqyP62zuWltnt-0D5ddTNH3fP61C-zhE5CvWWr9bo250rGrDJgfADTLRn7OBPvy3L_pRej7zcASmW1WTYvFQdEhlkTJrspK-VyvtPnaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hheiUc12_GKsmb9DFiWguUr_d7vCKLgAYUwhN3WZkD2LFu027RGIIckpVVnMZMgpvXHljtZZyG9q2Y_j7BJKIHLgenOw0Ys0XLHLZ4kC77uZZiA84zsni_qB-t0tLECB1TPDfvtMHltNEarPz75kYr2F1joRxr7JtKjRqmeXN898QF31-1VI4SHvxgX5sz7J0B3SJoz8cFSbWshhmh8UT2PCbw5cyU2NCn0KiTbTuKxDPJYRLa2qSt7RDQLTGLjT9E75S-nzgitKhZimzIKIB-yPqwecA845qVVr34kq-4Qd96dLnfbnJYMlKX0cSXyDs1TLgYrukhfZKfzEFPQj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
