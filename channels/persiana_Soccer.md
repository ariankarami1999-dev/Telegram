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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ_ynT7dHsY1H_jPrZHJmTGp40vv7kJxXS94y2Rv3bA0N2hDGjvudy-TT3oPgbZf1HAKvXAsf_o0VzgwnJmcR9mpow1F-Os9DTxBGtJy-w69wMyXU2zhdbtMiUK05XULeweG0nUOKgh72mDZ9B4ZynTa4E9c9iEuZmwN2jwHIqeuJEPK-bQoUsQbosgcjWzAB20Oz9_B2y0TY0515idxU5A3n6w03q0mTrAWLOCT0KNstgZ4WgeA2LKly_P6BoHOjgGgJG5yFOFh45OBwxqRAFQxXIHkNPTX_dX2-R5oSXRUZu5bg5iyNPDXCx3gqTfz2-73Xse3rfb9uUcsWY6-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECd2-Pof3kcXpG-i23OY2bvcjPl3FbAQj0_5QxHpCep4qDI-Z_Kx-u8i9M3FA2ro33s5_oGNE53P60ORzjbz7Kio_wExNQjevN_ntnQssSMmfo-MIpNGCaYtegdiewnfj2ij0mBqgc2QCZ1molzjPgfMHnC3yFVJ1Pdd3wI3nXBCVYbsZ-RFdKJvh_wJQ5et1BE3t10MLQzNP6xHtFjGp274BQkpFX_BQVw6v4-5rJJoiK1mgdamm2qJ0ZlK46b6ZW9Efp6D0MxgeM6E9gniGlgy-WO7YRFGqzI63V6S7CavU4yufo0R5v2wlmXWJVisdm4mCjLONiCOklrsHtXojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwJtQXhRUnaxSviHcTJX03SkE_yNj5BZso64tzdBD2NVYRlTJ7XovnQ_BIahzVGET2GPPhXc_FiY1SVBHhoW_qfqZcqxxWFHnuFTp8kL8Fv_gXrpFIFb1U2DUhOvt0JKHLUITEqd3xBiAa65JqNPlaeNTmyeSZDejwHuiRHlMOisIkKc7g6CMhnLQ6nEJZqDGd2nyRA0_aq0RDheq2sZEgHXLAgtnVNVMtU7VPMyBA8CctWX8D10Qht2H8cjZj3d3Z2J8zDc0_Ta2YA_QhYB7t6viYE4TfQks8LkUdXkHzdm9a4upKLLSY_9oDtAtDIKiez1QybxdoAvQ6CCoR06SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twp7h1DuVPA6pLVwCcMJjOrm1MExBxmKWcwMFDh-vJS4v3bw7X0RAU-qPXQR2nS7OYHD3k6G3nENhGD-lgJ-xSryw0GtXeDt5dFuBQPYEQmVO905Qm144yDfB3uPR23Pecd1AHGgaXJS2yRcuEKLAP06I3jIxv376y4OOUZwXCiKNT1D3YiMoJYPw2gyGVMKguBpYGvnZQh-MqVY14iUQyq_LBS2IS_Z7s33OPE-m0zQsRdfiiOEBrYvNUhTHbBxRYXLqbvZ7Ky6n9BbrOm04YqwIETbM9K-b0ClbcLAforuFLhJSAFQlbdBI45YKs0b2JLFbL-LLNv_D-fH_qZNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3lpBbPg5Eabq7dm82zdkMHcsf9I1hijuCJCHVtCNu48oIZcKlc95jokyaybFV1wRFW50osw2bjLwV0DZA6sx9gDSHUTPQYTVbyafqbjF0qst5Nn-39N32k8B9VfNvzxJlkpRenRdSLWmd0cpuXm24fHCoXwfFghQj-b3bsWC1uN_20HT2KO026l9cpPTSWKRIGXmfyJMnA5mq3bLK5emWL9Fr0C9G4Z_t7nV0XSPZgmk8KBE6zW3J4PjmWg4wHIIyadSnZjs4_Swl8vk3braVMeCHiHgtS7SpXztVkt8Bqwv5fF6tp-FlS84vVWUQg8LOJDhDniujw9MdbnOy1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HavWvbD-7j9z9nBFSi3S1GUfKLXcTp2jRECb2gGfE7ZaS_v4I9lXp1bOsS73b23X2QkU29GQeN5otSSo1tpLnQWZ-2j5vGzMjQpMjYragn2ovRryt6fA9V__twAv-psD2TryLnEFwFp7NBV0AIQ-eqJr2jSEnLc1ToiGHrS89lSDaoCdBXEjaPl8zbJlUUOEVM9P3EmX_CNrSyn7xQJD3dAsP6RDbxTxlZVzpn4giE7gARYNJPe9LtqarZr8okUZ4gUW-vILGqD_emudcUpYsABgswDhe7mB-o6TzqBX60QcccS0rtJBo0RTbRPqlfWLAJJyr4Hf2fDcuK0mTWulYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrGefmGesUiEcK49O9w7IJBkqFLp3qX_4lxmqh_7sfpHUsP8SEh773lcDLgCT_9uh3TTSt3IuAZ2tp-WpR0EXduqP0t-elk6EfGRC-uHX4j0BJuUq2YsPZPBPxyADVzVyfKIrAPxztCFIOwlOVYTL4l65L2FWfNufa9VXXZSj9UsD7lFUZ3UQfaErqZD4FmHKsr5Tu5Tc5EMmPkPstEXuu5YfH_vrfavGuJjc4B0NyM483N8E95IXKhrUrvH0xXL3D2KWYz6_tng8XfL4u0XMCnp2rm2h6K9c53qqZDKfCAmKiHM9mnmvH565bIJ8Vlh53JxzJbNeOY7WgeuBXzy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXQw1D0zfdhMqPoFIhM9L8bCxtQyYVioWs5YzbjQRNbsYUGxLiYSJn166HRMXc8KlKJtm-kwHlviPIFH8pNbVtjAH1HO_nRRVFKZzBiHEOAD74N2vSbxYAxO-U28LCLVN1TSjGSGoOWqSIZRqn1JKUe-BOKPoSujsmi9Knw3xr52kBkLkOK9N5GqB06RVLXc8pbgM0V3Fu9_d2aoa2177tjzdbU_O3v_CNiQ17KlN6faT3__o7qwshiezpmbLxoOWz5bAPGOs8OCXUOHXsUWIe5DfdktS0MLSeU759yIZKcKu6XsbRgIlZbcRLM6o-SuQfxNEY-5Hq2b4wyXIDgyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgDGydNJCcvO4ErEBejToy4PiqyKecJXxdjbSDb2hpP2NmOO0fmbfKbaluBFKxFDcw27o-341mvyWsdKaFcC_qGRBGuB3Fakpy8oTiku3Nh6XA2w_CBuU0CdT1gUqqBCZmZMeTofckcgUEm4Zehizaq1IPEAAcBVJTx1mui0UIeRfdEuVHEXShkGF12bY5TfJt3XpgAiQSqokno3Hy5A-818BHWBwTju8wMPhPjnsCJT0jIy68CAufsqKvi4qGDheEt4IrAq8rRq4yUiagxTO1OCOfutG56dqZ4_5aayMVIsNlqFNm0ybxlOztpqKocou7xqnth7Q6qK0wqih-QAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAj-l2Bt2FkSorCP7NLtlgscKiK8riFh20ItJQ4GMyTbmpvNPG_av77G52qcPPSBr5da-HLG-T1wrw0dKczP95Kyk-0UM8GFq3c1GXq5bW3S-1K8koloij-3eYCOjAnF71sn3rJYA-QTN1OsVpLQjVafdE0HyV5X8eJs3Z4ImBkw9gsgmD7hcFKjqLWJKsQnfSmUp-w-_8JJ5_EeThm5J9APdIGHQcZjw2Zv2bL0bcWeM9Geda0Yeq12yQa5OOVaOJCBRXNNHI-XuK4fBp1s7nAE7-pLlkawvUpTEC920UkA2YwOWk_DG0Tdr7214h4NsrBjOKpUnTmbKtrEGU1u6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Btb80ne3590zhoMtVqwpiELq_oeSdFhrMCBiPINbAHut_KA8WAcL6trl6ZZ7ai33aVr0DwUw9NGAEzZ1v0LLeInzIw_u1DIAGWXS5CM0fqEO7X5UAjveVD4-Qpu0Uo7VfkuBDdEp3RmtWMDfmGVTVQMMzrT7tVTJptLjh9uG-z-efwLQ8aW4MEnYvfuTse5fH080jmcD3WBe2eSSVH_WmpXlrU4sSyEzhBTwzlkBpio3MbEs2uZYh5n2kIVNwxg_ceogb8YBJ8myR5gY0OiuRwL4hFPe73GmUu_h0gEeRMDa9iLu5DpsX4HwW62tXz4IpJQfayIiCAE9nx93ZvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCdkOmd_Q3Z5bKvsEUmANVAvzHQ3SbTKRZd1zAm5f9jcCyVgSW76Ohn8o1mWnPLvT98fOh_687u2pAp8-Wwz5vPZt2x633dWIvVTDf6llv-xjQsV9cmaSZmg0M6SUJsxvRfAkRChRVdc0GT7Pe071uvTGJLlozlv39H_22uDNRIXul4RyG3Kk2OeYt05umIxdbWT6_9uXVa9ewAD3ufAcqE_fSho99K9zLhOafePZWFGrp4ybTohnSS398ayTLV_vwJlLY5-mUYbT2hgq2MS_G-CbEZ2qOANSOzCePE1CG16TmNNW6WzRtoltQOg_05A5mWKk4Ag7k1Q7-uMZPE9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25284" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC00z27goK4g5gf7FI7reJlntqrY-rxGq4Mh0QzkZvDW2wKalxwFh82DpdPpG5PQY4EjR9iu1d8PTTWiCuxowG1d62iHJ2PK4mEGdQbLujhcbc-pjvdwRHGbK2wHLmzXAKWaGpwhssiEgzZWrXMAnIr1ruCNAg1URejjz62EanAramLFkON9JQwNeSAeO6_YllKqxEoPzFj3ccCxSjRZNCxV69GH9VLFjUYM9ALzsJjsXVxb_KDK7ED3VDq7Jfe7CWBpYhT5iwHriTLfF8qYBtYqjWQWiZdac0Bw-mTm8DmcBdC7548UoGLfmq85R5mDYnHrF-psMAxuAOF9oUk5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT1YkV4P330oq4-9mvtHyevIii-tObMBEn9hPoTC8ApXfgNzZkvRZDlopHZsLDIkbWtcdnOX79OzkfsTuPHZyxezHu-H3Z5H6VBCBFzb1uZZpcKTATjnMy-EmeKBhc6L_FmZxb7twwH9yaYN3yNchVhFr9pDFPUUs3_wJEuY1-I7K-rhovv-8DvDmF_MaIqh2hJ43xUgME-rVj8e7Z5oAA7wErhnAXsEbOC5t4jvgCR5qhUmpGmmik51GQG7YILDDYaO5Jn0EsRoOerJnCidxf2UQjB2D5jeQkTLhHCdg_LsV3nV_MKTDqRClJh2OLXob0z_k8gUkM4AbBVVP8puvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUNpWBKwecjFe1m4_AyHp7umMEz2eaA2RFRmPxZ3bShTh2IASqrHvYZ2zRchlM6z8AyQ6JUT2fiHz3QcKmrIfxYfBYaEsBgpHKA_fIcOx764Sx66u6i0zLhNaGHZXKoUMEzg0UOuPYGZctM7HMsPoOZzW6rAn0nybWTaJbs-0sc_L3j1t0qFNvCjni_4OdedatyzcG7D3fPP494iT5azie8zAB6ML2od-vR5WHhG_ghMx0VUib9SG6sBEWJexKOvIkoK-jkFPW86hVM_ExrT8rLGauqXBFd62uP2D1ompA6srzNyUP7HffLmya5VOHvIJ-mnIEGFAqTtfaibWGGCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7QHzCOVmH2YzFvNggK-Piyi8ZPfuqfKYErPxnbjSsKVwF0_LdFI3wYLI4NosCS7PVfSN7ar56yiRIV9IATPmPK0aI2__EVHB_ONep5BP8duiwZui3dNZTXytvUDwjjFOLRvQbE4gqwTSjqrJRu9EhaPRvpGxI9jNaVlH2MPPZjptZ4XI8tqlkMfAMLREqLshUaoHCqwPKi_YAPoNAPZ0mWT0R0-RyvbXIbkCwI8DQrVEd3ag6VHTs_VT5puOvCQ5XaUZJBTFcS-kXajBYOxbg0eFrpa448astT6fsAcXTDR0GXP5r4OkAxaKxYW9abCGm4LXgpX5sisx71yKf53bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_liKjs4iGyhWa_apgo91ofu6HR2Ru8MCz8DnT7NCGm0A6n4ZZS7AVx1FMY-Qr2KK0peciwXIuj7W1evKBpURbFUTeHR7ipM-h6faSfnCqYNdn--v0X1OlayaLHI8COsLmg9ehCFEcXxdaMlFHn9Ubx5ny33HWO6bnbR4OsxSjNO9QIJXAsqVcFADgRjJUe2vMee1jPQvUCDI0qLWCbEdEqogum3YAn8SBL53P7dz-ak6cPxOY7IGobnV99iVlnmUn2KSvJJEthbr0NjG7jHdojQuGPux1-HXDCWEADZbSRLyovq8ffMtuHKuG47lm_2m9WG8Z3JyPO-qkGZFey5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKeIrhBE9PB2YgYGlUqi49hcl1YeJcfpaduU6Xl87Hu4rX4Ho2b6cWpRgUfGJIY0jSr2OH0kdvcBwS77jm3mDaSF5jYm_t6gHBjD0XO1rjSW2DT3iydUhfyXF5ZLC_WxsTPFlFnawfB5DFb1PUSF5POMFgZqjUcXTQKxiU7sEeWNmxFtrwrvO_DiIubu7ujudcBTLnJQrtkzZrPWbCn3ypu7M5R_YRK3EAsNT3Rd6NSRKVwE4ccSL5_urNtCskMYOAvYwgfR23NMh9th5UWCTfd3I29i7SHSixl2-Edjlxh7aQ6KqU9tD6lB6JgGZWLOPGSGSEvl1Wkf2DVk9hz44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAUM7kt-oHcC3bzVi3dRFiD5gZ2_eg2Duf0hjd_NMpaFJ-K59CzvAbj7iNlg8T7SIbGKkKwEMqcQJkNsuv6UjLUopdGBxGEcEjCr5L80lKzWlWp9jCSRQ7gDx5MZXFPC5R92fpN16Uk6xPS8bo0TURKvKwT6rJequeqd2i7mZPAb7NFDzZxQSjKkzehvFM2vSWoHf9qQd30oJmdVjF_lv46pmo2OJ_D8JFrcThXXLGhYf38WKMlXsYohrl90i5PRWeRjxeb6rBEsivDO-IjTA8EoRe9Yt7wxSLhO2GcubiEIos2Vuj-q5uhvpWf3aQysXMAadxfvbl6FoZ3l6NFkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLA0WXYacawZWx3_u4HVWty577zpM2nH0JI1PYVmyGQqUvEp1q01uG58hk1ZbELZeOu9k65wQWfMzumJCziZA4ySjt6IcbKkOX2HkrF3jBPNSwBL7d2RkREWAe-miI8qBFzB_EpkvmR_IuqmCJP899WGGEqcH6kwVr047R3CHt2wMn0FrMKT5jUcPsJVs4eAPTLyt4Y86CBr0NZoVfxbJ85lZUh6lJQvUkthwDoCJO9pRBoAtPiBX3XYOe8dqUff3iEZd5LiHoX4Xr8yjw86U89kJw5-nQ47cmEahzQ5wEt4QywttGBhnYPQY1RjG3eKmo-TjVgUQ5xzt_o6CDZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JosCXh85VHRAbDbcDk3trNKCJqfhPLRdbzFIu3hQ_vtvTgWHJicx5F-AX9JLs09T7lMfL_1f2BNRTU57A74IZ2ObgHel7f8HBT2UdoKQPLT-ZG8PBWiKpPr9r4dfjzF2fhu9787rRd05pYkNHuNjMytulfndcHY1NdJ27vgzp-xxNol3Yf3Ms5Zr88oj5cBTg1ksb15L7Wig6QBD2QDznE5DcTc3R1tzEYH4_90VucOiG0VidRLBCMr_YoLL9k9p4xYdilNi1GOmymufb9Jra2ugB4tBSKNraF1BVTQw15yU4sqJbUVl_wHvLFqXs7LFge_U7QhiYerpbL6Y3PY8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGSojSNHXigIM8WCCyt2nR8U6TOX3bq22Zp5Y9JYwD2Q-TQfIGGckVJ4UlpeGsvsmrNPhJJgoR7rU76MhXFViQiC1KP0geYwgdjlXMd-EWMBD7SdVcRxnkosqFu3J4aVM1EbF_UBoYVBJhmwlJjvoq5jnGCFbuqw108mwdWbKYWzO--qDjTCXob0gfJJ_KRMg9lFWahiHPrBK2wiF3CxC-whueRyRKfadatsjzYhpTY2bIXwQKAzzLWWP_zxvhTKpX3r5GlM_EmBCg6alfOLTAHVGQa9Osc3D9qM3-7_3yC5YmXNXCLUCbc2xR3c8l8I7wnLOogmoPtc3ZoA2eWxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZRC9aevzFKeTh4BpUZLkE6WHX4UqsrJ4C2ytUphunW2rx60tzxwaabZv_pvO1-F15KMosIkPUogRbtSCxfYIyTwOStA6ZVmLUUEa8kgSVF9j6JlEnrk-ZH0eu7mxscFI5Z7IZaZYdW3mkC4foilwKrHIxGXulTU6DCx-faa-cUN2ukParKe3BLa_kRvIMCqHt6byNKaHPENADiBm-JMxnjW7gYgNlN_sgPzlddjCDakQ7LPUqqSaDuhQw8DELtkchwmcFiOqsnYvofUzBoNpN7cLGDMud5KAAWj6lNJ-eCrNl9tXJ2Bo5m_JjLbZog5FVNwPYySm12JP21rGZLvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6i2n8PFV17vV5Zfpw33wIvuceDMylH88PsTcg1g0fcCu9Z9unttg3uy6tw9cCBrx2tSbxheSjYmAw5qAtwCOOwBTeng-QwJFGyaQqFmNBTeUSx51bVNf6Bm1ajuq-lasL9PcKdEoaNtzgj1YlapXAIKhm4DllA0QcFaUrpzM6qBDeS8aHExrSUMn-xUB10yHGcimMPTjQvsuaOMfB24o2grLV0-Px5JVuzCyqJCW3xy2kU71NT7W8TzDY6fDgOReiUs9ubYe9YSCosO-ov1ldE01gAcpTN74BGfIr4hQDdQxaEmcyEA2Qhovr0WQFjedVxuIluVTnIjPal_EmaAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGrO7o4TkGcYSN36AsZ1XqVJkykTBdZf8Ul_4MJF4BAWwemSsh3aSZlsN6ESXc4DyR-ZtSjRBPCvVW-XDUSC4ojgB4YaO04OmImMku5_CYqk5o4le7S-SPkyljQmSqyz_J4fcPC_NzVsl_fveWEFBNI59rzirak3ngvmTGesjqPdFz2CUNt4ZIbknQd4qX937WvJt9-ejyK7kJI3ehfB6tqQ7UJv2bh1u5oOjSJEFMxLjQQvn8eLWhDpEERNe3SWVTkpZ0KxpWCX0_xCj4kej3_G7SegykS8o9P9woEqWusf-BlY4HteZwdsnSnj1wrcNOICSiW23d0EPaZf2Ckepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLLPefh0n0EsOmzciyC7is5ZG_HT0HGjnOxx26u665mnfiFffwQLGwzA3Nha40_zKCPYGqDx1JB_XMxY2cec84Qe4veG-pu7srzVJSPyOY-KWfIn2r0D2qhiapKBV5r6qm8uR4JDwYSApbKamXs1Tp1v7MyTOmOX0smkwD22T-vLoc-kJ9MPIEnfqSYF8dO1djRwfRr_4bYaW52G3cnO81oQGG6QjbtUGRX2ujiiIyecYbxY9nDRzxNzrpbjMq4kymqfylk4UzEMxkbo2hEMgGxhPOqg2ZJzyl2O3f6N91guWO5AheSF8tvWOS9kC-XjUUZ2TcoMdusIiNWoj49kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfLxTQg4XuZbECFNbt2For0mwYpDzWxjaz9GwVye2ayxM7GWtMr3EcI1TPtcYr453jPxg4itN43gzaQV2thtwfk7BoJ9S6JPJTv04zLpzV1omrGRXFXokO1ihivfs3VrCm1QkNwzwADMjWaG0llOFzcWlfdpC2QB6gGoBQAiW_EdyONF4N2iB7cLj9J1Prm6Arkj9Hk4HgD8oVO-1z7zgTprA46kn2X0SZ4UZg9BNpp8WLh-0aB-R5hyxQ3Z8pFnyWD8RZQ3qCCnkWLDbgXWWHwzq24jh4f4XUvU45E82kQpiKZrK6NXBQPSD6mIm0sqZUwQk-QbTCJKzfeBHo0M-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=PuMoZ7f6B8IwNdJscvwDa8DFbRbSGkcvR22_DZX0FGlDWxDzXBuw23k2JnVOduKhNVtvWQt2r9VEWtJAHb9YJEbFlNu8Dy1sGWTVqcRKl_Qbc7ZQkikUNVcwc9nXTy1M163qJ1mRDcb1z7DXLha5Rircp1fJ2EUMyAY_GSvEUSgVit3N1nWq1Vv6G1hccf7-MXW1sBo_Yy9cjCyAM1775aeoW7Kh98o_kbl7NWvJcwZ1Z0odCn_6rmD-I2loZjMR9MmSZ-x0ffBCvILRjAtC5a0J9zwf4vmxlJgOkAR3SwLx50PWZxz0_uLlA1v_VOtjYmrXN77bsejFCp_oySJRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=PuMoZ7f6B8IwNdJscvwDa8DFbRbSGkcvR22_DZX0FGlDWxDzXBuw23k2JnVOduKhNVtvWQt2r9VEWtJAHb9YJEbFlNu8Dy1sGWTVqcRKl_Qbc7ZQkikUNVcwc9nXTy1M163qJ1mRDcb1z7DXLha5Rircp1fJ2EUMyAY_GSvEUSgVit3N1nWq1Vv6G1hccf7-MXW1sBo_Yy9cjCyAM1775aeoW7Kh98o_kbl7NWvJcwZ1Z0odCn_6rmD-I2loZjMR9MmSZ-x0ffBCvILRjAtC5a0J9zwf4vmxlJgOkAR3SwLx50PWZxz0_uLlA1v_VOtjYmrXN77bsejFCp_oySJRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzEerOt9U70GnuCkiGer2_UBMGJRO3ENw5MngWAVyvithTyXu8I6uR4CvmY-nBj5fp-EW1QNxIG-RKxlSnMrHptBGNAA-caoWa0ytLU4zGmh7sUAau9H7RgE7l8xcYSmOy7BXBIKRFZxla65Nz1ffiGcK6YW9bL_crctzBmD3qWh5yy7ej-fjRmC241FPqWtVLQX6oZFivmqpSFY9tMQoP6VEcHgRWftHWCSUETA1VUw2mDdGlr6PpKDcCF_McuHtOA2UROtDihsyjZm4uv678SpDPOeJVnZUvtGRPutPT-_wWP2-HGwbqldvTHiMYZZbXKJ9gOH4c0bsj6rLZFa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_Oo_Cgh61LSrrlqld-1n1R02GdHBAc7NtvtGqnEm6fFU7-2KLIDLcJVGmVgshkhGVf3W4XqMBOU98xWITw8hjQCKL_w3oBMpaWGq8jWp0ObTSNlxm70QvHDQqYu324NGGQbauyKfBDfFWZeU9kizfZQWA0FCUm8ZmkLaLftL9-3BYWQGlM8SVY_h1SpN5YF0wLj9t7MXUAF7UOndYkNe57LOECoC0T8tXXP1J1jdN1D9HwlW3MPfohMC9zvkX625zf7-2e5u1eg5jcbc65gbHbNCyNIGFatkarHnQ9Hum5zHv6O5k0GUp_Dc9VOCrb_6hU4gQo385wgOPvFS29CEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5jlQA1ww68yvzPaXYPvwHglum5_O8ZsHb6t_Ui-vILw9fzoUsdW1aBPfYSigF6X9dQYsRLs9cYSJND6WLKDkXhBRM-5V9xY0zLXnT80cq9Pf7HOk97XYgr9LnpHopjFGzbzncP-RGpYnzVXSF1OZrOdAo4HHTV3hpNqmD6gepG7Fe7M71RLXqa1HiCMoMXnf0SEWLMhezH2GquJMMl_tIdf3kgmQrHDt5mbEEh0LuJzpL44ACqmzeEi5ftZCOiWPjnkBmI-CEMtjDZhQDeZIOadKlMLd-tHZnLnAggSssJOD6x40ACoFaK9ykeehGALX79ZyRD6L1RMyHaL2w7StQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=mlMivXgZN5njWYEwjKkHjFVkp155NKHznpmw9SlwpQ0DvdCMmqc5SUYFXiy61c5cAiF1xVc8vyETiEZSKd8NwTFYD72m_LVxWuSPYWCbrdY_8PmrIJDDVzf9M4fGhqXk2O-23O4_4V0vaVRvJd6uLjK5fvz97kFbfrsvLpq3BKH0iZUaymiB7mbrBj8gjQnwExMIsxusQs_2n3bfaPfuZPl9gjON3ie8-r3YNGndLFX__KjUzqiYSoXWRCI5UgSZc9OnxzwJlGH0DijKenqrkWUlgROlh0dVnxRNCa7mdvuQ4D6hc5zyP7vGz6rLJeMw6f3bPLLySHrF0Rb0-6-AzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=mlMivXgZN5njWYEwjKkHjFVkp155NKHznpmw9SlwpQ0DvdCMmqc5SUYFXiy61c5cAiF1xVc8vyETiEZSKd8NwTFYD72m_LVxWuSPYWCbrdY_8PmrIJDDVzf9M4fGhqXk2O-23O4_4V0vaVRvJd6uLjK5fvz97kFbfrsvLpq3BKH0iZUaymiB7mbrBj8gjQnwExMIsxusQs_2n3bfaPfuZPl9gjON3ie8-r3YNGndLFX__KjUzqiYSoXWRCI5UgSZc9OnxzwJlGH0DijKenqrkWUlgROlh0dVnxRNCa7mdvuQ4D6hc5zyP7vGz6rLJeMw6f3bPLLySHrF0Rb0-6-AzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYuVMG2xAwWoSXLZP5cfY4Mzp3eU1VFKVW-So7M32VC474uV6qvFB3b-8iurpjq2BCKgKUG9hlGAJwyZNgF33QmJdCeTxfDbjUkh6s9gmFw_kxI3hVztJ-_ESeR3LXdHqH8ggcLej7sFoWhP_qt4cSs8b4_u11f37Lz7WFeAU7YuV_YGs4rng_yShQtCWHESVe4b6vFTXq-hihRrQT9mW2lalaJOz7ZPyKNgwqnjqoXnNKV9v-UBLLZbuKB6mAX5OnDfFHVsF1jBegcTK-S06FvmtQeUrVJxs0FY1hsko-pqwnpR5Y4a714TQuZgSxTpYiIa3qDLMke3Qd_-kafYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP2KqC7v3XNqiua4Jt-FPCYPrNP8zQqNyJfkePDQZLcwD_Ae6Qftto8mfCdkxjRCWWph1t68dBvMTVlFo9wAqbWE1yL0dAh_Cl9exGYearKi6XnpIs1u8dAH2kGUG1CkjYz2FBeN6ygJgvRyHnNFZ7JbrsL14JjtAVgh6da0I6DeNBsxI_wE5gZcrLeoYohPda1r6hFQTxcsOzEaU2Dm8rG9atcxdDAYL3mAsdxatls3d4dKuVkpVh_J-OGdq_eIoIi4yh6zH7FFhusSBO9qCKWKpk9tBj82FrV7GO1E_YC6v-qTbQFdMFU-GvZsWF8to2-oZFk4RDVYM1E9cl7zPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dlr9cCHWK_KWpaAqf2_8a-ZiMDyvyftTsfKOiD2BtmtCNfp0LlKYyedn76OGcUznd3XQ-6cGlbqkXCsNdtgJUuZaVjXkPJRaB92n-QDIjMu1W5Gd4-obwMr8UcwLlwzdG11QjpxGJVVJ18jMSgBWGymVOS0PHmiV6pRHC_UWEiYUqjGWALCI8yw1AZQA9DecZTA2l4L2YJAUyYvIRPmiMK20nCjQ7GpLUA8c1gQ1upONZVV2Mj6hXDYC4hXJNcMfWQTp9AQZrcBCuFwoX5fUleGtSzArStvSzdvrVPSJXWbnvcwXBVKn4X3jE4AQ46rEMb0CJSMCb53xGIGS-hQX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTcUq16Tkpi5VVB8G7Bd1jO4i_Hral_vcKM73s7xYuIRQriJWOLL8iBe9O7MacqmSJQRr97Tf_yi4ExPsVyaW5cvCW_RAK6cyZZgtM20o1KWyAK1h12a_Eo3ElZ9w4kOlNo2ErIKHV0JgYxXDCZ0FU4SmD1WR2yJXqs2k_YGABKmfbNlvIyj4N74WRdp8c9w7HTvb9pdZkmJiutNSLHZZfzrpxX0GKWjOtaJLA5_uR4dWVGSxlOzhy9ZVfyxwgbt72Zajs2-IICL4ACYKvLo_ZnjlUW5ZoyEZcKPwwUrnOrfCdzGBdUeKvu86hDRukYAztJ1UrpGCb8P2K3qc-ITqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4oo-0f00eHk8mtRf5egdFubq0ngHdhV6_128Sf_0NOxSqUiZmT58TU8c3tKkg8iJR2dZvO2zLYnPcwRVmLJC_FyHQOcZqkKC4iZYn7hR0L9GXE6G8gSUJuGluK-C7MrgKtvFvyLA3X2EVocy1JbRSF5Gnaq5xt8kmDj--XjrUe4DC4Zg2Af1lcuUmFfAcX0P_IO68S4WB7ZuzGaA6ru7lLwPz5DKvZsz6_qYfLm80rKjcUDknTLjz5rbdFaC8C5850VyvKEdzT9iC3pn9XbIKM45FBLcRVLyY-RGjW7_rNRJF7R0jqe3YlgLv0Cth9mcZt1Nce1xKN2MUx4MgwdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrjVk5MVy2AxQ7oTbiRe430lnyI-GLKHVHcSWkdoiRK7Yek7fPYovT3P5HMeqE0SIyhk3Iv1HYKOC_L-97EywrFsPmoFyivVqwciq2hJ_RPJnKAqh4OHnpYh4Llx6thYJRRyYjuQ-4cx7t_2KC-063dz8tIfjKcQHjpN6Uvryv8uGvpibY99DN8062098wyxI9l9HvPJZ_vgeHXgD75b6qGpibdcpWjf_W5KRZYf5c1x5Qut7LKKS1w9GQasv74gTPDbrUnHtZY39rQMkjvc7rAO9J6qvKeJxYgBmShc7lYE1ZXKVXDFEfaar1RaIpDOeBqgFJgHfq7LMwhU6YQ4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlfhVw0CmuBK85kKgGOVyZkyvOiswousRnprj4snkMZInGQReOtFEdTo5k8eqwjiD2p7cG2v4L8Enen2ru9plC-3GxkV5ehwk34dqkuA1iWIa83Qnaauecii9vI8MQ5V94_hcHpol7hdIOWMTgW9VOKvbv4PqSwv64qeJ3kfmEBZZH3NVvf2VStawhtoq4SZa3H2WxxIrgpESHZ8HF0UlmjjgVrnW91mhmpX_bTGCsjWUIrv2Id2VcC5cAO0qPopoaL5RsXjp-143loM7LrMc19fDWL90r1EyQl64k0PdDqaP8xdu2mN3qvLKQinKMptmky9n-wKM6E6FsxJRUB-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=KPyQlu_mA_9EAEqPxCm3ADigq6Mwtqyu8rKiGfvPZhvNY0FISmckdpMCQFgtUyUjwVTeYaqwFfQ2hdHsx8TVF0Xg8Dkv2jAOUxVZtG2vTGUEI1i7TQVgFHvL03TrRiPtmzq6HS_LDdKbKjt88_jffcyfNMhwsXbgvpLHfnOuWRFTLb7WoFuOxQz62jHundzR3qsjHqHLg8xOLwR30-WedI1ALnt0GV-5ze9loUq1c7bqtitsrE5mwDXWOr3fil3MmaAl_RQs_2PEOg7K7A6cv3I0XsxYV6l3vhan-ioRUEh7Lf_rrzZs7eoHK_K6eIfwcAFh1pigMVrOYuDUyPzuK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=KPyQlu_mA_9EAEqPxCm3ADigq6Mwtqyu8rKiGfvPZhvNY0FISmckdpMCQFgtUyUjwVTeYaqwFfQ2hdHsx8TVF0Xg8Dkv2jAOUxVZtG2vTGUEI1i7TQVgFHvL03TrRiPtmzq6HS_LDdKbKjt88_jffcyfNMhwsXbgvpLHfnOuWRFTLb7WoFuOxQz62jHundzR3qsjHqHLg8xOLwR30-WedI1ALnt0GV-5ze9loUq1c7bqtitsrE5mwDXWOr3fil3MmaAl_RQs_2PEOg7K7A6cv3I0XsxYV6l3vhan-ioRUEh7Lf_rrzZs7eoHK_K6eIfwcAFh1pigMVrOYuDUyPzuK4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPoG5dS4oyBGrXFS2A7qbYW9NC_jkvbcccN3ej70hjf-hB9y36fWwViG_Qz0l8CKH2jzsQ5CFFAcbJ6JojGT_IrLRdc-0qxYHAjLvR91fkABu7PYBs3XfcjcvpM2q8YS14ioww67C9yZ9gcMbhZPyuzc__QaFrha_uaXUe-sNWLkhR88uE0f_pmrzf2v6xGI23yIcVhtDBUFDyIaU6dL48jGdcJgYH8ND99v-BPTEOA5e4_f4hQJPMbVmYhvKHILax8n0rjONKqKEp0ZKH5kuy88BhSB2x_9_CBZuXrWVziM9ZfCKzwFML3Ha2PSxXSnvR8VqJhdm0FkRpvKRxXVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENPJNUaAAeQTd63MUyKKaNvN9SwoPBgX9Cuxa8KQMVMVOR8qON5ebpAX-I3rpCMBXqsWUW92B-P8aji9yMeCtQUywD1fbOEu8bHfN0eHV5CFXqhJzN24mNHPgwt5H5ZLhyE54rFNPflrTubsQu8u0fKlflT5Tz7CFY3LK0vGdtcEgxwRbS7nckpSGlzoZnEAZc04-2K6gEIA9z28YyJe09z8vq_Qd03f3yes_FbLy0l7YvjD7ti8rM6_H7ldvIJPyEgGct2VTA3niY9uahJtwoUVa0AQSf8eRZC52i6CZamJ-e4jxoA4Eqv2cUXOBmhR3aIHaufwEWlIVFQPOQaYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHWNmQ6W8SkOjkjeipqAl9K_S0kHWRip4GdTbF4E9C57xJHAbr_jHXs9FYpbRKTvTLnW0JnuzY4IkiiDfGaC6JPsQiMgS27dEosx9YgbVmzbM3DMTZeN-ntWEM7L7XI3IlQJVenSFohserDyQmJtip3EcIzbXNZVHVxROZw9g5rG2IRBz3diIkll0NtW7dL0s6h4u-B3a34SR7cWZHdguTjYgPh1iDnO_Bm3uXcG0-wjS8HcSlWggpVJqCkGiINEJdZWQHKAg-V1qF2ATXF3EQeEWQEteEKnlfm5mYYGP3K_FUwEJ553owOg4SgHsKEVo7NRVWeJ97fHJ4MwVP-wmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=uWENPl2MaFCCLO2-t2V_BL4zyvQtLSD6UorR0jTpv7dzt7hyP-clXMBXuTsZruU_ThGlOt0w4mSS89EZcL395TyvNQ1uNK8l7g3xMpPhSAt8n8ZHe7c0uhKQaNlNMmm84lWWNzqEEUj4dDVQ5z11rgIS_5O8zWfmzpioooPIA_ckPSLmwUq0qavBlGHBf2pXgDcM5KkJLcnR5vxF7eTIfyj3mfReS8qrVzxcV3Z6skVIpJed52gsY_kd8vwmgSuN8y6--mUpJVa9Bab7zBJMXR-yOdh7mNbt2Bt6GBrIJlQ_oYPFjfSzfJf-QCkCmF6tSY0RRspetXG_LRbSnsKhMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=uWENPl2MaFCCLO2-t2V_BL4zyvQtLSD6UorR0jTpv7dzt7hyP-clXMBXuTsZruU_ThGlOt0w4mSS89EZcL395TyvNQ1uNK8l7g3xMpPhSAt8n8ZHe7c0uhKQaNlNMmm84lWWNzqEEUj4dDVQ5z11rgIS_5O8zWfmzpioooPIA_ckPSLmwUq0qavBlGHBf2pXgDcM5KkJLcnR5vxF7eTIfyj3mfReS8qrVzxcV3Z6skVIpJed52gsY_kd8vwmgSuN8y6--mUpJVa9Bab7zBJMXR-yOdh7mNbt2Bt6GBrIJlQ_oYPFjfSzfJf-QCkCmF6tSY0RRspetXG_LRbSnsKhMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8hQqedU8DxQSGWBoik_y10G0dOpYhOnFG0mEw7lqh9hGVW8GNI2rxmm7TDBMlTaoo-KME-uT7HBWZgPgGa3MClagSArgiQQTXh-zE9eXemw5fc6Sv-9t52_nwasMxFiiS0I71cwyyeCLG8kMKRn51YTqs1LZn-_TM-yaGZ_pYOM12aypmFoefnAlj2ya217wemLs1Kygp7jFmdT4xYuRm8dkfFBn6TV51G25w2lHHfyzYzuVYssdy8W5Cbhh57ysiRpgyE_BnWBnEWEB-HV24GbD5Ls8vB1yib51_q1BKY_STmyeiw46yjptqbqWJ8RAX4fsdutiMdHmYCw0RNQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZwGxvkDCQPBdKBYBlc4kH6xpW5DTzHiSWNVR8FGuXwiZsVFKBiQSedLcxpAVMHb9FPcniHLgUWBMsbhamLqQRYo7lps4pE9y28oiXJw5S6iRBc3OUTN57ki_InIdzokYPnjU2vsDcvP399O0An37By1geGTTMypKzsIIqwxIjdMDm_mhTJ7FOSK4QQAo7Jn8rlAVPH-gZTfFxFnsVOCSynzrHMiecoqq-KAeEoNdyvDKv7YcqVn5rqLFM_yD77_wJUZJBfGHB66lN1AB8lFZK-9Jsyoi5Epvlu2IksXVo40XOQ9_8PdFbxmyQS2MWwQUPjSWPOdtoEJCZfQLa0x3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc7dMaanDRZaFBE9saKzpnofElNEFPszzI9WDUjRxVXP1ctCdI3YHVihPpjkiUaA9KehvEzsplugPoQwo_YsSIMkKMNCDT0MzSbOw77szJDz3PvCV8KfF4Ab9iveQD2qrf9o29Tw5irU6sbSPZ2Fxbc4sGMnjZPeP2tVrURhAurbszGe9UefbyOE9-d9LcACIOPJpcvYQv0U_u6OSgVzHW_vhkFJHSHMq6y8FaLYBR8PPhZ1aOZZmNT1qqvpXdsEBGBV5VB2oKIQRBs2x34tW1CuvGDLgds43-mXxY9b5VGyy84UZOEmgad2hTVeqOQDCn13vpq6q8DvdgHn6BiWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_CTgJGuaKydvfi_SdFTIHChBNldCzlNhhQax3fqMJZ3ne1SdXIkVmKUJgm8m7t8KYB9VnvNWfD6LBG3bpMfqp5_syngpBJOXqLKJhvDQJT7PxXzlCKXqWglfqm0VqGl7a5B4-HOFYdW_5pC_biGK8kGhbjGBJIca_JT0thK0X5kXSLTbWXdFiulc_LKj3Sst3cLDn4XDpzKVq5_EanB-FZoGcpRUKm7FdPK11HR18cO3R8seWPR6K5UYmki77Ca0pqk4eGKoGHLR74mSRJGgfYS6fSca5CMOoafIj7b6VRfMEW2336HPQ2UGYlYYeLQ2bhMBP2Cfev7ScyQQMiJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe-zfxZzCKAlBkS6TNr9UNRPlh2KHXpY5KU30xTlz4IG7F5bCVV_kWoRNutmxm0jCmYTc0gBK4QIhsvQG24TistlSJB0VwzNCoLYlwnABq8HJM2kglXXgpFoYJb-Gherr3Vpicclh8pc58ll-JhtGhr2mimbQH7iJPNydtQlvV6xXGer4BAHG1rUuugQIP_nhIQfUgXbZeeNhp4S8_gFAcMisIeL09Mfv2X2OGdqXNCAbVjOTN-9W1RW-lYmBUGkLraNwC-YpXnjudPHuwwmssRzqqcQAl0YifIqekYN1pv843EtykW2EzcJuoFQQDu0kHH0Amlv7e3rUNQp1HFQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5ESgFsZxOpk4XebYsridN97t8L-hPqEJcVazOV9xd24kJp_ie8s9MvfRx84b5dOqPCwOx3P6PcD6Ko-ZiywR3pmkTAQZytgMvn7CM2U0PwSHAHNYIonbCN3AdJ_OZO2u80ojtjzM3-SeJJKPBKBXnzm2NylmlGipT_rEYMxOO2mQP-mljjCAouNnlux3mt_gYA7-fdi-43ofGsTqCFErj4XnU-MnEjY20gjHQufyQLUrsxznjYtFmndwnwExoNeJAIqsT8D9MqkjdxYEifaqZShjTGfkbrxw9dOeCoMdEzIDidw12VYyMA6ud7Gf3RloAWQGOkCHyYxJFn0aL8Qqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE-qHfZUHk1pXlp8tti-CcrKYXmv3INWhF4eN3zbrFvLIVlzvA73SnbVtqSHkm7k6rrZ0XyAcPA3exBHrbSdbK8ahvMCBs1TKo6EHhVlErujqOkVFpkRTlM-S1yTimveW3uNxfQ9694ZXLZ1mbyNYaxOF1SjNZKjkHGaOUt32SJ5ARUEzuGNbWoHQLv8rC5a4fgOsUelIQb7Cj1RNewm5-x5qLKL1ehG-my93jMo1TbIYmw_UPAyzN8ehn-viZKD_TjUfe3jJ-RRzSFIznfkY3pmFKwnlaO_z-n8l-_BpQ5PxIue-hdKWiR-4GCnI5hnacmfZoXM8uO8g5nTDsDh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEWnkuNqmnoITAZKKPIhIxOkKikX1a4hNlrLZynRelkFENfDGU0oQEyk5mznfl0UIiICa4r3e3pKQcqsoSs1IFBlaBm3Brq_NjoewbPJd7xGPzGbN2ieId7dEqPWgqk_Pj4uF-rQzDT_E6NJGxRp06A-mj0u_W5WjxxoR6y1lBNhcBVKo-TOMRT1crZ8XStAjb6ecnfTAof8U74Y3zl3-LpKSrpVHKTuI16vsjZOi2E6fhzTpn8c1t5HEKfGNo56iwpod6LmAKyiOr5BnAbqJh-JSiV-lO0dwoFZqVL7r4O2-2O2ckVzzOq8hzjWSbvz-cIpEARnVIUVniAaWfCtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zz7E8ada3HBmP0p9xnLulO2OUYzkSWG0Zec0eXgAHlpr3NAvkcPO1wQTfzA5NF-sd8ERxLQvATnVtzQISViOwuubxNEOlTRY-wroAOTwQE8rZuDJEt-QZQA8R9K0l4DcM6KmoSpAY12Xmh1HJsrl4KF7i2VcJjw5kOYT8DuCJn-07a7w83NZK9hSBDEJKDpedIMJhcnE432cCIYbUpc0nyMUEfCP6AdYEflv9hcyUdpQd8nGa2atjfxb0ZcyLQzqyzqg5EgVyqU2ScktO7OpfLAy6-VSbtmLG6koMCADwTg4Q6oc_S8Y0XrQptoFDvakiw6rPUKNccjRmElre9DFUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=q3EuxSKonwqeNN0D3V1hHICAuH_EufX8DoppKeBO19CcTFOP5ZWBn6VIh64VFs7qIEcTt6tk1d2teqxDvj8tdtUluniT0V7FkbpDIFOvyepeXnC9qu0nIj6HSrCndtLc4fj-weumK7sI738G0ueSgWvamD9YAh3wSpMQklybLw3DTiSqok9iPvVJEsza3iI8OjnLwcr2rmNGjT1Ne06QO0OEfqA9RMADNj1DBEB3xkVEQuKs34wqgXq4l7SncjJFVqh8qDIvifMsCnTW_rLkLAZkSEq1Q5qvA75UM791tbNgGiTks11HyPrhhK72cZG3nmrhjus_ya8IinwzltPKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=q3EuxSKonwqeNN0D3V1hHICAuH_EufX8DoppKeBO19CcTFOP5ZWBn6VIh64VFs7qIEcTt6tk1d2teqxDvj8tdtUluniT0V7FkbpDIFOvyepeXnC9qu0nIj6HSrCndtLc4fj-weumK7sI738G0ueSgWvamD9YAh3wSpMQklybLw3DTiSqok9iPvVJEsza3iI8OjnLwcr2rmNGjT1Ne06QO0OEfqA9RMADNj1DBEB3xkVEQuKs34wqgXq4l7SncjJFVqh8qDIvifMsCnTW_rLkLAZkSEq1Q5qvA75UM791tbNgGiTks11HyPrhhK72cZG3nmrhjus_ya8IinwzltPKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeouMHegO9I4I_CPYR_v9e62YS20njWM8PRffcqkh817OqisuNbr9eQQQY2sMmf1Ro3abn7__uIRc92dJ6xnOh0XIPlgK2wJvMwVmli6MPdYnoHU8ybc5i6qUsB-YJpIM9ER_a5Jp31LpKhP4YicnqOSlKFQl4F8JnLdo3XAcqWf9iN6niNX2XdIUfwyrDb4bNjGzn6SwP1wPCZ7UJQpUds4ReM_NYRQwqnUJa4P1KsrgFOujxK717pJHIgODy2sC4ybaWKH5c-SVeXWf_O5V8X59f3_Om5jjoLCT1A3FztjSsjaHQPsflGQm9N2Q406afTx0G0Qv4jcI1w2vleAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=tev4WzgpEVIbN9vJz2IEEvPBipAZmQKHcb9kIJHWef4BvRrevyyQ7VdeBnZKhqcIL22taL93qoflszyt1eR-BwUjUl6w2lN5q6-9WBLxdMuwh-vIzEk2Z5pPZvRV90AqKOWm9Iho7di5S7iOuX1-EsincQUBa3BnrQr37OuPSiUYbd9DBhCg--pNCKAtIiY-z9I09kUlCIj7JhtAhP7ZuNyfSnaqJIu3N1pDyRDIVwggmfjHX5_7k_d67AIq_TVTS6VF_LEPuHKxYTI-S5ASzsbjzccI7Z8Dvr7mgvd0hK6xel6ggzDZKYj1A-2-4fLILDFsI1BpGGR6PiAacW_uDI1vUG3B6KW_7Er6Gjg6HTluXAFLMOGUdqZQD2L-3SmHdvNqPTPN_CE_lwtxjZMcNPsOx_6jyKuvWFgcOhfjt1yhC3-jYLcjjpO6RuFYDSDqBlIvp6Ol5wFZKpXexN0m2CqTO0bv3WxTHviRHl-pRGrn_kkdFth_JvY8BkQR8e2tkAa-Yv024nxmGLv7tACwheZkPJxPrV_P3xPX0ApODgei6JFaJi4ryRCgUXXWmQZRmuzhrO6NtQlYvh358qsAqrLpUSx8VI2h5K9p0pjevJ-Ro0SX3kry92BykiYjaOVcrtxSynSsaqtM3QmBLOcGD_8IvVTkyzwCO386y24Fx24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=tev4WzgpEVIbN9vJz2IEEvPBipAZmQKHcb9kIJHWef4BvRrevyyQ7VdeBnZKhqcIL22taL93qoflszyt1eR-BwUjUl6w2lN5q6-9WBLxdMuwh-vIzEk2Z5pPZvRV90AqKOWm9Iho7di5S7iOuX1-EsincQUBa3BnrQr37OuPSiUYbd9DBhCg--pNCKAtIiY-z9I09kUlCIj7JhtAhP7ZuNyfSnaqJIu3N1pDyRDIVwggmfjHX5_7k_d67AIq_TVTS6VF_LEPuHKxYTI-S5ASzsbjzccI7Z8Dvr7mgvd0hK6xel6ggzDZKYj1A-2-4fLILDFsI1BpGGR6PiAacW_uDI1vUG3B6KW_7Er6Gjg6HTluXAFLMOGUdqZQD2L-3SmHdvNqPTPN_CE_lwtxjZMcNPsOx_6jyKuvWFgcOhfjt1yhC3-jYLcjjpO6RuFYDSDqBlIvp6Ol5wFZKpXexN0m2CqTO0bv3WxTHviRHl-pRGrn_kkdFth_JvY8BkQR8e2tkAa-Yv024nxmGLv7tACwheZkPJxPrV_P3xPX0ApODgei6JFaJi4ryRCgUXXWmQZRmuzhrO6NtQlYvh358qsAqrLpUSx8VI2h5K9p0pjevJ-Ro0SX3kry92BykiYjaOVcrtxSynSsaqtM3QmBLOcGD_8IvVTkyzwCO386y24Fx24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۲۰۰ میلیون تومان درآمد در ماه از معرفی دوستان خود امکان پذیره ؟
بله.
شما ميتونيد براساس مراحل آموزش داده شده در ویدیو از معرفی دوستان خود کسب درآمد کنید.
عجله كنيد، ممكنه دوستت زودتر از تو دوست مشتركتون رو دعوت كنه
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSIN05qy4VyfkHCCr3ByCwr34mA5iY9ysLcUiEprOfo6G7y5G1yUrGCnpsw-KYgRbBvuIlWLzU9YUQGKGk9jTyqywVSqwLNM_lSisa4wxS3QroVRdswELM8C_mvGTVp-erZQS8bQ2k09XxpUPwXJqCcjAr6a8mMRC9C4i8jtUnK46KALyGynK-OLrcAhCC34bfBUTaFijWVF-jOkXwv0-_KbOyza3i8bqDGLB86aQPSmgu0UA_lQz9FFJuoNJxpR49amFqUekcFmDxVs8oiAsxxDF5WVesDUd5-pmZiZvX2A0ugnldMjaKaM1u6hElshVdLrC_jbXyOiHjmCu8JamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdeeQW871Vcfl8JTabEmLiuh1Cm39jPcjS2lBreUZYwv3_0DxcLagsPeIm2vRBxWyIizYYZDhxmNnrBgQQKKs_7znrC1OyU1aLiqwI_xgDJPL1WBAH-5aXUNcT9bNxg2pKpL_LK-Tb9sOnqy1KWwqz2bz6n0n5Nb7UuznpmY_-S3bc0euxsaCQdUvXhGfrS3zrKwTL8uY8uKUVPjGSioJ1p_STuew0xvgkJKh9yVW6tPO55AMFndGl9-cWNd82kG64clB5x3XA98ACAixZSA_fHHybjWNy2HO5bOjY7g4R0A3DBPnLOrYv28QCrYvG0epOzKAlddeTW89CKS14urAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4P6daKlk3m6uAeW2qix3OidYhAPwfOUaYpgn2vNHZzXz4FqFDn6zWaOs8Tso20FZkl1Bh-VQXMwO0kMmBU_Ndd-z0WbxWcPs0PpNb4wb1Tb7rtNVQalWfX7n-h3nEBumFcm3RMk6kS0GddirHD3fuCVA0MCSQdgUM-iCRX3BcugAkDkhRQbTZgOhuZlY9kEem8_FLKQy2wDRDpA2sfDXTyRHm0DEw_ZweJQZieZQhRCLgm5oLJz7cYaMBl_qHqMD92VOcPPOzWJFn0DC8NOpBWat5iBVi5_S4aBeFxaZYxK9zUB-45fCaev2MGy6rmz50oeFT0qyvm24yRSutJVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWtY4pscqpU62tRw7ULzMVKALnKPAUopmuA8RBx6G5Yy0iEupFNShG5xg4RjYVzqhix0am0YrQ4f1dLxLPOaiSUT3dbnf6QSrcVIStywlSsY6RlV6KeSyMc_DtF_tAvWEpV26brUaxl16gArKUT2OUL1ktUb_FgtznylRLXMWwCDQ9EHLZIjAIluQGtgUVgyRsbNWTIJXCvxENJFs3pnloUql2712Bdh28rLnH7kMNoFb3_9rsVNJHEUw7FZGWVpVEuJkCV3UsjZrKPdPRv6t5Tg9hVYWMe9RrSWyWkkMsWFL3SnBRsufCHTWgpr9LxNfL9ZHBygeNVFzmSVA1kzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbfsaDiLRLx9D2TrcxJxDVJExxjIEmThwse-QZ8GYMSQWGItPSYunB_0sknothGXFxmbk-fMqaNsJNLkUa3zp_UNEWf7b4-6eYAzDDDKtZpU2by-tryohMhPKHsOajWDN5FgkphZv4yHs69Z8XaI7mIQs8pKqes55_S_Ty9JFnxImNkqhzZjoPsievSChwoul5q3CHCC8ayIXHPndA-CEcSJGdV6z0tUOWj74GzeSlSA8CfHOl1e_BjmwHxcyDhWYN3ul4RHqnxXI8_heiapOFnD98PbZy-3uRSBbadrmibTlpGN53B0JZ7retLRXaReTtfx5k9sGqa-OTz4iHOo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzolcS0deWbRlvgFnn_hFC0d78pT3cyjrh60lD4cJupPPm1TKHPs68UQsE_ALcGOfQEf4T5p878L3CJM2ahaRtNzkKeOw44t0kA1KHU-wnaxheNZtjg2buJ9Ogj_nipVeVmH8GfruhF84K8Dxo0sfTJJ0md0JUlOZ2UDNaqT4AaaNpVZ_CtyBgb1s_PhY0alJGcDUA0DTbwatwE4FqA96814k7nl72hdsFoxJV_qkJnBgmrKlxefw0jPGT7RHXXKTiyGtwHJcWWECNlv6Rr7DAKI88bB3ZKmNPi1cK988F1nTIwjISYy5djGOfdF7RZvZAAC0w4G5963FkQoUuAREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-Sx8QQC110jnWUSXbSGlPVPZy7-wKa7wbfYkKmIUy7yinmLoYUJfLCp9wwkMaY4faMjjWajG5UaY8bcKTYcEOZhyW3SHg__kwuDmL3JYf1ihoEa2IMtOly3Nqt5yiLOLk5TodsUEQF3klGQhixKHcL-Ms5voajkkVHlMmM4GEkPyPZxq9Pqe43fG8qIE6nzACCsVRb_CNfgIfp3-vcVEDaTEs3ES9Fg7KfTpr_9yqphfq3Tw8Ls4ASxYRj5okb_0SfUqPV5jWEVfDpNX1C6kt4kIpIHnZX6XcJoJrne4qAtNE7NxRYi6hNURfaZzc_OSCKDw37YsuWWUwnXEke00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChgWXDrWaTerCkl-S9SypM0fi9G-VKwtXMCHTL0LPzoOwjAqa6ovwy5YXxlXZ4hfj0M15M4V6atmLkd5I_c51jrqnVWZyLg2Ovea-n0F6SB7oYND7IJOcUKXdYN6KX7dmR-zjWn0boAsb8pCxIcUEaVVHmQ7vy4o5YMWrT7W6Ben_7ZpFS3eBPKzjWbV-RVX0GlLajepEjnRJv1qQcH14pAaBngJs2bq-AvaSQ3zPNY_6_ceaJ5a1Ahc20LxiRI49uUCEluKyzLCGhgsqAKhWbm7G4aj8ZdtiXh11OnwKEZ5pTtUIlfbNak3MdwNvMC_diGESzRqx9Mu1t0NVH4Jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ophnmlDlj_ydyfnOdasERemk1lz5K0iGOb8dNOA5oELb2Iah3tiQyJcTyrWySdpIwp3Nbphb8mR0G_O23PfuTCfXb4kVJeRxF-i01AoRWYE1NqI63VTMvpCgMzuQldV6kLmyk0fgucCsPoroRarpoV2va8dktOQcVJ14QFOiY9alq0LSjPADxM6cteXcxA_bQoiKx7499-3g-nfbSABaw1YRhBchyH-vWkrQrt7G01nDvJv16xwhw0mN2WCoBRcfdfsrxo0hSGnKoM_ru4m0alurlF4hXHhCmB6imma7mhRWyQakY27okBzYqjDox4olEmZ7Q7_1Qe-zr5394C6MsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=TVt0IjxjR1YtNVbl8zhdvDpvRat1R0EX7CvUqrfsavIZUlYGDqJlipHh-99A2PAr4F7YRTDnS5UQHM8HjeasGAr6VDAy2rOgyu7DhTD1R9KPlyc4AgIE8ORIJqx1K7spVqh97UJWqWWfzJWhk0Be45BQgLrjoDPfu53Q6slpT-cSgz38jABzAmFM19yyJqt39LKYL1soc8E7XwaC8VqdE30LCURgRXkLjWE_xldjrhFI_cjAI3Tux44yeLI4NtQHRFnU683dIwsdZ8z0sDnTCxbFwMg6gtP-u60nRKR-9yyXVHKSzyTAGyr3tyiXHGvP6FItu9tcwRlwhYxTmI69Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=TVt0IjxjR1YtNVbl8zhdvDpvRat1R0EX7CvUqrfsavIZUlYGDqJlipHh-99A2PAr4F7YRTDnS5UQHM8HjeasGAr6VDAy2rOgyu7DhTD1R9KPlyc4AgIE8ORIJqx1K7spVqh97UJWqWWfzJWhk0Be45BQgLrjoDPfu53Q6slpT-cSgz38jABzAmFM19yyJqt39LKYL1soc8E7XwaC8VqdE30LCURgRXkLjWE_xldjrhFI_cjAI3Tux44yeLI4NtQHRFnU683dIwsdZ8z0sDnTCxbFwMg6gtP-u60nRKR-9yyXVHKSzyTAGyr3tyiXHGvP6FItu9tcwRlwhYxTmI69Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua2dIVeJTn8C3lWBLOFRB6ubPaBXY4rXlV-0bScr3P_Lnl7gGjawPEO_UhQY_glTq570viEwC009Pg--LPIifhSKcPI4NVA5YXoo7RC1JiSA98z1Y6O4_xQb8pwf_VlDIG4y4d0HxnzpcpyzFi65wurgj8XzXN79KJQrlWXoJX8xaqekKdLedZDr-LVhu_LLNb6bXQ766FXQKwzNvyglhVrZOgaEgFyxC4DAMOBQW2iRP2ysIR_Tv3TDRH9GDFNE7KTsIcdi0juOOwB_muZommHb5yRKqcNMvUcwRRwMYIxCG-rPu801k5-Q7tUQfFqvZEy9YGkgrblshSPUJHVAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpGhMpNbdva1MJtkELWh_vXyrYwGdWhUU23Xd5NbmGACvwYaA6hy0qZuRtUfXGstI5QLn1vbxJ4h20AgOGM1FIQmNfzpgszOp9eJdTkPyRa9yIUETIIudfJKloxrkXer505e6ovTqwLihrAB2S0-X03_L0vbH8e1esAw84NjFmT2LRRIAcOpkkmGegERRjzRE61DcjRTPW6sJTlrD5eCZpbG5Nq5xsavennZu9tizLpyOUzksYEPUKGHkQ4uQ2j_kXnRuc7lF0fmyIYqGhsLYa0sNct_jp4vxwCAhMH8AnHs7bpa_LzC7eQB3VBplWY3zbkrupZ61e3Qv8nxRZkwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmXQgrbWkhDTJJORU-kH13hNQ68agZkU8NUNZb8aHKd4x8y-My6wT3Bt5t_MO5leXd48Bie1BQHtTD9fJ_L55G-uFzhuY5EQJDZmACTrJIA1M5ahHriRivPhzeAsYZSd_SFbLWvASGCckY1DS6yUnCf3CrlkrKY_r6a-XZ_ipNd4800dNNu57oKBoLvoxixGRg4w4dHqtq8CsX6Q0BAid_O0KKysR5M0pyOuzh6I6VHh1Mc3Jr40y6LsraGkBEWh4ExhLbx2egV5zqbTuAgo0-clz5DN9bd1q-7aTSS8b74BbD8_4h6qcrTf609quM0E4xHClpC-fCqU2SZGk2iXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxMcO-aZ5jMUh26mL1IEAlTRwbm3xe02G907Fr2xBWyCfw3fmxpZ5POGbWjDNqHFbuDvsSY2NTZCCx2DxqOfeNy2r8MbPmZUWa7KMTdfvj03A92et-RHo6rOFnLwCTsZpKqpRrmniBEYn7mDa6qcBbBZ4fecSAzxNfCDsnHhO1gdme4bBMTDYFBnRsp71D9JhmW1Rnw3DQLnlVgLMW1EbFmWprn7bh58saOledo7SgW3E3R8W6UvC8VcCpcnZm8Dscb-hbjsa3tZfjWsBog6f8LhOvfePFHv3t-z8MTAF-nNgODlPp-HFpKC_kQHGBy8x11IsSofCmZEZrssKvGDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHzn3lxgldWPvPbk9e4iC2wJL0XxeHCxo9oVRL48gdLTQa2xMrClXhIbgMOmfpqDUoLKetb-mvfFDz9FR22wu2J49i_QvHNb_f4AO5S24hOxCrFUQd_U2NHvLJnMK-8uTIUt7tXwfslQ0rky6x-k6R8gRVjh9tXT41xpIRSa5FGJ0jy4Q_yehJ9GqrZJ78_tFRsTGcRpR4FJBW9R86c_sPqHKixgKZ0pq_YCfTNq8LxYYwjPI5PPXD3R8Zd1ohEygt1bpOuty79gfTd-sNKsSXv8DrlCnBmL-hc3WEwdRKWd3GJ4ZjYugpyLuu24xtYWmjjjdAcgPhV8WuLeUAVMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvGYktq0nqRcvH7vheis1zh_qp1-4Hk0ByDWrjbyHOgPhf2e2Rv1SmFuMPvDX_ZHfOXeaT9fb9FyUKVk87EBN3faz5qKsrB27vyStK3CxKQlOCnld74Px26KHUH-BM9yciZCchv918NhtJb6uu-h54ejypn2Ke5Wyxs1AESiGU6lrSVKtgruHMOKUtX-v_-yDusJq3Pc-F-UCbQ-frueg0MXz3onGqcQRtCha_7kdTsgK-DJJqBw3me73dqU84IHfC5IZFnOrGjZtYhLL8G-QMJAZiaebBR9JBB2al9ePhzY8FUjLn-X4lvFO_Y7G5Rq7pDRZ62u9MEoJ5UNhachIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI959Le8_KcWrSrQSkqSOkzRc2JXvEEJlGYIYUB4s-MQPkcFMgcHjbrWuKmp0KWUze2-WkLygrpsGm0yOGJ8FZzbR80-UBUK9scAJh1fyIMDj98AsmLObcmgsOBe92M5NOrMgtKG842uzziV3O9J78mSe5x0f9MnQKR8Rpdutcdm5o1olf2e7j3w_hNaBQlnLRJVVyCffxK-7ZZvEksTZFBmeNSU4rYzqvUFFIP6v-Hwsv9Kg5HTpcUfS7kv2tBwR6eteCyZesdfZwaEB2uAuKDM8ryxaU_lYQ7TxNr7N61gjK_uc8TYhCrXDtz4DGpGUBZznwEonKH-53YMcq2_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebWRd7wAhgi1Pweo8vU7w_Qm4CdMEb6jSfyblKewmJa4tDQ460KeRW79YBuI-HzCdh2oLMcA-RrqwHoQvbeu4iRfyaveGZFbIhc2EcR08BwRFz_eOCOQrytYmSNHIlywFuV-BMhc5_6iIHJsQroIVez2zAUsGpdi8xcqbyoNuJ63YBhIYAzmaKddjjWVwyQBSR3WMJds8cJjXVcu7sRVrwAsj2ao5D8QRwhbNWiklW2DuXaP79tvby0QNG8KbiOsjYCLvNkMUWq2Miv7YvtZHRAHdrp9xjcpVmA6Z6xnAxE0yCSE1P_dvANwnjMXS_9yZrwyMBPFwM9XnaUovAhuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=E56IQkQp8ybSq1VV94OqNb545ax0cwAo9oMsDjKd_QstrPigv_RlTug700qV7RbYGtZ4r6umBLCE35yJ7Bzqx1iJrxbZX9SfhL1NTjHb1vngxQjTbdF7ZYjkA2JJ9psc80kKqfglHSRtAhQ7p8OjeKMxmKkFF8HqYnTUuy8XYbnKa7JugfsXYUWqdKtQ3lQVVtThJADSkWTP1IddzygLJFDPRWlnJFMk-dGXFiuo42dEBAIAVP54YhFRCQ0DlTh4d8sBoPrMeET4IPhdrzfZeFzpD9bqcw5hHoRDo7yy0dz8oFfRcxkpDHDQp_v6BgfEhKwTpk-B7CsQbeKRim2Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=E56IQkQp8ybSq1VV94OqNb545ax0cwAo9oMsDjKd_QstrPigv_RlTug700qV7RbYGtZ4r6umBLCE35yJ7Bzqx1iJrxbZX9SfhL1NTjHb1vngxQjTbdF7ZYjkA2JJ9psc80kKqfglHSRtAhQ7p8OjeKMxmKkFF8HqYnTUuy8XYbnKa7JugfsXYUWqdKtQ3lQVVtThJADSkWTP1IddzygLJFDPRWlnJFMk-dGXFiuo42dEBAIAVP54YhFRCQ0DlTh4d8sBoPrMeET4IPhdrzfZeFzpD9bqcw5hHoRDo7yy0dz8oFfRcxkpDHDQp_v6BgfEhKwTpk-B7CsQbeKRim2Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv0WX3GDHLwF-mQmhfRLcOiwAcXyERAb4V_M5ZRvScNGG96VBdDmODBqB3VeY9dkgb8nQpjs_-Dq_ENlZWgaKelhwCJpbzgMm8GwRYBMS7PWEVoedvHmDt1QpyY5aJVYXroutteMLdvOE4w-nBrhBmmXeW2_hgSDUVyS07u1vtWxePzcZGVrYIcr79MaoAA06XcZXb16i3tjyp2r8xJsNCiKio-gyDBJk9SOveZPAG5dpfpJnw4I9EI7_7nJAc-t_rUXdEFiPBwLOg9hK1QOzM537rDueS1lsjI2I6MP-fwadVZzcp8rqP5MoZfZtMB7KlMQ_T3nSWEAJ-dDhQLJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YziyV5kte2kfE06hTBmR3V3b9DIirniZKv-QIg_6HJIror-aDwlqAfq6WgvdvVXL-BzqGwsPtzaljVnWLHmcQK8lD7SorZx7_esPqOtUVGZv8EPdYaytuk0hmbqrBVqfMiv6uI6O0zEOZTGerB3ayU5_o8ZGzLFzs5pE4ymfKuZANplNW1JuR5G-UdaYaxkvjdchXpbaHocV_d8Whfa0CA-8Lpuq-COAGHwnvgXOEW9jnPCofzMtcqyJzVaMzwXN2jZh-NC0y90CCCx3H-tL-5R14wpRouyluvV-fWvSvAmbyuJgKS1PoeWN_ntke_aPaHznLoT9KgrcHWcxu2eQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klsidglaq4b3Qke4si_zO12RMkrQs90qcX7dhcahzBd4qXxoUDOgN1_4S9hSVAuMnI0BHHlaGLH7uSuGAkQ5m2gRF3r0eJZgbY1nqixMRYadLSJMTQQMQL5m5cyagKYe3H2GpqK8E5IpC7tXX-_sYmlSKp11Lkq6DVAL4crn8jFqgekskLvYlzwHlWxk5S7oiLDrxqe7NlPAIpWqhfBcV88tL9c-ikhn72KUKNagC57S9O45vAzdNq7uz2ye6-eh4f20S0uyXsuQL9jboYN9M2SNDWmQW_0pNWsfEd2Tgyr7OIN1NjlGBeaqF0KwMofig2-bFGIyYAGfLeleaneFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVD401dtiAd64H0QKX6WY_ylxcWkohHlwVNkgCcpCWROV3RHfjL15G9CC9xJSCnOexUcc_nRhoPATWjJZR_Ed5vDb7b4_xBF-iNeWyC9m2eKHygcppDZauBiJdi3mNgOxfdLz1N_3N0MbuBek8D2xtN6KRF0CDXu8JdDNUgZzUMEK8hpwrZe5H75IqQ_fGkiaZRIlStjsRaIdmOvYoeklDvdluVSmn5sriRq0wcb0knJ5GjWtdAEdF3ZuGWd6aZnzhpoMgBKx_2UHsF5v6Kdq5V7GT2jw53LuHq-5BQtcLL0p3S-V-qHdeZTwItsCKqPM31mcpYcTXJFxjwFF-DkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=QuPiM0QfeoQpimv0Zh3DNz0B0MEvSH9T9Wt5cjG1PfD76j38Kz6T8I763aylkeVcZjuO8GSSTZO64SN_Spglf69Yx2dHiGcXld7je9oNeb-O_Ggz-MqAfNw_PIoO0lOh9I3WnT2bKA-A6hy7DaL1r97vN6cl6DYP_qUdUCB3KejG4aqU7D01oeP7eZ8KSfZ2DIBAqtP0DfRB4gjLxMdbIjZqReI0qc1c2O1hljCqs6qM8SQzYQshAA3rPpiEM_fAyK8--PnLbjrtHbta4ieZMQvRrmDUTu-qfdpXTyvbPo0BGEARI_9eIBKMUjAzqOkRnW5EQ807-Am1FGij9WtUzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=QuPiM0QfeoQpimv0Zh3DNz0B0MEvSH9T9Wt5cjG1PfD76j38Kz6T8I763aylkeVcZjuO8GSSTZO64SN_Spglf69Yx2dHiGcXld7je9oNeb-O_Ggz-MqAfNw_PIoO0lOh9I3WnT2bKA-A6hy7DaL1r97vN6cl6DYP_qUdUCB3KejG4aqU7D01oeP7eZ8KSfZ2DIBAqtP0DfRB4gjLxMdbIjZqReI0qc1c2O1hljCqs6qM8SQzYQshAA3rPpiEM_fAyK8--PnLbjrtHbta4ieZMQvRrmDUTu-qfdpXTyvbPo0BGEARI_9eIBKMUjAzqOkRnW5EQ807-Am1FGij9WtUzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9_sNlF0QpMrLfAbs7QGOdii3vz301lkSXUcSLukYbiuE-12u5irMnpWQvuHwk9Ha1AIZUanN4mST5cIZaak0mHNxJ8JkVIOo4BERGKodABUHfW2XjaGyU79I8hvW3MAvlHggoNd6Siowf4WzBOE95o4vhWO0ZHDSsPRkgQLa9QnqRTmZ91bPvEPszRYD27ZimHB70BY5L-me3HKeoo-CY46fATfIG2ouNTH3X9aggouVRVYY-mzBqYvmVtngEFxopfz4xrMoCalko_ts8Amf07d29lf5Im41AzG47GhcCIJST--6cK81HwiQShNE2A6rCivFqqgxgIlDiSS5p5ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmJLUyLW_O0ZZ-GOl8Oqjil8HtW8yHxkvM3WKoGxuuSqkEMfS1wCaiMpvHg5XlZZNuUxiXccTeW4oG91oqYHpE7S6D7vBz_HLVNw7PokNAQyEFQ6uP2RS0EjzxIaOkiPnzAmf0_uN_WC63d0yphNaDBzthK5Q-3dnZzmVG9IO6V_U-MO-Y-ZsF8sl5yhYNlNY9_OodDoJw8MT6XoWW7FDtequQcPDmBxdoqnIvcDOu5fowcYeue0lilMIvL5RVcGoaIEChwaGygJ4YPeFur0WdGRtczXb6GOM8bb8Uu0yUrngSGqZiuhlduMl-GuUb-NcMCH8NTzfFUKF2Fbk5125g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV9wuefwRMbNr1b7ZJ5LywNrcNjOmnzAMARaH1l4iZOGlPjNOBgFakKohmtX3C1J2ip4z9W_bOVQNxEXErtFqSSlgmglkb18AFv1QlOEO2b-IDJSByppbvXxy84rVH_NHnHRJC4mOII-wb81a9ozTnhsrC9B3Qw3-VnrAg218688cIdM8Ikgkqln2MFSvhhLggoiqP0u8iYs8Zbf20LPbHZg2uSysrZyTWPDKyKoFVtZxa8-MdNeHeIhg_f8jLmfRRk0C_uBpVWbm79LV9LaHtJUbNFpW6QNOSTCibjFO6982LH_emLwWJriUxgRVBN-TPhi2tALZAfFIHTi7TF6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8ONGn9CyO7m9j01W5cEQi5dsoxBz0YsMARNI1zDlw6hSM-60LWAS6DEvyNkcfMAXCxTnf_B-gjarUW9X4vSgPnGrjBg_MKriU_vdyq08spcshpHwQyDnjm_otYSsFF5aMlCj92B5OLx3auvH9mLx5cm1Do6ko5JpgkUVURdBrTBYM0glapY3O7cDHxtnKRP_kB9ZM-CeyXfPUFwmDnIkr2Y5yTmdbzMirIrZkUrYtS0UxBzXv8cIbGeiLEvK5O95j-7DpF6acFPkZIs5jWqW0CRDejezfYzMUN6kWhRlsy7OKfUuSrt-k4Ekw2ugv6zhg2WMqqJ5j7xl3E9xES3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=bx4tRWDrUXVy-DAWrkUkIHuBe94yj5_-EBZnvcPHLsmn6bLLwjBEW4pXwN54vSyq_B6wMVWIs2DFufA-tlYvUHPo_hbGtYVnvrKKGAf5H72quMbHK3ZjBhn49eofpR9d9pyJU8XX5HSRCJgeUlOquuswEPH-EhI9HM3D03wtFUcxsAXJPWb8yzVg73lLKOjVCOxp65RdtTcfQMZv8b15ruu1Rj4o_PIbtSQrkVJ61-IrTlXhXvGOlK65vtdynEoqG7YLsWNmuX4_QfN1PLioVyCy64SDIlZL1IO6oui5JJSrQARWRu6Y0oG1yY_2EABYlf7LW0UJQyKLFm4tR62fqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=bx4tRWDrUXVy-DAWrkUkIHuBe94yj5_-EBZnvcPHLsmn6bLLwjBEW4pXwN54vSyq_B6wMVWIs2DFufA-tlYvUHPo_hbGtYVnvrKKGAf5H72quMbHK3ZjBhn49eofpR9d9pyJU8XX5HSRCJgeUlOquuswEPH-EhI9HM3D03wtFUcxsAXJPWb8yzVg73lLKOjVCOxp65RdtTcfQMZv8b15ruu1Rj4o_PIbtSQrkVJ61-IrTlXhXvGOlK65vtdynEoqG7YLsWNmuX4_QfN1PLioVyCy64SDIlZL1IO6oui5JJSrQARWRu6Y0oG1yY_2EABYlf7LW0UJQyKLFm4tR62fqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=hQsy8vgLjsECp4-_QqcNYHPSBoHHQAjTtRKGnYipXx6xlR_rg_2jfSuQQS_jo8O14MqDJkzSJs17VE5eecXHIw7_bgj8RqLaTQuTLLxm_YXAc35hxlRCBiefBgeQO7LzkbMXy23sxgg9wtlgNCTlCGayhA69PZ2onne2djzJqIN6EdDusdaA1GymiZn8Vei466R8ndS_luJRVsNloARa2w0sNTdCk5yw_Ym0aof5QwYm96wDvlsGrGA0OTqx6U77tpGhAyL24EToKCeJ_ZoKK8nMjDxDPwUZ_QvO-QeITqCIazec0ZHVH9z8IJ9wqHt11djK2EQM1o__oJ__cZSv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=hQsy8vgLjsECp4-_QqcNYHPSBoHHQAjTtRKGnYipXx6xlR_rg_2jfSuQQS_jo8O14MqDJkzSJs17VE5eecXHIw7_bgj8RqLaTQuTLLxm_YXAc35hxlRCBiefBgeQO7LzkbMXy23sxgg9wtlgNCTlCGayhA69PZ2onne2djzJqIN6EdDusdaA1GymiZn8Vei466R8ndS_luJRVsNloARa2w0sNTdCk5yw_Ym0aof5QwYm96wDvlsGrGA0OTqx6U77tpGhAyL24EToKCeJ_ZoKK8nMjDxDPwUZ_QvO-QeITqCIazec0ZHVH9z8IJ9wqHt11djK2EQM1o__oJ__cZSv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHUmridCF6LYnYRRAUVzTOpmdutG2TFkV6oMo-g7Qm3N3j5Ubkt1RBeAAqyjpfOd3pI9MSEP0MBdG7moLOlybd2AD2ldnZLpIjrWxH8yyUws7zTr71XjAgwwEiUsXFoIbhvm3CkyuZu00w2-fl9zrTY2SFjytEmw7emUbLSJcBJrltMgkss1ChyhLAWBzqaPOZhikdOwyWyssh1MtETneCIpl7B802LikE80RBsGTkj2DNtNkCtHQqmhDHLVxMjlMR6cplSo-ca4P4eXB4VCt92TQBrfWzK46JUlRHfDNgd-HqSLmzkZgICsM2i6eF1N_dyH4I24FMiFud-M0jCSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTKNIKM_TEXpqXfpDOY-7HaTcaFyXWP-bXmuWeNRLe_M6wGRU-pKBBPLRF8hxoxTeFTUeDqPsXBCtqMZIzoVULtswZiP7wTN4TXX5lYrQRkBwL_uZoz7um5rQL1VuNvZ0mIltqXIfSpamRbtykf392uAdFgYdbgziuGGLupsG_ksySis6hPtSjhJo9rL7UooQb0Afivf0i0rHN88ffwIh8Mdi9yDbYupkY2nTxW9ih2s2kcDMzsb0J48SUzZHoY-yfOAhhkqzJCyqtEzl15G2eYe8OSCYHhyG1r4H3DZW8N0M8zfI-Xy-64qXM8sWpeN1n6bL5lSH-OOo0XnkawlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Qi9jl7USQVemdVjtkg2kXgdTNgfS4Rsbe8QUDDsbQExyTLwI_vLWJTQbcy6zbTBaxnKgxztea3ALOqU6rlwk8sTbRIupRSUO2WjZNk2IJcSUrQAHjcTqdUh2BmI8FSUu05E62Y1y5qhFsW4SAZy-OxLHJr7p-BOAhKxk8Q6rIi5q79yUDPCF2HTztCn6FydGlv12t7a8MgZLWX-5ypl2gsRC-1Sv6_jHiIBdK0JMOszASQw9nYX2CUFx0W1eLeGZfPCwhuci-dvhls_itIwLMj_f_SbZ6z46Qu7PftDS68kSY97-qPDhKKip5-WrZzfcHLGFR571Qmyc7HUw-UBemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Qi9jl7USQVemdVjtkg2kXgdTNgfS4Rsbe8QUDDsbQExyTLwI_vLWJTQbcy6zbTBaxnKgxztea3ALOqU6rlwk8sTbRIupRSUO2WjZNk2IJcSUrQAHjcTqdUh2BmI8FSUu05E62Y1y5qhFsW4SAZy-OxLHJr7p-BOAhKxk8Q6rIi5q79yUDPCF2HTztCn6FydGlv12t7a8MgZLWX-5ypl2gsRC-1Sv6_jHiIBdK0JMOszASQw9nYX2CUFx0W1eLeGZfPCwhuci-dvhls_itIwLMj_f_SbZ6z46Qu7PftDS68kSY97-qPDhKKip5-WrZzfcHLGFR571Qmyc7HUw-UBemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=KZ7Rh1bPkuDcHmYSAoSxqKGdovtUZCG_yfv9Ua7rAzyoJQwmFjltLJzhJEKa_rj6jZknU2RTmQGT6v64jsFdGX9ikO1tTEttJZUoWR2DsWJF5VM5Vu9kIRCVTwXNFrcppnuTlEzdZTHzHtyfH_iS--vYZzNFOyZVu7G3HwWAN6YVFl1XSmebmAfe1bLZjvFROm-3SIsiIEX0k6qiDXw4Bss6SMVuMReu7m8F1kyO_8thVvdUNb6nZ9c-BXTFzuOhqwkRHHEWJs-_b_ZJVr7o5bamy8amafKaQeqIxyAO5BTpBbJKrTA5gfu7yreQh3btiCa3E-K1u2nzWvWzR-CtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=KZ7Rh1bPkuDcHmYSAoSxqKGdovtUZCG_yfv9Ua7rAzyoJQwmFjltLJzhJEKa_rj6jZknU2RTmQGT6v64jsFdGX9ikO1tTEttJZUoWR2DsWJF5VM5Vu9kIRCVTwXNFrcppnuTlEzdZTHzHtyfH_iS--vYZzNFOyZVu7G3HwWAN6YVFl1XSmebmAfe1bLZjvFROm-3SIsiIEX0k6qiDXw4Bss6SMVuMReu7m8F1kyO_8thVvdUNb6nZ9c-BXTFzuOhqwkRHHEWJs-_b_ZJVr7o5bamy8amafKaQeqIxyAO5BTpBbJKrTA5gfu7yreQh3btiCa3E-K1u2nzWvWzR-CtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS5Kd0qBPzHZIIDhOan6b2TNusA7SGmrnLilvr7N5kQ399x5X46ByB00TtquUfoqd3BdV78V8UOom2fq4TZgwehwAwKLMVaOvfW94FgUWGMmZmGB7QruPY8T7LaoMFTGTf6zXdMq1UUqlYexC88ZJfzEoaBVtEB4fAI-YDT-Gaogf4pRRWlMbPmAm4nQOqDD065ft8YQH9d7o7nZHz1jE4Zi1NEnBM8DN_FV7nancmS6AuK56Djb9c2VP5aJ3pVxWEbQRXSKsHFQwnfuarTZI2tcuX-Jbmas5ZFHmfe8yCpyeLmnHQlXpj1NESzvu1KRA4MR1Rlm_TRN0rgLLOPifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRLycVkkz1Xig9Z7JgSQeWrebkiymZ2oP8Jb_Zd2PuvtU5X_G0YxTINSnSodR5IlEo1-vYs7evg34dvxVMjVDwyZU4IKK8hzkx-b1j-KaQuZ3SIJ7KQziWJDps_JKkGz5hkWJCI8W4TG-lgRJJxjjj98K25DPcDLesfyt2tvnFGBzSr1fAAy36cZ1Ev4Wuv59aUURKgRVabjAxS5XYyMVNAXDKzISv5kSNcMu70fvScOQe5THe1goElQLOEfwzjLV7ItRKu_vvFBuCvMRgpL4RHRHeL28yrtBiposl1FVwNJrjggjck77bqFNJCFcYPUPU4XLn1POl4Sj6xGhL300w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJbwefE08N9yMnRxOtj1qbyMiftZHcCRE8i5MMtjMFIsz9yFodFSePVCPd4XZ1FUnBxH6h_iTB9mBFNzcFPJM2fLhMEbOIHEQn6vhqiGESB_POK_56rXzNftnbykKE9oUVvHhXQhGbqhZ8P5wmKsdfQMYPRog2LYrip7-1UQrAOmZ_0zhrvlvJZqmOHYEdmxuP2vPXlAP6F-KDd8WP4KA0k5k4ipjqEbXeINYFsc4wOOnOyonxaWUW3nzDoXvuZE-rQrZU4D1fz8zpTkfkyaY0Wab3a8N8d4Uqr2kFEqF9KbsTHdVR1TPqp8kMmNglWOZblnwrJjm2ZEJjNfLkO8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=j_b4fi_6WAQb9n-SC27sM1pJVCd6rya7oVF6hpgdkMCRwC2Up5uTOub1xPN7rxdWxFH4zZ7QKBmJgxTjwpfs0DE5WvPwtqB8D5B9nrXgAgTm89jb3jkT8XO1vIYZQgxFblr1auzczVN9dXkwiLopHA6lCMxzLteHYY9HdgvVRBHKKHLbe9_Od0iVoA4wtCLvRaFzypM33dXOHGs5JryR2GBQgR7Iqpyuci3EK9q554gccmpfFcf8I2h1pgt6uDQKtnU0wJR9OvRfhdaxdD7xWsUX7egbUjNZMxSQ6qkhCyWF-97at0aEUJeVYfyW4xNlnd-_e5zfDY9oAyH_VQn3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=j_b4fi_6WAQb9n-SC27sM1pJVCd6rya7oVF6hpgdkMCRwC2Up5uTOub1xPN7rxdWxFH4zZ7QKBmJgxTjwpfs0DE5WvPwtqB8D5B9nrXgAgTm89jb3jkT8XO1vIYZQgxFblr1auzczVN9dXkwiLopHA6lCMxzLteHYY9HdgvVRBHKKHLbe9_Od0iVoA4wtCLvRaFzypM33dXOHGs5JryR2GBQgR7Iqpyuci3EK9q554gccmpfFcf8I2h1pgt6uDQKtnU0wJR9OvRfhdaxdD7xWsUX7egbUjNZMxSQ6qkhCyWF-97at0aEUJeVYfyW4xNlnd-_e5zfDY9oAyH_VQn3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=gwLovbyy6zkMWr-fQiDkIeCW5sKuh-yOt_sWCQwlGc_0Ihqdu9hwqFj8eMc-3Dllf5rl5qNxUgXTsjUH1jEU37j6FMHcoK4JkV8fSsotCUJX5f6iAOaPbA7uDhGwuKeSGCo2347y4EsOrkp6JzX0brbPc4028weVKxXmDNV_rIUlYfCTFBGzcDbkyX8mPKeeSIFVV48PymlYr_T2eVRlcAZ8k1LfHVUJFm3ePHSerN70z-bVwEKmj6q_xR3yB-3gfW-04Kx7oP8kTxw4NS0cdxSyrorcFd9zeFqiGAeogMJqYpBdVn2nN5k0L5E4E09mU_kYZ7njSruZC_KEi2Czng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=gwLovbyy6zkMWr-fQiDkIeCW5sKuh-yOt_sWCQwlGc_0Ihqdu9hwqFj8eMc-3Dllf5rl5qNxUgXTsjUH1jEU37j6FMHcoK4JkV8fSsotCUJX5f6iAOaPbA7uDhGwuKeSGCo2347y4EsOrkp6JzX0brbPc4028weVKxXmDNV_rIUlYfCTFBGzcDbkyX8mPKeeSIFVV48PymlYr_T2eVRlcAZ8k1LfHVUJFm3ePHSerN70z-bVwEKmj6q_xR3yB-3gfW-04Kx7oP8kTxw4NS0cdxSyrorcFd9zeFqiGAeogMJqYpBdVn2nN5k0L5E4E09mU_kYZ7njSruZC_KEi2Czng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cqj0NXVMMwPaNyi5d8m_NgB9nq5Q-QhVHNneKbZYuQ7GzKxVcQvl7XBUtEDsBFhbcZAeZ9VDOUaGFjQjZ8AOBbc36JdNsvFlCcjTMU1apO55wMUA-I4A2W_WWY2er5eAv6D1q4aUQBGwnoqRZLas2a35pqvKpQeFeFhprxrTCs_QXqdHHYlpU8taRA8yHs_0vLQ1f3w_Bc9J0bfjLfrpat6230T9kiz5JME102myv95eqFEJGKpaf5jt4VuY_11y-upW1mtpAQwVqkIOu-04oBdfESlbioSUZj_ATCsYCXYbOaXCdFVmro2EKMqsmrhE066krzU2-IKYVeZMaG7f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqRa35EOdTYZ5PEWJsf9Fq0OL6y5Jdd9gTS21C_W__-DAa7BUc-irEtijW2lq9Cqd8S4GY5Jzb-ZgWy5OEwDAy71p6Ox_QD2XQBS-8MeNFcfevfA_GdTPGU4_iv643Dz2EIujUE0OJcks7Ko8NK2jfBTfAm-UfZppNG6HLGSOfYxRZbqWe0AnwP3yhRuVgoP4uIOwl5HVHQS1RoGBqy-M25Ig-DTjFd4RaHoWCM4f7QouXcREiYIpoNEFeTXzpIQBP6pWTSqgmO11k29ZlWbDj3s74FId5neU9-4lfCZUOGAbyD3IZcAUXr8mCO0xxH_99p60Uc6FgtLKzIiNJ58ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjI_GBFVNqyzKpmr8jbsjNoPDj7yzRpBOMumusJDMBdUn4gBHDTbOMkzDMgssdBF2qLTFyfX4Yo2N4_DK8i23KgcGIcbZbxmynEPvJysYLCGhi4-CW-VoI4vO0wriWFO4_lrCi4LxNbzzHhIgzurG6_fSfwFD1gTqULctvdEwP3--u-SVUJxx5BVunrruhJiYaDPdqC8rJZJ09FMyciH34NnM6iB7WxEVrl9qFfzdQioKgx5N1hG7gKVALuQiTkP_8OYuDApkIZsLsr_geFD8SSTvwkf7IK18Xw60AcfpGR2EgSG__4qGztrXORruokhsU_Qo7Feb_gvKovR-M-jfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkCx0c5xEAjve2UcsFLBRVM5iWzyNQqZfegam2yG_242dAmQ-WXhcTnGt8GDKbywsCzcYSm_HBvu14o0Cg1K_wZGh3mKgmUj6MfIWEAbIV7aICu-5radAx95-KouX91BcPYm51L5f8BF_Sn5RNFRNoMsTTnmLa3OtgwCbIO80gMZf3el9PZcdTGsH3a7AJhGIrtl2y_Ee5dsAxkJ82J_9ZrkkhYsHb9XJFZr2qf_OXhpfgVrzK4uIFiCJMIsGJsXC4trItgxuR_M860ddsgLRtcEE1l86Hb_J63XmXQhkrkmUUqDmWvb5OAU686Ty__nomgon36JlwIqIxMmn9CsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE98agHffGLlX3Bc3RWRK9vRzOcrAwAJJImlyBcgyxAIjN8gLmGYsWoEY8H3EKDvlbjyIVUn5HuCNzOQXPQgCiaYLmA98n5U5iD0RVgMgfVXxrCmFU3NwJgpCsZoEMCdAbV-otLh72QB8u1VDwwvp-JmP9eDgMLMjuPBJge-HVBUqzj_I4wpcO0X3ESDwezwDXKJcq7z_qY1KppenZKCNpBtuZcAjrqARQQS3C4huuHAOpNnfAj5gQhwUHJaTwOO3d7hx563O1Il2F90_LYq0mCCh7QhXiuwLn_LGsBJTx-YuVNRTZx7WI-ucgTm0Cp_3RLIFpQ5nDfMTEgHpAF2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
