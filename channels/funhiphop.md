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
<img src="https://cdn4.telesco.pe/file/nbbBaaOK-_Xcv8Fwpww0mLzgRB8IVc7fE-SLb-TwzHtdOh-G_vxkmb0Gqe5A2UEzUXc7dKONVJ_WpudzduCChle0oMQXEIYlmUr2Zzu8Qh8Tr9AzD8bJwfkLBnnWaNh45goOb_sQS1JWhY1LMs8-cONHZD1objzBvr95vz4drhLifCZrw9SDsH3R5zx0LbfeNt2WdBNB4u7ct0U6RWQNLBQDm2joimOS3nkK87CSW0oeCpddZd9F8ItsztI7qzvn37EHp6pLsKC73Vc1N0bigSa6mezxVIilic4N7pZm_m7CMeaT94GvFhhyAmdA36ENUlvminILR7SnltU7vs212w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 07:35:57</div>
<hr>

<div class="tg-post" id="msg-76878">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باز همون همیشگی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/76878" target="_blank">📅 02:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ستون دین با یه گوز نقض میشه ولی اینجا آتش بس با 2 دور تبادل آتش نقض نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/76877" target="_blank">📅 02:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HedsQBAn7G5zs-z1zxiqvs-Pxsim7slPEV2DM5W7neJGrcBfUBqpZa64bpwq67VwBEsj5hZCA-VfScUqoG4xLE_NY2cg5BcD1ELON_SpFkmTxpEw5egpZqAJfsnxq9DjZwCcWiv_gevgaXhPF-TQPEn0OmIgrUcyz6Q6-IY6651CQCSuFo1bZW92ZxTaGxU9Z0zmHKAQj0efrDCj72a8l17JuXFD1izDuK3SY0cK2SU7-0pfKb4uwzPmuqP5WGK9qc6lTBnxPW-f_TKhWzJc1pk8Ahks5gRAA2TKKw1X6dJRuquEry4MnkGrm_6zUpEuhxqD9OhbaKOvSjLK4LqDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m88sZ5U-BUkzxeXGqAuDRTCkv_BV1HlgmQneBO74USEb0Uf8tY5WT-dxn6TtLKtL6Ns-SsUPPQft4l4yeeuE_eTYH5XCAy6v3Ac3QVvGBQKgNhZJZ446j6gIuAQYxPJ2LS9DKHoEQowMAEUWhjiI3sO3y-lsQQ_XIch53PlaVQsmhpD0sADNVL5g6Eyipg6POeW_nnNfMbnEdgoDuO4A77uI_8PMcelNzkb9vVTaFitx_WQinLR-NzQ6O-Xu25DyVbu1bNtnUsNYFBljXQA_BcGXY9fh0zqL6eKk8mwQ1ogwziFDi6GNfZHgMSO5tlg_UJEO7WBcNyqZlWzJdDh7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu0kPQJqlXlVMMOlp_WCy-beCCR-dochU_6kl5EHTk4IEHrMQZy51aAYG5p6R2NMwRCrp-6MLvhTt6_NeuT-4DH7jREmSs9hjKNaJKDeOhmcGnEmOC7n0jsgSuoWUUXcfrTDjdngnUOswbkX8RJthfGun0glfay93HsKTOgmMFrrs1HZK9_hY_2v-0qfHmbUQKZ2RIK2VZgLCTX_0-dJ7NxR-l4J00WrsOmJP1JxV7Q5e8kmdclipQtCmJbzyi4MkKFx7Y4fSVrCoxh-n4ExjFwhS8UnJ7p67Xhx0ftgT_-kcNnqEw8Z8UjNazm2WJhu_76STJJLQcdhfPKG9KcXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76865">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEkRuCSofcTj5IuNr0CwgduTO-l00mVjW7RImt1DdctS5gGbRZyUcHznXWL8MqkMWy6GRm1ColpdV6bprtSppYU-ak69HTgE493ImWoi1dWGA401oT1SmLpQgBRpo4K2Kpv8e7iMh7MVHn0j2X9c5HF2X4CP-Ux2-GFOyL_19Mr6EE9ldkOttkRSFYl3giNkzhNuV3RoKLAQOEDY91dfgCGaSIWi-hR9miJmmrlnyVz2zWGRVpmvYGb_5ntHCItfJDAG49o9puPacpAFc-m1XhhiGzYcODvkpxhgyGPJVllPEA1Xf-_1bLcswC6tUZc1rPH66HkYNW-Hla73iMIPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلن نامحدود فروش باز شد به شدت محدود
🥚
هم براى ايفون هم براى اندرويد
🍏
🤖
600
تا اکانت شارژ شد
📣
قیمت آف شدید خورد
🏧
فقط و فقط تا پایان ظهر قیمت 397/000  هزارتومان
( )
➡️
حداقل خرید به علت محدودیت درگاه (
٣٩٧
/
000
) میباشد
💓
جهت خرید ریالی از ربات زیر
❤️
@V2boxinobot
اينم تخفيف امروز
💓
تضمين بازگشت وجه
➡️
➡️
➡️
بدون يكـ ثانيه قطعى
👍
اپليكيشن تخصصى
🤖
🍏
💻
اكانت  ٣١ روزه تكـ كاربر
✅
📣
:
@v2boxino</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76865" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟ فردا چن شنبس  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76863" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟
فردا چن شنبس
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76862" target="_blank">📅 23:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76861" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76860" target="_blank">📅 22:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76859" target="_blank">📅 22:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH3bMYOGmfFFXv5c9w5VLfbPrIqC3JHYS3SU-6ANYyZU1YQCsPdCuqmzRSG6Ly3VIxgUyrFer0nO1utuwpe68pGzxBXLhpnO6Dt8JpwWR8adACbtXAJinb0hz2kLOV2U099JBaBH1eaO4Vaeia4MzRT9YlPe2GDmg_Uy6fygoOqjtfQF7hV2_YsZOT2jIeOwJPjgXZMAHMqZNr5bU4pTCIKGZ2jEnWzIq0tcKEXNXJo2p113rmHxKNpdfwzJNmOqlZ4X9L8QG-CESZYawmPjl3kXwpDDJwGuO-6dxURuQOvHlCs3v0DZm3SIkmowfZ5xaMXaUHTMzKNu9s3Brm85SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76858" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بخاطر وجود بزرگترین تهدید علیه جمهوری اسلامی یعنی پوریا پوتک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76856" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد پورنهاب بخاطر داشتن سوپر فیلتر شد  این وسط نمیدونم یوتوب برای چی فیلتر شد    @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76855" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد
اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد
پورنهاب بخاطر داشتن سوپر فیلتر شد
این وسط نمیدونم یوتوب برای چی فیلتر شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76854" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYkfhW0duR7YoOZ1bI936VOKLE8TO15St7Rqp-i7ISet-V33DQ9Q6l0libMLmroD_T_Y75waRwAVLYr1O766uKtbo4GaqqFc2NFr_FiN8obrk2-wzt88VyQV6pwIL5oaMTBOI1eXqItV8hfWXhk7DeXPjagp7a_vvcbY9C7P4RttqsM6jgsP-LMgbBvzaPmPcKmP_Mnfjj-4Au1Erz77IOLuL7CmYbmkXO-oHQ_g7LRFmRQdMr4HtckzrLMJoVnWwTxLPq4IV18o9kyT_ZiQ4qtlXJghMsYgAFm_JclkU5SvwsBV99louBIue36AjzW2dMkAMMaRbCpyuoq2_tt_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76853" target="_blank">📅 22:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK_FsRjcO1U9pZmxLFJbFXOEZk6Asm4a5KJCxpWzuBo1XHKCbzbouAsRbXQQZ9tAhg9jbidtoK0ZMjuIbj4hyOL63ENz5Ndw36pneEBlYVrX0JAskad4opJdsMgyhdZwlFS7-DwTxDrvHyMQB9Mg4XDyN9DoXe_ZIDuH2-xdNt8GU_JlakF3QEXNHyJnRZN2FCRym4XlzuyjdTWJ9xHqjRHhrWw9WLxJIn_AQSEO29c9AYXXOPZAHTtITaBme_DUQAUIapIFpDEsfNJaM7FRqjg1m0p9uF8YavyCNxHIux05-tyvVLr2pWLyUpRyac6G_szlLAVxM_UBZC3sjOOOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش تحت تعقیبیما
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76852" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e570681.mp4?token=QMG-GYYNvrE-FMCr78ojqTEmPd-V6Q_BvzuJfYTJ96pG_KFh_FVuWMKR6o8KhZzRpITGJRm4ijQdfqQEXPvA01iYw_pKhfcuH_o0dW2WjD7zGeujRYZEBs0hi8IN0_rlt-n2uteeP8cLcEQY0vInc0SvmWrO13kgfWB-v7hKJlKvll079w75KQo3TEONUPkBulFlPtCkvJ1JUZIs3mEuuUKZq-3uG5riB1hzwNLt9pdWlUZ1r6cSWiR6vMPWn1u1lISM9ttduqByyL26kXdb1X_7e_df89uV8bHByGAkGv29iocYPi3n0i2gceW41mp0OiVWoZokYFjM8PEIAp8PnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e570681.mp4?token=QMG-GYYNvrE-FMCr78ojqTEmPd-V6Q_BvzuJfYTJ96pG_KFh_FVuWMKR6o8KhZzRpITGJRm4ijQdfqQEXPvA01iYw_pKhfcuH_o0dW2WjD7zGeujRYZEBs0hi8IN0_rlt-n2uteeP8cLcEQY0vInc0SvmWrO13kgfWB-v7hKJlKvll079w75KQo3TEONUPkBulFlPtCkvJ1JUZIs3mEuuUKZq-3uG5riB1hzwNLt9pdWlUZ1r6cSWiR6vMPWn1u1lISM9ttduqByyL26kXdb1X_7e_df89uV8bHByGAkGv29iocYPi3n0i2gceW41mp0OiVWoZokYFjM8PEIAp8PnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر جدید عصر یخبندان ۶
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76851" target="_blank">📅 21:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🛍
قیمت به گیگی 8 هزار تومان کاهش پیدا کرد
🛍
حراج ویژه تا پایان امشب
⭐️
💎
30G-295
💎
50G-470
💎
70G-590
💎
100G-800
🤩
لود بالانس شده و مولتی آیپی
🤩
🤩
بدون ضریب و محدودیت کاربر
🤩
🔴
ظرفیت به شدت محدود هست
💬
خرید
🚀
کانال مشتریان</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76850" target="_blank">📅 21:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شهر صور در جنوب لبنان بمباران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76849" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ژنرال محسن رضایی:
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتونه آمریکا را اداره کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76848" target="_blank">📅 19:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2HVN2cjqxebKmsMc-GalUwnJq-27Z6jncbRW19Rh979n38EmxTZajHOK9EEos9JYxqN67ya-ZvPW9kKz1Nit6ziVaMpCA-ZFzMlvEz5_UduuHqe-1bbFCyMHeZeEG8S_a5mzIoS63VrO3q197KqrXr0TJcvUyniY6gQXT9iibyECSS1hrY-uQwNCh_a0qpEcZZhDWUXBRlRVRYwk9zNuFGkTv4Txpm-GFr1wz_SbzoeMc7paxujzC4jE4S707CsRMi-0UiYbo_yAGYXuZEugwkgG1LSjVkrq_ib1TYSMXhe9SlSR-U0Bq7uAd_OPmPztyjDaIfK61ngLkdVn2WM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷ سال پیش در چنین روزی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76847" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyEFqLZRSxyrn1AvP_N4GwsNKZd9sz6hDtH2R0LzGGsI5OD5jRYK_wh5oc-cAhjODNHyLJ7p8U4hz0TykGgE8TMTlwYkdkt6HMr3nbo77p_M5mPA75EhNLFgyHKLOCTOFyBWafVaDuqhDODiCN6g2wICxe_Eer3diyVvLabuBtSrzAJIz1Ruvqzk5SS5WyUeqOT-sUG-SVK_90taxo0HOJhjpIEytzgU0KEG_6axLxUlmT-B0xfTe3Eh5rBJ03KO0eoDclVufLczQwedM9SMi6-ikOkaf48JwhGbArXB2XJMNG9jMcpnbBq3R4WDyRKXtjIyNHp_PGYyARtBa8urjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76845" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حاجی کاکولدی چیزی هستی این کارارو میکنی؟
- اولین سوالم از حصین وقتی حضوری دیدمش.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76844" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=RfEsslAbvxdPzGSqCS9JhaGGl4KJ6K8m3UqmQRQrUElkTXxwi7WKY-fQZw2G8W68LnFUNWEOs5oF6nc5tkDR8bpXr4Sr5Ml6o_6rI3o3tnFVau2--cUGa_DinoTgBOUEYXZ1LzWLd5Oy_r-7pSHreLTgyiP7g0edGFtxWNzeoH6qPsItHwXrQiLdL2M30A3J9Bd-3vrFZH-Qq0-Tc-idF2AA5r5mNDWz5WaLqTWC9bAU_G4dKp7bxEK1A88gy5buqVYjV_SWmNgQEjo0IfeQfpsAYwJUyYrgv0v8j4AQbh7RivmMqeSTVsfaeegvoQQ5ySeR5iJExEpshdxLLk3Adw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=RfEsslAbvxdPzGSqCS9JhaGGl4KJ6K8m3UqmQRQrUElkTXxwi7WKY-fQZw2G8W68LnFUNWEOs5oF6nc5tkDR8bpXr4Sr5Ml6o_6rI3o3tnFVau2--cUGa_DinoTgBOUEYXZ1LzWLd5Oy_r-7pSHreLTgyiP7g0edGFtxWNzeoH6qPsItHwXrQiLdL2M30A3J9Bd-3vrFZH-Qq0-Tc-idF2AA5r5mNDWz5WaLqTWC9bAU_G4dKp7bxEK1A88gy5buqVYjV_SWmNgQEjo0IfeQfpsAYwJUyYrgv0v8j4AQbh7RivmMqeSTVsfaeegvoQQ5ySeR5iJExEpshdxLLk3Adw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آه فدایی آروم تر
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76843" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=X8jUM5xjl-xowR1IjQ8aD7DZ_lOCuhYI6SMyrnmu6aeVcAkgwE0wDglW8U1LwO-whfgO78qtWCKnvnQc6f7D3PsrHgrXkF9ZVDO0nyUUyNJ8iHzLLuI30t7A5h-9MxgGmidRBrObFJ9HYnYnjVl4Ktr0MnfOUgTjAsb2NhHdSJgM_AWx3ZXoa-3VCnMfUZpAT0gxYmElDa9wB10QLL5V1lYf2RaeHxbmS_WITwDQL9u7B19h5ixE9Ddgh2RvEm6pk4nCJuEIAN2Axilwujq-U0bizT9DCtfRiFYRpvcSAArvHGX774Jnr6Pcq4QZVAQmEYt_CZddj4kjU9aSG1vyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=X8jUM5xjl-xowR1IjQ8aD7DZ_lOCuhYI6SMyrnmu6aeVcAkgwE0wDglW8U1LwO-whfgO78qtWCKnvnQc6f7D3PsrHgrXkF9ZVDO0nyUUyNJ8iHzLLuI30t7A5h-9MxgGmidRBrObFJ9HYnYnjVl4Ktr0MnfOUgTjAsb2NhHdSJgM_AWx3ZXoa-3VCnMfUZpAT0gxYmElDa9wB10QLL5V1lYf2RaeHxbmS_WITwDQL9u7B19h5ixE9Ddgh2RvEm6pk4nCJuEIAN2Axilwujq-U0bizT9DCtfRiFYRpvcSAArvHGX774Jnr6Pcq4QZVAQmEYt_CZddj4kjU9aSG1vyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76842" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اگ دنبال یه سایت با هدایا خفن و کاربردی هستی اینجارو از دست نده
🎁
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/76841" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76840">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SttY_bxDk4CZii53zrfIZBabEkR95Opn-oOXl9f0xpDo3NKaW91gcSMoxytAYet5S21DrArcQ2JAEipeF367cxGNTmPrRw75dl6BKVjl_EZaxlO26uDTyAXirTcwn3jIrrYmagXVQdDVfsaezK9c1-lNr6JtknCccCKAXR0isWiqF_32WwfwPxFVtH8mMuZuFm4s0rV3QQEWAZXJ4aQSdH3Jt5aUZUffgRe7QgS8UUHHGQd-A7AjLRXLzH7Bx0nvfWNe8BjbIRFuIctxt8xjJLUoRMmovrKD5fQcrrlUY2OtYtqjfP1BfavnssFfaSnmC1dp26u36Gkyvbis-FXY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g14
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/funhiphop/76840" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGwgg1zBkT9vAZc0r7aBobL4FEYjJxl_GHBfOwSdbrM8byY0gMjqyS3q3co9RveBF3F93o7xkd6SByhLkC06-GsgFzKwNyVjPRlUwvpiBod13TnKNMW-JsEKQnLiEQTDBoJby6V9mQGadUw-1FPdpVZdq9_7EiMbQ11Vag-rnkFsjGLJNOrBCzBC0Qmljywn_oqZpAFTSRun1gJu6d1zbC90CvPmFMS_fCKbQ0rXnLi4MUTl-ChqoLifeKYjQsZ6yiABZO48yNWbYzXyUmrEdF5ujRgHOUbRYDvKVUObkiTRp83mEHUsR3R1iQ9QV-D-KektgYbm_9lUiUXA6ddJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpMcPA8oRGNHAYtm4I430vf7h1S8YivxMyjoTdb-nVsUwoCfpSmmiuooVh23Yn4EqbYKJHmqEDeAnlKyh9EhNnOOLxogJI3wu1jOUrb9h2h3_wWYakmLuHEsc-UEawI7XLiiQlMCyBaH_xn7hOr_T5bLUXQJYenI7tWXrsnus2Bq3vugABSxSRJcbXsGz5KrpeoVinr3SKbbgZ9F3BSEYYJ7etS9DHzIrp0p8e0KRVOC8KB6DdODxS6Ix1lLqOBPFF_UndYW9Cerb4ZiQ3qnVfjT6_o2I0ztZTsjcJM-RMFtKQR8DzWz9d7Qu2auQwmlRgM8AuNcA0hH5X46k1RZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VahW6px_shsl6mqtUbK4DqMmTbR3G6XHEqBJsGZ-z2VqybGg4w1GiU95SLQx4BMaU2QbyirWRqHN2R1G6tuQrL1J3Go_85PddsiPUueXObaN4c270H_NC02lJ6u-Bgz8AC4d_idhRI3Aob-F32v4_ADbo0YpuFrw9Y3-Pgkz6H727t3LDezL_NjrIaotLFJopxMuWcpmws3uvqVKH6_ce8iJQEJe7E4vkb0IPt1p9sZa_f_PjQjFl0UAlwiqvueCvjEUSOMfUsjTF9fh4JY_1dqFCykjlPdwWphxwEGuZyZ1fTkVSHqk-cVnwfeincsIJM3pK4bKGd9FC6qVBJKyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq2G8G7PAASC-Q8ifXjf5_3z8ey6Mb4nRNqSjwlgPHDV23F39S21e2a9J24r-9J4hPqc8woB5KzUy5KQ-7qYM0DaLvLq9BXd0NbfnicolK83gLnT5lhZtEusxzMZbZbubbZ-lVJIOaFUvifONG8ZOAZRDX1a7pwVj61Ce5UWdagBzrPkAlh5bUVH-B6l6bsn0u3HFdVvbX_AB93IIudGWEmhxaFLhSwOuktfkTQooeJ0Bb3w_D8e2hHXjYbsx5IO99U2sSB27lrx6Ze0f-L-3TVHCVD4x_Ppit4sUZm-JJ5IpHJh4dWHpqsFx-Om1PN5KSX8CeaKkcnulcgpD95jEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iirRBtHsacXFa-2imnr6JzGBnZIlIl6z42a3tu9YFd04xh6cf9QXAj8kpniZsxbfzbWITyResRtrLHXdm2Azux2LZdqhDCF33lC-1OQK__KJ6FwoYGdBDHFZX5aEg34t-5kTJSRjsXkiaN_NIGmn_FWHF6cJ8NJtJcuasgJy-DKAS2b4ii8K2o8G3SmQZu07Nu9ZewAwbe6X1qbLNBBJA6PK1n1Kysvy9Jgx6h8LzfgMSFpsz28hk8RQF_ccHqL4nhBLJgL_aTZKBHr4k0Da9RhrGaEXLiHT-D634cqLHTQeNpnea5RYzcbBFD76pvIq0XHi2PEh-rav9kK444DJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=pbT2IXPi6Z7sWjp_p1yNhOLf1_LLe1Kt7I36eNX3BwWInKVcz-WoN1NVOavVma2f9ERghVGT6wt8KExpYNTla0E0ZQWGq7SBStIUgHBEyJhcIi2wZg8OhZZ4wLerrPJDu_xnN3xPP0L11BT_hvegu9eg8z17HfcTW4FsLSEqMNA_e-ka1-B8QEqaNOEhiUvF89CqQ4pb-bM_2BMtVOihzsGncTUtxc5cro3atdLnM3yHnyDQx5jcqtK8IKt_qM0yi_ICxtkaVWAeTmBTZg411qtOov_VGbCFcCFVD1cc5p-mYrU0tPnhz2n5Nrcv_duOOnnFacllu6w8WGatumNsvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=pbT2IXPi6Z7sWjp_p1yNhOLf1_LLe1Kt7I36eNX3BwWInKVcz-WoN1NVOavVma2f9ERghVGT6wt8KExpYNTla0E0ZQWGq7SBStIUgHBEyJhcIi2wZg8OhZZ4wLerrPJDu_xnN3xPP0L11BT_hvegu9eg8z17HfcTW4FsLSEqMNA_e-ka1-B8QEqaNOEhiUvF89CqQ4pb-bM_2BMtVOihzsGncTUtxc5cro3atdLnM3yHnyDQx5jcqtK8IKt_qM0yi_ICxtkaVWAeTmBTZg411qtOov_VGbCFcCFVD1cc5p-mYrU0tPnhz2n5Nrcv_duOOnnFacllu6w8WGatumNsvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLA6eGPhpb9UgTVqUFiVkFKOV6tw2SaBnHBm2AMT8t00YP2BKYbzi283tly-yfRHvA8PC_gDKHcQ35QMFEb3qUtM1Zhab-uMW2IkuR-0290n3kuG872rdNyO5UqlThQlZoFMlTp3cBbcaqy1lfntt8u1gCwJigMlFwK3XEgvp1-kgMU2KNyrMqp1xuRmdoGfcnbqWA0WPXKPjBN_5B7mfsuY_-dex__69N72U-hE4z_in6rodomcV1-EWtC-V-4lgQmAxmWVl2dbB16Q0fd6jQAxar0FMA_WIuGYZ-O4ZWJ_EMqYXm64xhFAk3rMeF79wYx5uZ-wrDRSQjoclqSETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76808" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAnRb-OD3OovMQ8gyQrMDmnIo-k-JmOQA-oVTI0QiSSvmlWyxp7EDAoIL8UUanVNm7ys5iddIZEpks7gx5ldoYadjfBx58LqZyKlQGQgYie9i5VW8y3LOOcZYC5gDCHZGmfZHwa_ZZ4UzxSmf8ytt711AzhwzqnVRcRS3oB34cqumcEEbo7LqQhhvc97iXSC595_DGJaFwi8EmYY_6dqT_ZQ8egDkqsukCkmrA-Thstb5qDHqsDzdxx-A2BdHkpDIk4grKNraRnW4rhTEVN_4QELmUYH3HnskfhzYlQyxf_q0rRoiCO4DDroDkYTDIH938JX_vi3fxXL7R2_Ao0LbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r14
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76807" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=V_jcOFXbGN6k6SoXYG1Ou1Me6md5GGPgA-Bwr_7urEgmFs-CnEvDlvj9NjUQwHS0ugIcCSVvaCrJgHIyXH_ssCIfK9UcbH3Q6KwUtT0WYr8v0H5avUrqBRBCPkwURHhZO_1n77Ly2xB9TxBZz37KdRAAnGy2EOyNfhUQlUGBYynvdkq68J6gGUrIO2NqaN4unQNJl5XKTzBdph665p5HC3ZPOxbEkBb7mZOf1L2SsqA_QBvT2ETCA5hL8Tb3kvnMP2nEh5DeuCvBoHJedw0tGXZAQr7pTzOWt41cLuQKdAFxZbKaljE6HCbtv2YYPsC4I0ZIn7_sy0FlrqW2Mj22TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=V_jcOFXbGN6k6SoXYG1Ou1Me6md5GGPgA-Bwr_7urEgmFs-CnEvDlvj9NjUQwHS0ugIcCSVvaCrJgHIyXH_ssCIfK9UcbH3Q6KwUtT0WYr8v0H5avUrqBRBCPkwURHhZO_1n77Ly2xB9TxBZz37KdRAAnGy2EOyNfhUQlUGBYynvdkq68J6gGUrIO2NqaN4unQNJl5XKTzBdph665p5HC3ZPOxbEkBb7mZOf1L2SsqA_QBvT2ETCA5hL8Tb3kvnMP2nEh5DeuCvBoHJedw0tGXZAQr7pTzOWt41cLuQKdAFxZbKaljE6HCbtv2YYPsC4I0ZIn7_sy0FlrqW2Mj22TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=e0BOwXkiww2QZ71YFi-E_lj_LdnPFUJh8kLrQ2q18so-w5WiggRmmrQzvUWIP8g_bFZxLEocrz0S15m01i6uofb_LotqihYedTkLD2AIlFUtoyA5x6L28XKsJ8JsNofPbzPkHnxgeYaEIBotIzKsH6Oi2QviCnoxrwX1wHL1iRNHfx9h4zyamcEBKZKRtibtRAlw3zfwAXPc5TtcO6ZU_ZRxznzofe73QMGVuWVBK1SOpqphP0l3vcH-zqctnRxibS7CxRzo8YSABZA-t5nnIpP3TOnVaQ47LU2tIkGKxA-cdcqk7Xz9d3dS5lWZs2-TPLNtDshAb-8WLP5_KGaW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=e0BOwXkiww2QZ71YFi-E_lj_LdnPFUJh8kLrQ2q18so-w5WiggRmmrQzvUWIP8g_bFZxLEocrz0S15m01i6uofb_LotqihYedTkLD2AIlFUtoyA5x6L28XKsJ8JsNofPbzPkHnxgeYaEIBotIzKsH6Oi2QviCnoxrwX1wHL1iRNHfx9h4zyamcEBKZKRtibtRAlw3zfwAXPc5TtcO6ZU_ZRxznzofe73QMGVuWVBK1SOpqphP0l3vcH-zqctnRxibS7CxRzo8YSABZA-t5nnIpP3TOnVaQ47LU2tIkGKxA-cdcqk7Xz9d3dS5lWZs2-TPLNtDshAb-8WLP5_KGaW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDkO5owuGfLnflBkKWzJ75f4xu8r3zxYsTxSO6mr2gKTq2BknKp73ZNvoer9YRx_gM95AERto-Hc-83zZcowm0hE1duGFlhhiYgoC9nHkCZKHV62YWFykSh76zPAsXinyl2Kx937j8y8vW7ti6uTG8zbF-uByUJw6QQwa4XFHeTO9ekevZOmnNGAgZ24xyJLZXNmmQqbZjYXl4huIZLkTpOL7LRZpmQ76ByzT1qEk2KPuNaNP75c6aROSVrfeOKvh0aSP5TSOoTjhJDNmUYc7QMOBvUiXAAw5F9jMw47F8HGwH6nrARIO0orJl8vS4jfbhhp3Bas350OFczeuYmO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbitrDbsOrTKGve-8E78Y8pLxNuiRbfDftRPgnooQT1Lyy1T_J9Yl44LdM8J4xWHcB4e4vpv8CLO0wNXSZBT9X2LB2E7AJEmLbo4R4hvTu9C3Xlou6cktVGj7S5QBXTOYAmObOtmQ48V4hnQJh7dZd4CNi6ZuHul9_TrpB_AxiSXPpfZ7BnCZtCqoNTL2ygD9RAY8YnJN-cdtIF-AL5Az9MntyGBy0kFnwfql3xDySniIOenr0rlcGqSPVMJJD7AEhXyghtFbHX0YTKyVfxFLButtI8cXMtWlWdDFPau3x8gI0zdG4bXDwfoEZK7kHT82iaFMr-zPRz2m4wywKE9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHAYreXgXz5s9tE5mIUrr4NlBEbRk0LGwWSx5SgCX3EgEuJfEZ7YVzXz9wfpaYvpM-FlsN9LW9tabm8qY_2NOzny7K_EAb6R6lrgMbaXsHlcBgJQZeqUkHuoHlZ7sxanNOU9uF1jmt88beUvlsNNn444z5zCr4MF_j2zl104nV_YEJ9jQT2J_5T4mkvtH4m7nA8Yha1ZlGufdiR9gKsPvF9gmYSgDiHZMNq-IA9cxJVyR_oPkVAZ_6ULr0KcMZcdVr3zxE3DB8bV_QOAKXfBFushzCfEjvhxhny6RrSOok4RpQnLZoutE2Lo0LDHxFZpyFsK89XLXxMVwQ7nXuZn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=KQdo3lGxEBxrJZfUYXjYLhk1ST1MwJIyPCXzGJnjV4mMqxfZK65c2zeg4ZwgSTKv01lQU4w1giI5wlybNquT8KsPNaAKBSNk6eI0wVml2AYYmNgRGXl7EwyyMVEzmsppiG5EVorGxl8x0FKYt3XoIozEsLUjZjkQfrPXpntDm_v36dlsXWlcVBzKq--jPwszo1XLlbYzGme52JmrwDKf4iBub48aVLKB1TRuNyLPjX2g8fh8C6xU5fWNucQlGsEeAvBXns8WdC6B4FSRbBlyqpM9KtJO0ryRUSr6X-2eDcPVVCxi3Qixq6HPAaI5UGc4WFJi3R6NUT4Q2ct7GKj5VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=KQdo3lGxEBxrJZfUYXjYLhk1ST1MwJIyPCXzGJnjV4mMqxfZK65c2zeg4ZwgSTKv01lQU4w1giI5wlybNquT8KsPNaAKBSNk6eI0wVml2AYYmNgRGXl7EwyyMVEzmsppiG5EVorGxl8x0FKYt3XoIozEsLUjZjkQfrPXpntDm_v36dlsXWlcVBzKq--jPwszo1XLlbYzGme52JmrwDKf4iBub48aVLKB1TRuNyLPjX2g8fh8C6xU5fWNucQlGsEeAvBXns8WdC6B4FSRbBlyqpM9KtJO0ryRUSr6X-2eDcPVVCxi3Qixq6HPAaI5UGc4WFJi3R6NUT4Q2ct7GKj5VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9aCrRp8qcZI-tGVv__45EFCf6PaH9S4F0Nr777W7lGTfPFHXvgE3T24uYVz0UttFg7sZV4D-n-SWvPLFvp-h1JtEv2MUenzTJQgo-VJKAme9IlU8kOrfAUA7K49QkC45gXeUsPpJI1n85j0ToSkHWeumDEehVI02LGAyKeQN92AFHhHLwz3FLqgukI3IR4v-0RyJ6QY9-p1t6yI90GlaMMYhqLJBqgdCTs723oOAsu2CJwoluWPhv1tszQRLhODjOatmi0De1oVhF2hffLn7hLjJ10nuAohssKjnWRHYSb4FObrLnscr5IkpgoN4feDlFlN1FR_smbutUpVaz3zRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=YKOKcQ3xfSlqJHbaQ-h2WtFM-v-Zah1lKgdEe-RzuWRPrG81e4HS-7aVdjVjxMVzD_xSu4dTdJv-sLWGuC_DkODOicRunHsVJ7swK50v5xjC7qvTTWbo8Mtu4cZwhSxt5AROEF_jMn7bRDd0dvDWPbEnpCQuSjQmS-qHAU8CEc6Sz_-HvLS2NMScZbNS6gmfCEFkUjjWBf2NJJXS0y4MSp77XQleaNuoYScHDBjZ4Qq-BA1S0MyCUM2TSL4CYii9WehscT3aivJo1q0rtSIV7QI04Oq8IYl6OfSB9b1zSvu3q-tvJv6QPjdcrNM60PT6jTSaq_zc1ebVxxD2Fqe3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=YKOKcQ3xfSlqJHbaQ-h2WtFM-v-Zah1lKgdEe-RzuWRPrG81e4HS-7aVdjVjxMVzD_xSu4dTdJv-sLWGuC_DkODOicRunHsVJ7swK50v5xjC7qvTTWbo8Mtu4cZwhSxt5AROEF_jMn7bRDd0dvDWPbEnpCQuSjQmS-qHAU8CEc6Sz_-HvLS2NMScZbNS6gmfCEFkUjjWBf2NJJXS0y4MSp77XQleaNuoYScHDBjZ4Qq-BA1S0MyCUM2TSL4CYii9WehscT3aivJo1q0rtSIV7QI04Oq8IYl6OfSB9b1zSvu3q-tvJv6QPjdcrNM60PT6jTSaq_zc1ebVxxD2Fqe3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=L-xx_BXAB3UEUOzcsTqI-KsykZQs1dVTZHCVFH7aQk_7pGaUpgZGtL_-08ch0kmtIX6JzNJ80CRWVdxRsXSQ6Nyh2z6PTz2raIdpYXSCS000aeN6oHg035dBzl2WK2P6FVysSNykS4M5hrnu3Wrol6qiY-QcO6_r0g2zEG6x-indRBxrkIedR96eKY2Ats2RyTnrbzxp8TBp8175wLJywi585vSZdh4Yay1iE1dr6xe1-gXGuyUZ-qyNiW7ld6sqSQFRcD0eGBONeBrLBKlnf77A_rKolr5-lMeW-uTEwb_kZsK4Jl1QrQ6RHj1Hr9-rX5n3bhjhQiMvfbhoggLRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=L-xx_BXAB3UEUOzcsTqI-KsykZQs1dVTZHCVFH7aQk_7pGaUpgZGtL_-08ch0kmtIX6JzNJ80CRWVdxRsXSQ6Nyh2z6PTz2raIdpYXSCS000aeN6oHg035dBzl2WK2P6FVysSNykS4M5hrnu3Wrol6qiY-QcO6_r0g2zEG6x-indRBxrkIedR96eKY2Ats2RyTnrbzxp8TBp8175wLJywi585vSZdh4Yay1iE1dr6xe1-gXGuyUZ-qyNiW7ld6sqSQFRcD0eGBONeBrLBKlnf77A_rKolr5-lMeW-uTEwb_kZsK4Jl1QrQ6RHj1Hr9-rX5n3bhjhQiMvfbhoggLRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
