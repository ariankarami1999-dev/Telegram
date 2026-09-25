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
<img src="https://cdn4.telesco.pe/file/ixCl_7hTwlV-GdJeN2zUWdxaHdnA9WeV_9_KlDpPCwBlEW-TrUh61Iu2p18HP83kaL_wrPp95HsTLIml63xGg5fbGvWc9Glvx113zT4voOkr-KX0Y2A69VIuuvgEsC6eIMTh4mzll80bV7pHsatYqG5ehHxav5sIgitZuuTtzcvE5eGnAU0YHlohFufNXxp9PY28wHOBb0vwF1a7gPY7LD73ye1hGbwIkob6uYt2dSfew1Qb4nJfFkZheBtqFSjvPCm7hlkQHj_jElyfhEVli7BjopthXgQ-zstfV-a0cjPtWR066aSUJgxOf4-8RH1nXgOGzJapB5Mi4Xlqc24IrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=dnUkFoKNLYMJ-kEZ7dcwWefejFIyRorlcE4dl9rSjQoa4X-owFFnlE4Fh0W_MauzpHKcbCutZnIRMt7PeEAQNrqTYYsT-ee5S__cROvjA1R6Z1100jgN4dWmeaZKBbQCXAg-0Q-UHEcS1yETsl1EYjbgluhDLPASc_Ke9XIm2l3yc6_1ceytpBbQLR3Phelx8ocKp-NPswGWjPkl7On516KytYaNENGPXMFC9ZTI8INCZ2feNdS7IyZd0yqebNUclDPuAlu1t2_C1SeuyOjY7YO_G4KMIOFH8aJ9K6jWMmKqraFwyZi56kTV1ZxTZudKOKeJOjv4Kbn9yEs1YweW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=dnUkFoKNLYMJ-kEZ7dcwWefejFIyRorlcE4dl9rSjQoa4X-owFFnlE4Fh0W_MauzpHKcbCutZnIRMt7PeEAQNrqTYYsT-ee5S__cROvjA1R6Z1100jgN4dWmeaZKBbQCXAg-0Q-UHEcS1yETsl1EYjbgluhDLPASc_Ke9XIm2l3yc6_1ceytpBbQLR3Phelx8ocKp-NPswGWjPkl7On516KytYaNENGPXMFC9ZTI8INCZ2feNdS7IyZd0yqebNUclDPuAlu1t2_C1SeuyOjY7YO_G4KMIOFH8aJ9K6jWMmKqraFwyZi56kTV1ZxTZudKOKeJOjv4Kbn9yEs1YweW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROqAPsN_vPouGQyLQdRSu1P081EYtSRuULd7yd9LLWaWdoLoTUYHzcq6Xm1O0EupPzqviiKP2YhAqDbe2ZMfKRi2IjiBQ8TBp0q6sj0_8RofM_YczPhne5NR-GKXCCuMvBtlxkcl0ZYxBkqux98yc-1PfHwDpNAZXDLqsQgMBYkjGtyd5BNCwZ6g9EmjeoZq-yHTqmIcSBEIDDvNXG-A8wuAtEGG7RCo6KsaRlFhnf_lEwZ35D5IIf-kFY8MZWuBcNuHDtyyRZE1nJG-0GGR2vAmSEcSsBJ2ubIlPO7ZnV11-O8vth_pHguDd9x0c-8TyLP9lpSVmXr4-3nvrqGcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=lfowCFvWSfaVJsOyxu9-uz4IU8oOwrjdHNGSHawu6NBvlcpqnnR2waytU26ELVai56Buht7UUyPKY4ohPBVXPIFtfVR7Xc4O6pq346q7pxvZbwNgGHDqDMjuo68OgeG-_OKgRrnUQ1SVSdeMD7OkWbP2il5zGe-sfA0kfhB_lebcNT-aktUpshXCgKd5H77Xlnd6IlScj40eJ5XLXuPLKVpv1BJHj9Z0b4zHWRebNnww6cTdbOYh_PGtgZ3eZ21bossZd-Hylt9N3pp_nHMbvL51dxZen_dgaEZcHynvzltHMOxmvJ6A-wiXWM_vrunJFBJMT3nyPxdP3Ac2TthqeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=lfowCFvWSfaVJsOyxu9-uz4IU8oOwrjdHNGSHawu6NBvlcpqnnR2waytU26ELVai56Buht7UUyPKY4ohPBVXPIFtfVR7Xc4O6pq346q7pxvZbwNgGHDqDMjuo68OgeG-_OKgRrnUQ1SVSdeMD7OkWbP2il5zGe-sfA0kfhB_lebcNT-aktUpshXCgKd5H77Xlnd6IlScj40eJ5XLXuPLKVpv1BJHj9Z0b4zHWRebNnww6cTdbOYh_PGtgZ3eZ21bossZd-Hylt9N3pp_nHMbvL51dxZen_dgaEZcHynvzltHMOxmvJ6A-wiXWM_vrunJFBJMT3nyPxdP3Ac2TthqeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZzmViQVCqAzesoPE17IIqn9A6JGMCJzwxEYnyvSM7Hmk2jnNeslMEzjN71pJaoisYomKi3WHroB6KM43jrrzr2nezELN0K02Fq65fN3j2VfHGSS5mKIpcxtvW3Ne2LFgkumU3LYZneQdRDTCrkqCxYOX2hj7Slcio0W9Kc7_6ILzXmjaNQvKcGNx3V18c7yzASV49PPU1MaHbkUsn4dhYcvxO8rCSeLUy5AIy7BjKbHnCxe7DuiET5tl7Ktj2h98Ybi2BvUw1SK3skqZ9D_xuknEImqCg8y6l_okuoXIy4R-tpt7fO6S083P-KzfcDWt9C5IMGd2jhW_gOtGleq_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZVNIs29jpewDUHb_IXa7fs_atEjJynlIfPA2tRX7mkhrp3kgiH5o_rXfDsnCg--8lifaICFth-VFZqiD5jTTzrRpSmjR2a-eSpX4dcjv9VJSb5tA7fRo4S-yAoRrT1N1yFEvPT1OHzH64uQUkytIUK1uzSoJ9V0nyGWFKwqU3sedCKKo9x4riB3wM16gTihNzRrtzEr7o1QcZBblahKKCmrl926w4v-eSnj2-dAVf7Gl01UTps6LUXuFn3Y6ePlHcvlmTmik9-l_WuWKQnvh_8DaaVp9fgP9BpaekJOAFBYu7EnWEz9tQE-ufymZM_Nz33B23sBSVZXX9cDPNXROWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gjFnm2U0jRRrJ5avULf5DZNTUktOd9JYNIMiU90j_6k1YibnpVwcArAJz7e3w55CPloIVwLCwlPzPb5SV9jXgdG6y2Sq6gXMIWvRofx-rBhW969sCdyikpUffHYOlSfJNduZgAT0mc98m-3xARaeRcRabhYvaeWpMjmGSaT60ZTdKXm6h3ksIEOydHfyxLZQETzu3rpB3_9fnLTZo8A-eECBTt7dsWpm23fSRbdeLVKFwONIJTAQwga3s5LkiPcSO8YJ-m7YRL9Q0Q59TnEz5LDjwTGB44KMeMlxCubJgFtG9N1RPOKOyjkU9UE4yvg5ujvqpHLnpsPzntjwTSTtoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aopbI8R00m8duGMYPFkrv8mLqo-Vq36zq7c9CmQPjZpJi8K5wIMowTAMASX70Z9X5DqAJjF6JiLlARaSQMstQVCH23G0YOhTizEVzG2iA9a0SOVp52l8K81SW2lBuYz5kqTBwu3RYqAF1sDPmdUsBA2ISOxsuQmB-oJZwKuxiw6DfMxEspIkyJV8EcDiqbE3Ok5pVxWY_OqIudLWujwmoLLimjG9IopNltwcbtGHhUSLBorAyTIGOT5T8Rdzym1eMwFIKgrXawP2gr0_DeevUNJ6WKvEXh1C7nZc3fEUL5wFILJEdPwvQCuZS9nBKKFbO5ocgZjqZVwxCPp9-JULRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X34z499UA6W5eWICMpDLf_hvc_rp3V3v1IjciMzi0BkkJNxOcV0nTXiiYGvDzxw5HIo549qVpr5krDhrq6GeBtBVrvTZeqkf8SFEkndPRrmaCxw1PXrNx-Ic13R1o_Ciskon4hLs1iU0T2VoHRnMP7xr-IBtEbEh9eP32wEaGCiCWwnjb2FzCOpVuJC1e_HkQWe3TkhIEWvqgWw7QyrGuHCA9WRVtKuLNqg634qVWxWcS-AqPUfz3jATKRt00MKdn5o65HrhUBuNmcAgJee6PGNsI1a_WAlzSxPgPvQgTI5uly969G5ZH0qC89VvkihyCM74fbrWX6ohafpjr16sBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULuQtdlIlwJy3_smn5THeniEMa_MEu-xqTlrbgA9BrP_Czurr8TDvH5IrIF6HSNc_PmE_g0B8X-zggcW3FY680L-khoYBK6vnfYk7gR0tOWKISvHQ-xFtl8BHFwmTqq4NtrSdbCAe_nejihI-_OA5EpcRzgGIO-1IgrRHdFzWZBMd9C7r5TkbyJ-TsZM7mG7wtkaS8zCvt7VHiJFm2NP69RDCY-y58xgFly9GEeFzih-I7zxjqAnPb0KCPw7maFhJf7U0ux20kd1YLC6stsv234zoSEShnw4rsaWnqX1ZpOz6fUomj-yj61DUjySP_yox_sG0cAAfqR6IDFQKg3dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSsLa7t_QloWFs09jHFhrdM1KnGCVezu-c1pPyfK2hzCrcHAq5CYh7832wYRd-V_EjXCOXQPisnUx9SMF_8jYtAdEDxwydtB8JV_M6U9R-vO6uoPB0sYPbA77T8ZMxMbVq5poCwqvzWE1UUGbBpJ60FcSgqFP8VOea3eIl44yxoQ69wzWdBKBD2Gw6NBZcxnpGKOEjZoaYU7hk_Z5WjxcVjHqPM3ocC0YkVP3sEgrJ7XvIWeLWplLcbqprjz9OMAyMju6bQxsHBdtzUvT5ABXdwvgaOjwPmTJ29K7Xl3wkzBnpLX0i1WRqHrDxPj5kdQ1kZvFWhSmH44bd4l8h5kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=qWIOIdBVN-tHExtr4FXHxotL1-d1v8Tw6AqImsMvz8ho4eshh5uDodcveHzEra2PNQbEsek16MtCYufBdO4x1sIv8PqNu1iAJlsZ8NkIddcjat01s3Re0vTv2-vKO5qKfCR4ayJnb50FkE08czNGCp0ebhjYgMRgghmUo-hZGSU7XN0wkA5AyqVzgKo5OWI5qv3hEhynB-uOu_cUVDCaHzdczMo-_0HYrbSLZ2nRxuST1YDxff65xjBEEL2VGB2iTMVRoqJTCD9dtkTsGSQN5EP02AhFEy6_ajAZB7M39Z8AWGhq1J4GEFTATw4sQ0OCQHgIjVIuXTU3m89TDTVn4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=qWIOIdBVN-tHExtr4FXHxotL1-d1v8Tw6AqImsMvz8ho4eshh5uDodcveHzEra2PNQbEsek16MtCYufBdO4x1sIv8PqNu1iAJlsZ8NkIddcjat01s3Re0vTv2-vKO5qKfCR4ayJnb50FkE08czNGCp0ebhjYgMRgghmUo-hZGSU7XN0wkA5AyqVzgKo5OWI5qv3hEhynB-uOu_cUVDCaHzdczMo-_0HYrbSLZ2nRxuST1YDxff65xjBEEL2VGB2iTMVRoqJTCD9dtkTsGSQN5EP02AhFEy6_ajAZB7M39Z8AWGhq1J4GEFTATw4sQ0OCQHgIjVIuXTU3m89TDTVn4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=UrReZyOnsjUjJO7YHaUnM2yQL6fxrSGOcW_YxTHAaHsKhBd1N5MT88MgB4-PSxx7cqjwX8YWG0F9gDf6V9cLB2LMEnnHbdjiazim1cN67VRDm_ewFL8uVQ6iECo-0nvHV13ODZhY6bAIj-7hNe93bRnNO6uL9kB2ppQ_rMxQu4q7U4r531fMKGOSuyzTAsXJu3jsxqY7Z6Zdeq5kyExvGLaEX5RMUJIIhLhnVfs1-Ql726Nk6WxsRf9cdhvdex-O4-3ID74a3XrmeA39NWve_cEM7iEOreNaMsv37LdHHUcFwIMsCBlnTTrQiQSn98NBxpxiXq_Etr1SaYU2bTFj9qrWJVlpQPW4SDTb3AmucwQvnroYmsBvmNRSoWSa32XzUa6u6pxXtlh8aAc-mLtAClvaU7eCOsxZONJtoO1U-SdPMZl_MuPIkRSBb6wl171oaFw6EgrMML9UC6XFyoCVOJEP_R_IF0QBCHH297Arzx39lR-8tVteF1LQ_DSCKwBOPkmWMw_ODa-hQgl4fPlJNxH-UeOp5ov2rXpVtK_Cz3MIQnpBBbJTMJNXAYB2UvrJ2ZRvmSHiPD9J357VTgAn5WYs-OVfbjusdi3lFoOkj_4bApCl2_p-_5I4gFptGHaZI-R_olWBoWqDSmdTyUShsL9fSJDPcgLBtlOje-P3E7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=UrReZyOnsjUjJO7YHaUnM2yQL6fxrSGOcW_YxTHAaHsKhBd1N5MT88MgB4-PSxx7cqjwX8YWG0F9gDf6V9cLB2LMEnnHbdjiazim1cN67VRDm_ewFL8uVQ6iECo-0nvHV13ODZhY6bAIj-7hNe93bRnNO6uL9kB2ppQ_rMxQu4q7U4r531fMKGOSuyzTAsXJu3jsxqY7Z6Zdeq5kyExvGLaEX5RMUJIIhLhnVfs1-Ql726Nk6WxsRf9cdhvdex-O4-3ID74a3XrmeA39NWve_cEM7iEOreNaMsv37LdHHUcFwIMsCBlnTTrQiQSn98NBxpxiXq_Etr1SaYU2bTFj9qrWJVlpQPW4SDTb3AmucwQvnroYmsBvmNRSoWSa32XzUa6u6pxXtlh8aAc-mLtAClvaU7eCOsxZONJtoO1U-SdPMZl_MuPIkRSBb6wl171oaFw6EgrMML9UC6XFyoCVOJEP_R_IF0QBCHH297Arzx39lR-8tVteF1LQ_DSCKwBOPkmWMw_ODa-hQgl4fPlJNxH-UeOp5ov2rXpVtK_Cz3MIQnpBBbJTMJNXAYB2UvrJ2ZRvmSHiPD9J357VTgAn5WYs-OVfbjusdi3lFoOkj_4bApCl2_p-_5I4gFptGHaZI-R_olWBoWqDSmdTyUShsL9fSJDPcgLBtlOje-P3E7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=Ti2l_IW9aHqFTCwZYYd5GuEZhgtzRKiL5qiDr_BFQqFxiFBYLI5UTRRw9itBZwWR0gcicnkW49VGRUceilt4XbKFZNZej2b2UT83b7Zxvj673grMVPgzV8opp2OxI6YZXQIEZzWxOXzWMQMQALVmFBFf_hXH2sGiS7b055gDOPiZDS0yvEJZdWymZFbfz5FADGtTUv6Yhpr92rNGfboFZ6klY9YoTbGIFnJ-B8YfB8pclc2EZebeHwF6ReBteRN_kHxqDOdrSdkn4c3NSj0GlrbSfPzTWtha3BYDu3DjFaDGVRhNzFaW1ekmJSrVdLRHvanZTtNQFsEjOviwlnEJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=Ti2l_IW9aHqFTCwZYYd5GuEZhgtzRKiL5qiDr_BFQqFxiFBYLI5UTRRw9itBZwWR0gcicnkW49VGRUceilt4XbKFZNZej2b2UT83b7Zxvj673grMVPgzV8opp2OxI6YZXQIEZzWxOXzWMQMQALVmFBFf_hXH2sGiS7b055gDOPiZDS0yvEJZdWymZFbfz5FADGtTUv6Yhpr92rNGfboFZ6klY9YoTbGIFnJ-B8YfB8pclc2EZebeHwF6ReBteRN_kHxqDOdrSdkn4c3NSj0GlrbSfPzTWtha3BYDu3DjFaDGVRhNzFaW1ekmJSrVdLRHvanZTtNQFsEjOviwlnEJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJkUNyuPQpKNv6Ba3dVzxD77T04T5ebyprA9tfNAF-He8F7IDTDdHh9u1UWqmBj8OgQZIzBOqWDtqn3XSnKggvL2sQad0VVq8kfTOcSYxSu5m1yjmWoPzoAWW_DPsAZOtVm--hG1eYDOkn8c_7xC2H_4OeaxR7lbfQ0CwjiED0zpwqWIFmAhpyzhuqa_ZLNteldWT7wf7mUEdXclfFVlP4ouurp7E4oi88ui8rvRnDqCC5nFSlbUy_DBZZbnSByefceS9hJMvVVN6nzK6n3lDdlZ1l7h9rd8qtLMg6rDMbTwQdfHwuao3kUO2oy6sM65JFjDYAt7x1CmP7P1cGY7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=UQPcrDpvu-EW_Zoi_8BAx5Y9gZnOe9cvnh-6RPa-Fmbu-2cz6qbwxxumq5X5h6fWlRib-RXrvRp9VACoRHXhQOkdYVntLLXpPVvdIp9iehxD3NG7mWlny7GSiyfvAUZr42IZPJO5ieQndRbDqvcyMKQljXL2bVW4gWCm2nvZWnaVttqVzXkexXV_kk68Hb0i1YIK3XQZev5YcYvQBiZHdrXw6acvvp2iFI1t9Gsyb-j4BsPRPzshUfZ1HguF_KumdUBz1RA25Kw92_dep5AfLC91gWAVS3-oTsMwsNpXdqjIy4wGMoRGdLmvYC2eo3emr-yYhVTcoNhN_NBd9xv4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=UQPcrDpvu-EW_Zoi_8BAx5Y9gZnOe9cvnh-6RPa-Fmbu-2cz6qbwxxumq5X5h6fWlRib-RXrvRp9VACoRHXhQOkdYVntLLXpPVvdIp9iehxD3NG7mWlny7GSiyfvAUZr42IZPJO5ieQndRbDqvcyMKQljXL2bVW4gWCm2nvZWnaVttqVzXkexXV_kk68Hb0i1YIK3XQZev5YcYvQBiZHdrXw6acvvp2iFI1t9Gsyb-j4BsPRPzshUfZ1HguF_KumdUBz1RA25Kw92_dep5AfLC91gWAVS3-oTsMwsNpXdqjIy4wGMoRGdLmvYC2eo3emr-yYhVTcoNhN_NBd9xv4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=mNlUuy6NJkr3vTbXI6C5SV6-AdjsmSuee2RcGQdScLU8DHb5i77tWgINJwOpr822C4feo4ZOdfVFtIB7PpYdurcp6PGkx-sYlUYgc8FRrkiLGPWYqXDuQAxA0ZT5nBLhGJuAMkofn11YCl0faAk7I6u_IRnWyft0dh3k1ZTLsSuzI7X9Exo5CVh5lnhq-TdJ4LKMqln-zS3WOD5UqYUvg3Iqd_m_YUd4fStkMjsY-3zCIat59k45KkEwxvpeOqtuCTgrRqMLXZkCfmpGLQq1zNj9PPUllEj-UoIHgrVwIrnO8Lbpm0CAJK8ooQZGf7DdTBewN027YRHhUiLrD3r-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=mNlUuy6NJkr3vTbXI6C5SV6-AdjsmSuee2RcGQdScLU8DHb5i77tWgINJwOpr822C4feo4ZOdfVFtIB7PpYdurcp6PGkx-sYlUYgc8FRrkiLGPWYqXDuQAxA0ZT5nBLhGJuAMkofn11YCl0faAk7I6u_IRnWyft0dh3k1ZTLsSuzI7X9Exo5CVh5lnhq-TdJ4LKMqln-zS3WOD5UqYUvg3Iqd_m_YUd4fStkMjsY-3zCIat59k45KkEwxvpeOqtuCTgrRqMLXZkCfmpGLQq1zNj9PPUllEj-UoIHgrVwIrnO8Lbpm0CAJK8ooQZGf7DdTBewN027YRHhUiLrD3r-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV7JKKl_O_I0KAkfHsgV70YkszpkuZXdhELZnOdSXv5lRyMpBcOQp1xmim3EwbY3jciV0CP5dm1EUtV-pxwJiiS6VvyGYh_g_DAEqLOE4NcLVvpnvYdDOBC3UCj9RKfFxoRq6yH3_-8nf_H9G50ARuo9r06SdhBmI8YdpYqZnd8to__xgc2kOmvV3cRgLox5mV_iiiKiSCT53zOLBVyZx2lmiMPRMN1-GZ5SdQWqD2GsxycrQJ-y09-HZGtR_kHyH_mB7awfMhkvHlT9gFhvdH2XJqXzgl0Co9rIDuNOimRFIZFWUjfTtzW7CTtiADCVhzxSNHpDV-PIX6RnesB13TVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV7JKKl_O_I0KAkfHsgV70YkszpkuZXdhELZnOdSXv5lRyMpBcOQp1xmim3EwbY3jciV0CP5dm1EUtV-pxwJiiS6VvyGYh_g_DAEqLOE4NcLVvpnvYdDOBC3UCj9RKfFxoRq6yH3_-8nf_H9G50ARuo9r06SdhBmI8YdpYqZnd8to__xgc2kOmvV3cRgLox5mV_iiiKiSCT53zOLBVyZx2lmiMPRMN1-GZ5SdQWqD2GsxycrQJ-y09-HZGtR_kHyH_mB7awfMhkvHlT9gFhvdH2XJqXzgl0Co9rIDuNOimRFIZFWUjfTtzW7CTtiADCVhzxSNHpDV-PIX6RnesB13TVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=i9czGnkzbwKDTXcbTfn3JOJ8eD0GD1Mlum-Y5JFs1SEbPlKSgWEtKvcZjXray_Xu7dYAtchDN_czmtF-UHbo5n-SogN2G94I9niQ9Uc9YVMot-JAQVzOvvGsAFNGsoN5qEaP6TTSsoF5kMlaSgZzTtOXaie3klYNhI8mqEoQtmYhugr8DJxhDx16UYEO4DqhObLEViBiR8xyVGyEXzZ9zLqy72NeisrqnjM1hIIbkqp0eDMDVYZJHB1iDXEPWLL0QZLVTbkD1uDA_U50IAO0enAbrzmQip5wiBHF2XftcFR1uM2ZXYmZ8tSU-gIIDVpjsopO0WfXY8LMtZebQRGRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=i9czGnkzbwKDTXcbTfn3JOJ8eD0GD1Mlum-Y5JFs1SEbPlKSgWEtKvcZjXray_Xu7dYAtchDN_czmtF-UHbo5n-SogN2G94I9niQ9Uc9YVMot-JAQVzOvvGsAFNGsoN5qEaP6TTSsoF5kMlaSgZzTtOXaie3klYNhI8mqEoQtmYhugr8DJxhDx16UYEO4DqhObLEViBiR8xyVGyEXzZ9zLqy72NeisrqnjM1hIIbkqp0eDMDVYZJHB1iDXEPWLL0QZLVTbkD1uDA_U50IAO0enAbrzmQip5wiBHF2XftcFR1uM2ZXYmZ8tSU-gIIDVpjsopO0WfXY8LMtZebQRGRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
پزشکیان:
خیر اصلا اینگونه نبود.آنها تروریست هایی بودند که توسط آمریکا و موساد و کرد‌ها مسلح شده بودند.ما به مردم عادی آسیبی نزدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=b2jU2aYnZGddKFn--TsqUft3uqkPf6yTLgZssUCJHaGIxJvoxS8lpYvpsO5j2yerBzgvmVnPIVUNxKA0D3YTxuSzi9BF8rej9lrzRY3LdfCpZHf0etDOemU5nfGfraTw95RCAz9DtzdFBmh2mUC_w4UTWDRJ62CH06lYLeh2AtYExefKustBkk66K84oAgB5UwabZ5vljb0vb5gIhxCCXnlAOqe50lukuxMoHN4qrPa2Bbs8-tVlAOjvCtwkhzTA0mG1fBv9MSAUZ4V6lxtZZytfNkoGwbyGu20vd89aqHe1r8rYish5p7N-z5BAwykLLrkXcYK0cn8JgrjrMvBQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=b2jU2aYnZGddKFn--TsqUft3uqkPf6yTLgZssUCJHaGIxJvoxS8lpYvpsO5j2yerBzgvmVnPIVUNxKA0D3YTxuSzi9BF8rej9lrzRY3LdfCpZHf0etDOemU5nfGfraTw95RCAz9DtzdFBmh2mUC_w4UTWDRJ62CH06lYLeh2AtYExefKustBkk66K84oAgB5UwabZ5vljb0vb5gIhxCCXnlAOqe50lukuxMoHN4qrPa2Bbs8-tVlAOjvCtwkhzTA0mG1fBv9MSAUZ4V6lxtZZytfNkoGwbyGu20vd89aqHe1r8rYish5p7N-z5BAwykLLrkXcYK0cn8JgrjrMvBQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=ak-7Tb3r_L0kwHluK7EEUptNJs1s0srlhA5At7VT9NkudxzR2xX8q9JTt0VpYXndPH0l-kN1L_Q18qbCinR4I4b0XQYPBtEFn2s-gDXGYDLUCWl8uQE_z4YxTzm-0oNoz2ed0kbqnHBDV2jjhI2sGyssUw4xIRhsyzrnhzsurrU-FzQitlr39fqq-4KfmtYXZpEENaG5ik2lQ8r6LXgWrUOtf0E7TjhDcB0sEHiuyn6rspP3xoOq8All9UbcB-6hRJfrKSbPXiWE9e2Nfdgp8wtgcrN65jU4EmnKq2GOhZguZFDbC2UkEDoqG8yN2vjfBjT_rd5UzI3TKTKBXU9O6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=ak-7Tb3r_L0kwHluK7EEUptNJs1s0srlhA5At7VT9NkudxzR2xX8q9JTt0VpYXndPH0l-kN1L_Q18qbCinR4I4b0XQYPBtEFn2s-gDXGYDLUCWl8uQE_z4YxTzm-0oNoz2ed0kbqnHBDV2jjhI2sGyssUw4xIRhsyzrnhzsurrU-FzQitlr39fqq-4KfmtYXZpEENaG5ik2lQ8r6LXgWrUOtf0E7TjhDcB0sEHiuyn6rspP3xoOq8All9UbcB-6hRJfrKSbPXiWE9e2Nfdgp8wtgcrN65jU4EmnKq2GOhZguZFDbC2UkEDoqG8yN2vjfBjT_rd5UzI3TKTKBXU9O6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=B-qRo4VL9l7CLzgIgCs4ezIgrz5moi4Zw-Fbr4Od6yc7iDuqHqVHRahzoHjFWQrJ3UXPu35XkV8vj44hsgcJ2ZspWkRACYGB7usu3vKMJ9b76aGzjesjgIuvvyDPZH98-OwqJ8bNSs1mpgmLIRW337X5WNnoC08ogx1MMkT1LkW2Qr5e3GVRHINjmEklM8B6Y-VWL9IS_XfKnBB9bxfAHa_yZY0S4Sq45vc4Qj4ub65r2j4UsZsEinIf0J0NT39xrZJryg2vifUSR34N7JT1z02OUl6Fh0N69LFjTcC3W-P53pU054wTRNFUDxEgCAbJpl_v9qq6zbqvPqADyQ6pUVdyoWXD4SihOlEUSFyle8JQOBB_XmqToo7LTGWqdmiZaA7Ylj7x26LCs-LvOUTabgE8edm9CF3ZtPw1ldwCBszJ5wWE5AXVkC14SwAvs-rinAcm6Kc0Nxr5drl9EOAYRxiBv5j16wnbSvkMi-w_w8VNU4yj-hibJf_ZHcVpWara0tAUdCQ6-EglopIxP7kDxrETLaGU58zogmbFHVK4jlM0Clg4cUonjzaDqjCMFJSUQLompSpH7QV1W2TkLjBeqrIQLw-FrSEUG6QVE1S2mA-Fev3xmd--kRxHPc4xaShPLAZK0GG_jHrlHoXss0j1C6TdjvQcHJ4y47-iFo5rxdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=B-qRo4VL9l7CLzgIgCs4ezIgrz5moi4Zw-Fbr4Od6yc7iDuqHqVHRahzoHjFWQrJ3UXPu35XkV8vj44hsgcJ2ZspWkRACYGB7usu3vKMJ9b76aGzjesjgIuvvyDPZH98-OwqJ8bNSs1mpgmLIRW337X5WNnoC08ogx1MMkT1LkW2Qr5e3GVRHINjmEklM8B6Y-VWL9IS_XfKnBB9bxfAHa_yZY0S4Sq45vc4Qj4ub65r2j4UsZsEinIf0J0NT39xrZJryg2vifUSR34N7JT1z02OUl6Fh0N69LFjTcC3W-P53pU054wTRNFUDxEgCAbJpl_v9qq6zbqvPqADyQ6pUVdyoWXD4SihOlEUSFyle8JQOBB_XmqToo7LTGWqdmiZaA7Ylj7x26LCs-LvOUTabgE8edm9CF3ZtPw1ldwCBszJ5wWE5AXVkC14SwAvs-rinAcm6Kc0Nxr5drl9EOAYRxiBv5j16wnbSvkMi-w_w8VNU4yj-hibJf_ZHcVpWara0tAUdCQ6-EglopIxP7kDxrETLaGU58zogmbFHVK4jlM0Clg4cUonjzaDqjCMFJSUQLompSpH7QV1W2TkLjBeqrIQLw-FrSEUG6QVE1S2mA-Fev3xmd--kRxHPc4xaShPLAZK0GG_jHrlHoXss0j1C6TdjvQcHJ4y47-iFo5rxdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=USUxpsSksxxiv4xsCXFMP5L5LKbmUoDDjbaYJkW_6PU-9hJWGBosgs5xALaFTCY95kM5kPuQPGI1DyOcdt5EBP0k6d_yL1MTg61Cg-ptjsXn_ZmRgDaXrot8CkbmvJ4-9EAEAnkAeBO1inkUanWO34c-Wq87RxOLqJPNnx5QVgJdWmJ2-bdZagJbJPSiTmyBYVQ5n_gTLWbfYPKFokclpwiGJ--mnKrkkqKurzogMUI_cCw8ZyYLkbtc-4arT2RKhSnBi4VipzKDb7cwzgG4KbtulVyxXFXHwhJ_V5JhRh6-AveRSxNYFzr86-XF2K5pvGkxB2AsPHzz2pignj6nZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=USUxpsSksxxiv4xsCXFMP5L5LKbmUoDDjbaYJkW_6PU-9hJWGBosgs5xALaFTCY95kM5kPuQPGI1DyOcdt5EBP0k6d_yL1MTg61Cg-ptjsXn_ZmRgDaXrot8CkbmvJ4-9EAEAnkAeBO1inkUanWO34c-Wq87RxOLqJPNnx5QVgJdWmJ2-bdZagJbJPSiTmyBYVQ5n_gTLWbfYPKFokclpwiGJ--mnKrkkqKurzogMUI_cCw8ZyYLkbtc-4arT2RKhSnBi4VipzKDb7cwzgG4KbtulVyxXFXHwhJ_V5JhRh6-AveRSxNYFzr86-XF2K5pvGkxB2AsPHzz2pignj6nZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=PkfR5e360RfnV46A8KDkNYUvSIZGKl50tBgFw2yZFUP2D6TrNm06j_H_HD1vYfDIHEDm1xvrOrdKJxm8sN3onD-N884FRpjjabS7Ie9AkiXmvp85jGbxQ3GMPFXaCVvWGkThS2cMh_gtkheOR8Pjh_VmfMkZKTIFSi8n1Ml3VPgmQrHxzt5iRg0oSCM3dNAyj0umavNhB868ThI-rGqpcUBhd7kKgAymg_fBU-bozbopNuZRaV1Uh4KvI0F9DPFNQHnTvk2KCeHa-f38wuchhWIDTt6jWtZPoqcHuAFnWfmUby_OQMlwS0t1eZx8hqH3reQ9zE9eHWTRwdG2SNGPqDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=PkfR5e360RfnV46A8KDkNYUvSIZGKl50tBgFw2yZFUP2D6TrNm06j_H_HD1vYfDIHEDm1xvrOrdKJxm8sN3onD-N884FRpjjabS7Ie9AkiXmvp85jGbxQ3GMPFXaCVvWGkThS2cMh_gtkheOR8Pjh_VmfMkZKTIFSi8n1Ml3VPgmQrHxzt5iRg0oSCM3dNAyj0umavNhB868ThI-rGqpcUBhd7kKgAymg_fBU-bozbopNuZRaV1Uh4KvI0F9DPFNQHnTvk2KCeHa-f38wuchhWIDTt6jWtZPoqcHuAFnWfmUby_OQMlwS0t1eZx8hqH3reQ9zE9eHWTRwdG2SNGPqDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=kVRTP0wRQ80Ze8ijZLEzofXjSUPCIFfQe7JfNVr9NAaSBb27QRuAKk4SMDD68rCtI0qFKUf5j5H6wIAKSm2cIDIiEkmV7alHvvhT9-6PxDAVdSpdOScERl14hL1cOJSTGbnvutV6hAlYwkmOfxQJ5MbvgB8RsITiW-9SXXJ_C8V5OUqiLQRlhhbDsT0oougBbPS7ZhdMr1pilsFnR4aJuCLc60MUsZ386t26h7LASxdoY7HpoygqbFPR5GpGqC0UCUa9rQt_avkaIwtZGzuAxUw0DFd4TV-NFVcaWjDbtJTjwa45w0M9mFIPtVDF4MU994SPFWcselZGnSDvFzdr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=kVRTP0wRQ80Ze8ijZLEzofXjSUPCIFfQe7JfNVr9NAaSBb27QRuAKk4SMDD68rCtI0qFKUf5j5H6wIAKSm2cIDIiEkmV7alHvvhT9-6PxDAVdSpdOScERl14hL1cOJSTGbnvutV6hAlYwkmOfxQJ5MbvgB8RsITiW-9SXXJ_C8V5OUqiLQRlhhbDsT0oougBbPS7ZhdMr1pilsFnR4aJuCLc60MUsZ386t26h7LASxdoY7HpoygqbFPR5GpGqC0UCUa9rQt_avkaIwtZGzuAxUw0DFd4TV-NFVcaWjDbtJTjwa45w0M9mFIPtVDF4MU994SPFWcselZGnSDvFzdr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=kAu0vf-bSwLpLZ5014gqenK7kxZGUDlJZtbEUtmmOtbhjTXZBn6GXAqHYHK1Um0-KvWcwepB5-H8M9OL__Jb61bjnep6cIHYln1B4j488UrX2oo7uAxBKPp1JDPsCo95i2p1fIFQ_sBXhNW-tBSp34VUiIBTc8HwqZn960ZUV44lYahp6J0Ygajngwet3crsBY3ku7ECEhqa-1ppb3sl6LvKoNPk0Cm5vXbdqQgQfvJdz7Yp9S-akIaDQOel0KFY03D5rQ0sa5wK7pHcjR-4egKUsQuhocVbwa13-wLUeWE2R7lXeFfw-gWxY-4fOnXqCnFo45vo1nnRblRteBLgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=kAu0vf-bSwLpLZ5014gqenK7kxZGUDlJZtbEUtmmOtbhjTXZBn6GXAqHYHK1Um0-KvWcwepB5-H8M9OL__Jb61bjnep6cIHYln1B4j488UrX2oo7uAxBKPp1JDPsCo95i2p1fIFQ_sBXhNW-tBSp34VUiIBTc8HwqZn960ZUV44lYahp6J0Ygajngwet3crsBY3ku7ECEhqa-1ppb3sl6LvKoNPk0Cm5vXbdqQgQfvJdz7Yp9S-akIaDQOel0KFY03D5rQ0sa5wK7pHcjR-4egKUsQuhocVbwa13-wLUeWE2R7lXeFfw-gWxY-4fOnXqCnFo45vo1nnRblRteBLgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK1DRZd_fiitezxZRJ3_lsdKtefe7MzFWcYJtjQ_0x73-BIeAsRb58VaJUhSbJ1ZIx7vijFD-_o3tBbC8j5DVhqfX2c1VrlTFCNMJpGhiG9cwWIk3dGI45lh6F2ekTfZSiDtn2d4BCr7bIUU0QF9if3if2wl8iOAG6wO8wLKZF6ckPpv0DhTWIXSH22KN2RhL3s6Xnxc_6Ctc7LqR0EjND1ym6frUjf6by3cNBqVsi4_F8hYz5wFgcLa-jnI_OpqMHyPMaFQ-4eN9cUdW6FsnFzPdqtvU8Tf28J65OHJ1O0vPkVpJpBYI7tkW9Oj6iHjMlm34Vx3Ehq0BiParBXcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25201994ac.mp4?token=lFXBeo4r1GIVY15ds-PBflniEwrMPj8Eap1FV-Fln-BfxywenVsGnBciJQz117qs5zKpeU9v39aPJlH9WY7iPj36oe1GuvRRHHMt5HwNOBTA4y5wo1Flgu81ciIm4O8qtaHHHAhlC9xaEQKeqE74nNoUkFhow8pBcGTgBAx9gdDVTgHLB--sTarXK7OMzulZBnpH4wOreDcFUvI-xeVTRjWy9L94Rwh2FSvXjYWbEGVfoPp3EEdo42unZhyMK93HBYh8zsret3hr7WOr2JKa2Rn9ZHpnUzrjUhLfUQlB2Bal8sZbOfOSd9izVnVQH2yCqgMtWnFeWYMskfKmksRb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25201994ac.mp4?token=lFXBeo4r1GIVY15ds-PBflniEwrMPj8Eap1FV-Fln-BfxywenVsGnBciJQz117qs5zKpeU9v39aPJlH9WY7iPj36oe1GuvRRHHMt5HwNOBTA4y5wo1Flgu81ciIm4O8qtaHHHAhlC9xaEQKeqE74nNoUkFhow8pBcGTgBAx9gdDVTgHLB--sTarXK7OMzulZBnpH4wOreDcFUvI-xeVTRjWy9L94Rwh2FSvXjYWbEGVfoPp3EEdo42unZhyMK93HBYh8zsret3hr7WOr2JKa2Rn9ZHpnUzrjUhLfUQlB2Bal8sZbOfOSd9izVnVQH2yCqgMtWnFeWYMskfKmksRb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
🇮🇷
🇮🇱
🌟
نماینده اسرائیل در سازمان ملل دستگاه «استارلینک» را به نماینده اعزامی تهران داد و درباره «کمک به مردم ایران برای سرنوشت و آزادی با این دستگاه» صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72234" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=DyQAx2lwxnh7ZvdA_DFsVytbLMJUjIH6MxsfdwStTXdEbMuWVpXYZxiH4oHSh1r_WGGlhKy9pUsUEDB7Z7QaOtoBUXNi82oTmd4sB4PL4wPtY6K5H9k6yQAi_91qxED0hKKsi0trMtmlCj0UpQq9Vfp_UhBiiqUtceD0b1vxubiOw9Pdg39JHa-wo57dRTIfOGecZ6F6CuZzBEeyVtGugQ16q8S_nI5qBuNQ7cfEEUGacqgpYFp5A0dzDfTvALAkpB6oiyZH4S2wYvgy8XP37rKhGe_6t4XRRRhKCTcHArbyKsOAm5KBuOf8KlWAA7Vlj9OqjZ7OFXbgfMRHzPIL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=DyQAx2lwxnh7ZvdA_DFsVytbLMJUjIH6MxsfdwStTXdEbMuWVpXYZxiH4oHSh1r_WGGlhKy9pUsUEDB7Z7QaOtoBUXNi82oTmd4sB4PL4wPtY6K5H9k6yQAi_91qxED0hKKsi0trMtmlCj0UpQq9Vfp_UhBiiqUtceD0b1vxubiOw9Pdg39JHa-wo57dRTIfOGecZ6F6CuZzBEeyVtGugQ16q8S_nI5qBuNQ7cfEEUGacqgpYFp5A0dzDfTvALAkpB6oiyZH4S2wYvgy8XP37rKhGe_6t4XRRRhKCTcHArbyKsOAm5KBuOf8KlWAA7Vlj9OqjZ7OFXbgfMRHzPIL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستربین ۷۱ ساله شد و جشن تولدشو با صدای بانو هایده جشن گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72233" target="_blank">📅 00:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72230">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=V-EfkGZOU_sZgwW05EAFp3SiJkHHN3J6j1nm7p-GhIgINmgOQ19x67b2S_nKPR-tr13TrH-9Z3gIpkBmpdFPK7q0YRPFuCKi3TqXJXyikhZGRAYa_9apBCL8MC60VL51Uj3r5rWR-KlhD7HjTqaUuc-AOOhW1hwK_tBslQrtii4rxNoScQmw4iHvr1VuAeE4h_RAAQ6Retp0B9LsGIAC0F7yEb-AkYiMX4pS9F_RaNYUkGNpVI8syzkddCgdtW1fMbTwpMb65iAhvjaBXCP0EKxy-USxd2gvLDTcWf2Os4a5WpakbiDZRFaB8ren8GN5uS5zP8g87hBxoh5bVlkzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=V-EfkGZOU_sZgwW05EAFp3SiJkHHN3J6j1nm7p-GhIgINmgOQ19x67b2S_nKPR-tr13TrH-9Z3gIpkBmpdFPK7q0YRPFuCKi3TqXJXyikhZGRAYa_9apBCL8MC60VL51Uj3r5rWR-KlhD7HjTqaUuc-AOOhW1hwK_tBslQrtii4rxNoScQmw4iHvr1VuAeE4h_RAAQ6Retp0B9LsGIAC0F7yEb-AkYiMX4pS9F_RaNYUkGNpVI8syzkddCgdtW1fMbTwpMb65iAhvjaBXCP0EKxy-USxd2gvLDTcWf2Os4a5WpakbiDZRFaB8ren8GN5uS5zP8g87hBxoh5bVlkzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب رئیس جمهور چین  به اقدام ترامپ برای جاگزین کردن عکس بایدن با «خودکار»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72230" target="_blank">📅 00:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=epsdd9LymrZ3WL4sOdQlopqd7nBCWXtJEFH0E3BlooIKozVr5wSIHlJvF8e8h1W4iisS0XxeUzLC9mGhRf0Aai6ZUW2ky9Rm1Q6Oq7Y_xPaS21I8gkgqcL-ylNSX-aEdQURHEA4e7GhjGz_avJ85HNPr_S9xdS6qBYJyOIdqdKFgnNdWA30I6f2do89e1J3oZpwwteOP3ZJTUILMgEq_0cQ5Vv1-BVK-FdtfUKZ6uzitzNtIC-4TWIhZUKdbK-9S-32IlnE9A-aPs-ivEl9fTEu2SaY2F8SAQFb5EprMau_W5qW30N3SvAk9y-ypw74ou3VixVdIao7rUHGf7rvBgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=epsdd9LymrZ3WL4sOdQlopqd7nBCWXtJEFH0E3BlooIKozVr5wSIHlJvF8e8h1W4iisS0XxeUzLC9mGhRf0Aai6ZUW2ky9Rm1Q6Oq7Y_xPaS21I8gkgqcL-ylNSX-aEdQURHEA4e7GhjGz_avJ85HNPr_S9xdS6qBYJyOIdqdKFgnNdWA30I6f2do89e1J3oZpwwteOP3ZJTUILMgEq_0cQ5Vv1-BVK-FdtfUKZ6uzitzNtIC-4TWIhZUKdbK-9S-32IlnE9A-aPs-ivEl9fTEu2SaY2F8SAQFb5EprMau_W5qW30N3SvAk9y-ypw74ou3VixVdIao7rUHGf7rvBgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=tDADA1ruAQ9cpCZSw_5Tfdt0DAFrsBPbImmpEJ1f8tGYl8Ens4neeDUr8ub4GNBNlwJwaNlTTej1mGdDUSx_L6KcnngZaRn73JvJMrM2MQigFnTJspC22M19mvG1yHgdpbzUoPCb6dkIW-AQOqk788Lzal9xiftgDaJL8JUN6x1v30r2Z4Mc65BobKmrv9YPDbgMJ5F30WejwPSh7tUtE7HC-xJYr_RNJSunQjpm343AYNdtfw8D_1gtJNRskp0HFB7NFsChq4q592QNM_nOhIE9bUogYEieT7bZUGkmcZxx6efoMcfu6qGJ6PE6-xOBFlBlYQ8cBMsfz0uFbkTdMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=tDADA1ruAQ9cpCZSw_5Tfdt0DAFrsBPbImmpEJ1f8tGYl8Ens4neeDUr8ub4GNBNlwJwaNlTTej1mGdDUSx_L6KcnngZaRn73JvJMrM2MQigFnTJspC22M19mvG1yHgdpbzUoPCb6dkIW-AQOqk788Lzal9xiftgDaJL8JUN6x1v30r2Z4Mc65BobKmrv9YPDbgMJ5F30WejwPSh7tUtE7HC-xJYr_RNJSunQjpm343AYNdtfw8D_1gtJNRskp0HFB7NFsChq4q592QNM_nOhIE9bUogYEieT7bZUGkmcZxx6efoMcfu6qGJ6PE6-xOBFlBlYQ8cBMsfz0uFbkTdMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72211">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: کیرم تو ترکیه
#hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72211" target="_blank">📅 21:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72210">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو: کیرم تو قطر
#hjAly‌</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72210" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72209">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=ZMGoOpPk9aUhD-5iXex5Ip7NwjpjMbuk3dSK7v4hdgqsSAVRQAHjSuU-xXGW7x-kbrtz9CF87fJHM44Uo7IIK5KBjAJfNQq7qhR8f_1Qf3nxvnU0OGjewx7mHatKjdRdCtFxbpV4vebgnRraydTy5ow4_CI5qJevDu4TPGx8JnTqVzD1Pvrf3q28X8VnQE9V73jvE8RHenND44Ut-BG5kNrcyRGw2oKDAcxOfALzb1bEn4jObi-3cOVM1LqPYtnXV2Kj9mPdi-UYPZtLnibyejrZ9h0v256ZrYnbc57mzDSrfehQJpLhnSmQagZn9DnMwrt2KbyckF5Ct0Zsb4zIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=ZMGoOpPk9aUhD-5iXex5Ip7NwjpjMbuk3dSK7v4hdgqsSAVRQAHjSuU-xXGW7x-kbrtz9CF87fJHM44Uo7IIK5KBjAJfNQq7qhR8f_1Qf3nxvnU0OGjewx7mHatKjdRdCtFxbpV4vebgnRraydTy5ow4_CI5qJevDu4TPGx8JnTqVzD1Pvrf3q28X8VnQE9V73jvE8RHenND44Ut-BG5kNrcyRGw2oKDAcxOfALzb1bEn4jObi-3cOVM1LqPYtnXV2Kj9mPdi-UYPZtLnibyejrZ9h0v256ZrYnbc57mzDSrfehQJpLhnSmQagZn9DnMwrt2KbyckF5Ct0Zsb4zIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
با دوستان آمریکایی خوبمان، ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را در هم کوبیدیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72209" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72208">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJmwEeODb5fqq9ZvXi40MDfOKmcBnVKdH1s8U_44k3uD70bmY2H9EpJmH3hG7SBvNJrV7gx2akI8ZTkBoF_fHSYpI-kBTmxpJ87qRWqid_4DJPf0P4ky1yLtBwAbgEXtUNYgmmGkguJATtTaIv75vURRzuGEIj22aabTfBoi1dVi6cJeMMWkfsxwBHcFNAo-6xeKWth76xbGPghNtAiwXwdltIWyqA__M5MxINlHk-yoJQ3lF-3vUKcE5kWdlEktIFzVNhzXC_GbzMAV9IAoSrnw9pW9NFgGQei_OLbYyLvrPWjF603sXdWTDEmiZ8qihWJ6FCb4-AodC8mBl43tn3B4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJmwEeODb5fqq9ZvXi40MDfOKmcBnVKdH1s8U_44k3uD70bmY2H9EpJmH3hG7SBvNJrV7gx2akI8ZTkBoF_fHSYpI-kBTmxpJ87qRWqid_4DJPf0P4ky1yLtBwAbgEXtUNYgmmGkguJATtTaIv75vURRzuGEIj22aabTfBoi1dVi6cJeMMWkfsxwBHcFNAo-6xeKWth76xbGPghNtAiwXwdltIWyqA__M5MxINlHk-yoJQ3lF-3vUKcE5kWdlEktIFzVNhzXC_GbzMAV9IAoSrnw9pW9NFgGQei_OLbYyLvrPWjF603sXdWTDEmiZ8qihWJ6FCb4-AodC8mBl43tn3B4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
آنها به زنان باردار تیراندازی می‌کنند و خانواده‌های کامل را هدف قرار می‌دهند. البته هیچ‌کدام از این موارد در رسانه‌های بین‌المللی یا شبکه‌های اجتماعی پوشش داده نمی‌شود؛ هیچ‌کدام!
آنچه پوشش داده می‌شود، گروهی حدود ۱۵۰ جوان کم‌سن‌وسال بزهکار هستند که می‌روند و سنگ پرتاب می‌کنند و درختان زیتون را قطع می‌کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72208" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72207">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: هدف فقط پیروزیه، همونطور که داداشم یونی گفت، ما مجبوریم پیروز بشیم
#hjAly‌</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72207" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو: دم ترامپ گرم داداشیمه
#hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72205" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو: خامنه‌ای دیگه مرده
🔥
🔥
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72204" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: این پیجر های تو دستم رو می‌بینید؟ حزب‌اللهیا که خوب یادشونه، با همینا دهنشونو گاییدم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72203" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: خدایی کیو دیدین مث ما که تو هفت جبهه همزمان بجنگه؟
#hjAly‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72202" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو: مث شیر می‌جنگیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72201" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: سال‌ها پیش داداشم یونی تو جنگ با اعراب بهم گفت ما پیروز می‌شیم، الان من همینو می‌گم، ما پیروز می‌شیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72200" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو: اسرائیل کوچولوعه، انگلیسی های جاکش که خودشون استعمار رو اختراع کردن به ما می‌گن استعمارگر، کیرم دهنتون
#hjAly‌</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72198" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72196">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو: ما به کشورای زیادی کمک کردیم، یسری از همین جاکشایی که الان رفتن بیرون هم از ما تشکر کردن، کیر تو هرچی ریاکاره
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72196" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72195">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: نابود کردن تاسیسات هسته‌ای جمهوری اسلامی سخت بود ولی انجامش دادم، اگه این کارو نکرده بودیم همه مرده بودیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72195" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72194">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: نمی‌زارم آخوندای قاتل به سلاح هسته‌ای برسن
#hjAly‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72194" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو: کیرم تو جمهوری اسلامی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72193" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72192">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72192" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!  این سخنرانی تا دقایقی دیگه آغاز می‌شه #hjAly‌</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72190" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss8-KoW-p8TSpdlJu00k0trBvjsiN1tMvEFV_0QqANcYiqzsdRiv8vfJwVKwTgsCaaciQZAodNDZw_M-CKRTK2ROlNY-TSLhXDxkfMLfIbdiStsGNURPBRPA6SKSAIGGRtpq7iZ5p6vU3qRgSO39aMwhl_U2lD0AuguX45mV4zLcrqy0HbZeVALTGMXIdm27Uq-w_xN79GePEvGXOQvxVqQx6Yc3lv-ii3Wr4FGslnlvJ5h2mLLSzvQDIUAjB2xRoxQfwt8tTQ3mWgon8XkDp5eMkIeybEBCabYjf9s8bXCUjww-i9knxkcO9k46RaPZwJdvPDvblgVyWwu3qKPRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان درحال مصاحبه با فاکس‌نیوز آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72189" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=nPNx5N5U5hvxcRjNcG3amaLyAiXWNyUuJDsPW9R1zCQNCXFv5P6ePolFBvfJP_yKxruRwUFRJwo3RdCSVzntdZPU0soSdGAbYlp7ZbqDxyiC9Jj8t3QDq88gFLfaR-nm-TA9dT0GA7xtzzg_HUkSnY9B0Fc7wMEovTaGXFNT8YO3rTQby6JZdGP2x50dN-bZ13LmlbxtY29YLyDymhL-XFxgR8SY1O-Z6grlJNfZgZxAYX7q_Dj7e2kMYa7vCvEIkPA1SNGOIsGuBCuu1gj6MB3HjtjHyvMo925GjBWC9DtU7TIrDU82xWMRGuqn2-NKtVKUZVfuqMhoz0r-T33OFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=nPNx5N5U5hvxcRjNcG3amaLyAiXWNyUuJDsPW9R1zCQNCXFv5P6ePolFBvfJP_yKxruRwUFRJwo3RdCSVzntdZPU0soSdGAbYlp7ZbqDxyiC9Jj8t3QDq88gFLfaR-nm-TA9dT0GA7xtzzg_HUkSnY9B0Fc7wMEovTaGXFNT8YO3rTQby6JZdGP2x50dN-bZ13LmlbxtY29YLyDymhL-XFxgR8SY1O-Z6grlJNfZgZxAYX7q_Dj7e2kMYa7vCvEIkPA1SNGOIsGuBCuu1gj6MB3HjtjHyvMo925GjBWC9DtU7TIrDU82xWMRGuqn2-NKtVKUZVfuqMhoz0r-T33OFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوزوی‌ها به روش خودشان برای بهبود چهره روحانیت در اقشار میانی جامعه کارزار به روز شدن راه انداخته‌اند؛ آنهم با «جوانگرایی»!
یک آخوند مبلغ، طلبه جوانی به نام «رضایی» را به شهربازی مشهد برده و از هر فرصتی برای مالش و ملعبه با او استفاده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72188" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=iNAdrK2rIaGpeAV6yye4sqW2ttXO01eOITE8Iw0eiHubFvdKpqBfDYVhzRXFXQ_H8lTGQnqvNrTXGCS_gRcC7zMeIDO8uVBjkA7NzxEgJ5Mm-pQuCSag9ZY_2MKL5ghdZ7oQZWOLF-1CPRnTqWGVWI-98C5rl3YDOeK00Gwq7gQvHRJId232uJvcaOXUjdWtP_PeIp3r_z1rD-jvqFJxWxxGi_ubNgQkbwKMSaXfpoERry_4V_Nfwzw2i5Qh8EDynEna0Kzdm-wqHAFi0OFWOs9cKoCWucjDsjORdpMoXfyhmQ0TncbOYN26aEr1MKxbpcBpdgqsssEYVhWEA9NUlTCTMVDY9tr7FUuqjqRxfTC6pKCqzqe4ddSiTWZq4LRurrotr6TOZ_X12rFF37SQL7URhRJeN2TiQsNr_MLk7ZnY9yQ5SCuKbF9zPu4KQ2HlxuCJOpfbYhrQiAPMrBdcEyvL9d56SEgeuRhO-LQmzaOxCO8nP1sbBGVv6DJjIT8mUFRrYqX4XPnQRPNnChOpsaAtCtsUuW97l3tTFrqP3YhQXPldcfZsjfYcfeVgcYNOH9wh3lDCIP7vhgW5DC9KcyuVUVUYusMmmfwP7PL9DGYrnB-g_VgkPBUqKRz4ecWTlJdqN_FRpdBJUt2VUKF6JnDjgkwTQjJz6gD0Xbe_TV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=iNAdrK2rIaGpeAV6yye4sqW2ttXO01eOITE8Iw0eiHubFvdKpqBfDYVhzRXFXQ_H8lTGQnqvNrTXGCS_gRcC7zMeIDO8uVBjkA7NzxEgJ5Mm-pQuCSag9ZY_2MKL5ghdZ7oQZWOLF-1CPRnTqWGVWI-98C5rl3YDOeK00Gwq7gQvHRJId232uJvcaOXUjdWtP_PeIp3r_z1rD-jvqFJxWxxGi_ubNgQkbwKMSaXfpoERry_4V_Nfwzw2i5Qh8EDynEna0Kzdm-wqHAFi0OFWOs9cKoCWucjDsjORdpMoXfyhmQ0TncbOYN26aEr1MKxbpcBpdgqsssEYVhWEA9NUlTCTMVDY9tr7FUuqjqRxfTC6pKCqzqe4ddSiTWZq4LRurrotr6TOZ_X12rFF37SQL7URhRJeN2TiQsNr_MLk7ZnY9yQ5SCuKbF9zPu4KQ2HlxuCJOpfbYhrQiAPMrBdcEyvL9d56SEgeuRhO-LQmzaOxCO8nP1sbBGVv6DJjIT8mUFRrYqX4XPnQRPNnChOpsaAtCtsUuW97l3tTFrqP3YhQXPldcfZsjfYcfeVgcYNOH9wh3lDCIP7vhgW5DC9KcyuVUVUYusMmmfwP7PL9DGYrnB-g_VgkPBUqKRz4ecWTlJdqN_FRpdBJUt2VUKF6JnDjgkwTQjJz6gD0Xbe_TV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇱
🇮🇱
شماری از نیویورکی‌ها در اعتراض به حضور بنیامین نتانیاهو در این شهر تظاهرات کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72187" target="_blank">📅 21:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!
این سخنرانی تا دقایقی دیگه آغاز می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72186" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=kFa_j9xtZhWqaYFVP1QOvC14Ho_SzGkjJZY-EWYvEMjjEU_5_1i7la2ANLpBWHu1pxoBzEe4sX2jfaNCURhDyTaP1_493_yDFTFCJNG2BuWKjsEDaz4ocxyBdS0kkOeeLh2go1U9ZBdmiMTbbFc4lHtfjMILueRVkFWfGJSscXIBppkIiEfL4B0Ysm6QwcY255Gsi4v1f1VusdyQJrEatRhhUVm98HkcObohKRJo-l5LmKYlo6Z8ghccDv1qSYQ6DrbSL5otvr-3bCH1G57Kylrv6jvhU2b6y6u_r1VRnlORUMbGctycSWEI5NW7ppUgcAscr5lav9767TKTvKV2YYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=kFa_j9xtZhWqaYFVP1QOvC14Ho_SzGkjJZY-EWYvEMjjEU_5_1i7la2ANLpBWHu1pxoBzEe4sX2jfaNCURhDyTaP1_493_yDFTFCJNG2BuWKjsEDaz4ocxyBdS0kkOeeLh2go1U9ZBdmiMTbbFc4lHtfjMILueRVkFWfGJSscXIBppkIiEfL4B0Ysm6QwcY255Gsi4v1f1VusdyQJrEatRhhUVm98HkcObohKRJo-l5LmKYlo6Z8ghccDv1qSYQ6DrbSL5otvr-3bCH1G57Kylrv6jvhU2b6y6u_r1VRnlORUMbGctycSWEI5NW7ppUgcAscr5lav9767TKTvKV2YYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇺🇸
🇨🇳
دونالد ترامپ درباره شی جین‌پینگ: «شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72185" target="_blank">📅 21:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=a3jcsIXVSMtOjlJa5hOkeLv1oPNCMvtXC7sw8BATisCcd3hXnOcmOxXXBNwlADA8IttIE94ssNrQein7wqbrDiABf8G2tRrEuomyS2SrguVD-u4JNI2bk2EE74HXjemknfEHvomXsbqAVp-bRc0Uj6m28cpEw3qXeIoluc-Q0GlIOtxbOITM_xjwIxIAy3GacMsawSg7-c6FCBOyXfiioz5KyRjx1IyluN8c_IVnP5qhQj8915IPKeQVj9JdSsHzIQ1pUsa2xiVMJiKIFy_gTU-bZMH89lEJntWCwQwfyowdyXD0dcm5O8HBfWw1AbGLi2r4YAr4N3WxRfPFycvHlolnkHbUC6pa8DJepwtp8h0nMYKdfk0h3B80wrdKqDitlABVwI_6s3I-cHkUwNc2m_hq9z1nSd9syGWsHsLkmsB1SmcPEAsyQe-FG9KQySgTVrDayPGrnYAIzYViMu8yXBVa6RaAdvuumwF2EHBAEWiDZMmeHmhItt8iVQ-CWqfqHDN5ytZl-A6MgNMRC2LdZjzys3ql1CXX0WEscv6lYDTqzkcwE--6l9_f48nr6EvSw4INc89RLpoGOzrDd-14pxreTyDbjevMwqVbEvwTZ72ioQC2CNsaHhVLblp99FB46-FgX-9IaeUxWzLcFwuG32fYp9Lwcg1vequaZcJXvg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=a3jcsIXVSMtOjlJa5hOkeLv1oPNCMvtXC7sw8BATisCcd3hXnOcmOxXXBNwlADA8IttIE94ssNrQein7wqbrDiABf8G2tRrEuomyS2SrguVD-u4JNI2bk2EE74HXjemknfEHvomXsbqAVp-bRc0Uj6m28cpEw3qXeIoluc-Q0GlIOtxbOITM_xjwIxIAy3GacMsawSg7-c6FCBOyXfiioz5KyRjx1IyluN8c_IVnP5qhQj8915IPKeQVj9JdSsHzIQ1pUsa2xiVMJiKIFy_gTU-bZMH89lEJntWCwQwfyowdyXD0dcm5O8HBfWw1AbGLi2r4YAr4N3WxRfPFycvHlolnkHbUC6pa8DJepwtp8h0nMYKdfk0h3B80wrdKqDitlABVwI_6s3I-cHkUwNc2m_hq9z1nSd9syGWsHsLkmsB1SmcPEAsyQe-FG9KQySgTVrDayPGrnYAIzYViMu8yXBVa6RaAdvuumwF2EHBAEWiDZMmeHmhItt8iVQ-CWqfqHDN5ytZl-A6MgNMRC2LdZjzys3ql1CXX0WEscv6lYDTqzkcwE--6l9_f48nr6EvSw4INc89RLpoGOzrDd-14pxreTyDbjevMwqVbEvwTZ72ioQC2CNsaHhVLblp99FB46-FgX-9IaeUxWzLcFwuG32fYp9Lwcg1vequaZcJXvg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به مقر سازمان ملل در نیویورک می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72184" target="_blank">📅 20:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=OofHW0nP9vLbtzgKw8HzEJANQ4LStLfSRjzSQUWwpxoUM0S0ERFh9-JYIRIN-QLYr8Tvibo_4YkvTJGsIYhKkOiX3d7XFLffEX13VuH81JUSMO5__x_ESaAbALFx0EbNf3n15R1Pw2vHtckxnyoTwMQYJQf_KI86NPLoWpueLgxi1E0c4JQ3d_C4mf1EvDGtrwiP2Nb95-EQ3a2iONR5sQeoVyvTqqOXl_ocqJwhuwMKBnRQ5ZrznZJYkWkPKt1SYjj6TqFZXBSeksZIEzz2oC6h5KcH5tACSxMlgghhUoEesnrEHY-0mqK6Xqr1smzICzcLHE0Ego6cBnD8zclEvGkBuWJhXmCw7qiYVRjNH1Jg01tcp1rEa2YF7C96K7_p8UUiQr5vFPDiK2wSAvDvki5A4vpfSFymqdwkWKmE40DCVbDFZR6w0Jz9-yzWSHvBFYiMkwmo_m4Y88ggrbiaB6z9B-4UH4z9esUWTGoSreXgIt6MZH5KCnPdsCbHGdbI9dRQXzZy-T3xdnNQnH5q1PD0QHCIQdiIyIypsMaGT0pnTpBR5lPiz10wKqbl6qrKECWkEzjgi6WYUjT7st3-_g35kApByr4PcHpaORZVbA2nwl4tmcWQSRBGBFrk1hW_tgDInETPHT_ADrFOeET09ztPBH2FTmskqlBrMdYtkBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=OofHW0nP9vLbtzgKw8HzEJANQ4LStLfSRjzSQUWwpxoUM0S0ERFh9-JYIRIN-QLYr8Tvibo_4YkvTJGsIYhKkOiX3d7XFLffEX13VuH81JUSMO5__x_ESaAbALFx0EbNf3n15R1Pw2vHtckxnyoTwMQYJQf_KI86NPLoWpueLgxi1E0c4JQ3d_C4mf1EvDGtrwiP2Nb95-EQ3a2iONR5sQeoVyvTqqOXl_ocqJwhuwMKBnRQ5ZrznZJYkWkPKt1SYjj6TqFZXBSeksZIEzz2oC6h5KcH5tACSxMlgghhUoEesnrEHY-0mqK6Xqr1smzICzcLHE0Ego6cBnD8zclEvGkBuWJhXmCw7qiYVRjNH1Jg01tcp1rEa2YF7C96K7_p8UUiQr5vFPDiK2wSAvDvki5A4vpfSFymqdwkWKmE40DCVbDFZR6w0Jz9-yzWSHvBFYiMkwmo_m4Y88ggrbiaB6z9B-4UH4z9esUWTGoSreXgIt6MZH5KCnPdsCbHGdbI9dRQXzZy-T3xdnNQnH5q1PD0QHCIQdiIyIypsMaGT0pnTpBR5lPiz10wKqbl6qrKECWkEzjgi6WYUjT7st3-_g35kApByr4PcHpaORZVbA2nwl4tmcWQSRBGBFrk1hW_tgDInETPHT_ADrFOeET09ztPBH2FTmskqlBrMdYtkBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز یک بمب‌افکن رادارگریز B-2 و چهار جنگنده F-35 Lightning II بر فراز کاخ سفید در جریان سفر رئیس‌جمهور شی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72183" target="_blank">📅 18:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ElRxkxW0EGnFFqhA6-Au-cAyiZsMfJi3sFEj3GDQUtuJk1np40FoN8_t9v0kxa6jgbEq2d9aauWaORjhn90w2gkyxyU0XciSWFK1UzTqy33AWDdSfG2OIK-jJAhx1TrWLB2YetD8zAOz_9FmCLdj6glDpGPPp0_qu4I13x9_5g4Q8JONY_N_ea-4af2OFs6Y7u2C6rbaQZm_EWBuzJK2RXaLB5UpkhgatcnPMmSszFlYoxDYKxXhHKtYbEROUmOekdqYVXEgUb56FBqyyhYH6__qR_dpd4qCxrcAlIWpOCJRgWKZxi-O6zabXjjYb9T2a22xp9kcyM3HxWxW2Shvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز گزارش داده است که نزدیک به شش میلیون بشکه نفت خام توقیف‌ شده ایران به ارزش حدود (600 میلیون دلار) در حال عبور از اقیانوس اطلس به سمت خاک آمریکا است!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72182" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=TcDTXuMt-iWSsNA_SnmNJDy9bYS3L4oNUIJOrG-XMOzbAnej-Yr4gd09Cvy5pnWr0liDo0xtJytldp26HdAVibot6A4Wh2W99IvE89scEQproaXcrkOGGHe1vywljpSZA7tWIr9AdVmkEev0Js0H09PzXDresg0H1myf_do-F-GKknB_0KtWzZVhk4JMETtVPhdGJHSCRe-fKqoujz7y4aPf4iqRf_mEr4PnvOk0t2bOsxyZYNZoUVIU-04fQXw0JjphB5RpaJgdVCmvubAUxjO48ydSkRC6NAdFZEfgOAZcQWsUjshJUeyDDjW3m5fEeg1PWYmMvvrIZRvRiIN5xgD4yfHyphUhJetyxehW6FicoIsmSfuk_F5e41SQEHdxugjFrNRmjxt1hNRk_hON2Wls02I_JoBqaym5IGVJCYAyJZnhfgh8j0B9JyPmzIhxbI9pjeS7ss77hLL4VH3AIsWSNsUYtFxMpVJJeWQ1uHex5s0z2SU_yYVRGG3KCsAWS9UA8bXnCfYupRAyLCqqPdkgLBZUI_uMEiJkR8C3CzvvSlq06do9-nouh94bQj6vWpJHO9mwok_qDTGI2nNAub1fkx4J-JASFCvOcq3Kil5oXf6lmZVShlU4RPccLDLGr6t6t9UuIoIMDahEGkPkNjq5N5_mmHJGTE3JIKajSdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=TcDTXuMt-iWSsNA_SnmNJDy9bYS3L4oNUIJOrG-XMOzbAnej-Yr4gd09Cvy5pnWr0liDo0xtJytldp26HdAVibot6A4Wh2W99IvE89scEQproaXcrkOGGHe1vywljpSZA7tWIr9AdVmkEev0Js0H09PzXDresg0H1myf_do-F-GKknB_0KtWzZVhk4JMETtVPhdGJHSCRe-fKqoujz7y4aPf4iqRf_mEr4PnvOk0t2bOsxyZYNZoUVIU-04fQXw0JjphB5RpaJgdVCmvubAUxjO48ydSkRC6NAdFZEfgOAZcQWsUjshJUeyDDjW3m5fEeg1PWYmMvvrIZRvRiIN5xgD4yfHyphUhJetyxehW6FicoIsmSfuk_F5e41SQEHdxugjFrNRmjxt1hNRk_hON2Wls02I_JoBqaym5IGVJCYAyJZnhfgh8j0B9JyPmzIhxbI9pjeS7ss77hLL4VH3AIsWSNsUYtFxMpVJJeWQ1uHex5s0z2SU_yYVRGG3KCsAWS9UA8bXnCfYupRAyLCqqPdkgLBZUI_uMEiJkR8C3CzvvSlq06do9-nouh94bQj6vWpJHO9mwok_qDTGI2nNAub1fkx4J-JASFCvOcq3Kil5oXf6lmZVShlU4RPccLDLGr6t6t9UuIoIMDahEGkPkNjq5N5_mmHJGTE3JIKajSdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از شی جین‌پینگ در کاخ سفید استقبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72181" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72180">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72180" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72179">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYWqICHE6m0DENkDuyu6s4Zq08YtU7SgTtlepDnanLLesXXwgLVdeJ55iaFUUZHnv0NerLMKCSFnMOEIkUnqmL-4RFs-CI52h8xsNNVNCztl1UTV3DuRaO6lXxCNY-3dBPA5QGmekIVowE_K7zgfMvq6UIyWuUDUPAGbGlPy36Wg5lqY9boW4AbP9uCdr2Cs2LUFi7k3Y7bas50zbF5lcgsH8mftTqBNNREXszqjUNRDrOQB7h77lWJvYqSXZEboVX32epCtOn8VJBQkhCB-mjXauWJ2R1NrXJ_XGOkZA2HKEVuNoYbKEll5vjw90KzJE32SOr7bjalf_IkABvFMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72179" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72178">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuUnw4JYsfjaRevQJjA8XwHpZDPnRV6Fb2Gih4NBJeLjCepimIrnTNw_a6tA31eme1nCe1k0zOir8pdgs9oUJCzR4ZMcE6C7iF-IdYhrKVRYSFAl3LOUdEF0eYZfymCgfbKA8osUIrlfLqNZ_hfOHHKz9qd8EYBqdJ56jZyWSr6azqNEDNQ_H5YbQytjbSPcvNOwz2oaEieBnQbGBKrls7lg7ZFyfbTGKVnlGJ3I3gsRF20R-xBdxCxOLw3D_j6KAfsUteMxBVgGYWX2veME8CzGm4ETID7apOCThCAomXoSnUdkXLoyReNSPNePGYfK2_wjjE9iCV32T6OSIw_9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو برای شرکت در مجمع عمومی سازمان ملل وارد آمریکا شده است.
او قرار است امروز در نیویورک سخنرانی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72178" target="_blank">📅 17:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72175">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmaZ-XSzYo8W-E4mydWQS5YGTW_mZCRAMbcSl_5j4RS0ohCx4FCpjlLQ1GCumLiWskfPNVPC1_rwgNQkeJqIJZ6ccevD1By2gNNjHurFBUjJJHwcATEYmovlfqb9Wxcs8-iKd2TbT8_8aF0yoWowqedfWKlZ9dZ8Dla6nw0UGp5xXRya6rzy0wfLoeKfjxm3pobmlu76UQBD0UdIL5yZyEuhzav1dNXyHlbYUQnG1vRLbQ8oI4jtFIAit8z5luwmWG0giA0JIdcU5a43hl5dKeO0s-PdxUqEJmkfpAtiiuw4g0B_RmljI196Asno_8KAfgTzB4wdELLBEs5KxPO1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfzx10LJGlByJJWsLJooMPwRUl8h0jIGqkPdg9OAJJFF6sp4y8KFTshat5_NT-B3oUAp8gBTPMCP_UZSCFKRKD2tFK-IzCKoeBWwTwzsoQHSFgaZwsr_FMR1qZvZdQofbY6gT5Lm0E5rVHQgD5pxhFDHK3zqHK3AopnQWv7muTg9d9V0hFtV69Gx-SAZdZvFwkUCiWZU7qOGvhzqyZmpsAZnARSaJ0VarlyzRjMwuch7JUPmygj2VTQjSUVh9tlWSKU2wm--IaWnWXlf5WA317lMhApcru13VisGjiHhEF7a16MPWIQEN4GSW4oKttE32k1qL5J1kcrCrld6q8szAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=GLsAqNup7WE1LiDiB6HckH6YfMdsV2cPH2SMHmNo_SxPXeqAqZf_d3MyFk2PdG6uAEMYsAnqFNOlzbZsVpJ78NgUjxkSzjs-kdsMKECia1owQw8alQNNT7Q-Fca8GW3mWjbzrGxflJg82pEaAoNubKAXxUC94Tgjff58aenw2O00DQ6oLPpxmIOCtzhRAkNDKtDZNb1Fyorz9kNUBtnF4FHTbbV0jf6sRPsxuCEi0Pje2iGRSVqsqdKi4S2n7qee5pnMgVIOQ2Ph1Z2F5iCTt5MsEDg9L6zauUjKJo8xdTldlQ-j4OVzPgZt1hgkuQSz0AoIZ0yafcKq1D39Rk9pBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=GLsAqNup7WE1LiDiB6HckH6YfMdsV2cPH2SMHmNo_SxPXeqAqZf_d3MyFk2PdG6uAEMYsAnqFNOlzbZsVpJ78NgUjxkSzjs-kdsMKECia1owQw8alQNNT7Q-Fca8GW3mWjbzrGxflJg82pEaAoNubKAXxUC94Tgjff58aenw2O00DQ6oLPpxmIOCtzhRAkNDKtDZNb1Fyorz9kNUBtnF4FHTbbV0jf6sRPsxuCEi0Pje2iGRSVqsqdKi4S2n7qee5pnMgVIOQ2Ph1Z2F5iCTt5MsEDg9L6zauUjKJo8xdTldlQ-j4OVzPgZt1hgkuQSz0AoIZ0yafcKq1D39Rk9pBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل منطقه «کفر تبنیت» در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72175" target="_blank">📅 16:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72174">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=WxCNS_x2ahqHv_vz-aUId7wwgA71SAtm1aOBInK2XwK-17Ll60fG55itQ728-Qm5Qu3FPBlv8PG1NPdLAyxuZVZ-3-UMXcTlLlkh_qbX6Jr8v611REfo81OMN1syUcVFA9RIzPtUsIyNe0EUzaiQna2LW3XdybS2ZPGRbUS2oKzwCwWfBlsoXG4PzWnED19-Dz3kEfGpiDtGGkO08XOEC1i_SwRR8ucfffBwplNPDAK1Cy9ngVwcTAoHXV7SWb9I5aX5T0DP_clSilIrdnBbP0RmmDkQDQ-TwDKwImNiICzOYddH1FLwAKShnn6x4FnHbb-NJgyxxTIRjNyEGFK0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=WxCNS_x2ahqHv_vz-aUId7wwgA71SAtm1aOBInK2XwK-17Ll60fG55itQ728-Qm5Qu3FPBlv8PG1NPdLAyxuZVZ-3-UMXcTlLlkh_qbX6Jr8v611REfo81OMN1syUcVFA9RIzPtUsIyNe0EUzaiQna2LW3XdybS2ZPGRbUS2oKzwCwWfBlsoXG4PzWnED19-Dz3kEfGpiDtGGkO08XOEC1i_SwRR8ucfffBwplNPDAK1Cy9ngVwcTAoHXV7SWb9I5aX5T0DP_clSilIrdnBbP0RmmDkQDQ-TwDKwImNiICzOYddH1FLwAKShnn6x4FnHbb-NJgyxxTIRjNyEGFK0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غذای مجلس ترحیم، اگر خود مرحوم. این نوع غذا رو خورده بود حداقل ده سال دیگه زنده می‌موند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72174" target="_blank">📅 16:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72173">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=o2TAvuAMgfqPm_M4uJ7ImMosp9sxqR9C67hENS6AU50_yC4RImWb3FpqaqzBsp0cJOZu3L6K96Z4u7Iq1Ae27X9yNQKpJivPaX-Vph3Vpyd5H7h9Sg2X8Ugi91IPmJY4PwkUygv8aXqJLEXUDYiprVJXlfh3eU4xwqLd2vnNlzaU3LYlB1rU6cderGgkF2HQAptiE7amphLyNAPkdY3SMqEjxc6wm2Cz2rtz48h9WHEfVU7E8QhLtquJHfKaWcC485Y0A4VAq3VMNgUfjnzv2IrQXG4xn-fNG2XLoCIJZzLxoVpgU0hYdh3ddI08rufNc5BredSjBnfyh9Uemdu8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=o2TAvuAMgfqPm_M4uJ7ImMosp9sxqR9C67hENS6AU50_yC4RImWb3FpqaqzBsp0cJOZu3L6K96Z4u7Iq1Ae27X9yNQKpJivPaX-Vph3Vpyd5H7h9Sg2X8Ugi91IPmJY4PwkUygv8aXqJLEXUDYiprVJXlfh3eU4xwqLd2vnNlzaU3LYlB1rU6cderGgkF2HQAptiE7amphLyNAPkdY3SMqEjxc6wm2Cz2rtz48h9WHEfVU7E8QhLtquJHfKaWcC485Y0A4VAq3VMNgUfjnzv2IrQXG4xn-fNG2XLoCIJZzLxoVpgU0hYdh3ddI08rufNc5BredSjBnfyh9Uemdu8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقا پسر برای تولد دوس دخترش ۲۰۶ خریده و اینجوری سورپرایزش میکنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72173" target="_blank">📅 16:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72172">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a803db071d.mp4?token=cZ7r5wMeuodzn6BzdAw5eZBuB6sNgKSoLA14yODxGTgNHRxlaSEyPFaiAvCVujvytFkQHscz83vBNBOmlY7c91IfvVfaJxkpWYeyc-rUEOqYhBylvKqdktMFksrJPWFgf_RMiS4FJwqCEr9QkbeaHS0TK-yZnaoFiy0fNLHDeOXTywvWGm2nCJiPeGArFTPydz95faY51gtd88888yi50l69Wm5F2iSfoPH6J60XHeRzQV_P_IbHFueizro4_VtA0aZ4vkrpGw_p8OXR3UM-y0vYdkUZU4O5WlabpkM_KRBxuYfPKd3g0-lj9g9_1tMEIpYO8Qw1QFAA0I-QyzKN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a803db071d.mp4?token=cZ7r5wMeuodzn6BzdAw5eZBuB6sNgKSoLA14yODxGTgNHRxlaSEyPFaiAvCVujvytFkQHscz83vBNBOmlY7c91IfvVfaJxkpWYeyc-rUEOqYhBylvKqdktMFksrJPWFgf_RMiS4FJwqCEr9QkbeaHS0TK-yZnaoFiy0fNLHDeOXTywvWGm2nCJiPeGArFTPydz95faY51gtd88888yi50l69Wm5F2iSfoPH6J60XHeRzQV_P_IbHFueizro4_VtA0aZ4vkrpGw_p8OXR3UM-y0vYdkUZU4O5WlabpkM_KRBxuYfPKd3g0-lj9g9_1tMEIpYO8Qw1QFAA0I-QyzKN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور هائیتی در مجمع عمومی سازمان ملل خیلی جدی، از پارچ آب نوشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72172" target="_blank">📅 15:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72171">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=ZgD2iyXMu3AuRxBPKi6-fetq4qPFJsLsV9yIrZoF0_p7WpJjoob1DkfdrUExdqsD0NOEjcDPuM2tiE_PhqUsQYRxUrZzePlKxsb4LRYFbrZPRZzZ5MYP3KSeMJ3pwdeIwki1wmFDkqB1Yj2ECEjXmP6SxiSQb4trtbMJiZhcbcO3rDPaPKTNnm6BF-ooS34eMYdUVMHKwrrIW_ZpGbcg-pdtdH1BsIrbgwlzabNRxPlnnzrgifUmS26hvsGCtlGDbspI3dBfegKKGVI0SbK1_gzYmu5RafmM-bDeKNsrlVb_ovF4gyq15l91bjO4xSZkTbYWB-xs2_Lxzzc9IkgYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=ZgD2iyXMu3AuRxBPKi6-fetq4qPFJsLsV9yIrZoF0_p7WpJjoob1DkfdrUExdqsD0NOEjcDPuM2tiE_PhqUsQYRxUrZzePlKxsb4LRYFbrZPRZzZ5MYP3KSeMJ3pwdeIwki1wmFDkqB1Yj2ECEjXmP6SxiSQb4trtbMJiZhcbcO3rDPaPKTNnm6BF-ooS34eMYdUVMHKwrrIW_ZpGbcg-pdtdH1BsIrbgwlzabNRxPlnnzrgifUmS26hvsGCtlGDbspI3dBfegKKGVI0SbK1_gzYmu5RafmM-bDeKNsrlVb_ovF4gyq15l91bjO4xSZkTbYWB-xs2_Lxzzc9IkgYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماتون بریزه، ایران شده مهد عجایب خاورمیانه؛ این آقایی که می‌بينيد لاله گوشش رو سوراخ کرده و یه مار کرده توش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72171" target="_blank">📅 15:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72170">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=nIcDWNGq1kpzPGNe1qPKDwPTSeVXVi3TFn7Puo04bdzHgEYpYUa8lUFfTAx4AEuYWLFQObtTNGX7wiSoCk3OZ4MDgXp6OX58Zr3E6kFmeg5lnHilgV0eDa-zknjz-1kV7KJGDCBuPofh3QzLDOp1_JPwSk6qX2w3O5_6hJ3_QOaVPs3uxgTIYA8I5E6rZEPQH81E3qflBC6diTXAVP1pRdz2V8n1RcTLeiXanfpHHvZwjoA7m8yfVFuWRq1c2mgM4k60yUIqD5Y7hMGisTqdvuxYg6Yqe-XM2-AK0Xpmcq90jkFadgoxd7wU6Afvjs1rZmOYfOo0Y6BfxFPMQToNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=nIcDWNGq1kpzPGNe1qPKDwPTSeVXVi3TFn7Puo04bdzHgEYpYUa8lUFfTAx4AEuYWLFQObtTNGX7wiSoCk3OZ4MDgXp6OX58Zr3E6kFmeg5lnHilgV0eDa-zknjz-1kV7KJGDCBuPofh3QzLDOp1_JPwSk6qX2w3O5_6hJ3_QOaVPs3uxgTIYA8I5E6rZEPQH81E3qflBC6diTXAVP1pRdz2V8n1RcTLeiXanfpHHvZwjoA7m8yfVFuWRq1c2mgM4k60yUIqD5Y7hMGisTqdvuxYg6Yqe-XM2-AK0Xpmcq90jkFadgoxd7wU6Afvjs1rZmOYfOo0Y6BfxFPMQToNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره ترامپ وقتی B-1 لنسر وحشیانه از بالای سرش رد شد دیدن داره
🤣
انگار اصلاً نمی‌دونست داره میاد
😂
قیافه شی رئیس جمهور چین دیدنیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72170" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72169">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEqSfowS5TuUVesWFaVh-UJTtKj3qfl_L8FQjh351kbikmRCSCc37M2Yi4hrErD-L0z1HOlkZqR4BP_HX52NvuXvAasry7r43dua0Q-AsZK_Pf_oj13X0PH7Cm7LyczHXfAVWyci8p-ID3f9y5Z5GlZXh4mexdII4QsUY1XcbWkqTYeCE77VklDt30Wt6YCiVuEmiXbg_1RNI3e9UeHf_XsEsx6LtVn61sDTvY0CxXHsOy3BS1qaOVJ7lUySigUSYJeVqbZQHFhKprW4LKIdABCs7CggKCV0JS5Er-GJpuhlakNNP87BAuSQIaznvWo0UylOBetDnrb9ws8rMaqcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا و به نقل از سازمان هواپیمایی کشوری ایران، تمامی پروازهای شرکت‌های هواپیمایی ایرانی به مقصد امارات از نیمه‌شب لغو شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72169" target="_blank">📅 13:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72168">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyPzW5s6PqD_ofAVRkkXNnKh13R2mTyyo6Nk7ZhoSvI-dfDBQ38H7VQUJNxhpXqRQB5Mni_nWG1VjrhCgJHPsrMjGWeAwqFNPz-duUQphnffQdXSnau96EvEAznWLATop_g3xNAEL4ZN5pQRgi_UNG8Qy--p1AqRIsDWB2HOQeOC6iF7f5Nd_P16sJnS9To93f28Uueny-oCTLUHnKI43nSTz0d-VmB8H7R2UDT5M9os9sGo2eHC9C2CWh1k6D93nOZc7xhPE59-p5fwvh63mQlWF5hXfrFDDpU17PJADixeKH5PGzq9v091aQMS4R76CAnppAed4MSQCP2gK_jPY8jpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyPzW5s6PqD_ofAVRkkXNnKh13R2mTyyo6Nk7ZhoSvI-dfDBQ38H7VQUJNxhpXqRQB5Mni_nWG1VjrhCgJHPsrMjGWeAwqFNPz-duUQphnffQdXSnau96EvEAznWLATop_g3xNAEL4ZN5pQRgi_UNG8Qy--p1AqRIsDWB2HOQeOC6iF7f5Nd_P16sJnS9To93f28Uueny-oCTLUHnKI43nSTz0d-VmB8H7R2UDT5M9os9sGo2eHC9C2CWh1k6D93nOZc7xhPE59-p5fwvh63mQlWF5hXfrFDDpU17PJADixeKH5PGzq9v091aQMS4R76CAnppAed4MSQCP2gK_jPY8jpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:جمهوری اسلامی در نهایت تسلیم خواهد شد.
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آن‌ها سرانجام تسلیم خواهند شد.
هدف در اینجا می‌تواند یکی از این سه حالت باشد:
اعضای رژیم به جان هم بیفتند؛
نوعی قیام مردمی در ایران شکل بگیرد؛
یا اینکه ایرانی‌ها را متقاعد کنیم که اگر خواهان توافق هستند، به آن پایبند بمانند.
این بار، اگر توافقی حاصل شود، تضمین می‌کنم که آن‌ها به آن پایبند خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72168" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72167">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=KiRE3qzD-ACo9Z-2att7tcXM_QmdWp01mKzjbn07nEk4WKdx5n_r8LZAErhe4FoXdGUHCQweL8Zu3Vk5lIcnSTXSVm_aFV2Dz6bFhCk5ZvEPTKvHEzfUxfKwA0qUM0mVJPGWl9i-JA2QhwHWfl64zyErsNsTGzMQODnLgV_RvQEUc2fMW3txUzZh4FUZ_MiTSrOQZfjIWkwkEkYErfyxMTBIVaJwNtZdvjKh7rjSFOuWQJ29yImiPmhEN4uvwPA3tPIDsHgcKA6oPnKHwI1kmg959Tzn3gvpV8DJhlMOj70LKmcf-8b63-Q9POiKNJCjjq34ykiKH0YgjQWWBxxKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=KiRE3qzD-ACo9Z-2att7tcXM_QmdWp01mKzjbn07nEk4WKdx5n_r8LZAErhe4FoXdGUHCQweL8Zu3Vk5lIcnSTXSVm_aFV2Dz6bFhCk5ZvEPTKvHEzfUxfKwA0qUM0mVJPGWl9i-JA2QhwHWfl64zyErsNsTGzMQODnLgV_RvQEUc2fMW3txUzZh4FUZ_MiTSrOQZfjIWkwkEkYErfyxMTBIVaJwNtZdvjKh7rjSFOuWQJ29yImiPmhEN4uvwPA3tPIDsHgcKA6oPnKHwI1kmg959Tzn3gvpV8DJhlMOj70LKmcf-8b63-Q9POiKNJCjjq34ykiKH0YgjQWWBxxKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی رسما فرودگاههای کشورهای همسایه را تهدید به موشک‌باران می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72167" target="_blank">📅 12:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=fxkicJpxbQOcfQxdlLotOi6DlGewJo6lWT0tpK32SHpvoiSDriyE-VVdG-8jctEtFHuo5A2uChU-pj1ee2TS01ccg8Ce7DkSlPRRVJPbGwMXzACpJ1LGJO9NVHPtmHsp0CGqqljalN3EsYGXTz0RVDwvnyXojCOllydZocZ0X7VDNyemVuewzF9efEWO8E1eQQ_82uEzHoTBsQPmWZIJSB-Qj31KkWGeNXYMJIs3PL91jxHh_6b6Q9r9qRt2_uKdoPra7S_QpSAbaXSjs3s1_xDBL4h9ye0EW5X2jI2t1yJGR1x5Zkux4XhujbrFNq-l7IFFi6cS2Yw13vgGymAcC1oq0Tmyx8toVPIZfR0YllndwZ_iC7Kt9YjS8bTR4lsSkAFdP4r0rGF-KH154dVVDdAM3jjZRCCdwm97K7Ig3hkYF9Y7ycJxLlmF9MTR6cQKsq8zPiAVcC1uds2t1Y-7v-UH7bGrDzNsLqIa1bSJSGmOWYABbrqRB21m9rXaQ2f9BSFUFaO3DRj4TsTlMLHIAaJ1omq7pZ1rJ9PGLLYhD_qPBfxYCJflr3sqAsdCYx471HGT2_iE6obAizEvXgoU2kXs-FavcGz4QFJgq0XtC3NX5ZzgWMTZ6fGwJOwOJ-GscJ8B7B1mkFa1syvVlCXtcrlj7WIknBI242UMo-ZnBgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=fxkicJpxbQOcfQxdlLotOi6DlGewJo6lWT0tpK32SHpvoiSDriyE-VVdG-8jctEtFHuo5A2uChU-pj1ee2TS01ccg8Ce7DkSlPRRVJPbGwMXzACpJ1LGJO9NVHPtmHsp0CGqqljalN3EsYGXTz0RVDwvnyXojCOllydZocZ0X7VDNyemVuewzF9efEWO8E1eQQ_82uEzHoTBsQPmWZIJSB-Qj31KkWGeNXYMJIs3PL91jxHh_6b6Q9r9qRt2_uKdoPra7S_QpSAbaXSjs3s1_xDBL4h9ye0EW5X2jI2t1yJGR1x5Zkux4XhujbrFNq-l7IFFi6cS2Yw13vgGymAcC1oq0Tmyx8toVPIZfR0YllndwZ_iC7Kt9YjS8bTR4lsSkAFdP4r0rGF-KH154dVVDdAM3jjZRCCdwm97K7Ig3hkYF9Y7ycJxLlmF9MTR6cQKsq8zPiAVcC1uds2t1Y-7v-UH7bGrDzNsLqIa1bSJSGmOWYABbrqRB21m9rXaQ2f9BSFUFaO3DRj4TsTlMLHIAaJ1omq7pZ1rJ9PGLLYhD_qPBfxYCJflr3sqAsdCYx471HGT2_iE6obAizEvXgoU2kXs-FavcGz4QFJgq0XtC3NX5ZzgWMTZ6fGwJOwOJ-GscJ8B7B1mkFa1syvVlCXtcrlj7WIknBI242UMo-ZnBgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«پرواز هواپیمایی وارش» از «تهران» به «دوشنبه» _پایتخت تاجیکستان_ از مرز هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
این هواپیما سعی داشت از مسیر جایگزین و از سمت آذربایجان وارد تاجیکستان شود که مورد موافقت این کشور نیز قرار نگرفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72166" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72165">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72165" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI2qR9YFqkqANf28bT9W5arCnV6GQHVhWlsUOblYkR_AgG6bqjNkbG435suZERuhbiGWBmjqPfvfajJ5TJDJXNy_RdQ6eeJHKkxm5_1KIdmvUayrxxYXoUANvGHFFo_8CuiZel0tjho8qydbWWvewuHY9tuFUCxw9CutL_aR7l3H8Ny3f7xvOsDa-3_dd7aiOgHaGVPeFocJ3XJIC1G2rXdFYNLoCGLE1SbspJv7m-8sSAZOHSVRABZxvm8dwI8XQbz6lGxFWv53hAuVd7LVFUmUeFyN8ObwRX-SYWFkj8682ixvVmOi2SLf_gY2JUsi5IfoEh9wNz2OMF9PlCSqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72164" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=pvYC0hrN9oygyOTWvsDuIBy-znjU08O28YneQ722e24yqe0n-y1vxFKmMIh4JJQEY1NYZ3xXwPFGmchh_lo6iznXBimIEKQt0YQ9OMyzRfHe5C9MlOfrnr-qehOtpoLjAbaC4Z9KXJCMJmVrc3SqeWZTjMDnnWiTPktLthu19ja_3yddiJaeCf6JZrizMY4wK7OLG2AgcEsVgrmHN4GH-yPQnn6ECVzt7WuN4sqgAnJiBwFSfh2eRGXHBU7fyHhCTYgIHtXUI5ieCkFWIFpzGRTW8-Y7fDeEviAxji58JTYz3yULM7-aMjJj742KGctIkTDhVtjbMEBkQSmDUo80Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=pvYC0hrN9oygyOTWvsDuIBy-znjU08O28YneQ722e24yqe0n-y1vxFKmMIh4JJQEY1NYZ3xXwPFGmchh_lo6iznXBimIEKQt0YQ9OMyzRfHe5C9MlOfrnr-qehOtpoLjAbaC4Z9KXJCMJmVrc3SqeWZTjMDnnWiTPktLthu19ja_3yddiJaeCf6JZrizMY4wK7OLG2AgcEsVgrmHN4GH-yPQnn6ECVzt7WuN4sqgAnJiBwFSfh2eRGXHBU7fyHhCTYgIHtXUI5ieCkFWIFpzGRTW8-Y7fDeEviAxji58JTYz3yULM7-aMjJj742KGctIkTDhVtjbMEBkQSmDUo80Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که یه پسر از روتینش قبل از رفتن به مدرسه منتشر کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72163" target="_blank">📅 11:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=cqVQz30lk6IgoQofedxNo7Z3t2BVoRAhitIN_bNMtlPcOB49w4swwP_JyBPFCfvkGJiLG4KWBAFGlteiQYKI1BukfFujy23YdvN_-CI6RNqU7Z3p4UzQNpgOqEZx85D-GtVuV791vAcyfx0_IhhWCMM8kVe5pNra38mQnNEhqh7B6soKkPfOTh0uBsz-LT96F_9V6YbwssEdtyxkg4JwO18RhKYK43epeZfwRnMydpE5IErOyd-UV02iPn7I7XyqrqYXMUmXrRMWmjzO5WPOt1J1hGnJVH6ua00SBu4RQ2FzT0vVtSDe7cDo4m0hjqxLgbH_hCBouWaw1Y9L8eW0mGzVe2mRmb6bUcgjzFroJ1Y7snCmkoMJIQepTW3T47tYc9al8h_wslbiA7RPqSTrF-wXrkEJnZPBqBHz9LqNMSCfjrMTkLeBd1B7IJY10ZkY--fiZwILQnr9OXJYOK2RMvAJMyt4-iet_gM4F23rNL8zGZTwDYhagM22PXcgAb4q0tJbWchft7K0OgBaH1WO37tCXynKc_hGUbS0S5Yf13AFI3H4oycT-JIlJEcqp82mg4qQdCOhCP7s0eflDP55UE7DxQNsMKU5szicR3crKR4olSS7Hfegp_movlJM_qiQJ7Q6aUgzWmqqgqpCQOwUi97123B_lOaRypmMzvsVvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=cqVQz30lk6IgoQofedxNo7Z3t2BVoRAhitIN_bNMtlPcOB49w4swwP_JyBPFCfvkGJiLG4KWBAFGlteiQYKI1BukfFujy23YdvN_-CI6RNqU7Z3p4UzQNpgOqEZx85D-GtVuV791vAcyfx0_IhhWCMM8kVe5pNra38mQnNEhqh7B6soKkPfOTh0uBsz-LT96F_9V6YbwssEdtyxkg4JwO18RhKYK43epeZfwRnMydpE5IErOyd-UV02iPn7I7XyqrqYXMUmXrRMWmjzO5WPOt1J1hGnJVH6ua00SBu4RQ2FzT0vVtSDe7cDo4m0hjqxLgbH_hCBouWaw1Y9L8eW0mGzVe2mRmb6bUcgjzFroJ1Y7snCmkoMJIQepTW3T47tYc9al8h_wslbiA7RPqSTrF-wXrkEJnZPBqBHz9LqNMSCfjrMTkLeBd1B7IJY10ZkY--fiZwILQnr9OXJYOK2RMvAJMyt4-iet_gM4F23rNL8zGZTwDYhagM22PXcgAb4q0tJbWchft7K0OgBaH1WO37tCXynKc_hGUbS0S5Yf13AFI3H4oycT-JIlJEcqp82mg4qQdCOhCP7s0eflDP55UE7DxQNsMKU5szicR3crKR4olSS7Hfegp_movlJM_qiQJ7Q6aUgzWmqqgqpCQOwUi97123B_lOaRypmMzvsVvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیداً دوست‌دخترای مردم دارن برای پارتنراشون آیفون 18 میخرن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72162" target="_blank">📅 11:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72161">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دیروز صبح، تو یکی از مدرسه‌هایِ اندرزگو تهران، شروع سال تحصیلی رو اینجوری شروع کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72161" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72160">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=diaN8KCgo5X5w73K5vFANlSyD5H0AZfBnnTtrv0wfAZtM__iGN5OKzMd5hVmF5U3luAbDvLCGtNnIGbQNwvTIcej2pUMCZwA2FBsdvXXruXT3ESV-JlMdIoE3hfs4ryIsq8TgHlczD_nTA4gEs8qcfy8Av1hIVVRsm52_eiZqwYmUBVwAngsFQAmtm_0HwpTOW1QCX3D9Z-H9XubVMhB0I7TSXmxR7NzUk5TbfDAzJjBObjCcOiHZ6u0KV3ufUhQtkaYAakEvtGW5Sqx50E_hq0clVywYovqw4u0_RRXtyrNQa2o9VDASIyJYctmt_QEKVzetSKxNv_WXPZ00UEUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=diaN8KCgo5X5w73K5vFANlSyD5H0AZfBnnTtrv0wfAZtM__iGN5OKzMd5hVmF5U3luAbDvLCGtNnIGbQNwvTIcej2pUMCZwA2FBsdvXXruXT3ESV-JlMdIoE3hfs4ryIsq8TgHlczD_nTA4gEs8qcfy8Av1hIVVRsm52_eiZqwYmUBVwAngsFQAmtm_0HwpTOW1QCX3D9Z-H9XubVMhB0I7TSXmxR7NzUk5TbfDAzJjBObjCcOiHZ6u0KV3ufUhQtkaYAakEvtGW5Sqx50E_hq0clVywYovqw4u0_RRXtyrNQa2o9VDASIyJYctmt_QEKVzetSKxNv_WXPZ00UEUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره از خروس میترسید و رفیقاش گفتن اگه بتونی 10 ثانیه نگهش داری، بهت آیفون 18 پرومکس میدیم.
و در نهایت این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72160" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=BPJhbhe9aD9tjWtSHfQBgBLd4Dfs-4WeBDwAcZvrpXcdFWKWE6spgnAJAqu940bRFXccy03AmiLadwDoTRGxvUMYz_0W_Pl-bTgE4mlYnhweaBoBIoa5NWOiuM5RPyIV35h3mVfN9yxyz41LXPRADQ15nNUMsD99T7CRQ-OeZJsAX4QdWWUppKkGn29aRFnlZbseaSjbIa1V1oMXDGOqCYavs2fx0iyRrC0ZMCyluix3_KIIhaAypZxkoUinEkBmAhjD5WghqZfrhuHktFRvOhhL1weouohnvZB3ly9wqWAi6HJDRTGAE8dn6r2uj4RrLA2jKILKsogMCWl_kh3YuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=BPJhbhe9aD9tjWtSHfQBgBLd4Dfs-4WeBDwAcZvrpXcdFWKWE6spgnAJAqu940bRFXccy03AmiLadwDoTRGxvUMYz_0W_Pl-bTgE4mlYnhweaBoBIoa5NWOiuM5RPyIV35h3mVfN9yxyz41LXPRADQ15nNUMsD99T7CRQ-OeZJsAX4QdWWUppKkGn29aRFnlZbseaSjbIa1V1oMXDGOqCYavs2fx0iyRrC0ZMCyluix3_KIIhaAypZxkoUinEkBmAhjD5WghqZfrhuHktFRvOhhL1weouohnvZB3ly9wqWAi6HJDRTGAE8dn6r2uj4RrLA2jKILKsogMCWl_kh3YuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لحظه سقوط یک جت آموزشی RAF Hawk T2 اندکی پس از برخاستن از دره RAF در انگلیس امروز را نشان می‌دهد.
هر دو خلبان به سرعت بیرون پریدند و زنده ماندند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72159" target="_blank">📅 09:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=svIvBofmmmdGWVrvyZLfSyz6TOi0X-pZZ5aorDwgtV3ifz4Z7z7t8760LYMzq0pWIRoAv_f3IYoBW1pMLly59DtvE0r8Ij0jgr6f1BCDpJn6hXrxFq7Y15WI7u5Y2YDjv2I4NORHUwZmH3Xnh204pEINfOuozzH0HbvlbWYUDNGBzGHKuw9oFlQZU9u60-HlkNPLdVRYE79m3xAzx1JIgSd-uddyynvvdROMcN5hVBlCLfxknvyntBc5AOcE34fZ207yDGoaoaubMrCXuQUqCQSUR0iG63mslNK3ix8YiKQncMUqwRs0OBYoXIQqhx5Z3egJgisPvCYttKN-arQeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=svIvBofmmmdGWVrvyZLfSyz6TOi0X-pZZ5aorDwgtV3ifz4Z7z7t8760LYMzq0pWIRoAv_f3IYoBW1pMLly59DtvE0r8Ij0jgr6f1BCDpJn6hXrxFq7Y15WI7u5Y2YDjv2I4NORHUwZmH3Xnh204pEINfOuozzH0HbvlbWYUDNGBzGHKuw9oFlQZU9u60-HlkNPLdVRYE79m3xAzx1JIgSd-uddyynvvdROMcN5hVBlCLfxknvyntBc5AOcE34fZ207yDGoaoaubMrCXuQUqCQSUR0iG63mslNK3ix8YiKQncMUqwRs0OBYoXIQqhx5Z3egJgisPvCYttKN-arQeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعجب از  عکس‌العمل بی‌تفاوت نماینده جمهوری اسلامی در سازمان ملل، به تهدیدات ترامپ در یک برنامه تلویزیونی
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72158" target="_blank">📅 09:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72157">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=d3rEYt2BsRDngek_UVLaZdDw0JHxsJ_TgUS2pZ9VKm8xMttGGkqeXSNC-reCv6siaW2W91hDMDrzhXPpigqwGcxsWMIV9-2PHr5vbFsa_LUbZ2bM0RENaCzRgQC3W65eCA-Iw4CINoFawtOvSrvOgb57cU_kPX2Pl-EfT8CFcGJOjn9gibdsbMzUvC94kIiclokYRx_0WB2rKcvStsg-X-sPEQIEl5-vE1oXFQT0UbCkxH2jzRGbbn6a8-bLyk8e3YxDyvz-wi82tUU4XssOkrpOqQhloVPuYvyOfyo5GmKTv0VRgUyWXtW4mG3X6OPU2XAlYwvzGisTOYB_6d4Q5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=d3rEYt2BsRDngek_UVLaZdDw0JHxsJ_TgUS2pZ9VKm8xMttGGkqeXSNC-reCv6siaW2W91hDMDrzhXPpigqwGcxsWMIV9-2PHr5vbFsa_LUbZ2bM0RENaCzRgQC3W65eCA-Iw4CINoFawtOvSrvOgb57cU_kPX2Pl-EfT8CFcGJOjn9gibdsbMzUvC94kIiclokYRx_0WB2rKcvStsg-X-sPEQIEl5-vE1oXFQT0UbCkxH2jzRGbbn6a8-bLyk8e3YxDyvz-wi82tUU4XssOkrpOqQhloVPuYvyOfyo5GmKTv0VRgUyWXtW4mG3X6OPU2XAlYwvzGisTOYB_6d4Q5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ممکن است به نفتکش‌ها حمله شود؛ اما بسیاری از آن‌ها به مسیر خود ادامه می‌دهند. آن‌ها صرفاً به حرکتشان ادامه می‌دهند.
ایرانی‌ها ممکن است ۳، ۴، ۵ یا ۶ پهپاد به سمت آن‌ها روانه کنند، اما نیروی دریایی قدرتمند ما مانع آن‌ها می‌شود.
با این حال، ما روزانه بین ۱۰، ۱۵ و گاهی ۱۷ میلیون بشکه نفت صادر می‌کنیم.
برای درک بهتر این ارقام باید گفت که پیش از آغاز درگیری‌ها، این میزان ۲۰ میلیون بشکه بود؛ ضمن اینکه احتمالاً ۳ میلیون بشکه دیگر نیز از طریق روش‌های جایگزین صادر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72157" target="_blank">📅 07:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72156">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=gUxMNnQzFhnxtOvnotyPmWnxGHkJZ215bvMViQIngctCA2rLyOb7Hx_3mQe7mC__tdQRpL2KaoaZOWPCb6ooB_YoSj2DxRKFAVYmKb9qCfjYEV6RvHJ_b5iuy0JnQOvkpVgcrRMWtcEAxpk1BseIS09yaaUnx7UQ_ffCGbYofr_PofFKNvgnEvUuOY-HRELbfujfAzV4H2MAexkgFbw7iBbAiRfIDscz831cDBjNMEaepPZ6MoK48l2WjCqji3jdq2ZwTrI0qGGj2oyISlwfd3nehrVY5L0Tt-fSCNYWVdsXeQl3-3eRtaTRISDWiccxTFIPUOi3NJs_pCoq79svrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=gUxMNnQzFhnxtOvnotyPmWnxGHkJZ215bvMViQIngctCA2rLyOb7Hx_3mQe7mC__tdQRpL2KaoaZOWPCb6ooB_YoSj2DxRKFAVYmKb9qCfjYEV6RvHJ_b5iuy0JnQOvkpVgcrRMWtcEAxpk1BseIS09yaaUnx7UQ_ffCGbYofr_PofFKNvgnEvUuOY-HRELbfujfAzV4H2MAexkgFbw7iBbAiRfIDscz831cDBjNMEaepPZ6MoK48l2WjCqji3jdq2ZwTrI0qGGj2oyISlwfd3nehrVY5L0Tt-fSCNYWVdsXeQl3-3eRtaTRISDWiccxTFIPUOi3NJs_pCoq79svrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
احتمالاً بیش از ۸۰ یا ۹۰ درصد پروازهای خارجی از مبدأ ایران متوقف شده‌اند.
مطمئن نیستم نمایندگان ایران در سازمان ملل چگونه قرار است به کشورشان بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72156" target="_blank">📅 07:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=ebBsDiy0MyIkQqyaMcmtUifSkGfxccIPgiACMY-vmwNu-A_K9rd3Tcl9tE6dHOwpWi5xdfwK66HXRW7lG_XTjAkgM09azG5ndB9hxhsR_E4Ia7eQp1g49_44CpaXt6dQ0i-3PdkU-HceG82QjCyM2vwcAypdGOwZn3GJgZlNCoA4BovIMg87ib82X4oKHzAP5I9QQgbKgYrg3JJfNw_DHdNPICbxKZ0xgHUpn4vm70hn2mPXBsJE9iqqEHyzqDsmrl1p5KjFpakFP9IuyydnzyEZ-drTv8Gb28d4w7hOMsd75tXrV6u668C8O8RmC3JBBF8v9PpQcnZI0wO22HtqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=ebBsDiy0MyIkQqyaMcmtUifSkGfxccIPgiACMY-vmwNu-A_K9rd3Tcl9tE6dHOwpWi5xdfwK66HXRW7lG_XTjAkgM09azG5ndB9hxhsR_E4Ia7eQp1g49_44CpaXt6dQ0i-3PdkU-HceG82QjCyM2vwcAypdGOwZn3GJgZlNCoA4BovIMg87ib82X4oKHzAP5I9QQgbKgYrg3JJfNw_DHdNPICbxKZ0xgHUpn4vm70hn2mPXBsJE9iqqEHyzqDsmrl1p5KjFpakFP9IuyydnzyEZ-drTv8Gb28d4w7hOMsd75tXrV6u668C8O8RmC3JBBF8v9PpQcnZI0wO22HtqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن B-1 Lancer نیروی هوایی ایالات متحده، همزمان با استقبال پرزیدنت ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، در واشنگتن، بر فراز این شهر پرواز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72153" target="_blank">📅 01:54 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
