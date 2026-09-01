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
<img src="https://cdn4.telesco.pe/file/u41zx5H1e1syxXueR_Ee0hMXZz9GqG0-Gog22pIFIEgpNw5RcOgftO0lljIcyvMAcjmTUd5mjD1vtWA9W6jNgcASxm_9UFFoiugDlpWGZqTo7iv9prZdG0iFtiOvcEU8ZJUdwSd0Soipw3tpqx4VUaZuyzVNohozQ39USmy2w9g_rHmQygd5LqMjXb123Q7Kb--apRue9opI0jbY5_TNThFf1sl3kJ448idEPzaC8AfusLGfiPZsqLUm-nWjHAieJO337z-3VinIvP2yEFCieeILNjWLCVJ-s4VyQAVrc2QSiFg40JG6ZR1oAyg1_7LSXYQqsBX3f1QM_ayOogx6qQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-459436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1409465bb9.mp4?token=sYUZsJ-afdyBLsLvP9yADVn1z5tqz-eEWSZE0QPtDCYjK9_WBvaXpP_RR-UknCuN4CxYISLjMzLyEf350GbVzOEWcj-BwCJSLNxboDdKIK9oWGdjdF25i3TndhUdXbDO8HkEKuZwQxyf-mEAZ3w0KDGd6BSXBVMEmeivpeiQWrlWAMXp4C8omOiPBWXm6IRw2ed6LhWq7tfLe4WjLi54pskE-EauWFFDqpjcwlwjw_NFQte82imQGk-b82I0xekmPRXD6UstC3gyffm-ZYb3MZ-z-KKroY_WqqGINtW9RLjfrLl6KEMz-jeCf7D2FYSEoo5octQeyBs1EL_wp7tXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1409465bb9.mp4?token=sYUZsJ-afdyBLsLvP9yADVn1z5tqz-eEWSZE0QPtDCYjK9_WBvaXpP_RR-UknCuN4CxYISLjMzLyEf350GbVzOEWcj-BwCJSLNxboDdKIK9oWGdjdF25i3TndhUdXbDO8HkEKuZwQxyf-mEAZ3w0KDGd6BSXBVMEmeivpeiQWrlWAMXp4C8omOiPBWXm6IRw2ed6LhWq7tfLe4WjLi54pskE-EauWFFDqpjcwlwjw_NFQte82imQGk-b82I0xekmPRXD6UstC3gyffm-ZYb3MZ-z-KKroY_WqqGINtW9RLjfrLl6KEMz-jeCf7D2FYSEoo5octQeyBs1EL_wp7tXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: در تفاهم اسلام‌آباد آمریکا مرتکب نقض تعهدی شد که در بالاترین سطح هیئت حاکمه امضا کرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 23 · <a href="https://t.me/farsna/459436" target="_blank">📅 15:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHsEIbSKCcogIGC7pkoz-a27nWriBFKkVb7vUFqeLhMy-1TjZ39Tu3eIhcQmDEzob4Vis2rRWeD2Fm_S1k4_jmXuctpvj4aTDhQ6_MENUY0XzKzJau3N9fNlP1VGCu8c4ixDt5UD1Fka05hloWKbhC9iP64wSSoh4BGZ8KzfY7oxc_aiYhsJUT9xZrN9ufasuJB7zaxYI-g0hEllW437JwaesiqfKZCbV6yTqQDfRA3g7txcwROo0MUBy_6pwnSR7y3SlkR46ipsYn8irCbEQVQvLu4OzoYmT8gUorSlt5CAYSyom0W839JP8vJF05aoO84b57kc_F2UM477r9pnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: نیازهای نیروی پدافندهوایی را به فناوری و فناوری را به قابلیت دفاعی تبدیل می‌کنیم
🔹
سردار ابن‌الرضا: روز پدافند هوایی، یادآور مجاهدت مردانی است که در خط مقدم دفاع از حریم آسمان ایران اسلامی ایستاده‌اند.
🔹
نیرویی که در جنگ‌های تحمیلی دوم و سوم از نخستین و اصلی‌ترین آماج حملات دشمن بود و رزمندگان آن با ایمان، شجاعت، صلابت و دانش، از امنیت آسمان کشور دفاع کردند.
🔹
آنچه امروز در این نیرو به کار گرفته می‌شود، حاصل پیوند نیاز میدان، دانش نخبگان و توان صنعت دفاعی است؛ زنجیره‌ای که باید با شناخت تهدیدهای جدید، همواره در حال ارتقا و نوآوری باشد.
🔹
صنعت دفاعی کشور خود را موظف می‌داند در کنار رزمندگان پدافند هوایی، نیازهای این نیروی راهبردی را به فناوری و فناوری را به قابلیت دفاعی تبدیل کند و با اتکا به جوانان و متخصصان ایرانی، برای تهدیدهای امروز و فردای کشور آماده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/farsna/459435" target="_blank">📅 15:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2815123322.mp4?token=OtDAOhTC04wBmKRGurWuTVnDcnKevM1C17MZxqLHfGo9K3fXRivrz3JudOtzwgtZ3L9mKCeNfdkNEoCO1XudnreFSTqSZoLEOSZMprZ7kpCuYIQZ65H-ixKpiq5E5X5e0v-ArkNhUkvvEpGKNTsqKJ8VI4KrOiQz_AKkn1DnAbxwClzyfqLETVZDQ7Xp2yhLJmwVuXqcutuJkw73grUgIKFmR7rN3xBWSBe7UH3H82j-_kpXYp9m7IxipHdr6E_R6JPO8J0X0t5qilgQE326qrPYxldf4_PX2ZRmcV87EcG26fFXP-jeh3VEO5SBTe01N6pQUmpm8d1ltjUkEi-0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2815123322.mp4?token=OtDAOhTC04wBmKRGurWuTVnDcnKevM1C17MZxqLHfGo9K3fXRivrz3JudOtzwgtZ3L9mKCeNfdkNEoCO1XudnreFSTqSZoLEOSZMprZ7kpCuYIQZ65H-ixKpiq5E5X5e0v-ArkNhUkvvEpGKNTsqKJ8VI4KrOiQz_AKkn1DnAbxwClzyfqLETVZDQ7Xp2yhLJmwVuXqcutuJkw73grUgIKFmR7rN3xBWSBe7UH3H82j-_kpXYp9m7IxipHdr6E_R6JPO8J0X0t5qilgQE326qrPYxldf4_PX2ZRmcV87EcG26fFXP-jeh3VEO5SBTe01N6pQUmpm8d1ltjUkEi-0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز برداشت انگور پیش‌رس از ۲۸ هزار هکتار باغات تاکستان قزوین
🔹
پیش‌بینی می‌شود امسال بیش‌از ۴۰۰ هزار تُن انگور از این باغات برداشت شود.
@Farsna</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/farsna/459434" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fc73ac55.mp4?token=iD3ozy04D0sOkGT6t6qsHpceT9OA0rLTF9tV-zQ0K4z_XR8eM_G4r8JaZjw4EpPGULowaTfkEMYEsd2x8ttcowekZ_D7xuRb7iyg58URRO-baNcGj82TNzgXPDJWRgvLzMcBD8bkh2C3hYW8DZDRF4ItOfaa7QMIqKWCxusEHbWF05vfMJ9z1VMLy23l1ayX5Ksncf1F6Yx8JVKBL9tQgQ6N-IsUZrROgHaeJZ081IAzp8kQ82BMPMiDJSiTE3XAsNMR42UFgmK2kR_2hoxFNlMZPafy9wS1kMkD0YnxeVi3DfRccTOt5OL_W1320CnmTBIJAn8nsF39Nksyf4z5tTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fc73ac55.mp4?token=iD3ozy04D0sOkGT6t6qsHpceT9OA0rLTF9tV-zQ0K4z_XR8eM_G4r8JaZjw4EpPGULowaTfkEMYEsd2x8ttcowekZ_D7xuRb7iyg58URRO-baNcGj82TNzgXPDJWRgvLzMcBD8bkh2C3hYW8DZDRF4ItOfaa7QMIqKWCxusEHbWF05vfMJ9z1VMLy23l1ayX5Ksncf1F6Yx8JVKBL9tQgQ6N-IsUZrROgHaeJZ081IAzp8kQ82BMPMiDJSiTE3XAsNMR42UFgmK2kR_2hoxFNlMZPafy9wS1kMkD0YnxeVi3DfRccTOt5OL_W1320CnmTBIJAn8nsF39Nksyf4z5tTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح‌های جدید دولت در ۸ استان به‌بهره‌بردرای رسید
@Farsna</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/farsna/459433" target="_blank">📅 15:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459432">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d6ce48f1.mp4?token=SvtqsWwMdSDy72sDXbsBAEs9ZviFto2-3BbuqNyGBgn1U-ds-UeMS-qkCanH1CQEKx2PWpSovb39JnbLVH7Zfg76-aCGwkUx86xivn4C8waL1RN1KJ4V8zxE9ycSiruI-cAVdkmejolJDmSRwEwaRD30A-u95TtodBn24MbzpUkIbGCRURj5neTkHSDPLZW03yreUI767XOWSII7JdWDWjhgC1TkQFAN42L0qOF8rm7RaSk-WxDJmPu_Z04Sc5ojsLAhq_h_m_jz3d_c-jw3WhCPMOq8ZhSx_4rnaWQeSzApCdWnO0IN_-7SWe5Ku-csuCM7cp8Z-VrxmKMaTUfbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d6ce48f1.mp4?token=SvtqsWwMdSDy72sDXbsBAEs9ZviFto2-3BbuqNyGBgn1U-ds-UeMS-qkCanH1CQEKx2PWpSovb39JnbLVH7Zfg76-aCGwkUx86xivn4C8waL1RN1KJ4V8zxE9ycSiruI-cAVdkmejolJDmSRwEwaRD30A-u95TtodBn24MbzpUkIbGCRURj5neTkHSDPLZW03yreUI767XOWSII7JdWDWjhgC1TkQFAN42L0qOF8rm7RaSk-WxDJmPu_Z04Sc5ojsLAhq_h_m_jz3d_c-jw3WhCPMOq8ZhSx_4rnaWQeSzApCdWnO0IN_-7SWe5Ku-csuCM7cp8Z-VrxmKMaTUfbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت. @Farsna</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/459432" target="_blank">📅 15:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459431">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=alFCG_bmlBojoMLdeZ-Xqy9G020xBBZsadFTdzeXn5-VHhyy6TD24l0nfsIWJWabcs4eVZXdRndta8Jy2pRK34aYLB-sW16q4oDGmJXLJKRz290-g8NIK6PniyPuces_jj_3iQX_QIfvHfNGk-Ns7MTcrE2-2MxmBuzaM023MP19THmbk3XaViX8ySwDLL6COHTC9xcRsIEXTLe6JEwT4PYO1Kg7GUOYJwe9NzU3DkgEjDW1Phkh3IpTUV8ARYEhRQpE00Tq9b536xzezWKUWCZNQn7SzWg6miDh2xLBg58iBdkh2DiMPvxibEVfmjGTVaotJHwIGkVhA-FBtS-_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=alFCG_bmlBojoMLdeZ-Xqy9G020xBBZsadFTdzeXn5-VHhyy6TD24l0nfsIWJWabcs4eVZXdRndta8Jy2pRK34aYLB-sW16q4oDGmJXLJKRz290-g8NIK6PniyPuces_jj_3iQX_QIfvHfNGk-Ns7MTcrE2-2MxmBuzaM023MP19THmbk3XaViX8ySwDLL6COHTC9xcRsIEXTLe6JEwT4PYO1Kg7GUOYJwe9NzU3DkgEjDW1Phkh3IpTUV8ARYEhRQpE00Tq9b536xzezWKUWCZNQn7SzWg6miDh2xLBg58iBdkh2DiMPvxibEVfmjGTVaotJHwIGkVhA-FBtS-_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/459431" target="_blank">📅 15:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459430">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGz8IIKGGNZYz6EfTRjqakZ3uL4-3lNonyz5k0lQf3TYUWuHiW9lef4sOGnndUB-OlV25J69L-EU7HsSoKGE1Q9FeRkAfV-fJ5aqdZRC-4sjDbfVX2ePyZ5T9a6EcfSTHpl6rqSAOFiLONb3-q_U52RpagYEt_9IRaMsHfFE2zOht93THi2FGBs40VtIDXn13xVpjVvhyqlN3R5FndqryXb1dpIiGcGh_oQIDN2x8HyruRlKvP2ZyX5mkd5gJGqyawqzz5unzobI-UVHvnEujOAa7LfNT-qKgJ4E1rIr_osNa3ziKAWPOn_d5aAAtWhhi3-OfWpv-gGhBjTz7WuUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بسیج اساتید دانشگاه آزاد: وزیر علوم با مسئولان حاضر در نشست حاشیه‌ساز برخورد کند
🔹
شورای تبیین مواضع بسیج اساتید دانشگاه آزاد اسلامی در نامه‌ای به وزیر علوم، نسبت به قبح‌شکنی و ترویج هنجارشکنی در نشست مدیران ارشد این وزارتخانه با نمایندگان شوراهای صنفی دانشجویی…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/459430" target="_blank">📅 14:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459429">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ac79f340.mp4?token=UdNcurmQRMBKqGwCreqZ9n5zaL_lCgZIFMEug3YAao1RjCCfKiN7Nxed6RTILErdI7zQqvhBeEIaOMrLPK1XQvjWnlMFXIsI58bejCchJK46NfRRevZKfEiww5cN1xZybivhcchIjKnP7W3V42AUzweOfz1NAfSugZmgEKxKxinqUeEGRSunYN7xLdApLJ_F_knHL0oWP1VOlCD4bNlOBsx1qYGiX1ct-H_rCLJkZMNeviZnZWrxYlaJDZ33lUfI0LFaH8lLLB0wf3Rvv2OlooAQCHfle1g9Kr9rARLdnztyXOETKYHyC57hxoY6v82BEomCHCxFhdB7Alvc7nk4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ac79f340.mp4?token=UdNcurmQRMBKqGwCreqZ9n5zaL_lCgZIFMEug3YAao1RjCCfKiN7Nxed6RTILErdI7zQqvhBeEIaOMrLPK1XQvjWnlMFXIsI58bejCchJK46NfRRevZKfEiww5cN1xZybivhcchIjKnP7W3V42AUzweOfz1NAfSugZmgEKxKxinqUeEGRSunYN7xLdApLJ_F_knHL0oWP1VOlCD4bNlOBsx1qYGiX1ct-H_rCLJkZMNeviZnZWrxYlaJDZ33lUfI0LFaH8lLLB0wf3Rvv2OlooAQCHfle1g9Kr9rARLdnztyXOETKYHyC57hxoY6v82BEomCHCxFhdB7Alvc7nk4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۵۰ شرکت تازه‌ترین دستاوردها‌ی حوزهٔ فناوری خود را به‌نمایش گذاشتند
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/459429" target="_blank">📅 14:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459428">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695fb09308.mp4?token=jj550WUUoEOQkHHyQSlLcE7M0MNI5HtWIQEIB-QlfMSWD6SAuHPV4NuWllmCSAaNSHzeUXKGFW8oV4ROzuybXe-uFj1cpGkxeVURNmJTqxtibrrxK0L58zp8sa2VLBuz1CiR9_nDk5JU39MO3qWhZXeT3Eg90rkmZcBIp5ykgOnTi1aLH5sxk1H8o9TCiJcDGNxNXs1ytpm84Bm1u1spGL9h57exqgkzRR946i-2nDUBoT5c4sFSxrdGKG_e3TWugN2Z8tXH9EBYlSjRMGXprNIxoVF1kCrHP2XxyfzRNjwxkINUujurTDIMB6J5ajRmNfd7bgI59cOqh34pMycDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695fb09308.mp4?token=jj550WUUoEOQkHHyQSlLcE7M0MNI5HtWIQEIB-QlfMSWD6SAuHPV4NuWllmCSAaNSHzeUXKGFW8oV4ROzuybXe-uFj1cpGkxeVURNmJTqxtibrrxK0L58zp8sa2VLBuz1CiR9_nDk5JU39MO3qWhZXeT3Eg90rkmZcBIp5ykgOnTi1aLH5sxk1H8o9TCiJcDGNxNXs1ytpm84Bm1u1spGL9h57exqgkzRR946i-2nDUBoT5c4sFSxrdGKG_e3TWugN2Z8tXH9EBYlSjRMGXprNIxoVF1kCrHP2XxyfzRNjwxkINUujurTDIMB6J5ajRmNfd7bgI59cOqh34pMycDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگرانی جنگ با ایران مقامات آمریکا را مجبور به ‌استعفا می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/459428" target="_blank">📅 14:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459427">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9648bcef.mp4?token=FE44WTus30JkeVgZnDeOeO17VylOxaZnNdJYQOX6lLGSHhwH3ofhDzd_BK5UF7IIXhlP8SIixflGzfzSZkzZaN3XPMmrLTKzIBH0YqKYVu_KPfWnV17T1TgVv0Dd_Ab0jHpDdu0pHDyDuTVECNFRz0LxlVPbuLNydmBN0Rv7XYeTxiJxbocgsrMNENYGllf7QQ54TIma9j0v4K4jwX_KuJ1QdZplqq1YOWO8se-LPFPoy5Bls7Ot91FhwYjrdJh8Vsd6lcROItRxD-KRaXS9u1o4nK45ChNo8XolUXSvTBBejaJ-SlztbZIx80EqUzA0pU3TWxnFy1QRrBEsV0RxVFMxIhYYtwLmqUGTVU1Tt6Bk8F3pJiK4v0CzprYeNDM_-tEmo9kjn5sCiYTfDJoAz11G31eGN_LPkJDQiCvIDUTtOVhfTyrbsGfizA9mvmMdwDfW_gNIpgNnhh_mU_JpHJqCLQ3iypyZqcGib-hl99gPgWuJKXFSruUQHK5uMma96T6W1LqdI0vMEyG7GQGL06ykD6pgriZRSz1pyXFCeSZE7_nfH1r7yot6BAjuwAuD_zKR5mZ-hVePkKbtzyx7pGGL2mdhbqmvVGVUIEjTij9svu_-yPVT62dySuAWVCxz9kr-XEl8-97C6EXn-JygBC0Bt4maBH5M88wqcztvhG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9648bcef.mp4?token=FE44WTus30JkeVgZnDeOeO17VylOxaZnNdJYQOX6lLGSHhwH3ofhDzd_BK5UF7IIXhlP8SIixflGzfzSZkzZaN3XPMmrLTKzIBH0YqKYVu_KPfWnV17T1TgVv0Dd_Ab0jHpDdu0pHDyDuTVECNFRz0LxlVPbuLNydmBN0Rv7XYeTxiJxbocgsrMNENYGllf7QQ54TIma9j0v4K4jwX_KuJ1QdZplqq1YOWO8se-LPFPoy5Bls7Ot91FhwYjrdJh8Vsd6lcROItRxD-KRaXS9u1o4nK45ChNo8XolUXSvTBBejaJ-SlztbZIx80EqUzA0pU3TWxnFy1QRrBEsV0RxVFMxIhYYtwLmqUGTVU1Tt6Bk8F3pJiK4v0CzprYeNDM_-tEmo9kjn5sCiYTfDJoAz11G31eGN_LPkJDQiCvIDUTtOVhfTyrbsGfizA9mvmMdwDfW_gNIpgNnhh_mU_JpHJqCLQ3iypyZqcGib-hl99gPgWuJKXFSruUQHK5uMma96T6W1LqdI0vMEyG7GQGL06ykD6pgriZRSz1pyXFCeSZE7_nfH1r7yot6BAjuwAuD_zKR5mZ-hVePkKbtzyx7pGGL2mdhbqmvVGVUIEjTij9svu_-yPVT62dySuAWVCxz9kr-XEl8-97C6EXn-JygBC0Bt4maBH5M88wqcztvhG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مردم ۱۸۴ شب است که میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/459427" target="_blank">📅 14:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459426">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f99bac187.mp4?token=RNXqIC6eAXxstFO4MPFyuI0F7M4rkpApmx-UysHn-7c5-L7Yegx8B1RN93g2unkgW7U2_HJSi_VmkQkjopSkX8RelELfS6ZrvhM3e6H_oVFlTPYF2dY_abbfHQpSs02sUyKD7HQuLrAEf7W9ydIOTB9s7vlrYebMAD4-XozfI1UvHFfmAr4v2A7VIKLqDMjqS2NEF1xuawl6bqI-xS7Nr3CucbzvJpvSMz-fPvpGvwgvKSVW8Wou5KNXFbQRKF7k3dtWq_q8Bg-8--lc_qSp-_yrWfGd1aDAs07iIa4Dd5RVWWO7aHMEeq9grM0t-lbPK8cGfYhMM4ZKd5fYPtDpaAZwTeydVE29OqjhTcptGzOO32SwqmEbc83kMCeaQYoXZgP2uo2lANaC0bgjttm-8kYnW8lFkmheZXWhMygr9vH3veRgd-o3iW-5PpUWwAVJEY0WTEklA7bjHYXhWnlgpMowlQBLi1hPL3KcR4l2tLLB57k4nztPYRU11-IvjNHD_uUIeweWDUkMZ-KLDbuTY9NH4bn200cmhwr6PKgMVOz-Y_Dtc3UXWVsNj3KNwqZAq-u02VrbgZIxA0Uj7v8-lUI4UZk-Ry2S-BYyAeLoBOi8Cab6YSNJyUN-ZWWlEXbQtv5C-uSw_Q1RMIUnDyxh_vV04WzM2E6gDCbHph1mNV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f99bac187.mp4?token=RNXqIC6eAXxstFO4MPFyuI0F7M4rkpApmx-UysHn-7c5-L7Yegx8B1RN93g2unkgW7U2_HJSi_VmkQkjopSkX8RelELfS6ZrvhM3e6H_oVFlTPYF2dY_abbfHQpSs02sUyKD7HQuLrAEf7W9ydIOTB9s7vlrYebMAD4-XozfI1UvHFfmAr4v2A7VIKLqDMjqS2NEF1xuawl6bqI-xS7Nr3CucbzvJpvSMz-fPvpGvwgvKSVW8Wou5KNXFbQRKF7k3dtWq_q8Bg-8--lc_qSp-_yrWfGd1aDAs07iIa4Dd5RVWWO7aHMEeq9grM0t-lbPK8cGfYhMM4ZKd5fYPtDpaAZwTeydVE29OqjhTcptGzOO32SwqmEbc83kMCeaQYoXZgP2uo2lANaC0bgjttm-8kYnW8lFkmheZXWhMygr9vH3veRgd-o3iW-5PpUWwAVJEY0WTEklA7bjHYXhWnlgpMowlQBLi1hPL3KcR4l2tLLB57k4nztPYRU11-IvjNHD_uUIeweWDUkMZ-KLDbuTY9NH4bn200cmhwr6PKgMVOz-Y_Dtc3UXWVsNj3KNwqZAq-u02VrbgZIxA0Uj7v8-lUI4UZk-Ry2S-BYyAeLoBOi8Cab6YSNJyUN-ZWWlEXbQtv5C-uSw_Q1RMIUnDyxh_vV04WzM2E6gDCbHph1mNV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران آغازگر جنگ نبود بلکه از خود دفاع کرد
🔹
در عین حال، ایران همچنان دیپلماسی و مذاکره را مسیر اصلی حل اختلافات می‌داند.
🔹
دیپلماسی بدون حسن نیت، بدون احترام به تعهدات و بدون پرهیز از توسل به زور، نمی‌تواند صلح پایدار ایجاد کند.
🔹
اگر تهدید به…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/459426" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459425">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9aBGHhp1S6RH9U9gR4ahYpJFcS9jfZDoc-3lipSLj_6wQNtlH_1GYIr3_p8bWHnbyCSYWCnk78EImHme5GOTjK8jxN6NuVRDHoYWsVhqUu-IEd5bqN8ejg2jGtAjIrom4aKtF8O5ENTzbqADFpe5O9rYbsfjjqYwDndoBmunrAR4oED8Q5zFDNjUueTzacoxXMD-2-c0VKWVOoa_AFzQDoZmRIG92WkbLcipPl5PuA-0MyIoN9q2bhxLTAYjSTyfA6TjYmHSj9xoM3L9z53eaQ3Dj3hfgvrHY1Zv_uHORT93x1q4WCjgPZ1xw6-ZJZojpoFv6T-LqGIbYL21E-Lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌از ۶ سال کیوی ایران به بازار هند برمی‌گردد
🔹
با اعلام سارمان حفظ نباتات کشور، پروتکل‌های فنی صادرات کیوی به هند رعایت شده و صادرات به این کشور آغاز می‌شود.
🔸
۶ سال پیش هند به‌دلیل آنچه که رعایت پروتکل‌های بهداشتی گفته بود، واردات کیوی از ایران را ممنوع کرد؛ طبق اسناد، گلایهٔ هندی‌ها از تاخیر در پاسخگویی به نامهٔ گلایه‌آمیز آنها دلیل اصلی این موضوع بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/459425" target="_blank">📅 14:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8c04b989.mp4?token=NYl0FKR4266KW20t-M1Qt0JHgzfWsiWAmpmEZFZMXGKTnCKjTgGv3Pi3NtF8t-QJSVAAOwVPeZOFddRKyBpXTpo2uJJ3P7V9Zb-TCoV7topifgTHyOmnlnF5v5h5hOhhC6sNWCxz8s195y-oJ2wMmL8XqTu9SmeWHel-JiBf_hbBbLeJwtq6kBiWs1wftFmUyXyq01lZlGM9FIXPPsqVzczuf2ypFSMlEncCKXQ98SXpPPfcZbhxmY3nRTBMa3pfrsEwLS7YbRDKdrwruqmysCSHhOoGhI-RI-TQT1E8dqKkNZNx9mPuZk87b4arVM0tJWOrdVvGs17DtFOsOLtsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8c04b989.mp4?token=NYl0FKR4266KW20t-M1Qt0JHgzfWsiWAmpmEZFZMXGKTnCKjTgGv3Pi3NtF8t-QJSVAAOwVPeZOFddRKyBpXTpo2uJJ3P7V9Zb-TCoV7topifgTHyOmnlnF5v5h5hOhhC6sNWCxz8s195y-oJ2wMmL8XqTu9SmeWHel-JiBf_hbBbLeJwtq6kBiWs1wftFmUyXyq01lZlGM9FIXPPsqVzczuf2ypFSMlEncCKXQ98SXpPPfcZbhxmY3nRTBMa3pfrsEwLS7YbRDKdrwruqmysCSHhOoGhI-RI-TQT1E8dqKkNZNx9mPuZk87b4arVM0tJWOrdVvGs17DtFOsOLtsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار بزرگ در ادلب سوریه
🔹
منابع سوری از انفجار در یک انبار مهمات در شهر «بنش» واقع در شمال استان ادلب خبر دادند که تاکنون دلیل آن مشخص نشده.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/459422" target="_blank">📅 14:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ اردوی تیم امید به حدنصاب گرگم‌به‌هوا هم نرسید
🔹
اردوی تیم ملی امید به‌دلیل به حدنصاب نرسیدن بازیکنان شروع نشده، تمام شد.
🔹
حسین عبدی برای شرکت در بازی‌های آسیایی ناگویا ۲۳ بازیکن را به اردو دعوت کرده بود اما تنها ۵ بازیکن در اردوی تیم حاضر شدند.
🔸
عبدی عصر…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/459421" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42630e22b8.mp4?token=PbxAG_GqAa0L2KxpuWwEXYWFTloM4QUC1FfvvIAhxzB47r3euC86Z1mmjfOBYpHMiTQmnRgOdA9xUNij6IjcjqCiH24OZ7J0Zh6rguwavVL_ESOQn_enshnOYaH40PVSvpUaC41IxfyxxekRiqifoEju0YEZQrj_cYIfUzRffWuH7FRNz8wTZf4js9UxSJKa4k6FelrtUzdtAA5iMBgsgvVCq2MX8GoTZCq267LE7E-sbX6XOsKy61iaLEGRhSw10Wkb2s_DHwjOFJYgETnoJN3MOXo0psw4W9xIZrtbjruDKt4Y-9X-1d_iksuW7iL1DqgUEflz0SBBBG9tPea7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42630e22b8.mp4?token=PbxAG_GqAa0L2KxpuWwEXYWFTloM4QUC1FfvvIAhxzB47r3euC86Z1mmjfOBYpHMiTQmnRgOdA9xUNij6IjcjqCiH24OZ7J0Zh6rguwavVL_ESOQn_enshnOYaH40PVSvpUaC41IxfyxxekRiqifoEju0YEZQrj_cYIfUzRffWuH7FRNz8wTZf4js9UxSJKa4k6FelrtUzdtAA5iMBgsgvVCq2MX8GoTZCq267LE7E-sbX6XOsKy61iaLEGRhSw10Wkb2s_DHwjOFJYgETnoJN3MOXo0psw4W9xIZrtbjruDKt4Y-9X-1d_iksuW7iL1DqgUEflz0SBBBG9tPea7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: عملکرد سازمان ملل در مواجه با تجاوز به ایران بسیار ناامیدکننده است
🔹
حملۀ نظامی آمریکا و رژیم‌صهیونیستی به ایران نقض صریح منشور ملل متحد و اصول حقوق بین‌الملل است.
🔹
ترور رهبر ایران، حمله به مراکز درمان و آموزشی، حمله به مدرسه میناب و لامرد نقض…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/459420" target="_blank">📅 13:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3OP0LNkXS_Ny_C-Nj1v-tqcatn2acAopyUz-K-p42BcndaKihXFLCZ98xOdwcthyzXMduBIXwZc9U4HqiYF0XFy5UVt6cxrJnJfhoZuUGfTq3jN7xwXO75J7lo7JFyZZxSF_rFtbJ2DWUPN28fNZ3mt8NXPBv74ZCx5_5WKjG8dH2U5-eguysqoRI6kgxykNDZVs5AFPsME7ZIelV2LahqIN0zmjS3BJMAEn3kUO5-xlh4uu30x60ZtM7lfxdp_nasKE0BoF0gaOGgt1ljkfNv49cIE7BuTIXzJhWxA_ztvuklW_tDHrJGAbGDWv4jGKgCh5dtNwq7G0idAAMoZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام جاده‌های شمال یک‌طرفه می‌شوند؟
🔹
پلیس‌راه مازندران: ترافیک ورودی در جاد‌ه‌های کندوان، هراز و سوادکوه سنگین گزارش شده است.
🔹
از ساعت ۱۲ مرزن‌آباد در جادهٔ کندوان مسدود شده و از ساعت ۱۴:۳۰ مسیر جنوب به شمال پل‌زنگوله یک‌طرفه خواهد شد؛ جادهٔ هراز نیز به‌صورت مقطعی یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/459419" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVKNeMiltkwCVjOVI7G34tKD_3WKXhHZyggAYD3Id4r3JN0OLu3EHaoKZnt6eQiT8XHIdulfotpAI9VK6cUweXYVCyjHWGn3jRV_zLdqaBU1aIfxIYBunbKGzPvvOALF944K-PNvigZI-pUyzfsZxzvQPAgj8Ml6ifOh1NhUqxfvGNvawLfE61AKHszW2yIDYwxGcdg3gDW1E1d8E6VvQUdjk6UIEVv-5zWBCv3WH6TWAcfWP1BL_7vQ3Ltpwe_8xyKfug_8K_AzT0mtgRLhapKfsNHMZ1LxCv0lkxPg1AJ5IZcCTL_5TXYF92jHDGSUJIphFRPql9MvUJ4TXFqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نظام پزشکی: مطالبات انباشتهٔ جامعهٔ پزشکی از بیمه‌ها به مرز دشواری رسیده
🔹
از سران قوا می‌خواهم در جلسه‌شان مشکل مطالبات انباشتهٔ جامعهٔ پزشکی از سازمان‌های بیمه را یک‌بار برای همیشه حل کنند.
🔹
حجم این معوقات به نقطه‌ای رسیده که ادامهٔ فعالیت برای بخش‌هایی از جامعهٔ پزشکی را دشوار کرده؛ در حالی که با روش‌های علمی و جدید اقتصاد سلامت می‌توان این مسئله را سامان داد.
🔹
چطور می‌توان انتظار داشت که آزمایشگاه و سایر مراکز سلامت با مطالبات ۸ ماهه، ۱۰ ماهه و حتی یک‌ساله، همچنان کیفیت خدمات را در سطح جهانی حفظ کنند؟!‍ این مسئله قابل حل و نیازمند اراده و تصمیم جدی در سطح حاکمیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/459418" target="_blank">📅 13:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر اقتصاد: در جریان جنگ رمضان، شمار حملات سایبری به بانک‌ها در برخی مقاطع به ۱۰ هزار مورد در روز می‌رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/459417" target="_blank">📅 13:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7049a10267.mp4?token=qR44IE4VGv37l9HbjwrHzncou55__qsj57KmwgiXOKX7xxCx88bkpJJMTm-AEaOjsPdM1moWaXcu-Jtr9uIkXuDtdrHKFRFL0f4OmY7VeU7jJ9_Ioz73EDrqIn8wZPsEo7PZ9ZcVWCMe75RQl3zLY2E_QmzMUnsZgNQ-G-RYdivvlpzFxbsqUo2N3oA_lJhYvhgzyG4fTbP9_Gq7D5ZARS2zpz51S9JbHSgphWIVXFI7RmIaoCPoJkBjT-2FF3RKzKaVtAScGu6K5UxtK9FmLAMKMQ4zJGvIuC_9Wd_eBdguW3BSZ-hUECvWNbPTOgm2n9p_9T3Mlb1iH9FF--Jc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7049a10267.mp4?token=qR44IE4VGv37l9HbjwrHzncou55__qsj57KmwgiXOKX7xxCx88bkpJJMTm-AEaOjsPdM1moWaXcu-Jtr9uIkXuDtdrHKFRFL0f4OmY7VeU7jJ9_Ioz73EDrqIn8wZPsEo7PZ9ZcVWCMe75RQl3zLY2E_QmzMUnsZgNQ-G-RYdivvlpzFxbsqUo2N3oA_lJhYvhgzyG4fTbP9_Gq7D5ZARS2zpz51S9JbHSgphWIVXFI7RmIaoCPoJkBjT-2FF3RKzKaVtAScGu6K5UxtK9FmLAMKMQ4zJGvIuC_9Wd_eBdguW3BSZ-hUECvWNbPTOgm2n9p_9T3Mlb1iH9FF--Jc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
گفت‌وگوی کوتاه رؤسای‌جمهور ایران و چین در حاشیۀ اجلاس شانگهای  @Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/459416" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس بانک مرکزی: معماری آیندهٔ شبکه بانکی بر فرض وقوع حملهٔ سایبری طراحی می‌شود
🔹
حملات اخیر نشان داد حتی زیرساخت‌های پشتیبان بانک‌ها نیز ممکن است هدف حمله قرار بگیرند.
🔹
بانک مرکزی بر استقلال و آزمون مستمر زیرساخت‌های جایگزین و بازطراحی نظام پرداخت تأکید دارد.
🔹
هدف این است که اختلال در یک مرکز داده، بانک یا تأمین‌کننده، باعث توقف گسترده خدمات بانکی نشود.
🔹
خدمات حیاتی بانکی باید حتی در شرایط حمله سایبری ادامه پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/459415" target="_blank">📅 13:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1c33ca1e.mp4?token=uwCDD_TZBGtY5PU2RIqowHexLG_O4tYu6L9N8LLy_XTjxL3Hp0hOoh7O9LGXJFzIzycIeaLniiDBGTZd4-c5_o6bNoYi_omTyX8jRvWvX6gkZ8_AAGxNQG9k4UaYl0LahWwEAGW9m7Tfo-YcX0xNm_TxSbkxX3x4GJCqiazoih1KHYW0diNF-LMFbeXn37rQ16SZ69e3vJayLIjwApxNae87GRMka5PUaRhbl9X1F_zuozVeXddmoF21794UgNbuuJPfvxyOMAiu7SoTHL-U76MdSZ681NJQ1gWuZ9ET5Nw61c-20L5Ealpwicgh81Db0G6WuCE7vZiGSlrWGmX4nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1c33ca1e.mp4?token=uwCDD_TZBGtY5PU2RIqowHexLG_O4tYu6L9N8LLy_XTjxL3Hp0hOoh7O9LGXJFzIzycIeaLniiDBGTZd4-c5_o6bNoYi_omTyX8jRvWvX6gkZ8_AAGxNQG9k4UaYl0LahWwEAGW9m7Tfo-YcX0xNm_TxSbkxX3x4GJCqiazoih1KHYW0diNF-LMFbeXn37rQ16SZ69e3vJayLIjwApxNae87GRMka5PUaRhbl9X1F_zuozVeXddmoF21794UgNbuuJPfvxyOMAiu7SoTHL-U76MdSZ681NJQ1gWuZ9ET5Nw61c-20L5Ealpwicgh81Db0G6WuCE7vZiGSlrWGmX4nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت وزیر راه از حملۀ آمریکا به هواپیماهای حامل دارو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/459414" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHUR5LFXT0p79XKSWfFLd1BLhaeP4Afe_VD1bx2rMnZ5cumwbjbSTRBN6XTvXmE8E9SUAGdo1k8I7r-EBEQIt0ZwrwXM7RKq1aUTOftEelJqRNDFPmtLE7-qwQYAl19OwBvA0fN5r_ZjPwdMiDeXchezi1bom9cWu4Smeu5qL7qgep3E5fPZyOBiMqfj5OqnOsn5rSy-fYJkz23Srs-Jm0EXlX8VMc9EaI_kfE6e52NuKJrP-6UU7gJm8FfJxyqnXF_Wz5CMo0AEudA3OHJoD6dN7POu_EvvRqJVJlfbfe38YBlnpFnvCC827IZA1VY9t_-PiuwMP_EnYrl1vy5qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  فدراسیون کشتی: بدهی ۲۲ میلیاردی برق ارتباطی به ما ندارد
🔹
سرپرست دبیری فدراسیون کشتی: دبیر با رئیس اداره برق تهران تماس گرفته و موضوع قطعی‌های مکرر برق کمپ تیم‌های ملی را پیگیری کرده. دبیر در این تماس تأکید کرده این بدهی هیچ ارتباطی با فدراسیون ندارد؛ چرا…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/459413" target="_blank">📅 12:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تکلیف سوابق تحصیلی کنکور ۱۴۰۵ مشخص شد
🔹
پایه یازدهم: تأثیر مثبت
🔹
پایه دوازدهم: تأثیر قطعی
🔹
سهم سوابق تحصیلی: ۶۰ درصد در رشته‌های پرمتقاضی
‌
🔹
این مصوبه از سوی رئیس‌جمهور برای اجرا ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/459412" target="_blank">📅 12:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDB5g3Dv7xfGFa8VQl6bvCt6UzLnV1Trv-ZoKdDu8jU8d1CjOoBIEafN6uRBw8ateicN0Jb_UffiDyA4Z0rRkDur2gv565IfdYr3z2qy7B8TDdAV4Ik3ccAzv4v82PRkQesiValaRE_zEOd5Hd7Ov7BGu_khEQK1WcNiA93nhu1IUOe8IxYWHo3rZ6aIzyBCzoxMh44UOmacOGn3vzI__oApwPy5qK9X9rfb72bmpfiywJc6Z6VA1VNZOgD893CWh-rPIopYxh95oTpXnIlkigGQNCVyOAl3Cu8cxbH6oVO69JCMQsPMM_vs_WTCnQzVI1l6EahqRXXUgv-eIK09UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران صدرنشین جرایم سایبری
🔹
رئیس پلیس فتا: امسال نسبت به سال قبل ۱۹ درصد کاهش وقوع جرم اتفاق افتاده. در همین مدت درصد کشف به وقوع ۹۰ درصد بوده که یک درصد افزایش داشته است.
🔹
پلیس فتای تهران بزرگ با توجه به وسعت جمعیت ۱۳ درصد، خراسان‌رضوی ۱۲ درصد، اصفهان ۸ درصد، خوزستان ۶ درصد و فارس ۵ درصد جرایم را به خود اختصاص داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/459411" target="_blank">📅 12:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcP-LTQqAAoAUVcQ-rbUtm6gv2Hb4xM-_FRNZTRLg-8dk_VblP8ARafzltgnFzuFSftSeSNlRffXeInx0RlDLQsixnCLOsRcLd0xNUmjK7-i0WWfsP7uIslEt91luRhb8u12GhuogzmbTs-kBRTr7iMYR_jWSOW8Pxy3cs1-CJCIwbPll0-l9maqc3R5AIlYrwbLOVekg7Aw4mg9_khQ9C_YwdNK1F3k8b601_86vFhX5YKwCf5gITHJB4CdWSWJ6HrJJc6C3q1o4X2VpdJRWXdeDMQSJVfH_DfNOctigzB_5kKYe6z0CurYaLR7wCCQMJv6gQII1gjgrC6Ukv9IKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از مرز ۶ میلیون و ۷۰۰ هزار برگشت
🔹
شاخص کل بورس که در آغاز معاملات امروز رکورد تاریخی ۶ میلیون و ۶۹۹ هزار واحد را ثبت کرده بود، با رشد ۳۶ هزار واحدی نسبت به دیروز و شاخص ۶ میلیون و ۵۸۴ هزار واحدی روز را به‌اتمام رساند.
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/459410" target="_blank">📅 12:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اعتراض به حضور بدون حجاب در جلسۀ رئیس سازمان دانشجویان
🔹
برگزاری جلسه‌ای با حضور رئیس سازمان امور دانشجویان و مشاور وزیر علوم با برخی اعضای شوراهای صنفی، به‌دلیل حضور تعدادی از دانشجویان دختر بی‌حجاب و انتشار تصاویر آن، با اعتراض جمعی از اساتید و دانشجویان…</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/459408" target="_blank">📅 12:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNcACdv_BGGULcR61Q6D92Z5JEBmAO6_lH1Mz5z7JBVs_MEMBcmx0KrKVJ7T71g3tZF_EhlpcvmnqBe2xuWMFO_077Pxe-F5lgrGApFARz7Geza7hT-FQF-ZJpO8U2Mp1svRjBY3RBN-9GTRsS5lW29c-vQiRjG-L6AzmxILT9Gaic3qvKM5ZbelgMmxeMNEGqZszGO9-bloBeAAkTjcOpoCJ9I9qArVSMiVM4tRZ21Qe4R1w5V80sg2zUcvTSbvtWJr4qDADlo22Rw6_5daMqmskDUVgBet4T8wA0khYYFYgzOytjZRH4uXYT7kMiytqdhser8VicTxa-viy3btmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدیان، نایب‌رئیس کمیسیون کشاورزی: نمایندگان با تقاضای تحقیق و تفحص از عملکرد شرکت پشتیبانی امور دام و سازمان بنادر موافقت کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/459407" target="_blank">📅 12:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXjzTP2OIekzxwMPluk5JBblicLzJPuB2Y_JPIgRk27XNh24eY539r5WIlySn0DdkrQ6QDSW_aN_um65qvaHxEP1vQqB3nfNsEVVJpvNNkdMRrmcxlcC7Hm9Ls0CYEVme92R8ykOw1higVNOeaufftWbtAcvXoWhwACY9vaiUK1_VYNHfiKdtKFs427y42eSNSZRPObgYNjbs59bBcekXvoeYw1eWeOhFCy1KRX1Koc0BbCDs-Mphb1HxBHF7ihXIKiCnTrs7uxh0nB2UwBFeXfzXzuB-OwzUoZ35j9rqra9aULVHg_23CKiZAgZKxuZXTyAD2NvVh-yAJfCszjClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه‌های پدافندی بدون نمونۀ خارجی در راه‌اند
🔹
فرمانده قرارگاه پدافند هوایی خاتم‌الانبیا: سامانه‌های جدید پدافندی کاملاً بومی در دست طراحی و ساخت هستند. این طرح‌ها به‌تدریج درحال تبدیل شدن به محصولات عملیاتی هستند و «نمونۀ خارجی شناخته‌شده‌ای برای آنها وجود…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/459406" target="_blank">📅 11:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803a537e2e.mp4?token=R1H715YII-JiIP1UH08icGgXBVp5QMm0Dje3_tq-Xm04hTaS3tdUGT54SxCjecoTM8z4J0KMivzAEPTQEyX4q-XuvH0GLxciuRx-f1qDN9pB4sow4nEcR4hbOXWtngfYJFwL_7SEl2njwRwwLtOngXzZX9EpDeBj9Y5FXb-PQuT7YsgirBj0kcXP2LyFhNe7HjrN4bGgz9yJBLKEfZnvyb9HeDhf3yFJouxNJtQEOHmG8i4Riy4iU6Z7-l-PBabLoX_LkEMhDLQEWPFuVsf0dcHK-xzJzK3uAxGWChVYqWKyYgyzISef4lkJF_HkFWf_wSxKlXlKLW1DwOxHUPQcSF3mSjYIs0_kVj84mZoLY4steX5L52wn7ixVDnotXt9BVIsRFgCQLOc-VvQcJESbh_75uGZwVmmvtVEURGnIdlD5MOFHFcbovYawSVgVz9PgDq_cLoIiQgYl-uKZtD-Y7Ogp1ep4A23cVSR3XuSgm1f4LI6erFpOgQePKIi81Q5XIYaa1WwpVfDXtMS1iAEHfYa2-LkNKZ8KSMtkgKQCV-b2m7q8wActLtvRwIcAloX8QTtwCLFMrchbXtqk6uJ84YtybgiNsdeOBG3ZTwB2BQTv5xFxKFmBco8OuSPq1xkU85PPvxdD17OHYtTFEX5L_P8Sx0fgvH2BUwuO-foQQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803a537e2e.mp4?token=R1H715YII-JiIP1UH08icGgXBVp5QMm0Dje3_tq-Xm04hTaS3tdUGT54SxCjecoTM8z4J0KMivzAEPTQEyX4q-XuvH0GLxciuRx-f1qDN9pB4sow4nEcR4hbOXWtngfYJFwL_7SEl2njwRwwLtOngXzZX9EpDeBj9Y5FXb-PQuT7YsgirBj0kcXP2LyFhNe7HjrN4bGgz9yJBLKEfZnvyb9HeDhf3yFJouxNJtQEOHmG8i4Riy4iU6Z7-l-PBabLoX_LkEMhDLQEWPFuVsf0dcHK-xzJzK3uAxGWChVYqWKyYgyzISef4lkJF_HkFWf_wSxKlXlKLW1DwOxHUPQcSF3mSjYIs0_kVj84mZoLY4steX5L52wn7ixVDnotXt9BVIsRFgCQLOc-VvQcJESbh_75uGZwVmmvtVEURGnIdlD5MOFHFcbovYawSVgVz9PgDq_cLoIiQgYl-uKZtD-Y7Ogp1ep4A23cVSR3XuSgm1f4LI6erFpOgQePKIi81Q5XIYaa1WwpVfDXtMS1iAEHfYa2-LkNKZ8KSMtkgKQCV-b2m7q8wActLtvRwIcAloX8QTtwCLFMrchbXtqk6uJ84YtybgiNsdeOBG3ZTwB2BQTv5xFxKFmBco8OuSPq1xkU85PPvxdD17OHYtTFEX5L_P8Sx0fgvH2BUwuO-foQQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استخرهای گرم زمستانی زیر تیغ تعرفه‌های جدید گاز
🔹
معاون برنامه‌ریزی وزارت نفت: نظام تعرفه‌گذاری گاز پس از ۱۴ سال اصلاح شد، در الگوی جدید، مشترکان پرمصرف که حدود ۵ تا ۱۰ درصد جامعه را تشکیل می‌دهند، هدف اصلی اصلاح تعرفه‌ها هستند تا هزینۀ مصرف‌های غیرمتعارف، از جمله گرمایش استخرهای منازل در زمستان، دیگر بر دوش عموم مردم و یارانۀ انرژی تحمیل نشود.
🔹
قبوض چند میلیارد تومانی نیز داشته‌ایم و حتی مواردی وجود داشت که می‌دانستیم استخر این مشترکان در زمستان روشن بوده؛ بنابراین نمی‌توان پذیرفت هزینۀ این میزان مصرف انرژی از جیب عموم مردم پرداخت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/459405" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbfytgA24jFjkl4k7X3bC2vQlWJgWzBbPrCFPDQVrOIbxYUp7rjinRLOMtRCjPH3yIbAG2fI41QYgFPyWtAnh0zS6-TJjUbyRQO79fBqkvtP2BHeyH2WJiLXKNrg6lnyHw36qC4nlXzoJiqTId_2qd8YbKI-lqu4Bf_TjODUX1CFKYICYgnSkH8zSiCD2VkBv-ufOss_CF0Zpw_kJa81-t2QzOrpuyk9cIZM5JIedWXQ_pGV-Nv8YOFfVm8Ys_Wyqrbmpopo0WxouFV44izD0bvi8blDZp16J6zAWFe1183a8GkPxky1P0Dl2CkEC36IG1TJpvU2uSIc3mOrgSvgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشست سران سازمان همکاری شانگهای  @Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/459404" target="_blank">📅 11:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvTsQe8NcGInRdqT4zrgiSsXoxM7tqVqtM1ZhdwuOtSBE4WQEtCQjUTTHyjRQTnQj9PKAh_LOgL0MlO2A5-aW_iHc0k_XHq_npqLSveU1To6coMslRmiX_N13Wl3LDiDPkHe8M_V0pc9DQbtykYw0k9vjrUwiwJR1MEOgph8TVbnoMpB9Fzl8J4znycc6tCQ1ycd43Y27N5cNkdS1yDhKcb2k_vP2Qjdnb-4pWykC9wI4Bz3nhB_YcjcFRchjm2aLy8EiNcTE3fkHxtc7sSlC1gjIMtbEAE_AsJoPwvQu2kqVzcXrK9ddmBgEcb8_AN6pI6VuSybZ3SSwHpmzn_BZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقرار سامانه‌های پدافندی در ۳۸۰۰ نقطۀ کشور
🔹
معاون هماهنگ‌کننده نیروی پدافند هوایی ارتش: پدافند هوایی در سراسر کشور چهار مأموریت عمده شامل کشف، شناسایی، رهگیری و درگیری با اهداف هوایی را بر عهده دارد.
🔹
اصلی‌ترین مأموریت پدافند هوایی، کشف هرگونه شیء پرنده…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/459403" target="_blank">📅 11:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0916a662.mp4?token=IBq3pDl03iQOI_ZZxmt6SVcog2Ttc2jNRVSSegYaqiBbNsYBVT_kv7HHpa0g31GcO__G1fWxHqHhHctGneJ2R4ZZArRO3KtWpVr5da_4KPxAKwxM872fcgD3B0r2HH6yQe5I2kNYG9LpQtOwaW2cdmDgaFBN6Xg51pYonRpNcvZ_3dtWO6xGiWo4PWe5rrLW5K317Aaaz03ktAgXBEGpnWKfJNtLnpMtkkR-oNCTlx9DamC4M_Kam4MGFYggbQP2TZI7KmnrPCrPPWBatN23j6vZEupCsGWcS6IhyQ4vMNmpDoEBhmDYD0JfI7E5bXuJ3jONa1seIuco9c9kWku6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0916a662.mp4?token=IBq3pDl03iQOI_ZZxmt6SVcog2Ttc2jNRVSSegYaqiBbNsYBVT_kv7HHpa0g31GcO__G1fWxHqHhHctGneJ2R4ZZArRO3KtWpVr5da_4KPxAKwxM872fcgD3B0r2HH6yQe5I2kNYG9LpQtOwaW2cdmDgaFBN6Xg51pYonRpNcvZ_3dtWO6xGiWo4PWe5rrLW5K317Aaaz03ktAgXBEGpnWKfJNtLnpMtkkR-oNCTlx9DamC4M_Kam4MGFYggbQP2TZI7KmnrPCrPPWBatN23j6vZEupCsGWcS6IhyQ4vMNmpDoEBhmDYD0JfI7E5bXuJ3jONa1seIuco9c9kWku6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: هیئت دولت طرح دورکاری برخی ادارات در فصل زمستان را بررسی می‌کند
🔹
سازمان اداری و استخدامی موظف شده برنامه این طرح را آماده کند تا پس از تصویب در دولت، جزئیات آن به‌طور کامل اطلاع‌رسانی شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/459402" target="_blank">📅 11:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441bc9d262.mp4?token=lpYwKMyi8v1b1ReIo7drDvke8GN2DKlmM0PU2sJzwcbMNxwwFJ29rYkakk1To5HWXxbJpk98dukHfJuFevhaW8ij-ZRElcfkF5RdfpIsq6Ju5ccdq3K2-9Xu4sWnzwxLh0qtD0eITTDi7zZH-m9lDkhVfEBMLY2uCp6_CMdQckL7MUMg9L5oxdPmd4F1hImk0DOftVs7bqWB68T79pTio3WVharIPFN_AvM3h0mAV6st7tBonLhCRfqshobFO3vl4OkgVq5hpp2chAVtH_cnRfj3DPFCjhWWRhrP64cMvX4kwOXzt_3RG3NdEFvonbV9eoJRaBH_GNDQDi8amaNPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441bc9d262.mp4?token=lpYwKMyi8v1b1ReIo7drDvke8GN2DKlmM0PU2sJzwcbMNxwwFJ29rYkakk1To5HWXxbJpk98dukHfJuFevhaW8ij-ZRElcfkF5RdfpIsq6Ju5ccdq3K2-9Xu4sWnzwxLh0qtD0eITTDi7zZH-m9lDkhVfEBMLY2uCp6_CMdQckL7MUMg9L5oxdPmd4F1hImk0DOftVs7bqWB68T79pTio3WVharIPFN_AvM3h0mAV6st7tBonLhCRfqshobFO3vl4OkgVq5hpp2chAVtH_cnRfj3DPFCjhWWRhrP64cMvX4kwOXzt_3RG3NdEFvonbV9eoJRaBH_GNDQDi8amaNPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: غیرحضوری شدن امسال مدارس شایعه است
🔹
برنامۀ دولت برای حضوری بودن مدارس است مگر اینکه اتفاق جدیدی بیفتد.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/459401" target="_blank">📅 11:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8c03c1c0.mp4?token=kLVK8XK6eSvXddvq9ttoqcFdFf1VjPOrk2LAfAL4cKCXpTP-qNo_soghW0w-5xgygrhrk4eXUwF4joUnXKbXVNeokfgYeHGH1O5hQv1mNn_Q3doLiXT2mimhNZodjq51oJieLjyTzZyyf1AQEHvBXyv97Qeea833I88P-_07N_R3WiZ9ewu3QszpfyQtFdv0lVthXsBGiqZ5tRUQ4N5myhF8n_0boTBa8vB2erB2nvtmekzBqE64lu4VQAzpfV5OaRi5MtWAPEssuqCSGjwoCu2iVFTUR03DWtipHsD9DARLusNhl-1pRXawvj_1HoFZh77V9kg3sgUJQ9WbTifR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8c03c1c0.mp4?token=kLVK8XK6eSvXddvq9ttoqcFdFf1VjPOrk2LAfAL4cKCXpTP-qNo_soghW0w-5xgygrhrk4eXUwF4joUnXKbXVNeokfgYeHGH1O5hQv1mNn_Q3doLiXT2mimhNZodjq51oJieLjyTzZyyf1AQEHvBXyv97Qeea833I88P-_07N_R3WiZ9ewu3QszpfyQtFdv0lVthXsBGiqZ5tRUQ4N5myhF8n_0boTBa8vB2erB2nvtmekzBqE64lu4VQAzpfV5OaRi5MtWAPEssuqCSGjwoCu2iVFTUR03DWtipHsD9DARLusNhl-1pRXawvj_1HoFZh77V9kg3sgUJQ9WbTifR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: فشار اقتصادی مستقیم حاصل تحریم‌هاست
🔹
مهاجرانی: منکر فشار اقتصادی به مردم نیستیم. افزایش قیمت دلار ناشی از فشارها و تحریم‌های ظالمانۀ آمریکاست.
🔹
دولت برنامۀ ۷ محوری را برای حل موضوعات اقتصادی طراحی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/459400" target="_blank">📅 11:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMNzFOp2HUX-KkQlCOZFa-aV9a8-at8EmH9U2GNlKvJDg6dco9_Lznw4RoVB8Ang_ZDI0CFe4MRI-WR4aYzaTNOEK1nma-APzenSHz3m2K97wKSorDOGVhd45zSwcwU4BxYwrpGeY1XkcLq0Fx0RbE94rMq6zLvJEUxXWZ5dczkhUYoGTROAw7ZUvrIuBSoL-h8niw7WFEZ05YzPl1lVRcHPp0R69koQ5EsSGF3SnCSeCKMZse9pa9y1EB9tiDCYQohtmnwfus5AijZpJja__pmz-Jtl6MWlEYIztRse3qj-RMiZZJhEb_-5oxyNMeKFjNdCtlnat2bDZHGMVfQkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«میدان یار» ترند یک توییتر شد
🔹
درحالی‌که هشتگ
#میدان_یار
با استقبال خیره‌کنندهٔ کاربران، صدر جدول داغ‌ترین‌های توئیتر را تسخیر کرده، تیم‌های سراسر کشور در حال صف‌آرایی برای این رقابت بزرگ هستند.
🔹
از امداد و نجات تا روایت میدان؛ وقتی یک کشور تصمیم می‌گیرد فقط تماشاگر نباشد، نتیجه‌اش می‌شود این طوفانِ ملی. شما کجای این میدان هستید؟
🔸
اگر هنوز جا مانده‌اید، پایگاه‌ها، مساجد و غرفه‌های ویژه در سراسر ایران، آماده ثبت‌نام تیم‌های شما هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/459399" target="_blank">📅 10:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TexjFY7TZ2xba6-JVGEVDB1H0OyxbM9mqEdCdQONRqiy_xpwzAt0wOT0CMVt9pcNfrtO3jKvg7gAb0C4fT_-hGHZsXWDx4ym2o0zHCRWlRpfZ0T6txi0HeTQOpHP4wZGaunoPtAy7DKkCsBN6TOFeJDheL5-7kkXoxFRsgFeIsguKPUJAELD_YUJuxCv_W6qbrkIuWP7dfvjzuJz6VCSIEKEfOu2sJ5-s3C5wxtolC0ZeyQBsJg8-uu5UH9hFNpYbS_h2Lz4JtTcnxHR49shDIDVuDcTR-FyT6Ab2hQEFLpHACy6e3k4CNwNEJZ43sji-c0rV98EP-GCajXOg5bpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ زمین‌لرزه کهگیلویه‌وبویراحمد را لرزاند
🔹
بنابر اعلام مرکز لرزه‌نگاری، ۳ زمین‌لرزه از ساعت ۸ تا ۱۰ امروز به‌بزرگی‌های ۲.۵ ریشتر در عمق ۶ کیلومتری، ۴ ریشتر در عمق ۱۰ کیلومتری و ۳.۹ ریشتر در عمق یک کیلومتری، سی‌سخت و یاسوج را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/459398" target="_blank">📅 10:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmBJktYfg74zecM8aP90DQIXZzy07dETkpYPxWbvWgyMJrwseDQEsuFcMsGbXSD7pMOdWXzfE1CQLhB_14HSgeBsqCyDO0scB4tos6v6075bdSEYO7RESMKiSYz23cI543K7rLrV53CufBFz-B49TvCqjow0LkWgvXEJDPvP9HT5Wa_Ul2K4V4DvFe4hyqi324EqI1gIM6V78zt1uw5FVgpxTtF_fy9rfJRQ44CG3SX5Q9-yN_PiGVO_ifY8K5K06xDOveh01DK7JCMwS6WnovWt65dX6Cvey_Y8KOhe1HEUNHSezZ-DHBovrF2O83qfgqklj3x-7SDFyrec-QqQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون برق وزارت نیرو: نسبت به سال گذشته ۱۴ درصد انرژی بیشتری برای بخش تولید تأمین کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/459397" target="_blank">📅 10:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تدابیر ترافیکی شهرآورد اعلام شد
🔹
پلیس راهور اصفهان: همزمان با برگزاری دیدار پرسپولیس و استقلال، از ساعت ۱۲ تا ۲۴ چهارشنبه محدودیت‌های ترافیکی در مسیرهای منتهی به ورزشگاه نقش جهان اعمال می‌شود.
مسیرهای ممنوعه به‌شرح زیر است:
🔹
میدان امید ـ خیابان زینبیه ـ بلوار آسمان ـ میدان تاکسیرانی
🔹
میدان تاکسیرانی ـ بلوار فرزانگان ـ میدان المپیک(فقط وسایل نقلیهٔ سنگین)
🔹
پل سلیمان‌خاطر ـ پل شریعتی ـ میدان المپیک
🔹
خیابان امیرکبیر - آزادراه آزادگان
🔹
آزادراه آیت‌الله خاتون‌آبادی و آزادراه شهید رئیسی (فرودگاه) به سمت اصفهان و میدان امید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/459396" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RertljpdI2-Bgh-QHxBBGP1I81Y7DenwfYQH0yU2ZoHpgJPjwbP5NGhG2frUbJQZV588-1iF7fV95KLqf1NDiGjOKdmnmhxOBqFMWhTVXXJ-0Rr0nlBV7bXltZGafEs3eXsRK5tpRvyRTXgyn95HcSPLSmeuGHGJiblVoNuu-0ZDZq_m9YY9OYopoSE9uMT1kDggQsfVVkVD1hMPLvUJs8HhVprfQnUkvtGOryNESeiyPJvLNcnU0-IbPZNlqwopIedQ1S2SXe9xhV0kiET-zp8oh0PXJ7dXTo8v9vSiVGsGG7VgwPs_4z0WP6mRyH_i8V1I788VMVAZWA0NaAyjcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: جنگ‌های اخیر اهمیت پدافند را آشکار کرد
🔹
پیام فرمانده کل ارتش برای سالروز پدافند هوایی: در طول هشت سال دفاع مقدس پدافند هوایی با حضور مؤثر و ایثارگرانه در خط مقدم دفاع از کشور، برگ‌های درخشانی از مقاومت و فداکاری را رقم زد.
🔹
در سال‌های پس از…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/459395" target="_blank">📅 10:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG-WK4yK8Ir6deYYm9sbfzbjNUBCgKE8lodcKpOkbdFCaEfQMclY9T6D0JY14f-CzAwRqCnhCZBagRrk1q_ql61gsDq2dv6ngN2zgSMwHutuP7nN2safsRlZ0dyvDkj9yKgiTkbJu4aXfFXQ5bxeS_qtrUi6cl2zcpJGUsmeihVeAtE2Mimi5jxAJnb5p19I9RqCvaJows9xHWOJS6oo0YCazQz1-mqAeKsDDzJHJi3hZa8vYlVurL4-ZLowkMUKNfq_kzqlkprEJG-BwB0ijW29aaDthI1FlkBFEEsM0zp6vl82N_8TRoxzHjBMYNRDAiAjmFuujOmWoxnquTdxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: جنگ‌های اخیر اهمیت پدافند را آشکار کرد
🔹
پیام فرمانده کل ارتش برای سالروز پدافند هوایی: در طول هشت سال دفاع مقدس پدافند هوایی با حضور مؤثر و ایثارگرانه در خط مقدم دفاع از کشور، برگ‌های درخشانی از مقاومت و فداکاری را رقم زد.
🔹
در سال‌های پس از آن نیز با تکیه بر دانش و توان متخصصان جوان، مسیر خودکفایی، بومی‌سازی و ارتقای سامانه‌های پدافندی را با شتاب پیموده است.
🔹
تجربۀ جنگ‌های تحمیلی اخیر نیز بار دیگر اهمیت حیاتی و راهبردی پدافند هوایی در تأمین امنیت و حراست از حریم آسمان کشور را آشکار ساخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/459394" target="_blank">📅 10:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459393">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeeMnSjH6kvFcTLlJePaqwbC-MQv5OYGeA-gfXPpBTcgwmmQjO-YViHbyJ-G-7m_vjMRQjefCB5ZD2brdwv_4MyCzs1H6RDfX11J56R_lMzBOWFrBVGsaTvB9jypvagDkmG0WiEhsjFHeJS2tXBzldMtsh95PyvRITleF3l8MYMhEK_DjiusL1tmMP9y4peERSVHtQKHh4NHFYNQ5rkwbSnOFUZlxAx0Ipn2n3ElnsCrKhIEga3XxY0-IJRXTc8zX2CzLGKk7KFXIXN0YrYHvrzf9J1GyjeJhXMzV9y2oieGQFwF-y16d6Q5aZD_wuVoVB-DHDxNZmCVxCYSGGqAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان یک چالش طولانی در صنعت پتروشیمی کشور؛
✔️
تدوین نظام‌نامه علمی «انتخاب لایسنسور در پروژه‌های پتروشیمی» در هلدینگ خلیج‌فارس
🔸
سلیمان‌زاده، مدیرعامل شرکت مهندسی نوآوری و ساخت فناوری‌های نوین خلیج‌فارس:
🔹
انتخاب یک لایسنسور اشتباه می‌تواند سال‌ها تأخیر، هزینه‌های سنگین و حتی شکست کامل یک پروژه پتروشیمی را رقم بزند
🔹
با وجود چنین نظام‌نامه مدوّنی که پس از ماه‌ها مطالعه گسترده تدوین شده، دیگر موضوع حیاتی انتخاب لایسنسور به دست شانس، سلیقه یا روابط شخصی سپرده نمی‌شود.
🔹
مرکزیت بخشی در تأمین دانش فنی مورد نیاز هلدینگ، ثبت پتنت‌ها، خلق اعتبار بین‌المللی و دستیابی به رتبه‌های برتر جهانی بر مبنای روش‌های فنی -حقوقی از اهداف ما در تدوین این نظام‌نامه است.
🔹
این اقدام نه‌تنها ریسک پروژه‌ها را کاهش می‌دهد، بلکه گامی بلند در مسیر خودکفایی فناورانه و ارتقای جایگاه ایران در صنعت پتروشیمی جهان است.</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/459393" target="_blank">📅 10:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glV2saAncMCf1cIxRWoTRaL86N_7Ult2s7pnQDAxFekKuzHHl0jAphGzfDmP6JlzyvTld0WfW_23DCa2enDjac0y1XkF18QHhedWn90lRMwzkIHFZ8ZHGsnkdpNgWC8UQ1poBnVRwjK9dCTZZgvGxzHj4hoh44l9BYwz8qOs3AsWN8lls-CHmOeLFIjutq3j3hLkjpdT0mYcTQNvm_e8HFR9R-j6v6ZvaQw5Jadrc0wFth1V2DGBapewcCdNZZzhISbKPFWIS33kS91HY8_cLyTeXVXt95ivvcyR5HlhTkCqj2MORDLkryKPXMPU5ffZORxqBhWnJvWttr4tqRfJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
در ۵ ماه اول سال ۱۴۰۵؛
آغاز زندگی مشترک بیش از ۵۲ هزار جوان با تسهیلات ازدواج بانک ملی ایران
↗️
بانک ملی ایران در پنج ماه نخست سال جاری، با پرداخت بیش از ۱۷۷ هزار میلیارد ریال تسهیلات قرض‌الحسنه ازدواج، زمینه آغاز زندگی مشترک بیش از ۵۲ هزار جوان ایرانی را فراهم کرد.
🔗
مشروح خب
ر
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/459392" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/459391" target="_blank">📅 10:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459390">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c41f3847.mp4?token=F_lmKylN-ZC_s8mh_F63SXpa-FhwvHc493V9KXE9CSGcfUoFc0Z8OsH5qLpXeFCXYKOOxjswnvU3_f-rzC917WI-pFXSSA1q-czchoy_S8IJKIl5nTWRDg4MLTHGY8huys_czpwWDJp9j1p-3XEJviWTSOo96hKKSF0TdjqAX1cCYGJwiBtQ-IMX_hDBevvFrs6sTu3VPLT8znHrBeOXeUxJGnXabWzS9WwZeuRSyI5557OixfBXnWsB1TcxJz7NocDONaegXGPdPyRUKJ54fm04jmCjdJQkw5o0EdxPZsCiGkgu5nmkaae_zPKVYDpszvgmWf-2XxxEWGfkN8ziLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c41f3847.mp4?token=F_lmKylN-ZC_s8mh_F63SXpa-FhwvHc493V9KXE9CSGcfUoFc0Z8OsH5qLpXeFCXYKOOxjswnvU3_f-rzC917WI-pFXSSA1q-czchoy_S8IJKIl5nTWRDg4MLTHGY8huys_czpwWDJp9j1p-3XEJviWTSOo96hKKSF0TdjqAX1cCYGJwiBtQ-IMX_hDBevvFrs6sTu3VPLT8znHrBeOXeUxJGnXabWzS9WwZeuRSyI5557OixfBXnWsB1TcxJz7NocDONaegXGPdPyRUKJ54fm04jmCjdJQkw5o0EdxPZsCiGkgu5nmkaae_zPKVYDpszvgmWf-2XxxEWGfkN8ziLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناریوی آمریکا برای القای باز بودن تنگۀ هرمز چگونه شکست خورد؟
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/459390" target="_blank">📅 09:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459389">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec51668b4a.mp4?token=S3GcwxVsC4lXZXUXTgywTRV7PFGjnXtLrGqomMavkPgPz7tUH9j1QuZaLCdg2WBQXHJA7CmKSRPplgT7cqMsgUSp_ovo6l_j0XEvWhFzdjK4jGUy0Tl0ipwOO2mT2avnH2PR3aPuWmlZabUrhyqlrOteverflCA8WRUpLDOpjXJ39qtmyGtGNXTlrshgig4-yd5bnOllkWVy5FsWa_lQaIRxaCZsiVAMbKragJOaKwT6LinkSfztelAjBL2NSLWxU0wTZstTLZetvkbvtwMBTzbddqszPcOfbR8pUY33dTpXAJeKN4NXAivSaMPyPYCpe0gH0cB05puAR7nnV9eGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec51668b4a.mp4?token=S3GcwxVsC4lXZXUXTgywTRV7PFGjnXtLrGqomMavkPgPz7tUH9j1QuZaLCdg2WBQXHJA7CmKSRPplgT7cqMsgUSp_ovo6l_j0XEvWhFzdjK4jGUy0Tl0ipwOO2mT2avnH2PR3aPuWmlZabUrhyqlrOteverflCA8WRUpLDOpjXJ39qtmyGtGNXTlrshgig4-yd5bnOllkWVy5FsWa_lQaIRxaCZsiVAMbKragJOaKwT6LinkSfztelAjBL2NSLWxU0wTZstTLZetvkbvtwMBTzbddqszPcOfbR8pUY33dTpXAJeKN4NXAivSaMPyPYCpe0gH0cB05puAR7nnV9eGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل نپال از ۹۰۰ نفر گذشت
🔹
سازمان مدیریت بلایای نپال اعلام کرد که تعداد کشته‌های سیل هفتهٔ گذشته در منطقهٔ مرزی این کشور به ۹۰۳ نفر رسیده و ۴۲۴۷ نفر همچنان مفقودند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/459389" target="_blank">📅 09:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459382">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FD2AxSoRppVdY6UyEqSq4rimOi6uieFtEc7-SvD-7VoGUFVhEt1Cx2JTlnkr8lU5A2Bj013qhTYe5eKVtpTcy6-XecRPkofnQTjPc3Q-8b8rH3vp12PjEAvxNv9MSHPjbNrZ1823Vl10AbBjm8le3AN8b-bCTBwpl2SQQNz7PgG9EpfXoCOIPafPvONcHj8YQcg8Cojst_-BsmEpYyfqnHWroFwd48mswaVLS6sua2TNCCbj9b2QyvVXnw1ev2wv7LxUUEbL1rZDIKAWnWDuOO-BgtP8YRDQmHr0XXDvTF0RZrf0HcVP5b_oHHf1Y23ZwFOU3AstIriqxXRb4uU7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2KxaEGvsJ-MCVc-vbyJlgWXGMjW6JZK3FvOxNOcZd6fQ03pRkQ46X1YYysU-TN7ho0ofBgd7UOB8DKL6mXO4HvXZFws0dzE5qKizke9l2m_0gF_ntpulg87F4HP-CrwVh-uI4kRPrDaFAce6qfU6G2AokJeG5NjPNghjYmaDp_UwVh-fwyvf1Mzpl-9xIxZHRZrbBd4awXkr6XNIerPchQKeu1X8LqtjIwxCY6HGBayUKCRmTbrdapg9H_5S2x0YWbicmfUXsRe4NdzvDeK2mnEV5KTz6Xdul5biVkX4Kkhvqya7e3zuC75LGlxXxHxMmIvzhFxLv_EBYfr3b_-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1fnV37lrcm1oSdHPEJlIvPWvfEFaMQb-Uwl_-V4WurtF8Y85BLBSzniNvbraF6e9RksU5svgDhz1J6wAno8zuM3D2UCKZElz7NtDe3gwSe62prFIaC-Ky3Dpp3lo0c3C-uYHc54qilKpWVzcCxZ4DIqKLz04WB07gh-SlN1JqCUJ_7k8O4YwzV6o8yophGBNAM9lZs_8w9U_droCM5rhksCOt2MVHes_Kuh-qv9ICZ9SRcT1FG58mmwu44WMULsQNpvpfF7d33M8fdJX11jiXZ7cDrnjkBmlQYCvf30intfEsMT2o28fnTP4yijR7EsKhXhFbCOWAsvLkDiNx45pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXzoIPMNzbV8ZIB1-RLHDHkvHxvTGmXmRyXLKY5ix0_WMV7F5v2clxX7VD-_g7TsmZZkvaEH2avVr9qWbRfET9KxUAI_6o6E75j21M6SJBTvb1hNpgVabyFvv1g9XjLA4Vv5s87hAVETmS6mFcZ6I_TIGKNdVKA7H9XLnk1WgHj5hMIrY074vnY04gGV-rgKjpZ8EC82BLlEfMciPVw38nAlIPqElAHQBqjVnLh5FHnacwKSTBkpQ2pzpSS2zR7iy2rWCaXQowbqGQx5r1PeKlwaTrSDkGkVPmK3IhsMn-yiL-GQafsf6PlJI1aX3Ivj6XpciRkYf6iG7Zk7sc3Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6Xcn7KVIAwYGy2eHC7vRKhfgkUUmptO4bIdNNs-0eR5tgUW6qV5ONUPBll0NbyxEvJ0nSeLuFEhQPjSK9_9XMjBJmFQ1TFsWr1MMgzGnk7GlkLs0RIRD9XXN7fiW7fHBAaqintThzsyskS2wj-d4JKbktWT6B4Xvl1A1jYOQxAjT1E9jpiPicRcyNsyXsjtTutoFljT0doQGAyh5Kt6lIsUHNdYi6jDl130ChxpZWr-dsFRpW_NAPYl_z8BOwMYxf0IYH69unKzYa7gRyJy7WljiHQZxFb8so1yiPKIiYeezb76sK3p4mW-mdFdY5O1V5MXV5CvLPdLGd7oq6xZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sshkNIZRONjo8A-gWHX4-o6xjw6K1PJabYeFyhzRvagEMyiDvmGDtmF0Vxl8uxZUcT48GLtP8FS1oxbcq45VwBZ2PPKD9lhUrY3Jnle6psH_fl_IJoNQMlm-OntgYWvGyhBv8dmR3nU493gg00khfSS7ya16HAC8lztmS9rtq8Fn_pHNiCzhE3KcgjD-nhgMYtkhaY-MtUMSfwjV4sS5Xq39LUfPsxTJ4ujCReDLDWAklTS5yBY9ii7DJYQ0pzeJgDWuzmgbjU096VnTvBWakFpnjLV-b_EEJJ5Z_xfXBIrceGPC1Yl6CsOln7nCE0hJ3FpRe9R8oQNCnbaLzWwecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZUnBQAzzTRFuy_P4GCkrpACquu7BQvxOOPQot37aVQz2ZuZB25rtbA_Nl8PLHu9P9GJ9E_l-NN9UZ3Ui0jLciJKhFJHQgrvl4OYQ7kjNM_Xo8gLH40eYyp8QZFluJ42Ga_7WJEAqHferzQ0kyouW8T-ww6afgrJGUvajutu7ssPGafYvzsJfcYIQMtA48ENyAwljirajfbYUJpHL_SejENJePSrDIZAY5xvhO62xZHUoeCFjjAKNd4R2Jj9U4S5QqwpGfVq002LkM85B6biSE6XKxYC7pIVyfMHPuqZGrlvklDcbjq4yMTxSmNU4W54Qm5fQ0lkx9NhxuMuVAs5Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: رئیس‌جمهور آمریکا زیاده‌خواه و بدعهد است
🔹
حدود سه ماه مذاکره با میانجی‌گری دو کشور دوست و برادر پاکستان و قطر، نهایتا در تاریخ ۲۸ خرداد ۱۴۰۵ به توافقی منجر گردید که به یادداشت تفاهم اسلام‌آباد معروف است.
🔹
اما تعهد آمریکا به سندی که امضای رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/459382" target="_blank">📅 09:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459381">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbrjKpDXOLuBAwhiQ1r08p5mixhPusmI4fVBF47bwp03S6LAUkUKDumZR1Sd28Eet7X7SmCpNm8QvkzALL0OxZdkE1dI3WyI6VNMcmmwsS9E-JPFd9R5BdCbW7yWc63LT6jNqfvwZ4OWoroVck-Ql0dcwXG99tGJUx27TJPvgkQb6wd7Km8sMKlt_eWsvNx38C4MTIyN6GJn1QNexgOFM1KltnNr740EMM6Hh9uM3FnHMvvdcgmD3JEcdk8Kl-oEiizn5lzwtvTt5es8mKMv040tMV--N-I2mmY0PUP0wI0A38X7wMPZOAFnL485ZMworXdT9Rg9133yCmompCADFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/459381" target="_blank">📅 09:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxgrK54jlUwDIX7JFx1sWSQ-dlEXGyvUb4FHgBOCrV0zfFRjqPMmqyOGie6vKuvHLd2n4TS_t-otWYBBHNl1qwqh67UA-UqKc_0vpeELWzf6tIuQ-Y5X3P0vocXmyZw14jqpiKg06eSCt-i8pSh4IuwE3xvHbtRBif7rOTBLayYJXMqww_kjbH_k7O9oZuJKlXcM491FuVxcI77Vnh_Ukj7ukmaZFqv9jqYab8I2elJv7JayNf7ZV4EnPg8swSMeFzz6r2DB9CYBQK5WjCawvJkU3u1blJ5MFCXN0BQUDrWjTyUBJluLaO8LYy7UPcZb9_QBVryTeegIZIj4GIgbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش هنگام عبور از تنگۀ هرمز هدف اصابت ۳ پرتابه قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/459380" target="_blank">📅 09:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXCdeDvx8KY2QjX7NdTkORvvn8tz8C-TiMrI4O3E7Gt0bYqZiSO46dbgL6e93j76x-6JjNryBlZJitL1GLTbyRJq54HiTFgxhBXZu7Zyke7KzMtdb3_EGX75EahP3Ouk1KgbcGP3CWLsHOrPIDsQtl8XN24YokBktFR2bOLdcPCPb5YUYvzp_TgBjhDhiB6q8W6W7mTapCfTol8rcIC9q_kJmuT3TqA798N59qa-coY1T3lSVgOh2EO8NnwSttzoKQV1w9vI-BPUXXhhNrVaQGeIWtj-O7zskmEFdhHCHt5DSvT5JmDlwFA5JX2CF0FHOZNoXmK8hjTt_rrVsWARhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس بانک مرکزی: ارز داریم؛ به قدر کافی هم داریم
🔹
این ادعا که ایران وارد فروپاشی اقتصادی شده، به‌طور قاطع درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و کشور علاوه بر آن، از ذخایر داخلی نیز برخوردار است.
🔹
منابعی داریم که به دلایل…</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/459379" target="_blank">📅 09:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459378">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئیس بانک مرکزی: احتمال وقوع ابرتورم را ضعیف می‌دانم
🔹
حجم تحریم‌ها و محاصره اقتصادی اعمال‌شده علیه ایران بسیار گسترده است اما تأمین ارز مورد نیاز کشور، نیازهای معیشتی مردم و نیازهای اولیه کارخانه‌ها و واحدهای تولیدی قابل نادیده‌گرفتن نبود.
🔹
با وجود اینکه…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/459378" target="_blank">📅 09:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئیس بانک مرکزی: احتمال وقوع ابرتورم را ضعیف می‌دانم
🔹
حجم تحریم‌ها و محاصره اقتصادی اعمال‌شده علیه ایران بسیار گسترده است اما تأمین ارز مورد نیاز کشور، نیازهای معیشتی مردم و نیازهای اولیه کارخانه‌ها و واحدهای تولیدی قابل نادیده‌گرفتن نبود.
🔹
با وجود اینکه مردم از تورم رنج می‌برند و سنگینی آن را در زندگی خود احساس می‌کنند، هنوز وارد ابرتورم نشده‌ایم و احتمال وقوع آن را نیز ضعیف می‌دانم.
🔹
اقدامات پولی و احتیاطی بانک مرکزی باعث شد شتاب تورم کنترل شود.
🔹
در شرایط فعلی، مهم‌ترین وظیفه بانک مرکزی کنترل شتاب تورم و جلوگیری از ورود اقتصاد به مسیر ابرتورم است.
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/459377" target="_blank">📅 09:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">ایران و آمریکا در جنگ‌اند، در ورزشگاه نجنگید
🔹
«پرتاب سنگ، بطری، فحاشی، تهدید به قتل». این‌ها شرح یک دعوای خیابانی نیست، وضعیتی است که در هفتۀ چهارم لیگ برتر در دو ورزشگاه ایران رخ داد.
استقلال در این هفته میهمان فولاد خوزستان در اهواز بود. استقلال که سال‌ها اهواز را خانه دوم خود می‌دانست، حالا هر بار که این تیم به این شهر می‌رود با استقبال نه‌چندان گرم میزبان روبه‌رو می‌شود.
🔹
روز قبل از بازی یک هوادار خانم استقلال از تهدید لیدر فولاد مبنی بر جهنم کردن ورزشگاه برای آبی‌پوشان گفت و عنوان کرد که به همین خاطر به برای دیدن بازی به استادیوم نمی‌رود.
🔹
در درون ورزشگاه هم پرتاب اشیا و ترقه در طول ۹۰ دقیقه ادامه داشت و حتی برای دقایقی منجر به وقفه در بازی شد. در سوی دیگر برخی هواداران استقلال نیز در مواجهه با رامین رضاییان، اقدام به پرتاب سنگ و بطری کردند.
🔹
در یزد نوع دیگری از خشونت در جریان بود. خشونت لفظی. دو سال پیش در بازی چادرملوی اردکان و تراکتور، برخی هواداران حاضر در ورزشگاه علیه بیرانوند شعارهایی دادند.
🔹
در همان بازی شجاع خلیل‌زاده، کاپیتان تیم هم حرکتی منشوری کرد. اقدامی که بعدها با درد کشاله توجیه شد. در بازی این هفته نیز تقریباً همان اتفاقات تکرار شد. فحاشی مداوم به تیم میهمان. این‌ها تنها دو نمونه‌اند. در سایر ورزشگاه‌های ایران اوضاع دستکمی ندارد. خشونت‌ورزشی جدا از وضعیت کلی جامعه قابل‌تحلیل نیست.
🔹
بااین‌حال، همه چیز را نباید با جنگ، وضع اجتماعی و اقتصادی نامناسب توجیه کرد. نبود قانون مناسب و البته مجری قانون باعث شده تا هرازگاهی زشتی روی سکو بیشتر از نمایش درون میدان نمود پیدا کند.
🔹
در انگلیس و پس از فاجعه هیزلبورو در سال ۱۹۸۹ که منجر به مرگ ۹۷ تماشاگر فوتبال شد، به‌سرعت قوانینی تازه وضع شد. قانون الزام به نشستن روی صندلی از همان زمان باب شد.
🔹
پیش‌تر اغلب تماشاگران ایستاده بازی‌ها را دنبال می‌کردند، حالا جز در بخشی مشخص، کسی اجازه ایستادن طولانی را ندارد. بازرسی دقیق برای جلوگیری از ورود اشیای ممنوعه، نشستن روی صندلی شماره‌دار، نصب دوربین‌های امنیتی و از همه مهم‌تر اجرای درست و کامل این قوانین باعث شد که انگلیس حالا کمترین میزان درگیری را حین بازی داشته باشد.
🔹
وعده اقدامی شبیه این‌ها در فوتبال ایران هر سال داده می‌شود اما هنگام اجرا با بهانه‌های مختلف فراموش می‌شود. حتی آرای کمیته انضباطی نیز آن‌چنان‌که باید پیشگیرانه نیست و اغلب به جرائم مالی ختم می‌شود.
🔹
همین باعث می‌شود که مسئله کشاله شجاع برای هوادار چادرملو حل نشود.  به همین دلیل هوادار تصمیم می‌گیرد حالا که قانون کارش را انجام نداده، خودش حکم را از روی سکوها اجرا کند.
🖼
حمیدرضا صدر، ورزشی‌نویس فقید در تعریفش از فوتبال یک‌بار گفت: «فوتبال ورای نتیجه، ارتباطی است که آدم‌ها به بهانه پیروزی و شکست در کنار هم قرار می‌گیرند». حرف او اما این روزها در میان خشم و سنگ و فحاشی گم شده. این پیامی برای هواداران هم است که فوتبال را با میدان جنگ و حریف را با دشمن اشتباه نگیرند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/459376" target="_blank">📅 08:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459375">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9-Z2YvEKbwnTgLopcfk8sJgAfFkHAtM1mZ2Au9xPaW6Kmrs9FHRoMcZ6QMzxaxugLadmx7hG6uxGzQdzZqBFM1fIjEDmSiUZAJ6btnonbKsjV9DJu252NraUvqM4MzIbs0jOs95D2svpjgOK0fB037KUF1vWqPdo0ysJO7ykIBihiSXD4iOmvEiVPNaXZNuFLKFz2C0pEv6Ya3Hzv8XvH7SBStw4oXtIz6EAQaEF3bFyxeq0hKtVeOBk9l5OpWEVEHk1yXdWOt1AvAb7LoEy5MrPxgFYcZT9NsPlrjWbVMtAfv9lZeWhwcynie0FdJ7VbJD2MCAokTT-Lal4axRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: آمریکا و رژیم صهیونیستی در جنگ ۴۰ روزه ناگزیر به آتش‌بس و پایان جنگ شدند
🔹
تهاجماتی که در ۱۳ ژوئن ۲۰۲۵ و ۲۸ فوریه ۲۰۲۶ توسط آمریکا و رژیم صهیونیستی علیه ایران انجام شدند، تجاوزی آشکار علیه اصول بنیادین منشور ملل متحد و حقوق بین‌الملل، علیه اصل منع…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/459375" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z60n4YZGQWtarht0AnSyYZV3ZGoFfh6wY5ULlPW_BhoZmrF88QRokYfT3XbCqMv9fJagsebXdZKoiFMsKtxQqUfE6wNyRepMP8wp5ki-Y6K7ju0qcujNLpOJb1sjgVjgqMcCOklDoA1fGe2Dn06xze84tRDjWbiBJ4kTdhclU-zbHZ2OYf2IFk9zEKZlBpilmwqz7WVnsqu8wvMAFTzNNC2pGOkh2QWdlNrdEg4Vv9y8hsvwZXpFg559yKJMrQ0lLMSSlVNDyoFICzPCdO7-XFJ1UhTeJxl7vYg7OuW8ci-klq2VD2mPpTWetsNVOVZeiqt9TDb-WvOPdRETCp_aGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: امنیت منطقه در گرو مقابله با رویکردهای مبتنی بر زور است
🔹
رئیس‌جمهور در اجلاس سران سازمان همکاری‌ شانگهای: امنیت پایدار نه از طریق تقابل، بلکه از مسیر اعتماد متقابل، احترام به حاکمیت کشورها، عدم مداخله در امور داخلی و همکاری میان دولت‌ها حاصل می‌شود.…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/459374" target="_blank">📅 08:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRY4BtU29DwnbU4Rmvep-5HNDtOEH6_fFB_DFxe4b9w_9tcDxlmHY5abyJX4WVNZk8BKr_1eSDnIe5FbomnIkNDJK5ke6tor5OooRmmciqS3stu_q5OOE4BdKlivaY1Cobqx46AyTYiTnyaXUTWjgmfhA18aEN88ipTMUFgISN0WaN-CNeIc4UOx734AEIUbVhcOlQJ60OfgMmDMlh3s9CZmN1l1W1s-QPDP1JdEYszaum_6ulzuvBcZVkxAAP4JDismysNRfqLZL12XiHJyR8WWK4TFu0Pbe2Konsre-bMPNjU5p-_FKs604g3iuqj0LHR61ZKvwFoM7IgK4KBUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یادگاری سران کشورهای عضو سازمان همکاری شانگهای  @Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/459373" target="_blank">📅 08:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607c16eea6.mp4?token=C7b8vcaT68eCiOCIdIIeYIZ3HaXKwVLisg856ISRgrUAo26eWexau6vWZpKHsuUB-rQJx10pLvMNBx1pes36hcxXk-zOZINyGeiQsQfyMCdJDb5NhlNswD1U1kPyFF98EBJeBvwDeqHxLizgHRYL7lreLHCxWeHjTNv6Q5u2JM-UmIfcFr9ndglwoEIvK0uidfnC84wD4_hNhLuelQyH4Eri091FK4RVLuwR8oppOHsxLaxfsm6uNU2_kNDc982ka9_v4H8gnavoZG_aQvSP47O1ynCSoqkklQG5In9TDuOodTz1Xx-wu213ofaYPCuQMG41eyCjQbH6Mblu7hxgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607c16eea6.mp4?token=C7b8vcaT68eCiOCIdIIeYIZ3HaXKwVLisg856ISRgrUAo26eWexau6vWZpKHsuUB-rQJx10pLvMNBx1pes36hcxXk-zOZINyGeiQsQfyMCdJDb5NhlNswD1U1kPyFF98EBJeBvwDeqHxLizgHRYL7lreLHCxWeHjTNv6Q5u2JM-UmIfcFr9ndglwoEIvK0uidfnC84wD4_hNhLuelQyH4Eri091FK4RVLuwR8oppOHsxLaxfsm6uNU2_kNDc982ka9_v4H8gnavoZG_aQvSP47O1ynCSoqkklQG5In9TDuOodTz1Xx-wu213ofaYPCuQMG41eyCjQbH6Mblu7hxgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌ها در شمال کشور تا پایان هفته ادامه دارد
🔹
از روز جمعه مجددا دما در شمال کشور افزایش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/459372" target="_blank">📅 08:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آموزش‌وپرورش: امکان ترمیم نمرهٔ امتحان نهایی در شهریور وجود ندارد
🔹
با وجود درخواست برخی از داوطلبان کنکور برای برگزاری امتحانات نهایی شهریور ۱۴۰۵ با هدف ترمیم نمره و ایجاد سابقهٔ تحصیلی، سخنگوی آموزش‌وپرورش می‌گوید: ترمیم نمره «خرداد به خرداد» انجام می‌شود و ایجاد فرصت مجدد خارج از زمان مقرر، نیازمند تصمیم و تغییر در ضوابط مربوط است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/459371" target="_blank">📅 08:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM-6rB12Xtcdmix4572os_D0oMpTkXi2d98equyFoyDV3z6-gxHsuSn4QeJSyA5gYKzWXxS67VmdCXbNuNh7DNF02JHtHAZHeLpuypTqyuPw6IbmkZHB5J2GW_vgY9LYnnVVodY8mRlQXAnNG7D3o4uORpqi28P2KU9V6CArafq79jo2GlVMu0CWRKOgiyMn0hOdZ07YZd_Pptr-jWgAejuQGHHCMTjxiNSCDFWBzxMR4-fV8F3SzqCzsE_bIK3rMomGe4i_vod8u64bNiYbhBjGe6Z7HZu0bLl7Kz7HJL1mbOxHP-DSnS15Hb7NTyofQmLZPdG2HKQRkSwcpuiMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان دقایقی پیش وارد محل برگزاری اجلاس سران شانگهای در بیشکک قرقیزستان شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/459370" target="_blank">📅 08:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYdvXE5O_yKgiyWkNg_56ck9dp5QJZX02KgZ6-3m1UCaj2UGxcGU5riHLUpIfgl-9714zlCm7y3E8D74PFVB1j2w5IFeHQJowISAz2RDp6diSePh8rOHN0F9_UMwvSbaG5dwkHxl0z9mfSMlpmH5RHby374rxr6k46og-ndcQGUpTmfFWdlVpYYW7pSny3g5pWcn4e6aeUvON5q8KRyEp6OSsv8sHu4ZpPKe5SmzzeL0OuS681Zh5CcAsrCpfc5DO7bHbn5-HCZzyT2d94x_3y1-fSK6Yneg70_1RfrSsmlOBvEBevBvT9lSOuOik4DtLwl3iOe3dS4qsHVJ4tLkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwqgWmQxRwspGKOSpODie2E3NU_tU_oMCo1noUt9O0elGKQUiwcEjCSTpNP1J-IqIMqEo1_Nr5DJljntE3hf7fSakVOdyd1KjrBsO6TPWgEh2mBNRmQNFeBDC-gAvq9w7__28Tu-99RGW4GmAq2xGdfg2IZpzT6IPxyxRFVOmYWywWhdIITntaA6hzoy5RzBI8kc6S6t9LLmMJzibO_f3eU8S1lrkRG65SakydvaWkxluB0wDJ-G6G1m-YGs-cRHOXBEmevRKTA8mSxY70i8qqM0wpqT6a_MfXKJlufF3Epul0jjdIRFzqVMPPpbuE1IBABvaW-OBnBfP1vCRw8j-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yr87cMCtR4bP1yOz75GK0xTwVcj7-sj3Xdxdmu7nO7b8K6c107duEmO8TVsZPAcCKyTiS437PfbhHUmyvKYH9oJZap3hso4dM6mbn0n7E-OHDJUd_yuBjglvLBKTVMOp9v8N--qwCsmwV60O0-jTdRU-URSZPEKeommbicmIawGimeQvC9rzB1dFOTlJjcR5kgbI2BBCnnvQi1VXX3eRSbjwM-NlMXLZ9NCUXJ770R3wj3OvUfioDKfzTiZKwxVQ5VLEFLc-Yv42YUdeh1r_IcsaJsMHsiJQ9Q_H86f6Crb46DaNGmPa4AHJX3C-Ys5jwb3aJ1T0wDjRKUB1E-Ep1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2J3Hvkj2YHAlJlwWt8KXdwDTwl77FZpo86dHMlKjpV_LlcKECTAj_d3yUeJHppur-7fmJEbJeKgQNjDSSosFg1y-CzZTygG_wANVuIVh1-lz8uBBiDp7OPF8f6SA6yAwfS9NM-4xkGQDOESImWJO7gZajhEMTpz179fTsbnXnMhKYZpHEI0c-5pH23Uhw4f5u876ANIEkmVEbnHqJCxu1Eb-Mfk6hu1Wwdsez4H2SePOgBxJHTkdJi9R10N44jNtPQn2BqDdWU6zA_9YDZiWyNf9_i8Z-PQOkYF11XKALxZlUsJB6bIQJCBd_s7RTVkBkRkfZ5Eubtr3G7R3aDbpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار وزرای امور خارجۀ ایران و چین در بیشکک @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/459366" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30559817.mp4?token=XtAOpXB8Nd59sHTKR1xKjH5WR2-8FOC72ZOCU-sG59fkJO8FQBMmfwisxbjVBX1_MyjajV_p0IjoQc6iUEMgxXE2Ybjsxze4g0i01vNzgsVxnepjjApfexQYPnfnLl-tUXBAcnhcp7nNg3tLeI2er-kxh7un1jOOoxWx6D1IgJ3LdpgCpMQwOTkTwe97iuGI_0F6xZ9X5V8VEgdbowznSZE3Q_nWQBs7Tt4VHAyrPP2vHTMTJ8u7DWUK_WWWjRNsSwpMEq6iKfCyH9Ya1pP8rBTgBgV7MjoNGxgG5hxlfEKUEVHPFFluIolSCGKXfRUI64xerXon0S7f1h4ogJUV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30559817.mp4?token=XtAOpXB8Nd59sHTKR1xKjH5WR2-8FOC72ZOCU-sG59fkJO8FQBMmfwisxbjVBX1_MyjajV_p0IjoQc6iUEMgxXE2Ybjsxze4g0i01vNzgsVxnepjjApfexQYPnfnLl-tUXBAcnhcp7nNg3tLeI2er-kxh7un1jOOoxWx6D1IgJ3LdpgCpMQwOTkTwe97iuGI_0F6xZ9X5V8VEgdbowznSZE3Q_nWQBs7Tt4VHAyrPP2vHTMTJ8u7DWUK_WWWjRNsSwpMEq6iKfCyH9Ya1pP8rBTgBgV7MjoNGxgG5hxlfEKUEVHPFFluIolSCGKXfRUI64xerXon0S7f1h4ogJUV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
عکس یادگاری روسای‌جمهور ایران و قرقیزستان در اجلاس سازمان همکاری‌های شانگهای @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/459365" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c65-PAri1QbW-D8J8iLx3U3T80zwPtRRJXRbPHuDfXkL9uxxM5noT2rHlkAuQiayDyHJcYV2BSLC2Ra8QMGYuHJ4B52vTE8Mv3m8E7p8fzRGvysNDLqtL3jMc3WtRPVcH2Ly-Ar0iken2HYxzXNT1giQmD40lat14nVAq17dMPnwNg7p2iNJUElCp5jzMPcwTFutlrbA2RYrQVXeDXDE_xSAAFZJ4nN5Hd3EZvKasyC7B53tfIeX5MlaJK-lsRpZ6uppipRKTjeXvcNNT_UBEQoAXb4z90gJQJ5eV1tNPfOpgWHe4YHneba1m6eDZbhSYbduQhm-Fk0WdcY0wvAXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار وزرای امور خارجۀ ایران و پاکستان در بیشکک @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/459364" target="_blank">📅 07:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcyjDeGB6Uy_7BQmkUUaPhtcXuTkf_PHZ5LV1Ffy0SC28Z0qZCkFnU6yfLRblrKaFSDajIwMilw5Ul-A-S-EOmHvz1ckmxVgeFW2DT9X4PbVJv1VjsosygIDCVzUeUKQ5z5-Dg5jpvB2iN9CClOszfGZVuTFlXrjydDKjDsNBrueWfL9VjQ7okrN6RLfJPT661R7mfiNkGlNDrbUFvkpgsoL8S8HnQ5EIRR8Bnsz4_wTZizQHbz_N1QmO4DF8R5o530iy_d7jkdpzKdGWvaQmDSJctrgdRNINRTvsG_3z5IEU8LW5TaLu0S8PXpU8AcJ53g0Dtjt3ctQg_QBzzW16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ جدید پرسپولیس برای «پرسپولیس ب» کلید خورد
🔹
یکی از گزینه‌های مدنظر مدیران پرسپولیس برای راه‌اندازی تیم «پرسپولیس ب»، خرید سهام فولاد ب بود؛ تیمی که به تازگی جواز حضور در لیگ دستۀ اول را به دست آورده است. اما مذاکرات در نهایت به نتیجه نرسید و مدیرعامل باشگاه فولاد، اعلام کرد که فولاد ب در فصل جدید لیگ یک حضور خواهد داشت.
🔹
پس از منتفی شدن این تیم، پرسپولیسی‌ها همچنان مذاکرات خود برای خرید یک سهمیه در لیگ دستۀ اول ادامه داده‌اند و درحال‌حاضر باشگاه‌های «بعثت کرمانشاه» و «فرد البرز» به‌عنوان دو گزینۀ جدی در این زمینه مطرح هستند.
🔹
البته هنوز توافق نهایی میان پرسپولیس و هیچ‌یک از این دو باشگاه حاصل نشده و مذاکرات ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/459363" target="_blank">📅 07:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgAgPGCeHHHBddzZDY-SPlNUiIjA_9rPBegIIubkr0_CviAlwtT2UIu1BKB2KOWeKEzLDGWzoayXtPS8GlBgGFEvKDPmEgoYFjPdQQ8o9hblMUosiQ2sIYu8ovKWlFE9t7QyJtVmuHToaZwSExKLmRkuYkrKF_LDv55S-iJtdPrlA6hZVhrUiw8WVbdljmknpLdq8QTE9io5EnchVOYVOYUd_LhRK_UoK4ooxPKfkFCBVsoYmpINTMRR2bHOEDc-1w_GNr7Ii0j63f197wRxQ6jiGWLqiYHGIAXS6UUb0mLzEn6-EB1Rbtgo-UCYaZNSwlOyzeiBs6opXYUaB0G9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار وزرای امور خارجۀ ایران و پاکستان در بیشکک
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/459362" target="_blank">📅 07:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvIeg6MCFGCj8FRx1PBcugYjh8hzXQmTHXg2eRzk28KNdTbBHk8RCJY30rKmCYrcgjT73ZGj-4V6Zua5Kmz1Izt6lSC_IL9HIj7i0iChsQ6ukHITCY3AQORNI-SzM2TSaQroNzaJ7QMFzQKyDZWug5vbjKcnXqX_XxDwpWpjyb5JDz16Fh9s4cqr4DtJlgfBM-l8coKDOG18KFNPiRHtmIc8czGtc0eGbCfipDuMFRxUHJDsKBys1-K91Pi_qieIUm6nNSrqtjvD-eCqD3Aa4ZB19y2RkcB5bgbaD738iUZFjj0zlluCIVSQa6sdBeOBvHyyAeIigC5IIUDMVWtSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان دقایقی پیش وارد محل برگزاری اجلاس سران شانگهای در بیشکک قرقیزستان شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/459361" target="_blank">📅 07:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e781b7ad2a.mp4?token=gd9FmL_IGCQHXvVRkLUvmz6_wDFOj5R1_9_NFCecCPN_ukm0h4lRhJtQuJxaN9R72xKQvRgBSDRV2cDkxVUjT4HE2MffHTEDVYM0nK6fi3v2Vk9h2Yxyh2Bjc28LXWtVMHRnnDbMOYpI6OcXvPvUANNcD-rAL_0RFh7yaOCdLYwWd51UuQ0w2WCSYDJDwZeLFtluqxEoJ64bk90MyhqTqjOtyQJdQ0tKHC1JJy1I16VN_F7k9oSCQpGtdrWzZVl6OxiO2f2t1cnPrIAMVHvvNGcquomtsUe03IL-VWnBQ8c1UEZRX_hM4dYUY4LtU4mKlm4NAh6ypOADJkJTQDM-zDJj-9MQydMGyJ-QjNMTT0EIC3uCUAnlIOSQuWpL-vI6bsmi74Q25nTvdHMR09eGRoAvXGuo8PpnGFn0qHNG89woEoIVdV8KGy26r8-5syHZS52ufCOcfTPihHWjK1xaei5ZN2CuMF1FPwUffbL_nB723pnojTxLrfTqSi4_XXxG7SJICuaAd86m_eTfeyxyMfdi6PpUMXsLf_WUEVI-mLZWUKGX3dEcKeY99VjnPje2FApt6-n7iLtzSO20m4ODeciQuE3yr-p1Ks7-kf1_ShvC3VDWUqZnwmgKbphFQGKr4hdCYsSfc4UqKu3yQ1GgVEOz4QoxEUF1NLCODnbIfSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e781b7ad2a.mp4?token=gd9FmL_IGCQHXvVRkLUvmz6_wDFOj5R1_9_NFCecCPN_ukm0h4lRhJtQuJxaN9R72xKQvRgBSDRV2cDkxVUjT4HE2MffHTEDVYM0nK6fi3v2Vk9h2Yxyh2Bjc28LXWtVMHRnnDbMOYpI6OcXvPvUANNcD-rAL_0RFh7yaOCdLYwWd51UuQ0w2WCSYDJDwZeLFtluqxEoJ64bk90MyhqTqjOtyQJdQ0tKHC1JJy1I16VN_F7k9oSCQpGtdrWzZVl6OxiO2f2t1cnPrIAMVHvvNGcquomtsUe03IL-VWnBQ8c1UEZRX_hM4dYUY4LtU4mKlm4NAh6ypOADJkJTQDM-zDJj-9MQydMGyJ-QjNMTT0EIC3uCUAnlIOSQuWpL-vI6bsmi74Q25nTvdHMR09eGRoAvXGuo8PpnGFn0qHNG89woEoIVdV8KGy26r8-5syHZS52ufCOcfTPihHWjK1xaei5ZN2CuMF1FPwUffbL_nB723pnojTxLrfTqSi4_XXxG7SJICuaAd86m_eTfeyxyMfdi6PpUMXsLf_WUEVI-mLZWUKGX3dEcKeY99VjnPje2FApt6-n7iLtzSO20m4ODeciQuE3yr-p1Ks7-kf1_ShvC3VDWUqZnwmgKbphFQGKr4hdCYsSfc4UqKu3yQ1GgVEOz4QoxEUF1NLCODnbIfSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی پس از اولین روز نشست شانگهای: تأکید کردیم که ملت ایران همچنان برای استیفای حقوق خود ایستادگی خواهد کرد
🔹
یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود؛ تفاهم‌نامه‌ای که به امضای روسای‌جمهور دو‌ کشور رسیده و آمریکا آن را نقض کرده…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/459360" target="_blank">📅 07:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هوای پایتخت «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۸، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/459359" target="_blank">📅 07:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc4c12292.mp4?token=l1NKTGV8jn0OZmd_DC2axl-N3jL9csemMZzn4kKZwZNqtXRUB9vpDF35LEqzvYi3K6fem4vZaWU1UvEXtyO0i_VOP2tLhFsVuKCKguKrnmpdAS86QLGASSOlhyWpwyEgVNXM4nQ1t3FNWIaR3IiZI8ljdkNd_FqvDyZOTtRLWOrMM7tb9OsoQb6L2gZKhg1e7B6zz7mIhTpSu2HQaiSshp8rAqZ19B4a0O7UlLfqH7n2FlO74_lHr6EuaVYg3HUgPROuN6IMAu5-1okkzVMMDpQq514x7IV4JbhiBTyLcl3u7GU3NAzXdQvnneL-l-Mhet5IKvFLY5mBf2JjIBsgMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc4c12292.mp4?token=l1NKTGV8jn0OZmd_DC2axl-N3jL9csemMZzn4kKZwZNqtXRUB9vpDF35LEqzvYi3K6fem4vZaWU1UvEXtyO0i_VOP2tLhFsVuKCKguKrnmpdAS86QLGASSOlhyWpwyEgVNXM4nQ1t3FNWIaR3IiZI8ljdkNd_FqvDyZOTtRLWOrMM7tb9OsoQb6L2gZKhg1e7B6zz7mIhTpSu2HQaiSshp8rAqZ19B4a0O7UlLfqH7n2FlO74_lHr6EuaVYg3HUgPROuN6IMAu5-1okkzVMMDpQq514x7IV4JbhiBTyLcl3u7GU3NAzXdQvnneL-l-Mhet5IKvFLY5mBf2JjIBsgMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبی(ص) هم جنگ دارد هم صلح دارد
🎙
امام خمینی(ره)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459358" target="_blank">📅 05:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os-wov3bjRRkKbERmTechwbAD7kVkTXaW7-rpEUUacV4vyZnyHpn7wtf52VPGLNUd4GEusL7HcOBm7Olw0HLmfJ8kxI72M_oPj6HWr-ojCkkRBpQWthPCj9pUEVyNNSjxnSJ6YkgRlCZL5vmjoQTI5v4T3CEb4KaDbF5oyGn_aZiBu1DNtALDgr6xSXbb4q0Gu17_RcNcXDrPk6nUHRm4qbMOofgTjF_Fk2i5blql4gWkmZMiZXR-r3t6oHDrziCo04KZjmfjSWCVxdwk0HrCUsao7tE5F4wr1X64rECv79ue7dE6FIaQsqzVR1g6O1oR_hKkkbADr2UZADohKXGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اتحادیۀ اروپا با چشم‌پوشی از استقلال و ارزش‌های مورد ادعایش، نقش خود را در حد مجری اوامر آمریکا تقلیل داده است
🔹
سخنگوی وزارت خارجه در واکنش به بیانیۀ اتحادیۀ اروپایی در حمایت از جنگ اقتصادی آمریکا علیه ایران: نویسندۀ فرانسوی، دو لا بوئسی، در رساله‌ای…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459357" target="_blank">📅 04:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN08W7mO4xTrjyo7zeZPCRmujNdFCEQZAqiEqk_CkQKmqv6UAW_Gz7oqKPgrV3aGU7YY3NXg1o7WJ8GdmLhY_9I0-WklKB2cmQIz-nFkCbWUl_KgGYMCw2Nvrg7aIQohlgi1XFi57sElvp6CHdpkmWiAcPeV5-LiPCUOsP37i5OtgMyxsQ1rnKnas8b_DV9ZjQ_gmmm_K3vzH9otCdqTlveT5f_f8AqxJW1M0gtaNlF6NENcyPNhta4Bibwf2TmDBlXm6J2IZdV0jsXIEKvlV7KneP0oidpth8Iz0ca3ai3MX1-YmB_1FuBa6cIPJfSEz8mTFB-St_4fwmRuHnZQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت دادگاه با خرج مالیات آمریکایی‌ها برای سالن رقص ترامپ
🔹
باوجود انتقادات گسترده از هزینه‌شدن پول مالیات‌دهندگان آمریکایی برای ساخت سالن رقص ۸ هزار و ۳۰۰ متر مربعی ترامپ در کاخ سفید، دیوان عالی آمریکا به نفع این ساخت‌وساز رأی داد.
🔸
این در حالی است که
نظرسنجی جدید مشترک خبرگزاری رویترز و مؤسسۀ ایپسوس
نشان می‌دهد که مردم آمریکا از جنگ ایران و هزینه‌های زندگی مستأصل و ناراضی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459356" target="_blank">📅 04:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ماجرای تجمع مقابل پتروپالایشگاه لیشتر چه بود؟
🔹
تعدادی از جوانان جویای کار منطقۀ لیشتر و خیرآباد گچساران صبح روز دوشنبه با حضور در ورودی پتروپالایشگاه لیشتر نسبت به فرآیند جذب و استخدام نیرو در این شرکت اعتراض کردند و مانع ورود و خروج کارکنان شدند.
🔹
تجمع‌کنندگان اعلام کردند که این شرکت پس از جمع‌آوری رزومه‌ها، تنها گروهی از متقاضیان را به مصاحبه دعوت کرده‌اند. آنها با ناعادلانه خواندن سازوکار غربالگری اولیه، خواستار ابطال نتایج، شفاف‌سازی و دعوت از تمامی افراد متقاضی شدند.
🔹
با تداوم ممانعت از تردد کارکنان، درگیری‌هایی میان کارکنان و تجمع‌کنندگان شکل گرفت که با سنگ‌پرانی به سمت نیروهای پلیس که برای جلوگیری از برهم‌زدن نظم در محل حاضر شده بودند، بالا گرفت و با تلاش پلیس برای متفرق کردن آن‌ها پایان یافت.
🔸
معاون استاندار کهگیلویه‌وبویراحمد در این‌باره گفت: طبق دستورالعملی که به فرمانداران و شورای تأمین ابلاغ کرده‌ایم، کمیته‌ای متشکل از نمایندۀ اداره کار و نمایندۀ سرمایه‌گذار باید تشکیل شود تا افراد بر اساس ضوابط و تخصص و به‌دور از هرگونه تبعیض و اعمال نفوذ ارزیابی شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459355" target="_blank">📅 04:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBvlRgZCvIKMWY6CmjfGUTEycSeEGM3gqEAiV3D9IB0OojYoaBxtd-GII8Gsly7bG0LLLLdYlQedHddynqY9fZN_ftvsdmjiXf2PLXn0_7xvyFtr3n8sXvzoJd9dtKJrN-aVw1hgyeJUTStdqjAtFHg4L5VD8o8oNEP2RQN8ufytUPC5OExDOcR5q0MQlc9ZBn6OU1XDvK-sAEdOD1kx5HZ9OCo6vsiW2vI-WZJeD0bwOHqBgEz2F-q1iZeQ8ZhRga3msuzTY8oWIufQufv8Hi-jhLkQNuhHSBAJaRe-pe-RcKzoV1b1h1mtnA1NFkt0fOLvKbYk1K_k4Yc2OeWxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار ۷۰ میلیاردی برای فنس‌کشی جادۀ مرگ یوزها
🔹
رئیس سازمان حفاظت محیط‌زیست: ۷۰ میلیارد تومان برای فنس‌کشی محور میامی-سبزوار اختصاص داده شده، اما این اعتبار برای تکمیل طرح کافی نیست و باید در فازهای بعدی نیز اعتبار لازم تأمین شود.
🔹
قرار بود در سال گذشته ۱۰ کیلومتر از این مسیر به‌طور کامل فنس‌کشی شود، اما بخشی از فنس‌ها نیز در اثر سیل از بین رفته است.
🔹
درحال‌حاضر، دو بخش ۱۰ کیلومتری در دو طرف جاده فنس‌کشی شده که سرجمع آن حدود ۱۸ کیلومتر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459354" target="_blank">📅 03:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حملات هوایی نیروهای یمنی به دشمن سعودی
🔹
ارتش و نیروهای مسلح یمن بامداد سه‌شنبه پایگاه‌های مزدوران سعودی و اماراتی در جنوب غربی این کشور را هدف قرار دادند.
🔹
رسانۀ عربی صابرین‌نیوز گزارش داد که نیروهای مسلح یمن به اردوگاه‌های سعودی و اماراتی در بندر «المخاء» واقع در استان تعز حمله کرده‌اند.
🔹
همچنین پایگاه‌های دشمن سعودی و شبه‌نظامیان اماراتی در الخوخه واقع در استان الحدیده نیز هدف حملات هوایی قرار گرفته است.
🔸
بر اساس گزارش‌ها، این حملات یمن با استفاده از موشک‌های بالستیک و پهپادهای تهاجمی انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459353" target="_blank">📅 02:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSm6oBYIZh5gJiV4mYcWmQKcWq9cuULZt2zyYg575dm1tbDEGKFqFRH0724wyyMWyKJJ5f5npZAKUhJUOk2aDS6hlKoJBORjhA7e6rchWk1VZpgG5PtnqcJfgaSQW2AFT5uQwm76CMNJ01LDs-ghSz7oEFlPLxXCds673fHrzAXMQxkKGwjg5hmT7Eey_SN1fGcnRlulE425a-vVzEUtYK2CVNQ93eWIo2qGotlIiQpK9D1r6WyrtXV1OE-6KMGAMiJngHrmX8IquuJKK7zxmvIu-m_aAsu2TLvL4NZ8iKddo0GgsxRbGFr_f4PRzc2Y07Cs0ItCF0xHeuC7Hue-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش هنگام عبور از تنگۀ هرمز هدف اصابت ۳ پرتابه قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/459352" target="_blank">📅 02:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1966c1289f.mp4?token=TnwLSxKJX0NuJlKk7-d2M1G7Qv90jcfijKv9NUSdl2Xg7rLaRQz1c8L8g8Sg5m4dMF2AK_gRSkwC1pfzgTdQNbcEIR8t_scNf0rtOXXESns_MfTI7aRw2Jbv8K2rGXCFxuHeMGWOAj6_d3ovzpsPXpoVczh4_jYZDWGUEXx1ZVqg4IZ94dPkkW-HG2tQccCui1_1BFL4s4MX_a5tzKhY8ZPYIHqUBPh8kIVRYVkq4kLeaLJIE0VjOtHD3lDs-SYfCEmZ5JQRgi2A1LLQJ5omx_DGUWK1_KYWxkT7aYTwvlpUXFUkWbNJfW6mxyJHwpViVBHHoopwm08aHP2_0I5I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1966c1289f.mp4?token=TnwLSxKJX0NuJlKk7-d2M1G7Qv90jcfijKv9NUSdl2Xg7rLaRQz1c8L8g8Sg5m4dMF2AK_gRSkwC1pfzgTdQNbcEIR8t_scNf0rtOXXESns_MfTI7aRw2Jbv8K2rGXCFxuHeMGWOAj6_d3ovzpsPXpoVczh4_jYZDWGUEXx1ZVqg4IZ94dPkkW-HG2tQccCui1_1BFL4s4MX_a5tzKhY8ZPYIHqUBPh8kIVRYVkq4kLeaLJIE0VjOtHD3lDs-SYfCEmZ5JQRgi2A1LLQJ5omx_DGUWK1_KYWxkT7aYTwvlpUXFUkWbNJfW6mxyJHwpViVBHHoopwm08aHP2_0I5I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور شیرازی‌ها در شب ۱۸۴ تجمعات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459351" target="_blank">📅 02:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1K3ZiJmKdcKWP1OKzxsSNyio1dPcuoHUyOzzRSff9xCqq-4gaxY_GuymyB5dr6iYDL7KTolcwgnx6hEc0MEjwQh1nxfRXsTIazKml96VXrKW0eVCm_RF3sQ_BhtOE2mfi9iwI-EuKwX5cGcrDWAM0yLRaPXYh9iWmuvxqhTTzLNEGelsuhSbHKcywtbTdTmMIkq6hPQj1ODDbZKBQmRB8B2lreAmSg0Msc2p2XGfhtiy6_nJ861NSeHY2Z-qCgH1DHl_I250Dr72y04uMmjOkZ8AV1w0ZdGLzHS0T_VgKQWkWv9T-zRCzyUnYNMJqUsZ4wDXxAGvKXBHk--HpqPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون برای جنگ‌هایش دستیار اختصاصی پیدا کرد
🔹
وزارت جنگ آمریکا رسماً نسخه‌های سفارشی‌سازی‌شدۀ چت‌جی‌پی‌تی و گراک را برای بیش از سه میلیون کارمند نظامی و غیرنظامی خود فعال کرده است؛ اقدامی که نشان‌دهندۀ عمق روزافزون همکاری میان بزرگ‌ترین شرکت‌های هوش مصنوعی جهان و ماشین جنگی پنتاگون است.
🔹
وزارت جنگ آمریکا در بیانیۀ رسمی خود، گراک را ابزاری توصیف کرده که به «سرباز» امکان می‌دهد مأموریت‌ها را «سریع‌تر و با دقت بیشتر» در طیف وسیعی از زمینه‌های عملیاتی اجرا کند؛ از تحلیل بازار برای متخصصان تدارکات گرفته تا مدیریت زنجیرۀ تأمین لجستیکی.
🔹
این نسخه از گراک نیز از طریق شبکۀ ماهواره‌ای «Starshield AI» متعلق به اسپیس‌ایکس، شرکت دیگر ایلان ماسک، عرضه می‌شود؛ همان زیرساختی که فناوری استارلینک را نیز پشتیبانی می‌کند و پیش‌تر در عملیات‌های جنگی مورد استفاده قرار گرفته است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/459350" target="_blank">📅 02:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcYmfCugxGSkJ2QS9ndDrEwMHC_xEDQsI5TycahAOtcMW1ZMCKVk1l80SnSYTD4oALZ0pPKQLwVXgXoZMl9vRGrUshaKKL1G72NbLeAJZwkVE7BEqlPYZAra2Vhdf2z2FLVWMcJoTtrKqGpwgzb4Ukv9CSqNXg1DQbPtf3VFitQydvz5kPv5ZbxRMtSx-l7oD03GVG1Nj-oFdyVQBwVIAbmny5iI-q3o5LJ9MFcxEZslqjY-P4s8Xw6HW10YD1rJfgBBFnTk86ghy22eEZPNr5HnJgPC2mDuFBzbgFw_sRJeqWr85jMAxuxpYb-rbXlUQNTAsw2ZHN9zT5ubKhjC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر جنگ آمریکا استعفا داد
🔹
نشریۀ وال‌استریت ژورنال به نقل از مقام‌های آگاه، از استعفای «دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش، بعد از ماه‌ها اختلاف با رئیس پنتاگون خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/459349" target="_blank">📅 01:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023803cd5e.mp4?token=d20lqbwfKATP3sncqtEBKPo_-3vmDmRwB6QUZV5x1256e2YtAEoPyllxHbVc_GzDg-u3cpWzbtC1Ljm0OuNNyin_PHhrHDdPMm2_r25JSSOL2yiQHHpH2lSG3REycWv41W_XoLITKzknvy41s4JyDaU_gj4sWUyj34bvs8vf-BKtqfv-2RATH_cW-IB7oNUV-3AE1sI---Af_69oQgBuFWufYMHtO9h3f6VQXGvMv-nFljKMJzRLLZRpV2mNYUrAdgzoW9jd4ivlbDolEvMaHIXjeB3mg2hpDKaMCpqhxaLfSc3xqL_9aIXPf3IjLpbLN4pNpzrd6ZiCwmu0wusPLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023803cd5e.mp4?token=d20lqbwfKATP3sncqtEBKPo_-3vmDmRwB6QUZV5x1256e2YtAEoPyllxHbVc_GzDg-u3cpWzbtC1Ljm0OuNNyin_PHhrHDdPMm2_r25JSSOL2yiQHHpH2lSG3REycWv41W_XoLITKzknvy41s4JyDaU_gj4sWUyj34bvs8vf-BKtqfv-2RATH_cW-IB7oNUV-3AE1sI---Af_69oQgBuFWufYMHtO9h3f6VQXGvMv-nFljKMJzRLLZRpV2mNYUrAdgzoW9jd4ivlbDolEvMaHIXjeB3mg2hpDKaMCpqhxaLfSc3xqL_9aIXPf3IjLpbLN4pNpzrd6ZiCwmu0wusPLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای جدید وزیر آمریکا هم دروغ از آب درآمد
🔹
ادعای جدید وزیر خزانه‌داری آمریکا دربارۀ صف‌های چند ساعته بنزین در ایران، با مشاهدات میدانی خبرنگار فارس از روال عادی سوخت‌گیری در پایتخت، به عنوان یک دروغ‌پردازی دیگر برملا شد.
🔸
وزیر خزانه‌داری آمریکا اخیراً مدعی شده است که صف‌های دریافت بنزین در ایران به ۳ تا ۴ ساعت رسیده و این وضعیت را نشانه‌ای از فشار اقتصادی تحریم‌ها بر ایران دانسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459348" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار مین حین عملیات اطفای آتش در منطقۀ حفاظت‌شدۀ بوزین و مرخیل
🔹
فرماندار پاوه: در جریان عملیات اطفای آتش در منطقۀ حفاظت‌شدۀ بوزین و مرخیل، یک مین در محدودۀ مرزی منطقه منفجر شد که بر اثر آن یکی از فعالان محیط‌زیست حاضر در عملیات مصدوم شد.
🔹
آتش‌سوزی در این منطقۀ حفاظت‌شده ظهر ۸ شهریورماه آغاز شد و عملیات اطفای آتش همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/459347" target="_blank">📅 01:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e7ed18f1.mp4?token=ThhRscxj_h7nZPTWm6jNCgrr4gcJFknA6APe4rLL-5cj6Z_W00LWpqn3MQGmnh500C1EWL7bQuE6-QYFFHiFLfyfFqXTl0gnjUZJI5NG8SUnVF8ulV_onZLwJtshbq_LKzKSLmijPeDDF1GsmVJ6-ryreA-nX8S1wyV1FghTjSdFJUj6rcTvJk97SDP59z1JF3faDOe8VIlRYIrRSrkHnwCO02sEKZWPEzuk0WrHJvse1U9gf3dP5RjP0YEUS7aRldzfX4LefQdw0fVy1QpzQJV259jPA9VDrhh8JAnJ2PafamD5r9TEJojasPtmVP-9Clq6__wc7k3uSUaho8qdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e7ed18f1.mp4?token=ThhRscxj_h7nZPTWm6jNCgrr4gcJFknA6APe4rLL-5cj6Z_W00LWpqn3MQGmnh500C1EWL7bQuE6-QYFFHiFLfyfFqXTl0gnjUZJI5NG8SUnVF8ulV_onZLwJtshbq_LKzKSLmijPeDDF1GsmVJ6-ryreA-nX8S1wyV1FghTjSdFJUj6rcTvJk97SDP59z1JF3faDOe8VIlRYIrRSrkHnwCO02sEKZWPEzuk0WrHJvse1U9gf3dP5RjP0YEUS7aRldzfX4LefQdw0fVy1QpzQJV259jPA9VDrhh8JAnJ2PafamD5r9TEJojasPtmVP-9Clq6__wc7k3uSUaho8qdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار زنجانی‌ها به شب ۱۸۴ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/459346" target="_blank">📅 01:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZcPC1-BAuJm-xJfAONO8omdV3hY4kYxWyOmgSjZyRDSEiW7DuNPw29Kip9huhnfKL8BF_sL4rvhINM_le4P_a0r7aLXKxs1hVV12O50MQaqpr882U4Crh2HM_u9n5kWQMF223MUarjTDiz__oxG_rIq2pwN9tHrxlP7oiH49JpFlBhnwJVyWoPRVcTBjqAzsAJtS0ruc-rU-ePtTFh4uD_2G8TzQBGjMsfsfcNc-aEuH2thnhOQkIbjQt-SlgBZ65xa8R_WV7Hffw1lsxY6RBRS99AEujwaayFxfGHGIeZKTCVoX6R93RGakznEnejPfumk8OJCGk8ryOSAB-vD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYw6-uyuCece2-uCJTbVMMovtgeGvP2UJHlFNEwgE5EeXupHlyannZb0aOqq3cw-nTnx-FChf-zv1B4MIalNShYZeQcM51OvGuO5Po5MhF2oejCJRrn89dn2MfVDEIZhpcOAzgqqIfvuVvmAB7ZiqzQfvecErgOJA5TZEb2_0_y0aUUOWE2TBRl7fOryArFQhY-YqNxf5E2W-gUqLQVgS-yiQTR2IaIr05tJQWTX2u_4Z02XtPH62k9B1g82GlhKsY0YWzIPO-uJih3_QuWkfQvr8dsC_uFKz-_N9IRJB5W_Kq4MO5Brc8dq2xn6mFYfmTgdHg9WHY5kqclhPGuBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmfMopEMB_Q7Gx1iIWfuVBfs7z_PZXjcacwxeXoqVEHKjRzEiXA2U14i0tLWwSyXILp1pmaHBwH1ByhFeCAI21kVqirzyOnZTDboWAGBz_5OsoYQbgEf0cgUYs4Z--tqi19nOXgbcmtpL3yVxvnU1x0WnwfWLd0I19UfKzOshuJVzr9aQ4vi69vX1tEpe4S-SJ6i9e8kMxyoDSkiB3tHs86iBwQrTDsPPbT7pfXJueW6Z2AZEMBsfuZ5pYWoXxV66zVWeHGELCDVXgd-qyasog7AnVPnIjNu2Zzz2NjGEy4m7VDEQyZrJKs2RYYNfnUvv4i6ivbsim0ryttwoTvF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIwjLXPMQUnE-TDjSbL9cVy00jfnxpWTjeEvaCl-HIO4OQgGoj9L44PUCtOV0wfrt5uBMSd8zHLH9w_Asq_GO3DQNEVJKW-wPUczZv-wxkwtk52HUdsaGOW6m-0KZHLLnDV9i8D5LRawyvXV9MP5E3LjCg_iwOX8uY5ymdFsZT8LD-muhHdJb_ghoFP7SYeM82n3krcaQpHKLli8JN3nCYuF6t7QjPGv_2C8P0RaF0Bcsao77zblL1S0A-LvTFbJ9kOyCP1oK0qn6pdK8AUA-UG_Iiv8h6AJBtaS9NYnvabLDS9iW70ecYM-Nw9usKk0A0OMEJCc4ce25HWs2P_Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti2PeqwP_G0wN6eH30ZzfY2KntUAIjMbTv55YEbh9LBr7oU8BElK_6YCWR0KNXNxhx1IGQ6ouWwif3xFOOJF7Gu2tqLHNUktUeB8nBJnYV2WnHyb_riTkZv0rU43HK_xWZPE4G4oEd7H-zxyLXEMaZBvj53A-Uisdq9OuIdOHR_0prnn8vszVRZAFHaMvixa2XaGzwXc5LTQjvhzex-tSIy1Vh5eASd_W4cDYu7FotxkBZkeSVQiOI8JCRK87bwzIfFxqYDt5tyvFnHL4CtQXF5RI4EqY6qVyyQMM2Qb22PFsddwWqBNwhnboXWi1c4pyzz7OlaG8aCCOtYJrYs7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHUPOXEqJm8L2__-rB3BcAftWWKz8mZM46J7PZDp-xUPhAhuVg5LArMoTZhCWbRvlE-A0jmMbyspIli7cvUuZA797FgKEBjg3HssQToIzgOhqje7JTDhiNPOc2fz2WGs0otMHgyv_OEQTQUqGDN6t3J2-mqdBWTz5HmABXoNEKwplwJOKwqx1mtUGrNlimZs4LNCyycFAKV94-qTrILOMZ-lxREOiZAnte73ALj9IkCJbLdfjCExz5YJLYq1UkHxDDaDXCJmgA-iUm1_6a3Y_Zf7Cq0owvW2TzAp4jUZjde1py9ZZ4SV-Qwa3LC043KdrmvH7brpZ42Hs478jMlirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7O-vtqhdkLPZbA3J6Qid_yEfOV2NBWMuJhAL3CXtDJmjMeRVMpjFwaxjOV7BRUF9L7NiYy5Hj9WSvZtxUDXy-tXQfeG6-S_c4bf6LUkANn8c91wXmyvPk07YOhJS6NqE1CTH9xV6f1BamrIHAp9BLn6dI5TtaZ7Xu_Nc4tzfWnfF3h5D127Of0wgtx4U8-JySo3sAk9OTIo1vlKgXFbK3Uh10fnWIzNcLbF5iNKjk1ZtFeivSyziivdIuQbJQAi5xMWp_KosKAA-asECtB_ktYo9AekZoHxA7uJxrskck2LDNAEAmro7aOlc4cu-EBTGc5lY1ee-B0RijnRzGtRDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۰ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/459339" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APBFh9E7NYvmfiAl8pyy7Qqn_jCBqOZMVRz0nfmUhzRqVG5unRCnENBZbTHvRV-PPEnPj-qPtB5e1k_8YQ7k1iPL8Ng_s98aEvxuYo7uxRQA89D4f98MsC1MQOuJwc8ArdaAim36Hze8rWCHQFu-pRRMWNT5X_vIEiYprFyLa4VzF7PqB4qLiF0ilSjBDnDtXu7A7oHd8x_h0xcIP8rauTPkZVXXWZbzjIXk3uzlw5ov_xtmPWj_iHzBWflwr50d9HhhJLW4zbPi6ng4JTElEWefjnNA4pKhPhgl_8QP8l4krqmND7AZhVvKdjL2oP6WuCNWhn9U0Kkqjo4IXdhr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQEhiI0_Gq4TZbh_bTSiLVXybDZb9fmrUfNEh0_Kok0NfZRSMJh2_DYYmsVljkTCSDfsjKs6dikhea-ANew8Fp8AUBfx_GGhoxCN2mzvKFaOBEYPWXFrgWw81aNRto1HUmNyftqenGxqcrMx_rf09-XkLNklyia4YEevIX6Bq77_cNVSDQP6o7F_M39DNzfI9KunDkhY2pMxkkbqUDt8aIpUKJKqQWyDlbE_FRC6G3N3i43suBYWNRvYPvxMzxdD6_sTKzqkxG965f7iZlbeAT80BS0Aw4Zx84fwGJ5RB7B5dQ0vRv8bDnKnNKsqBf_clbudJuGj9aGlb9zyBMMORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tm97aywvaA55A4AWXpMFWg_K2DJGzYaSuUk7nk_EiCqLQRB-Z_lcaYDlvqeb__EQ_ic_V0Q7FVjYbjSid1cnrUGFa6j7g39r8XJO5Dlgc6O47N6flT3NYktk_6bh-80oM7fGNpjwXGg9ojEIm7FmXqWPgIzdqWlZp9J_Yfa-qJcMVafrGMrbI9SlVEt335Gcb_2TN-9kpKpEBOzLmrK3zOaus0p-xC-sZ8HPjmdjSpm3a6t-_UtTM1Mr-qoH4RzFUH4N0j0M4gK3YopBpT1wIjyGEQHKFkINv3u8_7W2L2h2gKgzotKLVM8N-Q0fbpeeX1kJOmsrlX1d3Qc7nnqd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhX7-9B-YaWF6A5hXoXeaCNEmP7ebG6pByiJF6rP5J7f4VyHa0PocHflx5kP9WsJWUWqeqfKiHHSwnr_zopvbtlMQSQkJdvSeY3CyqfTBAGezGx85KhiL7ryUqriVXOI4M9T9Ge_TiIVE7VpTP4sVKXzP0FUjjZOs_5HfwVHT6rTQvdQGWNNYinyOAfVOg7em79yz_ViZ4zw8RE5UjKyU-hx_pX5JY4OktmKa9LeOB69B64eggAtnoRAZo4OqzhiI0TxbODvhX54v72BM4fw_ReqgCZ8FGHAf5FJzra_eLAqp8y9FJvcXeXbKCj-6B8BVWI4-FualJSONCpo86-J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohSOKrvFPTNXPM0m6Min_EDbD0SR-ub0HDKIIrLmM3QlMnUPApTu6YjfXDwQx0VYLKPFuhSpVuPoU_lR1RWpd66kXxZWg7FRpgtu6O1GgsoJqUxLkpBsf6Zbg_HGT9j34iMLwx568HjGY94YsfbGTt1i_z4tbsv6r77XxO1iXUCjRvlACcTAQglxBDZ6oA9lr_X1KQK0rcp4iHfYtSubDz_Gcbi34yVEDo847FWTDyWfo8LLdEhhgRNo10TS05nYAtHR5DIv6IsJui20MRzYNJc83LmxuopJXQEvI0oV87v-MfofVxTClYjFUJCCv113yb1A-CvRfzw7ZWbh96iFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kroyIcuJHz4IscnZxKMpaojEY4Gxzst2QPIThiuGhAuEIsVJnXLA61nlozgdi2c20Fp2RGFq1wPN3jtGyhQdORloGqosbsLqal66FC8ZrQOfSxQJHUWbMuC8IS91rtp7yZgkgSy67wivrTZb3fyIqOf9U2U6H4KVH-jFY4j9oQOeb1MLHTBzf2uttnp9bbACB6QMdQthmO3OTw69mXuzNt8SohTrCbEn0up7Pi88ZtPE2iEBqFlVdVie7zL5lTefUWdqBH1W7wLDa4jnny6l7XKD8lW_AeMet7tYNHmjLTPAUi_Bk5rVa2nf4PwTZwmDHbpAXyJyTr3utX0q8WKFPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spDO82CTNL-Ra7NfeKc_BaJ-5tqbrUkcICLArkZOb6y0J-xqfRdXro2PwfbtI531ljRBsHlOgdep_JHyMB-srictmVOuMZ9hbxp8XhlNrwn4pquj2cBNW2JRmgbc-HhQixOCnXjiRfruU_YYam9Tu6nR7bqrue6DqRbNk2kZruMRYw08XZNIo3J6dzYkzEXWEVuFZXazWCOzTkXRW1vKuk9Uvxvw1c5RiVGcqbUqDOdrOFR_cwBXigtOECEui--X8s9z-yIi5QymzPEGvj48EuTwmS42onioAkS945dD-3R38kaghE8oDyfXIdol8Xi7Rv_3uQQUasRfUPuGWNvSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWkjrtRpWHmLSUqYkC16x0xG_qrNrVn8cIdsFOkwA-G9leaDih-9Bfd9OlirXHMudZk5VTfr-cK1KwCdbq4RrIZYcmu_0JeIR3tebVqqfeQvg7gRzZLmSm2bd4W46eML_7C1BY7ZJgzqKzo6IJn-RS1SiwP9UV9U5kOAllG_k4JhVigsUTzVv0FPLJlTekKYC15YzqgCO4r59HaXoGcmhCtrIuCBXLXoXFuUflkUxkKJAOjNW-Jw-JdEzrwGhqIxsd50FpW_fRQf2x9l2LApqKBpv7cRnuISv20M4Taj0Se8pv0PwGqEzpx5lC_NNRQqKroKwvzUqHHr-JpAl1-tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBmxr7LtBV6pNzzpgnjxYIDoxFJg5mEerVEwnHDRMovsI6DiLd5tj99vEvGmqdY5XvhOgGuBlVc6LCyAwfYiijH7ktMOenp1wWAL1pLUgP22G0imLIswGZ9DBkG59fazCco8eAoGqkzSPVDA5pFCMvMkftKxDC_FOiTcOHXfCc-uRYHTuTnKEc_wkC2RWmjWTLjXViGDGdK4c__p6ury2kuFKZSSV0x18Vi90ya0qT5g1Ou9P0Kt5XkXvJFYCfbqjl-Iu6sIcOrsAVwCm9-Dbn5ASlRT0Y2H_AZh48MFk0o04SypOTaDaCDAKVs2XrUjS8PI9v2JQFJPex6x-nbqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS1zU-NbAuwuqMw6tEiAtIEAwf5uHgrbiFOXd1D5bT1LyVj9UPW7At_9v5G2aEQ3TT4kzMUts06QJUIBBBAgACW9N6dzUaeT-KPobp9e3o19GWjsMqEPj8-UPxXfvotwEskd4izrs8b1bGNXRv9sWeOEyk67-kRtPF2cUOopr2CjhmaMrKFMgdRlZzBHmsjQ5CKML6PJoebTlBoRX7Wx_rWlemr7E9ZPLqz8LR_f2s0VkOuyD8Thny2xz7OXykC_-jTHLU7srjFLUYb8DyU-G-_1j4j3gW8PtKyQnVILLDLsL6eyO_oJe-S8WtI3QmAtoYOenjDRu4_QfWD-9GD2jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/459329" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🖼
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در نزدیکی ساحل عمان خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/459328" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVdDjwoJI3XqA0KNL_VHsEPXmjQQiZPtEQxt-u3xggn3h0qmVZ0WSWRGe3C6IAh2dwSdT6M5pL-WIuuISZRpW9dbYv_mzyiQZDH_DXWnRRWL_O_iYwg6xvQw6mQpMZD3S6Ti8IXHB7waBmqzXVRT1t9e5Ghwku7IssZTICrLSIKnaTVNxr09_vV9rNbLYQXDsQHUBcnjZI0ycSobyaMLbTk8MiVrjA55Fal3z5zoItBheJTypEVGH-YWXctH6g2ZD9iRvJYjo8G3gbWUfrjsprbib0qA0L5NfxIxz92GfRlC7wveRX5onkh1ZVGAhk4c5maz-eW6h7qC349wu-QFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات صهیونیست‌ها به جنوب لبنان
🔸
با وجود مذاکرات مستقیم و توافق دولت لبنان با رژیم صهیونیستی، طی ساعات گذشته حملات اشغالگران به روستاهای جنوب لبنان ادامه داشته است.
🔹
المیادین گزارش داد که رژیم صهیونیستی با گلوله‌های فسفری منطقۀ کفررمان، و اطراف ارتفاعات علی‌الطاهر را مورد حمله قرار داد.
🔹
همچنین اسرائیل یک ساختمانی مسکونی در شهرک زوطر شرقی واقع در جنوب لبنان را منفجر کرد.
🔹
جنگنده‌های رژیم صهیونیستی نیز شهرک عدشیت القسیر در شهرستان مرجعیون لبنان را بمباران و شهرک القنطره و المنصوری را مورد حملۀ هوایی قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/459327" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUCc_b-hctlKO7tk7gBmzwRkVDV4js1fstO93TXd93xfJx7CZax6RYhFBV-X_Jg4kiiB-XI1Lk5Fyn-yuSczWqN5yA_u3eIFZqiCZDM_UKyCg7be_dBHMDl0sTrN-F7SkRQlunGTCr-Gusw8HWFucDZVrg1uXQPaVmp20FDGPqUZJUPdOxIXNP69EdLcjvb5nRjNa5a9x-D4MReurU53BsIOBllr-aEPvTJ0bxnXvVmszASjAb9R0_U-dbN9NBGGKkYffDRxYAIBamfQMDxHpWeeb7CZ9-6eI8OaI2bdBJaKTcJMaR4q7hjs0Q8v7ynD4nA3ctaCYZLhW0n_-CPq-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اتحادیۀ اروپا با چشم‌پوشی از استقلال و ارزش‌های مورد ادعایش، نقش خود را در حد مجری اوامر آمریکا تقلیل داده است
🔹
سخنگوی وزارت خارجه در واکنش به بیانیۀ اتحادیۀ اروپایی در حمایت از جنگ اقتصادی آمریکا علیه ایران: نویسندۀ فرانسوی، دو لا بوئسی، در رساله‌ای با عنوان «گفتار در باب بندگی اختیاری»، حقیقتی بنیادین دربارۀ زمینه‌سازان استبداد و سلطه بازنمایی می‌کند: سلطه فقط محصول زور نیست بلکه اغلب با تمکین کسانی که توانایی کنش مستقل دارند شکل می‌گیرد.
🔹
اروپا دیگر نمی‌تواند از «خودمختاری راهبردی» دم بزند، در حالی که عملاً خود را به مجری اوامر واشنگتن تقلیل داده است.
🔹
خودمختاری راهبردی با بیانیه‌های پرطمطراق به دست نمی‌آید بلکه با نشان‌دادن اراده و  تواناییِ‌تصمیم‌گیری مستقل و مسئولانه محقق می‌شود، حتی اگر این تصمیم‌ها با موضع یک قدرت بزرگ‌تر همسو نباشد.
🔹
اروپا باید انتخاب کند: بازیگری مستقل باشد، یا آن‌قدر به پژواک سیاست دیگری عادت کند که این پژواک را با استقلال اشتباه بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459326" target="_blank">📅 00:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d4640bd0.mp4?token=i8BDI_yeAYw-Y-7pbfVyv8rl5xPhCTV2QPjjRuwH97ClW5muRlUQLkRN5wa2fpm8udxUcLiDVj5UNir1t-PeXEVN4lAcIqdHRFfuRE9TT2o8MmdYXERpzrxl6woWDElQoIQyWaWcBmUEtKf4yQ22pV5ooLhvVbw9Omz9cYEa-BDn2Ch9j7ZNwDUISd4TbBSKFFZ5FdFNdvL-8vuPl972-VLYtecAkZQit7t8FE3qtp6CX0vAkfTO7tJcPqNdI2IKC_T4b_GY3yxgZnrYLEenW9xKzgUN_wDQZ-8NwCG_h2L0BZf0rXKu41cKbg2Byt0iJsoGXfJpJdmgxGx2D2A_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d4640bd0.mp4?token=i8BDI_yeAYw-Y-7pbfVyv8rl5xPhCTV2QPjjRuwH97ClW5muRlUQLkRN5wa2fpm8udxUcLiDVj5UNir1t-PeXEVN4lAcIqdHRFfuRE9TT2o8MmdYXERpzrxl6woWDElQoIQyWaWcBmUEtKf4yQ22pV5ooLhvVbw9Omz9cYEa-BDn2Ch9j7ZNwDUISd4TbBSKFFZ5FdFNdvL-8vuPl972-VLYtecAkZQit7t8FE3qtp6CX0vAkfTO7tJcPqNdI2IKC_T4b_GY3yxgZnrYLEenW9xKzgUN_wDQZ-8NwCG_h2L0BZf0rXKu41cKbg2Byt0iJsoGXfJpJdmgxGx2D2A_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: ما همه جان فدائیم شیعهٔ مرتضی‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459325" target="_blank">📅 23:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Of-QCVlBpWMBswosFYBBlThgNGggNZS0CT-dXw6NxhbpIZcHY9cykQR7CymRxrRxwferP5aW9I8LDVMmIaT0QMdycauaQ682R5OLfndKMfUTWIb5qJoD1pfvz7c80KMTrOMY4QdNMUYc5DXuuUCZcQdDK6KC1XtmLA7_dsujmO--XNad6oS2wQPDUsnMtLcPjHTtWXnamKGLGdnv88o9BwwrPQhmypeJqxILb4qq9xM8Z_NZGB9YLaFMFsjiLWWoT-Shh1uPPTsZwRlTix5h_DpqlANJcQ1GfU28uBLYbL8BGXKxZAC90ljayXVXeGgVBCJIWHimI3w5ML3FLBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در نزدیکی ساحل عمان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459324" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogXj3_iSCAbyf2nE-4pC9GaF5oVEzyrgWjL6sbG1jVTT_EwAOM2plN4zMpoqWEh77kEVYa0TldMjYw6muzr2Jq5S5IbU8KA-bcyvGKRZgAia1z77PSXtNP2GyAt6l_1mfizD_zZOA1xNsSMG4FD54LkqOpp35q1WFWFXr6KDDq9CWEcmMLsfGm9EfPWF189gWC2l68mqxvReCj5ebbL0_MV09l2z3VKjwBA36MKCbWdWTr3owm_I126ZBGGxKAy-mh6f_L6N5xcGJo305JBq0C3c3Y2gMSryIBgYjmpEKQQs5p6ez99sm7jg7m0T3fOwenGY6WKFwyoYG97xEcE4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ بنزینی ترامپ با ابهام ۱۰۰ میلیارد دلاری
🔹
بر اساس اعلام کاخ سفید، توافق نفتی ونزوئلا و آمریکا که با همکاری «نورث امریکن بلو انرژی پارتنرز» به عنوان اپراتور بخش خصوصی منعقد شده، شامل توسعه ۱۷ میدان نفتی با ظرفیت اثبات‌شده ۶۵ میلیارد بشکه است.
🔹
ترامپ در شبکه‌های اجتماعی خود نوشت که این توافق «بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی» به دست آمده است.
🔹
باوجود ادعاهای بزرگ ترامپ، تحلیلگران بلومبرگ و سایر رسانه‌های مالی نسبت به عملیاتی شدن این توافق ابراز تردید کرده‌اند.
🔹
وزیر انرژی آمریکا، کریس رایت، قرار است این هفته برای امضای بیش از دوازده توافق نفتی و گازی دیگر به کاراکاس سفر کند که شامل قراردادهای قبلی و تفاهم‌نامه‌هایی است که ممکن است در این سفر نهایی شوند.
🔹
با این حال، نگرانی‌ها درباره دوام سیاسی این توافق، واکنش‌های داخلی در ونزوئلا و ماهیت استعماری آن همچنان ادامه دارد.
🔹
پرسش کلیدی این است که ۱۰۰ میلیارد دلار سرمایه‌گذاری وعده‌داده‌شده از چه منبعی تأمین خواهد شد.
🔹
اپراتور خصوصی این طرح یعنی «نورث امریکن بلو انرژی پارتنرز» به تنهایی توان مالی چنین سرمایه‌گذاری عظیمی را ندارد و کاخ سفید نیز توضیح روشنی درباره منابع مالی آن ارائه نکرده است.
🔹
همچنین کارشناسان نسبت به کیفیت و قابلیت بهره‌برداری از این ذخایر تردید دارند و معتقدند حتی در خوش‌بینانه‌ترین حالت، افزایش تولید نفت ونزوئلا به سال‌ها زمان و سرمایه‌گذاری کلان نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459323" target="_blank">📅 23:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9915508bd1.mp4?token=IUVxq-PYsF1YiZBjaMZmMHTtzmCd6jK0jdyGxqQYmu_9wKd-7iLvfkVHrt3X8_kmZ3gEtF3C9NUySQRPtnLZGt_TIbAwrN8Q_YMB1sdIbtVkQE8IvIy9UAI-TC02IGaWJJbBS4GhbRqNOqsCkXiwTnxa1sEd0QrJj0CBMm22APcBpcTXKLz1L3VVcaY9tPWJzHp20FdGfhBuQj1ygeGmidlyBN4avCu_L5czKuOCTiB6C4d0Fm_YIQPe4beLnBSOm8-8Q4rpORHrPStx9NBY3In24IgfA16sYMQy_UvijVRmDk-WG5qYTqzyApfGqtAIhPBpMU6Ly6TQ628_gUdf07CEMl8O7mh1lbS4WRF3NqalWt03qqtm5j2OBEhoxkucxU-r8SK8TO-Z72RcMvDJg5iYG8S2LJMhFItqbblOhH40gcnBaq7Bj5nPlMkyBulV1uv5UHyRWzG1gBmeuiTO6IBM47nQh6Cy-nHDiRljTELhgy2GoCj75e64AB3ZX3chbnzHfLFaPjNfhODHYCxmXCwtVI6KeNOirSScmz68kAHMbBRMW5PPMg2OIsS5Pyg9u_L6qAyqSd5tYrNQk5hA2k8be5_yf5e9iAstFr3Mayc8n858Fb32mcLuaXml7JZLyARkr4nZJtr0q4yYksuqLfYRemulI5eY8anxhCKvC7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9915508bd1.mp4?token=IUVxq-PYsF1YiZBjaMZmMHTtzmCd6jK0jdyGxqQYmu_9wKd-7iLvfkVHrt3X8_kmZ3gEtF3C9NUySQRPtnLZGt_TIbAwrN8Q_YMB1sdIbtVkQE8IvIy9UAI-TC02IGaWJJbBS4GhbRqNOqsCkXiwTnxa1sEd0QrJj0CBMm22APcBpcTXKLz1L3VVcaY9tPWJzHp20FdGfhBuQj1ygeGmidlyBN4avCu_L5czKuOCTiB6C4d0Fm_YIQPe4beLnBSOm8-8Q4rpORHrPStx9NBY3In24IgfA16sYMQy_UvijVRmDk-WG5qYTqzyApfGqtAIhPBpMU6Ly6TQ628_gUdf07CEMl8O7mh1lbS4WRF3NqalWt03qqtm5j2OBEhoxkucxU-r8SK8TO-Z72RcMvDJg5iYG8S2LJMhFItqbblOhH40gcnBaq7Bj5nPlMkyBulV1uv5UHyRWzG1gBmeuiTO6IBM47nQh6Cy-nHDiRljTELhgy2GoCj75e64AB3ZX3chbnzHfLFaPjNfhODHYCxmXCwtVI6KeNOirSScmz68kAHMbBRMW5PPMg2OIsS5Pyg9u_L6qAyqSd5tYrNQk5hA2k8be5_yf5e9iAstFr3Mayc8n858Fb32mcLuaXml7JZLyARkr4nZJtr0q4yYksuqLfYRemulI5eY8anxhCKvC7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور مردم سنندج در ۱۸۴ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459322" target="_blank">📅 23:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6de282f13.mp4?token=bOm0Hxv1Krgb-zbo1FRfk72VXx45zfhb39xPc6fZmFASA3aBAoIxAdRINb_vCUTGDDyirPu4T850pxJIAwWD_bC9ae0XUFpMChkw9vJ-gwNbmBN6ttxvUCdGcV59w-hyCZvB_eiBZs7WOW_xfwk66nXpUSckC98lNZ8eqqO3I8UAKqQ0JaWGvI-BDVra_p8s3XYfQSmWNjtanVO_7cx7uCZtJ5uHcwp_dgMT3K2nMi7STbRQakMPi8vy69xrKAYHxZkyhWfNXbq1lDC1ahSLdLfAlDOU1DCC0bXtSlG3Zt_T9TjqQFpAgVZJ4kBOz99Jq7morjKzok_J-2Qx6uzD_7uzD_DjOzmPkGODQKYZqsa-mEtMscXtIt03QCn60wYzl5oiIkFyTDYrQCjJvM9KAqqkwvVCyW-cCKKWqwOuwinD1_1Bm3EbNYS4b4F_kEcUmC2sWuDgKI3GwbokTMmajububQC3wdu3g9-zBjZL1gtZW0unLD6YQNok7vPUJUlWLbbFIEFOIPQ6DqIziK24GmjBf76TabF3aS1_ox2CWqxwP9PkttmB1WLA4YOfLYC9jvhDGTyyFzZ1nYQDfGx5_IoGypu1G8Qp-jBTaYCz-HtHE8Fih1iYKs3mGXNe9Fvl05kYn-r6gmtNhO4uhvuT6IjG5TIc2tbQ9yB6HSXzFGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6de282f13.mp4?token=bOm0Hxv1Krgb-zbo1FRfk72VXx45zfhb39xPc6fZmFASA3aBAoIxAdRINb_vCUTGDDyirPu4T850pxJIAwWD_bC9ae0XUFpMChkw9vJ-gwNbmBN6ttxvUCdGcV59w-hyCZvB_eiBZs7WOW_xfwk66nXpUSckC98lNZ8eqqO3I8UAKqQ0JaWGvI-BDVra_p8s3XYfQSmWNjtanVO_7cx7uCZtJ5uHcwp_dgMT3K2nMi7STbRQakMPi8vy69xrKAYHxZkyhWfNXbq1lDC1ahSLdLfAlDOU1DCC0bXtSlG3Zt_T9TjqQFpAgVZJ4kBOz99Jq7morjKzok_J-2Qx6uzD_7uzD_DjOzmPkGODQKYZqsa-mEtMscXtIt03QCn60wYzl5oiIkFyTDYrQCjJvM9KAqqkwvVCyW-cCKKWqwOuwinD1_1Bm3EbNYS4b4F_kEcUmC2sWuDgKI3GwbokTMmajububQC3wdu3g9-zBjZL1gtZW0unLD6YQNok7vPUJUlWLbbFIEFOIPQ6DqIziK24GmjBf76TabF3aS1_ox2CWqxwP9PkttmB1WLA4YOfLYC9jvhDGTyyFzZ1nYQDfGx5_IoGypu1G8Qp-jBTaYCz-HtHE8Fih1iYKs3mGXNe9Fvl05kYn-r6gmtNhO4uhvuT6IjG5TIc2tbQ9yB6HSXzFGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم مراغه در میدان همدلی و اتحاد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459321" target="_blank">📅 23:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6f58959f.mp4?token=I9NDDw9-RHRucPOCuuUC8vBHhkJBuJjZt65UDu6Y0idl9-EJFG47-jhS6aG_p0XXj16ocwHIF6WnZdWNi8havCU7QdUSbdTvTmKbInBk3lAT_SmhmepNLPUPNwv4BDb6uRZSr17s5xN7-WO5Ucb9GdeZ55BRiPL34LEZ9dR8NnKswmTKazFfIi-rjMGSNRIEWf3e8x81hx-qKz7yXdd9GbKSUJ9BNTC2OLuxPnS7SgMW8K8BgCHnYkQuRXp0l0wBXNcW_sbwZfmXYUqUF0MxXF5ACdPeUlvhjHsHxY9rVdpdVaPARTT5OhJ19-0VAu3YWswTF_kiYIQvWWOXJP1d3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6f58959f.mp4?token=I9NDDw9-RHRucPOCuuUC8vBHhkJBuJjZt65UDu6Y0idl9-EJFG47-jhS6aG_p0XXj16ocwHIF6WnZdWNi8havCU7QdUSbdTvTmKbInBk3lAT_SmhmepNLPUPNwv4BDb6uRZSr17s5xN7-WO5Ucb9GdeZ55BRiPL34LEZ9dR8NnKswmTKazFfIi-rjMGSNRIEWf3e8x81hx-qKz7yXdd9GbKSUJ9BNTC2OLuxPnS7SgMW8K8BgCHnYkQuRXp0l0wBXNcW_sbwZfmXYUqUF0MxXF5ACdPeUlvhjHsHxY9rVdpdVaPARTT5OhJ19-0VAu3YWswTF_kiYIQvWWOXJP1d3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: خداوند به ما لطف کرده که لباس «گرفتن انتقام خون‌های پاک به ناحق ریخته» بر تن ما باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459320" target="_blank">📅 22:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93e7c790a.mp4?token=g1CWR3g5Rv4TYtYYdd_Izc6oqCWAvzfnNPXQTS_zpYx8y6PIAVj2xGDlBUA6Jv72GDAyFHWwwzpUjZJErbovK0UFCb2SbAGA9G_7BZtyrlTnxJrTZ8c_VniHXHvqfpYhczwva9VOsSNhsdJJUUtAufmCCBkHSRGxz4uNilwUeF8i-kz4q83aUHebvUnTJfdSH1iRsMpcDb-r0KV0UUHPn-t3en-sHXk0p6v15VAGK-j4zbTv2rhPnYSNSFa3JoXq9beEmcF4RCoY7YdYcbdFTW_FMP8dNIs7RMXEAysk6UqMWdPPcFolRPmA0_TAYgGDFEVFCQ2xka0fSvPNaOiM7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93e7c790a.mp4?token=g1CWR3g5Rv4TYtYYdd_Izc6oqCWAvzfnNPXQTS_zpYx8y6PIAVj2xGDlBUA6Jv72GDAyFHWwwzpUjZJErbovK0UFCb2SbAGA9G_7BZtyrlTnxJrTZ8c_VniHXHvqfpYhczwva9VOsSNhsdJJUUtAufmCCBkHSRGxz4uNilwUeF8i-kz4q83aUHebvUnTJfdSH1iRsMpcDb-r0KV0UUHPn-t3en-sHXk0p6v15VAGK-j4zbTv2rhPnYSNSFa3JoXq9beEmcF4RCoY7YdYcbdFTW_FMP8dNIs7RMXEAysk6UqMWdPPcFolRPmA0_TAYgGDFEVFCQ2xka0fSvPNaOiM7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مادر مینابی از لحظهٔ اصابت موشک و نجات دخترش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459319" target="_blank">📅 22:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzppv3XGj9WGvCfVCXD9yrfuwOzbEjYpctHa9Aszm56n6u8VnKrJlViJb8YN8uChVhqI21nHXhCJzqd_HkZDBX72Idld11IY2pkt9t0cr1GJ3qhp4J5lrc4qjsxrzd-DEpmXOJ5jM-3rXE-NNtIXixufCUpjQIfYxgl22B-zoVsIzbDMejw7ZH4YsdENXnYEJHLAObiOgjraoBrUIserirOKmiBaoVyI5TpW9ojX4Z4XsB7krx4LrtknbFqdrqp8cm9C6dLosthJakMbDReFRUD6bUnQKik3ROJnYMAEa3mGl4KdgPsaYPS9NwKYUa8DQtNVqdIje0I1JX1vJ5n86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیشهٔ عمر ترامپ درحال شکستن
🔹
ذخایر نفت آمریکا باز هم کاهش یافت و به کمترین میزان در ۴۴ سال گذشته رسید.
🔸
پیش‌تر ترامپ، بایدن را به خاطر کاهش ذخایر راهبردی نفت، مرد نابود‌کنندهٔ آمریکا خطاب کرده بود.
🔹
هم‌اکنون ذخایر راهبردی نفت آمریکا به ۲۸۶ میلیون بشکه رسیده و کمتر از ۳۶ میلیون بشکه تا کف عملیاتی خود فاصله دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/459318" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما اولیای روستاهای دالپری، جلیزی، پتک اعراب و نهرعنبر با نگرانی عمیق نسبت به وضعیت آموزشی دخترانمان، خواستار احداث دبیرستان دخترانه (مقطع متوسطه دوم) در روستای دالپری هستیم. دختران ما نیازمند محیطی امن، نزدیک و کم‌هزینه برای ادامه تحصیل هستند. با این هزینه‌های گزاف سرویس و کرایۀ رفت‌وآمد، تحصیل دختران ما با خطر جدی توقف و ترک تحصیل مواجه می‌شود.
🔹
خواهشاً موضوع حذف بنزین خودروهای قدیمی را پیگیری کنید. اینکه مشکل کسری بنزین را از ماشین‌های پایین می‌دانند انصاف نیست. ما یک پژو ۴۰۵ مدل ۸۲ داریم و از سهمیۀ ۶۰ لیتر نهایت ۳۰ لیتر مصرف می‌کنیم و امکان نوسازی نداریم. در حالی که مدل‌های بالاتر بیشتر مصرف می‌کنند. دولت باید سامانۀ پایش مصرف طراحی کند و مصرف مازاد را شناسایی کند، نه اینکه تر و خشک با هم بسوزد.
🔹
ما مربیان پیش‌دبستانی الشتر از آموزش‌وپرورش گله‌مندیم. نزدیک ۲ ماه است پیگیر لغو مزایده و حتی تمدید یک‌ساله هستیم، اما می‌گویند خودتان پیگیری کنید. ما مربیان با سابقه بالای ۱۰ سال باید با کسانی رقابت کنیم که هنوز مهر مجوزشان خشک نشده. این چه قانونی است؟ سال‌ها بدون بیمه و با سختی کار کرده‌ایم. لطفاً به گوش مسئولین شهر و استاندار لرستان برسانید.
🔹
از شما خواهشمندم پیگیر قطعی مکرر برق در اهواز باشید. طبق گفته وزیر نیرو، قرار بود تا پایان شهریور برق مناطق جنوب کشور قطع نشود، اما متأسفانه این روزها برق به‌طور مکرر و درست در اوج گرمای هوا قطع می‌شود؛ در حالی که دمای هوا بیش از ۵۰ درجه است.
🔹
معلمان حق‌التدریس کشور با وجود تخصص و توانمندی که در طول سالیان متمادی در عرصه خدمت ثابت کرده‌اند، همچنان در بلاتکلیفی مطلق به سر می‌برند. علی‌رغم وعده‌های متعدد مسئولان ارشد وزارت آموزش‌وپرورش موضوع تبدیل وضعیت به قرارداد معین همچنان در حد شعار باقی مانده است.
🔹
لطفاً قیمت‌گذاری عجیب خودروی MG360 را که در مرحله اجرای حکم توسط ۳ کارشناس رسمی انجام شده، رسانه‌ای کنید تا مسئولان مربوطه درباره این موضوع توضیح دهند. چگونه با مبلغ ۱۴۳۰ می‌توان خودروی MG360 صفر، اتوماتیک و توربو خرید؟ این موضوع مربوط به حدود ۲ هزار حواله‌دار است که خواستار شفاف‌سازی و رسیدگی به این قیمت‌گذاری هستند.
🔹
لطفاً مسئلۀ شهریه مدارس سمپاد را پیگیری کنید. بر اساس شنیده‌ها بعضی مدارس حدود ۵۰ میلیون تومان شهریه در نظر گرفته‌اند، در حالی که قرار بود دهک ۱ تا ۴ رایگان باشد.
🔹
ما اهالی روستای پیرخوشاب ۲ در شهرستان جازموریان خواستار رسیدگی فوری به وضعیت زمین کشاورزی روستا هستیم؛ زمینی که تنها منبع درآمد و پشتوانه زندگی بیش از ۱۰۰ خانواده محروم است. این زمین طی سال‌ها با هزینه و تلاش مردم آباد شده و اکنون بیش از ۱۰۰۰ اصله نخل بارور در آن وجود دارد. زمین که پیش‌تر در اختیار ادارۀ اتباع بوده، اخیراً به شرکت ماهان واگذار شده و این شرکت قصد دارد آن را از اختیار مردم خارج کند. این اقدام می‌تواند معیشت خانواده‌های کم‌درآمد، زنان سرپرست خانوار و جوانان بیکار را با تهدید جدی روبه‌رو کند.
🔹
من خودروی دوگانه‌سوز دارم و مثل خیلی از خودروهای دوگانه‌سوز موجود، تاریخ مصرف کپسول CNG آن گذشته است. حالا جرئت استفاده از خودرو را ندارم، اما می‌بینم کسانی که هنوز از همان کپسول‌های تاریخ‌گذشته استفاده می‌کنند؛ کپسول‌هایی که می‌توانند بسیار خطرناک باشند. قیمت کپسول به‌صورت نقدی ۲۳ میلیون تومان و به‌صورت اقساطی ۶ماهه ۲۷ میلیون تومان است و واقعاً توان مالی تعویض آن را نداریم. لطفاً اطلاع‌رسانی کنید؛ شاید دولت بتواند مانند گذشته طرحی برای تعویض رایگان یا با هزینه کمتر اجرا کند.
🔹
چرا در طرح نهضت ملی مسکن، بخش چهارفرزندی حذف شده است؟ از سال ۱۴۰۲ ثبت‌نام کرده‌ام و امسال برای پیگیری مراجعه کردم، اما گفتند طرح چهارفرزندی از دو ماه پیش حذف شده و فقط طرح سه‌فرزندی اجرا می‌شود. در طرح چهارفرزندی، هزینه آماده‌سازی زمین از متقاضی دریافت نمی‌شود. به شهر جدید بینالود، در ۶۰ کیلومتری مشهد، مراجعه کردم گفتند قانون تغییر کرده و فرزند چهارم اعمال نمی‌شود. لطفاً این موضوع را پیگیری کنید؛ چرا قانون برای افرادی که از سال ۱۴۰۲ ثبت‌نام کرده‌اند تغییر کرده است؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459317" target="_blank">📅 22:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459316">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9723c6bb36.mp4?token=fyQDVu_w1ClrjgsC_qLhomL7lC3gCl5j_2nkjmCZqgeilGPo_GyHElQebd9M73o-HFEuY9jrfEgYLgD3CnPOmQlB7rMJbPq-c52n6Q0Ym4MDEvxIGTYe1D6K6A5oSvK0dMNMObfwFDfs4YHpdNlgy-0XoYh-3bOHEej9cd6Ctj6EYMaxIWeaYFl_GSrWhuzgGBjfOi-JqjAwBvJI-yoY_e3Qfbtomk3RlnOs1ysiiSBUCHtnLwiQs0cxkqAl2puOnddInCz2XjsYv8EUt_-UIi0PzmDJKYpB1OOQA44GffpUu2TLuxKC4xO_j119WKOiCkYNZ_vnBY6UCJtiCYTF9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9723c6bb36.mp4?token=fyQDVu_w1ClrjgsC_qLhomL7lC3gCl5j_2nkjmCZqgeilGPo_GyHElQebd9M73o-HFEuY9jrfEgYLgD3CnPOmQlB7rMJbPq-c52n6Q0Ym4MDEvxIGTYe1D6K6A5oSvK0dMNMObfwFDfs4YHpdNlgy-0XoYh-3bOHEej9cd6Ctj6EYMaxIWeaYFl_GSrWhuzgGBjfOi-JqjAwBvJI-yoY_e3Qfbtomk3RlnOs1ysiiSBUCHtnLwiQs0cxkqAl2puOnddInCz2XjsYv8EUt_-UIi0PzmDJKYpB1OOQA44GffpUu2TLuxKC4xO_j119WKOiCkYNZ_vnBY6UCJtiCYTF9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: برنامه داریم ناوگان حومه‌ای تهران را گسترش دهیم  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459316" target="_blank">📅 22:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff7bc0562.mp4?token=RwdEBdrlAeL8SiAteWdWbvocZ154wcRt_qTOvPRqVvirqlx9j1a6So0tYXWobyFbpuGa2vKQ-GcG6yvbznNCEaFkjagR8uydV_sz5lYYIFqE0UqJpVMOzJaFqM7vZI1H1o0qXeJBtO9SgWq_FdTDxi6cg4KZ8d4ONTGKW4xNv0Fecrt-ybXjZqABqBOknwqqbsu2icWIrJ7kSJgD4xiWf4WG_6FoUcqpkow3CeXnNPYORj-SvGhkFboXM1eip1yTFXkr9xGC1lOd4SgAK09F1SjxoB4qMGmDotZlGwPLqgPAsYMP5Y_YKDMsz3bCtY-QgdytYiFo7OIZKvi8tMJhaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff7bc0562.mp4?token=RwdEBdrlAeL8SiAteWdWbvocZ154wcRt_qTOvPRqVvirqlx9j1a6So0tYXWobyFbpuGa2vKQ-GcG6yvbznNCEaFkjagR8uydV_sz5lYYIFqE0UqJpVMOzJaFqM7vZI1H1o0qXeJBtO9SgWq_FdTDxi6cg4KZ8d4ONTGKW4xNv0Fecrt-ybXjZqABqBOknwqqbsu2icWIrJ7kSJgD4xiWf4WG_6FoUcqpkow3CeXnNPYORj-SvGhkFboXM1eip1yTFXkr9xGC1lOd4SgAK09F1SjxoB4qMGmDotZlGwPLqgPAsYMP5Y_YKDMsz3bCtY-QgdytYiFo7OIZKvi8tMJhaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۸۴ شب چراغ خیابان‌ها خاموش نشده است
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/459315" target="_blank">📅 22:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef54732e3a.mp4?token=X_SRxJKl4-EDdg7kL34QljnrZk8D_u1OliWAj4KgcynOn-WAFM1MAOfmgIdmKx-ZM0z6Q18q_yApR4LM9t_31g6W79z17KWRasaR4Eby3h9HGaa42SbWbyXT8399XugGR5dcCI68ny3WYrPRhWFvKahRom6119fWfYg-ZalWnMmAU_Lu3ke47ZPGvFK_cpTm3Tvp8VHJetamroObzTyzfTTOGfDQnqj8jeSP6N2C5Ohi7I0IabjuCGAqI6psdlbC5w1LU7bD6GkSjciJ7RVP1sviQjOHeW1kpNR1nfML0ggONUuVsbJot95KOgBcuZJmFzaDCF7ESc52owEIOnMwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef54732e3a.mp4?token=X_SRxJKl4-EDdg7kL34QljnrZk8D_u1OliWAj4KgcynOn-WAFM1MAOfmgIdmKx-ZM0z6Q18q_yApR4LM9t_31g6W79z17KWRasaR4Eby3h9HGaa42SbWbyXT8399XugGR5dcCI68ny3WYrPRhWFvKahRom6119fWfYg-ZalWnMmAU_Lu3ke47ZPGvFK_cpTm3Tvp8VHJetamroObzTyzfTTOGfDQnqj8jeSP6N2C5Ohi7I0IabjuCGAqI6psdlbC5w1LU7bD6GkSjciJ7RVP1sviQjOHeW1kpNR1nfML0ggONUuVsbJot95KOgBcuZJmFzaDCF7ESc52owEIOnMwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکهٔ سه از جزیرهٔ لارک
🔹
تنگهٔ هرمز همچنان بسته است؛ هر روز کشتی‌های مختلف هدف قرار می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459314" target="_blank">📅 22:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459313">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFjwtjp2R-KsOK0wAMcULej9I3cSnF1MVPStZh6xfWZtTwXZh7KFmO3VvNG4YN1FHRsWdQm7EutPjkzdSRH_DK-gqXRQwmQLoC-5ucnvkiWbxEGCL-2a3xHPvmjDoVvw-m6urXxjF20fG6LhP-ydcU8dxgMyJQmms9ptGqAUE0TAMg2zXm4eLtWy1D_lUTfPdXdS10C1c6NHHxqt7rO8b1XIgH2hYfzWsChPhtWt_31sMxjWhQn9L14cAo1rfj_AQO9zA3B5Z17I58HmXLUR1aPIX_LbLp8VGvZkpdmTorPUl7w608Rq-GJ0wBbZ9C2S-wt_gUXud-_LpNbXMrbabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا برای مهار پهپادهای چینی کم آورد
🔹
آمریکا تلاش می‌کند با محدودیت‌های تجاری و فناوری، حضور پهپادها و ربات‌های چینی را در بازار خود کاهش دهد، اما مسئله اصلی در این رقابت فقط دسترسی به بازار آمریکا نیست.
🔹
چین در پشت این محصولات، شبکه‌ای از کارخانه‌ها، تأمین‌کنندگان قطعات و ظرفیت تولید انبوه دارد که محدود کردن صادرات به آمریکا به‌تنهایی نمی‌تواند آن را متوقف کند.
🔹
بر اساس داده‌ها در نیمه نخست سال ۲۰۲۶ حدود ۲۲ هزار ربات انسان‌نما در جهان عرضه شده و ۵ تولیدکننده بزرگ این بازار همگی چینی بوده‌اند. مجموع سهم این پنج شرکت به حدود ۸۶ درصد از عرضه جهانی رسیده است.
🔹
چین از زنجیرهٔ تأمین صنعتی عمیق برخوردار است. بخش بزرگی از قطعات و تجهیزات مورد نیاز برای ساخت محصولات الکترونیکی، رباتیک و سامانه‌های خودکار را می‌توان در اکوسیستم صنعتی چین تأمین کرد.
🔹
همین نزدیکی میان تولیدکننده نهایی و تأمین‌کنندگان قطعات، روند تولید و توسعه محصول را ساده‌تر و سریع‌تر می‌کند.
🔹
این الگو را می‌توان در بازار پهپادها نیز دید. پهپاد برای چین فقط یک محصول فناوری نیست؛ مجموعه‌ای از موتور، باتری، دوربین، حسگر، تراشه، ارتباطات و نرم‌افزار است که باید در کنار یکدیگر و در مقیاس بالا تولید شوند.
🔹
بنابراین، چالش آمریکا فقط این نیست که چین پهپاد یا ربات خوبی می‌سازد. چالش بزرگ‌تر این است که چین توانسته است فناوری را به مقیاس تولید تبدیل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459313" target="_blank">📅 22:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5Y-v1HAZmX2_nvU4xXT4o8tvzlmsrfvJZNejBCxdChD8wJEfw5XxndIB9Bzb4d0LkiwaH_S2jkYfajmdDEcIYZIVK2DSjAlIOH5V5brZuYV6n10KL7DcHX7PaaV58ixTD98EgP0ZZz_HWZPUCsIrTtcs3Ke73GqBuaXKrqJ49nY3sb_q3UgRTLycYIPj7B4YIflMKy82cK-NKK4zqjIjc2qU5jBWtOfhF5Uw_roEoxRebp_aSWAUgEYVNqK_DAzORhc9Ym_TK1Vcavi8MAuck7BeDNgwMYw5C0IHHGHeVw-_dzITJmcdQtItulXTQ9KRDleHYD_2zT5oMloJWI2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس: ارتش آمریکا در حمله به لامرد از سلاح مرگبار PrSM استفاده کرد
🔹
رسانۀ آمریکایی آسوشیتدپرس امروز در گزارشی تحقیقی نوشته اقدام آمریکا در حمله به «سالن ورزشی لامرد» با استفاده از موشک‌های «پریزم» انجام شده است.
🔹
آسوشیتدپرس این موشک را «سلاحی مرگبار» توصیف کرده و گفته ارتش ایالات‌متحده برای اولین‌بار در لامرد از آن استفاده کرده است.
🔹
این موشک می‌تواند تعداد زیادی ساچمه فلزی را در منطقه‌ای گسترده پراکنده کند.
🔹
نهاد آمریکایی «ایروارز» گفته ۳ موشکی که روز ۹ اسفند به شهر لامِرد اصابت کردند، غیرنظامیانی را تا فاصله ۵۰ متری محل انفجار کشتند.
🔹
به گفته این گروه، موشک‌ها بر فراز یک مجموعه ورزشی و ۲ منطقه مسکونی منفجر شدند.
🔸
مقام‌های ایرانی گفته‌اند در این جنایت آمریکایی، دست‌کم ۲۱ نفر در این حمله به شهادت رسیده‌اند که ۷ نفر از آنها کودک بوده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459312" target="_blank">📅 22:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYxBgec5wLxPpSnSMjR6Ioo4WdwDGXSE3HEhKMxUfaZNUs0bR2xiHwPNM0iiqpKsKd7-hojudfQvYq3w_uGSoVoqpWLOlktl9xzJyMlm4ymu9l0Y2pteDjIIm5S6IC6hXF0y5zjXPju6-gl2S0v3wI1QduWPVupMGiAzOIZ0pNTLEokzz8ajEVXizbzNY1SA9cs1jMYwRvflPGiii0wlfU_kvC2aG8dogWdaXH0BxaYkzdN6YrZdouhBJnhq3n-zelFnBF0c9uxZYwZO2zdXaPpntcJvjxe2me4KOpU8OZIUqp7CU6dEgEkVsUqwO99ZFDGEvFdYe0ADMXGM1E3-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت گشایش‌های پیوسته؛ از اشتغال و تولید تا انرژی و زیرساخت
🔹
روزگار ما، روزگار دوگانه‌هاست؛ از یک سو موج‌های ناامیدی و از سوی دیگر، تلاش‌هایی که بی‌سروصدا در گوشه و کنار کشور ادامه دارد. در کنار همه چالش‌ها، طرح‌هایی در حوزه اشتغال، تولید، انرژی، زیرساخت،…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/459311" target="_blank">📅 21:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2zMP5cn0gcZPWssd2MnxXlp4lGpmLySAi1lqOnOJryoqGSdnXgdtzDmTWCQhpkid1Ivk1DqfZBpANt9m5f28I69JqB3eY52tfyt3_sjYDF_AOLilygyi2b5e1OZcTLeDMDFvVJFL81Ruqa5f96GVIZ9FPqYWOTJ0j3qZgRQDpY2UsBd5Wg8f204i_RKS8_q74BpoG-ofgZmk0rKrCzbvudwrA52KONfAGlc4Xw06oYryRlJiwJAAhaZTniFbLRpFSz1nih653K-y-RZxbyu6-pLR8ILWMuYAhq-7cLO8__Yo2TfDs9OQdub6EvIQqOft09GeupGrdWXWhyzcu36jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_Wwm5wBoS0RaHbvBeXfg8Kps4Uy4mdlUfafeRid26u4Cs5bNf8igAUWiLS5eZuZbQ9cdmWl9_merc7AIKps5C3_Nwi7p1I4VNVeyMq8lfqQ3SVUUY9qGbns4C2zYu2JoK8wnR5YeUV0BBJk_pzgt-1Stp2xXDdKvoC8ZVsXYKY0CkXAn6zG0Ou7BMCl-SYZLnfuTLD4X7gs0nOVIYRV_sW-Mj9oaio5iavv5sWx0Kl-dXp0spkd9UAy4NG5r3ZDadcVMgoXE1DJECJsQU2rKk9O41mcFZ-oQD8mjKmbSFyRNEM4n4pmv_9FUhL_jfqQ2ZkUPovgtzxOaskJ30r9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlk1walMQit0UoRhYV86aCiJeUnGbfi_R8j_qfJB76ANneLRtWsKH8eXVzKOTtVHV4aYlg8fsAQTTf-PBGoIioyjB-gxS_Zc3KewJmH_SeGixRsCHMDT--sp80wnaEkKz1RyzsByFZj_LfmgNaP0QWZBDjvOWZt9UvUCwzPHmQk3H3PKRB1g_NDHP0YfPx9tJQlj4FStlA1aCmNNObE8fPA78GT8YeBJmDQaC1kq-9bx27-hBaHDH7_Tnn-ldxCmSHPpL-9EAoJITGvEFHWjd4kIB_fbAyPPTlBH_6vuA1Z5LoCs-2ED1hg1ujSJlC2SUcUbJ7JgH95bgQ1OmIKYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wbuuz_vvnlMBx0EqORWr4aNpHxBX4Ph17cMl7A-9BNbmfDHjdp6rjF6Djm6OnwgzLF9QJXULwtuil6jZ59gln2CsA7St5gn6mKLxrlRATa8zPtu9qaWQ2OgheLBxSUHFaVumAoW-hzcHa3eKKOHEUir0nlMrNnXwevalmABzqROIetsn7qFkNKHvXvVtQ5effQ3dCW08HJdHrU1h37Es3dancU65SEFdIUSEyFF0HN3hIdLMuHg8wacr1gkpqrsjfzAQqwxVfjiU2fpidrJXG96pKm5lSLz0pRyNNs5l3wAwgpXiUNEDZQ2_C8SGIwUhZVEDTiNbnu84IXSNCeXJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bG6mnXPkgi6-SUwmJo6qd8yGZGGzYJgj1xVFVzIpoidNDPqnSs4R_Wx8hc_Hr21JyEiyNxNyz81C6bL1V1WQHiFKGvpkrYdJ2Xa6NkWZnVfu6KIRlTWsdRAtV1NshOyEDmIwFAamhH0I3WSiIvod3jq6Z4BHUcwuoWEcXXhE82TWicnbmbw9pfz0pG0lzzPFEmWBOpr7_EgWdlNZZkGtiNGeaCBPR1OvWrheZc2-dBQT6q9ULxFdSBHj2I04VULUlt-i3RCYyjdqoITMrZDzo5BQg6VpjYiCTXW42YngXRFE2Hixe99Vsp-BjFSrk31MOLtqYqPX5GgKlnITyEw6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdyniSXiJTRhW5dW4OpyxftwJN3Q_kVRADxBX-fF_For_1gkaWqp2Oi7CeBzEg18asYSN-jw5SpD6FYylmB5J0hWGC97u-YuVy3Wl-keC2sVHYk89dp_jdf1utWSvjyJ_NzzsAEa5-pUuOK02cEGgsTHI8c8acM_m_jzmVSR49jCoRsc-mvr1c0jS0IggqRzZaLbRr4TFsdcQsiNrtVaAtcXeQjyhr8B2Th8qbv-eA_1XMuOOjDjkznvmhm5TEj-Yte_tzebEuMqaN47sDblsMtnJTCPFLggQwRBQdtgwIF00IxJZvdOWmXaXL3jbrw8tnxFfbHdnzR0TYlB7OBBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjRCUx4WiFab4QvJhcD03xuP3C4g-pPlTXaUBWS-Me83t8jIemmdRhM-S6KA1zLODYlrvxcGczyuhX3bwOnhKnbfauxL_ES9blIyNuzSElxxvjjELhEnllLs_LRhiMEdAHlBdxOscQAgynNOS7xESwMe-l5ddxDq5Jjg4JeJvFxoivzzkCJctSK7UzC-H793IJechzO7RDQLxpvyPUHx8CVFMDJD-P8U7e9RZskJ3kk23u_1q1yh3iVLrn9CelkGrUSApVUv1l74CtXsG0hfouqyEMbaiT2aO8SfHKg5IWtNYBrK4FERkijXOh3RKtyEU77gMFz9Ift7LkPsypO2JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهارمین رویداد نمایش اسب در یزد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/459304" target="_blank">📅 21:52 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
