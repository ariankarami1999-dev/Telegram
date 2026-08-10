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
<img src="https://cdn4.telesco.pe/file/JVpKHfmKCLddTHUOEZv9EfRD045cHyEL2LCyh48ZVLyjcMFdNOAe10_a2i2-9V6VFhX7W0W66NZyNYf162Jt2sVwQdhLVLGELvXNRSVCw-Sin5UFSuS5nXMnwzeGY-e9nCYr8Exhy483XGFo2LRw6zNVp_DtfzvQv9R0FNZ3o6PZYMniKYCu7oHvu6yg_WmNxFpM9R4FA_UCXItJN5fDWn0DqFJfWWy7yjQYtMtiSuadiIhxWXozI5VoEtVbzqNKhqH59791f_RYwhiYU6Pbh89BQXhrRQi0P3JPc7XbbSCWG9uVbN2T_-n0CYXsmpVXpgxkMeDVppsEpY6dNShCDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 03:27:22</div>
<hr>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEUHpg5J_-7xE9JO5gWmUQQd2_9SnqJQWYS2Yk6jmVRvN0D_9m0ZzZcG2xA8FYuUcvEtX_lQ9d0guGgYNVZMZ5BfnhOhLnJ5abfhK2c0aMFZam2IHkdysgqJqOYLaOrc6MhPZw3XX8Qq1fLGpUdjBqtqBWTFbVVZee-leIOn8LVcLOIpdLnhfbLRWXqrSX-thK8DItDxC7f_JGEatzpkaBmkpYTi26xp9PbTHkeTEPNSAh2wChZ7YetFRbvc82wV9-9LH1qVf3_QQpQgacRqQFKK36nFmG3PG9E7XVd9P4mxyPrb5OwYfqqZWXFMB-T8NklkCz_b011LknxsWTAhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp5iZvW90EYRbXI43VFiozcAYmmwjAkAfoKJcXrcpD_OyUGpeOqe5eQ-_SnBi6_HTwkB_wvRMYmvCuzeczQFJevk_L0uqVLjJ-GKlsiZGxsgPk1ZLxMiNduUlV7-ch21CW8WNzZ2OU8BGZ7tkV2YFInA-_tWPGjyqkl5sm1NEZId8nU7zxgXyCxC0reGyNdBS95-mCmYifI95VmsLK9IgFWyD2bn30HFgIGym-2TA7jFPm_yhQxqzfljyGqHP0YLmh2WKqAUWcyBuNPce4GRpB4ZmwY6f5Idf2E415-Hl1WalwNrGA7ivUOXRu_gL01u7LOzx3PJhJF7L9KcGSP8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWU-AUruaBXSztQObPcV69K0CvR3ymh5OOf3a9VMyy16iJIZUuSkJBZXPFZaHwMmSx3i_Bab74Y3Fye1DuVm9olfqNaF9mNAR0DE5rV7tstIzrKCTCZlCJY9p6Su2YWiVqpS0rc1pG2FY8lKqGRho-DisYyji6l1LhopySUWi_50pTr6vGrRqato6NiL1ipxLEUm9xwMmRqWa12D89nB9XC24LZbiH8XZNEYuKjcx9T3o4CJKq-ZuLh42QV1D32JwnrGNd_kSs_iiv6VK8SZVQtB978_EPpCQadcGpyJgSsbQGs3P-NZRQOidSy1nE4z42xZ9cm1MAnZxIQ_OczupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=QVSj0k6HkKeq-Pw1OEckGzwezvq5AHJYSbhHhFrWcrNzOoDLzPhz-90ehrxirQ4fS8azm7RpDiTUGSvq2msMyJ4Jbq3zTPwuqMCc4hQvboFXRG8_cy5SbfOLqo92eFkuZFj9DtkDNB23hrT4E1TgdCYavZc-8AO_iz1ozS65l1MvVb1Kb9bmmCcNdW4Pv4YD4N9TlIafjZi63q0lPOF9VapTqW8jroEQdsAKBiBpFSi51e7kblQnApefqi2AvF005Q78eZaUfAu3FyxoR5UnPEk2Yc1-hqO0G3K-ZGKnug55vlb7pUwLcbpFNuz3HbymjRsp4zhPujJbDaD7lKdhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=QVSj0k6HkKeq-Pw1OEckGzwezvq5AHJYSbhHhFrWcrNzOoDLzPhz-90ehrxirQ4fS8azm7RpDiTUGSvq2msMyJ4Jbq3zTPwuqMCc4hQvboFXRG8_cy5SbfOLqo92eFkuZFj9DtkDNB23hrT4E1TgdCYavZc-8AO_iz1ozS65l1MvVb1Kb9bmmCcNdW4Pv4YD4N9TlIafjZi63q0lPOF9VapTqW8jroEQdsAKBiBpFSi51e7kblQnApefqi2AvF005Q78eZaUfAu3FyxoR5UnPEk2Yc1-hqO0G3K-ZGKnug55vlb7pUwLcbpFNuz3HbymjRsp4zhPujJbDaD7lKdhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=vwwYkNIGRtSboQjNVUfQ1n8OVw71HaVSQFZ5TpW7sc-XMHuNbk0AloOYZaUa4BbkqV9SswKMCIfMowm1p20GEzb5oDsZPOuqNUFykhzg4PG-UQK6x9ZmFvbDz1npJmiQM8QlKhoOdv4VOPutIuBMXHhjjj5okHOkJYJk-YJ6CwTRj_ipQhBpx4qSYbBl3zws9vxHz_QaUS_6AHKQpxBSeQP_daXrbOFeKAVpyFDgXUk3ZdWxR1HK035YsAQgBUTypXVdx-paqHBQcpIsQK4jMaqZGZJUCNvlRLn0xfJHUgqZsA-qv-jAT8xdkuibSEZYfy0jABHq7r9_mxvgLP14HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=vwwYkNIGRtSboQjNVUfQ1n8OVw71HaVSQFZ5TpW7sc-XMHuNbk0AloOYZaUa4BbkqV9SswKMCIfMowm1p20GEzb5oDsZPOuqNUFykhzg4PG-UQK6x9ZmFvbDz1npJmiQM8QlKhoOdv4VOPutIuBMXHhjjj5okHOkJYJk-YJ6CwTRj_ipQhBpx4qSYbBl3zws9vxHz_QaUS_6AHKQpxBSeQP_daXrbOFeKAVpyFDgXUk3ZdWxR1HK035YsAQgBUTypXVdx-paqHBQcpIsQK4jMaqZGZJUCNvlRLn0xfJHUgqZsA-qv-jAT8xdkuibSEZYfy0jABHq7r9_mxvgLP14HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjVg-MiXsEx-bCS1WuLImRogx8uoDR2Bd0bfr6PuycrYyoUgJKtAkTJhWny6f6uJqb1owXhX2110chJSGgGaMRvYS0gwcH1zEfF6Ofgtx4VWZaD4ZmnBYbmu0w53Fa6lwFfpUuzexJna_rSjisnB9FvTJXZYRRLOTEBS_vIGxRUDfcBV1aFnLw08PTb8wtcvzLReckjvcAnMquDiHo0CR2HQm73kBGpMfeORJNUj4MASNcMhJh0cbzKNYyl-t2xnlD064hs8WlHsE8Mlfa25MzANMgfeABmLM-NkPlaYWDI_3vqJKQ3tAuSDdZWAB5RHyOKZWyTYYANCGRQjfVg8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFjj45JymGUX216F3Yek1JfzICvSYAaLDuXt6Q-lzFb3Ugl-QflDBPfgV_VoZUYuFfmTnV6mkfvqvC773wYbdVruNkC-x-onmn8y8mkEKVNoM4Ac7tHk_K8Y_EBcQ3lWdwxogrZJNuTE-a_2Af2rX7vQ8fI7YJHbzLYuvsOJyWzSN5VQXSZLHMTE5l4V_DorLKijT-3skApb2rNfuFKYY222jOvpBVbEIcR-nseyR91iK60RBOT63uLnHJiuF7e39B1st9A0cuUH_k8J37Dz5R27Q83Yq738e2AWveHqLl9V20NyChaDMDFB12csPN1eFYlPQHHp4vNXsdH4NMR2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8XqW8oEFRLP2sK2bGKsvC-6IVNC9HvHIbpPpTXQ_AEr280bHsEwvPIpDO0HH8zlAt9UhK-CNPFikA4hcNueLZpZR4nrKhDJAxHJVpQIleREv7wDfbgkrP2Dbvj2ChXSrGnLlwHIfzHgEIxi7h8xs0zUxLaSwThsKLMK2trJys4kFeHdDHWhE80vkqTCw2Z3M_3qk9-FCGXbi9Hi9uPVZnEArndj5aSSkaxZw1QUkI-3fSZzESFW19zRXxr5DF9ne8ieAPFXvWeQ_BrqIVQf-pb-UIPd8FU0vbbKxPCL3KQKJwlACre3Bc6qsUZwOS2JDwfcxAvzL6aE1OTRrYOWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
g18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82020" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HsMofORy62VADLcPOaT3CzaufPrfEFN1bvx4Eadi2LITJzcG_1pZNmNK4grXBqUo8naHqKWp0iJcYiKyG-fILxh0F3B80kNnfhy5F89DMylLljavDDr1Ema3t790Ypo3ze7O_KHLa0XCkLUAbP3R_SsTKF7jYr-hMVVszNa9wYerfiCDu3maKkywLE81qqSKlD6WmAL1V9OKcwupI_MmG4JaE3bgOAPpy8yUpWptIt_HrAEu3jXqiIEHXgj51_Kf8GnW-J-dWcRvcOmsvkj34ZtJqSAEY_T8FVd9gsEo3IIShncNGQZetSjU2yhEFD4lWZxO0s7IYO08asQok_hlGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv5FiLI-Bq-fuWdd0JTT5hURKXnlmhgII2K9Vt494jBlz_DHQuENx8bLdhNszaEjqP353Vm7kTnxWLbryoT1guinRJKlUMn_9RI7brJvnPriZZjmJgkaFE2msrmcXhwMq-3KInk6RcKkSFWOYWkPkDX5MOyPS3bQrX_8VzkjIvv1BDrFLTy-hjj8BtpjRYCA9AY3IE1or8ZD8MSb3ze7Vxzjt63qItoraFLioVfS4rFFnmc64r34TO4DFX82NPJwHdk3cQ1JWAfe0RBWweucVged7ZQIcdFoZRs_y2MdBJ2DswOjByCuyS5i-3i51yQmUMJmcJHGuK_e2xdCD_Goaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHybclasVVnPQUmI2rGaVijLN0QAXYHZCzSsOPP5x8fgkX1GBJrKB3l51sa3hUZfgNJGmGYcAFyoJyYVWc5JOxbpOjyd14RnHuI8gpsO_56H1X9CCGkMMcTTq-prSJEnmBra-RleJnodYKOb7g3iFHtHkgxz11Qf_EbJpIVFikxo9wKic_Q1VMYpIJ3Xq2o2PSHwbQX15RgV1uvqsH0G2nRtNREOE7zEZCmfA_SAu0eETh30o-HD9cr6I2nj49F5UE5kCR7rTyzSE5HTCgH7y1cw7BxlmJn8ugHgpZLdHZz0uV29zVNQEhKisVsQCduh0N_3c65Aot1z0g8tPZTXvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=amCbvHkjD8AxyI0j3x4cNEWDrTVYOLYzStiystjoWrnSsNqT9a-jE0rgJRwAypT5VwFyditSHEveS22GQHK9vya1ucOvzelUdPEtvdgsayIMNtDSoC411M7Av8oH1CRs2q733NO5yA7b-jRx57yREtfnP8heEaRGHCoC0Pd1WJPip-Pkzxg932PalltoitJ-odJJ-slwWZY8fbEpgOfkFuP_UvwYcv1cF5AUp29EoKy6xtp8i2Pq0hBrnV7Mo8Nc56YM478etn0niqs-I4usBA_VJJZe04vU_Wwha-XH-8vd88A_-BEi7Qh645h-9G6myFm3WSvR9dnkFwkXoWurMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=amCbvHkjD8AxyI0j3x4cNEWDrTVYOLYzStiystjoWrnSsNqT9a-jE0rgJRwAypT5VwFyditSHEveS22GQHK9vya1ucOvzelUdPEtvdgsayIMNtDSoC411M7Av8oH1CRs2q733NO5yA7b-jRx57yREtfnP8heEaRGHCoC0Pd1WJPip-Pkzxg932PalltoitJ-odJJ-slwWZY8fbEpgOfkFuP_UvwYcv1cF5AUp29EoKy6xtp8i2Pq0hBrnV7Mo8Nc56YM478etn0niqs-I4usBA_VJJZe04vU_Wwha-XH-8vd88A_-BEi7Qh645h-9G6myFm3WSvR9dnkFwkXoWurMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVIxWJOxwRQsYIUrAuRAGk2mmWZAX0jd1edzi4pAnZKU5wXLA_lnH85xO4979Z2C9LpqTeAyMylMZnvynYeTmp7Z8QoMA0ZHdaDiATfKxnhOyNvwLJ1clydTVdigzVGFSMlAJ-RpQzvqXr0Bzx6nLOhoG7Hsx5JTPCITp5EX3XQpKN4QkzZbUs5F7FkmGOjXJu6jZNOCWSgJqy91ZHdf2AEB5lfTzQiqNnZ0Voro4MWLZZErP93y8vg0sFWixlhfQxx-GyLMjUKGpufFaPQfPfNrHhgdivcIfdP9pQmL_nwG0_Xc_q-Vdxb-1rGZ7E5JzYcDqUvtEAU_PENfYQGmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82013" target="_blank">📅 15:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=KzCbVk1NpQJUzU_d3c5pOAmODWap52QfZIK3LEeqNX5kboprHkaXxguWkpSRvGp_ZdsjE7IQJg9FMFFgvcC2Nye2XB0aNRe_Do8XD4O8-i1NPvGpFozjQCU39rDamOrnjkuDBFO-NcEh5XqMSy2Y1Q3drTAYnBSlVgb6bUHhomgYSr8kAAxRMyUM0vnVO0yOYDZUxZzauRJbCQLj79qNfZCE9WRTaLm4-Q866dbejOlOAKF7EMmPdZPOA9_BPbWxRt1pP-wW3mXZN2ExyZuj2mGzBAjgbt5yj6ioTpmVC0tICjfMJ7ohvE7npJD_hHWRkwL9ckQeQcmpx08SXmckZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=KzCbVk1NpQJUzU_d3c5pOAmODWap52QfZIK3LEeqNX5kboprHkaXxguWkpSRvGp_ZdsjE7IQJg9FMFFgvcC2Nye2XB0aNRe_Do8XD4O8-i1NPvGpFozjQCU39rDamOrnjkuDBFO-NcEh5XqMSy2Y1Q3drTAYnBSlVgb6bUHhomgYSr8kAAxRMyUM0vnVO0yOYDZUxZzauRJbCQLj79qNfZCE9WRTaLm4-Q866dbejOlOAKF7EMmPdZPOA9_BPbWxRt1pP-wW3mXZN2ExyZuj2mGzBAjgbt5yj6ioTpmVC0tICjfMJ7ohvE7npJD_hHWRkwL9ckQeQcmpx08SXmckZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پهلوی و پوریا بشیری
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82012" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=plGrs7KCWMt7--eNpT73VUTmCUNffvzipxum6l0v6Rza7qWVl8WKOMo6b8v2xBETEFYBdeamKo_wPGHuxmZP1CYYKOKad3TbLxb4640NI_hB2IRWXcumXag_P9yKnC1G-QcPaAESBvydj8XLtpyY2LMgkKYkxElOT9qN4wzAJvbo2nfpIQoiZgyEykJ1fzONs9Ri1xmfNXixAxHwitExGI28MbtrywWcg8FQ2MFeOxMYx30XY9ghg91tcI5FxvFP-jcmAjmdtjgRtDnocvJAQPAEtfoWtiQug9PpfklobIVolBigz3w6ZWoJLyaC9jvawraGxWqUhY_hpLtcQFIQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=plGrs7KCWMt7--eNpT73VUTmCUNffvzipxum6l0v6Rza7qWVl8WKOMo6b8v2xBETEFYBdeamKo_wPGHuxmZP1CYYKOKad3TbLxb4640NI_hB2IRWXcumXag_P9yKnC1G-QcPaAESBvydj8XLtpyY2LMgkKYkxElOT9qN4wzAJvbo2nfpIQoiZgyEykJ1fzONs9Ri1xmfNXixAxHwitExGI28MbtrywWcg8FQ2MFeOxMYx30XY9ghg91tcI5FxvFP-jcmAjmdtjgRtDnocvJAQPAEtfoWtiQug9PpfklobIVolBigz3w6ZWoJLyaC9jvawraGxWqUhY_hpLtcQFIQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZXk6Cp1VIm6K0EObxJQ_rN-aiJ4B1D0c1sXb_RgrWhFMYgO-pTIu_xSIPKyy1ARiqdPB4HREy1GrxV3yNc0DNcJSoVqrrEU8WhziZuZByu_h5eOb1eCMUA0-La8NqQDiwsAJGyl1xntxCZeNA2b0LL3qXMj5c16i5WmwVde7uvxLNPZwV9yOon26yrN_5gvjyFLjTvvv8a2-575EwhSp1uzhnNUHfnVasp3XJqP5uoSt181fhHIwKSU9HjdUMRQPGcs5mIXoZoz_vp_HKGpcvHSFGbAn44MoNZTiGcNQcC9Y9GZ3iLd-lsNuFNHyW7GAqkWk1gQDynChCwR_UHFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWPxLVBp2gMNKUjNnQD21dMBJ7WRu0noUNs4B8y94Wtn60mFrsbyhwmzC0HIAFSX-qrdD4ANzCHrhUhZa3Bp2F9CcQdB9dHkqgBP0o_eEzMp-8vkCAHcWnFj2UNelEwDTmBV8XQ_yDrFVN-jGP-TQpZ07O9XZVsiBo2CA6VzENTHRqQK-boBP8kIklO8iXjioMBgZQR-U5UQYUJf-pCgG8E1E4US3ZpUjLoVbpo38t5VkkPqxvq3fRDq7eu3s1bD31iX7DjJL8dsje-ckKrKJq64ZhHK8K7nsX4Km758grW1uVNep2SuLlIc0-4GsMRh-xwEtYNAK6zKBHHF0NtDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ectVdjwDgtRcEUPGjRPHPXZt99ZuQzcGG9XmEGSJ9hxNPvICprAKcartUQOeeB55gC8xOxM-DJveSeulJvvNvLKri9QfWmDms_-aYqJYNYSXM6EJNbWk8mlWUkhkSuGx61_m4QY1MwtgT_wAILl-SBpLryQRRU3vFJWqO9qzFXDwiafbnA6AB1QHkQsz2ZpTXjE4qufJVBhNoBsJfFgtQTVrDDqG1-eJeWDMnDCYt9J7XPccUy0QQ0z0U5IAejo-zzceHUeQ8xx-0pEADMAuKifonlU7cYNCuy1gqwdVHMu4ih-QalZIVy_gVe4sjbWGeqoPjPrJnm6PPytPyEoBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
betforward_bot@
کلیک کنید
betforward_bot@
🅰
r18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82003" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=DdMQVHQb4FJ9UzPFvF7XSRTvj8u0fq80Dz68d7Gn8dPpwPKvoHyJmilhHoa6w6gESHLDSbrZ6XDqyxwuB7qsDMHZ_mdMK_w9T9Qk1GkH0vCfL0ay_tY4CJGzZnVL9oEGdnWqyzCM6hs3CZIh-GAQ0q1suJC-xEvGJs_nlAvDCU17S6QnJnB09Gu1GZCn0c-7DSPF5b8adjKCSQOtISdT1Fx7jFiZDLuhYjEt-yciDSJzX7GW5sc5VxSux-GLh-LdOpzdzP_qlo892_dCKx8oosYlKwIJR_pBrhisKMC-1DIehsFI8vbJywguIEDPPLJr6o5Q7-cQMPeVF-xWNwG2mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=DdMQVHQb4FJ9UzPFvF7XSRTvj8u0fq80Dz68d7Gn8dPpwPKvoHyJmilhHoa6w6gESHLDSbrZ6XDqyxwuB7qsDMHZ_mdMK_w9T9Qk1GkH0vCfL0ay_tY4CJGzZnVL9oEGdnWqyzCM6hs3CZIh-GAQ0q1suJC-xEvGJs_nlAvDCU17S6QnJnB09Gu1GZCn0c-7DSPF5b8adjKCSQOtISdT1Fx7jFiZDLuhYjEt-yciDSJzX7GW5sc5VxSux-GLh-LdOpzdzP_qlo892_dCKx8oosYlKwIJR_pBrhisKMC-1DIehsFI8vbJywguIEDPPLJr6o5Q7-cQMPeVF-xWNwG2mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7Lap1jezi7d6khnkj9bgMuNW9If5t31Ufb8twXCj6AUA69OtCn_I3bWWcqIFJ6f16_J5MponYIvUkKGW5u9UFjNi4STNBUOiskT3JuQFKZ6DxwLwjYStBDln5xNITwaqwC6mK8DMtQev-F2P_m7V3ZO6FQp40eTA-0xIChWTPLutIcvmnvO1KXd-kb1ciaKs04cBl7LKdoho9ItIjCbO58bpJVAumy_BqedsKL84pPaiYoAhr-W8RtLaG2fuUfaVEG441zM-5ljEof3HmoBgariWOYaJAWav4rMK4vWBkOXNR5wOtDcmorUTXmbZYCezRYzqMYgZMa9UFldrjMrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfOvPbGbPge9DVdIGKINqHiURnMDDaUGab5QVmI6EQmhp46bkxE5aHVofoTtRhgaGW7vHWPO7ovJmfI20Drx7-6aObeEHVW92ina1tFRFjk9d5cxDq7yqDSYdx-32gb2aPSx-7z6qgep2l5LiMq6_dahfs28WIcUTCohrram_dTkZkBefO-LCbijGJ-4-Oao2v_DGRmoxLPHs89JnCut6kjyNUWYAP63bzXpkd_dDtA0nLjT9v8u_mA2QTF4fOO01yQ9U2SJPkhZhufQlvPf4KS-FHumcT7LwRKSOcnyX5VGdgL9NG83kdyKVdY5rKeJywGUbBL_V4h3aHUYgE5oKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i68wXcOo-faCNtQGnGWcB20--020XakweX8dPwSwGPHz8b1RpzVwjBY_nmQWLSTFEBxEWjfO2MJJXxb1xC2I3cV50UPKmewDVP4idghBYiywNXvVclybm1e-gFectNwP7l70BuKGrCVWv-tPN1ZWvKew3VYR_tGKsi-R3yuGW-KqzgiRfVL2incYfIGpjBGYlmMbno0cNMX6KudTifergpiTMJDDajBO4EFXShZ_H4DjkUXPvPL450NDTWG3KZpLTNaEy7m4wJ-ZtHFcWcMeOkGRqD8U5Zvvf1IoIC8w0NLDtMqF_qqs9KuFo4wPzlQdTQ6QJ3l4yd4DTwp4v6oMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX7cxrsGMGJy5kkdDqNILm9G3aNvOL2Ax0I53mBnS_cpyy4Km7IMjS7s8n6uMcu094YYNAchwWazpLl2wMoOxDVETaub-TIW_g9Jn9eXus9Ipq2KuNvLUu0qsGvyu-eBhODgTzp0OI4Ld29d7qfylM3_OcmKaSaGEJkULlpaeKhK8RepA_IiMexEpr_oHE1D8hYJzuxpoqWA2YEh0EEtjizqZ9afAwPOFMinCWZ-vWbbIV590bHUY6doE6ccdtYr57kyOmYA8XiqikssC9CtZR0aqZaRTCXnh_lqMNclBjTKSZyA1ORHOORnsGv4O6cuvPSDzr9C0B-R1th5xBV9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اعضای سپاه پاسداران در شهر مهاباد با نام عمر دهقان در روستای «گاگش سفلی» از توابع این شهرستان کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81993" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این کصکشی که چتارو پخش کرده چرا اسمشونو سیو نکرده مثل کصخلا تلاش نکنیم بفهمیم sha کیه z کیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81991" target="_blank">📅 23:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_VI40DsuDCbDV7Ryx4U4P_K1joDRlxZrtHq3wfsH_BzKugCfB2Jwpj7jPbzJJeIzKHGbvh1llGZGbYJhssx-JZ2WS_Wn_dQrmMa-pgag-Yqd8SQjW8xvUY_lIJb0QvqwWI0i1WSue3UuKX5-FryEPd3gJGSGfpDWiPySJeJNL1Q3Cngd23imAGDG4ZUK2vh_urv99Dc0Kg_8QT5juIy-ADZdSvm6pLMKIEtdvG6JMiNWddY7x85wrbCE6ANB0fBxTcVssq52YphdkRUGJiOo9zR3I461l3RFFPQuTGooTMW8sXqPGV1IJBHdFZrVQS7d8WfZvGpmIlLPQp2SQxNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که پیشنهادمو دادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81990" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-84ukcRBRvTDXNCNijdobo3c2kwc_hZouj95XG968uAIrRYfGCQJePzJJkC1s2FLFH258I4UyR6bYGO_o7f-PNH5y0ExGQYUIc859T0K1jsKreI1wfbatBLpkzNu-r5ETpbPHvEVtNtDC4f4mfBeKoMLAPyfvo9uVTx9NnULD2FVj_7JAu5a_6gU56qpRUj79LdzAFnBUp1OVh4PLfLf5Ic0dN49k60yLmPIHiS4Hj9n2ZsiFKHEiwagKm0ll2u9ZV1arPLQFCLWq_HZCClAE_YDLX9j-s5nztVhAWZLdZIZEbiw1DETApl2fwvgVG1ViS_oi6TkEoftPQnmaietQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 کا اومد به لطف بیف با بشری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81989" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کار به هیچی ندارم ولی تا تلگرام هست سگ میره سیگنال کصکشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81988" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه مردی برای مراسم ختم خامنه ای از آلمان اومد ایران ولی موقع برگشتن نذاشتن برگرده چون کارت پایان خدمت سربازی نداشت.
مجبور شد سند یه ملک رو وثیقه بزاره تا خارج شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81987" target="_blank">📅 23:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfukmZwhaTBXy60v7-A5hacXcfH9Lcj_QrOY49PaKzyjeY5fKAoMBJIVEyraRED3FeF-BwEemjnk8CPQnAJbQcWUOlKTFCz6gyDosP8wyuZotQ1zELBjJKPuchTPkw7kUj0e297i9zsvadysdkqxWh1KtFqd7ghp0u4Fl5rCzB38TbCHRFrBNrBtKkmCmQMfpjHmkRvpS4I675VDLMGRXTuBC8tYDUIoZwFsI7GHv0XKncsOIB0Q_JS5ssTohDYEhQEZd3xRxNqK5kY7PkJ0qJn9fAAk1r3Uj3uBLAeib0SHV54SkBYhVJg154qAay5tRv8REkSBzDLldNZUygsxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81986" target="_blank">📅 22:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbdkSgl5CPIl0aBQFnno3ArblhJypADtq3l2gGThVO2v79oc1-2QvD948-4c6EO-X0-VapZ-ftPKDg6rVQN_R_V9a5Ku7KmYzjtQu8s_qF8zEr1LVxcfyViQ0UoGFllgeIdHFeMACC7gD6LsfnEEwHsFSaFs-rlpnzVLK-t8hI9KuGzHJ78QBS9qzxEIbfcLSw2YAGZ8MX5J5ZmAnEfadpXvwAuxSGlHatwsSrnC6zCi44AUGchcNqTMRnsjEM265cVjd8-t5hkfDty2maiZuxOhn31vlEnbD8AZRdlr3yt16gD9YH3r_Xv7032FOMZ_3Ukhz9ePZ9HWhmylLfe6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81985" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پوری تو ترک جدیدش یجا به مهدیار میگه رضا پهلوی رو انفالو کن صف تو با ما فرق داره
ما؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81984" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این جمله که "فدایی موزیک داد جوون مردم و فرستاد زیر گلوله" همون اندازه کصشره که جمله "پهلوی فراخوان داد مردم رفتن بیرون مردن" کصشره، فدایی نبود مردم قرار بود بشینن تو خونه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81983" target="_blank">📅 21:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قدیم اینجا میگفتی کص ننه فدایی
خشتک رو می‌کشیدن سرت
الان چی</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81982" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbV-K1ZGzM1PkeziO8eOQCM0JcdVbd9ZdkKvBlHe0avBPJwleZBsSH8BcU3ebGdIw-cQk9XCqnSIYNVRkAscKNQJBNcZBC7fAPD1ThRLyh_OQGB9AWNmzf8f20Wft1qgWeGoL1C3kQ-PjxAcekzVISX8tQNWVCYX31s8bihUhu81QyG6fjcIpR5swXy-QC7TDLuKBj4waE-AXSHAgFIMECnZ7fIlb3cDbw38aiZVDOle8FqsfyMg4GzZmVcLkRIoQq8hsDyHCTZGW2d1PkOmodDoLYHB9peFR3v_wNHJEsK2nW0aymxtokZEIuuTufw6TgmD5s_rGgWO_QlKS9cyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی میگفتم کاگان چرا نظر نمیده، که اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81981" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق اصناف کاشان اعلام کرد:
کاشت ناخن در کاشان ممنوع شد!
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81980" target="_blank">📅 21:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جذاب مثل بیف آرتا و پوتک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81979" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تنها سیاسی خونی که باقی مونده ویناکه فک کنم با این اوصاف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81977" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من خودم تستش کردم
راضی بودم
👍
گفتم شاید به درد شما هم بخوره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81976" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81973">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMnbpK1B2pzxXAPIFQ6yJ5Cc4FNy8Gzo8ddDqddMJdnhcoz32v_aN-iO3SUUymZJvPXLZvwixSiiPsfJcsNLXXBNIj_wERSBNMeaNkqfww2ma8miUl116-mKJAwos9Ql7lkEyf293ivXoxsqFcFa2ichg_EUKsi-6Bv5SRCTjklQSYVUax3BWgd8L8LYMBcH56LzZME2koin1asJXyAvZLXsexH9O9AmbzLXuVt8D7ixsOG1QPg74Cc_DQm8c1LdVMVYJEceT1s-dNMF14pv9NFXo01ra6wK7bTWPGiCghk8ekkz7q7-VSB4pYGKjvV2ZzwDxtKjAMqZs6503XSaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتشه بری دایرکتش آیدی دکی رو بدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81973" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81972">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhhZPRLjUsB9yAV-ZHwzZ4x4W_gs5uT00ZabjyRQbQL5XSNw2GkjvAjT-alRDtV3_xzFsjI1JSgMcecEpFc1iMHAR6UuoZEkf6IS5AQFzNC3xoowcnHGxxTS-f2nhulg4g03YImTB0FxyEj7BONKoLgbdIAOfITDUBq2cg8J8HxMqHGzvONI2taj91wpgSeXQ_gHz49K2ZHmSnnemDFHwCsAD-IBJvr2cmhMlDZm6a61SJ5_VM213wb5Yvx9ZV6zTQx84y8vWzLoV7881QsLB1Dza7J4h40FZ8m3NzAnBr1GC-YLacAdUeDeDlDeOkriPvTnURr7IqVsT6CG7P_spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پوری گفت جاوید شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81972" target="_blank">📅 19:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81971">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWEkA7ANpd62yYe8GcKGywESSO2YfG5nxSzSg5zez3mkWbQiaGFzcgLEmkDgQc-TrI1cGOpcs89HwG5IUtqVMmDG_0k5DTJGYT9lIG7VDfU6AJgouVmbs2mR-0OT8bIMC3biVjuHi6KbTIFJdcMJQfiE4oCI6SKZcLtKFDAkBq3IcywAuot2scojRNWpX4l46EHcZf8uQmtcSi0nb-NLaaGr84d6QTCpKqeRcyWJfXMLNIG-q5wqcB483WILL5oWU9hSh7GW4Xwr3G_O1zVn3FXSgmz5Iuo5z4XrG-O6LPPNc9tASmjohAURudqeb7ouIO81UdYvbWJ2RJ1WMI2zNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس بک قاف به پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81971" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81970">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pldsUZvfOsAcqZWQUR6qqy3u2QX3ZMg3e_nQs4r6ktOoPJUKrqUJcnC10T8eR4mDHQZTIhs8iEs1Bvh5vgc5T2nJiZGGRNVfTHLl5ZJy5xxY6l-zZLr_-8grzZfbhW0Tr9_hcR85fNyZAJ9kXAOAL8TIrhpGNMI1PmCK9fn7v7EZN7pfLJZKg904fO-ttUEMxigaA87IMnPO9k85LGW3EhynxkXyh5d1ZBRp85asVoO3qTbWz24XK3mhZmKCg3nRuVoE5ZvZnqa1cDDQbOiIeMqJG7S_Z1C3hrybSaDi8iYD1xRF07xS5PoP-HgnJ6ya5wm5xHBWJkqNi7AvtqpBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۱۸:۳۰
🏟
ورزشگاه گاملا اولوی، سوئد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، پنج برد و سه تساوی کسب کرده و در دو بازی شکست خورده است.
✅
منچستر یونایتد در ۱۰
دیدار اخیر خود، هفت برد و یک تساوی کسب کرده و در دو بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۲ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۹ گل در هر بازی بوده است.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g17
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81970" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81969">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7Muz2RNF3OZYxurZF6z6NvG5AvKiyAiv6NoCZjMH1GRFHAry8UdXn8QMl_UH3YUZ72WlaP-9AiZWMHlUJqP2Ep5jYG5vQDPJEpEWEj8JwspnBuI4XnDktoQ-WCV9moiTkz0eVDnI_a_NreASB2Y-9lw-LEFooOyA1rRkdejJWuFf5L2Nbz4nRJiMVuDs7c7bdgtMjUeC2nA0I-8qhVAoXndUjBzGk_hrZpA4U5m_q05enxOJmvpMlegKdlm3CiUuEDfQ7zG8XaHuXRVOBufCAu9V0iw6ynkxbC9PuQTDoZZntEiSEKiUsWda4W3AyTPgUVM8XILFDqj2HDyagqeoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییتا اون یارو که چتای ملتفت رو پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81969" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81968">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLVpJMYnLB0Mj8mBlfaeg1wGm5fc3t_x1g7lAWAWlANEJYj5Tp1DOJLov1804q1bsozCdJQhyYy23GRbHCMWy4dcpczsPpt8YZVAeX2SZtbrggnQ2f8hE4oDo-OTKeYSk33kHp1OOGB9wno9adF5-oTqpnop1NSFiGiLCL6ntmnda6WrDOUr_ZIz0NBTQ4RpZmbVzYPX64neC62sy4ja6NyV5DnHEp19P4AjC3Ov7_u4m4JZT1JemoVwTvjIk1cdRNJykUULyGlZCuRzMMmGpoxMDZScpBRQ7RfJ-Ly2pTRl_9pNV1nvd_4yx8J5IdJr5-4FcmTBEaCmnuT7u5_9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع کار بدجور خرابه.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81968" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81967">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خدا لعنتت کنه پوری ریدی تو کریر فدایی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81967" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81965">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برگردیم سر پستای غیر رپیمون بابا، رپفارس اونقدرا هم جذاب نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81965" target="_blank">📅 18:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA²</strong></div>
<div class="tg-text">فدایی 72 ساعت وقت داره بیاد تکذیب کنه
وگرنه دیگه مورد تایید من نیست!!!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81964" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81963">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بعد یجوری از فحشاشون به پهلوی پشماتون ریخته انگار اینارو دوساله میشناسید، همیشه پابلیک اینارو گفتن دیگه، پارسالم برا اون اتحاده اومدن ازش حمایت کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81963" target="_blank">📅 18:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81962">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چتا هم احتمال زیاد واقعیه، ادبیاتشون خیلی شبیه فداییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81962" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81961">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من کاری به هیچی ندارم، تو این سالها هم یاد گرفتم به هیچکس اعتماد نکنم تو این فضا چه فدایی باشه چه کس دیگه
ولی سوالم اینه، اگه فدایی کرج تا لنگرود رو نمیخوند اسم پژمان قلی‌پور انقدر ماندگار میشد که الان داداشش انقد معروف باشه که بیاد برینه به خود فدایی و همه ببینن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81961" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81960">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">من متوجه نمیشم، مادرجنده بودن فدایی باعث میشه که پوری مادرجنده نباشه؟ چه اصراریه داره برا ثابت کردن این.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81960" target="_blank">📅 17:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81959">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81959" target="_blank">📅 17:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81958">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خوبیش اینه کم کم دارن فدایی رو عصبی میکنن و بالاخره میاد تو بازی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81958" target="_blank">📅 17:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81957">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromㅤАмин.⚘️*</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPxpvYKjC-YlwG61-Y1oiJKTxncYTh96E4OjKUklsyjWRZdVED8axRncAQkg1uSew1CFciUHj0vzXXziQ71Aq9Hya_brQBn7WeYxPEQfW5GczaQpN5x7wK2gpG5lZwAWLzMWJQk51ihlk-jJttZtZ_b-9lUk2ZzwcK-KngusPJlnINBuqRwR0HB6VL8CRVoATgRax_EuXALmmOW8GR2f0wNAUCm4w0h6GKZKpkcaOeaXPxxE89ieHhLPBuvwdO1hFd--q36u3CG9hbSszMbtPQ0jvqgee4DK1243ffXz4Q6a4utfVN8ZDyK8RktYGcE3jIbRL0a7ZGlqECLwxxHAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81957" target="_blank">📅 17:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81956">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81956" target="_blank">📅 17:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81955">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81955" target="_blank">📅 17:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81954">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81954" target="_blank">📅 17:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81953">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhzaV2yAGYKiDrdKM3rZiZXk82WcEisW9QypKSgJByqnUlSLq1e4vVKWKn92bApUXfD0H9RIoCwSX3IEfI7oOaRD4ggP6yu5M3TOF6usCOIJH5l5qzrxR_QJaAOFCEovaWai7xIfzr2yoe88m96Y8rq1MAn_ef-cvW_SWLusja5d_qu40ZW4uWiloLPyvnlL7vFiEiJ0We1de5MzQawUMNCnAcboOzP_vNFu4EXV7NBJ9KQVFCVbElVq2uehaVTUc7Yjf11efCrpvhCp3EFBImIpOkpi2K8hgDTLr2Uy2uzldicr216095259zdd9Zpy7TPFAGCTca3mebh9fJdsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد
YouTube
Aparat
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81953" target="_blank">📅 17:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81952">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81952" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مگه اپلود تو اپارات نیم بها نبود چرا طول کشید انقد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81951" target="_blank">📅 16:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81950" target="_blank">📅 15:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdEOLzLtxKm2M0Riy0sV8RUStaaiCQH6iXcDpz1xT56UIoyFQwdo0FKZRO00OvCkLTF956VSzUbBKnMiD-SAiRvySGiJC99GpSdiqU4fOZb533-BOnReu3Ma5L3y0Ol1OJCZBanRnsNyNMZCuYtkhn0ti-cPwbDl6-uHAmQjkrra95EaNUJSajFxOAccvf0EfvqSUc6p7HV28HkWzQPq9Fy6weLz2Qi1qI1Ha_BQHbcn2szrco0Lj8Kg3v47iN1tq0NwIySqzUgSwpT-CI-PCe5bBNEoJfmHg0_nqNANXB3IgDSXemXZ1uUE_Oa0nxAW_yDaiOyT54O0NRXeACiOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
لینک حمایت از ارتیست
هست چرا یوتوب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81949" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81948" target="_blank">📅 15:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81947" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJWsx1eLpgP8cgeHzyowR2ivzwQWQ2fIIYDutUGfy2kKQBqWhELb20cGnE8SqgaD18oVprAFsPrYrZJFtsO4D908YqT8c4CbkrAb3bt5FLAWZQ1xdtx7yvFpMqTBtEt2LU8NY5YBRB4Lv-ghK_3Mlj54xFieTQKESkdakFwxtNrdvuUNg11W35FmrMXuzgFlq9w1OmrQUkA_tq8m4O3sxKeUvsCVeB6xZuFHDiXOtWy0YOr2mlt8csL22OHWY_C8t9ECHd3riClR5AOtKX84aO_Bi8ehSYTCzDtADRyJ4MksbzPb7N7ZITlX7VYYJS0LWYTaJcTTQUlDWSa_gcTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریود شدی کسکش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81946" target="_blank">📅 15:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2BDP1MNrixwM2rzEFIVYsjlku8oEiuFUSwyOSbC0RX5MEmZFWdgsU8bXPRlfIhq_BPzoCS4xci-b-1-zgQkONwNpomDy3i5XkhwNPkeuCrnjk8UovyuqUAOs2PNapaUQ4YU6QcuIYBdX6E7PSYYTdoF1utan5cRt9wlJYnitNPkQqZQ38ExQ81Lgw5ojJYsq-xiy2KlZ9tT63jmaW5HDKANAYK33WVBh9WUzFV-Np-Hx5NyVcTRqn4LIMS9L-UbamwUmoe3Wi2U1UUwS3Naf-LJrhgSBj_fID0uGf0vh_5kd7TlOZggy4oGbSpPZ8NqXv0NrQIx6BOIc31DC3NGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81945" target="_blank">📅 14:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبر اومده بابای مسی فوت کرده ولی هر چی چک کردم خبر مرگ مولرو جایی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81944" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صبر
صبر یعنی واکنش در بهترین فرصت
نه در اولین فرصت
پوری دوباره اینو گذاشته چنلش
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81943" target="_blank">📅 14:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=m58rXi5Y_Vf-ueymMqSluvCjVh7QVpgdFejxduKlqknzshiPfuS4Rm8E66o0o-I6jsygNisAbE_PJPS83tRLGDk4ge4zuIincWugcFfbw9JMtHt7DbEzWxS_nlpevCnoMPGIn-I26ZVG80OwsZpip3xm5PXHrAZAGyyhkv4-D-zLX9pEkZldrthjtAIMI0btkxBWY8bu36W41FsNfJEd1D8tnr2jXTkG2-FXb8nQzJqsPiBv5o5hHj34KkOLrXsb02YIExYepPp70J3cQDx0B1GvjPtvWmbQZimqPTLoC6lkHCMHkWVc1IfBCMhQmqyPriHoi9YwrvvJ-2sJgVWg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=m58rXi5Y_Vf-ueymMqSluvCjVh7QVpgdFejxduKlqknzshiPfuS4Rm8E66o0o-I6jsygNisAbE_PJPS83tRLGDk4ge4zuIincWugcFfbw9JMtHt7DbEzWxS_nlpevCnoMPGIn-I26ZVG80OwsZpip3xm5PXHrAZAGyyhkv4-D-zLX9pEkZldrthjtAIMI0btkxBWY8bu36W41FsNfJEd1D8tnr2jXTkG2-FXb8nQzJqsPiBv5o5hHj34KkOLrXsb02YIExYepPp70J3cQDx0B1GvjPtvWmbQZimqPTLoC6lkHCMHkWVc1IfBCMhQmqyPriHoi9YwrvvJ-2sJgVWg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هههههخخخخخقخخبخی۷خخخخخخیهیهییهیخخخخخ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81942" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2JylGOaKVxJPRUZnUMMtNzw9Bx_8R4N9k3qWKHwI0PvOjY1B4FTvJuEeXImi5Q97w6z5j6qnLuT229GIZsU_23xUOYOBcGpWjsNsDEJxErBDocjlFsZrlTsujy94Bhc4zSNwivpCLv0gB8qu-oHelc_hjgGzERDnzU_U0ouOYRyOynvyw8N4WfUmPvWKMwmE2gC__NA5PCM2i1se3SFFhDGnYL4spe8rzMnf-HYDYMhvhhoPuuc_iSijgzUFcWtAswUy6b5Jt8lr6icqkftfDheLXgA5tcD6U42J_nz4XfSHcOnm8bxzrmEJanoSXLJoZ9EOxu7LsBPplR16nahxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81941" target="_blank">📅 12:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEBoQRUY78lGOU-srKhnvYnhMsw64Ws6LgunrC0KE1XZkxZY5D0bg8uuyahIP_5Eo3tm0L-MDrBRHG9rrr_fyTsDJwvx7H7e2-B_ufgp7Ycdn0-2IaAf_qsfEupoZ8o161ZbNLJo-fo3ssPkL4ytEcWk1Gl5raEe_BJ-MuKTvOFGmRjF1T7uj4qqD-GfqUs-LBilLG3PxlJZWwAsJkH3RFarP7o2p4UyGUh7t48KR-B02VNzDIx5QLm6Daeuob-R4Ug-a7bqdYu9ipOeGYFcTuXr5GiFa6jJ_xGiz6ddeE0thidz3bSTTTmVzqs-qX1tQAjMVoCupxzzm8FqGKBPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81940" target="_blank">📅 12:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAy7p3fUd7GsAvHOYl3woIGVgdQ3vcDlAxis6FuTwQkrhYW4l7CwpCafs6rPjaQTck2JZGa4Xq_e_Ee3GS7s5FsZrR74IAkB8Er0zdRKViGVz-e4riC-6b4tcGCgmBkh8iA42RjJU4GKIuY6dJ4ELtqZdhmuhUJBjtorLRMN5aRjGmxFUDOtkcCNw6wdx82uepWI3lnrgP0T9UhEjBloQZQF8Pw_YYwss_Eu5a4un-71oXFF53tYryHUkychQ8kgyrkNLVfY2e3xVZj2eJlLwLPu-vK51o5Ck8vA-t4E-LfR4fl29AE-8rh2VCaT1hG3RP5YHBWJEczKSkA8kow6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قوه قضائیه: همه اموال منقول و غیرمنقول ساعدی‌نیا مصادره می‌شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81939" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktg682xsexDn_nAOFmr_gzrvzdQlOpOAVVp9y7ZRjfCpXzBNl08w4W1udfSmEK2isNmFeYqeHyMKm3bpWxwTwD0MSJunpHZ1yQPUrXxCGx73Ae2YJbNAteHHdi5iTY-MYdmq5eg6ME0R640a6StQusA9rXllTAnUbu5JBQHAzT8C3fvtLG2xGEfSsXzxGX6vmR2f3pp-47vNd6cO8Inpp_DjPM3YI3T_gs0STH3xluZiwAD15dt9B3Z9sg5Jr8AZlPjZ9OuBZ1W7CDGKdq2EI4gviK8jUuaINx8Zu_njAfh4NJq0602r9KCZfUm41CIL2OHvlhdk3cjr-s0uiuW5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۱۸:۳۰
🏟
ورزشگاه گاملا اولوی، سوئد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، پنج برد و سه تساوی کسب کرده و در دو بازی شکست خورده است.
✅
منچستر یونایتد در ۱۰
دیدار اخیر خود، هفت برد و یک تساوی کسب کرده و در دو بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۲ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۹ گل در هر بازی بوده است.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r17
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81938" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3XOsxBlRQpJuTisTIxU-xuqNMH4V6dCvt1k1vxfp-z9RAX_weJaZIfaB5lACk9vTgbe9ndXj7Sgmyz3AMamNRCcMp1pYMSViCfZGnMAgSB74_YbCMSYL56Cpuyq853xdLIt6RwO4duVvpjb1FjMTSqy-BP71P0KY3vNJLL4UqUPa4P1yCpNVgNA5Xg8c4RerQeX88EA0yWe_dLZbyZePhuizCIrW9p6wCrOIeEiatfUyUzIoN3-fj1TbBOx_LtjtVSWzEgzIQQdR0Hrlq3au0McQBgKkzFN655DbSxdJMQ46unGD-GgOJT0NLR9GQ-FqKIdvbxNmzmKWU62Ee7mbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک لیست و فیتای آلبوم خلسه که به زودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81937" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2u_MBslNW1MKJZaMYA4JIxnkgU1a72fbfXAu3_7eYZcE2VM8iaiu6JTatc6w-Olgxx0uBtJlHGo-pgot30m9ja1ltjTFTuTsYpEAsfIw68H8oPeXpJ33Z-MIhytEPn4GpAmN2Q0Howxswm2AmExMj8_8xUQlv2pWXtm7fzdp3VgCNEHsmcHs8Ra1ujrIae3A742jZg1-8ZNRe1ITeWM7tJbfGf1899J4qkQeNvpUfZoAx0rjIhHRY7Btoy4s2TIOhaEPq9JXTkAHjGQUQ7ixEJm8Re07OtC2AET1_iefKkZsj1yqp7G5owk76A-O70p7H5PZQLjbzYMI41QBevh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها حالتی که ممکنه پرز لحظه اخر رودری رو با ۱۵۰ میلیون یورو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81936" target="_blank">📅 10:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/funhiphop/81934" target="_blank">📅 01:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حاجی بارسا چرا این فصل اینطوری شده تو یروز بازیکن میخره تو یروز میده میره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81932" target="_blank">📅 01:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81929">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxcMrMivviiPaynzr_KMRqk4hN4V-N2uUgYQYq3b3VltfgIuFaH6Ge10t1H0rPCVdovv-MuYfp0wgWFCHITsKy1oQ9xqLjT-ffjM9x7koWTq3Mm0d5pFHpWv0D8CmPtwgNxjngg6siv_ZvnqbiGtQNrp9RYRCJ2ArMrQNxm-pqPEPy48NOivbIdHgGVNHqoUZ75HCW0dHSx-uVVHBJVMcQFW0Xfk93k7euheMkYvysqFTC5X9smJz2Hn6Kue6949g_qd_z9kp3wffcyFZyg_Rjfu1r5Awd7ZfYP17DCWq3f2rE12aSfaMZQdRD00iKyuT1uVPucQdjAahHJdjq5hEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7fDwGI20rFshUukgH-1Z2XYiuOqgsPRldMlsWq2hDYbMYTSQtw3FSCI19kTve1v2j9tqB0_Mk9POI3K2KOUldqYBCnLUJmpZ4Jc0xq0FZOjn2LTfRX37pa708K9zyTqNHvletG1vAL9NjOKPnALrUsV5APk_6QFH5H-wULXyQNeZTEpV4eXECHEFHbuEbjsBRy7lELLuiwf7M9Cqj4onzJk0Nr_6KBhfLWhtQlHMyOTWPK9KTdYEfEtM-wEuCLO-jnoigK2biCzMIe_0vorsCKCyRVbFpCIQPrV1ENTv-uBWwZQNRMXKLyfn0McGKXaHoFC95HFEeeLpXNmsO8HCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رودری هیچ پیجی تو فضای مجازی نداره، حالا فنای بارسا رفتن سرچ کردن رودریگو و رو اولین پیجی که اومده بالا کلیک کردن رفتن تو کامنتاش دارن اومدنش به بارسا رو خوشآمد میگن
حالا پیج کیه؟ اولیویا رودریگو خواننده که پارسال اسپانسر بارسا برای الکلاسیکو بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81929" target="_blank">📅 00:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81928">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=cxlSY62K6PRNpPuLA8-jQVYCfbm2Pkc-31Y61-KAqFiry7GzeNlc53TBgjhMuVwpqG2GKvlGJ7W2x4-ion2l2TySLn7P6TfcIeFVSbokdfScCnacPFj0liu5pc7gZbtl_GjeHLUBcAuPaQsgYu1jcSozldGCDL6PdmbojEBZ6ow6azxjoY7hzggodX52QzUJrEKGvNeNohJldBeAxZ_EsmYydVVUbTi5KIDmEy8sQJqu85rmFuaf7qMc67Ts6k-I5FLL5IFKHvsft02suaoZ97_Ny7UaE7CM1oDE2JeQ5BqOkZ_xrA3w1uZ4_XkS2St5Rin1PxKjnxh0Cpvt26vbEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=cxlSY62K6PRNpPuLA8-jQVYCfbm2Pkc-31Y61-KAqFiry7GzeNlc53TBgjhMuVwpqG2GKvlGJ7W2x4-ion2l2TySLn7P6TfcIeFVSbokdfScCnacPFj0liu5pc7gZbtl_GjeHLUBcAuPaQsgYu1jcSozldGCDL6PdmbojEBZ6ow6azxjoY7hzggodX52QzUJrEKGvNeNohJldBeAxZ_EsmYydVVUbTi5KIDmEy8sQJqu85rmFuaf7qMc67Ts6k-I5FLL5IFKHvsft02suaoZ97_Ny7UaE7CM1oDE2JeQ5BqOkZ_xrA3w1uZ4_XkS2St5Rin1PxKjnxh0Cpvt26vbEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر جور به قضیه نگاه کنی خدایی این یعنی تعویق دیگه.
ترامپ کنفرانس خبری خودش رو لغو کرد و به خبرنگار گفت هر چه زودتر اینجا رو ترک کنید ممنون می‌شم چون ما یه جنگ داریم که باید پیش ببریمش و برا همین باید زودتر از اینجا برم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81928" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81927">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAr6FtKDUQ14C_bk1vmytny1Qmak_lh2PZcTaMXabSYVW8c9TOegcZyNJM3rLZ7Z877LNxt5CR4kYWcE28NCs8g3Ww8HHGXdtfeFNMvvnAm9muJQmTJhzN3PZy8mhWr5hFWuIheiBc2knJtTzDtj7HltDoQUnjPXMjdEOcuH64IAUdiooQl7DsCaxntwtas9nzgIWEUuiKKHcsyHlt-w1rHJcivq7tuZ6LxHHFmsgEClclqyOGhN5G25d9GaH0QL42ipYqAWP8hetQDlt8SioXMnljyGJUGdFGIuoPMki9i_DVHAdKWqd-qRswZA6k5zFx6Vi_YCN8FuA1CuMZ5XvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رندوم ترین عکسی که امشب میتونید ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81927" target="_blank">📅 22:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81926">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امشب میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81926" target="_blank">📅 22:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81925">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81925" target="_blank">📅 22:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81924">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81924" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81923">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81923" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81922">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBjNI_Em8KPwmK42CTGnVgqadKZAcEZG-mW1BgEDYmomd3VyjuSpgUgbSFlUHK67qaXOtaWQn8YImXe176-c1C2TqODPJUXA-RutayXqjIMtE0vvoSuXjljfNHdDgZczSKzTZKT49-dPjim1qKa5lebbGhskZUIIyegtCy8KFsRa9gXS9yiaVR7x2hmHv82Epj6SIFSAyPKfqixyekIXbl3EuxEk6KCLB4jWIarZKTwbvR68G5NdKasq8jfyN1EFGUKLvaKUcAcRU9VSi1m0WVcmbTnfuRS8lod0EIfFII0PPfhnifHA6PFI-9WN3xxu1GB64qomsSRc0rzs2dCOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل البوم دکی هم بزودی منتشر میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81922" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81921">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuivUiXtm0SNfMRtm0yVhOzQT4CJBaTYKA8SqXypPkuSaMHFNmZDboUW7g7F5jQDcQSSHBK8_nXGXrgxAKxNMSo4IYZdT6A4AbJFQukE8-Y1VFpq_XkW8h2hTCW5kyUqf2kiNE6wDb_RMsBFeTGdX9eZ5gUbr4MmlP6Uqkg52UnAEfY63srcKj2Ifwc-aYlH2i2NNYMMWVJS2l9T8StUWiQnnJKpG2WemTUlxpVtDz9sYiCLAu0isydJRdKNWhdKbB3KVJJRe5xgJEnAhdZE2L51ZesV4mkPircLgjTktx7KEhjJeZGSUcnfEaKD5iZk62o9q_1zRSsTsl4sGyUroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دکی از نامه ای که مادرش براش فرستاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81921" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81920">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=FxXEx5D1v8VjCJodLo8AuX4eB17wJ-80uc9pjhhBmtw-1by8v96iydhVxiDRcWIJ3ulS_L5aFuXd_htgrJY_7VtsWTjzXcJJP7gSJReUQltY54RSkkA1A3wJXs0sQc18rZulJjWa3jcWB5R1UwIoOV31nPgxJ5VhppT7ahXGZzseOu_ZqRf5-v8FZARv_OFHeXINkmlTFw8jgoibPAMW75sqCFDjOx0mvO_dR_FQvyjfcWnedK8Vd_W4uy9YXo-rIQWW9gi60-zoY838Y3mriKHQYUfXW50y3yI6V_UEDORrJBR-fiKdAUMzSqd7_H3CzNcF73Qy0XeeXzCw0xIL56MDjPrPUE8Ms0qJWJgwUK2t7Iosg76X_pieiKHXBfWQekDVSdVXa8p9VgtvU1EuqL9eDzPsBbGh9F4o44bHkSSvlPXByAMJsi-5QiU9S9C3BXkrdzHJelEwHh7vsl9L0j-tJmJIN1cGI_kwB63btL58i95J4QddwSNUjE1WCrXXFvrU-Baz6fcmdx6hN45zYgKy6_vx9eszALvm5DSC5JpmRmRbtrhCSCY6bamkQctF2YTnMbCFIwro6rZqZbIeKp2nI0qTj5HtXn2J-0kRE3ggVEgPUsbmyJ0RgCPf2IlAQDLM2-tQeDl2xjwjU4yc18U64W3P4dzd2W_7_wqHEu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=FxXEx5D1v8VjCJodLo8AuX4eB17wJ-80uc9pjhhBmtw-1by8v96iydhVxiDRcWIJ3ulS_L5aFuXd_htgrJY_7VtsWTjzXcJJP7gSJReUQltY54RSkkA1A3wJXs0sQc18rZulJjWa3jcWB5R1UwIoOV31nPgxJ5VhppT7ahXGZzseOu_ZqRf5-v8FZARv_OFHeXINkmlTFw8jgoibPAMW75sqCFDjOx0mvO_dR_FQvyjfcWnedK8Vd_W4uy9YXo-rIQWW9gi60-zoY838Y3mriKHQYUfXW50y3yI6V_UEDORrJBR-fiKdAUMzSqd7_H3CzNcF73Qy0XeeXzCw0xIL56MDjPrPUE8Ms0qJWJgwUK2t7Iosg76X_pieiKHXBfWQekDVSdVXa8p9VgtvU1EuqL9eDzPsBbGh9F4o44bHkSSvlPXByAMJsi-5QiU9S9C3BXkrdzHJelEwHh7vsl9L0j-tJmJIN1cGI_kwB63btL58i95J4QddwSNUjE1WCrXXFvrU-Baz6fcmdx6hN45zYgKy6_vx9eszALvm5DSC5JpmRmRbtrhCSCY6bamkQctF2YTnMbCFIwro6rZqZbIeKp2nI0qTj5HtXn2J-0kRE3ggVEgPUsbmyJ0RgCPf2IlAQDLM2-tQeDl2xjwjU4yc18U64W3P4dzd2W_7_wqHEu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز جمعه شد
زاکانی، شهردار تهران: تنگه هرمز در صورتی باز میشه که تحریم‌ها لغو و آمریکا غرامت جنگی ما رو پرداخت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81920" target="_blank">📅 21:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81919">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSupport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICxIOLhBt7uwOZ5KrK_TzgIBYkuiPkLUVKP6uxIRKFboh4DaDAWeNM-1lA-q3ib9_BhLlU76NQXa5oYzk6q5-Jh3ufNJAgU3n8M5wdwmA3n80bzQRnlIJDLCTU0rLJfGb44XDdevuYrDs_-BAISu7bZyoAgQ6Vo2rnlHV24iGilylPH_aNDluEjdrN9dnrzW3WrRDAp6cntVqgNhuHFVR5tBRaZ-8af5s97YfTtP7vwxBkxBrRa5OSEO6XdnZO5eN5Dl88hF934VC5fDGLwhyKXVQeT5WKD1jjaQcopHMd1F_csbSVPKUS6kYAymeymXko_LEG8KcLS1r1LCQZHwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اول تست کن بعد خرید کن
🏳
50 گیگ مولتی لوکیشن
🌍
کاربر نامحدود یک ماهه 105/000
⭐
⚙️
میتونید وقتی که لینک اشتراکتونو به کسی دادید که راضی نیستید در کسری از ثانیه تغییرش بدین و از دسترس همه به جز خودتون خارج شه
🕓
💬
پشتیبانی ۲۴ساعته
🤖
آیدی ربات خرید:
@SirenNetwork_bot
🏳️
آیدی کانال:
@Siren2rey</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81919" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81918">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سوپر جام اسپانیا این فصل بجای عربستان قراره تو ترکیه برگزار بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81918" target="_blank">📅 20:35 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
