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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 15:58:22</div>
<hr>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWW7h8eV4XQlQ-eixZhR3PMUr_D7KXswAcNTpZ0jp6XXHgWPI6eFgPIIjahPnGE8RzrqlFn65B9GFaEdQT5jxPo5ImkY3bPUsmBvuG7yTyCcz7mTAL9UmbumIezRsjnaTvY1yFazRRznZY5lCz_RzxM12AaC352Y-dA1hvsUeglPn8u99crJ1Bnw8cD-lOwQ0lkI_kjAc--klLfheVDLErisGw-2uuCkCmftwg6IGNWWPMtaDuW1HHrbf-uqo7QAwsVEit_SaHZz4tjbvyocYxxW5Rlm2EV3c0c8A6LH3clJ2z0QT1lICSjKuj_fCc2GEMmt8F-NLPXXNAAOiNEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpbf0olxWIMaw7ui_PDKuMvAkw1D27ez2innIK6SmjaV55_Kd0xBBgLrZBfPnQVNLzkU3JN6v2mJb2SjAhWv7BenPGeoZQDlPj0w0qfplR342tcDj1x2H2aDH1Cb4EPcyZKZMxWBa4kOD6nPSXMKU7dYL_AI8wB6rqqZwifaUp9pl3ow49Dffna4AGKwJYaUreB16AdDlNXGb2Wq7FR-iXGpRxULd0Z1WqywqMwNVaeq1e5h--TtYiD2YSEQvd3yjFAihhUClvAF6qupbrtK4NUDpPbQwWTy-y_11nDZzR4qYxCey0U18HXHQx8TAzKOdWeqDFlUfcOS9uK2PKjmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuNRysP2pXbhx6dBhmffs9qYEuRh-HNanUZZ6G_ol8Us_W4L2YlFUo1Ii3V41w2dDoA5CuOG7UPBAeSEo0X_QworDVFcD41aCaWOwRJK7GyKYTBDx5xpMveBlbl0KVtp2tSHxvO6KyfFm2fhv9ca6z1zOKGmDuWyo_NEKQJP8hKguMvvBLstuDNsfLbMUDLNBENT8d5XySyHX2_oGOz2lldSuOhRoUpxe_eQa5ZJSaycP7MoMiAyASA7lmEqvccpy56F_sId-sA_09obaOpvdBKT0LMyxaCTLWTSXvQLIx7OcG1Q6baZrjADF4xlxp2eYxngwHGG5W3qKo0GL-aqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwwkQAdIgZvGFTFueIHDL5OVof0RW8FqVwHTcNK28OKlENjfcSzGQckxGAGG_TXJ_tpGTq2dh8Vhj5UgOMByOURa1iOq0EWl2EpR3uBY7xloHe5cU4ikBZJJ-KtJ-pdLul9S5LaFltEcjFp1au3vrg8OGB1P-tqY_jER0ovGWhhQuIQntYyHs0kkEs4WefZjARveT0W28LHrqT9I8dEvUWy06QhpfDiq9T9fRHw8KJKnEj-oXjNuSqlohTDJAO2xoh-ERjA4xSIwcg3gaYwAUI6N2sIl2-Dc2_5M8YZPE-DcsQoCyqaO0KgymKDqMWrv4j7eGAstUqVu2iG2JmeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLctmbZcPXgOMPwZwCOu936wO_a1I-jLcq2_W6Oa8GMH9IiYEsP3nd2cJpAip9GWWAhLBP3DQENHVpH8-ANWBPzX4ayj8Gknc6yaYrqzrJHqo9sy_ZsoOinp-P1PI5atj6dj9gU1BljZtPIHpkxlSrGSBsKZdyxbcVp8MCWb4qXZQVKcxZKdGBZcXp50O0prTiz8HoYD7iLJ8ooAKl0UujUWHY2gj7-PUO3WWEelaiS-53sLI07yqR6U9_T2qY1CWsR8Ifs2CBpmbILf4nBKl8c5ow8haz3sfKpElbuD-spT9B3lAeRPaL1paf0GiI6cU-JVmzj9tg752gkiCuuTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8lWTqogkqLu0r2VanN-ORu4E_L_NMxlLFR_Tj9U5UeZqM89VoWi-K-eiuI8I_Fpvp_bQOIRX2TOzjmOGSpzDbjD_mVeFbHuIKaM8a4bXEuEtmM-O5JeGdwjtmXD3SE1Z_ioU4Fi3Cx08Wf5B0uxf9LpuclOBqKEAz7rVm_1FHK4c4Vgt3QB6TxMs23a2_VdAFGnw0XeFqnK7ovtdOdNwDGlffyK9ui-tZprkAYP-t1zqRMZRqOMdLlRi9xC_tmsbrI_7BNdhQP44MGLuj4NBycU-0vP1DynmmYXLaKBA5EvaQi9vwyOApbyGqsP64seDgi2XuXwi46S-z4hJupYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2r1B3qBMTFPK8dLqAs9j_Cv2BqT2tQFrIklw6YWI3qg5yUOudW83tykOCl0b9AMcUB-pxrHZUnN_I-TKh-zY4LhF0wAGY4qvgEsXieDkj4eVXNK7yoeeunJEW1LZJFOrsvTkH_yJd04UxiSZCPezRCACjzzewZJmyUkVgxkT3Kkys6W-u4sv_NV4VlCJu6Et9zqluFtQ4_bcWph02PUbI-UQ89V8BgL7r6BwB1xbXKBPyVpICugUpazUEcpeeEdZ25ndlu1AZjciygKKWoh7w773cLYuXaV1UR_pu-j7GNt8TPlw6LZ-Ng70xpPx_c9GjW5R2UJb90IgIJ1x8wYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24664" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/airvqIQVxoBDLrSni_lVCpp6_19ZKs_p2ztXcLauzY0j3uSyABn49_-mGESU99RmpzQJP8iBDd87-Oho62NiKj7MfXjAm8VG6d8ancgH4cVY6AhkNgd7qp47vk5r5bn6USbTVHTaKoPHQzMkN4XHkGYqIVHfg14rFI2XEkeoFtvxzBhA2FtRwaMsk17CotnoPxnvHEYztx0dnTGFvQW80-p1B8Fy_SZ2-AL-77yciRryB1yi1GCouYH4alJHgqJFDp5UCf4HfcWRQ-zDDB2TYjwNq4oDvFbHs2o4G66Nhrf7AKbGuMxQj8xRNVFCB-iNGgGmaQri9fHs8bE6BGnfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Uf0xiSpGiLDTVG2kp_FQRqspEMSzmZieT4dOGJQZdqwAqtSKXx0NLscPEAwgKiQHAQpT-BPgHumg5cCG5Hxi8YoEhrK0vmr8spr-yKSKFhBQ6ETyeBNJCyaTOCSUpj44cu8OZhwVxpS7GU1mUOUvtPdc-NYpyZjuxqNnn_q-caBBqcX77Q7LFZq_N8kBVCfYmzo_R86iigJIAWj4sIYWE114iPVCqJqv6Wdp98dPh_qfyO2O-J5S6eHUXcLVr79VFPXLFGVaGpG8UbSAM23KLPDSs0QE0iLA5AaAgI289Cbn762fbYaKFsv4nXGGQD8FJk_13iPIPWBGO0qNV7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8sp1iX0ftyqojAa7_cnR0d8U350fCP-z-DLIQZTeyo-ynMjHnftlv3h0D2SzwiEsojxoIzQu5sFR5ZugkrxVar3x_kxs86kDXGGODxjsJlr9wQjzXPDA8lqTx_20NP38-qahoZH0eUHd9wsCnTgs3ab6Zc40mdqTeU8PEJDdnbIN4Ljg2ULIdKeX8ftJXvbUAVrpu0eZWF09NUoX9tAT6ewsgvI3eXj202A-jGgyy8ZgViayLc4g2SEQEENsUt5VVNg87xsO10OdkEOQGc-wt1BZdE4-ILVyxiKQbcbHfBWysZDAe1Sh7C0zlddu1fnkkj2gbpi6x4TcwYiISj8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMwDJQA1lFhNa8nYd-GzfXduI2RB-X_q0oKP1lhlFQfQArfYsgvRBR-TiY489BH_ASysGsojYKdOsRayCeZ4vImWo1mxN4t9XZ0ojd5ZhEXdhKsBSHSLeTcL88UsmtnhU-WtzKhcFAaqoW604mBjUj9tAcWb2hBVp_jYpdWiHU8yXThE8NqTaj30f_4dRmZQzzg4W1XCFOp1VulqMppk9OKyUOpJ3DJllDbIQn-Mr9BG9-_13A2La73eTZ25_kLVNSqihqSPIGk0MdgX8LWKn-Uinu7ch674omMOiJ45cDCLPW24PdCunO7C50GuOKlJ67iCeEs-4cm7HV-xzn2dMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMrruJ3y8tnDhHhK1LmgIVokqaulelkQWE101QhQRYCR0p_ak8ULgPr94HHHnjMWY5OiaqwrsZ4eRxOYE0Z3E6JQHNIgoKSexDrPHMYhhSMYhsl98b2eoBft3iX44MqX9TFJVvYHQFJI2Ky8c_jcfhn2pyuLSDfLAE07_T5qh7RZz-tDKlKX8sLhM91e_h35Ql8s-T-PfO4RCwP6gBRyEGi4E185WynbGy_Hs8h6BQ6edvXQ0jp5BQ4jJjoZDQAxrjXiVGgQm97SCOPLp5BL39EFyJz5Z1pRf2_exXNVdU_yp6rVsTp_kfe-kiAXmiXvTDJk9JECv1a5QMf3x2uw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g17cI34tjTAAtNg6LEtO3QZLEZdXBQmrfu_DeAnNIYqdppPtACzEZqE--ITpzBchh9hSLwVu7UD_Q1989U_QVLYP0fi3GQDl8WaccJUS0ajZC3ew-J03FppwNNhlzvibaYeOpaD1BdY2YxHQljHSvdgJ1DDl7i58C5VgwwtlZAjXymSCAYABa7Th55aD9Y5TTQpDMs8OfNcx8rsq8z-TVpB2ECTSQSjT-4fl0wgvjfVKraBsuvNIUqCafOvTldLEiXByE-OfzNNC-1mlKOyMzj4iAOiqicRVhlcU_flQDeyqNQlnYhbyQQfSQXM4uyLAnjijcpdlVegvt_iHfw0rCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8hUeG7o9cR16ZJkJzoEhMYim1wKCX1bwEujsSN1t9RAxnK4Ixi4ARlGq1hHehZF8hibSinz_XNZ9y-3DHVPjmErX0tYGkPHjtSEvNnR9uIYU1ob0LMxnbemW3BD47XvhjQX6c2jIU2TjPh7wlN6Yco-fE_aJGGhjliwLIK8szJxhLZVhuji_iMjp82xVmygsk4xWBl-CE5p5ppdQ2gQtvMvgbLrLKw3Qo1DaaFQ5J7VCn3360bf3kvXNrok-qrHLRFoo0RjzZxABieG35kdK5nD2c_FJFACyJGCBRI2Zdd7DQcMZl4xy0mR_AEQDrdpNdenPQLmJVOuBF3fq9Cu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPs1JN0qaX-MQKvw7-hDcrrHgYh3C3jONr9Rvy6hE0tPFRYu51T83sm-kFHcURrYBPnh3-hMxMVDZ4VFHLs1N887jrxSTsTzx0lvXWYB_7WaA3rE555OnmAMtbi5mxdiD0YKm9wPoBjSvhYr-68Z9vJ35VLEqUgU3EMqJpKBuT5d8k62XR7IqaYCbXWk9_VewZoY3CZdLcSooHsHiZHjng8tO44YkPqj-9D6F0aCm6wUB4Mjq-nla88EyaNlFDMI5wZZDWI_T2vSbZtnlFLaoZc1mB8NxTQRROG3UXid93QZu5wn-HCWXQFuVj1xWPj4Uxq0GrJzagKZiPqC7-KpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9VbT3OyjN_i0sgTlvOwrGxzZptPQKYbVGeD5HAIA7qxz7YCMC7qmreLCLF0HcclJo9mERSWzq5C_uH86tys4Hcrze2xZL8Oiqh9IacpSZRDmr0YawAucqydxF4PBnxYjw11uf8nS1TyQWobBraCBtmclTo9uvdzQo7WXPwhhjoeMJGGR4frWWdBfLYKq56-LAWOBxkfuiTe065QlXB0n0Bf8j_Xaei_scUohdP8wbxsvOIgl_V1vJ01s0Xy5fhDfexz4qXwbVTvzsmv2fQ_-RX8k6Xd--zoY1FmlIwrg7KUrY9c70uUDER2vUYbL8anysXsqTdSY0NxqwEG8mk1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqyJ2rBybwy1hA8rnDgZtQs9qNeU_DQ1cTTy5q8fbThMdr32sp3Kfiax68noXFujRdcLZniDQlKOmFd72G2-qelgKd2n7BzzBp77CI_rVlFoF6rcvHd59GNi9L74K4ezul_nKcOVZ8kn4RGCCL7qd58mNF2PkACmQbFUTayso99DcBRDhvlOBPnKVrgnIbXPH-1_18QCkwYG5OkZnOI1a8Rtms4JvHjt2dYpKd42t6myb9gKs5R0zaWjrkvIN6rbElehdRRW7gsgPqBIHK1e-iNXxDZAY4AxBGVLc3KFsoxeFZjC4osYYaE0NT-h43qcBKHq3tbk8zHO6Wc7ZDxdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZTJHf3YJkcbPNJj8VNaNMctii0tWwpBpdPV2RoZl25f4iUOCVkS7fzsMPr4pjAyhLSY9n6AKPyNXAUXM4mXb26wQf5AEw3ED7IBrugfYuBTMTrb3WovFhFJnNFxpIASYAa0U-3XRvu0QkMQJyU2GRKI3VAZFLA9dlhyAIlEXpqx4R1WFoYckH8XZD-wDwQuoSF7aNrGOnPcM0QztDEBgymjL-_iiG4sx8Xvnj7exuiqQRm19Bc-DrzP0szlNf4u-EUBditheBt_KLHiV9Q_uWDL1k_wrFOt51ho1gDfJaoJJk-sJcBeiCEHLOOlf8SjUXZWra9YMfvOUaejamnqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiPuovwBs9z-HA070srYFWxp5lSUdfTBTwZY2qi43EptBxtElBtpwRsEKbqFVzB1VUWcfUJqZoTOm5SGqbMR4_o_ivgaqqJ9QjQT7xYuIj6h5jgFZOLoEg77PsctDSV2RkdxQjyixojDTs9RKNp4-CilbMF3me7zHo1N_gg5_IgHlGUsqIWiVMt2VTfCVg_Auz3tHWnVvAKqJs1fLokqtw2ZVTJ_AYpAaF15EgM1gJ8_hBKt_vgrj5STx3svnfAuDKbH-B9KoUZJWLzmaisR0vnPvK1aZnngu5DTKUw26VrdDrKywvaERalFAD798oU5oTrVPEaRDKWPyWbIW3fHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um_EYNwUm38PC0QWuTmFPlpQ6uj4ooSqIr_FLugmDL47OHYTLyymdLogaLRDad14JTMIcynChhsDRuSTlRYlPwSysaTHAivEneJqv1QAjgTpfFL5xF2FCRsTHEVHCG8FKfi-pLkftG7_o4N7FcyomYFE1bACAfF7w-vQs_qADFAPv1zn0EvnZbQevjVrYTTpyV3ayahLH5cOWTC1j14q4oiHK96E5LiF7aXzX_f8GLNJTX8gVci6G6eAg9dfy1jznAZ3gLAm8IiydLZKHnfBO6dS9SFYxPSHs-0NcOvqyCBGRkj_ogh9TRjAfcUmC8STLTwRxU01unlwOPIVDATcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls_1P_wySArlWWGht1jsb7lYY58QnwWEsuYyQg2tFmrh17T87puLJmhzZc2BQ_KeqlCbnwn0B-fGQReV0tIxJEaOGObR7Atg9BrUNIuLVAFwcTjAhm8ODo8jkPErIhWjRfyqscVFHXZtXKD9rxz4_gKSQ6Bx6fT9wSHbXSDKgQOfBxloGc2V4wSaJEBmSctD7Ms4jvf3uzVa05OmDGg2hSkD-OAL9632U4eqlK9kFxUjus6B24qwkqK6GPwhkw_xJSpvHKXbmXVjeZw5gG2RKpp06vbtS3ydpo7x55mBDa8u0i6DAuwHlwJOGLeGPDYZRujcH9KdVJ9pO3i3nG7OJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyPuY08FLuTSz07guzy1A6k32JtDUcCH83DUUmigmjiGaKeFtoCEA7P4kuutSSPQsgpueTHz2RRPFljZVOfiagA0GCW89TyHDl8iEBakHbkit5FNqy2I0ILeNXXUCJKqa7159yjgaBUmMB_PBYTq9Ftfz6wqTh6IP1I6fPEhN9_Ylr2mQMexa4F-UceJSoJUjS6JGQusd1B5tRLmtQibCBqrjeKSMZlsSA9cXMok0nAIS9WOcYsr3f4xlkAochJ5bsxdoF3rxlhkDXzTzDVoL4j9pwpReFVTCBWBSutCrAIEFROnENv2xhs074EC1qwd_qZWhpiIUQwkT6f7QqG56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK8h2PYEHCb16ee2k2p08lBTCU_petDL1Jj_mn_m7HSzigVrHWOCGb8BMkHCs-bo5IeBodEfQh9YBP4GjUCHVN4g74P_Rb6Egzle6HsdJxVkHDZgbLMDisyxJYppGRrh7bcRngnIpDbY4etDQ7vYOXx6ocsnwkj1cz_5tkVTWpVGeMtNCP2pZ_DzRzWYeU2r6n-YqMFEJkWr0lsVJJy3OVeMXlACtcMWXpU4M40wtzMi2DGQ7qUonaF0roI2vdPiV1oDeeDsHUSsoooSacd2FMQwensfO1YFNYqLkytxlNKMyzPHZwD9mwYE7OQNlNgRIOJ7LRmqwgLuqvIvfA5KeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI3Fp2Rxu3o3bA64lNsYh7EzJxKsdSLc9GHwcD7Ln5xA_32k5VJlLI6OzsNG9sn7hDz76M343SqmHMU_U7ad0fUbVrvgUqLdBUMNu9D4Hh0xaEEX0U5agOL2yZBvmNjl3YLVUyKa42icAQcofU3TxGS5qgqanQQOqq5dGkJJGX3H1N9BncOiZFqAI5yXlVLOuDHnes1vyywNV9l1n-cpzq4xBVVnNugmMLcwjIbQtiinxFTrP6NcVpl56dADYPI_ahUgOW0t1BSQX4J37CQxIuLuSLQY0yr78ke6AaFCsKbz2gDJgT0s2D1IsOrxC5D8x4I3UnT9bOuDhmTILg9o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGrBoD81U66WFVvKGGKv0RxWjU1SU4V39UXnsNpvRd7Ohv7RKHAljQ2-96Bces996SJbwrJOnzBlxjyl75bMP3ML0dJe2-Ibdcr8RLqHGL_jybNdgM2VSfsc6ix9dwZuKfrYF4BODYYCkYJKigsQ5EkQl1fRvFp2yMKrV1bRs5W5HjR_PVtEBAQPpGOeWmSCuflNrEN5yaGPdyx-O5H0_4wXcTovoSqxaeMfI1zBXv2qLYrz24SKsUS8tgMkuTiU_d6SDKzSDJQA1_aQo0HLObTmxu6aIQAca9VkA2UT3avCbaoWh-BmYgEXDu687hHgGw8-WqXaSp9Gr9yuPp6Elw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC7mTdhH0AU5rHhkPEIPqn2QqfP29YB_ktgciJ1EoJiaYz5UGjJ-uUAjAYNmQUMt_R6OmrIFg8zeXFmje20F0kKvkFdjvCOKCiZNTtrVAR9lUddE4ZtFdUUYquZC1xPUrhcVvPlA7AOEfCFCejkcHEbo7yREFQSYFWPckfDhKVogeqymS1fVvEw7yXFV2icg4m6Md3vF0VudV_4kIZIdCE54FzAT9SLpdIuaGl5f2_uMVDYB_1SgC6E3Q561dPN_K75aRFY1-g4nZFVQgPO3kpWhMwhKBMe_pB_n6dBzcY8zO58kFc4QBxD8W0QyFDmZ0uURr5xjA8OtZ34Rujag6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=NrhBaT7i_XNScGm1cgR5mUn_Q-qAbMqEcLjy7HtVYxfSUGYrnmYzYnyGlEhfXf8_yBp_JWxbqFfVEzCArb2oisQIO0eJJWdPYufxHwN1kMu-MCboGtQPBYZEvBQlzjhdpLI6Dj9JDVLQxVeTwlR0twv6lQ5Bu3GGJvCs9Oo7-GhmZj5XWEDDrEI0ShTDWinXTdjqHw3UpL1xndyE0PSDo_kplpc4XJnO5XZaqpOrX3mmEgp24y33Fm6REMN_UjSFFRoKZqHHpsla6zJs44ziVL9h3GlDMJCy9Af4g3IJ8Az8Wy460ZVMRZfy43uioRlqmX3QzDB8ORZLqdRLBfxrIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=NrhBaT7i_XNScGm1cgR5mUn_Q-qAbMqEcLjy7HtVYxfSUGYrnmYzYnyGlEhfXf8_yBp_JWxbqFfVEzCArb2oisQIO0eJJWdPYufxHwN1kMu-MCboGtQPBYZEvBQlzjhdpLI6Dj9JDVLQxVeTwlR0twv6lQ5Bu3GGJvCs9Oo7-GhmZj5XWEDDrEI0ShTDWinXTdjqHw3UpL1xndyE0PSDo_kplpc4XJnO5XZaqpOrX3mmEgp24y33Fm6REMN_UjSFFRoKZqHHpsla6zJs44ziVL9h3GlDMJCy9Af4g3IJ8Az8Wy460ZVMRZfy43uioRlqmX3QzDB8ORZLqdRLBfxrIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=h6LPvK2i6tzLUH1K6ipTmCXK6pJiegFUnSWtNkqduFB-PrW2Xko-_wV_W2dE_BYSsqx2Tnqb2pRXvJsyUOn2TmOoH2SL3SDPXXHPkeBXbA119Jy9D56-IS3qAS_EwNXAi30mnpKK3Ug6byYf_Yq_hegw_9FfeNKhMV319VrSGgxw-wsXVkFbuXIVi8C8a0_Bp4Hb9Dg68STeOfUFM3wMtvOcBkocrt-1kd9fA07bpmwXSclSiTQDEEaVH9oFvobxyygWRoOM-C7T4dkYgbmvcrUIFf3VrOKxfIlE7iUike2sSqXkK--t9wHjNjs5HhsJr_nNuR2QnU0UtQlWcd56Kg9XSlC_j4JLbOcWgvOqt4fXqmN2_VNVuet92KgkI_tg1iudPqvEH2iYdv3wp49lWn_21UA8pJp5zN5BD0NQ-VIiATia9vEf1Z71i8WVeHP_4r-0CIlZGFNfE2LxMCghSNbfC8vsq0wupdmkxs5fWsFotsfxDty_N_-iVYOfEEL15W1n8_Tx4u7EBp9QZpWHN_e9rC2yPxXfulMJczpRdOzE7mKx87W8myst1npE_g6JqtSEQzQWk5Jbz6fPNAbL8o8WW-obB_DjkkC0tHA-gd4Yc7pxZBMLS6IZCLNBWGiywlUPQ0N-hwAPh_IvdzkknRnNxp4POhk7p_GbYrOpueM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=h6LPvK2i6tzLUH1K6ipTmCXK6pJiegFUnSWtNkqduFB-PrW2Xko-_wV_W2dE_BYSsqx2Tnqb2pRXvJsyUOn2TmOoH2SL3SDPXXHPkeBXbA119Jy9D56-IS3qAS_EwNXAi30mnpKK3Ug6byYf_Yq_hegw_9FfeNKhMV319VrSGgxw-wsXVkFbuXIVi8C8a0_Bp4Hb9Dg68STeOfUFM3wMtvOcBkocrt-1kd9fA07bpmwXSclSiTQDEEaVH9oFvobxyygWRoOM-C7T4dkYgbmvcrUIFf3VrOKxfIlE7iUike2sSqXkK--t9wHjNjs5HhsJr_nNuR2QnU0UtQlWcd56Kg9XSlC_j4JLbOcWgvOqt4fXqmN2_VNVuet92KgkI_tg1iudPqvEH2iYdv3wp49lWn_21UA8pJp5zN5BD0NQ-VIiATia9vEf1Z71i8WVeHP_4r-0CIlZGFNfE2LxMCghSNbfC8vsq0wupdmkxs5fWsFotsfxDty_N_-iVYOfEEL15W1n8_Tx4u7EBp9QZpWHN_e9rC2yPxXfulMJczpRdOzE7mKx87W8myst1npE_g6JqtSEQzQWk5Jbz6fPNAbL8o8WW-obB_DjkkC0tHA-gd4Yc7pxZBMLS6IZCLNBWGiywlUPQ0N-hwAPh_IvdzkknRnNxp4POhk7p_GbYrOpueM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7rhwPAlcVqKLgzNSp4S-ThdZGLHgYUZy5KHF-6og33p7xFS5xHFQ5oK17ZvS1aznbis6YTO8Pv-cAtnSNaWD1HE_kRm20NooJlDEiBhsBa28s4Eto9-Qhs35PVJEuVnC0nrEuoHPy6b_zphWpxw29-rL085uee6cSVfLoyznnCOXtXS81JDGt_0us1zYX0bHB-JvZjXQkePvlqLhDByPMpL7dT3pluiksey1i_ger2suwXXALbqK9mDm_NrRr91U7JMVc8DuHh7tA34TqT6LZHVHI-hwGaNBJP6XBQP06o5vF1COUpRwYJuyvq25NcqLFgWihwvj4wRmEAexQJc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1MQdJ4g3-IBDCWCbgdIIkYsnQ0PGPrLQ9F--L8pmUXo5_4LvVDZV5XrRe5d_PA9UpMZh_-dmFp4s5XSbUsyj3zU905h-6H3KwK1R4gIRY9ZUi_MdwoztwJqqaRR52_KbMDSJskG-ZtlieHJg3uc4nXBkFqF1QmvK9YHVFhB2dGsoxh0uqdHJW4cpJ885UmUB0cGuprrggiscYk3NbLzV7T9CRugNbd75MOwz-VuB1fI5nvJrdHNyS_vzV4DDr63bMzdn4M9q6rv5Q_df2hqAeT2TJPxrG0mr1dsg_aNSZXvLPqw4_s1QZU5gZw9EbKzfTpccdAiZucSWkC8ScywdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-M2nxEvJIYEIfq0FeHP9CVeg3SCsSYmEDvGtEeCymlP1nmBSGQ719QE85OPPqkl4ZHjOcnBBqf5INlP_syvJlTUSfENliJDDNPzUUXh3SceA0TYvdWt5QE6hkkODwWUF8dRe7-k4UWYXVg9lj_nR4W2fYAh-PNhCTu9BjpTxxU87mR9YYim8mO006w97Gs6EEpuR7uZeoU6ZLl9iO_czOGpAkU1o4rR0kLmSzq1ldnhr6uj93_KcaMdE12SUHqfl_c5b8i-_xaphJfvpYdVzHx6qK0OW26xZpCp9M2QEn9WSwnRrAlpCVnvwmZrM8B_-qgX0H04Hgqwe6-HZWue3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJnxSmhwOuRMnv0vmAmamafi1Hb1m2FqrZCzE0nkIIicGPVeNjyTb4U5tnakDxkF9xgnEaRcAj7yH7ehDHsRpgiR8BHPhPmN6IABBOwI1xr89hZOgVkMOvZRZjB50ND7fNWhdpGcGw00aeZUwMQLWNPzAGtL6EyZWQd-UIt--mm-piJKWPyQdnkSdL7AmMfYmU2dJ5NTZ1jA4eWMSGp6I-RPxpD_Zp-_3S8gaTZ5U72AJeVCS49hAQtkChVaLL1n8WcmGrcse303EZrgA4yaXqLzzZ6j4QC-8CeKckCJ_oPo1LXPqUwceYcctXI8o93EhoyJOr-HHQHwCROQ4faQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpkEpUBFRFR0FLbkP_wJzAvOkG5DN7v850DfJGjR-ngRbzUCaEhuj_uP3g5hduuqzFqaTaU85YnpI_o6OO9ec40mrY9aUcb-LH5SKUFh7Ktf_ebWOeVRGCbYU2hxZYaQeo-qg-OsPUCBqYvaJIjGm4RWzUPwOdWnXyue8eRRPPCngo87M39GaSr1U8EyW4FELAeF1ZBoG_yQLpbDwUThy7yQNe0MdiER6XH4bSN0EQ1xRJt8J-A2V5gcZlSBiIkpiOlEmQMOYMFonXNCbShP7F3cDIoGvAfJboN0XSxusaPCtShPQE-Bi-ilrYfpd5zITRA4tj0Rkc8RFW6N9T--9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg4E3oh08n8DLbHiZqFRvhUzZrQprDn3twtCiJHgeU7ao32DD8a7-RFP_X3GlM6dX2l6yAaR4_c2Pob9tQ7YJaHdOA1nNRaPSGOQktOb3Vf6tcDXnEWWbvqz-DSqd6RUvb5xycn2Il1aUn_aj73BE9XFpu8p3yzMSCYwolBIM6XZLpBFPVReWYPFviM6VmqiPvf48Qef-G6Gk8RFbcoAO_rw9__3IDhA_cC_Ah12ynwV7OYN9QcDhWo-G4QiBAltLFmktcu33SuZdbORonGTEf0T09F0bOwyLvzwOHO8txcGmMoHm2c_WlFv4J998tKauUpeHpXKiTA1nxEcoEJScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI7IyU1Ing1O5TQSjD9BJuQ0cb7DircRo3IDomkV6nscKUoE4UctNPrJsFT4CeN_IqxVlZyh07R0jGN-H7IUwz44yJdEqcOI9wDiWmvbwxJf4vUHfUEuP1KZnPQzT1ppYBkAr5IAuNlzl_P_1ZyU7rmSstFXi5zX20KhLxzdiiRKqkOQ-ytg2iDrORhN6xb2BeB5rkpQMNh65D55huYWgjhVYU9d7wgTIP88z9wFRMD24YyXe3MMI_Ti--g6L7xvBSLQ4nY8Oy0xNDDLHC6RsjWJLF6hEyiqB0uQS9H0Ox4pYwhoDkdontRlhw79ULrrRzOc6stlIqPiGAY1FF6Qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoJb4CoNdbJTd4Xb9o7YfuBBKNRYHwuXiomL2rRCqnTtJkvsCPp-NUI1c-kC86o89posxecBhChjh5JRxqNGIgJUwpHEea2xv4MXsM0I0hDLwLr3ddnNiwx4ADGefqED-m4IL88vNKDqGFcIXSwL08aSsbDmna7DI0xSiYt5xfxl3MEpZzULq_dmtFIrWB44Kv03u9TCc-tkfgTjFnCkYONdMJGjD25h3ClHEb8lzhYNb2bowIpfMjCVsHfF9OHFfqv-3H-IUTrkXKuR5lC41xfcprn490O36dX2iUG07ZbpTL5UhfkBZ0YkpUhTGgKEb4sfrAdHFTuL5Z-o9Cj6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W45FPma5tNKOFTDhBDhptd6cf1_roG721BdYkzYcmTTVa0r0IwTEAt6xroDd_lC2jcFg48-WMZtefzO8UPjTUTb20B-v3XmPK0ZIycdGa_zNkXFv079lgHhq5CxA_O2t2L8GbnSiX_-Jw_W27NqL7db_de5nfFTOacj4yG_CO06f7vSZACqNTgFvh_WkTpsLl6TzukcNhDm1I3EZcpzRDnH4rlCKEm2yr8VkKPsEjZY6HmjpxfjEvESWWn4-FmQFTTusf7SuSc1xnoiRa29vD3xvoqOZZaF-lGpX1XfZ-CYZ-oTWaiXf8TXO8g7h-ZPiyc4OuvumVIj08lZCkZD6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdmAkkMD42-Nm6nU2U0qGne1SAbJL4qSEjYTQtmtEqC1T7wADVbimGlHeN3Iouq2cxrUqH2Z6B6K0a8LZOFueS1yhLuEicZfrSZtxcmSGQ8l9nAcDRD5micPcfZIN2FQ0webbZ-aA3YjiVt1Mf1nTmUDUvT1Y5337nqQaBTvq35IxHftS0BtsQg5tef4dCmZGhs8R0uoDPNF7LZ2y3BdUIeV8IcIdGKhbMwzVbCZEQu_Yv26uXnCJXqlyuAfxQz6idGzJGZmQwc1BCZOLjcPUbFpHlUgA-ui9NUByKUiRziSjUoYgRQKVVB5lJ7e-SerVrXhcGQHW7sJ8F6w4eChvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viVFv0CQCQqz3o_NoHD5GBEGDr-h_HK0bJb7PHwBqmTSWDZTuz4cnylPf1BoRFoCKPSlg17B-jKPQrYCS2OGnCRfIIeuOan54FK6AIOflPhEFgriJfzxw-gIT6s_hAvE0eiSpya7LES-YwtF6Ym7lgB8OLBCni9go9ACzVMU3Rm91Q1c_goynotOVC7PYX2N05U9GWNKRYfb5G1mSwu63aaH9Vqmswz8u1jvs6jw4umD1ftYJ994uUJe-iPE_ip-P9JqYClz19vLaIb9hjufD6VJ-j9E2nyhhdAoK_FPJsENm8B9E6lJxwKXmyTZGqS4vx2YGvC3lIkA9SpMJ-Pk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heweYF1bLwBgy5QtdChReWknoUdpBmZupvAsD1ZFxurzmwrljNykRbkZ3VWItK3Ao-WH4YsKdsDwc9PqMu4kIDLV8Cc0hTWM3MWNgpda_5U6mS8IasOAeG-rf9Xd3-zMeNtYXKQ231zh_q0JVAMPiM-qsLotbBlJcADAhUBMNibZlpdQl3Byr7BtKEiQayFWK3qsSWp9cJ5UNIWsB4kxSxqBeJSTbj4djxzzOioltsieH4LUcVMRwK_dlf5WAHR1tHpK15dtmNs2Ufz8ssqDuLSS6ouAd8LFHjZGM4vVlGjzmjVzGbbHRQj8vVl10Tf14Doxxt0CeWz3dBOwwCaHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U09V0q-dEJpryxV6w9eob-ifhZ8P6cUE76E8fLkunbfXFKTv70HljuQNyv80fC4OV61lDoy10DTNa7AZS6v1wM_UKS76kjB4z1S5RrZ59KE8muuYk2txxODS0esk3-chGTQRy0W9PP7Cs_HAvgEmtyh3Tti9JkBRqAOn2KSUvXhY2fTltt_HyuTta_F8JV_Xa01HVF8SsBoryaDZrLElTZRYhDKXayqbniEkY0Tcvaxzdll-D4GGJcZCFLS5EEGgG2eNfFhYAhmf8-pFqT177B6l6qNLsmkkHT9EbEZeBZo-nq-Q2lx2q9NvR6aNBKnPdIzSmfwSE5nQCZVQGkEFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=UnS_LzogsRvVrRvB_UPtlUeMTaLomIvKyLyZbwwVT8laZsuUqzk8c1I37kKFmHz_oEYb_la06VJYQPG2vigYmv--Aa-_4oF90nFC3UzvRgoqDAQ2Ojv_MO9TfBy8zyjyWW_NWiR0V6kNoMvt2MqjEGRhZGj8Hux3s9Hg7p6aTPHn3atN7flgMQ0NWEuM5vz4VAE3hX2KiNFRHISOF4Ix-_XXsuLQbRGSHpgeTVWUKMLRKVXllIU-o26gpD4Zp9eRGk9i-QAV4ZwhPACBGXJzxppqL6JBxx0MAPfYxDzfwRL4frKE_rScoekW6HkifTSSAH0oabGCIX9W1tC9577rsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=UnS_LzogsRvVrRvB_UPtlUeMTaLomIvKyLyZbwwVT8laZsuUqzk8c1I37kKFmHz_oEYb_la06VJYQPG2vigYmv--Aa-_4oF90nFC3UzvRgoqDAQ2Ojv_MO9TfBy8zyjyWW_NWiR0V6kNoMvt2MqjEGRhZGj8Hux3s9Hg7p6aTPHn3atN7flgMQ0NWEuM5vz4VAE3hX2KiNFRHISOF4Ix-_XXsuLQbRGSHpgeTVWUKMLRKVXllIU-o26gpD4Zp9eRGk9i-QAV4ZwhPACBGXJzxppqL6JBxx0MAPfYxDzfwRL4frKE_rScoekW6HkifTSSAH0oabGCIX9W1tC9577rsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8AqAlPRZPzlInsIhEJoraGnwgBO4AkfzIELk5EL6yjlCmWPZ_qDtA6RrJfI9jQCfh7Ku51v7At2tFsgiyzSFcln5c7YvdsGL_vJ58A0tPKocUVdtph6y0PUG-jQUXpLfcD8JqU9mZXOsXfcJNEimUk8Bt9umLuIjoN0F11-CHwJjBHj5uCJuHd9Nm1p50t-crl1H3oDKzMZZjA9W_L4DpnRfIAygf9va8FRIG6w-DlpFmQWDXgz_Mqv_U_--HDJYSQx7uWqCqpZHhd5SYcas9zi1V3CAtFGhbYrucsg73z_AmttY4Zu14bFtRc6s8Ko8XPhhfCes0dHncb84nacFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qy6luGSeFSGCqxsFon3l6u8bpihKOk2seChOHReDrvzbZW8DxXIrb7kQlQqe12Bqb9Dzyzc7v5kyl5BGp2KRAYN2YW_gYhHAx6SGc76a2RekBaoB4TKFh6ysJm_nm8vJPnp7t27BVHPX38dgY8GTTxhq7Su2-z8WQzt8jgVlXV9oVZzU9WEVRNlWvuJwCT6Bjuc4H4OPVnOU9sYdEaUtL4ZnPn5vK9_G2qWpqp-ydKJy8u5ivjrvaqPwJTz0Dqti8OB1A-DXeqLa4RJmnTU8NCWmiaeLy0EA6JbuSoaAV6K4JO3jZhS4MgrO3bLWx9xj8VxeB9yqk-MrvOV9HG1kLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAbJ-ggB2wUv_GWiUXrDPvuxGlODE6fzO9z4KynYP2rGfUWDAOQZQDp98yuO6_NefIir1RhcN-LMauY1QkkEqsCL7Q3ySeXNIOPPw1ZqnajGHafdh4QsRCMOR1r0EQ1HfgHj1Zx2Wq21kZxQxjUJKKKZkq4YfSOlpItq3d6exOo7EGH38jXpibwczPYVNhS22q039V5iBTFYh74mu0siost4rwbMOYHuX7J_O_TpZr0WvwO_KY5bImkFYyJvthafOeZEcLgp_NCO0bdUMZCu5glO7WnMEusRtPI00D-FmnmsBaBQJRVjOZwdgu3ANr4BRe0kTvHxJdKuZhwCdK9_ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzR1umPymxo3YQ3L8xykU2SUigBeBkDoxEEE7D_nwHG0mAAgOuAo68TpEW-ZhX0zS8x5qbmnULzskkhHoPu8kk9vJG1wUwiN_hMnMSx_AnDNflhsfUt3wPiLHC40w2uwsYflZhjjtVAAMbg_b2nz0WBOZkcvfzJzKgEEkGlSyjvuqyqqO50RwxXy6-SVGeau7QzJK4vLvSzGUbECeAN1toCIbiO6KUPbcLYVi6EKbdjwN9n17AfWRzKJm0oTsSHZG_Si58s4NrPQFGUOjICxpqyS2yT4CBV-V5BYEIm6KzYMLHs7zMlE1pCPA7ExFC3QRclwx_ikMt-qC_9-rnag5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgcUS-LBBgGAsl5ImT3szN0RQoMW-uaTwPTw3j8j22cbfvwbtHgyCDA9D6KyPD_JtdfRdRlxrnbTouQm6uINxXBBrTuQ9o4lPvxkMte8HECOL_ho5SbKH-xwD6kQHscgNPReEiOftIFw1JaJYghnV5PxkMLRvOMS3YVn4VutRM9QwqcOX5iGyOtPNcUJfOkdTdDt0lh8-kekZjNaxySSNJcQNSdBK8UtTc5EPEK1TGhXsJA5nmiG4wMSmG3qSMflQwL_GJ1fFduVk_947LaYmfvphO1W0UJrkQccTe3bspcoRvY5US5jTPXQH7bZR6d22f3-N-JmaAWFo5PCvWdPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6O8tq8DJWWGUv-vxRmzYcZzMSbxr6_A-2rOHxHK7JdM-6W_R8wvChNpLR9IhwkXAcEGZgr7dVH4hPVTDNDs22wtL7YpgbRaA2NsSOk4XGJaOA9cTOgJN-I2WHEth2QI6fvyCDaAaqXmq1_jyetSUjcgn0CLr8OgO0cVtJWvQlnIuEFk0X0UwGHp4n7Zgq7Zj5vYfQFFl8SaRFoS8p6NnY8P2zKdOghpatDegi6YFwktSKni0ZRuSwFsK1My2hRjTwd-Z9XCfaGuxPs4y5myY495mACOP-k3x_yemqnoWIHSqmddOwdEJxo8_F9tdykE26E21EuTi3kb0pzj-JJnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=nSyDi0ehb4chXL2CwWgZjR7QCiCtarDW3esHcuxxgMIHZ_g9j3yy7lD5ynYNPeoAdZY5t0gd03MZaLpFQxg0RhSY277HD0RuTF1Gmhnh7Wjn1bdV4CRX-QAIzYSs-Pe8n3x6QYNcYOgntCrYGbeAfsfdD9BdcfL2b1sZeR-1jTe0tqb1f-9iRVAY3TE6UOv_ch91T_EycflD37gkyJykqUIPSm_NXwbIZwYahVQJiPrs13RaSKmL6zUM4l4AH1o0EYld35i7S56sfOLceYRj8v4iIhdid4zK_CIEZdXv0OCluOcGs_UmXrwk9ZOnzdVt-ReQwtkkAxYdGZ3Wsdv4d5fotSJFTVU3ICM6DyDP4ldXqREFXvemt2pJXbDkoC-RH3ZVSjEo6S2haI44JG3X7Me8ex-55N7ywphzpUzJy11FTWAfpQKza7KXjTI_9rCLo2ehdacvSSIcr2oeSreU6Tyk5VcpqSexDfznrK-vn4tAsAe2fkpwlwwhblRRqZp_7IzhZnPtxt3PDgs7jSyHCzPjMBYuQO8RW0kEgqoiFKWjZwrJDhhXVRoTQct0EF9o1bWP8u2Ypipt59dmkB4LR3yAZOkZBuiIJMRyAZP_agQ9V-yD2Fnj8hdPbfX4tZ8fdxVSBBOTNwerBUvmnn1hxDWlc8JAFgUfH6BvQDOfXm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=nSyDi0ehb4chXL2CwWgZjR7QCiCtarDW3esHcuxxgMIHZ_g9j3yy7lD5ynYNPeoAdZY5t0gd03MZaLpFQxg0RhSY277HD0RuTF1Gmhnh7Wjn1bdV4CRX-QAIzYSs-Pe8n3x6QYNcYOgntCrYGbeAfsfdD9BdcfL2b1sZeR-1jTe0tqb1f-9iRVAY3TE6UOv_ch91T_EycflD37gkyJykqUIPSm_NXwbIZwYahVQJiPrs13RaSKmL6zUM4l4AH1o0EYld35i7S56sfOLceYRj8v4iIhdid4zK_CIEZdXv0OCluOcGs_UmXrwk9ZOnzdVt-ReQwtkkAxYdGZ3Wsdv4d5fotSJFTVU3ICM6DyDP4ldXqREFXvemt2pJXbDkoC-RH3ZVSjEo6S2haI44JG3X7Me8ex-55N7ywphzpUzJy11FTWAfpQKza7KXjTI_9rCLo2ehdacvSSIcr2oeSreU6Tyk5VcpqSexDfznrK-vn4tAsAe2fkpwlwwhblRRqZp_7IzhZnPtxt3PDgs7jSyHCzPjMBYuQO8RW0kEgqoiFKWjZwrJDhhXVRoTQct0EF9o1bWP8u2Ypipt59dmkB4LR3yAZOkZBuiIJMRyAZP_agQ9V-yD2Fnj8hdPbfX4tZ8fdxVSBBOTNwerBUvmnn1hxDWlc8JAFgUfH6BvQDOfXm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkmiZX-oNRRF6eGeRqSqKxzhrT-dzE_yOwMFOO1ajjPPbE9Z136LDVQ3x9xS99iqKllAbjrL3_dZlAFTOX3cLp3RuGuE-6swzPPUNSNhMyNE6Folkwdxu20pEBQysj2OeOkCdgklPwoR-1drOAMBSdn7RShRrorPr6py301gfG216TTWDIBe-et95FgqdR5XyksT-13PIalyQ1UrcTzMzlr0cQJE8C6SVYVdqG7u25JM38LgDULbKhE0PubG6j8nbmqm16ja7WJx3NAvZk0K6mMCaWvjEU6qmsOzDyDQfGX7nFhmlISjHoLQ5sLtbXVqMN9O_jEFvQiUy_fGY6Xdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=FueR-jKHaCA4h1_9JGuyPyiY5EHhmax93POklGc7YaCKOiT8jqvbK9RD1W0S0Quj2m0NHCF_Xejeaw9shZqXDBAv8-5T03wtOD_YWjkDtYYYxdtWeM0JnR7hy-kZdQM9wkAt7qccbTHGoyP500yGQDE_2v4RiFeYw4Ud0X_c_5dobjU56NpbvYMfZp3OWy_yVbR5UXAAQdOEe6c1v-q6AORP5xy7NoS_iiPRic-_SG-Mh9vchbTc9NC_78mz1Fpsh5AvLLpc-Y_C9Ah-u675b3O1Hboa8ubcqOLxRNCgJdbaQ9h6n8kfpDBgyeDctMKucY5sm224PV166e_TMUofUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=FueR-jKHaCA4h1_9JGuyPyiY5EHhmax93POklGc7YaCKOiT8jqvbK9RD1W0S0Quj2m0NHCF_Xejeaw9shZqXDBAv8-5T03wtOD_YWjkDtYYYxdtWeM0JnR7hy-kZdQM9wkAt7qccbTHGoyP500yGQDE_2v4RiFeYw4Ud0X_c_5dobjU56NpbvYMfZp3OWy_yVbR5UXAAQdOEe6c1v-q6AORP5xy7NoS_iiPRic-_SG-Mh9vchbTc9NC_78mz1Fpsh5AvLLpc-Y_C9Ah-u675b3O1Hboa8ubcqOLxRNCgJdbaQ9h6n8kfpDBgyeDctMKucY5sm224PV166e_TMUofUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asoP4Fyec3ONg2atxv-VXstd7HxFZWdEi4rewJ2gfx8Uz1CtH_IfIdWdaF1_sjJhm4AqYEdirzXDGjFq4r3BSC9TMd1cgclmApx4NvqF9GWRKHdfs8w_ytRLmxF8yq6guID286vuiCitan2Q3C-dXnSyVgUb4scIFJ72PNuedQGKtj3qGXsEDk87vE2mvneh_XhAsoVuY9zOW8Xf91fNOY9Zxbkj8pqsqAnuwTeumtm3gCC4PXAlbLf4hulELKFnSZdBvbXArm8SKOfaNPGEDhj7lqPrVizL0tdO99hdYMRGLZgWURDLfa0UFJPhtQDpHul693ig4nfiwOaJrufdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0_B0Ds21Ecmq9yctL370YNPLmGWoZkDC9_ypT0EwDzIUAJyNOc3dJUBqQesk5KHPLFY7511k_wXwjQO4ajsx5w8f0c3_2mcZci2OaG5BjWNNvbXXmJJhkQgOBANJ3qEqsAKVzDmfEj39Tm488j97drc437yf96NG0V6PfZPwn8ZFEfsFlbz1oH4d2_p85zFXOx8IRR8oWbT2-JjrIWdbx4G1_8MELNkSoFEBwc1DlFGa5rt--6ws5_daVb29JimcY5tTj8YicIrQ1cJ7n6sJxESgxpCDVMdQhLBADjNQHRqkfoKt4DgcP66BO-7cqb6_gxImGNvqkwuFvii4UXIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBDE6EFRkYeuSqjyHCR191Y-5de2UZXHBSWbxTFsnRaj_7U0OhqsDreycmVpDFoY2qiRxeGBdI92RRqu4Pz4bPY6nJFds9thpL1LU84UmADb3-nZPGTQEJUK6FQ-JqbKEG6j4C3ug2LGxESChvUMGQ62UHjYQJfO2iogFNFxZJuh85-qsPZ3zWXoJJwfUSqH1EmM97SWeQs5-CWlsAkues1RmyeIOgmu5R7CDeYlp2VBmyre0cDLzguGtBTfWq2MBT2IuGRSmonY5hFO5ZWYLRpKwsTnpfBJ92amCxWGvZwEEhTaK0xVj4xtMlKa7WAbE97xJa8sS18jyUxnRmb1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1SinzirywVWB-UQnipaLBJZleOEbhxLBp5s9HNy6GCwSdrA0TzbUKP7lDOVuNFU5uREc5tWxaXfTYqirdbsn1xRGMfiqt1C1Sy5mvqjo_1KBzR3lH8BNYwu085UgkorIny73oFM9DVjG5yzNZ9q7Db9YDyPb94itBhqdZ4_NHZhtWXYy1OepCWaopaTG1fdoO14MIM0WOGmz63CLVPD1MHr_-mvlrTQ_hXR6yLOQv8rVbKnBUZlWey_6ZCTOtwfPXx-DiQbDdsG0rPlXJkSNXimDWUMUDpYg4l_phrJNEwPcl0ZC1BeNN6hjG6QNIEE4A3xYwqKe3O48fxCPL-HKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfNyDoUhLEFQnksAFghWcCmvnrHsrWkLteL8RBO3QfEUWFHuKIf1hY7nZZ79rrgR6sbAfEZokUbVRxm5OENG7_HDoPTQa5QLFmidTcEjtloa_HrQEDD2kbDUxEscmgH1va0tldl-ymToWQ_ZZjPlXSPyC0A_IKiwmYkA234Ci1Ox6EPgZ_3W322vkv-ixtf6aElMIx_hsffH-0zMsAJCQ0we9YyKr7Ce9xRD63OTxAe_1frECaKYcA--Nb_xsDY8mcGU1JjnzXN0yZNWPxPglfP5p4KRZBR1Ic9p5i4hdXEzRx7M9mkCyv8tuS2rB5HMXT5gGzcYFpo-ZfaHXH4wRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trf6Ir5Enignzh8y7lhky-dAug4HzihG-wstTaCgYw1JD8LDaFozSPTcmV3N6ufH9kQbt7aoPtqxiuF5HystNdCN73bnf_7tdwCDehLjlP3YVM0RtOwiH85bHXxiDK-07OaVZHuWZ9UThbZHLP4pIpshX0cqHGMVdAiXv_Br3oxAr-PF7MmxLN_yrRR5WzMSAdRch34UFn-EHfzt95WP898uyoznLzKWlPr9-zuDz_-lybffrl4-pZoATRaz0Aqxq7FeHcfTOtx-SaJQ9-aQDvMr6zbFBgA8Sb1PY3ZB6ATo3D1iHt6b-kYNw_q8rM8JiXE0LswSo1BVZYmLxP3_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=a8nrwCAP8IejmjsMeKipzZw97lBFDh5kFjmHuE1iVO-vDjFsR0PNcoPS1ZLh6m1Bmikifbf06RNLve7XSaSRVGEgeHMTcAUvXogw-1daO1yMKCsCBFORVE0ohHjrPNOLiMdJr678KemXIQw0vDBkg2UABWzJG1ELOBkJ938RiclGLcQbOIIBzqwrFYSJusSV7Bl1kiQPWnSbS-mATP4tOpvkn1MbHQhXIDSmhCWgOC_8oW3LNc_xdOKXEpVUWmVfouciQ8ORAgRjUY6N9tAad8I12g6CQQB2x7w4XBPlWhwPU7f0Wc3Iqi31ySsoxdCwtqkrbSpwkkDaXkrE4jLkCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=a8nrwCAP8IejmjsMeKipzZw97lBFDh5kFjmHuE1iVO-vDjFsR0PNcoPS1ZLh6m1Bmikifbf06RNLve7XSaSRVGEgeHMTcAUvXogw-1daO1yMKCsCBFORVE0ohHjrPNOLiMdJr678KemXIQw0vDBkg2UABWzJG1ELOBkJ938RiclGLcQbOIIBzqwrFYSJusSV7Bl1kiQPWnSbS-mATP4tOpvkn1MbHQhXIDSmhCWgOC_8oW3LNc_xdOKXEpVUWmVfouciQ8ORAgRjUY6N9tAad8I12g6CQQB2x7w4XBPlWhwPU7f0Wc3Iqi31ySsoxdCwtqkrbSpwkkDaXkrE4jLkCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV1uEfHwD3oK_t7MGGXQVwYt9kSx-_Yce5FntigZ3mVDsk5NR9UpbykiTvFHjZlZ1hx6P-gJsIbrs3TpYZn11l860F6VShoUmea088QBqMM5lRbSwVUZknfSphgYGjXaI4VSGBOkW1XeKj6AHElCi-fANOo24apLGhExr8BAkwQ6s6OjrgwZSNVi7F3oors-KBmDzVfX80DAaV8Iw-t4FI95i8HFY32FC3InH-J3rOr3TrjOUJpa_EcKIMFHs2BMmkVdBgL53lQnLtn808iTLKN9yemkPWmzXtR7fGWkccu1k88PCGIooW2pp1I_IJ2WrPVUJAMfEecDsm1M-1juFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktFbugvSRLnBYsEQIkbNzPX16NtEHEZYjAFg4mQD6FgVXjgCMBAmQU-xl_muakQ5hauhs6aEcKN_ncCZVNWFTBzeDb3VfRF-rhpVd1laFpmepYJyMK9ttC_UgWIL1YqAEEg8bIk4q1e2qYloii19SpLwt0S9QWKPOQr1cCSzxkwGFJ-HB--jhw1mbFOaaMLvODiVhXVb5k4PQZeB7kZgQO7evEvLGzgJwVUwxFfX06_WQpqykjYcWKQaQvvGV8dx11uYXpxWlrk_0M7BwIlzlIlQUeIWpvwM2DfiPs2AcWTDhjtA7l0176oCb575SYtymmW-zSgTBaH_FoIOeYoWnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=VoJPT2xZjPbJ2yLzuWFFr8V9HD9aMmBFQwLjvfyzerBd0EdsOudA4eR8umLVe8BYj6q1dKO-9jgGvQR-f6GznGgZvTU47ccEXk8E3UdGdmHvX4G6TIMjsi9lbhyUiAeXEDHiT-TmijNDMW8XnoILsm0w7kvP1-Wh9b9MoXPcxBm5bqHN223xdTzSsQEvW3rVSPHQNi5bLZunDfKjkQ29sQ2AR0o06pRyX2-QyAPn5vqm4dEWKSx9awBf3ZLJFgKs0HIvShGXiBbc9vC5bmatCPihjfdFNyg7bGHDDBpzo5UOwtmUqBEasDIyQeXjzwCn5yG7_K6qfqPY7iGJ-a1upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=VoJPT2xZjPbJ2yLzuWFFr8V9HD9aMmBFQwLjvfyzerBd0EdsOudA4eR8umLVe8BYj6q1dKO-9jgGvQR-f6GznGgZvTU47ccEXk8E3UdGdmHvX4G6TIMjsi9lbhyUiAeXEDHiT-TmijNDMW8XnoILsm0w7kvP1-Wh9b9MoXPcxBm5bqHN223xdTzSsQEvW3rVSPHQNi5bLZunDfKjkQ29sQ2AR0o06pRyX2-QyAPn5vqm4dEWKSx9awBf3ZLJFgKs0HIvShGXiBbc9vC5bmatCPihjfdFNyg7bGHDDBpzo5UOwtmUqBEasDIyQeXjzwCn5yG7_K6qfqPY7iGJ-a1upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=lDYWZCNPmbMfqLE-hSc6m6MrEJI4mLA84wT8OBWTpY4a49xO8Id2PJyd0nWjETEQPKxhzIR8JkLn2M0V2WPey0be0h6wtWrCKDwleo0sRn1I3RidKQgZe_kq4jHKmuKS5wAhw-5tyYbCqTdyh7pzWEJcDglVbEeYt1SrGjjnNDxfwUwZAAdV_2hlUU4yLa3t0LqUqqqL3RwySYFSthjQotUmG2Tkve5IbNleoiOWwZb0tYMx_0Mz2wFoBs2xTLxxDNOx9DzCnP1zHAQXpf5AsHjLmPcu4pVxR_gASRJvVwN_q4FgbH4w4z59lpJj3q2bRxw3v4u7_AGQ9HcJaODl8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=lDYWZCNPmbMfqLE-hSc6m6MrEJI4mLA84wT8OBWTpY4a49xO8Id2PJyd0nWjETEQPKxhzIR8JkLn2M0V2WPey0be0h6wtWrCKDwleo0sRn1I3RidKQgZe_kq4jHKmuKS5wAhw-5tyYbCqTdyh7pzWEJcDglVbEeYt1SrGjjnNDxfwUwZAAdV_2hlUU4yLa3t0LqUqqqL3RwySYFSthjQotUmG2Tkve5IbNleoiOWwZb0tYMx_0Mz2wFoBs2xTLxxDNOx9DzCnP1zHAQXpf5AsHjLmPcu4pVxR_gASRJvVwN_q4FgbH4w4z59lpJj3q2bRxw3v4u7_AGQ9HcJaODl8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=Gkd6cl_fzCrPLg4tQLv3T-mcK6tH-1M9StqN_FxDPO9ifAzJXdT-iXDntJJyHXUHZFHdF0RooBNVy7gMwkvkyFhwxvolbeH86CrsRn1OsJY9-VRKPoZ7spIHe-xn1lSsmOL4Aa5umVzT6szR4B8Jo14TW7vyAbUwQqUjJLN9b3POsyCvYdEvfGO7_ZUenpCOCuCPJAgHgiEeyUZ31gcHV5iK_L-175XIEAtqS0AVTh0eZtLHw8bnGsW-RrmqYC_OUzVF7IwvXTB_hnym8MMgxnw-kAt4A3UcB2F0NXsiCWbLouM0g0bNIox0Jn_arscuwJWjk08fHaW0o8Rzhv_t2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=Gkd6cl_fzCrPLg4tQLv3T-mcK6tH-1M9StqN_FxDPO9ifAzJXdT-iXDntJJyHXUHZFHdF0RooBNVy7gMwkvkyFhwxvolbeH86CrsRn1OsJY9-VRKPoZ7spIHe-xn1lSsmOL4Aa5umVzT6szR4B8Jo14TW7vyAbUwQqUjJLN9b3POsyCvYdEvfGO7_ZUenpCOCuCPJAgHgiEeyUZ31gcHV5iK_L-175XIEAtqS0AVTh0eZtLHw8bnGsW-RrmqYC_OUzVF7IwvXTB_hnym8MMgxnw-kAt4A3UcB2F0NXsiCWbLouM0g0bNIox0Jn_arscuwJWjk08fHaW0o8Rzhv_t2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8lfCx9ZwNhBbDAX-iWEMDPHRJYr0yssB3WbtiL3eTrjJR4gRllJwF3L4gE5ba26s7eIBCaKqiDbxc9FJJ2FC_Bwd_p3mr6WfR307p9b223IBY-Ta5lnUh3HrVXg_F8PYcQJ_Al_LPaYgqXJuSrSQUcXAJOUcI_26BtuYPevZRpep8-8cCERy-a8VRzavNtx0THy5zshdM8xLAasXm7TLgZOjrOEQfnadQ6lZ2QgnLxMzsNhCTC_mdKS3Hb5NEQaled8MJLCt0xIZ5OV5LA4zVYfaQV5Lf97_khsbGYnBU0jN-qja9lZfgae02EEQSRmEWEkn2thukRhb68tdytbfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooSB9aL9gWIjwkLCFMNRN1MAlHaiFPNw_JjMdbp_YpYZcBQPgcYNnqV8ccAnsosQjYnmAW_sKLTwYdT1N0MLQgiMvU0q598yFSjzXL6doShb8veri12fHNpaNF1X4bKM_Ud6W09LqRbM2hOjRzi-pgLnyzrCxZEd86iVcBaen55YOD-Y9X674fjG0CvY9QBuN64mg8veIZxaUKNzhbHu79kc25SJmxianLDnzqmeJEVCx-3g_shu7XPV4iit0MLWwu-yV4TnSRtDjFuqZkG11b0JQk5QQZRDcfqCZm8r9eXHZjVeipc5O5GzuWf-VQUhal7dGNDD-Q449n6r9Atbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTeIAYFNFcZW93e-6HGAtg1v96vHJQzgKdHat6RxUYDJ9ryGXSwwfftbblba1OXwIUUdvwb2ohWOGSOwfF8ymyOmZlhMIDlnOWfEu2ak_6TemodtRfp91Yp4WsLiSrhhcNvqFqpwkuW8bM9IsH43fyWIjg4V3_0mLoN1YUu3SoJrba3Umh2FiqQ1zKwGEAqU24eQWwY3e4LhqDm3wYDUdscUNzXTMIIewNWMzLoKwSAlwnv2D9lzmRkQaaovmDkwUn76UvVe1jIdKZ1wL40ey5Zt0tPh4zbn9MaabVGyCfNF49iU41jC9NO0TRmntiWdhe2ydLvmezx4bhCjWUTbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMz2EWM0rdWVssh1wmFrA8rasxKx7DldW-C_IjARbOLbOQeosB3jFlQGwkoWtVdTbXerrX3JheIk8SiibXtVvN1c0HTNkrRyYxn9hbVzrNAX3uK4RJS-dz_NdYlCVNXgmT66DzFOEiejy246kZdPb_-79NGllLv-QZmJhq-DCUfhGW4ft5WUQU5bPThEbqKGHS72UBOcJjPlHZDm4VvVELK41Y1pXl2Rh4MD_f89UcoWD38JZuCVapnNp6DKLsj5nb1cUCpoevA-Z88Pfc_YdyUbv6dvctchpNyLhelmN3P-ddMIs_g6-IDIWJb3htxMDjKeVQyHarJHsIi6JKJq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jtn1rwMGX3cZ5oV1tY_-LdCoBnW4Sd8tRO7kltYgSNsS2D2h4K-c6R4zX5GszZ5xnsNj2bzIwdOvw8U8Cvxyrxjt6fn8YLu8nulX_RlsRGjkEMum55rcV2ZKbT5fGUnhODC5T2sQYj8Yrq3HOj0ZVPRhTtZ5ASDBi4pQGh74MMUodQI7XHhzhY5GkpkIxWKTBaTuCQl09Ty6pJnVsxl960uP5wKq30V_zd-5rxKqtD0G329B7zItxNUVLJtN7X8IetVzSkk46pPCkhcwk_s9ORcodtJAajFeLez3K_NgP9lvfLux5YiAhpMyeyYRtgyXBvTM5X2RQTEXQ9y1GXAOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uztA8iZohUMPY1o76PerhpJzzraDrKCMkbfPIEmk2f5F_lHmob9U8JkbSJpECj7n1WAGBtiLM_Y4na_4zGtwGRcmQRuPsKvNtQ81aseVpfmxGjWHbyq_uYfnjNOc9kAfjUvGTt_0e_iqJOTTAQFXVLFWQF0T7DZdls31Zqr38UpYehuMkgbz6AIo0RE7fyWgYoxAHVdFHYNZ88GzYzKs0t21Rd2aUAjvsKFIWM9zpBlXu6TADDGEdQ4tsFTfVREVVlP8lfOddKpljk3sV62M51lklOS35-dmo0WxDi6KylFZq9KDMgv2PECXnmd9_I0tx-4j6K-OBNGQy7tl3iWT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wyhfwd8nFPzM8e-8No_jejCUg4cJ2FIUDH1kYvzTl-8LMBBMLEXuhA0v2LFIwYbCh0OvcThNN4gAty_30JP54JkwkJZ3wCz0-nDPOPW5iaSRT7l2Ok-ujFP-1jVrj_Q_BscqdUFREC54QlKf3Cb87khj8PFW91RfB7oFEpjrOIjbC81CWybGIiOtHoWS0NwAccGYX1lR3BEXGXLCH5LwSw2GQJZ65Qh3zuWKRlE_924O5weuKatD9WUe3oF8kMrrOybqEngqgaDt1xTKQ6DPYhPLfIMgj_SlMhWbc9wVnbSDAW0jRnLSwlYwbYlMv3l4bw8txNwRgTRIv12XmTymDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=GryISnWQ_XDF_hT2ebzTXhQcBJ_u7GENlppxXAv7Yi0ub43YHOy5kCHEPm_ftoIQLX5eaO-Tcp0JJVnk4nQrHHxeK7oMp0NOzpDED9ACZO9gIvyvfP-hqo86D7rfTYwznc0MdIjp43jiOXrGG-k5AVPBI91wWdXJi6CmgrSdcK4f_XCPLgxa1ak1g5fYLwqtFNbafDYWrPsFQecZFb2o8PvjuNKWRWqNa3-1R6OMpuRC_8sGqSK5NhxmMLBDzUrkpzhaV-Z31GhvHIYhjxkMpR24gr8V2EOY2aPmE2Y-m7l4BT7pGoKbxFckUObRaYRO-1AL3ynuQZGHKwHlduoSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=GryISnWQ_XDF_hT2ebzTXhQcBJ_u7GENlppxXAv7Yi0ub43YHOy5kCHEPm_ftoIQLX5eaO-Tcp0JJVnk4nQrHHxeK7oMp0NOzpDED9ACZO9gIvyvfP-hqo86D7rfTYwznc0MdIjp43jiOXrGG-k5AVPBI91wWdXJi6CmgrSdcK4f_XCPLgxa1ak1g5fYLwqtFNbafDYWrPsFQecZFb2o8PvjuNKWRWqNa3-1R6OMpuRC_8sGqSK5NhxmMLBDzUrkpzhaV-Z31GhvHIYhjxkMpR24gr8V2EOY2aPmE2Y-m7l4BT7pGoKbxFckUObRaYRO-1AL3ynuQZGHKwHlduoSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tog4e3JzgAFNMm6tbzh4wYlpwo9pMMeWFWp6AFpPazquO7wWrlWSFj_lbxZAMl9OIbjDdhxiTrxIbXPHTIb-NoMxSS8jt6faauqySXcF97uLpbTuDjCDrTBjS7nj72cp6pXtnizF0uf1FgczKcj68a0FF0UzAEo3BlRkFL3vDxfqZk8wRFPaZ92jnWPwvaokO2_QpsR3iwkpFUsao2NZE8c6DQs4jq0iA18jUdZZoD2U1tdNG58Mm_LO4pLIkBl6qooz4OZamIX9mjA26quL3EbQvQXqmTUSefr3Yj_Cy0Scy1RVD1D9oA9gqxsrt9RriDVWg_PmOGQB18F2miV2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKImBdwh3D4I50e-bCQI2-GjcVUSkmTdUr1xq0eXNkZkPkp4m3evU0nYLNHUs9J9RjJv03PAl62XEXoSKkYaCx-eRLQYPVEeSLfSTHTp4O_DjiINDkh6H4AA1KQsG3657kcgaRsqCGpPmsRDgRRVu9im_Wx3ym-vwI0xq2sCvoOjwNuB-kSrHBw1Rt2aY__hBfFzx43kaEtNj-jjb5V6OefPkNeFOeF6HgtgY0GVVtgZUM6RR8_VUNisYH_mbBNs_gZGnfWT1GvKQpHD7Ib3KSA2Fr83TB35NY1QUYNQihO84WK2r5IdSMK5Hr4bf4Fxhhlo1xvCb0f7NPQ_q6ttKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=DZgoeYIPyCJha1B3CQBEuc_05TMISR7-Qp8NEpSzUHJzfpEOFnMWyzTXPVFfxx0OTqvP8quFV78ysLjbs8FlYntyXIXlDMK1Ob-wUjIgHHcGldEmVM7lLRKPOsVpbiWbxHaphXecyck6pkPvjWUuSKUiUYvNMaOO16Za9yf3Xa_HVGTuvUd0HQE0uoP6PNbB57j-cdq2DKp8w3ISyaXYsfHocLUbTJ_ZLuM-5VZMAHKbld6FOYn1BjL5GBwQl9oUKyR5XwAIHjDA4_jeFpyKReqTW0M0CxY08kVCBjr-3HoatkvU6L0GddtkngJKezoFRPj8Da9YcilLtqFnvK-HlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=DZgoeYIPyCJha1B3CQBEuc_05TMISR7-Qp8NEpSzUHJzfpEOFnMWyzTXPVFfxx0OTqvP8quFV78ysLjbs8FlYntyXIXlDMK1Ob-wUjIgHHcGldEmVM7lLRKPOsVpbiWbxHaphXecyck6pkPvjWUuSKUiUYvNMaOO16Za9yf3Xa_HVGTuvUd0HQE0uoP6PNbB57j-cdq2DKp8w3ISyaXYsfHocLUbTJ_ZLuM-5VZMAHKbld6FOYn1BjL5GBwQl9oUKyR5XwAIHjDA4_jeFpyKReqTW0M0CxY08kVCBjr-3HoatkvU6L0GddtkngJKezoFRPj8Da9YcilLtqFnvK-HlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=sAMGpx5fa5MHmJ5RUtaIR2vyshkZ3IZHYk6net-oYT9BeSwyW4qH3Eqa3MZWITzqtjF_U_XVUN_xgHkP9OLfV8cdwn856PkGpfF7V0eYNV2IWcB0vd2Gg96oYQ5sDd49_x3ghBnr50NSjIyOKUq1lCghUYhYsA16Kem8Igqzs-k1CqsHpbdBF3sqnWojoliYkPec9dVVujJ-yO5xFQ65chCsHD3y12uh6cHGV1SkSSDtw_B8ScVDIsc9Fi85GT_tpm-hOW_oH_7sXg0rc3mn6gpI1RJkNRhs49l9HKidCs1HGkJCuhq9vjcAdfqtGhPtkBFoIJ7bnkAX4pRiDeqSoh0lRiuqeJjYhGLyR2TKL6AeBLssvn4wibdBl5JhGuFq6L4lQHjdF4KibF0DmpWIgurNQnswSrHY0QKlL3rDOyatiiI7RvCiVhbbxvpbvbkue0KnUYjjy5VBp4A6RLf8ynR8zVyDvvMSWVWtRGw8os87w-SosqOc-l_jMI3_yS7gcvC_otJTSH5cc9YWJLIOr9nFR6CuzsS7Pea_IE9KTs3BOIfyTuh3lN5r0sORn5uA1kR5mOkExnetYWivbwxq_2Tq12ew3GwL_bSYbFoRYMtfAEDHoLegpT5yp9cyijFAPYs0RMsyJrDWDIBBqfPLQrlkS4ReYgXulkC2kDn6FXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=sAMGpx5fa5MHmJ5RUtaIR2vyshkZ3IZHYk6net-oYT9BeSwyW4qH3Eqa3MZWITzqtjF_U_XVUN_xgHkP9OLfV8cdwn856PkGpfF7V0eYNV2IWcB0vd2Gg96oYQ5sDd49_x3ghBnr50NSjIyOKUq1lCghUYhYsA16Kem8Igqzs-k1CqsHpbdBF3sqnWojoliYkPec9dVVujJ-yO5xFQ65chCsHD3y12uh6cHGV1SkSSDtw_B8ScVDIsc9Fi85GT_tpm-hOW_oH_7sXg0rc3mn6gpI1RJkNRhs49l9HKidCs1HGkJCuhq9vjcAdfqtGhPtkBFoIJ7bnkAX4pRiDeqSoh0lRiuqeJjYhGLyR2TKL6AeBLssvn4wibdBl5JhGuFq6L4lQHjdF4KibF0DmpWIgurNQnswSrHY0QKlL3rDOyatiiI7RvCiVhbbxvpbvbkue0KnUYjjy5VBp4A6RLf8ynR8zVyDvvMSWVWtRGw8os87w-SosqOc-l_jMI3_yS7gcvC_otJTSH5cc9YWJLIOr9nFR6CuzsS7Pea_IE9KTs3BOIfyTuh3lN5r0sORn5uA1kR5mOkExnetYWivbwxq_2Tq12ew3GwL_bSYbFoRYMtfAEDHoLegpT5yp9cyijFAPYs0RMsyJrDWDIBBqfPLQrlkS4ReYgXulkC2kDn6FXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7U3VX9Uw5Sd9QmLAdLuG-DpPjNXqY5PvSp5bQZk6xdnuR1eIvX4rEjA0kiXNJhbR20k565czgOghUv8zis-R8OXtL-T5xI2x4AIk7gENyHeUkJNnfFedZH4Do5Rv7KZtWALJhN_Yx-qjcjwuivfIQl4vtLK5_WT09mVb4jMMhS1i99sRp1_FRUSxO6N_ZqOhhBElboday894gunJOX4kbXyPvRaZActJidTkEeiwqrRoCKimmccyqWgn-SxDLTJVNqWpfZAgqGyHHMrz_yu7yqcw0VzHHHexNOozfkv-6XG5hz-uTn9J--OCQQeVlcEBDSeu8LyzyaONpqwVKgSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=oswrkm8EWASGmlC6wWTfckL3uOI3DfON5fFY2Mas2O5ZAWAlK81om66VVyPusR9qdJuHbPzGDqWMMzBccz5wLfUT-yUTwL6ipfrn7GIw9XBec4eAR9R1_arxxtx-RPR0v09uSSSVJ7J09nF4vtpSgxHX9_lnN-8bMwVRqP5woff06tDbYXvL1vPFiHsE1k5t1aI9gIy5T_4wD7hq57BTQH_Jo8Z1vXj3Ckb0YEG16lTiraT9EsSy1BBR30QZWKn9X01Yi98qecr1VifqUNDJQVZ6h8XNxxUvrqi8iWEDJpCWHxzSmiO-4MZqWySv0OkePPOfpJxUZ6O4MtcP4xdeAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=oswrkm8EWASGmlC6wWTfckL3uOI3DfON5fFY2Mas2O5ZAWAlK81om66VVyPusR9qdJuHbPzGDqWMMzBccz5wLfUT-yUTwL6ipfrn7GIw9XBec4eAR9R1_arxxtx-RPR0v09uSSSVJ7J09nF4vtpSgxHX9_lnN-8bMwVRqP5woff06tDbYXvL1vPFiHsE1k5t1aI9gIy5T_4wD7hq57BTQH_Jo8Z1vXj3Ckb0YEG16lTiraT9EsSy1BBR30QZWKn9X01Yi98qecr1VifqUNDJQVZ6h8XNxxUvrqi8iWEDJpCWHxzSmiO-4MZqWySv0OkePPOfpJxUZ6O4MtcP4xdeAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCDZ_CTVuieX9BoPsezJPIMCRujNFcxJYH7I5r1K211jWBUWyZPtUCwbiA9stzfxs15guYNmfIhsJiU2jdtQ40LqeCpqrjdXcucIUYsRETcyraQPMLJppQS9uSzp6ukepAQ7_DNti6yLztFeGtRdUq2NTzEXg6KZl3qfYNRdeAG0qVRUzsM7O6tlBF46cW4fD5_ud-sdvS7MhwDp2nMckQm0CUS4jg48magvwfPANNrDW8eY_3SqvsjvVcDIJVqtcsttW-ipxmAwOB1V-pcdYVrnvIn-s7APMKYBlo1PZjK0oY_tJVfSVOoQd2Jwnp8YNzj3StnY4wDL_WmjEYeAow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=MO5z8ztlb9LLe8cmzD7fj2Q_Ef0KjqQMQ2teq4nevjR8zxss-JuQojRCZo8TV1ObyuNm3L0FKPu3pnCzszYuLRD6oempQ_tTJYtjS1Ho91AssiCoQFDgRxy9IqM0xJ0Ib_hrCgyEwL5o575Z3YcdY0Lkuef5iSEJrJAZ6_3heMqaXIXVrduG9uUGABOkQRklMqE0MpMFs_fTNM5A20VAl5hmxp8DZDob_TwXrtwj1gbc35eAnc0OhUbdBbc6OdePZ_1d4Oh2EMM544sLRInRbIfTZrWf_fmWDN0-XCk4IdKAzIoAtq2BRXyAmuXRfqBjvn5j7CPEGNU0ICh2nlnvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=MO5z8ztlb9LLe8cmzD7fj2Q_Ef0KjqQMQ2teq4nevjR8zxss-JuQojRCZo8TV1ObyuNm3L0FKPu3pnCzszYuLRD6oempQ_tTJYtjS1Ho91AssiCoQFDgRxy9IqM0xJ0Ib_hrCgyEwL5o575Z3YcdY0Lkuef5iSEJrJAZ6_3heMqaXIXVrduG9uUGABOkQRklMqE0MpMFs_fTNM5A20VAl5hmxp8DZDob_TwXrtwj1gbc35eAnc0OhUbdBbc6OdePZ_1d4Oh2EMM544sLRInRbIfTZrWf_fmWDN0-XCk4IdKAzIoAtq2BRXyAmuXRfqBjvn5j7CPEGNU0ICh2nlnvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=mVtm1IuJP3KN_jHhFvMoRavfpFljJDIOIlHGjDxstlLLRTbdbfDDNZe6xc9_G3D4ysmj77HOpm5hNK6yQVdQZooAkBPj9xC9qj9Z4iFc-H1hvKgYKe3b0iNlN4miahEFxIvo_v0CNc_m286BjK_V8QaNm4X6ZJVr6EfkLi1s-anf2pXNIqMnhUJOXh-RID0UzW-oQLFQ0X_tCMis8SOU7421Xy5VtU4cR7vi8i47-vmf7vhOkHCbHeEESOV5ws00PlkkFiZoT7Bn2JfkiHf9C9Fs91iE6OnTC6qdZaNdnM0z3hoQBLA4Fs1OOnF0lDJGimsE5auaud3cs_YUfebrgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=mVtm1IuJP3KN_jHhFvMoRavfpFljJDIOIlHGjDxstlLLRTbdbfDDNZe6xc9_G3D4ysmj77HOpm5hNK6yQVdQZooAkBPj9xC9qj9Z4iFc-H1hvKgYKe3b0iNlN4miahEFxIvo_v0CNc_m286BjK_V8QaNm4X6ZJVr6EfkLi1s-anf2pXNIqMnhUJOXh-RID0UzW-oQLFQ0X_tCMis8SOU7421Xy5VtU4cR7vi8i47-vmf7vhOkHCbHeEESOV5ws00PlkkFiZoT7Bn2JfkiHf9C9Fs91iE6OnTC6qdZaNdnM0z3hoQBLA4Fs1OOnF0lDJGimsE5auaud3cs_YUfebrgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
