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
<img src="https://cdn4.telesco.pe/file/F1dfKESAjAemtbSeg455lqDthi_uu8Sv7zOHVzes2MYBco25llZ6V52_JhjEBXRbxIH-ExbRFAYpNg_RzzYorGzVPPW5fqdXNgz_WrIcUKUEKDqfKF1Jx2PTGnsmt7cmis3qD71IFCaqI3JTjKgatYhu3rrWsjXFV0QFpUwNnnlqOfTS3OpeukYbaHpRgGJ4qx6M8gC5BDbu74k7i1FfNVc97SyiaXn8xz6K1llL3eiNbGZ08yVa3V2v7IvvRrc5UQgaWATUjlfWadVydeXIvhnVn4T5P28iNlUS0c0oOtS9VFyIszuDKdbTzE8YOthZa-I1AjQ9OY0a99_fzlEUbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 359K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 20:14:51</div>
<hr>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYJapWBhNYeDSkQ2AFYhPHUcyAKr9Rr6bTpURQd4SgrEdxOLtUTx3TPBgu1XYrnHX0xhOxiwvj_6e9U9rzVMDLQL5QEp60B8w2dHpCmm2bTTa5ZYg8cer7pNv_HiomJEK1Vobu3y-sBKb73gL6namCxQJlxteIb5G31AgnK-zOG5TDr5Tb9I-nUvLx0-CStaeDgODrO2QDirtIaC6tCnu6d34YuP1V15ps4UVzrcALSbLpd1CQ9n-5415fQbQb_veMwav7Ec_CUvIkeeNQ30AzBQeFr_L4R-VHy_vVgFV1dSado32gTSAJd97WRDK_HJmuf2UFcgfITIj-Idel-2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE7QS4O6i0_a8gP8hMpBS6rBb_QH3pS-LpRm61WAa6T7LRarxvCAnvR4kWY6rFTqPMvNGMGT5phR9Odd65F_jdLJzWeVOSQDJHxffxycsJY7C_qKBvLUozLwPiP5u4P4HW_oQCM_-uzG_kMoN8MIpTQJO9M26b67qbWyxjC9j15KSWYPvFHKR-Llh5l2TZbjbw9b8Mx898E8eOgmL1LwWuJlzF8vk750W_IFWAmYY2SJ6MkJLLNWGemOiZDPrqQAbCipo4NkpmnNw6wuN0P39CUCPbZtyBwzAP9tlYzFYhCInh2egvCklFbJHGsafk0WWShkGn2QzllEC8Tc9vbfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa_eezBZMs9eSDKr47gjaSXyxpsgc3dEWt-eW57WtYuBLNcQm6-XgNNU_QZknwBj48tpIxItqFqpt3G8N3SLyN1dqCFR1JJtYba5bVyuAVWpUNvRM48j3Tqf-P4tTiVe0JZAGiBb7Hj5M9dE2RYhCRqP8wv7QgzNYuqPN2wLf4GsECft1Bxv9a7Voz5O2mj-5McEfzLAEi3KFH20QnxdNf5N_ks6vDGXP6nHyA6dTw2PK1fbJ2I3tB-0OXZzlIkHCFoccK_2wqn5dTGZDMV99wqAQcbqTiVLdFWxkVhXBejC80y4gXZaSlR73JliFZ0qcrdWXiF6daq_WokIg8gU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxGjkm19LTVLDhuxs7ri8Jmz-gZwWKTdwGIJqz9ec2v2qxmdbDlZSk7GmQNDs5Qn-9WO7EgL66aQKoxP4PAvKDxAFy1SgQJOew1yRn3SZDOiGvlTFRJBvO3IRAmjfHaOsbtrbK61N1OfIYaRD7ns80dKsd3xoq_cIAO2onX7p9CT6It3MBDmqxAveQ6DHCyi0jlVcgmsh8fIgU3dEqLR59YQ7LGOD9tbY3P4JucnaAJvyEgP3rDPQz8vmzuQYxSHOGXBoXcuZdBQJRtbrjgKpokfhd81UTKub6hb8E9JvSPd4qEL_5ZZeFVyRzTCzv6h7_cRav8KFSdWKrcADd3EGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KawBcu8T16tx274cXDLHPgKAWOyNWrBZlc6J_efq3KDx4ef4BqJ2wZKao6aAkRbP5jVvN0qY7BeF0symkw65usSF1BWe3xD749IAC2kCHHpw0h5LyUIqYkd3U6gTiRqmDfo4CvfG6JyKVDk2n8Gy9eK_3A763p8BS6jDVY7UoKRUNVkE0Xk04FVO-_JX5I8TW3jfaySxz2bu5edxOs9BhMEhzFR2lNRxiwHnz1DsQNUQXmRNHkYdTXug_Gvs-SJqYAnjXF7lf5iH_JqXCMqZ_nVEnU4p60z42JbDSUMzthBXNGtnKVSMvjpPwxAB80Avc4KhyDKqZTOIi0UXbk6Iaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6n0uLxmmVZ74ca0Wp4Au7_R6Am_fgl9GJv98NLKZL8tR2A8auH7k6_tB9dfv7G8d38WvIU99OikuR_PC-_s8Tk2aYTQWGUzXJT7za27T_5zeFeVtkIHyEJ1k6OTheiukvWvtIdf_NApb1u9OUJokqXgCMe7xE7MZlpew7Fyajnp4O58AOGk77cNVh2ou4roh6GuyzducRGXBXZuWQEUEZdNP8kNoFxPTGCR_QC_XKHcuKvIcIwJf4tCrGGvgRSAI8O0Q7FsbMrTM9eoGItlw5KeHIHzimvwLo5i_oi_-FHvMHEYTODhOSyCYiDucsqkwsVbS7lgeSdtabqj_DKcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf_vswQvMJfRyR2Lqtfoqhtx1vD1JXju9dtXoIF0l4XZTRp9efh-7-3yqjo3f9XFQpe8luLrPoF7l1-9_MdwN3KL2978FfQwFD_pwbnejfl6KmxyzNxDNZGwGTFYamaTfkjxflPIlML6mikr45gBcIMdqxsE_s4bIBCi2AWzLVRPE6sV6TpRW0OeRj89RBf9nIZq7J2El5n-CFchrubhVibCkJd_B3tcp8lyEVC3jJMtWMPguBF81_UlPQpSbUb2LeodhN4lxvqpLrrRXBIK_GqEKwjbkWRMwpNhmjIHDyh0DU3PA_xn_CF6dxa8VtD6BhXoqClu05Rf6ICh-6Xwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQbv9sAN2GxVTbqNtjx2zgbGo-sKGGvgVRByH5pHR6jNHtDHnHIagraAIKmAauas7fWRstL83weFDEWuzN6yvCY7A1lFLpGE6DHKtn3_qL8R5MIUgSZ6rLOFdKmKB8-fuCZ66Mqe0ry_dO-9CoypJU7Vv2cJJ8fMdtrD4eeG8V5Q_qF24LpXnXJgrfLGCTYm4wd046MByK9TH3LtuRGKlTH2fSz8cALm4ScXrCL3EcaJkESevBJcILdPkgAUIsY1hTSlZoBUruCfnWCOVPeMajg2_RZbgZCKUXCJ4e7wlbskfpUbfWQKwgQArD25_k-btcH5IgQJeZGUSaf7Hs9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwWDDmBfK8pklkH5GRGd-M9P6y7Z0svZsRr84U0o35LkFFzhA7AWoMZ1oUSpBNC6o2BgISPvUHSdgeQotL14v1pMFeGBDJ5MPqnwcOEmI0K1JDAV2SOY4G1epbxFdag6y0teP8LIlL6AfXJiMzl__xRBoLuq2tJ4b8voEJiELaW4rQCXRbouE_tRHCSFLZV3iL6i5UVsoWLfnifRYMN-mcC1UCCrdFwlutbXI7OJVIm5xzwrr1LLvjRMr-PWTeRBAeBpdkWCbK8qCyr4MseODAMoI2FJ-aMhYVPG0srP3QMG6RR6bosp_TyfxmUNEbslsEwSzbh948ih14bXrm9gieso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwWDDmBfK8pklkH5GRGd-M9P6y7Z0svZsRr84U0o35LkFFzhA7AWoMZ1oUSpBNC6o2BgISPvUHSdgeQotL14v1pMFeGBDJ5MPqnwcOEmI0K1JDAV2SOY4G1epbxFdag6y0teP8LIlL6AfXJiMzl__xRBoLuq2tJ4b8voEJiELaW4rQCXRbouE_tRHCSFLZV3iL6i5UVsoWLfnifRYMN-mcC1UCCrdFwlutbXI7OJVIm5xzwrr1LLvjRMr-PWTeRBAeBpdkWCbK8qCyr4MseODAMoI2FJ-aMhYVPG0srP3QMG6RR6bosp_TyfxmUNEbslsEwSzbh948ih14bXrm9gieso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBn5CrpZ05Bh9bzkFnIEHjXLViNX_yU0o5j3nYR2yHBf5N7pyPjrx1ERmdsiCkxVm5__8lpgaA8cbRo3qXUIKUmoZaUsUtcCzQuOJVNtVmc65UCClVhs80ST8N4L0Hu9yvCZ9qLnlVV7cMQVI47ykwr8uu6HFi1nUYCor7SXIrOKWj0OZQyRAFbAAvpDASca4J2J8olhTKaONL8OzNQGRMoa5WNiohTc7ScHxlMxhzufoEpj4u_HPrDy0DGEn36M5IzHQ-jzIrHLymMf-kxmi4cNZI7TQZ2w6P73Hf3PkxObjgDV6mnFS4dLGH2pJ3AgZ-4dfUyCfPOjIKTyKoj3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6MyfFtxwfTgbtxwUurXvCbjl3SDDcs1XOLXv_qhd-vwvShF20SslhTuq7OjJrWLakdSDJ20Zg79JvUT-rnKTFjm1bXOWi82yuyulHDA-FiHj_-6GOmJtxES1jeFg4bbWiEeZexA2NhwIcXb4YLSpQa1ihTPS_wO5sTbWn3kp-kS4TEewvOLu1GCrvfCG7YlOECI8ef98dfa6Ek_Kq3G6N37GCRjU0RSp29Ya1Jvo388iOMQCwRw3AVU6Z3juHrGAyFcz4v-BeOGzFr4_L6BXToGh076VJ2srcPqTfHOk7Iis26bOUMVZEe87gOuqAfdS6sp1xrqQdFb917uvBoyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=nD7JxICgRU9T_EuzWjRFPZhXVy4xyDZqCtECgLfNtQDsZu5aakcgX7hzYyQyf1a9M1sFNulpGS4LykShMUlQvPfbWq31Y7voypScHEgVwvueuxvQsn7gHTSyMS_0xFfriNZdK5k8hkBZYZfOf8nqruN35ePnc2QuFPfrRbX1dnMYBpa1enouPFKl_8OTClnEUwryst0p_cuX630WKW-VhYVlqCulkzuMChbVPkmMZ30brcRJqMHZsG3-QbiC7LlXAWg5AbUowiwe3JPt6ETir_0v3lY6p-8o85Z1ErvckjMS-tt2VG1NwejbbubcwYGvJzXqQQHOo_yDWRT5jdNhcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=nD7JxICgRU9T_EuzWjRFPZhXVy4xyDZqCtECgLfNtQDsZu5aakcgX7hzYyQyf1a9M1sFNulpGS4LykShMUlQvPfbWq31Y7voypScHEgVwvueuxvQsn7gHTSyMS_0xFfriNZdK5k8hkBZYZfOf8nqruN35ePnc2QuFPfrRbX1dnMYBpa1enouPFKl_8OTClnEUwryst0p_cuX630WKW-VhYVlqCulkzuMChbVPkmMZ30brcRJqMHZsG3-QbiC7LlXAWg5AbUowiwe3JPt6ETir_0v3lY6p-8o85Z1ErvckjMS-tt2VG1NwejbbubcwYGvJzXqQQHOo_yDWRT5jdNhcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulEmoFdkYqxm7vAS0kK6A2JcTZy5TEssbDiHCuvivbRGf70rrB5QoT3zitU7Vq5rtLW7t8k0qStLhSrIX4HTORIeCsiJy_LJ80J86jNSEG2N33ImoBicGYbK2laT7BsITUuKqmGkgnl9-fhSNjlrNROe1bBPphskPKwKIwU5vITDKXaH0LtvM097ZXe3e9SPO6gxgTYAax0WfArb6d_5gHAXOUIm_5yaKKpNE2Zq05yAx6uCi4Z2SIU_hUVVgs_BpXLoq4qlt5xVScj-vOkunG3d_BIbb5X_jqCje3UAErpTbUMphFpNBt3vlEnFreqfnC2g8gqp52ZYERAXPDDZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upaxXSpRy0E5I_Htmmfii2HnkDD2u7BaTyhhWRwN6ORcMddV2hqWkH6N2YhpsF-AIBg8B3j3ljhFr0UUW9EOKK-yFzJSf7Ryt1-hAMntBkQQT2CvoBPL2WS1U08ted1JFsbEH8ec31maIjERpxDQWA7VTxeSkArGFnAJgywpNoNZJsGxj2AkSYruyPkvwFfpF6NBfniqrV9l3YVoP4JWLEqM6CcE8cP--CPC_XSPs5IaZRqqhsMC1AqTEUta4LvN2GKOOoWer-AugVeicH3eg8E6c2EFZ2u4ZPvDhyW6VB1BFXLetAhUyvdpRK6_1xy3KNFv5drh6cTAzv0MRRQurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhCgYMS1H0pM9SbJxLKwfVDUueyRnf33-CdUoFTnquARs3cm2qn7ygW2QBGyspycHWHiDHv6qaAxfjoriejFVsSQI0rGflaiU88AHLXsUIXipYjb_Sa6WABzuCBoUOQvx-4SH2xESBX7CxN2zr0dtuQAJpnuuKPMZyLVmpvta5vRSb77QsxIvdte04aNAXXG7r5vYT3HGmNdXSfAHaf-vOJDrjSQ0yZTv2xUc2-s6uimcdi4IebStM0eDa0_vqIcxSoJqioZBhS0m3hbkUXqgwo099XUib0oCz8XxdNOalDFYDs5QKkuYU6VLu3kLQ-SdTMmQMBqWKaqWHOZbO99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
پيش بيني رايگان ورزشي در لينك زير
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=DvYPdy9SknHi0fOHVk-QkarhDRrmRyrtkgx6ur2OdCeJ5YBIhurxiq5IWzQKzg9IdXISKNVSt30gXjtNv9LDq0rHIn7fNSHeRGkhCIW-_CLU17wRYT2AJe8ny5EYZQummXI3pbrngTYSoYOLcc0x4lRPgtISGasq6EPz7Uxh3V8rrsNldSE8fuct4I17m3OownCx-hbHid9vMTPVn0wdt4M1JLSmGg1DBDg5V2Bl7cTvaMGRGcXuyDD_7OE9YvvQxNlkEnireSmSGl23UI_LxXxq3qMWss6TWTvA-7PNxi6WCcSw3tSXbyE3FybTmMH8Tu7pWE4D4Ztu59LB5ggC5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=DvYPdy9SknHi0fOHVk-QkarhDRrmRyrtkgx6ur2OdCeJ5YBIhurxiq5IWzQKzg9IdXISKNVSt30gXjtNv9LDq0rHIn7fNSHeRGkhCIW-_CLU17wRYT2AJe8ny5EYZQummXI3pbrngTYSoYOLcc0x4lRPgtISGasq6EPz7Uxh3V8rrsNldSE8fuct4I17m3OownCx-hbHid9vMTPVn0wdt4M1JLSmGg1DBDg5V2Bl7cTvaMGRGcXuyDD_7OE9YvvQxNlkEnireSmSGl23UI_LxXxq3qMWss6TWTvA-7PNxi6WCcSw3tSXbyE3FybTmMH8Tu7pWE4D4Ztu59LB5ggC5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed4ldqvWA9Fb95Y1e9wP1wgUx72pJWBcLAtaf6NSha8Sst5P3ojHwDoGq0XRKkSBhxcf_9JTPUh2kY-mK1jsWHokLxQnY9w5vpIgXjSzHb1VGntJSmGSeZ0pQfO7oZth_gciupls7V7Rdy8nYA7KZe4HwmJylC4C0eWRhwfVq1efY6j4sioJgb8c5s2U_PaN565XNWNRukWSTaxfLfiwgUNB4qyLhjW0e3G1ZdTe9K0pX-ZnbsTWeV2GAhYDtUnV-ci7qDB6hBCYMpo57bv9__WwNRmbiKLeWo53nNokbdk-Gu3qYDdmb_aOMVlo4UsBNqivnvPfFuQOizK6gZnSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=S0KnZOZ_By8jNSoGbr1plXhkgWhezrMfDT4wdT25FTHkKSGLBw6ZQV1f848JIKK2MsxoIGoZHoskJp96vlHPrJ5Jqhd7gF8U4KjPGBu8QGmJuKCIybmQPV53SDGstKgbNfL0GpnG5EaeQKlcCwWZp3DdekIiqORFoOf3HcRRKkpF2ciLSDVrLcA0a5fjLkDUf6OVtVuPaMtJRgBixDGxejrUgELsdhhLWsCwbhEgDA2WuMSZHKdxHfi0DN2vLmWUPtmZB6MuJXhQHY-TXujnu38oZyHJPIcGWJxH0lYLTZb860mtfxOrfy6C4-nqJDIR1OzukWRCh0qQ4F2gMIyADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=S0KnZOZ_By8jNSoGbr1plXhkgWhezrMfDT4wdT25FTHkKSGLBw6ZQV1f848JIKK2MsxoIGoZHoskJp96vlHPrJ5Jqhd7gF8U4KjPGBu8QGmJuKCIybmQPV53SDGstKgbNfL0GpnG5EaeQKlcCwWZp3DdekIiqORFoOf3HcRRKkpF2ciLSDVrLcA0a5fjLkDUf6OVtVuPaMtJRgBixDGxejrUgELsdhhLWsCwbhEgDA2WuMSZHKdxHfi0DN2vLmWUPtmZB6MuJXhQHY-TXujnu38oZyHJPIcGWJxH0lYLTZb860mtfxOrfy6C4-nqJDIR1OzukWRCh0qQ4F2gMIyADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuAtMNj63ydLT1RihsvMam0URjtXoc9XyFFgVsPcWw9c-6KJxLe000GCCMpxSCc76ujCuBibbQszT5DSe4WuPSxrJk_kdZ_i8nChCMrilPBPdDmmu0coQ41_SnddDHStz1ClF7zqLojEAtcwbf9O2mVA2dxl1ZsMd10Kyh3DUQOd6SZUpp0FNIkbKq2en1mQFGUCKbwJsp8wCC1Citny3c0e1smSrvdcosc8WVqD0Lth6G94yVhkt4tbkUyfRBf5D9B84zU5izFfy42CT7u20dFGxMIe-quQBcI2Tm3GDblNeHWixAFrVNdETQU94WSLQV1Yd7zqJ-R6QkzZhhUpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3cni8fX1tfoLuc85Re4rxblz7D8r9p3vgbpTDkdqqVt5DXjlYa3qkiEeDJu96ETUSEFrhYWoJQzrf1RLcnR9ZLUZhu1qTCHDWTukPuSmRBY6lck50FZ-bDMntJbnU1-m8v6Q5EJL-YuKKC2aJD44pjk_kXP388MFrPOCHK2xXwXHJrcOxA0k7Z6clCPFdEBZkgxNVy3buZohnT3C7kMle8LNXTZ8uRfpXX8cfuYgyE6Cle5OcALtJ1OnTT-ChF3zABCflvwzBNKRCnzQx_Q7iKfJd1xlz59i-kTHCisxb9Pk-As3mlWPSwdnyRqftNrTtC0fGKHsNbHXQUDdxgRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=UQuULHS9J7pmNqDWaUx4Qg4hcbupnsQDhQrl14UOh8Gb8MHO5wIep8-sWafh4HqT8480jccnPf_9tc2QJ9hK7YvkjnBFbY37mGU_8Zqd43gbzNPQ0X85LtKlqZkgs1skPKbsRRyt_eIdxfgazym7rCJxTcTAVFu1tfJnJaXhho8nRafSNpKHuoq3Gxw5mvU49LaQVvAAWeoqToyAxNUkRqRc6rXu5QKegNvM3jiUz_uS5NEPLd8Ic5tlUmDk4EFHtl3JkN8b5NlKK6Z3hxxIdqIrCqqhzcy4As9NGvUBKbW2n-sH7wazTc8gZi4h_ijW7n8WW_nNQzrkuoHb907nsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=UQuULHS9J7pmNqDWaUx4Qg4hcbupnsQDhQrl14UOh8Gb8MHO5wIep8-sWafh4HqT8480jccnPf_9tc2QJ9hK7YvkjnBFbY37mGU_8Zqd43gbzNPQ0X85LtKlqZkgs1skPKbsRRyt_eIdxfgazym7rCJxTcTAVFu1tfJnJaXhho8nRafSNpKHuoq3Gxw5mvU49LaQVvAAWeoqToyAxNUkRqRc6rXu5QKegNvM3jiUz_uS5NEPLd8Ic5tlUmDk4EFHtl3JkN8b5NlKK6Z3hxxIdqIrCqqhzcy4As9NGvUBKbW2n-sH7wazTc8gZi4h_ijW7n8WW_nNQzrkuoHb907nsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=A4GkSOuOlL64EUVub8cSrpEvdbZBYl0R2Wf6OW9xXUS_TtTQKyukSfBxNqhRBlX-11Urn_LamzHBgLKn28T6796JvxJCuDzc6b7KWiFvHTtFSXxyDSmqG5Lszt2Dk5r4pOdkFPqpRD55pgKTWghdNRb4yfk4_WXbIiBx7KYtoPV28TRKmnxzj8VPxo3WJzGbI3IX9HUA42IznfIEKmHXHwAURI9bnsNGrKPisr9TnKnUVILdp8wE-EQa6nmM4kukKejY27YCSlLDiVICSou9oSs1hnzpsRyQ2ts1xveio0WZ-VU3NsR_IGR2_V7mUFbE-EOWnWNSa3fiuM7n5GUXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=A4GkSOuOlL64EUVub8cSrpEvdbZBYl0R2Wf6OW9xXUS_TtTQKyukSfBxNqhRBlX-11Urn_LamzHBgLKn28T6796JvxJCuDzc6b7KWiFvHTtFSXxyDSmqG5Lszt2Dk5r4pOdkFPqpRD55pgKTWghdNRb4yfk4_WXbIiBx7KYtoPV28TRKmnxzj8VPxo3WJzGbI3IX9HUA42IznfIEKmHXHwAURI9bnsNGrKPisr9TnKnUVILdp8wE-EQa6nmM4kukKejY27YCSlLDiVICSou9oSs1hnzpsRyQ2ts1xveio0WZ-VU3NsR_IGR2_V7mUFbE-EOWnWNSa3fiuM7n5GUXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCgDqaFJ06HSRc_UZMDp68usVXrEdpCRLKAj5mqTI43XqWa4y9TuR9PqtUSdvLkcNAF2iVcdvk2RGSh6RqgXSSo9A2GC3el2d6iQh4S5pjwHVysuhLje4vNhAtprDUDwOeBavmIZUjlo9HRWc6zgNCpLR2scut3knR-CFcRTEcDB0xOcB426_tUqdlJ_uiI1ALcQz_3ASnQDzhUJ5bUu0CssywgUB0LzvAtKqnTzJrhhC1Xd4_k49UTzYnjS9HH-GtbSPLJMzTl2W8Bk9aQOgIX1cFMHVL74IgbVT-_WqFZFV3LnwZJP-VW8gUdKG4GlH0m5C-9vcliPrWL3nvcQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apssXipOSvXi2HROtXJ0ayb89E673eNpqF0g3LkALTRMHonyuSe6PVNuD4zwiOCSYJgmMofMAZ2UwpPPXepBCZpO_FtPAk2aflNp57OZxt6P1HY-yEGCB3UerCk7x0vDSawEG4ZdacFZ_Zh4dX7uQVZAABV6srdjaQg4ZzTQRpB-rRi6ChBVlgf8C-orjXxY-mBTEQuTuLo6j77DgXnJ-bcy7JWo0kYlyczWdi6PrbxtPQxzNh9eLZ18ZF5SvmfNGht7sgbCBbNQCjIEE_6GVhFpwuE9RSXMoamvf0_bs8gvjPlsxaXawW-7xxWaVefD7Q_R8GBvKeJSdKqc34hmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxSFwFj3nUWDklxL-jZ6eNvC122V-fWHU5o0hoFuC-_gIsnmuj2-UbeLm2MgNRzFJ8UjVIODMpIhBW412yZ3mz7elLE_mcIv4dasaOhaZqeMCx7aLgXMQRWAuh_kVkG5xTqALievZ2DAX465NLQzQX03VOvyCgzxyM8648RUAHCZ0DiqRSCJ-bZHLiIOcntBWl5Wfto2p8InY4cAtWtIzaJt4jnQ2psFIMwp5ouX0qQYMN3SJrpNKMQZGuq1h_exPscFkpynOKdKVY9JoK_uPMov0EZI3O71v_Q79lKqDu0IkUCmNIumEx7KiRPLx_jc4dxpeUkVhsFZGMRdu9Z77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=T5CYtQRIYGLlJZia26dIQbd2CsOL4iLSHop_S-NiEEvWHJTE34yMXx997_tUPupOW1Zh5cy-yxbWnmDNyo-RVTWqAmN9HLl_ZAuC6C-5foNqycS0GqaNqcDtQGhuUE0WioB_SLMOtGGnvdxXbXzVENrhBRIf0y3BwYOApSonZ77jXLWtqS4CJ1PUiGqAV6fQFO4iD-OV4f_XMoPAsKJVBN7szsTbbm9dXKDnbhPXNiF2pSYXzQ2uxli3UF6f3J9UVETbbk-Z8KhCQhmriSGtWW-2ExJaV8d3VyaiEb2ZfPVAln49lwSX7ddJqCtbvhieAjXMmkaPW23oWWtGAsUy6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=T5CYtQRIYGLlJZia26dIQbd2CsOL4iLSHop_S-NiEEvWHJTE34yMXx997_tUPupOW1Zh5cy-yxbWnmDNyo-RVTWqAmN9HLl_ZAuC6C-5foNqycS0GqaNqcDtQGhuUE0WioB_SLMOtGGnvdxXbXzVENrhBRIf0y3BwYOApSonZ77jXLWtqS4CJ1PUiGqAV6fQFO4iD-OV4f_XMoPAsKJVBN7szsTbbm9dXKDnbhPXNiF2pSYXzQ2uxli3UF6f3J9UVETbbk-Z8KhCQhmriSGtWW-2ExJaV8d3VyaiEb2ZfPVAln49lwSX7ddJqCtbvhieAjXMmkaPW23oWWtGAsUy6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_c1p-dx_qGjm-o_ZtC04z4sQkHqvyfGzSaDrn7bH2XXW8x8-NL13B6nFCw28GfXpwG0D3PNiMOfyGOWouZqgJsia9gU5546JQ3cAw0FjmpzRnVyk0kcvyjjddYLeqZlEWRVfWWHh12VET7ODH1jP_lh_63oxeKyHq4gQXWej04ZrrWnEVdToDfGhSMpkTTm8obxwRZkloPlJieUTmC49HeNTpaL_EvvfoXS1JoNu3hs9_0kSL6D0RMPD94aLmCBeRPaji0eu7gNHSKQsDT-fdmpBqe5pBtovtjFwsATxm0SdtKRwCk3P0dooPNuqpAJuo6_7Y_yLh7FkhwjAE6vLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=WCvA8QyXLIqSO_UuVesUidxm9DGdF_zUOwWJBMA1C_Xs256ONNRiBHJceGdI1b-chH0js473K8SJxgCqKRg8OV3D7RYFsUd8qs9zqjCKWG_msZWwhQCXf5IlOhk3E7_HYq_rOeG_u6bLFdsZq-R8XOy1D4bjybd1LrF4YFqPQcQW2vF1djfChONXyFcPi-mVmKFnY1F4UCdbqmxPg92nC5g-xlwrzlHDDZ4VHLGevsmFZxWxUOuDy26yiC3VTS02alemhTzqN426rf_Q7G20gx8EN96dT5Zi4bL_6mVWRHpAX1tQUSXAZssjoLcD63ZcLOyc83_n-q4tRzzpmqKHOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=WCvA8QyXLIqSO_UuVesUidxm9DGdF_zUOwWJBMA1C_Xs256ONNRiBHJceGdI1b-chH0js473K8SJxgCqKRg8OV3D7RYFsUd8qs9zqjCKWG_msZWwhQCXf5IlOhk3E7_HYq_rOeG_u6bLFdsZq-R8XOy1D4bjybd1LrF4YFqPQcQW2vF1djfChONXyFcPi-mVmKFnY1F4UCdbqmxPg92nC5g-xlwrzlHDDZ4VHLGevsmFZxWxUOuDy26yiC3VTS02alemhTzqN426rf_Q7G20gx8EN96dT5Zi4bL_6mVWRHpAX1tQUSXAZssjoLcD63ZcLOyc83_n-q4tRzzpmqKHOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEm3fWVqEP-NTSaHj_Vwi0j_DIMfMWB7l9Ygy_HrtIXH5SSACal9nY2wLzbrgpYTiUdu2RTLhUgrIZTQNwfy0yXwkTcp1ldBAzbLqTg2WenZABEFzZOXDsSNI9KAei6Xoh0c7a3qmOgcak9ujbWooWbYq3d8h1SUDsUudiYVS8-iMeF6VtpfvFVfvmjp9JtfJGT4B9WWl0uJZ7XTsIuxsvKkljx4LeJcEX0b0rGN-7J1fhDiyyHlj-DISQRVwOaKjIuQmBwwf1K0XD3sD-r5BLIdk-MUczcvGkKrLhO0LNLbzsRZc1AM0fvD8dux5wGK3Agr9HtRZSZtfbKodWu8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=ZqdFWwI5lLhCJwX56BU5VpiYBeE63nbr0Ac6waJ9_g85ya8TNWwJo1b4C3w-r--gJJUE9QLi-VerxnPhZZG4mk2FONRiOaSFz6S0miIxvNmbNwPfOBQXcKl_-roQuBbzmQSQLMhK0vvOhGtsM--COt3PGH4UOD-tJuh06X2ruhgYm7OGX_Fp200ypB-tGvECpq3o7wdjrf1Ekgd2-2i4m5ToW0a3xNziVqpprexIpGEbZgvNq_8v72oHBzpnPCt64SjtM68WkuUKsByPU18ncmMnlQiAma-yVJtKCkEtSCQihEk6ZV7ifr0xvKFV-FCIo8Naydq3IP1w_1ru-aGBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=ZqdFWwI5lLhCJwX56BU5VpiYBeE63nbr0Ac6waJ9_g85ya8TNWwJo1b4C3w-r--gJJUE9QLi-VerxnPhZZG4mk2FONRiOaSFz6S0miIxvNmbNwPfOBQXcKl_-roQuBbzmQSQLMhK0vvOhGtsM--COt3PGH4UOD-tJuh06X2ruhgYm7OGX_Fp200ypB-tGvECpq3o7wdjrf1Ekgd2-2i4m5ToW0a3xNziVqpprexIpGEbZgvNq_8v72oHBzpnPCt64SjtM68WkuUKsByPU18ncmMnlQiAma-yVJtKCkEtSCQihEk6ZV7ifr0xvKFV-FCIo8Naydq3IP1w_1ru-aGBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcMtVk3vPjTJQsbEtRcIGh2pfeglX3lcCnKAqcwr6VUTiV1gL9g7JOMf7LIZftYpcDwn-PL34HH5hz8-DslhUMw-Vt9r6B0KgFjwmL2EBDkk60Z4GHRmn8mgD84Zmrev1bac8tiEmJf3awBmtAXQE1eJpniuroMutNdwLw8IlEN5isEftpGG7gvypN-o2wdIknXgOS3sV-3K85oq4ydLVrZ8ybVNDoQVMzoxL-s0z0-iVQ3sG8KQx-FJW93TAO-eIGH2nVSerWIxXn3qetiV3wwaqWE2YDRBHE7odTADAbbxMGN8OhSrteMbKqnuFXoyRrILW2M4kwxXAYhksUVEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-vQ7AZiK1SQ9y_KvVc_mYBX0wMT2Nmj2lK028CBVTf_gf5Edepe6vJRxSPe4SkqJrbnl3fGdduEXGS1YGAHKdl3twV59NXl3NFbA5RXOkdR9lwKzZu2M5Eec7CN7ZJfIWJXIQQEYrfo-ZHItSNxCZrbu2vqWEXDJGZKcESBEixLAqi8fXh3py0lA8YWFRaN65zryKNhweSHIWDRLf-jo65s5b2sCtt2yVpAh8SufIsHyzuhqUFfgH1mr3mLvohyqGOEYijnSP-coF0kYA7I2g4O8UAXMko9BYrHtQDxFBXokSMzBJGgjUECiXLX1r3tUVj4Ig7Ooxytp-KMA5Gagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI3DVjL-FDj7XB-U9XDlOhdW0LBVqmAqO_jFLL2P4FCRMGYgBmYvLgnE-i8TsYA3p1BcEWyUbqvrPH1opMJrP2Mf2aEmAvOiBQpEmjfgeGz_ExD2fS1tasH6QvMKE7MW7dXPOBi6L7nFlyJOuSCryFXMyLnjGimpEEYmLIFy-VvyiDTp6PgiEyppRWDz8A7k9Xo1xeeDp9Q5m-eiKRDLmsiuElhm_sqeeUCheiz56KPNSojeniHkXk_SsCDqJbyJ2EoH1PBV9KK1KTlEKoICkCg1Lc0V31tg6D3OoTGBLQSJP-b5Du7EJV92f_w2kvMZgd7Qe57dM3tQneobaNfngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlQNI4B9TumlGprFCsKor0IREh2e9mBFFbnYrkS9bmsiHaOj9XFO2k1BGOo8TuF1EYcb8qdSTfn9r4EkFNipC7ZcM3Cjc-nQnEogV-z3y3SU_L5MDuoA4_LM3rRbMk7jAgBngZ7B7YC7Wy65Zc-8h4jwTCzYHVovg1CpvDsZr0IZgK-SlA2ptLoIkh76Zsyu_djYasVL6PyvPmcFEE1BgH47BkceeDdHmaylLokYZp8ocbo3Itb_Mfkc8EuFaWQA5ODzFLTeQfndhkUnP_38pVH2JJs4flLWHAXWlhIkv_Z59jE6hQLV58-eeW3HXG0pjRjxEbtWOXY3NaAciq93rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3On_7u8TxQQzgQnHFoO0pOZM_mlF5BsSodDbaensH76Q8vjOVWucNVVKLgYJm8af61iI8nlHhjD7PyLKS921ZFIXczbbsvILa-is4xk9l0_3vO4Gn44RiHQSPZlAQVyILHbpnDZy__uMwgvJkcShH4P7j8OSz4W_R-xxMzFMEmVTnS0tz5U1o3WOpVzZA10X0aRjEj44FOJmg8IxoiBXG4RcL0AaM-y7lpC2Dk0sYBcmJRJIMb4Rv2SOSQlP-shh3xtMzDKbvY9w3HdpHFCHe7nDVZkCxOD-Hqpm-U6FVdw5YsMk3Qy8m28MVq9SDtzBUUEY_MvRkk9xkDeFDp6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=EtO-iuEqtHnFWFCE1Usgc8fxQY-XLjpfFyonGx9KIEg9qPtZvsGPPpIJm9JZNCkpb5hvl8vVfj38-xt-pbIAOndIgAYN9x_RyqRs4uDDZVss3HKuBcXimorXqQeOxIfTfItfgxGyy6SIQTAddPmxZeb9WYQvY1M70yjEV1SPyjr6EAiXW6D0abr5FdMbGnvghCI1g6VH1zqBLPocJ3-9ETXVRxUCtarNg2ralMGJtWU28TRJYEsQcvyBo6HhlgpGFdE-OP4kJZJQfeFrUpQSinASgxbG7f8ZyhpvGkPeVIyBJEGK8wLI4EjmSHJvYpjf-f-Nk5In_G6H7zmfZb4rOhhyF-KQq2vyVkpr-9S6QQCeMfks5o9J-5z7PodGM1bpz-8ZbPMzL8fT4Cl4GKFs1lSO6X-6OnRbWxznuwAqJWj4MP8BAs0RAD91syGE4hZLW3ZYTEo8eevr9iJvakOKNlfypkb0cdbH-5ysvkEk2BemdxHeBh-3y62xCIOWGsF7-zMmSbuUgE5Cpmr8ynJtW1m27Euz0Kd68mValdxf2C0KgsW5402ZcFGlJmj98T2TEEtd5fdwT4L1sx015jPkAR6M2FdRTj6l-SI1Q0GbCJ3wQc3xk3wjgWjRMfjMVg8U2h9xlczsrzad5W8S4OcqwLC1_Qw_0dim5uLmyyeYmHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=EtO-iuEqtHnFWFCE1Usgc8fxQY-XLjpfFyonGx9KIEg9qPtZvsGPPpIJm9JZNCkpb5hvl8vVfj38-xt-pbIAOndIgAYN9x_RyqRs4uDDZVss3HKuBcXimorXqQeOxIfTfItfgxGyy6SIQTAddPmxZeb9WYQvY1M70yjEV1SPyjr6EAiXW6D0abr5FdMbGnvghCI1g6VH1zqBLPocJ3-9ETXVRxUCtarNg2ralMGJtWU28TRJYEsQcvyBo6HhlgpGFdE-OP4kJZJQfeFrUpQSinASgxbG7f8ZyhpvGkPeVIyBJEGK8wLI4EjmSHJvYpjf-f-Nk5In_G6H7zmfZb4rOhhyF-KQq2vyVkpr-9S6QQCeMfks5o9J-5z7PodGM1bpz-8ZbPMzL8fT4Cl4GKFs1lSO6X-6OnRbWxznuwAqJWj4MP8BAs0RAD91syGE4hZLW3ZYTEo8eevr9iJvakOKNlfypkb0cdbH-5ysvkEk2BemdxHeBh-3y62xCIOWGsF7-zMmSbuUgE5Cpmr8ynJtW1m27Euz0Kd68mValdxf2C0KgsW5402ZcFGlJmj98T2TEEtd5fdwT4L1sx015jPkAR6M2FdRTj6l-SI1Q0GbCJ3wQc3xk3wjgWjRMfjMVg8U2h9xlczsrzad5W8S4OcqwLC1_Qw_0dim5uLmyyeYmHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=M00JHX6fFeysCBHaJMOHNcuLtDhojwQYPEFVFFPNXXnbK6qkys_R84dZsbPQWxEPu_5kRuVViZKwkV5fVn7TaGGBEa6BZkFgtk7Y-9I4CSEcIT5KvEO80qTJZ57QU0m1oNWdyA4v6_OhCV9vywuW9oG9yCcdCgiEW-HTYPXqQ4hwxa9xNGNDLlVU5kynUcaZlhYxhbqb4evIip2LkIYkWa0D-vyE7cgbMk9i-tBKxWuzfjlWw8luOS8P-hGuh1uWDuO3b9ayXASYjevnjsDyx4S-05DQIa6Qy2JgJjQ6I253Bthw3BFO93oP6SlsWJHsHB5JynrzmXrKt3ufpBfn_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=M00JHX6fFeysCBHaJMOHNcuLtDhojwQYPEFVFFPNXXnbK6qkys_R84dZsbPQWxEPu_5kRuVViZKwkV5fVn7TaGGBEa6BZkFgtk7Y-9I4CSEcIT5KvEO80qTJZ57QU0m1oNWdyA4v6_OhCV9vywuW9oG9yCcdCgiEW-HTYPXqQ4hwxa9xNGNDLlVU5kynUcaZlhYxhbqb4evIip2LkIYkWa0D-vyE7cgbMk9i-tBKxWuzfjlWw8luOS8P-hGuh1uWDuO3b9ayXASYjevnjsDyx4S-05DQIa6Qy2JgJjQ6I253Bthw3BFO93oP6SlsWJHsHB5JynrzmXrKt3ufpBfn_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDEiXJRKyJEtssyD06byYk_lCj0VsKgNMVeYyte3IGMbPOqNAFiZqv6PQ4--cdb_5jM5niIo7sWFXAwDOc4Hz9C7rKa71B2K4Iv1Zz6Yfviu-VOnHHS7M4KXkrnlUiQ63YDDL6CXlMQhypJtlwVHDQQpcKoIp2Mj0uQvYVVdR2M3NGdB9zj5KlbYiOsBLt5bScSmUnLHZqRLrz8C1jRD00bwllTExMil0GAfxo_C9tQiSaP0ZcyQkAxry0ju4ydXJfocZgkQNxmLGfZ-jcmrWaUvWPdFHPeEvqqzPw8H4vl_0PlyiFbyA3j2zFpgnbqeWyA7bRvC1D7C3XVChn48Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=AH-GdZqCtdHzsKYkYPEeGxF5UfyWWW6-cC0RumNvWIckHcUGiD_05e_1FvSb4A--ciJJjtwZxVMDTQcZA6RKoR_p_AWej_7mRPkhWaDyOpU9nb_ihLRAyP42gNzW3ZWazMf0mQRkms48AobfQuUJ4KYkEXNHdU5XXhLRwYJ4vYim2tvbq62kYVsjd_vpesTAr-7NR--4NTs2s0do6iPOX4sQt_v4j_GdapGPCzM-OQiSPIdBnJ8Pg6zjQr0wN8nleO1o1xZZuuK1Hp_lPz1QPRzN4CT4U1Vf1yEwDwa9sYxa8HOuSPtaHnSPLxe1sKxm0U7qB5m1sJIAzNBRWNDaYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=AH-GdZqCtdHzsKYkYPEeGxF5UfyWWW6-cC0RumNvWIckHcUGiD_05e_1FvSb4A--ciJJjtwZxVMDTQcZA6RKoR_p_AWej_7mRPkhWaDyOpU9nb_ihLRAyP42gNzW3ZWazMf0mQRkms48AobfQuUJ4KYkEXNHdU5XXhLRwYJ4vYim2tvbq62kYVsjd_vpesTAr-7NR--4NTs2s0do6iPOX4sQt_v4j_GdapGPCzM-OQiSPIdBnJ8Pg6zjQr0wN8nleO1o1xZZuuK1Hp_lPz1QPRzN4CT4U1Vf1yEwDwa9sYxa8HOuSPtaHnSPLxe1sKxm0U7qB5m1sJIAzNBRWNDaYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=iYM1OC92RbIDlkSX0PRHJelnRwkLLFkK2V2vGvfOxsdqx0ua4eJO_bdAVtlalueGmiWh6xpCmFPb_z-aacy8-wgj9955kz8bMO9sEH2UZ2wNQU2HwkNVLKL0MN7lnpxkTgghB22KYGX6tRNsRlIS-g-PbmHg50-xIbaVlaVyYOjghyAmMdi80HKXmunV7s9cgrpEUvPctSvPBero40S0gF5q4I2qbrjgOT3DdjC1iUesFY2OkzS11L2ETVJGlFTnHzwggwHOxCS87DcalE8FFGznN6M-mOCnWir9dLwguD7NDPXpm9UzgRRoLmovM3nvghAnoAFc1LRK3HkIvfFd_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=iYM1OC92RbIDlkSX0PRHJelnRwkLLFkK2V2vGvfOxsdqx0ua4eJO_bdAVtlalueGmiWh6xpCmFPb_z-aacy8-wgj9955kz8bMO9sEH2UZ2wNQU2HwkNVLKL0MN7lnpxkTgghB22KYGX6tRNsRlIS-g-PbmHg50-xIbaVlaVyYOjghyAmMdi80HKXmunV7s9cgrpEUvPctSvPBero40S0gF5q4I2qbrjgOT3DdjC1iUesFY2OkzS11L2ETVJGlFTnHzwggwHOxCS87DcalE8FFGznN6M-mOCnWir9dLwguD7NDPXpm9UzgRRoLmovM3nvghAnoAFc1LRK3HkIvfFd_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdTTNXtFp-_rIqt2h_M0V3NnPoM8E1dWTIm-VKOkU16i2FjFIj2Ei-c6rNtaaLNvRJImoiSmB0MNAPZl51Pw_aGTBDO1bhPIQn9Z6CbdODmdvOvcUbtIkDzDfzBCA0It7-So6tNp0meqL7s-px0TN5ASM3V6TAOX6rl5BYLhFQVxgAsqxaK_c6abJzoRw_aWZ3qYV5gcLx21NpG8MEzuwKm_jyDxASpVu9A1Lrd3UaHQNAE17JuxxPSF93xFkCQRJqLuQIxCb_2_HtY1Gk2R8_Efja670l1C90synzNIlLS_pkcG2c0RGh4u_LqttZyJAmpnT9Vm-8o5Ub1JDZvB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9x-p3bw1S1zOFDV4xPk04_Obk4VDpNQKuOjWbTJUXuSBpp4X3W6y-mzMuEF-e7UAF-kycX4kqKnsaU7Nvdqy7i6qsY6D8nXSudf6P0qx9ztmDqkuVumJR27q5E8H47majIHQpmvOa9g2qudtKk82tr7UaM1I4rkixj1dWD5469ets0Kyef_nj09-NmGNlVZqdh3u2jEgVWz6b_kq2Kz3_G4kv6jVX5i6a5BuRCI8wqZO8l62umTkt1fc-sCL8jt7MrgCMXI7pBk3cDhp-Dk5dMzLtbvO3Ch_UaluMfcRvYiz1Hw8vjcAH9-Kg9jF5D2RRz7wkx9AEYVRk-oJR1FeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqqBMjzNgbOi3bk_WwqF3g-eovMQg2v8g_oSQ50xR0Q8T2UwNhAEBsXlEj7pBBAG6yhkAeDMFeATGDI-MzwiXoqbEM5Fa_96Unzvyg10zYpiVlu9e8TG-RQPO66YdJ2e3yQqSAdhVRc3S68AbLO6bv6vJzW13IM8NWc6uxw_YNIbJ-jWgbksenvGQyqKSYQHpKa3PBd7sEp3i1QydOGFgWmV5EgtLALfY7H4PyyQaHM_YWx6FkmFEPEgpUPo2rQ0FwvPRBtgB6DFNB4ulN-FcU9LAZwltuQXbAJx_mPXfaE0TQFS4F9Iv847zVx7KAIDRJ9JF9jTTSBVhkRX5rOn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7LeczLhHp3XD7fIx9Kcpj7VHVuOTAct6LVg-UuRqdhZRdeeWhff5mR4NNpv_dLrgFqWfCDfPy_k6k6hgi4tgSiPC8Jjx-vUXaFI7G4HKtiOLWQA12BT3d5K6EUAt72rlmojSrZfIZKNeR8lHqVI0ycwBM6EBs_KgqRw-qigrORitfqk9rRReH5PY3dxiqmAcddDf4BkMzcZqt7UrQh1R6esz_YFvRJGNdwrNbEibeLJudIH9tmXnJjO-fLgIu2ZYu3cCaaoGZiskZE2ib8F8Z1BP29KmZMIg8_jv3QDD5-l_bwO4dxxUrZOdBDUzNzacS-RCUQkH1Ki1N672TxH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=W1HIMmS4qOELQ3OD0EPr66PyrN6fIb3Sc0-7I8v8byWU9TC71oaS8qGnxO9FRCW62joLbPGfhFImBfRNtW4GOBicBEFE0oEu-yWDEYTu1MTugBsmQQF8QJ_9DZxEzNLIKzVD22IaangGOga42JtrZAAyk24XYCBjfBnOGJKdXIlfTfbO0A8qApF5mr1I8zk2iuHkeqe8lHpj7X3eMLfG_K7U3SnJ9WgP_JljaBZ6r-VHnFhpBMzxpCIbfFtC7WkZj6593IBmsvp7Jn25kpOYw4fExGGdIL0SnS8aB0WYyGkwNGVKIwL59G6APTmEX2bU43jNzlpsXYgBH8g2D4dSUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=W1HIMmS4qOELQ3OD0EPr66PyrN6fIb3Sc0-7I8v8byWU9TC71oaS8qGnxO9FRCW62joLbPGfhFImBfRNtW4GOBicBEFE0oEu-yWDEYTu1MTugBsmQQF8QJ_9DZxEzNLIKzVD22IaangGOga42JtrZAAyk24XYCBjfBnOGJKdXIlfTfbO0A8qApF5mr1I8zk2iuHkeqe8lHpj7X3eMLfG_K7U3SnJ9WgP_JljaBZ6r-VHnFhpBMzxpCIbfFtC7WkZj6593IBmsvp7Jn25kpOYw4fExGGdIL0SnS8aB0WYyGkwNGVKIwL59G6APTmEX2bU43jNzlpsXYgBH8g2D4dSUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0_r4nKetgvclXMMLkoalGF09JQrcFdCEIkU_jCSgOP85Hngw48DyrY6dVXkuztCeDLolst8zAKetEvd5j9e5pf4VxVDH6K2S-TVcznOlSJZJ2zeVeXoESSzgHtOxSMuGVhfIpxmNMfH0O2cJSs7aiUXZUEfsI_TGMrk1XZZa0OUgWWtWxmE5LFsBm7C0LMVIaLGmNkylFwHQ-KF4OPmeal5i2zSmg00q-HBX5uC4DVcdX62allKy0QEosvZkfR5ZoqLTYS91P3TH_qIRZ0mnTNvKc8M5BJoRJ5xS2D-waGMycs1KnbWNTEa5Fe7fpcf7Lu_McUW8S7jYL4JrigxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kb_kLI76VDBuxKt9E_0r_mdkKiOhmzjTXo4nJlAHM_yHuUZY0QwT_zWaz7Y7eTiP-BQOxNhOSWZ3yZhnAkoQsBrbgJgvqD8in03DuTHRBDOhiosBm3GHLq9PdzRva_-iZ41adpstDpgqs7ArnhdvsQsEVbGPDb83PlLbd6PcRuDjZzK5Xg3Xou1kHw6sJAOu3JxGe-iSmcTHh7Jdtf671grzuR6WKC877KSglcPEGOtyMKHrmXtfiDN1mISTvJGLb74CHCD3tb5OCj_0dFy--4D9g4wXQr-Tt3xRYUNMZhKzh7J6HrNBumy1Xw4AmJVt8nEoMbPvecvpXae9jFD7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=P8M93OoA93qPoNIA6yEb1s3bYyw0aI0PeiA69AKdV5qaxkdugCNz4hIIwYb-HsSs84bNfnkPaAaVccRdQnx-D1wSMaBSR-g27tVq5HWhTlYN_MSiCQSOz3GeiRigRpeDJ6bbOlpk6hpc_BnjAc3Inmeci5dTdRjdw310yrSQaUsWnvTFXHNRmGpvsZ51EI-M4AtJOqqWpZkXLxx8sFcQqs4VIBQCu6DA3qBPg27sfYzRh3PveyGI0XayOKFS8tOYLWZjytT8KWGXp4NAC3voNEdnMCaf4l20QS1Y6aZk9w1VuLsmsxhY1BJzdJ42B0V_6fbjeQAVtyfPLOzvprrEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=P8M93OoA93qPoNIA6yEb1s3bYyw0aI0PeiA69AKdV5qaxkdugCNz4hIIwYb-HsSs84bNfnkPaAaVccRdQnx-D1wSMaBSR-g27tVq5HWhTlYN_MSiCQSOz3GeiRigRpeDJ6bbOlpk6hpc_BnjAc3Inmeci5dTdRjdw310yrSQaUsWnvTFXHNRmGpvsZ51EI-M4AtJOqqWpZkXLxx8sFcQqs4VIBQCu6DA3qBPg27sfYzRh3PveyGI0XayOKFS8tOYLWZjytT8KWGXp4NAC3voNEdnMCaf4l20QS1Y6aZk9w1VuLsmsxhY1BJzdJ42B0V_6fbjeQAVtyfPLOzvprrEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uudQmDT3VHVeGkstN_pVQBSCl13J5xadNLdQRQP0zv0TS17xMEl8A5tbe7lsdvWzQm-_8Yxq4eEqehH7QhmoibYc22ys-hEoBlHUWUNzrHAV0sqM63UBwrBR3t-hQAq5nO6DOX7867Lblg3DHvi4xbZjkElFq4WvyUFJwblTPizo36I-q27TsHY47J75sl-XT5jVVWxOFpI7oHDE4fGqFWQDu9X6yOHZ8DHwB3DDPnwUazknRlWhiMkTpPZ3NVdWfHf5-WNFzkXjl0g6r28E_X87_GKgruokbU0GS0Tf31N0MdRBtwXo9WOyS3g6M0IOgxqimcilgQCOGoshc9SaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG7Q3CloP6NXSx-kLm-O0gjVkJ-oL-GGzBKxN3G6njIQMnkButFvUGxAQtdsACGr7Wg6ZPUz8ZiP5Bd5W0McmhIn700uf4aQn2n7pf4gvHiY2zahdXwta1uzEMWndmvQ_-89iTIaxbe-aNEPb6Lbwp-_MsvTpnPG7LE0P7Ws75oRwf0Z0tUrN0ru5F9LgG54O-sCLhmcpyRE79HEAv4vtImFNBXl3Lln60Iq4i5YdyxhuQkD8JuVqBZ2Pk-Bj7T4aRA3Cws_VHOZKmDnu7oPWO1V_Ow6-ktYwMBauz27BxQULNzmU2O7GkbIUK3Jri0iYPNECIkixsxGuWABh_6Dyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMisdHRNC084IdHsbmnV2G_9wmYxCu0jQGn7rTDDNlTEimQwViwefQGuN-dWVeK7oeY21LkBiDzcfcqms_RTAQoezDzVWeXudW-4r8xtjByMt7bH_EC-cM5Zyygl_y9GlKV3sn_iai2F4BrlT6XkjdjV_DKhqN-wWWCf5OhIJTj3hWGHvItKvJXvOHxyXb0FXvpheyQN88PXUnXqNG15wmvOF7d0Fv1nPpDuJig9mXMIIsV84TB4Bo5Me0MvL3YxWYlivWDY1scut_81JP2Yfbkqi9tFxHYlHXF2msd0unkFmKLRZw_rWU_gQPQtZ-panXpHVLfXWBzYs6avho36fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9PXCvgFJHcWjooia03lxCe1xs6nYAhXnmkh_lLxNWouoG917AM5ZF_7cHKUiXBgxPqxuN2itYQfcYLcyihidezB5WPhwinCNBGuwg-Op6Gi3avl8UnvR-q6g4RBWsvOhcx1NOFILBQMwfHSkxXJCpP0LubcTWjfS4OG75dDiRUAu7Q9Vt3oT9x4Jmf8oEc1l9XthIWk53aKzuCbgbQc_WvkMqpHbalP7834dOS8kUZnCJBwBQAYBAScgv6UEpCmccr_DBrUvs74_CuT93RkFoUjAlWOtpuBy4sYivqMdz3TEPW18YtRL7V1GaSaO2iZEuR8UJOB4UUeeQM5x21jfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=aew-Ymcz9CChTPPKJwFbdKIPL02A2o3GRbbH3KZ5sqR6P9xquBo2B_7czginjN8F2axZizJ4yP7wrKYT41yYZwyY-m-Orqg8IcUaW7gXXdw71qa4vJGDGU0gjgXlMFA1bfDqD2Xt3UVC3B0ieQGqTaVAcngDtcrBX4uyUOh4pqS2vzy7t6FFkFP1cMcV7F0ojXsVQ77X7V8ZGZVvmNTo9cyklpW8m6BwQNRUGUhJaS-jcKaUd0f5jXtCfzhi46w_aGZg7Lq1p5LECYGBJsRAlXMCYTqomrkIPSzLinXh6TNPVOvBggQR_K_Zurv6yo9hpO5ZERLy0H_hmeC0FLHJcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=aew-Ymcz9CChTPPKJwFbdKIPL02A2o3GRbbH3KZ5sqR6P9xquBo2B_7czginjN8F2axZizJ4yP7wrKYT41yYZwyY-m-Orqg8IcUaW7gXXdw71qa4vJGDGU0gjgXlMFA1bfDqD2Xt3UVC3B0ieQGqTaVAcngDtcrBX4uyUOh4pqS2vzy7t6FFkFP1cMcV7F0ojXsVQ77X7V8ZGZVvmNTo9cyklpW8m6BwQNRUGUhJaS-jcKaUd0f5jXtCfzhi46w_aGZg7Lq1p5LECYGBJsRAlXMCYTqomrkIPSzLinXh6TNPVOvBggQR_K_Zurv6yo9hpO5ZERLy0H_hmeC0FLHJcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=dklPvB4hc1gsRbKmYYcjW26IW615cWOuJEPTvc4GDxVyyKs19CX0uxs3Jp71pIumYqAQ_DbTbPf9A84OFnVsAXspwMMOLBFzLDjG4Wbo19fsMXYjBYPyahJ6UeW_gf-B21H3bWiy5Z1wLL3bHFKgyaVUYSVcVaPNMp0-ip_spIEoSNE4hXoDcAwH8dPGL_uutwp0gz3Xm3_1EV8YaPbc5DmpxwhdMJqR_rQp1e1VMUsUA3xth6ZyUt-dyFwwysKfZcqmwUAskwc1wIwluwoq9brCEjp2VX5wfpOVX59YyKMsCTYXASs4ennK5GCKj_JfbyVuMycIkuZ9aESopQbI1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=dklPvB4hc1gsRbKmYYcjW26IW615cWOuJEPTvc4GDxVyyKs19CX0uxs3Jp71pIumYqAQ_DbTbPf9A84OFnVsAXspwMMOLBFzLDjG4Wbo19fsMXYjBYPyahJ6UeW_gf-B21H3bWiy5Z1wLL3bHFKgyaVUYSVcVaPNMp0-ip_spIEoSNE4hXoDcAwH8dPGL_uutwp0gz3Xm3_1EV8YaPbc5DmpxwhdMJqR_rQp1e1VMUsUA3xth6ZyUt-dyFwwysKfZcqmwUAskwc1wIwluwoq9brCEjp2VX5wfpOVX59YyKMsCTYXASs4ennK5GCKj_JfbyVuMycIkuZ9aESopQbI1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDetWCiW6vZ4ORG0dhxjwMvjCVzW57J0Yh-AxEdH5pu9eBcOJAPgHd58WqSAG5rXo35VLDwukmbRK7QanM1HO5Hc-21n2hsA61s_zqGF6VCxnMF9gHEU6Otr91Ae5ECT24QANVGeL00EdFWpzZrYl5nA7Qly2O4BJ7KCX8171RqG2FNNDJ9vmmiavTG2VZtwFnORl2RiQtO3S7AERsWYrIP4YApanmRzrVJUg6CBsHc_smCMzjCmgUi8m4cMnhDrjSOzD--swPY3pGSWnV5wDhyyhxM1bAmKrhaY2rO3RWeWdKGnWCfmuP16iW0oWRcyhA5EJfv1j6YICwP2LGs1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=rrX4AnzsNf0qp2nxLi5JcApqAcC7sukhEC1kmG_DLJfiSDwRmFI-o31eUNSeoqp-enY8zF5kHDC_049vXEK9qdxXcyTAuX3wbwie38z_TIHH5ZWTjehNF_kk4x7MJ7PH0gHqc-t9Bezac-Sjy5V00LXfG1tgGPytTlGFo2b8KT0QCLrQni4Vx3Nh-eBC0pTzx-z5jni-hKfi-IyaS2fMf_5EEGy07Eaf876RxQv-vchwBaexQZ9kfKZgUj8yxYsdOaDQ9kb2z7qLqZx5pRLKy5Qvl36eJikM009B5EoCJmtlpNBGmbt2l_5ih3X9ujPc44Gg4QujsSJomq3ocbwXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=rrX4AnzsNf0qp2nxLi5JcApqAcC7sukhEC1kmG_DLJfiSDwRmFI-o31eUNSeoqp-enY8zF5kHDC_049vXEK9qdxXcyTAuX3wbwie38z_TIHH5ZWTjehNF_kk4x7MJ7PH0gHqc-t9Bezac-Sjy5V00LXfG1tgGPytTlGFo2b8KT0QCLrQni4Vx3Nh-eBC0pTzx-z5jni-hKfi-IyaS2fMf_5EEGy07Eaf876RxQv-vchwBaexQZ9kfKZgUj8yxYsdOaDQ9kb2z7qLqZx5pRLKy5Qvl36eJikM009B5EoCJmtlpNBGmbt2l_5ih3X9ujPc44Gg4QujsSJomq3ocbwXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=CqoyRCqncisPVpIxe2nE65Sfsh1BQdIz4VrqKMG1Re0Uqdfkknrd4q0PfmmjTsr9sKf4ctMkpYRKJLo5xFiM15bK6OplYHcJBKmMOxT4MBkkAZwf6BvrdPJql8SQSMhZtbR4fuw5juoL6x7Y2qd3lEfVNUGCm6UtferMGawQYt34FU-zsA6atGM1liAK3iSHt6hXZBiEWztKfPHg5YTudOICsBIAaaejeJlebuyJm8amGmEAJ-YFWxibNDh87SVdckr8quDnM_4cylB4QJ3GGsTW6ZwWOrWpbdRtBzyVpLL1FCdnWFgim6d5DdYLfL2do5MjDbyW-j3NcJmLEx1FPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=CqoyRCqncisPVpIxe2nE65Sfsh1BQdIz4VrqKMG1Re0Uqdfkknrd4q0PfmmjTsr9sKf4ctMkpYRKJLo5xFiM15bK6OplYHcJBKmMOxT4MBkkAZwf6BvrdPJql8SQSMhZtbR4fuw5juoL6x7Y2qd3lEfVNUGCm6UtferMGawQYt34FU-zsA6atGM1liAK3iSHt6hXZBiEWztKfPHg5YTudOICsBIAaaejeJlebuyJm8amGmEAJ-YFWxibNDh87SVdckr8quDnM_4cylB4QJ3GGsTW6ZwWOrWpbdRtBzyVpLL1FCdnWFgim6d5DdYLfL2do5MjDbyW-j3NcJmLEx1FPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fofhpB0GX-BIan4Opde5g_5TcYVO_PaIdO2hB7w1k7yh7s4eGEyK2VpSlhCvuIyQ7xqbaYIhCMMMBqADQQi77IzgSu1LVrZlJce21JTreKpsOw-fuSK3VNoedLGy0G6A91Jgc3qQAnR-MBS_is4DopLOG_I5YaPEmYoe8ukJsxZqHSjRXVdDOdnXTNSilenLnO1WKMrr8h9GzLCsIukuTBIojCGetJ8vejBMWR1Jv0Agqb8Qb5SucmJgfGHOFKqeFKxQRsWPl4RGWrritC-Zt09RWbJbWL9Zmj0TA_wq-A1YdB-0P4r92ti_4R9RVXL_9193uaapp_75nZl6uiOqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwqR_yqBpe7ISzGh9ui4SSctZgpogb-a9rHXImkG9KwZmH3K8IyCr047HpDNWoNEHcrnjV5BY6JDKldE9lS-IopYHd0UAjsi8zHbf3Bn6oTs8CwxHhYNDInBrWtQFpNyNL_alpwp_dTtpNX7QiJ_kGa4AgbIj2U131KUjiXZg75SI9cSmus3hhU0YF3ZjAFdA8yvhIp6CqnxK2NgoIoktJHAx0nZeGdYsUrGNFdqodXmXAGSQeTYtbAbyKDvwbgqetyZp4xnurydax0DGHlLzm1RPSfP6iwsI5p-hmjzF-VJ52FbmhnaNaYHuAYe-fnSxYnexgoNDPTUoxnGz6SbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGPqTHhyu31goljCDbjAjVLMEoHkKnpvVtZY8Rnu8X9SKtogxgIrwGj-C5qrhffRjSBaEeg0E7mlm6he0J0fS4N0CDO29Svy-0lwQAjyNie1jbuIRigddK6QUHvFUYkZ2KrIklNavqvVezJYRdaFA7fuO7g_H1rzjrMFvPap_rC3ktdaW890G1kfm5XCEiJf6rNg-oMToQnPkTKeaQWN2Bj5imQT7oNnGr4o9ENXpuLHpD3AJjR8MFiiwZSJEv7geXkAko8Q789W6uYiZ9yMYd1A9xAD031p8J40psoYOxjdptq5hzzZtjSW0eKQNuFKZXfioLfk_cS4m0BvdxKBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoiUdSzvfFPX5v5apEVrcfMRsBLadndC6Sf9_Q95SxjGOZ_Aysz-SnAJweiBlmZu6YM-ND8Y4ZZDhhPLlJ6yq8Ko0tGy6ED3-d0VQ-d8gujg8SjcvC60wVzHSYhUvRMB9wacDusQFihW8tWxu4xHRB14z5jFGwU1EHSBTAWIqbrnfmIFPvNLU9-r7sLyb-n029FAFP36TeJQRLZAYXTta-hzfqsQvJvAX3ijX7hu3zL2FCEbfi5cVwbvIAxDMAFQV4QUFJWZzG_WkDaBIxJOt8fgiXZGEXzaPoJs6b4qlsualGeAED0wNiqZIwa0ofvIjwaek5NVLvzzv3S2PAATyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=ndXly3kbMC-GkVlK24JA-GCKXgqnj2D948356EFSmT_yk5PkI2RbvGMGdyc4HbS4pOlvT5Nrdtn6Q1hZpiq_xiZVtjnJk1nISSy46I7B6pb_VuMvFTYtVvYeTcyQcUAiwK6y-Wq8RXtm_ihFSoJMfcIO8sbqY2fGovLoSNy_l8Wvs5vFojr-Sp_WpQ-CFhVObx-Q1Jid88bGqYkDE3p8LScFUS0xxqWzNHz2KmUFi7ZrbWPJvut6_79pC0ZJ1JeyDZVhzvAs6qF2O865-d7rL0k1-Z7KERTHPNV70O9uXmnKzG9XuV-Te1HvW9WDyEn9FwkGa68Pkg4qBTRt7t3VMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=ndXly3kbMC-GkVlK24JA-GCKXgqnj2D948356EFSmT_yk5PkI2RbvGMGdyc4HbS4pOlvT5Nrdtn6Q1hZpiq_xiZVtjnJk1nISSy46I7B6pb_VuMvFTYtVvYeTcyQcUAiwK6y-Wq8RXtm_ihFSoJMfcIO8sbqY2fGovLoSNy_l8Wvs5vFojr-Sp_WpQ-CFhVObx-Q1Jid88bGqYkDE3p8LScFUS0xxqWzNHz2KmUFi7ZrbWPJvut6_79pC0ZJ1JeyDZVhzvAs6qF2O865-d7rL0k1-Z7KERTHPNV70O9uXmnKzG9XuV-Te1HvW9WDyEn9FwkGa68Pkg4qBTRt7t3VMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv9VJeO4-VYdjkUz1z0i_zgzl4VXMX_yaKn4bqlOoOecIVCf6zhXr9buzmbWT_aR05uiiRlHktfj7Y4ZhE4NrPrdpqihENH4r7ieVIgijrIfIT1YAbl8kIbTHH_fe5taU_lAJ3ZRrZqO-S2F1uyrqlnZm3_VKyZ7rzd0CwBJ0LrSFb29R5Gj9aGJZOAhkCNmynTZZChtqrFOjOA-IM49FQeU8VU9nsWXsSp47MpiBaDvMJi13Pz6hw75BWHzStQdLiGlzqn5O1cy1F3ztaM6l9ws33l-5m7eHw4kOooStnzZD5lQU0cbngckGujIBCvE0_4JkDJdEVbSClrNsVzgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=Ut9J4aurHmYPmV_hfRdt4s9lxq00-a4AiXxTU38TwHneLbU5jMGSP6XhdbkaNGy8ElCe9GA1-PFCURg7-vsOplz5yfPfiUT84a2WvwQ5X-sXKtWjzQWwGKghhCLedVW6etnGC6IIB9V8b0lrmbg3213YarxC7n7BYti6ynckVnI_aS68Wm9u6eS1NBaXoluPeg69KkEz2n9tSb21KPm89M6eJgXKybfUP60w3CNDVKB4_Ha2V1BdadjBRxrkXTHMBjh8tZ9n6TS3RgteJM3NRisr75tWTUYI-656m3VEaMemp3p2O3U2Q4XyyUuSg9P97mI-U-RMJ_Ea0dqhp5HwSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=Ut9J4aurHmYPmV_hfRdt4s9lxq00-a4AiXxTU38TwHneLbU5jMGSP6XhdbkaNGy8ElCe9GA1-PFCURg7-vsOplz5yfPfiUT84a2WvwQ5X-sXKtWjzQWwGKghhCLedVW6etnGC6IIB9V8b0lrmbg3213YarxC7n7BYti6ynckVnI_aS68Wm9u6eS1NBaXoluPeg69KkEz2n9tSb21KPm89M6eJgXKybfUP60w3CNDVKB4_Ha2V1BdadjBRxrkXTHMBjh8tZ9n6TS3RgteJM3NRisr75tWTUYI-656m3VEaMemp3p2O3U2Q4XyyUuSg9P97mI-U-RMJ_Ea0dqhp5HwSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TphNTMQL3hYuqx1NTo1IxEDSZJfUXNnaXLfUtJ9hC7gJ7C9cbzSh5p01wNG12APiGWYfIDtZ1UpDMcg0JQ-spzwidnmm04eUt58KzP7DjcN79HUG_ocP5ErfNfNNKI9gH0u3pYTh_1BVk0ttvrCBHjzfZRNYZgnQFJc7XRBUPayY465Wx8t8Z_yV-oIHPKRl2I-YkZYa6XX9I_ZBNjAc6qOCrKt-Z12j_6leqI8rmV0rXTFBikVv6T8qih8C-ldTYLOpBeFKunG8JxxX5ra2Fnhe6fURrlPOTplXsMKy2DW-fIg6zaKnPkm6MRtY7Z4QvCFuHtYL6PkOz1ZgX02Igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5M8i8NbOkOOtWKzLiHrFwiMQnvoAYjcVbN0KAp2-tIVhF22L6BTmY0Quppo7KEjqnUR9w9-dtpWugIOmhQaGt_GQxM2SqZBtMDEm9VUX9Fca95IJc9AMw90Re8_xf0VahmDpSFLfBpI5G0OhqBJEGGo5Edc9PEEr4bPuM8WSnAKBoG6_H2SuPhQ6AFeGN_-WAbH4YZQComLNJysNHOx4X2O12NCAD5FIlnt8zd4KHC3ErF3uloKWO4PhkJgcY19vtUr0GtVQ5o8akWy1a-JDsWkX3_S_TCfndXoYrYvQkbnJ-qOTRh2Mg9jmop5Sh13_I0Vwx75bkjkDJmNs4jOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4lxkTHOxhSKVe3BEWJIG5Nw0kEQn5G5pZgFqvLL0VeoXDvoxlMojiPl27smS8uOb434jaVEMuOaerTptJ5ADHFQXy9YjRvDjLjlQyBINmeFhPMQAPLRZ6Js3C8L4mXt2h8wA0A4uL5PGlTnUc4M4cVzX3c9WMIg0iWVRGRCKGIAbFQSjpGwIMc-JdGACsYv9eGWMY_yhqJ5ImnHUIzA5rtXncdxzi9mKdx3S1bKE8iZwDweXA969FhDlbCBkw8sSndgvPVpJ9q2YuDByht4zlcFGwXomsjqhN2jz8Gl1edczT4zrx12e1Bz_q6N9qCAFQvJ-GIcKKefKHEHpeCw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZLw_xnK7a0ojpCOgRuZ6t4o8x2qGUeFGH-J1yf8TP1hmEb7sdzBNNlBF3XN0fK75K4Z0XzLVv4mWRoL0QTJp7g0DA5mn4yiQCsvHlW2dHnmTK0gmIoZEokVI2O1b_5sVEFySDJvWgmnnGm3bAqeh0mvBRGuuCLVfUvB4tej1kSRp5ji3Q3fnCpfOFvHD1xE4fynQAwtXx5iY3XXDolRFgCTjPJp164S3EADFaG47OuP77Ea4FvTGER2CNRDlbdOPT8rZqn88JxqrfZcNTTXuVnBANO74k9Jdp_Ad6WMnHU3QS0tBHkomDP0u3jxiJ5voEVxwoT9gq4_IXsVgYqi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMOsvpm07pjg4uIlTPn5fBUEdZFzPaiTwGULlQXXSEsS4xwUwUi1ZI0wHhfryn9p1CAORbQD3Ts0uXl1wH0nsH2ayqISB9DquVjE_XM_-ugLEhEAzhJ4zawlQDdeKAYOKx5oJWJeVCLOGJ4cK-jEZxgT5LoFFDaYBIhJnaaV1oVirHDgkE7dN1tudnvNbJLAvp9ENTFGT98JawhR3zeHOCPbI_7DG4AdK0U21aO1HpARBVk168xu5K4SyW2ncVgypnl3JSTlDsM_x1nPvVcQmQgCmeGgsP26r8Czmderqrl2dNHJqoEMCoLDkYdJtzw4QixamOXr0SfQ2DwZYC4TKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYp0KjBKrHOcwxl-TGN1aauZG7V6nSZBNP98A7saIW2-udOy_KjRwfPm-UXKFLujzwzB5W4Zar5JTSraxdMQzIH1G_na_-36cc_RItnRzGFp6hBwNn_QSjhb2eiHbpHeeAa2cAA8BXLPNC2ShSjghrYCKLCx6M-aEmQjYoW1r_xhcUAHp3Ry4leYLc13bbFrFFbvqPJT9uWGdgdm3JthXpeT6UNGFKj_glpZehAuSgAiQt9YSEWuflx8Uy9rmjMahIuRdW1caTvZPLeYqM6ZdyZJe1JWG9WtZljXi0WW-b1KkkFo9fFRd9vLsojo8_-CxWQEDMJQ2fIaHiLjonkKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNDM69DNXho9ovG-BsvZ21RlLGI_UxbFR33nyMx7mujqNaSiAxVmWLKbZ6qdjfw0p9HT8eCEDsFyKynAdo4iBUcFuIQM2MVjnf6QzgXhz_cVNKdwHDc117S8O8f66tEw19_nKYTLMEz-kjdSmSviKTglAp7N2ioi19nzWdkocCET8KlaU4StukzZYfPvA4LeyMXUWl9LfvG0GVTb9Ve9sIGryISdhEIgEaKVWWFFJsBs2RSWxg9KfJ67by2UU_HneHDzaaShPeNE5Gjk546hqCFyHEkhk7th4Jlz2XOapeE4WPOdNcLz67inKbpmW1QIuU9oT1pgMw7mBACLApLJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mckdngXHuKx2wvqfcQy6NSVEKsDOu1A8BmcaMTCeHvbkurk-ONaq_I3tk71XRygUJMQFynb_p4R5MrUbalBEIQYl-ugSCnuWEjSNizSHohGffPvBCVHfzsotw7ncE_fRnHZfrtqqb_Td4s53IV3bKBSPnl34oIkbSniLAY6Zvq_VTvRq9s8787cSobZRsOfiiVhc1ciL-BS8Ta5JK7MvW310f9HiuyGe1sYgtDTZfMjhm6RRJEPSxMKoRhCQ3ZIdFRsZtZbcsLSqs0qsL7ZIhQo4XYB3LXbcTEv_oWxNoXQQOi4wz--tXQ93qXfFOcE02wHKlD0vWW22AQUpsGgHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvMJ_Pz_oBdg76l_L7QfchwdUmykuFGwkXEn4hnvuwYP_XQ_aj-YAMSwGgm6F0dpz4ebrsLjdrt8YZ7MKeVUCkr_rQmkbGfdAueijXA_lxCciGZSSCLIej6OdjN7v-OtsyqTRj__ZMgW3p2OBnrhhAj0k-6_LiTxAP3X4gzzzcacEh9LByd1QhJwqGKownXF-IPu1XkrtBb1SlgBjNpVEe9Kya1ZIL_qDhk_D1yrUGel5iiuZHxtxpuV-YFoZCDKXF7YPnNBy7ac9nIcBuCgP1YkldWqP34M9w5yr8Lj-Ar0SNgAEa8Y_a7imvMJUKz3iH1ZoWvZ3KJtrwN_2pMdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwCHeHBsWKQ_wn6NyJqpe5DjosAhwWdgg7b4KATwo56kO_Gg21_MEAHW_zj03Iz-tl-CowRzAPG4NhU1wk2dNw660nMQhqlA2KXrf94xP1QzwmpirxGS-m83jdaTIDeiggdm2mmGTiTomWVfpViO96AS6bz0GKpNlboiLFZc74cO0dopR_iDow_GZ-Bg4F5A7RAo7ylvruTiyH6al0LG1qpPgvFarRstswqGuyNS8V_J12SZIcAPRaxtNbPZXiCVpvmqkTZD24qO0XUNN-kKavqFxUpaNeHRYDLGXICBs4DIYvr_T48PuBKBLxn4kL9MHNoO-kMJeogfaObA5S2VlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ6uAhjeePRpF01kgS8dtmhYjn7mhu5f3uFv7EZpC0ErdIduRnO-t9Ozbkme7_K6f-tRiAU_1vqM_iNcgywvnJMBFUlmhwNsYVqFHtbw9WVV4AOEgYA64CXUkvNG4JcrWJQvMuOx6UDIHlStIagZ0XFfGDbN5G4b2jVTwIcfSuSAUVEqcrFsnf9fRXWfOZJ12qdLKwpcqntX1DR30XSV6G1nlr_OLZoglXVIx-EMBblPVMBdOPGWpDBfgGB3I58y35PLaS2WPl3N5eOQrUhwzZf064EUAo1Px5tDcmcDF82ThwjyV41RaemfWSIbxVp0l5AG4jxxXHv63nY6vDhmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBK9SnHFaqQvsSGGqMxybVXDfHlIMgFmUVdxCZqrHhlYgWONMLLcSsZNrgO9dSUU1wogqw2wuZjkHoaKMNly5Gt9c8YwrS1DaO_sjrluEWQ0YdI0p9YYKIq5Hra0NszE017o6bsWlX45OLFvcYJTsciVnfu8w5pwGufUXZDqkXrCl53YPe9Di2iHKUZHe9E5NEzoxEYZwRLelRmhjST7BEFpZRA2xjcOI0cPhececpkIF4i5xUlZcNpOcVSKH8WmhbmzXOX3ZoDzcQ1MFziR4e4JM-eGdo0qA3bP7iOBXjK65go0RHgovpKo1oJI1KwaRlMQ6HS97hpL-DlwxNpUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEFUQr8rh3XV0_S_SOX5uYXeokMJdq21-Dpvu2dVKmB2TGBMjlpIluCNp1l_r96oU-HeZvwlQd-_v0wNoFSkkI8PB5PVxaXbd8lqqRCNHcSPrjLznv5gnMMjRPw7zhFGVEgzELW4ZVreW1ZjSa2WT2wDGqp1NFUx_QapcMwZJ0DGiefYBMPMm_H75nnm5xDiIlaQ_m7e17v4_rS4RRpN5lPKemwLxgVP9RfD0V_U118tfxGIdHQwz1PG_Fn6zMfCRY7n9yK9YOJpSp25z7r0YciyVrMaI_dKsRx_4SuXPo2TlEAwueUGPut9HCeYOD0nhAgg7_U62haL4vsGQ3MtfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-40gzjUvYBjk8dfQ5LI_Em8xTKBPMMt_90QYpL3EyaEqWqvNSs4MZhFdGeSVjfmCl4TkZCGnxERxemX0kfEDHL9TtNnxgQGAyyxe9fIEShJEVVgjz6CDJdfB9cCnsKTl7kUm238HsInljh1MRmaKATWSpCGXVfQ_p83lhPgwGxDZmQvJ5TBFhHIsBDD0_oEiDsFMGuFEcggloLSZLnXSW1cWjJ0SNNXGfqakiyUjSe-8zU9X6wHxsC6we9ap45ktGwPhkhh1i2QPx5Y0hTznGyEArB7jHigkWR-wjAdEOGmhl85eulzyeuT_8BsWIpXglWeSO5_gHciLl772Jl6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwMMmabJ3zxhIcoGYnTtGwi7sSDH045d8hMYqS_Qlb31-a-Y8C9RuJEo-Qf7hHKQTw92xbY96SEt9u1bVw0VIsg-yIMwNIRzMrNUOFn7bT-yuugLS__B2oLrJZXA-CM0bysIApeV-ujb-3Rx1l4CVirD64aSpXw2_RuxuxcM8K-UWYR59yfP8nZAO9Ua5qr8HHlkqwYAngHRZPfPROQCnNWP3CWJjOV-fWI76EbMepQrIyGhVJ_jwZJF1u4TNroX9RvJDXB-CncsAooHIfe34subqKTOioCvEumMQL1wJW1tDDYwwBgqGPGWsw7hkbNOtvhcpDT1DQ-WTfyLWfbTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTEbHtxdJFt5mHkDigsiMmvXvfNSLVz9QgCifLfXtOhrWlYD-Y0nueuHQtRg8_5Xs-WGzfHtySuLcu0oMMAlxArHWrit1rg0KY0iQEHn2XyBni3KMmoeMepedDx4Biy8fojwsyodtq5Y-d9AHv_dygv_sZukS__GUXN4SF6tPmB2PQtSKZR9VWuY84T3MTW5Xgy1vHemZSh6nWpA0llAddbe_v9EqjSjyMMA07UYo5Pz77rjUQidL1rx8vzE0Uy6Mx9y6metNTTLQMwSfulQwhuiaxbgo66mFDPY09Q1RYVISJ4nkv1IIBOvD_uuQzSAV0jEf1tWeZb0M00sYCV42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHJNSAWMY3r9WYwe83yyVIrTC5z8aRicp_hl3QjTI0uefeDc_CfKj5S6G1D5i6YYASXBhCGUB6Nkuo8zhYQvxKaixXtsv8lKQrYt5KT0uKNx4gLra8_HsRuBknNN3OK_vhAlQP3K7VLCgF-3Nw-arJqB9WDmowL3DfRqKUswbgHFWtpHmQ2pE10m_PYr-7gXhu_O1Cp3i3VXXZvc6e7LbsP_0I2CxPtmXS-K4SNYj3EiQuZDy1CL_2KKz_k8LiHsZGW5l1lzO-0VipxzO0W9-omL0XBApMie_pfbxbeeV2eExgFES5LZVYH_pSPjanzWPSqAEWxtbzO-qpP-A9uSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqe9yXC6hgVupwc50UPLeBXLw9k0grmRTCFfPVycSGb5sbYM2ju29lh2nYUGH5B4jJJfJP1hGl0Cfh43ZsD66b6KAs_YfO0YivQ7mL91WBZWzMrqd22JwqEZck2ydDUjsxPQXSuBWyLOhD7j2CTJCzczqwoDBT2zDHIRMeW3l4Gsp85rSweJT6ZfvKt59mp7U37YYGk47G5P5P-Sv7pC4FEMdRWFDwHB3qQwI_1_cdEbGkEvyCnZbUv419q_eilGKNVk14_mQkT7G-xbyZdSr8WkWDQaX0RcSJUVIZzNWOxPZQHUhO7qm5ue8dnfwq-y-1dppETGn-XANRMxiPCz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=d_y58N4ua2lDpce8Q34LH6XpPJuyUtWqkzrgJDJCgQir_zhd658TLIpXRhLGOIcgKxM61-pxUaY3XaZUSP-9rLdZiheUp89q7ohDeDhxI5R4rit9IR9B1OBGbfQ5g7hzMBo6v7ehbshK1jIqnl3oyNLwpkmlNyJEF2L94uPGsyicvm6Xc2YyOzwGt8xz-5PDCDpdTMgZFhi4w1ZTUnIqKnuL1YDtBya1Dd7MCNnF_XvXUC6d-MbpvDqL_wLJlW-hkzM9BwtqAe6EYPYLDwfWJfRGSMKoyuEmWUgFkKLtqa2PuaT_vkibpzx5wf4gKS29IyDU-bOO0uxQArg-3w-BFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=d_y58N4ua2lDpce8Q34LH6XpPJuyUtWqkzrgJDJCgQir_zhd658TLIpXRhLGOIcgKxM61-pxUaY3XaZUSP-9rLdZiheUp89q7ohDeDhxI5R4rit9IR9B1OBGbfQ5g7hzMBo6v7ehbshK1jIqnl3oyNLwpkmlNyJEF2L94uPGsyicvm6Xc2YyOzwGt8xz-5PDCDpdTMgZFhi4w1ZTUnIqKnuL1YDtBya1Dd7MCNnF_XvXUC6d-MbpvDqL_wLJlW-hkzM9BwtqAe6EYPYLDwfWJfRGSMKoyuEmWUgFkKLtqa2PuaT_vkibpzx5wf4gKS29IyDU-bOO0uxQArg-3w-BFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWBCMd5zVCWWdC9VqGh4BNNT9mMKXwCFKuKSqwKlebFlncoblxaW4qTrobdh65WMjBr7u89_2IP-pIBf2zrLGqJBJVLtLe17qY9pQDU1DFSbr7_TuSwMNpJgDnUfPZUHRuZNO4h8sSBzqVmiAYi9rAKXTzcSaNz_rQMicqM8iXMBmPw1iRN2JR-DEcs7S-5o0DHPYda9oj1FQmAOda0LRWEk2UXFWElIXdlUv3dwOnrooj2BToQMt4xPiKCgvmkbhuylS_v_7EocZivtzEmLcKjxJxEkrIOfLowPvxSzEefaRwhbLPSCdSn5H9W92FddXiIlH1moEtCa8ipsJl99gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
