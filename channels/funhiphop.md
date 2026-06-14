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
<img src="https://cdn4.telesco.pe/file/fiUtkfufKVOKcdNwJMsdSaiB0cUDSvUdrM8aoWmrB03xOR3HJXFTHCOQfR570KL518j_ZiB6T7GtfHZuv_3aAwgkhIFvYqgyvsFHtYBFv3fvTwUWzfaUZUrxFwXWWeSsB4AQX0lUSTzrlX-e3D8_itnokSjTa4rRvzBSMoaySVbNS7A3bwMw_VsR7PrEuKT9rCoi1A-4p3pbf40I3ws_0kKlkA4As4vZLJckj_uHus7ws09HKu1yzS8SSSwlSxg8scS6CH_sE-g7yJ4g8oynmHZzDDaQadj6_H1sfXGdRNPxEHc_5MArJP1Byojiuw-K_P6b_GF0eYzPXS1ixz61zw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OjnTjKCPNr_ZDFlEaAzAcoHXuarndP-Uk5hU1hdJ94szFF4jSecqczRwKlQVxsYZjVC51vxpKBdiSVhzFzARV_Odpg9N9IHGzxOsLN2alDzeli_aUIc7hsgaHpIVq6IK66Poy8LqNGp0Sg-G_z6JtFGFTLnXMvOQfdR4nXtaAAsjrA3UkQ_MAztwgaLiU5Qz5I6UIOsie3UQ3N6LljjVhzPXzh4S99UDmFTVIYvaXQWp77Do5i7DaLdo1w6lzSw3AHOSuMsfJ6jRbmfN3KCGOZgeXmHhhN9y_HTw6hk_HQVf2IGG_jwWWkFp29ogJ8rPl9CF-PIjJsLEhlQOXqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZKC20AqQrs4QEOcU0HmDtJfCQLnxsT7WmBQuCRjJM68t6TAHiGnR_obi-VqtDtsRyXfrrOT_ELQxKtBBCcSOvUiEam2YOvGQjcQTBKTk6Phi3qkN047mjmq-7z0JKZkeOeUktatdvWEAMNTE-aVXVcy_wytd92SXtGI2jIF3JDApH-SjAC21TpmxkEzc_m_jyKTTmI4aJVpM4EzbcC41FBJ744J4u5AJ4FrVie_QHLt6Ka54ZqYxXIA5DIEQIDsWALYGXlPwwCA5botPPPKQnF9Xe-eM-Wkzb6J3-YTQyR79YNLeJIVFhEXKMMCPKcPp_d6NbxJ1mJA12gdO4TxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-DWhHBMynzlMn5RF2jkTu_VPlGyVFxnwsf8elUaahpUXVpna7gXfVQb74QjjxxYNLDCJ5bIgb_tHAkBNkaHN4csIX1zqf7neVVGd8aMe_BaDlHMLkU_F-QcMUggaLQqciEcD8kzoy-cHgJx5h-JvvgqXtDLTG5gMIhk4qU_AS6wU--toWeGed2IEGjRr5vAsNukZkeO-1HbkgvidEpkJZshBa_eDj0Iu2ipIkbqttVA1RwZ0rVu1ntq1L4i1nQbiFWR_t_tLdnMYZu4K67Q1TH6iGzqprDeNsCmzfTnR4-Pg2_3av2SecjKLCPKY6nuXz6z6j9UUXxoSikzzedVpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMrTP2qEkxdzuTGsNkAiDXQ-sDvF_Ybrp9yclRccN10aG7HH74A-krCnHSqwQ9RiqUd-gMHaTX5U3Jaf2VgpKvgLokHfoYdJoDlS9YKgYEaEOlQNlw4me0I9Lk3IY3ylMQ3XooxGWFV2rnU7vuInZ5ObiKsS5t39FKsZUucyGJEPPWmh9B7LgnmpJ9hHpVcEsSAxhYsDJ7VkNZK46INMb62QF0Hot4aqsOxH87VxthxqerkM1g8t4DQoRbGj-nWf8gmpdvS_luGEe7O__CSjzj8LwYxKCaXXh-vIU2B93lwfi3zvJrw_W330-d-ugfoPc79iDPQqUc5MMXRWfuu-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9XH3Y1aapypLTyNRPTet_YFzo7zqgWDKWfQb32AFPzjRaNChpiH2T6tOtV8EnTQaqKXL5N80I4FXg0t7LgP1SmDPrfo4U1Lf-bbTcuvURwKQMKOATlDm34cNmentOT11WCPhoy3xVZ8Xiw5LgVpbfBybJq12kAij1jMelf-akBQ8HzmuP785rczSGYFoc8X4CjKkZjVFJsqOdCfl3rI4gZ3ktcmy2G_SipXuXm1__yeSglPEilK2XibBdRq8HkpYrUn75Xt5Oj40oRxNX9Mbprd58hNecclFUkbCMtMSrer54aQvAkWxm-zkUWYA88XsMHaDZxGIEWMZkesZ-LHNA.jpg" alt="photo" loading="lazy"/></div>
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
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtnc0v7z6KQCPpolQlOqXYuH6fH3eilu6w2-3qhfR5jrOL9fP3A4TntROoXPBKJEwa1vvaG8Rz0h5AniiM8c_8mGEgKnejhFpv6hfi7C5QxuMlAt63aGJCplXRRxOYfyzFFN5K6Z2LZ3g3bQhW5xEOlSVBYPO6S1fIWCSsPen91IMNxYYDvTM3Osvk_eHFKFWLMn4MNrOwDur3pORoMH2IKgPUqtPhytJZGuk-11cJ4RIz8Nk22M-Gr5b-uKiuBHVwFSXQP_wrlPhMjZoPIUMTQnO-nH7Xp5tGGnWQOYC_WEo1cl4oPJ0-wTcrLbSidc9z7V7ZLLUYIifrb_rleRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJeSGPoOpGpiiyvamsfMXtoPwKm9_idHFdo9l2hreMTl6rjZZZvoJFQcRv9901ckc5TVvDtz40J8khA96fjk5DbfHnu5FxDwpOSB5Ahvr12rdTNSj4kGD07mcZ3ghJTnQHdNErnqHfnTcDuDhVBjqal4ZNQdywnvLn0A41rMjlv-MtD4b_gj6xGpQX58v-yxHXfO6dfsaffPMe_htsjsChc2y1CMp4uopdmAlEnThXBx77_D-3Ndj7ZgtUgPBnuZzSs2F5OKrw1PetDpcSltX1q6iKC62Qu6UXKLMzR9ujijKain5v7i5xtWvf4bim7jwsOkrr1dmHJxcw1lPI3oOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml0DT7gxOFnSfKxi-G0HuGnmTQq8rOqDwq_RSqCsY4JcW_-7XtOUTYWFlMHvd1-VBl4fUJS6BIdpAM7bQd2l2d754zvV2-rRFrL6E9n2Od3u_9io0bhKFL-xsbGlnKDKZmmoqVRUiyFq53kzjqToahAxLkuDL868BwHEVm6Kj-JwrkHXPMnYy5q5IC5cxkhYdfoFoBLrzB9uvunxatVurkvJGIINWDTSOv1wcYBQF5g3u3jQyHoSLcBMIkhBPKNPeV6yO3VxINCV2-6ZNLwI9LHnICkmdsX4U0EesiPqRHMf4c8A4Et8XummI0MDXFGQ-TAJoQksga3KL3_4Z_6vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تا باقر کفن نشود
این وطن وطن نشود
مرگ بر سه لاشی
قالی مسعود عراقچی
این توافق خونیه
باقر خودش کونیه
خایه بخور با سینی
عباس بچه قینی
خون رهبر می‌جوشه
عباس وطن فروشه
آقا فکر شهادت
باقر فکر سیاست
عراقچی کن اعتراف
کص ننت قالیباف
اوضاع شده بگایی
کص ننت بقایی
از دیگر شعار های بسیجیان اغتشاشگر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77812" target="_blank">📅 00:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هم اکنون شعار اغتشاشگران مخالف توافق:
تنگه بازه برا چی؟
کص ننت عراقچی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77810" target="_blank">📅 00:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LkFGJREW8x4uAu3toQ600jBRLMO99F6wUZ74Vu93-UaNHp0tkL9fINsnoB3ugWQAE1KfcTVGCvdXJB0IC-HFawxEgHy3dZZADkFkb8fzqLFgb0D04ifxCmiPZZ88ZInXSqy_1CzF_X__f0GLMJz5Z1juRoZ4l34WsLRTCxx1yjCbE1cKTVyYYgqsqv-jQG0W1qcyVaIwUWlvS7FBIlZn9tV4TkR4TcKKCwYS6UbmQdOyaektO4xIKRPTtJ8_EO4Op3-jGKMIz9GZqM0GW85AcYkiyuAufAqWNAFLRuKGgGehSxyeRABTQGqr04MPbb4QfTvNfklDlAoYyktYqI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqglqCGALIYYZkqdBbGmeZFXW-snSqrP96g1Kb1uxHj0Zt3Y9XsxkyFgG5xdogwJcZxpAu2BEvNcLiO621UpiBa13l2ydyrvzB1pZTPPtcazGW3QID2RHN4ZcR7_H6zdILJlrNDHmjIwJlSoG0mnHHreu0OVw20qUYoFavuEl9O6-R_mfSRJlLhx4Q-wjWZdWV8_UgCAm6PaojoFAymJEWzwvdmvR3vgwawSX3YKgmLeYiO7kKmyGsOs6oYRNAz6rSzA3SngJKcYVCmZJK-iW7_H4zloZ10jgPi6-ceAxiQu-EGIFdqxJhXAKEF6LUsyFAyl2SfeKxzfxNTHMjqezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz0VEGNcWvXoqNKjY8dw4LPQ4aGcOCXg3q4AeAoGpLoOeKOn-XzfWNwIhFITG7kxPUIBSAPsgv9m6QkLb_uI3End7Lf5Ge78uK2SCN7yV92CLheReNhbqUfesI7Ypba22SjL07UrtOST0KCN2dYYahYl6UYecahA5lxGewfOEikvBQwYMynRdr9IBvpiLN-p3YHPqrY2YmlcP5fez7tXFvhPiaYLx9prU87SoKY-J-SJLB_U3mBvsg7RpCNyXIpAro9hNHCN2QmaxcziUHXiirmqbQawy0mdBWmsiCn5qtM3rf5mT3fMWaA9HQB3AWTuuA4auAvvRuCC8ZBucNYOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=NMysA4mepKtB6I3ytvNvUlG05HyDnvzhIe9z59Uls5iTCKKkRIoBNmvpVXbrrLXE4sIgPFdByRDuP_KunaDwOhMvFKYI3OndYQnQp3RHqDJAyScyx0NBtHWOj7MyZasf0bAZfe4ztWypgThWELkLQSH85pz7Q5LopTifMVWF8ThGLS3BPjAoq1kY9PFfFBxQBZTzI3Qh20IQQfuvmq9ZdFe9qCCqU263t-WHVVJwT4U_ejLYUoPNAUyzPFNp-EXq6eqpTsaPLIvxKlRb2rt5dSsiZ8QuKJWGnLoeNRu2FMCRmIzP6L5UQU1QAz5224EXkPxgN_2HYCuijkR2EoQ-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=NMysA4mepKtB6I3ytvNvUlG05HyDnvzhIe9z59Uls5iTCKKkRIoBNmvpVXbrrLXE4sIgPFdByRDuP_KunaDwOhMvFKYI3OndYQnQp3RHqDJAyScyx0NBtHWOj7MyZasf0bAZfe4ztWypgThWELkLQSH85pz7Q5LopTifMVWF8ThGLS3BPjAoq1kY9PFfFBxQBZTzI3Qh20IQQfuvmq9ZdFe9qCCqU263t-WHVVJwT4U_ejLYUoPNAUyzPFNp-EXq6eqpTsaPLIvxKlRb2rt5dSsiZ8QuKJWGnLoeNRu2FMCRmIzP6L5UQU1QAz5224EXkPxgN_2HYCuijkR2EoQ-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=HmNhQyQpocHwnGa7WI39s7vX94-sPYe1NGA8tZsGSsip8xq0hKfocFon6TrXxyDfbREVYD8h3FauXqJotuP3i8dTBQHDfXK_UP5MDyMb2vv8uxVN5MIbbRk3oZ1Un__DfzEVOYAMRK1-gUdw9SSh4OCfLTFRNJgjEnHr1ksGwMUb49XbtaFNHjexviytp_zuy-NmZJRuULy1sbk777swDLRhVU-G8UyowcHHv2hlpNaS4dLFmP71xb6jYRRsoZL4roMJOJOD7XTmWmGHA3ljC1T5fMRwQ5JGv0BcAkd0ZiBlECcJZUaJpZ5VnzCrxEWf2PtkF7HtiKB7n0WbkVpH5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=HmNhQyQpocHwnGa7WI39s7vX94-sPYe1NGA8tZsGSsip8xq0hKfocFon6TrXxyDfbREVYD8h3FauXqJotuP3i8dTBQHDfXK_UP5MDyMb2vv8uxVN5MIbbRk3oZ1Un__DfzEVOYAMRK1-gUdw9SSh4OCfLTFRNJgjEnHr1ksGwMUb49XbtaFNHjexviytp_zuy-NmZJRuULy1sbk777swDLRhVU-G8UyowcHHv2hlpNaS4dLFmP71xb6jYRRsoZL4roMJOJOD7XTmWmGHA3ljC1T5fMRwQ5JGv0BcAkd0ZiBlECcJZUaJpZ5VnzCrxEWf2PtkF7HtiKB7n0WbkVpH5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی جام جهانی تموم بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77786" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3780248517.mp4?token=gB0nC3drRIO3y0n4DhUbxBCqInkMyqKl-N4lykIh1CGQVhMzGMrYTOnwt49JXOJ3HGIiyeEomR8h5R8uPDvWE_zx9KoiR-FDgkcfOaJ1lEX8wjq2_taikHisBd-PILLiqobdJanXlSc2dFvmCyKadqbCdV0gITzT9rHgtjAiv2rT293eQzFUJLVXkJ0hgcI3YkYYyPv4B9IEp-rivUWS85Am_CFfiEV_UM4ZjHHQDAzZ_l3tQJvbxXDxuYk340INmmfnktr5m2u7NmcXWF5fhAn6QK-_ScPoV4Nf8AaDcwSJNqdvkHF8NTrjC13onxnH6cCX4tONVnrAEaaxhjmimA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3780248517.mp4?token=gB0nC3drRIO3y0n4DhUbxBCqInkMyqKl-N4lykIh1CGQVhMzGMrYTOnwt49JXOJ3HGIiyeEomR8h5R8uPDvWE_zx9KoiR-FDgkcfOaJ1lEX8wjq2_taikHisBd-PILLiqobdJanXlSc2dFvmCyKadqbCdV0gITzT9rHgtjAiv2rT293eQzFUJLVXkJ0hgcI3YkYYyPv4B9IEp-rivUWS85Am_CFfiEV_UM4ZjHHQDAzZ_l3tQJvbxXDxuYk340INmmfnktr5m2u7NmcXWF5fhAn6QK-_ScPoV4Nf8AaDcwSJNqdvkHF8NTrjC13onxnH6cCX4tONVnrAEaaxhjmimA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفداران جمهوری اسلامی:
مرگ بر عراقچی بیشرف نفوذی
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77785" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77784" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77783" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگه توافق امضا شد من کونیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77782" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7na8vGEao8O2Z3CM8luaPnAJReNdmZSLTTLph44S0ooH6NekTrBY-WN7GIPTgyaNmcpBH-9c_TcwBEoKaNaETjhYqVPmPvoPG9LZObxIxsoKpfqZJXfr2-XHEmilvDNIE2hTIbSJpMKPMhgP0VaJKrMXQcpyDwMdQRf-DlinNaJ0GAVRgcNOxtVHsYKTQTOCemaS_qqEA4bqIJDIQQGsE5LltFWQKLta4RW4yOy0pr4DpdOk8BxCmZISUEflZuGoqzgmYLTtZ22_iuPk74xh4C99gDV2p2e9ZXgWtI7Txt3uQBjkYoL-dgQJigAIKkf1QpMc_a1s4oAVpOZ_OH9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Joji
📌
Piss In The Wind (Deluxe
)
📌
Piss In The Wind
📌
Smithereens
📌
Nectar
📌
Ballads 1
📌
In Tongues
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77781" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک سری جاها ظاهرا طرفداران جمهوری اسلامی با نیروی انتظامی درگیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77780" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترام: فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77779" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWDFKUMEhiYCiuTuvV--cW6E_Tou98fU0oEFyW-k9czaAySSBKtmAlazflebpbnudFoZCILhAZYy4lPKURLNFfwb784kSq0GfWuzsjubAyInx70Yk3fJT6ZKoRbZG18FQPxTivPWJfEaqRSt6aOqVBSky0I7ytERjmrS6uAIzNzpTetLm07-nQXAdbMpOAVijkKSYFRLsmhW8UXp5IGINL3C9AkJbPdlowbGSBPIwsl1gmRFx6p3GeKDzY-9zqEjWmdfsjtodFcxD4JeNUKBGQpZ29Fy3VOc25B0VEgGi6uSmSc4UJAjdY7G5D_PxWS1OXDsElgWbVM6p2IVuWdPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترام:
فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای رو از ایران جمع می‌کنیم میایم مادر گرامی بنده هم جند
توافق باراک حسین اوباما با ایران، برجام، راهی آسان، زیبا و هموار به سمت سلاح هسته‌ای بود که ایران شش سال پیش می‌توانست داشته باشد و خیلی پیش‌تر از حالا از آن استفاده می‌کرد.
توافق من با ایران کاملاً برعکس است، یک دیوار برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود.
روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداختی اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، وارد عمل خواهیم شد و گرد و غبار هسته‌ای را که عمیقاً زیر کوه‌های گرانیتی غرق شده و قدرتمند دفن شده است، با کمک بمب‌افکن‌های زیبا و خلبانان درخشان B-2 خود، جمع‌آوری و آن را در ایران یا ایالات متحده پایین‌رده‌بندی و نابود خواهیم کرد.
ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای دور هستیم. امیدواریم این روند به سرعت، آسانی و روانی پیش برود. اگر چنین نشد، ما جایگزین نهایی را داریم که امیدواریم هرگز دوباره استفاده نشود! از توجه شما به این موضوع بسیار سپاسگزاریم!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77778" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYRgr02m3IzbNZYZmnNtOpf-FPCpriOo9A8ggeubMlqoVUTKIpodYhdsVOnPamlDJsLS-osHlPfi88WqZ2ig49Sk4NCDvxx3bfTiBuxX8gZFHspCBE8Jz4gMntxmZtMqkm_MEOkC-SG9hsHAHG-a0U5bRtZTsf-Q3rFqPfdOcWbaiI8kOR_Bdf4VlXbK5UCzsHUsOI02JG6JAQeO_lVgoMzXfz2mW9q_EJs5220W74GKqFlQGxmUvMorFDfrC4cVijPkfUvMNABqljCDsAw7LbNSNBnKQ3L4MFVb-Q1lcG393GsQKXOErryfQRB3IgB6kOtXMIo5tOPzJnmSsdoBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کاستومی پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77777" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-XAYk4cHvAPMWkF3NvGoTvl3SW0Z0tzi6_UCfXI5eMZDIZAxzuCeeY1N6FmVV9UYJJNtdlufWPaCjtS3wHel6BgYoLG7jwb5ZyebK4HQSGc2K3_eh75jDyoTj66T3DDxSLFTDwIYQH34D4CefI6GWdpnwLNOs-bSNqHeTgaLevqu_pAHYh7CPx7GdtTh2Mgg8Q8kGUo1ZCKh25jYnVY-KY5XVKGf294ikflBrEDHfYgS00POMkI09oiWwpyZY9VMfU-jPPT4gwgEFoUJtvcQP0XWcSrvTh3HZajHluxB8iTF6Wav0B4M1kflDOpyFV0_4FV8X6MtgZdGVGjLO8CtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع برخی از طرفداران حکومتی تبریز در اعتراض به توافق با قاتل رهبر شهید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77776" target="_blank">📅 18:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77775" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbPfzMWH0OBSfWvsFa_kttAriGWAHLpUgLUYePEeU1rPo7UlmMkzIq-1NyB8QkX8c5wkqFCtHfO-YWJhonqeqxV3f_QWPFAaVMmW96y12GilVBNrYUaaEcX6czC_heDVxOe8aIdV2aXSDS6dt8wIea9QGonCeChoPJkcJ2hMVHJwvZTIOthwOjXvgGlqpJrjabe-uLPtMT9-LdvPbvKM4qi_zSCbZYiSUGp177L4hQviqotQYuVHqlG75OgFXRO8ynfVDNCARvZRqMQeJ9rtY8hIUaiACzwPFgo-7HmFM-Vw_rMu0IgroBoS_Qw7uGnPvWYblarOOj6d0vJM1uBMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6FAFGZb5Y5CIg3XoZVauAfoyogmA9L99a1T0INWzK-vz09ZVHLhvqOQ2z6q4_mmebO6rWqM1fpkK2OcHJLwegodCFK8YUxrMBoJHN4RX3F_ajtQQe7VKhEBqKfNGkkh8RrtZto2nFHIUCoNnHs0WdtH9qbGehXwh90HV2xX4RngI4-nInXzSJewiv1Rx1yFTNNH5j6TwJwQaOuRJUvwRnrVBqDq7g62kCrdJPMvDqvTvRonwtdLRUKV4s0_tHwwvMI8Vf6uWVDnfQ-zqnX5vNEi08suONnuEfh91HniHfkG6fT_41Hm-h0tzQJZMd0C9AuJ7L8OGLIYvQeuiWz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان داره حرمسرا جمع میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77770" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77769" target="_blank">📅 14:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFP4uQWKbrLkWMyS7iSr5YPXhjUGexkGxaudRiiQ1zB0sB4xS0ciB7vzpERxnbyEkyYUXsoPQiniJze8KkTRamF2ZLRW-0hh0a0jkTIS13eQDdJJaRnaERjnVw6Bb9_T-UtTlavpZspTbu-UmGpFjhqs7qxRkC7KvNXy-_XMrGnarV443X4X1Y-Wo9axht9NmqJwRZ3fbQ2XRFjlHrNufjYqc2cUvPg5BqFZ5B_h-vRBWeEd_HptJwtdoo9rCVmE4xREelemyJkJuWf-z5XBqATiBE4E30fshQlPCiTDruTiHGwTFNJbNRZxRrht8kbQut1wB2vP_eCdSx-TkMFbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77768" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owzi2hdnXjf2xleB8GCupAWMniEfqFsmfXgnQkGjXc9NyC4PfhvSr-pbsNLnuT4lLf8XP5bdHLFbIzOjt_Nk19y9jc944rbZjcp0EEy7mO0CpnTWV5sQTz3xJkq3EWerSqMCNF2RT1fZFQssqqicZQa6ZorddO5lEG8SuACRzlyPpYn4u_3xG-ceMNc3cTM7YWlwb6DVmxsoJj_cr6ZlLGHzDFNl3XJXhGN-Qtq0JshdF62DSM-BABv4WkqcsQySwf3636Jb70kTgwv4pfi0J-Q1VCIYioNcWG2Zn-Qg1_MbS5M6lvFdHozIq8rAMvEE72TavPPqwNROvEefkeSGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف:
متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم
و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77767" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چرسی داداش چی تو خودت دیدی سولو آلبوم دادی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77766" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YByIs2R1Y7-8x7c1bjtItHMRx8EotJzlTRLUGb3iFQFAMPjb-9nQMDFjD0M_qcR9cl0adbHhnyBQDKiD8y9moYfMBP6-9IDvVibyc2mLt7M2lO3GE5TZboVrXWz1UJXpnmHAcDwOmc6j8MKi4galDqkwNU5Dy8ib519776gVyZl-odEWuktvN9MbJLi9BerMgXCVUSp5Tu1eaK9buxb5HwPw23NHG1UaBc6f9qaqp_DDjbkBvyv-szrOHr7Bj3XEAsbhUF1aQY4WeRyHr4O_dzKWZySIuPHZ-n2rxZsG8UI4Lk9HKZeMKzPhASMINxkSW_SzLh7bplBi_2WB417O9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77765" target="_blank">📅 13:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چخبر از توافق؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77764" target="_blank">📅 12:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN6ZTe4h6hCiOTEI4JaEmQHrhcs7YM1FI5r72x_adFYBRbFWoLgPzKmOgUJ5QiFZvdwhCuTatK6uLr46ljF8RBbN3pb6cQC5o5Qu8NFAYLuTkoUFe6mgcN5WMhS6LQncMe1zop3ak0l5fMy3O_rfqqf8QHjzMjtxI7jobg9IIW3tJFvbzf4VwxAMik4m-0LdEY-97v4WV7wsD5seKWlGH9s4c3i9HwpZ0_tITjVOgBULdQ92Iu--A6V4esZlkyvn_wLh2CeoZX_rSkGjsqjwzRKhmHOCUFwx34OUg00k7KTChWs8Whnft4cnGliFz-qcHlKn8pJCz1nmVhQ6e67_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwO3qmm7_6x-_ZL_eaVhiRZ1yYNc8VA1NXRb80_WunkstbxwXw0jIELkW-l_Xv-hBS7ShHt37riPRK21a6jpkQfvQH18va79OJrkeUY2GyUDbcBvt-5kLKZSXmlB4_zx0H_sCzZKtACF5-s4wgQgyfvLXlc0DlZVqMDKgGEcv3L9tyA48sRSlfpZ_kdLA_mU7E1cZb67vwwCJDyib6XV2CCnBRYCCkz1cbgqj8UuK96giZFks-ap9z72l-OO4qe1SDlfIaDM-A1KWxEPyx91lXKGdXAd9EvfCh48AIQOFHIkVxauSi14mBsZWwnAlSNumwfrGaWVtPinYDpdbZmpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM8X7WQonUfTGM_VPSwNmniCsbFXEGBS7XdT0Wk87uM9LBvY2CxY2NhTXvuiZTPiBL-hE7JOh6TJUSoGEvq8WsRVSJ7ZHRFV6ICsFGSAZw0OVu2CL6TghpX0B2wEKZYgGX6eg4CvL59SHnF_nBNBqR_8YGGXhIqRUTPy7Gp4-I6aYlhEwSbQ-Vmc1XKgfKTUGyfwBZGx1pFfRspTtG54H8qtpIE_iI-4SNKefeHZWlYqt_rEgdTaw5cJhMyBXlfnXPdv1Rm3YAqW6wmKr7TcCerxVAWT2Y7AaEwphHmRUTkCxDch35dwxaW6KljbWWSHaGqjnakgQfNRyQrCW2xqvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFu_h-Vm2N3oet8BHSB4jCB1_qwnKX9Kd3YTyEG99N0hXtum82RhufEQYmHBUYcC270zTA7-Zk7JUy-Jue4m99j80vwgkOazZ6PJDtQonZBa6iv8AJw1xBO4ZfmgN-BYrBhL1tWArPtsSdiCEsEjiVPPZYYseT3GuC7ELcp94SPbfc2RWgBWt3qSedOYHcfyvSL3XioZjfaw-X6_SCU8JHYycaF_cnGBNNIi4wbEfRQWcWG393p4pcHJ75xc9A7EiyhzFCBKFwQbK9zSGtgDGf1F6x7lHvfqJY-v2GKhE_cO2uTw7cR35PfcGUL_g0Vhq7Pdg2frt22_DUGXyIUYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kLen512IwTFvIUlojn7RZ1khyhirSAsiFMm4feSLvyqQEUXgD1d0NT4mpUspeqd87TvBWA0vZA6f-FrvcDmfTJdKSdjbP4v_EBCYT9d1LG2On-K1s1y_pqr39Eql6zYKUZg7sScNJDpLbfCcXpyMEZbLNTPCPtUOoSSvlfu19jyxVkkS6n2prAMVWTVxhIYRL81mkvdws78VZuw3mi5uMzAqMB4CqW8UuJaZ83MU1hMHp66i4AZEqn0MoaftsfR8xoJ-Zs4en-kyIgkR3n4_FX3u7pm-5kk3Gjg5rgjmmbr2UMEIRzOeqH_1RiILW0tyAPnXSfzjkwI4AQu49X39lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=kLen512IwTFvIUlojn7RZ1khyhirSAsiFMm4feSLvyqQEUXgD1d0NT4mpUspeqd87TvBWA0vZA6f-FrvcDmfTJdKSdjbP4v_EBCYT9d1LG2On-K1s1y_pqr39Eql6zYKUZg7sScNJDpLbfCcXpyMEZbLNTPCPtUOoSSvlfu19jyxVkkS6n2prAMVWTVxhIYRL81mkvdws78VZuw3mi5uMzAqMB4CqW8UuJaZ83MU1hMHp66i4AZEqn0MoaftsfR8xoJ-Zs4en-kyIgkR3n4_FX3u7pm-5kk3Gjg5rgjmmbr2UMEIRzOeqH_1RiILW0tyAPnXSfzjkwI4AQu49X39lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoKkkVfqHrFZfiDab3uIKYTDVeicgn4JWO_hwjDSivqDbGA7kCggIWwfjvZ8ofJ0WczvmYxAJlg3-ae6oZDQBcDjfy5bfj6IS-KqFFRUXiuibIF-rX3GxFllFdhT6OHI-X0np9avW4sEXnE1RZLAb0aklnyD1noeBdbHbhXKNan509yKMkQOgxmgs2DjVDewOWauETBO84BX2cOvKxt1Ct3VNbzqdiRGeyBgL1N_cCD0Q5jj0Ji7SxQtJFM2Bi5502EAYgVPo7rWNca2qtrN6pdBufn_6OdJFOXADLlA8rWB62W_ZHUHqghipbTKkqPh9xx3D5HYNwiROPVhGXs50w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_J--TYZ6aSEAnWhMwD1DR_tW61o8MPYbq0vAsVyDz_EcoXxdWQssLuNxb9h5O1mAJI0ciUBIDpp0qrolcocm2xOSZMcrxvcOs0xlXy2nqimva3RV18dcyPIMkytI40gkdyVdar7dTSkiragUf-JzeBtkjo_iBN2EITVD-6zTiiccLr4yYTh4P3jQevw25cn2Kfp6KIV15IbiAYvgLxCJLhDFgacUHBb6tiwIh0GL3po0ZQPagIWgfAwEpZqMbiVwAZWvMYsvUkQOpcV5G6qZLERIkRY8S9PR_YJDIv6V30wf9dKMLXtGyVxs85rV8Rv7Q2wJNCQI6dzPJ5Qs53bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO5dapp5UON_FtSJ5MzIsAN1XCOBTsxTuM4k5zELvo7lWIK1mDhgNb_o7EaCRgFnu26jzPat1CkKxjYZl0gMPQxH7ns_inHIh_JoGpyZF612n9_p_WQaoF6QsY0fz-X4bfgzFIVD9IrsSDjXzRm8Fwd1mHIoSIbrlkLONHKeCCWQ70zpOs7g1UrktfgQyfprZKB6avA1qcpAmjEQOKriozwpbmls38Pu0mj6jqaWpTcEXuu6pcjQh4aoZQcslRGso8Eyjg-s4UHq4R9dsEZLeoo2RVh9JhhMrkYdy2OpJBrHraPycVXxKe7HEXUVUoLMEPiGNODYQ0O9xxMUpL02mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDvZ-LwLmtjQFVjCq7Bqj1wDL4KvVZ2Re07v0-XVvxBj-6oN0xzNuP6b5wx3QPwHJzf-eIazgDIIjSTSOT7WlDdi7iw7pTYHn017IYaqOigeeskH4YMgAV4K2t_zOJjiv3qrnjsSRJMDoInK_eNYTF5yfX5H9NHEZSljrQQnM25Q0XukVq-bZrWo-Lh8Gjg6KU8kFAWz7CNuQQlq-xaw66oZ6GIdUxJt2FDMt5FAxt5Bwxbb9OWZ0IGjMIoQzYy5BEH4iOZbduJwfV655dMbbxMmRjI1M6C5DTmrRpNBc0D6XI0EihlsikC8jz3cLVKlUAzLyj28X8OXZBc8v97zEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGfhK0J_xU_w2MqL2KJRHKmPQwxr3hAIT9eMrufuCmD1LwLDZeuHSwSJVTp_Ah0orYQ_Ml3lFzrnjLcQyXhoFtgAoHAWqoyJuYMX2iysexxj_IG_pK_0msCSyBQ_vFXHtq_okX4WSDV552LL4f8ts7zipwcYcDlGCt0dcv7qCLBIj8xvv6eiAptn3nycuu10vWS9l9HrFpv6IDyEvFQb0tvo0bDTd1tgXRNit2CzgTohaE1EzfL37ohR-EGE1MYIMwL1wjC60M19d08s9vujXrTzPbN1KAsiKpIJkL6RaD_Ncl_nAXo14ops3ACacX8lKSzAH1v7YrB4sAA4Ki-18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCtGL8IuiI9ds6mahP86YHNzQzBJf722UvWgtOPmRWfkobcNOi4yJ6UcfLEqUgLd2UOFS29T52TXk1U2rvU0QypLwddiJtxgGYpgHoFFAIOEyId4DfY82NlaltGbdApe4CT25u8yNe9r4jCLta8tEsZr3yiFgUZuJwUMBurvYE2_rcOsAUOQb_L0TSQuVFxU0u45orBJyzA5rA77hjBeihpAjmVgyrgAymx-jgpqDZ4GcjN23ionjTIfcyXPMxOFVzZuEnDBEBN7UIQnafe9ZEG2TVbIDScbK7NA67tF_MapeI0-gY5H-gZF9KswoIjMFQXvVzpKADmeAcOU7khnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qas6arr3P7TSZoFxX27rtbGO7Mq_8rAVpdqBK2rmswxh3IH2GRhRFNWh6TKRMLIAtB7GVwhftty9Re3b9Ehyt_jEK5f9UqHsXUqevMUjST7Xao3CQMbyWW7qC5yUEAKeSEcXuangHfs-5rr6wP2X6Zri8-uiZsqFaFFKi4qON1VrwlMDjfbaAu82oOUglA0OEUeiuRZrl4z-mzRPG6KIeLFkcZDeDud3nHNyI31G1DqHBn-nnUpteNkJKeW6hQbIQHia9wXABykeDRdU4nCgXtjFrdYhKpB3U-CdYFQM57hNDx1jzaziEpjeBJm_CWrD0l68tvcVqUqCP6FkHd7Vrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJJoIAKpg2hNsKi1iofmPp40JsE1yzUwwgCfeQ13E6rrQSah_NoiVTOJxwwaoIRg_3HSxiTAbdoiu9gUvdJoUx9v_6QaXWB7gpA4rEDKQ3_7eEyxs68suBFya5bW5HZ7EWevdilNuUg6k2yuFSFXdVLS60exd0LmhGcRoq1o2UPGZrAc53CT1JHs0WHSqusf09IoPED24YYJHZ7UQK4tyYa8WrzDCXzur74T24ly94L2xLHhNMKIlQldYszArIC61GCCcozlPN1jzP6a5BXIBzQ1ey33NZr5TBkdLRNZiJA-BuFow1DSgJ5T6170fiiVsqI1mpTdRTpDlGIMsudyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5u5hVZBzixgr9qJFIAorDAjjRVRWiP9GYabXbdz2TlOxelEOWLZdwDIASLqTtDR773igTZXffsE1r0tehJSrrvsoXoGjhjO1zld5_SnMdehjaohZYq938Dz5F7vNTS95jZkmVbjyHTXHXTeff4HBT9kqIOIPRNkKdJ29BS-UDdAWs8hOwi54C0oYKP4vQNIyg_34P4RlDEiX3hANc17-JuKaA0R5humQavbSVkHudD4GYOB_XSOeo8v8ddS27fSbQqPD6CRVPJC1nGkEMV0WiOAeLLGozXi5VjLreXPQEJ7my7gtujyb7pxLk6KGRIWqAJHyzBT3ctwryZiG7oolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کره جنوبی هم خوبه ها، حالا در حد تیم ژنرال نه ولی خوبه
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77724" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9N_idq0a4l_J7ORPoL7mCvBLCr9yvQQFbNfv7hX6vi0TD7VhClqH1ZlvoDxFNjgO9tRs4wmUFDid8vEd9FO6soqt3oNs3hdN3KqHbxj2vmQLXOeQnah6wdncKbDLBWEPgnotozjWWlQAgCSXGjjy6Luarxtj7V4exVQsV1u--V2fIEJcvG5zh4H1mayRB3_Pb6Aqgtdl4BosICOhFOXigj3dp_tNL8BAlGsi4szgYQoj3hdCymCDI2o-zoKsrIy_7ct5L6AyNKk4I-rO9NcyVVLFo8p-lQYI24A3c-44TpSiwEUwW1Elvbxha5bjLlNYy02YhZUfNtnYXEiWKaH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو روزی که همه ویژه برنامه جام‌جهانی رو با رامبد و دیبالا و... شروع کردن ابوطالب رفته «علی پروین، مادرقحبهههه برو دیگه» رو دعوت کرده باهاش برنامه ساخته.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77723" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77722" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNMsd5t1-fjQ47EhJGWYhHvRRkZbmtEX1cSxmt42sqtuAsiOr-BYstKzCG3sae0rwxFcwxMkBjzgiTV2e3JxbmUuTA2dlZ4RRQRUs-j7TJ2Nd445W1gJUcqPrJoVpGOGkvrJKyw_LQo8rWxirFWcFul-Mx0hGEgtk1N0UZlcSaqp-jkYlvhuaykMTX0VtfBOfayThCuF9T5XNKZY8cDj_hi9RxZS-AITXuXxIB6upFTwb4Vv0h6bELmNleJqhOK-LJwOHkKQ-GfLwBHXf5AraUGBLo3denFCWUShm9uFJb6piWylk46wN46LSnBdRi33blLqfw_kdGGAfTM9fh-lPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77721" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز دیروز: لشکر 82 هوابرد آمریکا خارک را تصرف خواهد کرد.
رویترز امروز: جی‌دی ونس و مم‌باقر قالیباف توافق امضا میکنند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77720" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فاکس نیوز درمورد مفاد توافق احتمالی:
مواد هسته‌ای ایران نابود و خارج خواهد شد، برنامه هسته‌ای آن متلاشی می‌شود و هیچ پولی آزاد نخواهد شد تا زمانی که تعهدات خود را انجام دهد.
یک مقام کاخ سفید گفت که تنگه هرمز به طور کامل باز خواهد شد و ایران موافقت خواهد کرد که از حمایت «گروه‌های تروریستی» دست بردارد. (دقیقا کی موافقت خواهد کرد آخه حرامز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77719" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=HBC8XmfID76M7GzXcZ52Pp5sIdkYgq2YIg5roS-MChspPObcfwRnWFqcXCsC-hzFTE0XfG_G7f9JRK0R58mZAdU3SllfxY10aPmyc-v9CWb3oHhW5On6TFDtYBblfa_uuobh4JaG3zsR4oMsWYwE2K4N0W_6nAV62fhzrxEqwwD2KKg5aYu753pEACAgTJxvsE4xxVIffm4EL-la7MkJzEegRrJ80rYOQiEkU9K1j9eYO1x1up1Y2j0njvxh-3IMmCkMk6id3ThPsbIzPewyrNgiAJSykyEVIYoHY5fwO9d-80lIlwnthmvezhfZYOy5UIT4_6kd-6IgD-10dxEjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=HBC8XmfID76M7GzXcZ52Pp5sIdkYgq2YIg5roS-MChspPObcfwRnWFqcXCsC-hzFTE0XfG_G7f9JRK0R58mZAdU3SllfxY10aPmyc-v9CWb3oHhW5On6TFDtYBblfa_uuobh4JaG3zsR4oMsWYwE2K4N0W_6nAV62fhzrxEqwwD2KKg5aYu753pEACAgTJxvsE4xxVIffm4EL-la7MkJzEegRrJ80rYOQiEkU9K1j9eYO1x1up1Y2j0njvxh-3IMmCkMk6id3ThPsbIzPewyrNgiAJSykyEVIYoHY5fwO9d-80lIlwnthmvezhfZYOy5UIT4_6kd-6IgD-10dxEjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
