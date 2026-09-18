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
<img src="https://cdn4.telesco.pe/file/ZEsrOZOwbW9Zd-V92GXDi9w3tBrWShkLvCVqBT36BMWaC-wOaieo2KfSm6e_9UE4T0PldMdkuig8IBishZmIte7f-lMvvchPCvap8yMiKapcD-eTQcV4EYjJY3X38XaAd6zAYvpU2ckdg4_0htPjuEG1GRimfKzZlwPYr8Zgz53rw8JEE6aYv2ylVHB9E3hrbMxuaY882fSSNJbGqdxG6G0WxtoTAzbBgeT8YxIjVdxlrjNsaWJsEiwVjxT_8Pq5APKjMydbZdtkxt4dykCwE-DaPUTyHwMZVPZK5bSKHefmwsw-2rY7-eTqXZdE6-Y38cpYrYZPLy_Z1NZSf8OvYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=WcyEq6vMoCItyufT55TP0eKHNjaOliAkhiJUQ5gAIUEMu1b67OoEl1b9yNyl3QMzwFKmOf6gtqGkWwPcgfX0CtI5ujDN3ipUH8lQcOrl6PF3r1BdLEkbFGUA3MJTgKdyajyiW3kak--cYZHyUzEmdTQIOnJVt4WCh3I1bbh_mqxl2QtvIfvJHMGrYQzWbAcbTvKGr5MldkYNih9mibaaNDaif7toVtvSyWz6FVd2c536vZza0vw2EY6_Ymz2DQB4wwoYPWd4_Kib6nJHqbKVs9YI_Nka5haMhzSizeee8tqpjYDhFC1KalXV4wzK27mgKq1eScMTSS2L41WzSCFA0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=WcyEq6vMoCItyufT55TP0eKHNjaOliAkhiJUQ5gAIUEMu1b67OoEl1b9yNyl3QMzwFKmOf6gtqGkWwPcgfX0CtI5ujDN3ipUH8lQcOrl6PF3r1BdLEkbFGUA3MJTgKdyajyiW3kak--cYZHyUzEmdTQIOnJVt4WCh3I1bbh_mqxl2QtvIfvJHMGrYQzWbAcbTvKGr5MldkYNih9mibaaNDaif7toVtvSyWz6FVd2c536vZza0vw2EY6_Ymz2DQB4wwoYPWd4_Kib6nJHqbKVs9YI_Nka5haMhzSizeee8tqpjYDhFC1KalXV4wzK27mgKq1eScMTSS2L41WzSCFA0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C79Xm2cRyEvTsKHtUTVbGB6k-5cS2aqxiAaAbCUh1Ckojw55ers68mQMaPN1x4kaFJ_Xbw-Vo6YqH36CDEHkC_jCvkp8bWpLeGNcJj3R_-58cQ5Ub1lx_hLyVv2WHiqPy9_P9lcdRr2HnXGc8w9HV4eXP-lNYCQ3nx8_yBY6tHs4r3Bcl0wClIElCC3kvfXiag_5-MrA6qX8hTZ8VgHQP_KzwQ5uKhMH3rFS5QeaUZHUUY-x7UffSdv64UenHjLfzlGR1H51QBIZrGckNY-ptDmN9dJlvU8ju7qF4Hm4yLQ2oxbqP9dn7JlcU30XlYGJd6nSJANKxoPvec0_zNJ98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=p2DtrAVnE7RFR3y5NT-0FPyU3oNer6hKQtLAwngOrFodbume4ICfXsa7FuMYG3kgk8HMRk4ppOU8XWjaKS7-pASG_SlSKmjZYoFXRW-4n4RweohBT2XGfXjRpnctijVnfC5nuPdEcFnnzB6at5pz4SFzXi_BZFPrXjsdt5AuLJo5rTA--IDzT_XQjuOvdmFzkV1UcCxJTI_rKkduhmGUFx9iB0LGyOWd80GGJscJj_zgG0qzYJmfu5JTxWB4EEl4rd015xPJ8MKGI6k1__4HWTueb-zv-9NGA9cvapV_u9nRigCU2UjHApmLNQlrLhDCXAk9lxtJ6COm78-YyRsDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=p2DtrAVnE7RFR3y5NT-0FPyU3oNer6hKQtLAwngOrFodbume4ICfXsa7FuMYG3kgk8HMRk4ppOU8XWjaKS7-pASG_SlSKmjZYoFXRW-4n4RweohBT2XGfXjRpnctijVnfC5nuPdEcFnnzB6at5pz4SFzXi_BZFPrXjsdt5AuLJo5rTA--IDzT_XQjuOvdmFzkV1UcCxJTI_rKkduhmGUFx9iB0LGyOWd80GGJscJj_zgG0qzYJmfu5JTxWB4EEl4rd015xPJ8MKGI6k1__4HWTueb-zv-9NGA9cvapV_u9nRigCU2UjHApmLNQlrLhDCXAk9lxtJ6COm78-YyRsDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwwSrDFsdwCN9X2ggC605G0c8JJkrIlrhuV37jRw_R9nI4AQEdpvAHHqSFsgUhuUKCv-vDli2yO17K2k9xudP34oE9K9kF-31mG3uVpV1xkTaKWJc1ZezqTPN-GceggSX53Z_ZAkIAZjN2wu53CcL34hvy4k4-pvqoEecfJC_3NxctOkrWD0SEhxHeYvpKajJaRDg1eAWmeupVyrO9aETj_4XYPiY47OmxnbJXEpW9bacODu3yqCXqh5GuJUwqpic_hoKjpWbZ8D7BcqlZ2gPZdrKCB2QciUqScl8D8A5BdSB_r_cYgfV7uC945LMePLkw3K4n7fHv94zFAtsJ0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=rWMPMkV-URE3QrTq1VxwmrkccTVJ7Ef__HlikSdtzNKOVYo82iFN3eAKLA_FXHj7jgBa98l2C9oukAFmpqFh0D4SnmVsi1bbgJ3MHArT4AhoWGmScKipyBvG70AyGXQJA8v_cOhhqWWBJKkL6bBLha62YvpfCK5orR6ealonahLDhPawYmH2Ze_oRfIh9AN1Y6JpHcrYkCStYnjly_zUPab00f0ZLXLKvgXazJhDmBIM1H22i2DASsbK_AkHvHwX7Sx7fJtmLBc9fU4NZ5X71nxEF7HQEaSFmh3Ac9SfaYvpgDbUDbyVaAni8dJRwKuO7-o4qsL8dPkcc8HfSRg4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=rWMPMkV-URE3QrTq1VxwmrkccTVJ7Ef__HlikSdtzNKOVYo82iFN3eAKLA_FXHj7jgBa98l2C9oukAFmpqFh0D4SnmVsi1bbgJ3MHArT4AhoWGmScKipyBvG70AyGXQJA8v_cOhhqWWBJKkL6bBLha62YvpfCK5orR6ealonahLDhPawYmH2Ze_oRfIh9AN1Y6JpHcrYkCStYnjly_zUPab00f0ZLXLKvgXazJhDmBIM1H22i2DASsbK_AkHvHwX7Sx7fJtmLBc9fU4NZ5X71nxEF7HQEaSFmh3Ac9SfaYvpgDbUDbyVaAni8dJRwKuO7-o4qsL8dPkcc8HfSRg4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=QFWiqBYGz02En5oYDO1lPO2u4PIYLUjLhaD4o7d6QThctRaRH1WwjyHtnJb51kbAfgIMtbxvpG7QK-wnm9ZsQneQCMPHf1yuB2FT6hDhTnY8tGW-qjltNrZXhwGDFu0uDMoa1k_O3AQpV8S3PqSRiZQDPT_EQjzcg8YFtWsNT3IPLhf_RcK-ha8YylR-OJAeB2tJae1vXinrER542O_Y17eBdDFfFHEDcOXyJ99Q1823n-mvZwV-FT4wCcRIuHhcormC6NEZ3pPtfGlsrCJaQevagzd3zz7hHNgevdNKty1nvyiESjRwuT0UphCcncr17ydRRnHHJHHbUyPduXyqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=QFWiqBYGz02En5oYDO1lPO2u4PIYLUjLhaD4o7d6QThctRaRH1WwjyHtnJb51kbAfgIMtbxvpG7QK-wnm9ZsQneQCMPHf1yuB2FT6hDhTnY8tGW-qjltNrZXhwGDFu0uDMoa1k_O3AQpV8S3PqSRiZQDPT_EQjzcg8YFtWsNT3IPLhf_RcK-ha8YylR-OJAeB2tJae1vXinrER542O_Y17eBdDFfFHEDcOXyJ99Q1823n-mvZwV-FT4wCcRIuHhcormC6NEZ3pPtfGlsrCJaQevagzd3zz7hHNgevdNKty1nvyiESjRwuT0UphCcncr17ydRRnHHJHHbUyPduXyqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=TeF0_lG-ScmHEs71y0lFaplCcc-VoSEPlS-t-OKZ-tEQlKYFeDk60-kjjaH1ozJKOarZgKOyEWzXv8ZjxBcW6lbbSI-3PV6qWS6Q5vVZbRcIdGwDFXTeEEOAjp6Z2tQAYqQb87Sayi-u01ILqZspqyW-f9emW4DkIJuftLXpQ8y5Xnwhs8SuhrDwWMRD9Kewh4s4zGIqt27HDl9t0HbudWqObV4cuEtvzBTRC95XiHH18xLdDaIlzFK6n_B9w2gLbNG0tRf6pSHMthK4PX2Ktdhhr8CIU-e7IhcV7texl51j_u1UjF4vzIeNuvZyr2xC-gdRw9Vg_2vuIxGVJV8HTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=TeF0_lG-ScmHEs71y0lFaplCcc-VoSEPlS-t-OKZ-tEQlKYFeDk60-kjjaH1ozJKOarZgKOyEWzXv8ZjxBcW6lbbSI-3PV6qWS6Q5vVZbRcIdGwDFXTeEEOAjp6Z2tQAYqQb87Sayi-u01ILqZspqyW-f9emW4DkIJuftLXpQ8y5Xnwhs8SuhrDwWMRD9Kewh4s4zGIqt27HDl9t0HbudWqObV4cuEtvzBTRC95XiHH18xLdDaIlzFK6n_B9w2gLbNG0tRf6pSHMthK4PX2Ktdhhr8CIU-e7IhcV7texl51j_u1UjF4vzIeNuvZyr2xC-gdRw9Vg_2vuIxGVJV8HTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=btD-1hREKIw8lyW-VWjto26ZKoHpMzRJ3lxcNMd7qOj0H90rsvosWUsyQG-US7T2hU1ozrCumYxhkOPM5hWSjiW0-auTyYzezxJtuZtbjKdvSG8wEkrb74HpcXWqEfm9x-wgrVNnTIarpVBAwkB1jDXAOR95sQchxKjtPPN9TA-SBwaEYWMmFYCBnIsQJNzuhzgJ0RolAzb5ai4O_tXQSZL9nBM11b-BF93Vfbvx8dryf5gaRLTWIb6sIh3wS0kPHQiIBRuWTysAEsZHmQ3u-LW-wze5DJ5lP0c42xNWnDsC7PohH6o4oONNGsz3PSQkM48JlrPYJD_Vo6J75-PDCgwAmdQ7H5j99xEEBYmpB_8XxSQd3qGS_zi-05Iv8H12VwVaSRxwpi69DnjJs1VcyXq6fADq6pc3xYF1ctbAIBWyD5E6zmzzLfn21cJKrHY0jHzcZCL1ScWGoFlvad3EXc89A56lD1z3ZDi1hQDcATVgfJ8lnJGLJRYcf8VnLDF-Se0BQMt9tKXnM1-gdYMZDmCWZkKBXIJ_xpwPeejGHB567_wwCjlQRlhPHQ65uHKigKSnvNmyxZsNW5w01bBexbq7k97IhyfdGu8i7lWzPVZFABvvMJaOpUyA3R2xAGMmii_duheq7HNUhA13EujEbWtjr8xGw3hHB2N_h5bvhc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=btD-1hREKIw8lyW-VWjto26ZKoHpMzRJ3lxcNMd7qOj0H90rsvosWUsyQG-US7T2hU1ozrCumYxhkOPM5hWSjiW0-auTyYzezxJtuZtbjKdvSG8wEkrb74HpcXWqEfm9x-wgrVNnTIarpVBAwkB1jDXAOR95sQchxKjtPPN9TA-SBwaEYWMmFYCBnIsQJNzuhzgJ0RolAzb5ai4O_tXQSZL9nBM11b-BF93Vfbvx8dryf5gaRLTWIb6sIh3wS0kPHQiIBRuWTysAEsZHmQ3u-LW-wze5DJ5lP0c42xNWnDsC7PohH6o4oONNGsz3PSQkM48JlrPYJD_Vo6J75-PDCgwAmdQ7H5j99xEEBYmpB_8XxSQd3qGS_zi-05Iv8H12VwVaSRxwpi69DnjJs1VcyXq6fADq6pc3xYF1ctbAIBWyD5E6zmzzLfn21cJKrHY0jHzcZCL1ScWGoFlvad3EXc89A56lD1z3ZDi1hQDcATVgfJ8lnJGLJRYcf8VnLDF-Se0BQMt9tKXnM1-gdYMZDmCWZkKBXIJ_xpwPeejGHB567_wwCjlQRlhPHQ65uHKigKSnvNmyxZsNW5w01bBexbq7k97IhyfdGu8i7lWzPVZFABvvMJaOpUyA3R2xAGMmii_duheq7HNUhA13EujEbWtjr8xGw3hHB2N_h5bvhc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=aQCAW-mOe71Tkv9vjLeO4-rxBWrVjvaiWOt6K7fmZxpUCYOV33Fz-faiey1z8oESK46NS4bFlXaEa7Jw6bQWL2R7wVE-OKi8vCYhGTpZ6MNNyMXtX2uxzhBEAUejG_bH8z9JmmOEjqgG-ShlXUV0Oe7VZ1RnOnrFfQC8ZuAPS85aySC0CQeVeQKCklwXu7dCUHwLMnZyikCZCLvxtUNoT4hW4MNo1PF_PqEUYWv7m_gy8Mhu--_ENjml16vRUXuKbtKj9QqdTFWsVkkolOxLUWdWneV5LybE3LV6UXVNMV41u35NZZ0w26mDLc3P9aVFUFnz2MNLaE1gYffCiae3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=aQCAW-mOe71Tkv9vjLeO4-rxBWrVjvaiWOt6K7fmZxpUCYOV33Fz-faiey1z8oESK46NS4bFlXaEa7Jw6bQWL2R7wVE-OKi8vCYhGTpZ6MNNyMXtX2uxzhBEAUejG_bH8z9JmmOEjqgG-ShlXUV0Oe7VZ1RnOnrFfQC8ZuAPS85aySC0CQeVeQKCklwXu7dCUHwLMnZyikCZCLvxtUNoT4hW4MNo1PF_PqEUYWv7m_gy8Mhu--_ENjml16vRUXuKbtKj9QqdTFWsVkkolOxLUWdWneV5LybE3LV6UXVNMV41u35NZZ0w26mDLc3P9aVFUFnz2MNLaE1gYffCiae3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=IO-bsaaeJEWV3I2NmeB3WcfdWlEaqqErZaWHCa0jCBeA8WLQO47tZ4CTVHwL9A2F6epnTPayPy-dZS_ePSJVnt4uRBcPlJbAh4Aiu73bIbBNJFNoqsWonJVWXt93Dv2MR7Bxl1nz63to1bf-wNlpumA9cMKowFkCVF54XsmSZtEOhMguMQ-zk3esplOTJRpfgLkY3QTjXMeAdIEMMWlOOh2yvxwyrMssKJtp9w7ZqrwVaMh-LuOd3pOKadvBBKMhF-Bqzfk_OJ6pPKB0pGPIicYm_QqVgZ3Qoj-pNr09OS0tkB7Uq6n63YXx_OexMfjQ2EkhBrWLXhuzEJsCueLCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=IO-bsaaeJEWV3I2NmeB3WcfdWlEaqqErZaWHCa0jCBeA8WLQO47tZ4CTVHwL9A2F6epnTPayPy-dZS_ePSJVnt4uRBcPlJbAh4Aiu73bIbBNJFNoqsWonJVWXt93Dv2MR7Bxl1nz63to1bf-wNlpumA9cMKowFkCVF54XsmSZtEOhMguMQ-zk3esplOTJRpfgLkY3QTjXMeAdIEMMWlOOh2yvxwyrMssKJtp9w7ZqrwVaMh-LuOd3pOKadvBBKMhF-Bqzfk_OJ6pPKB0pGPIicYm_QqVgZ3Qoj-pNr09OS0tkB7Uq6n63YXx_OexMfjQ2EkhBrWLXhuzEJsCueLCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=b5HGd4_sz5kdG2CTDiVBftgq6kbNfF19HjQyz4CRwgFK7I2_T5GzMgFjncgb1p8c4evxXWhsdCnIQ59N04fo9uf73nkue39hEMzm6-FGfvGi-c2c4EodjWrenazPwpyaV04vNr9qLsOhjAdAD0mmUjTKumcR2a7GKVWu0XLeWudDuLaoEpFAMr1H3Fv1MFy_9J3tpeUZBBs573zgpMAsDoqzUSQN0-sR7WApxI1m1BT1o8Kzw2m0Yy_hvfP_uP5Jy9AgQLYhSBAXGcjuxSsn9vTi7HPojo6ASv9kemDcPiWaimOteCcJnMPMTwnmVcgqWWdsVWby3lkW05teJpf8OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=b5HGd4_sz5kdG2CTDiVBftgq6kbNfF19HjQyz4CRwgFK7I2_T5GzMgFjncgb1p8c4evxXWhsdCnIQ59N04fo9uf73nkue39hEMzm6-FGfvGi-c2c4EodjWrenazPwpyaV04vNr9qLsOhjAdAD0mmUjTKumcR2a7GKVWu0XLeWudDuLaoEpFAMr1H3Fv1MFy_9J3tpeUZBBs573zgpMAsDoqzUSQN0-sR7WApxI1m1BT1o8Kzw2m0Yy_hvfP_uP5Jy9AgQLYhSBAXGcjuxSsn9vTi7HPojo6ASv9kemDcPiWaimOteCcJnMPMTwnmVcgqWWdsVWby3lkW05teJpf8OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=CiNG6shBjPISrQ2tTh9Mx1K8eJdcErQX_r7eJAaNazFKUAfxjRvYmf36gyHpdOqP14iNAHfGvAknNiilq9tkyNje-J01H9hqNSq9W4IgZ17XdRMFDQIu1w1nSgMFIyiGM7JgSW_OQNeXcW8FMZ2nJ4fmLQVpy81an-SfIR0-YyW_Cks3PHYG0v6rtD785hTmtyAFG6U1vaBr0g0Ph2iCseJgZVKorHNFrwhVxwX2yAo13e0R2skhbRWW03rTm3kf-KQkgkQa-cZVo0AZAVR6ppEgmcjlaL8zul0XDyaieGBOcAWD0M_ZviZEGVB9XsYXO1fc5xpTdM2J6M0BCiNlgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=CiNG6shBjPISrQ2tTh9Mx1K8eJdcErQX_r7eJAaNazFKUAfxjRvYmf36gyHpdOqP14iNAHfGvAknNiilq9tkyNje-J01H9hqNSq9W4IgZ17XdRMFDQIu1w1nSgMFIyiGM7JgSW_OQNeXcW8FMZ2nJ4fmLQVpy81an-SfIR0-YyW_Cks3PHYG0v6rtD785hTmtyAFG6U1vaBr0g0Ph2iCseJgZVKorHNFrwhVxwX2yAo13e0R2skhbRWW03rTm3kf-KQkgkQa-cZVo0AZAVR6ppEgmcjlaL8zul0XDyaieGBOcAWD0M_ZviZEGVB9XsYXO1fc5xpTdM2J6M0BCiNlgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=Ngagg_fkKO1KzE3iSoLc2KqTxsq3VGPhEOoorzTGz9OZSVTBQ4wnQOgA8nYYabbc3IxotjQegRSVPAsKCU4vYZsT7mEV51RmOWBwhZXbBanrQWCaSjVSU5Vk0J8EjWwZwxNHSiOprv3TpOylxqzmerSIE1hyPuV9qq5NMQ-W7gEwJznZbSSxk-XoZ-iDntV-mGG-3OhkMaDiWTejxHPNkp5TJjx4Oq3sSnCe7D0kv_SxU6bXTbekNXMEFGc6cITK_bQGe0lJH0cMroa6uU7bXE8vWqw6966F_S-zZckJAkECbe-QUsoTwxAJdl0mIeV1CR_ehuI0VyT7yovkgI-nTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=Ngagg_fkKO1KzE3iSoLc2KqTxsq3VGPhEOoorzTGz9OZSVTBQ4wnQOgA8nYYabbc3IxotjQegRSVPAsKCU4vYZsT7mEV51RmOWBwhZXbBanrQWCaSjVSU5Vk0J8EjWwZwxNHSiOprv3TpOylxqzmerSIE1hyPuV9qq5NMQ-W7gEwJznZbSSxk-XoZ-iDntV-mGG-3OhkMaDiWTejxHPNkp5TJjx4Oq3sSnCe7D0kv_SxU6bXTbekNXMEFGc6cITK_bQGe0lJH0cMroa6uU7bXE8vWqw6966F_S-zZckJAkECbe-QUsoTwxAJdl0mIeV1CR_ehuI0VyT7yovkgI-nTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ICdacnQ4aUFOXWslvmgOwl0S9ct4_fhdZ9V1GB3qG51rhVj2jvFx3P0ic45joVcM9MEh5ZPIYn-vjJccge0NUaUV5tFzm5F2g0dUVFoOY2V3VFJUjkn5nfvgmYI43Ot7kmz76yAmdhuMrhPVmBnbKhsoe26v6owwa8Y0cFeb7YXTG0WpkUjohVakKVjPYzTBbOsWdzF8jaU9ADvpu5RogaxLONaqzYgU0cSc2PUBvuyhC5J_Cc19mIYmG0wgQDZ9AgNF5P1BLcys_ONTHuLmiKdX3V_5bwHDZ4w2BeunjriCQCvLvHsafMr3cpFpTWKEqnIlSXX3qmwOgKhvKSz4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ICdacnQ4aUFOXWslvmgOwl0S9ct4_fhdZ9V1GB3qG51rhVj2jvFx3P0ic45joVcM9MEh5ZPIYn-vjJccge0NUaUV5tFzm5F2g0dUVFoOY2V3VFJUjkn5nfvgmYI43Ot7kmz76yAmdhuMrhPVmBnbKhsoe26v6owwa8Y0cFeb7YXTG0WpkUjohVakKVjPYzTBbOsWdzF8jaU9ADvpu5RogaxLONaqzYgU0cSc2PUBvuyhC5J_Cc19mIYmG0wgQDZ9AgNF5P1BLcys_ONTHuLmiKdX3V_5bwHDZ4w2BeunjriCQCvLvHsafMr3cpFpTWKEqnIlSXX3qmwOgKhvKSz4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71815" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBXGcCRltNh2dRnEbhXBh8jFeapxm1CI8Vws3TlsUv6AOY-AIOa7ITzrHX62X9fYo3FX6jaOSy1-QzFMAM0hFMx2S656cr5yS0aB01vfVAiwDI_vydId-hgmP9-LSpbzHWhCRvYd4KNuVK3jw96jhO3H3BXc1FaaNjWcN2Zbb6W0dHQhqBPFqvugHd8_qGhi-eM7RKN-WcSumFub4wKL73gZJXPhspKTYQupzF914qymnxZTEZHd7UUZ87KHBMO7K9C9lGJJQ4ul22AwzOT43Pdg2ew87kTNwyt1wc9fvzci7V_KAtTTPckYeUOaGlLkjJH39jWjES-jM9D5VKtauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71814" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=jNLqxM91HQDD1li6cCLDwzX4XgHy2xC9RvgnD9B0PnzgesjZM-H4d3xGY9nlH4sByS30_9xZNW1wCfGWSUStIokHDRzusB_F4FMKYZrMmpWJuYSAFKksQkvrBwUHwTFhd_byvtbbqSQ-m3aUnKg-MW7D7DO8I7TWU7MG1YLFI9wFuE1DLYOMdZEeaAIz1bxKjUcgw8NnJboK6IoWAIizrOjfYm_PfKda4-f5kJ2pwX-K8ECXq94xLhavWHnRiBvwNJ59M0xdIqIDdfj4dJb6J7XzMvKMqTZfecEsRARGfmbYj7eGo8_f9pjIpsNyLftDFsOj3Svyczwn4A53O5EKQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=jNLqxM91HQDD1li6cCLDwzX4XgHy2xC9RvgnD9B0PnzgesjZM-H4d3xGY9nlH4sByS30_9xZNW1wCfGWSUStIokHDRzusB_F4FMKYZrMmpWJuYSAFKksQkvrBwUHwTFhd_byvtbbqSQ-m3aUnKg-MW7D7DO8I7TWU7MG1YLFI9wFuE1DLYOMdZEeaAIz1bxKjUcgw8NnJboK6IoWAIizrOjfYm_PfKda4-f5kJ2pwX-K8ECXq94xLhavWHnRiBvwNJ59M0xdIqIDdfj4dJb6J7XzMvKMqTZfecEsRARGfmbYj7eGo8_f9pjIpsNyLftDFsOj3Svyczwn4A53O5EKQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9pGGE4p1TkHpsF-pjAaEf1YtbtRB1ViBRcD5mSQqIhcGiSF47jhwwpCFQjQdLZ5bUoWTQKYIoa4uOEyoiIBb1UyMO80ZbSbbiRISOMx4WiZe3nZI12p3oQSsnQXdNuzXlfPPocGhjnV5zVY-Ncgdspyqw-FX_kogDn8cwjxNAJ1wjDXkJMdv3OGln3uMudFUzW0tpnD7lnrAuNuRjGmFA8s-NrHDhY4uuWPhA5H_Gq0aywXwop3T4ung7Wd6ksLFk5hCAgoV5udg7nla3EPyfIjyqgoJljRC1xWYxqkdpV_w17NBCAgsX-Af2lg15-WVubfdTT64Y7pSJhAnlmE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=EjMAsjqg-l-APuGa9c9etm9o0BM-TgiFikS1AkmOve__oVVd1O6zMIFUyd6RbkYytp2ZRlRoALMDrVTKo6g2bugLRfBqhUK5nkwcJeGaEqYZGAuHZ45Bxj2j2_KoITXLZaHfSa0td1NckhQB_D51ir37m05XDNpDIBmVd_0MTrpwLgDGUMHpLoHJ2vpW6feKEZKlnkZ63C1K8P0ppEaAZrUSamt_2EU_m98W_WtvEUGfDfhouCai8YgvKZyHJ3iH1YQwlD2OnzqQTRGKvLpQnx5uRWBRAHK72AmwNd2tTTXbHEVnMtwp449Tkm-It58rw_RKyUs0Z4xNkKtXHHaOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=EjMAsjqg-l-APuGa9c9etm9o0BM-TgiFikS1AkmOve__oVVd1O6zMIFUyd6RbkYytp2ZRlRoALMDrVTKo6g2bugLRfBqhUK5nkwcJeGaEqYZGAuHZ45Bxj2j2_KoITXLZaHfSa0td1NckhQB_D51ir37m05XDNpDIBmVd_0MTrpwLgDGUMHpLoHJ2vpW6feKEZKlnkZ63C1K8P0ppEaAZrUSamt_2EU_m98W_WtvEUGfDfhouCai8YgvKZyHJ3iH1YQwlD2OnzqQTRGKvLpQnx5uRWBRAHK72AmwNd2tTTXbHEVnMtwp449Tkm-It58rw_RKyUs0Z4xNkKtXHHaOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=WcIBk2svBxGGeCHggCTmlXddMZBdA_-QPDYUp8Umz_h-M3zBo8s_InmiwsX5dqekHponowWyCzY5L_jV-nKyAXSuodhkm-Pj5maQI5LdHeZop7JX8XSQsL7G4BFuipae2w1-r6NUrGdXTKpZR3S10lQqjO7PB1PKECdClnlMqk-2o-8zn1ZqmoMKJAsJt_LJcXX0O5G9IoXtDZooi7nppsi6Ym5yjVQMfNXpa8CFWvGCRnlh7AizN3WZ_HNiolTs29IxIBnQqSr1PswK2GPBjwBhhGNzJ3Qw27J-JsdVdfnyiEK-ZSFFzuOGStxP6Q6K7DLhIHUO9v5VVFwFQTM93FEH5dDja_-0M3dhAl_cDp_iwTkp4Qwd7LvmQs4O3r0o8zeit5-OSd4E0eA9cw02dzHK1TljOSfOjqQokY8RMx2DAlalUB6Rh4YUIW_BDOUJVhOsruqZ20YrU82sPMsLBh_NOVhA_Wm3_CANitO4TtwJd0K3vpjFQZUn4qPer3fy0tUbrG8Wd8TR6CyWPiuo9Pmzcd80KfVz1uC6SIP7ApVuhG-ahTMtroT_QAjw1BKV00XTO7vMR8_-xszsjBb91wGp4kRLutDtm32F6zbcBubXzV9A3ZDRGmSxpYjyEcocr1omDhzceJ2JK_ADqb1V3Sj3UJLBDYoBqzRLAO6bDO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toCrvcDId8da3lfKc62e4iQlxxshmSh7zHj7ZJBpjB_Ofp_wLjdf-hXsjTshXEnQhRTHI2wbYFiVSUngVA9Hqx3IzOIOCMcplAfZy91Oh0NZ6p0Bx2SfKaUDtz48vTmek1mKVYnFtB8FD3hsagM6Ze5N237BNBHnL28TQDex8IBPJf0Bi3-pKvkHD3-pkpQ39-KPiopRsqry_spV8tMQb6mlVSDMwkE9orS2s8E8pxO_GIFy-GnaNn8ey4-YI-N4gLPvCpo2Wz_cUPM2i1BlPRS6wzRz1nnJc3jQFvdseVXjr_TD1IDr5AV_LdkwC4U5SHL_wmnfUHpEkeAUfkiwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=XfnJkI-rizE9uRzEb1gcQnHgD1isA98AVUWZiIKHoILE8bCvOPNQZ5xK_HGs1RFTnq0wFMtCdxvZxMgtaHOJLBEfZPvEzB4L-K-XrYYT93_c6wBuYke8gR3jZ8yWHuNFw3AdCP_13jscipPbAiGxlNIblGWocuwyXy04n2YZPCu8Sfl30jTh-vg8Hm9t6V223HmcggjdlwhV_u79_lE33C5ccoQHtqB1cJPJ74rp8kQSzNo1lQFO6O-Gws2qmtU3r4cxDuVNSjgCGLBfdQAnduP5Jq0m3C7ry0YD7DQULrI-uyYXkhpjMkAY4Iczo0mZ18Enaz6k2isDZYdJPvoPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=XfnJkI-rizE9uRzEb1gcQnHgD1isA98AVUWZiIKHoILE8bCvOPNQZ5xK_HGs1RFTnq0wFMtCdxvZxMgtaHOJLBEfZPvEzB4L-K-XrYYT93_c6wBuYke8gR3jZ8yWHuNFw3AdCP_13jscipPbAiGxlNIblGWocuwyXy04n2YZPCu8Sfl30jTh-vg8Hm9t6V223HmcggjdlwhV_u79_lE33C5ccoQHtqB1cJPJ74rp8kQSzNo1lQFO6O-Gws2qmtU3r4cxDuVNSjgCGLBfdQAnduP5Jq0m3C7ry0YD7DQULrI-uyYXkhpjMkAY4Iczo0mZ18Enaz6k2isDZYdJPvoPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71802" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71801">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71801" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=kGs5M84_p-J07bP2zJ1nlaTLz8TvUdEgAmXTb-reYAcJQq2KiQx0DBKfXJ2_eAOSrN22qW3648dV3iVQXwqDdxp7Du5wY8O0hhsQ0qaaFkQlTD48j7MCELyqobEsvzcxX0QZQM63SyvVd_oYgRRr5BXdoLofAAGusdZr06qeUuF6pI4kwbFcFrj0VdfeMhfO9TLay38GVbgiRt-hRwXjKUMQoYj9FBq1oAn-H_3Xubk2ZWQff5Y4IUaWkEbJ4edagG0-J41fYy2ONPFDl3ymC8aXuWs5W8YeupNHbd12-KFC8j3u__oGk9UfCaZe5ld6TVgQfDngRfEBcyh-xR-e5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=kGs5M84_p-J07bP2zJ1nlaTLz8TvUdEgAmXTb-reYAcJQq2KiQx0DBKfXJ2_eAOSrN22qW3648dV3iVQXwqDdxp7Du5wY8O0hhsQ0qaaFkQlTD48j7MCELyqobEsvzcxX0QZQM63SyvVd_oYgRRr5BXdoLofAAGusdZr06qeUuF6pI4kwbFcFrj0VdfeMhfO9TLay38GVbgiRt-hRwXjKUMQoYj9FBq1oAn-H_3Xubk2ZWQff5Y4IUaWkEbJ4edagG0-J41fYy2ONPFDl3ymC8aXuWs5W8YeupNHbd12-KFC8j3u__oGk9UfCaZe5ld6TVgQfDngRfEBcyh-xR-e5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=olkSMMTo9eS4bLdbbXviQYcHpkUZLPg0TKWHqcIOycX6UIUAHpBXQAbNnpTmIXXG2bOex3DRycnLFD9_VQK451kat-KiCXsbe_WvTWgXIU5LP_iSP_RBfFr8rsNCW9zYmzr4NwNZiZt0b8Uruku4lC_yvGCBVVBlCrYC9F_nXxmxC5vp37UEjPhtKgpuhtAapPr60rzug8x6MPpHEhmKC6Cs6-_8GGZzjchLh76ZWw2oPmWXVqBh6O5xJjShf63JsbgzAhvMyanrikjXACx_wV4fTbSebZ1S_CMIkKAGbn-wdvsvdvMOMKu7DgD3VtziIusPOa9i-ZsP45Eb_bZ3TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=olkSMMTo9eS4bLdbbXviQYcHpkUZLPg0TKWHqcIOycX6UIUAHpBXQAbNnpTmIXXG2bOex3DRycnLFD9_VQK451kat-KiCXsbe_WvTWgXIU5LP_iSP_RBfFr8rsNCW9zYmzr4NwNZiZt0b8Uruku4lC_yvGCBVVBlCrYC9F_nXxmxC5vp37UEjPhtKgpuhtAapPr60rzug8x6MPpHEhmKC6Cs6-_8GGZzjchLh76ZWw2oPmWXVqBh6O5xJjShf63JsbgzAhvMyanrikjXACx_wV4fTbSebZ1S_CMIkKAGbn-wdvsvdvMOMKu7DgD3VtziIusPOa9i-ZsP45Eb_bZ3TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8MRiFz2aQFpRIvoFa3HXlz3RFpKr0QNEigLu1-XqnpkFVtw5AnRcFYkz5sanzp2E8rc44xF_g5xYC7yL8aMsapHJOPI4v9RKEc4a0fTxo7rNRfr7Vd8Dn_4_fVI8gv0drnrlO9GGma2nPkihlTCVVbcYfkxrcCKitOmFHbggSfmjVY7znzUYkduapWfA_fJmW0o6dfB-x12rY09nKsCiYazzWS855aGjbMGmszEkPnw9c4RaJwLDcpPqViTR0AIuGvkjZDRjqFPT4kP4M-WwLtsJau2Q2i5oHdrz__vDpRnZQb-NFHmJ0EVC3NiNeu-5MqLIlOg56Dhwrq_yWA33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdAgYTFF4PP4iadqPjsSFBgweefXg1AZhs0UUo0dor__U3LGsT4hikJl3STiRmrcxfCiSTumZv4bPoIBN8BOqsreU0aG1O7nE2oV_49eOMtnV1LVWhAKyhHKD2mim7H1GDfuKd-YRqS8eHvVhz1_fAd7ZbEDvyoY7gIUFbpC4xnsut2NaFCOOzW03a2hkTthrnYX0ilyEM-QXxWJKgF_pDjAgg7Zy4oLNgT5jT9cN0ooVoGyfAtLsl97Vz1c2a9wHuOVxfBXV3SXmxpCXBnumXccw10CCV0pN-htxnRm7Im1itJDHAY91P8aOUvtsyEjkiYWZYr-jOmArosQEy3xIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-rKuGOzkSAphjB3XAXKM2XjUeyP_PnMi_UJ4X96vS0ZAQp32KNtHWa0Ky2VTj07psdJrF1Mc358wdyMw2-GuY_g41x7CsUpj1A-xBcNh0BV1X5ycPwSZilinuj9fp8prQkRPnGKw1zwV_GlWjvoFd571y74oPb870DsMUeV7Sd06PQBWhpJOLm8qiFbl7ugTh1Ks051TWJy2aHBwwDm3L_mbLyZ-CtPvRszsnekmDagN60GbvFH7D5u8sWKvRQPEzD7p6ZEzKp0wT1dm5YsZUVMIKb5lwbsvsWgaoaKRRK4_LYk1b-YcOc-LTXE-VjMpl-R9V1oJoC_urxkG11aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOYphqQUh4YlJYO70cynWHP3VfPcntUW_ajmtjnTISUxxvDap60UIsKC5hPMOmR7zxa1dz8xDYbrZyUtOYuFq-iy_hBjzmGo7bXeiXqYXRgmSv8s3ANbhTaSTLH_67x5C8gwg1Lm5oK0GkYDdWg7iSVk2ID9XKTgZ1hZO_tthInEx35mnhfpJNjjjpzBU-LvjVVb-JR3r2AhESGuEXHD7T714y7k5suJ0_Cyqt6KiYpQWLE2Ymb1G51btDAcs-Gj3EYVzufZj5bW5OjvpkeS-SR2L5bUs2ZJBwKljDVHNf_E4PX2p2O0fsOsuChXTkUOE6SU2QgICs1mLyJb3O9EtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5IgIwDEjIqcapNCY3vIRW5ga8suezmuOnBusjEnH0d1S2LBrJad5LiunghmDz9JpdcvTLHy4ZCAyDRDQ4UR5kEkVVj733wRJLDTI5gXV60wkYt-IDwS6AUXpYF20Y3MM99bi4txQD-UwaT-vm2Rh4G6Rui7Ppm1mbHMEUYuImfMjqjZNQJn4B8FdTxx0qG81oQ_F5JT3cWIYpWPSNmMy6b4EJ7GwPxqpQ8O9QnWaHbmwnZmHXgRcLfMfe6J6VOumsLFtMJ6H9d43aWcnWmNt491U4k-t98QvAtjXwBHhoTt-URHoAjpo0Ae7K_WiORuSFqVToP3NCXEWEkSOvuPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Insrpl6Yj71gNNcbbwEVZRGfTysi-mZ22S0T8WrQ4RUrLe9F3chzB3drwSO7MfWkCZZ2AB7_CT8LwL65XNFURIWLYaoBeY9oia9T9DnOvHe2adokSvZJTTo25ZjO6PNQf_Mhibm3D3HUh8faXTdeLJ2SGvnjsJ2kaqh5pbfw1USfQA2WGi6clQ8R6gFwIthjJqd02YtDDVOcS6BwnJHnbBXJs7KULaUEsxS1QvT--kY5FZ8ebGgjLDbnblOy2bwy7EuHmMPCjeAxcTR3incBLQEzUYK223Ln9lGHFL-AoTzP33qr8f8_ItGoe26yyzUsbc-VOVgPwdrTszxU9FJnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItzsFfGomuUiEoPODSB5txapGYDk8VLgUlPj31ZpwHWHmWqqCfLH5ijjDytpcGr4qrwj1X2_83WcaJaedu6349esnuhNhbsokOjHhpyUFLALa7JjgSqOStVJglD3Au8rg4DTUV0c3N3fZAF4icPvnG_duihKdOMkNnyJ_u5tIcXySEayx68mmviVbflK9dZLq_vB-QTmJKYrdhSM9XTEPuiyP-RAkjLGX1cT1MviXQgN8inQfvJA-VOMmUDMvc4esE3FcD3tPZhjwY6aQPjizQ5OY8ZeVOvhefyFfnl0SRhb3-H5-Fj7uUq0cI7tEAMYBanKnwuKE28vhidTDf2bug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=sJYmlQjVE6zomqaVbc3ZsW1L3atHktXoHYk2vIiXgtiicO9K464j0RKHqBNIieAF0OLx2Zt5Q-7vwvY-F-Qi9G74PtCzLP2zQvra4WFT2NKB2NmdJtqqhB0GwKbcPJy8FJu5uhqI3JSxIpk57wsYpnIzFIAxhSeOS20njc1dX_sUsqWckSmCzBDqnR9H51PS_0TDYNVrM7x2NEp6aKiWGYG346lfT-wz299a-qQaPGphPNupQ4T0Ow2DxHpheZDMwYSdzkG5q5b71WJzHb6bPGAjRHuZ2z1VOwzY3w-VvLh_Gr0WFX_4C5Gnp-8TK0CDATEYWQdQ6yHPhrtDokHdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR5ticVerR0egxFAZkqgYme_jA5NtTv31qmjTxtHI-wuxUCAZEYA9ngfTt8EqbBv6CAYQRwgTTZvDRHksbj1o4yrvwIUGchbTsFEHKZF9h6yNzrE1bL1hAyMszPFFv1VwYJwPMLznK6XsJYNTQlB0OCpSjRuCw3Vcyt196HnrffdNy8f3Yb_IXilAKwTLBqShXMguAafK_uQMKHWLweOQbj5gI-FyhMKAG73DqvwQFABLHRWz0Y-LGq8d0VYf9LEH15IoO7lLN7juSXJJYvOAaPA5Th7LApDY1rjvxjIbK339gIXpQ4y5IIX90hmMaB9q5j78Gmzt5u4pjW1_852sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=bUl2aCZxoHQ4iX3gFVZNS6t6AaWp0lUL9f4KPzLkZomFAFnUSHS_VPgkRaD9kpLaAE0g7FIVmQhzPUyY7KsihqCahL7O7aeEqJM3oCQF44JjGTXzcusFdX0YzcW8m9STYZV-GNrzcKxsvKzznqufJSBE3FNrKa6Gs3aSvUX6-pE23VUcPjCkQL955_55XGx67ezh_MUY06kEoXinxvV2BnNK0x9NZ9VELuALpF3lF3UCiGn0l-ux9oEuqjTtB9wkzvDdemIVi3-BGl4iXtyyzxWyiQ7mZTxVPRkr2svQiFkiHLzThnVSp3bauAEsFzbOKKBNLVzsH9JuqRgyxIf8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=bUl2aCZxoHQ4iX3gFVZNS6t6AaWp0lUL9f4KPzLkZomFAFnUSHS_VPgkRaD9kpLaAE0g7FIVmQhzPUyY7KsihqCahL7O7aeEqJM3oCQF44JjGTXzcusFdX0YzcW8m9STYZV-GNrzcKxsvKzznqufJSBE3FNrKa6Gs3aSvUX6-pE23VUcPjCkQL955_55XGx67ezh_MUY06kEoXinxvV2BnNK0x9NZ9VELuALpF3lF3UCiGn0l-ux9oEuqjTtB9wkzvDdemIVi3-BGl4iXtyyzxWyiQ7mZTxVPRkr2svQiFkiHLzThnVSp3bauAEsFzbOKKBNLVzsH9JuqRgyxIf8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te5M0_AWrSUtFNe8c_mzlLlzjfFWY3sMhnPfa-2vebGQeBmxlMkIQLbVGDj1s-dHN7rGHsWL_tV_FsZank6jE23Ly07aGKaYb7HMV2qwFes_0k9iwE3jcTv5aGqvPklBKir1XnSBwXexwbVs2uVov8kDO2_mLlT-n8w1GA_ZGNvA09CSAuCYfcZ9TO3C_t0FMvjtXLNeZg-fal9a7_m2njKpqI9y0OxqUmXwle9jhptKBcL2ctDc7p-0QooY-DYdA5eHCHWXGXgS7jcS3fMV_zG4BH5cLAmWHjt2BSc5suguoTf7KPm4tYxDLBHK3QkiAfL0G5z-7jE74kqzsPwdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=UMeOKYeSIPHDeN5cww8I5PMkk46oeRPxggUt0K42GP5l1Rv4XMEN-3bnrxFRGYLNErja57Z7y_mcdfJumDgUmV_ki80uafrk3eLv_Pn_NFUayZjXkKoKIUzjwdHHbrmO-34n5g6f3RISfm3zYnDOeRqUN6TI9tMKpjM-dmLfjyVeZ6dSVS4SvG-fJ5Ri-LC_SzFWWOi8vDCa7KHjI3syTkMKf7xEEkwYbKhbmmYrJfgbMxJPgdlJSnJytSFsbMOXzK_N3qcPvzTmrZEHv0I5ZioctMHKJxjGsKIKyTeigfnasyHeGBy0jWcwCWfgZZ91Td19dAbUuOrzSzw8DauPDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=UMeOKYeSIPHDeN5cww8I5PMkk46oeRPxggUt0K42GP5l1Rv4XMEN-3bnrxFRGYLNErja57Z7y_mcdfJumDgUmV_ki80uafrk3eLv_Pn_NFUayZjXkKoKIUzjwdHHbrmO-34n5g6f3RISfm3zYnDOeRqUN6TI9tMKpjM-dmLfjyVeZ6dSVS4SvG-fJ5Ri-LC_SzFWWOi8vDCa7KHjI3syTkMKf7xEEkwYbKhbmmYrJfgbMxJPgdlJSnJytSFsbMOXzK_N3qcPvzTmrZEHv0I5ZioctMHKJxjGsKIKyTeigfnasyHeGBy0jWcwCWfgZZ91Td19dAbUuOrzSzw8DauPDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=dUbuRv31Zd-CTQFd9ckz8UyEDHzPp4w-KyjHjMYkC2Chy12l1Au5whQv0Puokww87p4KG3fpWJWmzVsMZMTtXxaeXCgHiAAR66Lsf43nHpEoyIFQATiUPUkE1T2x9Sv9zyajhe0B4m3nQMKNuqxIT6QcJDQ47AYuzzOtwx6NofxVmoSSx5mY4F8kofnULOhZRBYIJE2yY3r_US3j3l-TV30j4U7eXVpT-8rMKNEk_tbNnrwjJUy7433wI_79kyxzD60A8sUDSMxj_yk9THxS7xI8oqWeqfNuy53ksCgmkCm8KjM9BnZlklizDl7w9bfL-8mQt_EpRrbZw10lp3ssxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=dUbuRv31Zd-CTQFd9ckz8UyEDHzPp4w-KyjHjMYkC2Chy12l1Au5whQv0Puokww87p4KG3fpWJWmzVsMZMTtXxaeXCgHiAAR66Lsf43nHpEoyIFQATiUPUkE1T2x9Sv9zyajhe0B4m3nQMKNuqxIT6QcJDQ47AYuzzOtwx6NofxVmoSSx5mY4F8kofnULOhZRBYIJE2yY3r_US3j3l-TV30j4U7eXVpT-8rMKNEk_tbNnrwjJUy7433wI_79kyxzD60A8sUDSMxj_yk9THxS7xI8oqWeqfNuy53ksCgmkCm8KjM9BnZlklizDl7w9bfL-8mQt_EpRrbZw10lp3ssxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=lpv1IGjs4G_a4WSf0chdqrjPgZmgmHwNa_Kdp7l88DhqaPmPKpgICJnF9FhY_EMzzbcffyN-SYOQQEGhq6p9ibN9LR_u4o1cUK97QatwY7EMOPfe-tXVWvcZvcafwrU7Sw2_W3O7oLBT0SHLC08kYmelFZ_AANPV44XHqSjccEoQKV2p19WoXtx-LnvU4_itggsZ_vYDnYTrgu9uVYwpjvqM_2izA-5EPPFPqvAHDZq2yG4kxVgdEJJ4-iAKLuBHYh0yVRtZgIgziRfjFL_uvQJX0D-eRRmGOpfWFSgUPq4H27qyt5R-fSAA4bMOuxkeuootvE0gK4Wd0KNl-6mePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=lpv1IGjs4G_a4WSf0chdqrjPgZmgmHwNa_Kdp7l88DhqaPmPKpgICJnF9FhY_EMzzbcffyN-SYOQQEGhq6p9ibN9LR_u4o1cUK97QatwY7EMOPfe-tXVWvcZvcafwrU7Sw2_W3O7oLBT0SHLC08kYmelFZ_AANPV44XHqSjccEoQKV2p19WoXtx-LnvU4_itggsZ_vYDnYTrgu9uVYwpjvqM_2izA-5EPPFPqvAHDZq2yG4kxVgdEJJ4-iAKLuBHYh0yVRtZgIgziRfjFL_uvQJX0D-eRRmGOpfWFSgUPq4H27qyt5R-fSAA4bMOuxkeuootvE0gK4Wd0KNl-6mePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUbdmR77HlzwmGirxul3ehZrJgrivTikMGB7aiNGiQ1IGM5-3a2JNbEo2S5laWews-tC2dZombSNTL-8R1FhkCHJ88w9afcBybb-xpYiYpn5sv5MnUUv622ZUSblhUACRSk5-9vj0jXZK8LC4OUtKAE8xaRMVpq5_LjVw5IYBvvXvmZkmsZkImcuBDJbPW25OuJOmy4aPwBmfVZnHAzwq3A310-6dL3JuBX0hnE1EEZEUSEjfE8ajjDitw5IFIDmf7Uaw7IN4E5_dQjU_WQdOMk9nBFB9hXMzHIbxF-4autknGYskKFAl1iEOLKqfKAEeSdMDKGEivjbdjXKqPj3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=scWQy_L2lWbnV1qZLffVjaxEscRrT2H2Dd_q2OX30XHHBBI2xL1U0uy0Hu9SYrstqZzIJBq089b4BcloBnNVx1Q4aohugaq08psSmREf18ISK9MOutQevnmjiqmzi3Uo6TwBBO6ZVLZlc6qMbV-1k5RFF5bH_XAZcegGWgLR4DPj_FCwzf81Sdfx8M75DZetqDBLi3MjFQcvK-f9NYTotTJrRYdv4Fy6rHYpsD916e80LW8asqzOSbGCcvLKe34jGrFIxjGj3Kcm9c4ARHkMKk0wO5YCyQztImY3GBjpD7XNx3Dd5H-BBtVCTUBXiwDLIiSwtJwIO7fc0WJMbPT-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=scWQy_L2lWbnV1qZLffVjaxEscRrT2H2Dd_q2OX30XHHBBI2xL1U0uy0Hu9SYrstqZzIJBq089b4BcloBnNVx1Q4aohugaq08psSmREf18ISK9MOutQevnmjiqmzi3Uo6TwBBO6ZVLZlc6qMbV-1k5RFF5bH_XAZcegGWgLR4DPj_FCwzf81Sdfx8M75DZetqDBLi3MjFQcvK-f9NYTotTJrRYdv4Fy6rHYpsD916e80LW8asqzOSbGCcvLKe34jGrFIxjGj3Kcm9c4ARHkMKk0wO5YCyQztImY3GBjpD7XNx3Dd5H-BBtVCTUBXiwDLIiSwtJwIO7fc0WJMbPT-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=CSKZF27qnkKXGhF12vavaKro2htUdhAeV890zoL5TRkA7NIOHAdwqrEbaA9B1adiYcLXuxqhIYvDUergK37UloRQi5FUgYs_GT_vh4uMv5n889mY468O-9yruI8nMxFqdxCiHQvW1KMESD59v9zhzpeCX936TYdhWd_dhNchnzm2fC3IErkOHeCfzDl8epR-XOhti0vLrDbUYixGAwlFdu95-4zWJ5HTU1mp28WXE-gq6xUKFi0UKQh7UqTaBD5s3_j__557M7sZ1OFlvlUuTp8iReY5COy6n_-XScliHBti8rETsxkI0UqVOqmqdjjuF5zyeHhNsXvmmlGC9qMV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=CSKZF27qnkKXGhF12vavaKro2htUdhAeV890zoL5TRkA7NIOHAdwqrEbaA9B1adiYcLXuxqhIYvDUergK37UloRQi5FUgYs_GT_vh4uMv5n889mY468O-9yruI8nMxFqdxCiHQvW1KMESD59v9zhzpeCX936TYdhWd_dhNchnzm2fC3IErkOHeCfzDl8epR-XOhti0vLrDbUYixGAwlFdu95-4zWJ5HTU1mp28WXE-gq6xUKFi0UKQh7UqTaBD5s3_j__557M7sZ1OFlvlUuTp8iReY5COy6n_-XScliHBti8rETsxkI0UqVOqmqdjjuF5zyeHhNsXvmmlGC9qMV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=Y5JZYw4VqWImuWlwVbYsLFe7TuRDFEFXaL6tqkp-ZC2HJCgcAlSjC-mIqcaIHUC-DnFOLD6M5NCWPQGGfFEkZP1QOhqzFxC6EZgtr3TmROlnIY4YRuvZu76ePlTLpUAcp0Unj1GI1-zH5QUTGJhR0X-ACCPLhjp6KCfrxMiw0SSaS6lyRNERWVtneMbyGFVrwJXUVu1Nvi9aVfVp-q9Df06rU-HwVEdGI0lBumsqQUh2jblVYdo9c1JTmrO5vd4UJBJmSP_ajYwbcojUcyPTi7PrDeKaRM7-9ddGAawRr5WaCpVQi2Bvqmz8Ga5IsYWwmh45Ai3WvSaTuf13KJAZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=Y5JZYw4VqWImuWlwVbYsLFe7TuRDFEFXaL6tqkp-ZC2HJCgcAlSjC-mIqcaIHUC-DnFOLD6M5NCWPQGGfFEkZP1QOhqzFxC6EZgtr3TmROlnIY4YRuvZu76ePlTLpUAcp0Unj1GI1-zH5QUTGJhR0X-ACCPLhjp6KCfrxMiw0SSaS6lyRNERWVtneMbyGFVrwJXUVu1Nvi9aVfVp-q9Df06rU-HwVEdGI0lBumsqQUh2jblVYdo9c1JTmrO5vd4UJBJmSP_ajYwbcojUcyPTi7PrDeKaRM7-9ddGAawRr5WaCpVQi2Bvqmz8Ga5IsYWwmh45Ai3WvSaTuf13KJAZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=pxQ397Gc-VB2RKq1lsTD49hnTVkLpqkcfxWQv5euKRptTYXUGWwavEOwyg_dm-oSMLoTMx-K0aUphXaPvSSZQft5vY06I1sebay363mPduvfIgl_DaoirQdMDJUzsSKca-XbLTx7Rmuq_anuolm07AJFvIW2Jm65gfeIhun5GzBmTf9Xohb7J4GvavA5Nbqj-9XiEWoxEiA3QErmBF-IBrynRhD3_8KrAosIYg51EWq8W5PNM-VXGHZbGSQpcrxroZJTDqpA1v3b-GMnwGMI6jv6WFTy56rhdCgF7y3AnKc4ygp2LE_7O2I6wbyFHFOfZlLFXNMXhjQKgFclzX26WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=pxQ397Gc-VB2RKq1lsTD49hnTVkLpqkcfxWQv5euKRptTYXUGWwavEOwyg_dm-oSMLoTMx-K0aUphXaPvSSZQft5vY06I1sebay363mPduvfIgl_DaoirQdMDJUzsSKca-XbLTx7Rmuq_anuolm07AJFvIW2Jm65gfeIhun5GzBmTf9Xohb7J4GvavA5Nbqj-9XiEWoxEiA3QErmBF-IBrynRhD3_8KrAosIYg51EWq8W5PNM-VXGHZbGSQpcrxroZJTDqpA1v3b-GMnwGMI6jv6WFTy56rhdCgF7y3AnKc4ygp2LE_7O2I6wbyFHFOfZlLFXNMXhjQKgFclzX26WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=ET2T4u2ag3euCDjwoZNF1hoGYiGaUutmsDp0fLJofyy-e9CG-5mDfrYTFYgXmYniIvfOPOfTKQa8s6J3nYOZt4s-bZ8_K9OD60MnpcYcQZbxz1DPOgscCTrlQtKbIL5oAqqNWEsM25All36nSuX0VQZxHoUTVgwsxmT3g6uH2vhnAVqqoAnqzKAS0Uu-4b_qw93v8a0FWwpKsc_3BdItOFrbYHBbFRjJg0FScytjXgOKpXgNc0tHkUUzR-iyUM-trMpnkKNlGnnWVBY_3dsQZzzCSB7SRRg0GqlINoP8Zn9ziuLqClyGWkrahE7YGy0ABF9CEyjWdI7WSyswIVvbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=ET2T4u2ag3euCDjwoZNF1hoGYiGaUutmsDp0fLJofyy-e9CG-5mDfrYTFYgXmYniIvfOPOfTKQa8s6J3nYOZt4s-bZ8_K9OD60MnpcYcQZbxz1DPOgscCTrlQtKbIL5oAqqNWEsM25All36nSuX0VQZxHoUTVgwsxmT3g6uH2vhnAVqqoAnqzKAS0Uu-4b_qw93v8a0FWwpKsc_3BdItOFrbYHBbFRjJg0FScytjXgOKpXgNc0tHkUUzR-iyUM-trMpnkKNlGnnWVBY_3dsQZzzCSB7SRRg0GqlINoP8Zn9ziuLqClyGWkrahE7YGy0ABF9CEyjWdI7WSyswIVvbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=D6HNP8mXX12TkI_M6QWPNZioA-8GhHr4PwmCrEnpvlrEWpiGkW2Q09mSNb0Z02w9fWYkxlNRwImvq70_r8bLRBrxQ7kS-Hsmgb0rMZ6_M2NmQm1zl1D95fcfA3hDAmR2I-SA4hqdy7U7JJTBHEhuCXzl_RjrbFHwmJLZ0L8FYchaEPeqE_Vqaa-lACtZ2cM6fvyKGiStYhC1tydUQt9ofLwKdfqu15KrwaNaS5rwqWosyaO7uPdImreEPLQUbEAzMimUSip3hU7EhAC-hP2UZbVOgYL-WMIRAU5b1aH92c3CpImZMZ2kspGPf9cHnq7MoR5qJbjZMhPtZsmYUvf8yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=D6HNP8mXX12TkI_M6QWPNZioA-8GhHr4PwmCrEnpvlrEWpiGkW2Q09mSNb0Z02w9fWYkxlNRwImvq70_r8bLRBrxQ7kS-Hsmgb0rMZ6_M2NmQm1zl1D95fcfA3hDAmR2I-SA4hqdy7U7JJTBHEhuCXzl_RjrbFHwmJLZ0L8FYchaEPeqE_Vqaa-lACtZ2cM6fvyKGiStYhC1tydUQt9ofLwKdfqu15KrwaNaS5rwqWosyaO7uPdImreEPLQUbEAzMimUSip3hU7EhAC-hP2UZbVOgYL-WMIRAU5b1aH92c3CpImZMZ2kspGPf9cHnq7MoR5qJbjZMhPtZsmYUvf8yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFI_CsNbzvSGQmW44txGGj_c0MeTCbsWdjdrmJjBfAPkZ0eSY-xQK_nKwmxcCvLrpSs9h4w39zMOKHa0BxBV3p9pX7idpubhE8fdtsiqPy10q2SjNchgyxfuD6Pr3bS-03UD6Puv6Z1IvcFK7h8BxSqq8CbQDggk3s7YAyLVh_LvMeTon9yig2UTqw9rQiDCK5KoS87MSxOe9sl9rlDLNXPr0U8KUbywusWKx5qQt_fPMM_TbmHw3Uf5uHjHWjmKboUNbC0CcDmL14MCXyFatKGwW_BYOcJct_S8cNv1M4Z2QooBUAXXmwvnXoKgKZ5LR7lTFwymhP3coaZ6jCg_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbEa19MsOsgiPu_RJlRcAbY7rZvh2cN6jb0vOour8M7GgNBXvir8SEN7UUo5u58ZB9rm90mhkggYNpgeVVfjpjld2QLz54g5LAnSGTRcN8YlB0dunscJJ8WnP_MIk_tjhxBQbEZlnOzNKQ10UpA9m7kagApKQssCKGhZdiaP6uEkkPMM4EAmTQVBBk0yzNslNuknCobBGO_C0FxQ0R7xo2o28YB5gJlf5LjLUzIHRBXx3uu6U7v3pr8pgL7PT7euU5ocvmuuyOhvFownh4lPMmwkGZMFtSdyE9WiB3wGMJB7a8vmALw2g-e5jmRBgw8dGbCBZbZDT2KCao1QIvBm1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/run2656VsxCvvrKa9tXkV7YrZOW3y6-A9EUngQRtajPYcsRrPhBe-4I1-CCkNmn85x64V1c4FNKL0Md3yZtgTyVlQkoSy5CzowyVDNJHHJ1k2GPV5JQtDajizQOQAzPIt9OGAL-pS5h7q7ZICTyYJ6WGiyODoK4MRySNO0rrnRjykT8qJD8ZL_DFGtoKb7s-lj3MSV27RaOSop8bsOurtfI2r4kB7BvxKIFpciGI-AJltjOc920E7_H6j3vCGXYN8eUXAb1K_T6tvV6XE0ahqNJM7oxR9w6irxsR1xeovTJhibDkdh-taPwXp--DrpUFKZ9AGHXu0zs7vCovaPit9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlgrCd72LhUl3EFwkH4UhYQ-rQ2f4q0uBOgWyRa_fWMAOd4vGSxRNcwk0kh0Takhf0oRKe4j4WBEP0ZcewZIOkxAvrItahI37aWkgvlnoVDJj6pX8GJsIrAa9gNgwgtYB3wo6ymPi-35XzqE06BBT9f9N8djAWYlWP13js1GTNBBhLxC4cO6vI3c44lil3wA0QSSHauFJ1zsFyc_NXWObEB5A-NlKWNoHrijM_9H8ZPcbxG02rx6PtvMYYwwhP6JPciayEKt3kneTvk0dvHsS9oyaJYX1UFUF3r9z6Bwge5tw71EwQ-xuAFWXcLdhvjuTa2NfAtt_buimkJ-Odl-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt7etjm69M66BO9fnynYa9FxjMYxgTKvC19GRS1C4r_khceqLPud28VAR1d2yrI_NvsK5D-Io-jQttkAcRuPEKDVHj4wmWiX2KjZyvwC1rG2xO1q2hb_kB8h7LVK0lzGst-Bf7H8BdErKLc-iLY5KEUuDcSiwru8DvQR05fze1xqX8XW-XHnXJ_Kp8S6kKYo3SVtcUeP1Lmfdv6lLLfVS5uWr7_Q6Qr12sracKVJgis8XuMuJtN-zbyDkDteNr1xtE9EDwKs6xzur_cODPpA4TnzP-9IImunVsnSkDuE8m-gvbySO0ek-gyIzQfM_0TO4Cy5L43rnYu5HFs6yG7-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmjBSqE7hi6_Crqn8Q5o0rL-uy4meDsuEqInWM1JwNGS2tSBSAKuGDSd9OcbrXhHFjFgTQMrWBF5hXL_DFJVgGAXPLODx0dmfmWJJRzWJgequt-rg7XU77DNsdMp3UM3yySq4DCRiMelX0DqybQumC2As5Ef0jqotqoedyAMWSh6rR1KeN67jNA896YAst4VLa_l5kP_OulFVLuCQ3N9YOhO_qa0bCLXXl-yYpuiTKnBMnbwJzlU7b4oQEhLa2NCdpPoLsmbUY6HxAaZeZtLgnL7UOHPVs0zDFz3G0O_0FpU6Sa_i3lKtnK1BIn43Izd7a46yfLUEWC5qFvVFAbyrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4vGA3-5tUjordzumydQqba3dcBB_A2vmvw5QxFojv57gdKLzbdaQRfpWNZbQ0oW0uZ7naoibhObbxlrRkHk9_AdGfIivvWud5sWefYAReSXdc1WiEmu5i0TwAjnntPBkcSNGiuY--uT6lJs62-_jd_TCzur3EFhV_sdBi6HmmxI6MRuOLl1MQ1nHmJ5tRdmoxteiAoJrjlwe-AFrOInXvVdvuVUSHaSg1A9lCUHiQMH73rgvTBSHktKniZyVFNvmwMgCXrWyyJthf_92qLxlcCsGy7TF0lLoqbQenkBLE0OuSqZFlY2j666gPJGhubVbdCQrLh8etLLRV6NIPg8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=kkck-TtT1rblzbZvzIMvpTyR3taesslTF16-caU4Z7PM0Ok_KRRHeRpzjIq22d_D6i2lWEllGx2ac_-sDW7RKta-2Dghm064bP1hiPeZe_nkqYq_NA6wB4VxQSXiBTiTtGef8MU6yzJEqw3c-QKNVtHu2vuaYr3gyfv9AOhSinh2E3kTTCNN3pINLlOXhoUoE--ZLzADx5mT0R8Sau_gVeqb4JxtYrR4am_MxgHFOfXlVFz-HIz2aQw8X6zCaOLCnd_LnGzuQRQqAwR_IgnvKLjypaDRFgbkMEordItMLo8JWRZu695n-QOXUDh2qw3wdZGRpJMTugENyVDSjvKjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=kkck-TtT1rblzbZvzIMvpTyR3taesslTF16-caU4Z7PM0Ok_KRRHeRpzjIq22d_D6i2lWEllGx2ac_-sDW7RKta-2Dghm064bP1hiPeZe_nkqYq_NA6wB4VxQSXiBTiTtGef8MU6yzJEqw3c-QKNVtHu2vuaYr3gyfv9AOhSinh2E3kTTCNN3pINLlOXhoUoE--ZLzADx5mT0R8Sau_gVeqb4JxtYrR4am_MxgHFOfXlVFz-HIz2aQw8X6zCaOLCnd_LnGzuQRQqAwR_IgnvKLjypaDRFgbkMEordItMLo8JWRZu695n-QOXUDh2qw3wdZGRpJMTugENyVDSjvKjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdJBHrTnRwzwH1xlnInP9V-Cguifv9chKImO1yztgIOZruK9tLiHDERpuigH_y9DH6nQuOxm53mGNNdjx1dF0rZdUmbJIz2T1rZ3xvOTHQ4ffXjinLJFypGSktx3LnVq3Q7URdBretscADyLxUq1giQzYUGG5dOMvyJDUDmSdnSKxskxRNhwMbozcURhz3_7zvzaQm-ifPlQF9ovfhadV0Gud_SvVzrYLp2c4QETTuI1xa-59dLPMIt1lNznfCQakF4SrbL5hQ4fI0Fm43gai9Nif7qGewA2OfJqteQZSoSwjKU0EhT2C7KPzp2jHBwBCp0Ev-7ebzMntWGE4vf2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=eCILAk04MqhlveVNFF_4BVy0gtY-McVz8882UPS_QUfqNi_hppdHm8A-udjukWjr7MHyyUZBQNsjxTpPXZ1ZUx89ElmAahkIJdJWh0co3vvnMSC2Uw0rMrxFAMzZGfZV4OqCmXkxb0fWq97BDw0ClJpgfefXcx-vHerYQonL6wVcwY8SXaViYv_NMIvDXiLgBP_7DaKrgTsf8PNG63i9gtXpAJq0rMryjkKXD9qMwzhGoIeGONveqkuTYX31Dc_A1Qi1rYgoNE0iGOkDl-4jYFAaHlLkZdTF9TKCug1_q9Yc2WLpdr2gvD2_NdGqNk3cc370LU3iNxqjQaczEgHdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=eCILAk04MqhlveVNFF_4BVy0gtY-McVz8882UPS_QUfqNi_hppdHm8A-udjukWjr7MHyyUZBQNsjxTpPXZ1ZUx89ElmAahkIJdJWh0co3vvnMSC2Uw0rMrxFAMzZGfZV4OqCmXkxb0fWq97BDw0ClJpgfefXcx-vHerYQonL6wVcwY8SXaViYv_NMIvDXiLgBP_7DaKrgTsf8PNG63i9gtXpAJq0rMryjkKXD9qMwzhGoIeGONveqkuTYX31Dc_A1Qi1rYgoNE0iGOkDl-4jYFAaHlLkZdTF9TKCug1_q9Yc2WLpdr2gvD2_NdGqNk3cc370LU3iNxqjQaczEgHdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=TrQcvXOm_BNQqTHSUDxzMPwTp9CQvaa07gtwI-Ao0uyfHSlyGYjiJKwkKvCXaBqzDUAIEY1qBVwRLtaj3He6pbqFU83N55H5dn5QhDPUWmTbnohhgz9lbswEL9Oavt1l7hh90hf-kvgrZfmWj6sCT7S_zRf6zT0pCHb8zJ9doT9OHVCFGOvv_7upkRHyKhJAfKTW1oaopd5Op0ssryg2qoZKdcc9eZkUuWMcA2zj5qxugu5EXogFpLvpAuVxjzgGGtk71hixOwRpwY2VLjzanrkjPubmV461PETDZwVWhLXBYjgfRe4_n2QZeuIcMCJjlM_KwP-eoZR7NcS4kjD_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=TrQcvXOm_BNQqTHSUDxzMPwTp9CQvaa07gtwI-Ao0uyfHSlyGYjiJKwkKvCXaBqzDUAIEY1qBVwRLtaj3He6pbqFU83N55H5dn5QhDPUWmTbnohhgz9lbswEL9Oavt1l7hh90hf-kvgrZfmWj6sCT7S_zRf6zT0pCHb8zJ9doT9OHVCFGOvv_7upkRHyKhJAfKTW1oaopd5Op0ssryg2qoZKdcc9eZkUuWMcA2zj5qxugu5EXogFpLvpAuVxjzgGGtk71hixOwRpwY2VLjzanrkjPubmV461PETDZwVWhLXBYjgfRe4_n2QZeuIcMCJjlM_KwP-eoZR7NcS4kjD_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=QQ5u_r6FuMXOTjbITOv-Yxotv6lQjBEZuQKEWHnnJKz4_n6pBIuDgpZyF0xoNyFmf0Lua-aP4DtqrYPycfZ46LcQeTfCvnKZ3Qj9GepQ3KFGXvkdGTfQ3DTM7eM4toZvVjf5ABZjlvIa99e9gImMyF9-nW7yeQUtZImAZwF_py8IktPRa9gw32mn2rwf23YnSGcdKyslLiR6kWvsR4wBmsu31SocEgNNBUIB3SwfZmae9xsInuaYZsr-l9Hdgo_JKjtoO6p5vSu4u7WbhUmppZdTcP37AicNGyeEc90B-Ca2pX8-Xi09-N0bhCVAk5pN8W7YH6suF-KyB7xJb8vHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=QQ5u_r6FuMXOTjbITOv-Yxotv6lQjBEZuQKEWHnnJKz4_n6pBIuDgpZyF0xoNyFmf0Lua-aP4DtqrYPycfZ46LcQeTfCvnKZ3Qj9GepQ3KFGXvkdGTfQ3DTM7eM4toZvVjf5ABZjlvIa99e9gImMyF9-nW7yeQUtZImAZwF_py8IktPRa9gw32mn2rwf23YnSGcdKyslLiR6kWvsR4wBmsu31SocEgNNBUIB3SwfZmae9xsInuaYZsr-l9Hdgo_JKjtoO6p5vSu4u7WbhUmppZdTcP37AicNGyeEc90B-Ca2pX8-Xi09-N0bhCVAk5pN8W7YH6suF-KyB7xJb8vHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogU93LxaUZOU25FrUezm6h30Z9RzNpIGdAtSkxJCRums0013KtgKgipqpqaIGq66p3H3o1V-Qp_zfu_FKutDyRa9iniZ13yX5xUnrmvDrNt2Bmwl-oYN10kJ1YUGnyVJqiu_IQxeEHqVH1B3lLxffglL1JQRsBlpi5bVKmbn9mM2zTMdlYe5fQTqQ2q9zw7DZYiTkJfvq-O3jmGH0oewFggo4MUkLb_DNoyvL1CRnz-UKEHOKaLgzbtstutcTAPKl7M0gdzA9K8aN5hyXJInbQItdv3omUZLuhzOT-r3d9o8RLsLvE1NQjp9wSdgTmqZRB2IsauPdxw8C3rqNvgxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=CX9Fw0izITMzk8kuKeXbKOUjxPQlJkfaLDaQ00WfiNpskg-iWPU38QIzJc_VztgVDD8P73ikiRM-SnJEOZ5-v1QrbiFCf_jID7dguRmexLpUok2RSgM9yRIAEqbUdTagXuCFLYgl9P-WAefvinMSk6iVYt0AVPVCbqA69IrYaXctNwdAAqQeNRpNSieS-JJWdzG6oYyWXEdTqPOneCDTROchMaFZgMg6qUTILJn7LXtsUO5kQss84qFhp6KzHIn86mPM7Q8xPxsiMwAtWBL1vG90tXdp1LOoxXFCSIMwAEi9oVyHdM_2VoR4Ozq0nVnW2a1aNgBxZWAFC_KQ0VkNKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=CX9Fw0izITMzk8kuKeXbKOUjxPQlJkfaLDaQ00WfiNpskg-iWPU38QIzJc_VztgVDD8P73ikiRM-SnJEOZ5-v1QrbiFCf_jID7dguRmexLpUok2RSgM9yRIAEqbUdTagXuCFLYgl9P-WAefvinMSk6iVYt0AVPVCbqA69IrYaXctNwdAAqQeNRpNSieS-JJWdzG6oYyWXEdTqPOneCDTROchMaFZgMg6qUTILJn7LXtsUO5kQss84qFhp6KzHIn86mPM7Q8xPxsiMwAtWBL1vG90tXdp1LOoxXFCSIMwAEi9oVyHdM_2VoR4Ozq0nVnW2a1aNgBxZWAFC_KQ0VkNKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUwMJRbMO5-abt1ZOgvM3TTEg3oXy7xQKwQFfiLL8dDUX9epvTdfZGGHZcFTX12fm_K2JmqnBBHayS7ZabY01z7wSx1YwPbxTm_KNJjNbWOrbl7JemI3J88Zj7y2_YLPLhGAzyXQ2wLerPgmwoIFpYxleP-ifuyRQUiIG24f8Y28T4DuGSd-4Pc4bOhPoxY6oNwVtNAaammeuCSbkUSqi7pFIsCfDWeqDRpo5RMxe4jjxrFKplXVxaYahwwVSqkGSB8-4KaAn3um8myid2yqrUYnCFVrQOvMR_9dlMokcHwnWJzVds49hM8bAwczBWU8AmgVLoueQnko_iBKBvfIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=kW00cmxo80qJ7W7OKr1WyD7ejkOdvpgX0_lOyAfgtxspDsPfJeIXELKUP-6T7BbONLXy3Jjmg93LKlNBq5bDeblUJfWhaOl03fOZUMNRIw8SjiGYPBcQPBk9bdc9j4MdBBW7nIS-Fz7k3s_Zkj_G3Szlmu1yhcPFyStjcJvhmhFDqtF8s7uy0aI8c-q_ER_atnccAgs-f2LiH8MMzVsaej7YhH2qywLDXJqzjfPhXfa_Z0NoKCP5ajhGd54tBLYvOkbRl-8gmR1ZkzuUDzO81ZUELO7yDZIVkd0C-f6XPCBIeS3hFgDPSYHxDvtsrlyf0KjKfFUMOjjlzhL7uSJX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=kW00cmxo80qJ7W7OKr1WyD7ejkOdvpgX0_lOyAfgtxspDsPfJeIXELKUP-6T7BbONLXy3Jjmg93LKlNBq5bDeblUJfWhaOl03fOZUMNRIw8SjiGYPBcQPBk9bdc9j4MdBBW7nIS-Fz7k3s_Zkj_G3Szlmu1yhcPFyStjcJvhmhFDqtF8s7uy0aI8c-q_ER_atnccAgs-f2LiH8MMzVsaej7YhH2qywLDXJqzjfPhXfa_Z0NoKCP5ajhGd54tBLYvOkbRl-8gmR1ZkzuUDzO81ZUELO7yDZIVkd0C-f6XPCBIeS3hFgDPSYHxDvtsrlyf0KjKfFUMOjjlzhL7uSJX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=TlcAjeHZpEE62dyk5K7HfjRxGEK-2EEGKrKRI5cbNZK00DC6o49Atq5T9EMjt13nluMUUMoLEhbRkY6j8NOjwv6FiUoSSTnWeRWZ5T5AbQHh-cD8Hi93RD4gu1es3urhK-W2eXMo2cikRWr4Ea5Rq6_oPwzOZ5erZQfLaK7o9DRPLEsi7QwFhcdyfzRJbxmeCLIWT1NJMSCpveiUN0wQB-T66PhRzxX3J_Tfsewtl8Rqe56XAi6poEnf3k-vef3AhRPAxfhRTK7x4p8ONn913lXOca00ssY7r7Y5jcSmyJcR-R4tChOS4CT0OyeZ4zruOnw599luaG_ytpyLTr5QOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=TlcAjeHZpEE62dyk5K7HfjRxGEK-2EEGKrKRI5cbNZK00DC6o49Atq5T9EMjt13nluMUUMoLEhbRkY6j8NOjwv6FiUoSSTnWeRWZ5T5AbQHh-cD8Hi93RD4gu1es3urhK-W2eXMo2cikRWr4Ea5Rq6_oPwzOZ5erZQfLaK7o9DRPLEsi7QwFhcdyfzRJbxmeCLIWT1NJMSCpveiUN0wQB-T66PhRzxX3J_Tfsewtl8Rqe56XAi6poEnf3k-vef3AhRPAxfhRTK7x4p8ONn913lXOca00ssY7r7Y5jcSmyJcR-R4tChOS4CT0OyeZ4zruOnw599luaG_ytpyLTr5QOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=ZpSKedqZHBO2Hl539atzmVLFv-X49YH_625P724fIPSI0nQ5KcvK_7tP7KFWkmQIn-xmulxiQHwvOIl8w9fcB1BInnUYyTO-aBn88wqfnmnvbR9BKewdDM7xR4OHgGvYrTjopHVQUTqqy2908URPGDeCKmwAEIGe4L8rcy1f-su92sD0uOXc8DRkP7eHOuozYWAEHBBZOWk6svrKimTsszodr9J9LI-aXAZw-NQvMgpyjWzMrccKg5cZ1NZH_UWBgwN-_tU1KumatWvm5KnVjzX_JN3TUr3FSIj9HvDZvDjdmOdXY9M4VRHvacpHiDpuY9OYXkkypaWM9wSdtgAi3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=ZpSKedqZHBO2Hl539atzmVLFv-X49YH_625P724fIPSI0nQ5KcvK_7tP7KFWkmQIn-xmulxiQHwvOIl8w9fcB1BInnUYyTO-aBn88wqfnmnvbR9BKewdDM7xR4OHgGvYrTjopHVQUTqqy2908URPGDeCKmwAEIGe4L8rcy1f-su92sD0uOXc8DRkP7eHOuozYWAEHBBZOWk6svrKimTsszodr9J9LI-aXAZw-NQvMgpyjWzMrccKg5cZ1NZH_UWBgwN-_tU1KumatWvm5KnVjzX_JN3TUr3FSIj9HvDZvDjdmOdXY9M4VRHvacpHiDpuY9OYXkkypaWM9wSdtgAi3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eM3Pe_xyYzOIkY9y2ZbRWqPwp0xb5w6ZipJlCo4ERl5_rv8l-UGa2BkzXE5JOOxNYrS0ZguESLVZC0AoxyIY-bnVrr8QrU0_sl2lcSr2r_RoAz04FPn5Quis_RsaQqydpBvlsKXP6N1-R1f8_e5tZoHrMNE4tsvB2n9cTDuWt56Q3KmDSzPPznTEn_5zenGZpPqpLjhElf7UkApsRB47adimdCHklQn9GCo1IYWkSEJnjO4HO7OKpPpw3DvRgfzcgagxiHADkMXwt-Vqni0nw_j3VhRa33WEirNIiTluK7YyCZPy_qg-uXddETktXpxAph6AWZCMdMUaefEGiMhB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=onee5U4gxaCL6XYfc8JTFBIKNSjvARE_ZfU8-pr2j83CVbrgcTVtnBaD5Gxf3dSHo3Ov2RTCZDgP7NkHoIwxq1vv387ZHFZ3eJUXlNAwwQVVHKqIVA2SipCFNQCEVcpNcr5CL4tAfvFTK114dXLAj_7Lb-2P8uQq7zRn-JvWmbYZSD0xvIRzK01gJeS_rOuLhtIn56n1DYeHlxZHvxNKvw__zOAArV9d2ngKpx-p4gJ3CsONDu2mWs8Uxvm6dV91I62hOa4JZZVGQKtfsIN8ERWY6kX1zG4RscuG6IA1mHSIcX6GdO4WfMJJLVJ3qXW-xkTp-YUJTljErm7gRKehTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=onee5U4gxaCL6XYfc8JTFBIKNSjvARE_ZfU8-pr2j83CVbrgcTVtnBaD5Gxf3dSHo3Ov2RTCZDgP7NkHoIwxq1vv387ZHFZ3eJUXlNAwwQVVHKqIVA2SipCFNQCEVcpNcr5CL4tAfvFTK114dXLAj_7Lb-2P8uQq7zRn-JvWmbYZSD0xvIRzK01gJeS_rOuLhtIn56n1DYeHlxZHvxNKvw__zOAArV9d2ngKpx-p4gJ3CsONDu2mWs8Uxvm6dV91I62hOa4JZZVGQKtfsIN8ERWY6kX1zG4RscuG6IA1mHSIcX6GdO4WfMJJLVJ3qXW-xkTp-YUJTljErm7gRKehTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71745">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=n0nhJuavx1m4U_ejnn6xwp2BDGuuUMGwH_WxUSimmBRNvWv_PeL8yG1ps7jcnLM9a-4-i4Sl6pdjt4c9-kE-b7q19tCU_E5Z9t3YO1qjy0k-kzPhb4v97cjd5zNbpmOP0fvWZW9QQmIKlKlXcSDNYzvuCQyLkVem7TkvNozaLe4ZGJUOd8j6HqG72S-LcTsDqEVNRB1E_WHikvFim1eif_6LmpEmiuQhdrd8KlSrSGl5YBKSQsXIZW1TTqAsj5y6BfyBX-UldJD0tAjxGzf24CDIEUZW1LVpkMBYFSRNp1X70hvs5TNM8QkMnbqTKOYX69z8pYzx935rvBIX0Ks5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd261e6ac4.mp4?token=n0nhJuavx1m4U_ejnn6xwp2BDGuuUMGwH_WxUSimmBRNvWv_PeL8yG1ps7jcnLM9a-4-i4Sl6pdjt4c9-kE-b7q19tCU_E5Z9t3YO1qjy0k-kzPhb4v97cjd5zNbpmOP0fvWZW9QQmIKlKlXcSDNYzvuCQyLkVem7TkvNozaLe4ZGJUOd8j6HqG72S-LcTsDqEVNRB1E_WHikvFim1eif_6LmpEmiuQhdrd8KlSrSGl5YBKSQsXIZW1TTqAsj5y6BfyBX-UldJD0tAjxGzf24CDIEUZW1LVpkMBYFSRNp1X70hvs5TNM8QkMnbqTKOYX69z8pYzx935rvBIX0Ks5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر از همه شانسش یک‌جا  استفاده کرد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71745" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71744">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=oOumjzm8ZskzugKqZ2aGhBI0ngxMQKRBic2cGnQDPi10ld1SVWJtCfTMD23gUyc-q2pkCWy4cYEv7fdgWVffYWXlwBSNIcJiFHJhizqeYZGOWYpMiWsWBlb7m4OnW0EYp-Uslpm_7EesunWXIxxziz3aa48NrvFR7ZNqi-ZS5hC6axcfQxnke3eFWmDve43SACmx7wyRVY2sIRLv0g1AIvuappk4G-UWaV_M4gMEKD1PHbeOX_pADyuocj-6_b2O5zikGaqIkuCheALFXUJqN2pJlDQWEIOPqllOnQudgzqV3oY1edhDMIxhV9YgGMi2BFVGNJdTQ_EgzI6Hs1sqDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9a723e6.mp4?token=oOumjzm8ZskzugKqZ2aGhBI0ngxMQKRBic2cGnQDPi10ld1SVWJtCfTMD23gUyc-q2pkCWy4cYEv7fdgWVffYWXlwBSNIcJiFHJhizqeYZGOWYpMiWsWBlb7m4OnW0EYp-Uslpm_7EesunWXIxxziz3aa48NrvFR7ZNqi-ZS5hC6axcfQxnke3eFWmDve43SACmx7wyRVY2sIRLv0g1AIvuappk4G-UWaV_M4gMEKD1PHbeOX_pADyuocj-6_b2O5zikGaqIkuCheALFXUJqN2pJlDQWEIOPqllOnQudgzqV3oY1edhDMIxhV9YgGMi2BFVGNJdTQ_EgzI6Hs1sqDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نکته‌ای جالب درباره جنگنده سعودی که در مأرب یمن سرنگون شد:
شماره سریال (5529) روی دم هواپیما قابل مشاهده است که تأیید می‌کند این پرنده، مدل بسیار پیشرفته F-15SA ساخت آمریکا با ارزشی بیش از ۱۱۰ میلیون دلار است.
این هواپیما دو‌سرنشینه است؛ بدین معنا که شمار پرسنل اسیر یا کشته‌شده شامل دو خلبان می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71744" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71743">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=kVJ9065coVx6UDOFYimEfTPYaUpq7tFwMyRfGuvaqGwwNJ_wTXrS7QP4OoTvEecciYDLf-n3wSnz1ssSFvVGm1pWQtVQxnpOkdLVJoGbfZpWXWXbBcy1l7coWGcmNBxW8C8so8hIsTjA8QHhsVgVyoJGThabLLw5kl3oXT2sz-PDyHavmXiDeiIJFZGAp8y_oKyWhEFzICaw9Gj_olOJUH19evmOmm09TUpwvzJs1zTxXYdquWhM-rkwpg92uN22P9BOTjg04VhwqkHaNBX2mTBAlDLgDY53AiTIct_pwBOR1yIFsk7m14x4h6ylUou1tTf3OI5cyYaUeuLtcRpRuYhjUuFSWqd26vxxYgEqFvYKdtObvmU7E5Hv5j0ioP1tSiaKh8hI_1_qfZo612Ms7pS3mgny-eyZUDOqKCNeG6qin0FIEny9lZ13Ic0SP9sCzVGQKRQdt-rYfEG8oPjNn4UdxFkjTm05qANnvn5YTSFL8Z2OzrBRKcx52Et1DpJ5fUm8l_GS_uxh1aXe7OtrIrbVp3PFnGTZvIQVkDtTe6BBDq4zMGetHH6DLSsfrRP3zRlPMkxB_9-CmtFmhaSjijnht5hmdhpwpIJPELFvu4q2dB1-Uap4qrPcf0prPZZpQlYXf3f1R_X1Xi_IiVmvpnkzuHimEbEwS4CzetDKzZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb7be6388.mp4?token=kVJ9065coVx6UDOFYimEfTPYaUpq7tFwMyRfGuvaqGwwNJ_wTXrS7QP4OoTvEecciYDLf-n3wSnz1ssSFvVGm1pWQtVQxnpOkdLVJoGbfZpWXWXbBcy1l7coWGcmNBxW8C8so8hIsTjA8QHhsVgVyoJGThabLLw5kl3oXT2sz-PDyHavmXiDeiIJFZGAp8y_oKyWhEFzICaw9Gj_olOJUH19evmOmm09TUpwvzJs1zTxXYdquWhM-rkwpg92uN22P9BOTjg04VhwqkHaNBX2mTBAlDLgDY53AiTIct_pwBOR1yIFsk7m14x4h6ylUou1tTf3OI5cyYaUeuLtcRpRuYhjUuFSWqd26vxxYgEqFvYKdtObvmU7E5Hv5j0ioP1tSiaKh8hI_1_qfZo612Ms7pS3mgny-eyZUDOqKCNeG6qin0FIEny9lZ13Ic0SP9sCzVGQKRQdt-rYfEG8oPjNn4UdxFkjTm05qANnvn5YTSFL8Z2OzrBRKcx52Et1DpJ5fUm8l_GS_uxh1aXe7OtrIrbVp3PFnGTZvIQVkDtTe6BBDq4zMGetHH6DLSsfrRP3zRlPMkxB_9-CmtFmhaSjijnht5hmdhpwpIJPELFvu4q2dB1-Uap4qrPcf0prPZZpQlYXf3f1R_X1Xi_IiVmvpnkzuHimEbEwS4CzetDKzZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار فاکس‌نیوز از روی عرشه ناو هواپیمابر جورج واشنگتن؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71743" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71742">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مجری از خلبان آمریکایی میپرسه چی بهت کمک کرد با اون وضعیت از کوه بالابری؟
میگه هیچوقت اجازه نده کمبود انگیزه باعث بشه از تلویزیون جمهوری اسلامی سر دراری:))
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71742" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=oReEFvIMuOnaOaoO-pbL75Onlo-nGyNXEFuL_vl_DFjYRMGPwH3EoKr8rP0IhUERcHcZ-0cod7cGVu-vQUUjaLkaEFtf9unFjSh0B7SHwTL8HaWETunEpo25kkeWiRIPzV251Asvs5ghlQIvj-suQ3G1EPvpm48LPCiyAaFMe6uN92k6q83kxm_vUA9BDt4c4m92f2KexXy2ZCnGYpW-H7FAnwvNh0zCAMQMo1qkkf1e1-RBLKw7cgSemv7R-kQyCWThwXbdRsGCv9qP7lOhUSKEt0I1jFKJz_C4mVXMOo_Dq1ffhz45mADbJmESFYTEmozqWBs5rfyVbFjKUdQWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ea75ad1d.mp4?token=oReEFvIMuOnaOaoO-pbL75Onlo-nGyNXEFuL_vl_DFjYRMGPwH3EoKr8rP0IhUERcHcZ-0cod7cGVu-vQUUjaLkaEFtf9unFjSh0B7SHwTL8HaWETunEpo25kkeWiRIPzV251Asvs5ghlQIvj-suQ3G1EPvpm48LPCiyAaFMe6uN92k6q83kxm_vUA9BDt4c4m92f2KexXy2ZCnGYpW-H7FAnwvNh0zCAMQMo1qkkf1e1-RBLKw7cgSemv7R-kQyCWThwXbdRsGCv9qP7lOhUSKEt0I1jFKJz_C4mVXMOo_Dq1ffhz45mADbJmESFYTEmozqWBs5rfyVbFjKUdQWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاله مرزبان بعد از دریافت جایزه بهترین بازیگر زن در جشنواره ونیز، جایزه‌ش رو به زنان ایران تقدیم کرد و گفت :
میدونیم که سخت ترین دوران زندگیمونو تجربه میکنیم ولی نباید ناامید بشیم
یه روز امیدوارم رویای مردممون برای آزادی و آینده بهتر به حقیقت برسه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71741" target="_blank">📅 20:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71740">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ3jbuteg58KNnVGB05LNvGJcurnra5mMUyrPyeg7CEoOwFi6RC-wy6FDtwarU6lHMAAP1eqgl-TtgFUoqQt55g0_aLc1Iwp60SiRmxjzcR986PZHM3OmPT7NDTND_Yt03tpRilX8mP--HoGP3vpUdOknfKQUwjCIEAPFWkWRF90RI0qHPYcmxvXpKDpwu79mqJ0l8gmpTzJO_-PBfXDsXyfVTw0Byttepjv4dBqG43_ym7WANSl4ucFjKvURvJ9WNNBsi2Eaws_WsdZMOBLAdkUmn6pnDsa1yjIOGfeh0-O-Sfd0_hL6WoPvKNmbmy5dG8p_oJYT4o0TP7B5jelYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت گسترده ترابری نیروی هوایی آمریکا و جابه‌جایی مهمات میان پایگاه‌های این کشور در اروپا و خاورمیانه امروز!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71740" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71739">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارت نیرو از پایان قطعی‌های برق خبر داد؛
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو:
خاموشی‌ها از هفته گذشته به پایان رسید، امسال ۱۴ درصد برق بیشتری به صنایع انرژی‌بر کشور اختصاص داده شد!
بیناموسا میگن دیگه خاموشی نداریم اما هرروز داره برق میره
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71739" target="_blank">📅 19:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71738">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIwz-WreFrlqss9NHR1HCbY2KHvckhD6v6Xtg3T787ngyUVHQxhqFcK4NNtK7HqSCxmXE_noxBJeThT5Y-BNfaX_rzb-GRTql6yh_lH9W-6EM9J7FrbKV0Q4S5YTiKSIWWzNDnlC4CHALrcq5Bxc1D6JbOZQNDNE7exarZkEWJ_JizdPS9NXglI8hBM4SVlyXU_Peif7hp4Nk60oYfW-8jVCUrnDdkC-YzjVQDjZz4bpQt6q2v-YhpVPZS6WIfYRWKXoTVH91t4NaK8YCpduc72LBcbeBmaK2mq_WcXsIsLUZz4q0kfE54KlQLkEg9fPlc7zrLOmxRsal87yhbdIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، به «نیویورک پست» گفت که مناقشه میان ایالات متحده و ایران ممکن است ظرف چند ماه آینده وارد «مرحله‌ای بسیار متفاوت» شود؛ او با ترامپ هم‌نظر بود که این جنگ می‌تواند «بلافاصله پس از» انتخابات میان‌دوره‌ای به پایان برسد.
ونس اظهار داشت که تردد در تنگه هرمز به «بیش از ۵۰ درصد» سطح عادی بازگشته است و استدلال کرد که ایالات متحده دیگر دست به عملیات‌های تهاجمی نمی‌زند، در حالی که ایران همچنان به حملات گاه‌به‌گاه علیه کشتی‌های تجاری ادامه می‌دهد.
ونس گفت: «این ماجرا در واقع دو مرحله دارد و مرحله اول به پایان رسیده است.» او هدف اولیه را نابودی برنامه هسته‌ای، توان نظامی متعارف و قدرت اعمال نفوذ (توانِ قدرت‌نمایی) ایران توصیف کرد.
وی افزود که مرحله دوم، جلوگیری از بازسازی آن توانمندی‌ها توسط ایران و در عین حال حفظ ثبات جهانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71738" target="_blank">📅 19:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLRaf3DvwAGfrP8iNvtL50yAdWqzby5cGnryLSbjCfZgUEZO1bUiHZJEWpfgqQ1RwRW_2Qu3mGUBa79eDvD0S5WDZQq5-jzxAN8O-KC8B4W6_Rwa3ctou9B54zANLs4h59CmI98WHhdR7yhpYSSVfSuVGEXPiqxcLj7SzIBSjl4u8VXdiEWgfgPUKZxHjziRoLG6KmJnzkTOSnKUl-K4B8iU3Yo_vt5kI5CbzgzcMigT0pqSvohJ-6PuFWpeHIvcqJkSR6vbKiQwtwB0VSFk4zSsokEiOCyzrnnV-lJEvTnuY5XAFfPBP3pnXrgLg-HC0w0ZAq6MuCnG7J_ERXanEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlGrrlV9r8x9J5QDP7_IkylPl3n7WUs09DVy5Jr6YpHC6S6OTWM3jakmsD3HAWf-1YgMU8L83utVh2PSLm4ozLPeDVUaOq8b9_5cqNNd76s0-u0yilCRWRccNL5E1kR_2pa5ONNIXCvHPMM6HwEC1hGSLfvRcFZy83BQzB6qNadnY2XJag2-o5Z-NgOnqXJ4uwI7GS_GVyZzDQrBkoF6vPSNe3R6hs8adctX7v6Xzm_kTzeWLTskXnm03hqiATo9QdyMifWoFGRDlSXH2R9mQzFqwELK0RPIvbH0hZs4stM1qhASk405IpADZitaGVCJ35s1eaQrTHscHkCDlq2AxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=G25IXAsKiZUo-66puBeFlEXZpBxhxACGCAJjp6ZnefTqaTDeNjcZ2in9Xp_4C3uNuEfei7ndSljACaT0NZrud3jOziYzV3USegtLZhLOawP7Tja-VgOLqZnCgodzGSzravi9bW7eoA0YIxJZhmnhxsBH_yRyPc3BuHtJYq1NKJx3OpjNANjH-6z-uahX99Kf1EGSRa_dXT0ghVs4GN6RXKWeF3ut0SoOAAXQ1BvV6V2ZQkxzG-kzM8Nm8VU_i8aEQs4vint5QWIjw3d2Pxu2lSC6FB2umv2Lq8ZkhJEyId64g3Il7A5A_KDsA0BwaXc2woPDfar5KpO8EVJoCYgjwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=G25IXAsKiZUo-66puBeFlEXZpBxhxACGCAJjp6ZnefTqaTDeNjcZ2in9Xp_4C3uNuEfei7ndSljACaT0NZrud3jOziYzV3USegtLZhLOawP7Tja-VgOLqZnCgodzGSzravi9bW7eoA0YIxJZhmnhxsBH_yRyPc3BuHtJYq1NKJx3OpjNANjH-6z-uahX99Kf1EGSRa_dXT0ghVs4GN6RXKWeF3ut0SoOAAXQ1BvV6V2ZQkxzG-kzM8Nm8VU_i8aEQs4vint5QWIjw3d2Pxu2lSC6FB2umv2Lq8ZkhJEyId64g3Il7A5A_KDsA0BwaXc2woPDfar5KpO8EVJoCYgjwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C221U2gUK7uig3UnPqDDV0B6N1dj4UaAS2t8JVnJOleMWjIN7UwQGbFXM29ONo_7U3Ym8sWPqmgJb78dregVQ1G9v4Q7UehEWh-9a7qK9FuQGfJhvoJVozTctBPpeNbfLtHntzlG5k8qn3qrcnPzNSdl1Cld4Y642NHAWbV7DyLhYtwhUBecOALJSjp2kaIMVGz3vePL4j-jM7GUHSUZgb-xksFtRRWauPKEUmOEC5I2pg-TRuSld5U4zaBDiSHM9uZ4yjScVduWNYWtthkcr8ZO_4RNnSzg4JeINT7ZMVsPf_ICheIvEMjivJPq1cy02xjD-P6aVQLfz44hKftcoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=WVAj4r9cbLk-rwYog4kvuxTSkCN6qq3x75yxvo51MBou99i60NDvJ8CT3zLbK_usgws51U_-llQOkNj-yKD5dM1S4RlnLI5VbcnNsOrOTZv2oNNFLxUtmIcWwWJL5ckJE6ddIpS2ITFCanybJ3Avn1gKltsbF9RNt57v-2S-5tz0xS37flowVMpSF5h3rZp_eJ0Oq99XITBAt2iPWo4oIi_6AJ2QHJYGppEqMTmhjyamG2APmhFYs1NaBAEbMaa1o1F6XLfouC10mt-2z2Lc-GssYJR5RcKyvsJHV9ZJC9UB-Ds3lk90xjICiRIWIjB9hflZL8fFKTzYBeYQkqQAxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=WVAj4r9cbLk-rwYog4kvuxTSkCN6qq3x75yxvo51MBou99i60NDvJ8CT3zLbK_usgws51U_-llQOkNj-yKD5dM1S4RlnLI5VbcnNsOrOTZv2oNNFLxUtmIcWwWJL5ckJE6ddIpS2ITFCanybJ3Avn1gKltsbF9RNt57v-2S-5tz0xS37flowVMpSF5h3rZp_eJ0Oq99XITBAt2iPWo4oIi_6AJ2QHJYGppEqMTmhjyamG2APmhFYs1NaBAEbMaa1o1F6XLfouC10mt-2z2Lc-GssYJR5RcKyvsJHV9ZJC9UB-Ds3lk90xjICiRIWIjB9hflZL8fFKTzYBeYQkqQAxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQImLxD4RXJm2M4jTjP2PssfFm229obY6viCU9ZIVUrpvX7H4mOSZQhIjAOnmDP6_6JU8IiZ5DNIQYYsFhi6o43vcGTU3tdn4Hhx4bc386jLZ7ef1L3iXv2UJ3Z6KHIzrooyyi87IXg9pRRxhPG2dTeMVXF7sYKjlhsdyDa6zvXXIKsxMPG__wrju9VfjtvJMoeaANLfAGIZ230rIRHlI8PFcZRXn27ybjEQFNFtfPCtfg22_6H2Wntawa-_KZY5LskMLMjolNJTfnHts9GcjNmsY7QhKyfl3RUln48hr-B1YV1dOJx61ZPvHC97CJjMAJCy3h_2iXN4etLQnPJddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=YRvRDXIji9Y9TpmUGr3YRgtVtIS5fn09nQeucW0i5GeiX0aBQm0R8AASsLPqS2Cws3FJCJjoy1fgt0xyIGnaD_NovhmNVnb7UowSuifc8gswAPicoPCu4VQRhZ9-w03CB_0dkajHKtVDoayK4yd0A8BynvY2k4M9VRtAmOyxsnUmI5sP5nIFlxUUqgaFCvg1qx_zXOJZKMD8eATGWO-rwpNpDWaaLzCLUqiQ-0gLSoy-GAevZvGDSWMgM092ueF_rXE0Jz6uQYvzecbEqpYlw_-4Jnz_DkkoI82VXWyt8Y4xAENtn8bhjEcsRMfHYTkunZDZzTPtgbNfGRlOMtwayIdDmXz4lRLebekUhX1wfOXwt-wQRKcVU8XCskXArGgPYggbx6-IT_broHFlIjVXYStq80_hDQcbblDLS_91KQZZRTtr-aSQ8UFxpwJlE8bhhZWECbM1aKCt7fhLpi1uwLOGnxrhaGhZBiMUbvIPyv8dIajzZpzDlLLUzsNwOaABXIxeFNxh-IyrttahW4qJ4aHCAGDayGNCbTzEjnS5QYzVWEcujD53APQkKxcC4SWhCJV958Qdv7oBWsS_pPqYnRkHdkisCoUVNCqjzbqmqJ1V29rW13S8QiCZFmFEixrdPrtsLl3HMC7PC-2lyHFis9poR91R9nXhsvZ25crqvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=YRvRDXIji9Y9TpmUGr3YRgtVtIS5fn09nQeucW0i5GeiX0aBQm0R8AASsLPqS2Cws3FJCJjoy1fgt0xyIGnaD_NovhmNVnb7UowSuifc8gswAPicoPCu4VQRhZ9-w03CB_0dkajHKtVDoayK4yd0A8BynvY2k4M9VRtAmOyxsnUmI5sP5nIFlxUUqgaFCvg1qx_zXOJZKMD8eATGWO-rwpNpDWaaLzCLUqiQ-0gLSoy-GAevZvGDSWMgM092ueF_rXE0Jz6uQYvzecbEqpYlw_-4Jnz_DkkoI82VXWyt8Y4xAENtn8bhjEcsRMfHYTkunZDZzTPtgbNfGRlOMtwayIdDmXz4lRLebekUhX1wfOXwt-wQRKcVU8XCskXArGgPYggbx6-IT_broHFlIjVXYStq80_hDQcbblDLS_91KQZZRTtr-aSQ8UFxpwJlE8bhhZWECbM1aKCt7fhLpi1uwLOGnxrhaGhZBiMUbvIPyv8dIajzZpzDlLLUzsNwOaABXIxeFNxh-IyrttahW4qJ4aHCAGDayGNCbTzEjnS5QYzVWEcujD53APQkKxcC4SWhCJV958Qdv7oBWsS_pPqYnRkHdkisCoUVNCqjzbqmqJ1V29rW13S8QiCZFmFEixrdPrtsLl3HMC7PC-2lyHFis9poR91R9nXhsvZ25crqvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=efX3WyPqNYRCv3f4tGg1VMhgpR3hD10eqL3Df-h0hiRoyu1xnCI2yNHdKH5r6aqha0LqSUHR7ojRSJjjQ8qQPcgYqQDa_gbcL6zNN2c9Yl0g9MY4KvTLUQcKI2fMZeo2qz3lE-E0Ry8aRJlSSDs5DRHU9xXW1Oa5GqC4Qo8QTWVF2XqJjL7ZGeMvsVUy18xPcwwDSZTc5HO_MKjIOOPTbkEUTfQTA4skuGSG3tSbYlWrCCykD6fSV4Zsk6AP1brSgQHa0HSWhfM6DeZafgvMUZ93Q2tu7D0kJe5jhCU-hE__xr966d-NRyVQQP8f8mHQ4BN1IEeR3zHRAAhn_d0Tmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=efX3WyPqNYRCv3f4tGg1VMhgpR3hD10eqL3Df-h0hiRoyu1xnCI2yNHdKH5r6aqha0LqSUHR7ojRSJjjQ8qQPcgYqQDa_gbcL6zNN2c9Yl0g9MY4KvTLUQcKI2fMZeo2qz3lE-E0Ry8aRJlSSDs5DRHU9xXW1Oa5GqC4Qo8QTWVF2XqJjL7ZGeMvsVUy18xPcwwDSZTc5HO_MKjIOOPTbkEUTfQTA4skuGSG3tSbYlWrCCykD6fSV4Zsk6AP1brSgQHa0HSWhfM6DeZafgvMUZ93Q2tu7D0kJe5jhCU-hE__xr966d-NRyVQQP8f8mHQ4BN1IEeR3zHRAAhn_d0Tmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=TxP4mm0JEmOgcV_ZT-HL7M4GKjTWv6cSv_l-aBEXhyFSKuEdSjMDAieJxXQLqTDFcfDGqX-jpCedYt6GVcWq2U5-cThIK-J21mv0-CnfDEG0WOcmZnSopcol4kSLsyhgSXXTPZeQ_O0uje19i1GPEiI3LdjCyQy_z-cilZ7ZFDSjX01m8mFfb3rNR7km2XKyxcyIMaPEFTYYtbbv2-iQ8qvtUGMcptiEIcDJibUiHMCBeXcpKNaALFaOEL4vdGHuGqcJo8t-j8t68BinpZ_w5yj789fWili4ej1hiaSulHj0qiM-CONqp5yn21-j6X4ODSdXZwy9jbjOweA5gvPgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=TxP4mm0JEmOgcV_ZT-HL7M4GKjTWv6cSv_l-aBEXhyFSKuEdSjMDAieJxXQLqTDFcfDGqX-jpCedYt6GVcWq2U5-cThIK-J21mv0-CnfDEG0WOcmZnSopcol4kSLsyhgSXXTPZeQ_O0uje19i1GPEiI3LdjCyQy_z-cilZ7ZFDSjX01m8mFfb3rNR7km2XKyxcyIMaPEFTYYtbbv2-iQ8qvtUGMcptiEIcDJibUiHMCBeXcpKNaALFaOEL4vdGHuGqcJo8t-j8t68BinpZ_w5yj789fWili4ej1hiaSulHj0qiM-CONqp5yn21-j6X4ODSdXZwy9jbjOweA5gvPgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=AE84FEsQ1GmXK_oX9wfxQmTRZ8tYBq791BfEU3whfj3lwvWqkt4D6BPnW7yNfMiMpiuTJb9kUwog9tLUAxKTrJKsLAo2HmjDALE1_YPJGKRI6gJGgG1FRl3MKRx2dvneQP5hA4HwFwQ_E_O2u_VlRqJ5xEaSYyUDfFATg8sclrsLdvE_tEdEAhD8_xob1BVKTvgKYslJEC1TvZ9CLDOpvgZQGmywrjfSZF8ewZXb6R1zNZt5C_6A16sJ-1OL-jIntJTdw5LWLOvxluMM5QGUOjFBdgVTk5plFSXNKfu3kXK2AmRtPEknfUexz1oscq3spE3AMeovmXlzLUaN8dUxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=AE84FEsQ1GmXK_oX9wfxQmTRZ8tYBq791BfEU3whfj3lwvWqkt4D6BPnW7yNfMiMpiuTJb9kUwog9tLUAxKTrJKsLAo2HmjDALE1_YPJGKRI6gJGgG1FRl3MKRx2dvneQP5hA4HwFwQ_E_O2u_VlRqJ5xEaSYyUDfFATg8sclrsLdvE_tEdEAhD8_xob1BVKTvgKYslJEC1TvZ9CLDOpvgZQGmywrjfSZF8ewZXb6R1zNZt5C_6A16sJ-1OL-jIntJTdw5LWLOvxluMM5QGUOjFBdgVTk5plFSXNKfu3kXK2AmRtPEknfUexz1oscq3spE3AMeovmXlzLUaN8dUxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOh27dvlMa9ovtxi218X_IWJXiu-jr3DfzN355A62snadCK_ZJkYyHkCIsPcpJixBM_J1_rNWTjLG-1-zon19lr561HcnhwQ1zJeV-jlaq4qLfGypVGhBk51I9ePZMedxjYNQyAioLHh3ORqcDsKN05TQX2Fy8OWtOJaLtA06IYb2kwILrDnHBdVfVZFe4IFFukGADe7QQVABup9ilSvxz8LOL5ceJk_X5f_bLXQuV2kQ_RJuOwX47geQTXN8dfOv5wJKiHW7Pi-QH7vLJZoUbsB7zGyQu5f0fvJ3JqNJ9AT6sVTeX_Bqw60IPlWBQAQ50Rp_JX8IOtPDaIbgQTN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=vkjD1GUbw5OvFDRGfLBzwwJu90ZiELpF41opshR_GSnYj4gvGSGmsr26ETZunxbWVYY0HhUm7Ta0JcoNsRIHZ8SUMQ9WazheyHfpjF5Ur27JlWTG7LpFyK6taKWqr-AKOpAdf4h6HYmkKFWK3X5p7nwon5B6IWEJXve8FyzGj8BgCoEQvdcyJnReqgGSXoyFn7io-qJP_mLy2jDXB7yTvsXmWd4sXgWUOiHCivs4F9KlBjaLuuigK2Kotl4GI2_8jDEShfmALEJ9Q4Z0SY5lQbK-lZB62IRoqiaPR2Lx-AukqTKZCX4kRIxzdl0Q8xBOGIb40dBgsCYoK_YQ5OFIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=vkjD1GUbw5OvFDRGfLBzwwJu90ZiELpF41opshR_GSnYj4gvGSGmsr26ETZunxbWVYY0HhUm7Ta0JcoNsRIHZ8SUMQ9WazheyHfpjF5Ur27JlWTG7LpFyK6taKWqr-AKOpAdf4h6HYmkKFWK3X5p7nwon5B6IWEJXve8FyzGj8BgCoEQvdcyJnReqgGSXoyFn7io-qJP_mLy2jDXB7yTvsXmWd4sXgWUOiHCivs4F9KlBjaLuuigK2Kotl4GI2_8jDEShfmALEJ9Q4Z0SY5lQbK-lZB62IRoqiaPR2Lx-AukqTKZCX4kRIxzdl0Q8xBOGIb40dBgsCYoK_YQ5OFIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6W9ANa1TiV9Yt7z33s4gTPzXhmYoHr-QbxTOX_pHrW6r8ElOthyCQAwVDvYCMwHQiCte8AYgmykRMoExZB0XWUXVAw6mKlk6dMIsCj6mBHp07E8OUek19JNw40s1iQgCdX2zJvMVA87KF31wMIPQZi_YrwvcY6J3xCfXtDHgyZnSxTaf-Q1ynn8ua2yQ5o0CSjZ1Wxjy0WD7QkvPbozqyAd_5ou0ySP5fbYPGvBg6MDz6cgrmelLlzvD9hJ0yRr7caDf1-JttiVkY5tup7eAwa-sK-tqcVdldmVBp1Jb-5rtPINJkDziC15lVtKZzlWHNsPesZJiP-8hkv7TNFyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmwlvDGo4_LBws1_1UjLOFGDAgWmYErXQR_kNNL7hQkXQiBKZNAd_HWZG-M-YsN31rPN4plixoZJh3b95-lPQTmy3JxkrRSJoo1Zs7b9QYpQhNMSO4u6806vRO4o0iLiEOtBDrb-UcEaJxkD1K_aKklL8nr9ce3zRoJSDKC3AyAyF5OQ0PfUAmJdzV76EKpz9sI8StBAhEl62b9LP0kTLl7zah5uswM7eFeXTzIBUkyu39LueOrXtN77eGj0SfC7K44iEK7SScMW_whTqYkCd041CN5zCzePUbZhYyH8H9TbNjRd3Gc4q3-ZqMKrzMRGDKQUfZXcD-hLlSF3Uqt4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_jQV-sT1WimGMjrLSZSHIgLi51fk11fQqWwRMTLJMG_xW1hWk9Bvvk7Bn-yxQBZhDIRjzZgBMKrB7gYlQ6-zrecYHPWy8_slPGfu59r85MswpcGhy0FVeMbvP8w-lqv7Jx4dugMC5K9xySp6KXEeeWKAEdG2IWnrTwuZ4eFiBY9X_ho9dL9e95Sjwj6ktW3j2MmJ7SxuyE75_OOZpncXM0pen_MMgUptpxLWExaFZWFvJCIczYaqRCTZETcyYGM0lFi3CjtCJLH_sn41Re1e5WQjMZGwQOlvE3iMa_1Qd1uh5tCNvHuaxqiAY2YHwErD_m5ETAh8lso23Y1wrCBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDd-1X7t-pF136jH0TplcBfjRuq3zmQDWjPgsYKcVOBLGxhCFCmI9SujJVI_CoHIABw1C8-0Oyp_2GhZYNz2CctyFIpYxe36l7J3_B-TJTSKDy8JjXENkE6rY0A3WYdx-Zl9FsOP1Bg235e-ALLVw4F3BO8wTFy2y_yf9o6FkRcLCcAFX9zM5s3ttClBv7ZkWKduVq7hPQawFSyurAooop-VvNcYe0VxtnhhbiFHblBSvjkr3XO0oJHBFu3fy_qkXeG1KieO9X-LbUwK9Zf3SEP8FUqavB-Nr49-4EGxl9kPI6Ii-BUmD5-hUkamnO2HuZ_e4ehVB-5Om293WSu8YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWo7I6rJVspUsQLF3Wg-jXrnl2eBhT6vBCDKCrzqeJG0aPXbs0RGweRHWvqe2knn243oONdtn5RxkfDLsroMoavUHwFJ1Tt4UicrOQ9RK_huKPZSRc7kyTXpsouxRLDVkO-CRVeKK8pYYpvlOVqCOe1c-R2izqYL0hZ9K5LrrmIIeHyG_qFGRP8-pz14H6oI2LxojD0YXSqxDLo0E75LzuDV92auN6yApHRNxykAso4xmn1n6FHf2-SKuNc1rmqCg33YHHNUdJ8DRJgtSqaAUbO4m0SICwFsAlgirWt9X7Xb8Rhcvnn1v4sNmWnLzJbW4s5q79quPzMuMhl71jubww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=YnxiQAaJ5TuSXP7p_KWFnUdHr4NkZm3sl_S_clYUgiW6hVB8jlJGf5SF2PwwXl1SqOnOrqKQGvWQapZRH4Tz1bkzlgv6sMC_xYJDYyuJUrTG468bunS565Z10umwNe4qAVOFsP7m4KEcTFmIqN0x_FQpSlXCfoXUQ3K1VAY9EuuXU8Lw42Cf0vUrq-HePv39RuHECmdpT5qTqSIMidlBCcc0tEb7O5BABjUTMTMiJx9J2acezo_WK2YOm2HSdP6OaPsg0DetNEkuUCqw-4c94jpfiD8xcxnUiL6z-DCK10X-27TmHBgJDlvoY-9oWS5p7Ok4bCjmrmb9ni4oS8OvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=YnxiQAaJ5TuSXP7p_KWFnUdHr4NkZm3sl_S_clYUgiW6hVB8jlJGf5SF2PwwXl1SqOnOrqKQGvWQapZRH4Tz1bkzlgv6sMC_xYJDYyuJUrTG468bunS565Z10umwNe4qAVOFsP7m4KEcTFmIqN0x_FQpSlXCfoXUQ3K1VAY9EuuXU8Lw42Cf0vUrq-HePv39RuHECmdpT5qTqSIMidlBCcc0tEb7O5BABjUTMTMiJx9J2acezo_WK2YOm2HSdP6OaPsg0DetNEkuUCqw-4c94jpfiD8xcxnUiL6z-DCK10X-27TmHBgJDlvoY-9oWS5p7Ok4bCjmrmb9ni4oS8OvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLMpMBiUCaTr47Zhhb5MjQiC38GcVP1SQy8KYcVWcMEdC3CiEQpdXJwee0t6DHN31Jt5F4fOlEZb-yPNkE4v49z4OUJ2uZ7EjIdZ23lQSwJkMxFDRbckwcLMqXMBE290eW5xMTP54uZqgoL9APoT8XLNcBEMg5eUu4U-4liEw0_7v0A3H27syL1u2WbE2bP3KeqbF4rz_uTmeEhziphqpamdS22VitkA_CHD-4rEimrvemH6LvzQgqwiXtlNnKQcdCVLvaNdmCxTKHdSWcaTtFmi62LInZtEthatO1_UtFgQ-C5Vmx1fUVwbKhk8VfwlcZDJaK8Dv3Fan5PC_dOKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
