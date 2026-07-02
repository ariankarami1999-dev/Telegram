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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa_eezBZMs9eSDKr47gjaSXyxpsgc3dEWt-eW57WtYuBLNcQm6-XgNNU_QZknwBj48tpIxItqFqpt3G8N3SLyN1dqCFR1JJtYba5bVyuAVWpUNvRM48j3Tqf-P4tTiVe0JZAGiBb7Hj5M9dE2RYhCRqP8wv7QgzNYuqPN2wLf4GsECft1Bxv9a7Voz5O2mj-5McEfzLAEi3KFH20QnxdNf5N_ks6vDGXP6nHyA6dTw2PK1fbJ2I3tB-0OXZzlIkHCFoccK_2wqn5dTGZDMV99wqAQcbqTiVLdFWxkVhXBejC80y4gXZaSlR73JliFZ0qcrdWXiF6daq_WokIg8gU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxGjkm19LTVLDhuxs7ri8Jmz-gZwWKTdwGIJqz9ec2v2qxmdbDlZSk7GmQNDs5Qn-9WO7EgL66aQKoxP4PAvKDxAFy1SgQJOew1yRn3SZDOiGvlTFRJBvO3IRAmjfHaOsbtrbK61N1OfIYaRD7ns80dKsd3xoq_cIAO2onX7p9CT6It3MBDmqxAveQ6DHCyi0jlVcgmsh8fIgU3dEqLR59YQ7LGOD9tbY3P4JucnaAJvyEgP3rDPQz8vmzuQYxSHOGXBoXcuZdBQJRtbrjgKpokfhd81UTKub6hb8E9JvSPd4qEL_5ZZeFVyRzTCzv6h7_cRav8KFSdWKrcADd3EGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KawBcu8T16tx274cXDLHPgKAWOyNWrBZlc6J_efq3KDx4ef4BqJ2wZKao6aAkRbP5jVvN0qY7BeF0symkw65usSF1BWe3xD749IAC2kCHHpw0h5LyUIqYkd3U6gTiRqmDfo4CvfG6JyKVDk2n8Gy9eK_3A763p8BS6jDVY7UoKRUNVkE0Xk04FVO-_JX5I8TW3jfaySxz2bu5edxOs9BhMEhzFR2lNRxiwHnz1DsQNUQXmRNHkYdTXug_Gvs-SJqYAnjXF7lf5iH_JqXCMqZ_nVEnU4p60z42JbDSUMzthBXNGtnKVSMvjpPwxAB80Avc4KhyDKqZTOIi0UXbk6Iaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf_vswQvMJfRyR2Lqtfoqhtx1vD1JXju9dtXoIF0l4XZTRp9efh-7-3yqjo3f9XFQpe8luLrPoF7l1-9_MdwN3KL2978FfQwFD_pwbnejfl6KmxyzNxDNZGwGTFYamaTfkjxflPIlML6mikr45gBcIMdqxsE_s4bIBCi2AWzLVRPE6sV6TpRW0OeRj89RBf9nIZq7J2El5n-CFchrubhVibCkJd_B3tcp8lyEVC3jJMtWMPguBF81_UlPQpSbUb2LeodhN4lxvqpLrrRXBIK_GqEKwjbkWRMwpNhmjIHDyh0DU3PA_xn_CF6dxa8VtD6BhXoqClu05Rf6ICh-6Xwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQbv9sAN2GxVTbqNtjx2zgbGo-sKGGvgVRByH5pHR6jNHtDHnHIagraAIKmAauas7fWRstL83weFDEWuzN6yvCY7A1lFLpGE6DHKtn3_qL8R5MIUgSZ6rLOFdKmKB8-fuCZ66Mqe0ry_dO-9CoypJU7Vv2cJJ8fMdtrD4eeG8V5Q_qF24LpXnXJgrfLGCTYm4wd046MByK9TH3LtuRGKlTH2fSz8cALm4ScXrCL3EcaJkESevBJcILdPkgAUIsY1hTSlZoBUruCfnWCOVPeMajg2_RZbgZCKUXCJ4e7wlbskfpUbfWQKwgQArD25_k-btcH5IgQJeZGUSaf7Hs9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD21yl0lRgSEUGoc7j5XX644JB10mTdlV73V9tOHQtyWas-Qz5EZ3wCuKlgfZocs0OUjLVUd6eUx-1rtiPt7SulCDrGyLMaB-s8XjH0kz2YfKHSEn9qPk1RG7NLFK5YiiTS31Upoxo8th9UcrN8tXZacE-C4cCXyDKdDgPqwbNGGiO6RzD7dlUYSDLb2JLhE6GGbAg0V0I-5icxM8-1prrhGhVipeRiP37VnDSZXESWId9HbehjE9AyGgERyY_l6EUFUe2KJyFgzyoBHgFSmvW50IF30jrDcsO7zKvia9q49VVvpiVZFiVJav96Dyx54n5VYKmyeZAnkfZA8ouO85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsuwdhKTk6awCxIv-2uOhh59lYfTSRd8ZMOk1zxAAThXcN7yavTzHr8lujP33PriakNycoReYg4FtaxRC9_nHJPqnhuDgAHiIkk4qJu40LWIRBqyCgNkgZUYS2i7sGd4on9RiMGHreYBnSL1xGoyhU98xm9z_X7UAa5sxWah2jYYhaBk8nYqyWilzjlXOo1w-Xq3b4nzlJlr3j0kp0s3jeTK9F6ZhrL21kC3RILjLCufQBwAx0P_U3PBK2U-pkKlppzGpnsVAxsfoSVeMk42L5UrQNv4eeLdBssD_djYyuK1Lkpe0qSM96fzETX3VppdykT46XwvmUiLm8mDnALnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=eLq13jcArphR1vJL206gmmS6urQqTVJ4ATb5earv3SWiWZL2PG3QevhEWbPcpJjL3u5vVzEHNKmO8Fi7utqBXB8MI5dXkwLx0QxSp4RTcZTjI9V-nHbNImWxBGT0WyzIA2AL065uVU_ywMlH8Za0q2qVmPafkuMNEMWgqq6VS-ZC8I5mCpTpQOkTuycLE-Op2d03AXYMqW4DU3S6P8UQpw6XOYA8HN9KsbWw4OJO0nhe-izPda-HPMSGGzr38lZuI5qx5wqajwnbwcdE_IlsRvTil7jXNZgYbDIYz-lY55dJWRQuCJ3Wb-UBxUL0AxkAfRhuHJl4mZV3IKlJM5mFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=eLq13jcArphR1vJL206gmmS6urQqTVJ4ATb5earv3SWiWZL2PG3QevhEWbPcpJjL3u5vVzEHNKmO8Fi7utqBXB8MI5dXkwLx0QxSp4RTcZTjI9V-nHbNImWxBGT0WyzIA2AL065uVU_ywMlH8Za0q2qVmPafkuMNEMWgqq6VS-ZC8I5mCpTpQOkTuycLE-Op2d03AXYMqW4DU3S6P8UQpw6XOYA8HN9KsbWw4OJO0nhe-izPda-HPMSGGzr38lZuI5qx5wqajwnbwcdE_IlsRvTil7jXNZgYbDIYz-lY55dJWRQuCJ3Wb-UBxUL0AxkAfRhuHJl4mZV3IKlJM5mFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHw3hbV7J_Mdkp9lmEULLYToOGy2ZqVDajo_SLPheJfvZ_8zPA_awZeBSJfUd64_x2BvetanSoqHtsABzm8ZztEqo3SJFV6umG_Kgl2Rkq5rcXW11H-uWfPyGYimxG3C9AqhLrM0eHbXxU7LTc7Jl2hh6SuZIed3B4sfMsUaN2zVjfLF6G92LDfxWtWFGhRERp6YgAAZcurlrMiVLA95WclAhRxFMq2QLHXhRuLKjTA99W0tYeKrhqHG6lRUINnLZz5IPXaKmfOBPgbUyw413thJH5rOHDqsMYrFb3YPjuVHP0J1QYr4VfAueRO2DmrbaHDsPVaWy7IWnB8-sgUxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSl5sTU-zVyeS1qanPweEcJfrtBsk75vGofWxazxU-kI11cGrO6gZ16StnOKzWVlgR3MxjaAzSdizYQpa6m12sYC8JgtMnhKg5gwxyG2gHA-G60OMjcFqzldL3UIkGJ3a9dNHoOjHC5HwaYDKJDxrZ1vUdXacVwC2vn-RLBbIgMeb6lwo3QImgI3J9QyIAYhsaaiLw6ZgVVG9UFasrC1V7wtmhNQ8jDlSCgmNyqwnNGHsgRkUuTg7HD_gi_h2i8Wj2iC0ppbrVh4LCZFb7LH7c1puuTIQbrR2reP6s7vlEQ95hLWKI4QhmMuCJUm3gB8Fz_iOdLvvn_vXF4UlAOk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWJ_YfDSSLH4gCSVYKGAOwlK4RpAuOcJBCrWLrntHUF5UTz_aMcdjN2BrftuupBod7l6_A4wqRXIxCuTd-08_-yHevbBCzNiStylRAXngw8qn7hZXUi_UlamDPJ0CNu7qG0NDiXE1fWIqYnl27UDz1NTZFQVXccjxjLMwUjwZVG6TzGrdZNYfukA2Qta9VDGoQhNXUTjEgYtLZq6lKSctdxUrfWKy5P4NrbncatFRRvvFEjZdkN5IpaV5Es8_HUV1fQyQpjrez4zVXP4glBhurVIV4ByUZhoeYuin4viVzzNxV_tgl6wCJ6geY87O5MEZiRPLrZusdJsV829jYuEZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=lbBi_PslCI_crKFUBpT-sPWk0DZ_of0A8ERdZErjxt8LN9fK8KXhPsIndpNmKcU44q3T9DFvLqqVS4309Cr9eTE3zDTahl5KhHWGn5wfFkxjKUT8k9OfT8rPZmtkEHAEJbXtfx3iuJgmij2OA48qjWVDQLXaJLgbtQqY0lGn4_OdFSeQpKgOBbkzTbvefGAZJAmY-5WxKkMs6i0k-_zAgjIUrWOqH8PQJCQcH8_zg1y9kfFFihRAy7CPdY0smP15oEN3ozIDYmLXBAb1CazPQePrQQ2GI8MUwE4mKwHm5w07aknP3r70ZNdalK-I8oqrlh-sRjZqFNaMKKEsqs88Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=lbBi_PslCI_crKFUBpT-sPWk0DZ_of0A8ERdZErjxt8LN9fK8KXhPsIndpNmKcU44q3T9DFvLqqVS4309Cr9eTE3zDTahl5KhHWGn5wfFkxjKUT8k9OfT8rPZmtkEHAEJbXtfx3iuJgmij2OA48qjWVDQLXaJLgbtQqY0lGn4_OdFSeQpKgOBbkzTbvefGAZJAmY-5WxKkMs6i0k-_zAgjIUrWOqH8PQJCQcH8_zg1y9kfFFihRAy7CPdY0smP15oEN3ozIDYmLXBAb1CazPQePrQQ2GI8MUwE4mKwHm5w07aknP3r70ZNdalK-I8oqrlh-sRjZqFNaMKKEsqs88Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldYt_evZ6qMxxlHKZwrcyk97KoxYyxMnswFUNcVUmDlXHfFqSBk-N3RWhykCqP-5iW6ds15LTqkkC_yApXOn1CRyD95Cx3A608OpH5nXR9SjtWDGBdSzWJlIwORAcVbtElHxRlQkyh-yyNHsQD9IGZatzLZeuGQmJCGkSjX3C-2buKtmesvNQ6bW7poGHk_OGqq2aRJbK0_03eoegPNlJfyMj4INOmQP8nW0zXSn-GnxjZi_pkSTWXFLmdM0ECJ9dl3mS3xTruU2Otg61Kw08LTxLm7fUuMwH1xf6GVdcpWvCZGJjYtBUnWG4Y16qPeC0ZqaCPP91GVO7kdGR5ofLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=FDAAp3voB8HpE7BlrfB2DymiA-vfggB6Gs05jIaK57_A0rzIESADKkWgBZpRlAUlHwEvnwi8G6gCMXJPfgfQmYMV4VOzMTXDm6weHPYHmmJdFxdpY0z9SKwm_TtK8CvhZi5na0TqP5nLctY-HyjZmrK7eqdr7p0kEVQXp1dE9aKrJQFDvGnmlUOfnA-q6VRDTZYLNTX1c1mjzOsR4qPlODROIz9o5aX6Imtof3qfR5lqW-RnhogMoszCbNqJPV-gucUDBiqAYxd1U1QA2Wf0WLa-bL7gZ4xm5eriI1mt0zrPar1pVK35gPGFn7AMDe2DDE6109mIP8UhXOLQaDK_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=FDAAp3voB8HpE7BlrfB2DymiA-vfggB6Gs05jIaK57_A0rzIESADKkWgBZpRlAUlHwEvnwi8G6gCMXJPfgfQmYMV4VOzMTXDm6weHPYHmmJdFxdpY0z9SKwm_TtK8CvhZi5na0TqP5nLctY-HyjZmrK7eqdr7p0kEVQXp1dE9aKrJQFDvGnmlUOfnA-q6VRDTZYLNTX1c1mjzOsR4qPlODROIz9o5aX6Imtof3qfR5lqW-RnhogMoszCbNqJPV-gucUDBiqAYxd1U1QA2Wf0WLa-bL7gZ4xm5eriI1mt0zrPar1pVK35gPGFn7AMDe2DDE6109mIP8UhXOLQaDK_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPNhCpeMeX3yfNxSZ1Zax9oNWOlYq8VL1Lk0gNBN4ZdNAUZBoYQtgwVW4nm1wskzFPNPc28UBwJeZqbPsQUJ7oi04ujtiTTq8BlzNzqABvttqddBHlSBMxdH6hZ5fwxC-YcMRH2TdDzaKL0PT9HxXL63S4w0QjAx69xHr2ShebsQZB-fat0eE5DKTe_9AP7NA9wui8lN8oAkImBE38y5X22DW7KPm6dL6-rWdJTaNB1AvAY9sd_NBrTlBMwx9fOuntE44zv-Dn2w_hYtAYKRM50nUCs4WKi92LCZgiFIwWTwGMFc2KfaZSxOXbOzU5NCpnMyUvYEbVrNk-6nLZMQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTABo63sY9UrwOKuWU9uiFlHXCEAleEqXIDKd1lGUoCVxpgWdW_QipvZ_JZL4v6WMSt0civsJjz-2wptZziJewIYSFe2QOMKUnscZKnRdGZIcKBbLo3oo5NENyS3bD9AHUcc5DeSABvOoWNtaAUAjMurIGVgk8y52PXYz0oZxZBYXOzF3PNFb-FNrKuZlhRoXVhL5s8dxr8RfTgbIDec9e9lKrs7nZyp9pHvusub66vg3_qiJkDyDQlb46WsR3TzwpfPUacmGRv9LHrPvrbUWyPLbeI0y8ozLPiX7Wag-aPvL4cIzlTarZJA4m0rVhQmgVvQtb_61Du-EsPzqXfW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=NVPooDHdms4sLNTzYBLkZLOCE0_FvUURWuJ2jOim-m0ZSqm7oYCQWzJhV8hRtNjcDwbZsNHc_GDQtF06TsTh38C8xAigs07nvRdxvDmJ0Wq4GZlLOnukDgwNg-i0MsOsEtzRrtssmxMU_c4fu4Kfyuw1iaGt7Vksv5zeEz3vPmMHFPUUQhzIo60axaJSBBZiJroM2NFSQu1UqzUbGZ8CXud3BNtNpdS6e4PyyjNxUT4kBpMwnY3lfrDg-ISIpa1cZ03vuueXAFvvUDY7AaolVvg_7bunh22iegEVqXYoXCes9jNG_8j84ECax7aIfqcIPSRxRDCK056IFqAP9CxL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=NVPooDHdms4sLNTzYBLkZLOCE0_FvUURWuJ2jOim-m0ZSqm7oYCQWzJhV8hRtNjcDwbZsNHc_GDQtF06TsTh38C8xAigs07nvRdxvDmJ0Wq4GZlLOnukDgwNg-i0MsOsEtzRrtssmxMU_c4fu4Kfyuw1iaGt7Vksv5zeEz3vPmMHFPUUQhzIo60axaJSBBZiJroM2NFSQu1UqzUbGZ8CXud3BNtNpdS6e4PyyjNxUT4kBpMwnY3lfrDg-ISIpa1cZ03vuueXAFvvUDY7AaolVvg_7bunh22iegEVqXYoXCes9jNG_8j84ECax7aIfqcIPSRxRDCK056IFqAP9CxL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=I4G6xQ2KOuDgq3A6QECduTrzHAQ6zGsI8oOGxwmEshRkj1341kSGYS5SoGpKN7oI8uv3IHgARi6uRFdaqrPo88zEICyXJkKPAXF505TKUACYt-AUPjHU67GesuhuXRqQMmMZOkNXUeYBncVDUQaYQUwEHqpBbwO8VO6MAyxK4-Ty1Ie8Y14QGvvW8tw2ATz0ZGNtSkFg7UHD5DPg7Pw2Oih_iMKo1KVZkZ7l-wkuHzq2HxcWV2nJIc5ZsXT5NgnV-BaQ85KlO2pd5wRZZg4Q3E6qnRHmQNxtiuiKZfNPDF_03K2_83bJL_R_9b3425LZPkdtxKuW5uyk9KH5S6smrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=I4G6xQ2KOuDgq3A6QECduTrzHAQ6zGsI8oOGxwmEshRkj1341kSGYS5SoGpKN7oI8uv3IHgARi6uRFdaqrPo88zEICyXJkKPAXF505TKUACYt-AUPjHU67GesuhuXRqQMmMZOkNXUeYBncVDUQaYQUwEHqpBbwO8VO6MAyxK4-Ty1Ie8Y14QGvvW8tw2ATz0ZGNtSkFg7UHD5DPg7Pw2Oih_iMKo1KVZkZ7l-wkuHzq2HxcWV2nJIc5ZsXT5NgnV-BaQ85KlO2pd5wRZZg4Q3E6qnRHmQNxtiuiKZfNPDF_03K2_83bJL_R_9b3425LZPkdtxKuW5uyk9KH5S6smrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1StWdzFjnNAxkWNqhCAJMO4JOjW4htSFZ6At7faVW3PKMeLh3b9qD9SCksxCIdW9r-GuyMZb-jm3apbKf4eBLTcFDZRT8SbIYT1bd8f7mil0rLTlHCWsn7MJvE66vuszvDZvPpmL-le3afjpSuzHJ1nDDAdnIIyXtIzWQ7WwQYplBmplVkQ65YBudm7DzE5rbiH39RLNqH8BbzSmGSrq0Y6B0X9-WYNHDuN8JPNvNEymmTDQBGcVY3cMMNlbPDo_esJaRIdZdro0pKSaRKUAg6DWnGt4nmB3LDJ6YDM421o9iU4lEW6dpsgVMZJgD7y3_RSRmr4u_7l7I3T80hqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seNC_cG4ktxqd-6Zbz0MUrpwxhHBGqwdEw_9-Ff3a0hihxKn1TymA0DMGs3ANwf7hdninQnyUfZUZEztd_HTZw-bOP13BMHRzBtWhL9LYPpjXOO3DwQG6N0I9BFFdHS4d_ln17pFexgXuvKmnDDvTqjVA1P9wQXYWbPZ47I5eMOc6Bfynod_-ZKAmjhIjAVrjVQI13ar78va0ol2VEtS-r63TJsG0PVE66xrLFBcxvmfCaMgA4viG20tzdfJFjILq0Et5MbqvKz7DXt28mOTTg7v9MoZw95mV1RIxBbgqyz1iRSPR93sz3Nx7oYxDg0CsQjuTKS_YwB0HVmiE36lwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkKjF3W4-MQeEjBdg-o603jKDvuAdJELRJz2xoP_cfuvcNvsTHedxYn1XAA-FGXH-fCCXjob8ZSITfRe99KMJiBYRuvKtJtLjo607yecMsGovALV1fsd6kpfQBSah03XH1_FUVKJZMO4NniqytxaTSbAW38nXiVA44OIzNhOza3HMsy4xUjUvR5pygkAQRAtBYANgVI9mQdy6fkeYBxk6-YkDLzMxxWOMc14wBbvm8uEv9bvJWuwN5LKE4cck_q0a5Z_VDO0SnDCA_qxyXJ5-k6iwg2Dg6l5q2MXrP3-zDdqDXTDnu4pLtt6nTMAiZ2F66IVJe2P2V9YrPNVKqqCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TCGTgEfJJCnXycZyilskOAJgxPGEAHNh4g9TKpi3kGzAlDRNvSgY18hp5GgVcCkOZQFajd2StlARdtE6Qa2kGm6eKg-0sG6aKSKtGdbY8IGqs_IIeVwbeuu0M4Ybfm9lmPI37ql8ku6DeNSZgOETrn7BXJsoiy-lMuBi5Y8U0oDBCRtZm_unptDa3aHKJ957OHJ4Wp-dTxCg9RZdQcLarEdf8k79JSo50QdOLAfpWyDt8JpQy3H-TutgKmYkJU-i5D8rRTaoxMEA8tJ0YUBs7g3g2nKUPj7Yg2gNUCE8kHABt3qGFx3wQtBlKtgvt7rGH2wuWUVHMo-zGef2lPVZqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TCGTgEfJJCnXycZyilskOAJgxPGEAHNh4g9TKpi3kGzAlDRNvSgY18hp5GgVcCkOZQFajd2StlARdtE6Qa2kGm6eKg-0sG6aKSKtGdbY8IGqs_IIeVwbeuu0M4Ybfm9lmPI37ql8ku6DeNSZgOETrn7BXJsoiy-lMuBi5Y8U0oDBCRtZm_unptDa3aHKJ957OHJ4Wp-dTxCg9RZdQcLarEdf8k79JSo50QdOLAfpWyDt8JpQy3H-TutgKmYkJU-i5D8rRTaoxMEA8tJ0YUBs7g3g2nKUPj7Yg2gNUCE8kHABt3qGFx3wQtBlKtgvt7rGH2wuWUVHMo-zGef2lPVZqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpXmGrKXkuduQTj86uDhqvEV1HOoDRBOEp45IZZYGHgtj7EkEVC5-WxRD8tgGuLR9GfLxJ87uZ0hfacKpII43qnK1Oy6lus_s6Uc_50-k-sh9IGhus6HE2brgq837gaVi4ctapnWEbByhUSyfCxNUOSelnFClIMcdu_zAsbTuM3OVDFBh3tlK6MN5E9MLb1Yw8uyTUbvJK8Et8lXZkd4bvZySfGCCnYWnmKyjntOnSFeUyp0oiOU-K32Jk-xx6TuqxEwd-G9DPtX7os64IQxeRddi7F50lFf-C0-zmg18bPnXVh22FUHTN24Q2J6GwbTV6LwbxUZmkhIWey3RZZkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=hxTQ2lw1sQaCubmRk2Ncx-5BlwmXc39xmC2Dhug-WFKTtM63VsCT4ziQIaFRffVIrqzcORjlNFM0wpj5363OH77QWdoo1K01LpF6lUScCZU9I5qjOjY8rvlWd1jPQ9GWRy2wUv9uySC5jtbgGgwYfEcl7zMJLl4ABazD0Wvniw0vTboWX-APWg6kKr10WiDdUO7keEi_LA5fw3vJXLLGLf9KtEgcPeDAFcneXD7UW1SajHwBIn1ZDRufDUh8zeI3nOF1k2BcXG19bpXuj1meRPGCsWBVMbNsyfhQa6WSMivxEAv3gIakZixes8YkhSJPFF2CLEJHTAag57nwvwNzIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=hxTQ2lw1sQaCubmRk2Ncx-5BlwmXc39xmC2Dhug-WFKTtM63VsCT4ziQIaFRffVIrqzcORjlNFM0wpj5363OH77QWdoo1K01LpF6lUScCZU9I5qjOjY8rvlWd1jPQ9GWRy2wUv9uySC5jtbgGgwYfEcl7zMJLl4ABazD0Wvniw0vTboWX-APWg6kKr10WiDdUO7keEi_LA5fw3vJXLLGLf9KtEgcPeDAFcneXD7UW1SajHwBIn1ZDRufDUh8zeI3nOF1k2BcXG19bpXuj1meRPGCsWBVMbNsyfhQa6WSMivxEAv3gIakZixes8YkhSJPFF2CLEJHTAag57nwvwNzIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kb5GHTWiMEU2GxRZzbTb--6vz-cgJUpukdlIHz1PEidMOu4zMS9d0PjFaSRChTbNQzKSUguBmrZS9STTOjyjDqhSrnbDeEqCrYbkLD4Uhxd3XEI_NAd2M9UN3ZkvmZJ4ri4MvsBzmQWKNk8FqHNItK1YcpWB-7aEVHtF1c42Rxxqu2KzR0wPQuzMG0S6t5YYazKWWuTXmCvlNCn2TBZxKiS76Bfz50QJl2rDa4oadba5Zd52reGLrkbVm8f4zuQ3zIQAQLdolwNKZo3ALZOYT_zKQgfB14AE992BTkW8-eFQZB27q3qc8OO2uGEvUfzksXnlLbN55Uxj67POyaBY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=uQo3Wh6QGzJ9TtYQdVA0Rek4_kyan1x6oH-o6faTkOJvUwl_-0c-9j4Ad907AhVYtgzYo6Q1gjX6V-eoU2sa8gEg1jUktGY4OUsF3OarffoIfHHZQ1kPLFl-SYf2S5-Tp_gcMNX88TGiKYgT8BNx1obRrlTjedklQn51UKsjKmCkcPho51UeU0zJf7Xz4HVZMqppeJ612ghR5qQtZUBSd2edZvAS1X1Ng0L_u4U7mtrBQjBxQJygRMqi4klKeiCqiD_onqRM30cEtLm4J9nJ-9aNLBtjt1fD_diBekPSU_VD0VEWTNsTLW0kB9Fg8HEeq5VX4-O58MvTAcV3yeSx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=uQo3Wh6QGzJ9TtYQdVA0Rek4_kyan1x6oH-o6faTkOJvUwl_-0c-9j4Ad907AhVYtgzYo6Q1gjX6V-eoU2sa8gEg1jUktGY4OUsF3OarffoIfHHZQ1kPLFl-SYf2S5-Tp_gcMNX88TGiKYgT8BNx1obRrlTjedklQn51UKsjKmCkcPho51UeU0zJf7Xz4HVZMqppeJ612ghR5qQtZUBSd2edZvAS1X1Ng0L_u4U7mtrBQjBxQJygRMqi4klKeiCqiD_onqRM30cEtLm4J9nJ-9aNLBtjt1fD_diBekPSU_VD0VEWTNsTLW0kB9Fg8HEeq5VX4-O58MvTAcV3yeSx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKMPG5p1FpPkq2GaXhDIAtMuF4FIJbcFRUbih8xjUYsqmF5FytWtUgpPvQYfsrU-6MHfRMvXn-BSVaoOFzeScdL0wEU1KrazYJuAzAY0hrU4SyADATk_HUwFmPEqBzrkGSwhcLDfgeaBas129ox4knT3UfASGyO02GugYix4GfNX5sNqEw-3jg3f7akfCT8OF0W2JpwJakk0o6DmZeMFaQQ6ajuxeXQw9ETPX-CRSoJwtdBMgltwL5LyZGSHLcEapDlWO1x7B92huyNU9SWAA3YgNxIpMs98AG0wga2aL0ie6fsrcUoFLaMVROWB5sKkO1kBhj5z6iLHEc1G2asMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPU86ttUG8JCNmfU_foLWkn3TWmsvG-QPUETB3C86GQKPsU-uEacnjnd1Nmumky1G5d-reg1iFtEji4O_-hAu53BaVkOCHJtcA8CZPlfhUTHJlswiWswHcAPp3AIFx0GIrgjvjLXvniGBL7-Z8cDiwMgbjaZCs-l9gKWyg7ms4IxDWiTSQtK5TheWayYbipU-Fw_yXQC7thRK6v-q4gB4p6gUVJiLdKWyxmiGvHjubKW9rQkWYCUo9d_cmDT4tcExdCt-txjVK3WgnwgCVmypt30-r1pyAUVn3JPOb-m5O8q41c7RWl0Ke27wjckHSGCCTg4PmYEWaLtlHNkoC_Q2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNYuCLZKEuX6ancA754siH8xA6ce5lFUQlx1eSIKICTVSCIjoVmlPQBBwuZGDnc4K9GVsCGTidC45Def4WMMRi0Sd6bT3e7mJEA5oDv-GjTKLyDESbXS5CJ-Gz5PAkUagdiF8Tbal-o0msAJV0zUtH2eg1GJGhtDK9V327MUG5PEhR-kxqvDyLO0q1HmLvVemQh9x5azCJ8ZnuB0S1iVH5GSDpd2tMU-xROi6dJiNxX-mRZwqbdiGreOPvRrdeYSjfXjAm9iV228ob15Mz-mD_-yoCUuUgJd8kUZWwBDzh9DIFnbfo63Eu6zkX6S4BcKnzyUdhL-TfR3-gSilmbjQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfQOLN5wXwY9PgXikE4B98N8dsI3Hb8ZO-MWQf7SsIzwRqRVGVdikRxSy4KiNyi0T91qLlDRyiz1tmtTCQ7Lc-XZGNlQzOdSOenkaFfeSIdNjOJc39IkuH9VPKUa-IAfowQWFa8XAocsgD44U47IdIf63EeD9odrEQ4JIgVjY3rQlyrPYCUO3GYNb3k5ec9sNL-fPqCUIQYKCBC7G60-4weX0BjVeFP1TX9nbC5eCa7NNfT4_8A_WJRQyk9gm9-Nn24rUwSpVLxpo6lwAjKSi8r_RiBMxW9kN1BpAbCpkxI-ZoFp1zQws2oH7WAHNVrlL977yDWSQSsLFx4yMju57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8sTt0ecYD8vR3SR1XvKHCUz01F-c0HmX9k72XwGiJ7tYatM53Pleb3lXKws-0Hz6lNU2Q7e2ekHHNHpTmUimbwpc_cubHShftIUu--lsU4eGwUirmQhyognLvW5R9dhIbts_l6LbLtKOw3N1dQBQY2Jxpdb0JRiJ55vYtCn4arJhXbJIYdDhdbt_-cmBfhqIg2ESYultAEFemRLqZdqOWEiDwXRmC69sUC9zJkw-w5BUFz3mn0CKxKExgsj8TvZSDtApTcgT320Zr5a8-ZqFpyVZAFsy0lQrsX-UTTokpfgkm4SUXy7JfDMBB9riD4nxbv5f0hy53eeDGMGmeiMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=pCjcTNonB8KXmMZll9qzvyzPDzbq8zSdY7-xjaLGIJLbhOBXhGidm2OPn5dZ4jGL3mdA8Q9wVZnns5mE_O-cEhartAFg1vWXzPaqNZqFtcL-wkFNDI5KN34dT_XcjVPF5KzgKDCOBVgP9XFNNbZim76gCJhYjUELq880FnwlO2PMEOWccfBAEU2xF3O5q-5ZLCqIIp7Tp7xjTS1XbhwunD_NwvOacbdoYapv1qI8hrJ9Q4HmtUgSU4zz25p-Rns5_IiQzJUmu5YI2SmucpAKOEZJzwaUDQov6fJ08ahQbaqMP4fybzESboH2xxUPJlYwECBwSfKBb8dnAPNGhOxKj7ojbed64ZqnUmmWZKe0sBF3YIn0QrN-CgV4SXS9gkgPytTE5Wsis-yIQwSznrW7L6djNlzlyQ0Ihg72jrCGsTNvsNHLeNRSp5Kb9r_bBwu3trVgCR3_wQ-bc4LwRQEYNX5Og7GSCvCZojOC-ps178WRxlJGKRrRpIc9Xz1q7WV44Jl_uNZ5osSoe-Vllnk6AlXbXLZyoCgyHnQ_GSDx2dnc8_qxMHb38afpGtBqAo3skpyyltv_wE3sLyQHUua7mJGKJXoHLHTrM5LbVKfzUGisFtOFK0LO9ma69w3tQtrMzmb7zzCxpbCBMNXEDzTSxnV6UeBlHs10qPgMiwkTFMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=pCjcTNonB8KXmMZll9qzvyzPDzbq8zSdY7-xjaLGIJLbhOBXhGidm2OPn5dZ4jGL3mdA8Q9wVZnns5mE_O-cEhartAFg1vWXzPaqNZqFtcL-wkFNDI5KN34dT_XcjVPF5KzgKDCOBVgP9XFNNbZim76gCJhYjUELq880FnwlO2PMEOWccfBAEU2xF3O5q-5ZLCqIIp7Tp7xjTS1XbhwunD_NwvOacbdoYapv1qI8hrJ9Q4HmtUgSU4zz25p-Rns5_IiQzJUmu5YI2SmucpAKOEZJzwaUDQov6fJ08ahQbaqMP4fybzESboH2xxUPJlYwECBwSfKBb8dnAPNGhOxKj7ojbed64ZqnUmmWZKe0sBF3YIn0QrN-CgV4SXS9gkgPytTE5Wsis-yIQwSznrW7L6djNlzlyQ0Ihg72jrCGsTNvsNHLeNRSp5Kb9r_bBwu3trVgCR3_wQ-bc4LwRQEYNX5Og7GSCvCZojOC-ps178WRxlJGKRrRpIc9Xz1q7WV44Jl_uNZ5osSoe-Vllnk6AlXbXLZyoCgyHnQ_GSDx2dnc8_qxMHb38afpGtBqAo3skpyyltv_wE3sLyQHUua7mJGKJXoHLHTrM5LbVKfzUGisFtOFK0LO9ma69w3tQtrMzmb7zzCxpbCBMNXEDzTSxnV6UeBlHs10qPgMiwkTFMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=X_jpYuEluWSGA03UmBcVvijREZSsFHSQu_YkkhGKN4Ucc3pie1UEUZg2CorGwZ83tiwFjwYwLzVKg0h7qGftw0z_mjposj-wgbjsxzNXf4FioMiDou6q1u8q-BDC8xAn5rewvpD3CuicFsRYuozdlVs6BZLV4lPD6oNAQafwAGW_chEfZqFPy8nBDfP2F8m4Kk6un4pQnmoH1ISmrtRdwt99zB8wiTajHp6H3Jt8rpSYeeqGk-sfcFYw4dlVruzXJ0Jlo5yCUe7U9sHuYDYgPK1oNrPzxntg2KYeQXnFiyhNMTsKbyp_rvVeIaNj_LahU0kXC9Wl1386Z2dOy-PkWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=X_jpYuEluWSGA03UmBcVvijREZSsFHSQu_YkkhGKN4Ucc3pie1UEUZg2CorGwZ83tiwFjwYwLzVKg0h7qGftw0z_mjposj-wgbjsxzNXf4FioMiDou6q1u8q-BDC8xAn5rewvpD3CuicFsRYuozdlVs6BZLV4lPD6oNAQafwAGW_chEfZqFPy8nBDfP2F8m4Kk6un4pQnmoH1ISmrtRdwt99zB8wiTajHp6H3Jt8rpSYeeqGk-sfcFYw4dlVruzXJ0Jlo5yCUe7U9sHuYDYgPK1oNrPzxntg2KYeQXnFiyhNMTsKbyp_rvVeIaNj_LahU0kXC9Wl1386Z2dOy-PkWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vm0T5nqr-sVscw6Sf9s7NnpSsysEYoIzNaTEcjCkLd77pEJxKKHCcA9gCiFAd2T024QDdweOvIlPp3mOfZYA6maBzKH3jl9fXeRWEefRl3iP2tiHjUkARu4zuAT46GVf7H-9sxCrK8w8jMoI9FtL985nZ3CIbSRg9q8a-2pAhXyTWwVdwnG5RYGqXMo0utYq8PeKvnF6nN6OQGg-USOgNhdTqzCvOt0cz05kKGqwHUKjHRI_6s52cH-CzaCzBkXBARwL9R-0eF7JTGsoJSPErVIV-e5LgiHL9_HZmMEkOA11dHi9lphPLrL4qvRnSIOByh8weVj9cVLJtP-3de3FwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=OW-jQoePqIRlaF0ofDaoZeX1e0oBDM3zYO3sDqDKAN5uaCefyJiwiYIu61HAJ_hIDQniXrkSWcI1jbNU1gokG5399GJ-G7i3R0KOnPAHmfHZFwBJAiki1cXDbhOFROR6gFc7ni_77CrUc0GcP-__R0GX_mHpuALa8323PnYxAC6EVdYtnwvJf-j8Et7prJsDvC69XeV_Wq2Na2OIi2iMMZwDhLywReY4rzXiNA0wkwCw2zAcY5LBnYI6Obs8H7qHKmOjkX35t6fxlsDqUiFNIYLDn0i4uIY2X-8-O5sOMHGgJJ8LkWgxWydbcGeirk57jkjYxMpwMteIgWvDfINQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=OW-jQoePqIRlaF0ofDaoZeX1e0oBDM3zYO3sDqDKAN5uaCefyJiwiYIu61HAJ_hIDQniXrkSWcI1jbNU1gokG5399GJ-G7i3R0KOnPAHmfHZFwBJAiki1cXDbhOFROR6gFc7ni_77CrUc0GcP-__R0GX_mHpuALa8323PnYxAC6EVdYtnwvJf-j8Et7prJsDvC69XeV_Wq2Na2OIi2iMMZwDhLywReY4rzXiNA0wkwCw2zAcY5LBnYI6Obs8H7qHKmOjkX35t6fxlsDqUiFNIYLDn0i4uIY2X-8-O5sOMHGgJJ8LkWgxWydbcGeirk57jkjYxMpwMteIgWvDfINQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=lv3dpdG16QiSK3SXOQsV5TfVCkcdrc9jVcGZX2Qnwlc3yS2mUE0ChiSUpbMSaUZ0WNghjeSAp48xd7n65XSe4L5i6YXJkTSMj2QQS28d9F-thsDrpAN0RW8WHpMKRBoCQZ5rREepI8pSSyS0LF1ceaHWXPZy1sN7vtiYtfhVw_ExOQOSB-6w4LmtIcknQL0jsc0kPb0XdDdC5Ni7HVQvjZ5AkY1tQCGPZrseG0RxdrCtZ6G3r3t1oC3vfUhM1fW8GYG9mA1xHtG_9bTebUoO-W5umWaLg47qT6nUtSEjELa4MVGXNRYegS4B8RZetLI2D3K0MTdwTNlcPYC-aGpdeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=lv3dpdG16QiSK3SXOQsV5TfVCkcdrc9jVcGZX2Qnwlc3yS2mUE0ChiSUpbMSaUZ0WNghjeSAp48xd7n65XSe4L5i6YXJkTSMj2QQS28d9F-thsDrpAN0RW8WHpMKRBoCQZ5rREepI8pSSyS0LF1ceaHWXPZy1sN7vtiYtfhVw_ExOQOSB-6w4LmtIcknQL0jsc0kPb0XdDdC5Ni7HVQvjZ5AkY1tQCGPZrseG0RxdrCtZ6G3r3t1oC3vfUhM1fW8GYG9mA1xHtG_9bTebUoO-W5umWaLg47qT6nUtSEjELa4MVGXNRYegS4B8RZetLI2D3K0MTdwTNlcPYC-aGpdeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He8GJGXHj7iKXSY7ozSrUA7mXZ1v-n9p08PtXIAyGUHsUjb3irgiav7fV7OWwfimhDr1fmCcDp0AlJfeBCBPvq0jrzkPzCz042tWA8OlKJRlq2lLdhS1RTqUrbSo5RCLiROKZwVg5bAFEHJYNhVjeGsaHzj9NlTzu_2C5nA-Kgk5akAUkhaNN49jbsZbSXkFffKqhUBPqvcPzo7gWNErWOeY8kOO8iXpwKqYONE1m0YZvgaZR3ZNW-BWetoN2rmfx0UElo2lvKWZBLXFgX84N2UbohxwSQ_HQuzTMgjS4ilzmDURDkTfgZkbfmcqR9-7A4Gar6qJeXmYSeypOwPDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj8CR-Y8MdER5PqWP3piyATcrNE_k58moWvaWAGsm_k37Cvxz4Rpd4PPdL_hLzk5StYBPEDdOmq_Au4aaRszV3F0JATNBpD_2UE_V_GygxudFLU8dA823AfoYkVNA5Nz8uoalryQno12HpXQgKikTcnyaIj3bORYTg49aEm2XZRBum9FmBh8ocUFf6TGgGei8ymS6rvlbk3jjk9lGduMKvbL3rP9hw0d_0vEwN18LL_I48Pbz7fih7uPe9aieQF7BGwceAOmUa7y96mUnw5Kqbm0dPaQcjsfubPC8SvRxGvxT6rPvLxz9JJ_LGqdXjMMrjRfjcmePQI13WeTxzDSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmOZkPZ4SisB9b-EfPqQo84fH_8XGsNVAL94kShfmbQhbFCUswidxKM8fG_YEWhKjVFHyRhwo3jXL2d_X_tu37uRvAlpZFnrWR-K4LDdURXE3U38a-p9GVrxZD47oAyv9dVE6OuB66EZJgjL8dlBpPy00YuxL7BiObQzfFz5dFjhOVbeVSo5FGDvSdasBELfsJrNocIElvcfmOhcFp-RHst-cc6s0djaySOPtwGbc-_ev4GOsBzCFrDq03sAKocGBem3ItRoSog_b7oMDkyi0aDRjn9OrhgsUi_vMS7fYguznM36TII9b17DrWkRbDEdXdOYLe8VN8_ahXhFYwPs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTP9GZlbiUW-LGXVBES5AQjYykWu-DWnh4R079AlG2wozI6bNnmUJWOpg3QS1YRpyukYdscnke-ie7kb6w5ANbA71u6shw2gMJuipF1vLfH_JxaTBRUVTaoqf7Xd-Tj7brn218qIGrw6zmLsBbRpL4WRNlKMYsShllccE4oiSelTIKVKLyb4H5Tzfx0hUSIQhkL0H1UxSO1ojLjEAj7nlTW1Hn6O-d5YTP88L5w3-uq3ul9XQ3lBlBDMdRSm-sI-F8igIRgfTvaMpPe916jUamE8LUW4hhtTWWKYX8vW8gFPH3qE_6eWm3qlYzfsv_-inaPBjhFKzSGwM2Dj9t23sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=bfyeaONM3bzZttE2aW5FwNh_SrMRyBrjaWDHerQZTUtatlNkYQrqMuESJGKGTVXlSKAviJ4A5gRorctOa0aEd_TkqZdAC0na7BCwWrEK7cAXBELCXbhArW5II47GSxEch_RuUsvP7dioIAPXNE24RccNw3sw0KPNo0Xfq1s76eaoXm5buIR8bpNTc93CQFGmbchzWnpB2SYUdYofRerJhaTF8RtCnRzkBGdoK85ndPyqTpvGudj_Fd3ajFobSgcYc8C7wWHmYRkWCZ6O-hG2ev8q8uafjtveiRIrvMPJLL7aMBPcog1wA0j0-XzOXz3SM7qFSI2_l4Y-at4tq9_Y3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=bfyeaONM3bzZttE2aW5FwNh_SrMRyBrjaWDHerQZTUtatlNkYQrqMuESJGKGTVXlSKAviJ4A5gRorctOa0aEd_TkqZdAC0na7BCwWrEK7cAXBELCXbhArW5II47GSxEch_RuUsvP7dioIAPXNE24RccNw3sw0KPNo0Xfq1s76eaoXm5buIR8bpNTc93CQFGmbchzWnpB2SYUdYofRerJhaTF8RtCnRzkBGdoK85ndPyqTpvGudj_Fd3ajFobSgcYc8C7wWHmYRkWCZ6O-hG2ev8q8uafjtveiRIrvMPJLL7aMBPcog1wA0j0-XzOXz3SM7qFSI2_l4Y-at4tq9_Y3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suf-kfu2iyvn026G2WffXvCZd4VY4BOYVGTKXmuT-c4xI3O8hzTp6jphabEJBOu6V93OzND6hvZajJOYX1Kw14CxFBbdOSw8zejopHE1IMBf6aDAqbUeSoDAYBf2rRbEiYbDjLwhp4SVu2jL39_nYp41HMv0tUsinrLySu93bthYqCtK8nH9T0j7BfNthYggSphN8LDsU8TbIMQ4NJU9CPqXiXM9BsM1Z_L7aAx-3FxNk_gV7xHglzysGdK7aC-msrgOib922Np0Ab5p8ZwBppbyGOF-iIlZExyxqiNppcTxkGfhMkA1RQbJwYUhsBD1e5Y5bArVeuHlT19Y9fdGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF8Y81TGuRmOsZ1X32bqs0p6SCKEkef6oV6L6WJuTTBo_rE-AIchZ6LPXguW3GrsAg7PU0mD38XmkLCMsihijCjYz7zSzoMgWmEosjO6nOA1c9SRPyAha-enqidLjEvjfH3fnrDOPsrHdokSHkFNmSzaBnLs6TO45eLd01geyCNoMmUyiKbyxzr69Ek5YHam2sBvAbPT1zNurGUkexYF9w1Bli2ypqxzVUXPFnP0rURGQII-OBl-TzA2Xa6JJaFGw8URVgihKWXxGPAM30ikf-5TCu-YBb8YvXj7-cSpj9HF3V7a3S_MvnvG0DOdJZvI8fHTaEsfLJAjjs_L4wL36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=PbuWApFkj3etdcrqL9twfX8UU8rF0vFLKGXOsN4eHwgldFbKjdUewAoIdYl_8RK5q7VWS7YvNOTL50ohSXVAxu2wBkmFE9TV8MOVJao-472tQB-VP4vCSn29skP5XjOvbNqnI0MHaA9klctQ_sVbGsZm22X_vzdjEYWoSou2E09DH5G_ubK0GGrcNmRQYNTmL5ZuiV2k-S7wtkKZ4cGZS5RtEKqTZXHbQ1DDlJsvsoPyv_2p6gurIR4WA3RNx3Nw1gbOca09GplrPtvyJqfjDWYBiohZ_cUbiRTAMvTO3DTnObGfYh8jZ8MpaZEIYnPKmnVZXREk1Q6Rs0IjKIELCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=PbuWApFkj3etdcrqL9twfX8UU8rF0vFLKGXOsN4eHwgldFbKjdUewAoIdYl_8RK5q7VWS7YvNOTL50ohSXVAxu2wBkmFE9TV8MOVJao-472tQB-VP4vCSn29skP5XjOvbNqnI0MHaA9klctQ_sVbGsZm22X_vzdjEYWoSou2E09DH5G_ubK0GGrcNmRQYNTmL5ZuiV2k-S7wtkKZ4cGZS5RtEKqTZXHbQ1DDlJsvsoPyv_2p6gurIR4WA3RNx3Nw1gbOca09GplrPtvyJqfjDWYBiohZ_cUbiRTAMvTO3DTnObGfYh8jZ8MpaZEIYnPKmnVZXREk1Q6Rs0IjKIELCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrnN8DaZemkVus4aI1jpnYTJlE0E0Hmjz0iTF3AZXAaKevNavOggl2mHOXZA9InmCgL7gWkP26OR9Bnk2dpinmWVzG2fHJKVCQ00g5qETThi7nVcgHwqG5JgvDBejGI9Ekg5WYfq7dluDJrpTMghjCLEpnaXpmiaKzEJPUnFeEE7tfvcm5B4wnkqthDU9ELYa0KwPDkOTi_M4WaWvRRqCzv3mLy2vjVvTQlzcyWNjC4EqKjZz92-ULzqUbY0DRSGzgNJZFXoPrOduotYzcbg-OVkeZXFRCJczrnIzMJauuV0Z2ZPf7J4iKwlZ8CvN0iZJyTZMgU_IUt5fS1RBeXcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giYF_5Ya84dUNuCcDRq156Pwu0Ln0rz8o25XB7WA6D8WgNpQZxAwjv2DA4Y1b6BYY8jj3noEzOn-6hv-ScPqAZGTsHzUGpOE-yOmNyL2xODhHnz0syUOVlQVP7A723_GchUWDSa2Q58e05mwxEWua3Dw8PiclhbbP1spebGGJyFhBoVz77J7bpkJ4HNVBp3Rb-CSCeSBTiEMX9pis5n2Ty-FAqPjxEaK4WzWXaDT7kQMdHBt21yt0b3K4-VBngX5518JE2yE-h5PW8AMQz2V3OwJDwaI_sdoulbgXCBKoUyXmGRzgMDxOCjCHNhlclt_i77U-mi-ih5-6EGbpaVqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5jvLMQBPdO7n0d4VKeKPTrFuPV-tSOAFecFc-xqkZfYVRgDpStzWi7hvPwz-K9IQ4ZVlOCXy-7qjQFXJO8bRDIi36IoKeuWPvy-dHrO0VfySwjlMWDS2-c0FIKDc9YbxVqAqwOlouEuLbVWbcXjWyqhZorZXc24xKhy-4TSFUzVlCewCAca_YW966R9xKYcyAAqSptx5egQVWFLBVnd6vk5qx6DNMVAWyJ59rNkkPFNSwLBMBNjoXKsVfFoHNHJz0ZYfVngCN76vqaSxLkdKRJ38ZR24q1w1rtl-zpvdKm80Em5pSNSKvhZv4_umMrUTJH3UIyRgsv4IUdrnGapDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDB-eM1De2FSV-123Iu1EugWI29qaVtHCiUD6gWdYn4TL7UQWOrICFqSz_S7GnsNAlm3PQuXAME7_sXylot0ekDT49QdXQ1qz4uO3e539oe5pBrOeMRiPb4egZRD888sCOmY3cm_q_zVZIqq4S3Z_FZD-_BsUfacX4bePGxZP_TznUGTHbuJOOOEyZA2zkzSET-EpP_-X6EL5BD1M8rVckCEOQ8xOYZw05VYmyAJUCg3Emh-e6HZ71lWwhIAyYxIUNcqQWLI_sZy5wsZSAO4KixsQV3l7LBDvCuNasVUxQ4zdOhPTGVeavocHQRd7yUV5eb2sy5X6Q7Wfe16F3RvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=q83slwtExtMC-3VZg-aIx9U8SOMcQ9FZEgY9SWtR9T5eCDRrQeXwOz79H7dTAzDoReS4d5CVCP36s1TQOjgKmaJ10Hgw5EaG3AfGt7WNF3w6Ivmg_QSJpC6aLiF8rUFaCg3v1Doyj4VCL4m_yt82UhjGr6dU0U6u7NluVutePZ5-Qqg1tWsWyAIbzN0mLTlSdM3lSQSgaPzw5soVALUXCLjNwDwqv6FzKQxJTGAX8YLP3pwyb-rO9n443L_S-1TxTc8706Xrt6TYwrjwNT3__zR02ErRRRO9dFNnJDRM6sWb4eXc4tLsOjjZ5H-DKiglb9_znnzzSJMJStzLSlzGcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=q83slwtExtMC-3VZg-aIx9U8SOMcQ9FZEgY9SWtR9T5eCDRrQeXwOz79H7dTAzDoReS4d5CVCP36s1TQOjgKmaJ10Hgw5EaG3AfGt7WNF3w6Ivmg_QSJpC6aLiF8rUFaCg3v1Doyj4VCL4m_yt82UhjGr6dU0U6u7NluVutePZ5-Qqg1tWsWyAIbzN0mLTlSdM3lSQSgaPzw5soVALUXCLjNwDwqv6FzKQxJTGAX8YLP3pwyb-rO9n443L_S-1TxTc8706Xrt6TYwrjwNT3__zR02ErRRRO9dFNnJDRM6sWb4eXc4tLsOjjZ5H-DKiglb9_znnzzSJMJStzLSlzGcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=FwolYeGpXs7Yv7IvqzQEuOUl1no-EoSyPBrFJfmbAnBcQwaBBeH1yiYXN1XrTXEtzoO10ha7RuGJLY0wqNfJexb1Vmdd2ueQilEUBHGCTmY7E26BlKr3KolB4Lma6csx56W7rFqsAN83eIwCt2mA8H3NolKG-AKtdr8JXwP-8AoWYVtZQO6eXAr7P8aKfKZwav6Iw7QVnFVEhj8goa_pweKgvOOHgFQp2t1Vo7kW_CN0Ia9uviO1eR-K7i8h5I9oCwQEtQixF0W2F8OGxDFYSmZGy3xNnnbgdkHRNs_2F5Vn537Pd_PNDs4cBSLvEotmnpT_hGWF019jNpeIsDgdEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=FwolYeGpXs7Yv7IvqzQEuOUl1no-EoSyPBrFJfmbAnBcQwaBBeH1yiYXN1XrTXEtzoO10ha7RuGJLY0wqNfJexb1Vmdd2ueQilEUBHGCTmY7E26BlKr3KolB4Lma6csx56W7rFqsAN83eIwCt2mA8H3NolKG-AKtdr8JXwP-8AoWYVtZQO6eXAr7P8aKfKZwav6Iw7QVnFVEhj8goa_pweKgvOOHgFQp2t1Vo7kW_CN0Ia9uviO1eR-K7i8h5I9oCwQEtQixF0W2F8OGxDFYSmZGy3xNnnbgdkHRNs_2F5Vn537Pd_PNDs4cBSLvEotmnpT_hGWF019jNpeIsDgdEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIT-Z6N5DP87JQij8GljJBaKAIWgBZLrnnMVbDdAcYUCq_7nmBSqh4NtubwQG-4263TtHQtvijedGW5xCV8D34XXow2IISS2l2gxoFY2u3vCJ6fnY3mbpOnn-3BWW4gU5S-S3Ko9wCwraZDHFPpXokB2V8tSORoVy38pVRFLDdvMz-Al24euVLKWHaC_pF-oY-QLSgrUtQjZGJmQhPgF0HogZ2zyCvO9uJ49uxq0dpbyFLfKc3nAb_Q69ZlWME11SWbdIUV9ZRXGAfDYDwLyp-u4UwHBz-Firvgq6HDkLWQhC2SKOl6g3BUq-62uxzZWtdkTg4bNg87a0qm0fhAthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=bdnBPqUFDL-7gNTRgRRnLuELM2kFM_buVTnMmGvDqseao83Hl4OzutMP8dH_XQMNt21R86hTGkLuZ5gr20fSzV3iFmbR4GuGmtNS0iq2a1HHYkqIJ1ylbkXtFTvQUQQIfitkti0nvITzg9QDQqdjCos2zsiojxEuhdNTl2oaHA9UrL95hKTjv23yM6MklCxhEhC1wuzoaXsg_rlK_t_hRPDaN_xN3bGtCQvrdS4MIZLJcmAxzm2fRk72MRK1ukx7oArwIBjCGM0wuioW11kDEWqeKB4ICrsqvojE7hPSk_7Dqv9N_uXFxk7OPCRzRtqr5PxSvAwGp9_NSrwvymzonQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=bdnBPqUFDL-7gNTRgRRnLuELM2kFM_buVTnMmGvDqseao83Hl4OzutMP8dH_XQMNt21R86hTGkLuZ5gr20fSzV3iFmbR4GuGmtNS0iq2a1HHYkqIJ1ylbkXtFTvQUQQIfitkti0nvITzg9QDQqdjCos2zsiojxEuhdNTl2oaHA9UrL95hKTjv23yM6MklCxhEhC1wuzoaXsg_rlK_t_hRPDaN_xN3bGtCQvrdS4MIZLJcmAxzm2fRk72MRK1ukx7oArwIBjCGM0wuioW11kDEWqeKB4ICrsqvojE7hPSk_7Dqv9N_uXFxk7OPCRzRtqr5PxSvAwGp9_NSrwvymzonQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=SGRoDPiDEpNbcjqLmK6dNZBa7FHS9GDU0c3ww2owz_ACqec4oSx0llGRUOCf0KWD3VthPVqHuL7cvxiMvkssVvrw5Ph9iyE2UerCNUJbUmwQ4Z6krBbkCM-o3RGndQhbNoapvhYtgbXtjLIqCqfP8rzCDU84UkmQ9OEREQrfiXB0kqHW7aSL8spqqpH7MImAGiwgXwAX0CkrNEWY_Q_JqjdfL6IwkP9t60lZXlRK629toyzsKW7ax6yh4YLLEt0r8hXA89A05gKklGCEFxdZWdDCbrsPPqzXmh3hLaJwwCi0gpAIRbjYGr4r9YiFmWcrT624Mhp6siA7kXXytwxJmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=SGRoDPiDEpNbcjqLmK6dNZBa7FHS9GDU0c3ww2owz_ACqec4oSx0llGRUOCf0KWD3VthPVqHuL7cvxiMvkssVvrw5Ph9iyE2UerCNUJbUmwQ4Z6krBbkCM-o3RGndQhbNoapvhYtgbXtjLIqCqfP8rzCDU84UkmQ9OEREQrfiXB0kqHW7aSL8spqqpH7MImAGiwgXwAX0CkrNEWY_Q_JqjdfL6IwkP9t60lZXlRK629toyzsKW7ax6yh4YLLEt0r8hXA89A05gKklGCEFxdZWdDCbrsPPqzXmh3hLaJwwCi0gpAIRbjYGr4r9YiFmWcrT624Mhp6siA7kXXytwxJmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSbXdKoHrN3L47955d5LTJL1-5R4zH7moWohfuSsivJhxJNwAirSybV3WTN4lu3nIfmlTtMnduUhEXIg3uTcRMgMNPdhvt-YwwV2KmKOR3hlw9TlC9nraVwRd_mqPsaRPnFkaXmPO7gjOqK2x16KfW9Vx84FLnLQ5RWl63Mu-4nJnEsbRgzk34hBcXRIvf3yQ_IaseluZiSkdMcHMBpsawBirFBRn_eb3FX-PAACkTClep9egrlL--zuVjIf8xjPObNnYRbMvJlJ9Qf5pKzplDxUElG_V74LTi-k-ewFAxCOVuxGXCYZOA7FkYk8hN09m2F6KTFmwOjGXE6gYPYt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEWhhVEzJKJnIOvt0H0Eb_a8OqqJZR6Rr9aetNzfJkcTqLwOQsWq7gzSVySicskP9eoEhkirUI9_vrnPuVvWPpNhSSsR7KYxRAzbIPbmJ-iiasmhFD6PvJPt89ROosqhJaKEiXJshwYLLPCvAdciV99kHbPqFCrB0z_0n1mGfWgDWpdUV0RXPKomhOFwwsiGBLOTYtrDUWkBQkOhf9aGD3Wh5UqWzJxxXdOcD4QT1Q1Rr_zPhGyh3ZIdSW5OAVH0Wmj_fz-cejkkfTJrZJZAcIq4y6mGspskVhaxs_5F6kdP7FHsAwUe6ASc8r8crJExzSLS9jAMDnFOZEHcTvT46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ohQirvlFAvQ8zT1o1vJT802OoHDvRRQ8wUka-ZI8dfMOEsSjYkelFNtjVy5dxdGggUY5IgEnNESLOhhDkg913VWlBzqoUT0Ju9RtsChwPtXUSSBD4quMywyzcfYcKPrtQpwZysAwBuXT1dr5vNQ9CeNlQGUdDB1IfZSgAlXmdzoFBIqVWEec9J89dxuHtCLyVvFSfaiAOgDkSxIGIMXVhK-kOPkoa5C4jflldDDcDEkb30Tb5LH_KHLQV2lHj-WjOKw5WBNeM2CaL3fZwqx_UFgFM1xygszVngQUqA1fz-kwZtR67HQWEN5CMpF3HsYOVdtEmfhVEuQ0Asq7laaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5xEb7r3RzOLrYOkAW71DLxofoOmp6O8lmAtgUdwp6eTbFHk7dwjmt4gFuQ7dyCKUNRS8liqjSsDPLkIVplYaVcBGaovVvbX2FbGHDQLgmRb62jbl_GZXTvrKMihCgu-wPrsSoPC9Ue1RYkPSivggjxbWP99pbDwrChrjSA7d-rztC4Iuv3ar-GBuNcuVdmaU4vSd9UqzI4em2rDBAD2CcBH02y_Lepc-3-S36jaTM-FHixPiU02jqnUeCarW1CjbfReJOV5oXhvBzVPhzdzHOE75L1ihnUiqplFHPQWn707STg7htOKoW7bqHaoEHzV99TfkBzBQiPoVWf5zjCvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=X-IDW4RBKweS_9E2QP1RHxtCYNkjHc9rfPKjRpcbyfS7wA2nTG7W6p0l_xNYPXuGFXFEsMmRooFlZ91MPbMjrUoU-WwR-WhIF7Eh_VpioD0EGIcp-sCImjMCpr3-LMIGwYJp-VcNIW_nin8O-XAhbZhidujJ2_SwxrvwFMu6vekuuDPnOEy_uZfzKfqgIdwMUrZxtC5fBZdjYiWPIMZzrl7nKiJO9pSRIGJF2zvCguy_5l7nVxNTw-3sVPP1SRT7QjpcYm0aSJs5GdIPOR-XgKUTeBrPL2tP8-6G8l4zT7F3X29ssHT675NvHl8jXQHAJ_Awzwid9nlrQ8DTU1YxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=X-IDW4RBKweS_9E2QP1RHxtCYNkjHc9rfPKjRpcbyfS7wA2nTG7W6p0l_xNYPXuGFXFEsMmRooFlZ91MPbMjrUoU-WwR-WhIF7Eh_VpioD0EGIcp-sCImjMCpr3-LMIGwYJp-VcNIW_nin8O-XAhbZhidujJ2_SwxrvwFMu6vekuuDPnOEy_uZfzKfqgIdwMUrZxtC5fBZdjYiWPIMZzrl7nKiJO9pSRIGJF2zvCguy_5l7nVxNTw-3sVPP1SRT7QjpcYm0aSJs5GdIPOR-XgKUTeBrPL2tP8-6G8l4zT7F3X29ssHT675NvHl8jXQHAJ_Awzwid9nlrQ8DTU1YxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz0Ipy_CQP5ZI7KyX-GoBrYHnFVvdI_y4LjbgyE5Wg2hwd_1sQM1Q5F-izH_JOoFLaZlQnxLbsNdeJptIeJS9_ntnPpIrT5cNSNTS7tt6RhZhMWz4-5Wmi6E4R-mMRsxnViPVgFQXxQkMzEQrxoSMMJDVR_GbVu5wBRyz_WFEZhp3CVjT2WnS-1NDtsXuAMiVdONR7bu_RjVL3vHVnAA2TydDIlaYD5GG_jQlvpgYExCoEL_xIs6meoJmB-pDlCMh4ZMSLyWm6iFMCtyD0aWlNZoK9j-cYiumeBeUyJqEzpx_pTfb1us_26AOzXPF3ZRm0Jf9zBjeMRaUJYF934AVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=G5zw3S9keH_gPcljh2SNlH-mewqofg89Mr3Ede7CKkG6-Y7Z2B4B18cNm8ei8CmuQCA1MTEKPBuj4mR8zEDFFV2D9xm6KoKioD827pDZGcxUG4xuYTqmvKRXKixryeH2MvYAV1TdgNgXmZZH7Ig3oGgdO5xPhpdJqJ4xthQfYu9EGQMlTAYOKNhbeCajsrttmb8boHJRGOFWEYqzlZ3dM9ZyyP32qVohYBs3pHxGF2WeHkFkKi_OeKZAqyGi0VxJsYOTlNkB8P8vpLT64-_zhzLOadJde4RP8rxWBhOoOwrFveOrYMh_lxYGW0olJWRHOiMOcnWyLidBvwqB30afow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=G5zw3S9keH_gPcljh2SNlH-mewqofg89Mr3Ede7CKkG6-Y7Z2B4B18cNm8ei8CmuQCA1MTEKPBuj4mR8zEDFFV2D9xm6KoKioD827pDZGcxUG4xuYTqmvKRXKixryeH2MvYAV1TdgNgXmZZH7Ig3oGgdO5xPhpdJqJ4xthQfYu9EGQMlTAYOKNhbeCajsrttmb8boHJRGOFWEYqzlZ3dM9ZyyP32qVohYBs3pHxGF2WeHkFkKi_OeKZAqyGi0VxJsYOTlNkB8P8vpLT64-_zhzLOadJde4RP8rxWBhOoOwrFveOrYMh_lxYGW0olJWRHOiMOcnWyLidBvwqB30afow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2rNOXq8n2WSdpUdNjmZAFdmVp8VbpDj3643GaooKbaEXpEWck56tiMxF4JJvU0zfE7Phlk7PWg6uyC-Pz5CqAT9lOMMByeF0PKlstRAalII8yfE9PhzvQI33pqOoH7W5Wm_frL6EQVbFrzPbkN0pI148jV9XUXd7mYa6n3mXpLO_pr8wYaRtwdX3KwYqNkfHVqA-6XJjaeSKwBatuf7WrV8sqV350AUolt76hirKBFR5tP0yqolqY_gtwYzN6rYk0BOeDn8YWx-v8NJZgHVSf0jzaouEzccTFoTubVhBa418l3h7f_-2FAexgCbS2GtTdaSA4LYZKpn8r0eiiV7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_mVGJqsZj4Aajoc0erMm19UrPFo7HVursHbeJGYy9ZzyaklkJNFOY-rz0MirkOzSnv7iLaDI5lGXwfX6TjZBwZOgqjGhJ9P44UQwuvw06hqP3F7txl5rzUJ4-BbrYQjkvy_CLcG8t7-vjDgfcqshZTv3CuWH6kbLX_y-J-WrIn2MYIp66Ny5TpOoDcGmjJQoHQqKml3tERunqQGgD7ggVctWs1J_4QgI9MRsgEq6_WEm__7Me4u8kbmFl8S7MTMtu_ZQGBsEXBVXC9VkrUafkOQGAI2gCHH63_gisVH0jXxeustQ_qgmdTCukeK_OZOSLOnSOi0G1JRm8RUj4m2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erKoVqIAkPRhmGl3frsD7n9HSuuJJ47D3ww8dQuLSqqZMEjFSkkYt6nXEeF031KswPMFfxyXdh4-kKDwM0GX1GXtf272Mn0sNiUNNup6KTN3krV3IWM-eWjrUhK0tsMUe_lIFzRqj0XtFxAoiYEzhNYqgVbnWKAW4EegQIr30Na0fSLUd0sIyjb4xGvBF7XPpmh9DsgHpmWXwJn2gRHxeUzWY_brWYRKwWemfMoNsHFlJgWyVOXULQRRxHBeQRC6KMi7D_6kCFCx0tAr9AzuufMZX4jeDlyvftbfN-w1gmGcWIJTii-NKLD4_Lr3AoT6FAQqbQWqX-Z72ABtxM5_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtV9Fec1O8WeLpEpEjkiJkp1dmC1ZXP1YPMe5MvQwTJEsasm-jApOhbRbqwsn63Jc9kzmzjGA8oo62EnbrJ3fJFatpZnf53M1oznjX1dkDFbxOBJCxwn5FMcirP-B6_gZUx_SpUNOo4fr3aS5zjVXXHke_mp8-W4THRG1DHVHgzQ5zhfO9mXlMde_0o29qmyoAMzcljs3lZhIhEVlhTfoJz3qCvkEC396gVT89kzBFudJom1nPoRJvBhEfcSe9UpdksOr6Z0WHZ4XlIcxE11WY0coymUlb1pBG0IQBIY2W_4KR1ZYZnujIrdpw07hqeod5M6uEQPjYAmcXxAJnZ0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6n7ZCfSov99zV8IddnG4cpezI2SInoDfQjrhSh1fpjumDpcCeu583a8CbQZpRoCsXYYTOBhhhGe3taX7TE28SnAfBwG3oBfDSkdoHmx7N3Cew8v4BYVp3HAPeVpMVd-gd6Oj5USJRozsUq8V7nXPg-Eo1gueeEN8U9en7gd7MA3DIA3r-ApZHGJGZtkcJtQnK9M7uoyN_YYbo4vix2bPhFsvMRypFjF_lB4bROqF2S_lyPc4sEdTe6uAeoA8S7RFxVw_P9S2k5NMd-Q-57RMZHUfSrX-BZs2M9qGdbLtZAhPA3nGERlQ3sek_h_V1F2TwcolLO4vXqdtjH9xmMFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKqtL01Q4D2unKroQ66VaBV9sId8zdptlqjlUAx0ZAg7RcC66KgSHU1We8vCj6P2s4mfyZj8p5rT7xmv9aWvwKOYnLPgehSNfJR8Yz5B5g9jn-qoZI8eUxiFg1oYY37v9bEuVd_zFaOPHPE0-SgoXNYOIZ7umpryyIhGxsunAh2dDwgNtOTowQJIHzdXiSq54_OClrIROuFgW4WRL_G5xlr7mKL6V13GxeTezhROtYdxg3Luc6PtzwFqkDHZEZaPHz4j1yfNO_lvW2u7OD7eB-Eqv05Qvpg_RHDEULBx3hVev7-BYW57khJyejNDz0wfZz6JAhvUJ-qf8sT-NtdAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klV7VXX8_CUJkc3tZkuqqrj1ujtZeJ0MCNrFTZDRga8ehIzenoi-WI-WsdgDz40W-6qnYMHFILLsgreWjQuF89PhAr30MtP3un4HhuC3ZmtMWfsXAhxGC3GxGCZcZITRgompnjMw_UgfNPOrjbHyYLda37XtCbg49DzBtYwX6jt5vBlxGMc61c8CPBEwZcJHl5nBcrOFFpRFqKPi94haVP1V6gHtyT066BftnwL19ICvU37d-or5Gjw-WziTaV3yXX6x-e9rNDIdSqkpKL6NMf5SbA1LkLXEgRuQtEVI6yKFChViet7G7ZcQm10VUlxDdm_Zgm85QquzdlAxrckqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIZ_FQVi6-GWeUAUDstC7ZGQYAzeGlIEq5xoAGcSODIZYfJ6h9SmBIxTa-aD02-nEB8tGn605BG3QQ_F4fnA5X-um2Bd85PQwWZ8whHmYn2O3_cifKq3W0A2zPTjuoeC4URSN4bFRWaOZgh1WVLsZhBHQq_SL2C4-EOp7_bEVyCEP_ksOnuzvtwWovQSRFr7qQTfBL5fNdTCLqfz5H4doOMW7PX7Y3vCHcnc6z2dxx8oFb1IAzOfdt3OEWD5gOJVXJEARZI5T5KqMp49fiq49hFxUJ4gkk8fASuWNpntmM6Fkdu4kjaSjWkXeonpTZj6LZVZ-Dojdx268b3yXFI84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR-8OKbkrDaV-D6Xen1dyyALTtXZqJAGpjcYQB1FkUPGLFMVWwnzD60OxPGAsB4ubEHfWblKJDLR4j9Soz8QzuvDrRdEsjPnGdgmtayL4aFHkBCb-kw_7RPKFZnCpb6POmPd6vzQF5Lx965TOJLRbIyPKI0kKWbryYhDwZimYWfKygXHdSwadS0rrMgr0vckw1sgjt4V6Hn6RecSxcsRH7azd0ZcT1I1xRGae_Tl8D2hpNyEwzMYh54FdvmO5SSJIBohrfOxy5wPgwZXyFyU0HvHsBejIu2sAeC7q9tTeFG1gkv_Z6sMXtGXVd0Dr_9vsCaKFgJp29sTyI2nVC0N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLufnydFpwXvnYoLzdRTj1AfcYMdepvFdnOvknI2_zl5bHrmSB3Lrn9PtGib4rirvpu33nTJXjmHt_XIkTS5G-RIeLMKCzb7PhtQAnQNQVGqS5qJ9G4LSZQJEgA6Ah4Y8uhhnT8p5f-CHVa5qRppeL9GF9ITGWrtalXmQ65u4uN4-L5uhGRfBl9c7GYp_2RK2RoIKItiIX3kFeFKADLVzu6FcGGSBNkypUS7mpTdvgDaZiFFpzayE7HNC8baSDl5cqGRHttB01ZTVheY50DdivEKgjWMlGFI084e6egkOPyFsF2WQOf2t_alNxZ5R7xLSjE80294hiNmIuJiwtf0rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8csV5FDPXYXugrzHqlpLWgGMUZo9ltgcFAJMOAyDYwYhYqJp8mMlg_3lkHiimn8Xfvx6OFkhV2tEffhs5UaivXT0riVSKvZpfqi7D-Zg6a38MxZFJ47OlW2WgUUy2HRAy2YXbXY2LNwJx2SVd-Q4NH6bOSccXiKuF3GPBzNJUcDzUr0xSBZ95hiDz5S4DMP-DwX9YuA_WgGjY6TpGgXhYPnA0wMyhngbgjULUmOqsy3X0JcMfZl-HLgJzJsniSfJ_dE--RZCDjrQioYarwfL4SclxvJImMSd3txa4ApUE4uO_NGFZsDs2XNgcC0JpGgJOwNJ7p8zrLQmrrDNEVINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQUarhIy8nCDl8I5H_dtccuYH54I2S29kMn29UxYsciA0tHv7Ndv9pyQTDZRaThNsb1v_Cg_C2ajYijED6vg1BHYZeNSgSuVLqBKkXhx7TqbgiBzF0oV6w2QFNVGxtdcF-ma1sSZ_zm_lciIhDzFiUmsp6NEnOUfEjxwTvXCyGlbnb4FptmpGNFr8om7raSovpMO4KmxKVbcYsBE5_Kbj8vDqvj5M4p6PWBJZDf9_MzZAvq7BzHq6vIAJiyY8ku-lClYKSQAwFimoiKu8w_4UH_0dPuKCw9E55luev7CWiKa9b14xjcfKEfDpDckyA6VqT1TgSqQL110DNWvE6p75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6tvcdQy0NMSUvFs8SpodjjpCkAPHTuvhU5_gY8-udg4z0qqpduBiZo7_r87lG6y0TthztgOWTQaaxAOoF7MXkb0JhuoLQYshDcjxfS2iB1Qu-ErBWuamQ6uKAD0xGVkIFinktK2E663ZK5t_EwTVdqIgQ4amJKtR15pZutZ-ebP_C5o4wP8Pimobzqjn-RRDhLO6BUGDK6ET07XZsAAuSb9FWtXgA0tbADmnh0mIYj4x9jpbH_8dQQdDICiV1ZayLSLkth1loAYL3O3VVwoXSEme3S61W3AaWtKEg5D7QsGQU3fuJjciQBaxgEAAdy_Nt6vYmu51eAkhsRSoPKYvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWvgBK9ErXbZk9VrPDP8v6vS5wMJoATz2wSxM1RUcKLKDaawwoLD3VeosT9XUKzrfGihJz7OvtGRRJ055pbadbJ8jfqQ6we-lxct8e2LVRe15YvzqtY-x4PZ_ifoDjIdcvF6LMH4kqDzpVpujnvZFBXw2FKUPft54ajmDnpXRg9OqQ9kW24_7D8iv74LuIAkDivx7YB6yWPgbeIUBBqc8fI5mDdy3HG1nAfTAdS68t_L0P9qlk-F1yDcti3U0N4I-_WnshWvN_nCIUwfV_I9x2C-S4REXgYwQKsQqvLyDHDRe2epRVoFiLlpOOGz7mePtoVv6bb-yPkzlLCN_x9obA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbAVjXutCDqoCUwswThiQHIZKZnop-UWxWTNUSdk6-I-AZqHpinGvL-zAaxMrGIN7i_ecVBt6n3c2cRUjkXWhsxdLm9l7BG24CnQQUUiF5GaDEULQWQsU8YUfnMFEJktGyz57uiqzj8xUzO5CZbeKZsBSRQ5P7REOhgERJaW78mVOtbnSIuwGytDPMd4N6ABLBLO1Vhm8mbr_KXHlwRvPf3zGuKK0uCjTWMYMWEpr0dTgKNZ5zCEL9bBxwNeZR-lRknrEOWs7SI9--r1uDtH52LvFy5bv5ecfxMZSfOzrnVHpBBMRx0NyM_j4lXYWYcrqzTBAvAy31LSbouMOqL18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly1XBSeXJtJtiNRjnh0up278snjUlGzgPVozIWU-qRse_0fClFKnShil935ZorzxD9UNVQT3IdlFDV_7Gf2f427xaj5tE5VAJwXdwtJmoq3uosxun97J4b8pb743DhXFnUpM7OaP4zz3nsTXgJP2EBbRXji0tuYgYbw9RmgsWv1dR2dgj9P7dsYB2mg8-WUzlUf9RMZeY3_ZEIwsCe2Nmhh8YjwCRceb-73yUnqiVs8FQAd5CgmXKdQdZp4RRt2LBlAhPZIrbOCwhe5U720GRq0E3KTCfochPdjWtWNP71KTI3rFQsy-Djaohr7o8jOQPJkRsTM3OmvAqF-7C1nVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUMudj-8aYhSE6KTya4ptUqCjXCqdkyyN-nPCWGZPUxX7g-Lyl20f9994d69UWw_4B5NLIInVsV-01LKkvVIxI5TKDWwyJ7LioselLpQ-vJABb98edAMaWDErysVMJu2sMW-fueSRx5GnbLTcAhS13aa8Jr7FnBP9j6WzqQHmIUZrNwbh6_uvP_wJEBR_rWcdAfmc4oiMqZ3xZONzPCjL7NHLUnEfuz5984ZGTBFcHJjHtkRLB8UgRXFqHEdeQnQhtTgXa7GCz6oCY24_6wJsv3dAXu7Tv-Xbd7K5Kxz8JxTeekaDZQKhFBOMTyxX_-YaACmFLrz8FkwLRUPiUCeZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUMrbSgSU9A5lAuqWOqr14z0ZZjyyfjFCvXOgPM0pgWVY3utX7-KijsjHltQ2ejHlxad17omTFS1pLVpm32bWe1WBQX5LUDJzxq_v8_bfBNbKgtKdIA_aRM1VZURYiXnQ4uchgDZPbi8vYEIDXnNaH7hkSdBanCsCTQbkP5GtmON7uHhiphY1eRFLbtx4L2iBCvZA5mgcSTPAMGtAf5WPsy47Pg0XIO3-iKdzbgU81ONjdOVCzHkBLclGcbYiNYiOK8Qjpz_feQ9q4f50lUUdRbVNbNAHU3cJMg7pcajz6irwzvBqGT5GGIeGAdX4ZLde9axzNsloEWsBVANZt0fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=LW2b-7xp5MQ1ugLeV8q_EGmBbXYFueK2G188YPYxZjcac9PbHgtl1KSQWbwRwIVxN0HQXVUM7ozku41HGaRM86TBx0dpxJ6NA2u39nsC47lVNvFydWYbr5aS3xK8HNeTSEoud1FgBrs4XezYtgZ1O1VgoE2hd7h7hV5P4vYaROhI7tDHYYaIfkQCo9PE-T9fkZXN9x4UrCUJf-F6mJ_G_v3RCsN01asms5PJUKCiQ0oVDh7LOyhUdqDkLA-d4xtNiUj2BKkFdzu6pufXEFlk7ltNTPsRgeC9mEAchc4lwUvxnutqHPYzp5NlLGfkMEK3Zo3lTX3_6wYJvpY62brUwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=LW2b-7xp5MQ1ugLeV8q_EGmBbXYFueK2G188YPYxZjcac9PbHgtl1KSQWbwRwIVxN0HQXVUM7ozku41HGaRM86TBx0dpxJ6NA2u39nsC47lVNvFydWYbr5aS3xK8HNeTSEoud1FgBrs4XezYtgZ1O1VgoE2hd7h7hV5P4vYaROhI7tDHYYaIfkQCo9PE-T9fkZXN9x4UrCUJf-F6mJ_G_v3RCsN01asms5PJUKCiQ0oVDh7LOyhUdqDkLA-d4xtNiUj2BKkFdzu6pufXEFlk7ltNTPsRgeC9mEAchc4lwUvxnutqHPYzp5NlLGfkMEK3Zo3lTX3_6wYJvpY62brUwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-TE-P5ZKLAhtoKKRuu8PTK9GdL98lS5WYBxUTZ8AiRvGrpa_n25T_CX9zYI9AZB8n0bUbiFQn4C1QNFulM2vx_NE_pcNm4nJ7He1tmKsxx0EN_sooiihYvZ4LF4Z5TNTAwZDlYU9_9pNPXq8MkN9D97kU13Su2q-35IAhipthyv7LKnzVimuTOPgf55NhrmaINgfE_hoQNojjZzOKlCosnJMPJ87NB6k-E0qn10oGYWF3h0fIOpOWFAUwAC4MwvmhEVjAEKWkgUXBcVxvb0O0OIaU5r8oYWBQ1Mj3SC9e97hWwENR13xrAJAXi3zKBvj3iAB-E_dY1K6vtwaHV_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=EoHiMU3K9iO7Cg7jHK_pNYHhc_cygX_0DB3FGz6oRxtNmZ687OAOqNbJaNi8ynvxR3xssOSt4kSYyVHRosJsyKWdog-i_E3_NVWzehdgWum0oK25BesDfHUZqp79PvsSd179BdzB0BUd-3290pLqGps8cz_D7SzlbjclUJ_EAH82ddP_49dJR3vciWRvkbMb9jRchLoT3U6rQNfwoDZbMgy6U3vsMEjj9itXraxRrG6fBNcyMVCKvW34u1O-TSXdQ_8D56oJjVOleNZWT1tHHl8rTLgWtWGinA6lXzOO8SGoxT2_2ZoYR1d3lKuXtTB6kFRxCvKoyZQ8AcokZaRDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=EoHiMU3K9iO7Cg7jHK_pNYHhc_cygX_0DB3FGz6oRxtNmZ687OAOqNbJaNi8ynvxR3xssOSt4kSYyVHRosJsyKWdog-i_E3_NVWzehdgWum0oK25BesDfHUZqp79PvsSd179BdzB0BUd-3290pLqGps8cz_D7SzlbjclUJ_EAH82ddP_49dJR3vciWRvkbMb9jRchLoT3U6rQNfwoDZbMgy6U3vsMEjj9itXraxRrG6fBNcyMVCKvW34u1O-TSXdQ_8D56oJjVOleNZWT1tHHl8rTLgWtWGinA6lXzOO8SGoxT2_2ZoYR1d3lKuXtTB6kFRxCvKoyZQ8AcokZaRDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=G_aYUdo4JlmkU7mm23R4gtQyt0FfSSC6wWfLP7DjPRAzDH6dQS0FT3ilczFBi2v2oHfnIMc-F_ak6dXEymW8IBwn46r_gQgEA8iyrrO3P-Znloo4kQaRTo_oZm52264RBj6lWPoLU2mdu_ny47lr2CvVyz8e8h56af6NSNIUjfj7-IkAlmtifeuGxvXuM1TmjBX8FpxEU7P4oywLF56x84uqZYQhYmGvNIEoZTf2rE6XuPegN9sFyl8XOPonscdL2wr5U8ZfQfurGV1txFcYX8ixjG5B0eUOHda047YunGpnpdgG1jBn1LBZTFjgomEsRD29kP-2iK4w-NF9jtitxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=G_aYUdo4JlmkU7mm23R4gtQyt0FfSSC6wWfLP7DjPRAzDH6dQS0FT3ilczFBi2v2oHfnIMc-F_ak6dXEymW8IBwn46r_gQgEA8iyrrO3P-Znloo4kQaRTo_oZm52264RBj6lWPoLU2mdu_ny47lr2CvVyz8e8h56af6NSNIUjfj7-IkAlmtifeuGxvXuM1TmjBX8FpxEU7P4oywLF56x84uqZYQhYmGvNIEoZTf2rE6XuPegN9sFyl8XOPonscdL2wr5U8ZfQfurGV1txFcYX8ixjG5B0eUOHda047YunGpnpdgG1jBn1LBZTFjgomEsRD29kP-2iK4w-NF9jtitxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M921MhEzJeug7dL7ghjqQv54kdGJtBbEhiZyZ9OPLRSq6fgt-3JUqXK-1XN9LpUGCiX4buZ2C77J0pqGMkfR9p8XqxE0fOXP6_0ZdhXJGhE1qqTPlOneFWTa3KIuHEdCRQ7aiAfPfks1hTNBVTt3ASeOzSSirP-DuZpDOF6OeZD4m8PMgHfbaDmz0nXeUGUISQPWBR4bs3RkFgSqb9lZEZYqaQa2vYMy1TD6fz4KDam74qgl4nfKTyDmEKonP7wN6XK5CRodkpWfDOgrvCP3Jh8iVQEMk33ryeTtvdHva_RP1jRRkV5l0bTNqGvY4gNO4iRzTxq4Z_5X_L3zF8FDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
