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
<img src="https://cdn4.telesco.pe/file/jQV0XEJScMwG65mE4pqDSE_QZ2ZA4QeUAiANM4FICxPZGOXDdJFQzbDGRkuovz5Kbzr_W2DuPxrYHwSYgQ6FRAhm_vEtwrIXVv87FUBlEKAt8GS1j53El0SB6KFqRBkjqZgxQf8skju9-0ofZ2ccOSTWHnPHiEvrWjR45j8Zb4mtG5IY7j5fNiGdNfXBAZIyUyJL1Miua5__WRIIeM10O10DLYzbuIRNX7MoVxi5Cs5gwR6JTqtmr53AnakK4VS8q_VbAE7iXTXcNcBfLy5ferlPoWwfLV04M8EZLzQR4yW-bVcDFoZN7IWDTKr0dotFMSLec9JG6rFhuEKtjt5DVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 180K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWy5-BW6jwjSp9Nh2iYnm0q8RPnKQSjbstSmJO1uwPXHf1P5s3udI3tqpOwQlmJYwnFjkqaMQL4cczQOHXZ6XRCsM3ceZ2wKuQhsXvLGa3LPorODwrhn3lV6xFDcPzUeh71QJyLau03yNZUVQwK15Ca8rxFbzYoPoZfwLCNvBRbQmVwaf1IKbiNUz9ZMQaYPxFGEkydfhBkdBwNv3hpSxM7NLp0DQV6pU2Lwmk3GP6-mbzChTPkdHxCU5aNB_Y-7GWIkP_AX8BEe8EIvnlBxIkM8cTTAgj1zNw59jiJ1KFFT6qm0CNOstEIgxJOKmxAGCuuzu1Tc-qVbU5DsKNWHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2MnZ416rn7VhHTW7zUWEeiPXJuhLA7qFUsK1XcLo_Ms7WiQHUU0OshzGaND5O1lGcPefY--cdblFwKk79SwoddwcdPKCPdpD45rjKEwIjzHnGgD_VDMAerh9crgKu15zBeMnZXiGTBpI0bFyaLhXnVd7RZHS2lAg5Tecv1BrPCknmkdQ3cshg1FOSgn9wKCM9o5HGL1queP5YMl_aGvceW1mv8EyEo0gSxI9wzfMKtEI4GYVRxgjsUVJlsPF-oL0B6jQyY-w45Th2-o6hbM1aquLq8tMK6Qyi85vQU99KfhnJ5bXXp2grf9P2yR-Giz_JdyU5_S7SB1QyZtWr_UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT-bt18AY3Zi3bLQSrAub6QqldukgNJrSf6VcX1k9VU9FIayCALuVXzAYY-iXZNPTcMQ3HyZ2RVVAcM_bDJqzupVAEKlZUhOi0VX2SV9PnufKXkcD28jrlgFmXYJlFxPsH_AZaWexMuklpQnuKlD8bBiOgrf0w294BetCdmb6OTMX5UzCfmM5JX6fzQvDTrNvHTV3l56YEDfl2njwDcPHNFPIcWk7tK5q7rmjvr56x-NdVvbpomDdU_I-XeUQtOsP-UbourH4gECpETFhai2Ei65ePzeZ1LwPgTSBW4cmI2te2cgdKmKcUIcZX7lpka9PIdkzhxSp6wgMGwpk6u7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=lwKIfK5XZO0ywVcE4iBAtscS9WwiJTH9uzX_OZUZPBTDl8Q8B-0PWlukWkH-ibi1caVnAXy0_TqDhUpx8K2OzNlN2BlIiDr1ZLJBRbDsooNEth_iUpG_Md3RuYsIb89stau7_i6BZlTEekZiCW3oIa3wCJppWt3U3HSr3qgsMkg68A8GUQuMgjW6YBg5j98eOqvqWMzBO7RLajf4FKxyKa6EKIAp98m0pk3wAyC7ZSEm1rDNOAv5Nv0zaYaybovbCGtkdvtf5oSjQqEUvnNWpgNUCgYXua6EPCU6StTjAuJ2eIw7J-0R7p6cYQAZl-8c5zJtuxUV4jAkorcBtHlqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB-O3R4PMHMqBdZAQvaLssK_tWEYp0JoTgX850_dUYYKDWdUyHPa8qKEWpaBW66BOa3h1pWYH324fszfsvBYlnt3EYSgmt0cH67AHpCnyhYn4edg00R9a85lkpi5ENlcdw48ArJN50II-x84rWfon-v4MzE8T8EC7QMa1tH7Y6_7917znK1ojS6JBhTMzuwSsIfbRm9Rwt1bRKmhRhARGYpQ4GyGBS4ediLBkGXniJr5rVyxwwDAuVKMUHI360QTA3y6759NqhRI0g9kJLrE4ebr8um3w9oLfAKxOXYQcddqptgGoWth4l5bOEvcRodc09xTLev0Xge89PfwkU53aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBZfgYbufgyDXGVBqtyLjPD5ksR7mVdF0eL7uZ9-FNmoe-vR3FkAbmYVomu9xjs4Wjhzfr-xeqdceTI0dm3mw9nB3f62BPzAMNRnEiNbHc32Cg5S4aPgAflwcO0teGGt4_FymXQ3tdV8VK1FQtraDHazW4hsNPmEVDyHG-LWfSusy2RZ1Hp0srxuKl2IO8BUOrm8LqJ4r0jaTKU_Yx_a-qNGa-53KJAyyu_9Hol0QzQfDsxdDdD7x9npdJrAPNJ1B31CVUP1om8iQM44dsQSua_QffEL3PGCzK3bcpH5M4eM5x_xMtBAdhlbX57DN_yubNSF8NaLHe51VK9GK73DfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
R4
🅰
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78702" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=Oog6rtFlN7vI2ZQcEl2e84gcD4C2TwGgssZP5RqFMC06v7OzdpTjuQoRX9J0uXr6RWqkwANXJp30f9AteMzeWUIY1F2n-xyW7UVcUjTSjf6C6XgfGrHmg1-b8U0-uCPmxXfUzCoHEVdpdFHPfv51BbJNqv9qQyZ6sXJZKE5H3OI0h2i6L4hiFUC925L7JrE1ri9eOVspTrPG7hXU5D4PVop2uQW9FiuUnXa4HzBMwfTw0Hn8Bl2Sq5OW0K0YmR30TfxdSeYtN6LoRw66KGMvpp5_eoeFIViFIoeO_SoQKhNSixlBrkKzeDZpHBIUdjJSbSJRLjJ6Wm0wZt4sWoj4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=Oog6rtFlN7vI2ZQcEl2e84gcD4C2TwGgssZP5RqFMC06v7OzdpTjuQoRX9J0uXr6RWqkwANXJp30f9AteMzeWUIY1F2n-xyW7UVcUjTSjf6C6XgfGrHmg1-b8U0-uCPmxXfUzCoHEVdpdFHPfv51BbJNqv9qQyZ6sXJZKE5H3OI0h2i6L4hiFUC925L7JrE1ri9eOVspTrPG7hXU5D4PVop2uQW9FiuUnXa4HzBMwfTw0Hn8Bl2Sq5OW0K0YmR30TfxdSeYtN6LoRw66KGMvpp5_eoeFIViFIoeO_SoQKhNSixlBrkKzeDZpHBIUdjJSbSJRLjJ6Wm0wZt4sWoj4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuTY8bQ3CyuwQeX8pFhiZ9OwKlPM4GcmnW9Aydbk3htl07AE5VZdK4ecCSDJFks2hvOr0R8KnknaV5ymuqRB31FMoh3br-l2keECbwVRHko8w3VlJb77X4dJxbQsf2cy4afIdDoUsQtUiyKd4iIvQwbd69ly4L16_pHVyofn-3Un-jSvXWJRqlPKkbEYp7ROrICcCFnImBn-x6mO8U94a9U86xuk5anUhKIcYxPJVRYK_Au0QJJZ2XtK51YyjEX5KbBKdRWHVSpYbqF6pulbqfPw4TXbYZ8sBbegp6ReePLXFvfdC89_lcD5XP8Hx-Gy6S6JHtmTQPsz9qMn4nNMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4uWSmhGohBjj6j6t_AoGq2AcRtgd4Bn1VhLug8kIeAvgyW7FqfXcWROr1SQ3tsduhd7U2_sWjLdIUgNNUW-gXHVrj1y7pUJG7ujOML769MykvCjoTrS8vJuSkfU310UYr2Xh_zlpvWs_owBXTswjjBALzZa3lNaYORZ5WT5PSIaMRdWQw4yY_diuIFmifYbfxo6cnb7tYl7lmA9a1SN5Sud3gJ2hVFmxmwYGiEPj4UX2wAKVlHc0a8fwMcoATOZVOXAz72wUabUaaeN2PYWl3LQ4n9RnsJxC89u6FZELtNAZYEZ8uk4ELonn5Ug9w8Var5Mx6H16p7tQ8vYH20kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 540000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWNy1W2PmqeKauy4b-_Rlj7_bd12NYXP7FUq0PTIfhsoQrC0KtU0598JtaCH5u11uohUqms42ynXWyTrLNxdo7IX67xhXD9TrhJEvob_tyIfT6-A6ciLyMCvhGVN2xPxqRj18J26SIKlawOKL3-Ev7ut7sz897bGgmi-2oe-Q8FexgGNXeKXDYp_lxEp2QHMQWgju05h0iO9NUuJA-bUZ6TDfhpBxnyap3KIB55en1eBX3c0NIRamCND7uJNAMKb1DP7r-ZbPY0O_4_8GPoorFHEC12kQbGlk-WDckBbWLzbnL7LM1OLLRkGG16HMzvGlbjXIAPwqWDnJF4Cvo478Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLsEow-KlVB9cV8zXT89LkmXaG6-q59q6d5XjQeWnISWJKzocSLvuHzoT29bGJKYIg_dGmBT8ypkJf3TOE70Te2VlrFzdsL9BQxrjcrMHQkl7McUSuS14wkceVTZQtmiAbP4bHwcsFkr20IS7y0KqGD9RD7aJkjrGjJrBsZv8aKBevf1QT3VAlun309HYQG2DPWU_cD0hfVDPV9p2xMREsBNqwRl1N2G0px7lF2LJgNm2iqNq-WDqRbuDCDCJ3bLqyDLLbt18JMAg3PpAewx3w7k_hlkfehu0og_7dnkGJDjO0aVV_h0Yiw-wmJQTvEPfCp0wNuB-jyfMwGGVaTOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=qsGUGI9_JdHNiEZRsVXhJ2Ozl1cHOng53sFjmreRSMzW_b6VQ0IhvOqIjeYoi04jH25x7IOjwfVymcBkTJysdPwdboVrHbsifN3j1POgQ0dmX1D4V38hIzVNGleKnBwXvzk3TZjcbf0VbnveJjsvlXZxedqk60FXY9FdYOe4a-VEMYrT3RJrOXyr-zkCtveEHSBRlXxm2l4ukdb--BDEk5qvE3Ss6nnCQZo2oYQvNWttVQG66iHzX_A0Pxp6x-JX1jCi0e9n8SKPCUf60Q23dQ3Rr0GnjwmjumlpDRtLJBUVsdBOivKip9xemG4TAPSND_BGJZPJ5zohVOHOyVs1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=qsGUGI9_JdHNiEZRsVXhJ2Ozl1cHOng53sFjmreRSMzW_b6VQ0IhvOqIjeYoi04jH25x7IOjwfVymcBkTJysdPwdboVrHbsifN3j1POgQ0dmX1D4V38hIzVNGleKnBwXvzk3TZjcbf0VbnveJjsvlXZxedqk60FXY9FdYOe4a-VEMYrT3RJrOXyr-zkCtveEHSBRlXxm2l4ukdb--BDEk5qvE3Ss6nnCQZo2oYQvNWttVQG66iHzX_A0Pxp6x-JX1jCi0e9n8SKPCUf60Q23dQ3Rr0GnjwmjumlpDRtLJBUVsdBOivKip9xemG4TAPSND_BGJZPJ5zohVOHOyVs1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=HF7KxQZ4LVAg6EnE9z2D-iFq1ZHEpR6iqfpS_1b5ppBLWE8jS7MQBwAjHsG1WLtdBoD5FgVbzS-iCxvej1xeVHCsoVzE8qe1Uy-59zBCMLn3bs9O6CTUMRyl6oSum9YCwLNopcSxuYKhi1lXlcJHnmsJ1NX-1OjvLS0EqcZerWkAEKVivr1MrG6YyK9CEsMbkvE37NcPbEWIFUCl4qMnSXMYmLCXs1zDJkxyKWJAOrOlcJCcxP6XExIMzkaKT9l5aUn54_27qwpPD-wIwdAWzIEcX74qwW7uuxWNmF3_y97HU0IHYS2uFv9VuAnOh8ZWQ9Y1UVAFRIPzYy_GAHNDfx0nLI4Nnq-ry4yhLw21pAdOam9ZspcGHJV7waaK9pBlesTAb8yqnEBWc2wAEToYY8iXobTRYbwgyDv4r1p0Pk3tV2_blOqkHAtYMIzr3S9hsF07NNOFv2rJGVZcX0aFu2Y_VbZg5H3LOeU4zbUQLcmAD3XEs86B5EvN1yDZr4PcTJt9Yo4oLnzQXTqQkYntpdYz3SOR4lQkClNDYvhyDwHj14zrxNozGl2CS9NAHj-ywDo-xicAB9kg_YzDyNTbuqmmySVMxtsOwXbLXRaQDyj1-aF9AcM9vGCrQ3M9AEMvt2dKv-zDVtvxDle3M_8g_5Pj4HTDPJL6LSXSjsiDJf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=HF7KxQZ4LVAg6EnE9z2D-iFq1ZHEpR6iqfpS_1b5ppBLWE8jS7MQBwAjHsG1WLtdBoD5FgVbzS-iCxvej1xeVHCsoVzE8qe1Uy-59zBCMLn3bs9O6CTUMRyl6oSum9YCwLNopcSxuYKhi1lXlcJHnmsJ1NX-1OjvLS0EqcZerWkAEKVivr1MrG6YyK9CEsMbkvE37NcPbEWIFUCl4qMnSXMYmLCXs1zDJkxyKWJAOrOlcJCcxP6XExIMzkaKT9l5aUn54_27qwpPD-wIwdAWzIEcX74qwW7uuxWNmF3_y97HU0IHYS2uFv9VuAnOh8ZWQ9Y1UVAFRIPzYy_GAHNDfx0nLI4Nnq-ry4yhLw21pAdOam9ZspcGHJV7waaK9pBlesTAb8yqnEBWc2wAEToYY8iXobTRYbwgyDv4r1p0Pk3tV2_blOqkHAtYMIzr3S9hsF07NNOFv2rJGVZcX0aFu2Y_VbZg5H3LOeU4zbUQLcmAD3XEs86B5EvN1yDZr4PcTJt9Yo4oLnzQXTqQkYntpdYz3SOR4lQkClNDYvhyDwHj14zrxNozGl2CS9NAHj-ywDo-xicAB9kg_YzDyNTbuqmmySVMxtsOwXbLXRaQDyj1-aF9AcM9vGCrQ3M9AEMvt2dKv-zDVtvxDle3M_8g_5Pj4HTDPJL6LSXSjsiDJf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7gqU3ULP2sy-0jSq621mDqLF1zZ_QTWFjXwmruynD1j9HXl6e49RuLfRZuKnmOhCKiAW7BGQCtVZoBPHRS_OhKQPo_WwbOLeXOL_qdYpjFl5YefwoFLzuIZd2BlOGsoJMkzznIyrc7Y5YlVDKv6pFl4DjrZ_9GznBH1aSewWCuVkU0nWmTmPb1ZTCNZBkZtLK4Gwjy5jhPRC-v2TPbZ_kzf2AP5Ek5qQNTTs8jmCoIt9dim2kWLYyhQbTMoa0jrYiL7Owy2d7Eg6QtMMrzi9ZhDTdiKITX_GrseDHoDUnoyhLBmZXz7NeStbs7FUjkytYKW20oRCUPkSOwk4i_CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccjqiSeI4PphVloDoJe9gFWPSLS8fCtwXOhd1WKQJ_-aKhcaTBYAA5Z1CZ3YB_dZ39mLGvCxapFQZ_F3HXz29O7cLuSpNP0wdzAnC8-BkVSQQE0cxIDYCwnxTgoZmQ9LxUPpOUaigda60hNBxSbwzJELXYCkz-BzjnXLKT_OYKUXQjZTLAsc4eQ5kOI5XtutAMSeUMzxf0LklMTt-H_OqTq1qw2NqowizjflEZMmF0iRg8HwQr_NRuLY3uds8dC6lXLGW6tSAXgowuyRhz4Urx5XI2kahhDlhV5mCXDEW0JqeoZR9xp_UyZu6riZnMk9JVxiFa5FcZsVyKjz2BdP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
میلیارد ریال جایزه‌ی تورنومنت  جدید Winro
🥇
تورنومنت‌های هفتگی و ماهانه
وینرو
رو از دست نده
🔥
جوایز شگفت‌انگیز و فوق‌العاده
🎟
⭐
بدون محدودیت تعداد شرکت‌کننده
💳
با مبلغ ورودی دلخواه
🔝
بالاترین بونوس‌ها در سایت وینرو
🎯
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
ضرایب ویژه و رقابتی
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش مسابقات
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
G3
🅰
همین الان وارد شو و در تورنومنت‌های فوق‌العاده‌ی وینرو شرکت کن
🎯
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=jaJyrJvpfRlqz00cmhgPYysG5QshHOKYMYhOft8f-E4pKZjLgwWcD6JSQAFkES17mxJm2833Yo65O17lBS-QzaDBkgaVD3pSBVI_w86C3e9rQzS41EI7N32es0sYaup7DTxDQquqJOs1WcxEMuDCwdLXJ4bjuVjzIR50yXwu1fL7yGNQTyOYTLkeKq8mpXRUyoboI6w5Zm-m0riPOnEGtfSuJOmn053BUCX7ip6fSZhUBtaxNB3ssRc8qsSc5gdSbgGfk28bn3lzYbVPwnkgoPfzR2U-n8TjLhoLnh7mJwJPmxHljxbhL4xUuoXmUGOoWOFMiWDDiYXfUwgN2AkdGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=jaJyrJvpfRlqz00cmhgPYysG5QshHOKYMYhOft8f-E4pKZjLgwWcD6JSQAFkES17mxJm2833Yo65O17lBS-QzaDBkgaVD3pSBVI_w86C3e9rQzS41EI7N32es0sYaup7DTxDQquqJOs1WcxEMuDCwdLXJ4bjuVjzIR50yXwu1fL7yGNQTyOYTLkeKq8mpXRUyoboI6w5Zm-m0riPOnEGtfSuJOmn053BUCX7ip6fSZhUBtaxNB3ssRc8qsSc5gdSbgGfk28bn3lzYbVPwnkgoPfzR2U-n8TjLhoLnh7mJwJPmxHljxbhL4xUuoXmUGOoWOFMiWDDiYXfUwgN2AkdGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Z-hNh4VwVOrwqAtlaTMqChRU-mqsHDYaF50vHnETrbCo1LrFtUSfoH3WU-wepN9c3OMhbSvj3YKVqs90qA7ZnXTMK3k0799zKvFl6zLvxkyXOqYbXI6kQ-jEFwR8WwpI7PPw8RH4e2nrwIPflONUb_Y_xGiWjOFdDJBlzCKj3-fVodwyQHpjVqn9PsTPg7lKjmSrXny-m-ATtLJ34VZY1Cuv84ike_B5hLWHxtBiWUoSYBZgqSGFsQ9pEQA4YcfilC-I4m_LIJf9ZZ-jBY09SgvyJC96plSpvzQttXIuVKAWSn1q3y-X1Lkgo5jLkB8IRhgNehqf5iX2-73naXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b17QOSf4e9R8kGiOHhM1CQknNX5kxlgugswLTHggXsJfkn1XhPBrxQ0vYPgxfVA_dZ_CFQJ9BujCuwNvGZjNtrL1Orpby93Yd7JsnQ8GiglcNbu4XCTmOQFd6NPdc-7xuuRCsz8fLYTA9ajD7MCyJIdwnTpJypwEX-QYfEsN6_yaoOU-I_wwvEgRHO5lrRlyjRua9SPF0cU-_kvBmBeFS_2ZpYLFfHqpQZs9ld3gOA5qY_mLHsTB6ADPapeopiXesQX4XEsj3pV3FwtZSUDBcnk7jwH99-6R08YB8inj6DA-PijUhnYWKdA8F64zoouAzZmOrl9xzJGVi-w-eBRkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzv2sA91U-HtEMVNEB66XaqHZu43mPc9Yqiog0OEtUPQIubWfQqDcDtWi8S6WEqgCrsOAibQ-9PDOb6DBZZbi3wYd6fkSBAJ9_haguNsJVUft36yGsC3I-J7fpHYyvIaNLLremdu1_MgjMOPSobyyuhNXvJK8TesoCuphcsahDPB3oZloxF7aWLZ8f5P-ZaeF4djXrhF5pQ93GjLw7-PMZhWVROsH7niWVSkfhx7jjOrS76wjZk0H5-bRoeQolH6HfG-X-jTSyaRR0iOra-oFJpuaBhXcBc7CoOk0GE-EPW_QHlQs5klM5xfivxEBu4qxrVzDog7xJuJkUy1vbKvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3KR1xVySDSwKaaLi7JqtLTKOQMWUqBiHrcYWLNHi2tJFCuGlu-wPTmUdQIHsi1FIiSvLwPPZgjvB_U_WAEYFUpu4jKoCow9EX0SMIcmST-rV4dLLbmTASUhs5irVw-P2QOgRThmWbHYVhcQHMWprLyWKMzp7WpEa5KF84cZZ4_YBZR1UwJxzQopwYlAoYprV_t3NxbhED9Arw-dW6c96ocQc8KgQx_UpDCUSemI5jO6xpdM9B4PMQdmUGcgFSHoLzdNmogSWU3GxD03P0O-rs8J3LqIRuCchRUjmIvY1sZwlH27tsNiO6I3j1aKCZazXt_z0f5yUC-vsjvMVdTt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOiyUwdVhinGc1d09NnBDzN1moyNeut2YdA_PzWiRfiVT8lqylCj4h0DdnzDmKUSySEeutsxYNBVNI2FhfwVJfskueZKnI6VGIRhKeCoLA9MCgM-cVVw3-1WbsyOyjL5mvtNF5S5Ws_iW3URyLfw_jo2vc_MNXbwitIUEWF0uDxNZB02ikgWxBRhXAbbgjn9JQhqAwoQX-KTHuJ0B7q_KCna_DcB9Sgq1lhxh_vqXFOcAwbIDd7LX7fUz9G8h2RfFjzbMsAadUq7Xb-E42Js0uuzJqExiDmpdStUfuXEYlAbbVl0feIpiv0Q3lguQ0UOTJdMOEMIn381Ec2osKTSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt2u2wq08pPxd6pc0FMDqWvJB7hD8B7wa2fLkIbn4_38G3mgY-4NrqZXKDQoC0oOZXelo2vbVtd6KVNMaDmOsRnzTDUSvC8hfDPTS58TFFw37dEaHb9C3AKiIKJB1WX4A0vr5F-Sh4wvktmvOKeIqEyzDL84zNlP9dNpZSUCoJy10wg-mUQTL6v7Qt3H3hmaawTxpkwPW0psBssUVbCnEg1swrGITIU5_pLYiJHQJvY8bh8bRGC1yeQY46WHDKZFEaX_oKeQ5e_D5RRC2zuYKKc5YWFxmJTCtIJUJpVcE-Gi2FezuipopqRbXU8FB39UisLcO7M-rIxpCrwzQXxkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R3
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-ymcvvlspyfpcabZC_jFakrwYBCsH0FyIriUPiXWjH2kP6QsF-9kx0mhc-4-OYrkUFgq56Bc4Didldwc_9sQOyShr_Gjil1pFmGPQ97iAPG2LKgC0M7p6q--x-fVzHTRaPl_joz2waCXcP3_E458hMTZkWTkVt6tjpR9m2GuV2El_8CoXLBWuFBUihJfeS7qB7q2pNVGtlO52PWhCGWjLWSfXbIUYJWc-1qp-82HDlcDMuQSoCMNadCbaM5jzQdZDkS16uI9J0DPovhaXrNbtD1vH_wBYEpyXhHv1uxlZTmnlq3y-1aT2LETZqEpCmVNdszMNlGH0SEtuN2iZoS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=ebly4E6UKKB6pYDhFn-0Kc5pH25sUHmukjMfkx8f8bov8IKoyyy_DazZOnSw9YWfKoKWSdbkcYbMZR41OnclGwoudslog1_lUVUxJBEcJDpY6Nij8kw-C2oGU4-5cYmTUCOHUVq9YgzoV9bF8HkRKAAVKRGh72lXRvmJqBxkn3YUt_SpxSFUGmmrU2Jf2NJpddGHdfjyvnJcR05M5siNxM7n3vyLET0vafLZVZqptQpCFAD9AazjO4AHWCqaGlIUKJV6XqdViPKAKjiYOo2lUf8Mr2evaJyCq1J1-6yJHK_U66pxBUtRM3f1uu03fhTlWJve8B8Mq9NwSqKG0L53xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=ebly4E6UKKB6pYDhFn-0Kc5pH25sUHmukjMfkx8f8bov8IKoyyy_DazZOnSw9YWfKoKWSdbkcYbMZR41OnclGwoudslog1_lUVUxJBEcJDpY6Nij8kw-C2oGU4-5cYmTUCOHUVq9YgzoV9bF8HkRKAAVKRGh72lXRvmJqBxkn3YUt_SpxSFUGmmrU2Jf2NJpddGHdfjyvnJcR05M5siNxM7n3vyLET0vafLZVZqptQpCFAD9AazjO4AHWCqaGlIUKJV6XqdViPKAKjiYOo2lUf8Mr2evaJyCq1J1-6yJHK_U66pxBUtRM3f1uu03fhTlWJve8B8Mq9NwSqKG0L53xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMhGw0NtemFffQv51oAal32mWl6E4fKe8AAwHsg93Dc5WK5_HYGSD_WEj3zZebpfRUeL2BZ44wAWJ2uwmeG5QebxP1fiLU2r1ncuqujmFWcNLd98NlhtaH_enTgNhV0Vp3ZApWSBlqIHVxVPAWEzQADO9LjG3U6R5zQnsSvryqwGWJYWLU2-kBsYqfKTRHlT871u5xJAPl4Xp9H2h7VmLidczsyuU3n86W0FjQxi39phUUYBLV_3jKlFbthVJlfVs7E9Zf2Ks2tfyjcZRQrdAdLQoTBi91SOXYJF6LtObY43JYMifch0eGg_0sD_D--4lqbWg2Oj-rXtxeMPgFxZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc90ycjLY9KlvGESNwcX-4FC4rhOPdOVM1ro-nbL7f-mYZ9EI88YjKlMpePoGNoi_QIRp6HFS1lXqKAxXWSBoPw_v5rqCyhfpJoUg4-rGKqFyBGooW7Spywd1LqjuWEy7nZI82CuIXQzEOyG2tgvYgDuUbyOQ-s5BR0G6MuzNUwAYaVuDrAJdg9Z-Bj30ENTwgsFoheMvRsSJYTe31ymStu2qeqF90NjJb_950Y49xUmbDzoj9Ft7JJdbbWXxpVEfrRT3IUZWPgKad5tXOcx4JS0x_SUmEFzoJ66q5w3ayZBXX70WvkGZrbjBn46dqSGFv2mcqcltsKov0FYsyAPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW_UEFwp89ymX1VE4Dwv-bAC7TmC7oTRbInC5mBtQ2hapj7mriCZ7a00gDIryy5sE9nXdiYMw83APVH2Zcf5KSNN7bfbF3xbEgJe4wCIvslLCQe03sY7o7Lv1gHI4z8nNDWUJzD7R9huUADW3RTL6cWhHO7Y-QSmNZuZzhkpBtD99OlCKuGUw26y2XCCSJwceH_LJEBJocvnbSJ2MivaAUaPZ-lEfkTRLZ2KOap2bs8uIrtbYF6A-v8l-Q0ETLO9-kSm9hwXJMnzfLucpJtODCzElGWBMKyPkHW-5q7b-H7XBJklGIUke5HKntzm_PORuA6erE9Cxj3CGXzl1aoh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV7vWBP1XUFx4YHzCcWH7lCP3PluGaEUNiRDaplaXbB-pI3Wel_zR6AFN1H1TuJWX4zamDNIwurEAzIACWfUWZ9l1unz9qanRGi2gYYSaI0UcZD2kOnSFrA_w2dOBrhijE4M5CK8qlAJLMlc2zIIKztZUW5bqODMbwIWyPfBzPT0tT7btfDQrr2uSCvdPV__juyc0JS8Bj8gztP-PB0j_-o2H9-CgzEqoezEAMJigCaq2sK7ug0-GgbsrtT6Xc8fLqKZjNV-RMcMcPBFYnu-yLNCPlgORKJDI6M0_ljs_R-BqqGbq_ReUqV7puu1yfGtKGhttorMehR5zgh2OtSCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSYbw34wK9t-jgs_k6emyENvtxwp1ga55RfeWNwYqUVX9UWL9M7PVl0F2dJUm_uSP4KHxPdUPXxd5okaDk8cjoYLkd_kZ6zSbK02-3tWGzSrdCNPkIxqg82YXwz-3A7hsmD6lgfWQ9XZJrR3snjmNDwrRkVo4VCHyaoMi8TKYowSWHhCfIXVBBJ02F2kFwXqI2L44zOK7cMgYRqTwlJmFn8BKMz9GOq_MYVgI9A0Lr36Z7HFkV2T2t-9vS7oDedQHIGsGy3eeOIQK91aiVRCSP_JppK0JD_DGZhs_T7sbYqYp_Ei7qg1deqswVKYSO_tb-zJbjKR2GMrwIgf5gJ3BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=nN-xeVAYm22nXRQ0S8iT6VAoeQf6IDAbbLZb471-YST0qoYxW8BTavd_pDpH8M7h6-Xwp0a-daG2eveNFO_VAFwhBLXrWZwCE7W0j0MtJEho-wvfn4EiR1SLP8wPA9ssjSx8C7gbtN4B37Xn8D7IAt-ofLauV-UaK22zNtCjXUxM6mS2Wsve7mdgX8zG5u1oizyEKBhYjpB5Pjl4XK5oCX3Wixap18aDSaOps5-24uGANU4YAZqgSBPPCqVVIi6rMygCm_oDbTPMs3drAG2q96KKuD8xoiQ3cyhtfDIZATfU6YMDzmzPjOA9mewbO_MqddzC6mEBjvN1-qCh5Ri0qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=nN-xeVAYm22nXRQ0S8iT6VAoeQf6IDAbbLZb471-YST0qoYxW8BTavd_pDpH8M7h6-Xwp0a-daG2eveNFO_VAFwhBLXrWZwCE7W0j0MtJEho-wvfn4EiR1SLP8wPA9ssjSx8C7gbtN4B37Xn8D7IAt-ofLauV-UaK22zNtCjXUxM6mS2Wsve7mdgX8zG5u1oizyEKBhYjpB5Pjl4XK5oCX3Wixap18aDSaOps5-24uGANU4YAZqgSBPPCqVVIi6rMygCm_oDbTPMs3drAG2q96KKuD8xoiQ3cyhtfDIZATfU6YMDzmzPjOA9mewbO_MqddzC6mEBjvN1-qCh5Ri0qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEwccltH042ACllCozEb68qbSxzi37aE7VaVmGKc27j2jSoNpoXiwqMSkYaP4Joy-FloovvWFZIqZWB0AnlkGwUqsIk4ewT1LqI7j3m_0Ikn2sMYZm8kSDcNknmGxLxqJTftReKdvywoz0izMjWIM7xEDjljtCtK43eQIcikl1PdPR21U09ZSOtlGO36gN0tjGM_WMkS_HDuTLbKO2tkRBS-UOjNBh0Wec8jfXvPXHb478F3GBvQHiWaxEJrHn4I6MdwyyDaKbLfyzWViVKVcegeyyBmZ7jLTPhjBkA9sOfcB0dxwiu0LYYPWENyQKyoIxldIVIvfYEhJskCzr4WXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlocUzQkpZvwb8l8cp-gtmpo1Vo2yRGv5BENiH8GQva-JUHeOwyqTIMUS4Wc_JnMYNNUHK_higZDJkHzK8RmQPLpQ9PdjCVjU4n8kr4io0ucBPgJMgpsi-Fjbf-UbZh608_e0ag91V2h3aM004xNrpbToMQcpkTJYDeOEJf04yfqaB6Z6WECtilkgcgAu7t0QpV0A_U0sSizblE-r3OoHqm6zSpBEzgf3a5xcdqsWiopSZMKeffx2nnmLDgqetDFiQ7XkiTfYiM2JVz6pZwb26R-rmmZJsBsZ-n6eyEMdTxpX4UyprNNAOPdz3c2PjEms4c9REoW0_q-JvI5-pA2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seaK_6bSvxuotJELTrrTwJ8UlQiXtuwCvs9w9M9ksLivmlyXoGJwnD_i344uWvcLX94tfpzw5Kwyg7mwQjJ0NgYXyi7d7XVVWE93P0c6mM0GpJows1lQgEQKx-RjXd-0_MioscriJe-5Gaj6CJAVXDoH5hZhhsi3qeqjRbbnKefTeM5n3Zq8WtUA9mbgcfuL_Z0OsjHc8qxWJKuoRFZa43cza2YPkUdVsyZYc7crYfWaFcFd6BqAIuSxiEOFZ5qXqM-CPiGOFowlXEAjATIBeRyRVcZ_9-G2be_zxgfLyalTqy-zxBqZScvaviSo4lVdkOB_a5jNDnaXNes1sH7hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5v6XGMfCqg6WvyGKUbfDE2XHSUlJQ9EiDC1rnxH91LkiaTqU5leTdu8mBx7e8A02xi4vxXbRSmrudxWdsU-WxnMLiG58IC6unDZKDi6U_BHvMFZvPv_IA6DL1ldOQ_7b6tEXyeEGjsg3WCVEGix9DQZE12SHg8NoLmiS5JkZyCkHeRQR_mhL-NYz83YeB24I3czNdRHDgBEkClZ00FpqOquMjCHZnS1VQv2joiJwZdKq3tGklLvfNzKkWdy8nrXRv9XQLSTmvpPcyIWMfNQW60bvhxm-t12iApClzbZueeBS-UrMu2NIBSRsaM7djz5NkdCgfq84ZtyHPjAn8_h3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOmymPCVFml1gzXS0DQhSFEhfUJsUo_bZHs1xpSjp3oYlmsthqcJmeWUTNQbM1zF7fgBdXgbcM1SrCV4tEvh8QasvIOETKKYFQfM3AaaXTnK22jo20IZ_Zgbtge-kjTSpyMHu3Z7-jc5gcaCBmy3g_68fI9NwVWCTGbF95rUHZx5xMgjg-M06I5MKaJAVGDeQLmiVqVTFcGXhaxJrk_-zBiLhOL06oM64hV8Y6WIyngAeQVx3idf4sLH7aJy_AOoxYZCkJct_dNy1djqpY16J2Kz5Vky6XZA2-AGtY_W4ZSpNVg4r4gLFxgGgXO2rLfVSAMnrzUeD6i47THdjFLuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7_1TDZtFQR-gw4ESWeHERlKKS7oeMLoerav6wwYPlsj76cGP7z2jnUpaKwHQCoPy-VByhe8ILXBAxzjq24eXiZ7t2SnH2P7MIgXXV9sxIm3cwGESn16MxCa63pW8uXl0e2svppqNCabTWGZ_4KOobfPrGRIEF299VCwhVJXbA0uAobDOYIFe6yxtkWRnwtw0LJRwfAoyhiA63KEDiyifr7VjaHZLdDsScvgk3aOVcAhaN7EKDsRiAKEp-Ib828QpY0nWEcD2DDUm3Omol4drLdClYO6FHjJzv2sgNroVCNA5_moFsnr5On4gP7ziKYlxutqXG14iUZKiXh8fVT3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNEGurSDbgjuvqLEegYpaoQjMPnQ45Vci1zTXwkBbSXmnHvEl2YhpB7TfbnP2HnTz67ZAdkHCd_Atp49KuHasQtBbjDsetG08_BPNpg2VrOKL4hBK4LQB97VdF3Lfg5Z-Gn4Cdr0pyc42ipq3k1AM45NQK4EqQN7dIjt5ankykdgYnxuxkRtLTmDyzxeyLsl-KrdY1gS3qE20eEEfx4tp8MoQcXyVVYOVEmCU4APVRznXRktTqQz7ZZoqgK8JDvvggQELWv9evD7u1e18E1HMs1xIVXYcoKv8AnhIV4tB2hVUpUchU-6hrf7dbJoegjwBMBn5EHPrXPD_wV5y0EcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
