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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 22:23:19</div>
<hr>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyyVlmJG74CKlMntWMX7ZraUR3GD6VmY5hcZh-9S7DYETEuqWQrRjpTxwAMSGomkWbHAmpklnRWrG-G4JTGlmRaF3h-xcVbVChQR-E1keC7r2FFvvzRk9CTYWLTNHel_Flek4jOCRTLWD9GjOdRTVxmyPGzO-fD3F2K3xvtXvL1jRCCpisvShwpfAWYy4sEE6n4E8pkmGF0fnAV7XSECEJczDa2CF0-iiuDP0FxTzNmcYIDZw-otsJ29RFkKOd7dLVDeCDSwgC1U2SYLR-PJPjXz4m9tWQTHzVnwPqpR0gRh-9ivt8-k3EehUbiKhO4Vl5rPtDiAS4Hrhr_LlJpWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD4-s48PNZfajDaoMQXPn4bzSGOt-7nOlg37PSG33KtczHIn6eWh-UlfH4A3G2tWWRI8iXO4rY62sd24V7wfsKVz_X3DkaPI_GvKhJf8EWeQ8c8YiWhGLB89OkdEeLgBxFW4mDCDIUVsBb_bWXTURcpqww6nPmVs5ms-DSX5_9-QmOqnF3KMSZ8CWr3dvxcPMBNlDrnteHNcGFi6QnrA3U5r87yqyX0R4N4cHa_Wm2pe1n-f5V8_JBxcidAIU1h50jHKvh9sAX9NK3KJYXOSy70AHnjiM0TTy3imhsuLwPH6FEIM9_kJsDwzp2GI6zYOPrIsxOviQp2gaM00oK_qPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/82243" target="_blank">📅 21:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/82241" target="_blank">📅 21:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms5hIJh5BfuEQD2ZkxkRkC3YmRXE3Zm5hMzbJkLhINdpy1ewTUtEnRtjLYvuJoV2XvBHzydHl6mF17Ps6MlnMBfeg8-yVIFBXDrnPKG1SKhDJ8MjD_VedulKLEvIxiq6Ja8j93MCvtIyTOsYk-u70MgoD2EdfLOifMgWMTSQEtOoJRXsRWYQ-BZ4zkLbz4GQULSboYa5vG90vr715k_8ILKP5V42aqgYPre5BP4OdmDrkd4IM33QDmDbtEKh7kDfe-wJDnqWvBoK2ZgCUqQh0A6zeaN86RoP-VxMWTU64R19nrP1B_-EqbtPP7tpc6zOU_IeR-8xSH6l-faxEObsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLGWRlbx33hWduWa3AVZcMFO5XtyuXoYMx_0p8K3FHYysJI5_Pzy1ZYbAEPjXrEcHFJaMVZ6e8YE51MCNuG2jDSxQCVr0hAtrEzOWviElC68hjA-XdyUVLGP26dH0gq6x2NvUYZX0M8VFdTr50otsuxHFJNnVj0YNVfhNPk2HdGquKism8PMPYDvuLeDwn5v0J1FxlRudO3RbgmXrP3JTaI-BrGoVC8wsFuokDiDjm1MoB6dD9q29rBksaOqi0sNrBZXjMyQLRkgHqdwUhlS38ePNPHkni9ZzU79phwFtX0_KG49psEWuLUkIQRqqNvXjjmkSAg3rppRT5KlcmbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82232" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb0YNSt47KvBh2c4LHwjO1xxyM6YfYw1AzTA8N_szDRjBSh6UScCFqC9jfKua9SQivF0q2Mh4RkLHAv3zJrrbzgNzOCm6t5NiwSxW3ltMEo14CNDMMRjVHIhd5Jcw8vhTmJrzCNUPTh69Hf4fRWHctDfSn1F4jKU-KqsLNCDk6KwXfwM8TJobzF01UeN1GwNtRfJLF7UAhvHNna2ucQZZXG11kz5HRPCQ1rUQrh4iW4DJiaJRkeq9Cshun79ZJi48g9NtkdDyZcIRLk5y0I5i4rMTMNBZlW5DfsIFWaJeL-p78wAsKYj_MlElW9EoUytIhcETC-ZvO95KRI-dJ8QAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=G5GBgwextO1uKyFoIfnZPjMGuXby1FJHDsOkj36g3qCWUZ5b-NrcyI9QeB0rW3CHEYs9OX7miYhC7FXpq0I55vV1h9IqlaKfNpcC-grz2phZ2kStHkorHohgNQso0iSrq0ss6NUeh-T0KmjNIvW-pJgJ-ZpJSSEiWmmh5LiQOsrhgCCwXzua33diunVgK-rbj2m_SOINYx6FznUPRK09gIZL1KeyY5ScOOGLFxF2BwGCD9r2TMAKHtQhw6jard_epSAZhWnwoKbUEK5fk-f_qkuJup4JWRLdZXwtwRHRoiUvViFUoZEANSiEslBMfJ5CcDzFhsaMTvS_YJMhlMRhAg0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=G5GBgwextO1uKyFoIfnZPjMGuXby1FJHDsOkj36g3qCWUZ5b-NrcyI9QeB0rW3CHEYs9OX7miYhC7FXpq0I55vV1h9IqlaKfNpcC-grz2phZ2kStHkorHohgNQso0iSrq0ss6NUeh-T0KmjNIvW-pJgJ-ZpJSSEiWmmh5LiQOsrhgCCwXzua33diunVgK-rbj2m_SOINYx6FznUPRK09gIZL1KeyY5ScOOGLFxF2BwGCD9r2TMAKHtQhw6jard_epSAZhWnwoKbUEK5fk-f_qkuJup4JWRLdZXwtwRHRoiUvViFUoZEANSiEslBMfJ5CcDzFhsaMTvS_YJMhlMRhAg0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=QU8qPhdLw-5gqg-7DkUOc7y-uPGMeXJJBdLnwzM2BFbdX28y1aqPm_rbwJSyPo_h7CJq-rrK6ZmCV0-si33FfwSjQEjHL_d4STskKbeaVPCOJijhdn4oE5WkkRY3Znj3LpVaHPKoAJguIOLq9T1jsCQZpe-aE5rhTCl9PhJEbBxDM3H5lK8vg3l_cKSo1tTSknzJsnhV7oV8K5sFzAa0BcMCQD2aSdaEt_VYq1RcbGbtVy5z_lnHJCnqYPv35_prCXUQa_sIDBztUOtnO8k3Q1UKjjDNd-9MBbm6aA8LF8AT6DpLG8BzYRR2nMuv0rHOt81zAxOCUo1b6_kmPFNsTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=QU8qPhdLw-5gqg-7DkUOc7y-uPGMeXJJBdLnwzM2BFbdX28y1aqPm_rbwJSyPo_h7CJq-rrK6ZmCV0-si33FfwSjQEjHL_d4STskKbeaVPCOJijhdn4oE5WkkRY3Znj3LpVaHPKoAJguIOLq9T1jsCQZpe-aE5rhTCl9PhJEbBxDM3H5lK8vg3l_cKSo1tTSknzJsnhV7oV8K5sFzAa0BcMCQD2aSdaEt_VYq1RcbGbtVy5z_lnHJCnqYPv35_prCXUQa_sIDBztUOtnO8k3Q1UKjjDNd-9MBbm6aA8LF8AT6DpLG8BzYRR2nMuv0rHOt81zAxOCUo1b6_kmPFNsTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مامان ددان تو اینستا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=c0weBtP-aEVHsOK73HObaoT0BA3Mx6Pe3XdqMXY6V2d2g3TKSxoXcw-6oCQ0mTLtogqtL4V7kp7QVhQxBitOkWLkLe_S3uZL_UQrbxlDE2kYONDPtOYQMh4IsjSIh-EjijIupcjtnYigTNKBGW5Hi5kwvUI_QksXGuRGtsOZSomOzJkdzAv-Rn8QtH5g1YKTTOqIzIdgLnpZtEWxs_mv_4ob76pSUvSFIrtMHxwua08V1ufX3QiWCvXqnjAWgFjaMYn8RVOHatqo-YS7eWx3_UVwV4ci8z-4KWIulZqjypyJpI4w7L0WsJTRHw2UFgSxJ6m3VL7SPt4KRrDdBagjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=c0weBtP-aEVHsOK73HObaoT0BA3Mx6Pe3XdqMXY6V2d2g3TKSxoXcw-6oCQ0mTLtogqtL4V7kp7QVhQxBitOkWLkLe_S3uZL_UQrbxlDE2kYONDPtOYQMh4IsjSIh-EjijIupcjtnYigTNKBGW5Hi5kwvUI_QksXGuRGtsOZSomOzJkdzAv-Rn8QtH5g1YKTTOqIzIdgLnpZtEWxs_mv_4ob76pSUvSFIrtMHxwua08V1ufX3QiWCvXqnjAWgFjaMYn8RVOHatqo-YS7eWx3_UVwV4ci8z-4KWIulZqjypyJpI4w7L0WsJTRHw2UFgSxJ6m3VL7SPt4KRrDdBagjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فیلم Avengers: DoomsDay منتشر شد
۴ ماه مونده تا انتشار خود فیلم، این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-9EWCSyykywg3pSs8q0H8q-ffERskTaIZw6tdTiEHx7OhcT2q7hPLzaZab3gaCet7J-8T-UgrAJ8HkLARgWtai0is-2LBjfR_t8pB33XiIt1rDc3VvdGmJWg0HAEwF8oFvwfeFwEaaWqaYNejzXPrYoeIgEmjdTDOeJX9fIUKFCBa6j4-V53KKYxdJ6Q_wxUNqcSL0KUGVvWby8huBO7EvKdJ6gyZyrLEXZ8LTwSel8WndhHCm0FYEu3DIGb-mdPps5fuwgyyYXIZhvYVsPIWR9NfjWquS47KRoUu3mtekXazXtIxYvvGaOvQHKHbpojNPhSztEHUrkGIZP6pF4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuhqH011PJVDeetbPGZFGzTb4ZNDgydtVF0P6vA_QIkadgfh2KB08JFjnqCicCIqG_Qpl0eR7NshC50ZWspXoD1nCBdVuT_kSuScfDSAWg8nyN5j4vKEj8DBYkwGWqIKg0U05YkXyTYu6AAT71UhJEU6ruaJg52EOIkaBtgQh8YkqrlrF0hxRg3vA6NStTF5NwLuj4hrnoKviwpeOAixxktkiW2456s0IsD00b-HrtLcT72PaG9V5B-QwxPnXnpD3J2HjeNb-xTNUXhaFS788Y2AqhubMXFg2r-ONrZzu616Ye1vIurqXpTt1Pba4BLHR5_sv2tx2k-gGGq5MSyfgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82221" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMmWtuun0SoZXYCmXstMsltBodhWjznqpa4KPv8uLcH-41_uGZ_QAM3KRMTpuirBtObAXqEtFxV65po07rZN9V_1QxOOhxH7CagqTU65F_Gji3-P3PlzDaxwByztNOrsfk6Y3c29YSxPkQ2HRt2al5OujxZ3Syaw8kvXGB8l9N4QQUtYnF5Rt5z2n5CehVtCY1dVCyal5_y0th9rvvkRDIq04o-3ubZTyjUHpEHJ97WVMF2UwGqYtou93SK8ST2fSxQ4oGbxcr0tWjqucriYmYp2huBn99lLrDr5zrAmFohJpKQL-npYevd8l7vAsHtJR99m5xdnKwXK13hsD_x7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etzHVXCoIcFj2ipBSL6r-AXicXrGpBZJlLZjdRhB9k1tLpmTOBHtjkoMldGksJSv5JWWjboc-pxKn7md8EA-YjCLcYVxO-3GjjzrSJBzZ2g_UdrNepVLvfrB7viuw0ZeFQ6p9xsRQdLpKEI570vt6vdTAH9km3od3pzFZP2YIj2gMtzB41bbxKfPOvMzBOX597sLWdIC4JeNkzDOMioqPzAE_ZItblxw0kvEy1dUFtfjLEJtvp9elRV3dfjXN2e33nEMn92dvA7Cusk7WqpHcLqiZpvzLZbM_C7fYRifGfZhyY7IkHT-y3nyeQee0tpYTYRnM04En0-fXYvhdfsV9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEclWlKC4QlO9C_TPF0hKCGwtQwtMCrG87USiskgTva1bM0F1YU58kkeH80y05vu632R2JTBoghdvjEO4rUTWONp8oYPLmyaml5fMibQtoizDADFCfBNO64fHPQWeBdtLlT4DEODF-WREv-gxW5lhgsaRGoYMXNrL6UURjCJSlNJvi2eSBK1GVdJ2TpChycnsw_7WOOGeP7HPdad7lwlF9KMxYF23_EbUf7SExJDWWNUB2X1vcFHO72fGWpoNCOql7UTR-Gj8Nj7UnbYdhrVu4MV6Wx6F4jNbLE52oZCZu6XmsgjwU_kwuYRjqiqv6eWTnm1y8QSYGQ4Ylc8BWLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNu6FapxuJf0YmPr9qmHyK-FjWoaDmcLsfYqTRyIlp_5_q_yMzmxgkmz4EMBd-FWStqkTRRs-ov8ls1OilpxuAps2V4GhUYtKOlkiyog3wePygL-eaN7-wvqoSpSGFrWjRGZfKE48dIgl6vNRZmKKbfb-Yclef7rRoFk4HQSRCPUGAb9jrXpYWDgT2HteAUg4UR9KmkJsxyNyTNI-0nXp3xZvwgHgBYx8-R9DPDyBmg7levZLmSkmSfx8KER-PLFzmjwNypUFgpvTWcjyRdNaNJ-DrWPGXnw_olgXuZeLPnmuAFp0ruQEpIKt7gvEiI9WQXkUiExTb9ImpF_nXI5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFHWw4sUBxLtFd03Tz9OHizBY4SMKZhNxunO0is5ymE6eIeh9UyMEKM9_SxvAZQ8PO8VScHMgzhUEmUrFy1mjTDRGcEi2MRQw1uGV9KP9_iJJeRqKEpJ_g8jkBGqb67MeATY3-SDCyIDJIrmZUnXg1AOjwY7tS9rAONLLw5xCGfdAPMmhlzaCDwQB7xR5iDMtXH-T04TjBI9NQs2n-5C77MKhAZAjQHMJVVfFs-Oq7ifl6GvLWQh6898U3oLuJ29v4tZy4M5H4kfcisUs6gsV6BPbFEnQU1yZbA72aehQycqEK4HmYLIzyi0D1rJnWDrxCb7XcI2VeU0p35NzwPDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbqNRIUjRB9ZUsc5s6RfoP6RWUCYrdNz4BmwNu8-q3OdV79H9-QUzpWRlcQcfed56bHIqCvoxZGJHXYMx5pvwH5uq_KaAeJOspjJm9l6PtDY5_FddeitJriG-2qtsewsn6jE9iXwII0k7JRLNhHFyuLciWWF1uSp-r-usxYJuukoPrYz5GhCiEPq_nN0ZF1VEwrmlAlvjr-sKY-YdlIlD-Xtvxna114Z7WRIvOuimcqnvjbFpANYdR3uxp7eQcVyCl9Cpg84EdDN2xQPrp_ZkGtj7oZmjywtx01gbgIyAGUSLrsbpnLqEE0C8vERIo2zI2SsusqGPhqYct5H3Kn0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=Aovg5J57a4BlzHceef_DGVzhLlczI-aGnBttIh-AJmTqN44gO0Qc0ksKgtpP3AMo3Juqur6cUDtqEKZd0NejD-xt5O8uk3K9xmGnmt1MKFPQa78aKX5IXmTiyzX2PfJ_R8kpsQKCJK1w7OHttWz7pQSnaGbSBFRauBwTfYTvc_inYAAFZe2Y7rzSrT31oS3HeS-E5U1xRx5FJniTFK5_HEns0wkGsvmj3_XphpJ8ej4jyX2bp3JQ_NXMK9G5GmCyUn5ua4fi1b03MTo-hwf5mytIHZB0OrivMDJ21Bdf3QzcCc7ZtiLkfdk6Z5rxYGmIy9GPFpEuq31l9e__Uiz_CHb3gvNVj3Uh6GxGdMN0mvLMiqtXI2FJMeGnU8M2CDTXzgV4xfPVKID2_UqPMR1HWpV16sPBw7k0I-X_eTdZ66xJvVCCW_CIq3y9gWeji8LIgYJoJkiY0qmjBW8nrsQ4Zh58qHBQcztkyCuomVPpOsGixLZjhCuEBxQ8xJO1LJ40Xad-VO07aEStUn0-P-OgTzS_4Bkfmba3TR7Ne8Gs-l5Q0AbSJ4ntDnGRisvjB98MpGTjm95wfyekK4_r4XGcP8uma4JhQBilBnIojL9KA4RvWd1KgZRzsQzJWUfPbjMMYNehji4lbpO0sKvzbeCZ-XwSTUTa8Bg3S_QuBCvnSmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=Aovg5J57a4BlzHceef_DGVzhLlczI-aGnBttIh-AJmTqN44gO0Qc0ksKgtpP3AMo3Juqur6cUDtqEKZd0NejD-xt5O8uk3K9xmGnmt1MKFPQa78aKX5IXmTiyzX2PfJ_R8kpsQKCJK1w7OHttWz7pQSnaGbSBFRauBwTfYTvc_inYAAFZe2Y7rzSrT31oS3HeS-E5U1xRx5FJniTFK5_HEns0wkGsvmj3_XphpJ8ej4jyX2bp3JQ_NXMK9G5GmCyUn5ua4fi1b03MTo-hwf5mytIHZB0OrivMDJ21Bdf3QzcCc7ZtiLkfdk6Z5rxYGmIy9GPFpEuq31l9e__Uiz_CHb3gvNVj3Uh6GxGdMN0mvLMiqtXI2FJMeGnU8M2CDTXzgV4xfPVKID2_UqPMR1HWpV16sPBw7k0I-X_eTdZ66xJvVCCW_CIq3y9gWeji8LIgYJoJkiY0qmjBW8nrsQ4Zh58qHBQcztkyCuomVPpOsGixLZjhCuEBxQ8xJO1LJ40Xad-VO07aEStUn0-P-OgTzS_4Bkfmba3TR7Ne8Gs-l5Q0AbSJ4ntDnGRisvjB98MpGTjm95wfyekK4_r4XGcP8uma4JhQBilBnIojL9KA4RvWd1KgZRzsQzJWUfPbjMMYNehji4lbpO0sKvzbeCZ-XwSTUTa8Bg3S_QuBCvnSmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فصل دوم سریال Mobland که ۲۷ شهریور منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_K8asz2uXHxYUNHQp-HsnYjXodkpP42Hs_TibLZQQiIewFOdrPuwEyqxaB2ck3t3rZL_X-zWIDBPgb60fTPDyoTAk4jE8keiVNdFhDZDXSXk2e-VZ8K5FyPfIlOtLVqfH9TIKxOa__K-HGeKH3-pZa6Be_qGdB21amrSt_3ob6g1GZY2CseBhoo9pTxIlFAgULp6LyZd-qm_ZXsnozGz0SNjl-vzcewGkfFc3RfeuQQfHnaSLPivHqVIjstIbmkhrg-z9c5c9yNxDpvrnv5b2p7I9sMm7YBhMgzfUdTc-rUNcWONFdwxO6D-Z0pG1WC3GEtu85gDY1gvcNIlgCH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKEAg3pZjXxn3v5M4Ck7YZDJhXy92vTJfFy9tYKh9Srerp69A_TWklYCvyFtTe1tWqAAm6csmq7L1e6IwtKiHPun7Rr2ZJ5ZgVdCp10tEVyrjibL_M40PSpQ2obJai2GafPGJ-UhhK3oJBGALtIxyWT_ExntrHZwzAOv8X9_Q6mBKC5lHvvIOV_zmtDgi7UONPiGmpgxMskh6FY85yh4QoZ4vnnekmHF35wthEq0HjvdLvCzP4B0EMqpXO_t0JaRNR-7xDg_SvzbiwJe0oRo0-IhHt5jEGxXd2nVMQEYzryKKP2XH4HH7zGkPLsfMvgYiTZgYQAh908izMt8M0QfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj1I-dojd74vLI0-ZveOfSp_3S6K0EV-DZvW-HWs9kMcQBNLW10v5PGeeErZXcvHfycLGPhwd6tp2HUxzpY56dx1M2y85kizL90yfbCbZKGaGLyuYpAH7tU9nRKeCOcf0PLeaiXJaVyJPMED3fnYcfXw66oKrFLDzVNRsAlQftGCDKYDzfwcw7xK0mDjWMWmTEAHfIerlw9e5uHWO19RuBeuKisXV1fWfQuGTRXBly-i77qbcOgAsZJaPiyg8QWjz5e82CIq2Oif1SiRZNVCdj4KlZvqKVy9QRPfqKXHCRaLrORLDZ2zTcd3FDAo7YNiInkl6U7nT2acN2osyW3hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmCBvsXOGLNAQQz8ab0HN1zEsKDQpH4-4tZECzptxf6BLYAkJi5E9il4yrjfMaZHe4cQiR8nLUFs3MpUJYD5_e30Ty6v3FBM7bZB-OdT3rveHdgpnm4SnovPkyHz3gZE5UfDe3pUqI1sEZFain3nfOGvuaViqXvTx-rRl6SJ3ZIZsAvRjEEl_Nppp9N7jHG73OvaMndG9VqNS8cOuvBXK6HTEOIJuWhx4TGlqHikJpINzOvTm9HofyoS6QH0fiPc9hJ1S40QCi9DewhP1_CqCfw8UeMMW0WKGB6u5XjP-G2Xocpb7Bo9m-2uoGIihroMUVvM5QCTNauxJ06e2OVstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMiRk4zqajUwVpr35fRkypnuxrH2insJUPWUyfOk2toICUGBMOAPFQYl6M1S40ACJ-ukMXlZx9NP_NIEbXERINxFk_l_YAkbZ-0VCDsybIZEVgBMv_DSo1VESR4riXIJy0Mv84GFX33jQkUTQ2ytGDzSOBjpoyZWgkd9A8AqD_RGFzPrpktly_OVJcRSULNUzrmeHY-z7tatkDrRDmhCj-mW2hN89mYA-RQ6DEX4oKnVKxRAlTKIE16M1Bx2ESgMzVtO2dO-tjkOcQ-QjcyHUAsZxT7VbzNZVHUqAi9fJFmuWzAnnFshg05I7fp0Y7ubzCxp2e6aXpNPjwvRKQbziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
21
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82202" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atIjfNK8JdQbmYBdU84FNTLotCXuv5nBA9cGep-JicvSmHY9lOlzByNKjceycoILMRqYI_VVM38YywRIfTFM19ossZS8ktaQznQTLspHIxZFZK2MxjBDskyOJv6KBqSWUrVakD1Sl0XlZkZuMYuPikysq_73TQyZTuHMZ8lhubVkbE-o5tYshvjUlcick8GhG35evp5rgM49Ir9fX2tRXcNrs6k_MonpFkqq3_j-nWoKtJ77atLZk2_fOcWyyHM5-cCPVEEBpRNT_uKE6-OoJeHOO468J6W72y64N9_3MawO7_vHUbGH1SEuCqIuXuDSBRgrBFbUfircZxVdFPAlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nr2JC_ejLyrtuvkqBGoZ-8ug10HjLiiqF0MyIgKW7SgNVJN4sdpuaF3pXkWNvcbneXfEXSuSYbJBY2EoDMwGf8wURgCr-wKq-P0c3SAAgflmq66edOlQHS1cE9voZJnwjmy2nUp8SrHlQYZMPxDxeiLUkbQuBGsH4M5JDTvuiogVW4NjRy0wiXHxV7bHTiFR2aDVWn25H-KaBaWDRasZWwzFS6qgA6VZX_0kGeMDCa5NxF0qZhMfvBEyYQK7-Fxl6kOBsBiEL69JtvP1-3dkZd7Djyk3iPSI96ePzzO0sA4NPnexyH84tHDPpUw3XIq7rekR7QHX7dJ-anxubjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCJzAO6C-ZBCJrSMYb1lMw4H_bsJ4PjqUn-ZIipHI7Zu7956SVJVa829ToM4QyfDZwX0LRZTScyyHV1nTqXYT7Ffr5Zhk16mdc_2lKozFYc8Lrq97212YNJnm5fbWx1GpC0G6kDGTvI20Ub_tmMmuX6t68hc5UhJUTfW_-p2B09gmAk3m0OorJnKIEls2CaIIVdvYSXPCKclcIya2Ir7OmnQq1NMlgq57e2Kw7xitbiVHN6CAy1UJZuDgcrUwlL0T7y2U5f70iIYRA7xgPYh5fBUlTTNZPKfVlaBFAct8IQFmJjgJoFzB2QPuutE6VzKDMtZXI_fM9Vf-0HcnRdr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=tzbEUXwVIk8e0b_5uCyMfJGSaP5QmPN8SmX7reLYbbPS3u8ocFq5DkdueQ49uM3wmO-Z1Np9yElcvIqnOA1hjSN0h33OdouWibzCdSKH_6-E5LNMYuyaOKtC8871EHv_wXr-siAbG1NqdDJlymvhdTHxukfSooLoRZiw3uVLvOCUtAQINacE7EQS7fPY0Dp289jKDDci0GKs4ZaGbrsmgS_Jx_3BqREAvlu5LNdThUq5Qi37CER2Q_3CJxpOc8P9_N1PIv_TMuU0Xd6d76JpdLsG5HQa90zcfv5_pgBSgPe7cFxYD4lAGz1A_jWq1CtA6fQzhFUtECkjmNcnUBjdxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=tzbEUXwVIk8e0b_5uCyMfJGSaP5QmPN8SmX7reLYbbPS3u8ocFq5DkdueQ49uM3wmO-Z1Np9yElcvIqnOA1hjSN0h33OdouWibzCdSKH_6-E5LNMYuyaOKtC8871EHv_wXr-siAbG1NqdDJlymvhdTHxukfSooLoRZiw3uVLvOCUtAQINacE7EQS7fPY0Dp289jKDDci0GKs4ZaGbrsmgS_Jx_3BqREAvlu5LNdThUq5Qi37CER2Q_3CJxpOc8P9_N1PIv_TMuU0Xd6d76JpdLsG5HQa90zcfv5_pgBSgPe7cFxYD4lAGz1A_jWq1CtA6fQzhFUtECkjmNcnUBjdxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدایا ببین من نمیخوام برم جهنم، ولی یارو اینجوری پوستر درست کرده حق ندارم بخندم؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5R-0_fF6j8qPPUqWb7QKt-gMKwBOy2SEzJmww0SGXmiNVONunimvM2Jvgbrz4vHbwvWyN-FOYOABCWoKbuv67sm6AOLPcPeYbCm0MYtd0LD0VDw4J4KdnGHGbAcd2plZMkVuPWlU7WRl_aAoQTVLXTzKdE9J9KfrbCIe4TFMyIYUsLSadjWwyN_dsrhGvxvyVeObKg8w5w_r6WSmhjFV3-ekE_VbPwUeYiYBuX3cRTyRiGfiuajKDf3I_99VKS_o4HgrAv-2BcIg2V3nQrVXa4U9d2if1vB7yC4edKrNee9plp1JaZR5UAVZ8ckdGeHd9JHq3W2DOZelilqFYHj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6qhnp_6Qqa3C4ks0tvmTE6rqokaJ9oYGPHet_qWMRMzBTfXg1Dqe3_bigFEZ8_C0QCVuRuYtSc1ABL_tfcts4_v5qZsQG_wmK2rCklgp9yovCif8enWri6mnBU0ja2rm69yWO-IxB23SxKynDMNQNdPdyMRUCATcBzaK_RUYNWsH_cqp6m4VctQ4gcAvMff89QmmhNVy2l44TbvD7HzAm1DwCd9z5DpsMfJ-skWeeLJxWAXohn-ZhL5GZh09wr5Cf6y0xcrJGP1QyyWgaaAkz326X-p4KRmR9zMy5hbVbwn-4iGWxL9ZzXXK041_EMU6WZ7uLvRXerpdsfv0tCxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJFSpuw3DrYJkrybMFOFjiRRZYKCcE-QAIfu7KPY5teZgWjgK3VYAPlyArRqS2KNE4N9leadCfzz3wcTblEEKCaDo-VcY7dmDha49URW40z_SC07kc0Lg6_tCXVo-x7XuJLah5lFH-87UsauI83s2vYluk9t0vYZJ9FF8dJ3eDIsYFSKOdIyAg-keMysKMwA_yRnQsAeP2B8WbSwToxSgQ9ru8adqjb3ilay1rChh6s367y5XzBtE-UwCg2nTGDDCkdZbbKB_oNeMYR63NmUb3zFHy6AwkiQMclc_xx_FbAzRHGxVBwiklEvayz1lLxdFzXN69PYxRsPMeuABeY4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Oiby7X1Ahx5zUu7qFQybqtAIHRR12Ev4VxocOhIu7BGasP8RBa3aAVebydGwN_pcVliFEyzcROOkZc1Isnk4WIkjj3124pPr50cdoHRD-NwynPLQQH_uQ93sGGrBcBUpG5S7tuSniZgxnuXbzta9XIjuilxoHt67v0HSEubhGswZBvGXdUaaabG_CKETPl5WafJj_g3Evr4gO_50J3F8avBHeBAdM3FrPO0X7qkPm5QuFKwkv01cA9INhsyzbm6ucO8bGb5ZenlI1MHrZWcUk34_ARydhhPjgpjCkvMznzaGXH8s3My4-itDvK7uA12-zqvWGL-mFUUD33czFUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQTKlUXLTsZsVu5dXI-OnsqQb_-KKW8QVGNO7tkMdptOTC2SfDHLKJS635yyNWPKzMUfer7iEMsYWSFQOHP3L2ITMSzxaaNc0jHapItMRqKL2L9p-sX9SWzXsK7K0R6UumhGDtJhKeYjJ8d60vA-kA13JUHrT8JfMuuVGJ6wOAAAezpteJ_QCqUPkasiZdmwkwtMJtfncnNtGnDhC2Cwz20riNtWGzJcnAsaYPapbUsjtDQ8U8rXPvsyiiHCvCfHKTWsUK4RAAyf13RsRY9OTUbgAm6z3ORwVInYU7KEZUgyyFZxNA1zDuz6595TbSg292oi9nIkEESiQNrHDlIcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تراکتور
🔴
-
⚪️
پیکان
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
جمعه ساعت ۱۸:۰۰
🏟
ورزشگاه یادگار امام، تبریز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز+
📊
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۵ برد سهم تراکتور و ۱ برد سهم پیکان بوده و ۴ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
قبل از شروع، سقف مبلغ و زمان‌تان را تعیین کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82185" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEpGHA65w03_qDzkRc5-X-QVoHNxRpBv7pj_6fsR67CalRhR1FgDsznaUa4-408oqotCuwzhjZt_t5yCfnXHLNlqfy4oQuJ5yBaQhXie6oWne0V6ZFEvu0oo91VxSWPPucQefRIQIsnrpbveTqUr8cbZjYtvZGhQfzGKwDH4irFzRV9j0eO5mFwD9P4i4fU6MNfI-vwBn2vDbPk6UgfyRoWcd4ZxFrKWLPD3VBOvNXzhkS4vAsK0YGqUr0NjY6YzutPIQLRO9A99noUpX9ytIUkAGdSZR_R32_oM3R0FyCfBMOhaYBHhZyPbr8xzkSrmJMGwpp3ENE8UO3aQWjJOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0OwbAbL15KK2Wc0RGOcAL_UoRr62BKT64anwLPXeCGnCBt9kieMNii_0ljnLVVTsU1ZYrbCJ6X70umnp8Z5v0TIdyLoOQGElRvMA5iJL7zEf_9WzmNJYFGSMf7sW5VAC8zxoc0oDPU7ZLiUs6ce9Q32pCHxxT7ZAXtHTtIvkxnYFPTo01dQ9llWHhjIZHlmDYRAWoEhFV5Als1GSPc1CIhCmlzGX0MFbGvCrvP_DHEamPnUUGBBao0zaQIj5XxHp5MbhAvYLOGP_HyVgb9wBkoAityoQi0ufcUqtJLjFVeX8Wtci9T-f8eUAE5VxEKESWHnimKvDMV-3SAcOoG5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl8XKrhqeEwBjyuvazBpAmlnOZWoCLMu_7PtEtZFXTZrnyNZkurEAL8mkV1AR3y3w1euNnBTdXxxdAUoEIBOwd8RPXKU5aYJLh_3KAT9UAL55WFy0AC2_S7rDvp3k5xh1EuzwzjmZgR4wXWPCrNeoawKn1UgQx-0WXO6u_JPAiSc5A3HvkiyQOPU3EirsK09906nO6ygbGsRmT-QGp3AS63nagYzTyLDLrlPd7mzxCtl2v2pA6xF7vv5_SxHcpXTV29AvecIqg3RFewWpcFc5Y6ycla9ZCcqoSRKSISYtIpW0hplGU9hbFvZddX1GpdA1uV4HqkCsjLTXRFP4K0JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4GNTPXGbC_Oxqpsp-jGw2rCnGznN500CU7CXKjnZiVDxkIZw08pFxpRI-NJVpTbUwp0_ozPzt8qn6okpUh_Ab53-Sp24BcUOvq5mS_d7qPIpAP4SEOLpCp_4_XbZvaa7OVV3dyDuafhF27fKbFWCqhQijv9da-LaC3wIsbF6ClKF3csrokmS1h4WtocnlqjZtGTOvx0ufAgycQHP83nAQeH-dJM5pXvqiUo-P1sftCuKpDxBZhpgYcP2wj1dQ0MbE5uLkBJXn-nNK-LMs40OdWWzc8jE4dOTHmB6dH7YODnB9OojT3WmX-Y3Hb3HC2IS1Wp-m9_oT_kiNTxVnAgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcO1YKNmGo9myl9XBhJJEd1q3KnqyC2LKv9yL_ktgjy4KWzZaBZ6UMNJCqDMUxBUoYDIZqqtIsB4l8tRKD_hfQuhQDs1hPomDSYtFvD6xf6QYwUpIZbWxUosC0q9C0L2j9k20QWp6urvsCixsgDNUZZZMe4rY1wSqHGgo3owjZECC9-nuUa775ZMVmZVi-28gtDRibL3RZBpvukUh_gtg8LOW5YkulwllObnGSbOAdElyWdDbfzcdhuy4Qav03f3GLX4omk_ZTAcnnknrESQwayV3qqNF_Oy7qP5vJIaCUUZznAMvkwEEQHn_pHUzQS4mtZJzXLULNb0cJ7aZS1Ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=e6pmAUhqhCbhQEWAYCYOp8HL904EEn7-0_YYhK2PIwuLbEuXO4zteXmo4OMHD_YLDNFwPOLfl4ibyml61GMCSZNJwStLaMEBlwWLBqbzQOhDoD0O9dpdASKU6ZUKy7FvKx-dCG35GboAs9GusPKREcsY2X6VTceQ7u9cDGBgjxHE1xSldhfJkKzO7cafERaQN1-QNflGJZQc22tUTZ0LtNNlnq9RtIwxqEc8tCJhdsU7aC77xdx7Ya3AEGyr7aP07wLtidOncqXuZ31ss2PsgxWt7oiyMKog5VoYsoqHNuIFvAzXncBTyU1p6BDpYTCOZrFe9J3h6urciSTE-N6602oL8tkE8plL9oTkImgrBLqZFjnxVLi4VDAWkzNFa2SleSZ_DCEN8RphKf75KrOORI_FLztNVHY-idP5dXp53nl2dVGhrU6nVAabYD1Yo_NLGwKfv7omtw_cOXPvdev_0j4BugrPx_-Ir4GrF6tgzyStV_xOHo400fWzeVVmN-04o_j-AastdgS5pJoOanzDh_3Tb2P7roBNe1tha7rOpcZ_rP5nh_nh7YwAoSTVgNnOqF2O1Llm6pGi2BLdwDK0I9Mt9SsnRQiuXH895HVVJakYteZbQB8-LxG7du5IaTIff61xL9CgK7LUpT2brmyIb--O-1VYSzhBM_fcjF9WBL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=e6pmAUhqhCbhQEWAYCYOp8HL904EEn7-0_YYhK2PIwuLbEuXO4zteXmo4OMHD_YLDNFwPOLfl4ibyml61GMCSZNJwStLaMEBlwWLBqbzQOhDoD0O9dpdASKU6ZUKy7FvKx-dCG35GboAs9GusPKREcsY2X6VTceQ7u9cDGBgjxHE1xSldhfJkKzO7cafERaQN1-QNflGJZQc22tUTZ0LtNNlnq9RtIwxqEc8tCJhdsU7aC77xdx7Ya3AEGyr7aP07wLtidOncqXuZ31ss2PsgxWt7oiyMKog5VoYsoqHNuIFvAzXncBTyU1p6BDpYTCOZrFe9J3h6urciSTE-N6602oL8tkE8plL9oTkImgrBLqZFjnxVLi4VDAWkzNFa2SleSZ_DCEN8RphKf75KrOORI_FLztNVHY-idP5dXp53nl2dVGhrU6nVAabYD1Yo_NLGwKfv7omtw_cOXPvdev_0j4BugrPx_-Ir4GrF6tgzyStV_xOHo400fWzeVVmN-04o_j-AastdgS5pJoOanzDh_3Tb2P7roBNe1tha7rOpcZ_rP5nh_nh7YwAoSTVgNnOqF2O1Llm6pGi2BLdwDK0I9Mt9SsnRQiuXH895HVVJakYteZbQB8-LxG7du5IaTIff61xL9CgK7LUpT2brmyIb--O-1VYSzhBM_fcjF9WBL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mpnDlGovXm0n6O3a6e-qHz6CZ5wsXGksZYB-PibQSF27Jj7bs6XLCFq_WMLDAlzmwfjd98YvUPvyeWnQfdbxnySj0wn-1Xy15mBQE7RVkEhqkoiPzb4S5CvvRA1UhbBfSTPkxB-9ZiHQxPbEnDHbApEOtZLMm5Bn5byqOBlJtfiJxdAv87bVWT81wbn9-TVhB4Q4CxClz3ticGF2b_9-__H6uuZMzG_eM1DXphUPqR9On2E5uFOP0Jb83ZL0L5T6jhcGVJgOn3m8iqUspMO8BKx8nopkaWDsvM-PKaeKHubIjC9Ref_EFDvtHeLTnk_koi_ctG-f_ocWGdNTRvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=JZ6JpIYP69Al9SscME-P3hkMuxkjdGGWpSRsP24w_VjL0E5L_bBHGsysVo16GvZCRmMeugsdntzYVK-N6lZryiIfhBZ-vQ42az5sQ0mAkvnbZkYidgn1efRnWNThW1EvL11cBFOwhCU3sIYybVLySoGw6zNDGJVw6ahDWnWuz0lPmcTfsHLyBmBMUXj0pU11hEi2Qd6PSpQ7Zx63WLO-Ae-JHJXgo1KCA65Rh1k6FsviHjCEYOmc2cj5PDiVa9INBPFyTluEj-b06MliGXWVLqbhqs4rEuoT7P0xfJr3YWIBNBNO9um09SdPTE6Tm3AcEVH8iMp8hbY8Yzfot0gtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=JZ6JpIYP69Al9SscME-P3hkMuxkjdGGWpSRsP24w_VjL0E5L_bBHGsysVo16GvZCRmMeugsdntzYVK-N6lZryiIfhBZ-vQ42az5sQ0mAkvnbZkYidgn1efRnWNThW1EvL11cBFOwhCU3sIYybVLySoGw6zNDGJVw6ahDWnWuz0lPmcTfsHLyBmBMUXj0pU11hEi2Qd6PSpQ7Zx63WLO-Ae-JHJXgo1KCA65Rh1k6FsviHjCEYOmc2cj5PDiVa9INBPFyTluEj-b06MliGXWVLqbhqs4rEuoT7P0xfJr3YWIBNBNO9um09SdPTE6Tm3AcEVH8iMp8hbY8Yzfot0gtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7ITwEC1uuwrIH2jiW2lLPEO31CjyVpAagVX4ivVrDzIpNNdeSWX-3IqFTvgIZ3XZ1NeeHyE4e_VxlO156bUoNtBi6dyA8XsyWcHgmY5pTciLOPRSe41W0M3iSt6wEWz__KgXeMvmxH6Elao0vHX4Bl1KQpXtaztx-U-GIBvs-3G7A8L7wQNOKFBzIN1V3ChHn51cqR_pXj7uFT4EF28t1j9sLickO9ObdM3uZ-zxKxSR5l6LVQrkjQYd2_vhQ9ljge4Tn-QCxGeh8HTX6YMpTi1igi6RN_QNKcuKrir1Pv-dW9TkNnPWqk2dkOp2tV39AnJxV-AooGRgu8gixJUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZDTOKEAjqeZFDTfv1ffPhcOSZ7UcRxRHf5EIE4JBJ2sHWNUdSjZM_UycK6yKXmMMvQdsDcXw0hrPaMN9IFRelqwgwBpGfYRGFOiSV0oXj_QlMmCMdmp4mKN8M-uDMDOgNyQZ7CIX0g7TOHFarlBHmFwT5aSZabbnY83BNtbJkjVvIXiHbaCg7DiWbzDDV_1D32KaZ7nm4gIKyd4h9NiOi6h3pYKzaBaTFm5RSPJAtceX28QDyp2oUz-E-fyjuwLfHT5B7axIrmIrrYVttHSwF7SSJI6C42nKKJXTHjN8UF372pqNFvWBz66rb6ccyOeiiVS6ZVan1Ssgw4mihgevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9WWnpi1pYwqHgqRW5GCIp4Txf9N8zGZNbhBuDXLCh58ImsPCuNBxl513ZJNXtgT0RLh5KnQrOcbpVH-Pfvphy9TksDZf3EX_OdpJ4oB_DqFLt_XPXWmGt6BWkrwhFrmWNI4ABNY18gTugpX1wqh-eh-DJxbWaglpfu4ls8aJRe02Iuer-Kf80czXf6X3TMv9i_a2NPdMEJGRglR3GjWzGJ1m0yFyUo6NV7UrebzOJXRBo6Cgkgy1onIDLsRLkOWcKMSQD-RvTA55nJdBOeS_eAxMuRnw7FvZ8o4z-ihmq65E59_x4c9_3RZg0XnIKJ7saEc8GPJRNu902WGtkjfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZpJNW3iv7id2DqerCsbSpDO-11niq5Ev-xqu7E4E8sTPuTx1S_1LxCjTCHW_9FASfARgy2Ju1UL6T70-frMIRbSs2UDDkO2Z0bE-ZVPYdUElGotsnJVCGC2sv7VLo5K2gTxk-hxy_SYvbxWptknupV2j-zlCQM7K4BSFeIXXwQIjEVka1dnUFLBhGYmP-77FnAWrg0FMG0oNmynn1gIf2oO1DGhXzsGgz2f9ceCkomB3Lowv1m8ko6c18SQvBng4XPhghZZcm2FYi1gqnwnWv5BGBfIoVrxD002iAsVf5ROKLUPSUkdexAOrkvtVaUKZbfayX1YMWkWawXPYAdyGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=D5fgWV7ZBAghcN0t8u4YrFonFLyPXFJyY03F1zL9DLKBddmUxMz_Sf5rWH7AjI4qw91KgDPo9MQu19VfxpSJtdl8nCOFGEFstVWplzfqBk-st-wZBv3hMMWZBP75cUko1bmhlMDibMcowj9jW495tCoANNfSTcZuMiBUgvpE6n3E58mA8sKqCqtV1Csks_mBcIjZbMOlIfk_DDJFy505h4N7o75l3xoEklYqu_innS0yFBnOFIUKfMfj-7MFNHAxzuO1x3YUxLKNAZBJM9CjgcJOe0aQGX-laXaDa-Az0JvbM9frHxxyik0sBR45Ag_iYQJOI8bs9GtBfvnJVyijvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=D5fgWV7ZBAghcN0t8u4YrFonFLyPXFJyY03F1zL9DLKBddmUxMz_Sf5rWH7AjI4qw91KgDPo9MQu19VfxpSJtdl8nCOFGEFstVWplzfqBk-st-wZBv3hMMWZBP75cUko1bmhlMDibMcowj9jW495tCoANNfSTcZuMiBUgvpE6n3E58mA8sKqCqtV1Csks_mBcIjZbMOlIfk_DDJFy505h4N7o75l3xoEklYqu_innS0yFBnOFIUKfMfj-7MFNHAxzuO1x3YUxLKNAZBJM9CjgcJOe0aQGX-laXaDa-Az0JvbM9frHxxyik0sBR45Ag_iYQJOI8bs9GtBfvnJVyijvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2cUuvkRR6xK9CdFP0pWx6yegkn1Jw2qD0CK26XB54rS0LgeG-Yf09ObWikupeK5H3N0u9hF2Tjw8ahHmjWuXfSnoyKDW8Xey3n52xs_glM2zcz93qwvgU87Im6ZbIiBLIfmnvnTOuPa-vzk_qqifGE1bGioU7JP8iGAYc6uxVVsMeKytJnAy54YTgOYZu5q8sk693_W8qvkCzzp2Xm0I7m68eLPu6qUV4ZEen4BkKTueIYVfneG2RzaMwiaGXHVds9DV4vcRfl-5K0KLyh8OqWKTF4kge8vx6nBK8cQ3vHDs_wX_cbXxJQ46-cSmyRrwYfyiWZqxsALBepuo3EUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بزار جیبت بیبی</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82168" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82167" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL5Fv_XLIs8XfrygulwvfVn12TSW1K4gvTvBSMdTkqhReMquExhrZbaL4mCK5BzYQiTZxYmXqEq5ECF3B2S8zqdKIlRInCFuaM9Rswp5KHbOEqb9odHxHRiTwcqxR8Buc07JpKLKvO98f3HpYw6NrbnNi0vDw5izJmzona0Kb_2y8D5R9n8Ttdo0yDTH7SfVcAS3pHkNMZtgr2rDJwzirrwXHULjCTT7BFKSoI4T42eKKq4fl6d14BYK9oNAHVGMda6Wg62xmTc-whnCK46XoyIPFZzuGeiRilwuNjpO2yeB30H-qBRVNYyntkHkLncRA1R3rgC8HOvMK13BLSaUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82166" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82164" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbnR88iywTaRbhyeeXbvkyvuQTE6bEm5R30I2VqKR9b_VC89HlNk3uimdb5uYn9-2UQz1FMKyBeHXk5biUbm4FTPOruztnSw-sABjlHX-bkvh-l4E4qFoXJ83zfjfmo0tlCCBU2ea6MHeEXE2a3xaFz1VUR7IgdLIFO-1Burkb7C_X2AQdizeVzGWZfs8GOSUHzm69JP3iacdl5IPPVa6LCQZV1jE4RO1_mw_1bjzd9dbiRv2YAHK9YuM3KCDjZOVT7I3MCWh0RxKNQrVM3P4SwzfSU1fcdpxGlKH3wC5lsHsnGwcZJ140BYvrwjlJFFnpARGKars8TCQEBnLjoN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82163" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=seug9quxKIDbXAkhm6IovM80V_wH6FLgm1Z4JsiRmX80RyFoMmWFmSadAs6s841LqPoj6z0zPDIC--N915b1luySHgkthxLgfsieoEGUTF8yoLRKuKUo8_Te9Bd1rO0gP2VlKZyUEK9snwAe5_IVy2QqusFYhJCjHS3KGGj7MmIkNc7ZqibZgaQ62pPfcUw4pMF5O81B15JNc6g5U91HA0J0M36ObGFoscOUxGcI85qV8W_qZ1B_7DhvwRoEJzpTWMw1K1xn6VVZNCGCQ_j8uOettnBHnUjvwruzIgfDMBS7cs4VV_hw8VboaxjCTjpeOEmLZu2CMscTmBYqH2lCoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=seug9quxKIDbXAkhm6IovM80V_wH6FLgm1Z4JsiRmX80RyFoMmWFmSadAs6s841LqPoj6z0zPDIC--N915b1luySHgkthxLgfsieoEGUTF8yoLRKuKUo8_Te9Bd1rO0gP2VlKZyUEK9snwAe5_IVy2QqusFYhJCjHS3KGGj7MmIkNc7ZqibZgaQ62pPfcUw4pMF5O81B15JNc6g5U91HA0J0M36ObGFoscOUxGcI85qV8W_qZ1B_7DhvwRoEJzpTWMw1K1xn6VVZNCGCQ_j8uOettnBHnUjvwruzIgfDMBS7cs4VV_hw8VboaxjCTjpeOEmLZu2CMscTmBYqH2lCoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82162" target="_blank">📅 17:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=l0UR2ZS-lKIZ0yp8oX6sPlxOEveJAqCPk4LsbYFGBGzRcgWL0fkTIJyyUORqKWlU3amlM3sD2M7hjLarXqmxS0N-0qRhUSOm6gHr-3y-N0TXrHoky6vWDtYwEC-pReriyLSuEr4BV89xjBr4Un7V1Iaab6ympTdzJQedVIIQPgoUgxa-nhDFwwAmLOB48-cOn1DU2ZgGIAB_XoBun1sQ47P9aVttooCZsvd05N68fMybJuZuSRivS2N-xmmWQvcJV3EfamrgY4uHra2HBQVHrzH8KGO_z8OoHN3ev5uBa5Rio32Ss2ozbQXmlx2SW_jfKt_6dAfN6gKN09ruqSjJRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=l0UR2ZS-lKIZ0yp8oX6sPlxOEveJAqCPk4LsbYFGBGzRcgWL0fkTIJyyUORqKWlU3amlM3sD2M7hjLarXqmxS0N-0qRhUSOm6gHr-3y-N0TXrHoky6vWDtYwEC-pReriyLSuEr4BV89xjBr4Un7V1Iaab6ympTdzJQedVIIQPgoUgxa-nhDFwwAmLOB48-cOn1DU2ZgGIAB_XoBun1sQ47P9aVttooCZsvd05N68fMybJuZuSRivS2N-xmmWQvcJV3EfamrgY4uHra2HBQVHrzH8KGO_z8OoHN3ev5uBa5Rio32Ss2ozbQXmlx2SW_jfKt_6dAfN6gKN09ruqSjJRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارتوش کورک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82161" target="_blank">📅 16:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnZiBkw6h1YHxG1SQjXLTym3RJFR-CWFBXOHqGV4I05_ojKGBV7sYPmlB7Y89Xkujg6-61v0FvZz5NFPn4hdmb0Q9BPEuz_b90HmtqpahcpjtjE7l5MyelKGzH4Q5EZNmWumTva204HfMc9k-kR_2IkYTL3ThRVrctwbrKBTTt4JOaZfUTlYRG_XHcbv3_KFDUuZXXl1dllwsXqgF0t2PDhu7mm8x4sEDEQyw2HFr65OL9y9g2XWQhpqVKFOxNJ8HPq0HmV_6A0vwQRNHvrvVOCiNBMiDKYsukUn1CRU5De6WjTUVdxvo5pMseOxWi7QQvrrsPMBUcxfzVyqU7BGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویرو هربار میبینم جمله "آقایییی محترمممم" میاد تو ذهنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82159" target="_blank">📅 12:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmMvXXA7AaTftkNq9q8FdANdEBbxIokkhQmjGryRX5srnqkjOHJAgDQqudoo8vxel0W8591l-0de_MJipYBTr64JHiPWwSUDxrWSHwb9XA3YmzoTgP2Cz5D5-ite-GYqx4dH7yIKouGGlvhEizFSBxKC2DVYKDB-FwEow6FRCO5T7jfW8RECzZfiotwPBY0S6sBZmNPSv9cRKAdX-pmqfMnUZVde0fDkYvs53jiOA5Pr79fiRkKsO-KFFhGv3CnCVvx3uIfhWrYJVptX_TjTAtzO_m7IezyU0H0InypmHWcq48bU3Bh6ln4wk1zY3pdKatmMAGbgGxWkQcHrQijbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه ریدم تو سلیقت
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82158" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=nJidxAe4kkxBQAaweKQh-8e9qtPgC4yJAA6tvMFwp_LQ6xSJSPbLZCKQg9b8-LIDYB--QnLc4BrGSnCiSP3dbe10Et2Ox_Cj7bLk2t56wBkeofyz7kigdzocExG3MqTan0lKnb2JGuuD4KtE5SL4uuFdGje6ZnATrNYPlkZ68SfoDubKYNrbIf-Sx-BbOAwat3C68hafP2ZfIcrQvs-Oq8ps_Fer-wZAZSYE96UPzbVxoJN0auwzmHLyKTqKy5c_Wt4i95wCiZjR8u1U_72Ci3kQcCexJUosQUfcTrx9zNSOkyCSJY1ZnOcwu7-x9_gUbLvg6GvHLzuzD6PbunfWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=nJidxAe4kkxBQAaweKQh-8e9qtPgC4yJAA6tvMFwp_LQ6xSJSPbLZCKQg9b8-LIDYB--QnLc4BrGSnCiSP3dbe10Et2Ox_Cj7bLk2t56wBkeofyz7kigdzocExG3MqTan0lKnb2JGuuD4KtE5SL4uuFdGje6ZnATrNYPlkZ68SfoDubKYNrbIf-Sx-BbOAwat3C68hafP2ZfIcrQvs-Oq8ps_Fer-wZAZSYE96UPzbVxoJN0auwzmHLyKTqKy5c_Wt4i95wCiZjR8u1U_72Ci3kQcCexJUosQUfcTrx9zNSOkyCSJY1ZnOcwu7-x9_gUbLvg6GvHLzuzD6PbunfWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم آلتمن مدیرعامل OpenAi:
احتمالا تا ۶ ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82157" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=bsqBw7vBM02pp8aaX7NeNcIAuP69dRSPybORsCkAxh5DI3rJU9D7AFQUI6D2mLCecFSniZEcEwwyxz2Duht-B9o_CsRbgnwUFlZI1QBdGa4cFUd4_aFQcM7wyIWheKxtNda1XZGbpHNuf9uVYl9qvr3FkXYQLZRgWT-K_6l1I1YGPetHryWx7Ow31qyMUXDazHDlphc_rsJXcOGIwgpA6951nChndD9pVtgiPn-IET-x1s-jryxdolFy2CfK0BhVZhdX_8zpTYcpiLQen7fPPVqUoz64LxQPgtoCdMHd-tJ5uqsE1hzsv84GiTSLdYQP8i0wHEWz9mE8zYFjHB9OHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=bsqBw7vBM02pp8aaX7NeNcIAuP69dRSPybORsCkAxh5DI3rJU9D7AFQUI6D2mLCecFSniZEcEwwyxz2Duht-B9o_CsRbgnwUFlZI1QBdGa4cFUd4_aFQcM7wyIWheKxtNda1XZGbpHNuf9uVYl9qvr3FkXYQLZRgWT-K_6l1I1YGPetHryWx7Ow31qyMUXDazHDlphc_rsJXcOGIwgpA6951nChndD9pVtgiPn-IET-x1s-jryxdolFy2CfK0BhVZhdX_8zpTYcpiLQen7fPPVqUoz64LxQPgtoCdMHd-tJ5uqsE1hzsv84GiTSLdYQP8i0wHEWz9mE8zYFjHB9OHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال شده باشه اگه سندی چت کنه چی میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82155" target="_blank">📅 09:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یعنی نتانیاهو با اونهمه قدرت نفهمیده پوریا زراعتی آدم جمهوری اسلامیه و بردتش اسرائیل و باهاش مصاحبه کرده ولی چارتا کصخل تو توییتر فهمیدن؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82154" target="_blank">📅 08:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">درکل فیلم قشنگی‌ بود بشینید ببینید بفهمید تو چه کشور گوهی زندگی میکنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82153" target="_blank">📅 03:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=UgzVVxGf7t0IKjkYdfEY12nF-jmoHeb-8d6QIwyZW-MA-TJW4WTClnZtkXGn7NtqVXiTYoTcVv9sHrvcKoaYLfTRlC5pZ3U6a65f_GWQome37hcuAIuwhPx-RbNYQXUabbqgbzW7lHCmkJnddBjuDzWrJw4nMbhFc8fmaar3yuoDPLPFLy8-gMjseYO8ER0Caj3oEfYOsmA0mdoHFlEmmi422eWXrw2uqtjt8dgaXi5stkxYWTTkYB3L80GOpQ9-PXHpmy-V6bHI4o-hAJW_nL2BA_xlSAY1TvD6HSIkvzvzhZGl4iCed7-qEgllHslpkyaQplB6bHJKyy5_6wxKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=UgzVVxGf7t0IKjkYdfEY12nF-jmoHeb-8d6QIwyZW-MA-TJW4WTClnZtkXGn7NtqVXiTYoTcVv9sHrvcKoaYLfTRlC5pZ3U6a65f_GWQome37hcuAIuwhPx-RbNYQXUabbqgbzW7lHCmkJnddBjuDzWrJw4nMbhFc8fmaar3yuoDPLPFLy8-gMjseYO8ER0Caj3oEfYOsmA0mdoHFlEmmi422eWXrw2uqtjt8dgaXi5stkxYWTTkYB3L80GOpQ9-PXHpmy-V6bHI4o-hAJW_nL2BA_xlSAY1TvD6HSIkvzvzhZGl4iCed7-qEgllHslpkyaQplB6bHJKyy5_6wxKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82152" target="_blank">📅 02:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82150" target="_blank">📅 02:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmgZfbzapETXPVJB4O-cUQ7DrZ1YYEbafpFPCj_ocDYwkEvDVLHzAtf0oeIev_UpkJwVYOCVBeSVtQjLH7ZVu5qd0XHGh0Ifflxs4En3mnMagDHN3urCze4I2A_lrLr3rQvFnpem4BuK59fRf1VpPwWtfjn1jQ1StFhMdy18L7tnWW9h9Yg6C0qleQiGcoGNTeQWB4oHgikDAv42_K_6ZncIRm8gQF_LhV6PtreS21VfeK_dS8AL5VLJro31gPfg8xu4Oh_v7qk8_-wSznpOSOPxkhYcNJTDyEQLE2u2gW5t8-VU9JBMCtLWYbNmfeEmZGjzTzYgkb79gHnaRx9jyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=fQBxyL_BT2lKFcoHRrJzLhmbT3uHaTiRAIVvFO7all3lUiiQC-LOe71_U__hw6AGryk9o38PzuKvqRddAMkL7HRuWOhGMqjLKmuJNr019qDOqLpsby9ACGAUtkEPdLmCov3eoET8vTNGHnEueSw1NbuIBNkKT6sRNLZ_rUpgDJLtpsRqCFfADcEQBkBPc1WGWwn9JBBSSoVuAPZS8RAupm2zGxX6vgmzDeK0IC3uHkInPX8e9cfU7kYEP47mhW68AESPX56RB2MvB1tMpli1Hd7Rv__c0TYAdZh0P2ELvBem8j9IZ9A6JdOnnQGKC4xGdMq_mqvMk842A4h0vbVLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=fQBxyL_BT2lKFcoHRrJzLhmbT3uHaTiRAIVvFO7all3lUiiQC-LOe71_U__hw6AGryk9o38PzuKvqRddAMkL7HRuWOhGMqjLKmuJNr019qDOqLpsby9ACGAUtkEPdLmCov3eoET8vTNGHnEueSw1NbuIBNkKT6sRNLZ_rUpgDJLtpsRqCFfADcEQBkBPc1WGWwn9JBBSSoVuAPZS8RAupm2zGxX6vgmzDeK0IC3uHkInPX8e9cfU7kYEP47mhW68AESPX56RB2MvB1tMpli1Hd7Rv__c0TYAdZh0P2ELvBem8j9IZ9A6JdOnnQGKC4xGdMq_mqvMk842A4h0vbVLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال بعد دوسال جام گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82148" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAktVViP6vkGOzXxR16ob-fhzq9wJ2xHZB4axp34U9ACblxfUW9t4zSXW64CSf3-cwze8L0JrMqWpeV5WBTCpImi5k6aMLticImgs-FVSoXFxr5AdQxIShRymDtwvzCaoEx3L-pjLWVIELwWYbdLsJfxbZi5670HIXS4nwuZix2fp-j4cWXqv62X-HmWY1PgeoPr60HwcbBjW29r3IsptEksAg02i6AOiO61UUA893FOaJlm-kRZfAi2ODLamcT441gkxo_nZHET0ZYnWzr0L116wdm5m84DO4eYvFiIAxTwmQZ4u5Vs_-qzYHNlbuY9benUD3P-1r4tKMLjwaT6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اوکراین هم عده‌ای از گیمرهایی رو که مأموریت هلی‌کوپتر GTA رو با موفقیت گذروندن استخدام و مأمور کنترل پهپاد‌های انتحاری کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82147" target="_blank">📅 00:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پاول گیفت تدی تروریست داد بیرون
🎁</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82146" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کیرم تو توپ طلا اگه به کسی جز کوارتسخلیا برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82145" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGt8VLiwX47x4yV5Y1UCO7ikq8zRumF7JsAM2J9Xkv-OZHOR6DEpZm1jG_45GxvzQtuIwMY0V_BzdejlrmxtqoxDtRuo_OOwYE-enLvAdZdU5Q_EmXesTNbN3xKGa4aQnOJO5a3wAC0Tuew8s9E_pni7BiEg1w_Uu0umjbqw7l1cDpO-6FJaUPwctyu59TkegS1JZzuqq9XPqZggbZxp2i6L1gJXhXwV7O23tL93hu8ATGXGp79UzR3480WviWYCbQMVgzhOxIbuFp4iBlQmG3Lu1t2MmXZkHewKKQXG-pz8VehSkc5V7_yiZ5toQcIn7oohCKOAq7_U8q_xuzeWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به قدرت جدید فوتبال ملی اروپا, هلند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82144" target="_blank">📅 22:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">البته ما کی باشیم نظر بدیم، چین برامون بنزین میخره</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82140" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">موضوع سادس، نه میتونن بنزین تولید کنن، نه پول خرید بنزین دارن، حتی اگه پولشم داشته باشن بخاطر محاصره دریایی نمیتونن وارد کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82139" target="_blank">📅 21:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تورو ناموستون شما دیگه حتی با افغانستانم نجنگید ممنون.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82138" target="_blank">📅 21:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">داشتم فکر میکردم ماشینو بزارم خونه با مترو رفت و امد کنم یادم اومد کلا ۴ تا استان ایران مترو دارن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82137" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قیمتا دقیق:  نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان  نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان  نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان  نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)  پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82136" target="_blank">📅 21:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قیمتا دقیق:
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)
پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82135" target="_blank">📅 21:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82134" target="_blank">📅 21:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82133" target="_blank">📅 21:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟ کدوم کصخلی میاد به ماشین ایرانی بنزین لیتری ۹۰‌تومن بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82132" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صبم خلسه اومد این ویسو داد بهش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82131" target="_blank">📅 20:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مگه دیروز تو البوم فیت نداشتن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82130" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کچی میخواد به خلسه دیس بده</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82129" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/il6lmvhdzkY7De4UBOUJa2Gt_NqV6VOizgFDQOPTbQkNjBbmy-KRsBZ-VinUDfJ3_3N8ZU6i0UJNli8fBspm75159HuZYYX77YW2Qq32WGAezMgDMW6y1_58MS2AA6MtPMG01uv_VFBKU-zCK8Sr6RQCPt-pE0qZFHYWQIF5yzDNeZkXA1vYJz_9cyJnbn84h4AHf4fMuMqircuyRfJhF-6wfjgetp0txoG3SJtwcejV4a68QCL_5o3STrt-SIaODFc1abnO21RsCmPVfKAhOSNRmmx74Bu-GhTlnGvoveUeDaWX9ASJAKCGd1RdP3p6ur25_3ut722NKgxsoUT3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادت باشه اولین چیزی که توی استایلت باید بدرخشه، موهاته.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82128" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=SyXkJpxMuuz0g0bjmvklvxyFXEAW1uJAZNFvMDkPtZIkV6WEC-pq9ctQoemXNu_M2L0fz2vR34atxOs7sYXsof0BKq_cQvW3ijhdpswqwuy9iFsHaO0w6uEjYd308BySxOzjizi9zqIT55ORJ-gnmAEFcq2MjJKqDMgkAp7VxRx8QzrZ9vl1LjjeiXP8pCX2SAYdH-QV2F6AsiKyg0rnkHurvkGaL4Gq4Z_0oLQlHEdXFxFAngVQwGMPoNnyKWw1bRN1DXnx_0_-mtgiaWnKg2lK6OnB2l16Snz3Jeg2TVDIsxadWJOfWq5lIZE9f3giJHft_xrJisU0KBtQ2Xy4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=SyXkJpxMuuz0g0bjmvklvxyFXEAW1uJAZNFvMDkPtZIkV6WEC-pq9ctQoemXNu_M2L0fz2vR34atxOs7sYXsof0BKq_cQvW3ijhdpswqwuy9iFsHaO0w6uEjYd308BySxOzjizi9zqIT55ORJ-gnmAEFcq2MjJKqDMgkAp7VxRx8QzrZ9vl1LjjeiXP8pCX2SAYdH-QV2F6AsiKyg0rnkHurvkGaL4Gq4Z_0oLQlHEdXFxFAngVQwGMPoNnyKWw1bRN1DXnx_0_-mtgiaWnKg2lK6OnB2l16Snz3Jeg2TVDIsxadWJOfWq5lIZE9f3giJHft_xrJisU0KBtQ2Xy4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زاکانی، شهردار تهران:
موشک مستقیم به طبقه خونه مجتبی خامنه‌ای خورد!
خانمش (زهرا حدادعادل) اون روز سردرد داشت و نرفت مدرسه، موند کنار همسرش و نهایتا ترور شد.
مجتبی خامنه‌ای خودش هم مجروح شد، ولی تو اون شرایط دائما دغدغه نماز داشت.
با وجود زخم‌هایی که داشت، خیلی مهربون و خوب بود و توکل به خدا داشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82127" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
