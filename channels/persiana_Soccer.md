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
<img src="https://cdn4.telesco.pe/file/uQhk-sN4BYEX2u-XZQCdiJTOwlohhS5TRWvkaDwWKKRR49SEu-Gj0BKi_kM2efxvizIdexUN2xtbsgIJAjSbZ3eBq8TtPqNizxI10tTxJhHB8ihTP1QcJWQ_4WuzQ4LCSGS8CB1SC9ZI993XWs-7i5SYI0GeyfZMV6Ac380EhaEeJdWbgtr1WZYKOuzyUwkafw6z_Bi1hILqGJZRfZKvI1FmG6T62hfdF_YrWaRLlD5QigJg57owXM6Ta1ZvCpmry3O4c1IWMwxO0XmcOvZMy9pWwjGaMeE5_q1_ojZZ2mFS-if6vlpg7DazDDyTWhHujA3NNCPAVx0mpxEUM1EyOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 349K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=oG_dbmZ5BCtpFRP9Zgd4BHDxNVxJU65qszGm_d2DUczZMb5hE4Pr1hcEu5W0dSiX_9pmJGIQs4_jnA6sMpiS_bJVxfeilEnkqk42EbE38NWzuSULIn_aDcGEx3Oet2-YR2dqTit3jWDmmvWg_oNMeCKU1MV1inVwlk8LMgmAPIZpe_ZhWOSGYm5U0ooXEbTkO0tzzcOcxxsoryQ6vDk6MiIm1-T9Row_8Q23yC5Hqa-nwnE8UzfI1Wy10r8J_Pf6vfsQx5KqsUiZhl2K68OvzAkEQyMu776fYm5f75oGcvk28EvoUas4-3SGmEbeC72Iik7B0c3oeqLsLlNXAIOnRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=oG_dbmZ5BCtpFRP9Zgd4BHDxNVxJU65qszGm_d2DUczZMb5hE4Pr1hcEu5W0dSiX_9pmJGIQs4_jnA6sMpiS_bJVxfeilEnkqk42EbE38NWzuSULIn_aDcGEx3Oet2-YR2dqTit3jWDmmvWg_oNMeCKU1MV1inVwlk8LMgmAPIZpe_ZhWOSGYm5U0ooXEbTkO0tzzcOcxxsoryQ6vDk6MiIm1-T9Row_8Q23yC5Hqa-nwnE8UzfI1Wy10r8J_Pf6vfsQx5KqsUiZhl2K68OvzAkEQyMu776fYm5f75oGcvk28EvoUas4-3SGmEbeC72Iik7B0c3oeqLsLlNXAIOnRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwwkQAdIgZvGFTFueIHDL5OVof0RW8FqVwHTcNK28OKlENjfcSzGQckxGAGG_TXJ_tpGTq2dh8Vhj5UgOMByOURa1iOq0EWl2EpR3uBY7xloHe5cU4ikBZJJ-KtJ-pdLul9S5LaFltEcjFp1au3vrg8OGB1P-tqY_jER0ovGWhhQuIQntYyHs0kkEs4WefZjARveT0W28LHrqT9I8dEvUWy06QhpfDiq9T9fRHw8KJKnEj-oXjNuSqlohTDJAO2xoh-ERjA4xSIwcg3gaYwAUI6N2sIl2-Dc2_5M8YZPE-DcsQoCyqaO0KgymKDqMWrv4j7eGAstUqVu2iG2JmeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLctmbZcPXgOMPwZwCOu936wO_a1I-jLcq2_W6Oa8GMH9IiYEsP3nd2cJpAip9GWWAhLBP3DQENHVpH8-ANWBPzX4ayj8Gknc6yaYrqzrJHqo9sy_ZsoOinp-P1PI5atj6dj9gU1BljZtPIHpkxlSrGSBsKZdyxbcVp8MCWb4qXZQVKcxZKdGBZcXp50O0prTiz8HoYD7iLJ8ooAKl0UujUWHY2gj7-PUO3WWEelaiS-53sLI07yqR6U9_T2qY1CWsR8Ifs2CBpmbILf4nBKl8c5ow8haz3sfKpElbuD-spT9B3lAeRPaL1paf0GiI6cU-JVmzj9tg752gkiCuuTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=aWsOaYbZHnOfiEp5gQ5uhzEc7uGQ2Z7ai9XQfdw6-Ml_bSliaOWvSgMcyqc4pF6prkW14Blr0IdbpxaDWcRZBgqPxKcvV4GuP2Ltl2NOt-5SZ5CNKz1-srWtd3KM179k2YBs3LAkxR68j_8XUHAwKO6ETRhuhQUrxIEWHyH8w8LppiT32blFndxTRl5GbyYMs6A14_Z29h-DFf1Eer-9T3mevM4v-igsbfTjCthHusZ6M3e1Lm6EUcYkYyWHvS8fLuIAaCCkbWKOYhzMoZ47HM5A1HfR_6r3X59JzdkiunF3nLyW0aG-3tbvGWWAGmGBanPHM44z9C6Z_h38cJBykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=aWsOaYbZHnOfiEp5gQ5uhzEc7uGQ2Z7ai9XQfdw6-Ml_bSliaOWvSgMcyqc4pF6prkW14Blr0IdbpxaDWcRZBgqPxKcvV4GuP2Ltl2NOt-5SZ5CNKz1-srWtd3KM179k2YBs3LAkxR68j_8XUHAwKO6ETRhuhQUrxIEWHyH8w8LppiT32blFndxTRl5GbyYMs6A14_Z29h-DFf1Eer-9T3mevM4v-igsbfTjCthHusZ6M3e1Lm6EUcYkYyWHvS8fLuIAaCCkbWKOYhzMoZ47HM5A1HfR_6r3X59JzdkiunF3nLyW0aG-3tbvGWWAGmGBanPHM44z9C6Z_h38cJBykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=TcQckrfInqfYtUnbegfOOD_3C227n5vbpVGvHtDdlU81yxzDTZTcoF95laMfw-iRFG9GSWkmVPziskbQcVfbA9NOpjDmEpcBl97uRUKeQ5YF8jAoCOGUEKVv7P_z6oSi6E5DuyYy0MGkpdg_RuHv-vyXD-jL89pqQ7EO3kRtZOPJCavbh6yqTOcRT3T9HmTHl0HftbSGI5Jy8QDo518yAFP7AwusJ27-YoA2iywMuRJTT-3fBXXhzm7ze1h6gwk68s3gVFJVvkC9LnWYI9Bia0KKsEtrmVeqPixHwtYxpK9STJNDxLiTJKc9E-c0Gh8CIeJkDDkgao1ZOvso7AuNKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=TcQckrfInqfYtUnbegfOOD_3C227n5vbpVGvHtDdlU81yxzDTZTcoF95laMfw-iRFG9GSWkmVPziskbQcVfbA9NOpjDmEpcBl97uRUKeQ5YF8jAoCOGUEKVv7P_z6oSi6E5DuyYy0MGkpdg_RuHv-vyXD-jL89pqQ7EO3kRtZOPJCavbh6yqTOcRT3T9HmTHl0HftbSGI5Jy8QDo518yAFP7AwusJ27-YoA2iywMuRJTT-3fBXXhzm7ze1h6gwk68s3gVFJVvkC9LnWYI9Bia0KKsEtrmVeqPixHwtYxpK9STJNDxLiTJKc9E-c0Gh8CIeJkDDkgao1ZOvso7AuNKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=ScSRxj_14JOIYweuppOrbj5bTxnIDKqXA4aKo2b3dvLPOWc_sTGdBppkbedEWXjVp3Bw6pNyuObsUqnz4Wn1y5ocQuTIQkXLFG2cLJ62Aw1gffRwhQ7ntvLypPOouWP_ic8rWyTDSltVFb1ag5iRoobGHcvylq57pmgaxTnhDdoaCWb502RUJRzjGBEvqUlyii6OxdV9Lgq3aMv-Wj7Ef6rEMsJ0YdmZU6Pq1J2GPikhKDRm9wOpcMm0Fm7sSguC61hGCvy7GhNs6TSL0kKmXgM60_KEu-Ybwa7ETVE5oKtdrU3A5_JsTpDF-wiUdgcvzUdjM7n9hUZ0r6MI89MMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=ScSRxj_14JOIYweuppOrbj5bTxnIDKqXA4aKo2b3dvLPOWc_sTGdBppkbedEWXjVp3Bw6pNyuObsUqnz4Wn1y5ocQuTIQkXLFG2cLJ62Aw1gffRwhQ7ntvLypPOouWP_ic8rWyTDSltVFb1ag5iRoobGHcvylq57pmgaxTnhDdoaCWb502RUJRzjGBEvqUlyii6OxdV9Lgq3aMv-Wj7Ef6rEMsJ0YdmZU6Pq1J2GPikhKDRm9wOpcMm0Fm7sSguC61hGCvy7GhNs6TSL0kKmXgM60_KEu-Ybwa7ETVE5oKtdrU3A5_JsTpDF-wiUdgcvzUdjM7n9hUZ0r6MI89MMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8lWTqogkqLu0r2VanN-ORu4E_L_NMxlLFR_Tj9U5UeZqM89VoWi-K-eiuI8I_Fpvp_bQOIRX2TOzjmOGSpzDbjD_mVeFbHuIKaM8a4bXEuEtmM-O5JeGdwjtmXD3SE1Z_ioU4Fi3Cx08Wf5B0uxf9LpuclOBqKEAz7rVm_1FHK4c4Vgt3QB6TxMs23a2_VdAFGnw0XeFqnK7ovtdOdNwDGlffyK9ui-tZprkAYP-t1zqRMZRqOMdLlRi9xC_tmsbrI_7BNdhQP44MGLuj4NBycU-0vP1DynmmYXLaKBA5EvaQi9vwyOApbyGqsP64seDgi2XuXwi46S-z4hJupYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2r1B3qBMTFPK8dLqAs9j_Cv2BqT2tQFrIklw6YWI3qg5yUOudW83tykOCl0b9AMcUB-pxrHZUnN_I-TKh-zY4LhF0wAGY4qvgEsXieDkj4eVXNK7yoeeunJEW1LZJFOrsvTkH_yJd04UxiSZCPezRCACjzzewZJmyUkVgxkT3Kkys6W-u4sv_NV4VlCJu6Et9zqluFtQ4_bcWph02PUbI-UQ89V8BgL7r6BwB1xbXKBPyVpICugUpazUEcpeeEdZ25ndlu1AZjciygKKWoh7w773cLYuXaV1UR_pu-j7GNt8TPlw6LZ-Ng70xpPx_c9GjW5R2UJb90IgIJ1x8wYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkNtH2MxzhjXL7ZeJy_1GRbA1R0vBb2kwWzzTUyiBDuMmMBgcKYsXhlzsbifbHTOj7c4pYN-K533MQQXkM05IxIrmlWRXGNAGghHGMzwF-BZJmf_7ufRgY2mv2IdskSuLH2e6a3-ADwlH90o5eWMG5ODl7Jci37qiojSPxAvLgrtRQFPjNfsfVlIMS2x8SUhgzenNezKUy8VkK9ihAmTdaS74HcWGQ2Q786GmdWtmX1Gf7efBxkB_dNyg0Amr6LbFNstZTP2OrNCgKHORxkZOl9HQPsWV2-bS_vfo6sB5yzdJPKOZq2-x-0dOzC8MNhY85h_25nBSIZrbQAHKsNzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از هر واریز
🤩
🤩
درصد شارژ اضافه خالص هدیه بگیر بدون قیدو شرط!
😮
تنها سایتی که
به ازای هر 1,000,000 تومان واریزبهتون1,200,000تومان شارژ میده
اینجاس
👈
این یک هدیه کاملا نقدی است!
✔️
هرچی شارژ کنی
0️⃣
2️⃣
🔤
موجودی خالص میگیری
👇
🔴
اگر هم باخت بدی همون لحظه
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان r9
@betinjabet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/24664" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/airvqIQVxoBDLrSni_lVCpp6_19ZKs_p2ztXcLauzY0j3uSyABn49_-mGESU99RmpzQJP8iBDd87-Oho62NiKj7MfXjAm8VG6d8ancgH4cVY6AhkNgd7qp47vk5r5bn6USbTVHTaKoPHQzMkN4XHkGYqIVHfg14rFI2XEkeoFtvxzBhA2FtRwaMsk17CotnoPxnvHEYztx0dnTGFvQW80-p1B8Fy_SZ2-AL-77yciRryB1yi1GCouYH4alJHgqJFDp5UCf4HfcWRQ-zDDB2TYjwNq4oDvFbHs2o4G66Nhrf7AKbGuMxQj8xRNVFCB-iNGgGmaQri9fHs8bE6BGnfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=quURlYGZXfx-riwm3hzGbW-XiO36iqTMqFCbGROMIrsu4EFSuEqU8QLoN8wIwm38_feo25el1f43bfCoAcfP2Jb_oNGZoGaZeDXjg5uedZfJXyQN5FySHgwbajwjRAhRpAsRJKZH_eM_wwqX3EYV65y7Nw5H2L9ZnEGsT3NymC8Az2ruW6JfKiZdEEm-OPVRIxfkWWboj5xNm_NEmWqy1HkaEaCk3FfQXSFiIms32tbouMGreiZciZamPNbJD3IKPuwuZmmuC4cCOFyNLjL2zL04HsDk4kVyF1R8bPamvwZhnI1VQ4XoCLBuTOg4l8Al6HZmGQvZsR9p1CiE_m0asg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=quURlYGZXfx-riwm3hzGbW-XiO36iqTMqFCbGROMIrsu4EFSuEqU8QLoN8wIwm38_feo25el1f43bfCoAcfP2Jb_oNGZoGaZeDXjg5uedZfJXyQN5FySHgwbajwjRAhRpAsRJKZH_eM_wwqX3EYV65y7Nw5H2L9ZnEGsT3NymC8Az2ruW6JfKiZdEEm-OPVRIxfkWWboj5xNm_NEmWqy1HkaEaCk3FfQXSFiIms32tbouMGreiZciZamPNbJD3IKPuwuZmmuC4cCOFyNLjL2zL04HsDk4kVyF1R8bPamvwZhnI1VQ4XoCLBuTOg4l8Al6HZmGQvZsR9p1CiE_m0asg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Uf0xiSpGiLDTVG2kp_FQRqspEMSzmZieT4dOGJQZdqwAqtSKXx0NLscPEAwgKiQHAQpT-BPgHumg5cCG5Hxi8YoEhrK0vmr8spr-yKSKFhBQ6ETyeBNJCyaTOCSUpj44cu8OZhwVxpS7GU1mUOUvtPdc-NYpyZjuxqNnn_q-caBBqcX77Q7LFZq_N8kBVCfYmzo_R86iigJIAWj4sIYWE114iPVCqJqv6Wdp98dPh_qfyO2O-J5S6eHUXcLVr79VFPXLFGVaGpG8UbSAM23KLPDSs0QE0iLA5AaAgI289Cbn762fbYaKFsv4nXGGQD8FJk_13iPIPWBGO0qNV7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8sp1iX0ftyqojAa7_cnR0d8U350fCP-z-DLIQZTeyo-ynMjHnftlv3h0D2SzwiEsojxoIzQu5sFR5ZugkrxVar3x_kxs86kDXGGODxjsJlr9wQjzXPDA8lqTx_20NP38-qahoZH0eUHd9wsCnTgs3ab6Zc40mdqTeU8PEJDdnbIN4Ljg2ULIdKeX8ftJXvbUAVrpu0eZWF09NUoX9tAT6ewsgvI3eXj202A-jGgyy8ZgViayLc4g2SEQEENsUt5VVNg87xsO10OdkEOQGc-wt1BZdE4-ILVyxiKQbcbHfBWysZDAe1Sh7C0zlddu1fnkkj2gbpi6x4TcwYiISj8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMwDJQA1lFhNa8nYd-GzfXduI2RB-X_q0oKP1lhlFQfQArfYsgvRBR-TiY489BH_ASysGsojYKdOsRayCeZ4vImWo1mxN4t9XZ0ojd5ZhEXdhKsBSHSLeTcL88UsmtnhU-WtzKhcFAaqoW604mBjUj9tAcWb2hBVp_jYpdWiHU8yXThE8NqTaj30f_4dRmZQzzg4W1XCFOp1VulqMppk9OKyUOpJ3DJllDbIQn-Mr9BG9-_13A2La73eTZ25_kLVNSqihqSPIGk0MdgX8LWKn-Uinu7ch674omMOiJ45cDCLPW24PdCunO7C50GuOKlJ67iCeEs-4cm7HV-xzn2dMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80AHv8d98DwgNlZv9a1nKrgUi-QLOxiC6dFhdOb43ulZTxnsXrk0-ofxoRQgCLpXvH8jvmT62sxt8_IuwZtwX6xsex42D0rO98Wa7eJR-3U-bwFZjsA-ys_hwffp3IlkHzghGbB6DSaiS-KZz5_frDtQQrkMKFJn1v79ckRus8MSPxuNRCisY8nLHRiN69cOFwiQyGwzBLDDq7ihLzmvSt5_hXHwOeDROIKgAAxFCSY-CwN8DIY_hdASC3OfHqV92a-iPsaqxQASHq_-w8s0NX25F2nQT0bTeYG8Z0v756wtgmIQhFeRphjvbHCZ-HvmkpXY4Ur925GSmxL9qTLvb3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80AHv8d98DwgNlZv9a1nKrgUi-QLOxiC6dFhdOb43ulZTxnsXrk0-ofxoRQgCLpXvH8jvmT62sxt8_IuwZtwX6xsex42D0rO98Wa7eJR-3U-bwFZjsA-ys_hwffp3IlkHzghGbB6DSaiS-KZz5_frDtQQrkMKFJn1v79ckRus8MSPxuNRCisY8nLHRiN69cOFwiQyGwzBLDDq7ihLzmvSt5_hXHwOeDROIKgAAxFCSY-CwN8DIY_hdASC3OfHqV92a-iPsaqxQASHq_-w8s0NX25F2nQT0bTeYG8Z0v756wtgmIQhFeRphjvbHCZ-HvmkpXY4Ur925GSmxL9qTLvb3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=Q3OVpk2RLHuebs59eZqewQL03-8-bi9GZH_jY6e2jpNnYC5DVO-Q23K96wOjmJ-PCmJWxN1M4Xr6xzYvQ7LBxllWoIcQdqSOBglsq7e1F3AXRubA1YBPa6xw3aku9W2GyNrrXIdJIlJMqf3rgDD_9ahmw8btdUKte1wSO2skED_35nZuMaP-_mUGAiShq-arpkrmKdQQeG5MEZF-7K_9zutPpNw2l809GSD9ImW9dK1cQ-omB4RDKj195vgiUXI4vMRsP36xPB-SMmZivK0XbryBoErJst-0Y_a6M6EO1cBn5QxDuhj9iGzQ7_2wBhC8ycOVpBn_L0bZrOZ8yldbyJnn8qJRy180qRiiZ5PzYGvoIsxJAJjN054x8HAM1ov6eTRl3mF25SeOG8gGtJEfW6zoSqbKycv-aToQUiCDyw7BVE1vfEAKDhw5OCm7tqjQ_ShpOK5o3fJpO20fuYbb2TGTb3XjG_Sl-Er1HfTwTJrqkfH9uN3Qrg2BhEIyZz_yueXFlGjNF2i_H8lYpkW6uMhdic1hDK10E3va1JuUMO9B6VU-ENT51k_vOj8Woh4J04rKadM1C-WC8gHAV6ricaC34kB-rRcue51D131Msh_Jx-QlC0k8YJghh317D3Djc7JrE5h-3BJ-nDlVeIDh4MD_izG7_i-w1Fs6kLu9-18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=Q3OVpk2RLHuebs59eZqewQL03-8-bi9GZH_jY6e2jpNnYC5DVO-Q23K96wOjmJ-PCmJWxN1M4Xr6xzYvQ7LBxllWoIcQdqSOBglsq7e1F3AXRubA1YBPa6xw3aku9W2GyNrrXIdJIlJMqf3rgDD_9ahmw8btdUKte1wSO2skED_35nZuMaP-_mUGAiShq-arpkrmKdQQeG5MEZF-7K_9zutPpNw2l809GSD9ImW9dK1cQ-omB4RDKj195vgiUXI4vMRsP36xPB-SMmZivK0XbryBoErJst-0Y_a6M6EO1cBn5QxDuhj9iGzQ7_2wBhC8ycOVpBn_L0bZrOZ8yldbyJnn8qJRy180qRiiZ5PzYGvoIsxJAJjN054x8HAM1ov6eTRl3mF25SeOG8gGtJEfW6zoSqbKycv-aToQUiCDyw7BVE1vfEAKDhw5OCm7tqjQ_ShpOK5o3fJpO20fuYbb2TGTb3XjG_Sl-Er1HfTwTJrqkfH9uN3Qrg2BhEIyZz_yueXFlGjNF2i_H8lYpkW6uMhdic1hDK10E3va1JuUMO9B6VU-ENT51k_vOj8Woh4J04rKadM1C-WC8gHAV6ricaC34kB-rRcue51D131Msh_Jx-QlC0k8YJghh317D3Djc7JrE5h-3BJ-nDlVeIDh4MD_izG7_i-w1Fs6kLu9-18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMrruJ3y8tnDhHhK1LmgIVokqaulelkQWE101QhQRYCR0p_ak8ULgPr94HHHnjMWY5OiaqwrsZ4eRxOYE0Z3E6JQHNIgoKSexDrPHMYhhSMYhsl98b2eoBft3iX44MqX9TFJVvYHQFJI2Ky8c_jcfhn2pyuLSDfLAE07_T5qh7RZz-tDKlKX8sLhM91e_h35Ql8s-T-PfO4RCwP6gBRyEGi4E185WynbGy_Hs8h6BQ6edvXQ0jp5BQ4jJjoZDQAxrjXiVGgQm97SCOPLp5BL39EFyJz5Z1pRf2_exXNVdU_yp6rVsTp_kfe-kiAXmiXvTDJk9JECv1a5QMf3x2uw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=ri0Xe9GWRnpYgkw0ZnEUzUZoS8AP2b4BRSyH__99AbAllduUvsXWfjwAZ8KYvMMn124qsaIWnQuz45CyD3OCDkRK2kINx2ksYYw95ibJJDQynfgqxtTqHf09zqPvkjv0z4Lca9IMahd1EajKxJh_hBccQagvAUXbpoajgB6iEHRbo_RAoKyhO7L3m9ihaJgrpro4FOdfFPo_XYV4j6JcBLKg4um6bmwAA0VG7XeTS_SSS39TDIt3HnqO6Mg3QDdUfLBQn1e9nfDNVImHS9bxDjHMgsJtFNhz39wiGViILQpr_xzj7jeC8ooBLKtvm3J6ZRjk-3SHYbJCy6aB9CqkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=ri0Xe9GWRnpYgkw0ZnEUzUZoS8AP2b4BRSyH__99AbAllduUvsXWfjwAZ8KYvMMn124qsaIWnQuz45CyD3OCDkRK2kINx2ksYYw95ibJJDQynfgqxtTqHf09zqPvkjv0z4Lca9IMahd1EajKxJh_hBccQagvAUXbpoajgB6iEHRbo_RAoKyhO7L3m9ihaJgrpro4FOdfFPo_XYV4j6JcBLKg4um6bmwAA0VG7XeTS_SSS39TDIt3HnqO6Mg3QDdUfLBQn1e9nfDNVImHS9bxDjHMgsJtFNhz39wiGViILQpr_xzj7jeC8ooBLKtvm3J6ZRjk-3SHYbJCy6aB9CqkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g17cI34tjTAAtNg6LEtO3QZLEZdXBQmrfu_DeAnNIYqdppPtACzEZqE--ITpzBchh9hSLwVu7UD_Q1989U_QVLYP0fi3GQDl8WaccJUS0ajZC3ew-J03FppwNNhlzvibaYeOpaD1BdY2YxHQljHSvdgJ1DDl7i58C5VgwwtlZAjXymSCAYABa7Th55aD9Y5TTQpDMs8OfNcx8rsq8z-TVpB2ECTSQSjT-4fl0wgvjfVKraBsuvNIUqCafOvTldLEiXByE-OfzNNC-1mlKOyMzj4iAOiqicRVhlcU_flQDeyqNQlnYhbyQQfSQXM4uyLAnjijcpdlVegvt_iHfw0rCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8hUeG7o9cR16ZJkJzoEhMYim1wKCX1bwEujsSN1t9RAxnK4Ixi4ARlGq1hHehZF8hibSinz_XNZ9y-3DHVPjmErX0tYGkPHjtSEvNnR9uIYU1ob0LMxnbemW3BD47XvhjQX6c2jIU2TjPh7wlN6Yco-fE_aJGGhjliwLIK8szJxhLZVhuji_iMjp82xVmygsk4xWBl-CE5p5ppdQ2gQtvMvgbLrLKw3Qo1DaaFQ5J7VCn3360bf3kvXNrok-qrHLRFoo0RjzZxABieG35kdK5nD2c_FJFACyJGCBRI2Zdd7DQcMZl4xy0mR_AEQDrdpNdenPQLmJVOuBF3fq9Cu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=dvvyFxE_M7QZTzcdHX1Ppv73J3mo3Oxg0kLRg9MiFd7n7EgdXmuDqHPU5dyFHk_fTOzZZeEgZeQFfTZvJFxw8IFF9p96NrC9Yj3iUhQj_FppiD8UWN_zkEHm034cXm_8QlYk5qynZ2Iq4Tr8t_b3pnhtQXlDrM2a9f_eJ17jYIsKUkuBwABSQbmqd4Wp_lwJpV0ud8TIkKC-26BFw8ciVUWuxJo8Hs__gbgOE5_EozPW0OhNR1Pq3LprfLhlkRs6kiKq5SjIsuki8ZEIiAUuI6LAWzKphNLsgFtAdSM1MyKLdIIcRQxB9MTrJyTYxoHDerSrdfLLHhQH2Awpcfa6YaZ5cxuTK4mWJOJLwWkyWPxXh0EiidZ0bqApIgrCwXbqC0lWG8TefP8AlExGQWtkDwCV8XKnRvQrT7PuDvpnHMVfadfo2u4VyN5cHNPI-gVpP4eYKbJ4Ium-JhX3UwsDNLsK5mzwWicrqcvp10b8QxNFvh4VpYRmZxdDA3-SoJpoqN-hILGzq8LsTcUN4W4kavN0pryvY1tJNyOpmQeOSPN6TTMuWkCjaKiID13dgM1xIpsKz8pl--QHg3vz2-yGPHV6L9GhWWWLI7pYswFaG76xp1Gwx9s7i7tSYzB8LmhIdRRB-gKsqOyADxmtt5Dx04oFr0pyS_EUbFu6sWWSc5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=dvvyFxE_M7QZTzcdHX1Ppv73J3mo3Oxg0kLRg9MiFd7n7EgdXmuDqHPU5dyFHk_fTOzZZeEgZeQFfTZvJFxw8IFF9p96NrC9Yj3iUhQj_FppiD8UWN_zkEHm034cXm_8QlYk5qynZ2Iq4Tr8t_b3pnhtQXlDrM2a9f_eJ17jYIsKUkuBwABSQbmqd4Wp_lwJpV0ud8TIkKC-26BFw8ciVUWuxJo8Hs__gbgOE5_EozPW0OhNR1Pq3LprfLhlkRs6kiKq5SjIsuki8ZEIiAUuI6LAWzKphNLsgFtAdSM1MyKLdIIcRQxB9MTrJyTYxoHDerSrdfLLHhQH2Awpcfa6YaZ5cxuTK4mWJOJLwWkyWPxXh0EiidZ0bqApIgrCwXbqC0lWG8TefP8AlExGQWtkDwCV8XKnRvQrT7PuDvpnHMVfadfo2u4VyN5cHNPI-gVpP4eYKbJ4Ium-JhX3UwsDNLsK5mzwWicrqcvp10b8QxNFvh4VpYRmZxdDA3-SoJpoqN-hILGzq8LsTcUN4W4kavN0pryvY1tJNyOpmQeOSPN6TTMuWkCjaKiID13dgM1xIpsKz8pl--QHg3vz2-yGPHV6L9GhWWWLI7pYswFaG76xp1Gwx9s7i7tSYzB8LmhIdRRB-gKsqOyADxmtt5Dx04oFr0pyS_EUbFu6sWWSc5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=hKG58Mr86YnvS1H6GE1ScnuYpFsXTrenDhbgANjiItpc4ipLLpW_m1DPzkHI8gV9p21RwY7rm_1yXSIAYEXDE3BvjIopO-DlyZiAtoNtsy-y5aOHt4HdG9R04MyUPCu4gg677vC0jX8UQF7vtiyYBrY6LnGs179bYrNQ-FJ-v-fQRH60cxSLJ4uvBnSp4YTEuGgBvPhKO3P81hzjarBsvx9iw7ZHH1aX0DGjdFDGUfTSJ15ly0XfVLu46d63izr-XBQxXUhtCIPVDlnvHciFq6H3Dd6BPiE0IPko9QD8SgwwA03qXO2Kh75zv2AgNZdAAgovxaqYEISpYfvSacNZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=hKG58Mr86YnvS1H6GE1ScnuYpFsXTrenDhbgANjiItpc4ipLLpW_m1DPzkHI8gV9p21RwY7rm_1yXSIAYEXDE3BvjIopO-DlyZiAtoNtsy-y5aOHt4HdG9R04MyUPCu4gg677vC0jX8UQF7vtiyYBrY6LnGs179bYrNQ-FJ-v-fQRH60cxSLJ4uvBnSp4YTEuGgBvPhKO3P81hzjarBsvx9iw7ZHH1aX0DGjdFDGUfTSJ15ly0XfVLu46d63izr-XBQxXUhtCIPVDlnvHciFq6H3Dd6BPiE0IPko9QD8SgwwA03qXO2Kh75zv2AgNZdAAgovxaqYEISpYfvSacNZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPs1JN0qaX-MQKvw7-hDcrrHgYh3C3jONr9Rvy6hE0tPFRYu51T83sm-kFHcURrYBPnh3-hMxMVDZ4VFHLs1N887jrxSTsTzx0lvXWYB_7WaA3rE555OnmAMtbi5mxdiD0YKm9wPoBjSvhYr-68Z9vJ35VLEqUgU3EMqJpKBuT5d8k62XR7IqaYCbXWk9_VewZoY3CZdLcSooHsHiZHjng8tO44YkPqj-9D6F0aCm6wUB4Mjq-nla88EyaNlFDMI5wZZDWI_T2vSbZtnlFLaoZc1mB8NxTQRROG3UXid93QZu5wn-HCWXQFuVj1xWPj4Uxq0GrJzagKZiPqC7-KpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9VbT3OyjN_i0sgTlvOwrGxzZptPQKYbVGeD5HAIA7qxz7YCMC7qmreLCLF0HcclJo9mERSWzq5C_uH86tys4Hcrze2xZL8Oiqh9IacpSZRDmr0YawAucqydxF4PBnxYjw11uf8nS1TyQWobBraCBtmclTo9uvdzQo7WXPwhhjoeMJGGR4frWWdBfLYKq56-LAWOBxkfuiTe065QlXB0n0Bf8j_Xaei_scUohdP8wbxsvOIgl_V1vJ01s0Xy5fhDfexz4qXwbVTvzsmv2fQ_-RX8k6Xd--zoY1FmlIwrg7KUrY9c70uUDER2vUYbL8anysXsqTdSY0NxqwEG8mk1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqyJ2rBybwy1hA8rnDgZtQs9qNeU_DQ1cTTy5q8fbThMdr32sp3Kfiax68noXFujRdcLZniDQlKOmFd72G2-qelgKd2n7BzzBp77CI_rVlFoF6rcvHd59GNi9L74K4ezul_nKcOVZ8kn4RGCCL7qd58mNF2PkACmQbFUTayso99DcBRDhvlOBPnKVrgnIbXPH-1_18QCkwYG5OkZnOI1a8Rtms4JvHjt2dYpKd42t6myb9gKs5R0zaWjrkvIN6rbElehdRRW7gsgPqBIHK1e-iNXxDZAY4AxBGVLc3KFsoxeFZjC4osYYaE0NT-h43qcBKHq3tbk8zHO6Wc7ZDxdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZTJHf3YJkcbPNJj8VNaNMctii0tWwpBpdPV2RoZl25f4iUOCVkS7fzsMPr4pjAyhLSY9n6AKPyNXAUXM4mXb26wQf5AEw3ED7IBrugfYuBTMTrb3WovFhFJnNFxpIASYAa0U-3XRvu0QkMQJyU2GRKI3VAZFLA9dlhyAIlEXpqx4R1WFoYckH8XZD-wDwQuoSF7aNrGOnPcM0QztDEBgymjL-_iiG4sx8Xvnj7exuiqQRm19Bc-DrzP0szlNf4u-EUBditheBt_KLHiV9Q_uWDL1k_wrFOt51ho1gDfJaoJJk-sJcBeiCEHLOOlf8SjUXZWra9YMfvOUaejamnqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiPuovwBs9z-HA070srYFWxp5lSUdfTBTwZY2qi43EptBxtElBtpwRsEKbqFVzB1VUWcfUJqZoTOm5SGqbMR4_o_ivgaqqJ9QjQT7xYuIj6h5jgFZOLoEg77PsctDSV2RkdxQjyixojDTs9RKNp4-CilbMF3me7zHo1N_gg5_IgHlGUsqIWiVMt2VTfCVg_Auz3tHWnVvAKqJs1fLokqtw2ZVTJ_AYpAaF15EgM1gJ8_hBKt_vgrj5STx3svnfAuDKbH-B9KoUZJWLzmaisR0vnPvK1aZnngu5DTKUw26VrdDrKywvaERalFAD798oU5oTrVPEaRDKWPyWbIW3fHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=WFJcEAkASdHLOg4xiEqsFS49569kI6Z-fM7xNmPWDPGfrirs_lEzNlDv1gqMaHEwC4-rG77d4KrjdIYKOERhFfHA-ASqWpGR95puDfNl8QBY_KcUlzLqeoYJK_TycyrQLW-OhiKdotPqFKSTcxINfkagklaI3a7KM6HZVDIgmaTJoBVaWh-3jLMRXRbjhDaAqNbRTzdMOOwhEO9--sHI7kfEOxsBV_9v90Byh60ukxIeVJxlIRztA8fNWjngmcHFAOetBDeK8mphZIApgxdkWsT1A0TFagouEj9XahzgBA3l1Q_RqoQ1LI7BL18tMXFmkcfrbsHC-5Us5qAiq0biaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=WFJcEAkASdHLOg4xiEqsFS49569kI6Z-fM7xNmPWDPGfrirs_lEzNlDv1gqMaHEwC4-rG77d4KrjdIYKOERhFfHA-ASqWpGR95puDfNl8QBY_KcUlzLqeoYJK_TycyrQLW-OhiKdotPqFKSTcxINfkagklaI3a7KM6HZVDIgmaTJoBVaWh-3jLMRXRbjhDaAqNbRTzdMOOwhEO9--sHI7kfEOxsBV_9v90Byh60ukxIeVJxlIRztA8fNWjngmcHFAOetBDeK8mphZIApgxdkWsT1A0TFagouEj9XahzgBA3l1Q_RqoQ1LI7BL18tMXFmkcfrbsHC-5Us5qAiq0biaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um_EYNwUm38PC0QWuTmFPlpQ6uj4ooSqIr_FLugmDL47OHYTLyymdLogaLRDad14JTMIcynChhsDRuSTlRYlPwSysaTHAivEneJqv1QAjgTpfFL5xF2FCRsTHEVHCG8FKfi-pLkftG7_o4N7FcyomYFE1bACAfF7w-vQs_qADFAPv1zn0EvnZbQevjVrYTTpyV3ayahLH5cOWTC1j14q4oiHK96E5LiF7aXzX_f8GLNJTX8gVci6G6eAg9dfy1jznAZ3gLAm8IiydLZKHnfBO6dS9SFYxPSHs-0NcOvqyCBGRkj_ogh9TRjAfcUmC8STLTwRxU01unlwOPIVDATcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls_1P_wySArlWWGht1jsb7lYY58QnwWEsuYyQg2tFmrh17T87puLJmhzZc2BQ_KeqlCbnwn0B-fGQReV0tIxJEaOGObR7Atg9BrUNIuLVAFwcTjAhm8ODo8jkPErIhWjRfyqscVFHXZtXKD9rxz4_gKSQ6Bx6fT9wSHbXSDKgQOfBxloGc2V4wSaJEBmSctD7Ms4jvf3uzVa05OmDGg2hSkD-OAL9632U4eqlK9kFxUjus6B24qwkqK6GPwhkw_xJSpvHKXbmXVjeZw5gG2RKpp06vbtS3ydpo7x55mBDa8u0i6DAuwHlwJOGLeGPDYZRujcH9KdVJ9pO3i3nG7OJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyPuY08FLuTSz07guzy1A6k32JtDUcCH83DUUmigmjiGaKeFtoCEA7P4kuutSSPQsgpueTHz2RRPFljZVOfiagA0GCW89TyHDl8iEBakHbkit5FNqy2I0ILeNXXUCJKqa7159yjgaBUmMB_PBYTq9Ftfz6wqTh6IP1I6fPEhN9_Ylr2mQMexa4F-UceJSoJUjS6JGQusd1B5tRLmtQibCBqrjeKSMZlsSA9cXMok0nAIS9WOcYsr3f4xlkAochJ5bsxdoF3rxlhkDXzTzDVoL4j9pwpReFVTCBWBSutCrAIEFROnENv2xhs074EC1qwd_qZWhpiIUQwkT6f7QqG56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK8h2PYEHCb16ee2k2p08lBTCU_petDL1Jj_mn_m7HSzigVrHWOCGb8BMkHCs-bo5IeBodEfQh9YBP4GjUCHVN4g74P_Rb6Egzle6HsdJxVkHDZgbLMDisyxJYppGRrh7bcRngnIpDbY4etDQ7vYOXx6ocsnwkj1cz_5tkVTWpVGeMtNCP2pZ_DzRzWYeU2r6n-YqMFEJkWr0lsVJJy3OVeMXlACtcMWXpU4M40wtzMi2DGQ7qUonaF0roI2vdPiV1oDeeDsHUSsoooSacd2FMQwensfO1YFNYqLkytxlNKMyzPHZwD9mwYE7OQNlNgRIOJ7LRmqwgLuqvIvfA5KeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQ3wb-YAXmMJ3gUv4RMYI4q4Q_dVdRd4biu-iglrk7KVvnsse7n52XlTH23ocHVFoYB7p8cBdpU7ULyuVkHTG4Blv8P3L81EX7wkL0CRUHi8xXJyuD7ivptutnmRLhFZLE3LaPoWWClkDTxzUrmnqVtR2B6_rwbzzSbpbIE6GBkotOevxlJhtKFvgLTYh8wgq5EcwJ9dAikheFvMiZT3pU314KIOMfRzUxZqt257IwfbI3e2WOGQYElquAQmi6RzzNnQWHUm65lnbpppy57L-8iAoiwonLECp7ZuSDJvYHNk74EMNbO_6ub7SebzcXF9NFzCfOT6oChTkON2nZAOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI3Fp2Rxu3o3bA64lNsYh7EzJxKsdSLc9GHwcD7Ln5xA_32k5VJlLI6OzsNG9sn7hDz76M343SqmHMU_U7ad0fUbVrvgUqLdBUMNu9D4Hh0xaEEX0U5agOL2yZBvmNjl3YLVUyKa42icAQcofU3TxGS5qgqanQQOqq5dGkJJGX3H1N9BncOiZFqAI5yXlVLOuDHnes1vyywNV9l1n-cpzq4xBVVnNugmMLcwjIbQtiinxFTrP6NcVpl56dADYPI_ahUgOW0t1BSQX4J37CQxIuLuSLQY0yr78ke6AaFCsKbz2gDJgT0s2D1IsOrxC5D8x4I3UnT9bOuDhmTILg9o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dghTiv3TrhOy2untZBkIS1Z9JBiCWcMVOUTXncSUquVjhab_--orWpTFqDeCSv-Oh5YIZgK-9HMs0mhv7bSlKmq1Di0oIrrjsz-oc8W0r-Kv7VIzC6WtAAhbD2ItxgY8VlUd-HI5Fx9Kd9ajCMvlq4czNVvLZONy0orpGKA0F2O7Qo3zuMdVxIJpSiKfHdzCBcGzzZHk-2x84Gtx_5uFAanTo3jGRH4gDCycnoM8NK3ZQ0wKGbq5Po2y7-bXxk15M2fJI30gyg_beauLiWupdN3xBm-nxdl0aSsrRunzC4AcI2yOe7ck06dyrelfFtZJ7jTT8mno1-gk7vk75v-5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=c3cdPw5wConsnqzU5fgA7aBXFI0HGJVTgdAqPZM2cFbsWDv2T4gItMBj4mvUbcGb9OmTNRNmc84K_r9YCZxiMQqDz1KCGzdM1U7yiIfJPrDQMPLXMK_3nJL9M3ENEL5N4ekOcgIhRxntyBTGLNMul6HCFKvLotsZbN75VwGurLXv9CMxPP118X8uRLZkFSRKLd4Skq0NnXxpeLJtvAMrZbeLfUezzY8n1JxM1YVqesMk27X_xu-H_fmjdHTMBm8Ii67hwM1ELM-0HAOCP1jzcxl802Z8oBR9dgh1Gf2afN3JmFp-rNHe-Uls0IrGJvWJgmOqQXtslTNJvb517olVrw3tat6R4rSr-apK3hGtDZc6SL6JSk72462RjqtntOshrM_DF5nCKC1ZMXiebWl352X0B71Am_KSMONBH8RLNJ0nkZZvSi-vfApSbZCC5Ijdn6EwdgVUEcttBv2mo3s9_A-9OfAcKC61JhdTqXLpTIcgHhjY7f5Pz7WJC113Fwey822CkTpOM9auSkPPJ_fQSrOzGDLVwKY0_4poTXpCYfXw0Jv5BqiQHmKzy55I3yfeKYcLGuFDCuHVoA-7Bri3Rq5pEGe92Y-2tUAJEAQ1kmu7Vd3rK2UBTw8DaYbGQmOmEnES1v_eNigy0krAKGF3wskMt5NHfoDXSyqjZKjgCDM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=c3cdPw5wConsnqzU5fgA7aBXFI0HGJVTgdAqPZM2cFbsWDv2T4gItMBj4mvUbcGb9OmTNRNmc84K_r9YCZxiMQqDz1KCGzdM1U7yiIfJPrDQMPLXMK_3nJL9M3ENEL5N4ekOcgIhRxntyBTGLNMul6HCFKvLotsZbN75VwGurLXv9CMxPP118X8uRLZkFSRKLd4Skq0NnXxpeLJtvAMrZbeLfUezzY8n1JxM1YVqesMk27X_xu-H_fmjdHTMBm8Ii67hwM1ELM-0HAOCP1jzcxl802Z8oBR9dgh1Gf2afN3JmFp-rNHe-Uls0IrGJvWJgmOqQXtslTNJvb517olVrw3tat6R4rSr-apK3hGtDZc6SL6JSk72462RjqtntOshrM_DF5nCKC1ZMXiebWl352X0B71Am_KSMONBH8RLNJ0nkZZvSi-vfApSbZCC5Ijdn6EwdgVUEcttBv2mo3s9_A-9OfAcKC61JhdTqXLpTIcgHhjY7f5Pz7WJC113Fwey822CkTpOM9auSkPPJ_fQSrOzGDLVwKY0_4poTXpCYfXw0Jv5BqiQHmKzy55I3yfeKYcLGuFDCuHVoA-7Bri3Rq5pEGe92Y-2tUAJEAQ1kmu7Vd3rK2UBTw8DaYbGQmOmEnES1v_eNigy0krAKGF3wskMt5NHfoDXSyqjZKjgCDM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC7mTdhH0AU5rHhkPEIPqn2QqfP29YB_ktgciJ1EoJiaYz5UGjJ-uUAjAYNmQUMt_R6OmrIFg8zeXFmje20F0kKvkFdjvCOKCiZNTtrVAR9lUddE4ZtFdUUYquZC1xPUrhcVvPlA7AOEfCFCejkcHEbo7yREFQSYFWPckfDhKVogeqymS1fVvEw7yXFV2icg4m6Md3vF0VudV_4kIZIdCE54FzAT9SLpdIuaGl5f2_uMVDYB_1SgC6E3Q561dPN_K75aRFY1-g4nZFVQgPO3kpWhMwhKBMe_pB_n6dBzcY8zO58kFc4QBxD8W0QyFDmZ0uURr5xjA8OtZ34Rujag6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=XgsZRJE5msk0Q98zBIykSM3n34KVZLIMHfOZb881zaMWt5aUkJopRir-xf8i_x2TIIUv68JzOT4kpOo-n4g3qOEqX7c1yxdVZGVIHtVWws4gfzGe_WDmpEjNwjqlAE5_aJbEyMaHRodMEnZwbD8wkr0uEjnvePncD5ySl4VY0sRuIjZH1oNdbvOu_pdD1C2j2ua6ONX1KgpLVC-rRINgauZcO2peaXDE0sncxsxbnchEhihUx6H9UA-O8eju7F8GDtrKED13psKhCNburUCgVa_OYS6QhO8WEH1dZ8ypUzXSPwgBDkzrRiiiSql8iCEOXZwWWKzNkMw8CQ4OM97J8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=XgsZRJE5msk0Q98zBIykSM3n34KVZLIMHfOZb881zaMWt5aUkJopRir-xf8i_x2TIIUv68JzOT4kpOo-n4g3qOEqX7c1yxdVZGVIHtVWws4gfzGe_WDmpEjNwjqlAE5_aJbEyMaHRodMEnZwbD8wkr0uEjnvePncD5ySl4VY0sRuIjZH1oNdbvOu_pdD1C2j2ua6ONX1KgpLVC-rRINgauZcO2peaXDE0sncxsxbnchEhihUx6H9UA-O8eju7F8GDtrKED13psKhCNburUCgVa_OYS6QhO8WEH1dZ8ypUzXSPwgBDkzrRiiiSql8iCEOXZwWWKzNkMw8CQ4OM97J8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=pr6zrfKbkIGfX1eAfImr-iN4d-6kwwPiu99lOC6bW-FwhpgcwPGgzpSikOfNDQYmw33CDW3KRjVGQIF51to1i2ZzFKZgHcdmYBESkPHhHASU1EWqZ37hJOOPcfjxoL8gMj2Y8xktusQ_pWXlJ5eGXghRxwVhy1JatYVcuT2NL5NRf1wlK9t10hAUlODNXqFBhCXuhcIp8tYY0TU2cmv0joXgmxFXaXt4q1-JYfawX6OBLgE3g4f6Ti-MoAu_rn0ehBqi4NbC5iuMUA_3fj_LmFdToQd0H--YO54fl91ih2YLIp2SemdHNl7ImywfX28T94MDR0SoYjZWdCj5pQ58wRU4cTHuGWD9w0HlQf1iea1qtNSZhVRdIXJ8kDhzxo6j9vdv-2IrkfobFIlsewkgoQc1gkqFJLSIaV8ISJIK78rM5TLysBy48oOaGOdHgG9UrQIxgIjfw3pTfUf9b-HRVJBaR07LbGr3jVHpNd7Ksr-e_PEkNkrPQt3Nyxw5BCr7Q_s8G6IMfXNwXc64VoUvU0enO0pYIopPk2ja7oaC4sY14BXV-g0q0PzpByfDyY1wu016ETr_l9zkBvb_ir24XVY_o8XzOKQr1xlmaotCT7PUuwlPK7cjeuMRQTE0l5ACQVllLJDmZ4-5cvqJvXXAoObKGHBEeP8a8HpoehRNJgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=pr6zrfKbkIGfX1eAfImr-iN4d-6kwwPiu99lOC6bW-FwhpgcwPGgzpSikOfNDQYmw33CDW3KRjVGQIF51to1i2ZzFKZgHcdmYBESkPHhHASU1EWqZ37hJOOPcfjxoL8gMj2Y8xktusQ_pWXlJ5eGXghRxwVhy1JatYVcuT2NL5NRf1wlK9t10hAUlODNXqFBhCXuhcIp8tYY0TU2cmv0joXgmxFXaXt4q1-JYfawX6OBLgE3g4f6Ti-MoAu_rn0ehBqi4NbC5iuMUA_3fj_LmFdToQd0H--YO54fl91ih2YLIp2SemdHNl7ImywfX28T94MDR0SoYjZWdCj5pQ58wRU4cTHuGWD9w0HlQf1iea1qtNSZhVRdIXJ8kDhzxo6j9vdv-2IrkfobFIlsewkgoQc1gkqFJLSIaV8ISJIK78rM5TLysBy48oOaGOdHgG9UrQIxgIjfw3pTfUf9b-HRVJBaR07LbGr3jVHpNd7Ksr-e_PEkNkrPQt3Nyxw5BCr7Q_s8G6IMfXNwXc64VoUvU0enO0pYIopPk2ja7oaC4sY14BXV-g0q0PzpByfDyY1wu016ETr_l9zkBvb_ir24XVY_o8XzOKQr1xlmaotCT7PUuwlPK7cjeuMRQTE0l5ACQVllLJDmZ4-5cvqJvXXAoObKGHBEeP8a8HpoehRNJgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7rhwPAlcVqKLgzNSp4S-ThdZGLHgYUZy5KHF-6og33p7xFS5xHFQ5oK17ZvS1aznbis6YTO8Pv-cAtnSNaWD1HE_kRm20NooJlDEiBhsBa28s4Eto9-Qhs35PVJEuVnC0nrEuoHPy6b_zphWpxw29-rL085uee6cSVfLoyznnCOXtXS81JDGt_0us1zYX0bHB-JvZjXQkePvlqLhDByPMpL7dT3pluiksey1i_ger2suwXXALbqK9mDm_NrRr91U7JMVc8DuHh7tA34TqT6LZHVHI-hwGaNBJP6XBQP06o5vF1COUpRwYJuyvq25NcqLFgWihwvj4wRmEAexQJc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=Nl_Pim_5yKN3778Ewuowo-oAJz45N5rbP4Inwa_ZnbsObQoUT7qZlI5T-4aN2wUlQAuXyQvmtlVV48sYdC_aC2ddu5NbdyUpgRflBHE0sapqwFFT02ZQ2ewoUxs_G1f19_YD06oAejcIBHJw9nWfHvjVK5NzGg9zIsZ0qWcINvent2-pFvWIShROfp3OtZyy4wrHvPjfcYNX0M6K7-8_HWLyFe6b8nBoW-7jxNl9pKK5yDT5dXoC_iRxjpYLXix23VagAUQPJKZ0Db408q8-FhSH4OS1YWveiZrCqDwLfCi2CaPciimRmnAd5iT_aKCkqMQQzP3zi5ZbKT45E20wtT5QVGRCH-sThtd_sXklTYHtGXqArdEfhy6k50GW2cNQuyzwyfaJlILcGVb_2USnlENp9TgQBd2lGUMM75l-3H1JHRBo4V6a-I6mMjZO3jP44gYazQCdSi-buRjfE6MQNaFL70OJK3he8RJ8hWdvgPDk-iDjZ6HYMG-b7ByzFGEnmr0CD8r4sWJmFxOHSoK6hmNhVwWG_0ibc_L5c7DjoxEludPN9sWHu71XLl4fql1UcbedqTJF1eew7Hvc9Huuely-Ys8b4z0NFVD2wi71uP5LEb8eTyfDgFcySziqUPYFeqdMw6rUhqnkNguit5LEJaVnLYq7H2vMPpZYlkGziyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=Nl_Pim_5yKN3778Ewuowo-oAJz45N5rbP4Inwa_ZnbsObQoUT7qZlI5T-4aN2wUlQAuXyQvmtlVV48sYdC_aC2ddu5NbdyUpgRflBHE0sapqwFFT02ZQ2ewoUxs_G1f19_YD06oAejcIBHJw9nWfHvjVK5NzGg9zIsZ0qWcINvent2-pFvWIShROfp3OtZyy4wrHvPjfcYNX0M6K7-8_HWLyFe6b8nBoW-7jxNl9pKK5yDT5dXoC_iRxjpYLXix23VagAUQPJKZ0Db408q8-FhSH4OS1YWveiZrCqDwLfCi2CaPciimRmnAd5iT_aKCkqMQQzP3zi5ZbKT45E20wtT5QVGRCH-sThtd_sXklTYHtGXqArdEfhy6k50GW2cNQuyzwyfaJlILcGVb_2USnlENp9TgQBd2lGUMM75l-3H1JHRBo4V6a-I6mMjZO3jP44gYazQCdSi-buRjfE6MQNaFL70OJK3he8RJ8hWdvgPDk-iDjZ6HYMG-b7ByzFGEnmr0CD8r4sWJmFxOHSoK6hmNhVwWG_0ibc_L5c7DjoxEludPN9sWHu71XLl4fql1UcbedqTJF1eew7Hvc9Huuely-Ys8b4z0NFVD2wi71uP5LEb8eTyfDgFcySziqUPYFeqdMw6rUhqnkNguit5LEJaVnLYq7H2vMPpZYlkGziyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e15USgUfgYsm6azmft2D7cwKxcWGBQzIIf-oved9plkD6Iq6XFOlMD4nu6SpuAnuA2N5IqRfnm5CfRRmtsHyQ3EFT4LhGdBk3l72IeL-BpyyvOLmCdRZFD1dyKgGEFS6voUMOkNDUcJMJiq6_wa43SAZ5Q1B-Yfc9OHt_KcQl4pVXJTWLL7yZ5xIRAfgoGxyWxEE_KxSKoZFIuq_iOKsFb4FLih7_AASMBW8sl7Um2BooLAhcF0dnkTguyJTXyy6DwhC81wfhZingBD7aoNVpURVT1qQyzq_TsJiRln3yEq70jwsBehlzkbKLl1T9sZzqHVVmYhJCP-_HOvP_C1c-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-M2nxEvJIYEIfq0FeHP9CVeg3SCsSYmEDvGtEeCymlP1nmBSGQ719QE85OPPqkl4ZHjOcnBBqf5INlP_syvJlTUSfENliJDDNPzUUXh3SceA0TYvdWt5QE6hkkODwWUF8dRe7-k4UWYXVg9lj_nR4W2fYAh-PNhCTu9BjpTxxU87mR9YYim8mO006w97Gs6EEpuR7uZeoU6ZLl9iO_czOGpAkU1o4rR0kLmSzq1ldnhr6uj93_KcaMdE12SUHqfl_c5b8i-_xaphJfvpYdVzHx6qK0OW26xZpCp9M2QEn9WSwnRrAlpCVnvwmZrM8B_-qgX0H04Hgqwe6-HZWue3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJnxSmhwOuRMnv0vmAmamafi1Hb1m2FqrZCzE0nkIIicGPVeNjyTb4U5tnakDxkF9xgnEaRcAj7yH7ehDHsRpgiR8BHPhPmN6IABBOwI1xr89hZOgVkMOvZRZjB50ND7fNWhdpGcGw00aeZUwMQLWNPzAGtL6EyZWQd-UIt--mm-piJKWPyQdnkSdL7AmMfYmU2dJ5NTZ1jA4eWMSGp6I-RPxpD_Zp-_3S8gaTZ5U72AJeVCS49hAQtkChVaLL1n8WcmGrcse303EZrgA4yaXqLzzZ6j4QC-8CeKckCJ_oPo1LXPqUwceYcctXI8o93EhoyJOr-HHQHwCROQ4faQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2nn_ALugPguKIWdfInFOyyPiu6Ku4nuxfFxz5Bl4OTIPNBDIRsl7sNNuLvPMJo9TQztDkVicqRXzvSABSE8b4KTYJ4Ir3GSpXsaf6NACee-LgekKVMJDA2G3DTyayIKEnbfGR0iofVaoxvQs1slOJLnHPDil_M57Mi7CvHSxdCju76C_hyqQ1BGeb-4Yq2FoW_Q0bbU6FFiic81K_sFDLS0DNfn9IZVA5iadQBbGUNnF8f8xl0Ksn_wiuO9o-yPIWM51uWFplSAurRIkwxeAPp27sjsx8SMoLOVtlQPuZKInoxZCZlt6uqf00_F1wiwNecCW2k6EUgGqMMA1fJUVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL4_63i0tu-71Tfdwc_FJlY-puV2O3xyPELoQTY795QNlROhTGVbepVg1gJgxA3hbeTZ3BPR05av9FOz56KHSnni25OF9An_eKOOwIOVxMq7CIivOsHV3XLBzHG_dtY59idDFu1SVTHdgmSK-sIyy7HUD3pDk-IcJ2TNn4TDK1SLldjZiUvs001893n0FwafiDsI3nnEvuRgS7ouQ1FnUPIRRjMI_iLtHsvE9kzPjx7xTmvdWdAVbdCusvh5gldX_ut5QdCnEnBPoe6FyhOwrvYETsBinScrfyDpbAP9zB86ZttRhC5muPLyMNkQdTHtrF6Mx1zrzTO6kb_I1_EBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI7IyU1Ing1O5TQSjD9BJuQ0cb7DircRo3IDomkV6nscKUoE4UctNPrJsFT4CeN_IqxVlZyh07R0jGN-H7IUwz44yJdEqcOI9wDiWmvbwxJf4vUHfUEuP1KZnPQzT1ppYBkAr5IAuNlzl_P_1ZyU7rmSstFXi5zX20KhLxzdiiRKqkOQ-ytg2iDrORhN6xb2BeB5rkpQMNh65D55huYWgjhVYU9d7wgTIP88z9wFRMD24YyXe3MMI_Ti--g6L7xvBSLQ4nY8Oy0xNDDLHC6RsjWJLF6hEyiqB0uQS9H0Ox4pYwhoDkdontRlhw79ULrrRzOc6stlIqPiGAY1FF6Qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoJb4CoNdbJTd4Xb9o7YfuBBKNRYHwuXiomL2rRCqnTtJkvsCPp-NUI1c-kC86o89posxecBhChjh5JRxqNGIgJUwpHEea2xv4MXsM0I0hDLwLr3ddnNiwx4ADGefqED-m4IL88vNKDqGFcIXSwL08aSsbDmna7DI0xSiYt5xfxl3MEpZzULq_dmtFIrWB44Kv03u9TCc-tkfgTjFnCkYONdMJGjD25h3ClHEb8lzhYNb2bowIpfMjCVsHfF9OHFfqv-3H-IUTrkXKuR5lC41xfcprn490O36dX2iUG07ZbpTL5UhfkBZ0YkpUhTGgKEb4sfrAdHFTuL5Z-o9Cj6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI4WLvJEI4J9nmUOrWKNcz5y2Zla__0_M-czldEHZKUHGwsiOSm3VHvRReBpmjLqtRHLRdcnhJzC6g46YjkVDv7bnniY_txROWnkcfnPw_M3To9nWiBUiFi55m03pfMTR4LT7zjhN7_sJld16eHCSb1fM12lkUKkqd7eqvMKReBl5f5hvhF2_41jfGwnUgbI6_vAVGq3Fz-6FpM4HfeISScy20YdXlwESIolm9ku5MO-47sdrOT3FtV1IzddgYimJPl1mrbFnyl4enRtCyc1-3AeOI_CsgnH_30zepDSkl-WYplhMv3GLoSAOSl2U7KWizZe7fQ0ylD1hLPJR4Xpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdmAkkMD42-Nm6nU2U0qGne1SAbJL4qSEjYTQtmtEqC1T7wADVbimGlHeN3Iouq2cxrUqH2Z6B6K0a8LZOFueS1yhLuEicZfrSZtxcmSGQ8l9nAcDRD5micPcfZIN2FQ0webbZ-aA3YjiVt1Mf1nTmUDUvT1Y5337nqQaBTvq35IxHftS0BtsQg5tef4dCmZGhs8R0uoDPNF7LZ2y3BdUIeV8IcIdGKhbMwzVbCZEQu_Yv26uXnCJXqlyuAfxQz6idGzJGZmQwc1BCZOLjcPUbFpHlUgA-ui9NUByKUiRziSjUoYgRQKVVB5lJ7e-SerVrXhcGQHW7sJ8F6w4eChvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-OzjkTZtYkel20LYIWQUGm21KPxmJsCcQ56CjpBwl-Ea7zMprqyCeemePZXADjNn_UuSYJwNNIbUzkDxFUJ96bxX2SQkrq9ew94mfi9u64qvQ4vOwwR01mTKNb9_qmPZUVDXFSm9qngRi_9ekTK-ZDqWUsY0sWxchtxjoVGzJHZfN1ctgln_3WaGCHsYnp_r-bBNnCUVvEHw9kzpmQuPOC5i4UZ3_UtpLS9k0NKtUv5evR56fzDNHofslxkR1BMK3JdgEJk8g-SHydLXpV7xK2lUL_BRFn92YfUhGk6QPgZSlea6uoQaijFl_CiKZABLiTJVJl7okwo6JMhP2weIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heweYF1bLwBgy5QtdChReWknoUdpBmZupvAsD1ZFxurzmwrljNykRbkZ3VWItK3Ao-WH4YsKdsDwc9PqMu4kIDLV8Cc0hTWM3MWNgpda_5U6mS8IasOAeG-rf9Xd3-zMeNtYXKQ231zh_q0JVAMPiM-qsLotbBlJcADAhUBMNibZlpdQl3Byr7BtKEiQayFWK3qsSWp9cJ5UNIWsB4kxSxqBeJSTbj4djxzzOioltsieH4LUcVMRwK_dlf5WAHR1tHpK15dtmNs2Ufz8ssqDuLSS6ouAd8LFHjZGM4vVlGjzmjVzGbbHRQj8vVl10Tf14Doxxt0CeWz3dBOwwCaHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlKhOqLDx-HzpvTB7yi-Y6BTtDsW9K47KIh-d7O92VyeIcztwtvEz5F0vNMf08gJldnR_pYU-_Btv6RiSA63_seZK1kUSEOIMkU6oLKamhqrKZNm0rJ7vykod4hqDt_4VYuyd5taw_QkPCuyU9IUP1uHVwXwj9x5dwSnmhhc06RBA4ecgo1TxmHJUoFwn-pokULtzjzSIjcHit3weh_Lvs7CTOGbx--iPAyKiabem_MdHf4-WsZLXy5NPjad8K4oM6sHUcL8140VWtxpUFrWZemVAJj5ROBZNufD8CGcYbEFWR1pdE1uHizVugihM4pt2Hhs0hc0zp_bZRnSLSVlxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=V--DtDSC5vt_FGv6MkMzWAb5Dx8fgDeF5IpfV8Y2Y5xjAadOrIP-QBXhisIJ4zzLlkJtxHBoJvzWApwB7NWWyM72bzcTtb1q8iFY0fZgNLKUdLePsKVYK0AektHF2T5E1evBdAiEL2gxii29y6QCpYzlatSMOIE6adMWi5xtwE9YX7Bbv9SjBMmVhfDlYgWx2s3smTpcRGl7iaPlST9GeHHbqhUXEjmjF7Qvq1lkWSisTQokH-baTC--WKfeLBsVbHpkG8H9lAt8EuVhz0oPdlcPbxdnmPQwxdjt2pbO4Puaaq6UVBnOydOFMOPsCOMlZH2kbgMco6pY_YQHaaM-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=V--DtDSC5vt_FGv6MkMzWAb5Dx8fgDeF5IpfV8Y2Y5xjAadOrIP-QBXhisIJ4zzLlkJtxHBoJvzWApwB7NWWyM72bzcTtb1q8iFY0fZgNLKUdLePsKVYK0AektHF2T5E1evBdAiEL2gxii29y6QCpYzlatSMOIE6adMWi5xtwE9YX7Bbv9SjBMmVhfDlYgWx2s3smTpcRGl7iaPlST9GeHHbqhUXEjmjF7Qvq1lkWSisTQokH-baTC--WKfeLBsVbHpkG8H9lAt8EuVhz0oPdlcPbxdnmPQwxdjt2pbO4Puaaq6UVBnOydOFMOPsCOMlZH2kbgMco6pY_YQHaaM-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWDON8dQw8cmj-9s_INtlLdAqROGV6MN5nU5LWEERbOdwSHQbfbUr28LltIddBq4qUANsd-pRJBXmIZ_3IOnqp8nmwEt4NK0krdmBDST9h6n0MLUNZm6kMv2gYE-NbK87poJIkAl4TKTd4ntx2yMUhmLxky7IlrLETt9b96TIQeMCC0Gx6K1MWJb43xSCLS00cRxHPZFzKQfOXd56bCdUQZgQFx4COMF_FV1x3MGhT7_zHeGMtuFb0V7mXg-hNgWHxxJTa6ZgboB5wKrnNxjnSP9VK5KDJJa8GscfWCMoLysgxQyni0Gbkof-Nz8xp0BW0u2dfpli_s3nTYBN7oCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L04xMSlOYp-ZW27i7l4aYdfHvhT503gvWF9eN1-RniH3ikjS7SEZmVP95EEnutBUwT-JKH1vvezrYoCWOzcTTYr4NnqFQJ4H0EKHxJ6HuEe7fsKjCqtS490VDfu492ElXYe7l6TW7UfjYn4PP-fW96433vnWLv_dBCrPkWFqGOTg76NaOyPFgUm_ouUgb-fNvHwNBt8MABYmx0Jb2oK91kFqLblmDRHmMsMt0qSF7jjiMEKn5LSmLcnRozZlCrOP8HrmlH-op6TRFyD0NkVFOwz9yKYJpoQDmr4lTJzilPG3dHu0niG5oD4e9hHKB185YMUgIm-C5vh93rekISkAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGopvwx84wWz7xc_3r3lFV2rWrVsRf089-jsak94alag1VZFAdVg8UKk3QdX-zSkZVds1TyxToN3YqfO_KViI94Yp5XaowFi48rbQJhVuU1VXR_X5hCMrZFp1zUCWVPSia1ZCqCTZgshuXLtpMIxN7B3GpvvKQvX221QnXzEV0U2hWRuFltAw-zDl_atM1ppJv7K5od8WVrShYPq7ienRXXMn9eXVFt0_DxfEVhoqJE8kttjm81H19zt9BrXUIww0ITh3DeCjEKyb26gWSsLlcf1Z7Rua9LetR9biWyx_rGgcP9BdNyzL7SUTug-Gv2IyxBGIBms8L7PAf3cKHsEOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY3-lxR_jo5ZpyxXGhOfMsp0OkQOFpu92bVRZmoi_olBi8s6O0go-FQSnN7Fl2GMblp_1FWGy5Wqdu5DrMFuSOiQ6Vgn5LyyblzS0mweEp460tq0O-C4vRgqcIiUL8LG7gq60X3xnnvBtAKMcv-m_PsOjWheFIHwECkpiZqK5kaP0jdpihGhTw-WutLMzQGsXYiKDskJ7iALUrnEXnkCfAJ8b_kkn9vVFyYa1gk8SETFZ1JXBJL2U6EGBrBSnfNJKWQ7gstcOFnU30QstfnGvL1ccnWh2mjixzP0XWynX07EfkTiwaE-mGmGvEK4zVYgxGWSJbHLuePY2XxsJ24ESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGUZVvTLCfSssQT9UWoGteFyMKV8Uf22HjJQ4mnrsY53ksJvzIdLFWQ11Ej1j4nD2twHkQcFWd4ksje_FZkVLE3X608Z24oznHZIRKcEq0HyyqTcdD9chwicg-shJ6ZZArPAbKxjg04WGi5v9KfJgmqcGLqheFVGCTx5GM6PjyrveX7pqNnML5adblNc1vBUXecFmcER8JtRDwzf6INLXbuRpzGWK0R2BH1wvIUWgUpj5bYyPsfof8-NYbGz8oWQN5q_tm9yq02spPF2yFzHC3xDih5Hf8FRgCPxRJJdilTmDl395y7NqAUKY27cFlu8zY4Ph1C2L-2pEUyuhJIREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBNarZY9dwajLYF96nWSpms0XCssaKlzNNx7I9_BE_k8Ib-ZlN-XzEfBHhz5ADlinxyN89A4UZIY2iGbRHh4TsjZQRfCSkvKFaXYt-0sfyDmA7bcJzbUKvo6-W67TjRLPdEhcghgPTNjjiqXLnyVwzBUg46-RrzLKtuSdw-b7c85nomnm5ZMjGIUeixgBMtKBc06QRya8S61G6es1o3DTSAqaqCt7b-Ax88ZlYRRlSsKMnqwdTTNa7bWyS1M0HUADi7wRFf6aWnlvVPNH2ZCCLhMPTN7ZoXb_fzn1P-2EsJwErEm2jW4AhxPMANRtd8VtXpFfnjO28_UkKoZFW3mHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=iu-94__-2Unsj-QOBkm8o7k0qGctdIhQfcnNXYK-4TRmF82prmqzvvnWqgE-CQ0cuSm96WFSq15Nyk0MNlcoGivyzfYXNKz8LARNX4tTwJj_07ymQLIEBbwU80sA3qMVhMscR-ApEBvgI5Po_866XOMok5zBYJkjIkj5eX2quk4wLM7AsVkPQXQfAHIUQjPWh-kdVswAEpHVQlY6WHcKMdttVQzHmMRjEPWzVxY8Iii_ZT7jGNOCMnAMQrxV5C4XTzz8UJD7UchuOEO_mRPpm3Mmy5y2gofyZmJJaWUCa8cHbmsphqY-fsL6i8vVgElf39jE1a3yPn35yCOodI41uxyGUTeB8uicL9lCGKczHEZJpZ4U9TpSN6AXAkKjcV9QUOaUk5hNlcm31Ueb4ocBTil8x8hCrNVHVlCAI7xvedjA2F5w43Y2DqhxAFL9BU0Hh2xTUIw_vOQey3qSoRMk7GM15tbaeJgIMWhuqWq6wFaYeaZuzJHyVlduDj_v4Cv9wdG5B3YI5b5saGQ82By9CV3-kgErd29FpfBsRusg6NsbN79ic0ahV6Wuw7N3uHbjAct6VfVXL5VzU9FiT0a3ha059ean0vKca85By7CIqPcWVot2SRIfmI5ias8ucCBjidHp9l6bwLcgd5Hf4a2Yla87qStR2W4U_0g3GGvi8ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=iu-94__-2Unsj-QOBkm8o7k0qGctdIhQfcnNXYK-4TRmF82prmqzvvnWqgE-CQ0cuSm96WFSq15Nyk0MNlcoGivyzfYXNKz8LARNX4tTwJj_07ymQLIEBbwU80sA3qMVhMscR-ApEBvgI5Po_866XOMok5zBYJkjIkj5eX2quk4wLM7AsVkPQXQfAHIUQjPWh-kdVswAEpHVQlY6WHcKMdttVQzHmMRjEPWzVxY8Iii_ZT7jGNOCMnAMQrxV5C4XTzz8UJD7UchuOEO_mRPpm3Mmy5y2gofyZmJJaWUCa8cHbmsphqY-fsL6i8vVgElf39jE1a3yPn35yCOodI41uxyGUTeB8uicL9lCGKczHEZJpZ4U9TpSN6AXAkKjcV9QUOaUk5hNlcm31Ueb4ocBTil8x8hCrNVHVlCAI7xvedjA2F5w43Y2DqhxAFL9BU0Hh2xTUIw_vOQey3qSoRMk7GM15tbaeJgIMWhuqWq6wFaYeaZuzJHyVlduDj_v4Cv9wdG5B3YI5b5saGQ82By9CV3-kgErd29FpfBsRusg6NsbN79ic0ahV6Wuw7N3uHbjAct6VfVXL5VzU9FiT0a3ha059ean0vKca85By7CIqPcWVot2SRIfmI5ias8ucCBjidHp9l6bwLcgd5Hf4a2Yla87qStR2W4U_0g3GGvi8ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWp-Sc-Jj97CxZTx-TJ-8keqhN8sgZtUmsJozhATqPA_5BTa83Fro2ntxOM8DJ1tBWK-x5TyQli44tsyxZ0bfcNCbrAUe9dXU1omYeDqDvwISot6VHuQvjZQcZMe_HlPpXi-nVRkaSoZkCpi5Ao5ju0WWi9oODU1kVz7eperaljq2U1nqObY2cuvngcAMDKTA8dy3rfv1xjfXreaX6B9ZJdW9TluP4proRyEFyZ5Q7kYvO8OiQtbkCvuTRFsRoQVokSdt41tR0EIe8RLLJgAAEQIjhPFJjiGtDULwVAutkvpryeE06hrvJQ4jhFbVRKzQper8Rlwt07qKIPXRygMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=ct91s5amzSIbS7xvebudnvu9MdML6aOz_kze2WkznmFr3vlo-JDzXP6p6TfFjMQib_YIlk6XkDDljAQ0u_WcwzdV4J3aY2ohJu3NZKQk0IXAA3ChFCxW1BzR75nDqanxlrkpYp2Cj2GImpwJGUIOoCho0DfEIITZVafn8iAk56EuGNi-6PMT0RvyI5Y9QcMYXS7Xur36YAI3klmn3FpswMc5e5L6gdW2i5e3YGriX8c9KbnGIo-_U6GyeJUA8SqPSU-KOS-e8Js5mvhAZu7FlSHDFQukDYngDFk6AQiRM5MtJqDCpW1sjOU1TZC32nekSyA3O0MnRwR6-6c9TMPKQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=ct91s5amzSIbS7xvebudnvu9MdML6aOz_kze2WkznmFr3vlo-JDzXP6p6TfFjMQib_YIlk6XkDDljAQ0u_WcwzdV4J3aY2ohJu3NZKQk0IXAA3ChFCxW1BzR75nDqanxlrkpYp2Cj2GImpwJGUIOoCho0DfEIITZVafn8iAk56EuGNi-6PMT0RvyI5Y9QcMYXS7Xur36YAI3klmn3FpswMc5e5L6gdW2i5e3YGriX8c9KbnGIo-_U6GyeJUA8SqPSU-KOS-e8Js5mvhAZu7FlSHDFQukDYngDFk6AQiRM5MtJqDCpW1sjOU1TZC32nekSyA3O0MnRwR6-6c9TMPKQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS2xjD7sPCZC_laVjkYVaebkRS399XNAKfeNkF5jZ2tD0rFXjNbVeKB_jTQ-_VYkvtg8zaYfoHE_likw3AMMk_LWNvlvqFC4QBeLtuIz5VtkT9F61kt1V98Z35_YtGP7Qemq2rmwwKpMspYhdgL8zegKn6Da1C9-fd1yGagVvIU_mkEBSwMd6T1Ne-7bKbgn7mracYy2ZdqRbV7hQUcbnS7oYTSqtzUs5zfh4C1NxouR0qdauuB4WIhamF7SazQl-88jWwIFBQzVzJTbaR8Lr9C850XK68KDF4BWguzCTD0FVEkAM0AFVaM3oZ9C9q7e6fxk_3eIaGN39zzj4o15hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSl_KreQ_ctmj5roIkXNKcMJaLl9mPXeDF4pZ91YkrBEWoK8rxDZOWEd2qCxmRZzECauiYYt6T5kkhH3VFJx3BtzZGS8k-ZNq9QBj92MwnOKX7YNnnHb1C0RLHELxB9vsvmXWGAsQ5uiobBtgaMFjaBrkQ5iV1XKuAy8Yo55ATSQA3y3zXeGUJCKqogU8kQnOeKmuBGy7TzxZor57lwk-26cYjQe0qihMo-ckipNooEzsbFXD1jZLdshX-f240Ks1Mb2we3Dclc9RSMAvGW7gBVfXyvsbYX3fsVIFLaMVTqGsZPNRycY2q6BilXlnOQfmL7kCJRXNLLNBs6PtPOE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpkMgI2VlHcbJnCcHu4S0Sjey7fwInO7oaembMbAyvdo93tvT3HhASswnhvZUZwjO6lPxjP9KoVhM2x5d8KYF9qIfyD5jrowtoLrTnj74NdyNAOooLele-k9IgoQ3_V-wNttQw5n8hN-cGoSuXa-daKp8ZbhB0obu2wL5o-KaR47c4B8weAssqugFo5P-qkvjCDJ64XO33LhTHLReawYyoCFk06rYbZd5c-fGXb2_dzsbb1g2engNx3o9H5ki5mO69ucqlWvFfnD12M4Itv5aUbJJDQDUxuePp259iGeNZEG8IpbULqn5FL4nJ1yfjsoRmIqxmvCEfVqi9JKICIxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_KDf-3tkFoZe2PPcmgSuycuevVIF_-NmuLUOJMJF8aa22GjLmucZ5nmGOCZDNLM5xcgkmuFuznu2G9GD-pwD61KBdNublEL6LVLvRQDXGSokA_FGys8QuW_riXyXY366oSI5t8w-9aUuu5LWKYPTM7b5vQ9cDKTsChza91suEqZ1VAo6lm__ToqbjtEYqXNylZfP6IM9x4t7GhxTPvxN0Ryo7nJ50nY-BDCR6v2FrbysY7JDs7OR49yRkA9nyRFSuOlw4HJ8DU6QOFq5ocs-sIkw4WhUEd23myJwC7Ag29UKappILbXijmFZwWRokPeizR8cZ_vLPZCROHWlBdiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2vhMh_0PsX-ZG0FG9guFwwjaC6IArUvNw14I82VY2KH5JdiKqU3fYwsM9v9WbkoI96Hn5uVGl5jHZKLHwiqmMSfIr8e5o59EFM8AwDcsH9MJ0voxoOCUXTvWbQl0jw57kQNLbJPyfhIbdrsUhhca1XdJmRHs3PsjaxD3cQsWrHfnvoszzmycKOa5_fFL9nIvqQXum9ZzCr2uQVb_z5ags5MsnOUxajhjUf3GuBc4sa10IRzs5Vu3Yd8nbvbL0gn4MxTj8x_SQr3QgwCOehBnrE8bvjkYlMIkKrQ3DqWKdPSgyTuqOzlTF2Inrf0510Kt4Q8hQ_OxVuBW6oLwCT6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg1rDeAhZIWoSav73BkrIpZg3zApeSdT0rBJyc_T88zG9fby-QPXWnnr8k6n8nALDodVYoAf_ggZHTL2873frlmW2GX8arvVQU2eOZjYKhAO51H_0gRXiI1jaKyMDobrD1mA9tASdyAillWl9dENyovAJNTX8KLWchBnaYXjij3S8PlkAMiVPOh0C9I8ztXaUFD9rILhKBtBhaielGFXdq8Br_zx87qkGdAYB5ApH70BVa5JNjWO9uwiDli2frk3JBm9B5B-9Zy3f8R5ZPFwjLGM_6M2Ea8fNRjnygtYFYJmyrg3aOKf5y_kJpDiwDIEGIkZ5IKRTZVusaoQ73vnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=Cev-fgn9nr807rvYEoYq9PvQ4xxSw-_D6tehu311FBc_B-0ZtX7LERn41dAFiFX3ueI3ooDYvJJi_QTLC2gt3y9U8rEaiLxKx7OEyTddLtdGU1hTzt-Fr7IhuppiJsVtWQLbF41H7ZpdnK9qUdjOrN-mzTtYeXYz5eQ-AFMEDCe3E0FX8tR74wpZ2Ee9-ghIZEbIWi8frFF4ErKCIjx3TilCmO9SUdqy6-I0AsvXBhpS3eLH6w8iRSeIjcPzXGtqngSIp5LpJtPgcLghIcTPi0w10Efr1BluyLeG1FCPwW9-mHWfNFFUSrX9rWLHKTGdQTxsOnQ0_5RIqL_4wG2pYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=Cev-fgn9nr807rvYEoYq9PvQ4xxSw-_D6tehu311FBc_B-0ZtX7LERn41dAFiFX3ueI3ooDYvJJi_QTLC2gt3y9U8rEaiLxKx7OEyTddLtdGU1hTzt-Fr7IhuppiJsVtWQLbF41H7ZpdnK9qUdjOrN-mzTtYeXYz5eQ-AFMEDCe3E0FX8tR74wpZ2Ee9-ghIZEbIWi8frFF4ErKCIjx3TilCmO9SUdqy6-I0AsvXBhpS3eLH6w8iRSeIjcPzXGtqngSIp5LpJtPgcLghIcTPi0w10Efr1BluyLeG1FCPwW9-mHWfNFFUSrX9rWLHKTGdQTxsOnQ0_5RIqL_4wG2pYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YePcymVUdt7TUh-hhUbtnYpgMxWrmRkC0STZLT155D0nb_2fkLkdG-p6--lAt6oIh8i0JEs28GIp0nzzwk7YKnYDHgD24_IgGwjDC2apo5YbTCnDRKachW6lr3FVfObG8zUdjlabrTV9aW-GayclX5caVl5oghAGc0DhrXqn8dk9dgBOGOuoBkg8LvAHu8y2KDmVfXMfOfCeAzeR0pktiKLf88NWQJB3Kaxc_4aWoGbKCghcw_TmmjP2G45npUFr0wsiB_69D7rFz2xW8rZRhyEwkmdBkIrqujQ7HFSj5VnSRA2lszg0nmKltf9uDA3S9O_RQWF4XunggSoPE3EtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPeqNrrW9k1v3XPZg6B6Kyn8VtYo-2AIliBBtVKUCSSj8r_GuTJUWmPbhLd39wzykzWJz7_YrPYnMhBNgrFa_nvV8YTFq5QeDW1yGfpZrTy1MvGa0Zp8z_4a7kFEvOjObp8ZRJXs9NQwA0hlZDEY0ZC4fVhuchBwzQF-g3TT3I4GyUKjWQBGoE-RfmSspgugCqMrItXVNBHfRfU7lvnyljavwNAQpvVUXoyzY1JOMuKM2XzwcOzQzrcNdrbf0G6AlNmVIJvTPBkFPa7kb0qvS_elilGxWkuwzYPKTGvCHe2EyjvotikqvbVt5_1coviGPv_GEKEITKVF9hfOYwpv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=C2lED9Z_4_cmq_ngc7U-_l_wconZbsk0wIEfnf7K2uKboIJc8nCf0WONfh0TWdNwRNVDbX-rxPvr_vzVP5RIyNubFZnbEnIbSxvdcxyxqkejJo80k__vsO1sLrkWA0Ia3ewp_B0ZYqPUSLcoCeobFBcH1hUA4U11nd8MgTlkjoeBxaoBAddQ-TZ9BERfM9LrdNno3u4keiiDtY4K-N0cdUPNiGb3-BTTdTHo6BTyo2wGKARaWaPzEJZEZcq4CfKqxGzYcw9TikqnOu4_dSv38cC_QrIjq1Yujkrh859o2owsvKeIBZ0dfzIyt2vtIs0TyqL2R1a5mboa2yTIdkSRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=C2lED9Z_4_cmq_ngc7U-_l_wconZbsk0wIEfnf7K2uKboIJc8nCf0WONfh0TWdNwRNVDbX-rxPvr_vzVP5RIyNubFZnbEnIbSxvdcxyxqkejJo80k__vsO1sLrkWA0Ia3ewp_B0ZYqPUSLcoCeobFBcH1hUA4U11nd8MgTlkjoeBxaoBAddQ-TZ9BERfM9LrdNno3u4keiiDtY4K-N0cdUPNiGb3-BTTdTHo6BTyo2wGKARaWaPzEJZEZcq4CfKqxGzYcw9TikqnOu4_dSv38cC_QrIjq1Yujkrh859o2owsvKeIBZ0dfzIyt2vtIs0TyqL2R1a5mboa2yTIdkSRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=lvPHXYE4x0ZMMzkxKnp2n7V4dyNZX4DRv4eQkykSVXaTDAPHydC2eouGLTid4Gk1Ks-QKq-KsWmT_C3Mxaw265QJ_Y7v6DAaMeQQQ0f79HpcqZ0kB9J7Vb_MqJzJd2VeJsY2ClZ9p36MmfGE94EfEigoNL_v3JJCZ10UzxFNOiTpzH0r74rccQUMHA9a677rQ-WZF3nEF3c8hwxdaqAAB3CSsNYEGzsM9xU_UwPlKaZ-IYQBk74xxJ64nKPtnWA-Kd5mBM7FQjeR3ZDS80C2k0aWudbpoNStgJaLg2t0mNdz6JCdaJ-jhzTOyEUqSrA2AeTDeLsqiPtyu04NbPHFKYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=lvPHXYE4x0ZMMzkxKnp2n7V4dyNZX4DRv4eQkykSVXaTDAPHydC2eouGLTid4Gk1Ks-QKq-KsWmT_C3Mxaw265QJ_Y7v6DAaMeQQQ0f79HpcqZ0kB9J7Vb_MqJzJd2VeJsY2ClZ9p36MmfGE94EfEigoNL_v3JJCZ10UzxFNOiTpzH0r74rccQUMHA9a677rQ-WZF3nEF3c8hwxdaqAAB3CSsNYEGzsM9xU_UwPlKaZ-IYQBk74xxJ64nKPtnWA-Kd5mBM7FQjeR3ZDS80C2k0aWudbpoNStgJaLg2t0mNdz6JCdaJ-jhzTOyEUqSrA2AeTDeLsqiPtyu04NbPHFKYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=a4ExKeADrpQa8DjmhbxMeQQAbtBZGcpjf6J1nl4Jhae1yTZ61V3gEcQuHOxV7feQ-bMX2kU-hUJqVSQv6Q4__UqNQ0Wu2oLh8jjlF2h30IKNXEhuVfjO34nyXqsipRzSrWNkd9D8PXIDjtzcuQzVp-4mhJRYkyufiBgv7GyzpQOvfDgBR7lWliV3txLYDbJ3cEFUxNMBJ_zbf5vAK2hfBlMOJU6yN8Mfq4cvalDBCzkVp1SLagV6ngW-NwcMZDqapzOH9CT1M6e9qW47qsUTVb8x8RiI0-Z-DyFob6jXMUm12gJdT2x7D3SExmTALu9WlQhzFmk_9bCGOZj2-3tpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=a4ExKeADrpQa8DjmhbxMeQQAbtBZGcpjf6J1nl4Jhae1yTZ61V3gEcQuHOxV7feQ-bMX2kU-hUJqVSQv6Q4__UqNQ0Wu2oLh8jjlF2h30IKNXEhuVfjO34nyXqsipRzSrWNkd9D8PXIDjtzcuQzVp-4mhJRYkyufiBgv7GyzpQOvfDgBR7lWliV3txLYDbJ3cEFUxNMBJ_zbf5vAK2hfBlMOJU6yN8Mfq4cvalDBCzkVp1SLagV6ngW-NwcMZDqapzOH9CT1M6e9qW47qsUTVb8x8RiI0-Z-DyFob6jXMUm12gJdT2x7D3SExmTALu9WlQhzFmk_9bCGOZj2-3tpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAMTPRX8M-xFUexg1iwvJa3j3zBtvGBaD6Nxm2kiPDlx2RLJu02vhtpNj7L4iEVrvuFRBbHiUKtnJWEFI4QYANnmVATZZjYEprAHIY0L_iafiaXGrOwyBpPw8FP-4MQ0VFNgrw_kx134aQ00Ma1ipFo3OiOrsAcwyv2Lz7YdkfbRIoOxAZGzJdQ5kUgxqmsTnOEsFhkqa3xoM3Qe3_p8I4w9bp4OsqibVATslJ0elFcwoIbNNto4EajjolJLjmro5yzKOeaUTBgOdSiV4NqWXKefdh2eXTC_qhS_rDlnFsTK5Nd2CM1TxU1Re0jqSulNb-HSOtzkjcwPLgXiVgVMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhmW3NGKnDZIBLuUcgrcqWavG3PjSYxDYwhf7TM-_2hpPUzelfezRn8z0TFcBfo3DzrMASPFerwQ58hj504Zyf9hE1WDpdPJT_sagpJdmGlHdqdl3Uk3gHwjzfBA08NEOf2I2yv7v49sLbuC42q6hF2ZEYRvAv8BvsemFF_z3-u0Mvg1x7KzBQ02u41-NME8Dujx6MlIlJDy3ml3CY69C1cGFyZ0cpjvQ7GX4i61HdR-KALxc-LwIFB31Rn34EgN-HjKYiwrRH56_09W0b8KSYk4Ovp0om0-62eNveFokRGkxGE8ht2vFZmuOmnLS9y0BUf53zvM7Zj2-DQdnolHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THKCcySdhtqXUcOeozWYu7_U4UbuYofmvWmSdpnvec79TjCE7sJ0zr_zsXUttqRBGaS3ti01NKpLxKXH9oLXMLyOyjlPJv2mM4culQFEHa5eQT4wDRoOOim3yWpc33XdBGK8uTH8IR_Ib34v66sNlJlfhP3F-X41Zox-DoGIUlDrUnvB50FYecuwgeCnasXYy0nDmt7IPOoBzghCiKDud3ZieWstFChbxrLrzHClBjYjPPG94GB8Dg29fRjNAtkp7DGHz9Ct7AB6PwryworWsNjtABCt52liOD6tHcORHFL2Bc-GL6X5W9s2GVFz_KpK-6HEQFP87Q0KosRsxskmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5erilW7VgeTz2QdusRJW5_hOAJF0AnPdYScnKJv3n2HPqh8MFTo4TawZejjJCKQVKH-_l4C6XznKEKmfhXzS7E9aFSN6BXKT88rZbIvXnx_8mErdyBxSJXvpGPBkQfcIZifBCWOVFT5NS3V_jlFNpbxK2i225yRu7F9R6-YYHTC2FS-5hkHf2lJkr2FKLm02lu1S3xldoI6aOGcONwUN1GLxYAdg4AgeETUevusZgqV8U3Jhqe1J2Skjkf-E_UVBolA9FjMRvNdyguCS6_O2Z9FwFkk4_nBzczMz0EbKDFwPllxpph9ioL_G9tb-AIayzIZP0UNUr1FuVpXbekm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgC0E6a4f3K_dWdNlIMBbhAke0jM8yEupoN9f70ZyH8ZIeRAqxnaEi9XuMzvw6V_ABu6_ivF_JHqAfkJn5nCK86X8hynDICC2N9zk3e2Quh_boYkNVzwgAyylmTHhttUfhusZ3JHYmJrlvUNE3cI-wXxOFwbUCI59Z6Gcm4V30Eypy3vVI0CCMKt57YR4ZmWymtgS4_HOzv10RyajYYy9Rsl8vWnsqsLdak5l0lI-lB8l7XRnCST5uv2DKYXCf3ZnpS41yxPm42ZjpO6C1CQvtOC1PsE2aIFrKFwHaq0-yv-bUGsRDnY-uRfmadyifrv-F8hbGXAo2urhoapBg9Xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNh9ydiNyb2ww1b4GvesCwKzJH-RescD73jBzo8Gi7NFm3O4qXoxxJIseXMK2i8w0-I-H5zX6BVgWwQdWEzQ3uCosJyRbf6NECGxq34IlfeESkCO5zpHrEngAhwxcAVXGKa09RaPSJTEwkmzG0UlO4C07a3wAPou2-RsTcO3n_Rxaq40UsS9ZaPh4_gmsghqt50MXqqbHjRk8yyLvvrEwGwrPbDvM1SjZWH8u5SdJmVJ3cp9zifAF3__ILdHqjCaapn7C5RBMS9PWN9EsTvPDTWbGrGeHWZto0HZYn4qpmUzxf6sR6QOWuR5obntYmAoEh6-GecdxJA1MFBY6i-OYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfYFRI5fcG0QxKm40ZuW7RGpv8ZrNkN2toACjINIch1gaDDImkFfQvPLCLd92sy8KQ3ZcSJwjz-NuAS-JRxJ0eMa9FUnHBybyCk160oW4H6PseB8j99hjeNP85bZ66y4UJcnqmZBgmhcS5_45EZ0aPuTcNRF09GgOkLZnHxn0raLTot_pfjME131kwLQdGPkY8x7Q_sDDKFc2FgNTy8WgN1f3dAfqFUEmOZKO7zzFU-c8k9zJE3_qlNRkrRqUr9Jg0BQOQpblvIJELo-NXCWfoUZt5ShdNNm3w7LDmNSC-7qB5CJHvO-ENvTf60DeoWuPukenAvT72ewcoUS4soJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=WhLKVRBYDOLe5J-ySmBp9C9ObUpL8IDs4UaUD32IeZxQY03Nu68-i1B6tVielBfA7_OuNWps4OaTxqvQK--DAh73_I7F4Lmo8XBCwgsT1o-Jhs929ehofMK2viiJGWXp6L5scVR6OT-xqqcSSwGxGWSPOafAeEaC3XMxemTlnBCjTjyHfDDUrcLMQhFyEY4x5mywpHqUmScRYnamUSPhrlzLO3tof6J6vEo_Le2XzaPxK_fyyeWE895VInMdhp-BRhxRIRZ528QJ0W93zVjgmLwg-jrLiCki2Mg2O3dcgV8b6rGgPXJSCqesSx8bB-y8Ln4nGr8mMSzY3PE_bctM-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=WhLKVRBYDOLe5J-ySmBp9C9ObUpL8IDs4UaUD32IeZxQY03Nu68-i1B6tVielBfA7_OuNWps4OaTxqvQK--DAh73_I7F4Lmo8XBCwgsT1o-Jhs929ehofMK2viiJGWXp6L5scVR6OT-xqqcSSwGxGWSPOafAeEaC3XMxemTlnBCjTjyHfDDUrcLMQhFyEY4x5mywpHqUmScRYnamUSPhrlzLO3tof6J6vEo_Le2XzaPxK_fyyeWE895VInMdhp-BRhxRIRZ528QJ0W93zVjgmLwg-jrLiCki2Mg2O3dcgV8b6rGgPXJSCqesSx8bB-y8Ln4nGr8mMSzY3PE_bctM-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8s73mC4k7FQauXzFz7ettSheeQkvoO5YDhA9SFPMfZEcNxIiscSqulSmGFLZAXZP0TGERjPy294cg0hq-2h1Divygbd-pEKopbK4WI9cgYnNIwS2H0oGKEVwkUgBTKUaz8YmSy9jjZ82jKGM5A2wYz4QS4iDkS7n7I-rjqsF-GoX3ThIqXY51wgqhNMYa1JZW7gY4A0g20LSjx8HUxPyfhHfoF4wFaPhEKSXdxjcxYrWQjXhBQgPx4ckDfqC56RRA_2VDalu3zpkx4eR1gO8_bqsPVhxg8-4oq8AzTXM13YputFLFPfRi1pdSF8Hjw8CILIkPF6uygfGIyEg9I0vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAvTLM_XUaq-H0LLQrY_nkTZd0-1NkxQxmKpiQt6RyTVxlcMGvCae7gL9gfY7g3IV2jxWFGPqrOi31fnoBLC1KZHNzeFyOITonOQooKbJHr0SDOVrG5Ka_YyRBH4E3PsV3YXZbiurm3DtP4h5wQX9BZI5T_5O70sgfv1BI-in3YEQ6CeUJ1PO-EANsncr3MEXbcRNVeWYdEwu9TIvOSJquIP6ziIrSdG3TwgWQ7D_lfpRH2MFYtJ4TqmaLbfyN-FgwbKKu0zVRaw8DhlrOaiaFiafjgVbr-nZ_A7KfJYgPBO7hinqDRkr58wiQ9m5IWT-ImwgIA9Ml6QJPIvYwdMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=hUOh4kXkVzo4t1N5Wk6fRiRnorRnHFfsqUXIY431jmgJtxgGNQt87B2pMMP1jEHVIr4lRPjQwPTdlZJQXRdLvv19AmEW1DO4bEuKmsXH15bUhw7Yt52HOlSIbfHp-pakEe7EzWMxDterZrTIOmlJMMnZaU-NEBmX4nvcHgcjzUyWYcAPfwcsZvqg40QPF9tV8Rt5B4lGkOtJaqbRiI5m1kEeFzQEPAkaeK0G0uZR9u5Fk5J2TvrMjh3qsfv4tABLEFKGBsgoNo6RoYBuskuBvfM_8BVqM4j791fFnSp97fWIDuvBkbCn7Tv0O4MtoBUEkmwioKFf8MwzH8B_lqnihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=hUOh4kXkVzo4t1N5Wk6fRiRnorRnHFfsqUXIY431jmgJtxgGNQt87B2pMMP1jEHVIr4lRPjQwPTdlZJQXRdLvv19AmEW1DO4bEuKmsXH15bUhw7Yt52HOlSIbfHp-pakEe7EzWMxDterZrTIOmlJMMnZaU-NEBmX4nvcHgcjzUyWYcAPfwcsZvqg40QPF9tV8Rt5B4lGkOtJaqbRiI5m1kEeFzQEPAkaeK0G0uZR9u5Fk5J2TvrMjh3qsfv4tABLEFKGBsgoNo6RoYBuskuBvfM_8BVqM4j791fFnSp97fWIDuvBkbCn7Tv0O4MtoBUEkmwioKFf8MwzH8B_lqnihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxGaFRZ-hSHkxbglhyiCKGYsr8u5ymgGESVN01dYjH5n4Gd1TNYMlffof2MxrzouT09OU922aRKv_nwkP39bFj3yf6TwzH6gv4C6eFBKDXU-Cmmp20KGME_0kS_Df2OpiciFw4q_SaW4398mYSaRlYZ1gwD4mY71y9XfMJ-RoDGJ_E3ej3qDhtQGT98knkQlIKLYEcfcbGAz6KAqQisASwghYnhwgylaxaUG9byVvJHoa_yrVJ5USw5vLz3_FXSTWxAmpq7yguKA1fNd5iaZVy2svwnCTI06aDH_OPoEEJQIGnggC8CF-Hj4gwRbg7-2DnHH9LZXONh0J1EjHqDvEYj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxGaFRZ-hSHkxbglhyiCKGYsr8u5ymgGESVN01dYjH5n4Gd1TNYMlffof2MxrzouT09OU922aRKv_nwkP39bFj3yf6TwzH6gv4C6eFBKDXU-Cmmp20KGME_0kS_Df2OpiciFw4q_SaW4398mYSaRlYZ1gwD4mY71y9XfMJ-RoDGJ_E3ej3qDhtQGT98knkQlIKLYEcfcbGAz6KAqQisASwghYnhwgylaxaUG9byVvJHoa_yrVJ5USw5vLz3_FXSTWxAmpq7yguKA1fNd5iaZVy2svwnCTI06aDH_OPoEEJQIGnggC8CF-Hj4gwRbg7-2DnHH9LZXONh0J1EjHqDvEYj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcSjlQm_UMg2YYSxEWtuzEt4Zg5s_KhMVCLUyLEbKJQzl1vjfmLbYYW3H44_j0F1UcOHkSzaZRWr0w3v_7DtwHMOl5IMMk20nAaxs2GUwh-h-_gf75GXDqrjI2YOGwYw1kgT0tWeeKTSfO3_M4LSpgoh0z6ysUQLe9TFztm6U4LfnPQeH1dtqhbWx7cszP6CoY-guuAF8F7zMnFmAYMpNKcZoI7q83MjsoCZsJiNcAPR_RC1Bu-PpqIb1OdyeZDVyY--EMZFEf9l17VotGVmcFTW_BdI1hROk9hvEvmJL1BhDwvGIM4SdLjxt1oCqgV8Z2YIuRRZUigTgzjDqNBLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=XQA7GUCkldb7CyiQGyitZ7Vc4S7jEqKbamPLGwrRPn6STKHu1x0Yu_sn-o9msAEVRInX1qy5TE-Bo7abZvAiuFRxhNGdAxNzn6aLjWu4of-heAO4YEp0NbSvFyNR24uXgCTK_InU2PqWBtAWnOelGVo11MDS9QsEBvnDq6BU5RkhGVAcGYeaUp97azgmhZYsCpycRjeKMDtp0e3N46CtgrjkoMOGBK_qmkAvYeV5516EkJKaqHJFPY4x8UOpCuz074munmuoKUI2p8vkP7kJS3aRSEDcCzCVwuYR4oRtROcWmnKFJGg17gJwTONfMs2V23d55Ot0_MPLFDooZGEEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=XQA7GUCkldb7CyiQGyitZ7Vc4S7jEqKbamPLGwrRPn6STKHu1x0Yu_sn-o9msAEVRInX1qy5TE-Bo7abZvAiuFRxhNGdAxNzn6aLjWu4of-heAO4YEp0NbSvFyNR24uXgCTK_InU2PqWBtAWnOelGVo11MDS9QsEBvnDq6BU5RkhGVAcGYeaUp97azgmhZYsCpycRjeKMDtp0e3N46CtgrjkoMOGBK_qmkAvYeV5516EkJKaqHJFPY4x8UOpCuz074munmuoKUI2p8vkP7kJS3aRSEDcCzCVwuYR4oRtROcWmnKFJGg17gJwTONfMs2V23d55Ot0_MPLFDooZGEEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psPdgbjP3ETbGZKws5n6SckeB78YQG16Ys3jCIpIdjkftmk-ryXhMJjMnbw7_bQwdGAe5DMxOPeDt2KXotAzIOfZyjnqEYsVxpoGyfZcgqJtUAjbGsgYat8goT5iR1ZQHSS2BglUZZfUlv4CvyO28GK6hI5d5Zr8kSskIfsxrCAP521WXW8hDUpuS2wk4G2JDQ9qKEKP5KkJVYxP1ptdfI-zzXL_FndbxblvLR8pY7xq-6v-gbMulviF4oE4xk9BGam7d-Su5ycD16N8Be5HxGB8ucjWQ102oa8VlBnvARWHMC9zBGbbchVdKJd4L2lD0HdxvR1hRdQtjjyQ0UGqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=Mr6i1JdKUtqqIRXlAb2nmJvRrqJx6qSBjjWhGUs4Bdd1qw18ikRfds_ZsCNk9OrDLHGaHSXoIrKwhqReOUQh-l-ChmJPeGWg0eT6tMbBsEfdWyq9o0p8dYWZd_defDfQApvo0udLCFm74CU7DkNxzRogLuC1fEhVu1zoadABr3GBZ-bBnKwstAbDzd3wRhhiEILxgDIc1ak6y2q60lBriufmkkYlxBEyPCrlmrv0mv0-NLfmHdnnLbmCLREPoblLER3ZPskAM7wR-0m9YI7Uima1SUGH2B96KBmti3FDuDhEpsogM13apqTKG_thVxU8_NQ30SB-jCdp_bdeYe3WpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=Mr6i1JdKUtqqIRXlAb2nmJvRrqJx6qSBjjWhGUs4Bdd1qw18ikRfds_ZsCNk9OrDLHGaHSXoIrKwhqReOUQh-l-ChmJPeGWg0eT6tMbBsEfdWyq9o0p8dYWZd_defDfQApvo0udLCFm74CU7DkNxzRogLuC1fEhVu1zoadABr3GBZ-bBnKwstAbDzd3wRhhiEILxgDIc1ak6y2q60lBriufmkkYlxBEyPCrlmrv0mv0-NLfmHdnnLbmCLREPoblLER3ZPskAM7wR-0m9YI7Uima1SUGH2B96KBmti3FDuDhEpsogM13apqTKG_thVxU8_NQ30SB-jCdp_bdeYe3WpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=tl523yz9vzPpsG8j-F2cb6NHj3myBAvF5thQzutEvKHc17OfaeDJe809U6UUlLKsNE7QNfp9CS92BzhRksZrQu4N-nXRMMxXjPq-KE4JaROd1ul67C6CB0ANjrttutUgowuZRJKpDV2WjU1go5T0p7etVpXrSH21VqJlKznJR_HBMePdWQMqFQ7TpNNO98jEi2gQBNrnEUbZFyK-NJCvb1Qk1eTm5ZR7g9RNLgR2LyVtXMcwA3PnLT8t6pqGptu7_6DvmWlG3U56YrFHjY4ko5p2ig9BJiyOX1D_f2yhmk8Eiv1vQ_FnGEycFGY6Zm5y6eoYV-BJraubHJphTyQnKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=tl523yz9vzPpsG8j-F2cb6NHj3myBAvF5thQzutEvKHc17OfaeDJe809U6UUlLKsNE7QNfp9CS92BzhRksZrQu4N-nXRMMxXjPq-KE4JaROd1ul67C6CB0ANjrttutUgowuZRJKpDV2WjU1go5T0p7etVpXrSH21VqJlKznJR_HBMePdWQMqFQ7TpNNO98jEi2gQBNrnEUbZFyK-NJCvb1Qk1eTm5ZR7g9RNLgR2LyVtXMcwA3PnLT8t6pqGptu7_6DvmWlG3U56YrFHjY4ko5p2ig9BJiyOX1D_f2yhmk8Eiv1vQ_FnGEycFGY6Zm5y6eoYV-BJraubHJphTyQnKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=nLDudE9EW5HgZYVXD2h5rJSal4vp-_fKODaDnGIh7bnp9ms-dXq-hkqBqS2-xKxnpbFpzx1ELAd_W9mXhJnToLc2phTH2Qvq1dzcw2btqWoAWVh9yZNCQpd6ZPuyjVgiyNWJkVGIKB6Rl5ZvHG-T8WryGGcjPfvVLKDT__DmXf2CgLEyeiQPJfXaUc9YgAom9cUJ1f-vck7kNTxYTPykJeNzGRKQpABpsV1y8vj320Z8w0aiDaHSF6cmCiC-BudkWbf12Ra4tWPqMjUQnD91rTHdpm80ACPDkHBuiVZg96dOsHOb6MCgyhuuV-9Z2OSWDaOzDTQMCvDTnPQsvRRVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=nLDudE9EW5HgZYVXD2h5rJSal4vp-_fKODaDnGIh7bnp9ms-dXq-hkqBqS2-xKxnpbFpzx1ELAd_W9mXhJnToLc2phTH2Qvq1dzcw2btqWoAWVh9yZNCQpd6ZPuyjVgiyNWJkVGIKB6Rl5ZvHG-T8WryGGcjPfvVLKDT__DmXf2CgLEyeiQPJfXaUc9YgAom9cUJ1f-vck7kNTxYTPykJeNzGRKQpABpsV1y8vj320Z8w0aiDaHSF6cmCiC-BudkWbf12Ra4tWPqMjUQnD91rTHdpm80ACPDkHBuiVZg96dOsHOb6MCgyhuuV-9Z2OSWDaOzDTQMCvDTnPQsvRRVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=DIfjKLMpyq9G1_SHjNUnwXCpkepADpWxW3jQSFHhlsoAaHv-s1Y--kR9fyKE6ZQUp5fArFsKtKJlErfxJpxq8y-0LL-sJGMjXuOD_w7RzZsOfaC4j6_fjCBwztfQBS-vg-KNMw2Ag91kIJTej9sf-MgtwJ1RvjbGYZDbBaHWSSsqzNnTftgN3PxHlvGYKWND9M38l8kkxuyM_WqPEhCB7oS-M_GOt_4s-EK_RDugf6zRTHDV4RA2WS0cVIiF6WRZdOa2FZ60OnkYyWvEKiSD3g-e-23j8NX4vMyBmUPbUiV2yKYPX1wR4AzmikccONUHSL1CeS7gDaDgGzIKlLiAeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=DIfjKLMpyq9G1_SHjNUnwXCpkepADpWxW3jQSFHhlsoAaHv-s1Y--kR9fyKE6ZQUp5fArFsKtKJlErfxJpxq8y-0LL-sJGMjXuOD_w7RzZsOfaC4j6_fjCBwztfQBS-vg-KNMw2Ag91kIJTej9sf-MgtwJ1RvjbGYZDbBaHWSSsqzNnTftgN3PxHlvGYKWND9M38l8kkxuyM_WqPEhCB7oS-M_GOt_4s-EK_RDugf6zRTHDV4RA2WS0cVIiF6WRZdOa2FZ60OnkYyWvEKiSD3g-e-23j8NX4vMyBmUPbUiV2yKYPX1wR4AzmikccONUHSL1CeS7gDaDgGzIKlLiAeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWH8sZXVs2fIbPxoP_AscnzqRhbFd7S0cdeM6Tc7iC1ghANW28uvYf69sCQhq9MKMSZ18Rhj6jKlIEN9VuaMZJokGAxb-5hViwG-qUxIjklbO4qnXQ48RY-BAR1qte2zOSDKgonjzVq3sDng9twq3DbuFWgLC1HqqOpfHM3abOm6iJSvCJss-TojvR6gxocJd-DKbLvkcKj7t9yggBb2bUaVK7PMqA86OX13lAnzmW6b5Zb1UqsLDvbP3gvVkk3t6L5dYmW4Gc-0FxKo0Msruuj5W490gNLjJuAg8WgnqaK3f2RchBlQnqEUs0vJ9ytb3xknM-hlKCoKphoyAkqarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOhCTiojAFRlLQgaTZSCc5wJZ-054gOV3kKu0EDfcKj0sGhvnwSBPt9OPtSAAlrvzNZ4VuLEXqeSxbWJh4G9xaBqc8obNAHZ86xR4vNjf42CcNX3G2-0QFE9SFnSw9QksGtEx9hkHgFb1ztNRaNp4YVmjsv29pykot3ex_BLZwUdIlGLLS75djiN4bbjLpKAWRPBYzCXyECAezlkqSK_9CYl-RuVkAixaZlov_5GO_TdHpbcBLIgZisshR1cC46brAl5UlTsC482lrVZsrCCdP1gXgk68bsn60Fp_aXcngRDsS6SeQfsATWOqMB35o41dE5VGJtK8EY0honX0cAmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVchADxclwqRxn94-HRkW-sYk4Lfw3H1KgcuTDCZDMJlrrcuPIDzXZRP-5tTw2tqdq-Ay3cO9hHbab4VhnwEY86IOTgL1gLr0_QIqvrSwP3KRE3gT62NS1qtLPAEnPlMIw0ukCW2lUX03TdQH7o1ElC9hbEsTZkNDVaN_9_xh6DPGKoSWZ_Z0_EVs8607tjooiYF6cNVvLx7Nz9kggJJi0l66sWhMGNWRoDwdx0n4s72DDDSm8nmC_YcpEA4dLd0TLr48f_Hm4AeSH1kLYP1D2G9tGOxQl9e5wxgTgGCHGXFJyCXc9lrYu2V-r58UowooRtjI1UYQbmnH4mcksO9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
