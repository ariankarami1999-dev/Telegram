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
<img src="https://cdn4.telesco.pe/file/t_JGijPVxfoAic9UHVfeniCbkNjhuumzMhPmE6MZlNq-oMSvyaDOmQ2J12JlMXbCCRGlt4kvg2zVExm-5S5IHuS9bECXYXnP9wYT4cGFMsLpfj36KYMOCiPtontSKq8pmHc78wImwtFMY-JzzfW10gCB4NOm4SUmIEB95Zl9hWiUfU0SX9dJJwo6ehn8iAeN3FJU9zyTJWn05wq57Zb21VJpLFGF87pbS5DglFKgFestckVkC1KfcCkhyoSCNzKvD_a6NOz4eFgWQtvb6mfLIlJPWNiIOMx5L9BHBvRPRjdQDnSnTNWx2qEHnOliQZC2HPSS4x-0hs1l4ewDT9e2wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-128679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOINsKBFRly78CN20JCKB9pS1ToZhyPnoKdDE9zPCoFld31if_Zah-jADn0VrY4sX4DqGcYILPeJYys4z-8YA9sQhnmmLpGPsmfWAiWmVOpMymWmMg6JxHDeW3D9Ju6W1Ekq7Tj8HAqO3ettTlCY3fI__m_B7kl4kROyzoY1SeDKas6xXNsZNbx_5762hpZHaRX4_Uhn0KAjtibDqTFeaKToMNf2wVWDxMcBxJzxp8LbxYQf61jU-NdA5co2L2mOZ5-pAV1w4JitHciwkebLqrpadi3L3IAo0GIu7gV-apRyrEWLxjq5zZdggLHUJkWEtzXsamnelEz8hwkBjXcMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/128679" target="_blank">📅 17:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
🔴
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128678" target="_blank">📅 17:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c64bf468.mp4?token=CsEdxD9BUTWNMzFy5V6lTjGD35xjhk4ZrhHN-A9ZDIyAUqX24NCx2aaQM_eZdb9Z1CF6-gMfxMllKK4KIvGA15-FRqRVhDME3d7fHIxY3FKQ5twGZiFf-YuSSMwHJceDn7j15JKKGgByh5gDqoFzJeQkXpZrIx6AZtw6CRUsjXDpL36ReeeaDmk7Qg2v1d3VN7On0Q2bKzgD-e_KUxDdzuT8XUT2nvZokEpMEiiOnZN5-Q6a6KAUsL6GwKwpvtRFSeHSayzjWUHicZH1qw5gn086HvabZuTy_8IN77eT0X9w6ocF8dZXa4SgMxWzN35TpwtSrG5SLeKlnr2Z5z6KxpAyjTHj2cXWcDIs6tn3OsRxB59qZSGUht6vul876FH7PUZtAXqL_kqz2S8A5YlkdW9lAGnorq0b286ThoFDqhja5273cdonbsje2EpWPdr1alxYoiEzUyQOemS_ziKmfMx4Gfx8OVqKQVRdNjj4c__YLzSuZ5a-f-P8qjPKCIwviVEfWOjAtgajtC0NcKWoqncTxHOC4tYIRmNeulnzXBwGr9RPFeYr8dYk_OhnPMMQERJWtG03XOrd0QLKOrE6GRphCgSzyec-AoVNTVyYMRTldE2qRdzu9nSeO7zYVjmUkfwrnLmUqYd_LZUBojwifrDc5KdWxYBf1_2q_QLR8YY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c64bf468.mp4?token=CsEdxD9BUTWNMzFy5V6lTjGD35xjhk4ZrhHN-A9ZDIyAUqX24NCx2aaQM_eZdb9Z1CF6-gMfxMllKK4KIvGA15-FRqRVhDME3d7fHIxY3FKQ5twGZiFf-YuSSMwHJceDn7j15JKKGgByh5gDqoFzJeQkXpZrIx6AZtw6CRUsjXDpL36ReeeaDmk7Qg2v1d3VN7On0Q2bKzgD-e_KUxDdzuT8XUT2nvZokEpMEiiOnZN5-Q6a6KAUsL6GwKwpvtRFSeHSayzjWUHicZH1qw5gn086HvabZuTy_8IN77eT0X9w6ocF8dZXa4SgMxWzN35TpwtSrG5SLeKlnr2Z5z6KxpAyjTHj2cXWcDIs6tn3OsRxB59qZSGUht6vul876FH7PUZtAXqL_kqz2S8A5YlkdW9lAGnorq0b286ThoFDqhja5273cdonbsje2EpWPdr1alxYoiEzUyQOemS_ziKmfMx4Gfx8OVqKQVRdNjj4c__YLzSuZ5a-f-P8qjPKCIwviVEfWOjAtgajtC0NcKWoqncTxHOC4tYIRmNeulnzXBwGr9RPFeYr8dYk_OhnPMMQERJWtG03XOrd0QLKOrE6GRphCgSzyec-AoVNTVyYMRTldE2qRdzu9nSeO7zYVjmUkfwrnLmUqYd_LZUBojwifrDc5KdWxYBf1_2q_QLR8YY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: من شاااشیدم وسط ایران مذاکرات و دوقطبی‌ای که میگید، مذاکره اوج بیشرفیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128677" target="_blank">📅 17:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNEFYhwQfiLTQH_cLsEFZlSvh_KbyGKnEWtQoxU32ABtOxG2O7vrikwlUQxdlMtXDhATEHSy8y0Vd1PQQJEgOngAnQjeje5H0ujtk_FX5N-Cwxp5g54SBspXnqPc8PbtzhHLVucjDOs0H4moG32zrGoGwAsjqJ1C_pqOFv4_UJuB__0ofxiNxVKOO60bpc3rGHYEaa-g--QXSZ51qF0NbiD023eJSL0YVd23C1zjdRwNNS3f1SriFX5maW8OUfTYxlqX189hsx6gylj0rvAcENPU2PHMh0mq9PdGF2QQg9TvlzcU5L2WAo6UoRa80hTpi3lSgQa-RciWtUm6nFb6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایرانخودرو بازم قیمت‌ها برد بالا
‼️
🔴
ایرانخودروی حرومزاده الان که دلار و طلا کاهشیه و ورق فولاد هم تو بازار زیاد شده چرا بازم گرون میکنی؟
#فساد_گسترده
#فساد_سلولی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128676" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47c77e203d.mp4?token=Z6QzojwPBPncfGeh5rW1PvplePvbVxiQ7ORqBrbuYaJBRByP-zRnimALRIDCq_6M8semvQXpZSzJFxhstVqf-0XnYyFE_gYNGyBhNgDNYsm7SwRJ1l-2V2MSpmS44JnobZdFlQ0jBxeo2EXdKVvcF0-5ucEwgB9yyWrlcqzL70OyIYSovIv5S5r0-z7hIS_1J4VwTAZHZJL0ujXhpaCJ70ZdUNA_6gp9-YhcKcBxGu4M7yOALx_icsEhobLrtEbd7aU0cAXonsssXUQwVn9ku0cVI3ph8dddSAt2EBVaOMlxhCPtXfyueFeaeRPbHeIGX4haPEhbZ6spU4mNH7TFxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47c77e203d.mp4?token=Z6QzojwPBPncfGeh5rW1PvplePvbVxiQ7ORqBrbuYaJBRByP-zRnimALRIDCq_6M8semvQXpZSzJFxhstVqf-0XnYyFE_gYNGyBhNgDNYsm7SwRJ1l-2V2MSpmS44JnobZdFlQ0jBxeo2EXdKVvcF0-5ucEwgB9yyWrlcqzL70OyIYSovIv5S5r0-z7hIS_1J4VwTAZHZJL0ujXhpaCJ70ZdUNA_6gp9-YhcKcBxGu4M7yOALx_icsEhobLrtEbd7aU0cAXonsssXUQwVn9ku0cVI3ph8dddSAt2EBVaOMlxhCPtXfyueFeaeRPbHeIGX4haPEhbZ6spU4mNH7TFxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما : شماها دارید با کسی مذاکره میکنید که به رهبری تهمت همجنسگرایی زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128675" target="_blank">📅 16:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68014de410.mp4?token=cDahsA0sJvFtOUEIpZ6RcfgNLl0nGKiFCWIi-T7bSTNUAkRaomDQgUTdqLCHU6oN0QKUrN4vmrCznfKwaJpcvehKbaufd-jSlUVcgDu9ZTEeIke4gezlIztSOivBsqUMXn6hmnFvZX_X8VxHO0P4dpsnYGfmHzcVzq4Tg-J9vf44VXhxUhIULvdM_Byy3Zy7cHZbkqgGZ9uFD8LTB8MSoc9u2IrjwMGQpw8A7XTqo1KUGSt9lKUHFwUDk1XgF9RKUCdunJMyyX_fD-pq4vqEED278hR3T--B2VSFx9pg8prDn_mbIpRP4StElMZC4kfQbETOvZPsP__fvLyLgzt2hSXx6dfqPcIRF7nRqurQ6EN_V8hCwcJJM_x1BkwqZ8DJCXnrbi6dbIPAEDwJKywxwIkzYAUbtlwQUozElLvOF7ytorXg31WTLrA9AopjOzUH9kpSPFBP2LufhLDqha75lkf_zZenreOzlnzHVq5sCzeQHsOkBqKjN7ktMcgRRZLL6p_ytGyN6FfR_NXgw6IXYrbosew6m-ILTALlF-I833qbpYT4fs9Uwd66zd2ICUKTLhKsX2KQFsuefyBchfg6Piqc0jaET2yGe7hqWZfiZ4NI96Waq-f4EkyTo7xtK9VW89kQsEpAsa_4hiKdE8XPlGBdFhbPDUlErrJOLV0JnO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68014de410.mp4?token=cDahsA0sJvFtOUEIpZ6RcfgNLl0nGKiFCWIi-T7bSTNUAkRaomDQgUTdqLCHU6oN0QKUrN4vmrCznfKwaJpcvehKbaufd-jSlUVcgDu9ZTEeIke4gezlIztSOivBsqUMXn6hmnFvZX_X8VxHO0P4dpsnYGfmHzcVzq4Tg-J9vf44VXhxUhIULvdM_Byy3Zy7cHZbkqgGZ9uFD8LTB8MSoc9u2IrjwMGQpw8A7XTqo1KUGSt9lKUHFwUDk1XgF9RKUCdunJMyyX_fD-pq4vqEED278hR3T--B2VSFx9pg8prDn_mbIpRP4StElMZC4kfQbETOvZPsP__fvLyLgzt2hSXx6dfqPcIRF7nRqurQ6EN_V8hCwcJJM_x1BkwqZ8DJCXnrbi6dbIPAEDwJKywxwIkzYAUbtlwQUozElLvOF7ytorXg31WTLrA9AopjOzUH9kpSPFBP2LufhLDqha75lkf_zZenreOzlnzHVq5sCzeQHsOkBqKjN7ktMcgRRZLL6p_ytGyN6FfR_NXgw6IXYrbosew6m-ILTALlF-I833qbpYT4fs9Uwd66zd2ICUKTLhKsX2KQFsuefyBchfg6Piqc0jaET2yGe7hqWZfiZ4NI96Waq-f4EkyTo7xtK9VW89kQsEpAsa_4hiKdE8XPlGBdFhbPDUlErrJOLV0JnO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اوکراین، میخایلو فدوروف:
در حال حاضر، ما یک فرصت طلایی داریم و در ۶ ماه آینده، برتری در میدان نبرد خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128674" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
قالیباف: رابطۀ ایران با چین رابطه یک مشتری یا همتای تجاری نیست بلکه به معنای واقعی کلمه باید شریک باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128673" target="_blank">📅 16:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128672">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9370552a27.mp4?token=Y3ijc04zRLab9cBXlTx_PDY-A5dttzsRXjlIeGZeHFNK90o-LalLZCx9Y_3ST4d4tX51aS18WFMBQ0GoxQwEw7w1n1g9cGZrrv4yxCUnxwYctsJ14zPu_Xo_LV1rqf49GvJusboHeEvjlfZYWyWIn_ZMgwDx5L01iUDJIe3pZdaqkwx3qH9oIprqGvj-Bs92Z88bZojiHzOaBPUh9XTWcsQ0N8vasrJaUSH09fSOwcs5dQlf-22W5Asq-O-_WZUhhsBHFDz0LI_b3kVYPlx6xBP_zKER2pEpRY-e3EEk3RsHzPAmQ7uDqTSXR7fqn2SF2FGXr1LV1E2WqPlYFqwllEkHMZnCGdbBglZ-uX9L1MyUa4VupKhJsnxCjnpi3vfJUQBYWFeZYzR6YRXBfhmsFsjkUrUh7kxSajM5FxlajIZihiqX3s58gvdcp72QkEyAXSqC_Jv7rHm_8DeTXTGlr8GhTpgztihKPEL2wQyEEvJ321pak1DQgzAvORxSezeTlUGsKu4xg98v_v_rqJCI5yRFVEJkimF2vlB0E1d6QhCSd8KHFTTzj9zSTLN8AN48vPgLjT1185eZMQkPOBx879Mq4VcbmmiLOPn89AgaHdQq_sGpUI7ssk44smF92kUdIWn7vH_Iht7mSY7wC_g0BKbCCYTYvt2FsU8paVNocWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9370552a27.mp4?token=Y3ijc04zRLab9cBXlTx_PDY-A5dttzsRXjlIeGZeHFNK90o-LalLZCx9Y_3ST4d4tX51aS18WFMBQ0GoxQwEw7w1n1g9cGZrrv4yxCUnxwYctsJ14zPu_Xo_LV1rqf49GvJusboHeEvjlfZYWyWIn_ZMgwDx5L01iUDJIe3pZdaqkwx3qH9oIprqGvj-Bs92Z88bZojiHzOaBPUh9XTWcsQ0N8vasrJaUSH09fSOwcs5dQlf-22W5Asq-O-_WZUhhsBHFDz0LI_b3kVYPlx6xBP_zKER2pEpRY-e3EEk3RsHzPAmQ7uDqTSXR7fqn2SF2FGXr1LV1E2WqPlYFqwllEkHMZnCGdbBglZ-uX9L1MyUa4VupKhJsnxCjnpi3vfJUQBYWFeZYzR6YRXBfhmsFsjkUrUh7kxSajM5FxlajIZihiqX3s58gvdcp72QkEyAXSqC_Jv7rHm_8DeTXTGlr8GhTpgztihKPEL2wQyEEvJ321pak1DQgzAvORxSezeTlUGsKu4xg98v_v_rqJCI5yRFVEJkimF2vlB0E1d6QhCSd8KHFTTzj9zSTLN8AN48vPgLjT1185eZMQkPOBx879Mq4VcbmmiLOPn89AgaHdQq_sGpUI7ssk44smF92kUdIWn7vH_Iht7mSY7wC_g0BKbCCYTYvt2FsU8paVNocWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، فریدریش مرز، درباره تولید سلاح‌ها: من بسیار سپاسگزارم که رئیس‌جمهور ترامپ و کل هیئت آمریکایی تمایل بالایی به همکاری نشان داده‌اند.
🔴
همه ما مشکل این را داریم که در حال حاضر تولیدمان بسیار کم است.
🔴
این مشکل می‌تواند از طریق توافق‌های مجوز با شرکت‌هایی که ظرفیت تولید لازم را دارند جبران شود، و این شرکت‌ها هم شرکت‌های اروپایی و هم شرکت‌های اوکراینی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128672" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128671">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: ترامپ به اعتراضات اسرائیل در موضوع توافق با ایران گوش نداد
🔴
امیدواریم که مذاکرات فنی هر چه زودتر پایان یابد و صلح در منطقه برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128671" target="_blank">📅 16:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128670">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ایران امروز یک تفاهم‌نامه با شرکت سهامی خاص هلی‌کوپترهای روسی برای ۲۰ هلی‌کوپتر سری Mi-8/17 امضا کرد (۴ تا از آن‌ها قبلاً قرارداد بسته شده است) که باید تا مارس ۲۰۲۷ تحویل داده شوند تا برای مقاصد اطفاء حریق، انتقال پزشکی و نجات استفاده شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128670" target="_blank">📅 16:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128669">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان درباره مفاد متن توافق ایران و آمریکا
🔴
سی‌ان‌ان مدعی شد از طریق یک مقام آمریکایی به تفاهم‌نامه ۱۴ ماده‌ای بین ایران و آمریکا دست یافت و محتوای آن توسط دیپلمات دیگری که این توافق‌نامه را دیده است، تأیید شد:
🔴
آتش‌بس فوری و دائمی بین ایران، آمریکا و متحدانشان در تمام جبهه‌ها، از جمله لبنان، با تعهد هر دو طرف به عدم اقدامات خصمانه یا استفاده از زور در آینده.
🔴
هر دو طرف موافقت می‌کنند که به حاکمیت، تمامیت ارضی یکدیگر احترام بگذارند و از دخالت در امور داخلی خودداری کنند.
🔴
توافق نهایی ظرف ۶۰ روز مذاکره خواهد شد و تمدید آن با رضایت متقابل امکان‌پذیر است.
🔴
ایالات متحده بلافاصله محاصره دریایی را لغو خواهد کرد، ترافیک دریایی را ظرف ۳۰ روز به سطح قبل از جنگ باز خواهد گرداند و نیروها را ظرف ۳۰ روز پس از توافق نهایی از مناطق اطراف خارج خواهد کرد.
🔴
ایران کشتیرانی تجاری از طریق خلیج فارس و دریای عمان را ظرف ۳۰ روز به سطح قبل از جنگ باز خواهد گرداند، از جمله مین‌زدایی و رفع موانع فنی.
🔴
ایالات متحده و شرکای منطقه‌ای یک طرح احیا و توسعه اقتصادی ۳۰۰ میلیارد دلاری برای ایران تدوین خواهند کرد که جزئیات اجرایی آن ظرف ۶۰ روز نهایی می‌شود.
🔴
ایالات متحده متعهد می‌شود که تمام تحریم‌های ایران را تحت یک جدول زمانی توافق‌شده، شامل تحریم‌های سازمان ملل، آژانس بین‌المللی انرژی اتمی و تحریم‌های یکجانبه ایالات متحده، لغو کند.
🔴
ایران تأکید می‌کند که هرگز سلاح هسته‌ای تولید نخواهد کرد. مسائل معوقه در مورد اورانیوم غنی‌شده، مواد هسته‌ای و نیازهای هسته‌ای ایران در توافق نهایی حل و فصل خواهد شد.
🔴
تا زمان دستیابی به توافق نهایی، ایران فعالیت‌های هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا گسترش حضور نظامی منطقه‌ای خود خودداری خواهد کرد.
🔴
وزارت خزانه‌داری ایالات متحده بلافاصله معافیت‌هایی را صادر خواهد کرد که به ایران اجازه صادرات نفت، پتروشیمی و خدمات بانکی، بیمه و کشتیرانی مرتبط را می‌دهد.
🔴
دارایی‌های مسدود شده ایران به تدریج با پیشرفت مذاکرات آزاد می‌شوند و دسترسی کامل طبق سازوکارهای مورد توافق دو طرف اعطا می‌شود.
🔴
یک سازوکار اجرایی مشترک برای نظارت بر رعایت توافق نهایی ایجاد خواهد شد.
🔴
به محض شروع اجرای مفاد کلیدی - از جمله بازگرداندن کشتیرانی، معافیت از تحریم‌ها و آزادسازی دارایی‌ها - مذاکرات در مورد عناصر باقی‌مانده توافق نهایی ادامه خواهد یافت.
🔴
توافق نهایی از طریق قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تأیید خواهد شد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128669" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128668">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
استرالیا امروز سطح عمومی هشدار سفر برای بحرین، اسرائیل، کویت، قطر و امارات متحده عربی را کاهش داد و از شهروندان خود خواست در مورد ضرورت سفر به این مناطق تجدیدنظر کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128668" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128667">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اسرائیل در حال آماده‌سازی برای فروپاشی توافق صلح آمریکا و ایران است و به نیروهای نظامی خود دستور داده است تا به توسعه بانک‌های هدف ادامه دهند و برای تشدید احتمالی آینده آماده شوند، معاریو گزارش می‌دهد
🔴
مقامات اسرائیلی معتقدند این توافق احتمالاً پایدار نخواهد ماند، اگرچه اذعان دارند که اسرائیل به متن نهایی شده به طور کامل دسترسی نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128667" target="_blank">📅 15:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128666">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تسنیم: اختلال خدمات بانکی ادامه دارد/تجهیزات شبکه فرسوده هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128666" target="_blank">📅 15:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نخست‌وزیر آلمان، مرز، در مورد ایران و لبنان: تنگه هرمز باید بدون هیچ محدودیتی باز بماند، بدون هیچ «اگر» یا «اما»یی، و ایران باید به‌طور دائم و قابل‌تایید برنامه هسته‌ای خود را پایان دهد.
🔴
صلح باید برقرار بماند — و این نه تنها به ایران، بلکه همچنین به لبنان، به‌ویژه جنوب لبنان، که درباره وضعیت آن به‌طور مفصل بحث کردیم، نیز اعمال می‌شود.
🔴
آلمان کمک خواهد کرد. در منافع ماست که صلح برقرار بماند.
🔴
ما به یک خاورمیانه و منطقه نزدیک پایدار نیاز داریم. ما به شفافیت و آزادی در مسیرهای دریایی نیاز داریم. ما به قیمت‌های پایدار انرژی نیاز داریم.
🔴
کمک‌ها ممکن است شامل تعهد نظامی نیز باشد. دولت فدرال زمانی که و اگر شرایط لازم برقرار شود، یک مأموریت مناسب را به پارلمان پیشنهاد خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128665" target="_blank">📅 15:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128664">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نخست‌وزیر آلمان: همه شرکای G7 مشارکت نظامی و مالی خود را به اوکراین افزایش خواهند داد.
🔴
پیام به روسیه روشن است: همه شرکای G7 فشار را بر مسکو افزایش خواهند داد، از جمله از طریق تحریم‌ها.
🔴
این امر لحن جدیدی در وحدت و عزم اقیانوس اطلس ایجاد می‌کند.
🔴
توافقی که بین رئیس‌جمهور ترامپ و رهبری ایران به دست آمده، موفقیتی واقعاً بزرگ است.
🔴
ما همین امروز می‌توانیم آن را ببینیم، برای مثال در قیمت نفت که همچنان در حال کاهش است. این نشانه‌ای خوب است و روابط تأمین به وضوح به صورت سیستماتیک در حال بازسازی هستند.
🔴
اکنون باید این توافق با مذاکرات بیشتری دنبال شود، به ویژه دور دوم گفتگوها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128664" target="_blank">📅 15:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128663">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره سیسی مصر:
او در هتلی بود؛ من با او ملاقات کردم و ما عاشق هم شدیم، عمیقاً عاشق.
🔴
شیمی فوق‌العاده‌ای داشتیم. من دو برابر مدت مقرر ماندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128663" target="_blank">📅 15:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128662">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: من مسابقات جام جهانی را دنبال می‌کنم و کشورهای مختلفی از شمال آفریقا مانند مراکش و مصر را می‌بینم.
🔴
آنها بسیار با استعداد و سریع هستند، اما جدا از هم هستند
🔴
پرسیدم: چرا کشورهای شمال آفریقا متحد نمی‌شوند تا یک تیم بزرگ تشکیل دهند؟ اگر این کار را می‌کردند، به راحتی قهرمان می‌شدند!
🔴
این نشان‌دهنده کمبود رهبری در آنجا است. شاید بعد از اینکه کار نجات آمریکا را تمام کردم، بروم و برای ریاست آفریقا نامزد شوم، ما خیلی راحت پیروز خواهیم شد و قهرمان جام جهانی خواهیم شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128662" target="_blank">📅 15:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LvqUjzx0ZF1QXLGnccdaQAcDabeY95eU6RRjcWVCCK-HyxT8-8UqTWUOodzdxFDj5UlQ6NakwL7jbLzf4DNl7VrCFuzuMvcHjweeqfuMiYLFZT-i4bBK2dmqzg8OKN7vkG4o2OaYiO01ZXmN0dH9-8KnlKodynb1kDE9TpQ5yXr5f7qb45VgCk34mK5D0YNJlD-bxNeVrnFDNBeUjioXZCa_qM0qRgW2To7TjfN3SCeMsWoiSaQYm1Q9-FGGXBkjj1tkbJxCn_DW__mKQMVleK0b7n5JVZo-6QwEr59Mme7iBrRRtY9dtnT0MHSymdhbm93t5XZTf0HgybyN8oPqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/1ed7b41643.mp4?token=R3JQoSS51X_pJR5f_5WM8Xk3-oQVCZEwW0vsQnHh4AIwguPKD6-C5TIUutKGqhjErel2MGp526b_6IAhvtAkk214eXNGi0O_EclWfclYKsydlxFx3Z-cW5fqy2sap8J3UwEz4xA3mpcVqHdtXyDD6QO2IGgB6ZcaJKfqI2Rp6-NcTuOOXWnTjR6fHFZ7AJpsIx9ZKh4W4iVWeTCRMi1jcFG8TQXYE8dCpN-sxlnXgimB-5qIZLa2yUsV4X2KdaIS1IVpnDYfUGyKwCuSIsGSbcsBUEHoVbGJTS4d6oJLSItDO3JxeAekKFskt_-Fb3tWY8eA0j_YoVpaUf4JQ1xjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/1ed7b41643.mp4?token=R3JQoSS51X_pJR5f_5WM8Xk3-oQVCZEwW0vsQnHh4AIwguPKD6-C5TIUutKGqhjErel2MGp526b_6IAhvtAkk214eXNGi0O_EclWfclYKsydlxFx3Z-cW5fqy2sap8J3UwEz4xA3mpcVqHdtXyDD6QO2IGgB6ZcaJKfqI2Rp6-NcTuOOXWnTjR6fHFZ7AJpsIx9ZKh4W4iVWeTCRMi1jcFG8TQXYE8dCpN-sxlnXgimB-5qIZLa2yUsV4X2KdaIS1IVpnDYfUGyKwCuSIsGSbcsBUEHoVbGJTS4d6oJLSItDO3JxeAekKFskt_-Fb3tWY8eA0j_YoVpaUf4JQ1xjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملاتی را در نزدیکی روستای کفر تبنیت در جنوب لبنان انجام می‌دهند، جایی که درگیری‌ها بین مبارزان حزب‌الله و نیروهای اسرائیلی ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128660" target="_blank">📅 15:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: من با رئیس جمهور سوریه در مورد احتمال جنگ علیه حزب الله صحبت کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128659" target="_blank">📅 15:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرده که تاریخ آن ۱۴ ژوئن است و نشان می‌دهد نیروهایش با استفاده از پهپاد حمله‌ای ابابیل، یک خودروی زرهی اسرائیلی را در حومه مجدل زون در جنوب لبنان هدف قرار می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128658" target="_blank">📅 14:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e28bb5612.mp4?token=MhIBErh56s9wVIGCtvYJbpochVDsVRHLuDamwQMEzSBRO1hq7KlztW3Tkged99SdHbL6wJaZkS9y4eZlT0rbL54qU_I4JOLNy7vtcKB97ACWi6lwZf2MymOevtI9SY-PFZ1pWc6kVoh_scsDtNHNWutzWjsZADr8kGtldkNm0lQnNU7WwEEnLlBoZFi1pJfSQ5KnTzd0REYvKdwxn7FQyMD76n9cx_phCk2Mfiyk1cSEqxZXLW2aZueloEewrZfXjo7a2z2UnGfEbk4qrH3U-SZpWTk6RHsa163vy4JqJJOv0oEghb1wg4Q62S_EvkczytiEQPDLE3yjZvkoP-Hf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e28bb5612.mp4?token=MhIBErh56s9wVIGCtvYJbpochVDsVRHLuDamwQMEzSBRO1hq7KlztW3Tkged99SdHbL6wJaZkS9y4eZlT0rbL54qU_I4JOLNy7vtcKB97ACWi6lwZf2MymOevtI9SY-PFZ1pWc6kVoh_scsDtNHNWutzWjsZADr8kGtldkNm0lQnNU7WwEEnLlBoZFi1pJfSQ5KnTzd0REYvKdwxn7FQyMD76n9cx_phCk2Mfiyk1cSEqxZXLW2aZueloEewrZfXjo7a2z2UnGfEbk4qrH3U-SZpWTk6RHsa163vy4JqJJOv0oEghb1wg4Q62S_EvkczytiEQPDLE3yjZvkoP-Hf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟
🔴
او نابغه‌ای شرور بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128657" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfafb267df.mp4?token=j8Qcr9uMAH30Zp7-Wvh-B_SLiB3UPainAgrEYW3dwwFJMhKkKixPnZfGTgNNZ5UhFo3_Q1iD978zPsCdYJvdsCqX_ZUcllWVVuysVJyi3uPcJgyj9yoZLkvqW_LEqyf4mhncwmJ5HbnHQ4PUpIHbf5vGEwTCDf0beDhq2RPHi7ajVcvQateSZHSA6iYP_fhSNBY88zo3ywaZLKTp_qqta1m_h-BtawKDuDMCIU2i0eb9vz6kcChqw4nwoPR7TOC4pvsz3kx7_T1_6NvGb7jUckmsrY5HsHOrG8SyIDW89DCv0lJXZFVNU2pF6YrXf5CSbEer4Rp0N7JOwu4XS4F9Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfafb267df.mp4?token=j8Qcr9uMAH30Zp7-Wvh-B_SLiB3UPainAgrEYW3dwwFJMhKkKixPnZfGTgNNZ5UhFo3_Q1iD978zPsCdYJvdsCqX_ZUcllWVVuysVJyi3uPcJgyj9yoZLkvqW_LEqyf4mhncwmJ5HbnHQ4PUpIHbf5vGEwTCDf0beDhq2RPHi7ajVcvQateSZHSA6iYP_fhSNBY88zo3ywaZLKTp_qqta1m_h-BtawKDuDMCIU2i0eb9vz6kcChqw4nwoPR7TOC4pvsz3kx7_T1_6NvGb7jUckmsrY5HsHOrG8SyIDW89DCv0lJXZFVNU2pF6YrXf5CSbEer4Rp0N7JOwu4XS4F9Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور مصر سیسی به ترامپ:
نمی‌توانم به اندازه کافی تأکید کنم که چقدر برای شما احترام قائلم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128656" target="_blank">📅 14:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ درباره ایران: دلیل پایین ماندن قیمت نفت این است که هر شب کشتی‌هایی را از بین می‌بردیم که حتی شما از آن‌ها خبر نداشتید.
🔴
دو روز پیش، سه روز پیش، یک ماه پیش، ۲۲ کشتی را از بین بردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی را از بین می‌بردیم. هیچ‌کس این را نمی‌دانست.
🔴
نیروی دریایی ما کار بزرگی انجام داد. هیچ‌کس نمی‌دانست چه اتفاقی می‌افتد. به همین دلیل نفت به ۳۰۰ دلار در هر بشکه نرسید؛ بلکه به ۱۲۵ تا ۱۵۰ دلار رسید.
🔴
حالا قیمت آن ۷۲، ۷۳ دلار است. شنیده‌ام که الان حتی کمتر از این است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128655" target="_blank">📅 14:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: قیمت نفت بلافاصله پس از اعلام توافق با ایران کاهش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128654" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روزنامه کیهان: مجلس باید جلوی مذاکره پنهانی با آمریکا رو بگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128653" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df1ec5ca5.mp4?token=OKhPBOIDyRlczw2cSc_-Rx2HlZZtL5mAj8ZkQetXyNYMOR3sICsir4ku3gdwWm04WbE6VQb9TCelGuXNQ7y8vgg6kp_7WAe8E8WYUiLyynzftIlb72ZfN_MNAK0VhMfCIPOHJgBXCLZgG2xhhrUOnOeg3uTeVY1wFOW8aQG8pExPSzZmb5la4fqun38BYrH5qAwogfG4skjHlh1GujDs_dHfR6J0f-5VitBt_wZ04Q8G7P9cAy_n6P376XmD1BPTDyiirhLusiS7SA-vHlx7BBk4pnxwra1D2ryLRgWhKzaT7jIjQtX2ZsZfRoW0ePuf77VO8MrG-hrnfDPd8_soVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df1ec5ca5.mp4?token=OKhPBOIDyRlczw2cSc_-Rx2HlZZtL5mAj8ZkQetXyNYMOR3sICsir4ku3gdwWm04WbE6VQb9TCelGuXNQ7y8vgg6kp_7WAe8E8WYUiLyynzftIlb72ZfN_MNAK0VhMfCIPOHJgBXCLZgG2xhhrUOnOeg3uTeVY1wFOW8aQG8pExPSzZmb5la4fqun38BYrH5qAwogfG4skjHlh1GujDs_dHfR6J0f-5VitBt_wZ04Q8G7P9cAy_n6P376XmD1BPTDyiirhLusiS7SA-vHlx7BBk4pnxwra1D2ryLRgWhKzaT7jIjQtX2ZsZfRoW0ePuf77VO8MrG-hrnfDPd8_soVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود نیروهای اسرائیلی به شهر بیت امر تو شمال الخلیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128652" target="_blank">📅 14:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره اوباما و ایران: هیچ‌کس نمی‌توانست این توافق را انجام دهد.
🔴
برجام توسط اوباما انجام شد؛ او ۱.۷ میلیارد دلار پول نقد سبز از بانک‌ها به آنها داد، آن را در یک بوئینگ ۷۵۷ گذاشت و به ایران پرواز داد. و آنها کنار هواپیما ایستادند. من عکس‌هایی از آن دارم: «وای خدای من. نگاه کن به این پولی که به ما می‌دهد.»
🔴
او تلاش کرد با رشوه راه فرار پیدا کند. من این کار را نکردم. هیچ‌کس به این اشاره نمی‌کند.
🔴
و می‌دانید ایرانی‌ها چه کردند؟ به اوباما خندیدند و گفتند: «او یک پسر احمق لعنتی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128651" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53f176b7a.mp4?token=W4Av1yXVCybJlxsPp2ai0QfzfuJVOIM0zEAgnQG9B2O_Q2_lSE03qT-vzB-1lNuYvpaYLQrUKuvEf0q2IRRn3pRRukHmRN-WANrxu4zSo1HG7CGNRs21EEAHX3COUAK0g1v6JQ2fJ5brvdB8cbZrrfGbbon_co2a9n0ilvN2_v5ECGPnl_b26cB3Me_hiiBPy2EPuZ3jNCdwbaXHcjeptaD3mijaEKCE2tlBrRBCbNz-ztZKbMC9arXslHldETLB95qHxMHnsdhugtdQA_30Z74WziRpyOy4z_KxgSOjXUBOAf2Cchp4huKSiofRhsQHQIvaiFc0IJ-KE2veYR18BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53f176b7a.mp4?token=W4Av1yXVCybJlxsPp2ai0QfzfuJVOIM0zEAgnQG9B2O_Q2_lSE03qT-vzB-1lNuYvpaYLQrUKuvEf0q2IRRn3pRRukHmRN-WANrxu4zSo1HG7CGNRs21EEAHX3COUAK0g1v6JQ2fJ5brvdB8cbZrrfGbbon_co2a9n0ilvN2_v5ECGPnl_b26cB3Me_hiiBPy2EPuZ3jNCdwbaXHcjeptaD3mijaEKCE2tlBrRBCbNz-ztZKbMC9arXslHldETLB95qHxMHnsdhugtdQA_30Z74WziRpyOy4z_KxgSOjXUBOAf2Cchp4huKSiofRhsQHQIvaiFc0IJ-KE2veYR18BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: فراموش نکنید، هیچ‌کس هرگز به اندازه من با ایران سخت‌گیر نبوده است.
🔴
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری از افراد دیگر انجام می‌شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128650" target="_blank">📅 14:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26094f6759.mp4?token=NHcklbuS9P07ruJwSsFeB1LdOy1z59uUQoRZL_GuabZ-MfSbrl5gX-gQmcXWo2VCAlxskl0UhQvADIn4K2WWx7Hkb2iC8MdXa_A-XtMTekDQQaHn5U-of2kz08-67WToa80gKx3kJsVatTl6P3a2JvxPamUvRVCS9Dx3Q-pob57IjO7y1Xd60R6D5dRCpxaaCeXuullDtiBazE4B9hOf04roIrd4Wjn3HT_3_RaxPeXK4evwKYcKhmL6kj3h2gg3e2zPyRyHvzDqfdR7glWjkyJ1elT9Da-scNcx3KUCA5Jz7U8QZA9rxsT72SWYq-GH_FQ_CVXS7LdDRtyUfWsTWYJnp9QN-NzQNF1cCOuN5ON_WFiAt00w_M3UC7-7uaLqjpMF8lqIKdOWlRjsFklmzSWMT3spjm_pdvXkwsYMJIrsBw7v8-NFEItFFigOWNJodTB3SoBGBikqV2oFQZVnzfWcfYIt8-9p9eI8XKQZbkOmnXu6VAOQ9B6GEd18KsclBN8ZrG0B5sdT5qi8mhg661vdbuG8FFUHeTUJ0mOzZUKKLpXCAuk0jbuYSmQevJUbhzCcdXc1pbk6g9zn4sjXPXQbdr53GC5e4_iJ5tDDXshlzN2J3BOI9mRfpHBwyIaB1AaNaQQ06LAJ6xv4xrpNnbKL1bRXgQT2944pJsyWEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26094f6759.mp4?token=NHcklbuS9P07ruJwSsFeB1LdOy1z59uUQoRZL_GuabZ-MfSbrl5gX-gQmcXWo2VCAlxskl0UhQvADIn4K2WWx7Hkb2iC8MdXa_A-XtMTekDQQaHn5U-of2kz08-67WToa80gKx3kJsVatTl6P3a2JvxPamUvRVCS9Dx3Q-pob57IjO7y1Xd60R6D5dRCpxaaCeXuullDtiBazE4B9hOf04roIrd4Wjn3HT_3_RaxPeXK4evwKYcKhmL6kj3h2gg3e2zPyRyHvzDqfdR7glWjkyJ1elT9Da-scNcx3KUCA5Jz7U8QZA9rxsT72SWYq-GH_FQ_CVXS7LdDRtyUfWsTWYJnp9QN-NzQNF1cCOuN5ON_WFiAt00w_M3UC7-7uaLqjpMF8lqIKdOWlRjsFklmzSWMT3spjm_pdvXkwsYMJIrsBw7v8-NFEItFFigOWNJodTB3SoBGBikqV2oFQZVnzfWcfYIt8-9p9eI8XKQZbkOmnXu6VAOQ9B6GEd18KsclBN8ZrG0B5sdT5qi8mhg661vdbuG8FFUHeTUJ0mOzZUKKLpXCAuk0jbuYSmQevJUbhzCcdXc1pbk6g9zn4sjXPXQbdr53GC5e4_iJ5tDDXshlzN2J3BOI9mRfpHBwyIaB1AaNaQQ06LAJ6xv4xrpNnbKL1bRXgQT2944pJsyWEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: قابلیت پرداخت فقط یک حقه دیگر است. آنها کلمه «قابلیت پرداخت» را ساختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128649" target="_blank">📅 14:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس: تفاهم‌نامه نیازی به تصویب مجلس ندارد/ ایران دانش هسته‌ای را رها نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128648" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارشگر: گزارش شده است که این توافق شامل صندوقی به ارزش ۳۰۰ میلیارد دلار برای ایران است.
🔴
ترامپ: نه، این دروغ است. ما سرمایه‌گذاری نمی‌کنیم. مردم می‌توانند تصمیم بگیرند که این کار را انجام دهند، اما این به خودشان بستگی دارد.
🔴
آیا می‌خواهید بگویم که هیچ‌کس هرگز مجاز نیست در یک کشور سرمایه‌گذاری کند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128647" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aefc1a4c.mp4?token=r8EqBVus6yOVA_6UAprQ4S6y6LI9DfLMfcaSwZ6PCtWTFxRz0E7r6vhAHVyFsOGAdKKOTk9ha2nm5pqCNDeuE0w5WITM3-fCrhhtXiu_hrhuS31DNPbxbU2Se5ISTUEgBchf26Lv-zFaExVudEirUIvsn6KEFNYJHayQ4oXv1CzW2xXDScIfhvH7kBq0lOYkJkSS2lGToIW8pbkdnfAvMIMs9waqk4K28B120ODQ7uiEe0CJuymCqhYEcu33_v64_idu7ob6RkH3Wz6uDbWJh4ctreMpa7D-G32-ixzJe0UVhUCGYucDRIuPcg384ay6I1VplscXw2t9N1F2nhdBLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aefc1a4c.mp4?token=r8EqBVus6yOVA_6UAprQ4S6y6LI9DfLMfcaSwZ6PCtWTFxRz0E7r6vhAHVyFsOGAdKKOTk9ha2nm5pqCNDeuE0w5WITM3-fCrhhtXiu_hrhuS31DNPbxbU2Se5ISTUEgBchf26Lv-zFaExVudEirUIvsn6KEFNYJHayQ4oXv1CzW2xXDScIfhvH7kBq0lOYkJkSS2lGToIW8pbkdnfAvMIMs9waqk4K28B120ODQ7uiEe0CJuymCqhYEcu33_v64_idu7ob6RkH3Wz6uDbWJh4ctreMpa7D-G32-ixzJe0UVhUCGYucDRIuPcg384ay6I1VplscXw2t9N1F2nhdBLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره توافق ایران: متن نهایی نیست؛ این یک یادداشت تفاهم است!
🔴
اگر از آن خوشم نیاید، دوباره به بمباران سرشان باز خواهیم گشت.
🔴
همچنین اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به بمباران باز خواهیم گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128646" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: توافق با ایران به دلایل زیادی خوب است، از جمله جلوگیری از دستیابی این کشور به سلاح هسته‌ای، و باز شدن تنگه هرمز تا دو روز اینده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128645" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای هیئت مذاکره کننده هسته‌ای ایران: ما تعهد هسته‌ای نداده‌ایم/ گفت‌وگوی هسته‌ای در مرحله بعد از اعتمادسازی انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128644" target="_blank">📅 14:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: ترامپ به زودی درباره توافق ایران کنفرانس خبری برگزار می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128643" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7edd725a03.mp4?token=PAXkyWL8_gmOhqLWXuj4WEPDv9FGZxPoLHp-gURQP-t7vNOrsnXTjJpsM3DQ-1aUGcDtNI9_pajXLhEwWnR-JJstdcxcZp9vfrd-7KKcG4vrwX0Quh10BCALqJKjNG9KCTwHNDr5GYEVOpDifpR7rO8clz2wCp1RjzCpWGGv92k-ToA3w2MUyDQ18e_XV4GHl-2MAl6u0Hoy5XBdkT6jdQgUMGV1EyxNsRVqVxjj6vYg_u0_l7WzcBytx1hu44IdosVftpP-QSMSrMO6AAHIoIFjVrjzhcgguwJb8xqCtAe_YgW6LPNQoRvL9osI-GcPI1hMIrgbRtnbCOQw3xeSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7edd725a03.mp4?token=PAXkyWL8_gmOhqLWXuj4WEPDv9FGZxPoLHp-gURQP-t7vNOrsnXTjJpsM3DQ-1aUGcDtNI9_pajXLhEwWnR-JJstdcxcZp9vfrd-7KKcG4vrwX0Quh10BCALqJKjNG9KCTwHNDr5GYEVOpDifpR7rO8clz2wCp1RjzCpWGGv92k-ToA3w2MUyDQ18e_XV4GHl-2MAl6u0Hoy5XBdkT6jdQgUMGV1EyxNsRVqVxjj6vYg_u0_l7WzcBytx1hu44IdosVftpP-QSMSrMO6AAHIoIFjVrjzhcgguwJb8xqCtAe_YgW6LPNQoRvL9osI-GcPI1hMIrgbRtnbCOQw3xeSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوت ترامپ از خبرنگاران برای ماندن در جلسه و اخراج آنها توسط مکرون
🔴
در نشست سران گروه هفت در فرانسه، ترامپ به خبرنگاران گفت که می توانند در جلسه بمانند، اما مکرون با اشاره آنها را بیرون فرستاد. این لحظه در حالی ثبت شد که مکرون پیشتر در گفتوگویی محرمانه با زلنسکی به تنش با ترامپ اشاره کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128642" target="_blank">📅 14:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: هر کس دست به اقدامی علیه دولت اسرائیل در غزه، لبنان، سوریه یا هر جای دیگری بردارد، بداند که باید بهای آن را بپردازد.
🔴
اول از همه، زمین را از دست می‌دهند. خانه را از دست می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128641" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc741d924e.mp4?token=EjhPqEmcG53ibRnlQqkH9wMaIt7reLaF2N_hiu-ZJioXC7evwY_5vv8MGul9hVsw-Ethgn_VIsiwPkBN_g-Xu9Vm5al90ylC_6QXCEdRQ5RCdBo99-rYwv6-4TIlSUfZ9x2lutdtjXCQB2QR9iZ5-yQGuShEVMV0VQ5M6tE-sNxEPHdDt7GYUSwC94p-h5I3u3jHszCjh5JBjcUqzZmsICOqKerwuqKjLTkdgdCim-2Su0G3vRwK577iakg7LtnZZqRR15_LxEi33UjlG5SYdGIVDGY0kGC9WAFYlEplEYzWZ1ENev84aeUIVu_Y-8yPY-KwgDEQNtMTopVEJ9s6nlu_IiGkNB17d4AjDqsKdhqdV63fyF-TrMojfZbARtsGKf85rCtEIhj5k0ez5iVrjaHRuPtQ8FlTnM7HrmlNw5I42CUCjzfXj-MRaFLsKSBZT3TbHRoXJWCUZlxj0HT8FaBwVoLO9XbsJB3eYcLEhOaeUuo7POh3MIIeyfWvvexejA8TpyFzDWosAwHUbbxFeM0nOA25Cpp8Q6veHQD7hXIrRkbTyhWbfkl45-jzaPM9h-ZY0QgJjE7k29t6xINZEf1EqU5hdlsIvvSeKxnGQ6ETS0O6M9FO1GLYHJmL9NH6T2geBFWMxd7_45id_zg6AgAa_tpwyYAXjQLW79IjR8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc741d924e.mp4?token=EjhPqEmcG53ibRnlQqkH9wMaIt7reLaF2N_hiu-ZJioXC7evwY_5vv8MGul9hVsw-Ethgn_VIsiwPkBN_g-Xu9Vm5al90ylC_6QXCEdRQ5RCdBo99-rYwv6-4TIlSUfZ9x2lutdtjXCQB2QR9iZ5-yQGuShEVMV0VQ5M6tE-sNxEPHdDt7GYUSwC94p-h5I3u3jHszCjh5JBjcUqzZmsICOqKerwuqKjLTkdgdCim-2Su0G3vRwK577iakg7LtnZZqRR15_LxEi33UjlG5SYdGIVDGY0kGC9WAFYlEplEYzWZ1ENev84aeUIVu_Y-8yPY-KwgDEQNtMTopVEJ9s6nlu_IiGkNB17d4AjDqsKdhqdV63fyF-TrMojfZbARtsGKf85rCtEIhj5k0ez5iVrjaHRuPtQ8FlTnM7HrmlNw5I42CUCjzfXj-MRaFLsKSBZT3TbHRoXJWCUZlxj0HT8FaBwVoLO9XbsJB3eYcLEhOaeUuo7POh3MIIeyfWvvexejA8TpyFzDWosAwHUbbxFeM0nOA25Cpp8Q6veHQD7hXIrRkbTyhWbfkl45-jzaPM9h-ZY0QgJjE7k29t6xINZEf1EqU5hdlsIvvSeKxnGQ6ETS0O6M9FO1GLYHJmL9NH6T2geBFWMxd7_45id_zg6AgAa_tpwyYAXjQLW79IjR8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: تمام روستاهای نزدیک به مرز لبنان به صورت سیستماتیک ویران می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128640" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ اختیارات ویژه‌ای به هگست برای افزایش تولید تسلیحات داد
🔴
بر اساس یادداشتی که در اختیار ریانووستی قرار گرفته، دونالد ترامپ، اختیاراتی را به پیت هگست، وزیر جنگ آمریکا واگذار کرده است تا مشکلات موجود در حوزه تولید تسلیحات را برطرف کند
🔴
ترامپ تأکید کرده است که استفاده از این سازوکار ضروری است، زیرا آسیب‌پذیری زنجیره‌های تأمین و گلوگاه‌های تولیدی می‌تواند روند تولید مهمات، موشک‌ها و تجهیزات نظامی مورد نیاز برای دفاع کشور را با مشکل مواجه کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128639" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYgBnV7F14G5QMr1BpQ2VmyhNqqZdRIu4UxrZbwZELbAWYN-FXuVkC-f_4AOfTARQhKKZLgvI7Hmq-fml22D18XTC86sDAcAFT9t_LIZGGUeRWFZoQPScKRrd0mhdVj5xanXPix-9b_WU9VIpwspJ-NRMaE4wKypxTj6HoZ94CS7MrbHQphz4jI86S1ePn_J3KzTA7DklrCwKXysAhTLAo_BdQdrBW3OZ7eP9pxXeeyg9R0MgPqHXXOthriOWsJH51s4LNC4oaEnYdElrEEzx97UzDMqktC6hk2Vum6fh6GrvXSYjx7MJzJovIVjtFkhRxBnevBzaQJnNAiEOMjzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / حملهِ پهپادی حزب‌الله به اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128638" target="_blank">📅 13:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368ad2dab1.mp4?token=WYrNcefkX1z3Izys2OaDwZ6a5dLdaZMR-1Cgm4xGyNzE8sSjKZrjHrQt69YaHbxL-G1_8aT6gW8uMfep2VCpuDDS7zQlnDc-VFpG7v05ndD9Hr7i-bKO5p-Hgu7RQXQW4-eXe2s1evrbKcu9uy2b5jVw4YeC-5sjJbrVFG5FfaG-YsAib7YZOYIhOOVjuBQJViZp_cYs07QWMTgVs60UiK_unhCzgDLBQwAGD6ay91vzca646vxmYl7HDJSfYTJwFnQzYst18dq9O8VeVwJBB4Y7fOiPkBDn9TKDZOn-PaoQEXIjSQZsxxUujONIvx-nQKXmMWsloHE2wWwHjzWGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368ad2dab1.mp4?token=WYrNcefkX1z3Izys2OaDwZ6a5dLdaZMR-1Cgm4xGyNzE8sSjKZrjHrQt69YaHbxL-G1_8aT6gW8uMfep2VCpuDDS7zQlnDc-VFpG7v05ndD9Hr7i-bKO5p-Hgu7RQXQW4-eXe2s1evrbKcu9uy2b5jVw4YeC-5sjJbrVFG5FfaG-YsAib7YZOYIhOOVjuBQJViZp_cYs07QWMTgVs60UiK_unhCzgDLBQwAGD6ay91vzca646vxmYl7HDJSfYTJwFnQzYst18dq9O8VeVwJBB4Y7fOiPkBDn9TKDZOn-PaoQEXIjSQZsxxUujONIvx-nQKXmMWsloHE2wWwHjzWGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب نجم‌الدین شریعتی وسط ویژه برنامه شبکه 3 برای ماه محرم، یهو زد زیر گریه و گفت ؛ من امشب دلم واسه آقا (علی خامنه‌ای) تنگ شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128637" target="_blank">📅 13:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b91d542c6.mp4?token=KaHKW_ER7eCv0eRePAY3hHtFOtXfx7eEreB34LYyoyXUgYLdCnE5A8umlRlYqCMg_K2BZHULqOx7uB-G4knDpzOqU1snkHB4G5llleJs9D2DKPuCjgk5pk5p1XpOQo5RAnJkOmGtZ16rbtnM0zT0hnPOGmSK0H_vUk6ySgxJgfBWfyIHQCLIeGXZPJPDafjfW-pHM78Lo2-ozlf49s1Rw7v77XsDmjS3GJWKDj2fruMLUTAd2STRLg-yPGnRnPOXz3m6gIumdZxHSlP-wHEmIAihYVpRf3Q01JYM_tCm_xa8ttgV2jxBg34HzJR7GP8uywBr4gdGckCUWMWKPBz7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b91d542c6.mp4?token=KaHKW_ER7eCv0eRePAY3hHtFOtXfx7eEreB34LYyoyXUgYLdCnE5A8umlRlYqCMg_K2BZHULqOx7uB-G4knDpzOqU1snkHB4G5llleJs9D2DKPuCjgk5pk5p1XpOQo5RAnJkOmGtZ16rbtnM0zT0hnPOGmSK0H_vUk6ySgxJgfBWfyIHQCLIeGXZPJPDafjfW-pHM78Lo2-ozlf49s1Rw7v77XsDmjS3GJWKDj2fruMLUTAd2STRLg-yPGnRnPOXz3m6gIumdZxHSlP-wHEmIAihYVpRf3Q01JYM_tCm_xa8ttgV2jxBg34HzJR7GP8uywBr4gdGckCUWMWKPBz7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارنی، نخست‌وزیر کانادا : من جزو معدود افرادی هستم که متن تفاهم‌نامه آمریکا و ایران رو دیدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128636" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c1bf45ae.mp4?token=Fs3dT_MIeEHvYScB6Dfhz98jy3qzrDnJb7iuPrdj90CQzxMqqnpbeczGdAj-WNA8pntlV9FDqzdguQ0YGtk3J4bs5eEEL4CaByhIvh2sIqoF5L5_uWem-BYtZcoufSp14W0ss2-wOf534tQxC0NSka9HQ0g16wWK0rPOuGnBZK6Morat3_QIvkvBPmkxDpcDsjUSCHxLf75gRDYR0HSk3SKjqvDYDiKQ2SRXWoTnTfUBG6vVrHfm6ETzT8dd7aLYuu2wOTwh23SQ2YMytdLxjHmsEELgjNoCALEBzEGv1PPjIEst3HGukedL09xBLvVsFPpJDxaJvA-yN2pZ9b4YAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c1bf45ae.mp4?token=Fs3dT_MIeEHvYScB6Dfhz98jy3qzrDnJb7iuPrdj90CQzxMqqnpbeczGdAj-WNA8pntlV9FDqzdguQ0YGtk3J4bs5eEEL4CaByhIvh2sIqoF5L5_uWem-BYtZcoufSp14W0ss2-wOf534tQxC0NSka9HQ0g16wWK0rPOuGnBZK6Morat3_QIvkvBPmkxDpcDsjUSCHxLf75gRDYR0HSk3SKjqvDYDiKQ2SRXWoTnTfUBG6vVrHfm6ETzT8dd7aLYuu2wOTwh23SQ2YMytdLxjHmsEELgjNoCALEBzEGv1PPjIEst3HGukedL09xBLvVsFPpJDxaJvA-yN2pZ9b4YAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلاش بالگرد کاموف52 روسی برای رهگیری پهپاد انتحاری اوکراینی بر فراز مسکو طی حمله صبح امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128635" target="_blank">📅 13:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مارک روته دبیرکل ناتو: از توافق حاصل شده توسط رئیس جمهور ترامپ با ایران استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128634" target="_blank">📅 13:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک مقام آمریکایی به بلومبرگ گفت:
«ایران از مزایای توافق بهره‌مند نخواهد شد مگر اینکه به تعهدات خود عمل کند.
🔴
تعهدات ایران شامل نداشتن سلاح‌های هسته‌ای، خنثی‌سازی مواد غنی‌شده و تضمین آزادی ناوبری در تنگه هرمز است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128633" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
صدای شنیده شده در سیریک مربوط به خنثی سازی مهمات جنگی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128632" target="_blank">📅 12:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرگزاری تسنیم : متن تفاهم‌نامه بعد از امضای روز جمعه منتشر میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128631" target="_blank">📅 12:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1x_K4j7ZRGbTl5shxBstv-2qlMZ1ALE8mOn-BuIY2IY7USf_YKPpMTRgbyyWqIgR3uNzDtY39btsVFvwuv0VFTOn9JbtVL08YjPWh6IWAirF-dT-nryivb85rPuMsNbwb_XRERTIPsuIP59gJCkrMQpME5z2Dh7lNr3_2fCAmHcjR1-rvIEpaqfLvqeLjyC2CwTngu6w7tpQOrNLDd6RU0SfAmkn1F9PHFYXYzAIup_FzlRoLCxat8BNDXK3ja79tpozrMQw1x8lNRCwvXzoI4cqweLUkBBaDTGdKzHwPxrWFt_BP6ihL0dgcD_SurSLcz4jE9NRBcBmR4WNOJ72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با کاهش قیمت دلار ، مدیرعامل ایران خودرو درخواست افزایش قیمت خودر ها رو ارائه داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128630" target="_blank">📅 12:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYkhqY_Ppi_Ee07nw2FPrJIyzIgj1Jb5FQW4h1llSqUOAjRLawM2i-GW8PNjYbYVMQ9coSUnxwA264YVcmDs-pV1ntJA4AA9j5OeLj_AJyLITN_6IhAIS0bOpDSR0WqkTxJWv4FpHsEG_ZOIonU4PnbYlgc1GzlnND8tyDH8VGWNkXviRGAAo6BxSujzaLVM-pBM9qiHmCs-Z72466CInEobJnMRxgb6uPZlMCIPf4c9WkyPn0knltzVtsyv7EzXbMjsI8RX98kthEtRmwbMZJuqNDBkm2_aiIeaeBXVJPblFP8FSKoDiVaqhakmyzngU0bpLjt5G3fODo77gHMkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۵۱ هزار واحدی به ۵ میلیون و ۱۵۱ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128629" target="_blank">📅 12:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یه زوج پزشک ایرانی ۳۱۳ عمل جراحی رایگان رو به عنوان مهریه ازدواج خود ثبت کردن، یعنی بخوان طلاق بگیرن طرف باید چندسال رایگان کار کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128628" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ۱۳۰ میلیارد دلار ارز صادراتی به کشور برنگشته،
ارزهای برنگشته چند برابر دارایی‌های بلوکه‌شده ایران است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128627" target="_blank">📅 12:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک منبع آگاه اعلام کرد: واشنگتن شروع به توزیع محتوای تفاهم با ایران به کشورهای متحد در اجلاس گروه ۷ در فرانسه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128626" target="_blank">📅 12:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت خارجه: عراقچی در تماسی با لاوروف درباره یادداشت تفاهم با واشنگتن گفت‌وگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128625" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک منبع آگاه: وزارت خزانه‌داری آمریکا بلافاصله پس از امضای توافق، معافیت‌هایی برای نفت و پتروشیمی ایران صادر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128624" target="_blank">📅 12:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هاآرتص: به ارتش اسرائیل دستور داده شده که از حملات گسترده در لبنان خودداری و بر حفاظت از نیرو‌های خود تمرکز کند.
🔴
ممکن است ارتش ناچار شود به «خط زرد» در جنوب لبنان عقب‌نشینی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128623" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ: تعدادی از کشتی‌های مرتبط با ایران، همزمان با آماده شدن تهران برای امضای توافق، موقعیت‌های خود را جهت فروش نفت تغییر داده‌اند
🔴
دو کشتی حمل فله، یک کشتی حمل گاز طبیعی مایع و یک کشتی کانتینری، در حال حرکت به سمت خارج از تنگه هرمز یا خلیج عمان مشاهده شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128622" target="_blank">📅 12:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
در بریتانیا به‌زودی استفاده از ۱۰ شبکه اجتماعی معروف برای نوجوانان زیر ۱۶ سال ممنوع خواهد شد: تیک‌تاک، یوتیوب، اسنپ‌چت، اینستاگرام، ایکس، ردیت، فیسبوک، توئیچ، کیک و تردز
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128621" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
در بریتانیا به‌زودی استفاده از ۱۰ شبکه اجتماعی معروف برای نوجوانان زیر ۱۶ سال ممنوع خواهد شد: تیک‌تاک، یوتیوب، اسنپ‌چت، اینستاگرام، ایکس، ردیت، فیسبوک، توئیچ، کیک و تردز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128620" target="_blank">📅 11:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کارشناس صدا و سیما: جمهوری اسلامی قوی ترین حکومت تاریخ ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/128619" target="_blank">📅 11:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
غضنفری، نماینده مجلس : اسرائیل بعد امضای توافق، دوباره حملهِ میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128618" target="_blank">📅 11:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ :  تحریم‌های روسیه که تا حدودی به دلیل جنگ ایران و با هدف کاهش قیمت نفت لغو شده بود، می‌تواند بار دیگر اعمال شود
🔴
دونالد ترامپ رئیس‌جمهوری آمریکا در نشست گروه هفت از احتمال بازگرداندن تحریم‌های نفتی علیه روسیه پس از دوبار معافیت خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128617" target="_blank">📅 11:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نخست‌وزیر کانادا: توافق ایران و آمریکا قاعده بازی را تغییر داده
🔴
نخست وزیر کانادا در گفت و گو با شبکه خبری سی ان ان با اعلام اینکه نسخه ای از توافق ایران و آمریکا را دیده، گفت که این سند قاعده بازی را تغییر داده و "ورق را بر می گرداند. "
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128616" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران، 154 هزار و 500 تومان معامله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128615" target="_blank">📅 11:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یوهان واده‌فول وزیر امور خارجه آلمان اعلام کرد کشورش در صورت شکل‌گیری عملیات مین‌روبی در تنگه هرمز آمادگی مشارکت دارد، اما این اقدام تنها با موافقت هم‌زمان ایالات متحده و ایران، وجود چارچوب حقوقی بین‌المللی و تایید نهادهای اروپایی و پارلمان آلمان امکان‌پذیر خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128614" target="_blank">📅 11:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
طبق اعلام وزیر خارجه پاکستان محمد اسحاق‌دار، با کمک این کشور ۳۰ تبعه ایرانی، شامل خدمه یک کشتی توقیف شده توسط آمریکا به ایران برگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128613" target="_blank">📅 11:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرگزاری فرانسه: یک گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گروک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک، میلیاردر حوزه فناوری در جنگ غیرقانونی علیه ایران استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128612" target="_blank">📅 11:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzbrLHCdoNwtoNfOyNnPtyIrLrnXIlNEN-ISIa3a_e5jUzRWnz4yXsowWJOItVkZe2cWaNyisSDQiID8gX4AEoxjlIxxnQXKPum19g4VD6IaTePa-5-W60XtwYNvO9Vubiq8jdb_CIpbMsQBpium34giIPuWbiFOP_Xlg-uRGUE3Bd9S60ZwqV04y0ADziwgZYsSkL2ztkVqevujPR-BhOd_fCPsvPULraUAXtCTqcWG6FKJoxit6Ie_sz3BztsB9U24CLBL5joJsdGh9-kaUqv1fKaCEFwL_Vgkw2lwKtWcW-7atsqh7_AqsQlCwdLAO4YUwDLI6-Zg3AudgiDbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مارکو روبیو پس از اعلام خبر توافق تو این چند روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128611" target="_blank">📅 11:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844516bd22.mp4?token=bMyX5vXRiAAnbGIusieuSXokfFpo154MwlHB2u8KDRcrx146iPZGBluSEvSjTL9kY_6MgbLzCjFK37z1f-_cXMZBllDEYwPe6-wXszswq6XAgbRxf0W6clEcV7qINNNqhIy-llvrbuIw3fYl60LGQZ8A1xMU-IiW6A9wUYknj9aY0XFghC4yozERiYMSz5euS7f0yDR-wSvh9wn9qSY3WzyJh1v2WzYN3d04SioArLKG6W5kvtWEWKjQDi1Xrb8mAFTzUfo4ITrKWohk24rn7av54PZFva2wfqlLTPVhJ9xA_LwgNzrNbqAfNgd5fcjZkWQ7piUUmxA4B8gh7J7LzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844516bd22.mp4?token=bMyX5vXRiAAnbGIusieuSXokfFpo154MwlHB2u8KDRcrx146iPZGBluSEvSjTL9kY_6MgbLzCjFK37z1f-_cXMZBllDEYwPe6-wXszswq6XAgbRxf0W6clEcV7qINNNqhIy-llvrbuIw3fYl60LGQZ8A1xMU-IiW6A9wUYknj9aY0XFghC4yozERiYMSz5euS7f0yDR-wSvh9wn9qSY3WzyJh1v2WzYN3d04SioArLKG6W5kvtWEWKjQDi1Xrb8mAFTzUfo4ITrKWohk24rn7av54PZFva2wfqlLTPVhJ9xA_LwgNzrNbqAfNgd5fcjZkWQ7piUUmxA4B8gh7J7LzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادامه حملات ارتش اسرائیل به نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128610" target="_blank">📅 11:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2nhClYVhQAizrgH7hvRquo6skugGQ9rrWVSCkU2X1YG7jrPJo82I2xhVQteJfEa9KL9F7HyNMSqqwD6afM14vs97Xm1Gl_eoBjQmeQ7s0Q9qlFAB6ZfLcLrkPc_E2c8gdg9TJTO1MKDvWa_o-x2Aeo_qg0Xx6QVEWbcP82_44MR_RKv9mxgQm9nAUSECeL63EFbtRTrCUc3mlpgg_xPvfwLmmwz6EQoX3Fy7c-xIVlDpuX-btnIq4tcg7NBqNI3Vt3EdO-ehScaTWrRQINOX769oVlX3igqoEJeE3Sq3WvU8DLM0sO0XnXgJl8neZH7587r7WFIyszEpVyAj5xNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت با ادامه روند کاهشی خود امروز ۷۸ دلار معامله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128609" target="_blank">📅 11:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVDKUglvlOxSwRc-RiBVmhLevCYrpiVos5abkJATo-mroBFmTjcwEhWp00g_1OwZN3_gC53lMewn-_3miOlQADCEFu7r4Qe11mU6F0VZFamIYyvs0lxRER84k-2xT8gMZ-BR27gEFXqbvGAVg8ldkRNzXDSYLzxHYPjf4OpB2TtSRD87aAwzM3_jhTRIKDC4Mmi6j4yUqw-0AG1dhv91Do9Xm2ySq4xpOaDz5CZUa3uLFcueB2yP3XtS7IvYP1sbOv63vWWtrRR8g8M21TnffGPa_zK4c10Tbk7lFYepB10jVUbzOcde1AE6sJ-BO8EIj8DWM8Hfm3tFm_nXrwNo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ای بی سی: رضا پهلوی ۱۰مرتبه درخواست دیدار با ترامپ را داشته که تمام درخواست‌ها رد شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128608" target="_blank">📅 10:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03e93ff7.mp4?token=crh1u9-jBjqsF1u_0_LAg6mJUmYp1VwrUwhsg6KWxZ13loezPFGX1fap1OOXoc9yA02BRnXc6LTiWLuPrAwqfEqma8uLUrHswrhG16gnLK8akLyQBMUWCCRKEqzReG1UWsl_VblJZud4Z8oxqfT6H_bDBLDmBS6WVQLu83PQ6bfGemoI6KvMHYDjJ4GIy-BEmar5CFqx8xy2d-SDoN2DkX03wjrYe4bHcxOmjKfyCSABClI-idEgOPMwkwEZjdRRcTAdDxbEakpHkyHI4rKYwPR5oGu7M3YlWwgI25KBSY6rUuLKGh0KGXJOlce0dS0VB7uNKaJ4W3anxeN1KoHcsL0waJyp86C6q9kLXay1D7__lX5OZYe3nBg1W-E4yU2MmaaWmah1ctb1Gt65syOYBK4Ftmg0YuFct0t2FqwJvN6unOJuepmrBdJ1YSx-D9Bb2uT6bjSF_0a9GSjPCzD5m88bsdjaoyyIzQoUyQ_beQ6ZS60wyUGbeB0XFJpbYJ-Scr86wNPaB-xKaiD9bWoBKKUXsYzbwzg7_xtvlgP6bFBN0dic_wPtmj7s1SyHeXZw5LN3dr6ho1CMOtU_yOkmZc3Atte2MzTxn95lOCtAWYRTSpqyRg8kh3voGkmt39TBjN0Ld__DepwQF4HB3KoXd7q1ZLcT3y0rmWnyyGeaDys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03e93ff7.mp4?token=crh1u9-jBjqsF1u_0_LAg6mJUmYp1VwrUwhsg6KWxZ13loezPFGX1fap1OOXoc9yA02BRnXc6LTiWLuPrAwqfEqma8uLUrHswrhG16gnLK8akLyQBMUWCCRKEqzReG1UWsl_VblJZud4Z8oxqfT6H_bDBLDmBS6WVQLu83PQ6bfGemoI6KvMHYDjJ4GIy-BEmar5CFqx8xy2d-SDoN2DkX03wjrYe4bHcxOmjKfyCSABClI-idEgOPMwkwEZjdRRcTAdDxbEakpHkyHI4rKYwPR5oGu7M3YlWwgI25KBSY6rUuLKGh0KGXJOlce0dS0VB7uNKaJ4W3anxeN1KoHcsL0waJyp86C6q9kLXay1D7__lX5OZYe3nBg1W-E4yU2MmaaWmah1ctb1Gt65syOYBK4Ftmg0YuFct0t2FqwJvN6unOJuepmrBdJ1YSx-D9Bb2uT6bjSF_0a9GSjPCzD5m88bsdjaoyyIzQoUyQ_beQ6ZS60wyUGbeB0XFJpbYJ-Scr86wNPaB-xKaiD9bWoBKKUXsYzbwzg7_xtvlgP6bFBN0dic_wPtmj7s1SyHeXZw5LN3dr6ho1CMOtU_yOkmZc3Atte2MzTxn95lOCtAWYRTSpqyRg8kh3voGkmt39TBjN0Ld__DepwQF4HB3KoXd7q1ZLcT3y0rmWnyyGeaDys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل اسموتریچ:
در غزه، ما همچنان به پیشروی خود ادامه می‌دهیم. امروز کمی جلوتر رفتیم. ما در حال حاضر به 70 درصد نزدیک می‌شویم.
🔴
ما تقریباً 70 درصد نوار غزه را کنترل می‌کنیم.
🔴
غزه ویران شده است.
🔴
بدون غیرنظامی شدن، هیچ بازسازی‌ای وجود نخواهد داشت.
🔴
ما اکنون در حال آماده‌سازی چندین طرح هستیم زیرا باید حماس را نابود کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128607" target="_blank">📅 10:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
انهدام مهمات عمل‌نکرده در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128606" target="_blank">📅 10:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بلومبرگ: آمریکا آماده است در توافق صلح، منافع مالی گسترده‌ای به ایران ارائه کند؛ مانند حق فروش فوری نفت، دسترسی به صندوق توسعه‌ ۳۰۰ میلیارد دلاری و دارایی‌های مسدود شده خود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128605" target="_blank">📅 10:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر خارجه چین: توافق فعلی بین ایران و آمریکا آغاز راه است، نه نقطه پایان
🔴
وانگ یی در گفت‌و‌گو با همتای پاکستانی خود: توافق فعلی، آغاز راه است، نه نقطه پایان؛ از این رو، تداوم صلح در خاورمیانه و منطقه خلیج فارس همچنان به تداوم تلاش‌های همه طرف‌ها نیاز دارد.
🔴
چین نیز به روش خود به میانجیگری بین ایران و آمریکا پرداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128604" target="_blank">📅 10:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1b58f4916.mp4?token=kJ0np1SDLDwKxnYSEHpmt--0KdjU86nRYn3tTjAcmtXuQ2qrsPoGL-GbBAulM4CgN0lIgnTo2dMV1h8hyrQ6wmR9iKKm2Q71qpzSF6g1x3DOzuwWJiSzHe40kxnZ2JSTaqfcVMqbXyJ6FWX7lFD1F7CnV36dlvKh20ETOvqLR5OWMl5mK8SY3UnOxmGh5HkUeS2KJCE32G1yxEXTlU3pxgK9CQFLDgnCAHjyUxfGbocyoKrYoUJJVGO_LNz0VxF6pNvdTKMRqQvyeRh9kXidkt2beddaucGPwt--fbMp7vpNAbzkfcGEWlnADj1rz0i10BLELP5fHseLThwp9MWGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1b58f4916.mp4?token=kJ0np1SDLDwKxnYSEHpmt--0KdjU86nRYn3tTjAcmtXuQ2qrsPoGL-GbBAulM4CgN0lIgnTo2dMV1h8hyrQ6wmR9iKKm2Q71qpzSF6g1x3DOzuwWJiSzHe40kxnZ2JSTaqfcVMqbXyJ6FWX7lFD1F7CnV36dlvKh20ETOvqLR5OWMl5mK8SY3UnOxmGh5HkUeS2KJCE32G1yxEXTlU3pxgK9CQFLDgnCAHjyUxfGbocyoKrYoUJJVGO_LNz0VxF6pNvdTKMRqQvyeRh9kXidkt2beddaucGPwt--fbMp7vpNAbzkfcGEWlnADj1rz0i10BLELP5fHseLThwp9MWGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پنس، معاون سابق ترامپ: «به نظر من بهتر است به نیروهای مسلح ایالات متحده اجازه دهیم کار را تمام کنند، تنگه را باز کنند و قابلیت‌های تهاجمی ایرانیان را از بین ببریم و به مردم ایران فرصتی واقعی برای آزادی بدهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128603" target="_blank">📅 10:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe43e0026a.mp4?token=q2eL1caH6gyzFQcVkhcnul2M9TyddQ6yBIOydl0ADlY_aebFytl-z78U9UHHxWb7rLxzHyrEIFn4Y8qpOJXwQ-byK4XJ50xTCDOIcgcsTCRqNMVM1czgA1n-CWC9Rfjq1ts6aqiYx40tOmF1gH51DuMwjfhbyT-aDzdGuX7671V3om99v-5rGqYEXAerYwNu6PBIvMWGDhe3ArCT3_dxMf-HtEW49NCh4WQYmAgRywrUm5-vbm6qzYNHa3biHDR0Gz5yZK7X02wC6l6RPQo3gXce4IHl2r_SNsaxXHsiwgssJHAlm_JqJ8Nn573q-rmL0eDN_ygI1n6_2n9723LP2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe43e0026a.mp4?token=q2eL1caH6gyzFQcVkhcnul2M9TyddQ6yBIOydl0ADlY_aebFytl-z78U9UHHxWb7rLxzHyrEIFn4Y8qpOJXwQ-byK4XJ50xTCDOIcgcsTCRqNMVM1czgA1n-CWC9Rfjq1ts6aqiYx40tOmF1gH51DuMwjfhbyT-aDzdGuX7671V3om99v-5rGqYEXAerYwNu6PBIvMWGDhe3ArCT3_dxMf-HtEW49NCh4WQYmAgRywrUm5-vbm6qzYNHa3biHDR0Gz5yZK7X02wC6l6RPQo3gXce4IHl2r_SNsaxXHsiwgssJHAlm_JqJ8Nn573q-rmL0eDN_ygI1n6_2n9723LP2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت خودپرداز بانک با لیفتراک در بریتانیا
🔴
سارقان با یک لیفتراک تلسکوپی شبانه به شعبه بانک در کمبریج‌شایر رفتند و دستگاه خودپرداز را از دیوار کندند. پلیس اعلام کرد لیفتراک هم سرقتی بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128602" target="_blank">📅 10:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ونس:  اگر ایران همان راهی را که عربستان سعودی رفت طی کند، ایالات متحده کمک خواهد کرد که کشوری موفق باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/128601" target="_blank">📅 10:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل:توافق با ایران بد است
🔴
ترامپ از منافع کشور خودش محافظت می‌کند و ما از منافع خودمان
🔴
باید بدانیم که چگونه این بحران را مدیریت کنیم و در عین حال، بر مواضع خود بایستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128600" target="_blank">📅 10:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45fe35652.mp4?token=IhRO0g0tdRzt7w3C1c966wEtvn0Sc_hM-fUP9HvxLVYgKiJwMbnM8VDe_suFaxTDrSV6mQQ-KxnGozx_qYl2EnuRjyEm5L2PGoLTU0FhdTKq17-eBO70iyrlVDjHpzquTgz9FN4k9QDXDuC_n4eGmT6x2iH1gmX8by0hCh-nWF-dKCaASB0KF1tbhqkJhMgARS1g7mWIafci73r0XgMz2EBrAxR9Xhx9XtIr5Jyy0wxc4iOs7ifu8PfXc7vgFJ_EKO00jfABA7zgYlozzMxCsvw6IKhBxOcpBQqrliRAny0YsS_GM00GTX2crhpAffgoHxzBgtVyj8nyxMmKNYjd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45fe35652.mp4?token=IhRO0g0tdRzt7w3C1c966wEtvn0Sc_hM-fUP9HvxLVYgKiJwMbnM8VDe_suFaxTDrSV6mQQ-KxnGozx_qYl2EnuRjyEm5L2PGoLTU0FhdTKq17-eBO70iyrlVDjHpzquTgz9FN4k9QDXDuC_n4eGmT6x2iH1gmX8by0hCh-nWF-dKCaASB0KF1tbhqkJhMgARS1g7mWIafci73r0XgMz2EBrAxR9Xhx9XtIr5Jyy0wxc4iOs7ifu8PfXc7vgFJ_EKO00jfABA7zgYlozzMxCsvw6IKhBxOcpBQqrliRAny0YsS_GM00GTX2crhpAffgoHxzBgtVyj8nyxMmKNYjd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جوریه که حتی رهبر جمهوری خواهان سنا هم مثل من و شما از مفاد تفاهم نامه خبر نداره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128599" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bcf91b13.mp4?token=Y7TRuq8OACU3pjkoUErMLHJCHnPgA3pPIKDglhyCAc0fdiITUJaOdqBV5mtSueEqggHVYEZszxjTW3NaApbuuGR8kgv7QXRw2prjpnHrEPfE7dFHVpeCpkuu3_vk-WMlIKVEiJg3PvTuaw65xDHF-_ud34f6-SgG8BaaSKxJtUSvzVrjMMW9loHgNdZmgxay7kOKR3J2528l85TtkmJ4TU3VBLwXAiA7YrShFUaZuecgyxY3-_jpr2UAdNe5eEEUVQaZ1Od5W3jA_00pgP2sfs-y2-PY5MifA1W7ANNkpIQ3Vzqz6lZ5-dvqmTgfUUEJK3oeu_YxZBpRHyjpf2cBgFLozLDNQoaE5VmCk2mK-TuwVCMNqIj4W5VBIcaYFqlKpzMdc2Bm3spllsPaMnZWbhuoxjuShlHpce6Yf27arG1z5D6fMMS7iW7uuHOwXQPmR7WJqmUDCkV2kmIRllX5j3RAY1bkuky4lTgcJ4g3GNELKR1OgzDdtJZPuo11nJkFiIOZLSTxVp1ZMO7srGonyzavUDF0GWkFtMdXtwrOnL0ZKA7NRO10y0vZtOJRGHyksEWD6gW_9eW4EzljyHDVIP9ircqPysZTOBQFCs48XjpafQBWvBufI8-Gvnm7_FHRExZukatu9dd0EI-WgffQfLDsnDBpD2A0bsOtZ2Xzm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bcf91b13.mp4?token=Y7TRuq8OACU3pjkoUErMLHJCHnPgA3pPIKDglhyCAc0fdiITUJaOdqBV5mtSueEqggHVYEZszxjTW3NaApbuuGR8kgv7QXRw2prjpnHrEPfE7dFHVpeCpkuu3_vk-WMlIKVEiJg3PvTuaw65xDHF-_ud34f6-SgG8BaaSKxJtUSvzVrjMMW9loHgNdZmgxay7kOKR3J2528l85TtkmJ4TU3VBLwXAiA7YrShFUaZuecgyxY3-_jpr2UAdNe5eEEUVQaZ1Od5W3jA_00pgP2sfs-y2-PY5MifA1W7ANNkpIQ3Vzqz6lZ5-dvqmTgfUUEJK3oeu_YxZBpRHyjpf2cBgFLozLDNQoaE5VmCk2mK-TuwVCMNqIj4W5VBIcaYFqlKpzMdc2Bm3spllsPaMnZWbhuoxjuShlHpce6Yf27arG1z5D6fMMS7iW7uuHOwXQPmR7WJqmUDCkV2kmIRllX5j3RAY1bkuky4lTgcJ4g3GNELKR1OgzDdtJZPuo11nJkFiIOZLSTxVp1ZMO7srGonyzavUDF0GWkFtMdXtwrOnL0ZKA7NRO10y0vZtOJRGHyksEWD6gW_9eW4EzljyHDVIP9ircqPysZTOBQFCs48XjpafQBWvBufI8-Gvnm7_FHRExZukatu9dd0EI-WgffQfLDsnDBpD2A0bsOtZ2Xzm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره ایران: دلیل اینکه متن تفاهم‌نامه را منتشر نکرده‌ایم این است که برخی از میانجی‌های ما؛ پاکستانی‌ها و قطری‌ها؛ از ما خواسته‌اند که این موضوع را به ترتیب درست انجام دهیم.
🔴
حساسیت‌هایی در جهان عرب و مسلمان وجود دارد که ما در تلاشیم به آن‌ها پاسخ دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128598" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a337c7ba.mp4?token=ZJ17jScNpvBJUA50so5-8KEcg7HPMlaUBYK18NajD7PdZEXMGqAjlIHRwP9bAVGF8M2oh9rXVwqNJzdyUFaW3AISSQNqf2r2qKmsE4M2tjchGGcI0QxrrLuwH_e4Fg1cAaN-Q4PmBHR5vYyHAejnbddQ2RyZn7s_paQ0TMuM3XJUMaFJKxN-nhiEgIxoq5GTFmjWkRz70e3fv13LuOYujgWHhD_z1SBJxdwybGYpS7U4Me2peOAQwEodx4CCg2SZ4UHiF8RgWvlLffk2AXOEVnhWMCyWNATNhSc_x7Ebj3B-NhFP4vx70zxdodRHakBdQATQ7HILu6XbJtFtfDpz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a337c7ba.mp4?token=ZJ17jScNpvBJUA50so5-8KEcg7HPMlaUBYK18NajD7PdZEXMGqAjlIHRwP9bAVGF8M2oh9rXVwqNJzdyUFaW3AISSQNqf2r2qKmsE4M2tjchGGcI0QxrrLuwH_e4Fg1cAaN-Q4PmBHR5vYyHAejnbddQ2RyZn7s_paQ0TMuM3XJUMaFJKxN-nhiEgIxoq5GTFmjWkRz70e3fv13LuOYujgWHhD_z1SBJxdwybGYpS7U4Me2peOAQwEodx4CCg2SZ4UHiF8RgWvlLffk2AXOEVnhWMCyWNATNhSc_x7Ebj3B-NhFP4vx70zxdodRHakBdQATQ7HILu6XbJtFtfDpz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره ایران: ایرانی‌ها در موقعیتی هستند که می‌گویند می‌خواهند تعهدات بلندمدتی به ایالات متحده و کشورهای عرب خلیج فارس بدهند تا رابطه‌شان را تغییر دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128597" target="_blank">📅 09:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62be1a9ab.mp4?token=GrGap3bHLjelKp_kOV9UtkAJmFjlgT2WBxVwD-PJWx0fPrKpVeU60Wl3EkIm00y83fIR_hL-PpQRaGjsVqJxQCD1Z8-RO1HCNctdiixHUUQM-9vfgrQx50orUeGI_R_RJMTwEwwKVXwRLcx19MyJFtjSKJvMBzXcHFFryv08fyuecloykXWPIBpUTF8HR_2CkVVSQ_nN9pkW8ur9yMt96nhDLLUALldchmdDgrQ4AmDgYtRUTNi0oZhz5M-_BrmcGfzUTyPYg71rGjIPqE_uuXBbZS8ZFaOqcEn6DR-bkkfzXYRIgfIfiK7zexasWJQsxdahpMkZY0WldZ8XQ_Zz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62be1a9ab.mp4?token=GrGap3bHLjelKp_kOV9UtkAJmFjlgT2WBxVwD-PJWx0fPrKpVeU60Wl3EkIm00y83fIR_hL-PpQRaGjsVqJxQCD1Z8-RO1HCNctdiixHUUQM-9vfgrQx50orUeGI_R_RJMTwEwwKVXwRLcx19MyJFtjSKJvMBzXcHFFryv08fyuecloykXWPIBpUTF8HR_2CkVVSQ_nN9pkW8ur9yMt96nhDLLUALldchmdDgrQ4AmDgYtRUTNi0oZhz5M-_BrmcGfzUTyPYg71rGjIPqE_uuXBbZS8ZFaOqcEn6DR-bkkfzXYRIgfIfiK7zexasWJQsxdahpMkZY0WldZ8XQ_Zz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای "سسنا ۶۸۰ سایتیشن لاتیتود" هنگام ورود به تگزاس منفجر شد
🔴
تیم‌های اورژانس به سرعت به محل حادثه رفتند.
🔴
ورود به پنجره کابین خلبان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128596" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057ad2526c.mp4?token=IpbCQ1H7c2WXWKlqfw97IS6AYWq16xG7AlB-1kChetQ3qtJvhueNWMCj2vACVAhaidz_7JOR4bGnciRauV8ZWA-sVhpX3KfSS15oZFYyaViXL24UjpZ3IkSkHVyoG2Si-LRAEPy3_tMm6EkTdoWrhlIisGK8BXe-ietO5jpF3XuVPs8QhqFabcPAUfB10F9muniePGLrEbOWi_tvtv_OqI8KQQZNHyGs-sX9ctcHt5TzvhzFLHw2aQ3izHksgK-lHstczKvjC_UNpf9XPeC3UeL7wkQMZBBucW2G5WGokgndK-oISzSzV7QJfieTybduQZ2yWoa5IGtukdT6i3YTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057ad2526c.mp4?token=IpbCQ1H7c2WXWKlqfw97IS6AYWq16xG7AlB-1kChetQ3qtJvhueNWMCj2vACVAhaidz_7JOR4bGnciRauV8ZWA-sVhpX3KfSS15oZFYyaViXL24UjpZ3IkSkHVyoG2Si-LRAEPy3_tMm6EkTdoWrhlIisGK8BXe-ietO5jpF3XuVPs8QhqFabcPAUfB10F9muniePGLrEbOWi_tvtv_OqI8KQQZNHyGs-sX9ctcHt5TzvhzFLHw2aQ3izHksgK-lHstczKvjC_UNpf9XPeC3UeL7wkQMZBBucW2G5WGokgndK-oISzSzV7QJfieTybduQZ2yWoa5IGtukdT6i3YTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حمله هوایی اسرائیل به النبطیه الفوقا و شلیک موشک به اطراف کفرتبنیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128595" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شریعتمداری: درگیری ما و امریکا، ماهوی و وجودی است؛ تفاهم اخیر، اصل درگیری ما را تغییر نمی‌دهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128594" target="_blank">📅 09:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128593">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
با فعال شدن کریدور جدید دریایی بین قشم و عمان پس از جنگ، محموله‌های خودروهای خارجی به این جزیره سرازیر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128593" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128592">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daZ2RRm0IIj0mBSZmcRZgjPAA6zxznahoBBqYW0QxjMMVG4_TMumT2rYn1YcGUkNMwJd4hRC6_Cw4XSbGL3rsaUifVwfIQmbA_l4fgrKkPl_CpivnK3GWEpgFGSA1L-oM_nEYX-Ysd9P5XNSfnW7gSRp5Yv-oxS8SjOf-DOUj9rZNjr7xTqpVCAtNE1iXEkOkkyn4kBOd7qFUuQxAcXmR-a32VUMY69H28gni6za_N70M-S5Z5s-GPThM0qEz4sNzTreJ3ClHlRnshyXDqneGmTGyOB5HVh-dF8g53Ti4g2gzWKGK9OZAB7-B5YBZVDS2Rc-2mML9r6GpejaUEnNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یک انبار تسلیحات جدید حزب‌الله حاوی ۵ تن مواد منفجره و ده‌ها پهپاد انتحاری را کشف کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128592" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128591">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a5486709.mp4?token=AURgs4vUhjyeUT3vNmiV4f2rH9dZzE5RyhJ5KqkZNwbFlN_zIZu4uoU6OQLJ9pITaduUd4QewszSvH0b7-eRKwqWo-5MxTm3odRZfeAZIymva6gcBcJkNPsDZLKAecDkKtK0_HVGjsFSHOawOZqu_aGUXRlmTqiTSpMXgnAohDCYqxlihmE4dWZS2znzvLI9_LPOVsaa6RCXfcoJLHRLeRgz81XogTNp-Hj6CB7oCuy-yhNiYaVOGcYnk_i1NxpuZKFezFqC67fiUIX09jakKwaeNS1mDifflofH6yI0Kf-nusdWoXv9sjQCkoNl6pkdR4JXMo0X454sCvWnSicBMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a5486709.mp4?token=AURgs4vUhjyeUT3vNmiV4f2rH9dZzE5RyhJ5KqkZNwbFlN_zIZu4uoU6OQLJ9pITaduUd4QewszSvH0b7-eRKwqWo-5MxTm3odRZfeAZIymva6gcBcJkNPsDZLKAecDkKtK0_HVGjsFSHOawOZqu_aGUXRlmTqiTSpMXgnAohDCYqxlihmE4dWZS2znzvLI9_LPOVsaa6RCXfcoJLHRLeRgz81XogTNp-Hj6CB7oCuy-yhNiYaVOGcYnk_i1NxpuZKFezFqC67fiUIX09jakKwaeNS1mDifflofH6yI0Kf-nusdWoXv9sjQCkoNl6pkdR4JXMo0X454sCvWnSicBMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیراندازی مرگبار در بیمارستان ویلیمینگتون ایالت دِلاوِر آمریکا، یک قربانی برجای گذاشت و عامل مسلح حادثه همچنان متواری است.
🔴
پلیس اعلام کرد نیروهای امنیتی در حال انجام عملیات برای یافتن و بازداشت فرد مهاجم هستند و تحقیقات درباره جزئیات این تیراندازی ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128591" target="_blank">📅 08:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6789100e6.mp4?token=VXwbwlyb05aA4Xpv-ew4vAG5hedBU56CM9QjcjN2axAyc69xQPTv8Y9usyF0nEDCxZ-dKkpt2AE-TrHByvgsWgBM7upswlqY2MZw83Q2k11QpTu-dHKmzUU0vUapWzcqO_84bQeOBEuuAdCX2JRGuwJE8nsW6wOS_03ydhpnJiXUFwOa4u9I9-iloqPHxEHFVghlTe9_6mbCxw4k-nP2JQOGgTDJefUcpLsP_IMSewdeOrH3JHHCGmAWFbnl2x6LE4Xj186DzlokLiGT6D6VxqgEB9jMa0lsGuNf26At2eSiS9rnKC6_igOR2-QTjJrHLgfr-RqEjP70ra0Uj6-LpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6789100e6.mp4?token=VXwbwlyb05aA4Xpv-ew4vAG5hedBU56CM9QjcjN2axAyc69xQPTv8Y9usyF0nEDCxZ-dKkpt2AE-TrHByvgsWgBM7upswlqY2MZw83Q2k11QpTu-dHKmzUU0vUapWzcqO_84bQeOBEuuAdCX2JRGuwJE8nsW6wOS_03ydhpnJiXUFwOa4u9I9-iloqPHxEHFVghlTe9_6mbCxw4k-nP2JQOGgTDJefUcpLsP_IMSewdeOrH3JHHCGmAWFbnl2x6LE4Xj186DzlokLiGT6D6VxqgEB9jMa0lsGuNf26At2eSiS9rnKC6_igOR2-QTjJrHLgfr-RqEjP70ra0Uj6-LpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که جان یک سرنشین را گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128590" target="_blank">📅 08:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تنکر ترکرز: ۳.۸ میلیون بشکه نفت خام ایران از محاصره آمریکا عبور کرد
🔴
تارنمای تنکر ترکز بامداد چهارشنبه گزارش داد، دو ابرنفتکش ایران که مجموعا حامل ۳.۸ میلیون بشکه نفت خام هستند، از محاصره آمریکا عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128589" target="_blank">📅 08:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
منابع عربی: اسرائیل حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128588" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وبسایت خبری سمافور: مارکو روبیو، وزیر خارجه دولت ترامپ با انعقاد یادداشت تفاهم نامه با ایران مخالفت کرده و هیچ اظهار نظری درباره رسیدن به توافق با ایران نمی‌کند.
🔴
وزیر خارجه آمریکا امیدی به رسیدن به توافق هسته‌ای در مذاکرات با ایران پس از امضای یادداشت تفاهم نامه ندارد و تاکنون درباره امضای یادداشت تفاهم نامه با ایران کاملاً سکوت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/128587" target="_blank">📅 08:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGfYH1KSBweiSLclk_z5venqGeefcZ3E-WHeIxXQmXNaRHPtSMz1KRDM_hWKr4X6pUjI_jfhC-MkR5NCE3hML0_JElra8CELGU7v2atTLGS7bVHh5oiCGdCFTfRYXKbKJsKQJogeqBHi8hYGn0DNF5d9lCf5JmMJgKUaAc9bWNJJ1-QPr2CH0ksGPwFdIj39lOvHkMPUJeKV34eFL57rsrAoANATmMNIOruTqz6vKkSTcCEIgNYobK7PaPvzmUDSYGiUqPpTBB-57YAqgcffqWD2gl7JMchYHm9NFpk0vTv02TGrN7CA4V3wy_HFBP8owA9OCNrJIycqzyIxq02j6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/128586" target="_blank">📅 08:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzWUYaO0FMTq292HqyIn701U2EF06Uj_FJBfxgbJTK5Ozz2KD4QUnjiywN3NRbLgZF3sdT11Nmcfu30yM0tSwHbmshTxo0fo1fUKRquF90rpgnNDX9HR8pBg5di0zcMH8iT9iWhyBGAqElvvO4qdFWMFp3mojVj-gMiWv7-B5LWdxYvBdFrDxqt8ZYnKkJp46ycPmo1QcL_181KjpaCCLhZKcmTxoiYpkQe9QRtBs6jS71j6nk6xtcf1ZcHZnIbUvYpLkCfIBgvbbe1PTgzQF5AkHf0T_Qtf2qgSHlC-RvALs66qMUSjCOx17R-ZSnnpyyZCvQg6HEXD2EE1B69kFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید:
«نه سلاح هسته‌ای، نه لغو کامل تحریم‌ها, نه پول»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/128585" target="_blank">📅 02:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9flrmYzhluPhNxzUn6e43TDXhl7dx77Hg9Su_xo0omPz_Bak0p9WAw3UeciFzx533qOa2LZ8k0xQ8_K03qwTIzIATytDEV_SbQVToP2gPJkis-EayD6BiC9Rjc2AMRxbjuwwLCr7g-Unl5vKBUpG2Cpu6U6meRXsBAb9vbIO_FaZLS7nsPECVkpy2Oy__NUGn1za3wiqaWk_Kv5gbvDuN6pyIpT2SFi1nuEvi10KMWp2RPIv1LGpJjgx-zjOJDg4r7ufpdDegP8SEF4C7A9Lo-vkwERQfMIAh6A1hFaVIpjXmRkZiG-_-K-DNCA8N6WYOhVvyNwIA71h9SAYn_82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنای آمریکا به محدود شدن اختیارات رئیس جمهور در جنگ رای نداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/128584" target="_blank">📅 02:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_j_pdYQLyE0pda4n5p3l6YkSy37CqQMWkzkxYT-ZcrkI2t0Z3zp4Xwe5GXCyTRm__4JSOmUNUP4kzf-2i71k22sJOzX23KwUyFJUVqjiTn7mB-kJHmJU_lofgHn7Y3EJEzLlgfy7M3Fsqlk8nioY4kny8f2rqgShWV18DpdwwXFXOHKXLDmCHc8yG1wCNaYcU1xb2-1HjFcN4TbJqQzdqcbwM671445-yDHoJrU1XlHK_pUYOtioyEVUUop7F9Ix__25MPhmtctWUGcpS4w77nklLCVIJLzPu6dgBkRu_w5n7am104QMzM24EamHrQwlKpGE6RQs1RS55clbDDPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاملا هریس،معاون رئیس جمهور پیشین آمریکا:
«هر مذاکره‌ای که در جریان باشد ترامپ به نقطه‌ای خواهد رسید که در برجام به ان رسیدیم و این چیزی بود که خودش پاره‌اش کرد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/128583" target="_blank">📅 02:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128582">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96e36d925.mp4?token=JIsy7rAqDKBx6hNZXtWGwtiiAQX0RjXinTJxiV0pg6T9M_MeQBiZEFl79RDhMLUHvudnzzG201PvTWbjoKzUlfOLWqWc4WDDIQl88hh7GMvRuwnz33YHI7K7FPJQdH4Pu1O2hwzNtoBpxL2xlWYYIXxg75PJSc2ovydZbnhrHW62-tqI7m_H_ETJRhT09fReAVGp48KJbS-p2YRRoRqyOfKag1aUws-zY1D9rKeRXkEMAnv5Rlqma-UDZXt5kD1IbavTyL16lC8GNVs-d3r2vIUIplVhTTmegy9MqnGj5GyWk64rv26JTTyEg9LPRbvFZ01_gkvErFoAEuVvL2R3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96e36d925.mp4?token=JIsy7rAqDKBx6hNZXtWGwtiiAQX0RjXinTJxiV0pg6T9M_MeQBiZEFl79RDhMLUHvudnzzG201PvTWbjoKzUlfOLWqWc4WDDIQl88hh7GMvRuwnz33YHI7K7FPJQdH4Pu1O2hwzNtoBpxL2xlWYYIXxg75PJSc2ovydZbnhrHW62-tqI7m_H_ETJRhT09fReAVGp48KJbS-p2YRRoRqyOfKag1aUws-zY1D9rKeRXkEMAnv5Rlqma-UDZXt5kD1IbavTyL16lC8GNVs-d3r2vIUIplVhTTmegy9MqnGj5GyWk64rv26JTTyEg9LPRbvFZ01_gkvErFoAEuVvL2R3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا رب روا مدار روزی گدا معتبر شود
@AloSport</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/128582" target="_blank">📅 01:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128581">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPN7_yO18bcmxQWBH6mK1tMVni_TjFCBPA97LX77q2fgkxYAnt7TreS6-Qk3HsEyJ74rfOa_VfoXF4aWEjsBmrDsGOuGFXd1XZb1LqHTyUjUQJkf_Od6XYeyE0u4YhXJ4zUJRWrrWJ_-iPYaV0c0acnTlC202R2lljABgaSsxD6AqUxQ2Goquz-FT-MKvF0BdWeT6PU7KhbJwJdNhe4XpTgQ5LccVLGw5o7ViGsGTyaJcesAma9fHMEcPlN8KX3xiSJXkN9zeVPPpE6MlCa3veEOPHkfKZt7nOn1Kgi3f3ikGh8fWZ7tIcdUw8akj3oyIMQsowLGOT67rpPY2P2Glw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه خبری ان‌بی‌سی، سپاه پاسداران انقلاب اسلامی از زمان امضای دیجیتال تفاهم‌نامه در روز یکشنبه، هر شب پهپادهای متعددی را پرتاب کرده است
🔴
یک مقام آمریکایی می‌گوید که این پهپادها توسط سپاه پاسداران انقلاب اسلامی پرتاب می‌شوند، در حالی که نیروهای آمریکایی آن‌ها را قبل از اینکه بتوانند به کشتیرانی تجاری، کشتی‌های نظامی ایالات متحده یا پرسنل در منطقه تهدید کنند، رهگیری کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/128581" target="_blank">📅 01:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128580">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cf13291d.mp4?token=reIeIPzAlwd61zB1TnL_h8WhDQhvgkWkRJqatAX7rM97aXE2Og3fIJdX5fkK2r3JaPd1EfVsTjMRFQIT7GXg0qDCcw7dyoijalAyImnuogDZA0l8uzdMM6vrQJAPWkxYwKsmbMLZSw6CLfZKo4QbLCNTE5kkKOxeuvWsCOwjpiL5lBk-ALbskW2AUyRAtuhPwGMIVCg6woCidrE8gabrUj9lopleACHMolWgin97dOR47d1RJeT5B5d6VGI1qDeZZTWXZvSj5mYQJ-E_GyANcX-loBtAXGzc1wUypu_dZqbnGkPCbuRE7FZfjM2A4_HGordgZUQgNdqk1n7Dg1N7ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cf13291d.mp4?token=reIeIPzAlwd61zB1TnL_h8WhDQhvgkWkRJqatAX7rM97aXE2Og3fIJdX5fkK2r3JaPd1EfVsTjMRFQIT7GXg0qDCcw7dyoijalAyImnuogDZA0l8uzdMM6vrQJAPWkxYwKsmbMLZSw6CLfZKo4QbLCNTE5kkKOxeuvWsCOwjpiL5lBk-ALbskW2AUyRAtuhPwGMIVCg6woCidrE8gabrUj9lopleACHMolWgin97dOR47d1RJeT5B5d6VGI1qDeZZTWXZvSj5mYQJ-E_GyANcX-loBtAXGzc1wUypu_dZqbnGkPCbuRE7FZfjM2A4_HGordgZUQgNdqk1n7Dg1N7ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه عادل به خوش چشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/128580" target="_blank">📅 01:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128579">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
خبرگزاری نیمه معتبر تسنیم: به گفته منابع اطلاعاتی آمریکا، این احتمال وجود داره که جمهوری اسلامی در واکنش به حملات اسرائیل در لبنان، بدون هیچ هشدار قبلی یک حمله غافلگیرکننده علیه اسرائیل انجام بده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/128579" target="_blank">📅 01:14 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
