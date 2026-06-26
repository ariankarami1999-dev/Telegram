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
<img src="https://cdn1.telesco.pe/file/sF0G6QdBzfDdzcoy6UqOfW4eArxVU75kS-keBHOPNLujLpW9Ikc5CdIhLKcQ7pBZ3X0GUvAftpuH8w27F9nfQ2GSOLLWVBzZmdR1WgoFV9ECma67h7sWg6W7kvRFx_5vtY1qeYeddjrWvhUOHh2HcfO3rr6SXyCWO6xYfRFfnStELZJ46EbJVVP23M8P5k23Q3TgNgbqsyIrwStwEI9hxhwIfj78jJBLS-LDLyk2FR3ceuhFIxa2Cc0hA_o9hjjKbxDX4D_H57-cZRJew4U2Xh8xQ2kM4StVNmnnW2bCS1nkP3ZPiL1FNa5aE4u78G7lj1-H6Ws3DSnJk1xekiLyYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=le2aBpX6TPXfgfen4AbvYNmyHXsFhMjTYOlN5VT6BbX6Gx8r8zV5ZkBOTIy22NxpDyWkXzlfGRV5PpFUrwvVMTE2DTtOR6qZrO_Jv3aiu8hSmI_M8cB1rfXCbLxXrTluRlwTTn51aLcXYksQMETVBL_0VECAnWHRnk2nJVEMEp_q2AyKoU28iGhci6NmQkNDskMjVd2yXfWlI8UPVqNOwZ6zsxCE-eSL_rXGGUs1CXCLwv12WUM-1ffF6Qw6FISCYTiAeMu40PVz_AM2rNo_6nhauuwfNMzW4cDw3zH1s57KdoD9w0Hlb4L5fWfd71C1RaFqQYwQau6n5aq4Xh4JNBSjqACvjaBvgyGT7gaQ3LHqYk67bRVhcAElnA3XP1Fj5VujtJKIAV1ReMrKUyKJOw7qiUdX0olEYiaNPxgNUOFm-0nzcdeeWclsC4v_ET8NGFvByaMdjYcACBlTeDDNfVg0uwnzHsRbun2uKJZyK--hIlWVu6T_A_jNkIZ3ACHE_6hrR_XmBaB6PDrDWofRKDA557FxnlWu4iXiH2N1LrwWTdwWG2LVxuTFnFyRaCzl3AjH_bfhlqptTmuj9aSms2RIrIsovaScyySTSmO2U-rXdIXf9Xs6KJdWAOkSmmpQNJmuk_X8pZiCF5wpKHo3fR_mGywXbp0RAem4tzqH9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=le2aBpX6TPXfgfen4AbvYNmyHXsFhMjTYOlN5VT6BbX6Gx8r8zV5ZkBOTIy22NxpDyWkXzlfGRV5PpFUrwvVMTE2DTtOR6qZrO_Jv3aiu8hSmI_M8cB1rfXCbLxXrTluRlwTTn51aLcXYksQMETVBL_0VECAnWHRnk2nJVEMEp_q2AyKoU28iGhci6NmQkNDskMjVd2yXfWlI8UPVqNOwZ6zsxCE-eSL_rXGGUs1CXCLwv12WUM-1ffF6Qw6FISCYTiAeMu40PVz_AM2rNo_6nhauuwfNMzW4cDw3zH1s57KdoD9w0Hlb4L5fWfd71C1RaFqQYwQau6n5aq4Xh4JNBSjqACvjaBvgyGT7gaQ3LHqYk67bRVhcAElnA3XP1Fj5VujtJKIAV1ReMrKUyKJOw7qiUdX0olEYiaNPxgNUOFm-0nzcdeeWclsC4v_ET8NGFvByaMdjYcACBlTeDDNfVg0uwnzHsRbun2uKJZyK--hIlWVu6T_A_jNkIZ3ACHE_6hrR_XmBaB6PDrDWofRKDA557FxnlWu4iXiH2N1LrwWTdwWG2LVxuTFnFyRaCzl3AjH_bfhlqptTmuj9aSms2RIrIsovaScyySTSmO2U-rXdIXf9Xs6KJdWAOkSmmpQNJmuk_X8pZiCF5wpKHo3fR_mGywXbp0RAem4tzqH9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WkQvYE8Ki9B6PPzDthb13ze1Rc2RTqOGS8GhURGL6ORDcpQ5GGnnFWfjW9Q2aRsgOlp4Z1RSCUkrPnibTq6CrHbYhIm8JYGmiadedbk5CMrFAKKSz9CL-nUaMoDZodxE14BKLCxHvlznErPv3497FqvKYhyWFUxLsxgB2i0W7klNOs6CHThwSZh5yo-VeoZqmzO6HVhhopRvK7nPx-U2leSyV20rNgyI52IGp_yuK5s8lxqIS2RGdda1kU_UhbUmU6tcrM54WKpeVj9QNiAqGGO2Snyc6PColRsv3kySEbzsA-GL15gjftSCzNWO_ymy191eOy7qHvPhJ1lUmWn8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bo0dtqJbdbXUsLJKbChDnzXMbPwX6mb0Vav4QtHkkjdkiv-kQRQQc25xpjPWvEjNX9GzNgyNPAUsFX0l0uXX2ilNDOZ2LRDoZszIhbhOYu7ccKa6q5nvyc0pZWwIL8Uo04rRqLPEjCi9JU07qls3S3psK9tWfsWl3EFp_IR8de1GG-YeU9_MJkAYQRTp51Gxw999gamjlgEJHgPYCYuRc_ISrwK3_ZfKNVKnL6mczxO-ln-yQXideWCYE-1uH__7Lko_PHaujCWVOXuE06go1l9wqzZoX_nmtPPCZg0L9O_iv4R_9YZE-pwpQ8_movBubxYw5oHi_k9271lHQqRMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این نت دیتاسنترا کی می‌خواد مثل آدم وصل بشه من نمی‌دونم.
فکر کنم جدی جدی کابلا رو بریدن الان نمی‌دونن کدومش مال کدومه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4046" target="_blank">📅 13:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">موشک ملی‌شکن
🔥
@HexConfigs.npvt</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4045" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vMxnDTruSR9x-088_WV37AQgi4VfWzMGvaXqmJiOO4VgXDi184ZUA_aESbtmTO-tiL6c4pm8ek77sooQ2x1OyYHkjO5nbeT9y6hvsEQhlozhwVhl-YpYb8kQgNArUKM9WiV6mMFH9E1h3pdh8Am57Z1nDdDuMYhUXnH8O8Y576duV4Kp4SuMA7LO97zokgJtuczUTXBd6toF-ce1ORQn9wH9q-QCCbiDHe6iqp1744xU5ADWZP0oy8EnLtEM129TJGPZ0NE2apySRiPkIa32yPrixvChG5Yezoi0FyYb6LAy310ixizpS5ZEUxUDkIjmlbElj70mRwByYqoFaRksLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4044" target="_blank">📅 13:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB
۱۰۰ دلار میده
باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4043" target="_blank">📅 13:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چندتا نکته:
1- کاربرا توی ردیت گزارش دادن که برای استفاده از مدلهای anthropic زیاد به باگ می‌خورن و علت می‌تونه استفاده سایت از apiهای دزدی باشه. بهترین نتیجه رو با GLM میده
2- اگر از GLM استفاده می‌کنید هم، یا به ایجنت فول اکسس ندید(که .env) و اینهاتون رو نخونه، یا توی پروژه‌های حساس ازش استفاده نکنید</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4042" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu-sT6demre1SeGIHehuaRMocUJcrjChB_Ehai2sgYXouibOPqpYQxlxWsnESF9m6Ae26Usy7RVIGEeiui5pBcmTicLhR25a84yNk81pk8wmp41uri04gqD6_ghZy8YsFHZ66DduJ-nx3mKsFlvC0ms_NHx0tt-OuTHTs2XEr3ctP3ZE0Eqx5-j-pun6Z_4M-5D75wddiLxThLfS7mh7qqqcYcbnN2Mao3SxR3_4Byhkme6q3OW-cwq8noiZn1HDg2eBDQAYnGuySOVL_U1SfupK0SMJn-Nyp2oNESnk7N7RJYKiIf2LL2aaltTpWNXO3o9xfSVFZ6aINCIQgTXeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایپی 188.114.97.6 دیگه سفید مطلق نیست و با ایپی های دیگه کلودفلر فرقی نداره. /// البته رو بیشتر نت ها به غیر ایرانسل کانکشن خاکستری نداریم و به راحتی میشه به کانفیگ های پشت کلودفلر وصل شد. برای ایرانسل (و بعضی نتهای دیگر در برخی مناطق) هم با استفاده از فرگمنت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4041" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LIoZMTo5-TCBAz5VlSU4r2txX2Blhwi8XOGN4vdVAOqlRJ5mwkXyXZnE5INGZHyXkxJcURwRPXqXtirlAkPDo6-4qea-pnZHVcWwJHSqLEOdlRTDQh8mqcnL0aprMBXB1U52XALhPNkJrfM7McG-pe5MZvvfN5h0Xw06q_EwgcSruN-tYpHbQwD-46LlRZGW7r9QQZ5kV_JNev84ZmjI5NibJA_hSolFX19KjHPwEOUzknktLr3H5leRJQwzckhRPZnInVwYz8PrXNGJVP0nWWaeHWt7uBKgXagums4xb7vMnuQtrfuEdbbtY_ZMeO-bQZd7BcAkXvAmQWJYKFAk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4040" target="_blank">📅 07:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R4B76WvTVzd9NPKAbbU_oyhmyeeQJebQiX_YvngmD3oySlo990SHrXY60EsJF6Mzp2cVVZP591yO794j3eq6X0JOhBIkWyp-vcesDSsLvuo66-oTILh55dYPBTGhWw2bYidxjPIjcrFrqz6-g1I6wdiBtvorij8lAL8ZIzAxUySl85cRyX6tUyKUkOJui3DevyacAfF0ha3_KEoEz4NR0SUq4NB3XF0AuuT47rLg6rmMIgGvBU3zCFArF8etjEAMqZ7hpxbltOw7X49Cy6Qw0Pq_A1Dus-mxdpT6dhZRLI_XD5x7UXS3kSUUYTmQ34egURwfM-oFL3XZxf8liy3G9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4037">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKXxvX6JD4vQ0f7l0vTJjtCy1pmxmWME62PkhJ1Na0alg6Tiq79NCGqQDWnA2yadDpBTwzopboNcOPX5NNeA1vE8NElGs7cvMw1KN3Ee_faHNLnUx4m55VrjseVsQXeTFHUrROL6eKjtDROmPOQvVjopNP7_94koHo5s30PkJJsEvpPaDypKC46tWIbzIEQoarbRSqTTo3kFrfywWSUBzqBnUthm5wrG8sAlDIITIMpuj1CsLtYmuVg6HmVbREkEA3AmreVPfL5S9F-qVVb9I7j7w8GmQds4Ireh1p0S-0pxXcBp5-QGikxKPoGHTN-L8k7_pSGAdN85OjPDxA_O0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.
عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:
https://t.me/MatinSenPaii/4023
)
این ربات تلگرامی که One Shot کرد، کلی چیز داشت که اصلا من بهش نگفته بودم اما چون صرفا فکر کرده بود که "منطقا" باید وجود داشته باشن، خودش نوشت. که خب هم خوبه هم بد.
و واقعا نتیجه 20 برابر خفن‌تر از باتی بود که با MiMo(که خب بنده خدا مدل رایگان بود) نوشتم توی ویدئو:
1- بعد از اینکه ویدئو رو میفرسته، خودش پاک می‌کنه( از روی دیسک )
2- به لیمیت Bot-API تلگرام اهمیت داد و محدودیت حجم 50 مگابایتی دیفالت(قابل تغییر در صورت ساخت local-tg-api شخصی) گذاشت.
3- کدها به شدت تمیز و مرتب و با structure درست نوشته شدن
4- خودش چندین بار همه‌ی فابلیت‌ها رو تست کرد و تا مطمئن نشد که هیچ مشکلی وجود نداره، تسک رو تموم نکرد.
5- بزرگترین تفاوتش با MiMo این بود که میمو صرفا تف کاری کرد که یه چیزی باشه که جواب بده. یعنی اصلا فکر نکرده بود که این قراره یوزر بیاد روش، روی سرور ران بشه، قابلیت سرچ کاربرا باید چطوری باشه، لیمیت داشته باشه حجم، و... . اما GLM کاملا فکر اینجاها رو کرده بود بدون اینکه بپرسه حتی
6- مهمتر از همه، یک بار فقط بهش گفتم و همه رو نوشت. نه گیر کرد، نه اشتباهی کرده بود.
حدودا 5 دلار مصرف کرد و حدود 140 کا توکن، که به نظرم ضریب دار حساب کرده خود AgentRouter برای GLM چون اونقدرا زیاد نبود کار، نهایتا 1 دلار باید مصرف میکرد برای همچین تسکی.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4037" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4036">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">می‌خوام همین رباتی که توی ویدئو نوشتم رو، با GLM-5.2 و همین api رایگان agentrouter که گرفتم بنویسم ببینم چند دلار مصرف می‌کنه. با همون پرامپت و با Cline اکستنشن VsCode</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4036" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4034" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4033" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A74BqHTvrOZqv9-FnqwS6AuweM_YumRh_oCxaK69BFSDeVUlAAVs0XrHwwRUAVjErYTD6QtunVCplOqnofdpU6sIo_ZuzPY4WQ5T6R1G_XjJuQ6AmcerLsG0-WzKUQdybLEnFl_HKF3dOTtMU-gOeWl9yY-amHLPZyP_P1ApM7kFb7uA5xNzT_nxqP9WrMs0MNhtUKDB7Rwir7UHjFPgUjJkznpAQ5D0JNcIbjg35VYzrO0D8riImczz0g1-_hs1jeDUJTzj9Ax2GMn98ZD9cc3h7vTTDL8vdbxHe8MwkgE6vqz-HJTd4OmnYeMgoKVcMwQKMb2XOIBHP-AHnqt2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر براتون سؤاله که چرا OpenCode انقدر شبیه به MiMo هست، باید بگم که میمو خودش Fork اوپن کد هست و بر اساس اون ساخته شده
🧮</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4030" target="_blank">📅 23:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4029">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">واقعا یه سری آیپی‌های تمیز کلودفلر، سرعت آپلودشون خیلی خیلی بیشتره. الان که ویدئو رو آپلود کردم متوجه شدم قشنگ.
خوشحالم از پیشنهاد دوستان که تست سرعت آپلود به اسکنر اضافه شد توی ورژن آخر</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4029" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4028">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شدیدا حس میکنم یه چیزی اشکال داره راجبش ولی نمیتونم ثابت کنم
😂
۱۵۰ دلار آخه؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4028" target="_blank">📅 22:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IrTV8rx7Bapx0MpgPwyUH4g0ONmwT61TTyxNfw_76c6nMja4_HIbfnybeziaIwVW5H7ePYQGA8kl6Zi7aBRMPme10WdNlrUUVQQu48lr43E4C4k1doC49RqGiz4pN7pVknG1Xfr29BUF_fen7qvF23j3Ir3Maz7BSJwF9SoeLGvw3i2raDAPYCfOUWVyleAUYfPVA8uw971yneylZmbWm8y-US4SrebeaaYYfrO096F9ojHvghebc-VtI4qcECfcIJ0BUgI9fwY2cCtRNrLQedvq-k7vGKYtTy6j7HU5i3oG0Qs0zZp60s0If_4cZKUMLmbWeg_FmfTapalnd7Tuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TKtJllo-sGGTZo4fmsqCipoRvglxeC2Zu0zNtdxtIgB3ZFKwmb3a5svCX7v9rAjUma089q0pBmmQ9D55Ra7yCRA-XjpxwYGeh8IwKVkziFp_3USAGER8fIGOFSj1iPtqUx4W87TDaTk06HwXYxHFXwyCZrEEdFR5CHgxn8KgEbmYSTbqUV_D6w1WeVOyxzNptEAgQL26gmKFW2LmfV_3Ke56st2pLk8cDDigjlUY0ptuwmJ0JdE33TyrA61H7fIDEF5H3Tf1g4tV2epZW5BXKlxkJS_fTGySxVs3SBiOsVDbJ3XLvM3WjzMJcE-hKtxhh9BCo9LQjbCZS8aiAwQBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LvjJzkfCpBaCyMqiNPAT6jH9hfA_yAt3g6BLMH9OhmvDuyAJQXus_H60koBusEZmX1kumaoJ1gEaxrxiWaN-wITG49hm3NtN-y_Nrr_SIP886LS-ZGaGRNGBStzMyR6yv0gSgYE_tiR3nwf7Yahk8SqgAfPzAGy4Ar6kNoocgHIeP_GwZA4UlpzHfBe5-ERReohrvoGMVdwvnzfl4le8vMQSXEVjsMJC9eYBGXj62bSaVdembxXHpFpHqdy0OG7bStAQTISpphXrf4BJnrJIyv_YnJPv_LOJ9Y0qsB2AWYqxn-Ec2SPtP_Q-vT5blEkjMUK_eOmaVJCr7hyfGCAKsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HcESLU2Y6_WlIsY51EV2BVbclnAt8rbACYz-ZX2M_z-FOng6CNaAsbfB2I_5zKt3PVyxGSojXLEnUxiWzjq0Fn7LWz_J0kTyjvW13lW12SZVzyYiHPufUyCYSQNcGdvqLCilRmJTrsmRrLY1i0szcp2bn9MzxZb9MFJz_Tqo5lvWtVjlWoZs3XFJGx0OKitaXkV8iJCcS91EiTiLehx6BnyeiYo99KcxSNN--OEDwKa52UqFrZvv_A0VBieLDe0VrS5eeAEkBKzI7N3Ly8uG7P-rNncw823atzgQOmnPQWcdT6c93CtY8gzNZ39WmQ9lPYqzqUFKQ1MMWRQwdVeoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p9851YZZksgNAoD4ByUFPmt0Kgl1yD7M6ZhQcBNZk-2Ws74zjEh1CWs7sjII2fI7uYIDiVFoBFnLcgcfs7TD3V2O8lSDqiEFdw6tBTnatk2lPT_nOUNksM8tDPNz66n1Xste6EaEVG0yrQNF27HXsTsomL5tNpVNR7kRy3FDs6uihY1Yt-eBR5vAkkffL4kkpvFq2EFseI3aaA4eGyPG0qv6qHian51unCmenxBXyXYRxgwqTf8HxN27Oq1F1g84sxnmZm6X6HX-Cx9B0s5Mau7CT6iJBEj9pd8rh3IRZ_hK4RCh_4JhUpyPGXVLApz1vPFdBBgrdODwa_MUxSViJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این وبسایت، می‌تونید 150 دلار کردیت api برای مدل‌های
Claude Opus 4.8
Gpt 5.5
و غول چینی GLM 2.5
رو میده.
مهم: به این نکات توجه داشته باشید
https://t.me/MatinSenPaii/4042
منم الان 150 دلار رو گرفتم. با گیتهاب ثبت نام کردم ثبت نام عادی disable شده بود توسط ادمین.
برای موجودی بخش wallet رو چک نکنید. از منوی همبرگری سمت چپ، account settings رو بزنید، درست میشه طبق تصویر.
با تشکر از
شهریار
عزیز
فردا استفاده می‌کنم ببینم چطوره:) ایشالا که نبنده اکانت رو
من خودم با لینک رفرال ثبت نام کردم، فکر کنم ۱۰۰ دلار بیشتر بهتون میده(به جای ۵۰ دلار، ۱۵۰؟)؟ نمیدونم. این لینک رفرال منه اگه خواستید بزنید:
https://agentrouter.org/register?aff=PvaZ</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4023" target="_blank">📅 22:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پارت 2:
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
پارت 1:
https://t.me/MatinSenPaii/4021
#MiMo</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4022" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F7E7-2mQb_qJWGB0ydc_wJtAtQkRtykPDzPKZhKoe2rpA7nj1t5kUWt930owYSyeVmYldGIoOikeebKSQ2e_rgP42mAIT5kZX9Qabkj_r1mrC-JIaOJ_rvQ-0fMfPLlzf1ON2dROOR3EeSW3XRz0vUgaG48vPOBeCf5AcXNdeI5w4-EIcH-lhgMgUDlw7t1yDJzG2crwvWfjS_uPZxS3wyxYh17SCcrKrAM9eC8QTR7CNR2kUSu9LrG8fecZGKOMa9y4M41dT3wjAgGzPtbvvoO-OeyXwJNX9djlLkMi136sBBZ4RXLypFQSdXJfcLbCsXQQtvFPjowzrU680lw6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:
1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید:
https://grok.com
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای مختلف رو نصب کنیم روی سیستم عاملمون
2- ابزار MiMo Code رو نصب می‌کنیم
3- کار باهاش رو یاد میگیریم و مود‌های مختلفش رو بررسی می‌کنیم
4- یه ربات تلگرام تیک‌تاک دانلودر وایب کد(5 دقیقه) و وایب دی‌باگ(50 دقیقه
😂
) می‌کنیم
🤎
اسپانسر ویدئو:
شمع‌های دست‌ساز لیرا:
https://t.me/liracandles
❤️
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
✉️
پارت 2(بخش پروژه‌ای که می‌سازیم):
https://t.me/MatinSenPaii/4022
💰
دونیت</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4021" target="_blank">📅 21:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">توی ویدئو از عمد وایب کد کردم صفر تا صد. و قشنگ می‌بینید که Vibe Debugging ده برابر Vibe Coding زمان می‌بره
😂
😂</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4020" target="_blank">📅 20:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویدئوی امروز راجب Mimo code شیائومیه. و با پلن رایگانش یه بات تیک‌تاک دانلودر تلگرامی می‌نویسیم با یه پنل مدیریت کوچولو، که خب چون یوتوب به شدت حساسه روی ربات‌های دانلودر، مجبورم اون بخشش که ربات رو می‌نویسم و باهاش از تیک‌تاک دانلود می‌کنم رو اینجا جداگونه آپلود کنم</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4019" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4018" target="_blank">📅 16:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lV6fe8iNa88YIR_8W5oXS6ekh5OPtVAYvYdsKja2g0YahbFkdG_5OG_WwzbyNMLHZiyyTB93BP95WmM9fKkQzDiOl4injn1Hk0GMorfcnPUsejuaOJ7swVCA-1aSpKNULnyDRvtMvbHyYnFfE9DCzCBSiyWqQZ74st8VXxi006LJq0jm7oo-bflDSqmleQ4TecKbETjjVJgPg6qO5lblL-0SUul7K6fnnAsFMZiiK-DsmE12vFhlDuBEMQUrD5m4LWK8Aglsc_SCuTJbM7kUmi8Yx2ABUsWM0hzqKjDPEj8-j-3fsxltcT3r9l0KLUSX6eEU1LAgfmLtYa4BTKIqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تازه فهمیدم میشه با توییتر پریمیوم از grok پریمیوم استفاده کرد. بازم دست اون عزیزی که به من پریمیوم هدیه داد درد نکنه
گروک بیلد رو دیدم، جالب بود
خوبیش اینه که وقتی رقابت زیاد میشه، 1- یا قیمت اشتراکا میاد پایینتر یا 2- کیفیت بهتر میشه و میره به سمت تسک‌های ایجنتیک سنگین رو خوب(و بهتر از رقبا) انجام دادن. تا اینجا Mimo و GLM و مدل‌های چینی، واقعا توی هزینه و... همه رو میزنن</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4017" target="_blank">📅 16:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nlsGU72VU_7it0o7ZHIX43D1vv3H5mBM_bq95yOhmBhYG_r_6kX_deusQWyitNOBT_KoAt5Qu8LGrKPQUXle-TYwwFSLBMedYVGZY3WS0J6Tr571BUInAwWTO_8zjw8GcowAniunV4b5yTvGpZZjmui0CxTpv1ndseSt_MbJ2_IF93r3U5igBKo0hayZwXgZInGrIZZBGsx4vraV-p7q2ca9NbpkrDCtNhLz7Yqb3ZeqwGW5VxxvOkgwNFE90snoIOZ27l0gnzUyMSUkbOJXxbDfLUcfGQGZwo7Srkl53LNYtqeRJAt9oq0NR0KirSM8-ySAzdrTl5acQAQRd876ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه بیش از ۱۸۰ هزار star گیت‌هاب گرفت — یعنی سریع‌ترین رشد یه پروژه متن‌باز ایجنتی توی ۲۰۲۶. مجوزش هم MIT و کاملاً رایگانه.
تفاوتش با بقیه ایجنت‌ها اینه که نه صرفا یه دستیار کدنویسی تنهاست، نه یه wrapper ساده دور یه API. هرمس روی سرور/کامپیوتر تو زندگی می‌کنه، از هر تجربه‌ای یاد می‌گیره و هر روز کاربلدتر می‌شه.
مثلا دیشب که من بهش گفتم جدیدترین اخبار فیلم و سریال رو برام پیدا کن.
رفت که توی گوگل سرچ کنه، اما گوگل بلاکش کرد و نتونست.
به جاش از یه راه جایگزین استفاده کرد.
دفعه‌ی بعد، که اینجا پستش رو گذاشتم:
https://t.me/MatinSenPaii/4014
بهش گفتم که خب جدیدترین اخبار ai رو بیار
دیگه نرفت سراغ گوگل. چون یاد گرفته بود که گوگل روی آیپی من بلاک می‌کنه، برای همین مستقیم از ابزار جایگزینش استفاده کرد. که ما رو میرسونه به اولین و بهترین ویژگیش:
🤔
حلقه یادگیری بسته — قابلیت اصلی
این مهم‌ترین ویژگی هرمسه. بعد از هر اجرای task، هرمس یه لایه ارزیابی اضافه می‌کنه — نتیجه رو بررسی می‌کنه، الگوهای قابل استفاده رو استخراج می‌کنه و به صورت فایل‌های Skill ذخیره می‌کنه. دفعه بعد که مشکل مشابهی داشته باشی، به جای اینکه از صفر استدلال کنه، مستقیم از Skill آماده استفاده می‌کنه.
ادعای عملکردی‌شون هم اینه که ایجنت‌هایی با ۲۰+ Skill خودساخته، task‌های مشابه رو ۴۰٪ سریع‌تر (از نظر مصرف token و زمان) انجام می‌دن — که توسط TokenMix هم تایید شده.
📚
همه جا هست، با یه حافظه مشترک
تلگرام، دیسکورد، اسلک، واتساپ، سیگنال، ایمیل، CLI — یه ایجنت، یه حافظه، همه‌ی پلتفرم‌ها. به علاوه دو ماه پیش هم پشتیبانی از iMessage، WeChat و اندروید (از طریق Termux) اضافه شد.
💪
ابزارهای قدرتمند built-in
جستجوی وب، اتوماسیون مرورگر، vision، تولید تصویر، text-to-speech و استدلال چندمدله — همه از طریق یه اشتراک Nous Portal یا api ای که شما می‌دید بهش(اگر این قابلیبت‌ها رو داشته باشه مثلا جمنای) قابل دسترسه.
همینطور با Nous Portal، OpenRouter (بیش از ۲۰۰ مدل)، NovitaAI، NVIDIA NIM، Xiaomi MiMo، xAI/GLM، Kimi، OpenAI، Hugging Face یا endpoint شخصی خودت کار می‌کنه. با دستور hermes model بین مدل‌ها سوئیچ می‌کنی — بدون تغییر کد، بدون lock-in.
:
📆
زمان‌بندی طبیعی
زمان‌بندی با زبان طبیعی برای گزارش‌ها، بک‌آپ‌ها و briefingها — بدون نظارت، از طریق gateway اجرا می‌شه. یعنی می‌تونی بگی «هر صبح ساعت ۸ یه خلاصه از جدیدترین اخبار ai بفرست پیوی تلگرامم» و کار تمومه. مثل n8 n سر آدم کچل نمیشه.
🏆
اپ دسکتاپ (تازه اومده)
بیست روز پیش، Hermes Desktop به صورت public preview با نصب‌کننده‌ی native برای ویندوز، مک و لینوکس منتشر شد. اپ دسکتاپ از همون core مشترکه — config، API key، session، Skill و حافظه رو با CLI و gateway به اشتراک می‌ذاره. یه fork جدید نیست، فقط یه رابط گرافیکی روی همون ایجنته.
😎
حریم خصوصی و امنیت
تمام داده‌ها روی ماشین خودت می‌مونن. هیچ telemetry و trackingی نیست. از آپریل ۲۰۲۶ تا الان هیچ CVE عمومی‌ای برای هرمس گزارش نشده، و به صورت پیش‌فرض اسکن prompt injection و فیلتر credential هم داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4016" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب خب، دیروز فرصت نشد؛
امروز Hermes رو یه معرفی کامل می‌کنم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4015" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3-2MwY-c-kjGgTIgunQLBksbIxCSZV5g5_syeKTKIaYxB8pVIY_cDb_XRe0XBAGuMCijl0YXzqePMiBOLUk-zfDYBcsGPeOksW7DAclSvKLfg-fQjM1LVeIit5ccWDVG4L4RPJ44-0f64O3i5vwz4cHMFhlSOltXJc6mYj4Fpt2290sAq9TCM2MK-lMy4JdO9-qlGqa2mA7W0hvPv4f3BLxTfGIlqIwqfciuDO_fi2n60yOWcjtnMD1Pw6bfe7XqMnErSiEOVS8VEC-VAeZRVEexcKqiperQ97QHB4zeCu_fViPpDB4Qq5ZVUMjFSJqo8ni82ZSB-Ti4iSJcetZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UTIcbUCDsC90URzGkI5OjqJiWC-m97bT2S1uXInL9bOUqwOa6z--NKiry--xG_0gzh0bdbcaim25oeYQRITWif6pYQScUtiCGeT3MVHhpbeMz-BveYRsBpoZ_wNLjKfW7gcF0HIdDHiN6JVByzpl3jOUXcyxBmmy-egL3EX2r510Zvs3c1B70u6EfhwnnlVOkezrKR72ki36T62Jv9CiSijOkcQQvQEKYeEMmb6tx-pO8r-gNi5Tgk92emcMmWv7UzhKIoBE8a54sUwpTqYFL5ug579Nv973xI60S4d0GHzQNlEHaCX7Le7L8LYHh8eRNNuKaOcTCtjY1ibagES6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U9jQ8IpBsbbVG7-Wpx8ois38faTCMsjyFfHexIiUTK9LliJ79ULwu1d6L7Gnx_-4d_DlXHkXh9D8e5VENc1sBQyz5ABsAnpEYsUW-WHGa_JWQaGhEQse1IGhDeF2q0t-pYQ8Olth9UAu2biMLNWlPm4Hb9Ds0Y_y7XFKmKfYgz07aXmwAREVqgdufIek31_A7lXgy0YZDioCN9m3mMmIUeQlgVHMtdqWv-Mv827Q2-E9eEHVDBazHy4MWJCBM77YhoKSNkVTKy4EXelCLxKgVASZVIli_uBUYtIN4rmG5uJmrmQ-ADUqKyK0ArcWkQpvC4l5i8Y3IqBmA6oyJFxGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/no-AYvNqvR4HBTgM9VVe5PGDpluA4QkLZ1KZGjNaBW5Gzs7ALbLzIsioQpvWm3R_y70SijZwWORu6E5r0LvqGdUGB-VHA3RhdruO_IL02i-E_UH8tBlM6FY4KulWNKPKV2beZD4fpHTDc3WW1UNfWjEDPgUxYU7R48USRyGo2ztaaA_qS6RiZARRCoZoSUDK2zDJm4CG60_4PYMqvpJPL2yHComQINBXN9Z2Ohyzuqeb8LgTsmyzQQd7FM_dENEuujFsJ7mDAnuObmnuQcMQIgzLfhSCKJeMYs1Ia-yo5JjiGNKn1VNGOXrO6xNv-cA-Pwp-MKwY8V-QbWoZtvtUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NT-uxWcTIgyRWRyb23slhpgJWwayeZaZMPsD-KtCLuw7sDAYB7AKC8IwrP0IqIxI30CPlI0hvNMC5en3m-iwzkBPLkkxLPPb3bl-yXDbZ_DpuY4yq2QbHOUkiMAzPsUm4RjGBXk1ZRqXCbm4sgGWLFCEmjDSIGyctvY7WRpZrE0W2UT_rlyn3zXhKKGRKwkcNBkZS67tI8_HAiq076n2xcu4eGWcDnwiIYxeNs9-AwhwPiLz7xG0KEp2nxs_N0Kgav4gKrtlxM8HEjwYS-jGYdeOAoLKZlWSltqX_ZgfJ9P9bxC6CLEdGM8yDbcFaWOxSBkxqOzhqc2pI-nZxbck7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaNwwqROuuC39J-12Z2ne1CKw4hY7x48BwZu90Qj_0UN7OyL2z87DGjB6oPrXmsRhN9EbKRW9P_ugkHCisOx83C8aCsaya_B-aMsvh1WLOBPjT9jbcVGRdHqve6NFxXoRJSDRrvE84EEtLQcdbohcMge2ydZ4x6mbdkvkSuUGz51K7iQ5oUcx334vc89NlK3SgeDI8h-HE5YACoEZdJBzM61mREn0g3Hrr5-sY00LLtLUbAQYZFZaPn6hw4gyux2ltMyjS8oPpUlYqCAAelK1SKAVromz9pS-k3d8KvMNGaK33CBRhX94g4yedqn0DPm2hbXPorOuyBF4iIhqYRO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">از اینجا مستقیم میتونید برید سراغ آفر دیپ‌سیک رایگان اگه گیج شدید:
https://www.openmodel.ai/event</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/3992" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/3991" target="_blank">📅 15:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k8SOW4qJav81Xu2DraEBauOuCXS1X-KNBsJlRa9Br4qJEK15HWNP_hCyQH0MPE7TKIZY8DaAOIXlyyfjly9IoY-TtwHK1-lzlL5gFeLH_gAe1oQWAUS81ZM7ilyB5HwBB3LC6hFB32a6YdyKm5LMM0iQRqAGenTrmLcw_P5lSKUDAwYHZozXwHXCNBa2wr6hSAKL0-7ur98YDbzddsZ0lyohoMGZRygEXSvdG85K6X4oSsP0VhP8CRAfUgrLtuSbLgokjWvaQ5qplUg5Ahf-xmYnwKIjkfWBOTZ6vVxdLXSVi28Zj3JPysawXEGiJIoBHr86rfMBmn8GK0HxbYfRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده
https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3990" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VET6yt3-MXsXKi6-Sewps50EZjgmmptNn_FyhfPH9S6z5PRQbMUUKn2l4QoWin9XrHp4fV4VmIf_Os2mM7gCthjmA0H25WVzzFT6m7HPn9t_Z3ZBiatv32W10EgkV17yd1JPYqfhDd9H4weY3xoPfaBMJ1ck9Wypa6sAP25voSfk24Vqz6eVvpikLdA8LMqcrwU96Y0pABBov-qKK8nR8TEnahREGHDLpuJWAjmDW2OZBuBjCUzVcL0HZiCZ-1OZyrC1yqa2c9hQsHILIdF9Pj5u1QL8SK3Mns0Hivyp2i-D0UbaYaGdXIzEA8YA2v-KsgjSQFajJ-Ot2G9dCVkFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..    Site 1: retrogames.onl‎ Site 2: retrogames.cc   @Linuxor ~ fireabusefyan</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3989" target="_blank">📅 14:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyK-Bs18AF5u50p04L-Prz8Uh6u8yAlhschS1RIrWRUbz7mZm8OH02qccqUMj0FaCjC279FKujfbPf490Xiop1_1PzgCN16vbusqFJre3LX9Iz55SgtGoHSLMLu5Scmw7-gI9wgkYD-60YdC8zaLkR36NItm1u7Tx8-xV02S52cadgrnUrhcaQxJ1TUKs_AIcGN0KMhmGsle25uW00bIYuy4jBY2hQZ6S9wBoq0PHXIKMmJS46vzw_sRDfvT59SAv4Kgw267zLggEoSRQKV_yx97_8Sj8zjTH02lXhwx49CFt1Lc38QBIOOWW1fA_e4YLUgsYZZd5hC22hCpYoEvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..
Site 1:
retrogames.onl
‎
Site 2:
retrogames.cc
@Linuxor
~ fireabusefyan</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3988" target="_blank">📅 14:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده
اول باید چک کنی آب وصله بعد کارتو بکنی وگرنه ممکنه گیر کنی
✍️
ادوارد وانیلی</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3987" target="_blank">📅 13:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/clpIMCu6wZSs7BdGKxvd96WWl2Kn4d3aP4PLn3peV5NATlauOa39t9FzIEd-87mmiEwD7A10ndBrVxLBbvxR5D9NTmNuplbsYl6zK-9Iw80HCTmJIsqh_mh8UKEblOg-31Cw1af6NNzXhd0VP8FcevV3D_MGjMT7FDk9ebviNEiLtZFb1voInjcjmURWJ57V3iY44ZME75ceSvxMQs0k8mL3bm7rDrGqKG5F-7m0fQzKexFTbaUIQqCnrcEr652p0SgGWfOvd3wQN-BF2UrCtWDGOJcsXEyRoglrLEvY8YFyhUZWLTfOrOErqwQ3AW4vi7KaW2-ImxawAjBUV3NWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید که توی توییتر یا جای دیگه، ننویسه عکستون توسط هوش مصنوعی ساخته شده(نمیدونم چرا برای خودم رو مخه) می‌تونید یک بار اون عکس رو توی save message تلگرامتون بفرستید، سیوش کنید مجددا که متادیتا پاک بشه و اونوقت اگه پستش کنید اینو نمی‌نویسه</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3986" target="_blank">📅 11:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7NxSQ6om1bQ3aQuS5klKp-PSaNTzX1eYhvLLcb2TgoYc_4ziTeoq76MCG6ilKqYyVGZLyHrTpQOxQUGDl5GXO7pZUrEf9ZtlVCeDE8HI8kAjh9s7e4niXK8jLVhuQVYXLW85NqBU8orfhfwYbCFtOdlMpFB_LY50dQrdCD0Mt0v9u4roeAvQ2IJVyXlS2TBESfISqcVmL22OaQM6kYD9AByM9N6_qX_r9CSDGQoCIoY4F_IKO6BTk0D94N3ARW9dEN4iaTT3fT0aeoJ8KLeLXACzVAZdM82RClbvh_FM6atmN_Sh8AsSP67W5VNJHLJoiEUTccpQnpXGSUD3gVXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIwana?</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Iwana Proxy_1.0.apk</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔰
Iwana Proxy v1.0.0
با این اپلیکیشن میتونید به سریعترین پروکسی مناسب اینترنتتون متصل بشید
✅
آدرس گیت هاب پروژه↓ (اگر استارز بزنید و بازخورد بدین اونجا ممنون میشم :))
https://github.com/Iwanian/Iwana-Proxy
مثل همهٔ اپ ها نصب میشه، ولی خب
آموزش نصب ایوانا پروکسی
@I_w_a_n_a</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3981" target="_blank">📅 15:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">با تشکر همه‌ی بچه‌هایی که PR زدن و مشارکت کردن توی پروژه تا به الآن</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3977" target="_blank">📅 15:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TytViMIqUoeekJuOQwOcVJBpTgpx7OBDxDxD3L5unM6_PLBdtaNrvRIuZSby9o2kFokvCTFb9Q8XDDcDCDk_uPn6wFhswWTj0JZs2zwi_v6YfGRoWbFBVHpXC-M7hY14udHanu7Cx_dTtgmRO1vEDPSwFq3o6MM8oqYMM2k3bf9SgJNVFcyEsYd4KqSS4SR4qfgho0PL4z4UeOuTcHCEdgBuveygV3M0wxIamo3wIUh-vsDWgefEZVceJbxN00uHBTcgoDgEpEzs68L0WIlbaIGOuxFWDxn-8QYlDJBwFlhpCObcDB6Ifn1mbiUwfrphylVO3eCvOLZquq90TCEUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/myeYz5LKk7SlHYGXAjEsbT51AgmZL605osqCTZeypzjRw2FHGTqYJ0BURiopdVIB9xovVrN2sHNcfQ2Nx0bS8AMzxCZEo7xxRbhrRz5TQeoCs_-C91BJb2xPipn_PYgrLd_GH3RAxLBpD1CQ0cWEKXQZnLVu3R60hmw8U20x_wHhMLopymx_SwPEll4dM0--I-S-sqU-pmHVknAS6uszWGhNh5BpGjf6Bg8nI_3V1ssYwXM1sDRnjL-TGYBC0lC5c6-LKcUB4b0V44VqNqNxFVRnOS8WhwIK4lI-bKhLg3v6vzicsR9iulH06hJpf8M6RJbaFFKVTs6KcLUHU8cDGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متوجه شدم که SenPaiScanner تا الان بیش از 60 هزار بار دانلود شده
سایتش رو هم
Samim
معرفی کرد. می‌تونید آمار هر پروژه‌ای که خواستید رو چک کنید:
https://github-release-stats.ghostbyte.dev/</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3975" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3974" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بانک‌های ملت و کشاورزی هم Came to the party</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3973" target="_blank">📅 13:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3972" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QQx7Q-8SeZSaGKbZKGBCxKHrvK9Ncupq1MeV9fOCz-T-0Ks9AeFWI62BbN--ILnxh7cT2ynpuKKrpQ2nCaAqfsH10GUjMgiRDB5GuqjjejQtrMXqR3N_aLQhQbuC8m8ptgFR79g5h04CY8u1utbvegnduzL_xHmYLslYTemjV0Um2DMjWUVCZ-Go4MLh4bRfPYown41ezbI8EnjdFhq08xMbgVmWpmsNPMOKz4s4J9-iT_n2jbSTwZJfEzJzcoYIIgzWFBVK-2FJ7NVEKB1ktusaIK0bo3H_YaDn-z5MkPNLl6fWQY19Wotuw6GHBDL8zWAfwpVteBa8IXS8z1zXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbQvUXofLXoOsHCtCKLW0krZ7KbqMw7vheGlnU48X5CNiJYynXhAXbNOUOo7W1VLlzuEY6P23wD9LLc0KDcr8Tp_Ifw8xMKsZpazZRMWvon_aNkxttmzhG4OG5VrhFjAoAnVqb-8YdPtckMNBRLpBsOXDhmQ4xL6Sd2bGy4iheF0ObR9LYxubotgaiwHs_yBkBE719bYYaQ4qEYiaXI-FRhzKwCyvgDcEm3-_cfAeSPcqVFydu7OdmJ2A54cr5ti0fBeyP_wdqe4k8mPwFBDVpbyYzy7mSeGWt2OqQk3TC_0PUKg-soGA0tKWIEWjHInm_8LG1F3QNNiGh9YMxZJXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول: یه سیستم که تقریبا همه‌ی گیم‌های پی سی رو بالا میاره با بهترین کیفیت(عکس از
glock saint
)
عکس دوم: لپ تاپ tuf a16 ایسوس که اون هم خیلی از گیم‌ها رو بالا میاره به راحتی.
و طبیعتا با لپ تاپ شما هزارتا کار دیگه می‌تونی بکنی که با Steam OS نمی‌تونی</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3970" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NOGO3N5dM_HotCAEOUGOMe9oCv2RrmRLqhrwrC3N2kFpKUCgGVdx-v452Jx0vcraMpXDa_lLwJ1i2OzmOhPVvInlp-HyEDHUgYOpOHIi8qsOLVi1bH7rlNvDQPOo1e1GM30ts4QDwx6ydvTxuRh8dmgzjzIYMKUZvdILc21SXHZrg0Ofc_NZ1DPVcw2Q6HdosliZrlWFOJbog3BkIhClEf5PQFoZLo0wV1ZgxRWgFN0Zdy4RmtHzKpl1nvkyzafsDc05Yy0QU7IIjcknh2OSc69uQiQpdlt_E252UAORxtN2nJfexw2SHHn5oVgBWx2v-jlBUjPoE3p1evmDNbl5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oBfhvmoiE8DfWHQBArY-bNaMirFjTVyf2Ze418CTCio6-QKGSp42DuWZlfqCn_qpZhJhVtoj23ah4CbMbS7MK6GKBKGwOIbCPbIMIBHeZLWDsWjCZ0xPU7cSci-I6GRRxB99tzJpeqSImdpfiAKPM5KfEMpHcrdEEjJUFpXtVfG2e0WMWIGqhZ0YZXPzI6aFchrGrMr6K-4jA-WOVYcs_swlQNGZJ8e3-x4DenwwMtv_ok2VR94pbRRmgGBnJU9s5Mu_JYiUHo0MgHjZpHCxQURmvJfy5qrToOESdBCwvSMXFL1dl7ixm-yxPFm3RoS2l2YzOYP1WKIRjcfe3EzDKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنسول استیم ماشین معرفی شد، با قیمت پایه ۱۰۰۰ دلار!! تازه دسته هم نداره باید جداگونه حدود ۱۰۰ دلار واسش پول بدین
🤣
تازه پلی‌استیشن ۵ پرو با اون همه دبدبه و کبکبه قیمتش ۹۰۰ دلاره
نسخه معمولی ۵۰۰-۶۰۰ دلار
خب خارجیا می‌تونن با هزار دلار سیستم اولترا خفن ببندن؛ حتی می‌تونن یه لپ تاپ tuf a16 ایسوس بخرن.
چیزی که دیدم، کاربرا هم توی ردیت به شدت ناراضی بودن و انتظار قیمت زیر ۷۰۰(با دسته) داشتن.
میگن که به خاطر قیمت رم و... هست که انقدر گرون عرضه کردن، اما هنوز هم در عجبم از قیمتش</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3968" target="_blank">📅 21:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=Fg2PsovT2tF9h0duxLZAyxRFm1yAUP_uHrgeP7N4mG3-5u233Med8PQwWZh82uiKE5mNUBdZU_e6dilwxP_tOBtMuDU1gi6XOHXivehfVe_fr_atyeob-iJfIhUvGMu5kb5Rj_Wk2TC2ZJDHvTUUpITS-Qb8DuLDI5dS3gN7BvsjDgipYef60o8yUzrighl-62uOvkEQZzXCtGh6FK0vknpB4IPjFa5Ui2SI-eIc8pRI8vMTt8CvXIVmRPM0PFsfFzru4RMZUYdBzjVT6XsqNg9dnil32DLOx_uqbqDdRvM2k0POlnAYzD2DYyAL9Y6HNk6Zlcug0NMGJ-Tl-UkqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=Fg2PsovT2tF9h0duxLZAyxRFm1yAUP_uHrgeP7N4mG3-5u233Med8PQwWZh82uiKE5mNUBdZU_e6dilwxP_tOBtMuDU1gi6XOHXivehfVe_fr_atyeob-iJfIhUvGMu5kb5Rj_Wk2TC2ZJDHvTUUpITS-Qb8DuLDI5dS3gN7BvsjDgipYef60o8yUzrighl-62uOvkEQZzXCtGh6FK0vknpB4IPjFa5Ui2SI-eIc8pRI8vMTt8CvXIVmRPM0PFsfFzru4RMZUYdBzjVT6XsqNg9dnil32DLOx_uqbqDdRvM2k0POlnAYzD2DYyAL9Y6HNk6Zlcug0NMGJ-Tl-UkqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-dre2Nqd9SGrV-2c_FXXWpn_VAX8kBzuDb8U3r4IUZCQsNHub8Figb0rm3a48kcG7vldGMuXorASVQdOYr0ekxPFNCUD1Rabh1smh2cILQFW-rPctbM29uwDH0kW3KsAWz-6-qKbOwqN6eOyK8Kio9GWubvGSDMHbYnnDer7WQRAPiiDJ1mMODHsoHIlN4du5rQxkc62XiefFcfuJiO5pRWVzMOSTrJKtJY3mGMXfJTjU4rxdoSS0C9pPJNTha4JLiyA24_h-I3GKwqiQ49E53QTLk1X3k1UEwwVsW-svJKHYlf0wZmBLFvdqtOIM8269mhEBiBaEz5t3AZNxN_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/elDx90Qg8iNcchzVSLcYoLJMFRcMf6e9xwIhjyHxGlvJn3d9VbkPmuWFCvmxStrUCDXqhPm_izF-ueBexe2LD5Q0KtMm7E7ZKXdvJ4wxhDAhKTr3tcjBMhP0ch9duhFME0jhiocYngHG4_zodNOqCQl9AeVh2K0J_6HOpWbEzZb_D6AhK7Z0Asusphrew3gprK95d9yTGhNXNbEsy_jtfJaI9xpa0NnsEm5_2yGi-pr-TghrplggfcxQ9QTHWu5Viir9S_pCGNiRwVbazZDyjDNS74jSTkE-1nQ1xuVKpF1CbPhBPM0TGYH2IsbHtzch4POBnEjbPXYfurDMVfezsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXj-QrLTMGahax-l8-EvfcnuaVF64OvgjRvAAAWvyMCCkWUpoLN6PcbmogRIHTA1JO-Y6JM0IPvh3yaJMXcj3FzWn6Q-FaWj3H77Opx6WEZ-Qs8C659vbosBtjxNZn7cVOtpqU0yb52lKWHjmTVZk_z-ucZMGpTR2jL9pF2HjpBKTV00XcDvn7V31FmjPRaHdEb5JeAlkHYGs2OOydcXvZL3HKic8NNwVJAjfGsyH96EiOQsTERUMNNUUyRt1jznRSiLPAB2OZAe2HpO1kZM_JC1GGU00iLw5FlCBlFidJbvkw_o4qmShH6Trpkz22zi-PQ84Nom2gAo0L1_XEFBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nxy1giliexP28IyiaDYxLmYPw_HC6yrLEh5gJDCG8iXHCgHViz2V7gNZXXLacJOwM9-HzOWnQwdOKs3QIxJ01BnNqnEs6RnVgk1X1IS6TTntTuc7GxrOTwVwhvko5vge06hVdLtQPFPt9gCk3OZiWoKIHLSd1z6dAcwAaK_kZx25A9vRWxfCB0W250M78cSs1JbVmb-ytBJB5nmKwvAthRzvubElnrQtPytbtMbbiIyQFxiKstG8JDpf42irXGPqCuorZvU9nbROSecrYZFIPovLY7RN9qDBUYPG1MzZ6eDkt3hKo9j5gYG1eTMTQhWGTUTob1v8QtXbAAK6Us9quw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uoME09wytc6Niw8zVdxvtys1FODTtDW8dgG5i53I46A2oILALGWRb_9wn3WNrnjjvLPJiVeykCCd46ZFk5soim375ddyTWnhASEYs7DDx1foJloT3Y1T-lkLwN4oGYCgjyS7u9kfvO2ZLDy7iPlhHcwoVUV8Raf0-0T9YVd-Jbts-s3DlSV-xWRDgY_C4f6Kh3rRKqFKJPP_v9Y78JG4uoLvQ7uNej9t8mchzeX6F2I8_rxfaBiAtOkDjettFWRM67tp3qDTgeL3ufR5B2IdoO_Q3ULl5aKe9svLuvMGvFUiNjUKMAlgpMm-AOLaUxxuZxHaErcCqyvq4xmfjvGO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DhL2wuayIwi0bGJkifAmL_qQq-Rwe625fWp_XNfJFXBiTqOUZMdo1s8rkKFClkcqADAwH_mjphS9stRkw2sC3c3k0LsCnwhaGaRQXMDwqMqLhMfdxYkO2wYpjdUjBPEDwne0bX9G6oHSrHNIEErpugL4AfAVsYJDYYXZ_Dm6Od5C0b_4xb6gPH9uDV1Lo-TwX4hmLwCRWELPGXkfn7QA7pFJQsuGRmu_IkDgY-2AnzNCd16ysK9guu6DIc1p-WNbELHCnQkcUp7oJLDTkBZurP47Q8VzUl9xtu09Tv3e02Zam-RNsQkGl4p1Ug4UpvXL607NuqFplxVmdShtj1f1ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIM5Wzmw3cmW0ixtIfG1mQxw30Si3aiWQGWpiwwAW9BRWsPjLUawqsNr4b5yvn1QdIbFjzW1p34hv9vLo5aJqTXbK5IgPZW4-pogNyx4fnV-uVhFh0BqW4hNR6ECtl6VvrrfUpoywykGyEsLJPJFNaq9DHETVYHu0aiS1j-H6YA916kpZtGC-upoViAsPvkq9yVn_-J-avi5302vPU3Z5IBcGoxVSG7KVy3Cn09WkowP61rNAywBm628RhCgaoePymwiZ9sPqk0N1Fmndvt-GA6iqHXCB0tLNMG-X1aUPnVDmZJVijOC7ALMDfz8UJq98RkFvUYA8dijiVd9DA2mUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vk1s17Y-eqs5Mj7tgSgwmY9TJZ3v94a6qVinD4Ny7uo06OISUT8l2Reqo8kFmwDI_5IEm201P6_q9SVJB-JSNJiWmQsnLjieVZLQRFmsk_YENN_1l0rxxs_GIGjQBMZzY2YH5eFcBRw7kwm9Oa4kk-DHlt4ukafl0a3j2LyNBbC8NUZxR_VsQ4NmQ11KaOiDQeyw7nF7AaHGwUStKhSDNQuK_tbh3JjfwJAnAEjRziNcLORgbThmpdK00zLqaaF-OranrXqEnb77ikfR4IAJndEg-L-zuauMoi3iFa4Cv7QKsfuWXe8XHaQrKaJAdWizE8AmTmB0i0k0F2Io7Zfo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ibp5wWMc9-jbvBb6MqR-0FkvTj1pJIlsYxnxV2DjIxs0Qvz-01RiXgAScgPRX1MMeto5beQvjIyquFPGEg2gENvEvNzyZcaI6hcwawsqgYGb0qkUNTG-vpjHkkfGlHoHcS9Z_O0iSdFmsSeAABLTJ7nM5f3bpTESksSyQaxN4w3_wAKrhk-dT_jaCnqsj677Q1tecOSf16vssviqMzBMKLN0vq9irMdP9r2Ww6oFqwlUomgq9bntpblkATBUEoNYdHMjnIjM1zCelk2IOhbSb9Eir38UcnZ5neHFNubSjI2JgKBi-L4K7nMf3gvioIXP2bBpaz2SG20An5hfsKd1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OinSV9n0zlTBtlC2JjsT0BfAXGcX4Ig2goIGZ1vkcV4v6EX_RniDCfaFhpW4PXbfrofQ06Fj6MrClUZ5BMzkfHMdE9SeHZOweoHlbDc3lFNNDHAk0F1QI48u2Y4N_DCPHOXdky2UJRE30pxVYgH0gLtVjPp38YvJ35w5Mdc-fxRmqlbvVj29qdCGPyHUgYT4mdYq1Sph6YXA9Tn3NWZ2Q_Ox1UaQKCA2Uhou8z1S50MhrSNpIUXsKH6Syqdvx6gVQxxQGuA8XHcbsxxex8_J_4T5gnsHLn6zqNsBvcE7CWHxyDyaoTr6zT-tbWQS_UTtDDUszhqUWR6lcvsgl7019Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XrmzzYeXZWlEPTTHEI6OGPz9wnGOl64LoSAwJHsdKSO-ThroRWFSo7NJdSHxRguKRzTR5byrEKy4RbpzNVukdPpjSXljqDddRJNxXuGreyjI5ZlC04zVZgsn4JmPXsGItXtSyUaYxclsrAn_hOgB-gSkkuOljxOSnDeEwaUauWnjwzcKLCbPSju3aBbid92jn8RVJWkl8jlHvckAoeQNXV-kGhE6UfwilvzR7h0kVj9EloMIG9HD4jM8z-wJ3OMJBcnZJy3tqYI6diP8GZWaG-pJPLFiadeIi44H_EwlAj_nwSuPgSOCYHCOK4ZQVuzV_z0oCMEVCY5YKzGqrAmozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pchs0Ovx1j-kqi0S0WpfVxtamTZhlD64EG9CnHpoyyqSHuzsC_yHE1OeoM0s9lMoNe8qWZ1ojXhSCShsowHd1qMgxCqd3SYD8daybIGht3UHkgXnqX11aIUUQy0zVOEBZIKL6c65fWc-4xwDJ_UEycAiDsbHFByMZCi2GijVMxnngDyXmi8voWgIib3CZ6n_qPUZnOF2-LVZYr61kvNr7dSRHqDv_fNHxF3Bsrk3C3RNF8lhZFDQQPF2sa-iO0PfHA5DY66OeCRDcGABJJkveMwSMtBD-Q3ecXZKNqmDNrCPSz6Khs6OAz1ztc4MuVOgz_FW3V6lmDvVoUulnlS6bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
