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
<img src="https://cdn4.telesco.pe/file/X_-e6lMsEVsGECStl2MxiYm7fD5NtfG667xkgdFURD5mblanx61_mvDNFT9CHpF3cB-0FOLg9ebGqwSypLaBxUod352XvDqI3NL7SQMl6P5fHLujekxhCn2JeZ_DOtXkhTfSFid1dGKXZGcCy8YG_lPZWnuZ5qH9auzhJXZ-q8sQ15AVg6ZlxoFiwQ6g8xgWzZcyywBagCuggXckN-KxulGg8lEXbvUJPdnn7kkl6_yRYzyjpz-UL6z50cGhlFAL9IgYaqXxr9GVB_w0LUNbHLYa1VTxz-RQ921WUYqBeee4XdsHJmnGfmweOci7pJgVe0A5yedV9cnJfHaNp9z1lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODODr8wZNL7nJnqRWYkVfKSc-FmsL2MOP0EX6jBAwGOKFmo8rvoAvdawkYeryfK_tTM_W43OXTAOwqsQZaddPq50sqKVPNuN7K2YtLBDfXp99n2Q7NNFXDAW9FSNOXFOtjRjoTSaFI0dBfz0HIckNeiKdtz5yzPyNdLZOYBJXNXZVlpuqwL0T8uxblp2aGcYEQNqr_OV8Jck-mxyUWaIjaHk2fXa5U5KiBKRpCfCFX6jwlQPDUIUPRk6S6bGqiQhrAE6aEpSkkDip4G_m1D-RXTbvm2q3nYVViJNnH2QJiBf-ggO94ZH3vzUR2ztS6E0Hk37FKs2m84N8xXWah5tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz4ZB4Zsp14g1iLQ4aNyh8DGrNaoHwHK01HM6kyl6EgwKOXegXUiowv4RV3NeLxHH2OvbvdnU8w5uP6AK5A_enmn9XodehIKBTONfFU7Oua1RWl4DxHkbDzeqHjWtR-55R_7pMm_NVaqX324KXcoL48B5kpR0SFFc1JmMQSfZ1ZSRFoQO7D9bH46E6vnKPi-SXRb_cpjUwuXhQk7QWGFXbsPoucS3WF98uxSiI29gO8evvCBdkQYxvwEG1GEINVFcs6Qm6pVt_6xVa-lII4fCT30DuTCEJ5igFhFsycXtIjA_DjCUbVUrmYT3UVw-PhP4k-jM9UD11jwL5cjwz8gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9HvSSJgq5xv4_08gy67bB1oIUBluXs-aHjP8MqVcJu5dEux1E2eWL91lF6IrpzayNo4BmdFcC3ifNX_VFeETE4zONS-Zu6UCkfNX9SgC8MyECIKKBm79fIk5J5YSb3agJUMqYvxqv630U2hOk4tLFJSWAhvXgK9Ggo9XGveQLaNQdTRBwRemePZMu50nBG5r6gWMh6Wf5k71Df13nMhtPSjfaf3_wayP3r88K9OpW5_PRSH96NkRwHX38zRB9Jegft8BQLMhq0PI00UrC7TYCymjerRuABY420yBkqEH6_-LQ-QritMY-Nl6LLmgj_HkuRApdrSUCWr0cln42g2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=scWxXZR5nhF_ttJmx0VO3GSTbO8PByzd31Sd4FMsyj7TaQdb7-pwlNbYLelYxIjvtJIYAvuZBJNdbducvlcLvAv2O-x1GvHLbujeE8tDm-aTKKuJjowEHufpMW7r06WtbbiYwB6Ao-_6Gl8Zb3pd39_WCX--76r0Rq0qtXRKnawINF0PSSlHxo_y6l4TuK8_0ijzI6sdFmKe4S_jFg31aZT_aoJYs9k02vC90SxgTmxdqpUcChvjVkCDE9mkVN18vCw-INEvbNcXgxcJGjPGYhbF2D_ovKYbvqP6h5UNjrUwzMtyMUlGI3KVnI0hxW3VDVzCc4wNn1KFpl5CcSW0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=scWxXZR5nhF_ttJmx0VO3GSTbO8PByzd31Sd4FMsyj7TaQdb7-pwlNbYLelYxIjvtJIYAvuZBJNdbducvlcLvAv2O-x1GvHLbujeE8tDm-aTKKuJjowEHufpMW7r06WtbbiYwB6Ao-_6Gl8Zb3pd39_WCX--76r0Rq0qtXRKnawINF0PSSlHxo_y6l4TuK8_0ijzI6sdFmKe4S_jFg31aZT_aoJYs9k02vC90SxgTmxdqpUcChvjVkCDE9mkVN18vCw-INEvbNcXgxcJGjPGYhbF2D_ovKYbvqP6h5UNjrUwzMtyMUlGI3KVnI0hxW3VDVzCc4wNn1KFpl5CcSW0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw7bVnJ6lFdoBxAYBOkXdChQ6B3LovLinuiqw3HWtYo_K401DUdGiOekdsJcUe7ey2ruaEEO2ghg_cJt54b3LN_w5LrWe79pXsKxs_9zQPo0vOIFJp2e8TtDRhRFKY8s5--niwrrcoxs7jBaQRyqJvn604vI0yLd0oqTGMF3qeV_FM-SCoRcKnJT03CN-X17NoyCo83Ve-3mLRKCo-wnpV2EktMfC6oMeLoUtACuUfY8zhffsryW5w8a-Oh4oA5ZFZ_CCsqLyIk9I9YeiL1vv1R1sWh2_vIBHLpWppy_C7agOAT3x1DOAT3nLDHHCGPeedl8aT-X5UWbUmgWLilWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/76808" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll2TtrjZpEAL-bPJNsDar9DQz4u7CaTdU01sH7oMLU3r7xOtpq4eDo2pzPCrfpCamIaabHPujEayzUhJvl-fVeWj9nBelY3tjHgSZ77Fg0OyfTkru8mIVV_XoPYArBVmxlKUNeGfVpPQP9l8fFsMlEyZzFbSdhcaZQytVXxGu2-v7kCApZPiy9izTeppxaZ7hBlgKRfzbIGvs-IZpdKvBSIn8XuL3KbQ48-f-aFLkadnpZ3RZF3-aFpzxkPjPiYq49PV_FeAyaYWlzIoG3NYMuanpNMQdzR-K-K9CAKFYJ_5e6wI-iXt5WKtitt__DuedZZJw4Lx7mTqIL7pkUDneQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r14
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/76807" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=MBn-1Mboq1GZYsYz9N5iLT_m0gRllqe9jyatuum3Gz9Loywcy4jsN57hpPKBg7j0J9g_03d_nRNlh68aUwTvaSaTCYJaXD2ynn9ZR5p0F_4zvdzC7aTzTMgmpYEhTxrhcvQKtgbnWeZlWJyvlPW7m6iatlCNIfn-pRjyVh6q1pFx8AqVLyqQYIvbI842XHWxQ5VK1K_dNrc_YabetZXluBaVhdzAIF-G63Cmox_Q9Hh4uifBqpgQI6NQm9kiIhOUnuNxVaNfK236Yzng7TpcGO6F-ZfS4WCGSdstD8Egs_Xi5hUQPpGIWXiJCIC_-ZyXWRR4e6eFYu_GqE1tguJnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=MBn-1Mboq1GZYsYz9N5iLT_m0gRllqe9jyatuum3Gz9Loywcy4jsN57hpPKBg7j0J9g_03d_nRNlh68aUwTvaSaTCYJaXD2ynn9ZR5p0F_4zvdzC7aTzTMgmpYEhTxrhcvQKtgbnWeZlWJyvlPW7m6iatlCNIfn-pRjyVh6q1pFx8AqVLyqQYIvbI842XHWxQ5VK1K_dNrc_YabetZXluBaVhdzAIF-G63Cmox_Q9Hh4uifBqpgQI6NQm9kiIhOUnuNxVaNfK236Yzng7TpcGO6F-ZfS4WCGSdstD8Egs_Xi5hUQPpGIWXiJCIC_-ZyXWRR4e6eFYu_GqE1tguJnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=WxScwditMidUaI45CsEb8-hl9CHTJ6MYQ4q88blMsr4Q-JnfIxcHV9ZC7-KE-MMrEjne7yxRnu3gGVKlEyYRKYjEB3fZ5R-31jIZ7iEAo0x29uOTBjZG3FWeUEo2b3SAWydS_PMuytojJKMiyHhB99BH-dhMAbMYlbPl217FeXaWegqD3eW-30WDjHOF4_JAcFQGZmAnRZpBLr-wtYdfgn58OXDAAH5TBlg_dSjfB1zWLXgwxLOOUHeremTD6MP_oMAUJ_ptD7Dd_yafWOoLzncaEJ_zq9WSBphqcc_Cd6Bdp92FjByIpADpXTSn1ps3K29gXFW4mNfmBvuwPmMYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=WxScwditMidUaI45CsEb8-hl9CHTJ6MYQ4q88blMsr4Q-JnfIxcHV9ZC7-KE-MMrEjne7yxRnu3gGVKlEyYRKYjEB3fZ5R-31jIZ7iEAo0x29uOTBjZG3FWeUEo2b3SAWydS_PMuytojJKMiyHhB99BH-dhMAbMYlbPl217FeXaWegqD3eW-30WDjHOF4_JAcFQGZmAnRZpBLr-wtYdfgn58OXDAAH5TBlg_dSjfB1zWLXgwxLOOUHeremTD6MP_oMAUJ_ptD7Dd_yafWOoLzncaEJ_zq9WSBphqcc_Cd6Bdp92FjByIpADpXTSn1ps3K29gXFW4mNfmBvuwPmMYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw5xEH39-jISZ_AC6flT6shKOLRJ8EVRoP06OZ6qrlxBjzj6a2PezY2Vkx0N_-12QPoVsoJUau-VRBpXlpv8hmWGvUtnPxSVcC_mJzjySDxBICrZlQBqggVJE7B_qwYpgKVtK1Scw0Jxug09NjXvWKgDxuCFpPGgdV4h2LxRvzUcmJrrh7hIgeflsfp-nbvJe49Z4K5iOM8eqybxF0tGPEFDEUBGFT6SZM5bSIFYCgCq_0aK_3_pWqYnswTZDAwmBZD-WRuYekHZAVZa01bRDID1bzKL1JFEQ2VAM-M1XCo4514nsO1mIzKLtuMxjViIHoCahItqbCL01E_VrDdj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjsR8W6v5Uz4ZKPrQNtqKw3Dvfo1zUI0ktyugSdA1MIyjTrSSx0wlYEIfmpHSeY1_o5QhTlwdKRjgnnTpPQb9S0M69JbbMAmP9x098ppmIG27Ay1smKoH_dkneJbBwnr4YAk4NhaQXlWcgQ-cSiXY5AMrYp3Ig85zFXtqAowJlcuf1PDSekjC2h-7GSb_xGK9h86naSS7NPFN1AX9ifNVxrGEWWKV_oS1Zpomu4YysU8HYk3upc3bSb19KfiHMMZoYgzVj853XvyNzsQpuppWooHnQEFRzxqaaYJgVhMy9H5XPBTRIaG3NKyEFN0SqRrn6y0H2RRZSyeEhAUf8q7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1lGGofOfK_ESuq-ld0nhGcKdfnYcax68ZYKOgftY8IaHoFnf66sRE7S8RYIuCyOYR_l4T2FuS-DmvdS-4neY9fvLLCcUJwlwrYPvVisbcJDEj7Zicfap8s8O9ZHxKKsZO114A0BWFaoqeZ_4DE_pmU0rbJc9Fkruh5ablQqpYYIYquqtJ1HTO7HW-8kCcmxaMdlxdVMi1jtMnZZpmDoaeF-cGK11HhtrIKWZejsbiCJeShs5q7qo5TZnYkc7D5_OVHn596q_FgXCDFVxogxM09CsaPoGRwgopmMiSTtzzh7KELUa4ncA8tfBav5SukaIbxYSCFN4dFBzByfw7iVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=frBZ8Vp-ODD7crD5mo664Lpi-n6_4LcrTjfdeNhWRV8-RERWQSVRVwIZdAj4o7_tyNTAdfHjBi__ZTIrb_7wbZV6-zeBUGnHyz-8EHXk7JU3excALHAdhVm64veRjnroWMnjG2L3scFvWMcH6j05XisZrloTo_nrqvBg3Y6qoDhvLyEuDciQ1T-d8bPr5uvMj_3ictsJveAgOL44B7V5NuzBW7ZL1BbBAobNvsM3JxTXN-8HOjViLzIDKL3Zxewkp6J5CzJJMDUxE9T4Uv95hSZC01tJBw_4vRTfOVPw7XC-eVHWcWG-KL_4V75eNW2Mm2zJ3Kc595CUQmU4b0L_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=frBZ8Vp-ODD7crD5mo664Lpi-n6_4LcrTjfdeNhWRV8-RERWQSVRVwIZdAj4o7_tyNTAdfHjBi__ZTIrb_7wbZV6-zeBUGnHyz-8EHXk7JU3excALHAdhVm64veRjnroWMnjG2L3scFvWMcH6j05XisZrloTo_nrqvBg3Y6qoDhvLyEuDciQ1T-d8bPr5uvMj_3ictsJveAgOL44B7V5NuzBW7ZL1BbBAobNvsM3JxTXN-8HOjViLzIDKL3Zxewkp6J5CzJJMDUxE9T4Uv95hSZC01tJBw_4vRTfOVPw7XC-eVHWcWG-KL_4V75eNW2Mm2zJ3Kc595CUQmU4b0L_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8UQN6hQJO6f8_StsZ8YRp6HENfuzSqQYpYC6A8ghwC5VgzeYc-K5ntIkk7hRjklfgQwarn7vAC4CSGPszE6d751q9HLXN5V2ThYUgdXQpKgSHdi6YeUGO-RrFZ18vCazpcYLgKwTb-JtljcGHdXI7UkPvhU0B5aNEtKY2qk7RI7eAtN1C4DqYqCAcJ8WyAsBJCSefZSnpX10d5cte3LiIlVzuX_2cOGZChLVQB3ustYSy2wBF9TwccV_k4eganHsrB4AoF2iasei8sK91gZnDoDAx4ns8TnVDE9MA_v8i6wybT-ME3kvsSB961GqguV-rJJSmUF1NfGJMjNvxCXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=rdYnLPSAsKwAPJrBuAjLsDWRikyF80KWOmBZOmoTJ4za9tPEoPLykl1g66BjB6bqevVBK6gk_oq_pylf3aFzDySEuZir-WJa-kID8UYO53GofQFzrOmmy2IDcUV6a6Uy09iAKoFi40el_n6Vot0v-EcSt3pbkPQ51rvLTRkI_xJNuhZhUndYWE82bKCMsz1GJdWwJNjz1FzK6wn94rLyKTB2UmNlNOhfkeg2BDU14UBFEXCAai6TnQ9veoM_OnVOLdakABt9-ciPJUyq9iTJX4vxPnz1GpcXOxr_IF9IsqrP9NLBZUMVfGoy7bDIfNujjUBDU7bqVqBy86asmaJmuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=rdYnLPSAsKwAPJrBuAjLsDWRikyF80KWOmBZOmoTJ4za9tPEoPLykl1g66BjB6bqevVBK6gk_oq_pylf3aFzDySEuZir-WJa-kID8UYO53GofQFzrOmmy2IDcUV6a6Uy09iAKoFi40el_n6Vot0v-EcSt3pbkPQ51rvLTRkI_xJNuhZhUndYWE82bKCMsz1GJdWwJNjz1FzK6wn94rLyKTB2UmNlNOhfkeg2BDU14UBFEXCAai6TnQ9veoM_OnVOLdakABt9-ciPJUyq9iTJX4vxPnz1GpcXOxr_IF9IsqrP9NLBZUMVfGoy7bDIfNujjUBDU7bqVqBy86asmaJmuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=D5hQVzCr8258desYzSqZjbPpO-0qvSSdTsmfLqacObeHE4OYzwsX8VhhLqHhGHywrFKWnnqHPWS7fcGoCg138RiHC_UpvbKhfm0KmnymHsVntxR_YlXMz9hYfaPmjt-iduoRZw1VEbJD_lhYubyWS02koYW-oWQNAHedl3PIZNyyD9X8LmmwsFs1z-Z2KR35XcwLgnzP-XGIcRRv-of5ePK50Njs5w81XaCIGwFvy9_x-EIPzAZn3yjzGgKGOppcIdO8vx1aaKrLucTLPt9AwfVce_c9ZNhoTayYdyg2zGUMFdmh8-_esp9l4VfKG7-8erkndFzm7ai7MV4lQ52T4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=D5hQVzCr8258desYzSqZjbPpO-0qvSSdTsmfLqacObeHE4OYzwsX8VhhLqHhGHywrFKWnnqHPWS7fcGoCg138RiHC_UpvbKhfm0KmnymHsVntxR_YlXMz9hYfaPmjt-iduoRZw1VEbJD_lhYubyWS02koYW-oWQNAHedl3PIZNyyD9X8LmmwsFs1z-Z2KR35XcwLgnzP-XGIcRRv-of5ePK50Njs5w81XaCIGwFvy9_x-EIPzAZn3yjzGgKGOppcIdO8vx1aaKrLucTLPt9AwfVce_c9ZNhoTayYdyg2zGUMFdmh8-_esp9l4VfKG7-8erkndFzm7ai7MV4lQ52T4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGz8QMwGd-dN7wKljMavFTy368xo2VZHZEMw6HK6m6M5zv4HPMxsYtNXAVvMG4YpWnFAbXMjXY_3-J1D2AnQNSyPuG1W-rxkASRhGD_EVnaU-sZtjmnhbMo-jXsoYMjNAsRuijDwdpKCS0lUViUmyk8IJ2kNHr1d1VvNsvVL-zBcj8-p0j-9uZ3hfF5ZyrjXvEzgc6z5aQvt8UKp8b-LHJG82yJBMbyB1gjej88YVtwGwBUpE09xUeIsxtPQteFQC7wdLZDpKd2au81x9K7rCuC1aSYfTDlgfHuXKY3HKAzIa56Eyv4wp_RZ4N51gBCRdzVsBmxXh1kW_L8J2NKD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=Gn8CERt-MtPzMr_qLFPEmGaq8NFIyUBRh7HSNskCtL3cYdA0P6cDhKVp3DlB5_4D08Pj4FeRefYx9LiUU79MXiwKVNAhXuWLOiRSilyk9TV8ld54vldWAgICa4yq26VrGD_IvV__zSD-TtVVfw1ocULyNnKORUKCHkQS7a356kLVqoFbvfT1nZlStAFWAB7d9kd9gETLntbYNEn-nVki_Ml2YCCrvmqtpX7QJQcCvWv72oIeCmdmnYfxBor4JOmSp7B3QMerYrektxQQuzYZGX6dA26YSBoL7d8EyzaTXewyhmMH2X-ca368CXTuLDGOO7HBmv7HYpJVDtbI2tWb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=Gn8CERt-MtPzMr_qLFPEmGaq8NFIyUBRh7HSNskCtL3cYdA0P6cDhKVp3DlB5_4D08Pj4FeRefYx9LiUU79MXiwKVNAhXuWLOiRSilyk9TV8ld54vldWAgICa4yq26VrGD_IvV__zSD-TtVVfw1ocULyNnKORUKCHkQS7a356kLVqoFbvfT1nZlStAFWAB7d9kd9gETLntbYNEn-nVki_Ml2YCCrvmqtpX7QJQcCvWv72oIeCmdmnYfxBor4JOmSp7B3QMerYrektxQQuzYZGX6dA26YSBoL7d8EyzaTXewyhmMH2X-ca368CXTuLDGOO7HBmv7HYpJVDtbI2tWb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=Ko1Dc_D84oN96tAzLjY_7OHe2_EfqHUTIMuYunD0QfctjWIkcvzhfaWhS9PWdkltoCWutoi1UbnvvHxPGZApOO5Dx4IkE4Q1r3fMNMA6hGcQ9-1bdiG7tnyX3gkirHtF8UZHUGp19FsIo-_dcn2lduWxe2mGgZS7OyhV55Nz7btKz0KCUk24ieHARIhfDkMDheVc0dhTXc-3hO9Twb32v7n2FAxSbruf81l8X3hCm_fGg5ciXOtWxasDKIAgc_FtlNZ_9HaWOuEQwbYkdq1aKqvgRM8uVS_6W9m9rhGoKj0PsmIeumYM1vwl1sUmW-RmAplfX6vYYw15SaIUvFV8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=Ko1Dc_D84oN96tAzLjY_7OHe2_EfqHUTIMuYunD0QfctjWIkcvzhfaWhS9PWdkltoCWutoi1UbnvvHxPGZApOO5Dx4IkE4Q1r3fMNMA6hGcQ9-1bdiG7tnyX3gkirHtF8UZHUGp19FsIo-_dcn2lduWxe2mGgZS7OyhV55Nz7btKz0KCUk24ieHARIhfDkMDheVc0dhTXc-3hO9Twb32v7n2FAxSbruf81l8X3hCm_fGg5ciXOtWxasDKIAgc_FtlNZ_9HaWOuEQwbYkdq1aKqvgRM8uVS_6W9m9rhGoKj0PsmIeumYM1vwl1sUmW-RmAplfX6vYYw15SaIUvFV8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV-1vHQkL_DIZg7e-Dyyt5g2RzWvWAzisC-mvuu8Cx1ZyXrUKuVqfcH161tlP-qlI5fP3kMr-NGNDAoSF2EWQf1lLhiDXFBQP6rjAoNE41JUMoOWne0y1qFjrNY3sW5KXIFdBbR4gvIH4jPJi8Wwk5NGYYFVckEgZ5QRwKH_5VhiwENe1GSlryBBk3hvvUk8ENP0Zud0TwQp4Bfnq826z3JcZ1d9RVUDCxy_c6l8lUE8W4XpK9nxCrzkUxbXGvfiwzzPP8XFqefAgviD5x0htzEshUphbAFqJVNXILWENPw25ZMU0xVXMqMbkdnxVmU6uUjRVim_beYnDBb_xyarlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2CCVQCTpSd9xuNJIoQMohyX0vEPCPatUYW_JqjGThNiObsOPEVkWICFW3amH6W9_qx0NmtyVSpZtVnz86NNW1OxpvJVDxJQmLEM0Nmzq6762cpBt1EQT3Uf4bLE71aJUPfiEPEYNhCscw1UqfsKfK5_HzW0t-0WNSw80YuY1bsw9HfYkyM6-G75P8pkn7Q_1A4p3L-mD44ap4pZqQR5_1CpVi9jDmDE0wwG_HC8WH3cdF4rBYFRNrdgwODA67-ynsxZ9wb2YCct29I080Ue2mCFqIfhC--iJMmWBHl1fAa3tEpmACtIP0H7iPf-hqsLun4Y1yIh-7fuGNo9P6lkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8FHwAdH8JaYrN4tEEQlBAHaxOFzfQVG8pWK5g4xOYf67AYwTBD0vrejs1iWf2UXW5S0u0w1qkiGTeXug5P4y0GX-uN8DLchGZvPEKPMgcnk6N3IJrCv78bbY5Nw9CDRm_nGUQ1Ue6kLH-1MVUcIjyq07jmljVmfnT5RHsIBl1FULFuRAshB-0dHiRx4c2uzj1x0v5oRHZiyz2gwSfOtj0DFsLZFJ-kjQ414Ivesg7spZs5-JVxLHTB5J_aIJVM9qctCROCi03D0NxKGD8llYayg3VyzfeiqizO2R2FVMHqSdf5noQTvGYilitmJBqsm-3JPO8daDWngFCs_8B-fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGTNnvp-8HR1qpfMkWrvRIg4wekw_Hrg0jXnEXKOqFcs5oCCEGtTBCYc0JSiqTWey7eBxrqLYb5CvNApdMTw-61gdKoGAwUJ0oL9kUB0kXsY2ww8QWeClMxI-5bH9y3i8LZqCh-y6OnfsoKlaY38AeTQHP_U3WMDQH8l4jmTEnAyvs6kc5E9m13t8KoKQpGNGKVHs7P2uKqjOdYTka3oT2knnczoTpAKZkcIfqE3zR3MgffAhn9ei93MboLwUluIk7vH98l5CmOE3gmZw8GGC3_2mJGllxfxh93yoQWgX0yGjPKgoLM0FaavpshydbJHwDlm6Evw2BAIHTA_aSk0ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=FQyM-OCL98uzXUK2BhJyXsHHdyg3J3JRHiwaH3aD2e-ra8m_iZh0XSRz0HhzGHrto64Mi_1fyrC5tTTDDDOt23Dleu9n1-ZXw6jDxuWrDT9Rbrkf9-Ven9nzhskSkReNQBvpYRmu57-viK20DScmAVnd-DkKGYk_DTvCZZD0JjJv8KvCAgMYkwdXApcN5h2A6a6yHSgyBUodY2Uux73IIAPsOvo8q7sngo6tHfaSGJ7W7rZerj4TjyRsxCbU9hJlV4a3yp3IHYlL8XVIk2coe-ZzO_rKEAdCHbPpl98_meu2u_xvswDi6zN5NlMEnz28XyLOe6zNnwWPTLSc5hvvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=FQyM-OCL98uzXUK2BhJyXsHHdyg3J3JRHiwaH3aD2e-ra8m_iZh0XSRz0HhzGHrto64Mi_1fyrC5tTTDDDOt23Dleu9n1-ZXw6jDxuWrDT9Rbrkf9-Ven9nzhskSkReNQBvpYRmu57-viK20DScmAVnd-DkKGYk_DTvCZZD0JjJv8KvCAgMYkwdXApcN5h2A6a6yHSgyBUodY2Uux73IIAPsOvo8q7sngo6tHfaSGJ7W7rZerj4TjyRsxCbU9hJlV4a3yp3IHYlL8XVIk2coe-ZzO_rKEAdCHbPpl98_meu2u_xvswDi6zN5NlMEnz28XyLOe6zNnwWPTLSc5hvvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoQRnEwit2Tn5WkS79H5_ptw578yJxj3bd9G3E5K3ObAjT8Y6tMRsjRHrg88OjosNC955DPCGFiq64XEqq7WvJNLjXSum13dU-bdbUyehOB8lwElivh9qfMueUAFGO2IMG2_5QRY_TtUCmWBQMC_6z1h_AXu-M30Y_1piKeE3zMH6b2T88lV0ViFObFNN8eD4RGY7oyeEx3ILB7TIYziKoo__hTrAuOfwZR-QqNSNg9GdqfK_GGcdehkMfpLzozT9ZsG-DHWPA7fTydZwCFzoaaxcJc6AVeM8nVwV0hXRfIXU0yyBVWj4TkmT42PtN5IuOz0OeMJi7HpXTB6Fsjb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=fOZw90gXKnJ0ejOnkFHyAVhBpreSAxsGL5fNLXhc5lvUr3dojljsuJL99T5xjFAyXtdaeVnoH4FLk_yc1KFE0s7i_DF9j-OIjU8Lf2Xvv7dnvK0MIE8vJtpaeYIIl4MXvIDeq3YkTzUBNqWnNxoYel_y7y59rOcgGME57okW6exY-dWaTVEVt_ToQ6XrvF-735tdLY_tqzRN59uuy6SCw9CR19iFazXiyEgpAB4pEDmxpR8FwfdmU9Plm60CZxJ2H_HGVeLcPv4Dd3dIG600Iq-KvB8J80W-dqXPiIEKrKhGoMmC4SzkI3CSOxMCarFB7sk3Ry-pOOw3CJ1lSsuKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=fOZw90gXKnJ0ejOnkFHyAVhBpreSAxsGL5fNLXhc5lvUr3dojljsuJL99T5xjFAyXtdaeVnoH4FLk_yc1KFE0s7i_DF9j-OIjU8Lf2Xvv7dnvK0MIE8vJtpaeYIIl4MXvIDeq3YkTzUBNqWnNxoYel_y7y59rOcgGME57okW6exY-dWaTVEVt_ToQ6XrvF-735tdLY_tqzRN59uuy6SCw9CR19iFazXiyEgpAB4pEDmxpR8FwfdmU9Plm60CZxJ2H_HGVeLcPv4Dd3dIG600Iq-KvB8J80W-dqXPiIEKrKhGoMmC4SzkI3CSOxMCarFB7sk3Ry-pOOw3CJ1lSsuKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYJ3JILa61TeaJJ0rt51Fu2f5qjzkIqN8jpgNoF32sKMHHOWq-khZva4m_GRwHGNfTcHvgi5T6IZRGGAubTZX5utef3RizVkr5zEkOQfh4iB8r-x7kJKeQqZEHvh8tWOeTRuTr97pI_AaAPqaHjTPmT4kpsVU9Zp-u7ioktl8pi1HiHdOcNsXrydAWyUQeZA5sMkfILar0oiMOlH_QBeRWcuPgQuxmJrW47z1lpzbQ0oDdtRG3J7m_HpNRv0cxoLaBL5DWEERp57FGPdza8jKoGYWHbzF5S9l9B-CDA8YD_Ia19OFkp64M-57nNNvueGUg4zUDf7RKVelwRjl7q6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=UKFXPhHk91VxDbH00gl0bMrlVicWuoMWkDhbtkcPcBc1U66uCA9qXOb_X3ovHYyATa7WRdTVzWQZT9Jq625FUOOqFR3STZmSlrbXSr0l7vWUWi2z4IPfVemeJYCsLO5ils7uuNof2Je9pJ_D05zr3gcfQbE2KPBVt2bMX4vr1mNMhj_Fm2zvEGGyS0SCX6L8YZLY9LpvBuWnHQznrTNQaTBNy-Lv7JQ12G9siN0xI0sYZbMNvwwsvBVZJANHT-POn7gkI4gAvBJ7DMHV4ExJHBneG3SC_9tBnAXqDnj7Xthx7jT-ihF1z8JlrcuFtPMUq5MiFleLn5vFj9ZPjAqWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=UKFXPhHk91VxDbH00gl0bMrlVicWuoMWkDhbtkcPcBc1U66uCA9qXOb_X3ovHYyATa7WRdTVzWQZT9Jq625FUOOqFR3STZmSlrbXSr0l7vWUWi2z4IPfVemeJYCsLO5ils7uuNof2Je9pJ_D05zr3gcfQbE2KPBVt2bMX4vr1mNMhj_Fm2zvEGGyS0SCX6L8YZLY9LpvBuWnHQznrTNQaTBNy-Lv7JQ12G9siN0xI0sYZbMNvwwsvBVZJANHT-POn7gkI4gAvBJ7DMHV4ExJHBneG3SC_9tBnAXqDnj7Xthx7jT-ihF1z8JlrcuFtPMUq5MiFleLn5vFj9ZPjAqWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmFxXpnUUoKE20DtDhhEcTmOXFjaRqj77ajlCfN950SJbJUO1ZB3Dhi0exIhOjgi9gF1ZKWLxlHmFQhUNS6G7JZW9CRzHGxAZzY2PKeoTtBthmA7f3c_VCKjUdMi5l2He3_ZNsaYXHP1dLkqyClXlMxHEW9p_NB9ci6O972n8SZtau0iuuG5s9jXaRJuS6vXlzw82WYDhBqMvzdJJxPiv7kVRgYHmYAbw_V7M3w47SsVZlP780DuamAtk7HQB-IRLQdUknbNS-rviypGjVwSGfsTJ4m5b7NSJBvJR6SNuAYr6wa4djxn1Rx8xliQbJSkm9PZw41udJena-WHP9EDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H71Y0-iS856cAz3eWWG1rdY2wGERF_0Rf_AmQYyQJZFmZAFnOAShK5dYBRX1MU5bTdaeNEBpJd1IRAZj8VSrBxOR_zZ1wxYu63cB60SCo4_OdsjJ388hyp0SNdrrZlnnxISVZbwvJIZucvm3FnDU4EQ7-X0g_R7Y25rIcL5E-6JXeHrubyp13o8O09WTGnUHTugOp2o2wYujmPjBjpUXXA_DUN2_f4FlxPZWCd1-2XnhsPaZt7sKj7MASDLBrazSEZMLpD6a0CV6gSouMdk_d2jxoduLe_PgfShWHif6NXXmAwdXplVLzeowGxfRMMEwAhdNokrvJGWzeS5RreMr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV1zVnnCtjrgXqXrZk-m8AyZp3i-Eee_VDtBlSMAbMo0by9Gv2liYqROpDD2fc15ry1eQgpWExaXJrqgwgxMjWU3rnnKyEA0W_J1I-bf-_eWrqg5RAmMacT-6RQdNMF8VREjXMjef7TH0BzPtk32_-p7rk46Ao2H0B7n80-sMlP_Yn6VkMwZ1MFVs9EbP6a6Krt3edAODj0nKMCY1WWaNOKiIoyM-aP4YRFhl87ttoGHZSeHqaKu9XUEnKpcGGCW92kyFGzfkHjBuihZa8ybQP3QSIcCZwbCUSKoc4rvUXrpwG5QF5pTXpzV6FUTOT8ySHXim9pRec0afvOuuNZ8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfM_ZbJm4p47q46w9oC9FyRvas7B7TpLIghyJXSOaMvbgvJxJuaMgHUrk9cbNIg5xVTl-JoRdU-m9NxRsHMa7HESyHUsrbtWqZA-r692wsCChzA6-Ns_TuQtuxceqqS1ucF6SfzlhPrg6N4-he4JZ2hrU2tKBiPtJOqv3Nk0AHaARBbeqd3yek_0uso6ZSDxU6eZJDssIb4VvNJeiOLnQsH1Pbow4sMjbY0iwMQ9heY8nKmsHmu-CPPzcE4eoHGvQ7I9lYzgFlDm_rRJjFR-PeEbi4uvj9rRCvXPfmZ2-ELWhiqbt_k2pezXbeiJrapDJUGn8vyAdiZHLJzBoGSV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBKOoVNAmvw7sXtsMkwVmIIxyM0uW0ad3nzqR9CckCu3ZJ4eHpdwl0mvtoMLoe6AP0EuZLB9vG_EsHdKZj7oQfUKqBK2b_HXQDnDHg_5CP2lzQfIn7LXPTJFM-gFJ66mTiSLCp0ofueAlXKlL5c2rZriUu9JkjZl59afn3wC14qaa57dXg8l4aeS0U4bJ1RdCmtGlUxl1Rrmh6tKGTcaQHA6-b17xlJoUWzbw8PnnU96SXnysIUVyUt7JEXhprKlfdKEXgqqUMuS7d80Mpj-0gyKgD9bUobxDewzYV993Rin12K93bi9GBlnyiKNm3LX1di2FSinWR4kV-cb_2ZEVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKX7dkcHHgA0Rf8HlX9LRp3VVPyvGTB46giViWscE9VevDVrau7Xxx6M_bn6IPwr3_yl1OlfG3aEeIoh3T5g7cWty2oG5IN1uJc7VNUHJ6apGwV3TjtJkKq5aFx39ABsi_OGWtI7iyLZdi86C7tnWlhgc6UpaCoLncoj5lRlvO7sH3SGv693g7tAIBADhAfewzJUAmjXoBGslViTCjlWzrl5zuJLRkLVH_aFE1IMH55y3lf7BhQUknJQfW8K5gh32xetYvgETXhaFCFKAwCQXYye6gD5ZlMlWje5lRaU4RxjOm5iWNuuRKDhigcKO7Z-AG9vAEpPkUvh8-ootap44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXefaws3B2O9LZ_mKfSxQF2DwGdkNuXTP1iOjwCtRBt1vYDleLUfwA63lenSLMU0zhJYfmxPVF_A2VXYiMPPB5ezMmsljrWj_JbIxFX6KDi2yxl5iOtF-7nOepN-EtbwfxGHfNhpN3fp8n1ZTxiqQbPAurfSWtl-wbCWD3LRK-36CGHjE_LtpSqNE336QrvH4sucyQci482n-ti9ltZsyIRge_jyfHK3n2EZDB-nUcU2XKAGqiovhBfkK6r4n0ejKFClcdHJ-biCkPXxZvAt98r-hsAkEEroj5G0sf-zfN3_WGQavrrRhZfHYXWG9nBIowh4MeXvuwuettGSnUOxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وقتی میگید، کصمادرت ترامپ "🫪" اینو بزارید کنارش خیلی بهش میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/76712" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بخوابید ترامپ خایه حمله کردن رو نداره</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/76711" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوبی رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/76710" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عربستان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/76708" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آژیرها و انفجارات دوباره در بحرین، کویت و اربیل عراق.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=KYrZTalBpsbkfq_eDs36MNPYB2oPbDzIi7O_vnF5AusjU-Heq60TJHTeX__hh6EdYHV1OaqzbSDHEG_F1ingi9jATmYfXg8f-B_8AC2L5WnyZCA5rGVqxWi0-awLMXzf4HW6vpinmYW_nTRrvEVqiV3M9Zf1-Va0WnvevQej6YukMcgH1d8FQPQvIvwIz9KKu8hKCrZKVpVmRz8c963L7h0y7TQgR3voeQuvPXA8XNZiHlZvXsLOpD0ALu6FXwN0hdGupB53QVpG6jNn30hqb9mxqQGgwNXlo-_Ks4HwqDUen18ZW-GuckpmyjTcGzaxWDM-RMDh6ub1rfg8qRTIYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=KYrZTalBpsbkfq_eDs36MNPYB2oPbDzIi7O_vnF5AusjU-Heq60TJHTeX__hh6EdYHV1OaqzbSDHEG_F1ingi9jATmYfXg8f-B_8AC2L5WnyZCA5rGVqxWi0-awLMXzf4HW6vpinmYW_nTRrvEVqiV3M9Zf1-Va0WnvevQej6YukMcgH1d8FQPQvIvwIz9KKu8hKCrZKVpVmRz8c963L7h0y7TQgR3voeQuvPXA8XNZiHlZvXsLOpD0ALu6FXwN0hdGupB53QVpG6jNn30hqb9mxqQGgwNXlo-_Ks4HwqDUen18ZW-GuckpmyjTcGzaxWDM-RMDh6ub1rfg8qRTIYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی درمورد روند مذاکرات امشب:
به قول آیت الله خامنه‌ای، دوران بزن در رو تمام شده است.
بسم الله الرحمن الرحیم
﴿با آن‌ها بجنگید که خداوند به دست‌های شما آن‌ها را عذاب می‌دهد و آن‌ها را خوار می‌کند و شما را بر آن‌ها یاری می‌دهد و دل‌های گروهی از مؤمنان را شفا می‌بخشد﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری‌های او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و گسترده موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را بمباران کرد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای بازگرداندن ضربه به ضربه، هشدار شدیدی با بالاترین سطح قاطعیت به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
هر حماقت جدید، یا تجاوز دیگر، یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌آور، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر می‌رود و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافع آن‌ها در منطقه به خاکستر تردید نخواهند کرد.
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿و پیروزی جز از جانب خداوند عزیز حکیم نیست﴾
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/76706" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سلام فعالیت پدافند و صدای مهیب مذاکره در بحرین.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کویت صدای آژیر خطر میاد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76704" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادمینای اینجارو دیدم با ۱۹ تا بسیجی درگیر شده بودن و موتور بسیج رو بلند کرده بودن پرت میکردن سمتشون،
چقدر زود قضاوتتون کردیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esQBQv7t--dwL_dLqsTSGKyFZ-Elj8AG8Wr4gdym8ih62g2kDFr-de6wU4p0uIa8BI42tfwcUCY0g7AS-CYtkSrrvjoql1GLYwnr4IAsgVFB4ninAiOoviQ5Kkyx6kBGiXQVQgDuHPDRB5XnAxUQsFPMHfYZWt0xtJJ5xSXKZ-yucNgzY2ml6GSR7jsJ_A0q1f_ufkq6t19XF_XIFhqVruqSvqWzZgmeQAR5oey8hrv-ZDf2zLbTE7slnzjbxD5t-ZQXYVvOD44-rnlsgIikF3qaf4mBc5Gi4oWdT389UnNKT21eKCHXlZYdVgHIMw2c7p0lN-WNwixmjCZzEEeOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ی اخرو محکم تر بزن، اِبی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76702" target="_blank">📅 01:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوتا موشک از استان فارس داراب شلیک شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کویت صدای آژیر خطر میاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76700" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXF0JPvFkpvy6ZCEslW2VmfCsfSt2DpY9HvLOdJfhTURyXoHUzB-3XG-a4aqfqTBLPVQY8pF7gQGmIyCChAS6zJlkbHuXQVrKA2YGKApCi4TX5FZLXCHMizLAzgYOXvnit3BalrDNmzJohnjJHZ7ZWjVtYYl_n_nOSHxZCmE4MQ2sEN1EdIt_cqzfh5NVK-Gmfke5BHdExvnAGyjcbluLnbrqJc4bKbqf3Hbm0yWqI16PYCcw_bHHrROmjNVwBjVKhZtN-_iIHIq7IeK0yLIZjSw84-LQqEjsstuAA0bSn9Y099WF9L-l3sk7lkkE-Ic2vA5MZyQBUfsWeA4QdNaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ مورد علاقتونو زیر این پست بفرستید، شب خوش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76698" target="_blank">📅 01:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دنزل دومفرایس دفاع راست هلند و سابق اینترمیلان به رئال مادرید پیوست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76696" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ننه روبیکا رو کی دزدیده بهش برگردونه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76694" target="_blank">📅 00:08 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
