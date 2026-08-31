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
<img src="https://cdn4.telesco.pe/file/qmqweqrD3xzr51d2Wkt-_AY7Gu-mbTvaG14CxCf1xXfiDjdUnlgovFKeo2s8rjNBgsmdo22S8t2lOa6A3brQ8TlNDgfUnJ29Z0jULPx_BKbss9TzTiJnOcfzdLGuC1TbON-s-Cwh83Ih6cR1OksNaloFOTN6fW8j2esAFchyCFc_FqXQ7TdXkltXbiue8ohn1srdhEZRfI8ZkyRA3RmkGKFRWvn7B5-4tdJ6F0YWmrgAjSFMwpHA-R2MLnTAJqd2HcqjF0ICeXNvpu84UzrythWP-_RTwDsjZgpu0GNDhWtsj5mVf_mSN9mn-DuFRtEyOl7VJ-SMbAJqIJGz7uLvcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 960K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-144710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی پخش فراورده های نفتی مدعی شد: جمع آوری کارت های جایگاه در سیستان و بلوچستان و کرمان با هدف مدیریت سوخت و جلوگیری از صف های طولانی بنزین انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/144710" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCi-z199_zUddqWnepSwpVH8_2R39G0C76srQ_gZpqYQeEWPLptJhkPJcLgSTYOTh4Whgs0gIg2d2AgB_GwwFWK1jIne05oyp8gm13_G22SuaklmmV-QknVefwaViM1tmy3i93S5bpUkFntkG71tSrd9reAd_KJd13VBwr5QGlbNvvnn1TxUSFDPEY6HnJGySdlgvWVv58RrY2sZZDxl1O3Lti_Lo_GDgdH76Nd32vQUqwDOCjw8CwTeI-tJCB6IONyQWXFyW2i7sJNpMpCZaWBoZLjfOpJvAlistkk-ViLa7awDJK_VNa9DMpDihmE4oOryiAHsilEcVzr_-QH3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان با نخست‌وزیر هند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/144709" target="_blank">📅 12:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
انور قرقاش، مشاور رئیس‌جمهور امارات:
وضعیت «نه جنگ و نه صلح» پایدار نیست. ما به راه‌حل‌های سیاسی واقع‌بینانه نیاز داریم که از کاهش تنش و بازگشت ناوبری طبیعی در تنگه هرمز تا رویکردی فراتر از یادداشت تفاهم ناکارآمد (که نقشه راه عملی ارائه نداد) را پوشش دهد..
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/144708" target="_blank">📅 12:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سپاه  ویدیویی از حملات موشکی علیه پایگاهی در اردن در پاسخ حملات آمریکا به جزیره لارک را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/144707" target="_blank">📅 12:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNH-AeJV2Zroda__CdZrUA-ncQp9PorfxSV7_QDNlPJBQECDuasuSI9PkK_cuesSRCgCBtHH09D31RecKWoqd722_0jbSJoGTCwD7WlSMqNxIe7htyNpuXxegSzd2XQb3KWLMyVwf2Tbk0KJ6TjRKJvorybFI-5tlIa0OshVk6T2eKpRGoVvTf6qt9wPZnVCBjSotzTkTKdBCSYOxxkacJZk1KuPKS3sJcubCLvxh4a9-iDmzGxk8lxcAT_2h-bSaaC2TF8Lnp5epW8m2sGfsu9zzdV6mgklzUz8nD6jTwprz4tDQN7YjelLT30yDLFA1yEmBvTaRfMDAMAjmSmetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: نتانیاهو با افتخار می‌گوید که موفق شده است دولت آمریکا را متقاعد کند تا به جای اسرائیل، علیه ایران جنگی را آغاز کند. او در حالی که می‌خندد، درباره "تاثیر" خود بر ایالات متحده صحبت می‌کند، تاثیر ناشی از بیش از 1000 ساعت حضور در شبکه‌های تلویزیونی آن کشور. در عین حال، او با زبان انگلیسی، از رهبری ترامپ تمجید می‌کند.
🔴
او یک مار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144706" target="_blank">📅 12:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قانون مهریه چه تغییری می‌کند؟
🔴
عضو کمیسیون قضایی مجلس: سقفی برای خودِ مهریه تعیین نشده است
🔴
ضمانت اجرای حبس یا نظارت الکترونیکی تا ۱۴ سکه خواهد بود
🔴
تمکین عام همچنان الزامی است؛ اما زن می‌تواند تمکین خاص را به دریافت مهریه مشروط کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/144705" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0bV5PbbY-tViiATBYPUXBzcvnlJi4Mk61gaUcSppsi9ky51IPbVgJQQuyhYkef0IUvAKf-n-M_WNehMiO8nbSxjSYbAeWybkTtT8XMLQH9L27cQAKuaA4Rvg2TWBRG7Qp_lnc7Pw-2X9nq2d922rVrXoms2AjpMkl7y0qpnbOFIb60gJGKwGcSOjf1VEFxuLXyRk5QbWJm2lILHtd5QdIvw0_c3Ll9-8hUBXVG4uvYD-MT348-Awr9R7oZw2JorlCmkFH3V_QBTFBqhNMbuKpTOXzrNvKdwOSCUE7TaundNMSmPTyMrqC2g8Meyi-VNEFwRicXUAzf5evh87gA6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :به محض اینکه در جنگ با ایران پیروز شویم، قیمت نفت مثل موشک سقوط خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/144704" target="_blank">📅 11:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
واشنگتن‌پست: چند مقام ارشد نظامی آمریکا در گزارشی محرمانه نسبت به ادامه عملیات گسترده علیه ایران هشدار داده‌اند و گفته‌اند این وضعیت فشار زیادی بر نیروهای آمریکایی در سراسر جهان وارد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/144703" target="_blank">📅 11:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الجزیره: پزشکیان احتمالاً در حاشیه اجلاس شانگهای با پوتین دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144702" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5dadc26d4.mp4?token=EqkPlILlf2Rq0QDJHMtSowisoeFVR3qmNyH0zaOLkIO3ymUMNKx1hmlR2VESruSgQzccs6y34u_NiFJgBe-yPDS6ke3co50jnpLNteJVzZaH-9eqQ0FWjeCdp-afVVNmdSu9CAMaRjU8t8GDPdpQq1qLlAl0Ii_C_n6hKGivvGkWwX_qEex2BDngmsA-KEXDKloPFqm6oJuLUhBG4bOlaPAXfDWnCJBhfF2v_C171fISkfHrKSaKEPYTDEoMoERSEN3cLDECFo1-6ohsQN9_7jo2rxgybHvtPO9r8iWsvGhw_BwtytqiNqjCbK52X1h5Qrq5CfzjnYoOkNIN8V-EsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5dadc26d4.mp4?token=EqkPlILlf2Rq0QDJHMtSowisoeFVR3qmNyH0zaOLkIO3ymUMNKx1hmlR2VESruSgQzccs6y34u_NiFJgBe-yPDS6ke3co50jnpLNteJVzZaH-9eqQ0FWjeCdp-afVVNmdSu9CAMaRjU8t8GDPdpQq1qLlAl0Ii_C_n6hKGivvGkWwX_qEex2BDngmsA-KEXDKloPFqm6oJuLUhBG4bOlaPAXfDWnCJBhfF2v_C171fISkfHrKSaKEPYTDEoMoERSEN3cLDECFo1-6ohsQN9_7jo2rxgybHvtPO9r8iWsvGhw_BwtytqiNqjCbK52X1h5Qrq5CfzjnYoOkNIN8V-EsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش معاون وزیر امورخارجه به حمله شب گذشته آمریکا به جزیره لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144701" target="_blank">📅 11:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مقامات آمریکایی به نیویورک‌تایمز: نیروهای ما آماده حمله به نیروهای ایرانی تهدیدکننده کشتیرانی در تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144700" target="_blank">📅 11:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365909d20e.mp4?token=P072DuCM381tEMFSKKSGNlVGuW0TdN4uXH5dAwST7gzvrkaxlogRcztn5kN2HpUv6lPUWqbXKNs3Wi_RQwAYHQ_p4i-bJ9-Ljf_T5CEsPx-x8vHUzIUbvHoxySO3UogaFffJDoqtXVP6mySYufNakmLWyic0GCzC7AURH6-EGPuUKn8TNW5e-L4Cm7f4KMhKNtLI5LVbmsOBbq0TZtc-AmD3qdymXT3vuUUH2uhO6iXdqo_yDYYFzNxMAmVJUkw3MJpL9VzHCwy9Yh1j049gRc0Qk_AOJPchUwlhP_sIctNreWLEEz3q2uXE7I_0DsUhVEseErzwV92RyKVN0fgU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365909d20e.mp4?token=P072DuCM381tEMFSKKSGNlVGuW0TdN4uXH5dAwST7gzvrkaxlogRcztn5kN2HpUv6lPUWqbXKNs3Wi_RQwAYHQ_p4i-bJ9-Ljf_T5CEsPx-x8vHUzIUbvHoxySO3UogaFffJDoqtXVP6mySYufNakmLWyic0GCzC7AURH6-EGPuUKn8TNW5e-L4Cm7f4KMhKNtLI5LVbmsOBbq0TZtc-AmD3qdymXT3vuUUH2uhO6iXdqo_yDYYFzNxMAmVJUkw3MJpL9VzHCwy9Yh1j049gRc0Qk_AOJPchUwlhP_sIctNreWLEEz3q2uXE7I_0DsUhVEseErzwV92RyKVN0fgU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه انبارهای نیروهای مسلح اوکراین را هدف قرار داد
🔴
ارتش روسیه اعلام کرد که مجتمع‌های انبار در بوریسپیل که توسط نیروهای مسلح اوکراین مورد استفاده قرار می‌گرفتند، مورد حمله قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144699" target="_blank">📅 11:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر کار: امشب معوقات بازنشستگان واریز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144698" target="_blank">📅 11:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کرملین: فعلاً زمینه‌ای برای از سرگیری مذاکرات اوکراین وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144697" target="_blank">📅 10:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvHwGcHWVGmdNht_Ad1w_hWrWXORrsbdLBGhYC4eqTwV0YUwjcJ6ScOgoK6jYAg4bisUe3PBRGl6PhY71Uvh9zyAzAUQNsFi0MN8p0TIkqVG5uoHf8CcrsDvLirL0pjS0rQ7dgbz9dbWO94k1wJ7ticPxYUo6FIQ6e6tmuSpiWqroSqQaH2gk5Dxku9w7GMxco-Gj4KSTpVAstXBXH2zc7p51K5IIdXvH_gjpbHjt_HM-R3GmMKkxTnxVl3f_79ItJHMH9ONokEByN06Ts3ECLzqF-m99GRYKEJIP5tp-PKkQlTcoyx-jpFu5dXkjsCvSoAU15wt4iAWtH3lzrD1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی، فعال سیاسی نزدیک به حکومت: حمله آمریکا به لارک هم از نظر تعداد شهدا هم از نظر جسارت آمریکا ایران را بر آن داشت که تلافی کند
🔴
آمریکا پس از مدت‌ها عدم تبادل آتش دست به حمله جسورانه‌ای زد. امیدها به احیای تفاهم‌نامه ناامید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144696" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae84ddea7c.mp4?token=CvmSxlOw0P2MWU4LcYhBL3nOxtNRkXxWK_wtY-spdcQ4LJJp2-1hcYFVVkjA46IYuSMMaXsyY4PbkCW2wvyIGpwcam1ZpMvl2iSoqzEyqTaAfDXTMvx9cXTxMy07w8JV1fcw9CLzmc7FaZu4Zl4qbXlFc1711AaTkoQaeBTxZ5fQm6X6AMaNjxOlilJwmooyKAF3kGfDAUs2Zx4IEyFcoSrVFgOgHA_n0eRuHVMDfXUzch0257XwWXByHu9gBic5SYS9nK0PdlKEwP9vGkwNsOIzWSkoCFd4Ogwo6zR1xwTcICRYsD9kgcLKnKsnpDBbL-Mlir04YHDBAVLpacRx5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae84ddea7c.mp4?token=CvmSxlOw0P2MWU4LcYhBL3nOxtNRkXxWK_wtY-spdcQ4LJJp2-1hcYFVVkjA46IYuSMMaXsyY4PbkCW2wvyIGpwcam1ZpMvl2iSoqzEyqTaAfDXTMvx9cXTxMy07w8JV1fcw9CLzmc7FaZu4Zl4qbXlFc1711AaTkoQaeBTxZ5fQm6X6AMaNjxOlilJwmooyKAF3kGfDAUs2Zx4IEyFcoSrVFgOgHA_n0eRuHVMDfXUzch0257XwWXByHu9gBic5SYS9nK0PdlKEwP9vGkwNsOIzWSkoCFd4Ogwo6zR1xwTcICRYsD9kgcLKnKsnpDBbL-Mlir04YHDBAVLpacRx5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران :
اونا 52000 نفر از معترضا رو کشتن و تا همین 3 ماه پیش، حتی به خیلی‌هایی که اصلاً اعتراض نمی‌کردن، توی خونه‌هاشون شلیک می‌کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144695" target="_blank">📅 10:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت دفاع امارات: گزارش‌های رسانه‌ها درباره هدف قرار گرفتن پایگاه هوایی المنهاد با موشک را تکذیب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/144694" target="_blank">📅 10:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB7YQyehDbsRIDwFwRnrcOy_9vl2N94DlR00xb15OuGkMFHuhsyUDKQb5W9u6OnkxB_AQ0KW5sI-Rfg7Iha9sEMl8eFqTgSkY8envVVck5aPYcVk_KxNjVA9VNMtb7U8FFwtHBK7cQU0BPxLD2z7QTxZuGnI51TVCIkV13MWCiMuvTVKV6m26SJtwkUK0zI4c6j9k240h_62Nj0yJ5icOJ7xwYsUv6NJsdT_90tEM0hPUcXhqt_tEYX8JWVc6ZaG3mFnoL56zmtZoRAjy0MzZXZ9ZgSGZb_y-yMotCymD-M-2MzYmWrXgctTNbnCvx5zDF4_I7EfK7kQVStKi1DUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فلاحت‌پیشه: آمریکا می خواهد تنگه هرمز را به مسئله اصلی نشست بزرگترین قدرت های اقتصادی دنیا تبدیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144693" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794d812382.mp4?token=Oyz5vKE5k7he93SJcAtbMtc6R27m4oAKhYi8f1bpbRgrkELcqn6q2c3edZtD72ysCo-SrUUGSktSV1CAn2ce3Rl_5YTvJW9WAO24jKqhDvV1aI3FXZxu5wvyijVlESJpfPvgIAwrumQQZrrMkWG85eiCXTlZuVZ1FxVDjoZ0-MJy6ijqsELoD1sjwa7RZQeJsOqc7gzf9piFnEwL2gq9pn_K_kcvMXd_fxBgmzUkaOHWhm0a7LtKhJXW-maFiu2wFNKrcsBCEPCZP3BFbnI6jb9wmRnwsIKG2I9vvO3-iqveKNHwS0fh7xRDvoB5WIzqDm3fJy5NmnCddoysKAXd-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794d812382.mp4?token=Oyz5vKE5k7he93SJcAtbMtc6R27m4oAKhYi8f1bpbRgrkELcqn6q2c3edZtD72ysCo-SrUUGSktSV1CAn2ce3Rl_5YTvJW9WAO24jKqhDvV1aI3FXZxu5wvyijVlESJpfPvgIAwrumQQZrrMkWG85eiCXTlZuVZ1FxVDjoZ0-MJy6ijqsELoD1sjwa7RZQeJsOqc7gzf9piFnEwL2gq9pn_K_kcvMXd_fxBgmzUkaOHWhm0a7LtKhJXW-maFiu2wFNKrcsBCEPCZP3BFbnI6jb9wmRnwsIKG2I9vvO3-iqveKNHwS0fh7xRDvoB5WIzqDm3fJy5NmnCddoysKAXd-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: عملاً الان فقط دو متحد برای ما باقی مانده‌اند: کره شمالی و ایران. خیلی‌ها می‌پرسند چطور به این نقطه رسیدیم؟ چطور شد که در چنین جمعی قرار گرفتیم؟
🔴
‏لاوروف: مگر این جمع چه ایرادی دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144692" target="_blank">📅 10:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آتش‌بار توپخانه‌ای اسرائیل، شهر المنصوری در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144691" target="_blank">📅 10:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNsh2LILQ8upPyFlWkIdnHl1s0syXWy7zFvb2PsJaRYeZuScUKeO7AhzqvP4j_SpIgnIN1pctEiXbTxfIwjL4IHzylNjTXQo2Sv1V9y8hptt38Au5veCYVsknabU5ooDTSC3-sPgWRHgo59f0r4IcIy7JjfGGXNPkO7yoVJ4t1r9dcyrXm0jYnvcGz7AxdI1RrbNqmjoFms0SP_lo9mK-27DiFCH7-7mgEAdgtQlsybO9ThjKZ2VoPbjADhWZcQ5H1FldJj6XS_kjB_Com_v29EjIZbOGI6vCEueigDKyvrap-ykOPL52PoTsnPn6MHOD2wabYm3Xh6grqFyYl4JsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان در بیشکک
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144690" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز : تعداد کشتی‌های حامل کالا که قابل رصد بودند و در ابتدای هفته از تنگه هرمز عبور کردند، به ۵ کشتی در روز کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144689" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ مجددا اعلام کرد: ما میلیاردها دلار به ناتو و کره جنوبی کمک می‌کنیم. وقتی از کره جنوبی خواستم در جنگ علیه ایران مشارکت کند، رد کرد. این موضوع را به خاطر خواهم سپرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144688" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امارات مدعی رهگیری یک پهپادِ آمده از ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144687" target="_blank">📅 09:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc01c3c573.mp4?token=Xptadm-JRmHEtaOFcidbzR1VDkkAMrKZmrB1f4YqXbbVY4kYy_8j_cgUgcmv5pWkK8IWsFzx_6JsnMFIrcMqg7AIX5wTrSZ3NEZ8dCfGKmBsxGv6vCboIPRQxerKrIbL0xq7naiUA1YWs3w32Rgp-OCESvedXOnVb011H-8-kAb3VjKxkXXhuZXSSzrPuRh2ISoUwJFWR8HgyKyEgEXaABVoeeVr00ptYQ_Ydde2ZgdGplIHeB8syJBtB0SbvMBOxSQ50y2ZfJ8cKfKOjiTIoFWr47T5D4-JKzbvzWeF7bAJtL58mW58tjOnXvV4_hE0hPVw0eRp-sHr8M4rrnJOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc01c3c573.mp4?token=Xptadm-JRmHEtaOFcidbzR1VDkkAMrKZmrB1f4YqXbbVY4kYy_8j_cgUgcmv5pWkK8IWsFzx_6JsnMFIrcMqg7AIX5wTrSZ3NEZ8dCfGKmBsxGv6vCboIPRQxerKrIbL0xq7naiUA1YWs3w32Rgp-OCESvedXOnVb011H-8-kAb3VjKxkXXhuZXSSzrPuRh2ISoUwJFWR8HgyKyEgEXaABVoeeVr00ptYQ_Ydde2ZgdGplIHeB8syJBtB0SbvMBOxSQ50y2ZfJ8cKfKOjiTIoFWr47T5D4-JKzbvzWeF7bAJtL58mW58tjOnXvV4_hE0hPVw0eRp-sHr8M4rrnJOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اداره شهر اودِسا، حمله به یک مرکز پستی "Nova Poshta" را تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/144686" target="_blank">📅 09:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان دقایقی پیش وارد بیشکک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144685" target="_blank">📅 09:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMfQ4qnd6mGZJRFGcCcHiL0jDsw_5tZEc7EVztPeQW3BjO5iHO5wNgY-844A7aK_8Kl4qp75qqHdvADf6sjsOw81IVVgEoR2MSVRWtu7m1MILvLrnYM4uUtJt454W9NhFNzluoncAWx4959d_hlWy3E5pjee15a6Q2E_u5w-xCX1sNQZCVeXnxtAQwconhsbo1JjoWj6Jnec05MWFlf4LdG8mEAaWb6ts02i7-vDcKxozr1olSXhyZnRvnKMsO6OLzNnvthhuy7ZtE8BiNwevDj7CCefezc4sn0sY0O2m-LnR6uoF0FHyuJmuC97NTLJkggEXccYtSM0CfU6vjEoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تداخلات شدید در سیستم موقعیت‌یابی جهانی (GPS) و سیستم شناسایی خودکار (AIS) همچنان در سواحل امارات متحده عربی و عمان، نزدیک به تنگه هرمز، ادامه دارد. این تداخلات باعث می‌شوند که موقعیت مکانی تعدادی از کشتی‌ها در سیستم‌های ردیابی به درستی نمایش داده نشود، و اطلاعات نشان می‌دهد که بسیاری از این کشتی‌ها در واقع در مکان‌هایی متفاوت از آنچه که نشان داده می‌شود، قرار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/144684" target="_blank">📅 09:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
الجزیره: قیمت نفت حدود ۳ درصد جهش کرد و بهای نفت خام برنت از ۹۰ دلار در هر بشکه فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144683" target="_blank">📅 09:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=RDASOQsZ0YVOKDY4Dl5AHybfn9zQLowNgO3m-BE365iXVa7LvCx0_2XBmo5nzP9L95VmP5e1M8h0vIn_SGoWpoRcYOb8ReasWkIPLwtcOL1CYFVy84ORKb1X4DMpZU0K2coqc39CovpJfXbOlU0rZudtj7hfuxyzD2DmVCWJ-U4nuSquST2BvbE4yXrVKTlz5wK4tsFeLUMNLD2FpXvck5757pzzLOxt1v6cRZmGd3P_46t_47qhGDr4sQdM_r9PnKek3hAzid1Elw_URISzbe4vqAuCZJ5-kyGMIQDG4vHWaXDJq9G7geN1ZV0q7X1_qYrRtL2zyEtucvAlXZihgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=RDASOQsZ0YVOKDY4Dl5AHybfn9zQLowNgO3m-BE365iXVa7LvCx0_2XBmo5nzP9L95VmP5e1M8h0vIn_SGoWpoRcYOb8ReasWkIPLwtcOL1CYFVy84ORKb1X4DMpZU0K2coqc39CovpJfXbOlU0rZudtj7hfuxyzD2DmVCWJ-U4nuSquST2BvbE4yXrVKTlz5wK4tsFeLUMNLD2FpXvck5757pzzLOxt1v6cRZmGd3P_46t_47qhGDr4sQdM_r9PnKek3hAzid1Elw_URISzbe4vqAuCZJ5-kyGMIQDG4vHWaXDJq9G7geN1ZV0q7X1_qYrRtL2zyEtucvAlXZihgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «آن‌ها سرسخت و باهوش هستند، اما بسیار شرورند. این‌ها افرادی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت.»
🔴
او افزود: «اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود؛ دیگر اسرائیلی وجود نداشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/144682" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8272aef607.mp4?token=LARCB5B0zx_Z5Z9I9s5k0D3NaIfNJct16cq4WsjmF0whMOKsC8wwEvzxMjz3kTR1FLUwFPHyNSQVla2-Gjl6_RUz_NMyB9UVvC7hUPTPVn_BTyUZG9MJrA2w6VpVntMFlbctFV0adjQSbxtigZN82oOWeagcfgqzC4kjJlLQSdbN4AiYzXw5iIJ8zlePylUqs2_pt948mYkuwqaR5bRwlHx4ehki8GEj4fLj64DPTPTjxlfnkZmCcnhQk7KrgzO1ghTOeoap0uhZvhasY-1b32Lu_6GpH19CTR-16mf8ZA1g7d8i1Zm9W-FPs8mFN0R-K6hVxI3YH_OMRatSxGi56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8272aef607.mp4?token=LARCB5B0zx_Z5Z9I9s5k0D3NaIfNJct16cq4WsjmF0whMOKsC8wwEvzxMjz3kTR1FLUwFPHyNSQVla2-Gjl6_RUz_NMyB9UVvC7hUPTPVn_BTyUZG9MJrA2w6VpVntMFlbctFV0adjQSbxtigZN82oOWeagcfgqzC4kjJlLQSdbN4AiYzXw5iIJ8zlePylUqs2_pt948mYkuwqaR5bRwlHx4ehki8GEj4fLj64DPTPTjxlfnkZmCcnhQk7KrgzO1ghTOeoap0uhZvhasY-1b32Lu_6GpH19CTR-16mf8ZA1g7d8i1Zm9W-FPs8mFN0R-K6hVxI3YH_OMRatSxGi56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «در زمان مناسب، یا ما پیروز خواهیم شد یا آن‌ها کاری انجام خواهند داد.»
🔴
او افزود: «با پیروزی مشکلی ندارم؛ نیازی هم به امضای توافق روی یک تکه کاغذ ندارم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144681" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144680">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d419c5ff.mp4?token=eSPliCwxUrXqxt82R0orBVM5Xcw8wR03xG18MK1pmGqSsbYUEkZmkE8DScDP_0IMgj50YFHf6rZDDcsgjvrMtiZv622lQLieHt7UB1rBxA6i-q95mLfanY2n9oSn1a5ASlL32HKsCcYcoXdjt5qn20vKNAp_4tTYOPX3HHQ1C_ULnYT9cmPSGTDKeMwbyPnAP0cyLATC36fwgvh-_8RM3hIsJYwdIQBtwz3gFJ4iGFw3JLjnLAq58xJ4RlFexerC6Rck5DnZF2JkHxzLwBXdWO7c-kgfl_dY3kfj4H56VCSOI1PFEr2pPpzbOqySw0N0kEY3MiByViLWuJ7KObChpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d419c5ff.mp4?token=eSPliCwxUrXqxt82R0orBVM5Xcw8wR03xG18MK1pmGqSsbYUEkZmkE8DScDP_0IMgj50YFHf6rZDDcsgjvrMtiZv622lQLieHt7UB1rBxA6i-q95mLfanY2n9oSn1a5ASlL32HKsCcYcoXdjt5qn20vKNAp_4tTYOPX3HHQ1C_ULnYT9cmPSGTDKeMwbyPnAP0cyLATC36fwgvh-_8RM3hIsJYwdIQBtwz3gFJ4iGFw3JLjnLAq58xJ4RlFexerC6Rck5DnZF2JkHxzLwBXdWO7c-kgfl_dY3kfj4H56VCSOI1PFEr2pPpzbOqySw0N0kEY3MiByViLWuJ7KObChpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ گفت: «دموکرات‌ها می‌خواهند کشور ما در جنگ با ایران شکست بخورد؛ اتفاقی که رخ نخواهد داد، زیرا ما کاملاً و به‌راحتی در حال پیروزی هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144680" target="_blank">📅 09:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnU9bIpxvc5Q5Sq4X-DTCwhOviyYJJMHddihz_suSF9qCGfVqK8gMEeiwAC1tC8vzzFcfi-doQRvV_JjoL3pB_oww6ia5ZRNXsZHnN_wKKkgMp11r8s5niZWjkcl7f8Jfn59DCoflcFan7c0svSABx4L4L2r3eYKFSpfvMzRT2G6y_jFc5Erzb65hZ7m7TD5wWWYmXT8n2wOM7cm4IAAJa12qLqjQMA52OPW3quwlfASGSpJR3ENTa--7K4MyF5lyIyHLWzq3r95Acb1zFXg8FOs_4S85Bhha_jP1Nf-ztJqasBc6x6YTeXVeJ3-fzvFyB7SI91FqdfBSg9MWuQpzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله موشکی اوکراین به روسیه با ۲ کشته و ۱۶ زخمی
🔴
الکساندر شووایف سرپرست فرمانداری بلگورود روسیه گفت که در پی حمله موشکی اوکراین به بلگورود در نزدیکی مرز روسیه با اوکراین ۲ نفر کشته و ۱۶ تن زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/144679" target="_blank">📅 09:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1931146549.mp4?token=gvNyFapkplS9hUxiAWuvlcR6OVK-zvVBcm3PMDHXzlcatWPEID-doBDJ9FdOKk1ejJXFqe98cud2TehWN-Hanvpv99DxB9OxlniGgB_1rwO0UAbtHy3Arya_VZUaEMD83dKY9uS1n4sTtIMmjBLnkg6mbL9mr0-ZCMPJQFahMWF19OCkvZ_KH8tpTFYhb5JkQjHOtLV1OtjBY0ICoWQ7dsyLSpDhWtY8VGAlB78Q2Ji-8RSb_YahzW8txth_uoujHc2KtayOHxg5L6_fB2iqPVAYDh0XaK1kSPjZaxa3kowsnFZHf7uKubjFSxyDZ92dPvP8woObrm32ZFFie8pJow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1931146549.mp4?token=gvNyFapkplS9hUxiAWuvlcR6OVK-zvVBcm3PMDHXzlcatWPEID-doBDJ9FdOKk1ejJXFqe98cud2TehWN-Hanvpv99DxB9OxlniGgB_1rwO0UAbtHy3Arya_VZUaEMD83dKY9uS1n4sTtIMmjBLnkg6mbL9mr0-ZCMPJQFahMWF19OCkvZ_KH8tpTFYhb5JkQjHOtLV1OtjBY0ICoWQ7dsyLSpDhWtY8VGAlB78Q2Ji-8RSb_YahzW8txth_uoujHc2KtayOHxg5L6_fB2iqPVAYDh0XaK1kSPjZaxa3kowsnFZHf7uKubjFSxyDZ92dPvP8woObrm32ZFFie8pJow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایران اعلام کرد که حمله پهپادی به پایگاه هوایی المینهاد امارات متحده عربی را انجام داده است و هدف آن مناطق مستقر نیروهای آمریکایی و هلی‌کوپترها بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/144678" target="_blank">📅 09:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عراقچی هم عازم قرقیزستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144677" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وال‌استریت ژورنال گزارش داد دولت ترامپ تلاش می‌کند از بازگشت به درگیری نظامی گسترده با ایران جلوگیری کند؛ چراکه چنین جنگی می‌تواند فشار بیشتری بر ذخایر موشک‌های رهگیر و دیگر تسلیحات آمریکا وارد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144676" target="_blank">📅 08:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnQAun5T7Bi9RdYCZ6hXuYeJZv0Qk7N1Kpnz6d-YHLq3PlwIRUq3091-2H1uTVV0wUy-VMkVXVXmFwv2zhRpafXg77z6NG10sCq9BCbU-tLqeVfNkjOEoLToWo6wepko68TtMgeYGwMS9RTwGoU8ED6YcrplFwD0v4i6WyclpS_dVA0UMOnzStkjqgrYoZf1ZZ2m7TWRno2GcmlenaQ9Ag8IXzk77QgAaxQMYplclSNotknSoDOz5aODXmjCNybxd-B9N-XU0zJuWdQg1OJoND_PH6ODimKgu4FlIUXo40JDKGuj57-3JfqVRZnLNLKhrMxgWiMqJr5P5NyKGvQxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم عزیزی رئیس کمیسیون امنیت ملی
:
یک بار دیگر اراده ما را آزمایش کنید و بهای سنگین تری بپردازید، انتقام در راه است؛ فقط بدوید!‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/144675" target="_blank">📅 08:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سپاه: یک فروند سوپر نفتکش متخلف در اثر اصابت با دو مین دریایی دچار آتش سوزی های مهیب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144674" target="_blank">📅 08:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اعلام آماده‌باش هلال‌احمر تهران در پی وقوع زلزله ۳.۸ ریشتری در پردیس
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144673" target="_blank">📅 08:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ در مصاحبه جدیدش با فاکس‌نیوز:
ایران به امارات، بحرین و کویت حمله کرده بود و اگر سلاح هسته‌ای داشت، از آن استفاده می‌کرد.
🔴
اگر ایران به سلاح هسته‌ای دست یابد، هدف بعدی ایالات متحده، یا اروپا یا جای دیگری خواهد بود.
🔴
وقتی در جنگ پیروز شویم، تقریباً کنترل کامل تنگه هرمز را در دست خواهیم گرفت
🔴
ما تمام مین‌های تنگه هرمز را با کمک بسیار محدود کشورهای دیگر خنثی کردیم.
🔴
ما میلیاردها دلار برای کمک به ناتو و کشورهایی از جمله کره جنوبی هزینه می‌کنیم، اما وقتی از آنها درخواست کمک کردیم، آنها امتناع کردند؛ ما نمی‌توانیم به حمایت از کسانی که در کنار ما نمی‌ایستند ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144672" target="_blank">📅 08:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ درباره ایران: من به امضای یک تکه کاغذ نیازی ندارم. اما ما خیلی خوب پیش می‌رویم. نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان هم از بین رفته
🔴
آنها مردمانی سرسخت و باهوشند اما بسیار بدذات و شرورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144671" target="_blank">📅 08:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c58be1180.mp4?token=aWEZB9v1Kl6TIDQDjBwSfH8Ki1i0Arxf5vaa_TQi8fCHX1VwQAtIHwiIWV8UIn3s7chp-NysyEKXvSUx2UDckAA-onmB8LDd5Na9hLzdzlINPAWWSPtVZxbxvM0LZSj1lgLv_5uX56aicCFB8D-l4gGFlFK7CDTOcPeIgvbiA2xB-Gv0WqFzp3n4p0JtaF31RDc0l1eccG1jKo4y-Yq9fGhJiQPiS2cr30kLl_jSXC4jFG40RoCtJLjnzFeasGJsS1i9cor2aI9mCXtftsUvn7NyPTq_WUBs_IRBlBs6uC6NxsbT9zx71AjfqxhVKRxHaAHbMLo3akuxX5RYQefJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c58be1180.mp4?token=aWEZB9v1Kl6TIDQDjBwSfH8Ki1i0Arxf5vaa_TQi8fCHX1VwQAtIHwiIWV8UIn3s7chp-NysyEKXvSUx2UDckAA-onmB8LDd5Na9hLzdzlINPAWWSPtVZxbxvM0LZSj1lgLv_5uX56aicCFB8D-l4gGFlFK7CDTOcPeIgvbiA2xB-Gv0WqFzp3n4p0JtaF31RDc0l1eccG1jKo4y-Yq9fGhJiQPiS2cr30kLl_jSXC4jFG40RoCtJLjnzFeasGJsS1i9cor2aI9mCXtftsUvn7NyPTq_WUBs_IRBlBs6uC6NxsbT9zx71AjfqxhVKRxHaAHbMLo3akuxX5RYQefJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با انتشار این ویدیو ساخته هوش مصنوعی نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!
🔴
رئیس‌جمهور آمریکا تصاویری از انفجار و آتش‌سوزی ساختگی در جزیره خارک منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144670" target="_blank">📅 08:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndtVLpgFji_h7d-wMLkvOpvUPqgx36R0HLTGTUM8uwMhkow-wrO6igMZtA8sDPILqMIkhEpL3HMKhgnp0mmWYUUg1UmJWgyiMzrGczdEW-SvTJI69YAzfLQm70q6kBKuLcj0nNmTvA-qRsNJA7olyNX3e5JYvL94f4KnMRM9gPIkEkOcvSjhzvh-RQ_WlKLPgb74ityjD3Huq6zV3_1v5gtvWBImvRWVWupfPOe2m36i-NwpCsOcHsJDOCq6xzjH-VjaI0QhfLPuX-XvaZUzDNjhwwAZ-E_78yn0DXiBn8-34j3BDzDO7gE00m_9I7XseEHZCaMVrf6BvbPWFD5b0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144669" target="_blank">📅 08:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNbTkGWx30uNO9tXny3zfTQTpdgEWV9-iXfGSFaucCb--DMopWfnVUxJa1pe5G4cen_MvxDaBhJsHemNkVr_gLBdSyaaDiYdwq1S8QhiaaN_FiBg5zlXb_8n_UG0HlgUBnr5NrFQ4xD_L2jq1TLNTaACR6tfV09oyMyU62Hyo48mKTiK_95dmOB9PDOnopOv7OlwMd5oJlkU8p69bmYyZbb3yWSLXIkWXxe_j1ogCS9IrR8-29q8dKUoNVuFcOFABAb_BqYMk8DgqiCAqYGdcYjhZgcR8b1pdzTdmNOEWraDHcd-eaFBKvc4AopfatkcXvSwknqVA5ol4nlL2MnL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
🔴
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر ادعا کرد که حملات نیروهای آمریکایی برای جلوگیری از قرار دادن مین توسط سپاه در تنگه هرمز، یک "اقدام تجاوزکارانه" بوده است. این ادعا کاملاً نادرست است.
🔴
واقعیت: نیروهای آمریکایی اقدامات محدود و دقیقی را علیه نیروهای سپاه پاسداران که در حال نصب مین در تنگه هرمز بودند و تهدیدی فوری ایجاد می‌کردند، انجام دادند. به عبارت دیگر، ایران این تهدید را ایجاد کرد و ارتش ایالات متحده آن را از بین برد تا از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی محافظت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144668" target="_blank">📅 08:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سی ان ان:
هدف اول ترامپ حفظ محاصره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/144667" target="_blank">📅 08:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBVXwG6Eg6tuKGcar8f664cZcPLNOgePeeYxVmtjiGPQbTGv72RgABip9_bti0BF1Ds8Zfih12Y_cSNXLVA_Fb7JpIQlNVbJgOn608nV4X6DaLHtISNdgcG2thn9IA54pp9whR5Y9aYsPNiVaCWB6x8ZU6hUBmEj9nh1pC_wwaNlshROtX9JaPt41O4pOTrHycFh5frScSw6IcelDHjAzdy2velE14QaEYyPrPiyKBsL-sJvl1-_kHvvOSqQ1SPpLIMqJ6qfIANgmiMgcXSkIYa910ZiZ4I19Z-pIfIwG3beZaEeanpoN-tkz8bvHOQ-K7UuusGMpT_9rWM_jNS-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: دولت ترامپ تلاش می‌کند از بازگشت به درگیری‌های نظامی گسترده با ایران اجتناب کند، زیرا این امر می‌تواند فشار بیشتری بر ذخایر موشکی و سایر سلاح‌های آمریکا وارد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/144666" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
قیمت طلا و دلار فردا با خبر حمله   امریکا و ایران همه رو شوکه میکنه
👇
https://t.me/+8ARFoPm-00g4YjU0
https://t.me/+8ARFoPm-00g4YjU0
دلار و ارز فردا منفجر میشه مراقب باشید
😳
😳
☝️
☝️</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/144665" target="_blank">📅 03:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
صداسیما: والله همه موشک‌ها خورد به هدف
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/alonews/144664" target="_blank">📅 03:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXeK3Fxgn86ArFH8Z_6XL6wuHE8zxFejJ8rVwOGlhC_QuhjJzs1pVRufiUluxsOhF8IFfLyGdA0mg3XmztBJuHe7vCFeHGoF7dgUQtUjp3SVfjSAa4JuyvaE79mqvqYRRRf12KoZDaDNXC3qXG110_W8Qu-DOeDRGwGm5Y3-pN0xcIJWTRrgC6-bJX0jo6eAvf_mqOiuosBG9Bg7pJ6HD2vJaLqB2O6oWmRo4R-ikzOR_S7-z7tRVbGtnOf998I2ZrpSJABmcMuVqoC7jLDm-EjzVAnTv6gwcY6TNrZZWj4fxLpq4g1XbF2uY0mStRAHj5ZM_LFQJ7jBaXMejuHBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سنتکام: برای حفاظت از جریان آزاد تجارت، تنگه هرمز را از نزدیک زیر نظر داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/alonews/144663" target="_blank">📅 03:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144662">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نیروهای مسلح اردن اعلام کردند که 8 فروند موشک ایرانی اوایل امشب در جریان حملات به پایگاه‌های هوایی آمریکا رهگیری شدند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/144662" target="_blank">📅 03:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144661">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmBWe-FEyXvc2U5c9XO0FeZYwDoNWOonOL0hmM_ZX0wzGnowpR9sz-OGQYCTYBObO_-2_o6ojc5BMoKfbtWLabdCaoZTjdyBrY2Kd9rjRi5kt6aQ30lQALQgDzgQ2H_DCfB8cf3JPCbh7nc5imYVAVW7GDb45qHAu1aNAnfyCPAvAhqnn4nndA_IxTcwS6q7-PPRoawpm8GvMNtpqWqQ1iERPP9GmgLf-dAFqVajLlWlGh2zSkJmO50L9RgWxDCK4NuIrqq7a3wFXUJwUZsIIPT4RBRAsabBBn5qPrqZWpW2wraNkgV-r4D20DORx-jox7Gq3DuN8UH7sGwHjiMKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه 14 اسرائیل:
تو حمله هوایی آمریکا به جزیره لارک ایران ده‌ها نفر از پرسنل سپاه پاسداران کشته و نزدیک به 100 نفر دیگه هم زخمی شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/144661" target="_blank">📅 02:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144660">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فاکس نیوز: نیروهای آمریکایی تعداد زیادی موشک ایرانی را در حریم هوایی اردن رهگیری کردند‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/144660" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144659">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سپاه: جوری زدیم که فلج شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144659" target="_blank">📅 02:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144658">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
صداوسیما:
ضربات مهلکی به دشمن وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/144658" target="_blank">📅 02:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144657">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دلار منفجررررر شد
‼️
هم‌اکنون قیمت دلار به 211هزار تومان رسید</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/144657" target="_blank">📅 02:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144656">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری نیمه معتبر فارس با استناد به داده‌های ناوبری گزارش می‌دهد که حمله پهپادی ایالات متحده به جزیره لارک از پایگاهی متعلق به ایالات متحده در اردن آغاز شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144656" target="_blank">📅 02:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144655">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
مقام آمریکایی به فاکس‌نیوز :
تا این لحظه هیچ خسارت قابل‌توجهی تو منطقه گزارش نشده و تقریباً همه موشک‌های شلیک‌شده از ایران، تا الان رهگیری شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144655" target="_blank">📅 02:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144654">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آکسیوس:
آمریکا مکان هایی که قرار بود امشب تنگه هرمز را به منطقه‌ای پر از مین تبدیل کنند، هدف قرار داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144654" target="_blank">📅 02:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
👈
پروازها در فرودگاه جده تعلیق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144653" target="_blank">📅 02:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
خبرفووووووووری/ هم اکنون حملات ایران به سراسر منطقه</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144652" target="_blank">📅 02:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/انفجار در العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/144651" target="_blank">📅 01:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/هم اکنون شلیک موشک به سوی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/144650" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKoKBDbxuang6AtFPSQtEhQMKELvj2jCalyP4TeoDa1hcpw2o7ACPuBpgFKdPfEWh3GUbvc7NPFQsE4E1goP_2xARdinNhxDwz86VFuTEmNItGnDn1PHfwDoovFNkT50h7LP7lBs1HE1tMmnWY8ERPCj7hNSehi3QyI3GG-6MTjyYFJWHJkpcwyRBfRAbmeYdoA4of5VTn5IPKNPk3nbcF9LbDVpZBbmUfbOYWGivMGlCwQDyNoNlNlp48ekevwcysQ7gYR_efZyqMjUfgDVvO5h_awKqU8Zjdm6zWnts-EJvmnm9_xFRfN6gvPB43S3r9K8H2O8kSBqbgA45dMBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت کمی بالا رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/144649" target="_blank">📅 01:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آسوشیتدپرس به نقل از وزیر خزانه‌داری آمریکا: ما این هفته در راستای تلاش‌ها برای تشدید فشار بر ایران، تحریم‌هایی را علیه یک بانک دیگر اعمال خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/144648" target="_blank">📅 01:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوووووری/ همین الان با شروع مجدد جنگ دلار منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+8ARFoPm-00g4YjU0
https://t.me/+8ARFoPm-00g4YjU0
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/144647" target="_blank">📅 01:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kvlynsb5a-nJdqUhRk5lerkRKJpVi50tSflHAVJJCdU9-vgwPGAMcaEbW52djbCnkZGQcCE8YSYnRuCow9eZd7-V7JAsqqbGcfpxd2dpQif9LPrhBHSczf4Ls0DwIYyG25TcdGGjf6gSxb25IbU5dOohe5T9xNbWUFSfwW9L1SR71D99htroq7dbCHarEGiKaRkhgNvs-HX7WIblhSvzcSRTPXmGo_wYFWOul_ehQqcADhfen7qiupRi-g27QxmXPOypEuF7dGkiaxq4IS_H-TCE_LGuYBjmQenbMp7TXImYgsAK6YJwBe_i6gRNSXlZrtDpIgrNlhrN1k54pKLEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال خطاب به آمریکا: جرتون میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/144646" target="_blank">📅 01:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/موج جدید شلیک موشک‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/144645" target="_blank">📅 01:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/شلیک موشک از کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/144644" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قیمت دلار به 211هزار تومان رسید
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/144643" target="_blank">📅 01:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فووری /انفجار در اردن</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/144642" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/شلیک موشک از درود لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/144641" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/شلیک موشک از خمینی اراک
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/144640" target="_blank">📅 01:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/144639" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/رویترز: جنگ آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/144638" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXPkU-5V4de-mANGIsve7V4zE6c0rpgmS1cz0bkQnOvdFXmKEqZLvUEBzEKbtNS6aQ2a7hw-74EXK2Pdzyb90gxDdphUTQpBchqvCQvwiSggH64edK_xugMo5_fx5ThjaOARgyYohKtHd7N1HU9XWUpxJMAbeyV6B-kLvgCbKxLRFM5i4RmmMY_wyTT1lLsBcvBeaBTbgFrp9Qd0KcJXrE_XeRADavRL69dh8dFF64SkVeOgKtnf0SeFA4GUXU6ZnwjpY-tzr1ta29ffwDwnzX1U7UVP6TCnPpkZ76Jp1rFg2BhhJaO8J0N2Ei7YP_MxGUcFFLoCSMr9LwiO2c4RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
هر لحظه ممکنه اینترنت قطع بشه!
🤩
تنها فیلترشکنی که توی قطعی به طور کامل وصل بوده، توی سابقه کانالمون میتونی ببینی
😎
50
درصد تخفیف فقط واسه خودت کنار گذاشتم، اولشم تست رایگان بگیر که خیالت راحت باشه
👇
👇
👇
https://t.me/SattarVPNBot?start=utm_telegram_post_alonews
این کد تخفیف مخصوص خرید اوله
👈
ALONEWS
این بنرو بفرست واسه دوستات که اونا ام با 50 درصد کد تخفیف بتونن اشتراک عمو ستارو تهیه کنن
🥳</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/144637" target="_blank">📅 01:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/144636" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/144635" target="_blank">📅 00:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/144634" target="_blank">📅 00:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فووووری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/144633" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/144632" target="_blank">📅 00:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/144631" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/فرودگاه مهرآباد تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/144630" target="_blank">📅 00:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
✅
️فوووووووووووووووووووری/گزارشات از پرواز تعداد زیادی جنگنده اسرائیلی
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/144629" target="_blank">📅 00:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوووووری/حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/144628" target="_blank">📅 00:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/144627" target="_blank">📅 00:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/144626" target="_blank">📅 00:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18d748662.mp4?token=el6lWuHxPsHH25ybU7yG1cg14HkYL6wWF42t84gd_mgADkldwd2a_Se0bUSOzFcl4H9eA2JvNTnMu9uevH6edB0eHzDydtpxdeqpia868xVRhVGEDeo3yUp0GLwCuYKeoHGoQy0_IuxMXofVShZQju7CpJbHdWQ6zC5T5jhNwv3bzMjkAktboDDlWpp7mDuenCyOgV8qXzvW3fLvz-X4cOQqDaTVxGVtWAUy-46Ijdrnz3v5OWWeAQ0Cvsgj1cB3B1Wdm3T46DggA2d1UcD6Wg-MbqNPIcNsOoqsFMtuZerADjq6R-K8NlXnUxmDHR2zFQ-pn-9iifYyHHTjE-bhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18d748662.mp4?token=el6lWuHxPsHH25ybU7yG1cg14HkYL6wWF42t84gd_mgADkldwd2a_Se0bUSOzFcl4H9eA2JvNTnMu9uevH6edB0eHzDydtpxdeqpia868xVRhVGEDeo3yUp0GLwCuYKeoHGoQy0_IuxMXofVShZQju7CpJbHdWQ6zC5T5jhNwv3bzMjkAktboDDlWpp7mDuenCyOgV8qXzvW3fLvz-X4cOQqDaTVxGVtWAUy-46Ijdrnz3v5OWWeAQ0Cvsgj1cB3B1Wdm3T46DggA2d1UcD6Wg-MbqNPIcNsOoqsFMtuZerADjq6R-K8NlXnUxmDHR2zFQ-pn-9iifYyHHTjE-bhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره اسرائیل: این، کشور ملی مردم یهود است.
🔴
سایر افراد نیز حقوقی دارند، اما در درجه اول، این کشور ملی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/144625" target="_blank">📅 00:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر فعالیت سامانه‌های پدافند هوایی در برخی مناطق منتشر شده است
🔴
تایید یا رد نمیشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/144624" target="_blank">📅 00:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت کشور بحرین اعلام کرد که یک قایق ماهیگیری بحرینی در خلیج فارس مورد اصابت گلوله قرار گرفته است. در این حادثه، قایق و محتویات آن به دست افراد ناشناس ضبط شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/alonews/144623" target="_blank">📅 00:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaabb12e7.mp4?token=SY7uiHDLI2qVSxRV6xu5P5X_a4LlYeTLDt8kKjxi_AolV7i1zRc8cZFZW3lnAz0ab_D-RRGan0_wPQLU28tNeTgbiy-8UH4tD68vbYa_bJfStvZ3oRsW98gmAwavhe8f1u7bkEq3PT9edbtH4Nq0U1Wp6hWUqKGyut_mGoiIuDbpr2CrNiD6DSJ8IlxY0pS55pY1cWz5nKieCB__F9V05bTC7KkR_mFOhxsmqkvL4q_qWwNCcFf724gFJzz28sD5UX__zcLZrJuwXVcX1Xg9RlcL1trCJgln_o5TbG8E115tUdvUxET-sVF0M4oLgy_5fKkhy4_4sv2D4m9wp5aCyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaabb12e7.mp4?token=SY7uiHDLI2qVSxRV6xu5P5X_a4LlYeTLDt8kKjxi_AolV7i1zRc8cZFZW3lnAz0ab_D-RRGan0_wPQLU28tNeTgbiy-8UH4tD68vbYa_bJfStvZ3oRsW98gmAwavhe8f1u7bkEq3PT9edbtH4Nq0U1Wp6hWUqKGyut_mGoiIuDbpr2CrNiD6DSJ8IlxY0pS55pY1cWz5nKieCB__F9V05bTC7KkR_mFOhxsmqkvL4q_qWwNCcFf724gFJzz28sD5UX__zcLZrJuwXVcX1Xg9RlcL1trCJgln_o5TbG8E115tUdvUxET-sVF0M4oLgy_5fKkhy4_4sv2D4m9wp5aCyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری کانال 14 عبری
:
اگر حماس سلاح‌ها را پس ندهد، آیا نیروهای دفاعی اسرائیل (IDF) شهر غزه را تصرف کرده و حماس را از آنجا سرکوب خواهند کرد؟
🔴
نتانیاهو: اگر لازم باشد، این اتفاق خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/alonews/144622" target="_blank">📅 00:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hei19E8xHox9DU9Nu7fP-r8ggo0AjjpdHRaNQVfBjD3rAkzWPH3my1a-u9aNRo7A6Aq74qK_YfV_gDyiqATGoI8j6clFFlkFjL-BHmITiM3_zmVglC1GMQb1jEjULFgxhfRQV6PfDD2GKGarwIOm6eey6D8pyUk_E-M_BZxt0_hPWyhR-1vLEFbjiEPQB22EULJMHU5e3k0dwTdqmm6bn4bRhLwjDHNbCMSveT8mOSVda7wmUkmcA2rGK0bWLufJpcHqcd4-LdfT_38kmgLjF3KmnUDtr-6tbKtvQ_spQA-GX_ktn7n-kjbfcTAgpEMtfmoJOttVo9tVCHQc5z1vOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محل حمله امشب آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/alonews/144621" target="_blank">📅 00:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFKXSPMpq9kNHjRlWztOx6OhVUSJf0PgSbrBpTgZZYhWKSG_MpN9tyUVAOXcv5D-OXhT4z_lwiUntwrVfqLs5vdvVMOdBw5IkHjE1H5Z6J20HmbB8SaVHa1hzmAy943HBp3DBPXRgLwVdzy6L9CwDRF1h0p7Xf-Wun-P2xBwfUmaPqun5jK08IeVfLP_wzkcNRa3hXbGagA5yNGnEIMnU_ZIWu_qi5funR7XRTQPWAGddylskSiF6l_05MCkCqxbcuMxtq8MLKVf5YWo3SyZDpPSEtvBOap2-im_-AiabBxDH_imnZNStMYFjUPIDNEKWunXwkrSaw5Hb0N5WJZFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سپاه: دشمن در هر دو عرصه اقتصادی و نظامی، تبعات این محاسبه غلط را خواهد پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/144620" target="_blank">📅 00:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری / صدای انفجار مجدد در لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/144619" target="_blank">📅 00:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
حملات متعدد اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/144618" target="_blank">📅 23:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144617">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9vRmTWLO0pWchPGdsR02y3tM_VmSSMQqxPsiYR6JcWOLCv8BTvn5E8MbDMPPNXVop5cw8Y8_5PGUfZUm9m-p7ks3_ML1cnQJ01ZIfUluRusXG0dMYAWLsHJ1VAuwceXo0j-qUw6JOYWIYgx7CcG8C2pXIBjFz4dwfDUkrWB1koqjbgALO_WW2XTYzUjtIUr79L6qlu2UfmxzQOt4PJEMMLPEWnSco1SEO1xKApVrQdKXz_-7jc12jmyy4avsyfDrviOKsqbmCi5_myF3ndce1sWq91Datb3Dpa7U3olfMf1bZrZggEzMIOrcEhBEZnnohVc58QRlaXt_LztE1qQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قهلکی: پیام عاصم منیر به تهران چندان دوستانه نبوده است و خواستار انعطاف تهران شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/144617" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144616">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S6-rtz4foT_I2vc1qQMOqYmaZO4F5Lt0UUtlSxirYJd_2Okpgr-_2MHXChf4GtZZw8WRt1jD6rl4i8uKKhjACu5yx4wZoUkLzcpdApAwl0r2g1jjJPlJQntPLbkkoICewUI-I0UOtb5oYmZ5_kmy8aO7GxWO2sS2ZmO8ZtJNtSo-kmyq7NnpMHrE5b82EE8irQNXJXCmWb8g3yPbUNa2bvkMp3c68af1XrY89k872vxCgzAyg07hi7prf9l-lV55siK2-ilREq3BEG6BKhzO-wF1GhH-i9w-QMAH0wGpUMhCSvd-pU_TfQKatMuqKM6LtvUh44D15pRYjOsBjwdjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان ایران و منطقه هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/144616" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/144615" target="_blank">📅 23:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144614">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/144614" target="_blank">📅 23:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
گزارش افت شدید سرعت اینترنت، در سراسر کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/144613" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سپاه : تنبیهشون میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/144612" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / آکسیوس: ایران در حال آماده‌سازی برای پرتاب راکت‌های حامل مین‌های دریایی به داخل تنگه هرمز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/144611" target="_blank">📅 23:21 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
