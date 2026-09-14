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
<img src="https://cdn4.telesco.pe/file/tXKYkniiWao3s_e6EefuYrklfiHigUF2ErfuoFQlZvpEjoHcu-8DQI_jUwyCnhZqyW9CMUBB6Xsf7ymXjTGOSz8sAkwjudV1y0TBhJRr1vXao73lbdbA26OX6CAzqaCtDL91Y9eIAW73gsqAFY3e2OtSOdxHoxZO-Gv5fNquYIXorEJqm_fDWOS42osKrEDOzjC86g7r0_V2DpIg1APqoErl9bk0aQ4OnPzDlUfMjVXcWQEaDeLk5N3zW1uETz84PKyeK70ioLQJlQTMLkvx31ChqPwJ-ytlh--m6GQKgcu4ARteexmwCqONpgCW6GMHsZLaCZhqgKLfzpKGaYTk2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 227K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-83407">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">البته مطمئن نیستم ممبرا تو کامنتا گفتن</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/funhiphop/83407" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83406">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">زدنننن</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/funhiphop/83406" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بچها میدونستین خخخخ مخفف خدا خیرت بده خیلی خندیدیمه؟</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/funhiphop/83404" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin</strong></div>
<div class="tg-text">بچها میدونستین خخخخ مخفف خدا خیرت بده خیلی خندیدیمه؟</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/funhiphop/83403" target="_blank">📅 18:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حالا بازیگر لر و پژو پارس از کجا قراره پیدا کنن</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/83402" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS9Vkz4lyHUdKfZNxTCMIKS2GeVqOrpAJ1h5clUJkH9uuhj4rzeq1Hsbz0qjBhN9Nct3nOKLkZyAZvCBh34jv_ENT6jvJk-VNB_8Pg2-Pg4HKWqCYMCC1rUO0tzpHT0iAYRh0AIEqBSTDWlyOeez6Xo5c_rUupmGrTtUoZ5MYaW1syrlO92eCqZ1Li6bZhkaDHlgx2LsCfnkDQrb8JRDoGtYUNGDPaBmc0BaScnU9LWVWg4H1KDgMXIMfeGvl04p5Tk1JQDSOKLocS161QkyYxEm5VkpUqDCFGt9IfcTaI_nwC5mw09BtHXq3o9mpIXJ_N3h6-WKgys15VGVvomNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال seal team فصل ۳ قسمت ۸ یچی تو این مایه ها ساخته بودن که خلبان امریکایی تو ایران گیر میوفته و میرن واس نجاتش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/funhiphop/83401" target="_blank">📅 18:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بازیگرش تام کروز باشه کاش، اسمشم بزارن تاپ گان ۳</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/83400" target="_blank">📅 18:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">البته یکی دوسال دیگه فیلمشو میسازن میفهمیم</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/83399" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پس از ایجکت از جنگنده‌ای که بر فراز ایران سرنگون شد، «براوو»، افسر نیروی هوایی آمریکا، هنگام برخورد با زمین دچار شکستگی کمر، دست و شانه شد. او که به شدت آسیب دیده و در دره‌ای محصور در میان صخره‌ها به دام افتاده بود، می‌گوید تمام توان خود را جمع کرد تا از ارتفاع…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/funhiphop/83398" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینام ادامش که میان و میبرنش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/83397" target="_blank">📅 18:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83396">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پس از ایجکت از جنگنده‌ای که بر فراز ایران سرنگون شد، «براوو»، افسر نیروی هوایی آمریکا، هنگام برخورد با زمین دچار شکستگی کمر، دست و شانه شد. او که به شدت آسیب دیده و در دره‌ای محصور در میان صخره‌ها به دام افتاده بود، می‌گوید تمام توان خود را جمع کرد تا از ارتفاع ۲۱۰۰ متری بالا برود تا از اسارت بگریزد.
او در گفتگو با برنامه «60 Minutes» گفت: «هرگز اجازه ندهید کمبود انگیزه باعث شود پایتان به تلویزیون ایران باز شود.»
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/83396" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصاحبه خلبان امریکایی که تو ایران گیر افتاده بود
«براوو»، افسر نیروی هوایی آمریکا که اوایل امسال بر فراز ایران سرنگون شد، می‌گوید: «وقتی به بالا نگاه کردم و هیچ چتر نجاتی ندیدم، آن لحظه ترسانک‌ترین چیزی بود که تا به حال دیده‌ام.»
چتر نجات او در جریان حمله به جنگنده‌اش آسیب دیده بود. براوو می‌گوید در واقع در حال سقوط آزاد بود و متخصصان نظامی بعداً برآورد کردند که او با سرعتی بین ۷۰ تا ۱۰۰ مایل بر ساعت (حدود ۱۱۲ تا ۱۶۰ کیلومتر بر ساعت) به زمین برخورد کرده است.
ما هرگز نخواهیم فهمید براوو دقیقاً با چه سرعتی در حال سقوط بود، اما این برخورد باعث شکستگی کمر او شد. او همچنین دچار شکستگی دست، شکستگی شانه و پیچ‌خوردگی مچ پا شد و از ناحیه بریدگی‌ها و خراشیدگی‌های سر و صورت دچار خونریزی شده بود.
براوو زنده ماندن خود را یک «معجزه امروزی» می‌نامد.
او می‌گوید: «من باور دارم این گواهی بر لطف و مراقبت خدا در زندگی من است که مرا از آن لحظه به گونه‌ای عبور داد که جلوی مصدومیت را نگرفت، اما مانع از آسیب‌های مهلکی شد که می‌توانست توانایی زنده ماندنم را از من بگیرد.»
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/83395" target="_blank">📅 17:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzkhWilkQQKF3sDKvsJbrJKdiHGjvYTD-rZJUeFeHOgP5jIytoWxiH7zAamQmbBe9TZ9Q-8Sb_D2DDDQMBdsZEqB29Nkyp0e35Zv68yj9qlYoI5ZdQKFgcuZ_mcY5-QsvM_VObXEyhNaiHajD9pXgQRlGoxxfQiwrgTZypG34gqoI6gmADVA_P_qBNgSC_6ofH8V9yXdiY2CCqTxpys_oO57Kxr_sCFdEWagugABTjwlkdPPmWGkFLFQE3vKtMnyICtBruzpeaSfJKrrGah3OvNvVe5M5c7F7o1OaDH6W10R6fuSKwLE-HbQ7oFxFwpuz85HVdMRNDNCNPfsG9cYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان چی پیش خودش فکر کرد گفت من هانی رامبدو معروف کردم پسر</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/83394" target="_blank">📅 17:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83393">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هادی چوپان چی پیش خودش فکر کرد گفت من هانی رامبدو معروف کردم پسر</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/funhiphop/83393" target="_blank">📅 17:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83392">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هان اها چی میگی ها هاها اهان ترپه ها
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/83392" target="_blank">📅 16:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83391">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">متاسفم اینو میگم ولی این دفعه پوتک جواب آرتا رو میده و احتمال زیاد بیف داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/83391" target="_blank">📅 15:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83390">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4983eb567c.mp4?token=aISynd443IF9QW8MQ4FeYAH9U2OIddw2dvIgBJmw-MlzsQy6NM0d7HSsQpYk5M27iCVWfRZq5-V--EnrTZkPrynlGBaOI14AV10JzGTQOBZmovfBWD3bwnrNFJJqO7V-GxWibOzujX3MXpCxO0Wqyw36h3BZ4a2tIs7nol5y02mLZ3piwtkQOtwxmiiSnZMndPfoEqD4Zdqb1rCHM6qKXXLzk8dQM4JS4SpjIAkWAJLbY_t2TDYmWmT8gcGF8f1GA_Ryw7g_9XosefAyVaSyM9vzw7gNPG07m4cci92U8ZPQrgfJ24U_eMVu8kyCJj393ypYOKrfY2N29aDjtlbeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4983eb567c.mp4?token=aISynd443IF9QW8MQ4FeYAH9U2OIddw2dvIgBJmw-MlzsQy6NM0d7HSsQpYk5M27iCVWfRZq5-V--EnrTZkPrynlGBaOI14AV10JzGTQOBZmovfBWD3bwnrNFJJqO7V-GxWibOzujX3MXpCxO0Wqyw36h3BZ4a2tIs7nol5y02mLZ3piwtkQOtwxmiiSnZMndPfoEqD4Zdqb1rCHM6qKXXLzk8dQM4JS4SpjIAkWAJLbY_t2TDYmWmT8gcGF8f1GA_Ryw7g_9XosefAyVaSyM9vzw7gNPG07m4cci92U8ZPQrgfJ24U_eMVu8kyCJj393ypYOKrfY2N29aDjtlbeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتا این فیلم رقصیدن پوتکو گذاشته چنلش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83390" target="_blank">📅 14:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83389">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">علی گرامی ناموسا من آهنگتو پوشش بدم خودت خندت نمیگیره؟</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83389" target="_blank">📅 14:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83388">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">علی گرامی ناموسا من آهنگتو پوشش بدم خودت خندت نمیگیره؟</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83388" target="_blank">📅 14:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83387">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه کشتی اردنی رو تو تنگه هرمز زدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83387" target="_blank">📅 13:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83386">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKmhVMcQ5bJpuNSnpvYKyswpBlRbrI-lgBhcu7raF0OXvcecmaNeYlp3MQUVAqzyhlYXWaNplNkzZpQniDSn2wB5dewV_1aXDSbv6ybExliMp0R79E1oBFco24tKtseTtCf-OFk-CXy4lGwU_kKOB7w1bJnima15oN8wejhx73MZJDqS5RdVeBe9apT-u7vNS6zwZMeDL4p5nNPx1iKpys1juEBMSnsgifoS2rYXxReripvknlSrKVorf6vdhWLvCKQTeF2DGNYRvJ-aCYKL4TufzDD_MAMlkwOU0umlv8sPkqBKUVOtZgmU_i153orqw66DhCUw-7TlmDbHjIp-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیا دو خط خندیدیم بهش فروتن بازیش گل کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83386" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83385">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دیس ترک جدید آرتا به نام "X Mamnoo" منتشر شد
🟠
SoundCloud  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83385" target="_blank">📅 13:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83384">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیس ترک جدید آرتا به نام "X Mamnoo" منتشر شد
🟠
SoundCloud  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83384" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83383">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRJiWlf-3KC9oScpgrmf0FedY1d55yerkvJVPMLyyBoSjyZhevBMkshcZONUHKSsdo9Xp0W7Jh3lra4bfJRlAcibmJbPmJxcd9JX_RSpsb58hknYYTGtfqINlaVQ0qXJErU42kar8WycQYMAdqe-If4xKIVF5V05hsUViusy0njfzrAB_YX0tP5bx2aACihikKn2CJ1XjZitSjpMEHu509yM7Z7WxqJ3a7T8dC8_mI5DqJv9Q5SkDxOs3Z3r0DRZR985GN-3w1fSbMGnnLzhhAmEtYq_fDdajrgLzu1XQeMJEB52_QExOie3HWATZWVqsx-Dh0EsEUoP9sLCAlu2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به نام "X Mamnoo" منتشر شد
🟠
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83383" target="_blank">📅 13:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83382">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=QNqOE0iJ527Kw0prSN3-3oSgUR71hft39r4Bsfy4svxmmd7rz5VqBsDYqAfNXjEEPlTAqtofCW3REaT05yq0-6QLmviVUAIfu6XKwy2B_S8r32j2aIyBH4Yk2MyGjNdjFCYbNgS5LYNwE-d6aTRIw5tQUME8STfueU_SLhY1ek9k9srFSO3Va5w6UXJCxvkxFM50xWYcjDirlHku47bAHwIEeYj6ubprIQJUZV_NdPVeW4vJxt8QqqkHgh2Am_RTtbwvztnXW973oSIEFdew9PAV50a3ctqffOFajqfVb1fRVqJcV23ZRkc4ZY7bwi_bLpIofayPP9q_VQbLIYHJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=QNqOE0iJ527Kw0prSN3-3oSgUR71hft39r4Bsfy4svxmmd7rz5VqBsDYqAfNXjEEPlTAqtofCW3REaT05yq0-6QLmviVUAIfu6XKwy2B_S8r32j2aIyBH4Yk2MyGjNdjFCYbNgS5LYNwE-d6aTRIw5tQUME8STfueU_SLhY1ek9k9srFSO3Va5w6UXJCxvkxFM50xWYcjDirlHku47bAHwIEeYj6ubprIQJUZV_NdPVeW4vJxt8QqqkHgh2Am_RTtbwvztnXW973oSIEFdew9PAV50a3ctqffOFajqfVb1fRVqJcV23ZRkc4ZY7bwi_bLpIofayPP9q_VQbLIYHJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتا پوتکو دیس کرد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83382" target="_blank">📅 13:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHP9vZ1H7EjAy4tlPNwNxGiKDyRIOGrA0zl9TJDj7HJwyiGhjCqan25Bxjg1Olde82OHWk_-EycoPfft1SzQxj8kW_B59QEdTH6QQd-d4eRLF0fhnnsRO9K6AzFOo9-I4P3iZUU1UqNw7cDl11ZtQ9C0yiDt8IUZC-SeeUNbmgkrOvzW6uVgX5QP-dgTZ2iuXst47NqOs4FM1deJH5wQOIt1bBrRSrp17MOy5KDeDSkKpsZiSVILv_SNCSL7EKaSoScipCZx8EH_KKUGRM8o8l1_R54S5nMyY8P1vakVPtUfA9JRMa68wTTBvHzrBK8XbZgCOV4RZ61Pt61c-yqTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا اگه دیس نباشه یجور فحش کشت کنم افسردگی بگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/83381" target="_blank">📅 13:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85a866ba9.mp4?token=j0qhM9JBBv0-Ice2n8n6h82h-G4m1Q3RLhSFCyTWfWbGJ_nMLv2GqLfTi9Il14pC_iG1LFx802VpWKSVxe3dhgBCvvuZ_Es1keZE1o3nfBaNx8EfIl4mcsZzDA0lnKrTfqP0fS7ZzZqHfvGITcK_qRelC_u6Zy9ScCdbONCUi4z3P8xOvraYelCoi15q3QiVtyCaCkqJt9gEHbj9TeljJ9nwFEFxFQmkyjB0jGKoHwV0OmTzMtqLjbaeTZvA7f4KXsgvYZb_SWLhg345RoYsL9ayuu-rqo0bOXDs8p0DezBjtk2cc-RtFCHGfgIdUSn_9DllBkIOMhcfiPtadpsIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85a866ba9.mp4?token=j0qhM9JBBv0-Ice2n8n6h82h-G4m1Q3RLhSFCyTWfWbGJ_nMLv2GqLfTi9Il14pC_iG1LFx802VpWKSVxe3dhgBCvvuZ_Es1keZE1o3nfBaNx8EfIl4mcsZzDA0lnKrTfqP0fS7ZzZqHfvGITcK_qRelC_u6Zy9ScCdbONCUi4z3P8xOvraYelCoi15q3QiVtyCaCkqJt9gEHbj9TeljJ9nwFEFxFQmkyjB0jGKoHwV0OmTzMtqLjbaeTZvA7f4KXsgvYZb_SWLhg345RoYsL9ayuu-rqo0bOXDs8p0DezBjtk2cc-RtFCHGfgIdUSn_9DllBkIOMhcfiPtadpsIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشهدیا تا اطلاع ثانوی شبا ماشیناتون رو بزارید پارکینگ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83380" target="_blank">📅 13:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83379">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بقایی:
زیر دریایی آمریکا به غنیمت گرفته شده و غنیمت حلاله بخوان دنبالش بیفتنم اصن پس نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83379" target="_blank">📅 12:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6f_L0sHRQRG9urTZmFZEQeTPcghatlhjljcGCOS-OOK4SDN9T1nQu4-TJskXWDNBXkms5O63dZuTmrLtlkkmhifWF7Z0vn-shp-8rb8NozzT5RULm1Fx3xtjbUAqMTdqKm_vcFQquiWieNjw3M9Sh2pxOM_9REHZdty3JUqt0_toiaruBHXJtKIpfrQW8uC1B2oji7ocgiyHNa80Y_JmDpUxhLAT4K1Xu_FxSOBg23ONnR3qCnf1yVJu0Z5cEpI-8Gr2EFQPQhHN7RxcDO1jyeTSwIJRanZUobCp2C_xO65KzpPF1WiWhxVuWS_ld6UY_8gf4RHSHGvqyWi9EK4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کوروش، اصلا معلوم نیست منظورش پوتکه
🤓
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83378" target="_blank">📅 11:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83377">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjSau6CoE0Oy-gO-Vz8m5730Wou0WTjhTyXS0bmqr67OxOe1o0ueEvvcYn1-cDZEFLE0CPXmhKwLR8uMnhsHNPXgCqGw7n0yzvirfYxMsBzhj8BUPxeKt54WP8SFyVeqJX2Bgt1hf_0K-fRzW-gRWri-m8echMj87H67XkKs7jk3uMNDS5803kDJqvoUBSqAItYPs3m0bcXDO7rC2d-r3XT3km8M-jUoGp7ARHtWFUIezflZsKte7u89IbHvYQW5AdP7GAg5pOxdnBW-cIOXWXi7REAgccNnE0n8wuUByXEmapyWeke1sZZrKMb9UpyA3RXriFHBsqZudja56VCo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه رپر دیگه رو تو آمریکا کشتن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83377" target="_blank">📅 11:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83376">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚽️
مهم‌ترین فوتبال ایران و جهان با بری بت
⚽️</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/83376" target="_blank">📅 11:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83375">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQb1qs8JJ0Es1OkeIzsGGeWV1Mihr3FJ825nGMqzkNkKX1UX6w5W7iOLWUjVFaFlE8uNMCs0AnDGlXke1S0VKonYFiRywv6fJHXLzbW8-Ms7TlnyzXYSL_UiuDIcoIdW_Bhw3ks4VBGdms5B1hY8ZM22LkxT1T4gzjM7I2_ecOhwhwrV3XDwAC6MFQoLOYWtYjAYeb6g4pjBCKc0n9FAiPsyIAtiismZE-z_W8W6ZsGjZVY6lzd37R6UUgppSlIROTMzFJYAg1nu8x4J6L3HtOBrFrX7IXSudAmgeqjmT1_Fnb59GE0N4WcI_fac5OJsFM9N0xF8yWwqQjwBjEEjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کی میبره؟
👑
👕
السد دوحه؟
👕
استقلال؟
🧑‍💻
از همین حالا با بهترین شرایط این رقابت جذاب را پیش بینی کنید
💖
👍
بهترین و بالاترین ضرائب بازی
💱
😀
تا
🔤
🔤
🔢
شرط رایگان در صورت ناموفق بودن شرط بر روی تیم محبوبتان
🍀
✅
با بیش از
🔤
🔤
🔤
آپشن شرطبندی
🧲
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
💰
R23
🌎
ورود به سایت
👇
🔗
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
📲
کانال رسمی ما در تلگرام
👇
⭐️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83375" target="_blank">📅 11:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اگه گفتید الان چی میچسبه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83374" target="_blank">📅 07:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83373">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگه گفتید الان چی میچسبه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83373" target="_blank">📅 06:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obdVvwwZa8S3YZ6pus2yjrEE9-m5CNEkg5Q4XzObejF74LacmS3sIQXhxpSJUmttrDZrYRCqZNDo1WcZP_uiNXmLrQrijh61Bcm226pTQ4Mrd-CRG-y3lUBtsrX8dQcgytIeiETwToPKljRfYFqWmgFFBZ0-NBJKKY0pdg4d6FcsOFD7qvn5l1zZ6QMtSH3HNtfOeHLRLncWPXFXQh1jYoK8kgPEmMMjXIotwlXVCAGtiVG1MRVGhiCVL5ZAkcHMvYlon22WyUOp_Ala4KHLmC4Gr5kLIrnnsNlVwt4xwNqoGfy5gc_VUvlt4ZIo8F0r8BzF009aRMVyvKbpl0Sg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، همستر با سیزن جدیدش برگشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83372" target="_blank">📅 02:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83371">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Daf Zadam Roye Daf</div>
  <div class="tg-doc-extra">@vantaproducer</div>
