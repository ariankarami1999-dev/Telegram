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
<img src="https://cdn4.telesco.pe/file/K0TdvlDyrlflgUanRmE1jNKVxbAFJCy0iFNyTEzE6dnL51eG1_dty_FYKoJgYXNpHLreza9LCvpcCQReBQZVXP2vAiHxbSnUfBIWb6b9v3yDPIJYbRpWzuVLR77tUHy_Dq8Zh4hvTLLqdHG_zB1mKMlGqwPZ4CJcHo5JRYdrkswt56qzv0RwFbUmMN3HAEFc95axDkrGkKo_s7NMoWdhhnmJDsy-8Q1c3hdrgoEM7fiSsDJnjTUwTbuZd993BgZn0jPtLyfJr2Y9OwcMlcbQd8JXx6Oi3IP5JdXI9SN_fumJ6A6dVHk8YsljlNi1eOUNLOdDn7gWbGEpF5Jd8kL7dA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-79733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCH6DFUT4VEZmxcWphkhZDgZkkvYRmFodgBTp1HyzV9P5HdYTSwAWuqONvFSA5gGP1gTZbQxJa3p3c6dDwXJ7ompzf3gRQBqbHV4sNduPXGUl9Ji3bFMah1exA-Q4eErnDQ_Nlr9gvBIoxQIIdYTpBv207qLrbp3b5UYPQ48HWRuf4vqj56HirLNeza8pPIUcnq-LZGpT_w8JWZEWbN_kOnQClCnFLEwU843MGDUYuWm0yu4y1OzByJ1R2vrg1NCxNcUFtuqyIoFYqdH4m0k0njZEIFpBsucTQ0ztMg7dnYsTYkiNDKRQ8VhfDRyKKWdvbdCNvZ0S7KvFN_aMlLEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در استان فارس یک دختر ۱۳ ساله با مراجعه به دادستانی، پدر خود را که اشیای باستانی گران را در خانه پنهان کرده بود لو داد.
پدر این دختر نیز بلافاصله بازداشت و روانه زندان شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/funhiphop/79733" target="_blank">📅 19:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxggGTQX_Q7zlNacecEODzMNggQtkiHNaCon6KIlrqF9jMGuil_NeGL9uWz6A4_9ZhAAU5BtnrUpFy6qIqXnMpn1gW2SnNcDEqF6CaIgVlyIyaTqUDMWWv7SN89yTHKkqrP4qeEw6l9ahzdwJQbjoof3-qpbwnCqwMBtAHcbghMi3AAm-j7efMZSrE97jiRGYsXFzgcfnrn7ryqUeStI5L3zSX45B6wcsXHHJ-qy0C4Vlkv_GwVYnMbj1a0VtZPH3m4I1pjPvrcN-0HVs1LjintuXo_fLiMpD96GEq9B0mT3EWlrOtvHnaSV5lwtUcfZd98x6F6Nmr7jYfr37m7FTo3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxggGTQX_Q7zlNacecEODzMNggQtkiHNaCon6KIlrqF9jMGuil_NeGL9uWz6A4_9ZhAAU5BtnrUpFy6qIqXnMpn1gW2SnNcDEqF6CaIgVlyIyaTqUDMWWv7SN89yTHKkqrP4qeEw6l9ahzdwJQbjoof3-qpbwnCqwMBtAHcbghMi3AAm-j7efMZSrE97jiRGYsXFzgcfnrn7ryqUeStI5L3zSX45B6wcsXHHJ-qy0C4Vlkv_GwVYnMbj1a0VtZPH3m4I1pjPvrcN-0HVs1LjintuXo_fLiMpD96GEq9B0mT3EWlrOtvHnaSV5lwtUcfZd98x6F6Nmr7jYfr37m7FTo3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
کانال گزارشگر زنده بت‌فوروارد
🎤
⏩
جام‌جهانی ۲۰۲۶ را لحظه‌به‌لحظه دنبال کنید.
⚽️
گل‌ها، نتایج، آمار، ترکیب‌ها، لحظات حساس و مهم‌ترین حواشی مسابقات را به‌صورت زنده در «بت‌فوروارد لایو» دنبال کنید.
● پوشش لحظه‌ای تمامی مسابقات توسط تیم بت‌فوروارد
● همراه با جوایز، برنامه‌های ویژه
● سریع‌تر از همه در جریان مهم‌ترین اتفاقات بزرگ‌ترین رویداد فوتبال جهان قرار بگیرید.
👍
برای ورود به کانال گزارشگر کلیک کنید
کلیک کنید BetForward.com
کلیک کنید BetForward.com
🅰
g17
💻
@BetForwardLive</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/funhiphop/79732" target="_blank">📅 19:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54671d6f3b.mp4?token=YrlSVovqPobB2Q4chKusDQN8zfKRkSMPOc0U0UQJmkMbOH0XuQnvs5qM30Xy52k-NkdmhpE-jTM52iy01tembXkPEH2X6ckdwN16yXxDBKx5jgD4urAeuuaMv-KcavkBWEy1bfe0xgBKFtktAhcgyNVBRYMlr5fppNOAygRIqxOShjf49mcAysHPNWI7qDuDqAL5CiiBhBW85bPwcneFItfdYgGa9CUcu_4tOv6jycZFvaSFKWh7Wr2x_ZhDsJeAHgUWrSKp2tuCofHq7mqpkDKbDz1FQ6jG6pS4Fc9NYqFKK7e0y0g85r6iZY18TBV3K61p03M2pyM79pGX7v1JhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54671d6f3b.mp4?token=YrlSVovqPobB2Q4chKusDQN8zfKRkSMPOc0U0UQJmkMbOH0XuQnvs5qM30Xy52k-NkdmhpE-jTM52iy01tembXkPEH2X6ckdwN16yXxDBKx5jgD4urAeuuaMv-KcavkBWEy1bfe0xgBKFtktAhcgyNVBRYMlr5fppNOAygRIqxOShjf49mcAysHPNWI7qDuDqAL5CiiBhBW85bPwcneFItfdYgGa9CUcu_4tOv6jycZFvaSFKWh7Wr2x_ZhDsJeAHgUWrSKp2tuCofHq7mqpkDKbDz1FQ6jG6pS4Fc9NYqFKK7e0y0g85r6iZY18TBV3K61p03M2pyM79pGX7v1JhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه صداسیما رو گرفته فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/funhiphop/79731" target="_blank">📅 19:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">طبق بررسی های انجام شده توسط کارشناسان فان هیپ هاپ، درگیری نظامی میان ایران و آمریکا در سطح فعلی به یک جنگ تمام عیار منجر نمیشود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/79730" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار:
هیچ برنامه‌ای برای اعزام نیروهای زمینی به ایران ندارید؟
ترامپ:
چرا باید الان وارد عمل شوم؟ وقتی آن‌ها کاملاً از بین بروند یا زمانی که توافقی حاصل شود، آن وقت اینکار را خواهم کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/79729" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فعلا تحلیل نکنید تا پیشرو شیشه رو بکشه، میاد پیش‌بینی میکنه برامون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/79728" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:   محل نگهداری مواد هسته‌ ای ایران را شناسایی کرده‌ ایم؛ این مواد در زیر کوه‌ ها دفن شده‌ اند و ما تجهیزات لازم برای خارج کردن آنها را در اختیار داریم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/79727" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:
محل نگهداری مواد هسته‌ ای ایران را شناسایی کرده‌ ایم؛ این مواد در زیر کوه‌ ها دفن شده‌ اند و ما تجهیزات لازم برای خارج کردن آنها را در اختیار داریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/79726" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">زودتر به این ترامپ تریاک برسونید آروم شه</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/79725" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2PSk8DZe2ltyPjJFUp9H_XPupUlZnarEP8-o0DeqMZgm5762uH21YI-dvckvl0ZyG4nJPF8JbdrQQkf000ZUkbeOCspF2-t8gPO7aUmvfd2JNYc6wGsTaFXBcBQyU0VFM8qZeMMbBrATRLHC3J4FA0C9eAYRp_OS1vKm0YVKpYa4x054xd7Z4GoMx7bShl96yPhhIPaHER8aSv8XMi7Ypq5EnzDFHqrSfdkCbOWnJYHUJOkiVJ2o1eZUptzeut2IUJ_VGN0gTyaU_EO0o5zAJDMAH_gYmX9k2Jg7n19yOapASi0z4sLlXvv7TtkkCG6A_HvbamrHS3wMLXJYdOREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه.
آره.
به تو ربطی نداره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/79724" target="_blank">📅 17:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJQFA-60X21xF6QP461MZ5Wmd4OM3azbntM_bIs1p5u623aRuXn7uA_SofRXsfcaZZfoLl1azSNxrCxGWVChYCTPZS6kw8r27k_v3VX1cMhee-aytTBq0_im6EV6TXXgc4N1COS-W2Xi80SIGhu3Skn2kRfw3FYAe_FmLBHCLgaBEZJ9-qXTquGKj6vU2TBeqrCeZCazDhsvl3gLfSvBUDoUL4G9tSFlYJszTmSMRpTpUwoo2WXYd-Hul3wlJpjwHkh6mIGZAkGYThy3hw9QpqTSjx9up1M-_yhR3KxO4JGGJkW9Igqx4r5qmxAeMSkbuQMmhoGdXE3zU6nRmYLw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کاگان و آرون به نام "Geek" منتشر شد.
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/79723" target="_blank">📅 17:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79722">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویناک میخواد ترک "بلاد۲" رو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/79722" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐦𝐢𝐫</strong></div>
<div class="tg-text">صدف چاق تره
احتمالا مادر صدفه</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/79721" target="_blank">📅 17:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79720">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WesO_UFaQC9XdfuTvhODMMU5mXAAaAPsDtNEbr4hedreX1hMiI88H740r37HA70D3D9VsIysp8mJF3RFnjd0eYNN_9Dyq3b5q5nwhK6VjIuUYh1EPmEbcLmRkoVbuSq6ta-dogXS5TZU5jUocDWA6ludOpq-jg0URHPwc32a-NwyTND8K74bHqigt4PVKD3SOVfceMrDTgETymx5OiRymPs47ZGABYJ3WwYghY0VlWLNM48nUXWJ8C6whQpXmhExOnZLz0R4QOG9EZwP7g3qGF7rgnlPCUf4kIpU_rxKrUyZIyjsHf8XY8RH-aKEGbydvrVb3o8-ePv08DF42FKV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی یه کاری کرده کاور صدف باشه هم تعجب نمیکنم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/79720" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ هربار اینطوری تهدید کرده هیچکاری نکرده، خبری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/funhiphop/79719" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: امکان تصرف جزیره خارگ هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/79718" target="_blank">📅 17:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6fceb66a.mp4?token=F1yGb40nV7q8sz2fMwE1IGUiVDhOWsIE5cn5v0gsA2nNS1AlIKr9S3Q7ZPm21ihD2gMV4T0g0WqzmZRjx8IaHTYuvODumj9IxutrkN8JjQM1Kt9bbcxaXLy4luuT3Dw0VdP3jmfm6FRP7od6tb_tvB_cHOgDfAGFzRRK1WupwRZ5VcMis2lLV_kiDCdfVXlLtSLFEcxdYeXd6PYjTzTeq1JWvVwHk6og9nbfHkUXoSaDhikeyEAbgztxrnvQVOMlDHrp-HCmmJgbqS78u-n1R3yA0d3Y9HLEBxZ9V2ivY318do5cXX9bg1Y43wkjSouPr4d9onEIs6srJI2grW9Gjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6fceb66a.mp4?token=F1yGb40nV7q8sz2fMwE1IGUiVDhOWsIE5cn5v0gsA2nNS1AlIKr9S3Q7ZPm21ihD2gMV4T0g0WqzmZRjx8IaHTYuvODumj9IxutrkN8JjQM1Kt9bbcxaXLy4luuT3Dw0VdP3jmfm6FRP7od6tb_tvB_cHOgDfAGFzRRK1WupwRZ5VcMis2lLV_kiDCdfVXlLtSLFEcxdYeXd6PYjTzTeq1JWvVwHk6og9nbfHkUXoSaDhikeyEAbgztxrnvQVOMlDHrp-HCmmJgbqS78u-n1R3yA0d3Y9HLEBxZ9V2ivY318do5cXX9bg1Y43wkjSouPr4d9onEIs6srJI2grW9Gjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی ژاپن به ناو هواپیمابر ما حمله کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79717" target="_blank">📅 16:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.    Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79715" target="_blank">📅 16:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: دوباره امشب میزنم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79714" target="_blank">📅 16:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.    Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79713" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.    Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79712" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhe92pgGtRIPoK2o9shpLAATdZNcicoAqH8Ph2VT62a9GoSirWwYGu9TCfR8TH7YDIrEkj1OqWDTjg-6QfwLL5WVdeg4LsV3uHC1_-hd0JFPD2FhSprc9vhQ5kjg-_xhLOa8Wlktz17zc7M3ZKHLoJ9Rds86CzFrT9Xp3BG-MhjEPIhHzb0HWDSW3MhXTELUgoYGlOROHjIp0fZGMRIola3jV4fcrH3X1MMeIPYMDQwbEwrekD4Jd-Vproq21gAFQ2UuBeOOz43OpwZKfPB06iM1m2KM6ZG_87r08xV6TLU5IZcXDxKeRP--ALvyIJSGMTvlIHfwiKLn_Duoa54KLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست به نام "بار آخر" منتشر شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79711" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5fXjpU7dvHehaNrsnqQ-DcTuvv71GAYDh1KfFrr8bXPstuDxoWMm_YJWZQMNgcWy0pvSRQRtKIH9Mrj87AQNa-Zo_G37m-I_EFfFMXikmSnMA8hZ2yFAS9B3258Z5YqIXL-JN6fSMCfbglvn9_r24BeqkuZDCfBwfEnvtO8ngwVCUfOaUCeJ3eEAUpKWZfdS4T-8GSPHBh571zTjz7yL7fRup7fgLt-_bq6LVCLbbmWDxfuzJ319oRMXJVK-elQf9eGS8DnVmAHLpnV7488Ux8ACy-WwOE-RfyN0TzIGKjl9CIF1BH88d0Ue9G5S5E_W2TXHn_TdDSX2yDJq3kQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش در بیانیه‌ای اعلام کرد علی معینی، پرسنل واحد نگهداری و تعمیرات نیروی هوایی در پایشگاه ششم شکاری، در حملات شب گذشته آمریکا به بوشهر کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79710" target="_blank">📅 16:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">راستی اینجا(شمالغرب) یه ساعت پیش داشت صدا پهپاد میومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79709" target="_blank">📅 15:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4QLGb6sWllzw_Xbc4EnLfiqq5lFKI7VKyKJQtH_nsywZK02jAxNHYBtoigdJ-2rF7AF8WtgOca2X4cDTdtzs1fqFGZmsH8wTfmWZOGbNBz3TBzkoqoNIjoQa-eF-XhrU2RoZbjk48VMghwpPXEYkP7xb250gJ0jnTNX1nKk-UgCuvi319BLwqWvtRrtIz_FLi9qIDLoT3QeygNpB72FhKjM0qqv_XtgHwXa9LOLuwavpgaEUBFDwVgcxzzi50g-DWx8tlUjc5SINkc9cQkDhYFvoJoPWH_Ip-eDfAm1BD3KENeqWKwDNznrvS902_T7SQ2ZNLyVKePiqdL5c4iUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااام
😐
😐
😐
(من تروث سوشیال برام بالا نمیاد، لطفا یه نفر چک کنه ببینه اونجا هم گذاشته یا نه)
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79708" target="_blank">📅 15:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbb43a3fb.mp4?token=iB88aTsaOfAciY4vYFl_HR19USb02B5w9TcKnbObHYbAI3o_sErHvRYdOav9a_GaC0jz-evIDc_BPAuJE0JFpQXSKlcKD4XbNqjSiaTrvNz8Zlj1ebFjeg0vQoLGKX6PBXYBHH4sa1cia_08pfTDKWQaFfmwVJptXKPQ0dNN4wyVkeJF5dUYuGcaqV_qwoFYlZTOyq-L6VXMR_rHoiQxPc-niGB0750J9envPgT5sDISSleKYu7Rn2q1kdFv6O6yruHzR9uKUV8HcyuuP9feZQx9szxIb6KyQLvwPAjyRKZksVmSUQJUrqhrg_qTSqTXsMi2dty1I4B6m2wpCdgFNzBd9E8AutVjM7kheKX_7PBT1GSC_HG7huRJcpRul0uOGcowDMTPnchvqOkA7xtm_TWq1OZoDUUjEy3yp99OlUtw_ATTqcX0m7dNEfTZfKE9D8Z9J1XK-Yo1IHNI7DP3q2yH4zfQOdd41u8Z9KjR0Ax2XqsF7gv0Tzd_uVXvA3GKhqCZy0Dc9fXMzqAX___oOyNwcJ63e3TQNQYxjGBvFSzvldk9NPx_hhqAC6RT6Fc6NsydvJqGtvfBCGT6kKpIrA55dBz977cu9TnZRkXrDqXAylpl8orBR35ZE22bNDCIqVVpWoWhFpWGu8X8hrl6Z8evl7WvwdIKoeBddfhIw80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbb43a3fb.mp4?token=iB88aTsaOfAciY4vYFl_HR19USb02B5w9TcKnbObHYbAI3o_sErHvRYdOav9a_GaC0jz-evIDc_BPAuJE0JFpQXSKlcKD4XbNqjSiaTrvNz8Zlj1ebFjeg0vQoLGKX6PBXYBHH4sa1cia_08pfTDKWQaFfmwVJptXKPQ0dNN4wyVkeJF5dUYuGcaqV_qwoFYlZTOyq-L6VXMR_rHoiQxPc-niGB0750J9envPgT5sDISSleKYu7Rn2q1kdFv6O6yruHzR9uKUV8HcyuuP9feZQx9szxIb6KyQLvwPAjyRKZksVmSUQJUrqhrg_qTSqTXsMi2dty1I4B6m2wpCdgFNzBd9E8AutVjM7kheKX_7PBT1GSC_HG7huRJcpRul0uOGcowDMTPnchvqOkA7xtm_TWq1OZoDUUjEy3yp99OlUtw_ATTqcX0m7dNEfTZfKE9D8Z9J1XK-Yo1IHNI7DP3q2yH4zfQOdd41u8Z9KjR0Ax2XqsF7gv0Tzd_uVXvA3GKhqCZy0Dc9fXMzqAX___oOyNwcJ63e3TQNQYxjGBvFSzvldk9NPx_hhqAC6RT6Fc6NsydvJqGtvfBCGT6kKpIrA55dBz977cu9TnZRkXrDqXAylpl8orBR35ZE22bNDCIqVVpWoWhFpWGu8X8hrl6Z8evl7WvwdIKoeBddfhIw80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79707" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRsrX88B8WLKU9PUUfF2dy4Y3BLEb1TDrll7WtEX_hiMdKBDELE1oRLx-rhIhqiBqQ_foqnU1kCacG5AuvGbBXlZQcUjokBbi8DLfuJeLL3l-AD25A20ILVM3iRKzoJ_eRUtoAcQMCyF4DYcS1QMMmHzIOGyuzl2LO8i_64-yuwc3H62CTMy5acbwaXzTJ00elNelSDZ8yWRLxQh58E0Ymsp7aO5eUbBAvxo79jPw-ssAiVKi4RHpbSmWFQQjqrQlOdeIyTuAlnGLQ6a0gnpfZOUWmHDGwkXZMS5CiLfMW5FNv9NAmrt69dznnxLWrboitTMO1DxSuZimCOdfAnTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتما باید مثل نیمار چارتا حرکت نمایشی میزد که یکمم به این توجه کنید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79706" target="_blank">📅 14:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ بزودی، به درخواست یانگ آرش ادمین محترم فان هیپ هاپ آتش بس را دوباره برقرار میکنیم و فرصتی دیگر به افراد باهوش در ایران میدهیم.
از توجه شما به این مطالب متشکرم.
پرزیدنت دونالد مادر جی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79705" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دسخوش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79704" target="_blank">📅 14:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfMfW3ylj4tvzNbQa_JfejoWTGHRRkIA7A_MRysYs-USjdKdD8bwnTr-1fujaYlqC36NjpcqAGycuCPRmxyIw4aFnq0r2XggK4ZcNxPyV95yRdR1oyqkUVIlrkn8Ml49ZbGSblAyE4pbhiZkQHeCpV_asA6-awQHJaz-qjbPFJYhNZ44X3B5s9E33g5RIdGzRcZvJgkqPDpqC-2Rhd-d4L8xVAHG1pYUen3G1VotJeaC5BULFxOTvcqrICj_tQ_6-YQSsGbGKpWvlGm1siI0diCM82FeL1YXdyPEowkMIr_gTpOUYS2pdAdv_pg9tQlz_RbWLHVlQa4LAxcXtiD1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79703" target="_blank">📅 14:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpncL-tuFMTwiZfKlPh4hbnYoEhPxa1LQFYOhZ4gN3S-Nh5KKr_NzVhBndtOoqpAt8Xo8PgE-NHesG6w0Fdy1tQ-41JTk60-UTGg4cLds8GK4AtUfqOc5X3CMNTR8NqDAd6rMCB--Iw4sjxQ66vYt42VB3XccYkIC0R3A92dFfSn4ma7Cn2bV8e4ayipQ8F1030NZrcVWmaGi2Wd_LSQ6uP9ZGkzbX1y_-Yb9wK5flqxQa5i0FV6Cvijl4OjXAkLODczeFEqyEohzvaBP84UXoQfiSkbvw3nWAt-6aVG1d3PHffImtm4A3jUzVRVc_xOXfHB6qau79EmNz2ifOhD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب ساعت ۴ صب وقتی شما داشتید اخبار میخوندید من داشتم این شاهکار رو میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79702" target="_blank">📅 13:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_J7-DAdkuHDvIqUbpWCfcakkP2Wh1hx1HinoXEl8fuQOzesmRMIPeNvfaf8MDIgEHVZTJjkuQ8Ld8BxrU_DW8ClH5wKlqh7fwNlmqXT8fzfAdCZaTOB57Blw0bwsKBEJaHm81DsUFapEubKoEPxdw3Y9oduLOD6jEPgHup9d7u3wGG0ShoZTZ6ys_kFEvTHQJrE0r2gMCQKcoGZatXzluuFAieolgGX-y5r0UJ1eswbA8GASyZxKs1ahKhyoDgwc_RovOd4Opmgrr1Z4wLNz-vW0RGQb0OvivG5-VVb0ac_fWn17P9Oceu6Ewsx5-UPJZ12EiJh0pDeeZC-V9fxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدمممممم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79700" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79698">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb4956b2d.mp4?token=ri78Z_cXpVevXEOgT20yDeBx2WcwWxdG7UDaqiQ6BtuG2KoPEEXgIdipn5HExEvd6wSq7580evle5ngvfZ3jrhP5dxpMhSP6ucvcrLa77NT0-_A6GB9JEObGwQiFjcQvzQqAfT6L0iTPOUpndDEajxOfjiPnnYr8yamoQtlEPLHoV5C3Ks5-n3rTBnAETS5UULljiBWqTblgLd-sZd9sKpdC-U6KG1A9YPCbb8e7r0xYXkb-2sfoShxoi1wPRf1slRndu5RZWJjCAaRkcmUrfYnyZOi4LACCnL6LDVXkTZzeqbkAXf9Yvt22VzsWCtgTZAL3bq4CJHH6e9K0c3ZDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb4956b2d.mp4?token=ri78Z_cXpVevXEOgT20yDeBx2WcwWxdG7UDaqiQ6BtuG2KoPEEXgIdipn5HExEvd6wSq7580evle5ngvfZ3jrhP5dxpMhSP6ucvcrLa77NT0-_A6GB9JEObGwQiFjcQvzQqAfT6L0iTPOUpndDEajxOfjiPnnYr8yamoQtlEPLHoV5C3Ks5-n3rTBnAETS5UULljiBWqTblgLd-sZd9sKpdC-U6KG1A9YPCbb8e7r0xYXkb-2sfoShxoi1wPRf1slRndu5RZWJjCAaRkcmUrfYnyZOi4LACCnL6LDVXkTZzeqbkAXf9Yvt22VzsWCtgTZAL3bq4CJHH6e9K0c3ZDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
آتش بس با ایران به نظرم تموم شده!
دیگه هم هیچ علاقه‌ای ندارم باهاشون سر و کار داشته باشم؛ اونا کثافت، مریض، خشن و وحشی هستن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79698" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79697">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcAF-jskozccrBzt7cZFTd3QAe3F78hU9jLuhunmxYz9S6TITqsFFd6izlwohtGYPf_Svj-8ntIv90UFIWxL3nL2p1ztMypcY5dRkjXeeBuiISz1gmjwMbgayE9cDhtDEnhOVmphd1U90CiodwS_FaH2JtGzTXPncMQ_cf9FhWi7yhVEMYvCGL0HmXcWbCpdi2FMKWcUOG01G2bxkpGQINTNCvGK79zq1FMBxUqtouInPD0qjR5fVsD10qPPXr_gRdbZhMNHMPPgTLIfLEIDduTkgWcUcviAtcG2JGU-ca89AWvuRkFpe-Eke7goKDNsymjmv3g94eCZJwBYPqcTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف شد واقعا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79697" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79696">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=KwDZwL-utraKiCqAPn5tW59jttqBcnJvoJsrEcuakWzefpj6YepZppkmnOdHBOSiSsQIFrLaQ0ewmG8pBRUAhASUpf66DYpGg4oL6lb-9D8RKp5z8plYaLpWQQRU3LMI86TtyipkQMTj54YF26-wjYDGiSoGMWsZqMm5dW-G8jJ8hgq6KYycGspdOdAVnPN98L6hSNHGRXx7Byq5f9E7uaP_-NKGIEJHo_1k08NqCHpZ0Se3kx3hhwe7rL6FWvOgCS-KvGdACTEgS8ww_PYjeirfwnILj7mKxsog0Kt8iUAK4fdbmfz8HkNtConjZDez0x8GRZ6Q1He_WASHxenah7ydkTGWdhv-i0z0bAaxP0J1wKWrfuyS7ebTVvbQJGrhDtjtXTe4PIPueeNLMz7fETFiIblhIHNR9LrQFrODoXgc3PCDMMHYDppdkt44gHNMge5nO83Sh3nUgnwnxFLFmvIB8fI8tF7oXLSOVf96TQPS4MnEtNH9kn6NWKBum2p-gntyRgw0eN08vZbHQMCoFs09yEGfOy06K5VT23jIBM4J9ZApd3lPwDjfrlTR4gKojCf-DLPfRAKGhUIR1_MXG8Na4_Mefmmq551d_jaoa2hCgamgyAW5Gjh-1CskbgwgjD_EdH0nUKXtq5sL00x5eNVVkgUcmM9XV-44l-M5VKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=KwDZwL-utraKiCqAPn5tW59jttqBcnJvoJsrEcuakWzefpj6YepZppkmnOdHBOSiSsQIFrLaQ0ewmG8pBRUAhASUpf66DYpGg4oL6lb-9D8RKp5z8plYaLpWQQRU3LMI86TtyipkQMTj54YF26-wjYDGiSoGMWsZqMm5dW-G8jJ8hgq6KYycGspdOdAVnPN98L6hSNHGRXx7Byq5f9E7uaP_-NKGIEJHo_1k08NqCHpZ0Se3kx3hhwe7rL6FWvOgCS-KvGdACTEgS8ww_PYjeirfwnILj7mKxsog0Kt8iUAK4fdbmfz8HkNtConjZDez0x8GRZ6Q1He_WASHxenah7ydkTGWdhv-i0z0bAaxP0J1wKWrfuyS7ebTVvbQJGrhDtjtXTe4PIPueeNLMz7fETFiIblhIHNR9LrQFrODoXgc3PCDMMHYDppdkt44gHNMge5nO83Sh3nUgnwnxFLFmvIB8fI8tF7oXLSOVf96TQPS4MnEtNH9kn6NWKBum2p-gntyRgw0eN08vZbHQMCoFs09yEGfOy06K5VT23jIBM4J9ZApd3lPwDjfrlTR4gKojCf-DLPfRAKGhUIR1_MXG8Na4_Mefmmq551d_jaoa2hCgamgyAW5Gjh-1CskbgwgjD_EdH0nUKXtq5sL00x5eNVVkgUcmM9XV-44l-M5VKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
کانال گزارشگر زنده بت‌فوروارد
🎤
⏩
جام‌جهانی ۲۰۲۶ را لحظه‌به‌لحظه دنبال کنید.
⚽️
گل‌ها، نتایج، آمار، ترکیب‌ها، لحظات حساس و مهم‌ترین حواشی مسابقات را به‌صورت زنده در «بت‌فوروارد لایو» دنبال کنید.
● پوشش لحظه‌ای تمامی مسابقات توسط تیم بت‌فوروارد
● همراه با جوایز، برنامه‌های ویژه
● سریع‌تر از همه در جریان مهم‌ترین اتفاقات بزرگ‌ترین رویداد فوتبال جهان قرار بگیرید.
👍
برای ورود به کانال گزارشگر کلیک کنید
کلیک کنید BetForward.com
کلیک کنید BetForward.com
🅰
r17
💻
@BetForwardLive</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79696" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79695">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الاناس که عاصم و شهباز بیان تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79695" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79694">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79694" target="_blank">📅 12:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79693">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اوه اوه ترامپ: این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند. آن‌ها مثل سرطان هستند و باید این تومور را هرچه سریع‌تر از بین برد. این احساسی است که امروز دارم. ایرانی‌ها رهبران…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79693" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79692">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اوه اوه ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه سریع‌تر از بین برد. این احساسی است که امروز دارم.
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
فکر می‌کنم تمام شده است.
نمی‌خواهم با ایرانی‌ها معامله کنم.
ایرانی‌ها دروغ می‌گویند و تقلب می‌کنند.
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79692" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79691">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL4Gu74zNtJaJPmfEtH9GQfw-bgQqxrkqD7j9wDxYNJ4lYmm5AWJ7IyvFzDKnevEoRJNleMiKEDD69ZblkZTDOhYLgMQIPGGeR3-PmVGPKCllmCyKKynl8_3RLHZrQAObPVKnp36RJKtto4yiqo6vJtk1lWgGLgIEkMLogAM30aReWFtn_DpIstMrxepZ8Axp97uhmMmmFkTrzn4EfqyI3xlJI9Dxq88N7bY9dOsX0oZxk2Sbi4hyVSFE7PPXQync6P-4V9d6cdQaV4cGieJEmwwMq02VltDDPVze3KBi2rAMAimvrQ9blcXg5CH-Rf1qAPymjiKHECot0RG2iejgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب هواداران آرژانتین با نشون دادن پرچم اسرائیل سرمربی مصر رو فشاری کردن
😂
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79691" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79690">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=kpiDhZgSXI6rsRMK3TEQNAgL37z2mOvRe6rWs4UGZuYzem2N6jpQ_-oYqgBTjA4xAJCOxXUWNdez6JwtydRyNQOC4GQwRw7PEyHocRehK5nn191vqJUCf0lIZv7sKGahHW5PzEoMmSy3UxCNClSsUGQ6_Db4Us6Kuf4jnOoLKlrpP6gWaWvxdwkl8wSzObI5UwDewxuHoe2Zv8NtkDf-qFfsVjbRnfRhAVuPbBa5FD6cCTYt8tHl-kBzK-1v4HNobqM8432ZJHKp_XZXmrTmWtNOkgm5ZQr_B4blLe9M4naqHtxuMQXEIgbQRdmYj26e0zWK8YpyGbOA84e7_Pwp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=kpiDhZgSXI6rsRMK3TEQNAgL37z2mOvRe6rWs4UGZuYzem2N6jpQ_-oYqgBTjA4xAJCOxXUWNdez6JwtydRyNQOC4GQwRw7PEyHocRehK5nn191vqJUCf0lIZv7sKGahHW5PzEoMmSy3UxCNClSsUGQ6_Db4Us6Kuf4jnOoLKlrpP6gWaWvxdwkl8wSzObI5UwDewxuHoe2Zv8NtkDf-qFfsVjbRnfRhAVuPbBa5FD6cCTYt8tHl-kBzK-1v4HNobqM8432ZJHKp_XZXmrTmWtNOkgm5ZQr_B4blLe9M4naqHtxuMQXEIgbQRdmYj26e0zWK8YpyGbOA84e7_Pwp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 3
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79690" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79689">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوباره انفجار و دوباره جنوب کشور.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79689" target="_blank">📅 03:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79688">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79688" target="_blank">📅 03:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79687">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در مقابل دوتا کشتی اینهمه اسکله و جزیره یکم اور ریکت نیست؟
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79687" target="_blank">📅 02:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79686">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79686" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79685">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79685" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=CUi-CCCasORf-FbS6tLm_Pz27c2Mm_qH1JaQNQ6mwi8YE15OwRpS39fRENg2iS830AvGTZozUzEV3KcMV6UqFxICr3A9MK5t81uI7PSf6Q7j3Mg0cfV5jPyGMm0zeULscowcftA6Kgrvb3p0Q54IPFAtNqii_-aSpnH0IQ4ZW4gebB9Fdm0X2Opkf-oAXxzfBy8RwTCPL3BroMSTRCPFLejYyMqGZKbjz_tIIkwHJWTTmQK0Lp8kZo7svI0pNUR0nSYH-X9jozpFOK2pYyUfLAnUZs8JnLTXQY0ZOmcNTq0Mzu1qHUwGlKIonsRHmACT4FQJtc_z36Ks0oS85VVoQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=CUi-CCCasORf-FbS6tLm_Pz27c2Mm_qH1JaQNQ6mwi8YE15OwRpS39fRENg2iS830AvGTZozUzEV3KcMV6UqFxICr3A9MK5t81uI7PSf6Q7j3Mg0cfV5jPyGMm0zeULscowcftA6Kgrvb3p0Q54IPFAtNqii_-aSpnH0IQ4ZW4gebB9Fdm0X2Opkf-oAXxzfBy8RwTCPL3BroMSTRCPFLejYyMqGZKbjz_tIIkwHJWTTmQK0Lp8kZo7svI0pNUR0nSYH-X9jozpFOK2pYyUfLAnUZs8JnLTXQY0ZOmcNTq0Mzu1qHUwGlKIonsRHmACT4FQJtc_z36Ks0oS85VVoQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجا که یارو میگه خارشه گانوم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79684" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79683">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سد مجید بیدار شد
ابوالفضل ناصری، عضو فراکسیون مجلس:
‏ ‏آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
﻿
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79683" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79682">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79682" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79681">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=KCvlF3tOZYMQiv77pEnMk38P7COTdELigVMp9wdXCROrFQlSYqwEBx149SZlCEAfhU4uHHO-_rbLDSlOWE4M9Kyn_V6wWuMlzhHclbXnKbR5FLh1sP43VE13te5bz-Qws3RKFN--ZRbOObRzmI988X9kT-lhiTcY_24JsYJzKQXByFaoYUvQt8yUzWg5o0oZ3Jz22pm8OZVpuj6rgeThsUJgK6_SnK_PsRbROYiI7ss-UecYwzMHiu4aTGUwIx2IEB7GwoeId7qBFtLRiddxrbPjRDfs8lEtsmo6x-Uz8-lAC9uZRrG_2xiVG_u966UCibv5cH3S5w0ceuCveIBKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=KCvlF3tOZYMQiv77pEnMk38P7COTdELigVMp9wdXCROrFQlSYqwEBx149SZlCEAfhU4uHHO-_rbLDSlOWE4M9Kyn_V6wWuMlzhHclbXnKbR5FLh1sP43VE13te5bz-Qws3RKFN--ZRbOObRzmI988X9kT-lhiTcY_24JsYJzKQXByFaoYUvQt8yUzWg5o0oZ3Jz22pm8OZVpuj6rgeThsUJgK6_SnK_PsRbROYiI7ss-UecYwzMHiu4aTGUwIx2IEB7GwoeId7qBFtLRiddxrbPjRDfs8lEtsmo6x-Uz8-lAC9uZRrG_2xiVG_u966UCibv5cH3S5w0ceuCveIBKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم دیگه ای از حمله امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79681" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79680">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=c_fGaPstkYA7KO1_nDxcr0LiNblL5GO5EzAaqxiF57FVVnBIXW1JGCo24kUJgTgmXEVUeszOh7poWzdwfbmJvSrMYX88pC7OQWThPBLdfv-lc8wfd7o9_RBkjvLL_2XoYqIcx_hllYPZ8Gtbat7x0ZIo5HaoYnsT_YvtzPLM6SSXGHvGNGv9R-w3RJhOFFogtbFZXyw3tXNqIB7HN0sh8iZjAtwEAv8N7UCgRKAFw0ZLk0fV0NdO0beU_BULkeTPPfMWY3iEPUz9mkYpj56aTuQHNc84NjcndlroICm15iNbDZLBG3m8h6xE4LcuxPwLACaDz7e5eYeBpOQoi0IgJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=c_fGaPstkYA7KO1_nDxcr0LiNblL5GO5EzAaqxiF57FVVnBIXW1JGCo24kUJgTgmXEVUeszOh7poWzdwfbmJvSrMYX88pC7OQWThPBLdfv-lc8wfd7o9_RBkjvLL_2XoYqIcx_hllYPZ8Gtbat7x0ZIo5HaoYnsT_YvtzPLM6SSXGHvGNGv9R-w3RJhOFFogtbFZXyw3tXNqIB7HN0sh8iZjAtwEAv8N7UCgRKAFw0ZLk0fV0NdO0beU_BULkeTPPfMWY3iEPUz9mkYpj56aTuQHNc84NjcndlroICm15iNbDZLBG3m8h6xE4LcuxPwLACaDz7e5eYeBpOQoi0IgJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا پایان جام‌جهانی ای که پیش بینی میکردن، برای ترامپ حذف شدن آمریکا بود نه فینال
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79680" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79679">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قیمت نفت به واسطه ناامن شدن تنگه هرمز دوباره کشید بالا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79679" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79678">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=mlKjOS4zn5t5zUhYWWOWrxN0FwMtFvHvetnn3Hb_ReRqs7ew-3RV7qk2Cac48jj9Un0TTwpVAMkU7GVg5AkgvQuUgywaQyAyAh_YZkv4Ys4rsjIj28p-cT4VNz8PPD9G5dAW47YIzfEVVcht_vJ8k_Paiz0xvCu7uCg_D6p8Rnhsj28HEFAzETiJr6RloIbr0ewiHehkrwdq265bajbt29Lg8HrBAuqgQsQbrd68KjuLP77uxBZ7y320oqXxLrIY59EJk5K5Rgdkyhnnh_47wTszTOXwFvmkv6suRLbRcW_ssnFCZ-MbWM-e1D_QXFzS1hgDIVCu4xpS4j57Lo9wyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=mlKjOS4zn5t5zUhYWWOWrxN0FwMtFvHvetnn3Hb_ReRqs7ew-3RV7qk2Cac48jj9Un0TTwpVAMkU7GVg5AkgvQuUgywaQyAyAh_YZkv4Ys4rsjIj28p-cT4VNz8PPD9G5dAW47YIzfEVVcht_vJ8k_Paiz0xvCu7uCg_D6p8Rnhsj28HEFAzETiJr6RloIbr0ewiHehkrwdq265bajbt29Lg8HrBAuqgQsQbrd68KjuLP77uxBZ7y320oqXxLrIY59EJk5K5Rgdkyhnnh_47wTszTOXwFvmkv6suRLbRcW_ssnFCZ-MbWM-e1D_QXFzS1hgDIVCu4xpS4j57Lo9wyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79678" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سیریک و قشمو باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79677" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تنگه هرمز ارزونیتون، ذرت نمیدیم بهتون.
@FunHipHop
| USA</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79676" target="_blank">📅 01:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انقدر اسکله زدن که از بندرعباس فقط عباسش مونده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79675" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این دیگه بخاطر کشتیا نیست
داره حرص حذف شدن از جام جهانیو خالی میکنه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79674" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سی‌ان‌ان گزارش می‌دهد که حملات نیروهای سنتکام علیه ایران ادامه خواهد داشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79673" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79672">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فعلا اوضاع ارومه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79672" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79671">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آکسیوس:
به گفته مقامات آمریکایی، این حملات به سیستم‌های پدافند هوایی ایران، سامانه‌های نظارتی ساحلی، سامانه‌های موشکی زمین به هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تاسیسات بندری هدف قرار گرفتند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79671" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79670">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ تا ساعات آینده هستند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79670" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بندر لنگه انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79669" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdbU1nVWbmw2_M24AAfp8DqNSfn5D_JV7l_vu1NNL0ojPg2ZvFMfpa1sLR1xVEDLFk9gLbwCu2QTrCcCC26U4xGN2Diff7xGtMxO8NLlX7C-DUhLZVZxCNfyz-bBQsuYKUifEn92Jb890MsPlVY7Kk5SBCaqwChY9PxY9Y7eTdLQmqKArR-WO3jTAdUeAqwZslLV-0LoQEfvqCozHQ2TtE1BGARhxCk3TgU6_zjKW8hj9T4SJHLgDYbgKjhrm-PafFzI9ofZDirxV9jtMY3byMDwmeeHLxZDCd0pZZhNb1r5VSUCNdb-InFQnG6oo4E67H7l7oXCS87dgZoCD_zfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا صبحتون بخیر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79668" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=G-VFNpUgnf8ePvmNzHink16KSiCX75cAGDK1oNMjSxgQl4tbJrw57LAy3-IdxrPQ6FmtPRAtFRJfjgFAYt4wlGAcd67b8lGmCPlymABYzIw0nX6H0wchAKwD9OMC6CgZm1Ajtl5-ARcgBHH36nT1EJvIK7brDFAbPPN5q8_Knt5i5Y1A8_pwqG_vmP6pTQxWzoF5AiL35Dlm-Wd5V-ORsfnmTP1p5gn97z77-By1OneP8oOFOgJOfBGibKmhkUY6Vw99L6lcmb2pyCJz3989gpboZ1CmI2rha_z8dOJAUMcQLeCt5dRTfBqIsoxDScU6qGjeWZEvJTTP-x8fC5VMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=G-VFNpUgnf8ePvmNzHink16KSiCX75cAGDK1oNMjSxgQl4tbJrw57LAy3-IdxrPQ6FmtPRAtFRJfjgFAYt4wlGAcd67b8lGmCPlymABYzIw0nX6H0wchAKwD9OMC6CgZm1Ajtl5-ARcgBHH36nT1EJvIK7brDFAbPPN5q8_Knt5i5Y1A8_pwqG_vmP6pTQxWzoF5AiL35Dlm-Wd5V-ORsfnmTP1p5gn97z77-By1OneP8oOFOgJOfBGibKmhkUY6Vw99L6lcmb2pyCJz3989gpboZ1CmI2rha_z8dOJAUMcQLeCt5dRTfBqIsoxDScU6qGjeWZEvJTTP-x8fC5VMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا کی قراره در ازای ۴ تا کشتی یه زیرساخت پتروشیمی و چنتا رادار شوهر بدیم و آتش بسم برقرار بمونه خدا میدونه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79666" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79664">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بندرعباس هم زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79664" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سنتکام بیانیه داد که مهم نیس توش میگه اونا زدن مام زدیم اصن هم اتش بس نقض نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79663" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79662">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بندرعباس هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79662" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوباره صدای انفجار از قشم و اطراف روستای تهرویی شهر سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79661" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79660">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سلام فرید جان وقتت بخیر اول بابت برد پروردگار فوتبال حضرت لیونل مسی بهت تبریک میگم دوم اینکه ما قشمیم و صدای انفجار اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79660" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسرائیل هم حزب الله رو انگشت کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79659" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79658">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سلام فریب جان توپی که یامال دیروز شوت کرد همین الان افتاد تو جزیره هنگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79658" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پایگاه دریایی سپاه تو سیریکو کوبیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79657" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان نیاز به تعجب نیست، آمریکا خیلی شفاف گفته با خوردن هر یدونه کشتی تو تنگه هرمز یدونه زیرساخت جنوبو میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79656" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قشم هم سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79655" target="_blank">📅 00:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امشب سیریکو میزنن بماند به یادگار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79654" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkLylMDkT62qHlNIA0YiHA7VZ8TzB2VCMPCuX3EFI8Vo0RHLsm6FEkddrJ17IVzQfDhMrDuRtmEdgevRBq4o_n7bmA0bxRWTzAvRQPb9GYMkZJxqy4vfmG6yhyR9MWMJOxCDXXAW1gGXrhF5VHmxseOQCG_763WDYajEZg_63Z6nCL4OY-CKvoHfUZOWyPIOydYtZU00vBrDzPjvkVTiYe7PowRv-5pXimNNlJtq5fbWETp1WhbSF3uFIHvkuSD8YYsRWdt4l8UkJxgobf-5bhuLgst5wfMOSnwjAqSiflGSJMH6rvCCMyYXDpnn40Mpw1bYYHWsJkbr4ZpGE_17jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79653" target="_blank">📅 00:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLxCVP6Um0DMvjPfHpOIzZQG4y6gPfK4hu0gCT6GpSkqDs-GM0AQu2FcEevstFJ9SMBvdkA48htUrGy4Qyzm3cRKJXhny2x2mr1dBKLCNzQE9IeBaYnX84ZIHyZOpzB0b9AYXOVEg6kr0m7VK-mDiu2GQTduY-HQ-gseqEzmfTVTxK5Wg6HlzT01RZUr-9HRM9CxUnc_lI_e-48l8YHaCSwsXpgS1uSw8Evna97nljAp1Sjke0Uz7mn_91lAzVgeRhAIkMo22qw1Z7obDc2ROKUorvIpntpi6kv4NVNL77Zt5tosswLMp3Fb23MjewnOmc4V0ntPGDC9XlB3Ee4UkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "پاکار" به نام CML منتشر شد
🟠
SoundCloud
✅
Download</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79652" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خامس چرا دیگه خوشگل نیست</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79651" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زیر این پست آهنگای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79650" target="_blank">📅 23:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امروز سپاه 4 تا کشتی رو زد امریکا هم معافیت تحریم نفتیو لغو کرد و یکی از مقاماش گفت که بزودی چند تا سایت نظامیشونو مورد حمله قرار میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79649" target="_blank">📅 22:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7Nr2rXH8tEMQ9H2pKiqJ66SKGNUNY4Ko_w0p-izeU8s-3IFY1c1EJa7WkwuCpaDDdWF6RNGRDaWJV9zlSFzKMT_tT_K8bppIA9LPWBJGdmTrtcrsJOx0olN4MqDcxp7Jo_kaHhxZzXjmY-VUqmkK6YaFxEM1xJ4sfakwanOEE4r8LLEmmdBmiG0PvrjzTOB0TjV8lxOqxrtBC2CthUFMgXqvXt4sNFxIEcszvmAed-vUMMU0ST91qs1LUPgR6gYX1Kilc2Vv9JUj3vOU1La5DwrSVowR58x9F9OLd0RYiBYn3A9JwNYaBSAJNSlb6tqPyvwUq80wRSH1s7KZuxSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULoQM-_s7xfeEBzp_VYWTT1L3HxGxqlpl6qQ7OOWkHuu_URqjJmnNG7hvjGRxc54mBWtGaszehgmWWJKk4g7GcbLN9RGFaQkRm2QKLJU1sUOClLKKXYUXvQLs7HggsgURM_gLqwR2hbNgidyuANREhS9ZpuHvAXxC4Yxvt47GSPQA0b9MV2KBId5ARdZKmz9SjaS3uLLBwH2SUaK1Rzk4Cxa5phX5NENcugWYZ2p7CGOVCfh6t_Q7PuQ66XOFvClAHMQHkjuEqFEIZeO_HzCncz9-Y1rUcvfgsj2LrCE2V2RTCh5sa7va0xlxcxYSp0VB8gLiw3651iHtQdE4eJQEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این صحنه چندتا فحش به برونو و نوس تو ذهنتون پلی میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79647" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا به رونالدو فنا ربطی نداره ولی بنظرم آرژانتین یا یک چهارم یا نیمه نهایی حذف میشه، خیلی کیرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79646" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس رفع محدودیت و کاهش پینگ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho5hez5oinmRxEwHiprL2B3zZ1F77RLhwjFMouaQHdscE1_pcxZazqlxjq8pIs0FCnK-2p1ga_InFHNuQa7VAyO7uHqfbYgDYOt-Qtomf-GPgWbpsdX7luACQUITNW4tuHAds0kQI0Q0Hzn4udL08NBXcsJLs1xVSTwB3IkDt1snKvl12bjK7BLw6ZE0kN9DhriTfUwH0pOGg5i1c4t1frBMofPadsFcOaGe9BUz3Okgm3gVp511OCqZ4idr_E7mnmdBUSrc8NxWP_khiGwnyI3_smDqtAyet1YYZyBKbADQadz1t5clwQoTDB90-e6fLq5nWf1rurgPXB55lSioYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
یه اینترنت پایدار، تفاوتش رو از همون دقیقه اول حس می‌کنی
😎
✅
سرعت بالا
🌎
سرورهای متنوع
🎮
سرورهای Gaming
🛡
اتصال پایدار و امن
🚀
اگر هنوز از هاب شل اشتراک تهیه نکردی، وقتشه تفاوتش رو تجربه کنی.
🤖
خرید آنی از طریق
ربات
🧑‍💻
پشتیبانی تلگرام
@HUBSHELL</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79645" target="_blank">📅 22:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79644" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝒉𝒔𝒂𝒏</strong></div>
<div class="tg-text">ایران چی میگه؟
😂
سوئیس</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79643" target="_blank">📅 22:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حریف ارژانتین امشب تو بازی کلمبیا ایران مشخص میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79642" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79641">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWi0YTVYmS_78-f5uA6k7Js0x8aV8HZ6Lk2BRwoLQRlWLpzUUtsRM54LLh8jJvQDWaOt_2otUomiM9x7bmVSPOHhtAwc0Jf_EwX26ThclbxrnkTkO-qINBmjtitDGDX55xWjerYZvA_S_cIDeMD3QAqfR8FxcklHx2RlrouzLUY1mtDJfImUXG7teDCOsoYuiLSxXcsqytxmBA143--aopQuHApu36kIN6khC-CgeSPFGHWwOblRWr6lOIG5F7maJk4n_c-DE4BtAWBy_AqJ9tU6anYZJJ8Hdl_HlQBGh4S-aeubHzpdkwCOTvpNWlKjehB7EiLIcXkOh9X8c_nLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی روزگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79641" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ولی دیگه مثل قدیما استرس بازیا مسی رو ندارم، فینال ۲۰۲۲ تا نزدیک سکته رفتم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79640" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آره دوستان، مسی منتظر نمیمونه پاس بدن، خودش پاس میده گل بزنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79639" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqVCwvDH_qrtQ5ToFPTDVqmSTvlffoxcdFGEd5e8Ri5AldGEbNH9RAY9Z06uw6zml2DmFzJeIARMMLWktYdAWjmammkErF0iJsqHwi78nLquOoOO2e1PGlEFywElMZjznvwW0WR73QZ-qYc_eb8BlO3FEHyBVwzO0omU5WUHJAOWZbVRB9SaJJC1GFT25EM8HGzsevxF9fSIkKTlue_hhKSGLnkPk1sCcGv_V_8UPxsMrb1fXxVRk2nfYiddVn7amrcDuRA74MybRypfq_xBnykkbmRMV1WqBbrZJqDGkWaQjYWei-2pbg_sVGbBCQs8WM06eB-XJU-GMQw3xdliJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79638" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پروردگارم
💙
🤍
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79637" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuxlNB8Q2JhxPABdwHpix3d_-8h07C7f_cgcFOHgN-Q_5XvTQRfCOoPhONFUgvYQzvBx2zkYyJNPgJGQLfHns1Zcb6Iws3IJTqYnQFb9Dg2UzeTkGRCrbkWSrEacVA3dOi3rngZlIvsrYiwgzDjtngZ1CcmWkOgK65FOPNn2mdA_u_Up6s755ceCkxbxOUvDMKDveOfVQw6UbD4FUT31PYrMjXw7NPuPOo8QzXqeNfNV0fH7ty4dfDahreCNwnKGgE8KOSWvpfhsgSAPNrnTafXluWLyJ-9yYe9wTFX4OXoHs1gbn9vf2IKCdWe-8fG68BbwiRkba0Q8yloGYFz1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنای رونالدو رو نا امید نکرد، داره گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79636" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ69Po6oWjhm-C8NUVU8F4zGId9B9RqcTIikvTUaBaYr5zecPENZJLgFXhukxWzAPWeAHop3K3i9krLIt8WdUAENkS3fi5R2vAUGV7YZakRVogB6tdfI6xTpISh9qv4HfjnYCjzo3E023clYWjVFT29nU0ebgSNOC-tvDVcmsfkRnCYunmgwaSACfBPpzMZzi1uhstMs5TsU4ZlGMENXFOUpc-HosqWp8wXBYtkgL1_2Fks9UWOiMDvU0XkgxiwBr-WBtIzBCKZTRtL-6kV0NcsPAEZ_NDxFjtmIUGb6Vfjw9fZ9M0RrPSdlUb3u-4cK-687ecLp30cf_8_6r1Kqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79625" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عجب کیری خوردی
😂
😂</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79622" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=UphGWio7f-9aql6gk-OjxkvfHhe5Fxl0g9Phe2vyTA_rfDHsNxnb5v0mjGcivJXCyGmGrni32Q_KXFMm9Qx6c9fmZZuEP7rKhp45xPqEcECIZNM3EP6reyBbV0q6BBOrLOukHG4TlrM4HUbPRq-iNXL2CvKIVR9eJEnsq44OvyNdPjoAoRvB9yKhtC0kGYVXbo40iDM1JxVDhoObxJfSFQsWJQrRPSMKjU2eGu-6jV7K7Orsjajb-mp7NUtII3Es3BWC2O1yJcIz_cwCFC4FfBDkC4Fit7NSCKrMYJIQ3GIxWZ2R3UfkTiNfndGlT_CzU-5xvER3DUCBQHmjXuiitQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=UphGWio7f-9aql6gk-OjxkvfHhe5Fxl0g9Phe2vyTA_rfDHsNxnb5v0mjGcivJXCyGmGrni32Q_KXFMm9Qx6c9fmZZuEP7rKhp45xPqEcECIZNM3EP6reyBbV0q6BBOrLOukHG4TlrM4HUbPRq-iNXL2CvKIVR9eJEnsq44OvyNdPjoAoRvB9yKhtC0kGYVXbo40iDM1JxVDhoObxJfSFQsWJQrRPSMKjU2eGu-6jV7K7Orsjajb-mp7NUtII3Es3BWC2O1yJcIz_cwCFC4FfBDkC4Fit7NSCKrMYJIQ3GIxWZ2R3UfkTiNfndGlT_CzU-5xvER3DUCBQHmjXuiitQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79621" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79618" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه گل یه پاس گل</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79617" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مسیییی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79611" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79610" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لاشی
امام
حافظ
زیکو
چیزی نیس اسم بازیکنای مصره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79607" target="_blank">📅 21:10 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
