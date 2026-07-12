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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 180K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 14:35:32</div>
<hr>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVFtAQ86MAylaXfE7xOaqQ3mHT6fOeoOEW2DM7IobdnCoVwfo-d93goVNcNkv2b-PCYCzzNWOha40_pn_Bqu8QAKblkDrF1Xw9wxIMfhDA8oOf85yxA5fOwc-xKoNZBC3NJrIbWqxwPWPWT7hADqt5GYcKNf021KJTkesZFqaV8pn3Okb_u_RwX8l2ol-N6XYm_V5d_UczPLFxrXYR4tBN5YMO3rKTySzd15pmIM8h2VoLUR9Q8QBD944DOINdGvKDvjJBftGTQnE3XKwpDvyidhi2riQOdGyKBcEvQQjvkznX6yC4bnNMO6fqgaHgvK3Z1O1jng-WkeMYJwROWf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvULATMieiLPn4GUZSNcv6Mc5K65DginSdhqU8Yk1YUM4ZpVxwm8W6KLY5_XSV--29MFEKc11Os2MQRGrKRrR3zyjXRA4-XhzLka-Vez6jVMIhmXR8dWcvkMDxJRsH3CPaL__QUxDw3R3fjpIq-GHgbfJ_HRhVYtBbyDPH3i4Mi4Qn4Eay4mlqb7G4IRo0k-TDiz4Hbzz6VczWwKqEJUfs7GNJRAxaEeFOM9IA1rz17u4Ov0j4CMPqZTjUQjBLAAjxCRybUrgk7yNgkGk7sfWSrQi3BncNq_uLnDeSV_rQKavPGsLMCXfApewE1tpLa7TChOWMiA-MAvmE2jLAem7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF51OQyDSp1xoZijJUQBXccZOt-aQ_8tKQtdo1w47FLcLRc1pjREjqAc0qy7L6c28qLz9Ohng7wL59REulM201hrmJNfz08PNhQXCfqvVumC71iwq4Rc4uB6vEwiNCzClnsS_EjHPwl2KTKbbIAQ63ABgLXWCIZODW0L8rpe7dYvVYvTaANg3CG5_MLsOc93NNrN2Euqe0_Wj9CgOY5jCJVZw3hHk0IYDJ0JDH_8GtyUNn7ozqJLYjx_h9fiJwnE_8AytGcjIALjDgJL6CXBohhQjcAc1JwzW3idCcEvaVVYjrs5H32fjPhL93opd7Tz0nP-Vs40Uhwwp0h1pAsCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTcdl1PxT_ym1lUzYmLFKk0kM-KMwTNj5WQoSEFOQqfdMnacomg4QJ6cAiSetwUFIWpNdX7w2R1o6A9RNmaS85xntGpTQ8RzYOqdEn_srUMfZxeMELP8EhkhBL4tKEmrX1_di9X2x7aYDr0Xn5UEy0OyvhXkliO-_ZBkANw60685jn-6OYCgCiSTBniY44gl3UcAezoS_ncRxJJkfp7VRDqbmXUp8g5h6RtPaCdOfX4kQh-yd1boSZ2WcePN1BMEFu7lcjeCoKntzg61adCFIJlHrHqE34ezozxLdQHL_wvLCoTw6C_-a257I3pQpS9LO5AE7nbz0W1aL8G2GG_fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5JO8oj6TiPXfxFXFBEuLvRR2Bsuy94cEGAXykRSA8cSSKRZgQIMLhJshrS3Q-oyEmr8H400ayLSp9v4tC7lGeCNC9Q0DVt_n-d-OIvTPIhv1zVGCLDQTiZrCIamQYMKZSOesEEg5C2msFvjd0KXB03mtXO-M6G0Jj9BX30NKyei9Mux2LHFV_Nqojlac9BvbgVQIN89ttbiVBYk6v-gWzQIeyB3-IyFQDVXUrAxOfQltC_2YAH4Zc9glqexmN9YwJnkWLYMQwlGujeQ3dg8Wkuh0-6qxMNGUsWJ3pEQb9KwS-F3WSv1kAXtpVCjl9bpeH56Ig-XFb5fkUYGDH0kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxQXll24mOFqniywF86zHqRxVkVRtLfGz6kh33rdtqOYUSN4kmNh2NkmZRKTrF8DTUISOULKLrca2BejnbnfV69vdDUqqyjNVn8NZOMjhPlOs0WW9gfhdQ0ajKovNPyRPDmQ02BCSVejSSRpx0PAYUX1E0uetnpZg8DMFetJAItkOVbGrSNeymMr4kfgmlHiVswpPch_7VDETiU_-S6ML10PN1g-iQCO2UKbISlb8cxk9Gnr3JxcxNrfVQz9n5FGPjr607dc6UQFeWCc6MhwmjNAHs2Tz-4nL3FhTE4S5XSUPgtbovAKvpbbNq-mCFKWJyGUKWB0amDAULUehCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB61_-4et-npGTWkU8NgnGhAPRZkL6pKlsoj619ZtOvrqSHNw449PhnBFTsWk4MFHyp0soElm2Cw6JWHJdzey3raaxY8UvF5QFU9kz4z-SGQevsjfgFWneJ2Opoyiy_66t0BbHYP6Av3S9F9l8ls5UuXd9A6E4qKy-q67dSyphukUokdJVt7XR8bdrIRndcnYBZrP71RhcILiBbEuN-j-p2xATpBlaJ1ft42EXMslMxTFk4RaX2XwvKReC4LP0OqILPXmJ8ZNTswX3ZfKWm9bVqIaJ4ydUD8n0fjXhb4WgYJLQhcL2BW8u-Si7X2sran_uJiYiliUySlxtQ7O-0EJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHG_1B8n8RvtXkKBE7rWeTqDsRP47F56MLCmeLzAlNbXj6NZS05ytPJeYT0HNrpuwypBAS-IbtmUyOfWRs-66qyL-A12KAAQVmKNcS0daiDN6mPl1n1yIG4XpqWjyBcTWug5dcwclj7EvKv7jhagHTfdp8z9oK_BllCFS1VU-W_vDMpBd5bODeBj2Ae80OPzfJn6RQItkAzdTSpCbkcSBbo4ye8piJ9pIAjDUtJPS5C5Fkt-1t5HiRKpHviNSYR1kh2WH8555W2PbdPjFz5EknO3F30i5AFwobZi96Gk71-rSzezGNVRUL_Ej-66qO3FifJOWvbP_o2859JOnMwvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJTJxusanixgKxANJOn2Z8UqavpcDW4MrKxUrX_2sIeDHRr-KJATF76LAnp7DM0ntAzU62wbf3G7JBgZMaGsnu-qODMXxfbD9gNghxP40zC8Nqd3Zx413lHp7B76yfILIzJKi6grFO8_Z1dn7Jx_fYGvvwfYdf-xa1Cr-aibGDmHJLBRsTnXoCtBLCQ46d4HyAwIgo_XCdWtRyiUXmfWQUdmtHaUT_W10JgPOcpLdO2Fq7n3aPD0iUXC62rs5GLfqn661mp5sXJrLV8Xpdp2s2X_phA_Xa59-F7L7ooGBoWNWcJUlMcamLX37nVgwqQXSnLGQiNuODckzPyyzDwBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVMjXNhhi-NHuR80GLac8HYbXdzZy4spU5MQTiUwUyeX_wzM8lpYXw7V_WS5BWkBnrLyiIRPkIFujiU17WCa8otAUCUWP4foQIhTbtqoN39ihmQHmFMEBXvj_6Mi4683ivFY6ajKGk1mNtPs23iThd1Ozfg14VpgLcdG2H1VTjFQon8e0u2lhsQoDPAIkg21KLl1QzEuYXTMABJTr_cD1vhkV_x39k3oCpX_OS-3QyRMhnqLCqd5EfO-0j_mvVMvM8BF3_tC31EDdYmRdzQ6GEoouxrx7NF8opaxbJOTG7pLL9lP076KeiQEqYyIzyYO2NioMsX5VkWLRpN_pBVxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7O7-qLkfYWOHBltPeXc3djqJb35nVjJzjPYJvxVRzFqV85_lr5HvDbirnm4MdlN8IPKFxqQ2iPBJAanOVHNAgGucLeVZbnpA4oFKHRXaMGJ5bWuPU237nSPdMDEO_uT1utycWaZnph5RMQz-zWGHpdJ-MAEG9CbPk64cJIAC7AAhd1vO-n5Dm3eafE-sU-v_Tu4dKb7Vjv_DmMyoN86TK9ePKPYWy2lHCQ-c4uwvFKzJJIg_9l9zAkpw_Fp6hleY-SUSRImppCotZVm_qAiaDX3J5RA-H6esKu4zmqTAbkz9SGLTKHxXHE-vZxJUfmemkmwFQzz5_FLDi7ExgXXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=e4vI44Xyf-o5Rer-ppPIaA7WMH-CQpD_FVFHwberwzBcdSV0YZVSrQgp9XVOBE-VcnTngeGQEdeG58r-uJvbrNkl6PCXpmWVkZClK5disVO7ojbkQilMCaWVd9s67V6QuVnQtZWeRMNwfKge99WDOij_MwIwEdfTaECxxL17gCxG6kGUBo9Y0m7yZ1U0ENkUrnLDb_w348r0D_ybUum7Lh4om0SDHgKTt0yN3AhAl69mxY8shDhC7iXEaMBTPOu4HaM-B49Nib0Ro2m5rS9WaEolPxlnp3zu42swWgFfXt4NRpKITVjHMZFv01CelOynLhSvv4d1Q5d5KWwLxAEstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=e4vI44Xyf-o5Rer-ppPIaA7WMH-CQpD_FVFHwberwzBcdSV0YZVSrQgp9XVOBE-VcnTngeGQEdeG58r-uJvbrNkl6PCXpmWVkZClK5disVO7ojbkQilMCaWVd9s67V6QuVnQtZWeRMNwfKge99WDOij_MwIwEdfTaECxxL17gCxG6kGUBo9Y0m7yZ1U0ENkUrnLDb_w348r0D_ybUum7Lh4om0SDHgKTt0yN3AhAl69mxY8shDhC7iXEaMBTPOu4HaM-B49Nib0Ro2m5rS9WaEolPxlnp3zu42swWgFfXt4NRpKITVjHMZFv01CelOynLhSvv4d1Q5d5KWwLxAEstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpiYey0uDz-qT5G1sWOUQ8bqBi_NsHznCrr7NP-sL3b00AYSVs6d3KwBVUC6LlKIAc6N430HpqwShH_HvV6M24VUv8K6sg7kZ7DTxGOLG_A-I3JsYoFhaWgI150liIlPUEniI29X6vkF_sf08TCvqSaV2Ge9Dd5aasmEu_luSeqeczJOSlSUCmttVuWFvjEeOA3iUAhmLkFk9z3u8jLNdxUkZQeT1r7auyqxJggibYitcnCIuDcQe9q9OF3jmy4N9Uc4nCL6DFWYuU6Ul2dWpMXmvfiH83LbrnnNkQfhlDHwGl3refOskdzTPSraSYhfm9GCHUAtFTZBAsgIYT_0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow1n5GGfqEcCXrE0e-A2FHoU1XBELyPpDZ7fDbs8asi4DfQpXNszmQLYDB0YoozJicsaGZz1d9rWP0Wl41j-QCxLAuvuSoc3_moqkwVsu9nkMIX31cPoK9CEVJtoHWkqgHjwp-lKSYwi5Hu8qRFZwRKqh8jA0kF-p04cHyqVvyevJoD17eVv4Wzo_qe1dK1w-R5mkebN3fSCrpapdZievL348430VvQ7VeBs8iUcUl-ZCCcneLV4dOWOfVm7tD9iKGg9XmwXpxE7aPjIz_aMjnN1Kf5gR6qajGE8U2_wGckI_jF-p7GX4ZiK4eXVaTAvHOcY-olkNaSZN4jsXIuacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=Amub82FfYqW69F8TqJKjDXw0KdhS3vq7RLWGeNqC5smtjRdVvoA94gr2NjZIgA0nyflq-oUVJ5rrXLVzDT4J930l6ynBwTD0UoR_SVbMeLIYPR0TEfMFSsALJ-C-clQUl4Dxdp3S6NzbNEEawMD10fSPptwGK8su4GHvaH-smlHfW2O0wEVMV05ahVKIyizECSNi2S-3QBcVfVkDzR0SaEUpsSEbyidRcDSYBd3wnF8uVYGtqq5JjBbOTzNs_G4n7kNzkOt5rE7zhBQAhoNjyGCvt-UCAItJ3NgXWCg_XAfJvU-e6GlGZR3B6Mz5Z7LyEifeh1GIsskA40wauPp5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=Amub82FfYqW69F8TqJKjDXw0KdhS3vq7RLWGeNqC5smtjRdVvoA94gr2NjZIgA0nyflq-oUVJ5rrXLVzDT4J930l6ynBwTD0UoR_SVbMeLIYPR0TEfMFSsALJ-C-clQUl4Dxdp3S6NzbNEEawMD10fSPptwGK8su4GHvaH-smlHfW2O0wEVMV05ahVKIyizECSNi2S-3QBcVfVkDzR0SaEUpsSEbyidRcDSYBd3wnF8uVYGtqq5JjBbOTzNs_G4n7kNzkOt5rE7zhBQAhoNjyGCvt-UCAItJ3NgXWCg_XAfJvU-e6GlGZR3B6Mz5Z7LyEifeh1GIsskA40wauPp5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFyDdvDXFTPTTB7Dqw18n5atGer_0uuoRYzaUJrL4LByoNWArnhzzLSGpHocitRo2P-9l9XWq6cpUAPqSGidqlK6WR2F3I7fxhNltNzOdTC-_B1iRKhT39t5LnNQBz_m-OEE42Q8nrZbXhx6cfbXq7pps3PY2jkXKTg37p2A6JL3chNNzkS-VsvX-hlJg0f0P9jwRzq_H-NfqfmDWyQrRL2uWDpt-HUQYlmcqeHxaOz-tfLrk9UepQkvTimnG6LOWTsulF72VGR7gGZSEKZdwwXs83DmiIMG6BSh__MN8Mw9WGM-v9xwwCHCkIetVaVQ1BSZ94fwFhoEPjfSTQjEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmYDJ0JztKQiPXCUdnRMkEEMPtEqAR10MxMpHf7UjDuPdyEE4LRyxslvJkonc9zQkDF6fzFDQs0yimnPp6v6Q5eZCzoJaGym2zMQMnKgWRPax0AlDO9cfwEjKo2uEbfI2yFFL0Zal2l_LyVBmb8fRKulWkusTIp6fKE2HkuntIDZcnpS0f25cc-u2w1Xv_qO6phdkws8mMGIgtZtyndKHnqZvo_JTraGzkHsafUy0PgLvnkSzy0-oyXAI0KOSmLdXu-M8Wzqv49cFEboOp21h-6E6ki-cVY3yCqqak1bQzriO_mY8TLGfTbyiTkwYe7I4D4t5F55f29u_-OHuYhb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UofcYyA1ZwMONgiknZJU_3W6BCG41soA3v4sfYxj2KqjElcIgrnV4J5-Uk2gwDuDPhnoHKnwHhdp6FyJoMEEuk6RmMcSesyFe_muyNebIBTNjLjXmWaUu36JU62O3D69VlH9I9D6F65aCRtLnvNJVToyyxHoRkOhcMbBtEP23O0ex1AcoXCw7qO58qG6Ye--CMzkZQN0wvgFjowkLBG-qGC4UU4jwBDdtmg6cUrlwZZMb4I4Knil_s-MYC_IDvPLIkqEKAULzSPR57lU9UI6cATmkKKtKluh0E82MD2VmzVCf-kUVpBc7uKjddm2jmNhwBd9fJBS0-cjAXt97d0_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWcR9y7xUqXBfdeFvBZksxPFwx_yndUYTgS39FrJtQsh-xJdUsA9SzIq2DBajrbqH8oHSx7k2kiF5kNUMI8GB1JdxEFIdAGuLHrlyynLyCk98IT92jXQHK8xbrc4sqtiqRYOXR-SifzLMCSPt88-A4XUYWRv6bctX-YNpb5MMhCnq2FFaTKj_r0LUI5JBngsYDWza49Y83OgsVOwAjS96S8Hfl26DPZiN3P8p1q91IFvIrMaaHA0g3ov9Drnmuh_C3aWtmqw9N9C6uTy083-TcBqIQHWC-0WPrOrzUDjUgJq5cJiG7VI9AiP0isLi59zsrEXM_4j1BfDl3BiTmLaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=cK8hNgsGhxPkDWaSUR-b-O1YrZ8mRKoEziGmr-UL9HYPY51qFhP18hCFt899lkYAd3srXxfbwHVVlmaf2aXAS-_uBspKgoNpOHqlbTYMx6a--NXiEMsP5pbxhS7_sJV34EulXTIyV3zlqsc535B1LgPHftvlxrY26hObxVnbFrIuW1OOX9oyNADLRlpKkBp7brdc2RLetTzW0pb3ajK9hu6obyIEhncD9tL32GsL3SPwajjAqVj4tpf1Oa0F0QMGnuXwkveOdEgbkeU8lWv-nXhBzFymRsz-j5CPfcwLXhDNXMir_-QQ5SCNaMQUXoSvf--8dhzeGp_aw0IqzpaH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=cK8hNgsGhxPkDWaSUR-b-O1YrZ8mRKoEziGmr-UL9HYPY51qFhP18hCFt899lkYAd3srXxfbwHVVlmaf2aXAS-_uBspKgoNpOHqlbTYMx6a--NXiEMsP5pbxhS7_sJV34EulXTIyV3zlqsc535B1LgPHftvlxrY26hObxVnbFrIuW1OOX9oyNADLRlpKkBp7brdc2RLetTzW0pb3ajK9hu6obyIEhncD9tL32GsL3SPwajjAqVj4tpf1Oa0F0QMGnuXwkveOdEgbkeU8lWv-nXhBzFymRsz-j5CPfcwLXhDNXMir_-QQ5SCNaMQUXoSvf--8dhzeGp_aw0IqzpaH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8NzOW9l6fiNidf2L_HPwNP9BhMHWxbOU-luEqlG10an1G1U_Axfz-5LQ1cXhTHQ9-YPJ4wxSiMlbzZmRB2kLuGQDdUmr4mLTBvqImFinkcdE0BV3Qb4OdHm29oWznsoDOtRkg-6YPrQcD3_YBSa5u0yIJd5lG97KJOYY4oBb06U5GukseT1b10JeL_rtHRCsRpwOQw_20ahLfm12pb_q79ECTkh_2Ku7jP7KqCAQv_duqPiCW_q5E_8vjrilONVioN_fxS-1SSigSlracXqtIw653jsoxqrajJ_RxzYmkFsq-TDwINc6-jKBpz8PqQYHf0m8zb-21MxFzRzgKNQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=VXMxhD7lbN1zklWH8WGfpqu1Iz3_JblqBAFvVa39eGM7PYSdoWyp6IxcuZa-jd6_6Bn0579zHvOaZX243cQyCuslsM30LikMp7Enc3ogd9gAjBZOQ6MOhMUXrXudHFYBD-QeodPk1oENrbOOL7rfwSKBRDqsIagKx6OfN8n_FIploUI9uenuzQM2VVH6Czkq-DHjXLlRD-DlJhvE9CXiVKy7NgtcVpDLqciZCaxhpGsYh2sFI8HZfuRkInNsUbijyErAAqEOUNAGN2zOwND2Ccm0alvfhrN8tjmxiDveG4JL-8FKsOqFdu3PQgG3x6UjletuwDYpb6462yAVtv-yqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=VXMxhD7lbN1zklWH8WGfpqu1Iz3_JblqBAFvVa39eGM7PYSdoWyp6IxcuZa-jd6_6Bn0579zHvOaZX243cQyCuslsM30LikMp7Enc3ogd9gAjBZOQ6MOhMUXrXudHFYBD-QeodPk1oENrbOOL7rfwSKBRDqsIagKx6OfN8n_FIploUI9uenuzQM2VVH6Czkq-DHjXLlRD-DlJhvE9CXiVKy7NgtcVpDLqciZCaxhpGsYh2sFI8HZfuRkInNsUbijyErAAqEOUNAGN2zOwND2Ccm0alvfhrN8tjmxiDveG4JL-8FKsOqFdu3PQgG3x6UjletuwDYpb6462yAVtv-yqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=mcmylEcxCJoBszwXQOkamVBw9YOgCQZtC1ngDQt5Bc31zIoeidgFgSI1LPp9ehuVP5nG8bTU1eC1HDsDYDT0tc5l0KX3Sw4bpq1aHkxq_gncluGcCwy1aEpua1LajuPwbb8D1ATY7atRz0tZksJbo7lJgQ7pN8uZb9WxkDvU3Kj4iYfVJWUFpeQZp-fdwDae1mnusKhKGtw9WTFgCMOYYAO5HAOPxEe0fyKjS33wDkXlhV_imuCeMl053LIFr_UC9t0bw4x3yC-bSk_OvQlusHK2PtqRcctv_oAXbb3xN4hHA5PGSCuDBjpjU2rMeaEbVF95kERqLKsX5aVWWgTHOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=mcmylEcxCJoBszwXQOkamVBw9YOgCQZtC1ngDQt5Bc31zIoeidgFgSI1LPp9ehuVP5nG8bTU1eC1HDsDYDT0tc5l0KX3Sw4bpq1aHkxq_gncluGcCwy1aEpua1LajuPwbb8D1ATY7atRz0tZksJbo7lJgQ7pN8uZb9WxkDvU3Kj4iYfVJWUFpeQZp-fdwDae1mnusKhKGtw9WTFgCMOYYAO5HAOPxEe0fyKjS33wDkXlhV_imuCeMl053LIFr_UC9t0bw4x3yC-bSk_OvQlusHK2PtqRcctv_oAXbb3xN4hHA5PGSCuDBjpjU2rMeaEbVF95kERqLKsX5aVWWgTHOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=BlS4BRQBqIf5IqVFK-iHuM8DefQJ3dcpHQFv-wVpOwaIX024EXZ0JmL8QMflMdsF2j2JRVDTCjzRCIYdFSJo1GrqRAmb6hdcQNoZ_TlSItw1NOSFMrqQMsakNpSRmTWXuFvqfSeaKpiM6a2DTRqNvmPrPyqR8sQunez-wPO1dTB8Ct7Kdt2Yn8Uid9Zsj3m1HkcOGPeX-sjsgQIXVgSXUe-W_pCZMkYZoYN493YZL0rgly6nzay_JEF29O9-FpqabDlK6pMx1gR5qqWZEmDRXMpE42oSJ3SxiQrOvdkp4lL5SBMJIsuFEbxXxIlPJ0HajlO1hX9j_EUcs_cBsJ8ZroJISvbIzjfkcYSBONq2We_Gw9lHj8uVyCRP6Ria7R_VAREGLbfq5hD1Y8LJvCDrIumfTxUYsE4Db1mmo-NBjbIaUWlhuOAudREjMa22mhySXoOKy_JaDlzlwwCA-33pad2p_7CrCCrbG2crz5n0iVS5XSvvPvEDP8R5wqUPeXwk8KJ7tqwXc9DR0cxdCRFEj-Y5ci9B3113iaJhnQDsDNC72CZg5gXR0lumUQtyUTUYuMT0ZL5h51xC3kWzElseG6RrkYfuq67f0I4devBDcYIiN7TJ0yeInx4Czs53FVexlsLmibicmVgcvsoZYiNiQSM7MfmKWDuLl4pLgrN7ZvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=BlS4BRQBqIf5IqVFK-iHuM8DefQJ3dcpHQFv-wVpOwaIX024EXZ0JmL8QMflMdsF2j2JRVDTCjzRCIYdFSJo1GrqRAmb6hdcQNoZ_TlSItw1NOSFMrqQMsakNpSRmTWXuFvqfSeaKpiM6a2DTRqNvmPrPyqR8sQunez-wPO1dTB8Ct7Kdt2Yn8Uid9Zsj3m1HkcOGPeX-sjsgQIXVgSXUe-W_pCZMkYZoYN493YZL0rgly6nzay_JEF29O9-FpqabDlK6pMx1gR5qqWZEmDRXMpE42oSJ3SxiQrOvdkp4lL5SBMJIsuFEbxXxIlPJ0HajlO1hX9j_EUcs_cBsJ8ZroJISvbIzjfkcYSBONq2We_Gw9lHj8uVyCRP6Ria7R_VAREGLbfq5hD1Y8LJvCDrIumfTxUYsE4Db1mmo-NBjbIaUWlhuOAudREjMa22mhySXoOKy_JaDlzlwwCA-33pad2p_7CrCCrbG2crz5n0iVS5XSvvPvEDP8R5wqUPeXwk8KJ7tqwXc9DR0cxdCRFEj-Y5ci9B3113iaJhnQDsDNC72CZg5gXR0lumUQtyUTUYuMT0ZL5h51xC3kWzElseG6RrkYfuq67f0I4devBDcYIiN7TJ0yeInx4Czs53FVexlsLmibicmVgcvsoZYiNiQSM7MfmKWDuLl4pLgrN7ZvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLdMgcr8DJLKKmpzf5EbdCMvx8ew_ZeVL54XurU1xsrKw6fa1DrbVXWA4P58kqU5Ppc759Q_gHgrLE6vsapuujOF4uYp59c8dQYRbUb32ReCdrkQCR8Fj2ghfZYD5i3r-QCQwxx8U2NvCM2qlVlXGZM_hjMr3veLJ18LFeznsJxl9R1-CgBlntM8LABNepUlw3PKx54qIIKVGTw4YXX7t0WjW54T3kLOsbVYCQmvk3mLgzwxoHLf1pnzGM76R8PSCu9u4JOqnYOjTGZJ49CQhUTxnvW_nf9XpD_8vzwE1i-JUFkwke_F1yml7J2x-Fk-HLYFC6BVg_rolfawjGngfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=a3mp9ja4qbpurXuh18kwhEU4B2b3Ufx0qLEWb9CSbMMYbe8VlOE2U-vxgJAbqG3JwnRtKDhFzZRQmxRIP4gvBxQVuJdhOalraXEUMqjU_hx_MaSLfFfINnNV77_kMlsR6l4SEWXImI7M8R0Kl5Eg1eCe8yBJHy3u6aMZISZHJGUPHyd-8ulp8rSj5sVLEVH6aXnot87t-spfIMu9piDbwZsUXl7m8HYrEBJQZX0_2oHRvuTbdzbBS1Nx8YPObzuDMduOWE6zdw6IHFvpfvGaHbCpRUU9LnWmPf6tN2vddF8-CYYdcauGMiuRc2CkbsW2VwVQOrAg3hnvE3xYbBASWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=a3mp9ja4qbpurXuh18kwhEU4B2b3Ufx0qLEWb9CSbMMYbe8VlOE2U-vxgJAbqG3JwnRtKDhFzZRQmxRIP4gvBxQVuJdhOalraXEUMqjU_hx_MaSLfFfINnNV77_kMlsR6l4SEWXImI7M8R0Kl5Eg1eCe8yBJHy3u6aMZISZHJGUPHyd-8ulp8rSj5sVLEVH6aXnot87t-spfIMu9piDbwZsUXl7m8HYrEBJQZX0_2oHRvuTbdzbBS1Nx8YPObzuDMduOWE6zdw6IHFvpfvGaHbCpRUU9LnWmPf6tN2vddF8-CYYdcauGMiuRc2CkbsW2VwVQOrAg3hnvE3xYbBASWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=bxlb5Sn33M--bMxFS18CJkd1P53rfX0bIsGvv26ulYLEfalNSFW3JTR-Vuo6wD11ZrRig04yVmaDmviK0jy7iK6DuTXxfCzbcFe9jQEke1PW0HQlmfaiEtuLHSt2zp9Xc7bk_Vt9f0DdOveSlqcrtBgOjG5Jwwf-RinUqvZjFOq6EZDEpKElVGwREmAVesHJtsHcKaoxAtFnBthJsjZTMzjQ3DPyMkIzb73iH9OAE5BnPI35fXBuWqfZA_RF20ChjzVu0UAnqtofbK_gW9BqN9Ab5ToEcdhDyrovYFQtOHpX2fnPdirC1I55_dvv9u1HyN0bxBmgRaUtiL-2BVWbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=bxlb5Sn33M--bMxFS18CJkd1P53rfX0bIsGvv26ulYLEfalNSFW3JTR-Vuo6wD11ZrRig04yVmaDmviK0jy7iK6DuTXxfCzbcFe9jQEke1PW0HQlmfaiEtuLHSt2zp9Xc7bk_Vt9f0DdOveSlqcrtBgOjG5Jwwf-RinUqvZjFOq6EZDEpKElVGwREmAVesHJtsHcKaoxAtFnBthJsjZTMzjQ3DPyMkIzb73iH9OAE5BnPI35fXBuWqfZA_RF20ChjzVu0UAnqtofbK_gW9BqN9Ab5ToEcdhDyrovYFQtOHpX2fnPdirC1I55_dvv9u1HyN0bxBmgRaUtiL-2BVWbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df0-_aq2_Bvdkj7bG2VsaOr7rNXv8EF-tRRdVUH4qlVQXTsVByyDiD144oF-1rXIl0Ixq5Fqt2nMEyn4Jd4zgUO3pIslPteNt-ER3e2lKOxOVHP-48SiO8Y71hHxtR5WWKKHwKhiWDkwtRr6PYRMUzc4xsjRPg3NKgiZyRvyZQRR67tjr3JWbs_e81hh7Put1eJeod6dfyTNdJsEdKF6OEOmPGU1xJzVX4KTQYsgu56AfK6m9ohZe0yesBFFurlWInqeUIc19E37GcVsFwdgOsashDLWXHC5kaAsokIU4ousPYMAyG8iF8tjpVaLU_lN88MP_RBJRqVfR8QfrJnokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmBMfK6AMY3NPZ6aa5JN7WwG5V4qOcNZ2QbJcXB8Q18G2a8aTuqWcgrHeZPiGpk5yOGcheoR0KXYkQguyIjL8FGGdXrqktZk8VyeTbLwjehjmJ5AsJHVu1ODEEVjbMS210SBXFBYju1UAqiokDRBv74UrxQXAaoUEs12cETKqFsUEjxiJdOvRewyWGuD1lrL4rN2q5S2B7b2Q1Y05uWWLx7AF06fq_RzHulJaaAhmdbi33JgqbnsGXgA2qJ6HCVtbnKKQ3pTjltnca7oA0ROxQvqHH45p2jCvVS5pzP-NsjecJMWzDJjRzVgsrBJD-LXIFG3IE__u6qMmMLLcNvUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcz8AU7JXFDaRmDM1SWO_miSo8ObWQ4Hvb6BdG1tuersRZcdgKDdASh4VAYhOBzhs6zloRoC98Qr2kIl9Mk2JAr1S9ilxZeAe3lXJWv4Q6q5jvZGBSid8CGn1RL2UQmph_84JcZUSbCmpU_JMrbL3P1IZgSxGXMED-qgwrM5ciT2lyNM77-MoHd00Hf4ksxLgvweTAWZEe8_doeWRrtQc3jbGSHyKADIcUY4AYGPaVIVaDXU19ma5iNNuw-YEnwf9Mw0-JPTStf0d3zG6u-p-H4dQXJjhHfC_CSGrZVNUOVj-FwCKRhwfoLw_0Aus9LDB-dLys4ys0zV5aivqgaBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxi7UaNmaquGoZSBL0twav8zz6hHDoEqbxe2vsPqUw9WXYLlGNQTaBuoDdckJGwGc5LUXydwNHWp56moEcJu4cmS1kcsD-UC7ftmtBJpNniIKQXklN7UBiO0GfDNN_nRofV9QR9aDI8ugOluk4tea2HcKC6oyckxDaLPXDDcjYA2OyLfrEs8hgPwMyDjtMgrWmNoALNaEeAyAUWycFc3anpw9hizVkPg3xdLX9Mh2y76Y_ztU1Kx7YkYZOrLfUBNh9yfJdgPAF5iVDYSfT4sNVaQTQxW1cs5sSOdshPFfTVd3uS88M-VCRE1AYQGLWNbGw_-UeG3P3pB1iUuearMpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfFsUW9aWgP3Vxj6x-mrNmVt42gALQUOXRIJ5Ikbux2OJ-1_kL6ssrILAVgrRPZnoSWezDTq7hDDn7ymY_jkjE-zrVTOm7hoYJpthFoepgJs7t2ehzQ16dieYAjNNjpC58wUhYDSUWghBxWWYi_LbSUMNlf0EtsYrJKmVCiCC1p45wzGlvasmwm2JxpJtjyKrKctiQRQOJAhIg0bSGCOHa-ChyXQ6W_kekZw28YH3NzVvYId2v7JmGrtXxG1uYbJMmNaZxohDbQ_AkmepLINQBbouXn2p_lFj-WEzRmUlE7MGsCw0C4TjB7HYBrPeXaASuIQ4Gm8nedCn3Ro1HpEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWUumkYlE6Ao173-uT-vRYfSkqbonPWVIfZStfxGSqgqrD4cnlMq4p-k7Jq2UOzIAHtgo2y7BzAAabf2madj77oBZCqnkl48YHC4esGdQor4LIz6A6f3kC6tWR4knuJdvjWy0X9BSt_niC1PHDJQJ6WPTkY87Z2WtABYuZyyDUxMtqZ6_bB-jyH26CDpXvKMUn9w1Fyv7bX6m_qZT-l7PNeSLDYXq0JpEYKAPkX3aYhoLGycjnfQ9SvPf2eU25hGERLT9-KVFCrmQ4GxctpJwkwedmsA6pMivEJjbjjC8-oMZP61LmsjuWPOEp5tjAyQ0C7vwMSBNEnoAYtZ-y5nlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VENZUwfHEbD0Qti_wPUP9I5-NlgZyQziZwhZGQwGZY88yLzdaP0WUsoEZJRsGZQx9MrwpdKAtfQTi_cMFp1jenbpu0QEUlAIP2td6PDF4et8TT784Umf_piWO7Lgn0NIzpHOcS5iLaJqQc5gtdZBCJekmHDpv49HrzEw0qbbJJ5ZALjD9ajcYBijUquHRhcTxvpKYqyVxq-Z24aXyWw1UBIs2yDPdZR8V7FEGIRtrUpIH8SRxx0ebOZfKb4mU9LpfUOPynNtYiO0rmuzZbEvjtvr1Sm6YF9PeR97MQU4FsEvv-65qXmCRmlg-DERsei2Q8HIOBYTCuqfUAb0GdNcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NS7-CcsC8YyXHExJXbTGYcq1DBACWJv6pJC3ma4lC66IKBk8yZE2G4oI5J822Emg8YYod2PB6BKuqwhr9THl6_UbrHy2yfqlmVw58RDnnflcybfi4bZ7vFRZd6doyv2lWRmWl2d2BIhJ36Xf68tpb7x4FPrmHVztTdPrxcmC3qdS50vOXP-mWbBSGT0GP_9FwVbnfywbvXzcs_fkS4tQzeEfu-KgXeszOrS9dWtMYndxjgWV-CryvKaHyM62rIM8F-wNMAqXEikFdXyq7Yxd0sWy44J8OLrJS7DjnrplVy8lqO2JspyeDTFs-Op0INIaNzJ5w_g_QN6SxnZBQ-zmJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=lYIt1RSLU7oNnh3e0EUCCIYs6St7qKTbnxu_0NpGKlMyjpSI8X6I2zmcGiWvNWa6yakcnm1ZnEp1UYk2Y8tGi7G0des3U0P2yjQ2-0hKMTyNMQbBOR_IpzpknnIzX8hUAQf1B9UcbFdv3DcA71QbrUeAhOwsIb62zelrnNfTaXQYMDMEuY-sAnse3zlPrs0kib-jBHPxLG8VqJYYx7eQz64bRGqrQ-E1dSLd2wgF5OuSPDC2URknpU4p2n5RNJGxT6vhP2KEuYvpA97oddHmVixF6EaExVEaIdGGF4od0EJA4E_uWOJTzFVyDwg1jf5XO5YPWeANWHcWLnwKHQUIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=lYIt1RSLU7oNnh3e0EUCCIYs6St7qKTbnxu_0NpGKlMyjpSI8X6I2zmcGiWvNWa6yakcnm1ZnEp1UYk2Y8tGi7G0des3U0P2yjQ2-0hKMTyNMQbBOR_IpzpknnIzX8hUAQf1B9UcbFdv3DcA71QbrUeAhOwsIb62zelrnNfTaXQYMDMEuY-sAnse3zlPrs0kib-jBHPxLG8VqJYYx7eQz64bRGqrQ-E1dSLd2wgF5OuSPDC2URknpU4p2n5RNJGxT6vhP2KEuYvpA97oddHmVixF6EaExVEaIdGGF4od0EJA4E_uWOJTzFVyDwg1jf5XO5YPWeANWHcWLnwKHQUIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQjRQhHDf3WDLfiGcxZ8tM5wLWBC4gKl-ac-3lmyhReQaUIC5xTDh8Oc3gSXzH1e2Lj724-B0qPlfGgv2MHFylHXiX7ct7Mb7xhh777H2yEbCak-8FAUUweGlUhaKJTiRVXmFybr3TG-aj2fUIaf2mBvt3R5Cf7wmDz0DbH3zp019kQ91zY_Xq3H_QI8W-Tg4L0Dyf_dy_1bk1oFddI1KmA9tFR1kKAJ7RqTCrBL5DKaetRvvkiL-yOwmUkiE6EgDsiXuU1_q9XihEfJvcabFRJRW-fnlqnF9sXbIuWzVJ5CkiqTrEOwnhTNSUUS1oCwqtZtBCXVC2bGKZeNyxKn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4coHlsWWJl2xHLhbunI1CzmO50HRLgsGAYYg_crTSIuBWzBrVuzPsASHrgi7uuUwjqthalF5JkhyFDzTFNP4ONpPjtlY90GTZbGBrRfi0WNp1AkvJFRiHaKEYXt6cGu84V0KoKUXggSqVU6OTJKK-p_bj1d6z8ClicrIja9yXRz2-LrkSklfkB-MOtAQGsv_1ftrji5F_yt-iSd0LV2ynbfLjYWBhbbNVqLFFwkosjgdYLOMVUtlGvvQp2ziRbLyTaVlVtaNRNJAM1rVDHyRrJHUG_S6XbQ1UTOVJRYi_qp7evbl4nGhB0QuZFyEHo5-q8d_oHmuIHqFoUnL0bNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQd0OBWdf2e9HNPBzdQNwxA7ZYt7GnWXALv2gRCNe-lmAMPO790PWKqzx59vxo66nvraNYFNaEoLrl_OkO22HUND21UY_L1G61Soby1eX0yfZO97O0aBwF7zEcdH_z4NdzR9wogDg6yWr_4yt6wN7UhY8JO3hzGnbc4tkacIJVmXZ_G7GwrnYaNusnWMKxXh7EEEgUXWcoj1GUfSe5wQ1CCuml7qALUUxCwREMdXnI1jVQLnzOD8UjhOU0JA587KFopOv-8QMjRqgkfo87XvcDahLBDLqlLXtxV96WWafn2yTiS99Hkb7Mnwn6B5MZxoHlLOYrAM2lWAg37ci192eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzca4rxhWlPEtrf2dKjBo3DyWEW7xA1CKq9DEMQGXvMQJs2nk442_UNAdD3houCbW6CYCqZLuFiMtw-r1vekueFmuBJ0BdZaIjnA8zoRpsFF_iPInu7Zyy3IY0kvwfSjLknGkuX9pQ-vNPdRJ2IKfEIPntq5mmy3hTMXKmYewskj774SC1OgNrnxkAtaEQmhgHRxoHnv0Z3VdwhwJWLqLHp_ShSKMRVUIGytN1vpbOr-txd89HI01tvSMX-t06pSm8VIpNr8TmmIkekyOQTI5jGSVnSC-a2heaiR83GSw_BcmK-DkhC4Mi4H-bQhUKxNzn4z7qt1ItzYdY5020aI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=noEDwPAlUaVZb4-8gF4rS6CfGXzip4GfAU7wGsPnNl3w61ogLWqo4DNT8ou6gCZMZfjTgtoosyXnsfQAReW126GVNOnvuqBbio4lv-2TucT_R3wAeCmp6UcJurn-LhPKrRHispU1sNZiYUTcLKYCkKbFRZD8kH-7oGVpnvpS8BuzFAMd53TvmgDE3d5n-YfHZ8UBeGGtn_c5R9KQk6Iq50lIxAMtlhi9TgXoGWU-LdYO5cZn0lzTNK4VOjyRR68AZrjLwGIcmod31qhZAhR57Z8h6vD7Etdm5beXtRmPC0Li8-uURx233etqvHO1nixUcmEKF-qNV-o-uEzI8VJPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=noEDwPAlUaVZb4-8gF4rS6CfGXzip4GfAU7wGsPnNl3w61ogLWqo4DNT8ou6gCZMZfjTgtoosyXnsfQAReW126GVNOnvuqBbio4lv-2TucT_R3wAeCmp6UcJurn-LhPKrRHispU1sNZiYUTcLKYCkKbFRZD8kH-7oGVpnvpS8BuzFAMd53TvmgDE3d5n-YfHZ8UBeGGtn_c5R9KQk6Iq50lIxAMtlhi9TgXoGWU-LdYO5cZn0lzTNK4VOjyRR68AZrjLwGIcmod31qhZAhR57Z8h6vD7Etdm5beXtRmPC0Li8-uURx233etqvHO1nixUcmEKF-qNV-o-uEzI8VJPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=JI7kma3RrXkyBDE7wMrXNsoD6fEmUKQatFaedKeo9diqGb5YtEwexusuElwEFFxWseI-cVK6OxrBeo_WQFKHmumFAq1Z43XH3FHP6OJkruFb11ILG350X55nx4WLXSmjhd97ffG3S3ZwLQo1XrHzc4vyaaIQoIWhxBrCttTW624n0pn137VXyAQftNLLjEHxCw0Xygaut2RS6a_4VlxpKc4dmK7vkqpKTaJFGnU5veJYq7uailKvPFYoo29PR_qvNkJrRj01cRETG1FRydSAdqywl38yZfH3E3Ip3s3Dy1_PzEky8N8THFe5VVNIP6BrlK9miLUTxWj2ohwVcxJviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=JI7kma3RrXkyBDE7wMrXNsoD6fEmUKQatFaedKeo9diqGb5YtEwexusuElwEFFxWseI-cVK6OxrBeo_WQFKHmumFAq1Z43XH3FHP6OJkruFb11ILG350X55nx4WLXSmjhd97ffG3S3ZwLQo1XrHzc4vyaaIQoIWhxBrCttTW624n0pn137VXyAQftNLLjEHxCw0Xygaut2RS6a_4VlxpKc4dmK7vkqpKTaJFGnU5veJYq7uailKvPFYoo29PR_qvNkJrRj01cRETG1FRydSAdqywl38yZfH3E3Ip3s3Dy1_PzEky8N8THFe5VVNIP6BrlK9miLUTxWj2ohwVcxJviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=nYNRtObTCAKobiJ6FvRe4jWpljBZ_Ov-HnUkobPvzqLZW0OzZTcQEwjybxK4Gmi3gA_SONZy5hq46q2xFEux9JFSbilGqo8dTZlunI6ArLrF7jNFXzCr1DmPUGVbxnamEbAfYCX2o3dARChgbxM30i6xtupX3-xRZTObhUon14_FtgwJiIekM-EoF2akc0lT5oe7Vlirov1mGlNfuqcWxTHKAPDHgVm73Z1iIKggILqIHZzP-o8p-0gRfxv9dM0-ZBxR8I9wzLU9HauA7W4lldDHeKlLkNU2McC2yb4qfxXKwQyXmfDddzXHGnK8NKzN5XMbJqkMRYDx47S0__oPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=nYNRtObTCAKobiJ6FvRe4jWpljBZ_Ov-HnUkobPvzqLZW0OzZTcQEwjybxK4Gmi3gA_SONZy5hq46q2xFEux9JFSbilGqo8dTZlunI6ArLrF7jNFXzCr1DmPUGVbxnamEbAfYCX2o3dARChgbxM30i6xtupX3-xRZTObhUon14_FtgwJiIekM-EoF2akc0lT5oe7Vlirov1mGlNfuqcWxTHKAPDHgVm73Z1iIKggILqIHZzP-o8p-0gRfxv9dM0-ZBxR8I9wzLU9HauA7W4lldDHeKlLkNU2McC2yb4qfxXKwQyXmfDddzXHGnK8NKzN5XMbJqkMRYDx47S0__oPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7UaVJLYfSkzaIgvScsj49Ro5b7mL5rMeFBG2TaRo_a5nZzpLW7g2GG2VSLcG3gu18BsLIAGPdjVbDlGC32aeLSsShb7pbrq2MAN8U0dwpz2QOzffMN-Mj60uY5-QVAzjcsw79UjkrwllJJsfDgiTfpX0cM1hWcJGdZg2lkNtFqZhgTbqxQB_1brrYFXCbusPUA7oCCg8Z7DaPBPvcbhx_XGUJ836tkTrMVYTn47KYS9FjEF1WRLpUdOlaHJktlxwCHqVsM56FDTO8XooommfDMjaN-7nTzAbQ9EzbwrU_zc2m9rTm5yP3btXvsWVk9aofG5fyMdQ1Rddi1kJknssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwiOD97mATl1sYWUEO9yHZAAewCEA2tXxQhSiBDeN7Dwo6iloXxOqrH7aWTXnUeogkOLVbstcuDwZpUiHjvBCiIi74gueoS7CCYW5aGJqrBrgKrYL5XnwXWwIAZfyxpjwMEjPXsXT3zzlZ6BRjFv581pMPSXb7YA2KNeVyJ592Uvry4_DWx5Rfer_ka40SzCOJFaVYDpqnE_yMIpb70BsZLDWgCO1EPIEccOtF8Z4RrfgnzA-PB-tOK9qVMA2LQMw4aLMzwOwg0vLudtitXBsNyf77T2W5PvgSUV7ljduSu9nztgi64V4IHP7r1ohDw65V5np98GuYouIzf8deNTgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tioh5Y9az4n3JwEwjL_gEifL0o0kxrsjXDJe0crCnnwWBJ3alxrj5FlynWtQfztRZwJ9tuB_ECDT59yrEBswUk1BBm8LwcrK1ooSsIFfdlLStJDg3n3qaNhoz5ivCjhbyj8i69mhd-ysnF_bF2F4h8dT5p8w3rzKKkuHfRedyjIiehxIfOVty1vBA9Pas_WcaaDiCzzvTz79xP9jX4P8jgM0cIV_95xzxfGIr8Z_r4MGjAd6hadnJzpCXhR13iqcgcqQGbsjGs8NKq73P6c06fYu-UVN7-FtLRFecKZLEABZ4oTGR7sA-HfhlaG4WkFEmSDq05jVxT7W5EyX698Y3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/larwli1s6E1XgRtn6kMhIStuZJdx-aMsBXYhkMmziPwLQqD0Rs2l4DDEzM0_INnc86kriqCrF5WsnBmlpyNDrOs70DP1WukQzBjQrD2wRCbrhZih90TMUML79RkycmKKGIB44dCo8rPDib0i2oua7Hf8GAkKIPU7ZFvj1ux3QkO6uRGp9gdzR5RR_PhbZt24tPkwUsk65TStjAtKgsOXoV3O6V1GoZItjwWQmaxeDmZXuR0yJhM8wFRa88WAnHDiNTpV8kkKBpN6snZYaaW4v-4ohBZik4J3f7SjQLAwpAv8gRhh74EBXb2zeR4RgTU4rhsv9Nz8zGiRT9xBvRUQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=JAghwCcf9ygxICAy2hlVtaTF6V7zn5WivVLXg0bqePZY8H_uXyC_Gg5wLZbAoNq81vpppAJLQVP0ofPx9C5JXvAbll30HZ-PXbxKOGv11t2rpSWSSLl2B7e1u1-72nE_9Dlw8_9zGfLz74wOUNYi3A-WuxesvT-qopXK5aV3fU8aCx7YjJnhB1W49C05zMCYTdl4bHchzZxSWZj5tMXyqobwBYiqNI4USwZOQsqdjDkqoh6CGmQ59pCcCfyKL7TSPgE_lV5XKeJwIK7gaE90Ifb_xEvQJ4qNfn4cIymT1hur3kQ_e9v2rC7cHrVnzeiSWvrHcx-dUtNQ1xO-iVJq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=JAghwCcf9ygxICAy2hlVtaTF6V7zn5WivVLXg0bqePZY8H_uXyC_Gg5wLZbAoNq81vpppAJLQVP0ofPx9C5JXvAbll30HZ-PXbxKOGv11t2rpSWSSLl2B7e1u1-72nE_9Dlw8_9zGfLz74wOUNYi3A-WuxesvT-qopXK5aV3fU8aCx7YjJnhB1W49C05zMCYTdl4bHchzZxSWZj5tMXyqobwBYiqNI4USwZOQsqdjDkqoh6CGmQ59pCcCfyKL7TSPgE_lV5XKeJwIK7gaE90Ifb_xEvQJ4qNfn4cIymT1hur3kQ_e9v2rC7cHrVnzeiSWvrHcx-dUtNQ1xO-iVJq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjBworgiZwuiCwJBKqAAJ614BFmbcGbSo2p4ztUZit2Fyjrakm77qLvw3oHhO_Mvz64P75tlx_R-Q-qVO1i9hkPivujkUpuvC9IDOfq0SA-pLgSj21pM8fk5j3YB1a9tLN_hZrFP-jOL_as5djzltNY4F6vE9_G6V0PL2nruJFLrSJdtQq0BXa0FU1KS9SZsVK4qI3ftNsWutC26kox7uZZY5SArbmblbEuSKwgLpAHka5nT8GWIzgafLbXxPSTaULf9zwpJTM0L3S0cx-_zydQ4pWWvPas15VAlEO7y5HAjqx8t3RMNzuu8AG6ApOb0GjVmw007MRspyXJJoDeDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxPCY0Epy4sPEsKdBXSKmqP_bnhTzuhTNWrpnoGc8H-gzD4WIgJMXiuGNfriZcUNIObOFU5r_GLGXx2-XU-aH9tfmZ82RDXSzGMeG3T2sumXfyClU38x67E6AipEqSpz_WfEDMwm2HwSh6tv-CvG-LD6eD9K2X8MycgqyU87Gj3GmorpcRnDZhgHCX6y2ckYy5E21GaAHrxIOdRv4fscJnlpSLeqWv41dqFN7yEyWZqWueBkuY_i0HK1R1r5tlgk-fKdFysiPsjvh5wLr7aHCYl6kkLXCXTOEEgBEtOuWiTSgeRevikIwHbfGdopsSXSLHwFuK0Cx2L1ltPp32SqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=FAB1Moou0hWcaeMVWrB5smd6bjK6VdoV5TvV7sAe7SjXzGbQBbwDa4MGpUKdNwMIx0a0lZterpbyo8m8B2QTGdJZ32QpHMmOVt7wZkpmg7f48j4hVhXEoO0zshtNvDM60NRchiff8QDTYPgyn3dGqUGfn9GxFldazUBNqIYPLphKRFd-wtoUqDWpi9EWTN46Vp_NkB2QUswm40gK3aP6MclOtUbR97I1g1pbc1jVHk3IopHZbxKjYPzVmkLOUIMb4aIAItxhP_eMf2QM2AxbihdDpNs2oSl1eliKonqPoa6-5MWv23Ik6ak9t1uYdbinAU8ORn-K_GRG4tqex0fA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=FAB1Moou0hWcaeMVWrB5smd6bjK6VdoV5TvV7sAe7SjXzGbQBbwDa4MGpUKdNwMIx0a0lZterpbyo8m8B2QTGdJZ32QpHMmOVt7wZkpmg7f48j4hVhXEoO0zshtNvDM60NRchiff8QDTYPgyn3dGqUGfn9GxFldazUBNqIYPLphKRFd-wtoUqDWpi9EWTN46Vp_NkB2QUswm40gK3aP6MclOtUbR97I1g1pbc1jVHk3IopHZbxKjYPzVmkLOUIMb4aIAItxhP_eMf2QM2AxbihdDpNs2oSl1eliKonqPoa6-5MWv23Ik6ak9t1uYdbinAU8ORn-K_GRG4tqex0fA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5GPXKC8hnce7TMW4sO-abxQqq4r4Nri6DpRSwIoXjEP7yFexPbYLxFHwu-RcHZX3AOaueDf88v7G2G1WcaP7NW5i61bSOw7sc5WEVe1mrKT34rMT_Pz52c9FYfE5zRtP9JNGfRAMf6cJ2Od_Nb8XfqTnHtYsTmg4jbfjUVFWxmrT6uzL_Lac1eyKbyfl-NH63zfFLb79AJwD3Nc7wo9ovRKFGvHwdjvT7wRHtX5_BclI-TZQ8UuM8jxuKY3Ds5d16b8qabFywjfm2a88IzEjN7fwGBl8bwfaeCILR7tfoUF9edLeH4n6cCbVTt21JbzSCBkGOjrFw43Fr-eJptrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=dpgsgdI_sRG1lEt_dkanhSuusiZRtk_ojJvSVjSHVxMKU7LmnFgKsWPFM2IqxM4IMJv2672I43T7kFSL5gj2WHGY1lRAAqGJg2RZrhgRAZ3S2afm9MBKRoU2zT5DNQGwaYUYRBrkrW4R34r1Cp08LpkIjLwGKj12UVmBo8TXoXAPv7jdZemrEHoMtNdiw_QFs1yhJ7Ujni8hMHBCpRSDwDkTacHTLBs-m9oFlNp0FT94TyDU4Yij_Xzn3RAnYrvbgXfpGIowSPxs0hZ5FSC0XnDgg-K7jH9cQJDmc8fWPM_VjGwDXl7bRCb7dEQYnTtKbBOxVlo3k5Ry2nBza0vzow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=dpgsgdI_sRG1lEt_dkanhSuusiZRtk_ojJvSVjSHVxMKU7LmnFgKsWPFM2IqxM4IMJv2672I43T7kFSL5gj2WHGY1lRAAqGJg2RZrhgRAZ3S2afm9MBKRoU2zT5DNQGwaYUYRBrkrW4R34r1Cp08LpkIjLwGKj12UVmBo8TXoXAPv7jdZemrEHoMtNdiw_QFs1yhJ7Ujni8hMHBCpRSDwDkTacHTLBs-m9oFlNp0FT94TyDU4Yij_Xzn3RAnYrvbgXfpGIowSPxs0hZ5FSC0XnDgg-K7jH9cQJDmc8fWPM_VjGwDXl7bRCb7dEQYnTtKbBOxVlo3k5Ry2nBza0vzow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=sOa1SDjsaRZBnx6SbaiGcrrMikfyYwYD6qXjJ8D2niB4YkpPlKm8xqVUBBzyyt5NWv-DyeDf2v_0qzqEcGjNiQekLoaV8s8b9IBhTkP703LEEZgP4hUaP40pfIOAAr2l3NQvBISRHUvgbsy-eu_brf_YWS0lIbDoVu48n99OtEuFEKzcp4-6jTDUSwbUt5DxE6wP7qL2F-USAynwNrAX4J57wZXMxe6p65F1ayQ42NCJctUBmFOXUAnK4saF4Z02OTiVaHK06KBTm4sbHVH34rbsXjXZ_yyRLFHvalDGaXCbeLKYXoIXOSIbl0DDIiMjzbAIggvV-9I4a-jCqlT41A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=sOa1SDjsaRZBnx6SbaiGcrrMikfyYwYD6qXjJ8D2niB4YkpPlKm8xqVUBBzyyt5NWv-DyeDf2v_0qzqEcGjNiQekLoaV8s8b9IBhTkP703LEEZgP4hUaP40pfIOAAr2l3NQvBISRHUvgbsy-eu_brf_YWS0lIbDoVu48n99OtEuFEKzcp4-6jTDUSwbUt5DxE6wP7qL2F-USAynwNrAX4J57wZXMxe6p65F1ayQ42NCJctUBmFOXUAnK4saF4Z02OTiVaHK06KBTm4sbHVH34rbsXjXZ_yyRLFHvalDGaXCbeLKYXoIXOSIbl0DDIiMjzbAIggvV-9I4a-jCqlT41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
