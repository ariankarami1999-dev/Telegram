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
<img src="https://cdn1.telesco.pe/file/r5JY-bxviiDqCLefuxeCHBCiu8NUUkDwm_OuKq8iV-KRy0Ho_DIB7KA52Dub72jl_fZ9W-b1y4qJbGD0xvoehGUie_2kIho9Cdiw_BKl1S3J5JZks0vNVqR00CY5hGGl4cRqGa1Xkl7pYCCmIzLh93wRt6qxwW6PevltGnbbShVDucrVqqKwad6NU1RQCF6Kaz8eN6z8MeEL5vZsUbV0sySKurvVpR5ePYMT8QoXU3v86OY-hHWCwnZC3bMVXs06dc90mQfAcLLLyXGPoxrpmY0NKWrdAbdyUL2hJplUqAHZDL_sXex7TAKPlMMYXW-9gFOyhuDAeKCMyjeSMgTO7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=g9KWtDn2f-6G20PgKO0c4cqYECm7Fh-eHBxSeQEdtW5ju0WE8vrDtX-LT_ZSFJg7WYrCSzZMOxhbQTC7OSXRKIx7UZTSqmnAtN-iHl3a6JIt3WOy62odKElGY9YN8uC8CjggOj3tvEzsECgtjENEP0S9szVAdjQKQ-ZgzEtIB59Z4flEeHq3x2spSSDJiYMqZNv02zD9Bn5sgKb05tKx6OEqUr7t94Rg7zjWMRJYOqhhIoxWcsJ5it1LfPQZxuoIWnwm-pcvH4UQdqmsquTmprquQZIVzkNqFib9JcJaQ02k0LUhKhW5fPbebUUiVah_eBD3UB0GkLiWLAt6hkyoh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=g9KWtDn2f-6G20PgKO0c4cqYECm7Fh-eHBxSeQEdtW5ju0WE8vrDtX-LT_ZSFJg7WYrCSzZMOxhbQTC7OSXRKIx7UZTSqmnAtN-iHl3a6JIt3WOy62odKElGY9YN8uC8CjggOj3tvEzsECgtjENEP0S9szVAdjQKQ-ZgzEtIB59Z4flEeHq3x2spSSDJiYMqZNv02zD9Bn5sgKb05tKx6OEqUr7t94Rg7zjWMRJYOqhhIoxWcsJ5it1LfPQZxuoIWnwm-pcvH4UQdqmsquTmprquQZIVzkNqFib9JcJaQ02k0LUhKhW5fPbebUUiVah_eBD3UB0GkLiWLAt6hkyoh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=hdV8M_JRwkrZWXDPgLjVByImdqmF1Jo67KElGoahGiC4t8iCh9HfAQte2MfojC9TGoJodqcoKHiqnU6jJrl0zY98a0VbuQH6OuowaxJiU5Mh8p2Z-03O4VHAPnfeZTk_MFM9DVQpKiHkWlB4hnF7C0-ciNKFmPBqimzQRinnQd3xNEdAwLpRKW3GcerGjVwDOzMEF6Yt_nucLmSbJbCiivgNV61mIezev9OfC1XP_x39MVQwLk5DV5Vx0PUH_qeAyp1WnUKvZojYWOHyaimY0UaRrx3hHa8J8MjgJREEBExAAH4S3juXmyeL3X9Mh3eEbz8g2zWvCA4K0C7b-tD21A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=hdV8M_JRwkrZWXDPgLjVByImdqmF1Jo67KElGoahGiC4t8iCh9HfAQte2MfojC9TGoJodqcoKHiqnU6jJrl0zY98a0VbuQH6OuowaxJiU5Mh8p2Z-03O4VHAPnfeZTk_MFM9DVQpKiHkWlB4hnF7C0-ciNKFmPBqimzQRinnQd3xNEdAwLpRKW3GcerGjVwDOzMEF6Yt_nucLmSbJbCiivgNV61mIezev9OfC1XP_x39MVQwLk5DV5Vx0PUH_qeAyp1WnUKvZojYWOHyaimY0UaRrx3hHa8J8MjgJREEBExAAH4S3juXmyeL3X9Mh3eEbz8g2zWvCA4K0C7b-tD21A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTAE_dVJbFkgIOohopy9hobMS-Yh5o7A2TKo78it7WkGDG560NhTRCmTswYV0sweWkjf_6nP2o2AhSrd51t914WbNsCXrtjk1nFEBC5hjQJxl1Tm1ygtk8bOL3R_niLLJiM13SGC4UK7TUTJCtmcSDcWi-HqztH8JBkjo1r_V17nRGIjm7dMc2TKbkdwho4MM2ZfrNFl3-0lb5SFAMASSEzFC70cN6z14HVHA156oDsljq9nc1W1nx9QXP-UBQDocwXERTcxUDCoDQn8SDgN6McEJnQfpBFiSvpc_fC14TsKmzaHZ9CgtRnZzqxzR3gpn8ydcv4Fb_gpPOJ3Dhvjrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxNEs-Uqmc7ALFBtmvVFtg-E6HVtIa2a_YdW0FvbGlD9VosPH6UeR1bjykLG8iyQ2D3jo9pck5HdjwhuCm2OIQUEw9LOMuJCYjt_BZfU0u7B_HR000ae1vHmV2QP9_e427dIZafVgmp0n7HET0tzRu-ans_Q5noUmCYOJgRm08-5Obf14q5sg5_KsuWMPcLviXqbC5TtAwfgEwFKj_8SPiHDcjd_i_4cczXmZBbh7jx2QvWu-ULC7ptSu8BjNMZfl8-HG0ji00Mrb6zmrLkjDMxdSrcCCnkBvZmZyj2wAyX6Py0Hqh-ZDKfh_Jxq9zYhGrCpfZZBNTxtyvfM0UOOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ky0SjJLUUEvH3Cg2if3AuvTPIQxCZZCxqctvqfkUiUt_oBQVPiR-0w5_pO0AbQj0EMBKrma0B9XwTuTbjrrdrdG3JbUB7toergoECMDpz8j0xO4vZiT1eHU0e0iqnZT2x_-Eigcio7ycqD4U-KTZW-uynu7yiwAzGrUiHYjitkn4K_AtRz3gBZdX_a_jZjUrMjKZ0MYkVgrymn1OSsxRAWWjQaaACZv39GZ60VW_aMj87ZbvjWi824o9fd7CLI2RhhT9F7wOjdiETL6WwGQuODpW6gRCwqve-P8S6-VK0JB1M8QMSkdXBu775Cph8PVGFbtOM5GKcdrk0w41jybukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ky0SjJLUUEvH3Cg2if3AuvTPIQxCZZCxqctvqfkUiUt_oBQVPiR-0w5_pO0AbQj0EMBKrma0B9XwTuTbjrrdrdG3JbUB7toergoECMDpz8j0xO4vZiT1eHU0e0iqnZT2x_-Eigcio7ycqD4U-KTZW-uynu7yiwAzGrUiHYjitkn4K_AtRz3gBZdX_a_jZjUrMjKZ0MYkVgrymn1OSsxRAWWjQaaACZv39GZ60VW_aMj87ZbvjWi824o9fd7CLI2RhhT9F7wOjdiETL6WwGQuODpW6gRCwqve-P8S6-VK0JB1M8QMSkdXBu775Cph8PVGFbtOM5GKcdrk0w41jybukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektF2ozW-McCdN6Jbwxlgv7pabD2gdhwYUPmuec8XpmKeu0OQUh0UOSpVs7mTrJGT2WSan6nlMrqJ3MW5rOMyNCDP48Eswkd5AX4lA3uhUpF1NyVSWi6i_hjnaHqIG0x3g_qK11HmLnW65q_SkzNpZ8GOxskaLmbCQUYlHZPHlQfAKbPI_fAXIYmYYvSeyNw2UvvzDAPiC1wdaHr_xbcvubBbbCRhXv6vezOu9JLJqWSsrA4Muif9PETEIgqTzexNDAliT2RZ6Zdv4stAyzH3SoCL1LkbL0rHm_Q2ScMb0-ehOsps6O4WIstdstj257Z-zh3Pm4-Rvl2YY9kHpNArIIjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektF2ozW-McCdN6Jbwxlgv7pabD2gdhwYUPmuec8XpmKeu0OQUh0UOSpVs7mTrJGT2WSan6nlMrqJ3MW5rOMyNCDP48Eswkd5AX4lA3uhUpF1NyVSWi6i_hjnaHqIG0x3g_qK11HmLnW65q_SkzNpZ8GOxskaLmbCQUYlHZPHlQfAKbPI_fAXIYmYYvSeyNw2UvvzDAPiC1wdaHr_xbcvubBbbCRhXv6vezOu9JLJqWSsrA4Muif9PETEIgqTzexNDAliT2RZ6Zdv4stAyzH3SoCL1LkbL0rHm_Q2ScMb0-ehOsps6O4WIstdstj257Z-zh3Pm4-Rvl2YY9kHpNArIIjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sP98shhdu0oBaQbTo_jdJCVklW7H1rV7sYv76Oggq6hALIZ7Qnu8RKvaqaexL4_N7PNFxfDoNy_BmXHggu6vFNipTnNfo_d8W0AckEtC6nYc2liAZ06oWl62d6KsqHpQEo762Z4QxHYJK9ss2ZbNq2hdUNxT5KXthE60RGyBsfnxTaX-_KuRcG7SnLt4kqooV7ELmREGMKYfG7omtvPfMwe22e2UBSb2BGUf1jKLpuerEaTPotAuo5n79YddloJ9aLx6lL3OQypXSCbqY_COWyKiFpaaM-ARGMdNoQZt_20o5c6E7YtqSO5z9tv1IDgMIiXU9xhDG92IwcvRThUqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c1j-kGjSDWOf_fRVkfzI18xTx8GlRAKAa4QOqppw52bBw6K2L4ai3zHRoZghE9rbEdg53C4juNKgV9rlL0esyBRzx7JADrameJgf1e9xEd9wQyPi9YHV4zAkFgvM3qKg4J2dtPRb2syZ6BTxUgUx8Q5BUQe6HGIKLtPZkf5n9JguXjAec1KxbEO7Ff28B49Ahh-INJYlNdC0VbGx4apELOAms3dcAOATGLUg7Zq4RLZIo4zSMFaB9ULpcIMDx2vSsdvXbYflDHngRgIALUnY1WJ9J_M3F2pLrmfEa2bbrj034rnsgzd0RncUTg8gLENgSvWMIy9C_NcpwJtx9PJtvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/diLyjPRVKb-l-1xE1L6R8ILxQah0QHjRU0bwVPyxFoJR1lIpc5s38f1uRfG_1PabOfuwNp1N42JY_KTK81_C_-eA-f9XmOg6GWz-PH_KLpBymyEdW5fvVM3higI-BD5WS6BP6BToD9rNmvXlZulUfLNXHbX2Pg_C4alztlrExGq3t2poexAvzg1-Xpza77TR25QMJBkqiMHl-RnHNof_DXJ-j2cY4c2D6liNmIczL_f12K9LjE0OTdrn0I47x6gIND1nyf96i3llGf-1yRrlHFRU5f1QnaE2X9l57Elq7kG8FfbQHIaYNlLE7lBAN_ihNdEDvlyIep3A0FVa-zVoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kgUxxTTrxzLWgth1D4LrvTzeH_qR7QM38TyQ5cgKQQbdkcHEX3Cfig-_rjIFdKX-7_Qcimdd6NvhRnJSJlDT12N0Mdf5GMHcvBWHgsRRLqSnqcQ_oJRlcWGrXojWPbnLoCSuypHMwQSe2Y7DuPCfYYsaRZiiSI1UrY-0JswsnXbyDf89TnMPVLNETfeVERNYlECtY9ApKpBSgqltltfcWyq9aaMwkM6js7Tbw0aVLbPFquzXMvqacFPXv8mIPN-P_lbVQm3lwUSDoHSwcASgexpXcdsKmFeqn_kF8HeXhtDrRT9byrYGl6MSWceTPCpUCcaS_ePBsvsqJ78qseVA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OA0maPFl-LlS-m9x3ZtL57lFIMi6yfWpD5FNK69oNbHJi1qzJ-p64Cg0BBITkIqotak4INtQ9AAxviyV2Xb3YycnCPWvuT1BDLGIwUm62HY2pJHcIks6zvJpIQ3PH_4MaPSWfcidGIs-TyxMK1LZ7oEqqpl7gDMY6Mv3Q50r3rOznajWCu5pqgDMzLjRrcJazsRrLyh8kttgLRTR4OulPX8fqAzP3f-vVgeTu0DDfbC8Pu-F5rwkQ-NwPoT_zEoPPeqglXyqq0riBIKaLFpv1xxAlI8vKwpPN4RDinxVZnbvGy_s2zfc1I68b4NLkDups-38Wcs23dujMoMas54wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QDSbgZ8fBH_uehoFFP7aNqIiP8BOdPVPDC4o1WteC88LRs5VCKtGNd_xBJZYGCy-HSromtlHL4KFMdSrWNbKj0802dn48-t59VNgYbLMDO1UhJvYB0_kFvRTw8Uy3yrDn_z3kooRjR5EgnyqOV1h-d0OR5Iq4wB5k_ml4Y290RBRoAsWCI4T-5QB6tsUuFZWVh3SUauc3GdsrpkHeZ5auPN-3LRsogVGfA82URI5Jm0mkBEGFpiJ0qRjIdDoM-szo10rK9fJ0v3YEwoxJTTiAAHI_gAEFKNxudE7NCC462mQKp9DmUgBAPO-hFLG-hQrQzFEZVza89e3LaaF26iqOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_IOZ5WP9rwGpDR0nE2Gmsw1AsDS9bgnSgEnVzSj0AmlLm9acR5YUa_hz2qXhZBghlPxz0VIeZuZfz0tFACvHQxIu9XHq98cFX4DHK127ts8swuQ4Yl5-vOD7h1jTowz8QpilMxTktZaRIBe-_lWivZgEIoUiePEnC_V4RD3pv6Tk_kNVxxXbcjL3_la3jUcXRyr_uzZ1kmZs0VnQCyyxFtuIgDxYsnVbS2E4A2gWuCHZZr-2CzZOItdiUd3lkOd96m8j5wtDdOH5BudlRgUUzNVkYhTVSEWqED4CM6s5sZuu9qEF-_QgwxVbDmys0O1N7ml3FzViMJLMtKYbYHlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RlaDRTfczAIRYF8wfIfHnHjeIH8DWLklKnREJQrWQB-LkOnLQFmcYS30zBFcPoaQLlP2Y2npMrdPvYxcHGDEhiRE0fPMwCaA_niNBQYrzGpX9xug0l76pghuqWMrE-SGAhjhANNVV-8TWd3rGtxSg0E7thzre511opk8wgMlCic1EEI5iDP61oEB0bzP70YvR5SkHe9s13Zb2LJZ6ux2dGohX4z00pKCmRHcRiylsqrYKrEZ8_nfXGmpPzv5dIf6QfZWTeYM12ssk3VlGTP8gHGiYvSOlc14DEaXSxn7PMxjr8F1IU5WBxiTthKxzsOx1JF-z3WzzMkv0rrANv9Azg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/K3ZANOgo2IJBfyCe6G8QRmGL4zVdLCGEN_6LohHFJuBZUe_3jbOxZU402OuccwfIq9bTl_XbxOLyFVERaxHNWCXS8KZ1KitV_0egGIzWbN_6zaP1bzjiPALRn_qCnNmTIbGsRoITyzsBaYKYf5W8uAOktdFKcxsphJFoqHZ-WzXfaIHKH46BW3UUswv6Eo6WDhbirRDf2IQPAAVU_hJDGFEncIF4SFq-Q7MskdyCEPkMkXLTyHjBf-L-jSF29tNSMEWZxwEwn-hKo7EGasR6-aX8_-49fU7ONG-7oiqqgrBtSREFP-03-u3aJAEEllzag1zZDer0qnRsui3CCnVmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_4hFW3JrM8mNX6buYbKSa6sWdXn7e5ilgClHhQQOTym1V2VQKOt49ROAViPPYGGBACezYP8O-bPUg00HAtYEnHliCVQOUZFTfkwXsWfl07gWVMukqIs9Eg2bJQhojp5LY32wmEjAbEwRNHOp7uyCfSiQVLngDFGOi0ndESh5UOr3qGvXPeh07a6ZfcA1YyZrAzPpeeSVln1PU7phPIO63YIA0WN6Z91EXAS4DtClmSU6tgUGXuP5DSrbp94agVBQOphw1XW071AYK3-JIxhIF5Y3dvWNB2sdl1TiDEqAFpbEc9v2hl_cQlkNAFKaKcu32TXfV9u894ki4LKnrI_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3fnDOYMJs-3zvnYf6bnu7e5QAzkecE8Mw2NH4RlFU9qL6R1YvoJvXTZuPZ-JgNxoIcPVs1KN17QeIawa-6OM3iiQb4vU7PztFuCJsBgjIyG6HZk3RHsBBy-czYuJ2XGlN7uAYI07ZbOONhierScQx3EUnVEEM5RdssRy8tpdnRPtMclUWGH62EFSu1AR_-qFEUOQiRKzddueunmXpEbInu7iKQdWkRkeXRuUNkAk1sB1EXwC8t7u8FnfAS-oHZ8nqDTgZxUaBDfzJznPxlZ15wudkaw0LB7IjipZj9tKG7_YNv7btcziyql2Su_W6okMrEhz6tPmQg4DcBKdbUTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0aPUT_G-91FNqSugoS2rGuMIc5W6F24_kObE9mPD3V7CWAaB0AM-nc8Mo55Ozzfh24m5TwTbrMb_DJ8fYhvnkYeDGdnq573-_-vfpnmwng9UvY3KSsxJeepnQS9yrfaHA-Pu7dEE9Sb89BYNQav20O4OGwbVjCbw1mtDZqZ5SjiGcvsfTF1mpZhvlrMPoEloodOJLdag1TX4vFdk35QTVfJO9rdtV9FoUGdsRNNIvSwDHgNe_FR7p0KO8ZmYci1wmCm0QFb5k8qvIZLAZOvobB6sXsJMKk7GP540u5eBvYV2Os0DDXkTUWdy0928eHF5jYM7TUHTVLNWHNxMnrSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RIeBZbATdIEamjzmp7TG_q1XK4LokUowmUPQ6TEyndOzx0yK8zVXlbk6iiBf1y2psCh2KGhpBGUBYeElVlJBOdiwn4pzHIDIjrkx8FquI1PDvX96Rh7r9twAqhRL8P2U3U7wETPO0xAaBgLbuw8CpSYoF8m8CaHwxi1vd3oUlDOf1_4O-RMiO5zlznJlN_TXP0ugUQddwrF4KyAK0uqnQ_rfMsTppvJ8MXh_BjRxY0RGXpXuhFgh83cplUkO_Jk2U3f9KEqvIytOKNdVOKdSKbRGYSACnDWGM47AZ8MzqIMf88Mbj5zhSugI1AEvLdmyBoOdQpq2gqD_a5cBhEcnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sCwe2LmSsHtFTuphrba_b2ABhLsXGGiEJMxGNyUVrqk3nPQaFu0QeE8LQiRaCwY3A733yGqMMx_alZYtuMYVWs93CuDq1zxCTO249L2-vxxuVBdKhBXkzsyFjJrolrR4PUsEp9vYjXrvtEoJVvnsZpDYtCbc1V_zB14eFbEr1vZBUvb3CsGknbKczgq8YC6WMlsIZvduYpfDDYwNIZ-qM4FJvtC6yIL29PFOstm08ZcSZZUpM4Z2xOJtfiuyNUVssi2Dp4RlinNa_X94x-yhH8kAbIQPqqRFVgL4De8DcbjGXRQ2s2GpEbO3OqQGdCo09mnfZ1RCzM_yXlsHBR5K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3FEuCofz4E1LVM_7-5xKYgYahyBLVVzfPEibRTSbfVaGfUzj5Yi51YaTavxlcWRdUNxRjcfAZB_7dO1kk_F-c2EUnWrGJxFxKLfdlJlxRtXOt7hq3uOcDi05OfMnpfij9ikineobOjzNEUYTRLRx_neDHkl5QilRGqQNzGXTSHhp3U6g7p8m6-iF5qv6EbLPJZ89k6dU137q3I4GKRId6Ew3Vcnmy4UTaLUcd-ivcJrEDp2Zb3ze9-Ly0_JuBLmaCYRsX3_koXHMepGClE77Tr833Dg-bbHM80a3xBPFMnzoC8ghcqMLHW_0p5I04NAc-abA8-ryYnGZHPirwruTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNhoAPeMnsFWnQV_pQ1VCvUYyE4YsGZmMhLVbugOpECzopUWv8dHVZDkdf7I6pAkywxr1-x9e5jF9WpOrvIVdsanjHz7UyfzFI2Kl2Kj7SAjeL4GP3cPXK49lHwbwgWCC9iS8bS8knKQGlM-67i4K-zua6iYs8Od9MX9BC2N3iNobMbYMbxEnqPvkW49wy-G4zxCrXQH7Vg1_7lYau75L0psZLaxoiAEazN9LVIVf0OP1JerWnRdF7lVx7Mrl07CEHqCJ3BxhENBvIxYbxXqRFDGAS1svP-ICoz_3z8ldw-bUrtUB90nkgb4YZYZwDxR41k6R7mZ6J-39E2v49Tkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HifwzLAptJZL3mr4DrbOwa7lfmNXQM9VtHucQ3JYaNWxfcwKB-ZIS_DEhYNYr3YbxFfkwF-HJF1sSCFHIJNVc4SxIlEZQxLMS2juAK6DF8KhHSuHnoKtZIpy8ZziYB5MQVG2zJcaOJcf7vhg7cL0RT3Gh9XM1cooidqCc4w1Ep3eRmCykHWlnE6w44vG57yp564S0mX2wehnDyRsiZ54M7f8eqRUPFocTk3xwdQWibaUMYVJ9iS708NHglH8Uoagthx0yPiodEs0U5xrsf333HW-5Oj3J1Zyff3iCPowecf_G-sWFFPbKz-CXgT2ox_kmw-eRrhEjaiOKMRy5YY95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=d3J0TXa8gDmccFE5ffWdxRkMWVk9-j_C5wimSyytV2CeEi0yJJAXkgmyFXIZbm_1WzSm8FGr9JoJaDJFBeiNz8n1r5meumZPyYM6YYQCPY9xmJ8VeKYIayF0og1uR5QTXhii-PXIgUeMY2lxE-vbYxioyKPiGu-Vc5ojFwyyaQzDCv44HIVf8f6TLKSTrxd-AYO7jQgYv_Ui0o6-KBkfMy-lVeO7-NhyCUiaoCieoJ51Y_DldtKbnLNVNtlsLl04HxWg6QrWMx6FYeXcvE2a9svBTgTmE0_SfTKwHh2xD5vvVSWdRYSFYcDEgnIna9EpifZtoqxnT8NH1NW9mzJfgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=d3J0TXa8gDmccFE5ffWdxRkMWVk9-j_C5wimSyytV2CeEi0yJJAXkgmyFXIZbm_1WzSm8FGr9JoJaDJFBeiNz8n1r5meumZPyYM6YYQCPY9xmJ8VeKYIayF0og1uR5QTXhii-PXIgUeMY2lxE-vbYxioyKPiGu-Vc5ojFwyyaQzDCv44HIVf8f6TLKSTrxd-AYO7jQgYv_Ui0o6-KBkfMy-lVeO7-NhyCUiaoCieoJ51Y_DldtKbnLNVNtlsLl04HxWg6QrWMx6FYeXcvE2a9svBTgTmE0_SfTKwHh2xD5vvVSWdRYSFYcDEgnIna9EpifZtoqxnT8NH1NW9mzJfgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ts4it4KKsubhlLDoN_FZO7Nr2GjEoPy3hZbxm9mBHFY7ix7zqeLJvEoYi_lo8Rvn5Uouee3Sq1iFMhTn2aAvD3vu23JISLnwDDeQOnydEg84NOeTwCfHgtpTdLCn7BEgZwxp6K1Z6XpEn8sy-BHLhAm8UY0cQSDOS9fe7ByDALkVxHGctNoDDfoJCA99VZQ05xQ-tyKxpEMJoHlR9MVNxFcgPpSdJUomTRxKCbzXVlQ6-v3wHyzpB274Gxb-u5QDn0AZFuxOEWsvcNNo4kAZw2k8m7J5JBgbOskazWZ2EgqX6jaCApqsKBA8WIlN37KzZUoOjiOnmjZH0eZcwFDvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/swSidVAMm2LNB4GnUucQ9Iz0jPFmw_EGYmswOV9PqUjxUl8Gv6be-OdHi3qTccT2LepeD4KRK-PpzKsBSWsTJiNqaQjZ_Hfi4BI351ETtwPHepclmzWxBlOELemkp2rRRUXSSjq72l6wU5xXv_VFgYdKnMej1IRIvun48PJYSt1lmCfp7p2GEqaKJDaT0K8Ok04FRIKiPmiW4WjrhUzqW4T9tBxSHuidNC3liI1CRKA4UxYiSRNqGI2SIiqXdPjtoq04WjfE5EIs8Em5y3QQEGr9dcd7S4qdHLgzGVqcnfVo8cjfBD6cqZx2yZEug95ZBAo7lUzcyrWRxgGfoXnWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdAiObAHfporAgKB_9bEhij00KfrHCb4wDsOYCktKMtx-t6dA8oXHJZfAl_UNnh3Kql1SNhAfzYDbJlGgdqUdwWsb6f42BtYIm6rqDfmBHwJuvEZ2xk2K_tiu8wDvdxUFLgA2zijrH0hBxDbh23g0S3c0o_PAgE6BLWi4ks1kPxUW9RScHyY8HlkR2rDspHb10SStdEBF7dRpcceZxKeUENN-G9LIHvsgNU9e9LYVX0ZZKc--Ldx3POtC2tYiMTjksZTRK2CENpl3VuoKZPEorNaj0JuovzWcEaaKd6OE7oE7d0RqHy8hk9oIc4gitno1HpNmFVXylqFOOvGNsHUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=ai0j7z5om478lZ7wcPZwuMzB7p-dh0vvrbQQGZHEhSaI_xCEHSW5NmXGbagHZla7tiEMWYQX1wwUeGrKlUqUgz89--Ri8IZLz0LaEb2-S-6DH0dkQJF1iuEP73ALr07W5p3s6Vq64foICHfn-8q_w3q4TWyRTlGo0ubmouKKo2gDczAVeLrHGo5DM-EMFkQpWUIInSD4yC2Gk9yy2d5QJPW8fHLS9hXaIk-8doQBscNnNB_Ir-bFmQwU6Ci2w9hwrFxwbaO1Jg67QzAluS07ccxg6dFtdUPbsHDlWU7FEWox5ntAYsEn2aU5faV6N_4dWUCwrZLeRMsYV-zZU-V0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=ai0j7z5om478lZ7wcPZwuMzB7p-dh0vvrbQQGZHEhSaI_xCEHSW5NmXGbagHZla7tiEMWYQX1wwUeGrKlUqUgz89--Ri8IZLz0LaEb2-S-6DH0dkQJF1iuEP73ALr07W5p3s6Vq64foICHfn-8q_w3q4TWyRTlGo0ubmouKKo2gDczAVeLrHGo5DM-EMFkQpWUIInSD4yC2Gk9yy2d5QJPW8fHLS9hXaIk-8doQBscNnNB_Ir-bFmQwU6Ci2w9hwrFxwbaO1Jg67QzAluS07ccxg6dFtdUPbsHDlWU7FEWox5ntAYsEn2aU5faV6N_4dWUCwrZLeRMsYV-zZU-V0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBujk2XLFKdbFohVojz7ghmrbxurX7NjihT7SS25fSgCmnGgjdDJ1CyRVMGVLP5RhkqoRfCLEtPJOoblPuEJOXxEgq6gQQK0Bx7nXTudC8xIyL7rktYa1-6ZJlMixORsyoQhCM9Z2XAGd7qJKv-afKKY7iAw0i2p6_FmJgxQvujuZZt7s4CHjnk_cPb1A5T9TUBJZQ4XrPe0nvDXDfu_ZCKg1YiBspDILSKhgqpeDDafNVv7ksp3-KV88aRs3pOWdge-DBmCELGgLvdnIvvov3TZMzYzkbsj4JV3h3mumceNw0NRKCZsn1Ppl9ORxCxoTfzzhXIpZzplcq819TEe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6s58OHVJq80bzM5jkAL17A2-lrrsrQ35_T6ofPw6qgexJgdgR7RnbhD-OlglmbnQhmUxHMDjwR3OhGr0MTQvXMcskRgqh2xJiUUelSnBm4zQ07fHfHkQzseLTzo_K5P_zfEGJ2PdKPa540QqUF_ZAayVEgHeP30Ev_u1UIEXqZFdhm3RvF2xC07F3kmMNwBznb_-W2GiJC-W8_R9opZl38u1jO5w8BBUuA01JT3-KAOlIZhLP7MXeUGSDA6BZU3jREtBh-7z0UVnCJ4PeChsXWoWpcVNbSsE-PnEO9m0nDqSlJm6dbhxSXQxBNsR4ZWzt6cQJuBnG2DyD-1667WUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f1hpvU3N1JJnnYMmequGDro9drVY_YexxYRTQEvJhVtkvz5L4G9d7uzBEOJHUk4TD53C-d2ELv5KyI69CG6ajnF4378n7VFXw4-0kkDd0s0jvvJ0Ptfbju8F9V89k6p2xnx1kUJVW4h0nHGP5DsDFhGT5AGSnPdOc4iKil1ijT6SBs9DfEKknxaW53wAxamLvL3LAm2lZdjFt9dM_GVQ4MSH0NYvXvi7quWmmAkj4KRIAa-va-EnvH9Q1GIAhwFLUVJkODc9DHVs_WSI1L_l6iBUSjUkjY7kEnBZss0xyDq_9mbqVAtNVMmAAofSaoIti6zggCN-k2_0A_zPZg3-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mCQpbVDNV1OOhyAh0Eac8OvqbBfE5RJ1RvwLln-d8vrLDvwPvjWzz60pmXB3pJvjkYvkCqbk65qHR9nBQEc9tMjIvoXBY90jtfCyBJw2Fwe8R0CNSsykdinQa0V3CrvQXHoaLxfLCTJJMYdYWNZmISITOcebGtIDwltfYyNWJUoNu_Llq4H80wpjlNQz0S0eTabibJrzSY9tvKJpBZ0rQopws_k0x_jGaIP-0pXmjQ445saJg2rVawRQ7qZlnipIZ0Zz6bfsMPT6ngBe7dej0zcB6tj0lYPfrOZEbibXk-0DF4nlwnWxB0_A8iOY7z-2rdGPTCiaFE6Qbe680-c68A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVy7wvWIj-u6WpgaTCoXOqA2-56Luz7Es1rNAmOCRy-FIQvaICwF1hvsD0lM7Dg6xKAKb9naMyE5M2kp3xYm4TJnawX7GXkt01RhiGv9SRJ8K3fZ110DZYsfXRI2QOyMyNbfHkaWOG869x569F7k0S1p7jEq7JbnES2IM2OSzMxsGefDLIp3tELUbnh6WaTH6328tZzHfz0jPorkA_9IsuCY3MY3ccoP4T6YRazNMLzKznLtpMebcaIVEPysNHq8Ci7VL2nFVuNyIespzRDscGd2Fx4y-n71XFQ2l5OCQi_hShy-Jb4Y8h5ATWoM6XyCl3fZ27YAqWvSzNaypXtsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XhNfiYyfc2oqpegBa5BGuTQgo1RZalF3_j6GnkwH_5xd6klBHkiMdA1zxjDlrAIfTDi1FFG6ga2VINSO9OOKPrvYDZSgI2EkJIRCE62F8W-niReC5wOU1Fw8w2JHCarpZsAcQINCPARtyPB6yJhOvBKh80wLKVOZaD9sdVaSxtMZtn6okSj8DkyKBxJqmNqrWm7s3VDj2hXvHKtcLn4k6IQhecV81k-KEg9uyfKNliT8HURiySo_mpwQNSk0VmJ0dZeKkoOj1Kry_AAG6knNb90C8Kp6TSaJmf47j7mF7y4QvE2jZ8HDKtxYIPNMHigcfh1s6BCqbDxkLCR1g1Y-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=h6ZewGVA9RCBziPG5TqwNk7IxGbAwfh5YIx20ySCUZkvi_XZjPic7-DfN5DJBLCj__U7KCrGo0rMB6SLvInx3DXa-MJ3V6eFG0DBalUg6zHqS4fNAJYTFZaGCB9YFj4lLOFjFu1una4O5DWXWKfYGajaBZSOsg2rqLRTi6SevOSfNXw8AA2Ao8TA-SUtayKCnOKIuVeenIhCUFk85hNb2PBic7zUr5lWHA7_McYpW6tJLyRJ6qT_Jv8jlGGZkDOqmWJ2QFwbjkST6xz44C21WeY_E0HUZwMY9w76VQT3xuMTzQo1JpLRiZAZ27w0a32yIpCnB0-BbAPYQXwXCd-zpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=h6ZewGVA9RCBziPG5TqwNk7IxGbAwfh5YIx20ySCUZkvi_XZjPic7-DfN5DJBLCj__U7KCrGo0rMB6SLvInx3DXa-MJ3V6eFG0DBalUg6zHqS4fNAJYTFZaGCB9YFj4lLOFjFu1una4O5DWXWKfYGajaBZSOsg2rqLRTi6SevOSfNXw8AA2Ao8TA-SUtayKCnOKIuVeenIhCUFk85hNb2PBic7zUr5lWHA7_McYpW6tJLyRJ6qT_Jv8jlGGZkDOqmWJ2QFwbjkST6xz44C21WeY_E0HUZwMY9w76VQT3xuMTzQo1JpLRiZAZ27w0a32yIpCnB0-BbAPYQXwXCd-zpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NUWlAkXnDXT63_jsUlRB7hEbPlYdEMO7I52LudutOWqw9E3rROttpUtBD2U7sK4eQ1PKOc7WJSIDNzyltM96ZcWGPFRYcYSlDnV1tgbfPhDznoGTckmbzmaV7n7jIAtyqiV_KIYat7tsQGxrymMtqg89y-yuKizMATIwQSeciYWCZEj_jW_SnLcIzwLGbc5O4lwAlExKKpImEwp3l_Jk2MtzK7JCeifgX92vFpcJ_gWzqmSf7AHsCwUXfRaJrkxWIoDN_SoE_9yxkwBuvq_-Dvgdu6T075XmhLhWk-zTUcE4NzDPrW4CP1VNpaMg2Zn8J4xs6uSZylwCM7XTMCflIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u17KEYO-W_HnKESWuICxhb5DSRUERNN7fTzjVisgZpHssTwbwjaatY4plt68vpiS4WcHcuuK2rtjaHWxM7oc0CxoIGA5klnnRbH22OmzbobDnSCb5GxsgnYHpzyqdHSjL5WgkQUJGqTIDo8HHlDSz6wYNxWyMehb-w2fJqNMrzFVZ_vgk8bJz3qToS4ejF_9BLi72HlmXqH6YbHmsltLkE8goSakKNnvBk7iruirfpIG4M5ioggkhQUZIjD7wGLZRTOKFyPcy1k5_4Pz7ZKK8JuFwc2M2EH5m1vhtyeT6jmg4u_0VD5e4e1OVsC3r0abtsqCf0Gs61bNFHXfUkrZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MTSVBjQp4DwljPbPjYmgp9oaLANpNRx5_nLlR3J2fk3ee0Yl56hLf-UVLvf6blBM_jNlyWkEoPkfczX57IgJpCyoWvXmFp941GUyDIceaPKZkLbSEGx0yG2vU0nW7QvtnPYhrafO8pWg8lZk-jpKvlb6HFZ5rCQtbpFbf3gkQImmNN2aDvDQxIlPK6Q_9Q-VAen55loCSJI8HZy_s0h4AUkwvlvUmxgqodS1zP7XzEVnGknqNhIJPbndfOTAGcyEePAMFVerkMl4y7pf1_6-ASZuL5eg6mRUqLxCYrvPcKuMC1t3qQcsmdQZG63ItAFbEyt8bHUrv_6aXt8CTCVnRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPWeSs_jcEaNaUrWQMg3hZxxk6X8k20PFfC7X0g8fU_TWQMElS9Q-p9goOiU-h75G4ZxhIeGNbCv4VFFeukpWNPo3q-bQd2CYtP47DlA4K2_nQnJzOwauU7LRS2OoupcgVcarlgqARvmyeQabxzVx3hbdb8ARlWBlFMhrha7RW9-v-Q0DoERF6ZrkzrzY37sMyt6erg2QnaPktiFVNpAtBEpTWVDeURNx5a7M02XZSBzja_Bn0nNURf1JumapfcBQIpMMqvNrwNOW0gOqhkZjl6Zc4p-dd8cGBSP88eE_w9Rji4cEFtAo3oqT39xODabuMF6BQPi7Mld5WcBTx_x4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vujfsofbLgWmUdLbB2gquAAbLDJkZYWDdy30iDYQfl_7p1SQu-Y2PeuBr_rqzmDkquR9ntDiCnM1WKuSkED5tOrQCmTvjP-LebnFsNMyGQftypujDm-BofW0ijckVN1hdYcKL_fHDnXkbbvzJE-xSRoqXj_bmy0i6-AHJr1EIbKizJqmktRgfjy6pITZr-WwrIY5vaqwneXW2Trd1Ey4LQXIU1EJ3xpVqFxDEu3SjvXLioYNYahDlKag6A99qo6meBSoEP2qLbbNIIX1OOJzaEd_bttpaA6HtmqWygwHZSC75beoZCdNRcgPeqLFIjOPvwu5DSTp_-kv_0oTp12MvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KgIDtauzc94DDWTEbb69d_p5chvah1zePQkKRi9VSLkDXszhYQ93TK0Y8S-3hkBeNjgxu8PMFJZdrG3oNa-253Tzx38HAKFT3Yle2Q5HkNMaYaBGtrrNqrifW1g5RqBLJJxejtK0bb2WJ8DpVA0YYQ-c1HXD3fu9qPwbRxlOpqneB0bhnIJppr5ci-kLKw-QfIXZpaGzq9tgbDRGRiawwdGXhUC3SyrW7k4WvfU2It5W4SesjJsETwmWvGDUpfQw5e8wAK77zOuzYTLuQ5p65tKke3rNq3kGMAHXVRXpKXMH40fQ0-UvB13EdQ5XxuihpmEj3QnzOfqgHdIkRfG1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sMzGiQsz4ikrrg8aOQYbaN-fDXQNCpO-DQY2kkxGyAVmJE51QlvnOs32cStrQMOLqj4raNjkbnjgFZhVf0qVePq1zTUCn30R8-b5-b3vXd1WdnuLyyxxjctYEC104i_E0FlzTCaHKraFapKGQ_LTBllwFHbURyYHZY02SyavvV-7QcH6fB64hfs-DFNaKoklVQRk_9AdBbEelTHK7ewjCYf9rMC-tDtfL5ruU0AEW9uEw7wM9Pz_IBHL5scpt0GEQyNifDbiPfDRcLPiaEY1X3vzOqR_NB1BmPO30IBtkg45bENPOLbN9voasliO8f7k2czjTZ8GsMX2oIuTnv_4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WZsE_SjUeWAoY_tzKToeZVlo0yYtpDQ3afiIuonirN3CNcGeRQ20crmsXMSMVkWCBnSQvaAdu_KDiSnYG15GQ4Te4z0Kibf6kjxyAz_FkX5GCg0VLfO2Seupemc6oQqcXxUCTQo92_PLxbiQcxNcC755AxRPjtxupQAZFXnzmBk0J9AN7EVWyWOzwsmrZGrUFLYfJJXJmZFffIIWKFT4FwCjHHLkoXAGVzHXGLXDAP6l0IceCMyY2oNUgNaQfxX3MqrbZj3cXDkCiaAf-Jm1zLNvaxtFo-GLhqCP2yd01sn1zYuZ2gO2BQCv1NaJEkwlt7Li-UwiKJ1W8ZQUkcJl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=Zj5RtXUnNqlsefhd4hRORJCTG5bMYVGc38--wb7YD3PYssmDVqzIxr-aUxLZe0pb9cW1sZIamPLM_vr_cPL363vQCm7fp0LTT154LJzE4a_bIHFbkH-n-k4Gj9pz9acHWTOGGW2zYkHoGGwuWZN1XP_RU2SiISxcbQG2GgbtPqLnPfjbUzKaFqWtINUIiNlKxqEkA9Jwv_JKRVOtC-A7hblMZJ1l1kbF1CVfrDsqBXnOcwgKFbWzHDJimhvTDy744ReGF9yopkSv9H5lpCM51iWobN-NULbS3-0JfWI8l6WR67gXe5RN-tKXlUUCOIIImYZsghxczOjW1WV6ZnzsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=Zj5RtXUnNqlsefhd4hRORJCTG5bMYVGc38--wb7YD3PYssmDVqzIxr-aUxLZe0pb9cW1sZIamPLM_vr_cPL363vQCm7fp0LTT154LJzE4a_bIHFbkH-n-k4Gj9pz9acHWTOGGW2zYkHoGGwuWZN1XP_RU2SiISxcbQG2GgbtPqLnPfjbUzKaFqWtINUIiNlKxqEkA9Jwv_JKRVOtC-A7hblMZJ1l1kbF1CVfrDsqBXnOcwgKFbWzHDJimhvTDy744ReGF9yopkSv9H5lpCM51iWobN-NULbS3-0JfWI8l6WR67gXe5RN-tKXlUUCOIIImYZsghxczOjW1WV6ZnzsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U29PlSI8ARl_g7j4NjAAKVtA5pU4Yv_78KCtgw40kmoYeAwVecQYAf4Vn1WikCwQJO83qxu2FY8aUqMiOWq1prYMzw0zE8c-GxUidTij9jTbL9_lTHQAzO12v2MoG-QIRFNwCp0fBHfu3aAqAETkG4vze5wY2tAzshXepsDJWtnd51HUMlm9C_2hdcfWVvo_CEJ317mVjjAsN8-zF1NZt2RujYoYeo_fiKnSSeOk7Pjura5nzRSd-Vh8M3Sn2cjFYemc69tbukWwOQyxrSMQcuMUK0rE4a8YssN1pD5QbUCGEPZgEzwrTycjXxk0zU-z0tQ6sYQNLH8SRcmSRDGnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ocFeFSDG3AqhA1yHnapnZ_WZeU86J3TboQcvopRSqi2h3Dv6sG11U_pqF-NKU9bKSjhpFhbp-kOMP9rNvf9sv_EwDIuoDEUskpKaOHKXacpIvCIJGwwZOrt3mjOhTL837Q5D_F1r6ROK8-uM13lYF9SOIjh9H2qev1LLMFnfsoGaGMeWeKuJvIFAyCxQsoiKaHm4QjZLTcJvVlUocBp1SqFZi498xI9kPEaN_rtTn_SMP4C1mo3tk79CCS6U75OCtYBID5UH7tUjBFYlIpNI4v5TSKpX2GXcqJrhHWV7OEmZaVGABGT6uLm5fxf9rOe6dx1W4D9HzUyZoooV-TRY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVBxpHnIZWmdc5tBiu9c4rJgrZ_hJCX1RAvZCq7N1k_ztGrliE-VGhrulioS5FrkBUunLxMaPR8mW775oxnHyRilIfLsJxbAHxWtmti1VPV1_39oQT5JlTNugVTgXuuPNczRb0XkCa1mb54HC-SI2blWmfzgtFjPnUKBdiPXoiqspsuIzTkXEmtpV8HGkMXp4mjlYWIs5XhRFgOjL1L-uLv3Ec7D81EMl7T6SpLRG5tUytenalp7FBVDHHvVjzE08J-vIK5eRH0dCEC8bowErDrBa-DOfq4CvOBA0u4B-98eyHFP3UgWhtkZli7V1NR7Sl7lGLJUgZ6E5Q90RSqg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaAtWXtutvSzz2-UuvvQxPaH0YIym-jS4yR4Lelcf36OwChy8kk8_zid52y_MV3Zr2FC7ZGAvcu6AzvRT4ClmeeomNVS8iGa9bQStoqH7m_N3smon66pvqDzA2dw0DHOK01UyhHGCNAAl5Pv39aGv0DZj79kxucGjkYF_5lKGGLc2f9BQJred9G55W3WP_-2N4st7-XDosRzUkatIMDKsj7LgsX5RPyAPWc-gZpeXn70KxOH9ctDtUktc6HFoWSbFbYNE08kcg8W7Dooo6DM6P_sCYNZzQ7lTWvYGRrKpjykDR7tuGhcur90BnKpr9ZegPzIUqOEkGWbQ8S2oS9mDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0sz5rlEBSR9o3OvOROeFWCf4KeKhlBQ8AtP1C55KAinCcQA6L-KCrJhfD53FWU9i9W1jmRUlKmZEleAf5qa95zwbhucBeKwu7jX1NnJipN1_h3A7Ngvby8TbX93r8H6SCq1e_l2t0ngn0QxHHULXJdy0wbyP-ryp_kMtIfwJ8Ez17lUCmt5N6G395qi9LlVY4mgf_eotylWSVO8aqDpWyw23EDFAuheDi155e3l4sUOq52olTahYXZyRuL5zX8_bzDy7R1PLM6h4yXKMgSlIXBI3wH5_KpVx0G0qDYw5QFsJQ7GfP4jSihwILOq_e7lyx8S-A4bZJ4BlqTFVtgk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIkVgCBX6hqjbk627awmbve3EMh6kzzMd4_VdnxsaITY7MtKI0GN5hvD8wXcuwtVfYpEZBMYYlnQGelBrGGdZ7UXrnFkNjvEUVwyTSXanzXmrEwaBpX4c-oZnUuzgneKj7Fzp75ltWLV5IN8U1sy4g_63RcFXa8TJFgaW20qugfHUDlx99_VDq5rGJxFHYDEEtgeWPq7zRU9yvApZn1g1K550jA98B0o2cdfgMPiHfz91H2WqHYEH-SRvnJMzovQMjGeUg2v6aFppmflZTlfK9Cran7EmnXmrJxdClhts9Shoj0oU_a6Q8s7VdcsGW0rESaY1C6DsDns_WA_-l6xXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WER8r883nXjYX-WQ04n9W7fsFzLDa3L6NwFIX_55wDDltAldl-2d-McHli0rrndqY_Fm7qPwPnoVhcMaH3DyCDeN4sy8xk-GLqXmfHNkZesAfGnBFtVHQ8IngMM-7teLRvcA3XDednfqaeRGD8mFhBFs7-yCYPnBJ5q_SsR1aN0-M7iFmeXsNvqZPoeR2KHbgAv6o29sc2CDAcdBpTz7WRxys3NocRNaIHOr_ahQyyxyMYCBUrd3Wazfi6KiyVUMAniHvq-1OF5i6KyH69e9QwjGkeDgYrYPKthYqmRSsOOaqy3Jd2ljRq7lWvfxpQTMfqb61reYVZWr122G5VhM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fWLu0mUDwa89m8ldRpewHFraldI-O0p8BDeVLG6BVULatXjeHJ5ip2KMbAFGx4Tdi1w8dtnGEShf359SF07KOZhzB5GS9s2s3nTgxEbMz8qvWazvZOWUC6wsqLAVTOs4B8vLj0-0quSajodUN-fq0qpLKgiqwSAdAA8RYkVWsxFs0uzKqp7x00xmqypk7P9RXa2BQFfZOVOdLneqwTkCuk9NN5jh3IqQRuisFRUM85I6bXIhHbGiJn4zCtZPY3PHMlqwHn7MdegOBRCf5V4qlXBMMaFCgwJE1t50QY-zoXXDoUWlos1ahevGs_mHgCeFpwOXhMns02G5oZe4ZtrT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gK2xoDurfKyjB68IktmEidS_V-BCw3Ur4azw3CTFobh3IU73ZLQDjMvbeZ-KdQ9LgUcZuR9oYCobhHMJ2Mf4TbvgRXXWBB9pBHBi4TZH7GLUcuZFWTVuI9oA5axGR1oiR_gFCxQqHkCWX45JJ-D5e9hK4vMR6BZqb5rA1IAiBae4K1fJc_d1IZTN-AACVXKYB45Cs52V_vVefUxMjR2OscDUAMTjRfVbjrWbcdJmhvay4kGrIDNUqmJ4uDjVLHa-d3ncpEJ_NStBqK9eHi3sfJ1ykdH8TcZ-Cca96DmHuZ_pPiIlCOgBhAFumy9vE_XQ9RJ9her0vXm_lgPNn83npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Izb6q2jz9JQ9ZgoiTM6elRm0p2C_4uyBYeuGu6EZenfhmQ2IyyH8ftinApkM9UbWne3TA4y5gwNPcg2x4ycQTk4HX2oOG3L6jm5YkZh9eRzRID9slq_tC-w93uXwCxVpPg9syoQQ_WtbrZWx7lRUs9BPzeasX0r0H3svNhFj7FVd-VopgW8iexmcMsN0maXyjK06tV9O79kwfrOGOmultP_9Keu7oQcc7LzKSkcRa68Mcgn8TSTGwXW4aPBu_wd5M6Yt9OusKNbnbSt9e6OeFo3KQd295UuLjCG-EbEFUtarlLKbYOMEveEIQL_hNYWXiS6wQG4iBtaAP2m_sbbAKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jcdrSTvMtjl3C5QgAZjIOkM17AAjRF5KrAwdk74540SilS1acewrRotklntdQHJfyMREVjBzZRsjqn7_YCJX4qDWiIB8kqF-gUmqXFnVpvYlPRQzJhdSR7xTmr21xvzCWErrl4ihpzq4czj3VDtc8HBbim-QqncdXcVTWoLd2adJpj-BywDd6s4ozmqh-y5wiWuPm-lo392d9dGy2U0FF7e64A_BOUBLgt-5AJq2lPdQo9moMVaPtstV8D8_3g6yVq7MRR678fjTz-IUbsifNudPIevgUNBWXEexJiaos8zS_dj7QbQkE3a9dbJsS2mJkAujCobfii7YcOymTHCUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=cASzJ36m9D8y5TKaFn5rwVnSFYVdHPsT8jMei1dL2o9AjAfjfy7DdMWlyKfLqGOkViZoYNG72xtlsvlKNfoukkor-iFrRtszPW2u8bTd9c6b1HRt2r7MKYAuQ-eS5UfJGBzphkG3KusG6Ds_GvYP0zDCtNvd3U9x2j81RYZKGd37dyYSdkkaRKXXQF7PUnC-JF8QwPiNZ_eZAnuDDcdCloZBXrWwZPXH-vJ5Yg_iHaP2cyTWP_27V9bmUK_mDH8AEI9mX-qJA1qBvHKIIXhuuzkTf-l-IkHLeVAhmBkAj_o6BJCSFE8ccJJjregikOzrClcBYmYp523me1UOF-AtDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=cASzJ36m9D8y5TKaFn5rwVnSFYVdHPsT8jMei1dL2o9AjAfjfy7DdMWlyKfLqGOkViZoYNG72xtlsvlKNfoukkor-iFrRtszPW2u8bTd9c6b1HRt2r7MKYAuQ-eS5UfJGBzphkG3KusG6Ds_GvYP0zDCtNvd3U9x2j81RYZKGd37dyYSdkkaRKXXQF7PUnC-JF8QwPiNZ_eZAnuDDcdCloZBXrWwZPXH-vJ5Yg_iHaP2cyTWP_27V9bmUK_mDH8AEI9mX-qJA1qBvHKIIXhuuzkTf-l-IkHLeVAhmBkAj_o6BJCSFE8ccJJjregikOzrClcBYmYp523me1UOF-AtDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nGe2iFEKy3GfVbisE4lblMhJf5t79xT_hSa6ao7PM-3vFXW9MEnbFfxg0mDAWtr2dg-WajqyBdPuVld45IkKOIsQ721zkKBbWgfa8y0LI_E1UOHBcW_3wX8QgydDw0QRRp-jYeZv-Fef78x393yZxP8N8BzQLZUlbB0Ld6MoHOBozPKRgjomM7NCe1Di3QzmM8sZ_EKSSulUqcW6BKrtdnvEP01lzXQ-r-NvndmNXI0h81yH5oS_smV7Yx0Gk0DEhwQF0Q4CYpGXTcs-w-C-mdlcsyIGzcjcVDP28yN0rwZ1NIO1tqxaMjPXMmqQnJ3N_5OhL6IDVuMX8lGeJcz1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIQ9RzsH9w81Z4Rdtcy_vmWw22W4jZfd--1AYsa7vONSJpJ1PIEE6Lhs7X6IRPKvrzVqFgUIGJ2dKJF5Z93RsHMBSM_pEZY_Ja6aAz4_aWZcw2U03k_X6vE0kduh77vyJpkhH1qjI5WnFbhdzLw5BSrNolopmn6j5tTsuV99-I4dOzvxAEhJwixHUYWzZzhF9zGODRI00g8EVr4_dQ7an4Wlz3ui5pCDflr1bYCVSNGVoydzFD8BegJ13MuuOhDb8ZJQylSEs8Z-tTn_Ce7loc9aBhGxlVQRg2bOkW4_VD-uMPHAqVHtV9XSjIUaZgRY7ZiOJovzr1SMjFnCLfpYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_upDN4sIvNY8J-fjxZzuj9ZrK_uGZctuzqcWbazKGcb4uKdT-V6_pLrb-0WaURkOHXQpjmaVFqETw-A8zQjhu7KqWJNrkfTVgXTh1k8_gBYmBisMDALhK57dj4gQHI8hro0ZdFQIq4bN5klF3YPCnykpOWMKAf0csk1jdMEfP4abeBVT0pBj6ljXZ1zI1nJHpupxef-inEAfFpHy9eFtjHuBqqTLLUmAHVPX88sNTJDMf6rGBf0E7JdZ87oxhIzY1X-6UGETFS4En9AHJCQ6WuBVDThfoxm-jA9mew9vBDnRo_g2hhynf9-WAxRnm9t0exk0INaC1eOG_FZHC16JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iEDC1h9z1vKxCSXM5EadbRoUI5uKBnv78i5qdGs9y7LX5juZSiWwrz4GPLRIs8Y0WAZCSPId_VkcrHdZQS_EurqE33nZwlZaKRMMjnAXN6BIajycRgAMnPgdWexKDrRPIJAaWmD0zbiCBRlA3AQzL_X4MOmdNDbaZWtFjT7zVCZqYlFiC_xHoWZiL2iVZntXspdIcJLF7qfpNlJHYVqVbYa3B5WZVSvk6fmFmlMscHdzn2IfJ_cI2Pjo5OZcc4wxELQYjS2XVd5IlkQSkrsDiGV-VxOZqy3Q_p2lJC6Sr4BeSH8WAUqiR_YlM_8VBrUavJrf3atJuN0m0bxqBULVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
