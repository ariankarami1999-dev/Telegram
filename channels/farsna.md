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
<img src="https://cdn4.telesco.pe/file/b5e2NMAAzUJVUtfdA3rsccfySBU5mbTmCf0pj4cCH6VBBoCZFIJCOrZI_sCnnWh1id2EjRv6uW7DnrL1ek9Ebk50ToL-mVmnUcz6bVLVsRoWUfEVhnuuJiTdOWjQUhxHtw7yysy9WpGS8HVU_l6vBr4rUOprjfFipIZ15CPe3PfFeSU2o6XIrcxnaQnNe5zwsHonYPtNLksQM1ssP2eSXT6oEB3HGVQwb9_plpGiREzmGJj71E21rZlbsjMFYoxQbv16Z44Q6CMv73Hr8WHTDgKZF-wIcM1rUUZn701syNf3KPitVWCBeFahX6YvJOONabmyDZyQ0HiHraVBY_cUmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-443633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUc3ORTIfOsEQw2nDBktR9I3Jz6sdFmEGvcYNNra5KSOfQhfsUafDoqUTCWefupjmYXlfkrE9NZOJwye-fNdswj4ufk2oWrSS1iHKV-OqgMxzTB5cKHNDv6PexDg5nqSlSXHUScI4C2xNJ8Cvvsg77V-w0gqzEVcSYpcwkmn8XnJ5H_E42p0IhPnKAJbN6Ve_5WHvzNoxUNV00gqmNrWYqGnx6Zln_mQRQQzWcTaAJC_oyPt1C76JGcQDjFjYxQdTONYjmiQxPKovlMWIRClEFNWkdCzf9m1NvMf7PlnQ-RQJTwwisR4ck9NfviJ3ZvAwCpSFe1M-KC4YBW6C2hRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی: هفتهٔ آینده پایان دورهٔ ۵ ساله مدیریت قوه‌قضائیه است
🔹
خدائیان: گزارش‌ها و دستاوردهای این دوره از طرف مسئولان ارائه خواهد شد. براساس ارزیابی‌های انجام‌شده از سوی معاونت اول قوه‌قضائیه تاکنون بیش از ۶۰ درصد از برنامه‌های سند تحول و تعالی اجرا شده است.
🔹
در ۵ سال گذشته بیش از ۲۳ هزار هشدار به مدیران و مسئولان ذی‌ربط صادر شده که نتایج آن در پیشگیری از وقوع جرائم، تخلفات و سوءجریان‌های اداری مؤثر بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/443633" target="_blank">📅 10:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp1ED4B2J5NdJ_Ao4F3DRKKm00mcW34WLOiJZe7ZeO_P3ok_fiK28ilzbcdui_JErzTPz5bFnLAS6O3mabl3QAqG8Sjm0Q8z1MhVH4RlI5mX9HRdoO5vFxor_a0GxBRpUVdFHFZNRRIVBpEwEqCQ2VWtAbgCqp7-TjFF5w0JWmnV8Kq0V14g1AEQ0cJZH4mEc2Wzc52L7QSh2ubpaBZxpd2qDBaaS0ut5MoRZaJogjcRV5VMzK5NXfUw7nDjyiwNZc7a7OgERgzA5PuoCVP4gKrXSTBziM_mUP4tgYeGU-7VR12NcW86QI-m1cmUcQ69bDN__msdO6nmMlWPTjEx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پاراگوئه اشک بازیکنان ترکیه را درآورد
⚽️
ترکیه در دومین بازی خود از گروه D به مصاف پاراگوئه رفت که بازی را ۱ بر ۰ واگذار کرد تا بلندپروازی ترک‌ها با ستارگانش خیلی زود به خط پایان برسد.
⚽️
باتوجه به اینکه ترکیه دیدار اول خود را به استرالیا باخته بود و با…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/443632" target="_blank">📅 10:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0KdSv0xUs6L71Qhmk1QhjuwUE5j3Qjo3v2REbNHH9NolCKVcgnHr208-c51k3dy1Qa-o4DiWE8XblYU27a6z1RmZpQVwHLnRFgA-75W_Zsu0fP7SKWpeWXw24Sga44HSLo1xaRGpy7NL9W8HHv10Jhkp3ZxReaTViWaA_zzzRUHYPBrkWvY8ggjPrHx_lRmom6Rtui9GbqNCI8tPTH1AzkO8zGRDVLAym1Iwui4BicjVnYr3frAHah5sxAdxGh7cu50bRKNdkPsD1S9TPTmTRPg1tRxqYbl_v4dD0uuZsTzdIBriB1ipqeba9OnVoBKamcY1TQVl9ZDLHMbiQVD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار شهرستان مهران: از ابتدای ماه محرم تاکنون بیش از ۸۰ هزار زائر از مرز مهران تردد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farsna/443631" target="_blank">📅 10:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLu8JhHSeKKe02IJFp0_EvP2Y3022slVxZF-rWv52Vf1rzktWq1mFt_A3motgmyg2738f5VGBR-z3ia35H3Zx4ldeAgnIcrLGcbB2N_dkcZVGZa360FGQ8qLQRlCI95JrJx9e9mbwTEznQ-IY_XxkBgF_jW5HQg_ErPH7d2FVaKDsUFr0i-hzLf2Z6V0o7hu1tL1Emt9YKDu4PifjOuvRkOPGvf96mJAQyDoG5nmwKhffe3ntLZpKGTFrdTJS--cZNwvd9sKCI35LGirXX_KSZ9FiUwAPnU4fUtbvPMLCDZ3cmC9U63vc19CAzoKaVnUpCpr_D8RDzOzr3HFBrNgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاآرتص: ۳۶ افسر و نظامی اسرائیلی از آغاز جنگ با حزب‌الله در حدود ۳ ماه گذشته کشته شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/443630" target="_blank">📅 10:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آغاز ثبت‌نام زائران اربعین از ۹ تیر
🔹
ستاد مرکزی اربعین: ثبت‌نام زائران اربعین از سه‌شنبه ۹ تیر همزمان با نیمۀ محرم آغاز می‌شود.
🔹
نام‌نویسی همۀ متقاضیان تشرف زیارت اربعین در سامانۀ سماح، و داشتن گذرنامه با حداقل ۶ ماه اعتبار الزامی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/443629" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiMIqmzYlFQui4QyFCWxs_ViB0vv4ItQNy9TRYMfXk7FcYDCaqi1Iu7OSJMF-JMYzIuGbFzgW8J8FZlbwQfg2kAIP60-9cWuIBbo_7MXjX44oB7LeoX_WSdege49tiqyKdmJLhnzhK8MNpj5r_VoSYwiscZV6MleHNzvHkhph9qAE7eWaAXFb_RuJ5jP7x_3QN4OLiSZFlhg6adUZty4yknGPRQJcg8iId2S5CfKoSq-jJvLQeG8gN_S3wjfGFUXI9_J1n6JEPlmfbwQ7GGfItd8ZgeiH8nDs5e-IprUv1aoF8MsEDAGPBKMGLxKMZ1jw5mXS8eO8TkcvHjcFko2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
🔹
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند.
🔹
اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفادهٔ دشمن قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/443628" target="_blank">📅 09:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در دزفول
🔹
فرمانداری ویژه دزفول: بر اثر امحای مهمات از ساعت ۱۰ تا ۱۴ امروز، احتمال شنیده‌شدن صدای انفجار در خارج از محدودهٔ این شهرستان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/443627" target="_blank">📅 09:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525dddf3d3.mp4?token=tEXBOsx9OeqwEHi7uyeKbsh5wfKzpm_7OOR6Y3uA8XkD5gWhYCSaKFcfmJAXk7bT8DD1wlCz9hQf4Nt6I3RtUWhvYb8s2q6as5DHlVCV4QUCLzYm9NP5PoyNyhcquJ8USIULKFo-vmPGn1Oea4eMImujCwMHnjqhv129Ocz0BZ-1GBby5sEoJbZ7h89lNCFXIX8xdmnEo_WAg6gfGG16X6HERLDQwnyVVT_BQIu6ChAVoC0bknKv_uM2-qM-iZIx0cINRHU5oguKY9pqxGNGx2CY2f8RGFJKcu2l33VEl1d3KKrPtrW_GY5ufzjsFDVyLRV4g_7yCFSYYPTkKFBE6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525dddf3d3.mp4?token=tEXBOsx9OeqwEHi7uyeKbsh5wfKzpm_7OOR6Y3uA8XkD5gWhYCSaKFcfmJAXk7bT8DD1wlCz9hQf4Nt6I3RtUWhvYb8s2q6as5DHlVCV4QUCLzYm9NP5PoyNyhcquJ8USIULKFo-vmPGn1Oea4eMImujCwMHnjqhv129Ocz0BZ-1GBby5sEoJbZ7h89lNCFXIX8xdmnEo_WAg6gfGG16X6HERLDQwnyVVT_BQIu6ChAVoC0bknKv_uM2-qM-iZIx0cINRHU5oguKY9pqxGNGx2CY2f8RGFJKcu2l33VEl1d3KKrPtrW_GY5ufzjsFDVyLRV4g_7yCFSYYPTkKFBE6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم ژاپن به تونس توسط ایتو
⚽️
ژاپن ۳ - ۰ تونس @Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/443626" target="_blank">📅 09:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKX75PgpUdVLbNYB6XALJ49103hG31vi79zMDrsxUv5XmSx99cyx-5pepVD-VBLHLu7c85fqjwKkn20zmQHqn398RR8KSY2lcVxNVlIuO80pnSgAMzvPm7Nj8piTfY_WDgCV5eGExzm70b0vbtGi9zag13mvMGSDl4yOSb19Nn3pLWDKAVexcBTBenQNs_lRME5UOQ2paNY1_JarXlPBHUVduPgsRRxI35nG8RCBQa5cYOGvJfI5hkn2VniYWM7LXb9mZcYVCxgxQmQp0PiMkwA51opKMD2msHo8HDqvFHJGWnNXxTvugXvAGbZudkmxFc-l_-z8qPR-bsKlp4MvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تقابل یوزها با شیاطین سرخ
⚽️
پوستر فدراسیون فوتبال ایران برای بازی امشب ایران و بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/443625" target="_blank">📅 09:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d235dca4.mp4?token=EpnOy5dM1aJF0dzqJur3l1H5d2lMAQ8xHjE8QndzEqgLmte-VpoeNMhbYlGy4S77dgoelt72HC6ihGOUIHrEPTC4aD83GBUEo4UxxTU-nIkD1IQpC-La7yzqsZRV30gsNEGCxfQQeKtZAil43B46tFO96eCMp7wfjfrNg8PIBLU1QG8zhXxDf29YCl_1RetQEOuF9KgjnlB_jkvrT9lDw8QDXudJlo8e0lMY9TO_Xm5KtuxkQ5YBjFk67XY-CN7Xl6h3Wu8CEdPF-EMByg3qSfmyHQPS48jb-nbRPtAgyzUK-GQHSR7hALJcJfTgtXUYS91uRO8a75M4ueaLNs3fYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d235dca4.mp4?token=EpnOy5dM1aJF0dzqJur3l1H5d2lMAQ8xHjE8QndzEqgLmte-VpoeNMhbYlGy4S77dgoelt72HC6ihGOUIHrEPTC4aD83GBUEo4UxxTU-nIkD1IQpC-La7yzqsZRV30gsNEGCxfQQeKtZAil43B46tFO96eCMp7wfjfrNg8PIBLU1QG8zhXxDf29YCl_1RetQEOuF9KgjnlB_jkvrT9lDw8QDXudJlo8e0lMY9TO_Xm5KtuxkQ5YBjFk67XY-CN7Xl6h3Wu8CEdPF-EMByg3qSfmyHQPS48jb-nbRPtAgyzUK-GQHSR7hALJcJfTgtXUYS91uRO8a75M4ueaLNs3fYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با شوتی دیدنی، آیاسه گل دوم ژاپن را به ثمر رساند
⚽️
ژاپن ۲ - ۰ تونس @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/443624" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd89da9cd.mp4?token=IOjh3SGgYp46TxfT9SvZJFdhXpjb7v3HdnnfPKwtjhntJYxRTkGUUGhwPlGcqL_dgru7zerWE-cGBK7Jfijow4lvMIbbv1LNUHPxLDH0huF0LkOkCBQpaAJOi9f81qG_kGuL0hZaD68XjmB9P7f-CSu21Dp2C-fCXAH19Hv3x7ScFfWAUfeQkp3Vz3dvQMI-WmUaZL1n3HE0HTJAGAX94C3UibqMGlnZT4z6oVHsXHnTF2b_cYRg6l2A6LOVXxfxl0dj8RG3OCvO0rQeuaNFiHcrmjTSUS-STfWpsZQZUvmtzyjcpTiSYayWyhQXsnLYtUEae_V_k1Q4mlguI5HQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd89da9cd.mp4?token=IOjh3SGgYp46TxfT9SvZJFdhXpjb7v3HdnnfPKwtjhntJYxRTkGUUGhwPlGcqL_dgru7zerWE-cGBK7Jfijow4lvMIbbv1LNUHPxLDH0huF0LkOkCBQpaAJOi9f81qG_kGuL0hZaD68XjmB9P7f-CSu21Dp2C-fCXAH19Hv3x7ScFfWAUfeQkp3Vz3dvQMI-WmUaZL1n3HE0HTJAGAX94C3UibqMGlnZT4z6oVHsXHnTF2b_cYRg6l2A6LOVXxfxl0dj8RG3OCvO0rQeuaNFiHcrmjTSUS-STfWpsZQZUvmtzyjcpTiSYayWyhQXsnLYtUEae_V_k1Q4mlguI5HQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران‌های سیل‌آسا در چین
🔹
بارش‌های شدید و کم‌سابقه در شهر ووهان چین موجب وقوع سیلاب گسترده، اختلال در تردد و گرفتار شدن شماری از ساکنان و خودروها در مناطق مختلف این شهر شد.
🔹
براساس گزارش‌ها، ووهان تنها طی ۱۰ ساعت حدود ۲۲۰ میلی‌متر بارندگی را تجربه کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/443621" target="_blank">📅 08:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-n3w0IdSLIZ1bFU1i5d2zyJGWdv3_Q5vkUMLLtt7VLo0tR5GAoSkZrnaH17rbhOAIFEhe5r0wkbZRBZ0jyxpj_5AoqeleRjo96hjvs8Xm2nTx8GLgVZPe6BnOEGYJLjo8VwA_3SRwXFhyq3VwhdyutK1jGBNYX6Vdjlz__w2ay2iA2vKaYzv8raXKk0nRRPctRuGfqByeP0WnvE69R3XDCqx6rrDf79lBHVOfwpkyxpzK5q4GM5-qghSq-oqNuM_Kncc6-Nrzi2d_2anbYCpp6b2PELwVrbgQ7PGUUyfNV6AmcXpSpWdnB4Ao57U41HIugDM9beG63r0o_Vcl_AOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO2KMFKMnSAZavkMbMXnjsKC7rKHpNhtqsypd0dTDsWmo6J-mSZejk8k38O9qfz0JRz-cOt1wV8FKOoUo90TpHz3Loe2syzhDlWnbbaidaGlJh6jmOv4NR3clWG0-bVI7oW7h_z4O-1n1xGMZ5Q_fKP9ZVgTRTz8m8-L4goIS6Q9SNKiWP9Lw0uesVy71-d1VeFqnBea07eo7Q_64cTe5eNmYWLI2oan8b7vW7bcmhTBbo2CXC0pBbBPoTetcCtl-VAvobMikCSUr0E3UKpOKUqY1VzoAmwkYFUJCaBUkVQ2homKZ6LtyEoE6WaWdIqVtWmlkg4hsAHFIVy2_9DMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bakT20fJ1ZSrFyZwN-hsHkGNBEeo4L_j0REgLXBnsGSrJ6q6Y-P0CB-fZNL5LU17RWb0gbq3O_xPWfcg5vn8TdNglxYwGZnc0FXPcQCrCglsLMisZBHRErSkhisPSL7mMz6o9JQcnLsTTU6sAwsmmzt_TpREL4bHmMixbVVy7Sl7RbvwrvBn2niYm4fmBNl3CHEORene5L-54YSvbXhSgw3MFuRuentG3S5lGJBgLD82tboqAFN4b6VLZrEHJv4Rfz0cif4LYS3MGwIfaliOujBqeOtSIwW76H6URY5KtorsVsOzS8tF4La-Gr_6JvCW3xECUbiL13x5jmF2GzyzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stA00GcYc-pbhhGQRbuqR6xnl4LfBG_0uUFuuZMST0wmjjoYu9Kd6ijiTfzmBNm7RD21BPtIwrE2OpAMsXvfyguD0ymph3b4olC9WNEuI8GGCheORcBKGJ-_hh3W1VHjZ2G-2LQ3cVYe2jp4YlMU9UteX69DNzRTW8vFax0QOkD0khrjMMBocKamXaRTPS_LOKvcvxZ0z6AfEA3p5PJeiKqssUc35up_GZx5POG4ahSMg-R2NaN-WO0AzWulxyuCr-UGYnKDAEokGBfazMRxV_ZbGP_9lFFCTGnjzLPqx8S_XjqutJFdPHckR6zZ5SXHimvy8GVXs84gpXn4h_TyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe6tIsfmdyVH6tUufAhaWjsmFUfx0umvdNjwUwCMjWSGgankasb0PVNAE9sB_1qP3GwfIBg3FZ8pDO9zzWDKD87k7yBRSNLjYk9l92MFr0U-3xTON7flrg3SwHzmhp5QV0g9sHUwSwIZTjyORw50ITaBYnTRG70DX2ecsgCVfpdWT_MOZTUp5H7BxJSva3jhh6Cdegts6wGHKOiQx41QNJAt1-6vYqpxraMnOYw-Vqssp_RdZlS943RzTzwmx9H-lKD3veqf8HVoVCMmVrBwk30dyKyKM_2yvwo-dh9D1iaUrakC1YorJ6dnGXddTG5CspT0GH4hSKHJNeFZK0mbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uh_K0XEQKdxhVSv-gkAs-mm2BcdVYEH8dUDMQqUB3v4YmThDiG-8BtQreHx9hGNuyLxhUocAY_bUYtLL-IEzICSdOCLsT5uhg1AVzc0RD1omOtfxyM0tma1v2ALbmV_4EYlpXAFRtNz_8Z7NQ0zyAc1GwUNna3FGIq07VpIvaV7O-XUQg3W_v6CYJnoy8J4BHjVi_QlrQ-sosw8234TDxeeKVTBjIBsvuATm_w8_mXnGssEjeNDNcalU50Rumy9M3KByqMccLkvkvv4Re6wl0KxYK5fHsSWQMicyhGBpYL5MszlmH481vlc0HXVj0qaQfCTnMR1SPiF7fD2-l6xp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین روزهای بهار در تالاب استیل آستارا
عکس: حسن حقی
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/443615" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQF5ROEQbAG-pAoDesFhmxtJLxwqW3fw2fFfqGLmGrvarY6W_eHw3DGvxgW2_pP4D9JbO4Hk542DLwBDrLKXepdzO0Atx_aZgv-oKugB1BQucOtQKp1q_33ZKlaXeUDSDDA38Mz48N-wCH32I-V4LE7TkWG4aE6VvfLXy4qC88RixYZ39Bhgdhrs8NXkjtLJLkT9jf4GTDEZ2JkC69DVcTXbRI1Z1lat-9nBrjl0jdC_EmjmnM1dxs9XtYtU-3xktgBpWF1U72miRoh_NJatc1rthvqnHEMroMHkAa3YkqDhxsPKjpBd-8ebHlk7TnnNGaKX_5vlzC0WwyxSlU7EOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
کومیته تیمی بانوان قهرمان و آقایان نایب‌قهرمان شدند
🥋
روز پایانی بیست‌ودومین دوره رقابت‌های کاراته قهرمانی بزرگسالان آسیا از صبح امروز با برگزاری دیدارهای نهایی در شهر بالی اندونزی در حال پیگیری است و تیم کومیته بانوان کشورمان با برتری در دیدار نهایی مقابل ژاپن، عنوان قهرمانی آسیا را از آن خود کرد.
🥋
تیم کومیته مردان نیز با شکست در دیدار نهایی مقابل اردن به مدال نقره دست یافت.
@Sportfars</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/443614" target="_blank">📅 08:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMPD9-HxSdbsH901GxBWL0PCFJDc6Wr8zRnv6b04qVgtblVzoyYp-1BKetrGWPsdqfDo6YBcV2WqZcDnMqv60MajiLoFXpzUkyk5YS4x4Zs7jnvB358UeEG_WARBpfBqT0qEHk3jK3J8YDyOJcznGVKflDWdSg0s2wXrJU8xtJqbkeUwB8BLpW9V02mU2TjaQW9Dn6lwb35ydS_wQ8yXF881iTBBpf79kbNjfqmT9N35m9G5-E6s_c8NqaYgvFV-BzWOzJddhLUeBrooFxAC1fpXkD-0lI0U9BZss8bRYqD6Dryf81ZFCXNDTEUd1d78xiwkl9WGlwbvFrN0K8YzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی صهیونیست در لبنان
🔹
یک نظامی ارتش اشغالگر که روز جمعه در پی انهدام تانک مرکاوا در جنوب لبنان به‌شدت زخمی شده بود، به هلاکت رسید. @Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/443613" target="_blank">📅 08:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">توقیف تریلی با ۱۷ تن اضافه‌بار در اصفهان
🔹
رئیس پلیس‌راه استان اصفهان: باتوجه به خطرات حمل‌بار بیش از ظرفیت مجاز از جمله افزایش احتمال واژگونی، کاهش کنترل وسیلۀ نقلیه و آسیب به زیرساخت‌های جاده‌ای، این تریلی توقیف و جهت سیر مراحل قانونی به پارکینگ منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/443612" target="_blank">📅 08:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c4c5dbc0.mp4?token=eo1YKEAc1jIqgh-ZACUKjWbC25Amih0EKNW2zgSPI6zlHEbY3KIfjseREKaY39q7EeM1Wi-BTXSj4vb9QqsRh0gd6hKpSzGNsbcF9MUM6-lF09xQEhfv-2BVG04BKYQ4wu8uYGfn5nF1v7dzFiuqWC_70Zz0kg02Nu5Ryq1SK9wXkP_s-2n4NKpEc18rJy1Pb9VkQhrpz7O1rz7prNiBRcYXExsBN_L-Opnj1NDQX2KVfu-x2i6pjPwPPkl698wX1hkHcbs4hTjZtlkij-M7zeA23LEUijy20mk8iwqalwtT5p0qyvFVgNt8uI1cjUNe6UabLGM_VLs4l8gaTS-sIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c4c5dbc0.mp4?token=eo1YKEAc1jIqgh-ZACUKjWbC25Amih0EKNW2zgSPI6zlHEbY3KIfjseREKaY39q7EeM1Wi-BTXSj4vb9QqsRh0gd6hKpSzGNsbcF9MUM6-lF09xQEhfv-2BVG04BKYQ4wu8uYGfn5nF1v7dzFiuqWC_70Zz0kg02Nu5Ryq1SK9wXkP_s-2n4NKpEc18rJy1Pb9VkQhrpz7O1rz7prNiBRcYXExsBN_L-Opnj1NDQX2KVfu-x2i6pjPwPPkl698wX1hkHcbs4hTjZtlkij-M7zeA23LEUijy20mk8iwqalwtT5p0qyvFVgNt8uI1cjUNe6UabLGM_VLs4l8gaTS-sIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سگ‌های رباتیک هم آمدند
⚽️
در هزارمین دیدار تاریخ جام‌جهانی، سگ‌های رباتیک هم برای تأمین امنیت ورزشگاه‌ها حاضر بودند.
@Sportfars</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/443611" target="_blank">📅 08:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e6a7959.mp4?token=Hib2eAM165vZy3JqX5yQ_xLS7QWSEhfr1nFTFr1_ILa5CJZ1KPVI16t21-ZobV-iUOMNIx8L_p3bAqZIJDhxsPTGeG94i-RDiaGIvqFQLDV0rLmI1m-51q8ybE6Fn-KFJ9aQsBNAFb09lbmsVOuHmTyLjV-eDFWb9-BUhqadz_PpHe32fobyYlT5bVQtDBvdaZVYcsMvhrccf2hc9VPWkrhALiVXgScir4QcEb_OqLNCHWj5PBvo6oHWWifdMhU32yHsHRjR6atObCtvsvCsbr9BKwTdn4S8rD-PCox8GOmSPqd4xS9JyplnA5L1Q8LWIe61GWv01H4BtPadO4UgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e6a7959.mp4?token=Hib2eAM165vZy3JqX5yQ_xLS7QWSEhfr1nFTFr1_ILa5CJZ1KPVI16t21-ZobV-iUOMNIx8L_p3bAqZIJDhxsPTGeG94i-RDiaGIvqFQLDV0rLmI1m-51q8ybE6Fn-KFJ9aQsBNAFb09lbmsVOuHmTyLjV-eDFWb9-BUhqadz_PpHe32fobyYlT5bVQtDBvdaZVYcsMvhrccf2hc9VPWkrhALiVXgScir4QcEb_OqLNCHWj5PBvo6oHWWifdMhU32yHsHRjR6atObCtvsvCsbr9BKwTdn4S8rD-PCox8GOmSPqd4xS9JyplnA5L1Q8LWIe61GWv01H4BtPadO4UgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با شوتی دیدنی، آیاسه گل دوم ژاپن را به ثمر رساند
⚽️
ژاپن ۲ - ۰ تونس
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/443610" target="_blank">📅 08:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLyue-sAZijz_9rttI6z5MQE4qOzgUtsxS-eTovDXPnu_EWGQt7H0hm0B_D-Y3bAUnvLlaSb0HeB700RJY8y6DB-c08nEsm1hrLUqc2lBrjxh5Hin50t3kXKLyjSnn9HfcwWzzvUr7FtEe9VPQJRldwCgot3w_VjrawJC5j11guGvRskkOSV-lR6iFP_fPIQRGcKrBWT0i7SMNTQEe9DTJEnUqFWfPnjPTc0jTbtny5mgR4C12iICDUJZkM6oMRBjzVfk6GiyXRKsLz9OCsiZq3qH6eGpTzbd-soCCB22SKQSR1iT0jdCfZMvqOMSuBhqVS8v-KlZW5Epkbp0eRgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخت افسانه‌ای رابین هود پس از ۱۲۰۰ سال از پا افتاد
🔹
درخت بلوط عظیم و کهنسال «میجر اوک» که قرن‌ها با افسانه رابین هود گره خورده بود، احتمالاً پس از حدود ۱۲۰۰ سال زندگی از بین رفته است.
🔹
به گزارش آسوشیتدپرس، انجمن سلطنتی حفاظت از پرندگان بریتانیا (RSPB) روز پنجشنبه اعلام کرد این درخت امسال هیچ برگی تولید نکرده و کارشناسان معتقدند که دیگر زنده نیست.
🔹
این درخت که در جنگل شروود در ناتینگهام قرار دارد، یکی از مشهورترین نمادهای طبیعی بریتانیا به شمار می‌رفت و سالانه هزاران گردشگر برای دیدن آن به این منطقه سفر می‌کردند.
🔹
مرگ «میجر اوک» همزمان با اکران فیلم تازه «مرگ رابین هود» توجه بسیاری را به افسانه مشهور جنگل شروود جلب کرده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/443609" target="_blank">📅 08:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVvSQn_Cpz6GDCwIjZV2NHuiJGwopKYrbnCAOK7sSHSMsBvgUe16NaplSv2aF0_D6f41AKP3D-rDAfla1kGIgv5ZL4xPaRfvYpDWaVNXlsgrEQ_GSbrRkfc4FRR4nrvHgHA61zLEa8cbjRtTmVhhdx4_FLX1irIKi4NJSg1DKqOndHatTVc_dtMD62zbaEPLgZ70jCEHqzwVNuRkjA4npVcH1Ce2o4RL_PCAmgUcfwmy7B3zK2D_AB2WsFq8FJ6kU-r2a0jtcj_M_RDUFF6xDL_FAg5WtHzBmW_X08-4E5Fg9UEok29DuZXK5LLnbl0cp1iWUTo_avN9rmw0HRVwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرب نخستین طلای ایران در کاراتۀ قهرمانی آسیا
🔹
روز پایانی بیست‌ودومین دورۀ رقابت‌های کاراتۀ قهرمانی بزرگسالان آسیا، از صبح امروز با برگزاری دیدارهای نهایی در شهر بالی اندونزی در حال پیگیری است و مرتضی نعمتی، نخستین نمایندۀ کشورمان در فینال، با برتری ۳ - ۲…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/443608" target="_blank">📅 08:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFrli8C7-7m6kmlr8C1LMwiPHt6MAPBz2D5TKO_BrjhqlA7nwHOxi3ILiv69BU2Qt6akhTDRJiGNTUt7jqL8L_2DfYlje-MsRHmoiuLWn9bkPR-hru2xvWoFZmGTzS-bBv4v9GWBK01Sc2eV7S394omdaqAVmKbMoHa4z-qL_MHRqjvMJqskx-G201UMP0JG00FDLbfT4oN8Y5JUp_rnxFQNhvKNwJx6uAhm5iGy3RYMExzPRvsPO4gXxAPu8krgD_U0_xt-JgQKSIiWt9YKXVXDtP1GHM9wJxmDkV0nWzg7nnqw3qSOjomGZKwPog4ZFDrrz9PY3Qq4jpY7Cjc7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدرسۀ میناب میزبان زائران راهیان نور می‌شود
🔹
با تصویب شورای سیاست‌گذاری راهیان نور، مدرسۀ شجرۀ طیبۀ میناب به‌عنوان یادمان دفاع مقدس ثبت و به فهرست مقاصد کاروان‌های راهیان نور کشور افزوده شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/443607" target="_blank">📅 07:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2d86b402.mp4?token=c4RHQDzTX1b-TPMI5xN5wcv12gyiL-_iJawl4rX2wQ-dvwr6bJQ0MnmDDPdbkKSXvlizACHCQR_D9BVHyzKnexTzPOYrX_O8o7ZCNns0XKH4l2Eb6ZRhWx2buMrpJo-NE2gzcoOtlL766_WYPk_DTaLhY1dHgpA6Wt7jaIL5VycioTkh59KqrMj1VHkaN3ErG8O9xRyBdY0BVA7fZ8J4f8ouxXaxg057cTFtY1cZt-e8en0UmHSCnSJILO-EUIeqW9aQG6wd7fVnDrLrlueyhyTYauapUvWufXV1wtvrdpnA2GsR-7jTgOcj5A0u_ioqNKZl3TbQeAT9l3bdfTx6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2d86b402.mp4?token=c4RHQDzTX1b-TPMI5xN5wcv12gyiL-_iJawl4rX2wQ-dvwr6bJQ0MnmDDPdbkKSXvlizACHCQR_D9BVHyzKnexTzPOYrX_O8o7ZCNns0XKH4l2Eb6ZRhWx2buMrpJo-NE2gzcoOtlL766_WYPk_DTaLhY1dHgpA6Wt7jaIL5VycioTkh59KqrMj1VHkaN3ErG8O9xRyBdY0BVA7fZ8J4f8ouxXaxg057cTFtY1cZt-e8en0UmHSCnSJILO-EUIeqW9aQG6wd7fVnDrLrlueyhyTYauapUvWufXV1wtvrdpnA2GsR-7jTgOcj5A0u_ioqNKZl3TbQeAT9l3bdfTx6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سامورایی‌ها طوفانی شروع کردند؛ گل اول در دقیقۀ ۳
⚽️
ژاپن ۱ - ۰ تونس
@Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/443606" target="_blank">📅 07:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl3QFpmOyrbouq8KNXIO1ISg08RBByIV-naupIulAPdtND9VQFgSJfTBrXxfGbMAxwOWMG5AhkacBJ1y6iplIorej_rAEa_1oBA0gmgZZpF1fdGc-RqciUxcOCCTkKtu-5EyGiYvQUtzFzXuzB33Z0-zlvERf4mpt8xpScdUSK4Y35B7GXXDlRY81Sz51tRmeMXaWyEUyDpcUG6TztPEP53Tio1LIosZpGP4vtS0TVSsUN1QO6Oq3fSgomSUUUU-eeAPW2X4PzC8M2duCTyEDkhoGoL6lYHqck4jnV1-VTf3DoXGBSwWfb0-CcDCwJRP-MGGl2xsncIrDo4yQ6Q0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار تیم‌های ژاپن و تونس به‌عنوان هزارمین بازی تاریخ جام‌های‌جهانی آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/443605" target="_blank">📅 07:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAu1JpLi582Z5y-l8w5lnsELBSasyx0K2nWo_X0vM6Qo0VJjEzE8cUBx_niEvxjIAo2ekvHLOv5fmNna7bFOtT7y1rYQVqOZNKawrO0sLHvHfy7qEkJkGR9mC_Y1jZC-JphaOOG9wjjXnUJSrD2A99Kmst60j3CKyIVkBlg5sSRGKANu2EhII4QJSclYo2rqbZwaggyJi_V6oFAfisLjVBrI7qPUCYXXAXCJzYXEuCHnwWaDgg7SmbbDxMwvMpYyRVgXULcQnWsdebtMbdmXFKvWd2OBndx9Nau74T0538QYgWRjjL_8cbrY1Wl3uDbZ9jzuToZa_LCoZN4Z8Js6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرب نخستین طلای ایران در کاراتۀ قهرمانی آسیا
🔹
روز پایانی بیست‌ودومین دورۀ رقابت‌های کاراتۀ قهرمانی بزرگسالان آسیا، از صبح امروز با برگزاری دیدارهای نهایی در شهر بالی اندونزی در حال پیگیری است و مرتضی نعمتی، نخستین نمایندۀ کشورمان در فینال، با برتری ۳ - ۲ مقابل حریف اهل قزاقستان به مدال طلا دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/443604" target="_blank">📅 07:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443596">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4jDCgpVxgZdfvNqCnoFiTuBaxgerVa7NmSMGqpCr3S34uHfxxSL6xpz9GHWKMfpSgmvsU1rKRz5h2rBs769ilsvH6cm9VrOejx50aIm36eXpPTPucDnxGWhMNMLKA0lENccYCN6oZaGi0PvLgJUewTWUjALe8FttjN3zbRq0bjMcJEK3X-Uw9_nYsnL0SUdPqn4FsZgUDqWCObGjEoXeLhtrBXNDGUgm0f9DYcNedBTOgGfvSJXdgeZ3YPKUMgrQmBTLlaPc7AWDAydy6c8IjDYAongAhFgbRW2ZvvSSAvsd6XeesiGEswxTz9gJJ81LWmydgFGVuAhXpSP7cj58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rx07q1NRy3NDU37x4BX4K4oQKthHHiURw6lNerAE7nX1FCTWPc4b0AflYjNy1dwXe-wtPDNuwSGuXOlKCXT328o2dkiYx-ojLk_hCQ7UNGVruMuwTtJcgucICusjOHm_u3sdAmr0rH9o7jht7WwVTH5lWsEe5g75ZJtM0apfVbXjJ0UenH5YVOm7AGIJosC_TwrWQIUbWbDo92mQzhQGn6xx02mFYGznJ_UW3-ITv8OoZOLxLtfay_C53QlKjnrdKDiKy-WAboM8IiJHVygVtvIU43VmOR2wb3zLjo7h8CEVhg9faJYrgJlf48nUVOgEGdfkyQil6S1m7_iIKAWqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iodHW51IofbBI3pHi2V8JSeKgGTmt0c89ycpwkl4krBT2rpxYkDF-5aK-NJ_5W5lqcY57PeMPvimSKOERd5kLe8OdTx8ho_rgXQagnZVr-7Q8omAsUjOfIg-Btam7FPc-7gbMvExoyQFVCcpdxa42BVtzVYIoeLDwtgVu08ONWTEomZpjKmpyHm04nHxf2zFAitkv6uXVhh7TyNeDYRgwUog8TQu4izCyN1LzQ2SJxfZJlicTbQa21R0vqIJxXTIcQRRPRiy-RASdrYapk2YeWVzGv7blNRZFnU4hXoL3vEygxXixgTZA-YbrM1vbPUrEH1C6-lQk3hcb7M-e8l83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYVvOoUBYW0RNUvrHb0xAISfKJrkna1Nolotah0Z0uqqy6QDIbDwcuLbUzNXgBALHp85GRBjn79DlqmDs5efcqj_GNXtC9mbV36eOWlrOqZadIYPrk3uQxsq5q6L333AN_lbNbrk-w2W7t96K0oyMUOowANDkn80ELRHhaX9lWr3kDN5cRu_fyKeZRY5aaiaOCum9blIl1dEONRvo5DzZPEmXOGkZ63wwMxA_F4T_moDmbfj_93KvEBI7yqXuD3IBH0kaxBJryhtKQVzDTU4qVWgcG0oV1C_7TDNrk82qOxU10hMXsm-wLQSSjDFvK23MHDzrxnPdXrnoe7ILrDTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyW8aj4bYwqU_JJx1zuOqvXhy1HUOUclfgufnEJqCDhP7PUdgYlgPMnnctFqVUkor_uuv4KAZ2Vni6mm47LJhOmAn5ppRfOhg5_eGEHWdGY_V0QKQcvFQIIxhIlDDApgZYyKYo4BtKfZcOgOKV9q3NAJGe6TNr6_szk2HLtwizfYmT9pg77z-xxrd2d15uW2_fHsW3xsC168XdFFmkxTTpmV6EUtOkMqdvzM2BJHDrmDkunumrB4Oj3MgYsuipPPGNdIqhm1LAEejJfzaSivzlXkKbTZABrTr4LoVoeJ_J57D8JI38qCTrPsFd6UwppU1hbrnan7D5kqZ9vMw2u9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_d-JvTifprZjgwZRFpY_Z-8RMCCpKw7pzRGhwKykSFnvb0QlYsMVU-bsLM_d_1jGhN7EQlxj_27hykBmyZOu_wZZX2WgdR6GbHaSbDCwN9B6zJCJ51TYWjSSSLN2cPQ9JIrMLGQ8oYqOpfWphsTp7EoUX-XEDDfKS4d62lJZcoKgfmeLQX-4TiFujj1sYrpn6wyJof0FdnZJ58gnVgjzd0RKsg_7QgemW0Szys5nUbizO9BTOIpha4k-pruAWyeG97R9PaU23b8QBqskDQa3XJihAjICo0yUp7hfEvczPgtoMTcTtfAK-4stP-IhJzewksUMmKARnyrcmSOG9qr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guwG56yBstQ0QPpYhH6E6fOwEg0963W0-1RT2bSsxgZ47yDiPiZrpM29smxh95SH3i3oOv1qAA4aje6Tev34ysouWqojQKt4NQuDAum5RV77_XtIBCO_MRmGsns1i2NInKCBecUpVv0ZzkRus_vA9-BtsNphpki85WQ9ShFdOSx12pOYBON1SQtKISkrgli43uTFkF1H8ngprpU3RnUbqbPg_8K2mQnsFEFVt5KERqJoyTg-Jiy9fI_v3_tnVkdxr5Zmv1C8jrIhBoUez-hoP4dsvKEL0ToE1S4N94vZ6LZXEvLDbrtZQoWyOY8IwP0cBqMTU-9M41rjjBuI7G0DPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilBlIxgWq7szn2qcj_bOmdasZ5qyL5KeWEcuxAYy-hn8YDVHisEqG4QhGwrOP0CsAXqVOr6f6kK19jyJsJ3-NyftRdTsduihEIK3hB_VHPOJEUS9n5jjnbDfGsYZI7E9bGnTc9J_7nnwdK-oi8M_SRnN6pHN3w4gpcr1lIXno16913LSgMdCjrakkUB0EyxlYBMO_-cB3QwKM_0j9tKjBNVvUX_SKsUe8V7MqM0HdQQpOG5MjdnIuQ1GyLKpp8oMagPFsqS5-RfvGjjYesTG1PQKrZXP4o4CcQGWky8zV8a-ZPbbjVtraQT5__E17yD-L9TC5Cw7MBOTa42HY8Wp2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
«احلی من العسل»؛ تجلی عشق نوجوانان به کربلا
◾️
مراسم سوگواری شب ششم محرم و گرامیداشت مقام حضرت قاسم‌بن‌الحسن(ع) در آستان مقدس امامزاده طاهر‌(ع) برگزار شد.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/443596" target="_blank">📅 07:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443595">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430a0eec4c.mp4?token=kMIVwZ8SYOmiCBilvYmRqxNAh_exk0W8k8sTxIisnjrWc6UMgmuGXnAAjCtoEsW1xRZQbJ-jGmaSVtV_HD3yT0zHNUI3Iuo7Zrad45JE3aBz8SbeDuPDkDHuiBiB6Kb-AS95mOpCscubL3DY6Byj72ke9NE1vwwW2zGXW4N46JSekAXhNXhi0OS2ZffgRegT5U6C6e8Trh1DlZZqw07B0cuKb3dfxv7ZJFj_5FtbFFpXI5ix08ZVpWxyIZNait5XKb_8_Hcchx2EvPutg9OV7TAFqiObIfeNIX3GH0a_0Ycuz92R5gLbNrGg2nnFnhOSfqJpE3_O7Xpturkqql2zpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430a0eec4c.mp4?token=kMIVwZ8SYOmiCBilvYmRqxNAh_exk0W8k8sTxIisnjrWc6UMgmuGXnAAjCtoEsW1xRZQbJ-jGmaSVtV_HD3yT0zHNUI3Iuo7Zrad45JE3aBz8SbeDuPDkDHuiBiB6Kb-AS95mOpCscubL3DY6Byj72ke9NE1vwwW2zGXW4N46JSekAXhNXhi0OS2ZffgRegT5U6C6e8Trh1DlZZqw07B0cuKb3dfxv7ZJFj_5FtbFFpXI5ix08ZVpWxyIZNait5XKb_8_Hcchx2EvPutg9OV7TAFqiObIfeNIX3GH0a_0Ycuz92R5gLbNrGg2nnFnhOSfqJpE3_O7Xpturkqql2zpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای مردم|
چند ماهه که فرزندم صدا ندارد
🔹
ماه‌هاست کمبود قطعات و باتری دستگاه‌های کاشت حلزون، شنوایی کودکان کم‌شنوا را در معرض تهدید قرار داده است.
🔹
خانواده‌ها می‌گویند به جای وعده و انتظار، باید برای تأمین فوری این تجهیزات حیاتی تصمیمی قاطع گرفته شود؛ تا این کودکان دوباره به دنیای سکوت بازنگردند.
🎉
شما نیز می‌توانید مطالبات‌تان را در سامانه
«فارس من»
ثبت کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/443595" target="_blank">📅 07:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443594">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfLhLuQh1i4s1U56VI4POAucRtYdtFJBDb52UOK7mwmAhkyTIfVCTY8HBgPRC541OWAPzDIMS2Dr9aySU6Klu9T_JZ-xA5AyvltvyVttrgFsih_KtRvpn738fIHPn5rI-EF2dgTBhSuoqRHuVAV5-UmLoQVx0aLnmsvcdmxSrRn4sIFD6lcHuaOFa71uuBxQQm6IuCkPiFjXF3rUYBSJSjVSvpejApYami23YbqfjZY4Sv4pub-V-Gj0dsviZWZofQmPC3uH19xRITQrqGmcNsWhqccmrTxaMpBtAzo9lmduvGywswyaWNZBh2cd0cpuX5uxMDyWi2oaeEoXR8UXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از آنکه شمشیرها از نیام بیرون آیند
🔹
روز پنجم محرم فرا رسید. کربلا دیگر به یک اردوگاه بزرگ نظامی شباهت پیدا کرده بود. از یک سو خیمه‌های اندک خاندان و یاران امام حسین بن علی قرار داشت و از سوی دیگر، سپاهی که هر روز بر شمار افرادش افزوده می‌شد.
🔹
در این…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/443594" target="_blank">📅 07:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دریای مازندران تا سه‌شنبه تعطیل شد
🔹
ادارۀ هواشناسی دریایی مازندران: باتوجه به صدور هشدار سطح زرد و مواج‌شدن دریا، فعالیت‌های قایقرانی، صیادی و گردشگری دریایی تا سه‌شنبه دوم تیرماه در دریای مازندران ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/443593" target="_blank">📅 06:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656df50885.mp4?token=iglepMXvfkyikFXjQ_5eAoVPtapWdb3qu2RUeKtzDdz77tym4izfwgqo8OIPb7YOqY5qoxwJtXlOSs2ZEQPTqcNhX4S1ezH6Qcpd60Wm4djdu55WNuA0k_RDmVkBPjA8ej1bbFsPDhtagd6b12RHdNqKulaOzj-1JM5f4rz08IW23da9EILby3S-qh6PgbbxFZE7t0vGy9Whio5p9BMBhlcAN3enjaQ1DrJGPh4XFDrZ3a6JK90EhqRlv9qrYj4LNUGieJccy2fQ8PUNlbsIJeNjm_HT3DiWLjkTudS5dEwIFi_9TNKawcTZnj74A5XlebkLfq7CDce5VrvSr56gsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656df50885.mp4?token=iglepMXvfkyikFXjQ_5eAoVPtapWdb3qu2RUeKtzDdz77tym4izfwgqo8OIPb7YOqY5qoxwJtXlOSs2ZEQPTqcNhX4S1ezH6Qcpd60Wm4djdu55WNuA0k_RDmVkBPjA8ej1bbFsPDhtagd6b12RHdNqKulaOzj-1JM5f4rz08IW23da9EILby3S-qh6PgbbxFZE7t0vGy9Whio5p9BMBhlcAN3enjaQ1DrJGPh4XFDrZ3a6JK90EhqRlv9qrYj4LNUGieJccy2fQ8PUNlbsIJeNjm_HT3DiWLjkTudS5dEwIFi_9TNKawcTZnj74A5XlebkLfq7CDce5VrvSr56gsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
برای جنگیدن تا آخرین ثانیه آمده‌ایم
🔹
ویدیوی صفحۀ رسمی تیم ملی فوتبال، در آستانۀ بازی با بلژیک را ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/443592" target="_blank">📅 06:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽️
باتوجه به مشکلات دفاعی، بازیکنانی دارید که این خط را تقویت کنند؟
🔹
قلعه‌نویی، سرمربی تیم ملی فوتبال: به‌هر حال ما در بازی گذشته در ساختار دفاعی و اشتباهات فردی مشکلاتی را داشتیم
🔹
به‌خاطر زمانی کمی که داشتیم باعث شد تمرینات ریکاوری‌مان به‌خوبی انجام نشود…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/443591" target="_blank">📅 06:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عزت‌اللهی: تیم دست‌وپا بسته‌ای مقابل بلژیک نیستیم
🔹
هافبک تیم ملی فوتبال: بارها در میدان‌ها و بازی‌های سخت نشان داده‌ایم تیم دست‌وپا بسته‌ای نیستیم؛ مطمئن باشید فردا همۀ وجود خود را می‌گذاریم تا باعث افتخار همه ایرانی‌ها شویم اما نتیجه دست خداست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/443590" target="_blank">📅 06:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سی‌بی‌اس: موضوع لبنان در نشست اضطراری مذاکرات بررسی می‌‌شود
🔹
شبکۀ سی‌بی‌اس نیوز آمریکا به نقل از یک منبع دیپلماتیک مدعی شد: هیئت‌های ایرانی و آمریکایی قصد دارند در یک نشست فوق‌العاده و اضطراری، مسئلۀ حزب‌الله و اسرائیل را بررسی کنند.
🔹
به گفتۀ این منبع دیپلماتیک، اولین نشست دو هیئت به این موضوع اختصاص خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/443589" target="_blank">📅 06:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">⚽️
باتوجه به مشکلات دفاعی، بازیکنانی دارید که این خط را تقویت کنند؟
🔹
قلعه‌نویی، سرمربی تیم ملی فوتبال: به‌هر حال ما در بازی گذشته در ساختار دفاعی و اشتباهات فردی مشکلاتی را داشتیم
🔹
به‌خاطر زمانی کمی که داشتیم باعث شد تمرینات ریکاوری‌مان به‌خوبی انجام نشود و نتوانیم تمرینات تاکتیکی خوبی داشته باشیم تا مشکلات بازی قبل را برطرف کنیم.
🔹
در بین این دو بازی به لحاظ ذهنی و آنالیزی کار کردیم. ما نسبت به بازی گذشته تغییراتی خواهیم داشت. بلژیک تیم قوی و بسیار با احترامی است و یقینا بازی بسیار سختی خواهیم داشت.
@Sportfars</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/443588" target="_blank">📅 06:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wuz8EeBk_Cthu8nZM6_Th4I045xTfzg4VJZrR3VrknuQHMPnreMPLUy_7YrW0okLaYMzeCC2sFkNR5YkWV7bZOGFHeDilNGQLAzELZ-BpgP-px32P8zNWy9prNzZ9H-G7VwfUOv5yTSsjsSQ_qr_5l5tEoAWTIoBpwL1GTe987dKab3CXiN0fyvMF3h8NHjmr0OIEEfykKfPGB_Cpc37Ekw_q6j6wim5hlEqXWC1si_XdP4ytwv5p4B0NnOT7ZrNy3ei5d3HhquIlhRdnGmcyNw2OWhprltEGpoKU4SVxSthUSB9kF9-2sFw0z2LSzsDDduzeFaTv0TPmJ7ZnQRLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: برای این بازی فرصت تمرین مناسب ندادند
🔹
سرمربی تیم ملی فوتبال: بازی قبل ۲۴ ساعت وقت داشتیم اما برای این بازی کمتر از ۱۶ ساعت به ما وقت دادند و مجبور شدیم تمرین نصف‌ونیمه‌ای انجام دهیم و این کار ما را سخت کرد.
🔹
می‌دانیم رئیس فیفا تلاش می‌کند که مشکلات ما کمتر شود اما برای این بازی مشکلات ما بیشتر شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/443587" target="_blank">📅 06:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kB8ibG9F4dstDMBFv4kjXa2uJXT5Nnp3LmKZDY8JTiOoXBOGYW0e-gzKBkK1YqK6bws1AVGirZATb2CieMZPQSQK2OIqomDzQyWISnTGugNA_r0MhRzG7OIBTcdbR1R_h6wf4sLqe3FwIUjQVic8wdcB25wlOfsBVew7Rnv5_41NFh22u9snDHa_P_mlwZrr2ooTopbuWEXXJfFmiSxPbCCB7JnKGcq_4qFQb6bmc_PpyLUiNpJ9q3jL9u9KZaHXOa2BNxgWsS7f2GUnh2Jk4r0BJb0prdVQMb7d7sBhE6ME83MCVEes_WzxGF7dm5-PLBPw-FmfRLy6X804i2lAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2tEKKyOjQY1l7BmWN1H_r1L79JEnmofSIN27SKDUay56_Afs2pFvq1gQI17PrMFXUvF5KQPCiSJSP30qr75OU7DQ9BEplJtA5kkbGG0ILlbDQUr-bLF2QPtyiNLIHdF57-N2kmJp6fNoHPJjoMxDwQTVnNlPwXGyTRxoEfxZAkzQCli3Ryjv88WL4Pis0nVKvFwWEdzkI7lz4rQ_97FhUvUMkSO3wfHtE_dL2B9iit2QT71YVZMRv-H-vwal5QA9AJ-qzmv1WpwmExSrVWWEnbQIVUzu5bZiUB4WL6jdxQRIn1c5pIR6HkOQlA2omG2col3qzH5Db4sPzoOZqIWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usNnvu544kK-W-mv-xnHwvKfuBauCV-ciy7LFpbjGLVkf2PkvweLviUF5OGRK9ixYOc7p4TyhAntaLHWl3smjdzyZp_bytN-bdaa0Zr4_f5s47Qmb6wuK_w1ffN1DF-OJbXt7EGstm566IHStvAD2-gzMtkUgBhXO6rqC1jb5sqIU4eXHo1t1En7hFco8n5EYTVzlbuUGDzodQSuSlwuVVsh0p4966Z-MEs6qMTsagMh-NfWNv8FmS9ptY4kMIDRI6cNL2N810gFVKrTN6dtenBXboav2e2Cz3Y1UmobspqD2jBG0OAtldeJlV6JeMvwT8WnWa8lgNzM0c76PPcNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cgcb9ImO6zCwkBhsQEFs_aVim-Yxgkgf0uQRsrV5fbgP2I56WbNQJPMOP-GRy859y7fW2aprum0W0lEYRVfVygOibxeE_UaJrn2jMsdj3Je01iU7KIWps5YQ9ya_8OCJELtOQF6JEadVxvBP6JBFkwj9FwU2eZ5kmQdM5QsLtqu2joQxNGOFF6TpVdZn5ENNd1Rw3Rhnarwd08qmU4tbbfa8C1LGrUlIOV4RA4gEl42pX-pN_lPSU-0WjxpBDHPboHmxPPgHbyoHW_m1kG4VpnGHTdZyeN_LmMiXlQuUDSGgLu4xoy-HrPJ-dthu-Uy-cFh3-GnFN2xd8xvCSka9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHRLOq9DdZVFujRDDV4byBc0Rae35xVwVxS5Pu6i5cbf9iH8PqHsPbbT6U3UnzSOhv9d2NuMQva5eF1ahCxu72P3kvtZPxamoloFhmGuoO9AAGJZR0T__QZ78avFsb63HRzmU_nxduxwxnjV2oe1_KEVymRTSGeocmjAka_FgQbxhGrpRPrWbSS0FueLEd-Dax8of1sqvBSCZfcwZ1-h4mV1c1v7hGxJY3KvrucQEvwSEMdx2mdc0YzRgIw3wwjSCt0j0AxZa1-4HAfPUswdVWyW9ZSwI1zj4a7TGkMrkntES80dzao9G6pykiJO18TrWUfrLfm_y0cBhl1F-8ApJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از نشست خبری سرمربی تیم ملی و سعید عزت‌اللهی پیش از دیدار برابر بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/443582" target="_blank">📅 06:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba068e9606.mp4?token=O-0zEDTqwj9Pis4bOSPkGJia1a_KFI9SMQtN5STteM52fDCMwzfmmxF_Zyx3-C_O8ZceYhb_gxnfFRksHNvm2rB6Q6V7hxRJRTNPNYirt95JjEK-nXFPNlyk30kFGNDTOR-S1bqh_DoWlviJAfIXen0jchrvDg_GiATNRxlyJGxe8BYm4HMOo7cDJob4fwxAqrY3rhtrNOw1ncIHqKH2A4_RZE6lVWsO08xOADz1EKjKPI3IVTzcwIFJsC7c-5K1ou9Ko2nTAducuPiiJtSYb7YJ2I1YSfB1Tv9tQVc4Q4r77sFFOqJtFjqnkRP3tcuVIc-9ZM3kLU34w9P0s5H2Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba068e9606.mp4?token=O-0zEDTqwj9Pis4bOSPkGJia1a_KFI9SMQtN5STteM52fDCMwzfmmxF_Zyx3-C_O8ZceYhb_gxnfFRksHNvm2rB6Q6V7hxRJRTNPNYirt95JjEK-nXFPNlyk30kFGNDTOR-S1bqh_DoWlviJAfIXen0jchrvDg_GiATNRxlyJGxe8BYm4HMOo7cDJob4fwxAqrY3rhtrNOw1ncIHqKH2A4_RZE6lVWsO08xOADz1EKjKPI3IVTzcwIFJsC7c-5K1ou9Ko2nTAducuPiiJtSYb7YJ2I1YSfB1Tv9tQVc4Q4r77sFFOqJtFjqnkRP3tcuVIc-9ZM3kLU34w9P0s5H2Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حقیقت
نوری چشم گریان برای سیدالشهدا(ع)
چیست؟
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/443581" target="_blank">📅 05:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سرمربی بلژیک: ایران تیمی محکم است و تا آخر دست از تلاش نمی‌کشد
⚽️
گارسیا در کنفرانس خبری قبل از دیدار با ایران: ایران تیمی محکم است و روی ضربات ایستگاهی خطرناک عمل می‌کند. آن‌ها چند بازیکن دارند که ما به خوبی می‌شناسیم.
⚽️
ایران تیمی است که زیاد می‌دود و تا آخر دست از تلاش نمی‌کشد. آن‌ها رامین رضاییان را هم در اختیار دارند، بازیکنی که می‌تواند خطر زیادی ایجاد کند.
⚽️
ما با صددرصد کیفیت‌مان بازی کنیم. در آن صورت شانس بسیار بیشتری برای گرفتن ۳ امتیاز خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/443579" target="_blank">📅 04:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تکثیر یوز آسیایی در محیط محصور؛ آیا راه را اشتباه رفتیم؟
🔹
از آغاز پروژۀ تکثیر یوزپلنگ در اسارت یا همان جدا کردن یوزها از طبیعت و انتقالشان به محوطه‌هایی محصور حدود ۱۰ سال می‌گذرد، اما در تمام این مدت تنها سه توله یوز در سال ۱۴۰۱ متولد شدند که در نهایت هر…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/443578" target="_blank">📅 04:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جولان آزادانۀ نظامیان اسرائیلی در جنوب سوریه
🔹
منابع محلی در جنوب سوریه خبر دادند که تعدادی از نظامیان اسرائیلی وارد خاک سوریه شده و با خودروهای خود میان دو شهرک «عابدین» و «معریه» در منطقۀ حوض‌یرموک، اقدام به گشت‌زنی کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/443577" target="_blank">📅 03:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1Hi2TkaCEk5VENbDEbI9_QuPZwEzdvpRaAJjyvTRyHaIkpuweoDElb5CvCc_dQzl1qGXmYE5Y_2NIwhBMlFj_RsqEvubRgxOqfbXg4V9LNljULqQ6CC1ve49edkRTZJYdpcQAlTC5tuNgrFVbnurAr6WS3EponuRFW-wBLdRtNUpH05LBc_dXZN_A8ERA9ndz-BLfFPFkRHhk15gCcfXj_OMBIbSd6wKIVn7IuaR_fK2IujxEMoROx8we47dwIrnXFP85f_fwBJ_-FeU4rZP4vPpgSSKYka5WbL9DA_PG-1kf6upAf0rW8BPFaA5UHPtqPE1JYkdMZQYr6mO-CVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhJ-wf5qfLOsGa5Y016LGiZW1wFqAjJY1Xj5yUCJTA13KlIF_Hlz6cr4zFb7M_IegNiTUZnHj1rnCMpB5uZBAHlObmTZExSMdZzR7pp6l61NeyDLKQejwfnmgRSLjssMSYoN1ag6_zSxzfb-qid5XLQp8NoK8b9AgchemDN_bROKAJHGpMLYGtYBp_v9hjijtN0FOvsPjq2QKj6u--U-J4sAjXRZbIJKaAz9U-5Fnjhs_q6iI3aq2EPTvxadT7krrC9_Uc5BXwPqvGGSqiIfvw0tTazfINq7LtXP_JabiTVpj75l1-KtfC5XxEnAv8Os-NQR7HuwpTG04CuQFJcA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AA8ifoY7unJ_jlCzSa1-RK0MpzuzzNdSwJ34gvFD3g_HIy357z6iIWmyj0OycEFWqurlpJN7U6QWfQtPEOizxJFoa1XSoLHEjFOwr996D94ibdmZT7VNJ7umSwu5rV1oo-fY5_VzvFQxextefavcxAFTkmgfPmsxslIxCexdsT9YZS8hWM-HOmOKj1XBgRxwBL9XbaOwObN8qqyqX995hI1Zkm4nZm6P_HWXL8fRViQdrJisN-26oyil8BadEkCDIaNY07UEwn04_1DqjToq4ZeYTdeqg6DurItdzKriUR5IZ6Fm28VQXgdjXRO2HPU39Z5g2VB2a6BYGeJOUyBlxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2iDWgrO6VoC4CZ6DgA0SgyjPQF2vUDbWxIX45BAO3iRuO4p5Ej71Q9tw5wfzgYKhY3bFAzKiUV8EFveHJszDHiZgjGQIT0tau9IkYd-bM6JylITa8na84ZtmLlhPX5hohscO4cjRaBvaBDnx8AaUMUhZp7kXMsghFa6c7lRvhrt_E62rHmP3hQq9tdv6NU9S_DGz4oGI170yhUl_RCmZomWMbY0AKnVCL3R5Y7ldOuIT8BQ3WfiKT1kqO9GR2THA8uj-3cZABs0I610ilBLc5WrvU-Q6C0BANgSntA916ZSrvamBA0Y0lCwKFZnZwxN1jxQ2soVO58IhcH1MPXpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpUhABHQDILqm4UfPirljC_UZNRVmI5gkfiovHYh0mRieWODjU3es9Pn-YDH9K9o_RCVAQPBrBxlaXwcFk8gN7nI26h1UTCkJLeiiV6fN6gpdrbk_erakIqUg9M-0brng54qWjjYaXLQoz8Sa2LUX6uFDvm1VA6cm3Y0JkyrhzZ1e3k7y0X6UFNMc6aYvv1tdpO499jsOKtVjRYpFckCkuMw3dsGyrXI8ZD226opFZdNfTXVz8S_XNc7xt8Jv1WTXXk0Y4j9Bgzl3J-CIf3fK4koZNvP6q0g27StqaUmMj2lGg7W7dCrR2wf7lmabo0ENKaSqM9Df3yVU_bvlTfUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwcQE6cTwZqe1Niv8X9qW1FwJWpX-XxsiNWP1XSWFpsnGYcfhriK2BH4ONUMGz3mT6ucsN9JYgLUxBObKAlCJ3sZL9iVrob3PJi3Kw6BUCdsyKTl9pThAjXIXu0ph1_N02mUOiAiMFdn6oe7EQOY68cr_7_iPa7wZG5C_0VhW1TviagyxGqAF8_1VecBawzveKUT-1U5oPbe8QunYNDGHVqk47dpJRNYYIG4zDCrDxTTL5WVwmWKf3SFYAav4zgx6jpavhVJ-U1QoJtYEdi3ZszZryXVPnddKAaQek1WgO1mBrN2keecatDHWKFlh6LiwR1PvTOax-3RKQIwTAxSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prNBboXj8tODgFS2rj4AIKf1HizZQagg36LCuxq_OX-AS_1q1b4jqu3lt9LYUgv9zAhi9QCOZw1lOGgY32bcZqgoabMPi5j_cg4dhSOYc95b__vAd1czUdwNb7Ctng0DkfYq-xnYpwAK8pJCILpR18pKPTFv4KmZSdtAEz96QHtXgPsChuT0Q_sgMt_tlI2eeEjQ_NlpjbooSjWBz76lBDFhSp225qvZAxRMmbcrAvyEcN-HtiIHEidMT54UGAiDUhZI01_D4EdtN6SnIHDcBAPnS6pgFiSkcHCYhPO09wBbMVq19FdilZ-a0v3AfjjvswQbqIrqYICc2xPa2A1_Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هیئت در میدانِ خیابان
◾️
با فرارسیدن ماه محرم، هیئت مکتب‌الشهداء اردبیل میدان را خالی نکرد و مکان برگزاری مراسم امسال خود را به خیابان تغییر داد.
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/443569" target="_blank">📅 03:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نروژ ترمز ورود هوش مصنوعی به مدارس را کشید
🔹
دولت نروژ اعلام کرد که از آغاز سال تحصیلی جدید، دانش‌آموزان ۶ تا ۱۳ ساله به‌طور کلی اجازۀ استفاده از ابزارهای هوش مصنوعی مولد را در مدارس نخواهند داشت.
🔹
دانش‌آموزان مقطع راهنمایی نیز تنها تحت نظارت معلمان مجاز به استفادۀ محدود از ابزارهای هوش مصنوعی خواهند بود.
🔹
این تصمیم در راستای نگرانی‌ها دربارۀ تأثیر منفی این فناوری بر مهارت‌های پایۀ یادگیری گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/443568" target="_blank">📅 02:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzYXuCNnXsJV1OEPGltYUERfCyf0WUYsfAOKRWapaIc2gAneKhtxTxEyWuYlSc3g7pwS_k2UY7qLhvxlMzY--vUiZo_g_8BxTBmPxuJwj70-XYSm4m_x90JHXAnhYoucipQqgU-PXd9Uc6LX8cU5IKUkTFS2hcLxj-2pfD428fEdOz8_Wa9t9VsIHVYgLzPygGILZ4PCrX7C0fhHzczcAWcJgV_UdgPaGAbNF7iLxfbw1vWM_FLtRmHBSR3uVlHQFH7M-lppL084uoN_7dLyD8DNr2YFayeWyJlWanBoWbFBRp__1GZREBHUE1PmCiIW0iLqLIlo1tmIhvJb_iNqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع انگلیسی: نخست‌وزیر به ته‌خط رسیده و استعفا می‌دهد
🔹
روزنامۀ آبزرور در گزارشی مدعی شده  که کی‌یر استارمر، نخست‌وزیر انگلیس احتمالاً روز دوشنبۀ آینده استعفای خود را اعلام کرده و همزمان برنامه‌ای برای انتقال آرام قدرت ارائه خواهد کرد.
🔹
استارمر که در ژوئیه ۲۰۲۴ نخست‌وزیر انگلیس شده بود، در ماه‌های اخیر با بحران‌های سیاسی متعددی مواجه بود.
🔹
احتمال کناره‌گیری استارمر در حالی است که بیش از ۲۰ وزیر و مقام دولتی از زمان آغاز کار دولت استارمر استعفا کرده‌اند که تعداد زیادی از آن‌ها در ماه‌های اخیر بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/443567" target="_blank">📅 02:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf2-izGxDmWVFKP6q0iXyAeMc7HfR5AstIY_t29YoT2oiyhwWLk5imbNpT_Z9uBtjKdGcForJtJWABCGy7MdFLhxmPcz3kTcKxPTi2WcjMUIA8rxiGipfLCIow9dzDMZWpB7qYqplDmPSsgRsUEUU4ibfrQHysVjdK18YaNpXebI2NkvFjYjwB2Ol6V--fnt1BKm7aqe-K8IV7k6rjwYoxLg1iYxTMzXJrxaWY9MBEnWElhHqjD9IOajgjLWva8DtM7QIVn1cQ4e9DouoZxeV0nMj2NjgUX9mbQcE0SOTLFQyqpJXjhh6lGZeBPzQsMgTUPUdGRP588GQtLhlYnszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی صهیونیست در لبنان
🔹
یک نظامی ارتش اشغالگر که روز جمعه در پی انهدام تانک مرکاوا در جنوب لبنان به‌شدت زخمی شده بود، به هلاکت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/443566" target="_blank">📅 02:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
روایت همسر و مادر شهید ۱۱ سالۀ جنگ رمضان از تنها اثر باقی‌مانده از فرزند شهیدش، در حسینیۀ معلی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443565" target="_blank">📅 02:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlAKGH2KRcC7hDf9xF_dWJs0SXdM3yvUfk7sV9tLxekor0m6FjaN3WDqbtEbkbDZIJ3isvRUE_qO8x7E-rF8J3LmzRBrzdfj9Hy72wr-Nz5ygfJFxtZeRd27lEvqVSWY8XIXwhg5JsBgf0RgEWiGjSV9pTxL2srxuo7Io492aenWVqn9YO2CYsWS_eVWk6COli0PB7nPjOvkl1NUvvihGr6N1acsQt20YzwRnc7H3Zmtc5lDVgXFMde7g3GvP_YXoC-CDYJ6S4CaFlnXISAr7WLaIanBtuDGUgbCdL5aPqIqIY-xs1EQ-FVWI_Yuwm0_vCEPL_EQ5UUgZcCWB7Wl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔼
آلمان سومین تیم صعود کرده به مرحله حذفی جام جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443564" target="_blank">📅 01:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
خروش حماسی مردم اصفهان در حمایت از لبنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443563" target="_blank">📅 01:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پرواز فرودگاه‌های بوشهر و عسلویه دوباره برقرار می‌شود
🔹
مدیرکل فرودگاه‌های استان بوشهر از بازگشایی فرودگاه‌های بوشهر و عسلویه خبر داد و اعلام کرد پروازها در این دو فرودگاه از هفته جاری از سر گرفته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443562" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443561">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6715af8f.mp4?token=IcC6xVssylx1SdpoEikbpr-8Uu38eW3ZZv9AZ5JDMHGYJudtuoF6b4leTj_ltPOg7qeAZAI3z_utioAer1tJCg6ZhdwDS9ZL_HgjCcukrSbc2vvWc6UYIhede2ikI2EUYtfiptUdoukCNNL2G36BM76QT2L9FdT1XXnWHNX5YAJOj89RJp-IcutXbtMCMaL1V0he9y5GKW_-NLBkn3vakTOp9hOwm5WoWttLPOg06dn8u9F4JqQ9RLrFwtfL5B3hhvS4uWJBPPKZC9TLcCqYaFNljG4iOaitOtuFNkIZ61t8Mz-RA9FkzmGYE1U-SU_KutgtopCTr9aqGHulDCleMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6715af8f.mp4?token=IcC6xVssylx1SdpoEikbpr-8Uu38eW3ZZv9AZ5JDMHGYJudtuoF6b4leTj_ltPOg7qeAZAI3z_utioAer1tJCg6ZhdwDS9ZL_HgjCcukrSbc2vvWc6UYIhede2ikI2EUYtfiptUdoukCNNL2G36BM76QT2L9FdT1XXnWHNX5YAJOj89RJp-IcutXbtMCMaL1V0he9y5GKW_-NLBkn3vakTOp9hOwm5WoWttLPOg06dn8u9F4JqQ9RLrFwtfL5B3hhvS4uWJBPPKZC9TLcCqYaFNljG4iOaitOtuFNkIZ61t8Mz-RA9FkzmGYE1U-SU_KutgtopCTr9aqGHulDCleMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آلمان در دقایق پایانی ورق بازی را برگرداند
⚽️
آلمان ۲ - ۱ ساحل‌عاج
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443561" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443560">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e776df89.mp4?token=swJVJPM46AQVPJEakJ1SuXWHF0VALbcvzIZI8ERYQejuz1H9eTr5oOfmv34kxTyb3QBxqUXWdXMfD72dUx30ZkY_knginqWhpsc9MpJ4N918nY_MTJWGFYaKf8nkjzdxbDRNlczBIouUmKSSy2pCLSAb5fkTcH4ESyWzs84dDoTvg_iQN0gJHKZyQF398LcfNWzOYNYu5js7kGiWyKctCRm3rYtZscy4sEoYWNzWMS0Qs2RPcdbRxbTovN6GiUo5KzzYdmOVglZCWzIAZiRqDRP3UpoTPvnuLrVy1oII-GiLqC2ROZ6BapQXDxjirEML-CT1No13wLnaOXymnvMS4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e776df89.mp4?token=swJVJPM46AQVPJEakJ1SuXWHF0VALbcvzIZI8ERYQejuz1H9eTr5oOfmv34kxTyb3QBxqUXWdXMfD72dUx30ZkY_knginqWhpsc9MpJ4N918nY_MTJWGFYaKf8nkjzdxbDRNlczBIouUmKSSy2pCLSAb5fkTcH4ESyWzs84dDoTvg_iQN0gJHKZyQF398LcfNWzOYNYu5js7kGiWyKctCRm3rYtZscy4sEoYWNzWMS0Qs2RPcdbRxbTovN6GiUo5KzzYdmOVglZCWzIAZiRqDRP3UpoTPvnuLrVy1oII-GiLqC2ROZ6BapQXDxjirEML-CT1No13wLnaOXymnvMS4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان:  مقاومت به هیچ‌وجه آزادی عمل دشمن را نمی‌پذیرد
.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443560" target="_blank">📅 01:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443559">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32977d533.mp4?token=R01nrGZknjWoi5VF-qJfxBKiR0NtuEWHNKAXKr2Sz7c1fOB_I7x9nEpFBaM8wBjuQ6NVy1uW7YrP0KsPY-bhQ7Epjr4nXbVy-c3IAcGQgb_-gLZhUsx9jPn52AbisCF1zM6EnOIeMfUcZ0BU5AiwKgk04RLgx3pGTPrSXu8ca_WcrcCN3l2sULovBF4lAOpEVdxVzR-p0FiWBzuiNogdRrZxliYM3vLDnhCWDP1wRmSoUzKINgYbxvoAA84yYOyQxxt-yWBw2-i9_2O9gs_c4XPxWJjV_36dksEwZTjfJSoErGQsYFG-0zyJIHgAqYos08mTabhuH4u2bwxEXhPcQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32977d533.mp4?token=R01nrGZknjWoi5VF-qJfxBKiR0NtuEWHNKAXKr2Sz7c1fOB_I7x9nEpFBaM8wBjuQ6NVy1uW7YrP0KsPY-bhQ7Epjr4nXbVy-c3IAcGQgb_-gLZhUsx9jPn52AbisCF1zM6EnOIeMfUcZ0BU5AiwKgk04RLgx3pGTPrSXu8ca_WcrcCN3l2sULovBF4lAOpEVdxVzR-p0FiWBzuiNogdRrZxliYM3vLDnhCWDP1wRmSoUzKINgYbxvoAA84yYOyQxxt-yWBw2-i9_2O9gs_c4XPxWJjV_36dksEwZTjfJSoErGQsYFG-0zyJIHgAqYos08mTabhuH4u2bwxEXhPcQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی رژیم‌صهیونسیتی متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443559" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsXUrIL_Z5Z-YrcMLHEQV2esjNiuO56xCLF3oiV2hVsV9uHNRKEVPpPL6wsLbSIEcEQYMQ8U3SCRnJQIn-t4Bg4V1wt3QaxTdz4kZo913GmEdCUM4FXVdrTVCXJsNzMFB_VquNOOOQGi6Ap2_KjEIKyCqJ6raiHaNB9xLc7nxRFHO86eLpfcEqqF2XRSNEJqanavr59nysv1uwmtUuP2RvKDZnwq8FpWh8eYN7ndH6ssF8cTeFO3me_My28EsRnh3Wcg5c-R7k9lamq9kaSpO0NK2ZOE56Zua0N36EbuAV6V2nNCQ0pPnD3v31Qqc4h5Edo8hMWhcbh4p-g0upcYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JI9LYwVc6MlSUmU_xk7CPSgO2RDIR5_-xlyhpDguwU1JYwhHIqQk2LEr3OtUCM6yRkX-AHgAxHdVfFUV1ssda0Oig318cOBu8VLcRTw094_vr3YKtUIK81vxg9k7_-A3DBnO6VnPrAAQNY0czP5h4hR8Gbyq7-eD8zWkt81G2FHMS_Hj4cEjn8R_7aAnM3llaprf4r9IzQ1lUntiaZxHtgk-EW4vEZHhlkAOy0ywZuCpG-9WyZBGftXect0dqCvfuL03W6R42L4uRnoMQtdrcT3H_tua8cyRoew6B9za-vAtmIOTCx-8MRP1UOc8cUq9r27n_Dyusz6N3tNQ2tJ2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN7L9yeAbRXFjoDPeLvZ0wbsuCtswGBNCZ0HvfF8EQZvGRo4TeAfrOrQ8Ox4XbBOEHVjU_N641wb2Ua1g7xqNtemP1iDRgcYX--fb-rF-QkFR9FkCzj8wn4NVMP9Tw44ig2goH1dy75iVzvYSPe2yFjRfB0G3JwA7dx8zm48R1UA_OaWX-VC2YDBmu7UojGfe-fMMbKtee4n_8frqMqJleUFqPi1fh5rUwyNjQ79vuSI3h-GysglWD-9ALRM6FWSEot09W2LwI4vWS3yg_-Raupxu-BStiFlKVJj4yOnb0NKiE4oO0pNotNQ5zSqYrE9iZoSkVn47aJZZyKVFm6XnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDg86L-GuDtij1Cjm4iE8MyOhKfqb6cTShmlgnSoedZYYB8xNeLyc2bj5rUYx90aLj4nEbocTMRluZQj1VFqCp2Q9gsCoXnkSyMMYbMuTd4wQH4J38boTniLlEcJhJoZdxtDC4ocqQSlgVT71E7cI1MtkRkBK7_x_oROfYcvCoLKqNKBamLd0DgeGMW3WCQyHZttoDeuvRok1gZZCHBKU-mDjqhZ245qf7qoudbF0fDM5xE2tqwZKIFi73h0kvIItN-SCaI25MsfSST3tl3cxz7U1slHZ9WHyHMlGhLsQld8om2Kk7IVs6kw-dAc7sdc4aL2i1bHNmp0RxV_hYkCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAtY0e9XVs5kzF1r9mxx7qkZCLlR4cqUllB6M7Wrwaxxe2qKkTmdr6qFbl79etE3t00mowkyz-2Efz_4LPoBxGp2APVRH9CmtBojwZGvq0NnIGfGUkeM0aKFtwyYJjvzZf-n0eX_1EgT9UdkihwXKoE__5a66V1uAg7aG79XpfW7rfKC4yJS9kBT2TFWD915xgUJKMaHixN_CYMwJjuRir-bZRLfdNdVZmYaXhlW5OfCXCjmJIeakx5DaCl3Vxk9KR8H0wJ1pdGw05krwyNkBGz1QIU3e3dFxqStapo_IQ6QY_QdP2N5_wi6kYpISzBfNW0WYSgYc03Mh9L4dic62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQKAJ4T3CpuT6j0VOhr69J5rZEnw-6DX9z-yjD4xCw6uYc52rl5Cq34N4jQo9CeQPENb9_BfDR6o2N0-k3EUSJ2FTRLUc_laTnmwwpDNQxnwe2txt2CDwfOy51uFPjBhbV4nL9zVkElcIYKRl49IzbWHNz1qv5Ga9Lx8YFnY5H3rdvekAf_CD2FBJKbRxBbJrLOdXZXmSnVUaex1D-svWaPaTbKFEl4NGG8ZYDNsAIhjbCaT2XV0DX0LmFQygjlXEzSW-SZvb9VvO7TypbLzTcY4ythDlg_6iZS12dDy2KRxP5gOQIyOsf53ZeYTvy83X7aaBLm4pfJ_akviPITj5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3RWfjQOib_Z4rsGfX6MeuI_D-ziw46fFcrE87O7YOL1J79BFUKACW1oRrXZ6_4WHTvS2l2cbrPKFMm0t4Otd5iqIJ5Mx-rMD2I23307ntRSf9vd35bBCkI63L9CXtMeQfp5jptonihT8MsQd78h1dm1ezXTPrRmJA0vmQQTe0HmboQ9s4568WKpd1TQi7aHqjER38S5eQwDJ1QESBn-qVbHyNi7R27Ggf86PehGBcftmOP5_I2nHQFC2_VgyeXRKJt5Ctrj7Ms9YPctsrVCGJgXDK3pBCy9sjTg_F7g78oGrbrQYqMUuS2-vpLRZkpfTtfnM0BlDA9EMScbObqlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbHriWPs9p9wCH4kgm_4kWRH8pyxyLCy-l_B9_6urg4Gqxa4p3QqFLNGJ0yZNvCSOODVGgTLAqxNtmg4TT9PhMCFdy0F6sPR5MWjrRzMsmKRmbjHsDosdUZ4pIW-W2wq7uts5Np92F2fXqo-qwJl62rG9CkTAV8EpWXXJ8o66c1qGnFY-CyVs4leuFx_aSW-sETrp3-HzOocnGeIPUkCPgaoX1EWvHXyfuhEfw-4MG_gRqv9zJfu9v11o0AMTyCyl0eP8gRhHPS3CbvWQaNvPtJkNFVYryu5hz_QmSrzHUAJfaZU4MBN37JakO3SShKzEepyxqBiPW840pox6hcKzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
هیئت جمهوری اسلامی ایران وارد سوئیس شد
🔹
هیئت جمهوری اسلامی ایران به ریاست محمدباقر قالیباف، با نام «میناب ۱۶۸» وارد زوریخ سوئیس شد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443551" target="_blank">📅 01:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6fd72073f.mp4?token=ua1gNcFgzsvT-w_zqSh9Dyt52LffsvPXo5f6VhJxFiiCz1sWQfTftWou3Yt9jCocpuRYlBEDrRHVOeRZWJ8v_yepUNelCrAt9SyMgWrn789eGx9tAAFYRaaMX-1Cih30VZhDaZ_t-PKLPxLmpzHB15Vg5KfN94RXTUi5fA-HKwT3zFav8NOgDLqw3_7OBMwB4tEw2bADkH_WdPF36fbo8lqNvfCBtOVhZMI_a__jQBMYxCscPWQhirWE3jPoecJ1BfTBWvmjHPRf-QyQ0T21LmxY9oALuxpS9WYqPu6M6pGVrX5s543vVGqWc3NDLDx8gfW1x9OADy3JkShz9cWisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6fd72073f.mp4?token=ua1gNcFgzsvT-w_zqSh9Dyt52LffsvPXo5f6VhJxFiiCz1sWQfTftWou3Yt9jCocpuRYlBEDrRHVOeRZWJ8v_yepUNelCrAt9SyMgWrn789eGx9tAAFYRaaMX-1Cih30VZhDaZ_t-PKLPxLmpzHB15Vg5KfN94RXTUi5fA-HKwT3zFav8NOgDLqw3_7OBMwB4tEw2bADkH_WdPF36fbo8lqNvfCBtOVhZMI_a__jQBMYxCscPWQhirWE3jPoecJ1BfTBWvmjHPRf-QyQ0T21LmxY9oALuxpS9WYqPu6M6pGVrX5s543vVGqWc3NDLDx8gfW1x9OADy3JkShz9cWisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار مستقر در لبنان: رژیم‌صهیونسیتی پس از آغاز تفاهم میان ایران و امریکا، بیش از ۳۰۰ بمباران در لبنان انجام داده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443550" target="_blank">📅 01:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516f3b1f5.mp4?token=AqNB0D1KXy6EIsTk76YCZSF3zGKoScfyiiVLErqGVvACn7kMj1MxOzxZV53jiyLttapEnvC_eGq1XRNBzeRZ5sl6PWu98Trb9_GvE-Tp44t5VtCRfoO2MM9flWERnenFq_UJ-6U4e3mD8mTFK3P8PrphoVtC1YBqNsQgurgDj_uuHi7wv1UAvZIbvgBdjh1G7zYRXHzm215gFTgXVmGoyIjmV659HdxhSfrU_ej7Mz0XDtFK7cVZvazIEkgJR-6qBoBUjtE-B_T3dxJxUrzVYzwvtR_yIboOinjXQxEhUBp1hpjvFLd68rNxQZ1uAnUmBr5tuHkiqmvzwGddbJDklg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516f3b1f5.mp4?token=AqNB0D1KXy6EIsTk76YCZSF3zGKoScfyiiVLErqGVvACn7kMj1MxOzxZV53jiyLttapEnvC_eGq1XRNBzeRZ5sl6PWu98Trb9_GvE-Tp44t5VtCRfoO2MM9flWERnenFq_UJ-6U4e3mD8mTFK3P8PrphoVtC1YBqNsQgurgDj_uuHi7wv1UAvZIbvgBdjh1G7zYRXHzm215gFTgXVmGoyIjmV659HdxhSfrU_ej7Mz0XDtFK7cVZvazIEkgJR-6qBoBUjtE-B_T3dxJxUrzVYzwvtR_yIboOinjXQxEhUBp1hpjvFLd68rNxQZ1uAnUmBr5tuHkiqmvzwGddbJDklg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم استقلال در دست تماشاگر بازی آلمان و ساحل‌عاج
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443549" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWsqjl7x1_pBPXdKA6MAYqiQPWi1gyd83lvazNukmkotFak0WxoF2tKs-n0zGdkcot30tuN52vSpEKYQJjtFaHLWN1DxYYLIlINnZAW9ZFqRSXbK_4T8yeKBG0EfZLHU9bQeKe1pcnxU9kAzbMES-Sr_FwfvCKNm-JpAj-RfjQ1GUS7dduMXjxe341iqxGKega_EcxIHpose4fr4zEa_5FGOXNl2ORgX2PhXqJc9BvjoGMcbLw1sJZEfxEifXIrVn90IJqbCH4_9OX_7rlhzWwL3jM44VNDu-Ya95mGRDUp9TlTVI78A-tBQ6XbRrHSwK9r560fcaZWvymIK4ZgX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در بدو ورود به سوئیس: کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم
🔹
خدا کند که شرمنده شهدای مظلوم و ملت ایران نباشم و روسفید به یارانم بپیوندم که برای دیدنشان لحظه‌شماری می‌کنم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/443548" target="_blank">📅 00:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb841c156.mov?token=s_GUaFDXWAtncimaoqqvSy-PG9kSMHIs3xOtgc1RPnmWLTd4fxprzSybVAg65aXaOxpTR4G29HFYM0FPmK0Alf5TdiRLQlMET1sopMlfCNgtU3BC-JeyGEJ30j1o-kwgiFV8ls1meDGmpAB1Kqyd7ibEzRnTi_R3wsrxhsOhYBB-o-FfXrkQn0Zq233xfDLYJ2k8yZTNerDeSPmgfLXwqnSw1Jrzt25oqjouAE2SjEcFWJAKy7RJzRIhtsfMPCRPqRBHFpxjTOnwoC1-vGhaXRKGLGzUMHMbmictO6bT0xrkkIYN5uxXzl1n-z4S0rz4-9gD2qDLlfvYLB9_SShOjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb841c156.mov?token=s_GUaFDXWAtncimaoqqvSy-PG9kSMHIs3xOtgc1RPnmWLTd4fxprzSybVAg65aXaOxpTR4G29HFYM0FPmK0Alf5TdiRLQlMET1sopMlfCNgtU3BC-JeyGEJ30j1o-kwgiFV8ls1meDGmpAB1Kqyd7ibEzRnTi_R3wsrxhsOhYBB-o-FfXrkQn0Zq233xfDLYJ2k8yZTNerDeSPmgfLXwqnSw1Jrzt25oqjouAE2SjEcFWJAKy7RJzRIhtsfMPCRPqRBHFpxjTOnwoC1-vGhaXRKGLGzUMHMbmictO6bT0xrkkIYN5uxXzl1n-z4S0rz4-9gD2qDLlfvYLB9_SShOjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیئت جمهوری اسلامی ایران وارد سوئیس شد
🔹
هیئت جمهوری اسلامی ایران به ریاست محمدباقر قالیباف، با نام «میناب ۱۶۸» وارد زوریخ سوئیس شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443547" target="_blank">📅 00:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443541">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWMM4Pu5xW5eaIKHve8mWw6JcygVnzDvRSMQ0wfYPyGxhWZa0yI1NjQOTdH5JyPQo7o71WkLxb_6q7xn5PTcD8fExX2skisc3asKZURCLyS02GeepcLhRLog8TQGIydeFiFT7KnBDVT6xfo0SObRYJ797W01gGEdplzio65Z6NTogzWGxg99QAgSnOsuc8VV27PJHjZl_FWcd5BGZQkAd1Uoa97z0vHqhZ2DTy-Zn3Mg3BqnNfoK2omBLAIGtPyLKCpeNkJlNVzU-xComd7S0s1mFLHZ-VtfH1tj6NRIEAAd8BRemzX8Q2RpoSwAERbaNIcRwTrNuYWxVjY1CC-sZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gg9U9_jH_6jc0HB_K9HKIoEvXmfv1eLnxLpk9gEydyHc1aWtOXIWduSDawXJE-zrEO1l5KKbLClAwNeM6JMRzgw_96pAgzU7kUvvE7B4kiQ6pOer-jDQEFnFYQT1JhvWp5lEG-cSCb-CLqxdazt4pDhJWw7W3w_gkduap8dWpj3MlKcKOCfaA5jjqJLQnHcgasGECx51CsXfJgNxulgstIwC277Pil1AACLcW2MFzgr9D7U7XW43lYZbKSknU9wEEvwkmeEVY9MdlDQSq9LuNRys10qY6yaaYHgPqiOGjlopSFZ8zm9QSIsQnvgQqzCQKs_FZlYMhVI-7bPElsUQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NV1srO-gm1FCqVEjZJGeXym8TIUNk6ex3Nc8GOylDq33zTswE5xrFR9P2zGNbT_tnDcw9vci_1lZixcW4PRFJBP1MhfheUo9xkmn4wqFIpJOmHFZTQSr1Uz4WtvM8xca3_IncCv2WTYIgklOHb97peTf6f2AvrZnDq3znRrdU3V3nGuuMppwGUEXunSIr6-UoeZwyrkPm0k975CFnBpVnUc7bUV3dx7zurSFDIRyKCy3DI2zUeqdGJLVpS9JYaDSiT4cIXOYnao5LepUoy27PmeoLA3SRZVQ_XKCg5DbX5S89b2LTAZeWjQdeHQreiDCiAzZnNWD7U9hhSYkxcQ3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1iLuV7EzdlIAkKAuUjUcNX48ZvP1X6Dt7in-e6u3qlG4qVlJX5d93S0QekOcJhGd5eJ514_MEnGCaJTJ3nf-Gm-IQAsFPRnS13hWbcRHBfTOLInYkQKIL9uhcAOhvQZInlRyh2oS1Wc26-dwBGv64GCAnNwmkM0PfqF7Oy9qWDt_efteoKJAcCenBSE5JOwj-brzv3uqzHAslFIN8S8Q88vbV4BBjaLnWJ7goM1HooTenuDXcu1XTMaMYK_-9tWUeu-L7Y0Yxdu_ARZujdghp3Iu4t2QTwVL9hWdxVy6_3zf1zPgJKpexOYyaTS4x1Z5D8dyCVSUGDG7k3pE9bQ4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۳۱ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443541" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCue_7Q13wF8imEzxZP9ViGuAP6SmWmdzBY7OtkTrEZxP1T30ajIYrISB4nPY9DSyfJrt2AKxmckkRa1Pv_guOoew-ATQEymZY3RzXK8q8Hyrhvf2kZyFmWbedN1uNiPMVlmMyYJYgQPW-V9UuVBmssYPIAzI6iY35B8nBVciyOKyqz3mqNPRKQVIHaJLhjcVjuO-pVbGqwVmhAXhPV6y3PZnxL8wzz1oU-8nKKTsdg8ieakzndk_n4Zt4vvsjOh1VyfjRly-uOBimpOUDU0LXfAdMHgcdesKpusqDJHRraBILN4Vt3AnQvvxucxu4ApRolYRnyNWTyLkKcQd1xx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4D-76P8SfpBddvQX7Jtu59Oc4CrfD_KWvcaAZ5tkNfPDtU0xwHLwjDGcaK4zQSMS1uuCQmLWaeC6HdhJv5KoYeMJvBWLkvf3Zh4op8vMxUC3v3yvCGoYLMC0ybQLvrZanTUbRQGt8H2dPXAB2I4YqWOXez8VapAe7Q74qu2AJGsV99ae8CCrviwoFuZEBPj5cX7TXoIuD7-yw7Y8NobStSONXUgYHM88MYdvbI2z1atRsdtDFC2p2pmAufp8QirCPXXxG-7xQfEDxHOmMpQLcn3f3O28C86nkfw1cfOeAIRMEp83FqAkGti0hRxJuYS5uo5aiLFJ-GItimj3jN_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNa28PJBiiRnz6MPLuObYYV_mMkuEPTr8-moFvrrd9WON-a-K6XCLT7opr2LxqJJMBjgyzUMWc4ajuM7OMpUlGZbjDWotgAqBFdeao5YIjdjJQ1zbhDSqx4thOeXrVv01oLajBms6YuhrMEamNsucAfkEnHE268eNsKMCTqsNUhwttzMdTlsOxd8oiBsQDpsiOBZO9Zj2UUwvFGQsJvgeGsjzWwU02tbB-iZN_vcvstNTFx6aYrluXkbOIGbqT9KjqvU6Bh6q4sO8pH4xkiyNCmmK5BH0jmyzkcfrBZ9K51kXMZoUS0Cfjes1u8IgO0uH3Zj9r2jntdpRloRDABQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LScTIVL2WvpXGYhUHPW68onq9Z_GaWHU_FtsSYWZGflxzhlv5-oTHUzw0isXflXBt1nLaRqacMLEbl-QwtB-1gXvBrB5WXIAR66fqS012_hH6sPrsBxpT_4W8r3HIqH-C9dgSngLxbdNHYEaArOa-mN4zKhV9VKj4wUud_yCx3qn28RnU0IvFRJ7HwZFy_FDaM4IrWMyjvKE9yAzuww63_KLxP-QmELlopcaCzab4sYKqJvzq4vz3AIowwVlTGPF-2siEhmbYDX7GbI5z5NFpFxnm_wJK6kU2txncZ11zmDCpRoQjXicKXk7cAYPnmROarKo9JwQhIpTuXgJNJEJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6z6RxBTEz3ZYZknTFl-VXDXTG0z7GbCLGShMxdxzQHN6BawR82CLcuWPlSagxtp6PlQ0pnEkMYdt1JlcXW2zBzHdghiRv3a501XWjRZh7Tm6neT8M_kaG6CVeHkBDiatNLPDokDKb1bS130eul5Wk3A4txh5Md0_VQEtfQtWnMEJf7vyPoGtup5jO1qZlaLu8fN8j1omm_O-gzjgrNNhskg-PbJiqPKQpYZgcD_p1l-UFK6v9K5qvJlhu77RE6YgsLMBVR_YVdcR8kWaWP2SrwtPhIqX05miJA4cLESwG_5KK0wB7DRjH7awA5bH959xp6vpyVmOJ_ZKifYGjlPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrGU5ugkm2QXcCh_ngXJ25-Ekv29hKALEoyOKs3xZHWCpskseTF805fO6zFIqsUtMVpjc0mou2QozggNYrGQV8AIMUBGmnKK80uCxYnRUQqogdhslwIpeA3Mn1l8zRdi9C-7fEMVkXxyCuEfQu3kS9KXFr6i6kK3i9wrr8KmZcimulY7GLTYX2UOrfrOS9SrQL3fYOXRvi4Avd5UxnY0PkFqmqCp3p4IZKDqWh-8igAtPI4YRPvddogkubqf_T14inOW2Bm5inH4btIyuf47gweM-dpk3gyNkM8rMCyLIC5Uo5Y70FC3fqeoUOdrT6ssXh5bFcUFTQHpjEs9RsJmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovC7fC_0SjfCzl9rCIOCcSfutAs5Zs5hkKJ2afBP81c9UjbYUC1JfDqpdsNlWSY70sDfakHy6cGjpHtUr_GSIUrOTNGswCDsLwH637gUAKBLKwJ0UesRIVvnBMuMYFZmRuL4YV5WQKkSmu5zWhVzmKxBSforW9CxfjNRfcuPajtLhrGJOxPFrDCwR8WvhhwYn0AdIM2R4t-NTyd8RpJ6e-JRviSP0H5Q1LG-ahL_zFA73eVhnDBaxa9vuJJuEtdCr4RdlMeKFVG15k8yBpRF_ctOdHC-SKwV2rOscnqcTxmeLc3bkyhYdc3sWxxxkcBdyGQFkVE5YsLHmrli_jsCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWpvBkVkDsRZRvUPCfq8OF2bSkXFfg70efeSQxIfSu65ur9BYA4NiFzcsTGaXENksLW0TRlF8tk44-mJwAoHEX_orShNUL5Dxy-XL4Wpu8Bat2p3v7ENTEkGYibTTjeSydJWn0CEzQyKleE3js0eNXi_Ghr-KcP5RhPOEBrLGdBd21YxfmAJwCo2birPe5tnp3dgPqNKx3g8CNW68CQWeaKta5mYbqeb47UhMDfMzX0HDwBPBlMC3YZcnu4OFKme9gHM0SLqMlONBiEl7p9CTRGKCnYAlcXu65C_5pt1roAuaUh6uuhoN0UVVtmKfVwItvImQL3JLahZSzRaFuq8MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lykJoKhosbXV4z0LAvzWMgQEZYksT_RqkhyLNZ0V39b5_COhqjUUabOeGJhHC9j2E2bQzl3thA65NWIjOu4Vm72N4sIt9G9P8TFs5BDHWvYYMAHD8JJ0fNjYr967ML-ACala8Y7wY3nr7HJ8HKarZhJ7n-Ed_BcE-Wb2s2KPZBN-rcgGTu6TW_IQ66A3-kZ6qtBlheeGyfRu2z0JyYgxkrJNU4_rmbO8EMC4nz2O3mGGCJq5pZvo7j8vC-MZh3ifZGl8QR1nvaW-dtDC8Yq9VC7iB34DVUDfU1bzVLqDguATUo03dv7JtCeDzl8IYydp8ZfYtjkJEnd0KER68uiySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdqUt4fluMFpxtV_6ZcAHi9DbElEpynETjMKmxVvGixVQwbPBEOuaZsYESrbuajOciuNhTRKkRlz_0iod4rQQveJ1ThmQOMlkRgceJBJTjWrnu7IYbqNRG4miVkhoo-Vme7d9nUPsc8_LXNEC2dKbz5gc23qhrZAyAiOFlwEn40Bu0w5Xka7_GtexlPSUF1w3zSjNserK7CM0YvYmWLuoq-3bO9ICS4PrnnCDlZmoKTKulGjr3SnLRuQN0Law2p-VdIGR_q_2MIKgCSK7obGggmV7J7ptp_eUJyfheO1VLMMACnCwW9fhtBL4CQE5GnzW4bH5jn4zEv0fHYOG-obFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443531" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443530">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۶</div>
</div>
<a href="https://t.me/farsna/443530" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۵ – کتاب آه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443530" target="_blank">📅 00:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443529">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c173f979.mp4?token=N7IGkvpkcYJXSZpQiUqV10G3006FUfJahpheH2LK3lx4bV6xxJwnQX6qPbHHZd4jp-oEE5vCvZ3u4MFdedk6opUSeuEheMKI7-kAZ5y4S2rWNo7vjpIgft644MG1G9T782iuqGgIvfqPKGqBGVp_f4sg8A1-Rfl36OZAH9dH9nJf0KiIuEnKfqhCVjLzi3NgD9QFxMPZXdO8ZX6-A8jRDq7DVcIVmfoOQ6DO_ood7OPCJV3k-nbaQFRl9M1as0Y0VcSAgDId79iScwIzoo_N_pEdiIkoFsHXiQ9zFZABPDfwT7cjFMkMEC1jAESPFpPd3wn2c_MtE87KBHm5A-Xvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c173f979.mp4?token=N7IGkvpkcYJXSZpQiUqV10G3006FUfJahpheH2LK3lx4bV6xxJwnQX6qPbHHZd4jp-oEE5vCvZ3u4MFdedk6opUSeuEheMKI7-kAZ5y4S2rWNo7vjpIgft644MG1G9T782iuqGgIvfqPKGqBGVp_f4sg8A1-Rfl36OZAH9dH9nJf0KiIuEnKfqhCVjLzi3NgD9QFxMPZXdO8ZX6-A8jRDq7DVcIVmfoOQ6DO_ood7OPCJV3k-nbaQFRl9M1as0Y0VcSAgDId79iScwIzoo_N_pEdiIkoFsHXiQ9zFZABPDfwT7cjFMkMEC1jAESPFpPd3wn2c_MtE87KBHm5A-Xvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان تیم ملی فوتبال به هتل محل اقامت خود در لس‌آنجلس رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443529" target="_blank">📅 00:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443528">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCFv7zJbsdPHDLpiyeqO_g13dNvVp6jn9IMNGjMVbIWW9Q_Mr2rREUdihpOb9kTzFXtR8g7H64HHiq-iPW2t4vybaYlMGWl8rv_-NSaPSE-NBXFEupaAal0QHifsr9gvRLLXGLyMnNVabVf7Bv28Jhpv7-dH7gPVX-m6os_9nmLYPBqk2bcLlbW0wDyC6al-Y3p4AU7kzewn4HvnBBIacd1Mo6KlXBHrE0R-WThLUbRUbKYYW9ggSf1HkDFqKJJLeRy2Y1hlu-jECoVlisC60uuFAQNv_LLhb_jwZL2J6NCFGnGs7S6hCmuiZYcATLxchH8_sQNYsLKh-nAFX1uSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با محبوب‌ترین فرد زندگی‌ات دشمنی نکن
🔹
شخصی به ابوذر، یار بزرگ پیامبر، نامه‌ای نوشت و از او خواست که نصیحتی کند تا راهنمای زندگی‌اش باشد.
🔹
ابوذر در پاسخ، نامه‌ای بسیار کوتاه و تک‌جمله‌ای به این مضمون نوشت: «به کسی که بیش از همه به او علاقه داری و محبوب‌ترینِ توست، بدی نکن.»
🔹
آن شخص با خواندن نامه دچار شگفتی و ابهام شد؛ چراکه به نظرش این حرف بدیهی بود. هیچ انسان عاقلی به کسی که دوستش دارد بدی نمی‌کند.
🔹
بنابراین دوباره به ابوذر نوشت: «مقصود شما چیست؟ مگر ممکن است کسی به محبوب‌ترین شخص خود بدی کند؟»
🔹
ابوذر در پاسخ نوشت: «محبوب‌ترین و نزدیک‌ترین فرد به تو، خودت هستی؛ جان و روح خودت است. بدان که هر زمان گناهی مرتکب می‌شوی و نافرمانی خدا را می‌کنی، در واقع داری به خودت بدی و ستم می‌کنی و خودت را به لبه پرتگاه می‌بری.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443528" target="_blank">📅 00:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12f13278.mp4?token=up9g1jOioBe6Jgr-i0ZHiyuqybuIRN6ekJFZQmcCBWfYYLJ9oaIgTR6w8AzcUO7gtesHPdgG-d8NUWF9Nd_95kBQcUqNOU6qkxjF08gyejKD2Nxrlp12zO_oLHswx72FSaeGl-mT_RETXeqlQlVXvmf5Y0z_kBRVZCSyI4aOBzTFeOqQ4QVFHRRYaPqbBfrfHo8XS8iDKvjOaSxpIfLhJ6cS6YHpDPuvnkask9__0l7VfzrUtJBcnZRFAfbR2CqSSKkcp39-EnaEphbIjAXd9-FmwEGMIMsZuyIBtvXqlwomhhwxMpropu-an03yoGELEeSgvPiyNP27eVwbk2QsJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12f13278.mp4?token=up9g1jOioBe6Jgr-i0ZHiyuqybuIRN6ekJFZQmcCBWfYYLJ9oaIgTR6w8AzcUO7gtesHPdgG-d8NUWF9Nd_95kBQcUqNOU6qkxjF08gyejKD2Nxrlp12zO_oLHswx72FSaeGl-mT_RETXeqlQlVXvmf5Y0z_kBRVZCSyI4aOBzTFeOqQ4QVFHRRYaPqbBfrfHo8XS8iDKvjOaSxpIfLhJ6cS6YHpDPuvnkask9__0l7VfzrUtJBcnZRFAfbR2CqSSKkcp39-EnaEphbIjAXd9-FmwEGMIMsZuyIBtvXqlwomhhwxMpropu-an03yoGELEeSgvPiyNP27eVwbk2QsJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم در شهرک قائم تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/443526" target="_blank">📅 23:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09468846a2.mp4?token=ACVfH58GeP3uDu3VkdC-csJKA-LrTeNaJ6BWwT1K0vPSmLHZ9zEGYC6R_7HJA2V3nPuhI2AwZJ7etSl0Wqc-kC8lrfMp3IN1phpt5KwCW5_4seNQBxblzyI6xiP07-cB1c1rPqVb0BbaqEhQJ3GQhjwqC4X6oDbyAPlKxK3NPOGNFXvuT7ypVfTC1p5GYje_atPpVAwPP9pF9H3frrFpwWsz2-OB9-cLUoRZA8tQfB0qQqgAGvd4CXY2_vD1hN_f8cRZhOjcopSy7XaD69NbcKTCwHTxgaMrKmIisiOSbOmnB6iI81BO_p6Fud0gTn2-LPUrcLW8O87yE5X25GsM3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09468846a2.mp4?token=ACVfH58GeP3uDu3VkdC-csJKA-LrTeNaJ6BWwT1K0vPSmLHZ9zEGYC6R_7HJA2V3nPuhI2AwZJ7etSl0Wqc-kC8lrfMp3IN1phpt5KwCW5_4seNQBxblzyI6xiP07-cB1c1rPqVb0BbaqEhQJ3GQhjwqC4X6oDbyAPlKxK3NPOGNFXvuT7ypVfTC1p5GYje_atPpVAwPP9pF9H3frrFpwWsz2-OB9-cLUoRZA8tQfB0qQqgAGvd4CXY2_vD1hN_f8cRZhOjcopSy7XaD69NbcKTCwHTxgaMrKmIisiOSbOmnB6iI81BO_p6Fud0gTn2-LPUrcLW8O87yE5X25GsM3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتماد به آمریکا بزرگ‌ترین خطا در مذاکرات است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/443524" target="_blank">📅 23:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv0ns-4J5LzkNGLU00MKscS6zssJwvHRk3XqQea3GpdIPnh2JZgt5rVdHMrKkNXCh4cArE4IrMRIDuFhVJ9IzJgNzowVgf-8NREjNKdUe4_YyolSH9UX-WgE5ndwXLFA_B5B74isP-48STWcdC5jSdAonxDY6Lv80Vq9hu1EoUuVNXlflvqGdhvZUNpoa65hoxhBZ-lX0sLMaMGo_Haycqs_1-aKBPvZHroIgZGw0bDJixLCZzOfjV2KXBjiX4oG2W-wm6akniavet4G6oyNsL6g5aXlfNlgAXKYDDaC7fNXZXzgaeZ6Vt9t3DMsvmEhDxaNXpLTCiG6hFYCqxeu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی جدید پرسپولیس از ترکیه می‌آید؟
⚽️
اخبار غیررسمی از باشگاه حاکی از آن است که حدادی، مدیرعامل پرسپولیس، راهی ترکیه شده تا مذاکرات نهایی خود را با دراگان اسکوچیچ، سرمربی سابق تراکتور برای هدایت سرخ‌پوشان انجام دهد.
⚽️
براساس اطلاعات به‌دست‌آمده، مذاکرات میان ۲ طرف روند مثبتی داشته و اگر اتفاق غیرمنتظره‌ای رخ ندهد، اسکوچیچ به‌احتمال فراوان در روزهای آینده به‌عنوان سرمربی جدید قرمزها معرفی خواهد شد.
🔹
البته تاکنون باشگاه به‌صورت رسمی این اخبار را تأیید نکرده و باید دید در نهایت روند مذاکرات به چه نتیجه‌ای خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443523" target="_blank">📅 23:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067a3aa9d1.mp4?token=mRSNYpOYfr9a4ZdClGc8wHqXFft89qMGgMXJZyIgfbhh6ta8wkWCJMGvyD3SzZbpAlOqmzO5hiGS2P2KFZj-S4NlyN-bBiG8RdfPlfTsZGOmLeQ3mlA6TZ2hfMvqd9GcwFd4pvrOfu8SkeRcLLqjc34GAddQBb85tBDCH9xhUEmvNGJgh2DppbBDdUpsfoKD_Y-Arqi44DGHicYgceD5RUZod34JR9vvyG30TeT9_kqKNV9bAMPJjLee8XtPYOnwXRWe2ZL7gG82x3Bz1306YgyrNVY98NgSegpKlOLAZgeDWf9HwH70VZOwauN1M6o9QSSZ2KWlIcJBqB5W79mlXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067a3aa9d1.mp4?token=mRSNYpOYfr9a4ZdClGc8wHqXFft89qMGgMXJZyIgfbhh6ta8wkWCJMGvyD3SzZbpAlOqmzO5hiGS2P2KFZj-S4NlyN-bBiG8RdfPlfTsZGOmLeQ3mlA6TZ2hfMvqd9GcwFd4pvrOfu8SkeRcLLqjc34GAddQBb85tBDCH9xhUEmvNGJgh2DppbBDdUpsfoKD_Y-Arqi44DGHicYgceD5RUZod34JR9vvyG30TeT9_kqKNV9bAMPJjLee8XtPYOnwXRWe2ZL7gG82x3Bz1306YgyrNVY98NgSegpKlOLAZgeDWf9HwH70VZOwauN1M6o9QSSZ2KWlIcJBqB5W79mlXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا کالاهای اساسی گران شد؟
🔹
وزیر کشاورزی: یکی از علت‌های گرانی، اصلاح ارز ترجیحی است.
🔹
موضوع دیگر شرایط جنگی است که در جهان باعث افزایش قیمت حمل‌ونقل و بسته‌بندی شده.
🔹
افزایش ۶۰ درصدی حقوق کارگران نیز علت دیگر افزایش قیمت کالاهاست.
🔹
قیمت حمل‌ونقل رانندگان…</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/443522" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c702a45f.mp4?token=jRD_Sw3UtxTFwlfop-QCxhgtMZH-cc-mp2GU_Obz6JoFy8A1Ucoh3Nu6DPzKdJLn5I0K1yD7quC4Ev1hDqiFAJfYJK05PZSqzBSKnhQrFh-Ox1TBkbY0VN7OHGxqwP3ZmV2FcDxZdNkw5TE1IcqQnOPfts6QPvJtejuIzdtRP-zHZ8bU4s5-l1SUqqFLYsTaWIpbSyR0UBAQKqL7bYZ1MMx2NSqbrL-JVjYAwt8gi60SEiJhfOoM5EhSdag3ier-ZRaKWjT-PKJdkJksxJK5QtnLwgtXkpS_GeEo2sL1w5L-Hu9mP5loePL5QW5bdLgzuHHHGNcy-qjJtODpCR9aCgtmQtcMdCuZxWNhJ4myy92qYeBQiaARWMhxlxulUCe832MOIYNLbQ3WjKcoLFd4l5YhDSSW-V9TSCYMvQRxR6RA1HLbHqeEkYFrEux-R3MSu_5vI68wyP5GhyJfhWMxXEabzupiAZIbsmFw-3V1UJ_ZgzLOos2ImOQU8N2KPG4nJRhSA0f0uCZQLPMRfgxvpRcvc5oSlM4KW9YnYc0KttKXf1hqSHh6Jh-dBtpvgUyTdwgRh5vLeeMDPCWbzN0rweEok_emEyORBmr3Wn5Q_qb1O06AB2BGgMcWuF7WLDBJ9vEdjWX-aor00-FPW2ICd6-msRkHCzfEinw2qCrC0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c702a45f.mp4?token=jRD_Sw3UtxTFwlfop-QCxhgtMZH-cc-mp2GU_Obz6JoFy8A1Ucoh3Nu6DPzKdJLn5I0K1yD7quC4Ev1hDqiFAJfYJK05PZSqzBSKnhQrFh-Ox1TBkbY0VN7OHGxqwP3ZmV2FcDxZdNkw5TE1IcqQnOPfts6QPvJtejuIzdtRP-zHZ8bU4s5-l1SUqqFLYsTaWIpbSyR0UBAQKqL7bYZ1MMx2NSqbrL-JVjYAwt8gi60SEiJhfOoM5EhSdag3ier-ZRaKWjT-PKJdkJksxJK5QtnLwgtXkpS_GeEo2sL1w5L-Hu9mP5loePL5QW5bdLgzuHHHGNcy-qjJtODpCR9aCgtmQtcMdCuZxWNhJ4myy92qYeBQiaARWMhxlxulUCe832MOIYNLbQ3WjKcoLFd4l5YhDSSW-V9TSCYMvQRxR6RA1HLbHqeEkYFrEux-R3MSu_5vI68wyP5GhyJfhWMxXEabzupiAZIbsmFw-3V1UJ_ZgzLOos2ImOQU8N2KPG4nJRhSA0f0uCZQLPMRfgxvpRcvc5oSlM4KW9YnYc0KttKXf1hqSHh6Jh-dBtpvgUyTdwgRh5vLeeMDPCWbzN0rweEok_emEyORBmr3Wn5Q_qb1O06AB2BGgMcWuF7WLDBJ9vEdjWX-aor00-FPW2ICd6-msRkHCzfEinw2qCrC0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش گرگانی‌ها در شب ۱۱۲ تجمعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443521" target="_blank">📅 23:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443520">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae1b56c59.mp4?token=jOEQLkV4IjZZdL8FUQBhJZeWgYkKDaqDfV2Q30r86lyF1NL5vVu_girq4Z_rnZbo15XS8LyFSNxLIk9du28fI0hZPzGwmPvIrD1ADsEUtAxdmjShD-6riCuPDaff_JnoQFLrxsA-6a6-QpbWoRYONFSZR2h0XkFW-1PdMOi12gqyhpaYwnXwI2wMBACIsYsC31FeTgnrVDa9he0dHJmksVtX0Zlp3FuZNnHUaW25Unzxsti-Ifa7wEMhXIYth_NcSrfgmLAs3r8x3vHViNp-DkKdqn9ai0Q4pJzQELVkFTygD396xANb5FwR0rxiFsHNubdvTV-UoY8pT_l9cHjTPK_B37Z1oZSitttHMKLsRGl9Nij7aJcUXnaHWoJhyAUtfORQF5heKDpZB4GpNQT8n4eV-B0E8XUBJPmoYX7djrC8No0r8KbBf9U4ZM6DyOO6RkaspPRaHi2YPzUcyAyKPQy9pWF5gg4l1QO6X-PjfCTlBfsHvL6yYm0r-sW-WrPs70EPb52jQyvu2UjWnU4071EcVY7S2oZmhLf09vZIzwR0GnrWMJOtZ7_weO7AGJOREav_GeTzPtyZ-6JnDTgDzLG4vk6hABXsWizlFsO2AKbp8baF-EK0a9PsV94zBxmo0G6rEZPcPPmBdRclsKtd8CxHDoFGbttA8Gt1GEKaafk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae1b56c59.mp4?token=jOEQLkV4IjZZdL8FUQBhJZeWgYkKDaqDfV2Q30r86lyF1NL5vVu_girq4Z_rnZbo15XS8LyFSNxLIk9du28fI0hZPzGwmPvIrD1ADsEUtAxdmjShD-6riCuPDaff_JnoQFLrxsA-6a6-QpbWoRYONFSZR2h0XkFW-1PdMOi12gqyhpaYwnXwI2wMBACIsYsC31FeTgnrVDa9he0dHJmksVtX0Zlp3FuZNnHUaW25Unzxsti-Ifa7wEMhXIYth_NcSrfgmLAs3r8x3vHViNp-DkKdqn9ai0Q4pJzQELVkFTygD396xANb5FwR0rxiFsHNubdvTV-UoY8pT_l9cHjTPK_B37Z1oZSitttHMKLsRGl9Nij7aJcUXnaHWoJhyAUtfORQF5heKDpZB4GpNQT8n4eV-B0E8XUBJPmoYX7djrC8No0r8KbBf9U4ZM6DyOO6RkaspPRaHi2YPzUcyAyKPQy9pWF5gg4l1QO6X-PjfCTlBfsHvL6yYm0r-sW-WrPs70EPb52jQyvu2UjWnU4071EcVY7S2oZmhLf09vZIzwR0GnrWMJOtZ7_weO7AGJOREav_GeTzPtyZ-6JnDTgDzLG4vk6hABXsWizlFsO2AKbp8baF-EK0a9PsV94zBxmo0G6rEZPcPPmBdRclsKtd8CxHDoFGbttA8Gt1GEKaafk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: افزایش مبلغ کالابرگ همچنان درحال بررسی است و اگر به نتیجه برسیم دولت اعلام می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443520" target="_blank">📅 23:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443519">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b577d6a49e.mp4?token=Tw8g8k7L1L5w1rByC8p081F55HwzWZRchGKOzIdvgfsZQWpNsdoXtB9DK08lUoCrHwN9DtriGQYfwoJouvmMJpm_E6KvJ_xsEAGCCut0onsCmTPu00gRQgedr0IU_7vcjBf_A8d56JqGwpiVA50bTCVB9mgc_xNUA2F5e-UkmNe23zGp6qtcakqPe9WxlDOCjfy-kZtPkfyIc6lMkSF4YQnX9TR8ENh9IwZy893r8uz3Hisu--cVXCa1Zahkn8TumwhE78eniLlbwWbnsDaeeRiYC2BfCnBABNpyvgsuhgTU6vPTwwT8wGS95X6gMuVxEUL9BA73xZiuJMcqnjPIug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b577d6a49e.mp4?token=Tw8g8k7L1L5w1rByC8p081F55HwzWZRchGKOzIdvgfsZQWpNsdoXtB9DK08lUoCrHwN9DtriGQYfwoJouvmMJpm_E6KvJ_xsEAGCCut0onsCmTPu00gRQgedr0IU_7vcjBf_A8d56JqGwpiVA50bTCVB9mgc_xNUA2F5e-UkmNe23zGp6qtcakqPe9WxlDOCjfy-kZtPkfyIc6lMkSF4YQnX9TR8ENh9IwZy893r8uz3Hisu--cVXCa1Zahkn8TumwhE78eniLlbwWbnsDaeeRiYC2BfCnBABNpyvgsuhgTU6vPTwwT8wGS95X6gMuVxEUL9BA73xZiuJMcqnjPIug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غوغای دسته عزاداری نوجوانان در حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443519" target="_blank">📅 23:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443518">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO-4cBwbXDMJW-TwZ0L3SPCOwFMLCDN5NluVhQnUxPQrnXF1t37rp-Fd2wFGBnwdxdyRJD5CKw9L2uWz3qUBVDMJN9jlM101QfamC1Yv1M5dT8HrjGGo0PTQ_rNvhuqTg0GkoLn3qI4qtOPZxF7iNeKMc2utNWTtBYUHHdIW7f_9WNG4wZflT9ggUQGHCWGD4QnknY1XsD6fbkMhLqN-S1GLzUcruOhCnCQ_nbV-Es7PU0XrJsotlK8FN6a4uZBmXxRV_DmY__-MYz1AYrebX_M6tIwyExgFIA7vd8P6OuWCLhB3d3KWXHRN1egc55X4kwpk3XjysJYdFxSwsQZTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: ‏علی‌الاصول مدیریت تنگه هرمز باید در دستان ایران باقی بماند
🔹
علی‌الاصول وحدت ساحات و لبنان جز لاینفک سیاست جمهوری اسلامی ایران است.
🔹
علی‌الاصول باید هر بدعهدی با واکنش قاطع ایران مواجه شود.
🔹
ما منتظر تحقّق شروط گفته‌شده خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443518" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443517">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VreF93TyLM0S-24WAs2S0RBQSEC9n_6FAx1BPyUMbE79YHXDAStmBmfNckAUno-sBRKNubwR5t1P9kD1MVGxl5dHN_YJeP2MG1vJY7wyteK5HTybgdXkulz1JuxmEVt1KwzKoxStnadnzYwT-e-XmbUU8JQYDPm1P1p6UpBhHn3DSUPD71h6A3-vi8zzVKmYLbg-ieBs_dbSl_XIuo481hXkv6_rsKk_QohR_PqBijsP_jeBO936UpphBNCEsKrYGbeDEuvHkZmf2c5jCzIFqMN9Zw-gNBje5sF-JUOJxHDzsxB-pQNqRHONe4wiS621ueb4nN_g0ozafQCA5eUhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بعد از ۶۰ روز هم هیچ عوارضی برای تنگهٔ هرمز در کار نخواهد بود
🔹
هیچ عوارضی دریافت نخواهد شد مگر اینکه توافق نهایی نشود و آمریکا خودش شخصاً این عوارض را وضع کند.
🔹
این کار برای جبران هزینه‌های گذشته، حال و آینده و در ازای خدماتی است که آمریکا به‌عنوان «فرشته نگهبان» به کشورهای خاورمیانه ارائه کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443517" target="_blank">📅 22:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443516">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiMdc54vZLUejYwd03meAn9OQ0bsDaytc-Cxu_udjGnvVoorBOU-r_n7PEMhfDQ7FpV6dzJdArODO4l5OZzMkV7-LW1bZDKNcZ5GVwVHvs-33DXemzVTLeTVAW5HRlLDnyTfhiKJCaAo6jhmU9F50bLLIUAa7wMBgFMfQOQXjjFpvyjf0uHw5r3k7W0Snekk4kwkrQZl-Xm3x2sU2Sj29ruJa6GqFMd7H8I7SalgRBuLfvPrK4I4jD0GcFoLn0f6e4azqC-Mp7bEL6vSVnaow2jWP85rBvoMjjf9yBGfIagnTXTUj9BIypLJVoupVXFCn0xHwuP2YChv-8cVpvacLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کومان، گراهام پاتر را کیش‌و‌مات کرد
لاله‌های نارنجی سوئدی‌ها را قلع‌و‌قمع کردند
هلند ۵ - ۱ سوئد
@Sportfars</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443516" target="_blank">📅 22:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443515">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e035502f.mp4?token=Rxmt8QgDDQlkS2mH2vjD84SaCBhLeIbctcKi3jCHcOsGMcqTcsyQAAD3XkmtibE5vhBhqmFAHI5okQph68WoGMYcy9uHOBx2n_i5Izl2H3jwb9ROTRyFhd5C9pX7fV-J0paI4nagc5OMwZA7ijo2R9ND_SSLRL3QvGRLHvC0E27tHHfc-irBMQ3IiYDWxvKHzB-YFa39aG9ygFuOt9seKNztt9h68EoBoudVpIA1hfbN3-ucnpzXAOZdwaq4SbErjc_qb2F66HMK8b5P0aXFjfGds9l8s5ZGofMCmlED_OnaxYCLThMpuGRogGjOczQrTmo9NXX7wV9LULK60484tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e035502f.mp4?token=Rxmt8QgDDQlkS2mH2vjD84SaCBhLeIbctcKi3jCHcOsGMcqTcsyQAAD3XkmtibE5vhBhqmFAHI5okQph68WoGMYcy9uHOBx2n_i5Izl2H3jwb9ROTRyFhd5C9pX7fV-J0paI4nagc5OMwZA7ijo2R9ND_SSLRL3QvGRLHvC0E27tHHfc-irBMQ3IiYDWxvKHzB-YFa39aG9ygFuOt9seKNztt9h68EoBoudVpIA1hfbN3-ucnpzXAOZdwaq4SbErjc_qb2F66HMK8b5P0aXFjfGds9l8s5ZGofMCmlED_OnaxYCLThMpuGRogGjOczQrTmo9NXX7wV9LULK60484tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: امروز مرغ‌داران ما نه‌تنها سود نمی‌کنند بلکه دارند ضرر هم می‌کنند
🔹
قیمت تعادلی مرغ که ۳۷۰-۳۸۰ هزار تومان است امروز به ۳۳۰ هزار تومان رسیده و تخم‌مرغ هم همین‌طور کاهشی شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443515" target="_blank">📅 22:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443514">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d61d37ad.mp4?token=nvLh1yxzG0Aj4u_LoaWESEKG_g3S2K_U59EvQGwvexJGtCK6xeB6XSedzgcMx7UL1d4f-cgc-E4VWPz24N8rrngxYogk4fjVp4UV9Lbk86yXY-HE_JS8Cu6_uDRGhQJnZ2jWtG3ULImqeyH9X7XJd4TB0M4gvg47hBAHScwtAypIIyDU9CBD60rB8Nzhh1bIN9EUqTFxP9MknX9F1KTgdSR5Ogokxn9f5mAZ1sayg6-ZdgKvg0De8Q-FApksoujPFF7XEFTWXtf6cxATaeO3cILKr8G-WSv1UY8t06agGq-XfxZpfCIRkWGSWmQLP0peaGzTpFVUJF74HIi2rYEibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d61d37ad.mp4?token=nvLh1yxzG0Aj4u_LoaWESEKG_g3S2K_U59EvQGwvexJGtCK6xeB6XSedzgcMx7UL1d4f-cgc-E4VWPz24N8rrngxYogk4fjVp4UV9Lbk86yXY-HE_JS8Cu6_uDRGhQJnZ2jWtG3ULImqeyH9X7XJd4TB0M4gvg47hBAHScwtAypIIyDU9CBD60rB8Nzhh1bIN9EUqTFxP9MknX9F1KTgdSR5Ogokxn9f5mAZ1sayg6-ZdgKvg0De8Q-FApksoujPFF7XEFTWXtf6cxATaeO3cILKr8G-WSv1UY8t06agGq-XfxZpfCIRkWGSWmQLP0peaGzTpFVUJF74HIi2rYEibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: در حوزهٔ کالاهای اساسی و محصولات غذایی گران‌فروشی فاحش نداریم.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443514" target="_blank">📅 22:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443513">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6f4a0454.mp4?token=T7IM3GWvB5VHpRWojMucUp7ZR7vUZBhUVWFXkAI2CG34XhptY0J4TcxvUaVxNMOqpCYAD5QEAXp1EAtleNX8HHuBEEnfg82jd-WrRvV_uemGgIAO1ErMEYkEs7O_HJYzhLuZCIRPpIoM7uylTHxJv1lZ6-9U92Tof3wS_pEO41Ygo90u4Fjguo4FY5irDZMGtlDjSJexPcj5-6acIv0zc10LwPUwT1ibWJHRhm5SOWuX35_tYW1XE0IK8KyAeNw7e2s84efwEPe17Mn9rZwyORV0Uatp98alx4l65VG7RUv_Vv1Z8eNMh-67mhWPHpEBeg0YwTdM_8C5UobIfFihmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6f4a0454.mp4?token=T7IM3GWvB5VHpRWojMucUp7ZR7vUZBhUVWFXkAI2CG34XhptY0J4TcxvUaVxNMOqpCYAD5QEAXp1EAtleNX8HHuBEEnfg82jd-WrRvV_uemGgIAO1ErMEYkEs7O_HJYzhLuZCIRPpIoM7uylTHxJv1lZ6-9U92Tof3wS_pEO41Ygo90u4Fjguo4FY5irDZMGtlDjSJexPcj5-6acIv0zc10LwPUwT1ibWJHRhm5SOWuX35_tYW1XE0IK8KyAeNw7e2s84efwEPe17Mn9rZwyORV0Uatp98alx4l65VG7RUv_Vv1Z8eNMh-67mhWPHpEBeg0YwTdM_8C5UobIfFihmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: وقتی حقوق کارگران ‌۶۰ درصد افزایش پیداکند، این موضوع روی قیمت کالا تاثیر می‌گذارد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443513" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443512">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506cd7cf18.mp4?token=vZbm-cUzbwrCIos00ooyE8gD-YFvkl17M5ajCTnlBItFNZEsYWJXqSCD3OZiJvtafiff2iLoqfhnzslZ1mL8NQw__5rNc4xxd1y-S810nzWQlz9Etoq2CEYgAw1pmjxbINlU4m-6X2YsQ62MpKYfEqVZhnWkPWPIaGYP9PA01Qa_KcPOI40Wh99Ou5znSxiMDfkH-kQaohoaJjOTPQ6SiJjOqGnoUxWXNbyFMoxUv77mBqt1DSRoCKwhzohg3gOS7H9kROHiP_B9V7aie2KEEwdVH-foT4IHySispGnPIeawHaYTH0bz1qc0RFxWqkSZVmFLzxmAs0P5kRuxCs_Y7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506cd7cf18.mp4?token=vZbm-cUzbwrCIos00ooyE8gD-YFvkl17M5ajCTnlBItFNZEsYWJXqSCD3OZiJvtafiff2iLoqfhnzslZ1mL8NQw__5rNc4xxd1y-S810nzWQlz9Etoq2CEYgAw1pmjxbINlU4m-6X2YsQ62MpKYfEqVZhnWkPWPIaGYP9PA01Qa_KcPOI40Wh99Ou5znSxiMDfkH-kQaohoaJjOTPQ6SiJjOqGnoUxWXNbyFMoxUv77mBqt1DSRoCKwhzohg3gOS7H9kROHiP_B9V7aie2KEEwdVH-foT4IHySispGnPIeawHaYTH0bz1qc0RFxWqkSZVmFLzxmAs0P5kRuxCs_Y7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما هم مثل پدرانمان عاشق حسینیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443512" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443511">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eb62dba8.mp4?token=lJBAkXOg-xO69sHTsPU5e7SVPIwhXdKbHq6wVsTaUp3ulL6_hj66b8wlTwJ2LDWS4wcDRKTxVWrc5tgwvG4PHX-vqswdVhO2BSIPaSNe6ZPFJ1McmzhdoFBa51UdZWVT1fFKLQYmqZ7FjwgUL8u6fVUjl0gO-VRwkXtoaDs1jCyo-p3l6c0FNfRUeMZU7WyGWR2K2J5cT6QLqjFwmxnJRR4x-ObFyVo8V0NpZJ0rrxZZan56YDggl1WuSOK5zxWfvnWNZs6akmByGZAmR3PUL2vP2uDcLvmpKUaj9L8cp8sbg7iyAC5tJktBDLQjlZds-UN9mvwP2DTuve7O6D0Slg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eb62dba8.mp4?token=lJBAkXOg-xO69sHTsPU5e7SVPIwhXdKbHq6wVsTaUp3ulL6_hj66b8wlTwJ2LDWS4wcDRKTxVWrc5tgwvG4PHX-vqswdVhO2BSIPaSNe6ZPFJ1McmzhdoFBa51UdZWVT1fFKLQYmqZ7FjwgUL8u6fVUjl0gO-VRwkXtoaDs1jCyo-p3l6c0FNfRUeMZU7WyGWR2K2J5cT6QLqjFwmxnJRR4x-ObFyVo8V0NpZJ0rrxZZan56YDggl1WuSOK5zxWfvnWNZs6akmByGZAmR3PUL2vP2uDcLvmpKUaj9L8cp8sbg7iyAC5tJktBDLQjlZds-UN9mvwP2DTuve7O6D0Slg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: وقتی حقوق کارگران ‌۶۰ درصد افزایش پیداکند، این موضوع روی قیمت کالا تاثیر می‌گذارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/443511" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443510">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU0Gus_QTuUOuajh6nv2Td1_6StmbqFq3BlgtDx0fyk7kEz7VwOZBnlsuvQdC46zE7hjWmZLlPJpnseH3Cpeuea63A3LtRPHPKx0Hw_8zleZjj6Rf10OuxU1maqNE8Tnpvwndlp_uWKdzQmsvn0PT5l-tf1Sk_W0tGPbqHXLTJ2NEey2iy3kkckF2C_b-KNUDUJGR9zjKzJqlWff_uQFIN2huNWI1NzjKNXmuDtD0DYhT1XjEhlcRjlosUCF8vS_aqFPh0FL9EQNP1WXB8k-85f4LlgBLZKJZwR3Vfkl6xjiekmsYaxUPQ5bQRsxzkOYtNwRXLJmZwEqdiE_NTPIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو غایب بزرگ مقابل ایران
👀
‼️
به نقل از DAZN، جرمی دوکو به دلیل عفونت دستگاه تنفسی بازی مقابل ایران را از دست خواهد داد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443510" target="_blank">📅 22:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
سلام، چرا هیچ نظارتی در بازار نیست؟ زمانی که دلار بالا می‌رفت قیمت‌ها با توجه به دلار بالا می‌رفت، ولی موقع ارزونی دلار اجناس ارزان‌تر نمی‌شه؟
🔸
قبض آب این دوره ساختمان بیش از ۳ برابر آمد و بعد از مراجعه و اعتراض به اداره آب اصفهان دلیلش را پرسیدیم، گفتند چون نسبت به دوره قبل (در زمان جنگ و عید که ساکنان مسافرت بوده‌اند) مصرف بیشتر شده، آب‌بها چند برابر شده! این موضوع خیلی غیرمنطقی است.
🔹
در ایام ثبت‌نام دانش‌آموزان هستیم. برای ثبت‌نام پسرم به مدرسه رفتم و برای ثبت‌نام چند میلیون می‌خواهند، اگر اجباری هست آموزش‌وپرورش اعلام کند تا مردم تکلیف خودشان را بدانند.
🔸
چرا کسی پیگیر مشکلات ۴ بانک نیست؟ الان ۳ روز هست که توی کارتخوان کارت کشیدند اما تسویه‌حساب نشده.
🔹
ما الان ۳ هفته هستش منتظر پول وام ودیعه مسکن هستیم. دقیقاً ۱۷ خرداد پول واریز شده ولی گفتند مسدوده و یک هفته دیگه می‌تونید برداشت کنید. بعد از یک هفته به اختلال بانکی خوردیم. الانم همچنان مسدوده. چرا کسی نمیاد توضیح بده کی این اختلال حل میشه؟
🔸
با توجه به فرجه نامعقول و نامناسب در نظر گرفته‌شده میان امتحانات نهایی، شرایط ناپایدار کشور و فشارهای روحی و روانی ناشی از این وضعیت، از مسئولان محترم درخواست می‌شود در برنامه‌ریزی و زمان‌بندی آزمون‌ها تجدیدنظر کنند.
🔹
سلام من یه متقاضی مسکن مهر ثبت‌نامی سال ۹۰ هستم. بعد از گذشت ۱۵ سال هنوز واحد ما رو توی مسکن مهر پردیس فاز ۹ جدید تحویل ندادند و هیچ جواب درستی نمی‌دهند. به داد ما برسید...فاز ۹ جدید پروژه نارنجستان.
🔸
خواهش می‌کنم برنامه قطعی آب فاز ۳ پردیس را نگاه کنید. از جنگ رمضان تا الان وصل بوده، دوباره از امشب شروع کردند؛ تا همین الان سه چهار ساعت آب قطع است. گردن هم نمی‌گیرند، می‌گویند قطع نکردیم افت فشار داریم، در صورتی که نتیجه‌اش برای ما ۱۲ تا ۱۷ ساعت قطعی آب است.
🔹
کاش در ماه‌های اخیر خبری هم به موضوع پرداخت ناقص حقوق اعضای هیئت علمی دانشگاه‌های کشور اختصاص می‌دادید.
🙍‍♂️
شناساسهٔ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443508" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efab1522b4.mp4?token=Hrg_6J6E1Qg8Z3n2WimQUlEVjyo1Eh3vI4EYI6EbXkgfG0DWPvF9I-OnF2zbz6kvg73mVneI4O6GEwglAGhfM1kbqBxvSBHstYv1QP70TqkTYQSVfyIS_O3EjuZ2prx0DKAu-K2p1EaLV1vNuJGcRI6TIK1gkuD9ly-Hb1DdD0KDS2vwngohOTS3Ub0dmrJK79uLQwCel8yoTtN1sQOBIH-h_0qGx7RCpMtMH3RS3Mmy-a_yepHxEtK3JaTBxs0k5XtwXREU_WQahIYLx6OsUmy2HP3dAVla1EjApUjaLKa5FVIqvAmzvBPwbpjsF90EUAQufK418q-Av07-Rp3dxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efab1522b4.mp4?token=Hrg_6J6E1Qg8Z3n2WimQUlEVjyo1Eh3vI4EYI6EbXkgfG0DWPvF9I-OnF2zbz6kvg73mVneI4O6GEwglAGhfM1kbqBxvSBHstYv1QP70TqkTYQSVfyIS_O3EjuZ2prx0DKAu-K2p1EaLV1vNuJGcRI6TIK1gkuD9ly-Hb1DdD0KDS2vwngohOTS3Ub0dmrJK79uLQwCel8yoTtN1sQOBIH-h_0qGx7RCpMtMH3RS3Mmy-a_yepHxEtK3JaTBxs0k5XtwXREU_WQahIYLx6OsUmy2HP3dAVla1EjApUjaLKa5FVIqvAmzvBPwbpjsF90EUAQufK418q-Av07-Rp3dxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد در خونخواهی امام شهید کفن‌پوش به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/443507" target="_blank">📅 22:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667f87f7f0.mp4?token=d165AXho-F4UKj-syFRviy-y4297vT6nzL_owYIbjSawzhRN5BgGDivo4zibL2Oj_hUdfyAMGPfMthwEMnAL7J5dPFRUsaKF_mnaZrJ3a9IHlzwPOdrdwbY11kgX3RuMpqe_ofQnrtFCaqeo1FuBG1c5LyL_ryblIJUsg3udCz6wTetMkZcL89GCnO1XfzhIFDQEfUkSu7muoBs5Xvay2a7MSiEX0g90qr4Q9GrWZ-b7zShY7bH_mSa8wE3zxEvRVtPfOCFaXFQ5CVVw2Vn48WJRz5Ei20SScjZyomDA7aMa4B44Nz8W3SQG5LEOCobaIjQ68g6jRZ0H4ZqACqsZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667f87f7f0.mp4?token=d165AXho-F4UKj-syFRviy-y4297vT6nzL_owYIbjSawzhRN5BgGDivo4zibL2Oj_hUdfyAMGPfMthwEMnAL7J5dPFRUsaKF_mnaZrJ3a9IHlzwPOdrdwbY11kgX3RuMpqe_ofQnrtFCaqeo1FuBG1c5LyL_ryblIJUsg3udCz6wTetMkZcL89GCnO1XfzhIFDQEfUkSu7muoBs5Xvay2a7MSiEX0g90qr4Q9GrWZ-b7zShY7bH_mSa8wE3zxEvRVtPfOCFaXFQ5CVVw2Vn48WJRz5Ei20SScjZyomDA7aMa4B44Nz8W3SQG5LEOCobaIjQ68g6jRZ0H4ZqACqsZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است
🔹
اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443506" target="_blank">📅 22:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udQT1Et4y-3hA6tGpzdv2EY5sofOWwHoTikLQaGANUK7DJTAohdhNIey9Xun-EImEXbbrfsJmeYSaVa_T90uTSdwP34FkWgoc_pfzPiuRZbV1zMQRzYn02kfG_0WfxiM1SRTESSLLSujgjy2NmufNVOZ3kP6F8SViQozQfyy5oc_rLGYQoIum-2lzmewyaWmakey1pbRFNpiOd3q6yqGcQQcfGQ9VQRn8b63A7e8R4oy6DkNmClu_DVFVHp2aX5RKxviwIyR_5RnfIM6kkUEtD8ojEJw0Oabkj1QLhp_fmAy0C13noK5_Snyc5BW59uVveV3ZpnP_T1M3DUMd4ZuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1CIwuqcFhu1YQ1LdQBM8sl6lcZSMa22vb-XUVQkxNvIQIAjETc-I90LMVj_HadHYsCJxHvy4VbKGNt5M5U7W_Kou0v5p3D0NTcM4ZjYMNfEtI3BQvKp4GHQj1s30cc_q_N9_EcHFPdSQ9zQaUNeZrAQBGvI7uDxDQs091octisBT3In4laIobHrvtMJYqh4e7gMT0gx6uRyuS4DUIJNbf3KdHSQPK2X3xdvx5b3g8nxbuhsELdxFnNHxsbgQKBA6JAggGoUGo_1TAgCvMSAhoEaBviOu-_zhBnhXHg25k-JYW3ClXOMZMGNprHx_0Pr9PFy46zMhr-3lYcNVQFJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rngL78Du-sRsmxcDRdm874aKDKvMmLER454pfpHf4ca334lWi1RSmbTSJyH1zbKZJpQ_CIJiXGQKFEi4u5xQiVI-j-1whRBJ_xDxt3br6lPaEl0I0Wr0Zn9tT3fqKcwiOjZokaSXfAka5XEdCc1dLRMlhq3sWnzmrS5jvMJMPGVM4I38GT0M3vwIMxadKPPuErPdPpHBF8MFVfAYXDqCSCGwomHZDfd79i-2_w8L3q03DnK6aidXydZuH5f-SGE07K6BgBiFvkZ6_VwAk0DbERnR6Y01vAR_dWVYzp4SSJjJFZ0YkpPIPIXNoSgaZQ79ZTbOgN-qfqaXM6K17cboqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g56UCUYn28b29-fn3pYEN5iCPGPLjoLLhTV0xXnla1jz1etmsGv0ugmagKXg7O7jkL9_MCNsLh_91aRsYrQ5M77RmhUW2yLQz7dr_2ucqP-6LQb1rPFU7w7qJ3qcTGE91z9M8Y2FQzVildcwp21MmWLvN1YInLclx7Os3oqIMLfgkGTMOudOVZx8NBL5rz8uAGIDk65ab1UXEiUlAcb_Sy7RKtE0W_JtNFt097GEo7mw4L0KfUcxx2VOf9gG6uUb70QiapFpp3-a4RFzsbw_EsfElk-SuTTLPq5wxHuSLcY1tbsZb_M30TVhnH6Kx2sXFxLa4RuDmqQSt8xSqdmEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnckZx1dGvOrygULlSHvQ2-wHGGS8gslwZxrIYvpGKkB2nTRxJ79_ORVJi34G5EYSRVjv5afNKwPfOdYqvxW5opWd2313q--gblDk9C_R5bFqWhKC8ruFLLg9r60buuh2wRHpim9sHB7AckC0kKfnis8lpW9N5VhnVitcxAhWaDLGcDjPlUUnkmgbjOaNutZKidEHJ1yeRmY9phVkh5f-tTyDs8P9nta7KnV7yBA0NHeHHpjWVt267s0aufGQT7HEM-WW1llWG2cbUs46H0ES_0B8HuwPJDGbhrvijAq47rJ_EKMy5EcfUVbTnhI3igahqQuZiBwHItT2HX7_7gjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4dIme0RgFNU1yAXq2-KAEpv7HufkdMkUvjyfZcUvTiyscyGp1X4C_MBMh32_-g0b_nMdmTnibkQShZTzUwKOevUizFJWFmwqVJz-X3D7zCH2gcicpItV_FeWayqj0YZpslUmr7dJsGiXh4ooWg1rFA8QgqJx-pILGLZ1kSf17H6XmZqbbgHp_dBTBrI3TY18KYjbj11_OwHicE9wqO95HofIZLljHnWg3mtbtVrkZ_vBPAzqZ1y71QORfPN180GzEqPGFGMwZ0ah1z-2GLS2jSEAgWZ3UCPNlDo0YjpLZp-lJxcPwAkbHCwlKFUtD9uhC4jU4Vh115BQWkoeW-6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oik34l4NwHFFtKySMmjZii30qrsuTL1IoMu-mJZjtppakGWNNfkwbmvQOf39ShBi0PeMjNHUVR-TibUR9pc34685TpToqQ2KZw_MaL0LNURDMjlssD3supgcLMFHOAp5gmVAXaeuhpph2amW2EVhN3j_CW25RejdrbcYAYc7eeAGvo2db3ssCIzgCelM_sL91tSt8QzIUccG6srUims0S0qrkin-w0952g2SLbnAd8vJeaUCjUJ5LvzKPQchag1bQ59H6xHmIHfjhjQJGzTt-wXp3PQAIvqqMZmfPp9laTSA6XzvhBGrB5w54P8fpNcSA4uWcAyA2eYry_7ob3DBWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سنتی هیئات استان یزد در حرم مطهر رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443499" target="_blank">📅 21:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a45268f8.mp4?token=qunZhlF8wUzX_6Vt_yxGifLvMlz4rtDRgHs7TqSekX6pZaHy6TKnpp65XHr7UTk9_mH1kKfJfh6eoRGm_a0kZlw3dL2pNYanqN4E6wUz6VeU-C03XVOeeQ0KixdxAsSH10VIGG19l2KxhS9eycWn5CwJdHjlu6NnBb_WZ71Fy1A6jWwbqM90aQOcSbE5nR-0x5Zwp3vAxfI7Mgf0TgvVa78VurDpwjMv4EwhXcvLmQpffVZ_rDE84iQZ1oR635LAJppSvlXAY64FrSOEeSZtOWewdHatcD7oD8m0_MKxFhjpJ-1nDXRJFXATsPBMXIGzelsFZ-1bOjQj4VtTwzHofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a45268f8.mp4?token=qunZhlF8wUzX_6Vt_yxGifLvMlz4rtDRgHs7TqSekX6pZaHy6TKnpp65XHr7UTk9_mH1kKfJfh6eoRGm_a0kZlw3dL2pNYanqN4E6wUz6VeU-C03XVOeeQ0KixdxAsSH10VIGG19l2KxhS9eycWn5CwJdHjlu6NnBb_WZ71Fy1A6jWwbqM90aQOcSbE5nR-0x5Zwp3vAxfI7Mgf0TgvVa78VurDpwjMv4EwhXcvLmQpffVZ_rDE84iQZ1oR635LAJppSvlXAY64FrSOEeSZtOWewdHatcD7oD8m0_MKxFhjpJ-1nDXRJFXATsPBMXIGzelsFZ-1bOjQj4VtTwzHofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است
🔹
اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443498" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔸
ارتش اسرائیل خبر داد در درگیری های روز گذشته در جنوب لبنان یک نظامی اسرائیلی کشته شد و ۱۲ نفر دیگر به همراه یک افسر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443497" target="_blank">📅 21:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/443490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب ششم محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443490" target="_blank">📅 21:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443489" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627580024b.mp4?token=SDJpgq3hV3-KzSskBQCm5_SVxq5yrQnZA_UWNN9O6s5Jay5qoNyDi6jrT6eZmwff54eXsbTX3WpO1lVP4rFBex2Z2P84Swu9ccqYuXT2xnuLmzJpc3awtR8SUSPqqjx17ObMb89CVzzPNdgQDKWeeKca6cbuyS-TnWKOEFBMldd1b8EkK8d3Wzes4pYHJV8ODYm7Do5NwbnSMbz6sbXEQ6_Rt3550kZZnXuPrOdh9CeqyJwdx2DaiKZiQLKHgzqVFQVGf2fn9siZx3A6YAm4xrH3UfUW6T_DX_c9xAoa7ueBJdwKtSZpi-jggXnxTQ524u-l9rXdmpQV29C7IkhLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627580024b.mp4?token=SDJpgq3hV3-KzSskBQCm5_SVxq5yrQnZA_UWNN9O6s5Jay5qoNyDi6jrT6eZmwff54eXsbTX3WpO1lVP4rFBex2Z2P84Swu9ccqYuXT2xnuLmzJpc3awtR8SUSPqqjx17ObMb89CVzzPNdgQDKWeeKca6cbuyS-TnWKOEFBMldd1b8EkK8d3Wzes4pYHJV8ODYm7Do5NwbnSMbz6sbXEQ6_Rt3550kZZnXuPrOdh9CeqyJwdx2DaiKZiQLKHgzqVFQVGf2fn9siZx3A6YAm4xrH3UfUW6T_DX_c9xAoa7ueBJdwKtSZpi-jggXnxTQ524u-l9rXdmpQV29C7IkhLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیهات‌ مناالذله، پیام شب ۶ محرمِ مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443488" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1856500ba5.mp4?token=HZgo2HJ25pqeNg1Ytx0Mw244kYGAeAfMCbx8-V6SNAoZYjPIoCWP15-vF9ekqAPP5Xj8Th73l-Ruiq_467tm2cKb7IM7NoKiHmXYvoK4NtflS6UPXo6IQVDUL5pZvXUMLXvxdQUj_RnpXDgPRwTB5DCqzN3D96cYmgibz-ahwuihrB1VS24AHegHd_1LJNkk5nN1tTxl9Kq26re5a__Wvx67JEIkV7BwI0WnlBp_yCegkMI70FEtIWvB-fdoQqmYkesKeb7YJvOvuWVhQZFFFryOiZN-XTCr7PUtzwjtoKlyIulRCG9kHfQACetsbYN_mFB04vEAwAd3Mtfpz1zQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1856500ba5.mp4?token=HZgo2HJ25pqeNg1Ytx0Mw244kYGAeAfMCbx8-V6SNAoZYjPIoCWP15-vF9ekqAPP5Xj8Th73l-Ruiq_467tm2cKb7IM7NoKiHmXYvoK4NtflS6UPXo6IQVDUL5pZvXUMLXvxdQUj_RnpXDgPRwTB5DCqzN3D96cYmgibz-ahwuihrB1VS24AHegHd_1LJNkk5nN1tTxl9Kq26re5a__Wvx67JEIkV7BwI0WnlBp_yCegkMI70FEtIWvB-fdoQqmYkesKeb7YJvOvuWVhQZFFFryOiZN-XTCr7PUtzwjtoKlyIulRCG9kHfQACetsbYN_mFB04vEAwAd3Mtfpz1zQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند نکته از پیام صریح رهبر انقلاب دربارۀ تفاهم نامه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443487" target="_blank">📅 21:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f7449320.mp4?token=NQypc-LYVir1DbahNRCTDEuOy5xFbDg2bxhgwCnpS75SIdqTJslKDOvGOEwoKBRuVXrw7mJ6PQoWSW-ZBBq2zuxurf1zaintd4yfBOM49aD4wiwVXpWcmXrWfkpiq0NcN8tQXfRLRytp5nC83IhGHskQ7XUbicA12N8BOn0ClrMp5hWkKjmAhUQ577_akn5kIT4cW2LS-b5BVpg128owkrgvgIFzCIUd6sZmVdzm24C18VodT1F6yidPzjeEeq_s7-KkbV6Go_lg0s6PaCw1Q0dL_TMS4RhKm5V0Y9iZ4sS0ZjMC54GUzVv8BcVweE5k8jnbEWFx9vNrSwzD2av8UXOrKrR-6uG5keQLFJMrj1kfX2Ub-p01EQm-7ky9t1q3qEhBvtq-44OqHFtZZc_NHUSevjeIWGeoPBtSnhtEmSO1TKK5eKftkbPF_leHJMzwydekYwKij8wuKyguzYkOf9nZ2bNZ_UJz79c9ocqDX5oFnJ1z6qs5clFP9hbtau9BXRY8vtNr0uNA1lq5oDz678gNNB2MAmAr0WxdSd4EGAnPAZwSfy9EW1e_6pE-S1yyowJNMsxPfaID7zku_g4gimmXNlC0SYskSSgSNGjhPSWOxYjX7P1uZa3hyqEbbHZMDBt-xL0bNT0sM1BuomT2sVa4-eXZWBwhRFGgOJvEopc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f7449320.mp4?token=NQypc-LYVir1DbahNRCTDEuOy5xFbDg2bxhgwCnpS75SIdqTJslKDOvGOEwoKBRuVXrw7mJ6PQoWSW-ZBBq2zuxurf1zaintd4yfBOM49aD4wiwVXpWcmXrWfkpiq0NcN8tQXfRLRytp5nC83IhGHskQ7XUbicA12N8BOn0ClrMp5hWkKjmAhUQ577_akn5kIT4cW2LS-b5BVpg128owkrgvgIFzCIUd6sZmVdzm24C18VodT1F6yidPzjeEeq_s7-KkbV6Go_lg0s6PaCw1Q0dL_TMS4RhKm5V0Y9iZ4sS0ZjMC54GUzVv8BcVweE5k8jnbEWFx9vNrSwzD2av8UXOrKrR-6uG5keQLFJMrj1kfX2Ub-p01EQm-7ky9t1q3qEhBvtq-44OqHFtZZc_NHUSevjeIWGeoPBtSnhtEmSO1TKK5eKftkbPF_leHJMzwydekYwKij8wuKyguzYkOf9nZ2bNZ_UJz79c9ocqDX5oFnJ1z6qs5clFP9hbtau9BXRY8vtNr0uNA1lq5oDz678gNNB2MAmAr0WxdSd4EGAnPAZwSfy9EW1e_6pE-S1yyowJNMsxPfaID7zku_g4gimmXNlC0SYskSSgSNGjhPSWOxYjX7P1uZa3hyqEbbHZMDBt-xL0bNT0sM1BuomT2sVa4-eXZWBwhRFGgOJvEopc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای قیمت‌های فضایی در بازار موتورسیکلت
🔹
سازمان حمایت: با گران‌فروشان بازار موتورسیکلت برخورد می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443486" target="_blank">📅 21:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443485">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f7d6b0e3.mp4?token=LcVYQJnw5k6UFYUpQs3QLxdDfzgBpCCOIoiCIqUNriCwWhwN6ThaHt-sWUUM2Pf7dzyjgDAtstoFY2H7VnUBd5sB7yPVIMV_fRaEE2EVifJOFTCHKPFiztLWJTwdvX0TBo1ZcKRhy7w6bOYUIBn8CVNKMvJvR7cj-s1RV3ZcolDzbaKH-5_89SsHf_tT7GKjMMhTOLZHndhNHW0WtCYjui-3QpNkLCFUsZYOg4eIkRb_ESqGLOln4_pqSOTDjZsLYr1fpbPUJIvXfjH61GpLVfDCN54Q-XJ1Hi_uXK-2Fayz1KgwZg7ZuxJkM19KUcjqz2JdZF7riIArch_vYrKMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f7d6b0e3.mp4?token=LcVYQJnw5k6UFYUpQs3QLxdDfzgBpCCOIoiCIqUNriCwWhwN6ThaHt-sWUUM2Pf7dzyjgDAtstoFY2H7VnUBd5sB7yPVIMV_fRaEE2EVifJOFTCHKPFiztLWJTwdvX0TBo1ZcKRhy7w6bOYUIBn8CVNKMvJvR7cj-s1RV3ZcolDzbaKH-5_89SsHf_tT7GKjMMhTOLZHndhNHW0WtCYjui-3QpNkLCFUsZYOg4eIkRb_ESqGLOln4_pqSOTDjZsLYr1fpbPUJIvXfjH61GpLVfDCN54Q-XJ1Hi_uXK-2Fayz1KgwZg7ZuxJkM19KUcjqz2JdZF7riIArch_vYrKMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تمجید کاپیتان بلژیک از طارمی و رضائیان تا مصاحبۀ جنجالی دستیار قلعه‌نویی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443485" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443484">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34dfd69ee.mp4?token=pKJ10Y1QgWqEgCs7dO7LUtzLfwLHC3mBpOFD51XxoXkFWeVSW9w4ZzG4Y2uWRWXiR9qwbXgvj6KwMfwINg_yG4z8Nq5sgl7eFbrPBOx-2SsQglg8hEk_UXIrmr76m9qBlxIY4dGlNtNznW21QbzplXHpIDPhxFgB2Ms4xrl24KaGj24nVsQKwtCOLzJePsJ3peFssYm0unzLfmxPWsJlznccHwLCWIq8O8FgcrLmt7UPfnZpWr0CiCQWgINQXkdVrNTplwIUJpBIGdyUKetOJxBHFh-QumWeObiVKsPUEUNKut6y6RF4yhbtwlRIfKAY16IJcMi2GHyGsIcjFLGJcqrNVVr93eiRzrglp6PqfU_dPcv-Ih6tZlaup7P5FyBYjZJkCeRTyCsWxTPxeAU8eSVnclyfmTlFVZjp9pWb4Gmfii8s9xj66QlRElv9vMSWKStXWgKHKgmvMT6kNqhsss2Tk6HLcFssNoghKMkmxmKdRh8LrFnDhswoin3yjw3p50-_dI3pQSNTnBTpHeRFOdk2rk6QTe0d4zu1G_phe5VJ2sNXk8PuJZdjmpyvUGwM9GP4WVJTX-AWd8iIht2Cv3CGntoVh5meqg98dANNinsSnNlsIXGbFOu2zdwigrUe2GDRvBfYdajvAo9w7PV2sNOTtpwhDgQ7ErOmYl0ffQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34dfd69ee.mp4?token=pKJ10Y1QgWqEgCs7dO7LUtzLfwLHC3mBpOFD51XxoXkFWeVSW9w4ZzG4Y2uWRWXiR9qwbXgvj6KwMfwINg_yG4z8Nq5sgl7eFbrPBOx-2SsQglg8hEk_UXIrmr76m9qBlxIY4dGlNtNznW21QbzplXHpIDPhxFgB2Ms4xrl24KaGj24nVsQKwtCOLzJePsJ3peFssYm0unzLfmxPWsJlznccHwLCWIq8O8FgcrLmt7UPfnZpWr0CiCQWgINQXkdVrNTplwIUJpBIGdyUKetOJxBHFh-QumWeObiVKsPUEUNKut6y6RF4yhbtwlRIfKAY16IJcMi2GHyGsIcjFLGJcqrNVVr93eiRzrglp6PqfU_dPcv-Ih6tZlaup7P5FyBYjZJkCeRTyCsWxTPxeAU8eSVnclyfmTlFVZjp9pWb4Gmfii8s9xj66QlRElv9vMSWKStXWgKHKgmvMT6kNqhsss2Tk6HLcFssNoghKMkmxmKdRh8LrFnDhswoin3yjw3p50-_dI3pQSNTnBTpHeRFOdk2rk6QTe0d4zu1G_phe5VJ2sNXk8PuJZdjmpyvUGwM9GP4WVJTX-AWd8iIht2Cv3CGntoVh5meqg98dANNinsSnNlsIXGbFOu2zdwigrUe2GDRvBfYdajvAo9w7PV2sNOTtpwhDgQ7ErOmYl0ffQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گذشت رهبر انقلاب از نظر خود دربارۀ تفاهم‌‌نامه با آمریکا را نشانۀ چه می‌دانند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/443484" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443483">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57be3295c2.mp4?token=oCHl9ATpAgKBdnjE_qCK6Q3TzA7RhkaQEwO4lrvOFNHacKSJ1m_CoPE2lFiBKnhYNsR599r651IEU5duQ8d07QosMHQvUH68nGJSy-o-v0hTt7TYSIWZvXIzN8yzTTMywpqdGL_6SMaiDHBG66EyNU6g89mMDrQT1nHQatjSsHyy20mefExyPDWdqeAubrHBKg0ofcAsBTWg4cCCQN9w-_fFFG7-dsOU0FJstKs0bxF0pHe0kUB2WNTqzo65kUGUw3h0GIRBuQ7h6wmPBG1-sALK42x03NpwtFobgL-mwKRrtgQA_O1X4ZXMA01yrTYUNkkeH370fS6eW6a2r_KErKbL69BO5TGhFGbEgxxXDnb60icOWe6d5g_T3Vzcm2x8wsL2yphckTDNV2nMxArMFNScv7BfGkMUOabpKrz0QVFyi-Rb6MgdgwQTisOuE-KiMNUcD_qk9TYOWdkMgnCqSuH4J2rpMuOl3dqWZpkGr3tXEI7_S4Q93Fag7uiXHqJETZLMMjvOio0Gk3IaYHzIDixEXCrbCK84xahzTEhcuvn7RlqlAotZoXs_j1Ks3KUtcB62c4M1QVDQH_pvMmGsmcoJ3ZqwNbUE10Tt3DoIZfz6-07xdO_qtDNGD4HvFOqJl9b49fV_BB7Z3HvOWOztNHzfmyL5d8UUZpEfknOUloM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57be3295c2.mp4?token=oCHl9ATpAgKBdnjE_qCK6Q3TzA7RhkaQEwO4lrvOFNHacKSJ1m_CoPE2lFiBKnhYNsR599r651IEU5duQ8d07QosMHQvUH68nGJSy-o-v0hTt7TYSIWZvXIzN8yzTTMywpqdGL_6SMaiDHBG66EyNU6g89mMDrQT1nHQatjSsHyy20mefExyPDWdqeAubrHBKg0ofcAsBTWg4cCCQN9w-_fFFG7-dsOU0FJstKs0bxF0pHe0kUB2WNTqzo65kUGUw3h0GIRBuQ7h6wmPBG1-sALK42x03NpwtFobgL-mwKRrtgQA_O1X4ZXMA01yrTYUNkkeH370fS6eW6a2r_KErKbL69BO5TGhFGbEgxxXDnb60icOWe6d5g_T3Vzcm2x8wsL2yphckTDNV2nMxArMFNScv7BfGkMUOabpKrz0QVFyi-Rb6MgdgwQTisOuE-KiMNUcD_qk9TYOWdkMgnCqSuH4J2rpMuOl3dqWZpkGr3tXEI7_S4Q93Fag7uiXHqJETZLMMjvOio0Gk3IaYHzIDixEXCrbCK84xahzTEhcuvn7RlqlAotZoXs_j1Ks3KUtcB62c4M1QVDQH_pvMmGsmcoJ3ZqwNbUE10Tt3DoIZfz6-07xdO_qtDNGD4HvFOqJl9b49fV_BB7Z3HvOWOztNHzfmyL5d8UUZpEfknOUloM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌بس‌هایی که نقض آن توسط اسرائیل تکراری شده
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/443483" target="_blank">📅 20:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443482">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اطلاعیهٔ صداوسیما دربارهٔ اظهارات یک نماینده مجلس در شبکهٔ خبر
🔹
صداوسیما: «اظهارات یکی از نمایندگان مجلس که در برنامهٔ زندهٔ امروز شبکه خبر مطرح شده و در آن به‌صورت ناقص و مخدوش به برخی اسناد طبقه‌بندی‌شده و مکاتبات مسئولان عالی کشور اشاره شده است، مصداق تخلف قانونی است و پیگرد قضایی خواهد داشت.
🔹
صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار داده است.
🔹
همچنین شبکه خبر با ابراز تأسف از بی‌توجهی این مهمان به موازین اخلاقی و الزامات آنتن زنده، اعلام کرد مدیریت شبکه ضمن پذیرش استعفای مدیرکل مربوطه، به‌دلیل سهل‌انگاری و بی‌توجهی به ضوابط حرفه‌ای برنامه‌های زنده، برخوردهای انضباطی لازم را اعمال خواهد کرد.»
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443482" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443481">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه: قدرت، تنها تضمین واقعی در برابر دشمن است
🔹
اکبرزاده: دشمن زمانی عقب‌نشینی می‌کند که قدرت شما را ببیند، نه اینکه دلش برای شما بسوزد.
🔹
ملت ایران با ایمان و اراده توانست دشمنی را که تا دندان مسلح بود شکست دهد و امروز نیز جمهوری اسلامی به قدرت برتر منطقه تبدیل شده است.
🔹
اگر دشمن تعهدات خود را رعایت نکند، جمهوری اسلامی هرگز عقب‌نشینی نخواهد کرد و ما برای گرفتن حق خود، نه برای امتیاز دادن، مذاکره می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443481" target="_blank">📅 20:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">الجزیره: نخست‌وزیر و فرمانده ارتش پاکستان به سوئیس می‌روند
🔹
شبکه خبری به نقل از یک منبع دولتی پاکستان گزارش داد نخست‌وزیر و فرمانده ارتش این کشور، فردا یکشنبه به سوئیس خواهند رفت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443479" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a78498d54.mp4?token=a9ubCPg4YpeUYoEzDw2q9lMCrDgIql3uTc0bK54VTqfUzOdmdF7eQUemvkZzROTQP1eenKTOWAzNnFskVDZ10KgfL8rkME6oUHLOOM8ifh-V_6YwI9yyEwjEJw9H4L1L7atJEDUwkfU53K3Fc4nRlLNDw3-ijLQ6sXTVpcQ-Jj8HGKN74ibxYubHt974Lyrs9cEe1y0dejwPczlWTdYBrw4Gcevg5MLBbXJhq7LQ96p5R2UJFZ6waCCcs6vKwPpAWfdhp0jygG4mNL32ALu7BZLJGjdLWb-lwpPVOnUG7YvzfC3vvwMrP8aKAfSlDvfK9BtdDlidy2ZjaBv5cWZ4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a78498d54.mp4?token=a9ubCPg4YpeUYoEzDw2q9lMCrDgIql3uTc0bK54VTqfUzOdmdF7eQUemvkZzROTQP1eenKTOWAzNnFskVDZ10KgfL8rkME6oUHLOOM8ifh-V_6YwI9yyEwjEJw9H4L1L7atJEDUwkfU53K3Fc4nRlLNDw3-ijLQ6sXTVpcQ-Jj8HGKN74ibxYubHt974Lyrs9cEe1y0dejwPczlWTdYBrw4Gcevg5MLBbXJhq7LQ96p5R2UJFZ6waCCcs6vKwPpAWfdhp0jygG4mNL32ALu7BZLJGjdLWb-lwpPVOnUG7YvzfC3vvwMrP8aKAfSlDvfK9BtdDlidy2ZjaBv5cWZ4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مورد عجیب وینیسیوس جونیور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443478" target="_blank">📅 20:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS2trs4-y-W0hsw9nA-XmjHubXv5DsSaDSv811bFS-a4hPbwzgHI-lO2TmdXc6pBZRCOSDBVIiE2KgUmvK3uwjWziIeUHRY2Ved1kNUXCA6eY0WP8CNYDMBVgZtcYE5INNpXzX3fxFMsD-Fdk6_Us5pAZj4Ew0UvO4fX0L6Md5i6R2uxpL3Npc0cpQUTfjuBYxIXJOjLajm14COnlItj-108R3zlFNlWcqBe9cnypTT4ZR8EK4agI064-VLq9_uFDFatNk1j_l5xkHfSWbhNA60TfB7QpbJq0JBKbvDUar6TI3LM0vVg1nHER4vvJBuaLbwoKt4JSM13-yphtYMVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستارۀ جوان والیبال ایران به بهترین تیم جهان پیوست
🔹
متین حسینی، پدیدۀ والیبال ایران، پس از درخشش در رقابت‌های قهرمانی جوانان جهان، رسماً به تیم پروجای ایتالیا پیوست؛ باشگاهی که از قدرت‌های اصلی والیبال جهان و اروپا به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443477" target="_blank">📅 20:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM4SqAzzu4qxSeZ9s2xUa9Ga_1VwLZkv8G9cZLQl5ssR_tb6kSppnPN3vqS8PzUWvxso__ASA6lXMdocP2imn3apIfSiUysRYp3SBGhaUQl7GNQsAAFzmSqHmR_5r4FkHsH8E6C50u--gHIhfVgSlpC0422ndVAks6CjABb0uO0TwWKRL8301KPT3gkU5KIbFcpKjgrO7ClCvq0HtA83uxD2Yj05Id-CHoXyueyrP3zTzC0B90c98COpDEDMPEN3p12HKYuZGqx8bX8KzBRJd1XZ5IcQJNdzJZdQazVwSEFTdZM3EAoCSIG_e2AfkD22Xaw8aiuQd_gBI8uPRuJ6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ساترا مخالفان پرشماری دارد؟
🔹
در روزهای گذشته بخش‌هایی از سریال «بدنام» با عنوان نسخه سانسورشده یک صحنه اروتیک منتشر شد. اما اگر از حواشی مربوط به بن‌مایه داستان آن بگذریم، این تنها نمونه نیست.
🔹
بخشی از انتقادها به ساترا از سوی فعالان اقتصادی مطرح می‌شود که طبیعتاً خواهان آزادی عمل بیشتر هستند.
🔹
این مطالبه تا حدی قابل درک است؛ اما از سوی دیگر، نمی‌توان فراموش کرد که رسانه صرفاً یک کسب‌وکار نیست.
🔹
بخش دیگری از مخالفان، اساساً با اصل مداخله حاکمیت در حوزه رسانه مخالف‌اند.
🔹
هرچند این دیدگاه در محافل دانشگاهی طرفدارانی دارد، اما تجربه جهانی نشان داده است که حتی پیشرفته‌ترین کشورهای دنیا نیز از تنظیم‌گری رسانه‌ای صرف‌نظر نکرده‌اند.
🔹
اما شاید مهم‌ترین نکته این باشد که تضعیف هر نهاد تنظیم‌گر، پیش از آنکه به نفع مردم باشد، به نفع بازیگرانی است که از نبود قواعد شفاف سود می‌برند.
🔹
بحث اصلی بر سر «چگونگی تنظیم‌گری» است، نه «اصل تنظیم‌گری». هرچه نقش یک نهاد در تنظیم قواعد بازی جدی‌تر باشد، مخالفت‌ها با آن نیز بیشتر خواهد شد. این واقعیتی است که ساترا نیز از آن مستثنا نیست.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/443476" target="_blank">📅 20:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501eaf8008.mp4?token=oCPyacZjEDH8eUySck5vm_8a0FzW1Siu4kBQ0toVW9Gcq6NMzbiUmf_J7z8MTA4FUZrsMLWHIBfow-Axt45FJMJrGsC3zC4piOSnEwDVW_s4gWmGATm6XWrjDKP5rW-rYhtsirSFVBcTEQ9QOkQ9_IJlRCzJSd14v_i-cvRbbe0dVikQpqH6fcDWrsb6cFaUpe4FcttA1N4R5c9s7Vo-KqOOX5uR6iP771L6K2B3IZ6ZS_HZJCbJoGxGZQ6sOgr9znYpZ1FR3EYzJKvzojAtW58ngMZcodcvJFs9BuJg5LctD_fBssB3w0YNJ8TzG7pteTMwFThUIa_ipmV0EgAu3BGrn1Wj96VHGB-t0nELpAeHChUQ8JYY8PV7LCLp8QaZJs2pRf8Q6QUAqBxiG_YH6Dl_Ovxx-YuDYI2xTd22h0_lJCCD_c0rwSKjMERQgHdWyWuOI6vXqdzCK4sf8yhVlDVlChRcAbfUhEpbmg4W8k0SlT0RF-D0t1Pv3Ac9mWkJYweugZuOdP7_zi5bQjQ_JjcpcYqKloaICK2R-hd6x8YeFBrm89qkWfGn4o6EgyvDEy_T8FgCuLG4q_7-U5PIQXPJbVbKbm4QZaBYDCW2Z4iLel71koFDUYBURllfiQUAgJ1scCSoaogFvMfrB_SqPpEUsvh3RKjHvGksxrNn7xI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501eaf8008.mp4?token=oCPyacZjEDH8eUySck5vm_8a0FzW1Siu4kBQ0toVW9Gcq6NMzbiUmf_J7z8MTA4FUZrsMLWHIBfow-Axt45FJMJrGsC3zC4piOSnEwDVW_s4gWmGATm6XWrjDKP5rW-rYhtsirSFVBcTEQ9QOkQ9_IJlRCzJSd14v_i-cvRbbe0dVikQpqH6fcDWrsb6cFaUpe4FcttA1N4R5c9s7Vo-KqOOX5uR6iP771L6K2B3IZ6ZS_HZJCbJoGxGZQ6sOgr9znYpZ1FR3EYzJKvzojAtW58ngMZcodcvJFs9BuJg5LctD_fBssB3w0YNJ8TzG7pteTMwFThUIa_ipmV0EgAu3BGrn1Wj96VHGB-t0nELpAeHChUQ8JYY8PV7LCLp8QaZJs2pRf8Q6QUAqBxiG_YH6Dl_Ovxx-YuDYI2xTd22h0_lJCCD_c0rwSKjMERQgHdWyWuOI6vXqdzCK4sf8yhVlDVlChRcAbfUhEpbmg4W8k0SlT0RF-D0t1Pv3Ac9mWkJYweugZuOdP7_zi5bQjQ_JjcpcYqKloaICK2R-hd6x8YeFBrm89qkWfGn4o6EgyvDEy_T8FgCuLG4q_7-U5PIQXPJbVbKbm4QZaBYDCW2Z4iLel71koFDUYBURllfiQUAgJ1scCSoaogFvMfrB_SqPpEUsvh3RKjHvGksxrNn7xI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازرس کل وزارت صمت: فولاد مبارکه در جنگ اقتصادی سربلند شد
محمود صلبی، بازرس قضایی و بازرس کل امور صنعت، معدن و تجارت، در بازدید از فولاد مبارکه با تقدیر از عملکرد مدیران و کارکنان این مجموعه، راه‌اندازی مجدد خطوط تولید در مدت ۴۵ روز پس از تخریب کامل و عرضه به‌موقع محصولات فولادی را اقدامی مؤثر در تنظیم بازار و جلوگیری از کمبود کالا در کشور دانست. وی تأکید کرد فولاد مبارکه در شرایط جنگ اقتصادی در خط مقدم تولید قرار داشت و با تلاش شبانه‌روزی مدیران و کارکنان، ضمن حفظ چرخه تأمین فولاد، نقش مهمی در مدیریت بازار و پشتیبانی از صنایع مختلف ایفا کرد.
@farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/443475" target="_blank">📅 20:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNBkLbV21j2zAyRfVnOUpnFN0zciaN0WYo9vg7y97rsrZzAxOv7dLQpCWlG_mhhjWn5yjXvTAota5d5EyxF_Bocr3o1k46_hjS6oycUGGtNx4GrQEFqOVo8tgQSU_049619oUhMMyC57AXtph_g5Ylu--CXBr_VLwI7cw11Z5LHbcLDKldvXlm9MB7uwW5qiSBycBH9Ye0tzlFKeos_oxdITyUAjeOceS2MO3stAFCWf3EW0zH8VjoE7__a1WA4W85mpfTJZVZOSXbas2je6AEsyDkgNLdNKourGrC0TUocoY9M5WfHmZ5Cru0-IYSOtpOd9lNu1PmTEKJ5t03cxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سقای شهر»؛ پیوند خدمات بانکی با خدمت‌رسانی به زائران اربعین
🟢
بانک شهر همزمان با آغاز ماه محرم از اجرای طرحی با عنوان «سقای شهر» خبر داد؛ طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا می‌شود.
🟢
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه خواهد داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می‌کنند. این امتیازها در نهایت به بطری‌های آب آشامیدنی تبدیل شده و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع خواهد شد.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/443474" target="_blank">📅 20:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/443473" target="_blank">📅 20:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d88bd8e6.mp4?token=I2Rj1aufIBcCSmXekx8OYB4wcg01lKKivBpPRvpyiiEbv8_Ud20ASl2idA5fprWHV6t6RM2ayMz_2udZp1W1v1VntTfhQwo77muvB6_BXFDmLk7Lnf0hitnsWWA1q2YBsDQm2COTDd_-V3ZeuP8CbqMId76ZnqKfUkb6G4HSVZ-yXIrlV-nyttyUTyYaJwdVUnbD9sep-w4Y6gw-wPmeham7wZoZKftd-oWPUpbDyLIiD0WrSLevRVJ_hWZPS9adUnbrmEoX3Vqid_SDX6JyIPxJC-1YrsPookzrOuSj0EmkG1Dc9cAhVPBFzPny8_poCFMqUu2fYymG8xvNIVU27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d88bd8e6.mp4?token=I2Rj1aufIBcCSmXekx8OYB4wcg01lKKivBpPRvpyiiEbv8_Ud20ASl2idA5fprWHV6t6RM2ayMz_2udZp1W1v1VntTfhQwo77muvB6_BXFDmLk7Lnf0hitnsWWA1q2YBsDQm2COTDd_-V3ZeuP8CbqMId76ZnqKfUkb6G4HSVZ-yXIrlV-nyttyUTyYaJwdVUnbD9sep-w4Y6gw-wPmeham7wZoZKftd-oWPUpbDyLIiD0WrSLevRVJ_hWZPS9adUnbrmEoX3Vqid_SDX6JyIPxJC-1YrsPookzrOuSj0EmkG1Dc9cAhVPBFzPny8_poCFMqUu2fYymG8xvNIVU27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای زیبای حسین طاهری در وصف قائد شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443472" target="_blank">📅 19:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da9c41bdd2.mp4?token=RCvVU2aja8-tQjm89CpRRILYZ7Pcuj5X9FFFM1xC5SJCP4vfu8d7Vjirm1lI_QwxFnaXrjKvSWDoPIWaqo2Yp0m_hXzsD4ZV6OrIQCV3Oef5PiqlNO74AMM-LQDXFyjWXbtyaAXl3ugGjfFeTvuVhQ0zsVCw2kfK0pRLquraq13H0RwzPr2nNlq4U-ahMbBkrW3Ygk3UEhOMs1kVLsQXxrso3G_27h2kdcyTHnTcu1gQ75VqR7B44GFA131WR9Pv8yRiPaB1GGqRv_yopaBYMkGSAV3ZTEjy4jRbJKqklQTWgcnG1ofr8iLISvbfzYAJBas04fHY_3M9mxKsOgHMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da9c41bdd2.mp4?token=RCvVU2aja8-tQjm89CpRRILYZ7Pcuj5X9FFFM1xC5SJCP4vfu8d7Vjirm1lI_QwxFnaXrjKvSWDoPIWaqo2Yp0m_hXzsD4ZV6OrIQCV3Oef5PiqlNO74AMM-LQDXFyjWXbtyaAXl3ugGjfFeTvuVhQ0zsVCw2kfK0pRLquraq13H0RwzPr2nNlq4U-ahMbBkrW3Ygk3UEhOMs1kVLsQXxrso3G_27h2kdcyTHnTcu1gQ75VqR7B44GFA131WR9Pv8yRiPaB1GGqRv_yopaBYMkGSAV3ZTEjy4jRbJKqklQTWgcnG1ofr8iLISvbfzYAJBas04fHY_3M9mxKsOgHMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقاشی جدید سیدعلی میرفتاح برای مریم، کودک شهید میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/443471" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
