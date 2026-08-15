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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 19:12:16</div>
<hr>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLGWRlbx33hWduWa3AVZcMFO5XtyuXoYMx_0p8K3FHYysJI5_Pzy1ZYbAEPjXrEcHFJaMVZ6e8YE51MCNuG2jDSxQCVr0hAtrEzOWviElC68hjA-XdyUVLGP26dH0gq6x2NvUYZX0M8VFdTr50otsuxHFJNnVj0YNVfhNPk2HdGquKism8PMPYDvuLeDwn5v0J1FxlRudO3RbgmXrP3JTaI-BrGoVC8wsFuokDiDjm1MoB6dD9q29rBksaOqi0sNrBZXjMyQLRkgHqdwUhlS38ePNPHkni9ZzU79phwFtX0_KG49psEWuLUkIQRqqNvXjjmkSAg3rppRT5KlcmbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/funhiphop/82232" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb0YNSt47KvBh2c4LHwjO1xxyM6YfYw1AzTA8N_szDRjBSh6UScCFqC9jfKua9SQivF0q2Mh4RkLHAv3zJrrbzgNzOCm6t5NiwSxW3ltMEo14CNDMMRjVHIhd5Jcw8vhTmJrzCNUPTh69Hf4fRWHctDfSn1F4jKU-KqsLNCDk6KwXfwM8TJobzF01UeN1GwNtRfJLF7UAhvHNna2ucQZZXG11kz5HRPCQ1rUQrh4iW4DJiaJRkeq9Cshun79ZJi48g9NtkdDyZcIRLk5y0I5i4rMTMNBZlW5DfsIFWaJeL-p78wAsKYj_MlElW9EoUytIhcETC-ZvO95KRI-dJ8QAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-9EWCSyykywg3pSs8q0H8q-ffERskTaIZw6tdTiEHx7OhcT2q7hPLzaZab3gaCet7J-8T-UgrAJ8HkLARgWtai0is-2LBjfR_t8pB33XiIt1rDc3VvdGmJWg0HAEwF8oFvwfeFwEaaWqaYNejzXPrYoeIgEmjdTDOeJX9fIUKFCBa6j4-V53KKYxdJ6Q_wxUNqcSL0KUGVvWby8huBO7EvKdJ6gyZyrLEXZ8LTwSel8WndhHCm0FYEu3DIGb-mdPps5fuwgyyYXIZhvYVsPIWR9NfjWquS47KRoUu3mtekXazXtIxYvvGaOvQHKHbpojNPhSztEHUrkGIZP6pF4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82221" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMmWtuun0SoZXYCmXstMsltBodhWjznqpa4KPv8uLcH-41_uGZ_QAM3KRMTpuirBtObAXqEtFxV65po07rZN9V_1QxOOhxH7CagqTU65F_Gji3-P3PlzDaxwByztNOrsfk6Y3c29YSxPkQ2HRt2al5OujxZ3Syaw8kvXGB8l9N4QQUtYnF5Rt5z2n5CehVtCY1dVCyal5_y0th9rvvkRDIq04o-3ubZTyjUHpEHJ97WVMF2UwGqYtou93SK8ST2fSxQ4oGbxcr0tWjqucriYmYp2huBn99lLrDr5zrAmFohJpKQL-npYevd8l7vAsHtJR99m5xdnKwXK13hsD_x7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etzHVXCoIcFj2ipBSL6r-AXicXrGpBZJlLZjdRhB9k1tLpmTOBHtjkoMldGksJSv5JWWjboc-pxKn7md8EA-YjCLcYVxO-3GjjzrSJBzZ2g_UdrNepVLvfrB7viuw0ZeFQ6p9xsRQdLpKEI570vt6vdTAH9km3od3pzFZP2YIj2gMtzB41bbxKfPOvMzBOX597sLWdIC4JeNkzDOMioqPzAE_ZItblxw0kvEy1dUFtfjLEJtvp9elRV3dfjXN2e33nEMn92dvA7Cusk7WqpHcLqiZpvzLZbM_C7fYRifGfZhyY7IkHT-y3nyeQee0tpYTYRnM04En0-fXYvhdfsV9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEclWlKC4QlO9C_TPF0hKCGwtQwtMCrG87USiskgTva1bM0F1YU58kkeH80y05vu632R2JTBoghdvjEO4rUTWONp8oYPLmyaml5fMibQtoizDADFCfBNO64fHPQWeBdtLlT4DEODF-WREv-gxW5lhgsaRGoYMXNrL6UURjCJSlNJvi2eSBK1GVdJ2TpChycnsw_7WOOGeP7HPdad7lwlF9KMxYF23_EbUf7SExJDWWNUB2X1vcFHO72fGWpoNCOql7UTR-Gj8Nj7UnbYdhrVu4MV6Wx6F4jNbLE52oZCZu6XmsgjwU_kwuYRjqiqv6eWTnm1y8QSYGQ4Ylc8BWLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNu6FapxuJf0YmPr9qmHyK-FjWoaDmcLsfYqTRyIlp_5_q_yMzmxgkmz4EMBd-FWStqkTRRs-ov8ls1OilpxuAps2V4GhUYtKOlkiyog3wePygL-eaN7-wvqoSpSGFrWjRGZfKE48dIgl6vNRZmKKbfb-Yclef7rRoFk4HQSRCPUGAb9jrXpYWDgT2HteAUg4UR9KmkJsxyNyTNI-0nXp3xZvwgHgBYx8-R9DPDyBmg7levZLmSkmSfx8KER-PLFzmjwNypUFgpvTWcjyRdNaNJ-DrWPGXnw_olgXuZeLPnmuAFp0ruQEpIKt7gvEiI9WQXkUiExTb9ImpF_nXI5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFHWw4sUBxLtFd03Tz9OHizBY4SMKZhNxunO0is5ymE6eIeh9UyMEKM9_SxvAZQ8PO8VScHMgzhUEmUrFy1mjTDRGcEi2MRQw1uGV9KP9_iJJeRqKEpJ_g8jkBGqb67MeATY3-SDCyIDJIrmZUnXg1AOjwY7tS9rAONLLw5xCGfdAPMmhlzaCDwQB7xR5iDMtXH-T04TjBI9NQs2n-5C77MKhAZAjQHMJVVfFs-Oq7ifl6GvLWQh6898U3oLuJ29v4tZy4M5H4kfcisUs6gsV6BPbFEnQU1yZbA72aehQycqEK4HmYLIzyi0D1rJnWDrxCb7XcI2VeU0p35NzwPDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbqNRIUjRB9ZUsc5s6RfoP6RWUCYrdNz4BmwNu8-q3OdV79H9-QUzpWRlcQcfed56bHIqCvoxZGJHXYMx5pvwH5uq_KaAeJOspjJm9l6PtDY5_FddeitJriG-2qtsewsn6jE9iXwII0k7JRLNhHFyuLciWWF1uSp-r-usxYJuukoPrYz5GhCiEPq_nN0ZF1VEwrmlAlvjr-sKY-YdlIlD-Xtvxna114Z7WRIvOuimcqnvjbFpANYdR3uxp7eQcVyCl9Cpg84EdDN2xQPrp_ZkGtj7oZmjywtx01gbgIyAGUSLrsbpnLqEE0C8vERIo2zI2SsusqGPhqYct5H3Kn0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTC22m-0Urnt94AR4oYlcVi1mQN5Z_HAmAFlX11L8pfgnXJJ_qsXNBi-DKpX7kceP4dFfG0LJ3JPBN0NuN9RJBVMGRjFqDlRcGmLKJm61YyplPMsXe-CsoC6xD1do1WnC3DChRUUc7lapzeoTZa1vnxoUVWEQl5ubbi3EEVxC6B6kxvf5jcAj6lUwe9I5BAv8HMN-fjTsfBqXyaDa4aKxBpM5MTtFcd-uGrke7NzvdKYU3HF1NEiN5A-jLe8_JW44iM5ik9j1w-Jmq8rjXBVo1Y-Cfp7yG7oOX455yHqqKSAzIOkSHueRuajnNG_mR1LO21bQsOR9riZY8bUxW12WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4BoPa_Nx72GD7iDDifBwYpvMfviscBn_s-Z7dySAk11oUEIP93HKTwYXYUeVsV1C6-DU34xFfRLRv279p9b5iYecsBdQDnzcr0Uz5Z9DMXGnBvJHUtMIkINhHezHDLz4HeSvPEgREwO0j4ft1OKvCqKdzbMFP3oKwzdJd5CDKJmhjqqsZlyiee15EoooOi0fIXTrUfMPAJvJPZHjb-9f6LSnvuCRpRKMqlFw5BFgl7BdynMlw35BbOAIz5Xqs69_1ejH5-IQWJq8bwqNr19UqxVLdEQ0gcpn8mxjD0OEwIyG2x9WLvnEAGHA0iszrPEvCDVQJqsb0fnIaKdS0cJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjP7FnZ4xIO-T6SESs4JvmKaUT6xA5aGAA7Y17eNqxt-jODbGh2GV5f2tIj2RhI4jHmrG1Pr_eoxhJSVs945QKR7nYkSuipbnpQ_n-VWR34yvrPdVv1xB3s3sqSQ3AtOxSwmsVej_N6-b3uNtRxLWWDLTzmtgxbnQAUyQCgQ5jSHJePmSrIyk8vumc__2JNO9Tb0Fsfnqytqp9UcXa9vlM_nKnEQQATsZ8_TSGVIRUJpoXvaUiv2-MDzjNv0ET75WqvU32vz0PiLNN8yqvVdAH_kLuawD8hcB5NLIwPk6fGVRPlBx7PKxlWjaXPtgMVwIC1_QibtRrQV1AKeYEyLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtxJQgoK-FAr6nnKeaVcjvte_yxUfbERzejn_dELsu4sPZKz1KT_eHuePwA1CLt_7qS3C9Evmykrz0FI5ZMuN6rqAOwrpdNqzR0nvfZNBFYkHi7209q0G9d3BGVed6Oa97yse_6SmL03F_QfJBdkgtDX5gxrPyQfj4ibeYxexYI1ec0QFAAiKlQxmHSbOPA9vGaEE7FBZQuno3rcTmmY3dF6VGlzH-nEi_o1npAau6brAkrOIneRQXrQRnbmP9kJ36mwyzYLm_OxwGCOLplfnoVBIz1eYvYrYDvjJmGZX_oKufGsjc73nlP280mzL8vTShdRExWLdiwpYOJ3FQyYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrwNa7_Ay9thTU7DGStL7AHLuiXXqgMnBE-ipV1ItGaURAjoi1F7g73xby5ZpNqWfODGBwYU_sIaZrLNKnqRxRXdWMKaOwv9Cx2XxN9PeGXMKNTuiDrUCkf8D2scb-HoDiCxNbt29zIFJDEVSmm0xg40GitRs1B8nEMJH9m549_JzFYg2Fl4cp15B7lqLOnm7LwcpJdkISEH62l3Cl6fnF0PUxlMjOMKpvvNGrm7fUmmp3UzmWTxx4tjyXotd38UVLuWbe__XUtACEsqekT2TChF_0JeksLahBM9CZcSN2YSNFrdcn__pxyczBki3EDoS1FC3HAF4jZzKZF1DNOKxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82202" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyNEjtOoS6VnOnU11kvRCcU6PieVd6rlOWxJa__dxcrSjNhRC96OmdGxr-HGKHypfSGx9tAVrRPKkX2aERpXdTU-q4c0WuoIP7XfkZrzOady6dbo0eQy-ryXvvkTWK40ameiajv6LK69cB2zeGxMZQFD7HK2k0cNFJNWpxF34OShB9EFZ-8MLAiuIByJcZZQ1kuuWQLC4EMsAiHnxEc3XTUjY67KDKyKzD5FBBmZ-mP5tXrp_2mX9GUYi3woaVeBAVxycX2sG2LydD_StHbNB8WQdJYprgUOQ8LP60SIWxiYarN4FIIBcUlafg3bZR8dbcwOzvtRl1fzpTF0mbw2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nr2JC_ejLyrtuvkqBGoZ-8ug10HjLiiqF0MyIgKW7SgNVJN4sdpuaF3pXkWNvcbneXfEXSuSYbJBY2EoDMwGf8wURgCr-wKq-P0c3SAAgflmq66edOlQHS1cE9voZJnwjmy2nUp8SrHlQYZMPxDxeiLUkbQuBGsH4M5JDTvuiogVW4NjRy0wiXHxV7bHTiFR2aDVWn25H-KaBaWDRasZWwzFS6qgA6VZX_0kGeMDCa5NxF0qZhMfvBEyYQK7-Fxl6kOBsBiEL69JtvP1-3dkZd7Djyk3iPSI96ePzzO0sA4NPnexyH84tHDPpUw3XIq7rekR7QHX7dJ-anxubjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCJzAO6C-ZBCJrSMYb1lMw4H_bsJ4PjqUn-ZIipHI7Zu7956SVJVa829ToM4QyfDZwX0LRZTScyyHV1nTqXYT7Ffr5Zhk16mdc_2lKozFYc8Lrq97212YNJnm5fbWx1GpC0G6kDGTvI20Ub_tmMmuX6t68hc5UhJUTfW_-p2B09gmAk3m0OorJnKIEls2CaIIVdvYSXPCKclcIya2Ir7OmnQq1NMlgq57e2Kw7xitbiVHN6CAy1UJZuDgcrUwlL0T7y2U5f70iIYRA7xgPYh5fBUlTTNZPKfVlaBFAct8IQFmJjgJoFzB2QPuutE6VzKDMtZXI_fM9Vf-0HcnRdr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5R-0_fF6j8qPPUqWb7QKt-gMKwBOy2SEzJmww0SGXmiNVONunimvM2Jvgbrz4vHbwvWyN-FOYOABCWoKbuv67sm6AOLPcPeYbCm0MYtd0LD0VDw4J4KdnGHGbAcd2plZMkVuPWlU7WRl_aAoQTVLXTzKdE9J9KfrbCIe4TFMyIYUsLSadjWwyN_dsrhGvxvyVeObKg8w5w_r6WSmhjFV3-ekE_VbPwUeYiYBuX3cRTyRiGfiuajKDf3I_99VKS_o4HgrAv-2BcIg2V3nQrVXa4U9d2if1vB7yC4edKrNee9plp1JaZR5UAVZ8ckdGeHd9JHq3W2DOZelilqFYHj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6qhnp_6Qqa3C4ks0tvmTE6rqokaJ9oYGPHet_qWMRMzBTfXg1Dqe3_bigFEZ8_C0QCVuRuYtSc1ABL_tfcts4_v5qZsQG_wmK2rCklgp9yovCif8enWri6mnBU0ja2rm69yWO-IxB23SxKynDMNQNdPdyMRUCATcBzaK_RUYNWsH_cqp6m4VctQ4gcAvMff89QmmhNVy2l44TbvD7HzAm1DwCd9z5DpsMfJ-skWeeLJxWAXohn-ZhL5GZh09wr5Cf6y0xcrJGP1QyyWgaaAkz326X-p4KRmR9zMy5hbVbwn-4iGWxL9ZzXXK041_EMU6WZ7uLvRXerpdsfv0tCxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJFSpuw3DrYJkrybMFOFjiRRZYKCcE-QAIfu7KPY5teZgWjgK3VYAPlyArRqS2KNE4N9leadCfzz3wcTblEEKCaDo-VcY7dmDha49URW40z_SC07kc0Lg6_tCXVo-x7XuJLah5lFH-87UsauI83s2vYluk9t0vYZJ9FF8dJ3eDIsYFSKOdIyAg-keMysKMwA_yRnQsAeP2B8WbSwToxSgQ9ru8adqjb3ilay1rChh6s367y5XzBtE-UwCg2nTGDDCkdZbbKB_oNeMYR63NmUb3zFHy6AwkiQMclc_xx_FbAzRHGxVBwiklEvayz1lLxdFzXN69PYxRsPMeuABeY4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Oiby7X1Ahx5zUu7qFQybqtAIHRR12Ev4VxocOhIu7BGasP8RBa3aAVebydGwN_pcVliFEyzcROOkZc1Isnk4WIkjj3124pPr50cdoHRD-NwynPLQQH_uQ93sGGrBcBUpG5S7tuSniZgxnuXbzta9XIjuilxoHt67v0HSEubhGswZBvGXdUaaabG_CKETPl5WafJj_g3Evr4gO_50J3F8avBHeBAdM3FrPO0X7qkPm5QuFKwkv01cA9INhsyzbm6ucO8bGb5ZenlI1MHrZWcUk34_ARydhhPjgpjCkvMznzaGXH8s3My4-itDvK7uA12-zqvWGL-mFUUD33czFUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82185" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEpGHA65w03_qDzkRc5-X-QVoHNxRpBv7pj_6fsR67CalRhR1FgDsznaUa4-408oqotCuwzhjZt_t5yCfnXHLNlqfy4oQuJ5yBaQhXie6oWne0V6ZFEvu0oo91VxSWPPucQefRIQIsnrpbveTqUr8cbZjYtvZGhQfzGKwDH4irFzRV9j0eO5mFwD9P4i4fU6MNfI-vwBn2vDbPk6UgfyRoWcd4ZxFrKWLPD3VBOvNXzhkS4vAsK0YGqUr0NjY6YzutPIQLRO9A99noUpX9ytIUkAGdSZR_R32_oM3R0FyCfBMOhaYBHhZyPbr8xzkSrmJMGwpp3ENE8UO3aQWjJOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0OwbAbL15KK2Wc0RGOcAL_UoRr62BKT64anwLPXeCGnCBt9kieMNii_0ljnLVVTsU1ZYrbCJ6X70umnp8Z5v0TIdyLoOQGElRvMA5iJL7zEf_9WzmNJYFGSMf7sW5VAC8zxoc0oDPU7ZLiUs6ce9Q32pCHxxT7ZAXtHTtIvkxnYFPTo01dQ9llWHhjIZHlmDYRAWoEhFV5Als1GSPc1CIhCmlzGX0MFbGvCrvP_DHEamPnUUGBBao0zaQIj5XxHp5MbhAvYLOGP_HyVgb9wBkoAityoQi0ufcUqtJLjFVeX8Wtci9T-f8eUAE5VxEKESWHnimKvDMV-3SAcOoG5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl8XKrhqeEwBjyuvazBpAmlnOZWoCLMu_7PtEtZFXTZrnyNZkurEAL8mkV1AR3y3w1euNnBTdXxxdAUoEIBOwd8RPXKU5aYJLh_3KAT9UAL55WFy0AC2_S7rDvp3k5xh1EuzwzjmZgR4wXWPCrNeoawKn1UgQx-0WXO6u_JPAiSc5A3HvkiyQOPU3EirsK09906nO6ygbGsRmT-QGp3AS63nagYzTyLDLrlPd7mzxCtl2v2pA6xF7vv5_SxHcpXTV29AvecIqg3RFewWpcFc5Y6ycla9ZCcqoSRKSISYtIpW0hplGU9hbFvZddX1GpdA1uV4HqkCsjLTXRFP4K0JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4GNTPXGbC_Oxqpsp-jGw2rCnGznN500CU7CXKjnZiVDxkIZw08pFxpRI-NJVpTbUwp0_ozPzt8qn6okpUh_Ab53-Sp24BcUOvq5mS_d7qPIpAP4SEOLpCp_4_XbZvaa7OVV3dyDuafhF27fKbFWCqhQijv9da-LaC3wIsbF6ClKF3csrokmS1h4WtocnlqjZtGTOvx0ufAgycQHP83nAQeH-dJM5pXvqiUo-P1sftCuKpDxBZhpgYcP2wj1dQ0MbE5uLkBJXn-nNK-LMs40OdWWzc8jE4dOTHmB6dH7YODnB9OojT3WmX-Y3Hb3HC2IS1Wp-m9_oT_kiNTxVnAgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcO1YKNmGo9myl9XBhJJEd1q3KnqyC2LKv9yL_ktgjy4KWzZaBZ6UMNJCqDMUxBUoYDIZqqtIsB4l8tRKD_hfQuhQDs1hPomDSYtFvD6xf6QYwUpIZbWxUosC0q9C0L2j9k20QWp6urvsCixsgDNUZZZMe4rY1wSqHGgo3owjZECC9-nuUa775ZMVmZVi-28gtDRibL3RZBpvukUh_gtg8LOW5YkulwllObnGSbOAdElyWdDbfzcdhuy4Qav03f3GLX4omk_ZTAcnnknrESQwayV3qqNF_Oy7qP5vJIaCUUZznAMvkwEEQHn_pHUzQS4mtZJzXLULNb0cJ7aZS1Ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=B0kpjaA70dPJztIhOHxtU1LmBEuUWKdj-gh65oPqz2cHa3b-J3n7WrjfIy57Mo7U78Uw_OdqvHUFAAbsN-0LQS-PttpqmbYdXPtsLt7x0LXHxXXaqQBspXGIMaAIFDzV9P_97fJ8YH4M3XQBj7INkj13ZG6N5w6PGsKluZbpt87jqWOqdscpPtiy60-yOHiN_2YQp5PE2kCXTXOEkgJCuBbG5SlGqgcmimFd2Q_yI1vKpyeD_WztOByZujd8DkpxScp5hz9mTY4YG7IZRmVjxv3b5EJDwoub_UOIN6uBMPyQbDIBx-fzaW5n3zuLET7wblKtdj1OiQcKefuF9ZNuBqx7HQGMf7byLEvq1-RUlkPYZIiCcwRWMdaTb4YoXQkAeZg6jPTqIxptSo20KFhWZu07ZKi4GemjVK69A0Zqks6I2fMgDGytmTNvv_PBoK9r6x5iWnHSO3VCpErxAndVfo123xmB-P9A3uPdOdItmT6A-PmBpvh_E7qASZfcSOInSNHQRNVeDTytInZ9eygMu3yxxl8MR2DK1TibJJyt8PyrTaEP3iFO_CzhrYFLuUHx_ln93CFrmzZdh_EkpkhlpDJrN2MMwwh_tQXbpuchMix01T_AOvvZYBi7owWan2iENl_2atZL5PEPU1NXFpAZ6KaHmJMGblnRjM0nx-ck2mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=B0kpjaA70dPJztIhOHxtU1LmBEuUWKdj-gh65oPqz2cHa3b-J3n7WrjfIy57Mo7U78Uw_OdqvHUFAAbsN-0LQS-PttpqmbYdXPtsLt7x0LXHxXXaqQBspXGIMaAIFDzV9P_97fJ8YH4M3XQBj7INkj13ZG6N5w6PGsKluZbpt87jqWOqdscpPtiy60-yOHiN_2YQp5PE2kCXTXOEkgJCuBbG5SlGqgcmimFd2Q_yI1vKpyeD_WztOByZujd8DkpxScp5hz9mTY4YG7IZRmVjxv3b5EJDwoub_UOIN6uBMPyQbDIBx-fzaW5n3zuLET7wblKtdj1OiQcKefuF9ZNuBqx7HQGMf7byLEvq1-RUlkPYZIiCcwRWMdaTb4YoXQkAeZg6jPTqIxptSo20KFhWZu07ZKi4GemjVK69A0Zqks6I2fMgDGytmTNvv_PBoK9r6x5iWnHSO3VCpErxAndVfo123xmB-P9A3uPdOdItmT6A-PmBpvh_E7qASZfcSOInSNHQRNVeDTytInZ9eygMu3yxxl8MR2DK1TibJJyt8PyrTaEP3iFO_CzhrYFLuUHx_ln93CFrmzZdh_EkpkhlpDJrN2MMwwh_tQXbpuchMix01T_AOvvZYBi7owWan2iENl_2atZL5PEPU1NXFpAZ6KaHmJMGblnRjM0nx-ck2mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUvfcCTVCeca3X6wdIjnNg_GOrWbIrWoqJnmLIs7qcFeOVSSMs-h3Uxi6BrUGTJzsF7SAf1-GlEyKgfZP1UQKN_jWpefkqekhxZ7LspZYweeXUNsYfiE8-5_KHUyutqiYNeKcz70alZkRXVMFf2npV8oo-y9Q_2WkA3Owv3Ln6F4eHuthisOPsMdP6tsJmxkwA3neF7o79I6zql1a5ADYo06UKoKo94LMqRhf85TPCeDcKCnE58YaShEc3jT4vbkdF_GbkcRxWzqFBY_-68_9FE-zi2kOklZP5AkfI92p6nYK-Bnw3gogwpz4Am6OU5MPoK1AfQW_INxxN6e9ftPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=SoFj_sUsKPYy4I_Vu5oFMTXYSvwNXYeym5aLQ0xklKWXoAa-KOvLPoF1puo7BJCrMA58s02EUfeICRdZzsqKZjfRlAlO1d0iY54SW6fiKcawLxTvkR18EzacI0smnesToAyMrHLwEDOxdvyLgvxe36DdvPKwMPbx6qlDzR5BSbvqeswKtdUOUWfcyVHKYB3gKe2m8yxSWlv_j1OmHm1Hoj4IlROny8UVWlMp-zzvNdiND1pA3-YOZqk4cLBEEs634ZyeMXpW9Oe7PKek7a2GOmis12ZMdR4DyFigHPohBUt481AAQRXQwK2_VCmVN2NN-OM7XyZp4VNdoygiTwUTMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=SoFj_sUsKPYy4I_Vu5oFMTXYSvwNXYeym5aLQ0xklKWXoAa-KOvLPoF1puo7BJCrMA58s02EUfeICRdZzsqKZjfRlAlO1d0iY54SW6fiKcawLxTvkR18EzacI0smnesToAyMrHLwEDOxdvyLgvxe36DdvPKwMPbx6qlDzR5BSbvqeswKtdUOUWfcyVHKYB3gKe2m8yxSWlv_j1OmHm1Hoj4IlROny8UVWlMp-zzvNdiND1pA3-YOZqk4cLBEEs634ZyeMXpW9Oe7PKek7a2GOmis12ZMdR4DyFigHPohBUt481AAQRXQwK2_VCmVN2NN-OM7XyZp4VNdoygiTwUTMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erjiLW0trWdjpOKOE_WsQ0DFlFqIpHzwVVxEzaciGg2IQpgGER6mdktsVnFnEAlK5SbFEfUC4X87wDfsNW9cnwbQqaY8GeYVAruR_9WisljVJTWRlhQaf58QtMOZ8O_kpMNhz-wa5Fhw1sL2BwpiQShhH75r7QH0LfiTAbJtDlxNt2maoVgisUtMaSKRLtyxD_daFr2tyHPq27zvyrlpJYjV9CjwwGd7ADSBlD0vgPI6nJPl3HiCM_q13wk41PPfu8pMPFRycikc_yzB_cwmK08WxovaVZL1wLp1j3t9ZjqhfY_CPX3_4ebVblSYbQuOGZO7o1JumyO2yCq58UYi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIk8H9opCVlXf03OqLwZyt_qAAR7J8GBrmw-lCFDJ9luhaLS0NI5Z8BsT9SrRrfeSnBAiDXbfJSWUGaLGtKGP4EuqYiqC_7eofmeyUOk7K5BpQVpDVes9RA_zDZvJDkDSM98SPWBUXpmlrfY4DJ30BbS5Nh8qbkDqsD1BJpBVFwVk5JUyTWVQEBAlfC1JztSlOA64GIlSK2SMWZwDv_5TqQqbGlJLbibtuccha85ED4mHbYJqxEHx6-bRBTQm4h7ZHubAm0u5YrMvTwtgATP83F6yWdvixzLfmPGbd-CYiH8zMBdpMSgFNF-TXUjHAU8q_yW6Vurtf64PYSBwQwN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKY9-NytzLQMBnO8gWMRO7vqsEakxT6Y6d8KqCK4IVbAZFw7QwvsVeLf2rErANNNcOvAlGqM0yy2xtCUzORWTAcMsvDHrhVTWpaXliKDTO2DRFShIakQgVe87DvA1OeZ5VeddJ-wIG5YMXHpwj_FyStpi9WiS78m532CxHpWtTJhlJqrko5nQK0Bwq-P6wOWrndOCIGYZFyu8b2-6mRHgRS6u5lwWWRnybAMANxO0oskTl_O1u-HcotcwQQj3c5m4gjM2rd8Rtf0IwlMX3Yd3XOa4284gQVEN8pr3f58pMyGCdjpqPdGaFRwP2aquQgtgCRGyTlo4fNYHrD4MVjzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQzZONZg92OOR74LjwxVknmy7Bh61-O02G9IKScDSJyDddoBZt9TzsaIDdeakE-MuUAxSJPRWQu-3d0ICDRvYDXnrcXP9CDKqHGwpqSuBMg5Hsw6QM2qVmwDR70NEV6aH_5knk-O3kOVLo1UeoCFQ41tuEFMUyBoorHZK2QwlypIdIipXVLkxmFXYSHCwEynIkd4Vn-XFAEdWwGVG0VTdMdcugb4dHZ1Tj7P5bdYHFt06cKqpf15U25M07MWLTPOFwNTISBgyy9IRfHOHk1WlFqnecEzd_RFTsrH3M5wuSsnG4f-2joZdrH5eN6rPopU8jZO54KkNsq9qIp7H31d0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=ATv8IM57MqnUNPPmrhnGvuIapkaCLDuiRKmXgLy9-sUp420QNJHcnefIY2uXzCKMRPjGXEQ0fezsYWNVGYXMQKBLw4tpipEOePnl73skgee0G2X1zB1RQnaguOCFkabrwqnFWx0NY0auhOHRoZV0vaRXO_mbd3vr8ybmR26BzsIYCzDog_GrnPK4QPFD5R5WrnjdiSuo6jLhjl_PldJlvmAol2ekfEhMp33Y1Xx7Vsf5yFDHtvIrufwdDPNVTNPRQ6ckWY4I88pO3vug1RgSdZD9qeh0RJaoV_2tTI3buAT3M9Ju_11obHTK169LmLvT7ZpufGyjbmteaoBre0VMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=ATv8IM57MqnUNPPmrhnGvuIapkaCLDuiRKmXgLy9-sUp420QNJHcnefIY2uXzCKMRPjGXEQ0fezsYWNVGYXMQKBLw4tpipEOePnl73skgee0G2X1zB1RQnaguOCFkabrwqnFWx0NY0auhOHRoZV0vaRXO_mbd3vr8ybmR26BzsIYCzDog_GrnPK4QPFD5R5WrnjdiSuo6jLhjl_PldJlvmAol2ekfEhMp33Y1Xx7Vsf5yFDHtvIrufwdDPNVTNPRQ6ckWY4I88pO3vug1RgSdZD9qeh0RJaoV_2tTI3buAT3M9Ju_11obHTK169LmLvT7ZpufGyjbmteaoBre0VMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2cUuvkRR6xK9CdFP0pWx6yegkn1Jw2qD0CK26XB54rS0LgeG-Yf09ObWikupeK5H3N0u9hF2Tjw8ahHmjWuXfSnoyKDW8Xey3n52xs_glM2zcz93qwvgU87Im6ZbIiBLIfmnvnTOuPa-vzk_qqifGE1bGioU7JP8iGAYc6uxVVsMeKytJnAy54YTgOYZu5q8sk693_W8qvkCzzp2Xm0I7m68eLPu6qUV4ZEen4BkKTueIYVfneG2RzaMwiaGXHVds9DV4vcRfl-5K0KLyh8OqWKTF4kge8vx6nBK8cQ3vHDs_wX_cbXxJQ46-cSmyRrwYfyiWZqxsALBepuo3EUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بزار جیبت بیبی</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82168" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82167" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL5Fv_XLIs8XfrygulwvfVn12TSW1K4gvTvBSMdTkqhReMquExhrZbaL4mCK5BzYQiTZxYmXqEq5ECF3B2S8zqdKIlRInCFuaM9Rswp5KHbOEqb9odHxHRiTwcqxR8Buc07JpKLKvO98f3HpYw6NrbnNi0vDw5izJmzona0Kb_2y8D5R9n8Ttdo0yDTH7SfVcAS3pHkNMZtgr2rDJwzirrwXHULjCTT7BFKSoI4T42eKKq4fl6d14BYK9oNAHVGMda6Wg62xmTc-whnCK46XoyIPFZzuGeiRilwuNjpO2yeB30H-qBRVNYyntkHkLncRA1R3rgC8HOvMK13BLSaUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82166" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82164" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbnR88iywTaRbhyeeXbvkyvuQTE6bEm5R30I2VqKR9b_VC89HlNk3uimdb5uYn9-2UQz1FMKyBeHXk5biUbm4FTPOruztnSw-sABjlHX-bkvh-l4E4qFoXJ83zfjfmo0tlCCBU2ea6MHeEXE2a3xaFz1VUR7IgdLIFO-1Burkb7C_X2AQdizeVzGWZfs8GOSUHzm69JP3iacdl5IPPVa6LCQZV1jE4RO1_mw_1bjzd9dbiRv2YAHK9YuM3KCDjZOVT7I3MCWh0RxKNQrVM3P4SwzfSU1fcdpxGlKH3wC5lsHsnGwcZJ140BYvrwjlJFFnpARGKars8TCQEBnLjoN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82163" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=seug9quxKIDbXAkhm6IovM80V_wH6FLgm1Z4JsiRmX80RyFoMmWFmSadAs6s841LqPoj6z0zPDIC--N915b1luySHgkthxLgfsieoEGUTF8yoLRKuKUo8_Te9Bd1rO0gP2VlKZyUEK9snwAe5_IVy2QqusFYhJCjHS3KGGj7MmIkNc7ZqibZgaQ62pPfcUw4pMF5O81B15JNc6g5U91HA0J0M36ObGFoscOUxGcI85qV8W_qZ1B_7DhvwRoEJzpTWMw1K1xn6VVZNCGCQ_j8uOettnBHnUjvwruzIgfDMBS7cs4VV_hw8VboaxjCTjpeOEmLZu2CMscTmBYqH2lCoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=seug9quxKIDbXAkhm6IovM80V_wH6FLgm1Z4JsiRmX80RyFoMmWFmSadAs6s841LqPoj6z0zPDIC--N915b1luySHgkthxLgfsieoEGUTF8yoLRKuKUo8_Te9Bd1rO0gP2VlKZyUEK9snwAe5_IVy2QqusFYhJCjHS3KGGj7MmIkNc7ZqibZgaQ62pPfcUw4pMF5O81B15JNc6g5U91HA0J0M36ObGFoscOUxGcI85qV8W_qZ1B_7DhvwRoEJzpTWMw1K1xn6VVZNCGCQ_j8uOettnBHnUjvwruzIgfDMBS7cs4VV_hw8VboaxjCTjpeOEmLZu2CMscTmBYqH2lCoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82162" target="_blank">📅 17:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82161" target="_blank">📅 16:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnZiBkw6h1YHxG1SQjXLTym3RJFR-CWFBXOHqGV4I05_ojKGBV7sYPmlB7Y89Xkujg6-61v0FvZz5NFPn4hdmb0Q9BPEuz_b90HmtqpahcpjtjE7l5MyelKGzH4Q5EZNmWumTva204HfMc9k-kR_2IkYTL3ThRVrctwbrKBTTt4JOaZfUTlYRG_XHcbv3_KFDUuZXXl1dllwsXqgF0t2PDhu7mm8x4sEDEQyw2HFr65OL9y9g2XWQhpqVKFOxNJ8HPq0HmV_6A0vwQRNHvrvVOCiNBMiDKYsukUn1CRU5De6WjTUVdxvo5pMseOxWi7QQvrrsPMBUcxfzVyqU7BGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویرو هربار میبینم جمله "آقایییی محترمممم" میاد تو ذهنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82159" target="_blank">📅 12:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmMvXXA7AaTftkNq9q8FdANdEBbxIokkhQmjGryRX5srnqkjOHJAgDQqudoo8vxel0W8591l-0de_MJipYBTr64JHiPWwSUDxrWSHwb9XA3YmzoTgP2Cz5D5-ite-GYqx4dH7yIKouGGlvhEizFSBxKC2DVYKDB-FwEow6FRCO5T7jfW8RECzZfiotwPBY0S6sBZmNPSv9cRKAdX-pmqfMnUZVde0fDkYvs53jiOA5Pr79fiRkKsO-KFFhGv3CnCVvx3uIfhWrYJVptX_TjTAtzO_m7IezyU0H0InypmHWcq48bU3Bh6ln4wk1zY3pdKatmMAGbgGxWkQcHrQijbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه ریدم تو سلیقت
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82158" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82157" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82155" target="_blank">📅 09:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یعنی نتانیاهو با اونهمه قدرت نفهمیده پوریا زراعتی آدم جمهوری اسلامیه و بردتش اسرائیل و باهاش مصاحبه کرده ولی چارتا کصخل تو توییتر فهمیدن؟</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82154" target="_blank">📅 08:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">درکل فیلم قشنگی‌ بود بشینید ببینید بفهمید تو چه کشور گوهی زندگی میکنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82153" target="_blank">📅 03:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=UgzVVxGf7t0IKjkYdfEY12nF-jmoHeb-8d6QIwyZW-MA-TJW4WTClnZtkXGn7NtqVXiTYoTcVv9sHrvcKoaYLfTRlC5pZ3U6a65f_GWQome37hcuAIuwhPx-RbNYQXUabbqgbzW7lHCmkJnddBjuDzWrJw4nMbhFc8fmaar3yuoDPLPFLy8-gMjseYO8ER0Caj3oEfYOsmA0mdoHFlEmmi422eWXrw2uqtjt8dgaXi5stkxYWTTkYB3L80GOpQ9-PXHpmy-V6bHI4o-hAJW_nL2BA_xlSAY1TvD6HSIkvzvzhZGl4iCed7-qEgllHslpkyaQplB6bHJKyy5_6wxKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=UgzVVxGf7t0IKjkYdfEY12nF-jmoHeb-8d6QIwyZW-MA-TJW4WTClnZtkXGn7NtqVXiTYoTcVv9sHrvcKoaYLfTRlC5pZ3U6a65f_GWQome37hcuAIuwhPx-RbNYQXUabbqgbzW7lHCmkJnddBjuDzWrJw4nMbhFc8fmaar3yuoDPLPFLy8-gMjseYO8ER0Caj3oEfYOsmA0mdoHFlEmmi422eWXrw2uqtjt8dgaXi5stkxYWTTkYB3L80GOpQ9-PXHpmy-V6bHI4o-hAJW_nL2BA_xlSAY1TvD6HSIkvzvzhZGl4iCed7-qEgllHslpkyaQplB6bHJKyy5_6wxKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82152" target="_blank">📅 02:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82150" target="_blank">📅 02:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82148" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAktVViP6vkGOzXxR16ob-fhzq9wJ2xHZB4axp34U9ACblxfUW9t4zSXW64CSf3-cwze8L0JrMqWpeV5WBTCpImi5k6aMLticImgs-FVSoXFxr5AdQxIShRymDtwvzCaoEx3L-pjLWVIELwWYbdLsJfxbZi5670HIXS4nwuZix2fp-j4cWXqv62X-HmWY1PgeoPr60HwcbBjW29r3IsptEksAg02i6AOiO61UUA893FOaJlm-kRZfAi2ODLamcT441gkxo_nZHET0ZYnWzr0L116wdm5m84DO4eYvFiIAxTwmQZ4u5Vs_-qzYHNlbuY9benUD3P-1r4tKMLjwaT6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اوکراین هم عده‌ای از گیمرهایی رو که مأموریت هلی‌کوپتر GTA رو با موفقیت گذروندن استخدام و مأمور کنترل پهپاد‌های انتحاری کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82147" target="_blank">📅 00:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پاول گیفت تدی تروریست داد بیرون
🎁</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82146" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کیرم تو توپ طلا اگه به کسی جز کوارتسخلیا برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82145" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGt8VLiwX47x4yV5Y1UCO7ikq8zRumF7JsAM2J9Xkv-OZHOR6DEpZm1jG_45GxvzQtuIwMY0V_BzdejlrmxtqoxDtRuo_OOwYE-enLvAdZdU5Q_EmXesTNbN3xKGa4aQnOJO5a3wAC0Tuew8s9E_pni7BiEg1w_Uu0umjbqw7l1cDpO-6FJaUPwctyu59TkegS1JZzuqq9XPqZggbZxp2i6L1gJXhXwV7O23tL93hu8ATGXGp79UzR3480WviWYCbQMVgzhOxIbuFp4iBlQmG3Lu1t2MmXZkHewKKQXG-pz8VehSkc5V7_yiZ5toQcIn7oohCKOAq7_U8q_xuzeWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به قدرت جدید فوتبال ملی اروپا, هلند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82144" target="_blank">📅 22:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">البته ما کی باشیم نظر بدیم، چین برامون بنزین میخره</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82140" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موضوع سادس، نه میتونن بنزین تولید کنن، نه پول خرید بنزین دارن، حتی اگه پولشم داشته باشن بخاطر محاصره دریایی نمیتونن وارد کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82139" target="_blank">📅 21:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تورو ناموستون شما دیگه حتی با افغانستانم نجنگید ممنون.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82138" target="_blank">📅 21:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">داشتم فکر میکردم ماشینو بزارم خونه با مترو رفت و امد کنم یادم اومد کلا ۴ تا استان ایران مترو دارن</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82137" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قیمتا دقیق:  نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان  نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان  نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان  نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)  پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82136" target="_blank">📅 21:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82135">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82134" target="_blank">📅 21:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82133">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82133" target="_blank">📅 21:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82132">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟ کدوم کصخلی میاد به ماشین ایرانی بنزین لیتری ۹۰‌تومن بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82132" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82131">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صبم خلسه اومد این ویسو داد بهش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82131" target="_blank">📅 20:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مگه دیروز تو البوم فیت نداشتن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82130" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کچی میخواد به خلسه دیس بده</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82129" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/il6lmvhdzkY7De4UBOUJa2Gt_NqV6VOizgFDQOPTbQkNjBbmy-KRsBZ-VinUDfJ3_3N8ZU6i0UJNli8fBspm75159HuZYYX77YW2Qq32WGAezMgDMW6y1_58MS2AA6MtPMG01uv_VFBKU-zCK8Sr6RQCPt-pE0qZFHYWQIF5yzDNeZkXA1vYJz_9cyJnbn84h4AHf4fMuMqircuyRfJhF-6wfjgetp0txoG3SJtwcejV4a68QCL_5o3STrt-SIaODFc1abnO21RsCmPVfKAhOSNRmmx74Bu-GhTlnGvoveUeDaWX9ASJAKCGd1RdP3p6ur25_3ut722NKgxsoUT3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادت باشه اولین چیزی که توی استایلت باید بدرخشه، موهاته.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82128" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82127" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ-hdyqbC5j7GR6SpbGueXIqrtBnMBzsml7yPMhbDujX-n36XqK14W8bFEHKBZDFpYIdkeNSJ1NPmkQn23r59fkLW8sX_0gwbOkSDtke2daol-QkWIapcEh9p03iIlKkA10druR-wtMxA9YY7fEYJMBA0fWjjnhYyP3EWpPfuXS_MJpoFXzPm_e5bDFOfpGl3_A3eb41qatgTQgY8oQnOLfsKihSZGSBdGWFtyhBsmGlRHKboMhLOjsvuo3FLrrLV6thBnNjo3vEG1Qxogt5g6UkjsxjK5FE2fpnRS9eNg7YoTinhWWBGFK3uoAOTy-m2pCm_OFIiGP6-RzJV4tZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلنوشته مسی برای پدر:
اینکه دیگه نبینمت و نتونم باهات حرف بزنم، واقعاً برام سخته. میدونستم روزای سختی داشتی و رنج می‌کشیدی، ولی اصلاً فکر نمیکردم اینقدر زود بری. هنوز کلی چیز داشتیم که باید باهم تجربه می‌کردیم.
همیشه دوست داشتی آخرین جام جهانی رو بازی کنم. چند روز قبل شروع مسابقات حالت بدتر شد، ولی من ادامه دادم. رسیدیم به فینال، اما تو دیه نتونستی اونجا کنارمون باشی. دلم می‌خواست قهرمان بشیم و جام رو برات بیارم… ولی نشد.
واقعاً نمیدونم بدون تو چطوری باید ادامه بدم. حتی نمیدونم تا کی قراره فوتبال بازی کنم. تو از همون بچگی همیشه کنارم بودی؛ منو می‌بردی تمرین، بازی هامو میدیدی و هیچ‌وقت تنهام نمی‌ذاشتی.
خیلی دلم برات تنگ میشه، ولی میدونم همیشه یه جایی کنارمی. راحت بخواب بابا… از اون بالا هم مثل همیشه حواست به ما باشه.
ممنونم برای همه‌چی. دوستت دارم بابا
❤
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82125" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQM_rfxwtYXln43Qetu9TPIGZY4ENXOF9gAcFNUwdodVvD7lT-WaB9Owv0fyqvoAFtUc98BXWoD11WeDEAKF9rl1bL0J35FC-IJHjpgZN9wgX2gn5k7NdTLLwliV5WmMe1CoVPT21jWVi2W48269Ck_28ISsAgle7a7rfjY0mk5naunnfvVUn6koqcBSQWkef9RYyuS4rzwwAZIi1DbjjSEQuo2kBGMtmIeONkkeILbH_1L9HA3vjJVyQiQI92_rJ0-68WifkPOjj0lFZEButqNHxP8AOc54L-YliGXkHQV8vbC06Ok4lAkiUETJ3s7y0XACYQY82H91BQNd7PqUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر پوریا ادرویت به سپهر خلسه ویو بده؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82124" target="_blank">📅 18:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKEInFNNrV-MoQav-Zo3Ggik8ZxiYAvsaP8a2rCi078XdqfJ4YYVgzBiqIrFagsljQg-jxMM_nzQ-T_RPcuBCwY5Egv9crspYFb2VdgZl7lLCw06ioYbbL6HQXDHKz7QVdhuROzMYaKHX99zjRJSWSt34s4MqT_ww7ChEm5ZAv3gtcViqaiPQM_-_e-uL_1b6f2MdmULx7pddaakQZJMBp33sDtf_wMcSnH2moQINiaj8YMFEJwewiBSnrPpIbFCGZ3U3E4iz42QlROb70NPy2CCZEF2uHLIq345Y7BJj2R4rswerJmBezJTxgetXnM5PaopUGmtkO-mQVsLJ15mJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر
پوریا ادرویت به سپهر خلسه ویو بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82123" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpCew-PseRKCWjdYQPnU7_GqiwRmzjeQbtnW2g1C9Cc1wrp9PWzHDE4Q-Bca6bVu0cxPaNUJX1ehuF42zVF7g0-P3G-GJqV0Df67kS0SdUGB-5y8vQWmcL2qFE717cbEDtlQUvyl_e1EZaMqzaHyzkRYffrpK_WTVySXlzxSxgZ6G3C7grTGsO9q6jbui5xKex_Qdx59JLEufjLZcF1MGGv6l69Mme10ksqP41VS4Y-OSakx-dQNn02-s1jqglgwhE5uvJ7WKMqPunSFD6624W7HEzvP5ugJ1eh9v27fyg3iCWIB-xTOrRJx4JbO2J6DVw7dsRwhkyDHq8eh5h5jqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی، این یارو که چتای ملتفت رو پخش کرده یه ریکورد هم از پیوی مهدیار پخش کرد که بهش عکس یهویی داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82122" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.   Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82121" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq26zohZyM7HWfwhucuQeCDmVYHQvc3rMPA50LoSkWrffapmxINIZ2FC6YQXebaW3cq4tihN1bIETW-7nulgPWgn3e-aQGIdRgTp7E99iowa1WIkSccGAkrsrb3vqf2ukswyclWvbj5Zrzvf8clBsDNMCleBDt6tOGQU5TxC-MB7IxB0FMtwIFWhF-qaI-Zs1dcs2JNkkIHrwcNtpxqbrKJAGkfJ5LXAvwKV9uDEU4YprY402LT4rt8ikjQfopdfv2hjxI2l6qm32DAx89LfivjJyAkU5I4t4Xu5TKkKSkUUf1y_n6Crh49X5_vTTgPdGCsoFIqYsfWNSVVBk0GvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82120" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خفه شید عشقم آقای واحدی ترک داده</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82119" target="_blank">📅 17:48 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