</div>
<a href="https://t.me/funhiphop/83371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تنها حالتی که علی گرامی میتونه قابل تحمل بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83371" target="_blank">📅 02:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83370">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پرتاب موشک از سیریک به سمت دریا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83370" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83369">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امروز ترامپ نگفته ایران نباید سلاح هسته ای داشته باشه احساس میکنم یچیزی کمه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83369" target="_blank">📅 23:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شلتون یجوری افسردس انگار ایرانیه، خودتو جمع کن بابا کون بچه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83367" target="_blank">📅 22:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۱۸پرومکس قراره تو ایران تو محدوده ۹۰۰ میلیون قیمت گذاری شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83366" target="_blank">📅 22:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5wQHZSX8_8vAoCcF6zsLsQPylxWfnwoOUxpqYKe346MmMSxpvxVgbvVUBtQLGFhqOPYIN5z_dQF1XdF1hKndOsablGIQ0REqPz0oXQF6jlTYoS3_4iKlSUrV2hAaADTtyguUMXwDHMYK68Xp0ca9gdUdW4LaMV2EjOIrOcxmPNobDXUbI1GLj95O3aGwGW7g05vGAslF-x7c1Ru5sEnHj8GR99Mt5cX-nLov_b50Y2u93P1YzGLsV-iryyYGK0q--pOqk5NzD8NHhMpkWtiiXYkETefukWs4HJIszVeAcV1C-tQLrbcQn_YBMZuQEfWqRURoQryV6YfLvXKhT9a2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83365" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برید بشینید مسابقه شلتون و زورف رو ببینید خداست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83364" target="_blank">📅 22:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🩸
BloodVPN | اتصال سریع و پایدار  مختلف
💰
قیمت سرویس‌ها:
♾️
نامحدود | 320,000 تومان
💾
گیگی | هر 1GB فقط 8,000 تومان
🔥
حتی اگه 1000 گیگ هم مصرف کنید، سرویس نامحدودتون تموم نمی‌شه!
🎮
مخصوص گیمرها با پینگ مناسب و اتصال پایدار
⚡
سرعت بالا، بدون محدودیت حجم…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83363" target="_blank">📅 22:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloodVPN🗿</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWsEAyr6edFze2L9rmkb7Y01UPj-JNYZUxpeh-IxYeRRxxBpNfkyA2xB2a-jrl5Ne5RgSxAtogLSOrq7NIzv7yJMalIfPrP2WN9jFSGKLT2wga2nlyg5OmaqP3_3Sg6-F00fwqYpZT4GEE3f7laZ1ogP4LwYHmjcageImr8Ur-f6BbXtYrQvZMe_EBy2FMm3gmXYUEO2wSUZeu1pSeAta-xv39nuB2fIF3pxGiN8Zz4o2j7nwB81MWg5U8YibIiByY77gAMazRhrPlRtHTmfVlWn5HVWqJr63tnEozcA0E1kX5ziRSvCC2sxjZzRKTMG9F-9H78StcIBF7lquuuEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩸
BloodVPN | اتصال سریع و پایدار
مختلف
💰
قیمت سرویس‌ها:
♾️
نامحدود | 320,000 تومان
💾
گیگی | هر 1GB فقط 8,000 تومان
🔥
حتی اگه 1000 گیگ هم مصرف کنید، سرویس نامحدودتون تموم نمی‌شه!
🎮
مخصوص گیمرها با
پینگ مناسب و اتصال پایدار
⚡
سرعت بالا، بدون محدودیت حجم
🌐
سرورهای Tunnel از لوکیشن‌های مختلف
📱
مناسب گیم، تلگرام، اینستاگرام و استفاده روزمره
🛡️
پایدار و مطمئن
https://t.me/Bloodpln</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83361" target="_blank">📅 22:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترک جدید پوتک به نام «Honey» منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83360" target="_blank">📅 21:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اگه رپ آمریکا به کیرتون هست، باید بگم که Lil Durk تبرئه شده و قراره آزاد شه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83359" target="_blank">📅 21:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترک جدید پوتک به نام «Honey» منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83358" target="_blank">📅 21:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGKQDFWjtQH4URJYeC1WeN2egbWjxxGc7L-EfwdggzEVUkuV_EZAQLQ7gHprugM9pYPy1Uc6pslfcUEgbqNDq7vJeubMQmd39Y9BSSqlRan47Mvg0kcQdb-6R-y6t4vvVvbGYg9URay7iUcKERdvV2Zd2lvoVm_XVmFT1Z4e6lYF7fe-TpEs18V2B4bo2ZKRf9BEJLTKwqBAuD2XxN9xnXvlUNxsSI-pJeU37VYN2tBBq9JMF_0y30_mjFegTDm-fO21eE7L4UvUHcPtUzYh2RfJmcbSwJyvPJf-Iet-hfuww-dqn2VDjwDWGmbQ7Dx--jvqQ17TS0nUIZrjy082VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوتک به نام «Honey» منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83357" target="_blank">📅 21:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بخدا من با استایل اولدمانی مشکلی ندارم، ولی استایلی که لباساشو قسطی از اسنپ پی خریدی با اسم این استایل در تضاده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83355" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کریم چی زد ۱۰۰ میلیون اومد رو قیمتش</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83354" target="_blank">📅 19:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترشتگن برگرد گارسیا گاییدمون</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83353" target="_blank">📅 19:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c3b572b.mp4?token=Z-OfLVVLQRIQg-xCNP5IYr-i24pgK_RvxMpVQmN1EwbtB5JgFYJYnDHTAwE8RlD73Pb6axdzTA-uCnfzLdy87cOECjgV-MOPMey_gSJVTbgpRi7WiS-ImNYO3MmUGpwRSph6oJJrah7J8cr0jT5wxwIvW_VPRW5vnrTkMnyh2hPrSBLGDhWyQSIXrF8lArt_Aj5Xl9hPwWNyz8ju32_qrNJEkztk28RsIBdDo4vGWVAJ5fUl4Sy474cwWN-ky-FgrR0D1AtqJLnYo-SGWX51Xp4B3pxyqlY97dm3KCiAGVBI0xbcgc_bKCD2j7bVM7lax7iKYAAYf422-axWUNMrog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c3b572b.mp4?token=Z-OfLVVLQRIQg-xCNP5IYr-i24pgK_RvxMpVQmN1EwbtB5JgFYJYnDHTAwE8RlD73Pb6axdzTA-uCnfzLdy87cOECjgV-MOPMey_gSJVTbgpRi7WiS-ImNYO3MmUGpwRSph6oJJrah7J8cr0jT5wxwIvW_VPRW5vnrTkMnyh2hPrSBLGDhWyQSIXrF8lArt_Aj5Xl9hPwWNyz8ju32_qrNJEkztk28RsIBdDo4vGWVAJ5fUl4Sy474cwWN-ky-FgrR0D1AtqJLnYo-SGWX51Xp4B3pxyqlY97dm3KCiAGVBI0xbcgc_bKCD2j7bVM7lax7iKYAAYf422-axWUNMrog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای یوسف تیموریه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83352" target="_blank">📅 18:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65680f7b4.mp4?token=X4KNOOZ6X2YGrviNvXUZ-DoQtWZ5sqZbpzRmmq0oRDqASowKZFZG7YYOFQpdEoBUOLIux6e0OtO2zANYrVIisFY3wQlyvxFK0gT8oKXUMcZX0futOOIJEAI9SieMzSv5RqoDPE-oSVyYjjtls238lhJyS5EBjuUMYRcWtqEune4Jdj07gC7IRq9Zmo0qEUllMTAwvmd8Lr9t5CQmOVi9Jd54_kY-ozzjBHdTrnXU7pDlqEDCpO8pnPCTsas7cV7uW4kHgLi41kM_Z13DJfCwvlr9WqmjGBBPQ968teudMnpmSMBbZc3W6c7WRRDnetyAdy7-GU6htt02fFF-Km5cng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65680f7b4.mp4?token=X4KNOOZ6X2YGrviNvXUZ-DoQtWZ5sqZbpzRmmq0oRDqASowKZFZG7YYOFQpdEoBUOLIux6e0OtO2zANYrVIisFY3wQlyvxFK0gT8oKXUMcZX0futOOIJEAI9SieMzSv5RqoDPE-oSVyYjjtls238lhJyS5EBjuUMYRcWtqEune4Jdj07gC7IRq9Zmo0qEUllMTAwvmd8Lr9t5CQmOVi9Jd54_kY-ozzjBHdTrnXU7pDlqEDCpO8pnPCTsas7cV7uW4kHgLi41kM_Z13DJfCwvlr9WqmjGBBPQ968teudMnpmSMBbZc3W6c7WRRDnetyAdy7-GU6htt02fFF-Km5cng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای یوسف تیموریه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83351" target="_blank">📅 18:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UBjEzlWt3adYhvRjMAJ3m1TneI79d4KEy0DgGwh1icSuqIBVujDArMqmeHeMpYTmW-u3vhQyaYHezpKvbNPxjeDe5gZXqVkzvWOBnymd2ZuIHS8fsNb766S4iFgzXUrocp_KGQZkpD4EOMOyhxU4vZ2wDi2OxuZ2K0FBwi6NwjdCd0rPoco7ff3s_nEqEUc93XnwS1pf3jtoTKmSYX3zdWCCy0M37e5A6qvfhbjCZi_ZPm4WG6UYg9OvKTShOzPrzfsuFtvnEKEWR_Ewgul8OEe-kd3b8yDlQn_YCRwq1eRM2wwGthvu3WLbk2DjVDdigb40p31B2RjN-kOVXvN1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UBjEzlWt3adYhvRjMAJ3m1TneI79d4KEy0DgGwh1icSuqIBVujDArMqmeHeMpYTmW-u3vhQyaYHezpKvbNPxjeDe5gZXqVkzvWOBnymd2ZuIHS8fsNb766S4iFgzXUrocp_KGQZkpD4EOMOyhxU4vZ2wDi2OxuZ2K0FBwi6NwjdCd0rPoco7ff3s_nEqEUc93XnwS1pf3jtoTKmSYX3zdWCCy0M37e5A6qvfhbjCZi_ZPm4WG6UYg9OvKTShOzPrzfsuFtvnEKEWR_Ewgul8OEe-kd3b8yDlQn_YCRwq1eRM2wwGthvu3WLbk2DjVDdigb40p31B2RjN-kOVXvN1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g22
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83350" target="_blank">📅 18:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-ykell49goxPBdL5q9saaYN9bYFDO741w7pmQZ7bZtVZXqjsH_vR2fhoFM_h6JNmUAQZsUlYOPldjgY4EsX4Fsi_fCEL7O1ukUKOyNFyX8Q8SYIxmwifjcnYO9H1CXGh5g2feigoHlH5iyAkEpesE_7_YdkQ1Y9QDJQHRwsngwEEPIBM8esgm5MptXxFLvcUT6xKD5V_oehKs5ieHScy5jN8Qk62B1Cq2Fzd2nE6pEp-L9pNC5RyjQRmdTkq9owNGG25wDPkFRM5IpFnuvbdf2l6x3hUeBRh92tdXzzIhXDGl1WzdQ06gccX5KJlYL0oDTpze3SY0LPXbA4se8Nyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
مجتبی خامنه‌ای تو چند وقت گذشته بین یه دو راهی بزرگ گیر کرده و سرو نه یعنی ذهنشون به شدت درگیر و مشغوله چون وحیدی می‌گه بیا کل منطقه رو بفرستیم هوا آمریکا تسلیم می‌شه ولی پزشکیان می‌گه یکم اوضاع خوب نیست بیا مذاکره بازی لطفا و حضرت آقا برا همین نمی‌تونن بین این دو راهی تصمیم بگیرن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83349" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قوه قضائيه :
علیه عوامل برنامه «با ضیا» و مهمانان آن اعلام جرم شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83348" target="_blank">📅 18:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=JEyRc1pkXKEOs0Y_SjXyOS-cwSbiyn0HrOZh8IDBWiiLWhF_IwNCG77SgV7I2z1QzzLpgvnSClSfM7ugncbLIQjhtzZz5PGKgkJgfmJbohOf827KrgD0i7GZL9JKX7gE-na_-XxHonEc4eQqYGHMXiuIIzFHydPC1XjBdtmcVxlOlSyZ8ZZqqY-h7QoG0QUyiCxlA1r3ecqXPtxuHtNDHaG0skwFXhceVulVFduCQaEyx9F2uSoSylhYhZZHWlNwOrn9jCwEcTY3oPbwnOVDes3t2RCbg3cgo3BB773sgdvcvhYAx4kqze9N4NoWQIIqkNlam-YVLjD5_p543EO2UH0D_ic6saNzQYLJZKlgjARRvHYm90f9enygxsyOy_7lX2JBjr8aul7zp65eXObP4-EqUT9TAMgfrcarCEk9Satia2bopBkpBAfokVzjMk4YhIXmihOcRIL6hIvA7ZvO1pbvGVtfdCwrRPOT_UKiU14F8vhHrSYwbqRoGH0c3hJ5SIiXtUQJDxvTqRcJoh_7rrS6ueL064YBCMupjrYG9sT-n0uh0nHStOZ9x6C1NMxowxMvNDl2NEFRS014W_9AO-Z0_MVCo7L45dMm_gbl6SHG9KqI4qiorSGiOn8nVqqTgSuFvTci3i9Q5s2hzpafqOUvJ2VQSCl7Oyn6UkwT6zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=JEyRc1pkXKEOs0Y_SjXyOS-cwSbiyn0HrOZh8IDBWiiLWhF_IwNCG77SgV7I2z1QzzLpgvnSClSfM7ugncbLIQjhtzZz5PGKgkJgfmJbohOf827KrgD0i7GZL9JKX7gE-na_-XxHonEc4eQqYGHMXiuIIzFHydPC1XjBdtmcVxlOlSyZ8ZZqqY-h7QoG0QUyiCxlA1r3ecqXPtxuHtNDHaG0skwFXhceVulVFduCQaEyx9F2uSoSylhYhZZHWlNwOrn9jCwEcTY3oPbwnOVDes3t2RCbg3cgo3BB773sgdvcvhYAx4kqze9N4NoWQIIqkNlam-YVLjD5_p543EO2UH0D_ic6saNzQYLJZKlgjARRvHYm90f9enygxsyOy_7lX2JBjr8aul7zp65eXObP4-EqUT9TAMgfrcarCEk9Satia2bopBkpBAfokVzjMk4YhIXmihOcRIL6hIvA7ZvO1pbvGVtfdCwrRPOT_UKiU14F8vhHrSYwbqRoGH0c3hJ5SIiXtUQJDxvTqRcJoh_7rrS6ueL064YBCMupjrYG9sT-n0uh0nHStOZ9x6C1NMxowxMvNDl2NEFRS014W_9AO-Z0_MVCo7L45dMm_gbl6SHG9KqI4qiorSGiOn8nVqqTgSuFvTci3i9Q5s2hzpafqOUvJ2VQSCl7Oyn6UkwT6zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوباره شروع کردی که شیر
ترامپ:
ایران با شدت بسیار زیادی مشتاق به دستیابی به یک توافق است. آن‌ها مدام و بدون توقف تماس می‌گیرند.
من توافقی را که سودمند نباشد، نخواهم بست.
ما باید توافقی درست را به دست آوریم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83347" target="_blank">📅 18:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=npOlky6I_SbzdqrsCymwC3ENnMo6KKYzeHImm-r-Kk1-r6REJSDo2VKOTJBvHhK2UYMNPaVFTixeXXa1b0DplEfj35_I68a2y_4N61nLrYlAWHHBeLX58Pit95iJmMM5c3lRWIBVgetnX8mEFRR19wzrOIpyN2pjp06-a7SHkU2EOf0CcDTrkFQ_n-kJzV6yKsgUqcdi14NSg4oAUMDYhwB2cH43Agr_8eEdfs8xwuBt0KU3TaZdBty69mbmtfc3N1L9Vsuphas2i8vxqqncZ5s2oWLUJ_IGig7oSuIrmYD9zBIy2gZPmVyciETrJTGVgTsS_JdPM0IM6Ip_Z_Uzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=npOlky6I_SbzdqrsCymwC3ENnMo6KKYzeHImm-r-Kk1-r6REJSDo2VKOTJBvHhK2UYMNPaVFTixeXXa1b0DplEfj35_I68a2y_4N61nLrYlAWHHBeLX58Pit95iJmMM5c3lRWIBVgetnX8mEFRR19wzrOIpyN2pjp06-a7SHkU2EOf0CcDTrkFQ_n-kJzV6yKsgUqcdi14NSg4oAUMDYhwB2cH43Agr_8eEdfs8xwuBt0KU3TaZdBty69mbmtfc3N1L9Vsuphas2i8vxqqncZ5s2oWLUJ_IGig7oSuIrmYD9zBIy2gZPmVyciETrJTGVgTsS_JdPM0IM6Ip_Z_Uzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش کانسلو که کون خودشو پاره کرد برگرده بارسا و الان نیمکت نشین یه کون بچه ۱۸ ساله شده و طرف هر بازی میگاد:</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83346" target="_blank">📅 17:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پوری دوساله داره آلبوم تمساحو هایپ میکنه، کاش بعد ریلیز باز چارتا دیس بخوره فلاپ شه مثل فیل بخندیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83345" target="_blank">📅 17:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترکوندی شیر باهوش
مدیر سامانه هوشمند سوخت:
خودروهای نو شماره بالای یک میلیارد تومان مشمول بنزین ۳ و ۵ هزار تومانی نمی‌شوند و تنها ۱۱۰ لیتر بنزین با نرخ ۱۰ هزارتومان در کارت سوختشان شارژ می‌شود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83344" target="_blank">📅 16:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83343">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83343" target="_blank">📅 16:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83342">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83342" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83341">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83341" target="_blank">📅 16:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSYqU1Nr7orDQ0qh9h6VhY6MTz3dOlmxGJ2J1jY3rIyQdQ_pwfxUO0OaJ2Yqo4c2UEviWw74HzsMIoKN5noyDNw2nAKqHzfkVXNro9otHaEmtB69lVDywOiKI_-_rAvpjB6uatUvZcPSa72ysGkD0KWLYiPGITahepj3XntkSDlUW174eFGv8iNXlQ-mCuMk28rTRfxjBSy1TkKyK65c-Reb0ztyn9VXr86ZnFySQLbtXLLmLR7fTFFWS1SuJfLl-VjftxFWFhj1IG5H4IisL8DUTorDHL2fBxFdytQ3Yo5gXq2CLEaUxh-8RExquzbWETIgU5a4IIW8M1wo2oqL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83340" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چرا بس نمیکنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83339" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dws9bRWGJmmvn8SNvOmYpo6IIXwBKd-ZaR9t8MOyKfEWpmvY2zKcHmJRp6P2HgKy8eRg3TvPqGZ7J3AbArDaLZdqh4WznbhU-1VKzFzMv4EX1iz1ZXoOfK278_wV52gk6GUgx_bJS48B7NxdlN7OVG75VAkh1jInGnFJqIkvV9jyMM7vTuMyjqmmHDrrk_uxZBbyLs1yQVN4dbpzbTQ7MUXXgVcOjzgkSUumWOsN8DQYBdnZOYyl3-W5qnuFL1aNSWNDMXIryeZiR3KJWdNLAYfPC8hHC9RpijgumK0WXFfTO3aO7_MxxrskIvOmnVJNz1xQ9l4IacN4H3GI3J9Shw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا بس نمیکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83338" target="_blank">📅 15:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAkpUMl4HUXGTxLwTBrAt2PQm96klYMk7e168hRiS5YjkNvD8Zo166Pt05QcsPzyHUbfGVdqbQL1AV5XFxpDE5PPdPhSXNEoYN1Ff0ETIoJFgWmKb255yj6DmaNMxIHg9dfyV44JG415KS4evChUPhtS5-WFyy2O3v03FHrM8yK5ubofhnjNI7aRN5DEzk1jm8VoBLW_ahYVbbOphZBNCf2ytlozwv1YGQeZAB84JskuhBsXhqJ9Nkhl7BIx8pDetMxIEJL98QWSj_YZ0nuFLudRVqlkF-Nv_Co8KBtO0A4vRHGKdQZXIlpom3-6vUHB30FpvZDRQb1a68s2HDHNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم حالم خوب بود تا نوتیف اومد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83337" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83336">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این یارو کیکستی چرا اینطوریه، میدونی داره چرت و پرت میخونه ولی کیف میده گوش دادنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83336" target="_blank">📅 15:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxA_nY7Wt8BnLZSBnfhYVgjE3iz9tIk-_qEemtsq8WbfmFDzeHO-u3T1IItjoNrtLUdPX9RGcb3n7bFW_MP8aSroK5wej5s46qBBuaICij6hlkRCjal1tQZCr4756IcNv2bqLFQqNQvWDrlpqP-lM_MW4r1su3ZOF1sgb-NYsr7r5PmYDNS20tmNeaqIa7tyXJdzOcP89J_mIg8T_AZy4WMQH7sa7meK7bHwF-dKVWqQlE8Ubn-mgLQDfu8yhPDk98eqHrGndWk3wgEvhJ52EvCZaIUZlmql_-n-MMW6uXsuXNH8IK8IA4-ZyoYxSrH9GX-W-KSvj_PCLhjhMS594g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83335" target="_blank">📅 15:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وضعیت والیبال ایران هم جالبه در نوع خودش، همه میدونیم کیریه، ولی نمیخواییم قبول کنیم کیریه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83334" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjdS96Rw-0pz6MPtaqYzZOIcmmDHwLP1TNppxhF8gZ5YmA_XkBNJKLAaTtSVcEnUbvgURQjIElZxZj90vs_bSTBzsXD0C-JZa22EgZZ1aYAAWwqhxJPCheUhtQnE2SEwc1pZnsihn1A67SigEyG02PJrat_DjB8C0C24cu2FZMgfoOi5A9PM9B-8fzMH_efiIZkxUWZzbUo-vOUnv9wnc5uOQ4q1Y1wsjBwvz6rgLl1IzA96WyzDwoHMQPauNptWalEQn8FQMPLmmai8S3IFfUBFwDFtvLdT7E_4_c8_332VxM8WWC1qjRsBUGV28c1s6g2V8i-KwSQnJ06dQjN1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکیو اینو گذاشته چنلش پایینشم نوشته:  "نسلی که از زندگی خسته میشود، به فراموشی پناه میبرد."  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83333" target="_blank">📅 14:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83332">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c040dfe7.mp4?token=CUO9GcjuGbMTAq0RlFFkvx4YoYQO-D1Gk6fNBZ8Mg0j05Dhknkl_iczC7yX8fumWCB5l7tw3GJyZUBamDzwPABj71bgR5U8M7PAlud_s_pwuXkOqEqAC_GaP6g-mhWU6N16LwKtDD6jkmQJMTSdRBQDrMbWULCHOS3yP3_xn8kLXx5bGA83HkXGCCVFCX788gZ7bqf0we_IOUx_zVzrC4jxfbXkuLRGXgmcQwW7xGkme9d3HoiDstVVPWRwar0UZm9NtnCbAtHVP3PeY7vEVHTB7MFU9hUJ_W0fCwaXCnOpc-S5v9px4pFRdwvjzKZxXOxrx1poylHBoI6wRJ9PYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c040dfe7.mp4?token=CUO9GcjuGbMTAq0RlFFkvx4YoYQO-D1Gk6fNBZ8Mg0j05Dhknkl_iczC7yX8fumWCB5l7tw3GJyZUBamDzwPABj71bgR5U8M7PAlud_s_pwuXkOqEqAC_GaP6g-mhWU6N16LwKtDD6jkmQJMTSdRBQDrMbWULCHOS3yP3_xn8kLXx5bGA83HkXGCCVFCX788gZ7bqf0we_IOUx_zVzrC4jxfbXkuLRGXgmcQwW7xGkme9d3HoiDstVVPWRwar0UZm9NtnCbAtHVP3PeY7vEVHTB7MFU9hUJ_W0fCwaXCnOpc-S5v9px4pFRdwvjzKZxXOxrx1poylHBoI6wRJ9PYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکیو اینو گذاشته چنلش پایینشم نوشته:
"نسلی که از زندگی خسته میشود، به فراموشی پناه میبرد."
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83332" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83331">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وضعیت والیبال ایران هم جالبه در نوع خودش، همه میدونیم کیریه، ولی نمیخواییم قبول کنیم کیریه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83331" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83330">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اجرای قبرستون هیپ هاپ پیشرو تو کنسرتش از دید مخاطبا  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83330" target="_blank">📅 13:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83329">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71116434dc.mp4?token=ZAzRmMFGe0FJsoAWWQBwmFDf9auV0bpJtQPhulD4yTlnrIqzca7w-LCc2M160um9d7pk2Aqlc3L6A8qwIOGopuQrCnyEGo60jLc5SmG-crAwQmptpWOXAoI9AO0WLFQj6Cqxzy79TmBmoSd9k8KHTl_QXpeSIRrUCrRgTf5cZsxker4VCL7GcuOGk6AT3qJy3n5SeLbm7ppEZcos0q_IQad6tQrqCYxOqIrR5-nY6MavXZbsGKSrqCaAs1ehg-3aaHCxx7-wfmd6kNAB_YcDQ6Wht40pWbtzMOHyxETXfyQS3MXGgpCUTSxwbFPkBa2bKreCBwgkMW42K133B-euyQZYPp-8PmYmAzQwmvoMN2AI16MKBnociDUo-gHVKmbZ4cmD4m1tccCFKWUj2kX-2QHGUkPruxayjt9WjTe9lw2fRNwbxD-rrP5kAEBoaOQpWUw3HgLxnR3YiPDFIlc_JK2uQLr0MLJy_ls4UM0XCg6pgvz4pP8nnPyFHMT1QBie3_ri8y47nbuISK49wLeFIb6hIgiALIUw3bicw73rWWXjhmlZ_lKNEwRrTaik616-do-vKd11Ep28gXMNFZSZomXDfKhcopk_UJEmgPlF4lPC8W-NyFc1WtRnu2VScsmxV_oRb0VCC7WBQ31f5dnhh7dZmFSC3iOiCLFyo5r_anc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71116434dc.mp4?token=ZAzRmMFGe0FJsoAWWQBwmFDf9auV0bpJtQPhulD4yTlnrIqzca7w-LCc2M160um9d7pk2Aqlc3L6A8qwIOGopuQrCnyEGo60jLc5SmG-crAwQmptpWOXAoI9AO0WLFQj6Cqxzy79TmBmoSd9k8KHTl_QXpeSIRrUCrRgTf5cZsxker4VCL7GcuOGk6AT3qJy3n5SeLbm7ppEZcos0q_IQad6tQrqCYxOqIrR5-nY6MavXZbsGKSrqCaAs1ehg-3aaHCxx7-wfmd6kNAB_YcDQ6Wht40pWbtzMOHyxETXfyQS3MXGgpCUTSxwbFPkBa2bKreCBwgkMW42K133B-euyQZYPp-8PmYmAzQwmvoMN2AI16MKBnociDUo-gHVKmbZ4cmD4m1tccCFKWUj2kX-2QHGUkPruxayjt9WjTe9lw2fRNwbxD-rrP5kAEBoaOQpWUw3HgLxnR3YiPDFIlc_JK2uQLr0MLJy_ls4UM0XCg6pgvz4pP8nnPyFHMT1QBie3_ri8y47nbuISK49wLeFIb6hIgiALIUw3bicw73rWWXjhmlZ_lKNEwRrTaik616-do-vKd11Ep28gXMNFZSZomXDfKhcopk_UJEmgPlF4lPC8W-NyFc1WtRnu2VScsmxV_oRb0VCC7WBQ31f5dnhh7dZmFSC3iOiCLFyo5r_anc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای قبرستون هیپ هاپ پیشرو تو کنسرتش از دید مخاطبا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83329" target="_blank">📅 13:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83328">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41f1467fa.mp4?token=VHNY7JdSJZndBF7kVBQJchwJ7YP5imPtMU35Lv_9obBhoxjtSH7f--XiClzAW_sfKoEhvMT5_GjWnLMn_cznvbCpefeez27xpBKW0PmumRWYev0aI3qz8J7Sbyv559OxtI-4lBCwJKPxdULlYjpzYakSFTQaUachtzMcAgafa84KU3_sIecCMmmZuAnDan02xuWPgfdJYIxa7ZDDgAYe-1UMD-RHHdQkhoZQF50oW5Od3gq42QUDvEYebhges1zzBd3Nx2JpcQ5Pz5xm9jWANmEamdgHf0V5gny6timKPdvUyHmXUPORe2zyvBB0O5GXxqN-1gsF2bxIXeuU8qqYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41f1467fa.mp4?token=VHNY7JdSJZndBF7kVBQJchwJ7YP5imPtMU35Lv_9obBhoxjtSH7f--XiClzAW_sfKoEhvMT5_GjWnLMn_cznvbCpefeez27xpBKW0PmumRWYev0aI3qz8J7Sbyv559OxtI-4lBCwJKPxdULlYjpzYakSFTQaUachtzMcAgafa84KU3_sIecCMmmZuAnDan02xuWPgfdJYIxa7ZDDgAYe-1UMD-RHHdQkhoZQF50oW5Od3gq42QUDvEYebhges1zzBd3Nx2JpcQ5Pz5xm9jWANmEamdgHf0V5gny6timKPdvUyHmXUPORe2zyvBB0O5GXxqN-1gsF2bxIXeuU8qqYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران داره هر روز ۱۵۰۰ سال نوری میوفته جلو از دنیا
یه پزشک زنان طی گزارشی گفته دختری ۱۳ ساله رو برای ورم شکم به مطب آوردن، اما معاینه نشون داده که او هشت‌ ماهه بارداره و ماه آینده باید زایمان کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83328" target="_blank">📅 12:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فایننشال تایمز: حوثی ها با کمک هوش مصنوعی تونستن موشک بسازن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83327" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de166635f8.mp4?token=hpxT104j7loGZRlFGdM0Tbopyj1kHjyIvUtklpfw0cgcUHtEaklo4pJFLxIswoK6Ho-1HRdpS51V1fdbdFnZHh7XrGI1gZXP9eyuv4b_ckd47fuv31EtDtAN-KvVxQpENAYd-qzNQqVWR0csrevJu0HgYnCK1_ZxE9lGdL7dVmnzHZoS5Z3_ZKB82B1P1qukZ7Xx2pA6OwkYys0V24HIhGPbCxnxpJnJhFzxem_cUu3sMIm7oaQ41vgeiI3TUszG4S0sir2cFI0ntz1_ICUN33Szy0rT760RA29Hj2cTRwpMxXHQrmdwupIVA6ZzR0cHvCrktJ5nd3gOUD4FCgQ_oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de166635f8.mp4?token=hpxT104j7loGZRlFGdM0Tbopyj1kHjyIvUtklpfw0cgcUHtEaklo4pJFLxIswoK6Ho-1HRdpS51V1fdbdFnZHh7XrGI1gZXP9eyuv4b_ckd47fuv31EtDtAN-KvVxQpENAYd-qzNQqVWR0csrevJu0HgYnCK1_ZxE9lGdL7dVmnzHZoS5Z3_ZKB82B1P1qukZ7Xx2pA6OwkYys0V24HIhGPbCxnxpJnJhFzxem_cUu3sMIm7oaQ41vgeiI3TUszG4S0sir2cFI0ntz1_ICUN33Szy0rT760RA29Hj2cTRwpMxXHQrmdwupIVA6ZzR0cHvCrktJ5nd3gOUD4FCgQ_oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی دیشب زئوس به مازندران حمله کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83326" target="_blank">📅 10:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-dG_6YEy-u5QIEmh87KUhvDPLa36cKPqjg7OiLtCVPwFY7fnikYCe5hQEBEhJaz_lQ_-QxOt9LeUHIqKJoIZNKhyIWUSeslLZKZm3BTjRU__I-Sra5lr_X567utlwVPM53ppBGJkGhvaS6OtdCrGuzl2fJgbBOdUKYP0F45bcU91WP6Btv9isLIivajI7-QVoy6VyDjAGOkmS7H7qslxxIltF6oSPymb9JrNBSh590jBbt4gYJEUOXpFnj9R1f0gojoA8V-h5F2bmbiopw2o3ddBH-oQFiwkzWyWRIJHAaLDdz5m7C3hnnBTVGzdnjtBAlNvJ36gJMLR3fWgvuMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه حملات پهپادی به عربستان رو محکوم کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83325" target="_blank">📅 10:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig9kntbvbZvuupV0SVJXW_aHxRph78zYyUTlIYjZt96QjCoL82G-I5vv4cKzCb_zUaBCZr9tEbFXKZJfO4nzhHFeE0raHlW0B5KP4w9VTeXP8Vc7L6dwJ2dKbGjRkQ0gcd9jtOWWRGFjjTH2HmBEZn4Q3h2-d0FIae2keZGDn8XUhLLWWLs2hI6XfhN00L083IkOp9MACkwSLEWRcpopMq5w_Sz5njITLCPjItH1YGLF9eSapjvePA7lWbKpP7nC47z_Q8GN7PrihLfZc7QNvN4ORTayYzuBepgedH6c8Muva177_eY0VwY4bGzsbByqnCgr8g8Z3rFhKBe6shcPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا تا چند ساعت دیگه مجبوریم یه چیزایی گوش کنیم که دلمون نمیخواد دوستان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83324" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmRhZxhdN9HrsaGv8AW-emm86UB3YsDP8Yql-84xCkV8OdsgjTAdHohtkcNO-HWqMo-tBWnjMYdRsyedzeXedSIZEjehocIQty45f6XOgm6ECa9sodz9JiOy-nDHjyyzeyg9ZVz1XoGokITFD7rkQv-U7BjhsblolX2ed3Ffccl08mQziROOYzc3tqoS9CejL1ykdwBLVb989eicV6wDE9YGU8xzgN1TAGoCb32XM8OcmF7by13ESUVghxTn_MdNE12Qc5l1tTLhrjBFx3de2hKfZUVF3kOcedsd6l1OVfsYs-KSUDZ6lBZuUO1voezahMKqTGuO3foRwFvUzmSKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
منچستر سیتی
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 -
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر یونایتد
🏆
لیگ برتر انگلیس
⚽️
🕔
ساعت ۱۹:۰۰
📍
ورزشگاه اتحاد
✅
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی
💥
دو غول شهر منچستر در یک دیدار حساس و تماشایی مقابل هم قرار می‌گیرند!
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر سیتی؛ مدعی همیشگی قهرمانی با سبک بازی هجومی و ستاره‌های بزرگ
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر یونایتد؛ شیاطین سرخ با انگیزه بالا برای یک پیروزی مهم در دربی
🎯
انواع آپشن‌های پیش‌بینی مسابقه
📊
ضرایب متنوع برای انتخاب‌های مختلف
🔥
هیجان دربی منچستر را از دست نده!
🌹
کازینو رامسر؛ جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
R22
🅰
🗣️
@C_ramsar</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83323" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83322" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=AaxJjl22mVYN05vjwVQ3n0k1abdFhKzISMJIz30VYoOfgNbwbI-89NqKM_C2CrTTthlKs24y1TvSwmEOaV6ygZIQUwPxIVqU9Vgms-i1OLrOaRpgzN_-MQnStzwr4WQZuhjUYC4hHnr0ndMVco1GpC2Kfz4VTaLYOcsLKi5_sHN5JJFQ3lYRWLfVDJczMs3PwhqtlF5Tffce1jNTSd05IIt1SHJ4JpXz9oJMOUgrITE-WG_x5iCqRCSaDDh4ROOI-jeaLkmhOXNV2pl7EiNeT4vhc7h8E_jXan_zKUc4sV3toE1S_nUhzmMSZrhHqOBXr4l4V29HmZBdWrbvzT1pZXygKs8zSs1oTuB1Gy0-cS_wV7Ec8CYtf_f6hl5gvLN1oBs-gIrYI6R98U_-mVsYBzK1ye-qipvdk0V_fFFl43DBFN9LXZEGJH1CZKIy7M4zef2NalAJv3tRKf6clftGPoCmA6z5HT3kT2QwqVWWaeT_VJNDUlqfv1vo9QOWDXWjAyxJwHMR05j9sw-2iiTSsU9VxdUX6EGRCi_ObOnF8YR4R6Zufwo0enPdUi9Hd7S339uapHBD2Sl67ygg2TW1v5ce-0KhkC_IdaBADSkpOPuR6OUaV2Ib-mO9cc9Ft2e3UhTpocKlBZXfVs0o9pKWYqcAryWde3LXKimn31CIG3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=AaxJjl22mVYN05vjwVQ3n0k1abdFhKzISMJIz30VYoOfgNbwbI-89NqKM_C2CrTTthlKs24y1TvSwmEOaV6ygZIQUwPxIVqU9Vgms-i1OLrOaRpgzN_-MQnStzwr4WQZuhjUYC4hHnr0ndMVco1GpC2Kfz4VTaLYOcsLKi5_sHN5JJFQ3lYRWLfVDJczMs3PwhqtlF5Tffce1jNTSd05IIt1SHJ4JpXz9oJMOUgrITE-WG_x5iCqRCSaDDh4ROOI-jeaLkmhOXNV2pl7EiNeT4vhc7h8E_jXan_zKUc4sV3toE1S_nUhzmMSZrhHqOBXr4l4V29HmZBdWrbvzT1pZXygKs8zSs1oTuB1Gy0-cS_wV7Ec8CYtf_f6hl5gvLN1oBs-gIrYI6R98U_-mVsYBzK1ye-qipvdk0V_fFFl43DBFN9LXZEGJH1CZKIy7M4zef2NalAJv3tRKf6clftGPoCmA6z5HT3kT2QwqVWWaeT_VJNDUlqfv1vo9QOWDXWjAyxJwHMR05j9sw-2iiTSsU9VxdUX6EGRCi_ObOnF8YR4R6Zufwo0enPdUi9Hd7S339uapHBD2Sl67ygg2TW1v5ce-0KhkC_IdaBADSkpOPuR6OUaV2Ib-mO9cc9Ft2e3UhTpocKlBZXfVs0o9pKWYqcAryWde3LXKimn31CIG3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83321" target="_blank">📅 01:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ناموسا این آرسنالو منحل کنید، کیر زده به فوتبال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83320" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83318">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز چنل:
🟢
1.32
🔴
1.26
🟢
1.5
🟢
1.3
🟢
1.34
🟢
1.53
🟢
5.1
🔴
2.4
🟢
1.41
🔄
1.86
🟢
1.54
🔄
2.52
🔴
1.52
🟢
1.58
🟢
1.41
🟢
1.83
🟢
1.4
🔄
1.8
🔴
2.8
🟢
2.32
🟢
1.5
🟢
1.5
🟢
1.925
🔴
2.4
🟢
1.4
🔴
1.4
🟢
2
🟢
2.8
🔴
1.8
۲۰ تا وین
۶ تا لوز
۳ تا ریفاند
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83317">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یعنی تو دنیا کسی خیلی جدی علی گرامی گوش بده و باهاش حال کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83317" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83316">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhSX3W5NIiVBruW5Seiu43FiV3odJy8bl8C6Ki2W2mrt_C_vVRPYtnwQ3O2Jh5ycsopoL4NjgMgyYTcNdd36DW8l-TTobAQABlq6ZU2Lih780btw167VCPDrI0uqpBiWSlb5uvCNCm2vjjR4xPRCj1oY8K_R4DEmKb7s2snHn7gV9LAbcYnXtZCQxVJfDXQbQ-dINLvAcJKDC5lx-p6cMUSwgxEyXm1zY7oz1rw-efh5e6YOi5E7xcope_91Asm8hZ_rVclsNtj75rO1GtcHoCBEmH5fGJIVFGoeGxJaey9ayxu4KC2qJC54Y4Ko79ftcCTAAY8sto7kMMaw6djtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این استوری هایی که از علی کریمی پخش میشه ۹۹ درصدش فیکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83316" target="_blank">📅 21:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83315">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVb_2VRmiW1qokBPVRS6-y99ttmAAFejnNijpCE8snxfJAitz7n8m29TUqafxwGoqNREhWo5jwSnKfnw0jlzDHqMRJ2Hf1AREILeImfl5pLDEgINgci87qqFUxyOLXE1-HJCiBiPP1ZKhdDS03WFNP6ltGhwytrQFC5YpQt1zo4KvaAhT0GBt_oRIk2lBpNi-4dETcwq9Ign2RLSTtznqLTDuvR4JHoND0L2AO47axE5_5kCtyApFuwvSDxB4zVlZ-t_rKGS-ttlzjtCSr3QjAlUjd5bQ4WPNsg_MLGxU9Nbey4WBVPao4bTeevIHX5ytPdRnRdQ6sInCNhRdhXJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83315" target="_blank">📅 20:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83314">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=QaLV5jJRjf1Z9p749BbLk4wn-xWjbcB02D2h5dJ2Iym8G30VwGyUq2dwhS_tabFRoRH2BgeOLXgVpqVcS1DwENDzg3z6Z9MpIS5IaJJbRwpf3MBR8u8ZAUlG4bl3FV5aFb2F6bkXjb1tvZc7gqiQkb6aXilv3xvUQYz057tyA7JN3sTLlgv0fm55jauY8JNnGIt41_NIhxaKMjEvb3epmi3Avohw_RexEo7kKAck8Cx0ansfhQ3V6yjSewC0bCGr7mp2Bltdp8OpdkoqgAFpar4wh7Q5-kfYGf5miiVjMeG6bAZnjHTDo3yAB_U3hQUOmo0IYD-LZ4d2HA8rCTPP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=QaLV5jJRjf1Z9p749BbLk4wn-xWjbcB02D2h5dJ2Iym8G30VwGyUq2dwhS_tabFRoRH2BgeOLXgVpqVcS1DwENDzg3z6Z9MpIS5IaJJbRwpf3MBR8u8ZAUlG4bl3FV5aFb2F6bkXjb1tvZc7gqiQkb6aXilv3xvUQYz057tyA7JN3sTLlgv0fm55jauY8JNnGIt41_NIhxaKMjEvb3epmi3Avohw_RexEo7kKAck8Cx0ansfhQ3V6yjSewC0bCGr7mp2Bltdp8OpdkoqgAFpar4wh7Q5-kfYGf5miiVjMeG6bAZnjHTDo3yAB_U3hQUOmo0IYD-LZ4d2HA8rCTPP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک:
حادثه ۱۱ سپتامبر واقعا وحشتناک بود چون عمه‌م بعد از اون حادثه دیگه نتونست با خیال راحت با حجابش از مترو استفاده کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83314" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83313">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVdDPjhW9ayBkcZp-FI11HknyM-_uqhGnBvteHSxgK6evZY4u9mpLEFSssqzSCUCGl4miq4EvNxg4E8giBM_MzW6bnWhjSvVFOUtH9KikY-pK6X8dN12UIBhAemm0pdcPpRA4GBUVVZjnnGJxU9AodYSHTLhdt7QpXHrkV6ialnNYmI2YBJ_X6E_-IVb28DP6clwius2gAgYncz_4c8ZYLPeW_gjRz_SHGtWqZTsLWnCfBMygogBBIcINa18WMmki5OQdZ7WsOMBCnt67w00_ttu46TGEk7gvYVuZuUrWlap3GSNeTXf9IuFnCA_LR1JFIa0h1HeXpCSomfIS6yDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرو و هیچکس کال کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83313" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e048011808.mp4?token=tsuYKyx5mOH7z4-4EY1q6K_5YATnsC9wF0uLoMGHEXzYSLEmTgY4CJfNV_wF6WBKae_vMKa3D9Kv6eeSnDjjy0vDY3RGaqq-D0gy6rYbqOFzzNjkX5gg8oPNygmnVE8axOmvF3j2Z3Uikmzh9qY__7H5zmpmZpOz76IIXhtjgOFFA66TtYyHqCw1P25iBzAKIOqMy2vaySi2Ltg-nGCTANRIngUWhADIaKdzijW4gAjeFvcDgYkGLXayCh7lOPN-W2d31LloxLKmI3S7bCLHxGz3yoscd6qymsQyWg-n71XopbjTyW-uXqEfrlQlMp15-gkC4g1lkoYNT26BMnYfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e048011808.mp4?token=tsuYKyx5mOH7z4-4EY1q6K_5YATnsC9wF0uLoMGHEXzYSLEmTgY4CJfNV_wF6WBKae_vMKa3D9Kv6eeSnDjjy0vDY3RGaqq-D0gy6rYbqOFzzNjkX5gg8oPNygmnVE8axOmvF3j2Z3Uikmzh9qY__7H5zmpmZpOz76IIXhtjgOFFA66TtYyHqCw1P25iBzAKIOqMy2vaySi2Ltg-nGCTANRIngUWhADIaKdzijW4gAjeFvcDgYkGLXayCh7lOPN-W2d31LloxLKmI3S7bCLHxGz3yoscd6qymsQyWg-n71XopbjTyW-uXqEfrlQlMp15-gkC4g1lkoYNT26BMnYfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چی بود
تو سراوان نیروهای سپاه و مسلحین درگیرن بعد اهالی کوچه دارن تماشا میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83311" target="_blank">📅 18:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu4Hsvshr1UfTh3DUfiUcxsI67trD1Ji3GAYR3OaYbyhNDkfUOe4Fl9XN0oWK4IRTlFbg5nMbzjF_CPZnECarBBgtPfnNVi3v0MKjOKzSQRIAz-Nq9fnFX19flfUcZSlR95CpYGlIdzOlWZuRbAKdcVQ57t-r_N0Gys6MadHPfs7TfSfCX8VRP8SO5qEskW5vn8ZC4a2v4_ntvjegG4ZM4BFRf8Wmo-odDjQdQ1EabYTynXs89OepzVyyrYD-saGnguf15ZJSAVPfFxVpmDWVHHJYLI869ljXoqJX1EdBSpiayAo2BRrKBBiaZeg7j1PG5x_t7Qqv7rjUE5ORQFOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیت مپ این فصل دیومانده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83310" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83309">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AND1qDygyOIhrLEPQpUJPyB3wIhatqobA4vwLT673lUESaIaq5qcioTMQhpb5WJWD4x2I2eAkH4wugE8PMYvQp6Ou0BdUNvaUqtK-SoMtz97muN6rQXXHoLwnJG2Zsu6nLgKMGhao1hwwmWSJHePJWOQqeirYMLmgTYsJQkWXo6Zt4jhX9FNoT0dCQaIocfl5hiM_-8_9nEo_pPTjHjL09qhrQL8XckPn81188l0lPpzDzizMXdk3MVayq5KP5vJ38DoUttTWNwORoZ-WhjomiK5AgicB9ynWJiI75AgIkywx_4gUu_GjxZiHmxQPsPcIkohF6aNc3BCLbuIqsbrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83309" target="_blank">📅 18:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83308">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6yW0Ock3ma5NznwFb-5RiNzFA80FRlDnnvf43JqbXTBTMYvtPPomD0CEovGHJ8PAmZbXjECLujEdwfXxiPD3qyM7wC1rFWyaS9KbESWmOet8G9WRYXfVugAIihKXDEvshytP0LkH05wHWUB67c4iVqTz2vX-cQyyj2ak1HEEq-ojDmjmlfYJrC8UVLHIi9NCvOoFBeJH6_BYhWvC_63SbEpqXKmwe5NmEQbnCuf6Bbv78_rBc9sJw-cb_DIYVb7xdopRaQNsroGsWnDe53t3j6mgrmGWRO_AH74mjU5OrBULvkce5YkqNvQ442--Va_B1FKOjoysenzFf2HGuTVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83308" target="_blank">📅 18:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fEEge2W9BEma7_Bg9R47mRJkGOvKIi5cEPwBXl3VB7kbprO7yRDNffpq_xzsKkev4P9ymJYwYjkBcUZt7TRUxuto3x1k3s6TJTHss1oUS4_cNv9oZODhdXd6ssyV-6UEHqABZ59u2qb1WcvGYYkMqenzxlyfC1NejSRGxrJTZlzCmFeTupP8f4qrCQQGdSy0T6WixDrjXl6zpzd5o8-FhlWETPcAwc3CKXiuiQa-GzNEMw-fDoNFv642WWiBmSR82DkH-PCeAqIeNNYX95Gk4B3HES4UI8n6Cz7LaYwG4xe4nlpwMgedWBTzwYbs6pPTWXQKPvEeFYzvRgHn_HoOZ0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fEEge2W9BEma7_Bg9R47mRJkGOvKIi5cEPwBXl3VB7kbprO7yRDNffpq_xzsKkev4P9ymJYwYjkBcUZt7TRUxuto3x1k3s6TJTHss1oUS4_cNv9oZODhdXd6ssyV-6UEHqABZ59u2qb1WcvGYYkMqenzxlyfC1NejSRGxrJTZlzCmFeTupP8f4qrCQQGdSy0T6WixDrjXl6zpzd5o8-FhlWETPcAwc3CKXiuiQa-GzNEMw-fDoNFv642WWiBmSR82DkH-PCeAqIeNNYX95Gk4B3HES4UI8n6Cz7LaYwG4xe4nlpwMgedWBTzwYbs6pPTWXQKPvEeFYzvRgHn_HoOZ0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله بلاخره یکی فهمید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83307" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83306">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پسر یه بار نشد توییترو باز کنم چهارتا آدم تحصیل کرده و سیاست مدار در حال دعوا کردن سر مسائل سیاسی باهم دیگه باشن، هرچی آرتیستو ورزشکارو بلاگر تاریخ مصرف گذشته اس افتادن به جون هم دارن از طرف ملت باهم جرو بحث میکنن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83306" target="_blank">📅 16:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83305">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f927888.mp4?token=GLq5KlQ43_a001vh1BlmSFBEZWgfRi3OZlNPIeHjoEIYUPFv_Uwf0CuhVHuxSdN6RqgBDR-DGNsfTyKA0lxJ0Df2EVOFzGeUogdddCQMD62nKdG1bvmMvPrfozdbPTKMq_sdIVywt7euSKBAymi-SJfhp260irNKU5aay2ue4CzIoldXz_9LKr16TEiegHz6kiuixDcXb2xlqawQ_4HpOtpIa1R9C4TaWggxllQSsQxNO9JkTrmzWz8vyEVcO4spGD8Y6DnCHngyH8gpmzbPmzMcWgMzxEFgsh_Q9tVKqc5J34yClyf6bqpuwpChddJzsFIqSgMGf3YoS5N3QbsV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f927888.mp4?token=GLq5KlQ43_a001vh1BlmSFBEZWgfRi3OZlNPIeHjoEIYUPFv_Uwf0CuhVHuxSdN6RqgBDR-DGNsfTyKA0lxJ0Df2EVOFzGeUogdddCQMD62nKdG1bvmMvPrfozdbPTKMq_sdIVywt7euSKBAymi-SJfhp260irNKU5aay2ue4CzIoldXz_9LKr16TEiegHz6kiuixDcXb2xlqawQ_4HpOtpIa1R9C4TaWggxllQSsQxNO9JkTrmzWz8vyEVcO4spGD8Y6DnCHngyH8gpmzbPmzMcWgMzxEFgsh_Q9tVKqc5J34yClyf6bqpuwpChddJzsFIqSgMGf3YoS5N3QbsV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی اینارو حاجی
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83305" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83304">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=DySeeLFsI34eGroXjg6QQRwniZ-wZUOsgWn9lBNat7K96fTtToMJjvyjpbZzLcznF55-R4yPLF8BrkF-8WZFPRKMtaoabR7Cz2-FXannM5jnCzfhKR93l49ktMBhgbsGBLjHmvOoIJsmwP9hEij_LbE1oJGlbvEnkxsxharj59l7MqkHQaaPjHDPrinxkmVW76aQ1eFyLXFWNq4INW9bcgYpQXS2sm2r-qSMzQieaQTf7HMiULaY8pvAu9LqkBrVsT9F822AmQLMLDBEm66CA8147aMlHlIBuwt6TS1pgHEZ5DYh4fZ9l29N6fqForLrRG_KzR35cWz-_kb3BrmPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=DySeeLFsI34eGroXjg6QQRwniZ-wZUOsgWn9lBNat7K96fTtToMJjvyjpbZzLcznF55-R4yPLF8BrkF-8WZFPRKMtaoabR7Cz2-FXannM5jnCzfhKR93l49ktMBhgbsGBLjHmvOoIJsmwP9hEij_LbE1oJGlbvEnkxsxharj59l7MqkHQaaPjHDPrinxkmVW76aQ1eFyLXFWNq4INW9bcgYpQXS2sm2r-qSMzQieaQTf7HMiULaY8pvAu9LqkBrVsT9F822AmQLMLDBEm66CA8147aMlHlIBuwt6TS1pgHEZ5DYh4fZ9l29N6fqForLrRG_KzR35cWz-_kb3BrmPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر پیر اومد دست این دختره رو بوس کنه نزاشت بی لیاقت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83304" target="_blank">📅 15:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره حمله به خط لوله نفتی عربستان:
ایران به احتمال زیاد مسئول این حمله است!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83303" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=X4Bzz2xAzO2GOXECqAm1WOfxRQB1kASxtZtQkwVuHML8iC37hkVHOsnUHPy9Uvp-ZDOoaxk_rAg6ZvHz8wC0WvhZONbbpL_VSYGFpZ_DTqSH5OlBKk4-dHAdf2VmliB4peM28GSJIhlpu5i3HZn99CO79RbfctLYniAUhjvLWiayD8KOqjXuGFvXj-rFjsIrUj5caqbUEsKnNdoXPx3mUqwGTLRA_nJ907Nxg0PgJT9Xy0d8pJXK4r19-grakXVSv8qmbnufPK7br65SzUGqyVRYEQmiBatWj_TIkijhonTnRyqTXsYtLnlOuSwzcsk6kiBj8B8_W7e_L8m4-YuKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=X4Bzz2xAzO2GOXECqAm1WOfxRQB1kASxtZtQkwVuHML8iC37hkVHOsnUHPy9Uvp-ZDOoaxk_rAg6ZvHz8wC0WvhZONbbpL_VSYGFpZ_DTqSH5OlBKk4-dHAdf2VmliB4peM28GSJIhlpu5i3HZn99CO79RbfctLYniAUhjvLWiayD8KOqjXuGFvXj-rFjsIrUj5caqbUEsKnNdoXPx3mUqwGTLRA_nJ907Nxg0PgJT9Xy0d8pJXK4r19-grakXVSv8qmbnufPK7br65SzUGqyVRYEQmiBatWj_TIkijhonTnRyqTXsYtLnlOuSwzcsk6kiBj8B8_W7e_L8m4-YuKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چه اکسپلوریه من دارم آخه
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83302" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
