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
<img src="https://cdn4.telesco.pe/file/ZbDf6Po7P_q4vOrRIKPTF6b16ZCOrFpetnwrX8K5Xcqz3sjKCMfnucu9i6ccHjCdHhP9KEAlyOH29SzdSIeHiDswZ8gJvAX0ylYS4BGtalRtzZByw9o6FF22Prv6ESxEoEuj0FBnTeeAUTDl4UoUu4PVK4uq7zxaojcDIhiQFcaoWf8j6UaADy1lOgQkfGlXi9XTvbW8HBw4FA5-V4AXsVNPv_70Z4VdYEGcqCeiOV-9oLt8wU5myebUpsJb7mGsekGH94VDz6Y9BZ1YFqeK1U1bTsmlMsvl-dVqDTYec997YeBNiP6WO__4w5vlbUV22D6rUqZYPo1P_asdu3bAHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 23:11:38</div>
<hr>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=mrAblCHYrp_SqWLpBDP_ja-Ktfx7Vx30FctepiU3erWsOxJRsLRa00veWTl1AEuVWWh8KJqWUeGhOBnx0gI0yBOg0uPna0xfZ13L1YSzwI659PdzOBHhxWCViY77lHaJxrkqJFxGAu5YAJ44yyUqSThpPKokFF97iL29GDu8YHnJqT0h-qB5uKugUU73aHjxlbNCH1mlHwgKyptjeHCzKzSx6ng7mRhBQa9MQj2uJPWOG3ukQiVPSr3Xp5sopOgSCfR--qet3EUFgdd12amTthfyYeDncVqEyGdcpc2_pbfcqDophdFaAReMf-dJcfibtRWeHOYrlvq_YFyHk8wR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=mrAblCHYrp_SqWLpBDP_ja-Ktfx7Vx30FctepiU3erWsOxJRsLRa00veWTl1AEuVWWh8KJqWUeGhOBnx0gI0yBOg0uPna0xfZ13L1YSzwI659PdzOBHhxWCViY77lHaJxrkqJFxGAu5YAJ44yyUqSThpPKokFF97iL29GDu8YHnJqT0h-qB5uKugUU73aHjxlbNCH1mlHwgKyptjeHCzKzSx6ng7mRhBQa9MQj2uJPWOG3ukQiVPSr3Xp5sopOgSCfR--qet3EUFgdd12amTthfyYeDncVqEyGdcpc2_pbfcqDophdFaAReMf-dJcfibtRWeHOYrlvq_YFyHk8wR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyyVlmJG74CKlMntWMX7ZraUR3GD6VmY5hcZh-9S7DYETEuqWQrRjpTxwAMSGomkWbHAmpklnRWrG-G4JTGlmRaF3h-xcVbVChQR-E1keC7r2FFvvzRk9CTYWLTNHel_Flek4jOCRTLWD9GjOdRTVxmyPGzO-fD3F2K3xvtXvL1jRCCpisvShwpfAWYy4sEE6n4E8pkmGF0fnAV7XSECEJczDa2CF0-iiuDP0FxTzNmcYIDZw-otsJ29RFkKOd7dLVDeCDSwgC1U2SYLR-PJPjXz4m9tWQTHzVnwPqpR0gRh-9ivt8-k3EehUbiKhO4Vl5rPtDiAS4Hrhr_LlJpWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD4-s48PNZfajDaoMQXPn4bzSGOt-7nOlg37PSG33KtczHIn6eWh-UlfH4A3G2tWWRI8iXO4rY62sd24V7wfsKVz_X3DkaPI_GvKhJf8EWeQ8c8YiWhGLB89OkdEeLgBxFW4mDCDIUVsBb_bWXTURcpqww6nPmVs5ms-DSX5_9-QmOqnF3KMSZ8CWr3dvxcPMBNlDrnteHNcGFi6QnrA3U5r87yqyX0R4N4cHa_Wm2pe1n-f5V8_JBxcidAIU1h50jHKvh9sAX9NK3KJYXOSy70AHnjiM0TTy3imhsuLwPH6FEIM9_kJsDwzp2GI6zYOPrIsxOviQp2gaM00oK_qPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده: @wizard_0061
📲
همین الان عضو چنل شو: @v2ray_configw</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/funhiphop/82243" target="_blank">📅 21:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTlw6r67hQWRHPY4MG8vjzqx8tiQ0LSWRYtqdMOLRaMNYv28MzASXSVoNEU6kaWlnfQLPtumiA_N0SsryTvSgUKZs_ZT4b804TEOFCnkQJPhY4hgLyPuaWwZ2c_HdPb4RvaiR7ZNAU6GCw-2uX2AxK7gQYGvLvqqqPzejvLqEKAmSpZZgKHXqg4oweWGHiAdQO5xQlP5lkkXVNoltYJN-bD-0isrr5T4TGysKXXJUWmdzurLaEF3Gpyp__diqEwvM3phpZFg0F5dVUf5ik3mdN8zNfwGP7AYDQvuJvZIYejdDRfpmc0Zgkwu_ONnoxEaMhtYtCYD0zI7x6YKFQGTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده:
@wizard_0061
📲
همین الان عضو چنل شو:
@v2ray_configw</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/82241" target="_blank">📅 21:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms5hIJh5BfuEQD2ZkxkRkC3YmRXE3Zm5hMzbJkLhINdpy1ewTUtEnRtjLYvuJoV2XvBHzydHl6mF17Ps6MlnMBfeg8-yVIFBXDrnPKG1SKhDJ8MjD_VedulKLEvIxiq6Ja8j93MCvtIyTOsYk-u70MgoD2EdfLOifMgWMTSQEtOoJRXsRWYQ-BZ4zkLbz4GQULSboYa5vG90vr715k_8ILKP5V42aqgYPre5BP4OdmDrkd4IM33QDmDbtEKh7kDfe-wJDnqWvBoK2ZgCUqQh0A6zeaN86RoP-VxMWTU64R19nrP1B_-EqbtPP7tpc6zOU_IeR-8xSH6l-faxEObsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQ1yYP_R_OCiEDr-viUip_yaonnjQg5G3h-3dnSBV4QBp3B4VypUtiZPjYpm31TB1wrDpz7vTlQ5DKgMHhIMgA60QFeowSbFmsZVWrHnxvBZIxPMzndVdIwng9KgaaFdx_CyxAKM5q9WWPbZB5sjqZj9_0rXrco1oQvuxlQ1zUu_Uf6AtG7yGSuTPUp8ZLMCd0ObHxIXmdWa8zA9QHxKbDmzdYiZITcG4kOAzCddbOK-Q5N-_sgW1pxGSd9vI9dYnn6y3YnVM-HwYNz1jaxrGIvcbEVRR7Z40oUVZDUz_E0QhCnwN59J1JKHjvQTSZGjn6r3rxM28RRywFSQxIt1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL0KsV2WmhfkyaWtsRyZ8F-jTV52d8HakbMmAVoFX3Gpx-AY2s47kPVnqjC2yCVLRzEKnU-phYaab-eqMvBfxKK7fY6zidXOEFSHy77WOq48EMqwy_JS_htaHQJP8vP8DAvl475qtDnpjqS74QwmyN5BwS-j-u4K_k2S0K06OCm_rVjuoWbYP_MYcGd6b3_EvVBiBKWhtA4FXdmzCrRGBW9dUfwRDVJOjpmfgScOPnryp7YVkP2XRhrDQfAQKxKA6bW5TktDztPka7PNfBlt1Ooxu30h3hvuxRnJTBNHHouhnAel-bZyxa--pvIj6OyuA6dzBZQmnkLURVCrRdMQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O30yCNCFNjSJKJtPSEvzTVNxTgoPFVeKhrULIpXUpFYxTsUlVNn-I53atTWK3T6S3gwvC3aHX_BaKDuBeVrPNeBbPEuG3hHBBYmAZ2d4frZR466MyTXce_mcEso7hselPXF4io1cYHK8SEgdecZxWVynrtFi5X4rMO7VaWvFmQ4XKs4YGPECRp1P9jvX9tG3O3CN1Xd_YqX2_0DZJIfzMNnNikltUlENpTkWxeuRJDRFi9Vo5aDyaTOtiiFqDcqn2KlR5FcWP8AvGol_zVLxK_xTNqQs9-YH3uTs2AnYBRWK8uewIYA29ICAJ9SPwUh6zCcdLlrIa_9C7r_ZyhO5kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLGWRlbx33hWduWa3AVZcMFO5XtyuXoYMx_0p8K3FHYysJI5_Pzy1ZYbAEPjXrEcHFJaMVZ6e8YE51MCNuG2jDSxQCVr0hAtrEzOWviElC68hjA-XdyUVLGP26dH0gq6x2NvUYZX0M8VFdTr50otsuxHFJNnVj0YNVfhNPk2HdGquKism8PMPYDvuLeDwn5v0J1FxlRudO3RbgmXrP3JTaI-BrGoVC8wsFuokDiDjm1MoB6dD9q29rBksaOqi0sNrBZXjMyQLRkgHqdwUhlS38ePNPHkni9ZzU79phwFtX0_KG49psEWuLUkIQRqqNvXjjmkSAg3rppRT5KlcmbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=ixYHTc7XimXwAzxjf5J5_A29Ef8b3MoMq3EI6QTbRsZ_coUQJ7Zhkf1xmjfwJkmdw1emcDyyZgL9Jc3QywTchqpQ_d6WTfou_Bl_z323h6m5QHdIKyTjMwl09vl5b28nAj9jorr18aQ4sZ0WCQ9mCPRss60hT6owkPHJzZ0VjrP6Jo65mgmuTCjVONFEvQibRlkZlly-cbMofTfeFDgXfMWFKI2zf_OzM5neOusJCG4aAgI5X-kpoXZiTdeAKgmxs0j6IBtxkNkaGfiYsdCS6nUkdG4Ya1041uJF6OXul9cBMseHDuIPEsn_Xd-Kfn3W4_2fBT3-DdZlx-lzZGPBvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=ixYHTc7XimXwAzxjf5J5_A29Ef8b3MoMq3EI6QTbRsZ_coUQJ7Zhkf1xmjfwJkmdw1emcDyyZgL9Jc3QywTchqpQ_d6WTfou_Bl_z323h6m5QHdIKyTjMwl09vl5b28nAj9jorr18aQ4sZ0WCQ9mCPRss60hT6owkPHJzZ0VjrP6Jo65mgmuTCjVONFEvQibRlkZlly-cbMofTfeFDgXfMWFKI2zf_OzM5neOusJCG4aAgI5X-kpoXZiTdeAKgmxs0j6IBtxkNkaGfiYsdCS6nUkdG4Ya1041uJF6OXul9cBMseHDuIPEsn_Xd-Kfn3W4_2fBT3-DdZlx-lzZGPBvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم دیشب یکی از هوادارای استقلال داشت مصاحبه می‌کرد که یهو رفیقش جلو دوربین انگشتش کرد
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UadAzCBeGkfcIZJUAHy9VR_Rlc60w1wBzFdh4iMS7CyemJdhQRZYNvfEJ_ZoiSvLk0wsoLMIss2sFTYLlTH2VW_5JlGPzIWtl8pGPxbsAnmfX0waRH1fGPi2YQEE5fXmSN1OoePdzJC8oQ72UO8syVNNosRDQTUXtgHRYWzWCoGR9Z7L5em5VtLE1efkY5LWmkKqubeXtef980z0coLJflBaZ-w0NG631LqNuJi3pzV5BVVz3hqeyVtU1h7g2wia0_JVfYKGUkb4g-kgol1gccmjCaLbGHU70egqqYBknYY_OXC0n7-QDivSC4mDAuxII48nDSXW4SIalHGE96du0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82232" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb0YNSt47KvBh2c4LHwjO1xxyM6YfYw1AzTA8N_szDRjBSh6UScCFqC9jfKua9SQivF0q2Mh4RkLHAv3zJrrbzgNzOCm6t5NiwSxW3ltMEo14CNDMMRjVHIhd5Jcw8vhTmJrzCNUPTh69Hf4fRWHctDfSn1F4jKU-KqsLNCDk6KwXfwM8TJobzF01UeN1GwNtRfJLF7UAhvHNna2ucQZZXG11kz5HRPCQ1rUQrh4iW4DJiaJRkeq9Cshun79ZJi48g9NtkdDyZcIRLk5y0I5i4rMTMNBZlW5DfsIFWaJeL-p78wAsKYj_MlElW9EoUytIhcETC-ZvO95KRI-dJ8QAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
