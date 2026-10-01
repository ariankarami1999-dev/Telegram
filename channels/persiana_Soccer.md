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
<img src="https://cdn4.telesco.pe/file/bwaMKbaQ0tl2qFfmCtEE4xRXkzepqC17cHGG7IZcE0Igo-X-PIHVQHuoYlDZBIGLR2iVcUfrcVPouA3H7mFKV6C8jYEFSYKbsxgoqtjzoTo5ASs3lIqMLWJI0wfVmtUhb1bHkYg1nFLrfHi-uDco9vpKaqDyBPYvtMDd0HlxgoT6mcqhcTGEp8-K82RNDgaiDaKy5Ierg0-CestEpn0m7PrJLVW2aIvSwqsKc0lhSalK7YH_ShxkYSdiSK4Q_6wBJPpipnBNw9YIDpZ6LBOVww5qwJt3GEhhrOOH-dteER3b3fgHaNLdOBs9PKMsxA6Pw6ciyDj4cyoQC8xUrMnfRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 427K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9fF1B2HsEGx65UyV0kT-m6hB9IQpx-EsJ0Ncqsc2L78WkSzlNJ-qoFTh64yJpOz6ks6UYkzoT36oZD9uFfn-PL-BMh70MZLAcMFd3OVYzDZz78Mm7O-88DsqTLo-kUhM9ILlaxYmN9-oQFXENAfjCXuRXp2hZ4ZEuj4g57zS-VbZGGBCjSghrFMO6d775WOMgsPBBgZZvMQ4apsLG3wRyd8xYbrBlK3jRkPvzMCdROVVFQLY-qaummTbKAxmuAzQwzakYelAxx-BfoibtoAxFM2RbKg9WnWnchnEoIvxC71e3QgkhG8AfiVnDJDiuDYJlNlK7sZcYThu0-Ua1SXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5QEdCuxOxXlJTsOaBSwNlUZxg_ku7YiCqqsYrxMLhx0kO4d1916elhqXLwTQltAxuvm6MGgLvc2s9CAi84wPfO5PyR7d72iCnHfCVwYQkezQ8vxyeN-_pk28NnpumKGjJGamdMblOMjVM4LmGRRSfUnFoMtaT9fo8jeZWH8c8vz_lvBurIVKvyWgCJ6ITk3HnggbEFKa3DOL05zowrCjB_gbLs6CHs5ESTeKTVPDfci1CWiRco33GD4XyUvJD8bg2puVbyVOWJwUInxOILQVzqLdzknDn3fg_FkQr2EHoSAkBdbGihRH-3FXJCmpwhdeYzMcmHFL49vz_CADKr1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEKDSmWumwp9KnlaJJNwv7Cl0Pj-aea2QKTjGv2drBRv1ac1vca1j4GUWgT1vjsLNCOacsAP4M5_If_X0VSkrun0s39FreU6tOD6On2rl32SkN7eDKz4K8ndQ_6dJirWhrl7g9Zx6jr9wNiHpFkHecnHR_8gN1WbEn_CO3sljhioSa7Rm_XmPpN5gH85eFRNKd5dX37Wp1q60W2La5bn3u4nG0XNYVXRFtqT7YY8liM3Lhgd3qwLu6sk0AmT2ypHljYhcMJHR7G2zjuCjIu8MqONgkzxjaE7WoMviU9wE491_gTi3znulg_0snb7qgB3dzRBPue74z-iRxbGCASkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=bm8U2NPocKl5q0s6zriAQ_b3B6Bq9x_WD597QfBrVDWHspqC1ZEphfUJ5G7OM5g-Di-7MXzu8KwYuL_WN6MO6JhVzOcCW-k4oS36EU3j02Fgl5RAVEaqosxey5U6Bp2ZPxkP8VJp0N2MwBKUpsUG2jGH3JTaV4l2YpKou_J-VVdPABLSJIckBLLQ3qYem8iiG9ITh6ncalqexzC4Oxk0qm-qbeBya82F7p92rH7yPzoXZjjwMnDTJfaIt5FLcrGG9U3NoEmorIWclV0zlzqoQU8-HGjLZhjPUeRiDvGM14iY-MBXmLyRWmR0w0-7ay9D7HHF0EOlj1Sq0T1kAQDTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=bm8U2NPocKl5q0s6zriAQ_b3B6Bq9x_WD597QfBrVDWHspqC1ZEphfUJ5G7OM5g-Di-7MXzu8KwYuL_WN6MO6JhVzOcCW-k4oS36EU3j02Fgl5RAVEaqosxey5U6Bp2ZPxkP8VJp0N2MwBKUpsUG2jGH3JTaV4l2YpKou_J-VVdPABLSJIckBLLQ3qYem8iiG9ITh6ncalqexzC4Oxk0qm-qbeBya82F7p92rH7yPzoXZjjwMnDTJfaIt5FLcrGG9U3NoEmorIWclV0zlzqoQU8-HGjLZhjPUeRiDvGM14iY-MBXmLyRWmR0w0-7ay9D7HHF0EOlj1Sq0T1kAQDTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4e9xgBFj67-Hv5-JB_Nm4qjzPirMlasXCfXfSu45cLN196eSzw9X5zCbGqGQqjpL1KUVC4JO5PGdtWZjmntsnzT4dIVcCYInrf9xmOY6tiWFv6mIeuWlTfMTyIC7XWPTbr84GWN28Mm89ojruIU2i_alydIJmfB_ccPYaCcIOly7LGmg5knVUTARS2cOlBYr1X_elKl7ECu81fNI7g5-dt-oyXktt2kDD_mdvBQCaonWeAhrGALZ0lZOvxwVZRfED2U_ZuxQ1XkXVOFnl4mDn3pcRYjaTwcagDrd_wBTxz9ZVstrgzxmi6UL9MufycB80F557UZtkJG3DEk2okd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiYBz5Vd4-9_FQ2IvoW2sotTvBEtZTQqX_COdqdm5-rMER6CNno7IsmM2mupwKZ8hqR3BuT5b-_eT4X0nfY37C_mwvZGBGcCj2P9ZuE7k0O4k7d4arZQKDHyEilcQefMfzg2Y17EaNNWYM11TKfSivFBE_CSP8AkzYDFg4LpXnk05XELrWMjvKaKTPNPogl7fyF7uVSscdKaU66lFXfdmx6Kca-atva-NbZLRKXUAm1KDUlHfvKZStbi9Ym9gyESuSgP8roRcRTlKgXpKSqseg0lNdocMndTYr4fSY7jDqKd4EH6h6ynAaQRpGrIgbJSIXe7IZIIrN0eSalEfH8Y9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBhCDyLec8ISPlh8FRa3JOOKsU8QyfA0DhF9yqj-EGRVx7M42JNc3WT39qd0RN4eFCa5Rb9pa_ljViyr18uaKNh4m3qTwXzKn3RnWwCPeScLjvdD3crWjWaXwFY_Z__t3YMbC55Gx5pCdqYrsElRjEN1rnP4-mQ9Me9nBxJbMAuWnH_sZ0qLWZYJzc-0mNpr-Yyb2Vz4UNzDwek7pv-XF9TH45dcJopxBbnbm0udPojprZFc0iKe2YcY8LiGjtCwdZhKq7gf7w4JkqvIolwZ_MdJc0AvOWkMe5XpvJQFET4bUI9vwn3E6VtVxrCbFj7CfaJpQw1y8SRQXvVXXdTx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jlv-TAxKOo3ivetRP31kYwqronvaSgB1H65EF5GLG-aF1rm84y1LKH0tYRVWyWkosR2kkdlya7SmO63rOndKWcsMwyeK1fQasU1HgvGm7LtMtuylmyRfar-valm5jlx_5GnDqeA45kVwDA4Bn1mTunwnGi-k4FqFP85BjTSzkflldESB65IdHU6f1ATzhbKOGvxAjlzrAbUr9ms9_5TwNMv1S3KNqDvNvPo2-l6RFMNiMnnnD3Y58L5kPv8HVjScs6V8n_gxiKftG1Rt-QdUxf_atYc8EgRyGWmynkTvpZxxLXTE1Xpg8d8bevMXqeCGikWYZXJLUpDnD-BNMFRKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0x2B-V0sJ9a7AsAiS3hyfkAgIuTG8Sj1ypLTYUeQ4_mdUf2A0Dv5zoKiwIhFeXsago7JeEwk-SX0WXHkvrZwA2tIgOK8U3W-6XDbBGLi2bt8RZZeTNu-oKu6a8v-GfYgQmWdqJX3kaGA5nBuloXVxZXSUIaxJpVUoGZtSy2A_rQ2rIA860ESxcKNf2AhvO5S3KnbJ1nR3PhVpcw_vZ8yn3reAHJqZFvsF3-6dwUr19lwFyJRwWGSQohqRJAv4F_yx-bIYQnBAz56pK5qJ7eQ8P3qbWMpIdmlLFCRl2njhxL2GkO9FN1xCP8eDnBNIC0-EkIOjS4m023SUUZBR8m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0nThgzQeOGNndP8qgPmTAXLobJDXZ56p3S66IEpx4Sp9cGR-6H-5BRvA6U0AJpiym9HkXmm2J0dRyNMSnmDd4-ErDJB65WZRAeAFgMVIxRZMQqfrYaINCVZ-0qR1oozzhS5Kiq6Jbje_UdV4b_pKNEwPT2HqR6X9_gYI7DpvxksSVQyeBVoTkMM9y-du6V59fPOzMXP4xz6WsuiGW3XWa-N6h9kIborZd4yW0-xBhAEurzpoP_Bxl7lHEGYdR4Hz58Pg6f5aHGwp7psiWVLbMSWqO_pcQemwENWd0llowySRnWtMQ6mrjFEpRIwInFTUblutRzkfvRk4KgVr1osIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlXUa4DqZwySCCj9_CdSy2Pe4SHGATE6wHRVzHvezql_l68h5-Frev__7_0wZHq1Ty9BcCHV-SrqfaLIPedDay-pjZozSOg3CEdHaae9l3_IHmlsfpSrglZuz7fnj9bF9AjFTYK6chjhVS-MxjZWnfPsPT7eZSbjk3_S1BanT19uDFsTtmlYQuf2hYljniEqKH7oOscnvCN2pF4Fo65NULcxs4DWsOsQWfiBV1U5aUr-CAMAEuWbUawhOqvYg-pHj4AY1OgoRO_indQDiacw1vg2wTn9ORmX0X4aXaGDf6twNfkoOpOhtdE7_8ommZIz8ldqjb6lESaXiuxucC3dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR4QHnuAc3yZwTz7rXGCFosQkeZq0GLkd-P_BAXggCnKG4_2EDr9S8oR_3bPhTMXlBp0C2s9zm_QSZc-Rt_TgP-NF2Av6-FArcIqf251_Ku_PHgwrs88fzRwggtExDJ26EPlE0xFgYs2aQ1R-YL_KLaKHQiTBPppuWsbFumDfM-bzdbZyQGsTY4xxEj8HWLYxyI3FXlKRXwtBOoLyF4s7rbYpd3_xnoA9LBfXXh3q2EmQ1OfU9bn6TwCSWlZMmyjZRy5cw11hr6sVyXlsfMPT0OzOpgRwVWC7zrsB0j9bZHj4U-P65DZ4veJ1m9SnammwocQBPMftFKStpneIWr04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAPza1lCNWEVqOhYMrPb5ILmSnjkTSi_3BRhlXLdslc_zs1tUOu9JJZjoCd1kdTnL9se4DHiBo1svl5Y_K-XYsmlkiqZCl7M1DzjbSf0E6-aP7FwF9vaPB195u5pV3xfekIutOJsE0c2bqFtdh1FV32JSndZqyZCIv12AZu5wRzc443ZsQiktU4XN-5X2uyWfA_Z74tGRrceNrGzJHSO-OsQ8UC8mbnpCe-Ni7HaYJXd13qKYVQfJ0ZNEt1WFzQP7CNRkmsOrLSDgaxItNn_7VsqGcWtg8pJzeCjQ5bk9xj2SlSi1Blzb57bRAUAn_TE2H3sgi5-V-hTxC9PbZuYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k56JjoZoNyyZpZn11-WJ4hOEivZqZ18HfIUSmAqX-Zl-OzgXXdr6mZBtcM-WexaFCAO8xnesspiM4egWZ4SC0Pk9vQvMkUNrFnVKtbEPFnUQgdA1_IsFkSwbNONC_imWRKsRx0VGPtnlep6GYmuHpQa5tixyPmNURnfgH6xOj9nTePMsdTi1zARMMJQSRBzHH4aGEqw_XHhN3MvyUE1m5ZLT40FOqt-2BrUH_WQxTLOCwDBuZUf4HrKGb3rTkNt_5hYh24bpUX3NTUW0Mm8I5QRNsQrCWyyG3Irle7hxIoIfE1rCRmoc8PSi5oC4tLZFSAZZ3E2vfauZMcHebQo1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEEPNpkK-Zrx6Vk9sncDSJWQ2Dfzwy3g6ZcTUr86g2I7tUWR4OZ7rFuBb1Tgh-J9nVQJjfGKL-pqcaoX2NLDwH2GAGqGcPgUsCJ75D4i8IHenlhuXKb2qQx_SpWnZ_s65PdTRSYhlTYzdL1TIVJkV4czoDB3GiBCYf1wb48cmzjKpiEPvQwTXUftvACGab--S8lOOf55weRKkhW0ZOADXwJ9eZS1FyNuILLHDgVqK4J6qJ-Dc87TBB7t-Po7GHJaRU8e4PBYuEstCkjbi3Wr8T_3chHW_zeuOPkWVEL4hDHgsnGfjMv61ncjam6yif54taExcFDvaRIiLvQC5wKEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30801">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇵🇹
🇵🇹
نایب رئیس فدراسیون پرتغال اعلام کرد که کریس رونالدو دیگر به تیم ملی باز نخواهد گشت‌. رونالدو بعد از جام جهانی میخواست از دنیای بازی‌های ملی خدافظی کنه اما فدراسیون بخاطر قرارداد تپل‌های اسپانسرها از او خواست که تا رقابت‌های یورو 2028 در تیم ملی بمونه.…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30801" target="_blank">📅 17:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30800">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQicb6ZtKhYnDcPR5pv2ibq62WzUox6fwJdsI9v0GJvCGbg0f13jJbXaodOgvDaEjTZLN2gPgdYc3pAWs0UKO5Cl5BTqiNyK2nRRqMOX7-P-nlFPi4TvS5JaPOcpvLMzLaNr5CO0VPb7IAL4yNdl4N10rYYFrTxguuqeUIktnnZYx0UFoBwxxY0yZKRzQfMer2lRhlmhFSE4Wrq0HwBw1bBKDxEPQoq-DQa9Y5IXJY65K0MYvZv-T--Qs-SDFXPgjJ81W8DD7zTWiUPPMb9yQzY4h6yJk3oOrrlwkhTFWOAptzBWSWMPQuWlcJ3NqDjD99wEmJF5En-wDJos5SekoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی بعد از آهنگ خوندن برای کودکان میناب و مصاحبه‌زنش‌بامجید واشقانی رسما به ایران برگشت. جالبه چندروزپیش که خبرش رو کار کردیم تکذیب کرد گفت برنامه‌ای برای بازگشت ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30800" target="_blank">📅 17:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30799">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WunEvIBemd181lipVlNgwcJJHJzTzsnprUxgDuTfA5knC_7ghOqgqHu2Hh3NWJkAQJlvKHjFpSmLkTtWiZUCltoR3QU6FZXMX1jhD1uaUPXogQ7KpUhIij2VPCbXZZ81ErKqik481p1Y7lZ-nRX5IN5qLFfXkjuD1x2NaQ-j3mcek8ZEoPeNQlE3KaujD8GIbBI6OStpsck6A0pJwr1eVU7rsYCBg0g9qDDMqJh264SLMuuJE3Z9F6hssvbxBUJnjfBjChVGMxNehHKKvVrqIpbO1XcwPf2VpblwXdcxKZZxHkS4x_wBBdVTymoDsYIb817E3bZU9OVvhlKZIZdtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/30799" target="_blank">📅 17:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsSBZWckAQoy4bxlAjTuSkQO26U2Iypni2SwK2VaXA1KDTCc76_RBPFUz98JZjLt0LudpiM-fS43ov78Twuqnfmv22f5YKqQ-0ufhm5LpjneWymwhqGk5l8WKR6zP4S42CWrX4BTnex9D-3zWiB8XEVlRqxnHjuH1uYcJvZKtCSU_2UyoJGkO_1hYyfLon29JxtlapjZUTDHsuhQT50FVruQcUIfiGWWy9wF1qdLFwTq19vfbSnwQdBXB6iJ1ey-Htop6SlDqlHqhAmd4bQbhpUYyoRmlJni4tDiTgqer-HJcCE1fLtNMyHfwct-8GVO90WQzb9aP4qQbgzYDpDqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=Ic3JjANhBRxaZH80q_jlISG1CponJAHn7NPKDKKMjHAX0lhMLwR_m-EpiwBLnp9OIG-v-UVBh5bm4uDnRX_AYVHbYJ3p0miP4mDLzIa8t1T3swec_r9aYWCtneaA_7B8gUTD5wHAUSCFjqFPBKSsiUmlxdgztcsCz2qBQ74twC4bGzCy3C3VoGxVEPWQ09WkDKGsiWbm9pg9HfjphSrBWr1R0eV1RL7oupi3ehq1vL1MFzRMEKFAB6JBjLv0WMIC9ZfgDquCqWYIKICTimiZskYM0xq-fpTK8UNXQZNrM9jvuenDx4X3fwAk1kClmMrMt8EZ6x9yLxyJd-DSh96fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=Ic3JjANhBRxaZH80q_jlISG1CponJAHn7NPKDKKMjHAX0lhMLwR_m-EpiwBLnp9OIG-v-UVBh5bm4uDnRX_AYVHbYJ3p0miP4mDLzIa8t1T3swec_r9aYWCtneaA_7B8gUTD5wHAUSCFjqFPBKSsiUmlxdgztcsCz2qBQ74twC4bGzCy3C3VoGxVEPWQ09WkDKGsiWbm9pg9HfjphSrBWr1R0eV1RL7oupi3ehq1vL1MFzRMEKFAB6JBjLv0WMIC9ZfgDquCqWYIKICTimiZskYM0xq-fpTK8UNXQZNrM9jvuenDx4X3fwAk1kClmMrMt8EZ6x9yLxyJd-DSh96fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPF-EGoFLvTtWIha83UapQZudJRhQp-yIu9tsZZXgoQYF15s9jA8dD_6bwK0QsHUj-5PDI1oWQi2_CrrFS2uINbyV5emyKYLDMBhgLBh8wAe1UaF0L9GW3gWp17ye5hDd5N33oTGWj-67qOOhDVe7cp3O-voEbSou2gx4GnaXpTJy1amVGr9_Bh8mg8YhoJSG3gfEnI6GnewmIYGYtNjSFDExFGl3sPO-O8LNE2gkC2KEUykGe07ceS5xTm5uZdDs-xggtYtPsp2MiJvJW8wBdZASNjNgbySHtZugjiaJ-XXqaoTazvy_9W_YTZl0GKSvEsXZjdXULIbgohSr6RWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sss7PkOj1qfNoXMoyEAv4SXXRBi89Tv0F8oftpb07ED1ZKFIo_V_fp5HygyT6huicOyH_Rh2JUr3GUsu5kUCbb8QPgmZAPKo-LhX30E7Qjhr2z5342SpgfD6umPKzA9Du-k3cLtYsxVp9_lnZ5hO1OPDvI8AlPTD6ca7sP_TCN2-lAF49XwoLBFf76drYHwpYmtTS2lkEZ2bMZ-WH0-qENmauTfEQiF2RegtAaEk6TYyR4vpqmGWoSB_TcezQcOlPkTKIXFefQaH56UG3UeJyU6S4_5cSprJJtBQjxEXD8VcK7uN2MKpDC6QTvyMYbSJqzxeEeYRvnQtLsZhk3AJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUz-10UgH5KO7qlmmWlslmHB6bYyClI4VWaC1Gl9hOAvfI0S67szrAHnZYHHvO4hoejE9ZnybF8H8dFD89EgclWa5yG2BWhzVZTi9IAnHWwtKT5lO9xWPzd3TO-YU7QWDbqsfVfaR0AQWaQBZ5e4V13mRaQgftv35ban404YAwCZzcU770xSzWMzTuvCErZU5WsplIfXJ8f2rySnOhZVXL60cH61EnY3lX51Cw4xXEKLEFuXeGus4BsQZ66pXHxx_XST_zV24cLIg6RBbhoIUIk0OmiF5T_viT7-bdw80IZ6q1Q3msghCOoC-__3Jd8W60kxkDbo57NUoI-vy1_tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=lXBFG6ihujt69Qwv7ZCKVShdJ2nvHbduui6gvLRrLh6xFYu0zKsiLvfktd_9H60JFyJUsLqHKuAfpMz4-D1BA7snwv_kPeHyLACxFfkqkZOPRMZ1q20EoFzVNSGkcB4VUI2QBmPEZksVLA8g6QBUHuOXzfeO-msVWzLz8nAY-tO0sa2bMY4UD6qOR6r_WM9Q8zL8vUFeRamDqpsoMMU8wBopPop__9rExSu2iz9GUCECq63ruF2H-Tl9sNaM-k_iMpBkfdTT5GRkDP_sMA6oLMVj6-jC277As0p50347YyHgsBl9kYVNQ1ZuZDbHxlbD6w7sojtbX8Mn7rOJitvn5TMjcKIcXkoFeyczaX8d4AE31JQtz2Tp9-f9wXQQIFqqFJ0FAaM0DdII2RxmYrWzyhResoYRRa4fN0rVYB6_B3GxGQy9P4C6K9osm3zpRP6LHY7enrD7cWfmg19Q2efV98EkJu68gmvx4cCn3l3X7I9aQp_tDiAgEOLQURHck4gBUto0mVvPxcMw0p7qNMtzb-SUnsDsIAzk74kA47gsoeOOxPIdvtxJDHqgFfqm86gTXmIsBG3GmqNvpkPQbj211qfPVaXK91S90Eh1yZZXckvCj0FsAgznaO6NpTZaPOBHWmxNdWKNQv7HMDki9m02fOJ1QQfn8l_7SjcWiDNDHp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=lXBFG6ihujt69Qwv7ZCKVShdJ2nvHbduui6gvLRrLh6xFYu0zKsiLvfktd_9H60JFyJUsLqHKuAfpMz4-D1BA7snwv_kPeHyLACxFfkqkZOPRMZ1q20EoFzVNSGkcB4VUI2QBmPEZksVLA8g6QBUHuOXzfeO-msVWzLz8nAY-tO0sa2bMY4UD6qOR6r_WM9Q8zL8vUFeRamDqpsoMMU8wBopPop__9rExSu2iz9GUCECq63ruF2H-Tl9sNaM-k_iMpBkfdTT5GRkDP_sMA6oLMVj6-jC277As0p50347YyHgsBl9kYVNQ1ZuZDbHxlbD6w7sojtbX8Mn7rOJitvn5TMjcKIcXkoFeyczaX8d4AE31JQtz2Tp9-f9wXQQIFqqFJ0FAaM0DdII2RxmYrWzyhResoYRRa4fN0rVYB6_B3GxGQy9P4C6K9osm3zpRP6LHY7enrD7cWfmg19Q2efV98EkJu68gmvx4cCn3l3X7I9aQp_tDiAgEOLQURHck4gBUto0mVvPxcMw0p7qNMtzb-SUnsDsIAzk74kA47gsoeOOxPIdvtxJDHqgFfqm86gTXmIsBG3GmqNvpkPQbj211qfPVaXK91S90Eh1yZZXckvCj0FsAgznaO6NpTZaPOBHWmxNdWKNQv7HMDki9m02fOJ1QQfn8l_7SjcWiDNDHp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH3gDiHxm8PnxNGwts_IukvJh-TC7BZ0ZNYFiGkGvzXneInKKfuh3BGpXn5-ee6yfuVlTOeBVNgcBbJuNIGry04nWN91zWHRy9dLx3fMXQmC_fFU_j1ijfr3WQXB0WV_nMZNVA6s_6NySkSTtaGQCKdlf0MCjJ1hAKaXMX8LN-AM_YA3wuubEvvLgH4-t2x20rfEAZB-9CoRob4fJwNsV8jYuFe7OiO0voF3aJkQGfbeLUmlTj12dVw4zjhHzf3KSMqJsZg2JAl_aY7ZZYwfBnAxya7_onRJONPyM3uPaOWEIoBeu2rrZM5FBdKHxWpSP2l7cqYpMkVUP1V7zxpJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKOlyOksXnznVd5XXbTVRr9v_v7JYHEYAVEU1WvUWo6rRTTwzeof2SdGVufwUs1U-JCXY_sRNVTIEsCckrZbbOHuya04_jnKOi1u1x0DruyQQnN2uk8d2-YOwZnt0c3YJJv6VCFv6Y7dn8qRJcLgFVQ-Bh5HpmMYGVRcP1hFzyc8MeKmTVV7-2-umluw9g2XBVdCHrDQPmiaoiocD4hkhMUKUxdf68RFgqoKb-i0lSmAQd_zXbAA8_U4vvVjz5FmrzfjHP4YPpJ4lPPn9Qu7X9vRjmXdSSnM8qbktVyzRBCVWIbW-fn5eU6A9Y1-HS2bZF2tOOyeYFDxzA9am3GpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_JTN9UoyXGWm7Zp_GVg-q5LKz2dv-PeusHqsZQb68ll0SxNK7XhLPqubALeZUinsDArRpwRFRdJlFyQbzk3qN8IIWWyLC7jk6Q3-QRyjzRgBJyNvA-P0VmQWU-GYPae20-ihtZgytDjNbKqB-6W5EazzR_gsz_MyC1YgS2q_IcX1aFJ9NWmCToynI_tK80QluKIeOzAZo1rKlnHSrccoiv_BRiMvSBREWuPM3r9SVVkIDmN9kAR595CILg-ZICxDDK9W7KDM45gfo9r1s6Rjtos0qgTwS_6HJjf7mDKYWXbIYyQMdTCedCssfXHBFSEJBxBRGK8dBn5Llqpuz-Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFCpDS2avMvcxOmKPLEm-aHEC28ztrZDKb5lhYDW6GT3CH_oNOWno3o6N65vHrOoDUU6T544_MuPr9nB1UbaembuDyGJt7K6E_eQAJiI4XAQY5mj5UgVutZz27Izag3aCFo724L694R1TOlG05Vi1onJL_nT_x-UhFYyQrDeg_9mnv3mwSlR0qoaCyXP8JmO9hrwlcKn9REiswcMR0glYO99xDZo91KYzbrkxejpgvGmI2uqrFR6U_94CU4rmC2toBJJ3QdEwGtgMgMNKWezzytrZ5MUp61Z-iBx-Dyg3FxIWi6F9gh-Kbol60sc-Tko0u5p8MOOtP81WxL0uzSt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAgNKKx7G-fAYUIINrZVJRvcZa2lzI_vcxCZ9Bf71jNuhLxxyAzb9sik2_zSmmWZB-2zrT-p3ZTOGhSwpc6FVU1EpCQavnF82MmW59ncl0Qf8PU4cRCXAcKGTZp14W8ITyLQADaR9h-Gyz9YuKYdwBmtT5_IKTjn0PRb8LOVRFReeayUcaJW6eAjqV9n2zuQbqZVbXTpNYFXecx3W6G8d8D-tRPh4MyjLZcImnBrssne9dC7d55pOSTN7beMbwaGW50dAbHRpJ-2gJW-_814xSPdLQeU7pVPD7HMoKRA5OYDo_nQP4-YKBIXC_JgdAgEcOelnVpMipnETXHjtoAkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30788" target="_blank">📅 13:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXTXG2Tpld3lCleVKeWuzlyW28lye7D-o3QMVV2Hw5ke6YdU4YozXnyBtHqLXtord_IGE4VRTNaq16g9Wa61cqLrVs_i1Uj05d9MqEyKJyMySD8bvz4Uy012FWnKeLghQzC115Zr3SQ42xuhaPRS8CaHuo15-OHAuXWiFnUdl4ogHsvDk1iV1AlJnTSlb9ncUWscit7mEvmjJqyh5jHwSQYJ--u_xV7llIHNQw1FHn45DD9EyhYn88Zrs6MXQy367uBQfWWa5dcBZLjmwaQ09YFF3L9bBzVlqU-Rqb6On0m9_Ca9YeOLPxvxjpPRkGbkaJtOF-f4ONaEE90A1rYNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30787" target="_blank">📅 13:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcI3lDpCgPtDe1nz8nxygtob7KHyG_4FT7iOb007541Pxucpn0Pg_2IZKw31mPddA_MEsh1wdWjTbsEvQDSSEZ7xWlLbvSqmpz14um5eU1vVrl3_AMi99Y4p78VMp20s4251NHm7DVLFXCPchtP1MQg8nO6ulEXZk3q4n7zZJCRaeRzq51OS1ksITmaZcLgxROm7n1FE1GcNNPbl36liAZMEH0oJOfo8x9sgmpG0OoljljXQDdf69A1vXBYpmtHBof2IRJhmvLGr36YkxyUMAJkWpyCTvVpUic3yP7rRLri50I7s8w6WydromyMQRcKus08RZyYkuEwJ2uuwn6USgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30786" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5VDFBB9sdOxJA1GEsRpyFe4FHnUNMVl8favZcSMfI7FZmAfQpelsl_VSPrxMuzk0yBTdxBL_ckhdSVa46QV_tFwhwV_ogpvo7SHu_wcUgOCpTk-SNVpUgb7f0K3vLAO0iRu8yK1m41G7FV7aW1kt3pVkxXLsPndZr0gUYnh5xyK7ncPbxI3mceeifbyQ__yKXxY9Z6TU9IYiV0DkIeRpbIQZByXtgwdGmtUgTm-C26KPR4MfInPETqWxMwgQHfGWJ9oWdlE_EWbMfqU2bPFna3T6mPIOFdNh9qibapLaw5KP_wz-ROhpW7MwfhiGA7ON2PWQeqe71TshJfzzde6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛ طبق پیگیری‌ های پرشیانا؛ مهاجم‌جوانی که مدنظر کادرفنی باشگاه پرسپولیس قرارگرفته رضا غندی‌پور مهاجم 20 ساله شباب الاهلی است. تارتار قصد داره که در نیم فصل غندی پور را جایگزین ایگور سرگیف 33 ساله کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30785" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30784">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=BVuiG9u2_ZeZTm-KVMikLKx7UMtI_O6g0qcMZL_W15PxtB9fsQstqnIqtwt4TYzFYMKEGlAWBkIC28s1MD2C5ocPxn0UewhuqJQjGWWBSQdYSY9oLevFE-mIpE0UUrAmkB5KATKN2k1V6W9mMS-PEu0UfOkmHLzjzcldNAjsjRH-v0jPYuNEMcz3tHu9E51Q3Z7Qa1Woyfjvio7grHtbi7GqRWMhT9D0fH5bca7lJrf-QaOkGBdMvJlI5tPYBCseVkNQi5sFnDNjBDFXMNU_pqwTrm02pTMsGdJjI4CqJ2hgMzBxhh9jj8STJ1hVLl8ZeOJNmQmi8baWxWTJsdWaZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=BVuiG9u2_ZeZTm-KVMikLKx7UMtI_O6g0qcMZL_W15PxtB9fsQstqnIqtwt4TYzFYMKEGlAWBkIC28s1MD2C5ocPxn0UewhuqJQjGWWBSQdYSY9oLevFE-mIpE0UUrAmkB5KATKN2k1V6W9mMS-PEu0UfOkmHLzjzcldNAjsjRH-v0jPYuNEMcz3tHu9E51Q3Z7Qa1Woyfjvio7grHtbi7GqRWMhT9D0fH5bca7lJrf-QaOkGBdMvJlI5tPYBCseVkNQi5sFnDNjBDFXMNU_pqwTrm02pTMsGdJjI4CqJ2hgMzBxhh9jj8STJ1hVLl8ZeOJNmQmi8baWxWTJsdWaZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهره‌کسی‌که تو شش‌ماه‌اخیر فقط گامبیا رو برده که باچهارده‌بازیکن رفته‌بودن با ایران دیداری دوستانه داشته باشن و الان میگه بهم فرصت بدین بهترین تیم رو راهی جام ملت‌های آسیا 2027 خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30784" target="_blank">📅 12:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=RNaYTUBRNhD2FX-_s7zE10AkbZt1tLric82A-POgB9SBjQ891ZIXGnG6opufm_D0NgjzS8Cj75IXu6dkzBZHRxai3rHg6BnlOXUaHo8SB4hoP2d0aNfbHdS9iFY8c13ThKFM3UFi1Slm9pJXfacZTW844Lv6dqh6YrgXXkhd8RFIIS4EWTZlbcFCZjfWsU1iaSAv85mgirJD6mfjpY9Dv-Oa3aG9IjlvNx152eCGWtZ5WLT2M_08rarFt-B9b2wMABM82l6eW64tBU8-w2wTT8wvj707_9R8dtDGYLGR9NInRuJ0v4bg9fTZ9tvqTSnw3ypJeXNsckTBIpXI9NC_lXlXHeExxwhy0RWgKfHylf_qwSjt-r2r-2xdyzPMEiQS1CCLOsH6pJpv_t0kLK_b4xl9wYNZcUEQg4vkZ5C6X0zgovswJFYkxnTAWonL1s5EMOimhnFIhi6x22Whr9_2-MUYRs0JwgPG1t8W4h7kZWMWimvOMTqibkTEDkLlsJZP0CsVTT-8diOH-BG9GjsaZIMyn6OonFcLPbzqC9EVO0rJZxezuXVGc7VNQNWV5elg1O7L29cUSSSfby52jB5voh_-ZN8Yx5KjcQe4sHM3FDGHtdwlpO9pbO8aWpszPMYjF7xc55PGD-b7mph8epnTv93rkLt0LDs1LFWwpH_yYyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=RNaYTUBRNhD2FX-_s7zE10AkbZt1tLric82A-POgB9SBjQ891ZIXGnG6opufm_D0NgjzS8Cj75IXu6dkzBZHRxai3rHg6BnlOXUaHo8SB4hoP2d0aNfbHdS9iFY8c13ThKFM3UFi1Slm9pJXfacZTW844Lv6dqh6YrgXXkhd8RFIIS4EWTZlbcFCZjfWsU1iaSAv85mgirJD6mfjpY9Dv-Oa3aG9IjlvNx152eCGWtZ5WLT2M_08rarFt-B9b2wMABM82l6eW64tBU8-w2wTT8wvj707_9R8dtDGYLGR9NInRuJ0v4bg9fTZ9tvqTSnw3ypJeXNsckTBIpXI9NC_lXlXHeExxwhy0RWgKfHylf_qwSjt-r2r-2xdyzPMEiQS1CCLOsH6pJpv_t0kLK_b4xl9wYNZcUEQg4vkZ5C6X0zgovswJFYkxnTAWonL1s5EMOimhnFIhi6x22Whr9_2-MUYRs0JwgPG1t8W4h7kZWMWimvOMTqibkTEDkLlsJZP0CsVTT-8diOH-BG9GjsaZIMyn6OonFcLPbzqC9EVO0rJZxezuXVGc7VNQNWV5elg1O7L29cUSSSfby52jB5voh_-ZN8Yx5KjcQe4sHM3FDGHtdwlpO9pbO8aWpszPMYjF7xc55PGD-b7mph8epnTv93rkLt0LDs1LFWwpH_yYyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی‌ازسوپرگل‌های قیچی‌برگردون فوق ستاره های فوتبال در مستطیل سبز؛ کدومش خفن تر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30783" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏅
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت زنده‌یاد هادی‌نوروزی اسطوره سرخپوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30782" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1IyiFIZlrv4tRH4oW670-osSpp2ogBzkhBl2itpI8kW3tDOudc-n3UPjuBuu-H7SVARa4J3Pvd3HanjtUXxhxpU0P2mweXpv_vvw2t13dtXpH4EsnHIxCJSCC4B6RGm6rTd74pPGdXBu69wJLwiDJUg_6by-FbT1jEkUNMijku4auPAaflFpCvf7HVxAI2tcXevTzB0QVJ22QhZpNT0HZHte1BqJnIMj5XMJliDHczEXcr_E4e4Wu1QSt6qOa73OC9mQuTFf5_SNilZDc_hqYKqQa0Etqq1cS3yBhEG-QEmqNVA7pSjAockE-8GnpkcgtayF8L8xQa5l7-mMgd_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30781" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQzVLU54o-2LN24xWz7iOdOF8GVYBguIbc1ac8wRQOGTsuqmDvb8LZLkD5_Eh5CLZycxDwWrUuf2NadVa45OKAqZCYGm3vpKX6ajNABsNatMjDU221Iyz83t9YUBzRajhUQ7xZWFvNS2e9nZWwAJfT9QZWjFKdUefyYmxPp2BdBmVUn3ty0Scsco6h8js_FmUwiEZDqILVRkgurRyWKXtDLco6dY0U6_ki4GsdoJcFbEt9CdsQHkFVQ6tdgwUb6fDF_kMAWD4m7Cg03lnj-nfZHY-jWDAXbMmaMoDTO9fB6WiOi2j68p-Gm3aCIyqmjMZwM4b0VW7tvQJX4T_UAvZKXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQzVLU54o-2LN24xWz7iOdOF8GVYBguIbc1ac8wRQOGTsuqmDvb8LZLkD5_Eh5CLZycxDwWrUuf2NadVa45OKAqZCYGm3vpKX6ajNABsNatMjDU221Iyz83t9YUBzRajhUQ7xZWFvNS2e9nZWwAJfT9QZWjFKdUefyYmxPp2BdBmVUn3ty0Scsco6h8js_FmUwiEZDqILVRkgurRyWKXtDLco6dY0U6_ki4GsdoJcFbEt9CdsQHkFVQ6tdgwUb6fDF_kMAWD4m7Cg03lnj-nfZHY-jWDAXbMmaMoDTO9fB6WiOi2j68p-Gm3aCIyqmjMZwM4b0VW7tvQJX4T_UAvZKXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی تیم ملی پرتغال: در تیم ملی اونیکه حرف آخر رو میزنه و رئیسه من هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30780" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQB_c-ZxxgwRBCIbQUgwDmdAUkRJn8Q1NJ5YK-GUl4J-OyKSoH8Blxxc5DCvZIVkU6Aa356FaH7kT6zOvX12cbpU3CickG0GYAj7OFxRcOXu97mZ4vMhZUlpEaKkN4wodLagC1gNjJokLRYKpGFCzy-t1MzbQIAv6QmnmuIBqsZt99y6TWpJTrhAk7vvA66YTVtyPEI8tw8I1bBoeb6JjLkrwD5YrCKS9PfctjCIXISdkqv_KwoN7v_6wo6gRcru59HkhpTtag5OkmIZI4wuWJVNAMHc3USAuFeeOdu6Hwtun0fJRe1Xk9ZkYXLHNHbmv7gifk0XJk4U3giicq5xkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت‌شده و پلیسFBIبرای‌دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30779" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdLw2JYtdm6b42ycuydhjBrJEVtgVIWEFsYhGvEHv-oXealPGYIyWRsuepTYKTIVvHHZHkFJVdaQoG4KXk1ox-T3Qe95WmwdkypN7FXmb8GSqnxLv1rXCYCZMqZOHRWNdi8e4-VJeNm11EdMZ2bfIlM2Na13EVQYQFShn0-KOic1XnKpBaN16qBDTo5PLmrz7Jh2J9FyMRDnJMqWeZY-XQ8et9CRi0e7D0U6A9EEH3KMT5j5ZX8zxu6_y3B2UPKc1XCET5A5kNvDv8tuWnopCaHwY-i9C_YKZ-UGt82A1iL51KifItQyXg7fwLpPoeaRDe_laNRrjYFczCUFZvLsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=I_OytEuZy5pmnccSf3L0q6xquXoDNexdRwJ_LUA3bwhWai3qTDXgk7B2JzYVg9Cu2CQFEDSX4U6r-RQw6G1Y9mY65CRLMY9o5nOHP62YsE-6Z1RplaZJcfWp2P4oQY8LGtpUdJwKRxNK9m3yDI4GtMbg6r62THq-WwCilKGn-TPhCEaMdr_VFqKDYTnboArsCFJtfo9iCpmOZNlzPdHn5MIEpGaHo7J5qQ8tOlUW_wDR4YcV0yNOJpCb0_mkx5XCq7qpRXiJl0iWPum7d_FiNdxsAr7n56QVFsk6zEOqv15WcrHQMfoFDVTBlzD7xsKsN1dUXvNqZ7ej9a5AhAt9r5NNUnjRXXZ9hFllk94ZXIh1f4jwyc-q5Dg-7NiwidyI1tFV5fS0cVcUSGuPasFlgldpVqmCFzz4DjwV72NmSkkkaJVKkbES7d7pqWx5q01WOW2lksRCMNEE0Xnux1aICuEKfO5G-qGxIqH_gQJA1VSo-8HurvTeI3tcMGNJY9kGyh-FLmc2fu97-Nw0R-H4Myu5cDYWiMsPXNV6Sb76P-2LLWYxZG6HI3SbmBNhcCAiMgCXHOwVrOP7KIiNRewl2p9Oi7GR4-2KLeVQVonzPdEyNyYpR3Wlwx6s5D5DGDLrMzspQ0EhyB8iDIiQleCbgiodElWkIndIgGJrHhfH4EM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=I_OytEuZy5pmnccSf3L0q6xquXoDNexdRwJ_LUA3bwhWai3qTDXgk7B2JzYVg9Cu2CQFEDSX4U6r-RQw6G1Y9mY65CRLMY9o5nOHP62YsE-6Z1RplaZJcfWp2P4oQY8LGtpUdJwKRxNK9m3yDI4GtMbg6r62THq-WwCilKGn-TPhCEaMdr_VFqKDYTnboArsCFJtfo9iCpmOZNlzPdHn5MIEpGaHo7J5qQ8tOlUW_wDR4YcV0yNOJpCb0_mkx5XCq7qpRXiJl0iWPum7d_FiNdxsAr7n56QVFsk6zEOqv15WcrHQMfoFDVTBlzD7xsKsN1dUXvNqZ7ej9a5AhAt9r5NNUnjRXXZ9hFllk94ZXIh1f4jwyc-q5Dg-7NiwidyI1tFV5fS0cVcUSGuPasFlgldpVqmCFzz4DjwV72NmSkkkaJVKkbES7d7pqWx5q01WOW2lksRCMNEE0Xnux1aICuEKfO5G-qGxIqH_gQJA1VSo-8HurvTeI3tcMGNJY9kGyh-FLmc2fu97-Nw0R-H4Myu5cDYWiMsPXNV6Sb76P-2LLWYxZG6HI3SbmBNhcCAiMgCXHOwVrOP7KIiNRewl2p9Oi7GR4-2KLeVQVonzPdEyNyYpR3Wlwx6s5D5DGDLrMzspQ0EhyB8iDIiQleCbgiodElWkIndIgGJrHhfH4EM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌مناسبت خداحافظی غریبانه کریس رونالدو از تیم‌ملی‌پرتغال؛ یادی کنیم از این هتریک تماشایی و خیره کننده او در یکی از بازی‌های تیم ملی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30777" target="_blank">📅 09:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozx-0Onqt3fLk_XCiW8FWIIAbvJgXjDhBGOGpX_XmFKN_pQn7XAQhVmujgA-20ADJZbcjiFEU56WxUm8AitP2F2Du2DMlWJ6c_wwbDI67Vea_CFSZ5X1nFBIJ3RYwlQJCV2ktw4E9wzHH8eXQrvdxI7-sjWVzDsYByl006sBb9zNdDJGf13ORY-GTKVIIsYEnEb_lNtFPTtdhoO6FhvbiLn8sAsbcnX2Sc1ZVyn1s5h2VHB3GNpPRPGBCBthaFepFKH8a6t8jR3je_IK8-VMQK1ZYBdQml_ss2OP5H8kgNpoAMkRLRg43xEQSZIJukuUcV90s6AcFzDVmkTjwAgaww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30776" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-janbXR8lDz8jnJoDpR59TCV2T-Oh0z-hls2wc2aDm7ngEmSs8leCBu3ZGGDTUWXIyElbxYgC_tJu62kjNVb1YxtkKm5lGoqz3jxwQXrHL52u7PjA35KbgkiqWD6JpwuG_N2NxPcWJrfFARpnWPNVVPasxyOArrOe4v7rr1rbqu8Cq4zesT8yQhfut_uz1G3t-41JQWOoQd_DBdBjefjjNyX8ZtmtdxengrtVKd0pZC5r-lEIk6iHynN-_1DVvH65R36B-z9z6JKOahiAvuYKFeHqdH6KNuymsRQVm9-FtxdkoBbG0ORxct4jnDOZ_ubor7X-kUDe2lVv8lbWk9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30775" target="_blank">📅 01:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbbdoZrX2YmJ8bZRRc2jZHm21kGRCG8fW-WrlBufRHQMhIf5cMM2ETq4dFOv77kp7wCFDLXke_0SzXW8g5jSdQsaIdrtow1tdmk09TUDU6RotbiZUTW9Ll7u1eR-gOXSROYJ5zVbiI_khHZqH0fb5_tK7LNSDn7tR0Jb2wh0TLuBr1ubyT2V9_5Ae5z5eAeIx8gf27NDwwg4dw60-Z2YaPQWtsvYrVDwc7dtMeHHP35xpB2fp-4EmIYDHNP6TKk2uMs7opiJNOzf6MMZqNra4S05TjA0sfl6Lv8ivu-TQoMCx83YDaWcWUHPEozKZJv60kWWZ6sfMMJfllkkMMSVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از این به بعد جای این دو اسطوره تاریخ در تمام فیفادی‌ها خالی خواهد بود و بعد از سال‌‌ها دیگه قرار نیست آن‌هارو در مسابقات ملی ببینیم.
🇵🇹
💔
🤩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30773" target="_blank">📅 01:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnI6-SEWIEaeQ6VZJ3f0ODXnMf7m_bif8uT4WXI4IHStA5zSP3Vo8dAllG8rFMCfixjAaUoSnipnVBP9bZojD679wQc2kBXRxJ37Da2rHnvJqIZ_c5QcgWPw0rjAvm-9DKblkRL7HdmzPXWuCcH_IjihABmSOPJilsPtdHS5Kr-cC54kl9PQO3lMTiWoXIkaoUkJQ4pTejtVOywuzBHEyXMM3G5XrhRaOnCM3Bw5cHOeq8Lt_QFdLlAhzhmVLOQ4bWl8IvKisflNdQY-N9nJAMS9eKA74ZBoAabkDZTbLDROlyo-HYEHlux3jbQYW5mXM-cVzPVwJBtNxuQwS-dsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف آرژانتین و پرتغال برابر بولیوی و دانمارک در غیاب لیونل مسی و کریس رونالدو دو ابرستاره محبوب تاریخ مستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30772" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3y_P0YRkGPOcuPwyWLwrY6_Jo8k0EszrxD0xsxdYpnBRCsxJGXVSUW6WY0d-efrJiZ3QCnQONJLsAdBE1WQutSyAt2nS92sdL14yQuA-NWjcbJxinBR3qfnaMOgugrUhilt4tqgdQUPnmHzKHIwWpYCnPqqOwv_Lg8R_po59MKSvqLJDsSTBoLa1VWbsVnQvZ9av-4JkjMgIIsPebfgjtAbwfdHoa-i7rDRrdvLBX1CyFdt9Zow_LFBzAsp9TCH-VsThTpz6_Sy-sfSHChidc5jABYCFTsWPNaQn07wAFy8lduK0RBytAnE1y9uNXF5JmX9aOSHwYtS_M2pdyjDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
برد خانگی یانکی‌ها مقابل شیلی و دومین تساوی مکزیک پس از برکناری آگیره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30771" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4bJAkAKqfM7zAftZR-ba6rJZX1VQiSe4kr042WVYoe5VHEWhNAasKFo0tz61wKzwG5lRD8Vo7L2H7rPuGi1bhQFS7r_MSZMa74fYhudym-RoWyDgs9xT6uk2moWf48ezb19ujevYXbFWsiqgWMJNRvuA8mZPTHjo_HSZJWLLmAmmHQWXZoRq-YnH2L9eB48B8K_hQEPa7bSIBs8ytoae0LnAAoJpJBKtfsDudJKJRC4LpiTzYcKstaIgT83R2Qk2yJGsr8HqG0Dk4cK5h4UnoTNeoZw2HwIqGh8aKmqTBGBKDTWWF0QJSWXAgef8V-3DyOfdDOVu5TS2FqKympMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30769" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB8bYfYNi9QDI32B8B-Skx-Uhyv2GE3rXbl6-gJHEgyY4EMEID-R8WJV0QJr_r6qoybdMz89hBFFb9cJ9FrKOk11CAOChX3O7icYb1ikECDhQu4AUGN0Filqitaw9oQjX5JPT-Las2XmfcPjGwT1J5ShNDz0C43zFOzizZ8wkga042kOKnXfJXUVFqQ_cwvXP4ZB_b25gz80oyxBaHtR5T_TxbqgM0uw23R0aHf2YHs_ID0SI4jVkR0InHJEUnnDEYEhp1RXYgSeQ-YqDSQPtiXQy5hjQSXWvz6UcSoiVgk3PpJbAUxFh3I8ZZxVHExdbilWvlQ3VEVRyp3EP25Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
روزنامه‌ اوجوگو: کریس رونالدو دیگه قصد برگشت به تیم ملی پرتغال رو نداره و درآینده نزدیک هم بصورت رسمی از تیم ملی خداحافظی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30768" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ploTWtDolDS4HyV0DGA8QfcoX4seeT3xQH8dUBsWlV1Mdh5Mwl2oIPZJ8NBM3M8h5-W7rcAnrtLHrhelApoRi23m6oopE4O1GclvVwluy3k23v7OlLneYgx2BbGPN46uEzglRDITxWS2NGKFHFNTmgE-RmrHk79pSTfVDrpBlCOWSdz3f6ctt9r7XycVPnfG8879eQRUvdjhXQMGt5jm4t057bhkZ_lLcDSAYfmd3yHHAeQ2lEbG6HPiclNEqYwED291EwZgpr8JpQILRrawMVq-MRBP3paqLCbU2oinm8TzTXvnxYnIk9yEW68qWu0HSdYIm2AEj5J0_AxELNYCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30767" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq9PWfRS50GEK4h3d0Ln_7VnNItWDLP_BxjUkpfNvHmCW2ZsX0OX78_ubxHWNWDWyFYVc4Kt-40pttigIXleusrGyDZv6b04jF11_ZomESmRsJKkbvZnf08zrif2GBvg8TeLw8UjuxvlJ1VjmZE-KpV_P20vjm9O_L59s7xMSu6PUKb_52t1qB77esewhI4j5UClJKg5tV5Su138syTE2KDUfhnC-T3quHLZs66s6xaEA8NiDGHewgakcjgd63FIyiT7klxQE5tMLkx0V15bqBSM0aVbyyW0s0aRHU1pTfn5g_wawj9Prg0CpmxQeDZjHB9GVOIMDWXJ22AT4sTLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=ZTel60mz8qgKsqLQ6_LaoXMWcmq4BfNE0Ksjc6Soeql73dmEtOxCN5TXC7E5WNu-2rl5oHbEx4pjwfsN8CyWFUvsvQUD0mJwsYpo7aM1Pafqo5FSC0QqZJedke4U_3prIwRNR3NG2qhlV3XZ6cME4c2qYVXPNOmQu3EbZN-Cl4USL4bAk836MIH2AawUJilV419g7MomVAir78qfDUzF5undEqw5GZQnp9a4DpPsg00cafLRGi9JCWEBqOB99Y_tqipv6kLi6b2uSkRoQ00Saij05WST7dzwR8OmvVoCeDaycWPFUcC4uxtJSuBGAb_gXbNP9AHq41CXcP7oVI0t-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30764">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM70GM93OkeVLHDkkfOBHyjXWDs_WJN6870B6VNbgFPFR4SqB-4X48KTe75FqI4_IuJ6wEuiwDHlDM-MVkV8CIqgfjRzGTBD3q74QgmEgX2e0zyoWe-fdNheC80msuNyxdDwYtKZVWQ0zxiJf-XtC0m8YGZsi_41mzMyeiTW0ygd_GVCJ29hShwLIRVS-1I0X4xtTeFiKOPHMBpBn8icBYv1t14JQAJfnGb_FMDVeQ_pBB7PytVVexLOK9q2WLzKpsZ-9-3sl7qn72rOwFhW6oAy2oJ8J6epPsH4MqETWRoeVcJRyAcibVHa4q0RpQopRoaLp2QmiBmda_OGoMBisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30764" target="_blank">📅 23:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30763">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=dVGhXYMte3qIib2f5QQ7BiRXsoyEOw7N8YhmaREC03Z298yLs6gUbR2yNSHErtJ0m2Nd1Rv0fhTVZNiSZUXmnhMIaVf9L92EcR9W4yYta6Wm1P1rbxq7mzzfENPv77qHw-_xpa1oQNv8B1Kos5yY4ijdHSSp9I_JOo-UuXo3pNpIFRWUhjuF1Xjd0cKvUg7Awx0WFCMvkL1_NTUsyDaIzDTN56ckdp-0AqjeAx9VMsmYhuFHt4X0Q1DugAggTgmo6bOrbYUWKFGagl4mZjheTVEsLRm49_XqeB9TJl6awzvaE-5hQO64pOKJr5DXg2wRG9e7VgNv13mnhV8tgPaoYb1Cf8daxEP0SVTw_2DgGIeW8sB7ugrzweDkeN3EsQjrRo5yFye5lrBVDQtmdqAb9AMianoKz1XRR6p2O1mqBCtdY4G_v0YMtITwh6sjR_II0l2OfV7mb3zBjbZEONoAwViL4v1d34wzxPZtXGjv8WiGN_SUkL43B8P9FQtSEYJ65a-Q3RqTR22fzyM5F1a_1LFAXRxEwJ0jG7fCp8q7SmLTUPN79fZjsWxHZQfYjFJNv1EoNnUdi9q71h8NdN9DS289tOt2yNWCefaRsuy1Px5Etr6k_O9WR0Aqa0cDb67BlUXG74P8quHCdtR3a2ABn2H4NPgWDFDelHAL_ms_9Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
#تکمیلی؛ یکی از شروطی که فرهاد مجیدی سرمربی سابق استقلال پیش پای فدراسیون فوتبال گذاشته در جام ملت‌های آسیا روی نیمکت تیم ملی بشینه اینه که مشکل سیاسی اللهیار برطرف بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30763" target="_blank">📅 23:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30762">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7FhbIcp3ua9ey-7UMAtiyszSPoJhs7fuXSpkUkNpX8zSCbwGuDHrMERtRq3wqDH1hLeJbYv0znCCFPjRYTOn7hZXMmOgXLFQzUHoQnGTUczY_x6w9R9ymSh3POjxdtyCPAMmM6TxFTZKj7eqmGvEHnFHiOs8SdlE0L5L9gOm-Rkxo8HPaWznlm8dqVvCaQ-I6fFXrcfdI7f1DtOFFnhPy0aol2F4yfaVE6v4AI14gjZ6MWqAghnM0lZuSo69jIZ2d_h2FY1wYJOoTzwEs7rCwecIjxID8JnCefsgUkWe2oZUD9juhVrXCQOFnWhL09ElcvYxt7g4E5hgdcSZghVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
نگاهی به عملکرد و افتخارات کریس رونالدو در تیم ملی پرتغال؛ بزرگ مردی که یک اسم میوه رو تبدیل به یکی از پر افتخار ترین تیم‌های اروپا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30762" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30761">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsoBcbUhQNieYgdocZ3dky9yE5RttyrZnGb7un5ZcOnCuj1MTkQZVO-ZRWWvw5qaAHxiTkoRG5dShJSZgWcncOC8nwxL4QxbqnX3r7ef6HQcuF2G7mb39UeJ0BR2op669Q8KNJSASs7Cc75EnRGwWXrHauMMNPhHn6Pk_D0XR7JdPnGVA49s-Jdmv7IegelNGAXsDy0Q3qvfNrdDPQ8mRMZMjTi5F2TZuXaRLuzRpB4OPShYPd1ei5L72S6r6GvX4N4zIHKAUOL9HB3ohL4xm_EwQuUVlsVDwUR7m1qsSK_EiJ0hlGoWYPf0wIFQUE6SxqYSHUI3SGiT6iPUIKl8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعدِ پیگیری‌های‌میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد. خدمت تسویه و تحویل که بعلت‌مسدودی‌دارایی‌های میلی دربانک کارگشایی مختل شده‌بود فردا عصر پس‌از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت. همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30761" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30760">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLM8z05KTbAJ7qfXo11rAz9lMrsaE_T-sqftu0ngwBGyZP0vaTLvn4EkM2nT-HoTjIYEdcx4qa8wNL3zfsAVGMYW8FVWUjf8LTtX-h9L2TAOw9PeyZ4VBAWUP2eCSMIr03XCCXmoLW5Vr8C6CrUJK-7ydhQl8aZUlGgIaOB_ZCTSRnVMWig2jIS7-F02FwACsEnrTpe7m_3e0T3PJsc9Z_jflaKJke1OvP292jQz0OFxCCeQTJbbiOt8l9ssk78Er8H-7DvnjNMQ0Q-EiXFsgOIU0xFBuPdXy3fqmxU-EULXlkiNhirZnEoVqwMsJvk-D478Bb89o6Z7y5tK1uxLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30760" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30759">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzV5uKhWIc9O0AwWmbxY87_e7HpGBWWT7qyuhCJrv8bGwxzNgqZm6vFS5QCif6m9YKEeykNvOHDdO61-5R9rTVzoQ6kwnqHqVPUeIbM_-QrLOZW7W9P_DQ5ja_nYxHHrgEnVDlNBFf-ZItwYK2zmYzcUi62a5VdyFv_wbjfhIx-mT_si4ciPO9ys26YZvGYrFnY8Mbw41HOFcWDcMQroGtHxv-9S9qG4mmdEd4U_p1VqNmeLew_77BJVjneO-bWkdxBLNwiglOjM8oUnG-PrkSUfXmKRXBu9cxUU-IjvfbSCbHDU1Z8gBxDe88dFTNR8a6YhI0Z6HagMBfOWVYYswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یورگن‌کلوپ‌سرمربی‌آلمان:
توپ طلا؟ اگه تعصبو بذارین کنار و آمار امسال رونگاه کنین متوجه میشین که‌توپ طلا باید به مسی برسه. اون تو 39 سالگی یه تیم رو تا فینال برد و نیازی به حرف زدن نداره دیگه. چون با بازی کردنش همه چیز رو بیان میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30759" target="_blank">📅 22:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30758">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4VFhn_nOhvv7FByIegUeEgdP5_XIY22bGcUAxPdpmz91GoHSHFPSz2nNCMP_hv-ufwiSG6ZKcq8rcCFtmC1Nzce4nTsf-opQoRIPInhY-gCf57OX_V1AybB2wVMhI8JtfhV9S8fGap403FOA9ErgrB5DBbxh8MYFgMTPDLXVboE72e66Zu3zaa-hE9mZGYR24R-HePHzdvIM--Cck36jxtPjKQkTJSQvv42U1uA-baOLzxDgEbcxn1CbIZsZSI7JZ6dLY-Zn0ZO5JV3WT-6YI-T2F8lxNC5wVZWfb9ASLf8Zeo2XRZw7_aFWSBvvytk4Wh7PRXa0-gTvH9E6vUQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کریس رونالدو: اگه کادرفنی‌پرتغال نیازی به من نداره خیلی راحت این قضیه رو بیان کنند هیچ گونه مشکلی بااین‌قضیه‌ندارم و خیلی راحت کنار میکشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30758" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30757">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFHwsjCOnJ7ZHjW2QjNyo2pwuynQiqLqz2k2h65IfE1aa8vZeU48GrtM-lqUo6b1SX14aUPTSotWymCL_Wp5CLEHi2pl-S_b5XCLhWfWZFJtx73gKFYDq8JxBhdUBU6bSPOXTIZ6Rv4c1jYq0uH75DnTTygTDkbP0UFM1l4fNiN8pxkoSMbD1WsmNks7oZpgyCuS7Cl-TZH0zF7cuqVFt6yrWUtWzDMAlD750-zI17lcsCvLDR3TYOwl1xxSVS_EW1DZtvWWHA3BnjYSrCDUOsAyGitDly4wHQNrdprw6Bl4Qokx8nugVXrSoSujtK9HQy5BY1iycrNJTkIp25GeTNJa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFHwsjCOnJ7ZHjW2QjNyo2pwuynQiqLqz2k2h65IfE1aa8vZeU48GrtM-lqUo6b1SX14aUPTSotWymCL_Wp5CLEHi2pl-S_b5XCLhWfWZFJtx73gKFYDq8JxBhdUBU6bSPOXTIZ6Rv4c1jYq0uH75DnTTygTDkbP0UFM1l4fNiN8pxkoSMbD1WsmNks7oZpgyCuS7Cl-TZH0zF7cuqVFt6yrWUtWzDMAlD750-zI17lcsCvLDR3TYOwl1xxSVS_EW1DZtvWWHA3BnjYSrCDUOsAyGitDly4wHQNrdprw6Bl4Qokx8nugVXrSoSujtK9HQy5BY1iycrNJTkIp25GeTNJa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وکلفت ابوطالب حسینی به رقم قرارداد امیر قلعه نویی در تیم ملی فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30757" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30756">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnzdIiESg4qdsQ-9JL6GF2XMG9ODAeK40TNI8zPmFYwRq_IjyoQ284OSMKRtRWYmHlXSEqu9eh-h0cayp-pIB5kOI-zYXLIT2rjk_dBwNa5EE3zkk5-7x4Hw_6INmhkdF7Gp-gVRu1BtkVR3F0MEyroVGpNAVbVrDZTbyAIfVIPejrr_iftySjmwQ2oBQsUM05V3tA5UPsvoe8ObGQYzZM9DbSd_Y4LujhKIzuUL0DhqUBxMft95pUVvNvwUKajsBrVE2QxatT282WlUFqqnnXKIv0OTsIbO43r2_AbZ2iqNq5MmMfenqh7aSUFHEMY4faa7_sMjshDKhA6JtVvi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30756" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30755">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJcMiGLPXm_5Q_vCUN-vv4ezCQEfLvtv3TDEtPV0n0wsJC5PeAHEanJP4HUyjIf4koMWqI0PJH8_TghSgOcmiOnoj31bBpSc17ePX9YbjdNklRTATT1fVWJXsCDeY9IrrEx8CC4OmrDkbsNarQs6_42UfFyTvq1VpM0ylRqB7Mf2RqaitAjRiAqQyOGD3o7cFIsb84cPDgE_Tzzc_1VovoHAJd_QTjqckP4QKiXKaZQHM9aEBfpa8geIvdZxKxXzEzUhE6rQwom6Bjbe1FM02CnqEXfWc40oRw1-fo3j1VizAgP1qYdBxaWusm6yPbze_0SE6GZh-HFhLUQ1R77_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30755" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30754">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL20IcZR0qLJcQOYrpLPRf4npUOTF-QZuhydJ5OdZfzY2Ja5qyug81_A0gisyQsHRjbA3jcFh4_RRYg9ZmAMezkfPpTiNS8vdNM4jSHbajZzWss6ggt3HYT7JwRJF0Ixi4lKLfTi3Fh4qntHCnGsEfjCtQ9M2kIPVaDl1KMpD_bSpaH9S62LewLF68TFe7FxqNglpw1xx8uNDYmFa_FncH9IdvxEjrd1UGNcrqoge0MtmI00KaOqxYL-vGd67JFUvCpB91YJbGNU4tu_2ckwRgIAV9gSc9tgK4ZGAOl7H9X9rpMLVWg-ZmNZspVTDSInHt57HoIDcHpB8cXLWBB-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تالار افتخارات ۴ تیم مدعی لیگ برتر؛
استقلال و پرسپولیس با ۳۹ جام رسمی بر بام فوتبال ایران؛ سپاهان با ۳۰ قهرمانی نزدیکترین تعقیب کننده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30754" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30753">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=eTel-wfLa_cTcEJbuMtkLHdt6k15reWMFSfN8ABvGb-qG08jnCRO1pU5A3-6np86qz_bu1Kr2tbbVs7NMNLQ5lqz81JNS-rmwgWBRMwJj9O_VPo5yyCa5EjLRAX1GKbbeuJew0u74ZKXYy2h3-JNdg6KZLTLH6L9k0f4Fr4hJwAWtdH7_LAWJ_0XUcOwxWbCA4ecMH4iRSnMbBhypizb1qVkdSc9qM4mdJ5qzqXa95rp-tDG5YZF4TU4UK-v-2H0bxs8dQPPBbMLJBrJ9nUOueFxNKOHRxUQXCMCP-325cKRML0jZyBij8quccod-bs8RZfsHOdQL72wSjZedBT8k5TFHC982rg1b_ZwRwoqor4SpbY4_SF4SrSwOrtH3ttFRNj_tOr00YdnxggdVHnZPFh_YXvvVTHoryqnirSyBoeZ83QeSw3a4ws71-W654z4E4PsO2RMWpgA6TA_VCQ_Y43W-cydynekH71-fUnfDdfcaHs9uDqQpGcYWHqLbgA72_GN8IqCadPrk59dL5HKEvSo8QF7qfkrk1gLrGOxjZlboVqiNesnvBJ9L3RIu0ao8mAK-zd-5Ke7SY3Q0ZIsc1MV2Vgr9GiTHluUWUGzj3mhFITmqgwmrCHxjJlIUmUAi_wVtBJg7pn2d5mLixtCWNPrNjZTSdKHwW8fFIIY1TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=eTel-wfLa_cTcEJbuMtkLHdt6k15reWMFSfN8ABvGb-qG08jnCRO1pU5A3-6np86qz_bu1Kr2tbbVs7NMNLQ5lqz81JNS-rmwgWBRMwJj9O_VPo5yyCa5EjLRAX1GKbbeuJew0u74ZKXYy2h3-JNdg6KZLTLH6L9k0f4Fr4hJwAWtdH7_LAWJ_0XUcOwxWbCA4ecMH4iRSnMbBhypizb1qVkdSc9qM4mdJ5qzqXa95rp-tDG5YZF4TU4UK-v-2H0bxs8dQPPBbMLJBrJ9nUOueFxNKOHRxUQXCMCP-325cKRML0jZyBij8quccod-bs8RZfsHOdQL72wSjZedBT8k5TFHC982rg1b_ZwRwoqor4SpbY4_SF4SrSwOrtH3ttFRNj_tOr00YdnxggdVHnZPFh_YXvvVTHoryqnirSyBoeZ83QeSw3a4ws71-W654z4E4PsO2RMWpgA6TA_VCQ_Y43W-cydynekH71-fUnfDdfcaHs9uDqQpGcYWHqLbgA72_GN8IqCadPrk59dL5HKEvSo8QF7qfkrk1gLrGOxjZlboVqiNesnvBJ9L3RIu0ao8mAK-zd-5Ke7SY3Q0ZIsc1MV2Vgr9GiTHluUWUGzj3mhFITmqgwmrCHxjJlIUmUAi_wVtBJg7pn2d5mLixtCWNPrNjZTSdKHwW8fFIIY1TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30753" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30752">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT2_6fK7XGBQSOTWjNefxVTNwVCf6mUT-iSU9TucNnL5pUJXDTItIyTrQhrS4YoW_IJb0Qra1GayFr1lhQF9hfojw1qsudf0ml3hJm-2gW2orZ6x257m65g2t8gMfk1LlqjqoY_gnh5lJ5rNKEqFN1Vpq-CY1MSXOQ5Lyoq8Vo936Cg50M0vl41z1q3qUT8K_B_bATfJPWfz-uBED1TSkPNgjsCydIU-LCyyr2eETIZbqKyyG-uimvbMxedgQOknJKZ2fmo4O2zYn9ft7ExfxZgseKeen0yTt3Jk9Qr7F3oOC-6B8xVYXmsCqSRxynDD3qKBfFbcq-5wa6Do4jZbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30752" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=BX2qtRzbOVddPCxZLzFaRLc4f5XiPg9AVeFJ9hTbhvJK0TqDmUmlNl6V7sDs_7YRXP8HmQ3f5FAhVf4MsZqJfbX-ZlN7wsf9Ip3vulSKtN9TtCgoMPGwx2ITLMTM7EO2Y3EilsGxx_KlPemCUqbGOcnbB5MObeDC8WZ42St-d7OFZtmfB15YnvAy-ohHnjwesSkcg7kdtn1QHbx18qZLUvJ1UibtAZ0UY_TFUMhX70zr5gB2QrVwOUgZTeome2W0acqBD6IKFsp7OMkkDInuQZVSs_wnnO1PnXTWWSpzOAWAFB0LrGBuhGeI4HPTffr6z8uSRcGdG0k275-zPVIDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=BX2qtRzbOVddPCxZLzFaRLc4f5XiPg9AVeFJ9hTbhvJK0TqDmUmlNl6V7sDs_7YRXP8HmQ3f5FAhVf4MsZqJfbX-ZlN7wsf9Ip3vulSKtN9TtCgoMPGwx2ITLMTM7EO2Y3EilsGxx_KlPemCUqbGOcnbB5MObeDC8WZ42St-d7OFZtmfB15YnvAy-ohHnjwesSkcg7kdtn1QHbx18qZLUvJ1UibtAZ0UY_TFUMhX70zr5gB2QrVwOUgZTeome2W0acqBD6IKFsp7OMkkDInuQZVSs_wnnO1PnXTWWSpzOAWAFB0LrGBuhGeI4HPTffr6z8uSRcGdG0k275-zPVIDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqgN62rqqchuU0r5O4Pv5ZnlzYif_PjPp6gsmPubqku55bilVn-6IPO-atRD55GwUG_m9NiOJjysdKN4dsqce0whutt_zNCXSXpE0vpXBydNIWtEAMUeXDzdWlmKR6FfVjdrVxNwBOp3aVdp72eCqvvR86wkuqlGUmDcfa5MsSPW8G3gDgO5b3gllPAHk-REQtSeTlNrlbsSAiHhV5dqEtNEdfavTpqGL2ZHorZyOmc12cMTHraht05F1Zle1VRUnzMszyTO6tiAWlcaSjORdGFtCgMqyJNV7PSEzJNvMrwvdUBqxcWOY8a8BGmNBQ3Uu36uXdkoOvKpt1di8tLcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=WU3i4VqerJKCU0XgsPUaYQhKt5Zslq5xeG8ChA9QQU-cS8LlQRYGpXurtkYroiwX1lImMBK-wvOsivSl76ZdLvvqs9-mLPlI42NFULmn5e-AC-lyfPQ8XdfX0f6OgoN4gYvJc60AchxH5mp9my8JDXOu9ub-ADbnfetzpGL_tJyq44F5U13y4LseZiq0DfWBvfl_2iteNmJyjEWOhHP1oTqDz1lYTL9QVomzrvwuwg9dARikgv5UtLDpY3IZALGqSPN_mc8_nx7kP7qwlcEfHGxOxQ_E8aaVT2runpaMtOQBJzS1_l2WAaQ0wCBAeMUe0LlieoILppD1ZUgIOkJbwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=WU3i4VqerJKCU0XgsPUaYQhKt5Zslq5xeG8ChA9QQU-cS8LlQRYGpXurtkYroiwX1lImMBK-wvOsivSl76ZdLvvqs9-mLPlI42NFULmn5e-AC-lyfPQ8XdfX0f6OgoN4gYvJc60AchxH5mp9my8JDXOu9ub-ADbnfetzpGL_tJyq44F5U13y4LseZiq0DfWBvfl_2iteNmJyjEWOhHP1oTqDz1lYTL9QVomzrvwuwg9dARikgv5UtLDpY3IZALGqSPN_mc8_nx7kP7qwlcEfHGxOxQ_E8aaVT2runpaMtOQBJzS1_l2WAaQ0wCBAeMUe0LlieoILppD1ZUgIOkJbwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA12F8ocJwm8l_Gb1GgYpdcEuGgl6O_x0H1PSXYpVueH0c7lp0rEpVZNbEuYsWUpR11ZqkCLzME59cI7RaXjrJJmD4daf-bNfl4Zte4rV64OzYMGbq4Of6DN9Y_7OOXSVvAbiHljgUR42xDfae00FBPvsV33oYhI1rumIZgnh4LVRePwCM5RLaTFlm6XE0pyuxe5EEXQqP9xqFp9kinBGzZPncmDYdE-y0vHANsL75wfs6ltHxudLZT4Iux8ooit-Bb9HBEnA3bbmrgUXllOkSypmibOlvZgkbYk_eACqaZwQX-eZgA8D-DUKOWF4dYg8geW3s_FdCTcs4IopGmJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drjlm8M3tCvniVddGihosgjhGCcL1JibMJmzyq7fAkiiwCfaN8_GyRfkL5u2imESREnLWqQbaKzZkxaxGKmmDdnpPFzzFa21EMotlubQC1yeD3fzXobf3jICE_l0OnVagiU40St9izBu2byi6cNyVBKQT5yyxa_FhENS9qTk81Tmxe5MR1iFsrFg-a3j_A7UR5QZaW7dI_ycBfPjpXlSCDzwK3eCGfURyti03MOfD_lyeVG0oWWDBcpdZ7_N0NaYbMjfK-IZUC7bnulFtUP9Nxoezis25gCxYsOSRQ7-JasWsfQifdvlG9YL4yIzZOIucQZnDTIPpDb75N_0HFEP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛ ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30746" target="_blank">📅 18:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXSZ4Kr7sUYZLS38jhHin1mBVYZBXXLPLMiI_xtn0WbU7D0vG9g6Rwr3NAGWjvrbqbbuBumXl48wRkXF0hF6q7ORXkf13sM3P_ofUwKlmhXeLw5_ZLjUDAvfdYxeLNjDvTMa3kaJkrGT-xgiwsj7wpio-0vNQ1v57rGrO8U8i2givGnrbA7qELBghaa6ENDMHk2w_phoLAEUvCLcXQ-s1rDFNE54NXRWBfJBtcf443FNRahU2Siznrt7msOUUc-oMV1grm5oAgSJ42ls11lZLpcbdcMWkzmhf0alrV_0vcCOm0ciNU77XUOf0yPo7FR9IeQG5nuIuKvLW2Toer5lgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛
ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30745" target="_blank">📅 18:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCOlj0g5ecK2awhtLBHlFZAcAcIkpLfO9bcBjvIgas3AFwhbHCheETyomHD48Cp51kegQu8XuabohJjRJI9Va1R4ipGoIAEJwRw5G8c2UJl46FMiJMput1u0c_tY9GpNLTPisX3t5PJ_reWL1IjBgtEdF5TlGy_enPJtoTboqpUGNX3JM5vqYUSKZAdyfGHJ7fb-WTZMjG_mLNjZiBQ7_hpiLkKMs7P_7tX2HyqlvOA6bGqViynh2omNhl211C4OihiG29mbRyo5s0Wy54i8Tz9jHmEMpLAMh9Jx6fh65ng0RIlAOENCz4ZnLAbCeRqk_QGvy6mf8zUs__HsKaPsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتقاد دوباره پیروزقربانی از کادرفنی تیم ملی: من با تیم آلومینیوم تیم ملی ازبکستان رو میبردم. با احترام به کادر فنی اگه سرمربی تیم عوض نشود در جام‌ملت‌هانهایتا ازمرحله گروهی صعود خواهند کرد و دراولین‌مسابقه مرحله‌حذفی حذف خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30744" target="_blank">📅 17:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30743">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrBjtZ8bzSgZa8Aql3KaeDKihXPfMhY1j34YWAYHHTS8U2l0EnV98TpBRFWYNdeyCUVIGMSOvUakh7PS0RZKbFJtNU92cfR1_ZO1TnntQ9pX8i5pzF8LH4kb18JwnZyUZVaBAgqcYtYP_AmmYrNyFs6XU0KmKJ5jFj6zMED8bZQIZZDkX2rzPoYaAYtfZBG19wDrkIwf3d3tTkdUYlxa6JBqJ6880qWMESSOOYV6r2d1lJHc7GDcOtexl97E6H0vzEbdS4YswU14I9JPoKucYKS1s9U5-vgoZJ8KYOJwqlAaRAEeRxaJ0fDmoq2uxX3fPMU-Xuor8uZ0qzkNu7r45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داوید نرس ستاره ناپولی:
وقتی خیلی جوون بودم تو زادگاهم 2 تا دختر بودن مسخره‌ام میکردن. پنج سال بعدش وقتی به چیزی که الان هستم تبدیل شدم برگشتم زادگاهم و هردوتاشون‌روبردم‌یه‌اتاق تو هتل 5 ستاره. بهشون گفتم باید برم دستشویی، بعد کلید ماشینمو برداشتم و بدون اینکه پول اتاق‌ها رو بدم سریعات برگشتم خونه تا کونشون پاره شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30743" target="_blank">📅 17:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0DRzp4PHXnbf0uRBlxRVApnZiS7kE0oB8iZXeWvLSXYRgsGqiWnN1lIM3vAb8xwQmkKM22TDCp-rJzHBtFYpVcPDbEzf4P8SVKcnpwRQQOPdZnXRNYQAdpDyx9i0PuSzeZyau-nxOE9Uhnvf0NLkyTjxTqkimEJZaR_RiooXzwOByuwsCVnxTlKpe0eWKFiFDqyZDKgu9myzNPisKAoRnH5dBJ71ow5k8OUAqdxJqsHUdMEVp5d6NrjHdwJFa6gbSDtLwPATxf5GBZfIQyKk9fEiFAXujoc2QIqOpFX9tqv_uQ3LCytIEvmVkhriUkUmWHYTWSjX09fnKHMnAuhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علاوه بر مهدی‌ترابی؛
مهدی هاشم نژاد ستاره جوان تراکتور نیز به‌دلیل‌مصدومیت دیدار هفته آینده با استقلال در هفته هشتم لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30742" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU5G4uaPfRKK1otzFFuZQa1XV0CgCYWLGtdYKnqrHxM465MuuM5sBHVGko-agE6dx4RvbGiBT2DCp9psNwpDfqct3WiUFAgwFaZmDRkY-ZiFhMxCTdjQgp6XhpaVrBiYHw2LrYTng5UtjYe8LXzMO7mnEIFIxrahYW1bajF1t5xYsIS1RJt7vHm1XGoVTzWJptTdRSmtcuB_msJVeKNdVLPEbj48QkXc9lHiZfF8a738r7uPtvVv6ekB7Q95taMuEF2jBVpr62eOmvlcMGtZqvvR544F1X2uXlIBMpA5hwc0iNDT-nQviYQN6NPnUIdQqPKyVF3VRWI63kHqqq6COw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
لیگ‌جزیره هم ازباشگاه‌منچسترسیتی بابت تخلفاتی‌که انجام داده شکایت کرده و احتمال گرفتن جام‌ها از باشگاه منچستر سیتی و سقوط این تیم به دسته‌های پایین تر بشدت قوت گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30741" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiSjfysCWiYZMKGUnBdkcOCD5iPya7F1iEz0l_pO7UBuVKATwG4DwdC76LQCoyTv6gpL3QE5mm8GS8xBHjJt232z5B1ZojbCI5gMKtwIvdHIxQhr-VJaHs-GS0mkZ5rhsNCEgolRF9_OA-q0QgV3ZLEp3HZRX3c1zFNidGjwKzesgIgEpiV38m-ttgIJlpn7s4o77zOcPOEI9UmNZQKIsbwqat-UyF1rWXjFScIOX6XVovRI51yl6Hh54GMDlhqbyjrvORsOtMadQGdgy6JolE2qtBYQ-d2bO-kC0o45IzGg3S2rs3cDAXIqy_XH62U6b51CGooqLBiK16tkfwgLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30739" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
#تکمیلی؛ طعنه عادل فردوسی پور به بالا رفتن عجیب و غریب قیمت دلار به عدد 245 هزار تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30738" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAJ7s1tSBEIo8B6-gcjsLNmdybfQR6FidvV84CX5HkFrMBiSqUr9BTBWbr6StyRLC6nB3Y-4MJDJ69gLM702HQ_lNRxzXA9tRAtmQdkBzXSd38riH5mc4Pa-Jq6uBIFBxUUqVElObz9bviVI5RaziA_IlANxZECj22F6lX_gR7XEIH54rAJsNe5245mxZqt7bWvcBWsUSh3dkrngtoXBVaiDk3C_LJveNdGWmvJwpFU12_37MW22WJZ2UUSF4sQuQOEOY7i4_vw60pHgFuw-4ooP2IWQWXSzpf3iHiCK_7FDcs-kIMXu6nJtUdoOMxtPhAz8bSc1qaPixlu5gFj0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
نشریه‌مارکا:رائول‌آسنسیو مدافع رئال مادرید ساق پای راست مصدوم خود را به تیغ جراحان سپرد و حدود سه ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30737" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
کی فکرش رو میکرد که نکات فنی مهدی طارمی دررختکن تیم‌ملی یه‌روز به مدال قایقرانی ختم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30736" target="_blank">📅 15:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNFIPLtvEo14Qz-zw6VN-U2GRykN-OaF-r1H0esnkKpRsi5DPiqIRJtNlwbPGZwPKoX2-7qgjMHMXRWzB2lixgds2rnIbTqmUWfjwhQi3NRLBEmixy8lyDeRjZhdQp6bOPh3IqYk5S60d0i-46888riYrOVri8OjNYVxFhDDd3bG8bKXjtHXr-a-Q0aseTJasiSO_owA5UYkXzRZFZOcMItQBSz8nq9LQgKXcWAR6iyg56sDuoC9BHSUBBVzQqwKliyO9C9McCea8aRLK5_la6s7Tqjr6hqIBLkLzdZHWHHAzEDYxdaH6QWGl8N2fFEuQl1RHMrRigUo0avGIbolhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPcIVmxZtKfy-bvzz3gQFnkrQ3H7zG1Zn05fjZIbADEA1ROIhkvLG-kneF9lu6yETaJqI2iO3vAYTCejz1hhSfa0yUAz2m8u2VliPJrEe-BgyM3PdVt3AltoN7E_YqDbDAxEqH4jnKNKWohKFnEF2RuyXdCIQxLeF1GNSKmTcDWDMMsNu5zID5VaPIcS4act56C_tBKuAOnIkUtM_KAYHTTWOubtRUonlW3XI_QrGo34ijrONfr7ogbqG4AnqoWjYNs1YURgFlV-37xdad0mhEnoybtBrCoynQpKvr2ghHUTC5oVJxI-7fs-np73ZDKWsjISPSSwodk9Xi-nkhga7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز ستاره تیم ملی برزیل برای درمان مصدومیت‌اش اردوی تیم‌ملی برزیل رو ترک کرد و به بارسلون برگشت. مصدومیت رافینیا حاد نیست و بعد از فیفادی به تمرینات بارسلونا بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30734" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWouV05JUei_KZJ8IVAI0O86LIlbI9JUlckDElwhiMgbqNdzSLw5x_hCgQXS9jGHyL0UolRAut8TNcY977l5sx_RNA5yHs1pG4fE9BojuXBLoiKtXCm2Sj5Ic2U46ZZ3KHdWeMbVL_OvA0vRzKRdTMXhYtvZSoERRrJkafkqxOgu2zdLUuuIlfg3qOVgNwN-peQDQTOq523hrvlIyL6eXQBDbcxval2TINUpioHJ-Jc5Xc2NXhAnTXGx6HJPnajEZKtgkO7eE-hHr8pD9c1whwiQz23myDwEbE1ZKGPrxfs_Hiwb9N1Tsl81kkYo5gLSpvJaLGpf4hP555whFV1sww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30733" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjMlGW1nvLAyn7Wc0NA87M6LEtrs7LootUvmswJthkfawucRGr5W5y5zNY1myBHk5xPdZoDld5aTmiOsbSmA5vBMShQ2NACYFQmHscFWR2XAQ5XvlbyCFSG18qOA1n8e2Tr24W2wzIeyH8vxmJ_tDbSJO374WyPyBhYEJWzWGpq0KFff49eW4QJaZ6gXT4mHYHX7pj0YMGNhoKmmOqo5tTLnDNj5ySXlETj6c4AVc2pkDJFEZT1CL1oimOXzlMZ4SMW__Dmn5x8sipF05LgN4VfESRvu91JrSl5j3WiO-wROdUh59ja2zkFVpgUSsIrlcSYhohyR6LNUwBHyJl2MNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30732" target="_blank">📅 14:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA_Ecs09mDS6gixT-eJmqOzvtMcqjNTgpevpr3AeLndCcmTwLIHAXQs8MArsgw6rJlmj1K6oXL9WeSc-qGB8cJ-DjX52FZtgXNnZt33G9sooCHCRKRA8KlmGpoYa2I7z9Bd45CniXNHVSRcJkid2w4doAJFV36hpI6k7BtsRg4hI8i4NVuWDKZEZELXlDTnuv_o8IT8-yDzFNFizLFzEI1DQ5_oH6ufvJqw8VEwn1_ay0_Ol64I_2neg-2cqR3kpXpsOcs6BzE0Q-cDcNg6iZnGnJlyosTQ7zvk9i-wk2UVlnk0fajJ21ebEvB4WiJshHMELGyHuCbyFEsizkR2L2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
کول پالمر ستاره اسپانیایی و انگلیسی بارسا و چلسی در کریرشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30731" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UljtxBT6Nbe1kFwlg8nMXe_IuEeiRwq_VrN8BzkEh8NtT3jOXge9k5ei1anVmmGFsMnhZoO4A74p8RWJOBfkPd9ihv-ht2JvvyKpXLk2MFeFSw5wlXYyM_W77t1VsxYjMdCJ6kwSMLP5sAD1-2AJ1ol0LJdN6CGbHAo56VyuKCEXa4XOt6BY4aSniW2RM_NBk2_bSbMzb5DWlSCF6ABWhxoubcILGV8ggftcvxpGztVmDaskxC5qvWa1Vys_bfIt9S_UTRLdWIxG_pRlyDT8luvuXEomt4qhWxteK8vjC5KfmRUMK8O8uFFJGwrIFjW8JuhinHKAwNuc8QqdnSkwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون: در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30730" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHIAhbJ4JVd3hjFRfHrbT6c5APNtmSS5fSQW0JGwMThh2j_15sGMjlV6hvJP096CGwpXjDzjosD17-7mLu4jHORfVK43vIkbGi9PDQMincmyc1alDvCNNpKT78TDn016VVJ_EYDv_Z4yytuTuXYENSTCAlq2o-omWR8P7jYr40hYaVeF-b9OmBXVXCm2_c8b_Kr_dEHQqjr6-ITOgxPvhS-GuqC45mUsHWIazt2sHuAovpGdM-Ts8mjmEvKVffuDljTQJmGUsorUPfcHm8TYk5wKY3xqvNhaBv8GO2hYKL3KM_8m20nGFroN6rjs1bzyM_U--KBf7J4EC21fl_iqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون:
در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30729" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSCrM11CsHP6jt8r4MWXJ5dkUvJxXo6C-b797QBmYIPT0WRwykmJm97ZQQiyLdhagJcbECcAkJHntrVfrPYsP1NgTYOJUieQOk-oHjClA8huHZaq9XQdq5EeKnXKI6YoXNBqmFuVwz-MkBtunsnmyqve39aQ5-szZypwWW87bK-XZW0O0NA565-xrBWpKelpdZaR6pCyVxnwUA_m8IdViXWTgTXedhY0pD7b6EczlsLqt1pN4ZAzv72iaAn61cexxD_5KDa7w94aL5VORzbP75ZQDp9g04yVrrdxNydFDbk8_lH06oVq3LCV0IxAZ2V_3CKsVqPL8SQK6_dMVbO2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhBQx3WrVfmX7t3wDTjt2Hb-Tf-9HP1qtfYZtF5jqzXo4rQoZ2eb4GcmOXB8nKr8priqwa58muRHyRDScuitw2OTPxBU3J8CrAbidUY6hgkXiKy4qztR7AaK3HbdqEDSWvClwhVQzlhFS_BQ0dM85OU2GjS6LptWS6IJDIYMojPttBzzJlkbXYkaDbjiClqaO-QzUHUJhVWfV8Y8I_-DYV7a0pmTxhkainI5Yu7oiI2U6xP2YrBy0QbNaMi83y2ww3E7IxbHQsYSCQhu8yqJ_US_crwxHAopmkbh2HM5K7Uo_VghkhG_LbJX77GHHy-SssVki-x03FGeQWFtfvrR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmLtu1Aa6iXXAG7M6PvZijfkFt-IVb0LMlSEIwMlFkAOWbzRe9QVVX6MWGaTe7N4n1aa_uvGGjBJZ9C1zhTM1ws3fko1FfErFY9clB1_PiQ3JsjJ67TqpFULcb5SLnx3OPlqoQh6XQt224_wk6REyCUrdR1OMPQv4-ONrxW-q3dcivYE8MXekXJtK5vm9SLL-WMv0u-xPpxrjCFU6KAYpamytLMyRbZfIn6n_MINgbmeNHE9tCMz2bcywJzLTLyJgEwt-TGvTFOrA4z7Z4oyM-lfhbqUrm6JBorv9j5SfHTrW1pniXoq_ZrrqI4mF_r4o_eb4GSewMj0NmRkI6eQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30726" target="_blank">📅 12:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=MKQo_Ax5NFmxtKaaY8qdBvvvc8wD2Ha0nxv_7LGUPKWeOW7flTcDtbh5klyZPNR6hS7DDBPgs6XVWfmxtHxM2RW9TvFJ32IJfhxjeXmEArFYizf4ujNWIjlL5gcUUpgUqMOgHxkOiaoaZhyu-6w0_z9WYk_Q3EbSHQP3PRi4dLeBXJEU48iMyZVnprkHlk2K2eOn6q5csfusVeCvcYLR0QbYNEg1Twu01cGG5qdlFU7ZzgaBDKyKCy4cTapNPnNA98aFRnacxQyqLZ8gh9VCjYBl0t_Bof5HB0qTegHPyJybm8lBWPzeEU1kMsn2wULAPsLWgkgLMTaY3h_D4Cj8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=MKQo_Ax5NFmxtKaaY8qdBvvvc8wD2Ha0nxv_7LGUPKWeOW7flTcDtbh5klyZPNR6hS7DDBPgs6XVWfmxtHxM2RW9TvFJ32IJfhxjeXmEArFYizf4ujNWIjlL5gcUUpgUqMOgHxkOiaoaZhyu-6w0_z9WYk_Q3EbSHQP3PRi4dLeBXJEU48iMyZVnprkHlk2K2eOn6q5csfusVeCvcYLR0QbYNEg1Twu01cGG5qdlFU7ZzgaBDKyKCy4cTapNPnNA98aFRnacxQyqLZ8gh9VCjYBl0t_Bof5HB0qTegHPyJybm8lBWPzeEU1kMsn2wULAPsLWgkgLMTaY3h_D4Cj8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیرتولید محتوای شبکه تماشا: درپایان سریال امپراطور دریا؛ باتوجه به‌درخواست‌های مخاطبان بار دیگر سریال پرطرفدار جومونگ پخش خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30725" target="_blank">📅 12:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7VKpEbFyEmcSKzVPcpK6HmA-z-_zfGiAoslpqbjT89WxI0YI3bSaXeKY3coGJHhVsW6z3H5uIkJP52FknxGJPvAc-E8A_kW3IW2OEM34ncZO9eJwZdM4i1uv2Kc-i2-ZTV8bwZ7doFo7tdKv0TX4iCOSZkQWDWegUSoUSNMQWMceaUv11FrhiQrEwf0HqKFQkbA9xAx4q9Y2Cfd8EPzdUuQhvr735NEPHfaflEKs3eRXOhRbckcXsRJYZ2vu5cXRy6OfkF2NwkrGMqtgpw0L7CBsuc9zg5OUMvSmEDsA_B5u2BN9gjmfbt5Ag5Wy8jG7bcUh3IBrXHfQaUclCKmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛
محمد حسین کنعانی زادگان کاپیتان 32 ساله پرسپولیس از طریق ایجنتش آمادگی خود را برای تمدید قراردادش باتیم پرسپولیس درنیم فصل به مدت دو فصل اعلام کرده. قرارداد کنعانی در پایان فصل به پایان میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30724" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=V_y8qHgN8a3Z5OihIzEisHUv3xM_Zw1J4KOfNzloZ-ksKxKNMpGp7TsHPEMIYwaHpE5PmJdDf-JsKOwzrOued34qguBZuqjs_rbXCdk6zK3dV4McGHALMOObZv-vRJyDH6R6SQb8RNSogb8g5oVVWa9ba-wWffM8VY5VNmAPknzkFP6OUydEbq-8MywcfNmNHfNgKZ_DjLAYnPqZThaDL4mLnqQV7k1pQDYVCTQrtUEwvlpYyVvJQn-R_9GdnqAtzflzffFZ_O6e_ipJ5esWakPCKB8w_0wM_tbd66dABw0vutZof_0BImQ7WdqpTdbgn5JM8UjNlkFrmzCAI1nKdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=V_y8qHgN8a3Z5OihIzEisHUv3xM_Zw1J4KOfNzloZ-ksKxKNMpGp7TsHPEMIYwaHpE5PmJdDf-JsKOwzrOued34qguBZuqjs_rbXCdk6zK3dV4McGHALMOObZv-vRJyDH6R6SQb8RNSogb8g5oVVWa9ba-wWffM8VY5VNmAPknzkFP6OUydEbq-8MywcfNmNHfNgKZ_DjLAYnPqZThaDL4mLnqQV7k1pQDYVCTQrtUEwvlpYyVvJQn-R_9GdnqAtzflzffFZ_O6e_ipJ5esWakPCKB8w_0wM_tbd66dABw0vutZof_0BImQ7WdqpTdbgn5JM8UjNlkFrmzCAI1nKdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30722" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWHuZd9uC8Dmo1yaeL83AbjBxlOZyTjAGI48vGs8IADjZOLqeV2ovggubmhypmUwgvXxVDEUwhuxk3vCiZ7Rd5SSh6S1bUBauGOJ1EAM7xC7ArTRHnk1z7jcJi4VmhWK-heP7sJOTPTHfo0Bu5-I6PgG7z0vo9g6uMwh74PJNxXgjZ-BqCCElMOBuNm89I3Vzg8HrYtz54HJxQwKlU_F1aVgw2dlxRJSJBzo124M6V1JD8GQI8AvdTFN95yLqrS9QF6-9Pch2CpJYKttQ3Xiv9XGPURFBsGdoUUJkg5-h_BchdpU27N5HugNG0v0ZCgYcpV1qVvl00lUGTqbdAWhrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30721" target="_blank">📅 11:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0rzVIHhoNZT-30HPJw3IupKsKZDEqf7FCv2H8A9v9gRXpmc4cXCsIIVNeXZdK2EHYBt6Wc_vN8JLPjtd_CGuWvIi5IMxOxzrAIF6U8eSD75YfjPL3bfXh9GnxmdAufyya7KColJ_H6BxLKISacxYVCWMAKGdYAQ5Kwms7_BS8LdDXj4JWRI4YAifvgrWXyLDICZv4RS7G3FVbiz860V6RQez08YYwaZsRa55Vk48eqTCF4X_f3Z5bBAtHw97fqMhYzlrjLXf6m6kx7cKOEPXz8qejmIg-2_Hgr3QX16qc-WIzlOCV0yYtydf7D_X_lCyph2uwVplO80kRtJ_FXJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
تیم‌ملی‌برزیل امروز ظهر در دیداری دوستانه بمصاف تیم ملی استرالیا رفت که در پایان به تساوی یک‌بریک رسید. رافینیا در واپسین دقایق بازی با یک پاس‌گل دیدنی مانع شکست سلسائو دراین‌بازی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30720" target="_blank">📅 11:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHfLsaaRNIbVj5zpss6iASfrG_OVZpfWkMPN7-PGOOhuDViCiM8BHseJKzkQM-Y80on1sGYzXZXbHnLArucjLdAE1P6xi-uMR52ATbP5sow9oTyLSK_MJ6J6ZhVL5zZXsE8UPGr4--C_vmMtVscd6SZi01iskL6bsYErF7I94taxjpAX9Vj4_PZvUKn6V4xDIYIhKYw0IKmVslihqnxxejQ1gUw6lZZifWJZm3JbOLyoqY7StrkaZCQAERD5tY6oQHlQ6yxM6eNMyw4HNojVIwdaX_I3lSGlrzpiq6MYPo2Xpc-E7EYAse49Jny86G0jP4Tb1OnJazfzBMi9LL2tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با حکم فیفا؛ باشگاه استقلال محکوم به پرداخت مبلغ 30هزاردلار به مسعود جوما مهاجم کنیایی سابق خود شد. آبی‌ها 40 روز فرصت دارند تا این رقم رو پرداخت کنند و پرونده او در فیفا بسته شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30719" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxKNfzxaBbsmo-yUtYawuiHHoAOXMMy02PoItqpOcjFUVPxqDdNzOfp0MdYD1Ky00bKXt9JTFe_jhkLZ1d3ksiCJyqcVs0-tHhPzJhecmBFxcXoezTtLxp4888eud-L9c5oYC2qlPWJ2vdakCghooBvheCq7KBm2_NsA7Xg8ZnkimHWfLSHAuAAxQiHcuaLVzX_jcLFJW_Ap8Dj4w3M9ukofbnqxVxN6cUO1QEQXXrN0LPPLsFBUAj11uL6hPiPudhGkRXkANtN5dFgGuSNcGnLHwdKgXwX-266L5I-LEhep0e5vmJDn9WfFmuckWNjLGhMJOJi9Z3f7GC6Y9f1eKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد اسفناک تیم قلعه‌نویی مقابل 50 تیم برتر رنکینگ بندی فیفا؛ هفت مسابقه و تنها یک پیروزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30718" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30715">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfG7YHfXnApFkZxLX56zAlgHlKG5ass0I2o3Jr-bjlu2tbohf1Hje-2eoBurSpPmqCI8jr2LNnmDFdf7Qwm7jsznzrU-o2cBqDcewUXU0tbqTvwDRp7Q2eNPBsStEI3TFqHM7k5pENCISapnkT28VRT3PjygNkDJvFtmYtjrXWDcH4kPg89QApnfA-yE53q3JqjdTRR9cWpbpcOte8JieQ2lGhyFXSNX0oi6URC6OBGxI9HJJht-OWiP6L4yLF-M9Jb_rvWdt8foV1bSV0XfN4fpQU4-t5d9I5ItXyi9yaKBfIobHSS1tL0oHV8ZEcxPQYBOITdwoRKUF09Tpa6MuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30715" target="_blank">📅 10:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30714">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCmF9aAIX1grTex0mJKbkpekbtfXO3Ca6S9wf_J0QlgJUvEDJscrY8cv91-s5huYax_2LF4ET97uV1GG4U-oTrPUV9mB8RnUN4uFE9Gr7oI-x7cgjc1b-Ddir3zxMlE5xplp3h6k8gHfIQ6WsXk4XuEnjBsfwyZ8smsQaXhvB1Yl6I3ecsW8mqEU53Ddg4MnubYY8mmTJwnEqoCtUW99sZXaHRiTLCQOwxfDapkn2sAWrcYwrx4dz4nNp62ZF7_LC9LQj34f5Dh1c1O384IjZParzPfg9gbH2QFEjOBlsueP_oZxbEB1_0mJrl2bex474GoH2J-e-gmv8iN1_AeFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30714" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30713">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=YTj8_2IxstnrAaALrt-M5hcC4WD0arFQ7rQPewlE6wi8-u8xoqpD9bfy7Eyql9gY1B3zsYX0Yl6EQvKedJfMsJiA2y4ccbB0Et96UPuFM2FBICbEy9FCOC45GAxy2kQKFQB3olpNQ5stdWbkSgIKB5b6YpbV4Nczfa1iM5XJtirEmqck5NM6mPWGCQgb_JTeBOWYAWVAUajDFXX2DEly4iairD5zCbx6Q-wlLm9e6qH5UrbjPEqFDxKuofcEX4vT5xA8re9HH8ksSfLPVrX5uZxs6U6SGDqZnz94vDpHIrPgGsxeIZlmKz__jpNRRdB-cj2SegU2Zuz13Jvaq5x8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=YTj8_2IxstnrAaALrt-M5hcC4WD0arFQ7rQPewlE6wi8-u8xoqpD9bfy7Eyql9gY1B3zsYX0Yl6EQvKedJfMsJiA2y4ccbB0Et96UPuFM2FBICbEy9FCOC45GAxy2kQKFQB3olpNQ5stdWbkSgIKB5b6YpbV4Nczfa1iM5XJtirEmqck5NM6mPWGCQgb_JTeBOWYAWVAUajDFXX2DEly4iairD5zCbx6Q-wlLm9e6qH5UrbjPEqFDxKuofcEX4vT5xA8re9HH8ksSfLPVrX5uZxs6U6SGDqZnz94vDpHIrPgGsxeIZlmKz__jpNRRdB-cj2SegU2Zuz13Jvaq5x8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟! دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30713" target="_blank">📅 09:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30712">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=IM8NBAUcy4ndWpG3hk6F6S3wOauMowjCkzGY1XMsvqpnGR23GqRdWVRTxLG3EUkmloZa2JNokH4qsL-MbY-4IryCsZPRK9-7_0NRs3tU4T59FPaU4C21_uACpRz1KncT2mKn0XnAw4VFPTtxm3SXzeluE9O239z-TfQ0usrmdinAuWG5hynlmODbOnO0gI0UruF4uV4G2ubKtk2YsVlp29nZZocnkIZnsj3a1MqqCk5ewY_XvG-spisS9hqsJYmsFF6fMVf3CVgEz2OEZeeMI9JAhn9WlfSJFGQYfUrGgDBoRaDhKldhhoJWwEIAz8lyFJur9Yw3C0ZuXy9qYd4GXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=IM8NBAUcy4ndWpG3hk6F6S3wOauMowjCkzGY1XMsvqpnGR23GqRdWVRTxLG3EUkmloZa2JNokH4qsL-MbY-4IryCsZPRK9-7_0NRs3tU4T59FPaU4C21_uACpRz1KncT2mKn0XnAw4VFPTtxm3SXzeluE9O239z-TfQ0usrmdinAuWG5hynlmODbOnO0gI0UruF4uV4G2ubKtk2YsVlp29nZZocnkIZnsj3a1MqqCk5ewY_XvG-spisS9hqsJYmsFF6fMVf3CVgEz2OEZeeMI9JAhn9WlfSJFGQYfUrGgDBoRaDhKldhhoJWwEIAz8lyFJur9Yw3C0ZuXy9qYd4GXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟!
دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30712" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlZuQhdpzxOKUHCr-REBoTrKj6Xj2uxKjtlTlSyOdzy5ccTDdw6aVdHKpP9Glb93ugEp0Sow-LDUy-EoXz7jYW-72DG0oXVYy8G1idpmfu5xb4PUOYlS3wtG8l1XsLfJg5F8JQyv8UHINBosv7EHhF92t5S7bxBt6KSvFn-vha6LpBsvoWScJIwKBNXU3V75AYiwKl1yGwo-GURkRSmkO14BI58Gl4p02rhJziv-j_JhHItF47WRQNs3e3CbTszihO_skJD_z2nFjxCarkvgkNAXO7PYXkbcdzPhb3DW8GD_1oxU4xoyNYsbWuBWj3jU9OVMvV3U0dAZYhZbedelWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdhVO-p5X_6M82O_yImy9PrytF1n1YwB8gnvPH8R5XBpMMv8B5duMu7jpjuXIXNmnKP8BHbyx3heGWp19_wP-SxFFlPWNI8uDvUHiNTpyZQEdteI_xQt1Iirmxf2SNiTz2N6O_pgUSKwh2vyOVMvPx3c6hs88Oa3FNgslw2i5W4TvDRDHO1zQDeZpWyGfgVxR89rKwNeiqeng_pWSWcL6m8aEDz4YiMHCQp19s-_Gu7tL4Rs6tCNNptT6fA0nMNAweNk1dCJUWVfB0V6jeA-2VlFiai-MjOwmavFlcbiMzehLfMC957efE0TbBrMRctWxsisyMykH-Nt18KzA9qAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0ykFAbCYFWJkAcF5sCuSIlCPwHu9teufnzrq3ArDTlgn4WwNbuZVbhl8DAa6Xnv1x0jMYvM-VnQIhHBL2mwVBqF645jV3AxCx8Zae8PnDPqKqpCBDSE_tCf7CifZDbAPgmC4KRPaGVfV-Xbm3mw-duUnx4bMtvi4h2tgGMf8bP2DDBBs3n_he1rlp272-22BrjakS9mz1O68berphGWIY5aFiehiLqo_5z2rQ2MEXYmBDLE0JeQmlLHa0vnYyYEaekMTG52FKH98s9cCBKqNHeuzDAYEaIeLBu8IPSsNIou-pcISBCZjn45Lv31TCWlsXc2Ax1xY6GlhODN1nyHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pINgacDhKw6K4_ulD1kgG1pW-VsQAhO56tAMhEULjidCgLiru6fgFelX3n713XpGMDVM4GIMgEsr8X3FduXcUiW8on7TINzmj1xtm3VaDngEqAv58DhnnpoIPSvILxZMuVOoFRRpejNMj86QUt7YUI4la4Aoe-V8jtq5ZglcukJOqoxttX50dVV4dxgZC5sjgVR5G-KYd885qXfusWBkxtF2U6JZRKMLdUW1B5FMSK7e00_ip7_BMkr0nOOkiLVmalwZSaYY9YagqGu_E5GlpTaEhdMFEtKvi1NF-TWzgHu2E5WJuep1LENNorbH3Kjy6w_XElmTMTVdxW5apoRHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6BI1ki9H0mD4mIuKKHFWXvE13H4op2aQMoKMaxUU3dtggnhmfR3eaGZB6rQnrtNE4RMbARVB2b3MHmALYb8X4gSpLJ--wBi5jd9EA4_xJzxWDRly2-SX3EChyFn52ZOxoLhI9nHftXWL5l6A0ZxHbdmv94iXDsp0rpSyc9YaJ_gErTUhgpN_Nylr-k9yQGEMZsDdPftfA_dtxv-Bw7ZlSW8RhuAar305fSGPgmvLVnWIymetUyUxw-zxBaGppC5Dd3_u4OS_8_J3vaYfMEXMHdd3hsv3HLeBwU-DLnZLXQIQKrUV3qC7JTCJYzigZgeJenOjR_VfBNTVHzjxUm1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
