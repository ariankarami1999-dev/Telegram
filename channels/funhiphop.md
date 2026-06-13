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
<img src="https://cdn4.telesco.pe/file/vkhcwemlJbPYmHtMrLqr8bhhac4GPVW7D6W2HLA5JuSceKzNkcC6SbtN1Se8HohsHhlg2YW56ZApC6RDhNqsiS59cLiYmfYi9ZNv0pS4KKIyCnrX-k3dsefdBDkyxRjw2oEpD7CAAyqq0zgGNXx4Ah6GbIhddloSYOEJFJxUzgKyonpb71o6R0V9O6Bn6viP3XsFd2XfgWbiQ_2aX_qBRa6Zia33JNGzHYqcXM9aar_2A8S-jA_9Fmm8FPTcpq__dT-VbhHvNXh-1mSDK-f1ELlKf3z9Zt2mlXd12xV7DHrBKds_XCoHPUXB1xFumCY4-HFNrAEibA-_LT_6PaKLxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbPfzMWH0OBSfWvsFa_kttAriGWAHLpUgLUYePEeU1rPo7UlmMkzIq-1NyB8QkX8c5wkqFCtHfO-YWJhonqeqxV3f_QWPFAaVMmW96y12GilVBNrYUaaEcX6czC_heDVxOe8aIdV2aXSDS6dt8wIea9QGonCeChoPJkcJ2hMVHJwvZTIOthwOjXvgGlqpJrjabe-uLPtMT9-LdvPbvKM4qi_zSCbZYiSUGp177L4hQviqotQYuVHqlG75OgFXRO8ynfVDNCARvZRqMQeJ9rtY8hIUaiACzwPFgo-7HmFM-Vw_rMu0IgroBoS_Qw7uGnPvWYblarOOj6d0vJM1uBMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD_ZOMOGVIWhyBSz1KuZPyMDiKcLAJ5ePjGjgMjBtfUSJDg05CnAMIvkvOFQT1i8GGhV-PQrsE3L6Yk3c_ENiVIWg1sveY_FLFJoYUNx5ekQYCn_H2NFKvJ7MIhr72Rso6HBt7KJ4STZU3lG7SXmG62H_z_xi-zr9xcxaBPvYy6joH_M5da65y4VJ8-eP3rws3GQTl1a5YFmz01C9GJ0fHzmTggAvVuWsDAZGV-hhchYcetZqKdMM-MccMLG7cjzSFAJv-GwFoNkcycFYjC3YpAa7u8H5YluogUfTtUhBTrHnpDb218W8GhCnKyog0zB0glQiVOCg5oCxV34H9BunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g23
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6FAFGZb5Y5CIg3XoZVauAfoyogmA9L99a1T0INWzK-vz09ZVHLhvqOQ2z6q4_mmebO6rWqM1fpkK2OcHJLwegodCFK8YUxrMBoJHN4RX3F_ajtQQe7VKhEBqKfNGkkh8RrtZto2nFHIUCoNnHs0WdtH9qbGehXwh90HV2xX4RngI4-nInXzSJewiv1Rx1yFTNNH5j6TwJwQaOuRJUvwRnrVBqDq7g62kCrdJPMvDqvTvRonwtdLRUKV4s0_tHwwvMI8Vf6uWVDnfQ-zqnX5vNEi08suONnuEfh91HniHfkG6fT_41Hm-h0tzQJZMd0C9AuJ7L8OGLIYvQeuiWz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان داره حرمسرا جمع میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/funhiphop/77770" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/77769" target="_blank">📅 14:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFP4uQWKbrLkWMyS7iSr5YPXhjUGexkGxaudRiiQ1zB0sB4xS0ciB7vzpERxnbyEkyYUXsoPQiniJze8KkTRamF2ZLRW-0hh0a0jkTIS13eQDdJJaRnaERjnVw6Bb9_T-UtTlavpZspTbu-UmGpFjhqs7qxRkC7KvNXy-_XMrGnarV443X4X1Y-Wo9axht9NmqJwRZ3fbQ2XRFjlHrNufjYqc2cUvPg5BqFZ5B_h-vRBWeEd_HptJwtdoo9rCVmE4xREelemyJkJuWf-z5XBqATiBE4E30fshQlPCiTDruTiHGwTFNJbNRZxRrht8kbQut1wB2vP_eCdSx-TkMFbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/77768" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owzi2hdnXjf2xleB8GCupAWMniEfqFsmfXgnQkGjXc9NyC4PfhvSr-pbsNLnuT4lLf8XP5bdHLFbIzOjt_Nk19y9jc944rbZjcp0EEy7mO0CpnTWV5sQTz3xJkq3EWerSqMCNF2RT1fZFQssqqicZQa6ZorddO5lEG8SuACRzlyPpYn4u_3xG-ceMNc3cTM7YWlwb6DVmxsoJj_cr6ZlLGHzDFNl3XJXhGN-Qtq0JshdF62DSM-BABv4WkqcsQySwf3636Jb70kTgwv4pfi0J-Q1VCIYioNcWG2Zn-Qg1_MbS5M6lvFdHozIq8rAMvEE72TavPPqwNROvEefkeSGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف:
متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم
و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/77767" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چرسی داداش چی تو خودت دیدی سولو آلبوم دادی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/funhiphop/77766" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmcsG3Oaankc6t4jpoA-Q3E_wBP7lyLz_N1cCQbPyYliKZHy_3WGZNFWjaeuMuXMagDktp_vokARrJa6iC3zJnrTWaFULYJXFstceezUFGed3_MJHwfe2gN7XDWfMQdnADYSko4Kc7k5q98P8ED696hJPnNyMAoxnSkEo4lLG0pqv84azApCsRPovFngzBmV5c8FWN32PJm0UlS2R0fQz6lAZVPsiwbEokSfEu5BZfAJXWtS0EtmqEukUmDb5fYxEhRdkxcJmICP8I_qa9s9h4yJ_zi_WnQsyLfdCjKNvTMu4WykGcmgqoTXlOoYRRaXqwd9OBbRzWIX--5VMrR4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Drake
📌
Ice Man
📌
Habibti
📌
Made Of Honour
📌
$
ome $exy $ongs 4 U
📌
For All The Dogs Scary Hours Edition
📌
For All The Dogs
📌
Her Loss
📌
Honestly Nevermind
📌
Certified Lover Boy
📌
Dark Lane Demo Tapes
📌
Care Package
📌
Scorpion
📌
More Life
📌
Views
📌
What A Time To Be Alive
📌
If You’re Reading This It’s Too Late
📌
Nothing Was The Same
📌
Nothing Was The Same (Deluxe)
📌
Take Care (Deluxe)
📌
Thank Me Later
📌
So Far Gone
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/77765" target="_blank">📅 13:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چخبر از توافق؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/77764" target="_blank">📅 12:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCr5IRmrBZVz3jceNAM_9A_2sKdtKz0LMkq3eRpxYmB1St1pJXEEqR8Kc_lO95YLqCyrk6WfE3Y_xqT8Vjc-XJ4ZCh714u6RhC1b0-ShLLrbL3zNq9RV3BqLBBTiV0cI3wFzm6k9H48D60QDi8w5-D_oxbNpKXxCJ5Lx6kEXgdz3u7kwktJgfpjHMssckRNPW1k-AicMi0uLAoL_g0ezybTTvIdvd-ju84oPk3FzslfV1h1BTGrZ8mWMmW8ZYMw0Np8xEkEMNQtH9VYQqnUkA38V2SmIRxa5vxMr3HHhL20G-M1-5lCxu9FaTwiPQSwnXvv9Y7FASKhmmGC_Y25zLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNEFBJdhVO9bgOm1jYs4U8GiOTMySLerilsZlD-KvCo8tyuQuzmVh6Ixp4qE4KbcutbiN-Y9yR48QIQi2u8vgMrVUuojr5jbykyDJAOK31KdqEaUuNKjw6l7OBcV834fSis8rw_g2Y32BqJmgDMNXMpAIQMLv7ON4mf6znodyU7cBY9KR4pFOyWUzVkTb2SrWo4X43wCRTty1IGk-6Pd-a9MNA5uflCF1hBabqL9d66J5fLHcXhgVZj3MRnpm_X2wrz0uXnfpY_rRJQWsGJKRIzelem4v7EO4xQKzatKP5tDG6pWTUYmNjGqhl4vrqit7p_MMt9RX5Yefa429AIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo8Q-gnsr3OX3k5vn6B3vo7Zo3NGeVAYCDBMrC0_pp4BdZG2_dqLQxxExanNr3m-3dLMRKCmkNbaPfDktCM4oLoKtl4XN0Qxg6Gh8L7GZMC-su2GUhP_ke3TegkA_4RTRdiDLGOHDA4pry_PPP2qzEQKNoDX1F2RUvyjwMDifkEsARVJ5LHK3qgOLOt2NYe7Dvs_s96tZlQdKHHQ5f7uaw14eE7YPaQl0fLcjBc4069HpIQI4RObFe50_8beuBLkPDVW__l8T9fn-B67e82MUVBmbQoQ5d8WXHMGTNyWsv5sf_aNcim8pKKUnApZs1lgkatzALdn5tYzLPDK6CJ2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r23
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه) کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)  هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiJreJl8gv12rht4c-3HzkQ6FjCQpSWPvwIwnn0508j6hOrPK61APagaScuLJB08X3ffKCxaOAkxrPiws418u9EXgt-74Slq_bZlhONdeaypWoTKsDofMn4P78q-dEvrVMDUwDLy65ppbbgIfrY6TG3UIAXM0yx13t5YN71vHz829_Ew2zdxaj0PygvPgfUXZf3-T44-0u6Lo6nCDSCVXJz6QLEKHSSXwcEbhFc0qXxs4Itsn5XLgCFndAxHNc-ALFy8N5sFMH18fYNnjxkRMFxZZ_-adYmNAUEbf3Kah5BckNOuUf2x1OJ495dZ1F7qK-IvaZiejKFzELfRAqFQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kin3-FC-Nf4nXHcUIhj_eK-tnsC0CHAoDy15DS3YYRDuq7hJc3ncSooEpLxwmV_mbke_Dv01Ag_bVyiRORYEVGXMCbAtPc1bb-CXn4Enit5O34RaRcah8IaXFOnGqucAnBcM4BZjvZ_ySfV0odXoJTBcEenUroNiWdqPMbimbCYo3GSBfOPjl1MajdG7_U605EOJtQ0e3npfeDjIFdzsj0qFvuXlFcES7h6yw_6mCxObZxiJlGuTulB-0SgDowtjIwsGUjdPgDjWScz7e7g5jHkHw0_f36vLpyn5DA3eHeAk3GvU034Gt506JCmxCmbMfd-hCi3YddeeJX7F4PGB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kin3-FC-Nf4nXHcUIhj_eK-tnsC0CHAoDy15DS3YYRDuq7hJc3ncSooEpLxwmV_mbke_Dv01Ag_bVyiRORYEVGXMCbAtPc1bb-CXn4Enit5O34RaRcah8IaXFOnGqucAnBcM4BZjvZ_ySfV0odXoJTBcEenUroNiWdqPMbimbCYo3GSBfOPjl1MajdG7_U605EOJtQ0e3npfeDjIFdzsj0qFvuXlFcES7h6yw_6mCxObZxiJlGuTulB-0SgDowtjIwsGUjdPgDjWScz7e7g5jHkHw0_f36vLpyn5DA3eHeAk3GvU034Gt506JCmxCmbMfd-hCi3YddeeJX7F4PGB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEof8CV8VqKxSyf5ZcBbUt1ApxgjuGpykvVSOyBBIH_OQH0TduLKC4i-bmtHcxYP4jiaTy_nFmXq8-DjUD8_wQuoLPxRPDj-MlW424JFGRZOnH_RPe7YZX2spTo4FP45k0eoVsdnfYVQkAR45x_kbU9cNpXl-EEfdN5e-JOwcrPLGbYu8YNAsXTysgAonP96dsYfvhKcaQpsrikDynv_hcviRflRAt6ubbDhGpirKnKtdGilQJNdIeCsUwqVyy3OMJTkDSXjZ40VqzIvCFi2L7tvV0rVMsemMEc2JXaoVRkH4vrdr0PooGtB3Hb_3X-75MKzJ8RtRQILkZHfaz2g2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
YËAT
📌
ADL
📌
Lifestyle
📌
2093
📌
AftërLyfe
📌
Lyfë
📌
2 Alivë (Gëëk pack
)
📌
2 Alivë
📌
Up 2 Më
📌
4L
📌
Alivë
📌
Wake Up Call
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7_wXZrkQfC0FpEncTDihoOxNKabNDYtX7zHjtaNn4Zeb3Vv1wP33DZrPYOsYhXatFEp5i4RGh-wyGSlRvDvRV-AO24_AUyBwJY9o2DYmfrzKtEkcKAl2QmuqjKl7Bcy2XcIiSmiHG9sJ5eDM6RuNWabZkaoer9Qey4npPV1oqvmIqYA5rTUhEGy4sqG6oBNiF3GQk_W99bPA6tHdNCJwRgBmDNCK8pv9gUq4b-nuFF4pfyKX8ieVDpeYtsdKjT1QjQ0CxYR7VvIE4qusUUXlF6_J_bL0qwZLAYCxITxhAdXqAaEKSeLP1WS4JLdS7tq5WTH4KrNpQ87Uvy71z437A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIK_0l96Msbuid1UXezdWdYBjWL23UUZxNNp_4tf_0lJ6ll5YFBm7Nf4P6aErf1cMedB_gy58W7q59IK9vjnwQ4bEo-0i7U2l_0-RzeXSqjX0yhTLokc_TmNGV5ax-rk30ShEqkHgVxF-bU3qHdlHB6zg8NZMT_bkj1kT_qxdNSa4XVdoFbSL9B43QsExn-kW5JSwDrurLJtMdVOCV5FuLRVQa73wKYVfy7PvYScK0WojTbCZIvC5HUZIyPFJnWN2VYQxzNzp2NKFXXV9myRztJBwpJC328oODvSg2OiAHQ6R5wk4fqyYMSWNixR5hr3CXUTTv8ZiIJ0NvoxBVLsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eecXN4Ik3YDdeH0QvFp5UsoewCaWW-EwBScx_WDnqkE07SDssIXJM8ZdiiNmlW45lmYL-D8HLScR9H3czbParbu7mJl17w1vPAqnjimf9_w0IYeI6TYXi1rmrv7blaGQRsBsqOs2Try6PRmxiaWUlEGPwcpty2WwPEk9oolqBOCqR3xKR2IgAXflOlwd6wWLXInGgR_cBXEm89ViHMDW1yB_Rsj-_svnFjMrXGjY1VJPZeUQTpIYJJrGuuH4FP2RqgfZJM11c-PGfyiNVY5CEmQPhmdQ6e8JAKOmyVwpq88WwuGdrnzphupPWyvMEkrzPtgvxJCyYyOsNomngRq5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP0dk96hRMa0_xgAMmOsRO6XxAZtt7zLY39LGdf_tlzMZ9tjr9_CodQT4Zqpj1a3gYZmli6kawTHFrYm5S3D_4niRLnNNqsIMKiXqeuiElwB6OrIPqwMaG-HnlscmNs5soaiQlgo29egvrVpifKoY1J_jqL23sSNu0-lezlmE7ecGLl4KUBP9M9xGY0_FQpWHYD__R9iM8986xxPTozvksEBs8L8HN3rywEQ4SAi0_Gn0siHMpKUFIadOmLbpRA9kBKzroY5jmxN9iJO8wyWL1YHQam9brLvDZomU7DIgRuR2R2WsAth9qB1IzRgI9WgBGk9_KRoDhwzVelHAgdlEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPC0-LnKMBQroAz2OatY8Z4avhxrEDNJoeHlML_2PgHkS8Tgf8cLR9IL4kW1Yx4UwdckxolG5Tr1Gk8cls-xFl1FpMnZ1-ga0rvmVvErUJnE5Ys80mhOz8gKTfOi6Z5fhk17L5BRRTHkj9meCRaUy-Ko8iRS4ELwYnrB234ODsAWrEKtOl5dmkJzEBoO7CKqLj2TUiVab0hF2qDJDZobH1hHCiT0DJVpg19W94glXenwiEYYh5VRB6wkZdceRkyZgmw5sPbhyZUFUl08mYVcq6VY_-ZsD8mmRpFQoEgD9qwDF--tgJJDSuv8ne2nIlLXzLpwxJVi0_g1JNNKyK16hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZH-RGta1QRLzlBKC-8RldzfTlaNMASP1oHs01QdGK_r6_bhS-z4nS69qLOKTWocxNS0CDVlYqbL2TtB_JdVf_f72QdqMtpZLZQLYAlHi8awNzO2CS8p2d0Y-0pX0i9IGLCsJkNPlVb0Sh7lK55VpRlFof7MC9CmAtIRTV-FqsMlKYEWwnw2I061shmFOv9AFc9ToWu6093P26E5iNcqp5NPe3zfcw38VUAxfL1vBtpBtTTIu25XEUyGkgJq4eVYI2iXXTYvNfYWii441xJ5qBA0jFVn__IIIeQzP-YTnpxOtcfpcbJiDjEks_2qXGiXfBqinB-t3M6XpwLPF7pVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itoskFi4rRZGfb52kEEygde-gd32dl8s4dI6kNFpjRy-I_UmRvvJNSsNeFmZR3_bsUGyD_GSP8LxYskStgLXChgHoC1VuOjJm7I-pIXve7wUXGqwJjhMSz7nPPMK7BIFeWBfMH6l73T8bojreXI_LAbOGFhUQAt0oaF9-HOLUBXslbUfmzK0iEZJq5L1dyN-cfgtqD0er3ECOEuKl5oYjwwW_0FnHeS8MOt7Sftp3njOwCmMDYcSwE2riZX-iwbe1kTRT1djxHA8MTPzb4WcBez1u71FvXgq-dVmKB7pv-iE3Xf5UqcTEU-nzz7-IAALHiiGaf6lhS5M_11b3-Sh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9mM0PC9vAZRVvBRi0pUsEBDGUPsbG6b7zxbbL9ineYWVkIUWQ1Vg1c4UwABWlBuhzNplDAzhGm3doUKi_P-FZxQdlPopAEWPZId6yn22dDeMhpHpAOKRkyV4lhQeV0eJXjH0O-m8QPZvTU3w8PlCk3Ki8Plzp-mVogyya2Or16FsMc3fQy3IXGcPx1sKb26RAU7rXvQrCFfG_eY5nADJe9aJwzn_pvH18icnSJ9mjo-vkqDuF6HCbneivEYxcT5F5nG07WOxHfAHH2dTlvJrhE0LTjhWle8d7ETk9Ugw_9NeJ-KC2cUWvWHxVohTtRSKJvuYU91VvCBAWA6R1PmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کره جنوبی هم خوبه ها، حالا در حد تیم ژنرال نه ولی خوبه
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77724" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM23n9LdEcVfFXGhpvD9UtHSPZYOWPgxx5v2JlZQKOJLsQet5_RXIuLlwBVdAVVe8wGtwypGScOYBu6HPN778vd7go02jFqHeO663SYE-gkB1dR2Z0KnV9K2Q5LMvks3NYyNeSSvOjCw2lhbbJknmDtMASMP2XhiBAAdtX2UnTVrt-FUvU6-Jak8lR2xWh6Ph35ZqngXhDylKdK6h5yqmMWjDmRuB7g04I83s4spWo1KkdNomtdG941_6DHnl6yEZANn048JFH9E7YO9VDdW3e4W-opk5ebkyEY5rvVo7skiXKYPA7D8vwlvzRsXmoigm_-G5KDGaSeMPGQvB6rHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو روزی که همه ویژه برنامه جام‌جهانی رو با رامبد و دیبالا و... شروع کردن ابوطالب رفته «علی پروین، مادرقحبهههه برو دیگه» رو دعوت کرده باهاش برنامه ساخته.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77723" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77722" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS9HrL10cHaKGNWAEM4Mgco_BbyEq30O54Y-ZGaunSgv8wqIgX9EnF5Je0YZnKch_ZTvoRl8OUfj5uagrbC6HYo3keFA3Oa23AMdN_Ooz6boS85Wxf8NtLJ-vfUfjCU43Xx1QASE5vmAMhVzuwdKRBm3aDnUfxVAcMmk4QXtgGgfp9uv7B2unPK2KSQ3sJ1w64xgbpRFcoIXm1KGzmrBoU9hShv0HrzbfoGuiziieyKQTkBPslqnd9x2f1kcX82iwvKxofM9PdNiQt7hm7uUZhJejtorv24atS9vf3mfRSfRlt7DOSrqY_WY1tfbV78w978NafIkOpBKBgONUz3XHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g22
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77721" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز دیروز: لشکر 82 هوابرد آمریکا خارک را تصرف خواهد کرد.
رویترز امروز: جی‌دی ونس و مم‌باقر قالیباف توافق امضا میکنند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77720" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فاکس نیوز درمورد مفاد توافق احتمالی:
مواد هسته‌ای ایران نابود و خارج خواهد شد، برنامه هسته‌ای آن متلاشی می‌شود و هیچ پولی آزاد نخواهد شد تا زمانی که تعهدات خود را انجام دهد.
یک مقام کاخ سفید گفت که تنگه هرمز به طور کامل باز خواهد شد و ایران موافقت خواهد کرد که از حمایت «گروه‌های تروریستی» دست بردارد. (دقیقا کی موافقت خواهد کرد آخه حرامز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77719" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=iWS5X7J20UPZY2FYMjodaPavwihMqb9iO--BX6bS8JtsnbJxTOvk-I6rspsYyFMxc0X8KOleyTBw58K5kA9Mv_azFrGVRpgorRmcYMr7hS_UwCqI-RbYGhFIPjo0vL--8IZ_010CzgAayQZQ44hLh5g_WTQL38yH7dAl7a0mXWWOqRZEdTvAMvP248F43l6cjzIYkS2x-n9RGNGJmPEQTpaJOLbMOlENCJLUw8vuVSCEqF2nVRLvAHBTTUF5b4Ifyu4_qI-h-rWI6k_1Z3Jk1d4D0oOm9oIUAO_U1JhWiDGjyQmmCHW4I0Vy-kTP7bj217XULy46918Zecqd6Hj5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=iWS5X7J20UPZY2FYMjodaPavwihMqb9iO--BX6bS8JtsnbJxTOvk-I6rspsYyFMxc0X8KOleyTBw58K5kA9Mv_azFrGVRpgorRmcYMr7hS_UwCqI-RbYGhFIPjo0vL--8IZ_010CzgAayQZQ44hLh5g_WTQL38yH7dAl7a0mXWWOqRZEdTvAMvP248F43l6cjzIYkS2x-n9RGNGJmPEQTpaJOLbMOlENCJLUw8vuVSCEqF2nVRLvAHBTTUF5b4Ifyu4_qI-h-rWI6k_1Z3Jk1d4D0oOm9oIUAO_U1JhWiDGjyQmmCHW4I0Vy-kTP7bj217XULy46918Zecqd6Hj5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ یهو ریج بیت مودش فعال شد گرفت رو مذاکرات و رسانه‌های ایرانی:
شرایطی که ایران به اخبار جعلی فاش کرده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده بود ندارد.
آنچه گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره داشتن یک توافق، هیچ ربطی به حقیقت ندارد.
افرادی بسیار بی‌شرف برای معامله کردن.
با آنها، چیزی به نام معامله با حسن نیت وجود ندارد.
شگفت‌انگیز! همچنین، حمله پهپادی کاملاً دفع شده آنها دیشب علیه کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
بهتر است هر چه سریع‌تر خودشان را جمع و جور کنند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77717" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMilpEckVJ2HAbdgOqnWyyxt_f4HvK2EaW4aQ3e4dFGq9Rsdx2y2zUHIXwem2sWwKSudYeMG79Vr5G_v5y56WSIP9g_Sn8Ao1kSbdnsbw6EhWHpEX4YGrF2YxDgNddwcCo7GB4BWPPV-0lzxm-tVuw83Dvy-SEPyvKGWcww8DDSARA9VCyBLa9Ez4PLLmkoXaRAKYJ40R2O7nW8X_hBUDWWRqRg3viuOuqKIWmCz7OvNWcNBYWNAWuzsmTrjSIm3AatxJLiLdeJtu5xqlz5oHjU68BPp7slr4gsD-PVyv38NKnsEFi2qJ221YCwaSaLYfPBlaggVRiQK7lPaUPqicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ارباب سعی میکنیم درست بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77716" target="_blank">📅 16:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77714" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من تازه فهمیدم چرا علیرضا منصوریان کچل بود، خواهراش کنده بودنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77713" target="_blank">📅 15:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkiPIFr8O650kXcfIbRwbo_ZyzC45khaqAPVrFFUaMPcO9dkoQYanW-F3oMAL_YRdZnOW5M9lL-gwRv0pnA8dl7HHqwLOocPtj1BmVVx-jhuRwLheNvCHoSTF9ILVqRp2Eba0PgfMdSRG3sPLIKJC8h8CySniw-3AoZFnP2mHOlqoxWqbSWX8BS7__q4PCdnEr0tq2eWgD71JgWY0a9myrcEfQD3kb2wzyuii8XoA4vw4yUQ0sLNGvze01525vG-CVkTNy2-CRTeW4tz5kN74mKB1aTHAocZFy0WIIJShdOB9IHUfkfkz2IhpT52wVhfnoug-8Oqi1nRVsuXinNGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77712" target="_blank">📅 15:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=SLwwEtrPsp41uEC9EsfkHdyfkFGd-LPnZ_bcW2m2S8S8Y46NuAJ4EAIYBPg8oPNqhF1jm4k9G0tyyrv0eoJk1kQU7aWr6tkO0CnfMlDLTqQmTfvmbdRKR_gM9AxCCDIDRBcugVc4SKXkCjhLYpXea2eWHd4-xyi4kQPLGdyoWau4toeF7tVcQZxtNzgG8_qhr2Ww3q7qvd6CeUEfgNX5MPD71LzGTdxQ7a7p0saDSkbiKzmM_DErEBFPwsj3ySHoCPyQok3QfZgZA_mkCq9eIz-fqGVEEnQ0jZ9zQeBVdqeMuZM0Pj8l03dms710SGFksLgDYFFy4PaTNeM1HTBSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=SLwwEtrPsp41uEC9EsfkHdyfkFGd-LPnZ_bcW2m2S8S8Y46NuAJ4EAIYBPg8oPNqhF1jm4k9G0tyyrv0eoJk1kQU7aWr6tkO0CnfMlDLTqQmTfvmbdRKR_gM9AxCCDIDRBcugVc4SKXkCjhLYpXea2eWHd4-xyi4kQPLGdyoWau4toeF7tVcQZxtNzgG8_qhr2Ww3q7qvd6CeUEfgNX5MPD71LzGTdxQ7a7p0saDSkbiKzmM_DErEBFPwsj3ySHoCPyQok3QfZgZA_mkCq9eIz-fqGVEEnQ0jZ9zQeBVdqeMuZM0Pj8l03dms710SGFksLgDYFFy4PaTNeM1HTBSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توهین بسیار زشت صهیونیست‌ها به رهبر معظم انقلاب.
🔹
صهیونیست‌های ساکن سرزمین‌های اشغالی که فهمیده‌اند کار جز کودک‌کشی بلد نیستند، اینبار در اقدامی توهین‌آمیز یک مقوا با سیمای زیبای آیت الله سید مجتبی خامنه‌ای به همراه رنگ‌های مختلف را در رژه روز همجنس‌گرایان نمایش دادند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77711" target="_blank">📅 15:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU7-Xcrs8oyps1sg1kuY5H0ZK4CVfvjOpNWIWmWRas5IsE_Mr2aiQZJFJnJRO21uBP7RopZYOmjy9GeuZYssAFplIbt54O0LE3fbpGFz9NCx3Uvm3oh-taab1a3R9-x_VPbZfCb1Yo8DkMgVLsbPBJ2rEFGjUAb61LdKb_f64gVFZQ1Kezs0XfqvhL_KH-CKBKo4Txah9l7LxSvXas1xSxqV05Rjf2imK-DKF2ocCDmgNfHYy1URJxBH74HoWTsvYoHP4JLSF-0NdgW3z8fr0GTq4EeuNOMQjz1DnOJHddLeMPpgwrJgDpRTmqNhyneXjyIIu40Uqsjje3i9z_skBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رشید_مظاهری
را فراموش نکنیم
رشید مظاهری دروازه‌بان سابق استقلال و تیم ملی پس از حمایت از مردم بازداشت شده و ازش هنوز هم خبری نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77709" target="_blank">📅 14:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh8sogIXOS6DkBXlzBgAGKupWRhzthfMC0xMOZQqNGBWs1QPyYg3q7WlwGSXGdL8oUs2fJ57gIF9n1s-r9tSkxDzrm76LCGTafecx3HkZK2sNJ9pBia6yjPXWtsmfD5pwp50I2W44KQKYInPR7PSETAfh30gId2rOucLWoyIDq0lB2uznq8ZhS2H45EKoL5gRLxFvX55RYIDMruSNfzSEXsRUTGd2VMFIwYQ0sQDVAUqlKyPY2W04-1Y4GXwKIBzi8aQStnc6ZTpHT7EPpf6XffH126G1btswSLH9CCnSfQZ3qm4iA-4OcU2Btjiw_rko0TjtHUgNPq-8mIw5qSWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77708" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF9jex486oxQ4vQiu_rlweWEsTNCrK14fT2lVixi1WvI5tIYDhlyxw-A13WBufcm9U2hLYX9cJYd-O2tQ6_5WF7om9prlmxD88pF580kFHoK1ukc73aPvD6UArau5w0u_nVIkZsJ5uB8L2540LCwkEzQvlViiiBVfCgEx-Ua0T7c4hlXYI7uL5ixE1ltyVUn3n7VCh-LH0IDfOd6oB6aQS8lLaCoIFsAmHyAdc45u4-eI_evL9WUzY5sCbr15hYe3y5UCLlKjWl9q7dhUUNsy47vBJDeFwfXeNEuRn8kLkB9y-bQKExjrSVBFu73U90VlXd5Xiv0jwt7UDSmNQWapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیسو
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77707" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد: ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77699" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد:
ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی که منجر به لغو حملات آمریکا به ایران شد.
تنگه هرمز پس از امضا به طور کامل بدون محدودیت یا عوارض باز خواهد شد.
هر دو طرف متعهد می‌شوند که در این ۶۰ روز علیه یکدیگر یا هر کشور منطقه‌ای دیگر اقدام نظامی نکنند.
این پیشرفت در مذاکرات پس از تمایل آمریکا به آزادسازی ۱۲ تا ۱۵ میلیارد دلار تحت نظارت قطر
برای خرید وسایل بشردوستانه
ناشی شده است.
یک مقام ارشد آمریکایی گفت هدف استراتژیک تغییر رژیم «فعلاً» کنار گذاشته نشده است.
انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.
بند آتش‌بس لبنان همچنان باز است: آمریکا مایل است به اسرائیل اجازه دهد به تهدیدات نوظهور پاسخ دهد، در حالی که ایران خواستار آتش‌بس کامل است.
مذاکرات آینده ظرف دو هفته (مطالبه آمریکا) یا ۶۰ روز (مطالبه ایران) به محدودیت‌های موشکی، حمایت ایران از نیابتی‌ها، خروج آمریکا از خلیج و تضمین‌های بین‌المللی خواهد پرداخت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77698" target="_blank">📅 13:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فوری
پیت هگست 44 تا پرس سینه رفت و ویدیو شو منتشر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77697" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل بمباران جنوب لبنانو از سر گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77696" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORwzPM0KLYLs58Pu13slJ8Tr_L_lhRGoDcyG9SsrfILWUCCUvYBXkXzFaBNHwNYXGKzg6N_wB7UKFYGCzCKwoTGkNjeKikajoGkmVdNmx8okkTz1R3PcIlSu9d6EllV_SSOqTavRZf0xDQXRoxTcAKQgJhvq9cNj0oojISgUjMjvnPddGJjXOno4JYIXFQkqAoDmdArcRthcgFqql2nFyHOHELi7hH0Wqr0_uFoVEsG92pozM4bva5kZLH2Oj5CIXriGS3FiZFK0anBWNv89FrvEEUGQXFA7w4JAQrPMz43En_IWlBnw3vQd6gbvk49WiAx6bk0bSi5bKPXR0L57WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش اسلامی سال 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77695" target="_blank">📅 12:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77694" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRu8rB67zf9XJC12Ut5dxndaEkMcgYx4ALXPx4RR21o5mUYgAPHdfimbKCbth6lunyXDMsCB3BAJqzCWZDRzQn7WHfgFtS_bPvJ2VplcijU6fS5g3X3W63CAKXBiu687qjc__6a-iZOgugwpGc4-EFgxCclVoTC9grkAXFEApmkSDvh82D-_9tHPxBxEsjqf0GPC2F9gbZFh4zy3f1EjdzI7RzSSGe0Dmbl6ZZxHkroiy3wYiBiCvMNjKrYylTrCxvFHTNW2FZM6ZrHbBItsG4pxHloTliaZo9shl19fOg9bOAH48CQfpuNvKoy2a8srgyQ8sPa7SU5rfeEcGx8BFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77693" target="_blank">📅 12:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGMdnz-J4osC-imOHrhsXHQkGBHPj16yVJknvRhfppjz3Z3Q2jD3fdP2HjyTF0K6UPKyDQ8CQgRpp1AXMrnaPfrZ97tO-sOKnOdjpJ6pnhWsDu5DoqnoySxXQHfmjzpO2iTpQ5eo8TcGZJMt1faLNcOMVkb154xqwXXQmN-77Y1mQdJbIzLcVDDkk49hqGoENYyvO9OklbBNVA_6txcW897Y4_bFaSIOJNxs3LswVifQIIvIgBtz-mdo5lJKKUA1K9MRzdCqHJdOT9eeaqF6lxuJd8UqyGaHL1oQf8752ZUiY9qcSpZYxV8GuJUJ6SfpeOibesp_yZoD4B-n-cuRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهران منصوریان ساعت 11:08 صبح رو بهت بخیر میگن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77691" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrB6ekPaAsVPEbanS_xpEXU7EWoG39gT-X81PRLxqzIWF4hznBk2Uv5qdb2ZAnYxeIH-5KPYurFK7IXJkdlGPVl0PuAxj4mk43m5st7AVDkoAjQDWppoAJBN8A-UU0Q27j5jIsaSOf7aJlf5WYaY-DXgltWN3tFqSEmWBTrDb1Hs8hVh1kpmXsWgaR8XbBYBCkZt_3UIm86es6QdagtkXNUY9k4Cxy1hFWmmRFzJv8VVNDFXi0SP8MusWf0CwG3MOIb8IWa3fmdCHIr_OHwM-QOag0mjaAQPthBsaefLc_N7JijBLzgJY3xPS26dwQxKJNNm1uZPYK87Uk4Lqfiprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام‌جهانی
❌
فیلم سوپر BBC
✅
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77690" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77689" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaZhR8sQ_RvT35Rk-dHxw5ha-QrX2B1akO-47MI6UK7TurIPE5RoLFrQGIFk24cvir1asgUKSHSL2e_K_Y26dxdSSbymA5QJc0Sc_Kq7Txh8baAfiNEVGQ7xPUPFscUYWqyz1NvNP25QskffhOpdpTDcPwd9bV7KhkEknBLIVAO5vSqkFnElGe04mt4CXM2z1y_8KPMSQSwQzl26c_6AS4fQhcFp_5ihj2OoX34oYNuebc1eYcvgN2SFKiNDt8k4QmdxpbpNLXL3xyHeSKjai_0deSDlZCkmzrh1BYh4p8IgfVJSssbFlbZnQcqnO81QFtp22b1TH9bIlk0hSL_BBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r22
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77688" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهکار جدید جواد خیابانی:
خلیج فارس خاک ماست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77687" target="_blank">📅 10:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=XgXOiHuqlSShVXX6HmgYqWWv7NN-HBymmcsYlWyupS74WfQqZo6cGokIIukAelRMMhyjHgue-SZ0OLWuMW3VUyusdXJ8AHE4JT0ip2uE67pGPVdXQdfnpxaTRV1OA7x4W_0XlgcDVQ7BPfGpHjYmvXZy1BsBu5qH6uTdjl2k3BCSFYg6rH5sYJzxnrjN4K_saH6tWl2-OrenrBYHGMr-m-AqQOqgFH_eM3zXKJxD5YFMH_Axn-8xJvuvR4ZuHTmXdlxIPl1uMFmBP90aQ1h4Vf59Xi1bh10M3yT5rcNNReEXiSHEb7ImBZwPefe97WQSTLwrMGaRzk3k93pfHpL52g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=XgXOiHuqlSShVXX6HmgYqWWv7NN-HBymmcsYlWyupS74WfQqZo6cGokIIukAelRMMhyjHgue-SZ0OLWuMW3VUyusdXJ8AHE4JT0ip2uE67pGPVdXQdfnpxaTRV1OA7x4W_0XlgcDVQ7BPfGpHjYmvXZy1BsBu5qH6uTdjl2k3BCSFYg6rH5sYJzxnrjN4K_saH6tWl2-OrenrBYHGMr-m-AqQOqgFH_eM3zXKJxD5YFMH_Axn-8xJvuvR4ZuHTmXdlxIPl1uMFmBP90aQ1h4Vf59Xi1bh10M3yT5rcNNReEXiSHEb7ImBZwPefe97WQSTLwrMGaRzk3k93pfHpL52g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77686" target="_blank">📅 09:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=PBmSpKa-Q_35oVebpyCzC2X1m26K0rWdvTjUuWrffHa56ih39gYyll8_T8iojXFzt_4tpZo1bvpbrc9g9LaiW7AF0Pdjij2hr0lJe1IurGN5bijgPWxTqEvPAKI2u9c67TEEw9195wkvKSTyIHuAHEVaaN-ZPG0JPMnNRucJ8wrbUdI8CggOtrEjsvP8Z_sgWJjBZt9aINcVdVi9pvv2RMGLI9--ylRgeEI8nch99Vb9szXL8Q-1XhLa3zyViUd7zLXeHgGARi1c1uGcmzh3WcZsJSprGYtbflo_BsuH8Ss7_vgRfe-qA_NYN5ZHNZgDe0glTTh_5eqocUp3FVpPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=PBmSpKa-Q_35oVebpyCzC2X1m26K0rWdvTjUuWrffHa56ih39gYyll8_T8iojXFzt_4tpZo1bvpbrc9g9LaiW7AF0Pdjij2hr0lJe1IurGN5bijgPWxTqEvPAKI2u9c67TEEw9195wkvKSTyIHuAHEVaaN-ZPG0JPMnNRucJ8wrbUdI8CggOtrEjsvP8Z_sgWJjBZt9aINcVdVi9pvv2RMGLI9--ylRgeEI8nch99Vb9szXL8Q-1XhLa3zyViUd7zLXeHgGARi1c1uGcmzh3WcZsJSprGYtbflo_BsuH8Ss7_vgRfe-qA_NYN5ZHNZgDe0glTTh_5eqocUp3FVpPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که سلاح هسته‌ای نداشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77685" target="_blank">📅 07:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMNKk8j4EFROippc1LrivpDixI-2pTUAcoKGxBef-mBhso-2H2SdwhPKo3nxWL2LZML7PtfA5iw2oLFSm1tXdtdxMum4AN5mq5RLdWP9nkfXeOOfwU3gAv4u4JdADuh_SgmDfK6FA7hZXcKf2vMfgz9JMCFWDZc2VJMw2D3ogZcs8XqxCj2Rp0ezdQKZBJf7r3cNpAnMK2Rok04fn7aBIUbUBQEJ7T_w0Ig1gbdjnBFwl-Z_mjCWIUiTC9gFX9ITuaV4X5HbobOzcOc-lPJkvad9qgTDKS6lsPg2et6CmPo83MAw2VqCz8HHe47vA3fehtgOs3AT1ukRqXePVbkP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمنا می‌کنم هر کجای این کشور نابغه پرور که هستید همین الان متوقف شید و سعی کنید یه مدت تحلیل و تفکر و کلا اینجور چیزا رو بذارید کنار ممنون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77684" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه کودن زاده‌ای هم نیم ساعت پیش اینارو گفته بود ولی از شدت کصشعر دلم نیومده بود بذارم:
ما امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود.
این ۹۵٪ از هدف ما بود. و، آنها این کار را به قدرتمندترین شکل ممکن انجام داده‌اند.
ما، آه، با ایران توافق کردیم.
معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
اه، نیروهای ما خیلی زود شروع به بازگشت خواهند کرد.
تقریباً، اه، تقریباً کامل شده است.
ما هر چیزی که می‌خواستیم را گرفتیم. نکته بزرگ این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت.
آنها بندی داشتند که توسعه نخواهند داد. من گفتم، «خرید چطور؟» آنها گفتند، «خب، ما آن را پوشش ندادیم.» پس دو روز بعد آنها با آن هم موافقت کردند.
ما هر چیزی که می‌خواستیم را گرفتیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77683" target="_blank">📅 03:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عرازشه ای که میگید آمریکا نباید فوتبال و سیاست رو باهم قاطی کنه پس میشه بگید دقیقا سردار آزمون چرا دعوت نشد؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77682" target="_blank">📅 02:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2R-BmZ40uS6K_Xi5x4Xnf_8x34r3gEV4ltv2GnH_lpqC4c7Ih_IOKmSJ04fMYACI5CE0pOE6FWS_SGCJcAtAckmRaZqXmsQq67uveJIn-x_vhh2l7J5DZpHt4FmvaWnEHU5_E9vwRlLf9bqA-_Vjz6EVohAjjNaD34fK5fdgK_88y_EUyt-R13_UrU4_K7EcgZy31cuxTfKfO6n1VPZ9wK2sQRK1lWc1W6B-YeR8_FI5BFnCqxIv14VJ_yt1qAK7nhjb-oHCWVyZN2yHye2zdQ8gG3WXnG1Z7xmowM5wBeto9DP6PjkE_r5DIWK3duD9RlggyEQZVE5-4kS8Zy-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ترور بیکینی باتم اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/77681" target="_blank">📅 01:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">میناب انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77680" target="_blank">📅 01:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تسنیم: متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77679" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چه علاقه‌ای به گوز داری مشتی</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77678" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بازم گوز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77677" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77676" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S260TOWbSGvncZk3gQIkueBbuL4TY-l0hz8-zDEeBwM1AUqomHhunoxkkuVvP8eUHfeR5q_olBlHSuzJrerrEeux-j6hH8lTI5FyrtcOXMAUgZUIh7EL38WlYF46KegU0gVZA-o5A4hZAroRs_9-L_vYSg4rzjQwvidVEfNYMWhRUNasA0EX2Y7RxEEnEt6cfI87HqzJ_tNWLGLYw5FNZIes2hwtxuiUc2pXiCqghXtc5deNBE6pJyOzW9Qjue5L8_pZWtchTCPqFGoi-AIiIFG19KxbluSi2q4bT9ujedmCaYs9434g_5BTnjZVKo_2f6l8jAk5RRwDQb8KMmvgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اواکس هم داره فعالیت میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77675" target="_blank">📅 01:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پرواز سنگین جنگنده های آمریکایی برفراز عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77674" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گناوه صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77673" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">درگیری ارتش امریکا و سپاه در خلیج فارس
تایید نشده هنوز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77672" target="_blank">📅 00:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سلام فریب جان هم اکنون صدای توافق از خونه همسایه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77671" target="_blank">📅 00:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77670" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77669" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaaIZneZIrdtdLguXs_t0gwji7JRUGwqPaAiiGEOSoOOKlW5_MRh92PaYo9GYxBu2fWgCH_FLxLfY_3lZZRT-2bx2B4e408aZNnfuFKg-i7xHsHa_Bq46Dyr33p7xa62LKM6NpSm7tbjA0-3eux9-Z4-qDIaG6vWeDshr-1KD07CQHNVm-e1Wr6bz1ocOxyu4tFYfsrx6yjyVLM0aOosaElCVH4_ewwP-0ivt5MUWFuy5CV1d63I2WGCmS5LI0zPA1h45YLlvMEDgHBmOqofRKQTaCMEHWfj9Am_Z3VaE65704yYgSkYpyg9PjrphNnuVQsqVILqkmj2oRJCCusi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
