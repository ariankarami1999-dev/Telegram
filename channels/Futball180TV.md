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
<img src="https://cdn5.telesco.pe/file/q8zVPVUVXShLXCAWqdG99yp4UpuOlDawOqsNDgFgaSMNrxNiceHGMjqkj-icXmX1Hv7kiKWd5pCHrMaSC5omiKEBSAjVXD0R8Q0XOCHUAQob5zY-gxUQJw2EndY2nZDDzUJgpxChmwPn8iuvpgxJTesgwzJuFk5wDGES30dCWYjV6_UHxLZ0H3YBGEEi3rLr-PlDGKCMUeQpGuLaIOHqAFvu3mMhdv1lI6GpjwdTZbxZe2sL85I_5YeWDKv4Ptfet6iVMz0bmT9u0ygJVd8erPsKtcdWs-nRFXVAkawezxUu23YR6aZOLkKhRgQ8Rt397QTPiz65CoX6RWao0GMYYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 464K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 18:42:20</div>
<hr>

<div class="tg-post" id="msg-103900">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گگگگگگگلللل سوم آرسناااال</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/Futball180TV/103900" target="_blank">📅 18:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103899">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=n2DUabW_b70MJ188SJ-dnPcVR8cdS_heLcRVLxgUeCD2_yw_azh-BkXyYIIigiXbVt3Msd4wPEw4cx8nGEmfyjoqSgoyi5MZ6BLcFK9vfezizCBn11E4Vj6GAAAsVwrXz8MzzKZPxObdyY-nO-HVnCp8S7HTfFUeqd-3N5x0s5H3aZcM54BsytDso1N1iJEIzouby8Cn20IXE7yUCESog-VTA6EfMYokDqh-yM28USqLmFgct-SSVu7tzeKRClT8_Kk6RyRfsDggqS-y9w6JiiiQcijImMGe7D_ew2gEDDc-_YLLu9qoEdEd6Prj1cy9WmznSU8ZQKpNzmyzT-_MuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=n2DUabW_b70MJ188SJ-dnPcVR8cdS_heLcRVLxgUeCD2_yw_azh-BkXyYIIigiXbVt3Msd4wPEw4cx8nGEmfyjoqSgoyi5MZ6BLcFK9vfezizCBn11E4Vj6GAAAsVwrXz8MzzKZPxObdyY-nO-HVnCp8S7HTfFUeqd-3N5x0s5H3aZcM54BsytDso1N1iJEIzouby8Cn20IXE7yUCESog-VTA6EfMYokDqh-yM28USqLmFgct-SSVu7tzeKRClT8_Kk6RyRfsDggqS-y9w6JiiiQcijImMGe7D_ew2gEDDc-_YLLu9qoEdEd6Prj1cy9WmznSU8ZQKpNzmyzT-_MuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
امیرعلی‌اکبری میگه روزم نبود بخاطر همین ناک اوت شدم. ما که نفهمیدیم روزش کی هست
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/103899" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103898">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6oj6cKZ8K2RVchCMJiyn2ackZGbwA-W227vLvvXh2hZQ8Jz-wbcAse5vHHyRrL_OLXKqbdGQ3lC8PJVccaxlzThHhkPx0TAZYt9HyeUqKpDRRd0Dnf0_RXFGerf5lq2Xe4RH4xrXfMwUIPFQiBzxNoUc-5T7XyygaExK9Spvhj9j9hJ4EmfMZbYFjYGNfcWEw9DIosoKmtA4OWWwmPXCRLZ8_q9vuxw99wem8YTHdPQQz-e3BBnnEpLgffi_a3ICWE3MPBpDZ4NAfW1Z_w7r1XSENTdxpOCnWEUtiOH5IEFv14V5sU3ly8v7RrKSRZn3rBundQwjasc5NvbLi_BzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام اسامی داوران هفته دوم لیگ برتر
🇮🇷
🇮🇷
استقلال - نساجی/بیژن حیدری
🇮🇷
🇮🇷
پرسپولیس - اس‌خوزستان/حسن اکرمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/103898" target="_blank">📅 18:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103897">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=SphXLZhiSQvnhmHIzDhZorozf_1IOqvr3oxUxYbNkWSgKkn3udornisvCIUXaLUgzgBFNumtCXVg2Nb7rYQ3mrqLE8zKR8rqvi6po4f98y1NGebQR2G4AeaP37mkxWDgtODepXfq0YllyATNN3YakdBW25u0-1GD6C7mRxNfIzwH5nayYFitmk-I1BMylnpWSUBBjzWGSt1RQ3l7jda57KZvJnM9s8A-foRgu7lyXQ0G67v7BcVpuU9isAX9U9WI1NLrGAC2Fw-3pqO-bZOS5NXhx0aEQCn76QygsapXCh5Qp2uVNxGS-Dvd75RzRjMNBApTQYC-sBwL1kVyDnaC7S5ionPV1OFLcYn_4Af2sT2LeO7Tm40Ztt4Zf3H_yHWku8yDuK4UwP7Ewu0rPuAMpQ2SpeLYLq36QsoqHfSnk2_eUYnnD_htkfkrIqBzLQtbvOQUvGep9prwttZC4W_4-2ssJVt1qcwMX2v65XlMJC9gW-YT9dlPK2pjZwz85a-1QFNclSBTlAQbXcN2cub-5HQN5i0YRFRR4W6D-GZsrUg3BcR2lzEs7Jz1AmpOU8gz5EW9VAiYr7_vD9EttxxjB6baxn3gOxD44dwVn2v1Ue_xPd0ZpgUFmgypsxDIur16Q8dnrjLF235-MsD3ief8NCUBe74wkRiJL5gDe2s4x8k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=SphXLZhiSQvnhmHIzDhZorozf_1IOqvr3oxUxYbNkWSgKkn3udornisvCIUXaLUgzgBFNumtCXVg2Nb7rYQ3mrqLE8zKR8rqvi6po4f98y1NGebQR2G4AeaP37mkxWDgtODepXfq0YllyATNN3YakdBW25u0-1GD6C7mRxNfIzwH5nayYFitmk-I1BMylnpWSUBBjzWGSt1RQ3l7jda57KZvJnM9s8A-foRgu7lyXQ0G67v7BcVpuU9isAX9U9WI1NLrGAC2Fw-3pqO-bZOS5NXhx0aEQCn76QygsapXCh5Qp2uVNxGS-Dvd75RzRjMNBApTQYC-sBwL1kVyDnaC7S5ionPV1OFLcYn_4Af2sT2LeO7Tm40Ztt4Zf3H_yHWku8yDuK4UwP7Ewu0rPuAMpQ2SpeLYLq36QsoqHfSnk2_eUYnnD_htkfkrIqBzLQtbvOQUvGep9prwttZC4W_4-2ssJVt1qcwMX2v65XlMJC9gW-YT9dlPK2pjZwz85a-1QFNclSBTlAQbXcN2cub-5HQN5i0YRFRR4W6D-GZsrUg3BcR2lzEs7Jz1AmpOU8gz5EW9VAiYr7_vD9EttxxjB6baxn3gOxD44dwVn2v1Ue_xPd0ZpgUFmgypsxDIur16Q8dnrjLF235-MsD3ief8NCUBe74wkRiJL5gDe2s4x8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/103897" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103896">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/103896" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103895">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEkNGtnaM_SMUnLQYuAy93M0niQgphj1f2wa706yqqciusAbhBoDFU7qy1D5aWZUoF-TedQxPvPSzCzsM43QYZyessrfs_ARGOm8WuyZq71yHtc9vUV32iSmOEH1M492LWtab5CluLPp4Tci2LlT5x0jtFLg8hmR3KuH0netyAfzUDvcFPzQJ9vob7SzLnEfSzmjz25w1mDDcc6VtxduJxKD1BMUG_T_SCfjpuDHutOkNkBCLO2Y9LV2p0zM0WfavG6XfzEOQJ5ZdjNV36jiIcxZQ9TQ3D-awDJKAYOK2zpq7H_xnREuiIkKaqtHpAQUT2AIenavDoUiWMNgPeD1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g25
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/103895" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103894">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگگلگلگلگ دوم آرسنال هاورتززززز</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/103894" target="_blank">📅 18:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103893">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=CgK-wchzeemHv1dd_U5nQT1E9rHpwFKz3StlsvV8NNbAsZNYejidu1SJNHsFEhT3IJoxlM0wa0kSB3flIKVV586VQ-6yxvzt62oo8dxEwC30PzzElCrRbm3hmEL-Jw9Jh-GjsQoXqM9Ru3luin7T8xjhfeM7UCks3KlLARPdNPWfTA7pmS2WO3rLGNIveo-jLG9YKG8TiSD79qHlyiyeOyAciKT8hA0KaRJDuyPO0_uGWWC52foGyeL2hLrSGeFleA1eNgCpUP4jMBkXqi2ohpYGqIktG0EpSem178scxf_cFzlSRR4mvrP48xkt-YdB74AhQkOhFeAJIJkeQ153Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=CgK-wchzeemHv1dd_U5nQT1E9rHpwFKz3StlsvV8NNbAsZNYejidu1SJNHsFEhT3IJoxlM0wa0kSB3flIKVV586VQ-6yxvzt62oo8dxEwC30PzzElCrRbm3hmEL-Jw9Jh-GjsQoXqM9Ru3luin7T8xjhfeM7UCks3KlLARPdNPWfTA7pmS2WO3rLGNIveo-jLG9YKG8TiSD79qHlyiyeOyAciKT8hA0KaRJDuyPO0_uGWWC52foGyeL2hLrSGeFleA1eNgCpUP4jMBkXqi2ohpYGqIktG0EpSem178scxf_cFzlSRR4mvrP48xkt-YdB74AhQkOhFeAJIJkeQ153Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
سوپرگل دیشب ژائو فلیکس برای النصر که رونالدو از روی سکو پشماش فر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/103893" target="_blank">📅 18:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103892">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648b67b731.mp4?token=hfjwdVTez1M3KGhqRYi9WZq_EpYnk1o8TTXzcEEWghe6v1TKL9fhn-8Idh40NJ07an4gocEdxbzlBMMs2SxDjaMTSWk4utWP_ezTeyNtB0vthubii55rpPO1A0UsxmpAgaP6_BltpH8gnt1SwYNNgTz6LD2nLkSE4JCvGJBV7Kcfdaz_vuGxkV8igGUdkPg79-wsn4pModXF9BpZY3_qXZnePwLq2Jc6YykbgB6bfUS8l1F7iewV_sL_eDlRIdjaRbU1G-h8-WIEzZVKLQKz8GI9x2KvBBfZ_C303K2JN511CmD9-3edePVqiouC2mvmwW2A8hFeHY4UspENQWtmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648b67b731.mp4?token=hfjwdVTez1M3KGhqRYi9WZq_EpYnk1o8TTXzcEEWghe6v1TKL9fhn-8Idh40NJ07an4gocEdxbzlBMMs2SxDjaMTSWk4utWP_ezTeyNtB0vthubii55rpPO1A0UsxmpAgaP6_BltpH8gnt1SwYNNgTz6LD2nLkSE4JCvGJBV7Kcfdaz_vuGxkV8igGUdkPg79-wsn4pModXF9BpZY3_qXZnePwLq2Jc6YykbgB6bfUS8l1F7iewV_sL_eDlRIdjaRbU1G-h8-WIEzZVKLQKz8GI9x2KvBBfZ_C303K2JN511CmD9-3edePVqiouC2mvmwW2A8hFeHY4UspENQWtmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به منچستر سیتی توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/103892" target="_blank">📅 17:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103891">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آرسنال یکی به سیتی فرو کردددددد</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/103891" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/103890" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103888">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcoa6bEzT5WDhopbW9TU2WxkzXLdkB2HdOgfcYdsMWVNAW8VX-6u4OZxOyCK-mnugcML7EpO57nrBEp2hYXd9TDGBNZsvxH5OKhNGTIgNFcT6RuKxs-p3DCl9GMSmHxVFqXg-mhTAQXo4_sd_0w-NYkw_QMWeB94O5XDUkbnC-HPLMNbY9J7KzuTULGc7PHvseSOJTtVumiJriFq4F_HeDynmL32Kte2OJ_-2H_3GMO06HMDuFxf1xDm4DL0tDPHcpvpPt6zsUTQ8r6HzekSxWwGCdqoqICYlP-z2Zsw6AnjufpiFnNCUrzMEROwdnQkxTiLYAodysjmEeBIBPnFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZnzkiYKhhSExkT0A5EuwOtnCRq0_nvNxsCgQ2kPiw-32e3BKrJMQV5oF6ai0URjGj8TW6sMAKrm9TtavBewOj5U5GhzrjdHPB5DqxigMFDt2dXJZtx-GnafO22yGFVO8iiRTduMIPOGbdM5wVn4fsPoO7Lxkokk8qGDU5A-TWciHqfsv56ZCQjJALDmtkSLrJ--sx_HSia7gmBgVcOalvsDDekx4hXpIDIYw4GLHirc0QmDMTgFiUiDYS5w7NnRTrz7XlIR5K7JzVeuYnzMfjxD407V0qou1RWgj_8r_ULtdaK34PueAF1ybGGCnOtXd1rlgHLBPjld7ODmmYXKMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب رئال‌مادرید و بارسلونا در بازی‌های امروز تدارکاتی مقابل بازل و شالکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/103888" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103887">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ZGTYw1N6l89H7zfW2RYJSxszfq2E_ZNwkE7xrl2N0Q--GX3tzFCPFqazNiJixmbuY1XiOQ4nfA_dfP1yjiLNNjmLReWcTmDKQR8SjJka26A04rqkd0rcmk1m0oibE2G1u1jtej8O1Hpe5JN55PbhgyVPJhWT9Z22G-b9KtokA6tujH1gOZ04ANOizOua2s-0zwz6CZO76x8-0S8QjtNBZ6AEL4rDunm_FeaYdC_-uXpu-cpokeMwXVNOU71PIzSmPJp9VkJ_Da7twEXsX1RnKHhrYwu9XQ3bwLYrUacZRJ5DNSTFlq1FSGcT-Y0MLlYaKkE1wVgaCl20ERd2oTsICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ZGTYw1N6l89H7zfW2RYJSxszfq2E_ZNwkE7xrl2N0Q--GX3tzFCPFqazNiJixmbuY1XiOQ4nfA_dfP1yjiLNNjmLReWcTmDKQR8SjJka26A04rqkd0rcmk1m0oibE2G1u1jtej8O1Hpe5JN55PbhgyVPJhWT9Z22G-b9KtokA6tujH1gOZ04ANOizOua2s-0zwz6CZO76x8-0S8QjtNBZ6AEL4rDunm_FeaYdC_-uXpu-cpokeMwXVNOU71PIzSmPJp9VkJ_Da7twEXsX1RnKHhrYwu9XQ3bwLYrUacZRJ5DNSTFlq1FSGcT-Y0MLlYaKkE1wVgaCl20ERd2oTsICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
عملکرد ابوالفضل جلالی در اولین حضور فیکس در ترکیب تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/103887" target="_blank">📅 17:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6927287d81.mp4?token=hlveF5DQHl2Ddxfm2-BNanRqqBFvkm55WTAtkjONP-c1wXha_v2sSdK1ybaud8yb0Zxd52R9uhgMfbrRPqroKAJab7tITknOGAhT_vu2T3CCeZqMjPewgSg_87BVOpsMcp2SVzF6JGDNL1PeH__VnmiWMkIDrlc9nQoQ1uNfxiX1ENrIVosoZfT3k-R0vUJLhIV_gKfjS5epS8_7TsAzChdptvQguDJgp5WHF8g97zq72jzumS35uH9eXMB99wdbN18B9gbayigCh7hp5EoQNVXDJMfMit0hdOGJU9EUTF47t1uATqh26kBBl0aYt9gTckDa1V-8avzyPeUbIzhI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6927287d81.mp4?token=hlveF5DQHl2Ddxfm2-BNanRqqBFvkm55WTAtkjONP-c1wXha_v2sSdK1ybaud8yb0Zxd52R9uhgMfbrRPqroKAJab7tITknOGAhT_vu2T3CCeZqMjPewgSg_87BVOpsMcp2SVzF6JGDNL1PeH__VnmiWMkIDrlc9nQoQ1uNfxiX1ENrIVosoZfT3k-R0vUJLhIV_gKfjS5epS8_7TsAzChdptvQguDJgp5WHF8g97zq72jzumS35uH9eXMB99wdbN18B9gbayigCh7hp5EoQNVXDJMfMit0hdOGJU9EUTF47t1uATqh26kBBl0aYt9gTckDa1V-8avzyPeUbIzhI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
تمسخر ۵ سانت و ۱۰ سانت امیر قلعه‌نویی در گفتگوی خداداد عزیزی و مجید واشقانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/103886" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103885">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5zXh8-qGWsxccOao3MZK6jeL6POYF70YibiQQGCu4fU_b0gkhfexP7GTsDnjs7nL1RLfI6-uRem6pJJc3J3M_RJwGtaYfK5Wt_TMgSRMlsjSkv1ruaJETnaT5t4pRTHKH_p0dzQ-qmyppP_Xp3mLBH9zQW9_q6ZBzreor7o0xnpj3jPkfBKg-yIPkZvRpgxwAkyLRNUs99Q-ECrMPoN-YxZEK7X3RqrRXyqFEsDpHEgLSI1sGf_YK5q1oBjlbJn2rvrklhhrLDBxR_4yJonvYGxxfcyYjEvsyRtpa5CaJVG8eWPV8NVyUT1akPDlCPhA8YjBAjXncBpf8vWS6fJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 مسابقات اخیر بین سیتی و آرسنال:
آرسنال 2-2 سیتی (2024)
آرسنال 5-1 سیتی (2025)
سیتی 1-1 آرسنال (2026)
سیتی 2-0 آرسنال (2026)
آرسنال 1-2 سیتی (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103885" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103884">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=QxpbyYIhHLe7iuX0_6sxXMZjAcWRWnTcbqPfvfiY6BzIW1NVn-HHTfXhVl90tAJK595FQqU6tLfAI9XZjvE4d2gwz28N9zkpTZti7kavMB631ogyaDcZRzedYbRV3M_396AfeWVstbHXivpouFnJYca8maTJnNPmyG7Qhi0KYFaXxXAT0RtHJRxPhjbr9S5xhqcJjgQAEIlZmxDhjbWdeNx_osOckQA4vfQFokbiNoQnHO17UBpK7YoZ4HpDGEO3AI8ljclijC87n6-S-tTPa49TOHMmoZs3tjLNr1lgOmiFhsDu2ZfBNPJh9N35AZrihLXVY_2jjLr7X6CZLKUq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=QxpbyYIhHLe7iuX0_6sxXMZjAcWRWnTcbqPfvfiY6BzIW1NVn-HHTfXhVl90tAJK595FQqU6tLfAI9XZjvE4d2gwz28N9zkpTZti7kavMB631ogyaDcZRzedYbRV3M_396AfeWVstbHXivpouFnJYca8maTJnNPmyG7Qhi0KYFaXxXAT0RtHJRxPhjbr9S5xhqcJjgQAEIlZmxDhjbWdeNx_osOckQA4vfQFokbiNoQnHO17UBpK7YoZ4HpDGEO3AI8ljclijC87n6-S-tTPa49TOHMmoZs3tjLNr1lgOmiFhsDu2ZfBNPJh9N35AZrihLXVY_2jjLr7X6CZLKUq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان خوش‌اشتها
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103884" target="_blank">📅 15:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103883">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=KK_5J03YoZiD5ESlouce6hd7vH7ADwSrvzjEdh0xyF9vA1jAdGUJWExYEKTvFIeNhFvue67F88jOGlmSk2Ulh2ob0P0Ll442JFw400gXRxRx-_tCS_I8Lsu58__I_sr73B6o8HiUDOXDiFA9ZvRtD5hWVNY2yEJHUcIfiavChT0uqZcvscEuXiv6BlYdtEpkMMtJaCcKELo4qMXrTPC_KV5AtQWMD5TLsIBIH59m_3711KDZssCRUEaoHdlqLgGfmXYZg_pYv6LvIvya8AfZtTR4rBEFReIU_jwd6uMjubpGVOifCGk7sREgxbxcRyskNvaTga90tzIgjt-Jy1QS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=KK_5J03YoZiD5ESlouce6hd7vH7ADwSrvzjEdh0xyF9vA1jAdGUJWExYEKTvFIeNhFvue67F88jOGlmSk2Ulh2ob0P0Ll442JFw400gXRxRx-_tCS_I8Lsu58__I_sr73B6o8HiUDOXDiFA9ZvRtD5hWVNY2yEJHUcIfiavChT0uqZcvscEuXiv6BlYdtEpkMMtJaCcKELo4qMXrTPC_KV5AtQWMD5TLsIBIH59m_3711KDZssCRUEaoHdlqLgGfmXYZg_pYv6LvIvya8AfZtTR4rBEFReIU_jwd6uMjubpGVOifCGk7sREgxbxcRyskNvaTga90tzIgjt-Jy1QS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشی داره تشویق یاد میده یا تقه‌زدنو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103883" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103881">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXwNWZBLKZvmqIfdCcT1wCqvJsYUbz3MbXa82NoNvRJ_uPxdN9PY93tEGv_gjY7JcbW4YTavPCuB1vjz5VXPLusvnHc_L302qn2w3kC-Rs2vaE-mJeFUlodgS5adM7XKgivMOZLyPaJpAZFDdR6J_wndl5kYdWoY-33TqIhTi0dHJOkuXQMxgW_f5yZJZ9g2T68zn4GmM7zT6oDpbF1ux-OI5qQ48uM00Jjs7qdJE5AgRHVsw13QEdODlq35rnmCizWpm3TBX0ZYS_C_GQMp8L3LVbsiodXsHnNPPip3DNQyYLki2fwxJZkGZYMn_BKxHJMEs_uCpxUXFEyOU81ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q64RpEwc-qX9Tx83C_0RV7yMxzjC0fk5lXBlEodDer2A2kq7ClaZbSuIy3aqTp_59FgkBwPlnIbYrKvSyxBscg20QrfqlveF7dhfeuKssRIfZWJL49_b-QbtxyCLbDs9OI3xPnfRcYmfpzQtGJuUTdc7iE-AWMZ0EZn8AkF5IwDmHtwGxQky4JW_20-HHmcCTNLQ47LtSIrDFAFS2CqfqzV2BHUUwkl99pK5YxigT1YXc7Swc7U7LsGAFfgAta2HX_F-gqFDcUlQtu2XWb22Gtf-ety_I8U2VFcvGHbB31qZJCi2KbrPnrHw1x4rdORAz_oOpO1Efr_9c34UY-S7Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😐
🇮🇷
عباس اسماعیل‌بیگی لیدر پرسپولیس درحال یاد دادن‌تشویق وایکینگ‌ها به طرفداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103881" target="_blank">📅 15:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP311GYroWRpguZ4PY65duGFF8Fyo98ngzU7BVTwQd3LZa7la8CzOwWHBqs_bawPgBkjcnA9feOk9m-IUnymT-j0hbtupp9axIUv3qox-H0HdcQEvO5tPALRbjn50ehcwdPFkCKCGnIw0cR4s8-pJ-OuS3K5ASZUIy1fqUTn0ybN1IZRVLcD-FCQpFbRpmi4HeyoUs_iuQPNQ4CgfyHpZ1DxSLLcFi2ZNSL6r9kZ8izXtXCloE3Av9M1r6XuE_PxNrhy34D3KXNOZL3CH8p3Tpbx-Il1sE4Qr2bgR9ncM9Rtfjcw-lQ7y5wFM3Hlu0gUjewsywcQRpFAcQ-HQv4z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فرهاد مجیدی پس از گذشت ۴ سال حضور در کشور امارات ساعاتی پیش به ایران بازگشت. مجیدی اخیرا پیشنهاد سرمربیگری تراکتور تبریز رو رد کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103880" target="_blank">📅 15:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLCwaHbFxaBrkSbJA3MEbadhyC3BnjW2g4x5EKYQTexNKqqNRL9H2iAgKwO2M6P0XKah-4yb_7vSvliFJqono8cHzYey3uf805I8CoYM5Q7dkPsM5S01smlrL7nMC6k1qLfcf9V894FqCwamiigt0kaZ9jT3Dv34gj4uerg7vSdOp3l4Zdq9yl_HtZrntMS9YTl0cJfNui1bOPDjNTkc6QJSPSlokCI-2JEJVGW2mOqwhLBQHu-LBBdxxph6e0wtmY4MrSdRvEipFCHJZm8_-urVf_KyCWbeaa6yxgYKDnRrOf1j1a_SxXvrqbFoZ_nT0kZxML7G5T4QNUBIL3SQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇪🇸
#فوووووری
از متئو مورتو: ژائو کانسلو با عقد قراردادی به بارسلونا بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103879" target="_blank">📅 15:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lu-n3GUMsf4RsZr2ptxlP4lMfvRoEbkItIUp9xRQYQq8VLw3T9C2dwVVrHdihWYaog9fNCjs2tCgbvlrUJoY7Qva2CW-DrAOSn9SqUi7NO4dG4RA6ylfQomeWk268473uKRYJx11td2aFp0soFFmE7xZ3zNiNkyk9Mz6nWwRB5m0vZ7sOLvNpuOSTws1kCYm3fCAQH8RZJ5z52Faqe2tR-iJIslen8FZPZvIbdVqx4z4a792JbSH60RieQdFXlaYihW8cMrARIVJ8si1E8oIc0GWGdGT9t-Krywoh0CxiUDF9HNUAvvW1HkVkR5QR6CvghkaeRsHmtfP0f3Fou-e7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCrt7mDL34hsBaOkCUX3_JtMsyt5KYsGu2Ac-zY1q_zectVOSyhQkRL0njDIzFUT8G940fClGihBuFUQR3ukviiIqAMewlA9kiHa87xguTEyRORKrgUlNvQQ73CJ16H1TaFn-k2BUqISbT13OH2FOL-2EYaibdOI8-ggJq2iIWnfn4NnG6jfLoSKOzZy64lgjYLmRszRfZDwZHCP5GJXs4CQJ0GiwMbPBpUapJvuAJYif1cFqspvpKC7JxUcBdRoUacD7WreQY4C4IzawMrfoaLcrT0N2weZlm8IfdI5MiYj4YsheCLbg-aGW-NmR13ntBKcl0_lDDjYzS2ovZUmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezsXJ-qBUsXr6N72jx76GpdYpfTytCbsckW1wbJL75NkvcR0VsLceSBWnIdEQcyj5qgTFB5nvawv55oLcyqNuqCHYi4mb5id8MSCIZrWakNdjnWB_cowEfN7r6LrmX2RaYTozQL3In4ILRpe_xm56UOZmNTqJTLByxJvaSE7QA2ITTnzlGPHmfPfr6aWcWQjFLsnx-k15m5EQCK_r3OYBLjVJlkUwCB40DVYAo3DSYyv4vV7ZN_QfVb5LJ9vfmOg6mP4Pp-KgV-vaNEJCPAnYpAVY0dxDA-VzEKMWAJt4m0gUYUkPKo9Pvp8KL1goPiXxgkaAo9ZHKWyzC4tfDleGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103876" target="_blank">📅 15:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Wf29OCPSbsoilELIl4lNKQfrFV51lijmnUywExksZmqRMopBfQLE-b9xZ5ASK42v9qrpZMQ6sYcO_pDFYgF8Mae0JsPrdL792CdOfTt_gavNNwT7iShFzxw9KgV3ZNS_a0vH-p_DQHGfiQ0Ej6W5bhJwExeGuoBiP3bdFyNj-VjINGaQ3_YRzb3JZw3L29qgqjTIvps_WBR8Ad2UqzlXN73eStBGkudwRDmVMkIZzOmhqVvC56UNRJyAe-Zx8vX0mvVktxjzHt7L21HPweJjq7JECp4yh-nouyUYwaExLQqjyIPOrko4ULYOHrhSWAm6gBYnQPUVQBp_Aq6spZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
غیررسمی؛ زایان سوزوکی دروازه‌بان 23 ساله ژاپنی به استون‌ویلا پیوست
💸
مبلغ انتقال: 30 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103875" target="_blank">📅 15:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfdc09cad.mp4?token=UHmBY5R2wF1h5ll3YfkeF-q1ezm0Psrjt-v435LnyCzl4wr3WVeeNk5G2TYYUo2FV2oyNsIR6jUy5OP2r9QPC1NKwHZYT6eleO2uNwOvvnfE9vvZNH8wDDMpeR2IDQs6D5x70Oj5g3D29TJjID5yOXfu6T2iUHOU7QcKEUB8-JRqW7baKVhJyb8arHicSyiaJUnG64StDbc4CwGEzzu852qLAj2APVMXzxdsn-XAN2WMjuYvhHGKfSKhaguR4YFQswpOSzHDpkjAu0GZc3lki0qtlHLWwLN6bic-QWxnCA7nXEs2QHPCLtTpdNF1YEsR3HYmslbc44RhQaPWBl_22qqzsF0JZswuLTh6U8Sj6gn5z9PxCktQVcwXmGd8WQxDW0OP5SoKHpjbyODAkD1_i0yz1axqeA1aXc887lgW-YGm_IX1MuRKfyGTxFTZeaiMi3hSwTHBAK4hUJL0AC0lOo89sCNcTQtutRQ0BZa6tEZQoDKwvplsZy7UnQW3V6ZyFM27FFdAazjhVR-FOirI2Hwq0R6j7sFA2J8qIouGYkY5ZE1nZfzPqLuxiIETirUsxWNAJwxLkG-jDGh3PU8iJ32alRm8RNlJCWJ8KGcZRGR0b-cyktwYlxAUAs0LB6bojK49Sb5nCQs-YvFKOR0vj6b1Abvt3TV_yPDknGzea1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfdc09cad.mp4?token=UHmBY5R2wF1h5ll3YfkeF-q1ezm0Psrjt-v435LnyCzl4wr3WVeeNk5G2TYYUo2FV2oyNsIR6jUy5OP2r9QPC1NKwHZYT6eleO2uNwOvvnfE9vvZNH8wDDMpeR2IDQs6D5x70Oj5g3D29TJjID5yOXfu6T2iUHOU7QcKEUB8-JRqW7baKVhJyb8arHicSyiaJUnG64StDbc4CwGEzzu852qLAj2APVMXzxdsn-XAN2WMjuYvhHGKfSKhaguR4YFQswpOSzHDpkjAu0GZc3lki0qtlHLWwLN6bic-QWxnCA7nXEs2QHPCLtTpdNF1YEsR3HYmslbc44RhQaPWBl_22qqzsF0JZswuLTh6U8Sj6gn5z9PxCktQVcwXmGd8WQxDW0OP5SoKHpjbyODAkD1_i0yz1axqeA1aXc887lgW-YGm_IX1MuRKfyGTxFTZeaiMi3hSwTHBAK4hUJL0AC0lOo89sCNcTQtutRQ0BZa6tEZQoDKwvplsZy7UnQW3V6ZyFM27FFdAazjhVR-FOirI2Hwq0R6j7sFA2J8qIouGYkY5ZE1nZfzPqLuxiIETirUsxWNAJwxLkG-jDGh3PU8iJ32alRm8RNlJCWJ8KGcZRGR0b-cyktwYlxAUAs0LB6bojK49Sb5nCQs-YvFKOR0vj6b1Abvt3TV_yPDknGzea1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
به‌بهانه خداحافظی چیرو ایموبیله از فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103874" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9IINhDIiUVNuh7T7ULcpO0k4VySOax1KNbEyh0TEsi4Qvge_EcZzR9Wif1xbmOXq6GRISOh0bLeE0-22huT65lUtrIw6Oi6VUXv0w8Pl8UsJtokN_PgpL5vwRIdq3wK1BCaRlFeVxfdAN41wOKqpMbro408674uogL0vFpey6voulmtpMzUP--OOrMj9A-n1JXU_nhEdFbOBcIu0uyCCX_vaWImOilDBktIdZaxmYAmCG3yv2entTis1xuhfZBYTfb3CuvROXQdsiiTuj16A0a3GdnuuTYLqQ5pr0nh65wj8eAvxc30-5rL6jZTbuoivSSTN3wKi9lPjiFtNZqHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار فصل‌گذشته دیومانده و آنتونی گوردون دو ستاره جدید بارسا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103873" target="_blank">📅 14:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794f2f910.mp4?token=qfk-xsT3tA89ZqL_MC9VZFGO1WxBFyzys_BJwYTkSw10-FhzlMMj8SfQcWSnOBaBGc0S5ONwR8BhkPOUZwk-0GhjX_YmB8KpLzG6GlPTWeSE8tf7lENgRvxn2L9f55TOmHqlW6Pu3lCmThZ9t9ct2ayIX0DWIYodjCcjQCW8nOrAP0WnOLqcJPJPoe2iksjVRuyi1e5r-s331Un-5_hGYdEYVRnU-wUzwJcvNr_vrgQVY1X89-e_7vQL08gWxQHMJPBfwJzQG2tk_jDUO0HN1xozxew_75ytSS7mV5NZ8rwg7MhPPcC-JM6GNuwJZbDA3JHSqwGiu0anuESz1oxocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794f2f910.mp4?token=qfk-xsT3tA89ZqL_MC9VZFGO1WxBFyzys_BJwYTkSw10-FhzlMMj8SfQcWSnOBaBGc0S5ONwR8BhkPOUZwk-0GhjX_YmB8KpLzG6GlPTWeSE8tf7lENgRvxn2L9f55TOmHqlW6Pu3lCmThZ9t9ct2ayIX0DWIYodjCcjQCW8nOrAP0WnOLqcJPJPoe2iksjVRuyi1e5r-s331Un-5_hGYdEYVRnU-wUzwJcvNr_vrgQVY1X89-e_7vQL08gWxQHMJPBfwJzQG2tk_jDUO0HN1xozxew_75ytSS7mV5NZ8rwg7MhPPcC-JM6GNuwJZbDA3JHSqwGiu0anuESz1oxocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
روملو لوکاکو: تلاش میکنم یک‌ماهه ترکی یاد بگیرم، سخته اما من زود یاد میگیرم!⁣
⁣
🥶
در صورت یادگیری زبان ترکی، این هشتمین زبانی خواهد بود که لوکاکو به آن تسلط خواهد داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103872" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32096c018b.mp4?token=tUQ-o1mC3cptjxmUZ7u2czr-Bzm06GEHxfRmx5ZS0wDX6mDLOpL5Gw5Ahx3IF_jTKqfnyWTJgnWA8US1yHGV-FZhJZ6kbXCDeB12IPUSHGCoOnGhSxcUbBxwoVtxgEWOGNXe1fexXSc3-StSd7Y0kz2dIkrVrtILcg6JL74JhH61lIfgc021F7zLlW9jg48ZXwShrqgGts_nVqqxlvtYznWEIck617y_By9aaiOGPaNfU_NLqEGLyi7XMC0ulivudLvi0_Cx3l9kE6iflpzVEB8KLjFaYDf0prU_b0tjwCFXyAF0PVArXcnd6Gm32851vY12skRFhyZgP55tiH4ajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32096c018b.mp4?token=tUQ-o1mC3cptjxmUZ7u2czr-Bzm06GEHxfRmx5ZS0wDX6mDLOpL5Gw5Ahx3IF_jTKqfnyWTJgnWA8US1yHGV-FZhJZ6kbXCDeB12IPUSHGCoOnGhSxcUbBxwoVtxgEWOGNXe1fexXSc3-StSd7Y0kz2dIkrVrtILcg6JL74JhH61lIfgc021F7zLlW9jg48ZXwShrqgGts_nVqqxlvtYznWEIck617y_By9aaiOGPaNfU_NLqEGLyi7XMC0ulivudLvi0_Cx3l9kE6iflpzVEB8KLjFaYDf0prU_b0tjwCFXyAF0PVArXcnd6Gm32851vY12skRFhyZgP55tiH4ajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نونو مندز یا کوکوریا؟ بهترین دفاع چپ فعلی دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103871" target="_blank">📅 13:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2353879d41.mp4?token=BhyBJZAc2VZi_9w4KsqshEEyu2xSU8kdvZI0i16DTrpVJRZea8kIJ6UWseBplxOZ4-0U7D-1o06eYdCKw-jzD_-Xg0MGWAL4XM55-0OzdAjQv3WuISw29kDBh0MN0VQh5bsqarcES0k0LRnCdf_5hR--8YT9K1gQr6hXgH5jT-8t21YkMCS1uEHPS_XbKs2ycY0czi9r0zXMI-ZPJGfn82A2zLrstmU3uj8qvuib0QazGqXVuJ4qNak_x5MgsQf6WOT8Fhqa7wJRBWIXNqx9OHPJAY507BiDPFV-soYDydQceeOzddxrQYuYa1vvXzdAOcExwm-nCt7oGKzjunwkjGKz5zKifiMIZ0nZ16WyLLSn499dF7KXr7KtnlWitIoqyRYHP6nHy62cnpwkxhfTIk3RnVd4awEjs-FUKQw8pwpC18dcA4aizY0QjBS-3NH8GL4WpVax5K1BrDfZGLhCCNLukt11SMLuDFh-jm2iT4BStp5TQuAtvkOFB4K34okzIZ0Jq6b21DOk2sDLWBRCUCBm8IFkQb4D1oIhuRQY5G5c61ZbIHNmyV2B6Ql6bBd8vC64YeY5yGmiw3kFdd0K5QQ8XXYmohgDbFqJJDJOSFmqUJrRreihsZ_sp6kFCb1coEGzFqqO2GVv3IyVvFweIKrfW00f-hzyo9Bzlk7ic5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2353879d41.mp4?token=BhyBJZAc2VZi_9w4KsqshEEyu2xSU8kdvZI0i16DTrpVJRZea8kIJ6UWseBplxOZ4-0U7D-1o06eYdCKw-jzD_-Xg0MGWAL4XM55-0OzdAjQv3WuISw29kDBh0MN0VQh5bsqarcES0k0LRnCdf_5hR--8YT9K1gQr6hXgH5jT-8t21YkMCS1uEHPS_XbKs2ycY0czi9r0zXMI-ZPJGfn82A2zLrstmU3uj8qvuib0QazGqXVuJ4qNak_x5MgsQf6WOT8Fhqa7wJRBWIXNqx9OHPJAY507BiDPFV-soYDydQceeOzddxrQYuYa1vvXzdAOcExwm-nCt7oGKzjunwkjGKz5zKifiMIZ0nZ16WyLLSn499dF7KXr7KtnlWitIoqyRYHP6nHy62cnpwkxhfTIk3RnVd4awEjs-FUKQw8pwpC18dcA4aizY0QjBS-3NH8GL4WpVax5K1BrDfZGLhCCNLukt11SMLuDFh-jm2iT4BStp5TQuAtvkOFB4K34okzIZ0Jq6b21DOk2sDLWBRCUCBm8IFkQb4D1oIhuRQY5G5c61ZbIHNmyV2B6Ql6bBd8vC64YeY5yGmiw3kFdd0K5QQ8XXYmohgDbFqJJDJOSFmqUJrRreihsZ_sp6kFCb1coEGzFqqO2GVv3IyVvFweIKrfW00f-hzyo9Bzlk7ic5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
ادگار داویدز: زیدان مثل یه جونور بود و با وجود اینکه ستاره بزرگی بود از زیر تمرین در نمیرفت و پا به پای همه و بلکه بیشتر از بقیه تمرین میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103870" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1863d1e5.mp4?token=AmKloMRaVNaK1ZpJfinyC49RGvyLmIrMaI-prIu-RCHafrDBPBdyHHXrOGITZSiFowWoS4aP6ggPmm1qUviEdbQtERe_YpbZ7LJGsp95W7BbNJXYbjxuQVIAkJi0kieCErc_pjJ2vWYcMQ_PnOSplRJwqLFAItKxTZXYearCWv_iSsZP34x3YReKzt9ycxUIIi5vIVA2v_bMFxH-MAY_kFgPRiXvmO6lzqZgBDJz-qdStQSme3M8dvnIutZlNVtLcrNrgnz0UBeHU0E5z7kAwQnydS-QJFWi_nkB9dAFcF6II2_1bxhAeuX0vlwNi8f8vOJXsrSy3uymG1Aqpki3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1863d1e5.mp4?token=AmKloMRaVNaK1ZpJfinyC49RGvyLmIrMaI-prIu-RCHafrDBPBdyHHXrOGITZSiFowWoS4aP6ggPmm1qUviEdbQtERe_YpbZ7LJGsp95W7BbNJXYbjxuQVIAkJi0kieCErc_pjJ2vWYcMQ_PnOSplRJwqLFAItKxTZXYearCWv_iSsZP34x3YReKzt9ycxUIIi5vIVA2v_bMFxH-MAY_kFgPRiXvmO6lzqZgBDJz-qdStQSme3M8dvnIutZlNVtLcrNrgnz0UBeHU0E5z7kAwQnydS-QJFWi_nkB9dAFcF6II2_1bxhAeuX0vlwNi8f8vOJXsrSy3uymG1Aqpki3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
بیست‌سال حضور احسان‌حاج‌صفی در سطح اول فوتبال ایران با پیراهن سپاهان اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103869" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3orUlFNxr4c_t8ZZecSDJuDDQHTP-U4Oe1NjSsKnwNKVthzJ8xhFowWJnGs8xFu6aUPUuWvp9n_zHggdh6zqydzpGP9xXRkwmhQipELx_J7CvDhvZoV4xNQnkSg_Z5Jx9Zt2c5c1BJUz0soSztjiCeOzh0Q396X5SmthEwU4usDiybnOBoqR83sWiFmdWLFY6Ar217ygRTQViRFsYlABVDCktduBArzBDFcOoOczWvgwoxer1PhRlOdGph8GSTq4uDC-PcvlMgUsLf1ghJ8J16Ql-IRE59-ir0btsh6nSxQB8YJkPTGrUDIHvBCfmXEGuIzgkK1rGx5ClEHoSD7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBJBxmQwcthv1-kofbrd3dGQUFE9taYpUmGP4eHs8PY4lkXPUc8l-WxRt2HIP0UV24vIX0Pu9iV36OYgrjFE_pVc0kRCD7y3oCP7AdIB-gaHBc0eZgRMdqk93bA9WdWCL5NiQ-mpRDDLAM4qm5WJTtC7iab6AUrxUAtidZlhRSqgjGyUe52PcyjVTUpkrMUILsuZ31lFlxQneGSCYpHy6XmERzYHQtMduzSb8i-FV-5CEqa5l-33FsdUpi0W2JV2Q9JrsURVAs9M9muj7Ra1GQV1JIeOZgx168YR7cmd3aL4ziutyYf5mXL13gFi4cu-kOliX6rUEh2koS95ID0tHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
اکس رونالدو خانم ایرینا شایک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103867" target="_blank">📅 12:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTwQvjb3D002nh1UzdW121jdSgAXOfqoCtrNVv2O_Mrbr47Cye-UmG-aKuhVIVwSLYXAkPTTaupaf2_v9ygQbVfqQ5oMFKkqbicS9CTsAzE-Iqv3_b2_uJbFbE5IGZ7K54k8RrZQ93TrLJ5YPe7DtdlCBempPJuLd-PUDD2vI9nVH48u--xEid9kPISf3rMMty78UeMckWsOyHw_p0K_vMKYtcoHeJ4_bwQGLaHkC_A61nHGrcHx_8o7_uR2LcyBI-wP2e8nlfu_gKuBB_oLt8X6OJ3PR-RtcrpBNeRiUyhicuDCCmMBL-zZmasH9NlffPGDjISGXkgDYWds5zmqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از نیکو شیرا: قرارداد برنال با بارسلونا تا 2031 بزودی تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103866" target="_blank">📅 12:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86eaeca4c6.mp4?token=C6tb9ZWcQfNKBHRcM32CVpffe_WBDe5PpKLq3I3PnQZa5egu7WxLmvVnk1noaEDSt8-w8vT4oZ0QVCZITZeSLzC-QvcFhksYuJkp4yEgpoP8bTenACngwYi53WgoQ-FJ85bfBvFIaHHBv2FYqh0ZHReg9URbhNCSmgUvjHJkYQCM0BPYFBF1bLd8Z7C52WTlt_WOTiAcTNvosG01bbH91vYcbKwXCzZ6rkIy8iBljTa4b2Y1OclQnoZ7MLypvc1ghpj94C9QjsymT3Hnlke0BbR7TvLmtudVPKCmAuIjqRnlnCFNWLotgmGZI_xr19W9h3u3Ai1PsPJG-uypxrbs1C7EIOolRA1GEsN1mQl79liESXN5PLJG8P3mQzBg4QvkoMigPOJNXprXAyiaG2aQ7LkexymKREBhUlnwuJbWLtR2qOzu3TPEpK-QGb-cnG1vv9sD4LNAHptpvt_6sTRyIK9KYZtc7HcyPBinURRrRH0EzGhLib0mGK9nA8bGjx0GAhHnhtPqtu0_Io33hU2RWbjIrI9qv4TZ6sffqRdrWj8Amhlc5qAe0Mpt146pV-tNYM-TKNv8UQ3StUi4gspJbOsVfeYDvPcVqPP1GSsQlHAuV8Jo8alRHsTrQHI9q_vyBYg9MfDaVfL30J78cCiPvm4hHb-btJe-Xyv2Qu-qOXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86eaeca4c6.mp4?token=C6tb9ZWcQfNKBHRcM32CVpffe_WBDe5PpKLq3I3PnQZa5egu7WxLmvVnk1noaEDSt8-w8vT4oZ0QVCZITZeSLzC-QvcFhksYuJkp4yEgpoP8bTenACngwYi53WgoQ-FJ85bfBvFIaHHBv2FYqh0ZHReg9URbhNCSmgUvjHJkYQCM0BPYFBF1bLd8Z7C52WTlt_WOTiAcTNvosG01bbH91vYcbKwXCzZ6rkIy8iBljTa4b2Y1OclQnoZ7MLypvc1ghpj94C9QjsymT3Hnlke0BbR7TvLmtudVPKCmAuIjqRnlnCFNWLotgmGZI_xr19W9h3u3Ai1PsPJG-uypxrbs1C7EIOolRA1GEsN1mQl79liESXN5PLJG8P3mQzBg4QvkoMigPOJNXprXAyiaG2aQ7LkexymKREBhUlnwuJbWLtR2qOzu3TPEpK-QGb-cnG1vv9sD4LNAHptpvt_6sTRyIK9KYZtc7HcyPBinURRrRH0EzGhLib0mGK9nA8bGjx0GAhHnhtPqtu0_Io33hU2RWbjIrI9qv4TZ6sffqRdrWj8Amhlc5qAe0Mpt146pV-tNYM-TKNv8UQ3StUi4gspJbOsVfeYDvPcVqPP1GSsQlHAuV8Jo8alRHsTrQHI9q_vyBYg9MfDaVfL30J78cCiPvm4hHb-btJe-Xyv2Qu-qOXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
صحبت های زیبای آرتتا در تحسین پپ گواردیولا پیش از بازی امروز با سیتیزن‌ها
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103865" target="_blank">📅 12:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103864">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGgp7u27LEjo8viTaY19GsaPdoEed1VuHiRrIx7-WN4jhX5zCVCyjPc7YrA8SxoWQJPgPqMjtOdJoe3nKqf1FxWHFoVaLXnjIk1D_nMHubYKNpM47j2Cheb7bx3GjFS5cKg08QOhnWdVi4W7-1-sLFz2RetPAL6sj8vjekVyraGyRUUlke3W8kkNJKmeYeD4uA1PJGGnD91TdcmiY152DdPyqnvN6PcYXzkcdL4s3vqGTwNYYlXzl1V-jjLVNFvcvpKVVEPKtfVEivIv_4EopvbaJMraA4QccLp-3SKnbArMBHqXzvRkI2s7gu8Z6fp5jDsfPX0vKzpa9T3U015xaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
ورزشگاه نقش‌جهان اصفهان به عنوان میزبان دربی رفت لیگ‌برتر انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103864" target="_blank">📅 11:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14206cca0.mp4?token=ePREXlvoAmpakuW5LZnH0Rw3zv_h8ds7-uHOzxFD02muMEhjm_9aOdLVmDkH6MhQ5Zbtte8MHOUbtkAHSCmtnM7CYFTVxDyUh8ybR9_3X-YNPjZVtVwuy6-jUcxRwWxxIEN442vwB-nKLYPlyROwKUXJuHkq_9LmFZUQAQnUeyWR6ieZRqTUX67BVuPsUd0xAbRmoft-Ig3SAzbR8HgsC-oxDMwh6rriKvpQQEn07LWAp2_d-i4XSWIJz2awNkns_ui8tPTedd9qLHSR5vwbOhO2gJYkqo5jA-ZYjIu7cWB3u0l0RNdSDygY54SZm8I9MLwrLmFzU2batN6R3GmXbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14206cca0.mp4?token=ePREXlvoAmpakuW5LZnH0Rw3zv_h8ds7-uHOzxFD02muMEhjm_9aOdLVmDkH6MhQ5Zbtte8MHOUbtkAHSCmtnM7CYFTVxDyUh8ybR9_3X-YNPjZVtVwuy6-jUcxRwWxxIEN442vwB-nKLYPlyROwKUXJuHkq_9LmFZUQAQnUeyWR6ieZRqTUX67BVuPsUd0xAbRmoft-Ig3SAzbR8HgsC-oxDMwh6rriKvpQQEn07LWAp2_d-i4XSWIJz2awNkns_ui8tPTedd9qLHSR5vwbOhO2gJYkqo5jA-ZYjIu7cWB3u0l0RNdSDygY54SZm8I9MLwrLmFzU2batN6R3GmXbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظاتی با درخشش‌های یکی از بهترین لژیونر های تاریخ فوتبال ایران اشکان‌دژاگه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103863" target="_blank">📅 11:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f9fca4e0.mp4?token=pWtkZBeHmDtzC1C5i0tptm3yTbcE6A79iG3SSbmvUSXRzgmIGUUBSgn32YuzmqENviDuewtOxCkKsO3woFZXjtGo4RF3_Ia2n50g_6EsgrZKUI0tBra0Z5LhwghcFYfFCiVy0fQXml2tz545OAcmrjIjwsJqKZCG8fVyIZwz2SjALS9MmNjiAfULMGQSI6O8dSc8EEC1ZLnNzig0jSLJMM3XzGsA88tOn8xI5-x8545kWJxdokfQA-vcwiC4JuO9n5RfgIKuUdrGGoVWkE6seTttK5p_Wzh4CQ3aS6P1vm1kqrTWn4bH4ijSho2A_fPPcrMPtMOo7BXtr3LR0taRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f9fca4e0.mp4?token=pWtkZBeHmDtzC1C5i0tptm3yTbcE6A79iG3SSbmvUSXRzgmIGUUBSgn32YuzmqENviDuewtOxCkKsO3woFZXjtGo4RF3_Ia2n50g_6EsgrZKUI0tBra0Z5LhwghcFYfFCiVy0fQXml2tz545OAcmrjIjwsJqKZCG8fVyIZwz2SjALS9MmNjiAfULMGQSI6O8dSc8EEC1ZLnNzig0jSLJMM3XzGsA88tOn8xI5-x8545kWJxdokfQA-vcwiC4JuO9n5RfgIKuUdrGGoVWkE6seTttK5p_Wzh4CQ3aS6P1vm1kqrTWn4bH4ijSho2A_fPPcrMPtMOo7BXtr3LR0taRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
💥
اجرای جالب و دیدنی هومن حاجی عبداللهی و آرش برهانی، با ساز و دف و تنبک و تار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103862" target="_blank">📅 11:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🇮🇷
فدراسیون فوتبال برای مشخص‌شدن پرونده فسخ قرارداد یاسر‌آسانی از فیفا استعلام گرفته و بزودی نتیجه این پرونده جنجالی مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103861" target="_blank">📅 11:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df609bdcd.mp4?token=Rhe-9VuqRRT8H6DfTro9QTdAnn2p9Yc3O2SGRiZ5sqqka-QrxxlTX8oinyR6e8X_IS_yMC_fmjyQDtQ1LFVrZElDaL0yyFyaGuC2tReaCdxcpO6vACZmSc24otyedh58fMlsZcMgIYzZUcXyujajj17bFjnbVl0nyKbBAggvviILCYwO6sHgYl350fif10n0uJV9y4RDYndO576p1Y4tlSfiO2p2uzzLDxF2t7qtkl2qPQIK2cDxrfHz-dvUKNbQL-9nL93l2tkTB31s1SlR-y3tacrX_gKCiUNF-L5ecdM0myua0H93Ey7MTERTHMciSKvzXtpIWraNgq82kqlfD0Z7Om4bI-A88FM1vUXu2bG845VX589P3PGoDV-lQIf2U5iagk0Dy2aAHCnagxGXokzfIVQo8ld8xVRhV_wolO29JQsQw75fepPG-2m7Qg6S8QZNMuBalt67hp9zQrppKI8vmIS9eP7b-HNP4fTqvdTZ4laYgoXdboBMYZ2e19ezaeIU22uKtk2ZplznAY8qHjNIHbMRG8hR2QXXLQXCw8lindUdKZVXWXNCcKo-Byrh2FtT8MHfSHrPDGNgxuKGLGtfv9C1eugb2x6YGqqjWAAYdgd--fYBvh0c1ydtxNxKAEya9jiMhWd6mawjWpdhO7m8YvPbBIiFmRDkkJm0dvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df609bdcd.mp4?token=Rhe-9VuqRRT8H6DfTro9QTdAnn2p9Yc3O2SGRiZ5sqqka-QrxxlTX8oinyR6e8X_IS_yMC_fmjyQDtQ1LFVrZElDaL0yyFyaGuC2tReaCdxcpO6vACZmSc24otyedh58fMlsZcMgIYzZUcXyujajj17bFjnbVl0nyKbBAggvviILCYwO6sHgYl350fif10n0uJV9y4RDYndO576p1Y4tlSfiO2p2uzzLDxF2t7qtkl2qPQIK2cDxrfHz-dvUKNbQL-9nL93l2tkTB31s1SlR-y3tacrX_gKCiUNF-L5ecdM0myua0H93Ey7MTERTHMciSKvzXtpIWraNgq82kqlfD0Z7Om4bI-A88FM1vUXu2bG845VX589P3PGoDV-lQIf2U5iagk0Dy2aAHCnagxGXokzfIVQo8ld8xVRhV_wolO29JQsQw75fepPG-2m7Qg6S8QZNMuBalt67hp9zQrppKI8vmIS9eP7b-HNP4fTqvdTZ4laYgoXdboBMYZ2e19ezaeIU22uKtk2ZplznAY8qHjNIHbMRG8hR2QXXLQXCw8lindUdKZVXWXNCcKo-Byrh2FtT8MHfSHrPDGNgxuKGLGtfv9C1eugb2x6YGqqjWAAYdgd--fYBvh0c1ydtxNxKAEya9jiMhWd6mawjWpdhO7m8YvPbBIiFmRDkkJm0dvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نبرد تاریخی دو اسطوره یونایتد و آرسنال در تقابل‌های مستقیم و خشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103860" target="_blank">📅 11:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcsr9ONg3ZG-ijS9bfejpTMFogKlrsv4nVUf-HVLN2uPNl9KDV1tyvXmiwCxgI0alR-9HmWVLfhxV2i6nyWb2VEFc1n1qbhD1riylkObOH1oYtTmL7EuEXJ_fqHtmP1_Vp9m-X-pt-ON5naLsPM6Bw3mLUBdWGphrgsLzEPY-VF5cBpQVLiJ2Y2_DRHNr6ZE3z6h5AscnuHMadHrx66IZFhKsYA6rOk6_WuZRmFKm_7L8ukmIWQi5vJ8cZo_GcUauttwL4CCZ28VgXfPvQTe8B0oND-Aq5OoIot1sIfmOGHtRHMZ6SCzKYYwfMpmkTuwTNs6AZE5tbwiyWu6MTwlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
فدراسیون فوتبال برای مشخص‌شدن پرونده فسخ قرارداد یاسر‌آسانی از فیفا استعلام گرفته و بزودی نتیجه این پرونده جنجالی مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103859" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103858" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac_l0fsnDbR4zDd_EzJLH7oSQGR6QCZ-_HhCA1rxtzrFzHrdmylbLRg-p8i7He6-GDOFKO1zILlMIqbPYSHxppB3KIeGbHeWnkvPB9L1tHtczAOXmwSFgW3vJVue7FDbUcK-IsaKXV8oUy2rYZY68xJu8gGD5PQ0ZLqXHDmxf3gdbShW53tltizYHCwY18f862yM-Yo58qnsIcnrJr6sZl3NBcPQHCbVwkH8dA6nTTUaGM9lQV5zwyk1ufMkYyUKUrd1YWDGJPpjDBHYIDJBtvZBAp5K6mPuPcHnjS9WK0UmN1ceYB__qOarQeblanPr07AvhLFNU0th1x_hO7iJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
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
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103857" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103856">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fcc1320.mp4?token=eWv_xtojLY2Eirc25Kqg1BiGptGIiRrxWpoOSMaRP4qsZpVDtTza5OdLAHK0FrLLcaaFzvPkumSSzed4-znFQYEBJ8S-D-m9T4y2RX8TOHsjUBa8CaAryuz0pgJhg6RSNOdBaLY2SrXoIhSj17gQvikRbusZwA6VtfutOtiAxP4cBodwjk2NCIV0B_gBe029uQp3raKh_CRFuyEW4rD3Rn3fWBfniv_j0u5ppUlG72u57h2BEKq33PoXvOR-J_m87L0ZCu2J2NszFYjiQQ4nK8d_KETKUsVTw2p2tBsd15A7Ky4YrWHwyyJ-zryTb4cEMgvaY2IIkEAUxEnVdo4-VWXIn13iTBaJ3wsd1qsnR2Je4_441UdqZbwzGiVPgvzIYSU8gAHTRIUUZbLDdFBPxjwxD6-1LKUaLd9XBAT6kJr5U00nNCwKpBdsIFABRI4LBoa55OOext2ichsjRCg_Gkq_FVJJgOQs256zW8W3myfZkzJlGqRV3Y2dUMtlT40Smwd6_J1YFuM_LyE-3_uKm9DOlaebIoEaksYDniKXZyhatqvLl9AbrXPVS31BSm01JAMCngswSN8Bq6HoGK3j7GcLxM5ti4y5vjhq7v9TOUub7jP0V5SV5-m_BnrugvJvrmNgLuNqBbytmbNyEBRfO3Mity8h0XfsufRXRkczu_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fcc1320.mp4?token=eWv_xtojLY2Eirc25Kqg1BiGptGIiRrxWpoOSMaRP4qsZpVDtTza5OdLAHK0FrLLcaaFzvPkumSSzed4-znFQYEBJ8S-D-m9T4y2RX8TOHsjUBa8CaAryuz0pgJhg6RSNOdBaLY2SrXoIhSj17gQvikRbusZwA6VtfutOtiAxP4cBodwjk2NCIV0B_gBe029uQp3raKh_CRFuyEW4rD3Rn3fWBfniv_j0u5ppUlG72u57h2BEKq33PoXvOR-J_m87L0ZCu2J2NszFYjiQQ4nK8d_KETKUsVTw2p2tBsd15A7Ky4YrWHwyyJ-zryTb4cEMgvaY2IIkEAUxEnVdo4-VWXIn13iTBaJ3wsd1qsnR2Je4_441UdqZbwzGiVPgvzIYSU8gAHTRIUUZbLDdFBPxjwxD6-1LKUaLd9XBAT6kJr5U00nNCwKpBdsIFABRI4LBoa55OOext2ichsjRCg_Gkq_FVJJgOQs256zW8W3myfZkzJlGqRV3Y2dUMtlT40Smwd6_J1YFuM_LyE-3_uKm9DOlaebIoEaksYDniKXZyhatqvLl9AbrXPVS31BSm01JAMCngswSN8Bq6HoGK3j7GcLxM5ti4y5vjhq7v9TOUub7jP0V5SV5-m_BnrugvJvrmNgLuNqBbytmbNyEBRfO3Mity8h0XfsufRXRkczu_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
این‌هم تصویر اون خانومی که پشت تلفن موقع زنگ زدن میگه "مشترک مورد نظر در دسترس نمیباشد"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103856" target="_blank">📅 10:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103855">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7e9ad548.mp4?token=fcAX0tm9uR8FqVXQufzpbTlGB6qRl75ysRIPOn_zdwpEkPBoEChip8sSmFJwS6OwHJjNlzrQsBEXVZZ-yaa8DQ2_CAM2te2hamw_tUQ1RbXFwl2oiRAmgKjgevniqa6yvcBeFMVkCejf1o6vKzb65392_yLlKqtUAxfnHMnoXcf5NKqwHCVCg_gamSG2f3xmvJYeYgh6SPCDX5O3jM1N8qpD1IQzTiPzutk0-2t9HlySESeZCr6M-C52QaW7k7CdwLmXH5M4w9xGodMfHM5dz5sflELu3HwtkRSzlxthNxSdaajbBwbh1Ub8CgQoNIecKuu3DlOlWZtG-4pngIX1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7e9ad548.mp4?token=fcAX0tm9uR8FqVXQufzpbTlGB6qRl75ysRIPOn_zdwpEkPBoEChip8sSmFJwS6OwHJjNlzrQsBEXVZZ-yaa8DQ2_CAM2te2hamw_tUQ1RbXFwl2oiRAmgKjgevniqa6yvcBeFMVkCejf1o6vKzb65392_yLlKqtUAxfnHMnoXcf5NKqwHCVCg_gamSG2f3xmvJYeYgh6SPCDX5O3jM1N8qpD1IQzTiPzutk0-2t9HlySESeZCr6M-C52QaW7k7CdwLmXH5M4w9xGodMfHM5dz5sflELu3HwtkRSzlxthNxSdaajbBwbh1Ub8CgQoNIecKuu3DlOlWZtG-4pngIX1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇷
بالاخره مشخص نشد هیچوقت که عشق بچگی کنعانی‌زادگان استقلال بوده یا پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103855" target="_blank">📅 10:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b721594231.mp4?token=AvBwn7PXx_JICot7chWoU2UD3SP2y2aFbk2VpfNp3rjzaCb4Ep3r34an-EOjHqLNOIIp9RUsmuYcGOZ_mUAT9cxWMVDTXJyvuI5QXASV2AYkfNx4aoVlQgxWTVVWLqvoNBddzGpU9U1uAyWLxyFP1bhbInDXP6e7mGPGN3MrxqoXCSw8yHlNwQwl75psQ2---gd-amYOVbkvRsPexH9ghH0lQX3DDJYVPJVp0E1wgaBYyDtaGkL11cBmXzqtWtNI78nW--SRIQ7I4g8ARMIG1Cypwqkr_b4xUPQthHR_ykBFRHFKP1514M8sMsdCndQwwKXoJRk7EkDVvNo7McX-3WqICYWJdIpY1GMF8lP7nhhUVpwQD4xt4CnkNGozblLzl1GRQLMXkK92Bp9Cl6aSV6vbAtBD__JQ4KwqimaZX5wuyRAuRdIuJC5vw3cdjNjOL824jbc6kMtoHHe2CSx-xltt2vFKzo_G3fSsJr8LvcSPSl0bLtuIQWm4bpDdIyXLD6QLlrCW-SKLlrrpPCBOKZx7VNUa7V0k7m5QrsusRW8djZCR6aN1FOT6xCcU9Bwh0KX9UW9xMfcRRwZxl3k7rs8o0_gI3UVRG5n5jZn94XQnOMXiyDjYF0pgQU4gsL3dY4WHUPmEC7pqT0YM7yKLfxOu_rFOMD-CGcDM3EJ6qEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b721594231.mp4?token=AvBwn7PXx_JICot7chWoU2UD3SP2y2aFbk2VpfNp3rjzaCb4Ep3r34an-EOjHqLNOIIp9RUsmuYcGOZ_mUAT9cxWMVDTXJyvuI5QXASV2AYkfNx4aoVlQgxWTVVWLqvoNBddzGpU9U1uAyWLxyFP1bhbInDXP6e7mGPGN3MrxqoXCSw8yHlNwQwl75psQ2---gd-amYOVbkvRsPexH9ghH0lQX3DDJYVPJVp0E1wgaBYyDtaGkL11cBmXzqtWtNI78nW--SRIQ7I4g8ARMIG1Cypwqkr_b4xUPQthHR_ykBFRHFKP1514M8sMsdCndQwwKXoJRk7EkDVvNo7McX-3WqICYWJdIpY1GMF8lP7nhhUVpwQD4xt4CnkNGozblLzl1GRQLMXkK92Bp9Cl6aSV6vbAtBD__JQ4KwqimaZX5wuyRAuRdIuJC5vw3cdjNjOL824jbc6kMtoHHe2CSx-xltt2vFKzo_G3fSsJr8LvcSPSl0bLtuIQWm4bpDdIyXLD6QLlrCW-SKLlrrpPCBOKZx7VNUa7V0k7m5QrsusRW8djZCR6aN1FOT6xCcU9Bwh0KX9UW9xMfcRRwZxl3k7rs8o0_gI3UVRG5n5jZn94XQnOMXiyDjYF0pgQU4gsL3dY4WHUPmEC7pqT0YM7yKLfxOu_rFOMD-CGcDM3EJ6qEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
انتقاد شدید یاسر همرنگ داور بازنشسته فوتبال ایران از رفتار دیشب بیژن‌حیدری:
🔴
داور پناه تیمهای ضعیف‌تر است. با رفتارتان آنها را بی پناه‌تر نکنید. می‌دانید چرا؟ چون سالها با عملکردتان این کار را کرده‌اید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103854" target="_blank">📅 09:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641c149f79.mp4?token=ZC_SuAby36rpaqk2-6ldRq0Qt7GA84tSUhgEhJAgmDwDBwTPY68KN6WWbH2xAxg7HjKNoBqWDfEgOraF2CHG9Aju3bFpO0R-C-s_JHud6TAPH3rkiJljXo5Zgksj-G7djIopKR0NDof4-op_kMJbyJjNy7NkRNqUbrteKYrI8bALvnakwTsTieo2qp9Z90e03PPKQzbb8QW5q4eDaSWi99T0GDQ3qeLuV4m-DH9kE1gj_N7dxNlTTazel0UkWCfcWswnpLjr8rJtvsQvjX0_I7M-doBGJN5ccvmjFIq_mm8cjGutxjE12ZKnY5w9G-u3bMsPIG8H_10zCB71-WPiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641c149f79.mp4?token=ZC_SuAby36rpaqk2-6ldRq0Qt7GA84tSUhgEhJAgmDwDBwTPY68KN6WWbH2xAxg7HjKNoBqWDfEgOraF2CHG9Aju3bFpO0R-C-s_JHud6TAPH3rkiJljXo5Zgksj-G7djIopKR0NDof4-op_kMJbyJjNy7NkRNqUbrteKYrI8bALvnakwTsTieo2qp9Z90e03PPKQzbb8QW5q4eDaSWi99T0GDQ3qeLuV4m-DH9kE1gj_N7dxNlTTazel0UkWCfcWswnpLjr8rJtvsQvjX0_I7M-doBGJN5ccvmjFIq_mm8cjGutxjE12ZKnY5w9G-u3bMsPIG8H_10zCB71-WPiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😳
مصاحبه منتخب‌این هفته لیگ‌برتر:
شجاع خلیل‌زاده: گلم تو جام جهانی درست بود و ترامپ با دستکاری وار اون رو مردود اعلام کرد.
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103853" target="_blank">📅 09:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3905dabff1.mp4?token=dUYwrhb0BD55T5jrCrm1W6KfXCPWMulhLguTS2_FL0j4SCW-qSwAASpXMDHHcNwbQcjothkOEYKdMLSJ01kXpQafLG8Dfz1iGTHWd4q6tMooIe4LhIaj1TOlqWT5jdolPfj0g-7O2DPQnIaYru22appNGN-5Z8GWjFH5n86j0dYF21FWve0GmJ0dvRjvz5oZzKwb0Knd8I5tBuH5gVU5jLhCByuSK0Rq-vljcqIGKGydiFH9xHD2TKQzYVde5uSsEf5Ey9mrChyzK0KJ-DymqEW_xuFv29jsG0l_BYgpqahFWu_2ytpQriPdWSkt412HbnmUvt9peI8xWnRooRTN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3905dabff1.mp4?token=dUYwrhb0BD55T5jrCrm1W6KfXCPWMulhLguTS2_FL0j4SCW-qSwAASpXMDHHcNwbQcjothkOEYKdMLSJ01kXpQafLG8Dfz1iGTHWd4q6tMooIe4LhIaj1TOlqWT5jdolPfj0g-7O2DPQnIaYru22appNGN-5Z8GWjFH5n86j0dYF21FWve0GmJ0dvRjvz5oZzKwb0Knd8I5tBuH5gVU5jLhCByuSK0Rq-vljcqIGKGydiFH9xHD2TKQzYVde5uSsEf5Ey9mrChyzK0KJ-DymqEW_xuFv29jsG0l_BYgpqahFWu_2ytpQriPdWSkt412HbnmUvt9peI8xWnRooRTN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
خداداد عز‌یزی سرپرست تراکتور: اولین نفر با پسرم رفتیم و جانفدا ثبت نام کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103852" target="_blank">📅 09:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba79548dd.mp4?token=IeZhvMuJ30ZRXSAWPVi9P-RHb2_dovXJcaUuWUjhs-1co9SJuUssGikI7W3DYhOkY35m4l6oZYtB9Zu3dqbmApk4txckYlBPk9CImUOwP_uqPQa76gvobsUQsNe8RKOBvkgYHLmQq0sdbI1KqeQNhJjPBzCsJjdRzSm-VMRMPrWlbgQwAZam5VZFds9JavIT478kEAPAV2vYCvKqsmJ6mzwUzKhzLp20sn50SCuQA2a-QW1JvkYHiSKmHOumDwjhy8ying_8UWwIYsL49tU3JT9FgTg6bpSeUEFsKNFOc3P3y7RxeD7PpPEYM5AfSemA76Lo-pudoCUn4sBX8nsTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba79548dd.mp4?token=IeZhvMuJ30ZRXSAWPVi9P-RHb2_dovXJcaUuWUjhs-1co9SJuUssGikI7W3DYhOkY35m4l6oZYtB9Zu3dqbmApk4txckYlBPk9CImUOwP_uqPQa76gvobsUQsNe8RKOBvkgYHLmQq0sdbI1KqeQNhJjPBzCsJjdRzSm-VMRMPrWlbgQwAZam5VZFds9JavIT478kEAPAV2vYCvKqsmJ6mzwUzKhzLp20sn50SCuQA2a-QW1JvkYHiSKmHOumDwjhy8ying_8UWwIYsL49tU3JT9FgTg6bpSeUEFsKNFOc3P3y7RxeD7PpPEYM5AfSemA76Lo-pudoCUn4sBX8nsTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🟣
لیونل‌مسی چند ساعت پیش بازم پنالتی خراب کرد و اینترمیامی با ۴ گل مقابل حریفش باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103851" target="_blank">📅 08:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77aec0f40.mp4?token=bGsyLc-9UL-fudf9c1GA4JmQtXu26BAb04Uo7WUOyHYDYP-Hb1U-bLM9gu6HoACIWL4KyVH-hKtw75wUPu_ZpfPNJNNp_OOy7V7tbvUarv5B7Pq-0vvPg7mIYPO0hYzq-uHJy0aJs-gbEcphtGr0JrwIvCyEq2wwZExIx3jAlHGdOZM6Sf2DogorarFYrhMX1Ro8F98sy2eV6mo_DzxaMD-hf_HbX4JtB2G8JCRrQqGviUtXVWfTnNQL3zaeilaQZ3qnSYE2ukGn9e4sr0PC4-Q0LBbATmBrPe8jcGLV6ivGTfzmuqvPJ47AdJeXpomgr0uQxmD59QJvcsTmuZ-XaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77aec0f40.mp4?token=bGsyLc-9UL-fudf9c1GA4JmQtXu26BAb04Uo7WUOyHYDYP-Hb1U-bLM9gu6HoACIWL4KyVH-hKtw75wUPu_ZpfPNJNNp_OOy7V7tbvUarv5B7Pq-0vvPg7mIYPO0hYzq-uHJy0aJs-gbEcphtGr0JrwIvCyEq2wwZExIx3jAlHGdOZM6Sf2DogorarFYrhMX1Ro8F98sy2eV6mo_DzxaMD-hf_HbX4JtB2G8JCRrQqGviUtXVWfTnNQL3zaeilaQZ3qnSYE2ukGn9e4sr0PC4-Q0LBbATmBrPe8jcGLV6ivGTfzmuqvPJ47AdJeXpomgr0uQxmD59QJvcsTmuZ-XaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇮🇷
رسول باختر: آسانی دقیقا اراده فسخ داشته و همین موضوع کافی است تا قرارداد با استقلال فسخ شده باشد؛ فسخ آسانی نیازی به ثبت در فیفا و فدراسیون فوتبال و سازمان لیگ ایران ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103850" target="_blank">📅 08:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOLZ-u02wmKNJ-mkxHUtVxRbeGj5B9P3dZGIIvsufcNth6T5pjViYZe_H1FdLBd_ykXArRx-vNd6X8j7gcuCyQF4jAsIcU0nXE7Itn2-V76WbQA4OlVSo4fxFkvUDoahHsH8FBvhCvxYhX88M6nQ-M84bJ3cff94-dnleBLBt6D9n2anDmm8BEqQoyQ6EQVk8IMnNnm_kjyu905tYerKPpqjhVTZCMt5eTHQ_VHlkHGkZpwdlDi2SDWIGTtVY5CYCrDhVxUK8C_riMu9vsgnEA5YNBrxZZESoW6brNYtIK1XNwqmu8LoOEOyWdNqxIcapEq_pceIIaINSyLM809sPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو:
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی موافقت اولیه خودش رو با انتقال رودری به بارسلونا اعلام کرد. سیتی نمیخواد بازیکنی مثل رودری رو به اجبار نگه داره و پیشنهاد بارسلونا تقریبا مورد موافقت قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/103849" target="_blank">📅 02:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz2vRuCmSEUu3FjUyv57WdNTslJOnQoeij2AOJuCV_A3ztOfTm3W0NzSoBaeEBSIjer1F_81wEYqoHfmpb_ekPAro9LBDxAX-etC-itOSgsMy0tY-pKmXaJyFdCyIfSBeiNoHqBOtAuCtpAeOdTwXw0QUL4tSfre9nEmvsigA5xjtNX9WwcyN8fGuotz-F2kEZGrtuiPcF6_VfhlnTxnjdVS-IsqSRr7Ic73MhrPvm3m8UdiapKldHqhhGDyx_a1kobrzfrSe90SLqveZCndIlxqP9QrtSR1yyCbfHsYR2nZizZi86yII52oBUFnchSBA0l2Ub91mIHRSJIPcipg-pwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz2vRuCmSEUu3FjUyv57WdNTslJOnQoeij2AOJuCV_A3ztOfTm3W0NzSoBaeEBSIjer1F_81wEYqoHfmpb_ekPAro9LBDxAX-etC-itOSgsMy0tY-pKmXaJyFdCyIfSBeiNoHqBOtAuCtpAeOdTwXw0QUL4tSfre9nEmvsigA5xjtNX9WwcyN8fGuotz-F2kEZGrtuiPcF6_VfhlnTxnjdVS-IsqSRr7Ic73MhrPvm3m8UdiapKldHqhhGDyx_a1kobrzfrSe90SLqveZCndIlxqP9QrtSR1yyCbfHsYR2nZizZi86yII52oBUFnchSBA0l2Ub91mIHRSJIPcipg-pwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان یه استوری گذاشته از صحبت قدیمی مهران مدیری که گفته هرکی دست به افشاگری بزنه خائن و بیشرفه   گویا جریان درخواست نود رامین جون درسته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/103848" target="_blank">📅 01:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOFn2WPwigCK-2RydSWAFYzdAt_-x1UQx4qoSxJkXhyvu1p3aCWR_8Qj-XS2-1tmYDrFTYSbBkn-5m1siLop6i14UMm53ti_C4nZVAJbdzxO_3Y887mfRimBKO8rC9W33fftwjW_D6FBTBLH3RMRY3DTB014ScKlH2Gha4YSPRHsAgyDdcb-yjfX_sSGbv1iT3vUHF_P89Sulu__1LGcfU3Fdql6Nsf4AbUY9Fmmkjk3dedRKIX0A23BvpmntavW-ESAuPVdSfkizw3XFkn-Qo0TCraHx5NXoJ5ZaXp_FQTVCbuPSKb0DaD0b_0fq20mRcWNCac25CxxB81UFqZrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
از رسانه‌های نزدیک به الهلال: اوسیمن هدف جدی شاگردان اینزاگی قرار گرفته و الهلال تمام تلاششو برای جذب این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/103847" target="_blank">📅 01:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fbd749fe.mp4?token=gJjKoAo9rE7lcu6SzmsjEl8XnynTR3_5JeUX1BeMAWpwz20xHgyqa9XWBe1UA2Nx9qHT7I7L9TSVCRHathIyxHB9zWKE8F2eKTu72io23mWrY3AfQ7jzjrJgt9_jzOOLRUd9vkQ1u_UjJNNW0AxP2Dok5-SGv5uck8INk0U7WHvWuKsdoeaj7KUx8zTwc962xy2LpoMRpJ_ikhdQkC08lfaF_kkBUb8d2awf287M6eXsOmKTxPirIbMDfkeJL1PaP4HFvNe0agauI6X4nHst2razKRVynzaxIF2Bz4OAWJUTBq-amNxvfvxbRjF0r_gIHLIvbxuWMJwuW1K7yltPMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fbd749fe.mp4?token=gJjKoAo9rE7lcu6SzmsjEl8XnynTR3_5JeUX1BeMAWpwz20xHgyqa9XWBe1UA2Nx9qHT7I7L9TSVCRHathIyxHB9zWKE8F2eKTu72io23mWrY3AfQ7jzjrJgt9_jzOOLRUd9vkQ1u_UjJNNW0AxP2Dok5-SGv5uck8INk0U7WHvWuKsdoeaj7KUx8zTwc962xy2LpoMRpJ_ikhdQkC08lfaF_kkBUb8d2awf287M6eXsOmKTxPirIbMDfkeJL1PaP4HFvNe0agauI6X4nHst2razKRVynzaxIF2Bz4OAWJUTBq-amNxvfvxbRjF0r_gIHLIvbxuWMJwuW1K7yltPMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚔️
درگیری حامد لک با داور در جریان مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/103846" target="_blank">📅 01:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsLdwq6-aWllEVbidetNdl6-WMILohUiQVtaRTI5WjemSP8EQXYb_9cjdg0khjH2dEVMZyF02KwvsHLaTSyqpgqTMmExOCDdD7Zb8oMCOHiFCFrzKq1Dj_jDu0ofKSQuZ6MfuV_6u4l4FNMJlqWxlW9YGxbBsuq66sAAb1T-pGkpHVMDKQtwHFiachsc5F73bHPmfyVrWg_oBW88JxiTOdqZe5eNFMFfqpWrY-w-2Y39Q2mx0hLfJb-7MlPltmcu8lxTDP9zLgJ6WbSBWyvJDGVUuMhar-G4j6vdY3BwN-C4Gcldugjyxh6HQLvbCd62Pte2nBsIrllop9vpV_J88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
توئیت ترامپ در لحظات پایانی مدت‌زمان ۶۰ روزه آتش‌بس: پیروز خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/103845" target="_blank">📅 00:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSiY8ioirgzZ0dRbwQCv2agwjzp2jCiYYlxN628xQWRtAa17Lf34QUuIhUD736G-3LwGgPE1gNjBJrq0tICpbWGkNfr27BQ6YsGABL81Rc8Y6toFxYslS5gr85XyucfqbejQf8xgWVRXu_lpzsDoIoeRUVhyNinKWu0f9Msekk6F6EnVOIf7S_XfYcMG3SMJ_dBCwKgXDAodCVumrq4wsWBNyeUpVniSlP4QGV4xSOSbZfryEOMfPgaodT_jo60cY4T3gUoSw1NX_bCTMCglJeObliUORW14IgNtQKSwSXaKrrRYTfG00YlhdNA8FbrG_nV05BKxct30Bb1r0cxXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جرارد رومرو:
✅
مبلغ انتقال رودری حدود ۷۰ تا ۷۵ میلیون یورو خواهد بود. در حال حاضر قرار است مراسم معارفه او روز چهارشنبه برگزار شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/103844" target="_blank">📅 00:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7Cop3ytZpL30pkcbBmcf7Sdz2q8Rr_zsIqubvIPG6W9awj2fkJUkfDeB4-q1e4KgMMHqqX7Hozf3kZ3u-Noo3dc0G_sr_C73MKPH7ZzfYvgyUxVOZNFqJLO5Abs_JU71W6pFf90G_jvvU_bc38Jp5fcGvy03EqNbZAtocDiSdL9_ZaTpwwm9sL4vKPNr3ANIj8k--sTCK1IDAW0kbfsxG4PE0dmoD93JhC7AWKPNsAA-IvZFUAl_XHMDwqEdSX_TngGylCaYSDWaDbfiPt0AD6XKERA9TtmcukD5w8WhxgG674N-xXPHxHqsWxFZrXvzgrnlaEIKgL0sjiOFQDC_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🎙
پیمان حدادی: اعلام قهرمان برای فصل گذشته منطقی نیست/ می‌توانند تورنمنت 5 جانبه بگذارند که ما هم شرکت کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/103843" target="_blank">📅 00:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103842">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2opvGePKLeINu2kn93_VdOlSockQ1jJbiw1aAxLHQTkEIrbrs6Epy7Q3I94IIdes96XYhKvVDxCW_xxx2q6Boagl5MMPIwgr1VsSfJp0MJw1AksLoG5tv-Kw9Vu6ySkcpqxDVVaI7wIPCROOByHkYkjVI1G-BcsYTFal2qLaqhh5itOntFdAsP4tA0WI0kjfGsze2Z23SDwCsapaXzTKSRtPOxAzZrploF91VzQvdHWPNQ-AEu-LONz8eHe8HktyY-qrPUid0BRZd_4vHqe9uebQqAvf8uZjwNZUxhxyPFDVIY-pL_2JO9W3knBszUSCHowpndFMBN91ihbvSDWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوووووری
از لونگاری؛ مالکوم برزیلی از الهلال عربستان به الدرعیه این کشور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/103842" target="_blank">📅 00:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103841">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG3eUZaEQxcQ9DfLtbyz0RHO2y2Xdhk-TDtPEjmXbUYSu-qn_UzsECA5C1cRJjk28SYzXBNzIpiCT-C_r0uPb1ylGQtyJgbYLL8Ibff1CyFVjtdmoGwmiF38oZFNL7eoQUuF5UKzhQZueEYn5Sjv4TqHBVCOT_B3xJOXU7m7ur7b1HDGjfewrd1Zwo7ShpETFchufaHZV0xyvTSJSAdYItTP95c_3bFFsjpVHRNtiN68124YxRTnM2EzWLEgMtAkXSTFCoSFRWFyypa4Y3c43PQTV-LdgjpKtJ1ZaAm7WHAdX6EJ7C1_1KA0FFIGcxr4JxF_AN5Vt9eyz524e4xlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🔵
#فوووووری
؛ باشگاه الهلال به صورت توافقی با ژائو کانسلو فسخ قرارداد میکنه تا این بازیکن رایگان راهی بارسلونا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/103841" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103840">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103840" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ulqI7dLzItu2f9sdVIzxg26o-nEAvW45Zq2qota0P6wXe-bZ7m76Ia4LR2w43WIcHihCbMZI57NXmOvkj-3f5nCIfHB-x9dsUsdU4HkHNQS13jJpBpw-5krdFgVeHvb-jMzrPKrsf7Gdx6co5enkbNAc8k9HKf4Sg8nYNxhB-RRSEBmCZPqMrxWiphSOQ4iH34WPYRh3QITG6z6dun1fm34UVLinm0NQEqfAzHjC19vlaq8JEBolF_gRJNPl7m6rCMXUrHMUWjDjw51VWLBW1OxnQl3FV8gvrOgeVj7Z3Y1EqstOM1dFssE4nuxfGqX61Vpo3xgbTvFmltpceToFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ulqI7dLzItu2f9sdVIzxg26o-nEAvW45Zq2qota0P6wXe-bZ7m76Ia4LR2w43WIcHihCbMZI57NXmOvkj-3f5nCIfHB-x9dsUsdU4HkHNQS13jJpBpw-5krdFgVeHvb-jMzrPKrsf7Gdx6co5enkbNAc8k9HKf4Sg8nYNxhB-RRSEBmCZPqMrxWiphSOQ4iH34WPYRh3QITG6z6dun1fm34UVLinm0NQEqfAzHjC19vlaq8JEBolF_gRJNPl7m6rCMXUrHMUWjDjw51VWLBW1OxnQl3FV8gvrOgeVj7Z3Y1EqstOM1dFssE4nuxfGqX61Vpo3xgbTvFmltpceToFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a24
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103839" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103838">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
⚠️
امیر علی‌اکبری در مقابل علیخان واخایف از روسیه ناک اوت شد. واخایف با این پیروزی، کمربند قهرمانی سنگین وزن در سازمان روسی ACA را حفظ کرد.
❌
هنگام ورود علی‌اکبری به قفس، ریمیکس «ای لشکر صاحب زمان» از صادق آهنگران پخش می‌شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103838" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3713adcda0.mp4?token=KEK607Zrko57RaBlD5UE3b2DkQSsYTy_2hyUZi_6irFlwE6S8Im24lquIYTJN3iANpaVNr-2eElhFoRyl7_oJLPIUMoTPcoTXa-8Zbe4JUjhrcc3GDuB-bX1dDqGSklJ4oXWd1xggI3w5yPqkIE0TOr16tkgQsAP_K9UvK9_vSxuz3OgMXW5RS0wr18DacOi5rMgMJBIDK4nEWxlbuHQwOg7mxPo8fZKAeBkqBUKGvgPIKohfccbVPvmCqQR_PHTRhgnGHZZA1oPzKS7iOzAqJTzy58xQIM2tnK2EroFv8KvJLaE46Gqz2kErTOBDx8E668sOqhO4VAi6xsRy2L_VGgn5ilg3ksFXGthfM7KjzfYRryVkaMzXKAWjjk64JWLncqr3OoU-mV1_dS4GsG9FOyLLvgvXYN8XODaWlLewBf9e8MXJ1omKCuhiMKOnxizhdmcKJlWEb6xF-V56GaB_MN5mF2Dd66Zejq_k0cDNJHDrA_na8Lm6RnL4y-cUx6VGhL4Hcq7GHUtGKtjjs3Rv6iUbDR3xvZK-rF0KBALCy5X7QZVOvr1ZMuQeqA4aIIZukcMhtBfxRyud6AOOZmqE4ZFBTmvOW6N3NDw1tqBgmKKMTKHWzPMDqdWZXm_e6hcGejHw9F5Dxud77kaYSFkejPrhjpvrVCV5Y95dWxgKmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3713adcda0.mp4?token=KEK607Zrko57RaBlD5UE3b2DkQSsYTy_2hyUZi_6irFlwE6S8Im24lquIYTJN3iANpaVNr-2eElhFoRyl7_oJLPIUMoTPcoTXa-8Zbe4JUjhrcc3GDuB-bX1dDqGSklJ4oXWd1xggI3w5yPqkIE0TOr16tkgQsAP_K9UvK9_vSxuz3OgMXW5RS0wr18DacOi5rMgMJBIDK4nEWxlbuHQwOg7mxPo8fZKAeBkqBUKGvgPIKohfccbVPvmCqQR_PHTRhgnGHZZA1oPzKS7iOzAqJTzy58xQIM2tnK2EroFv8KvJLaE46Gqz2kErTOBDx8E668sOqhO4VAi6xsRy2L_VGgn5ilg3ksFXGthfM7KjzfYRryVkaMzXKAWjjk64JWLncqr3OoU-mV1_dS4GsG9FOyLLvgvXYN8XODaWlLewBf9e8MXJ1omKCuhiMKOnxizhdmcKJlWEb6xF-V56GaB_MN5mF2Dd66Zejq_k0cDNJHDrA_na8Lm6RnL4y-cUx6VGhL4Hcq7GHUtGKtjjs3Rv6iUbDR3xvZK-rF0KBALCy5X7QZVOvr1ZMuQeqA4aIIZukcMhtBfxRyud6AOOZmqE4ZFBTmvOW6N3NDw1tqBgmKKMTKHWzPMDqdWZXm_e6hcGejHw9F5Dxud77kaYSFkejPrhjpvrVCV5Y95dWxgKmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنعانی‌زادگان: در بازی مقابل تیم‌ملی مصر، عینک فیلمبردار را به شجاع دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/103837" target="_blank">📅 23:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bb9b634.mp4?token=WLjgbo--dN9UnFCKG0Mh6Ef7fFoIQdli2iYwPWTiDx8LuFbQf4nWBz4Lgays8pgXEz4OUj0P0z04wB-mBrSLSl9ufvq1bALsIoUMNDCZlxCqTT0Wn84UAyY0JpsH5ML9-FSCOvYwJM3027EYqXoxqEzda7ouDZqD1lN3avG4aCu9lF-Id5ygFVNB2DPhMqRZLl3aokJ1kKaB0dNKC_Kq6W-MhrzdTzeiF9CDGs1gIDCC6bdao8QG2OUe7TeUi-LzuavlQuvpZNt7pB_mFClvHX6Onf1pASkIBt81Hh1CaB6Xb05rWlI6BYF35XZ6PUQVB5b41P8bO2qFsoTlNwlL6LqC-yCHCfjKXPCmBR9stvhS61C5Wh_5A7FUekqaUK12cnGtEUe7f6EI1m8IGdoVTzszrgxZkmxs7NYAkqvcBclq0X4F60xnSaPYh64VSrSQvceZ6XP6VjC_agKbPacEYQFDJYoTAw5oaPfPgvzwtI1Nj6M07FZAps1_wgkQfsjYdgCjUE2NSecQuIseoPFp3bkbiqjaKmCk_7O8MHIsPPhg_uYqn7qGw1kRLXOA2aLJNoWlZvcl9E33iakFpgza_4L7xApYmjYroqeXDhF-YZuzv-SzKjuqfJ84mYI-pFx9PUIWELGPxwU1EA6xCjpo2t5au_rKOBsnC0_lhAPx1w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bb9b634.mp4?token=WLjgbo--dN9UnFCKG0Mh6Ef7fFoIQdli2iYwPWTiDx8LuFbQf4nWBz4Lgays8pgXEz4OUj0P0z04wB-mBrSLSl9ufvq1bALsIoUMNDCZlxCqTT0Wn84UAyY0JpsH5ML9-FSCOvYwJM3027EYqXoxqEzda7ouDZqD1lN3avG4aCu9lF-Id5ygFVNB2DPhMqRZLl3aokJ1kKaB0dNKC_Kq6W-MhrzdTzeiF9CDGs1gIDCC6bdao8QG2OUe7TeUi-LzuavlQuvpZNt7pB_mFClvHX6Onf1pASkIBt81Hh1CaB6Xb05rWlI6BYF35XZ6PUQVB5b41P8bO2qFsoTlNwlL6LqC-yCHCfjKXPCmBR9stvhS61C5Wh_5A7FUekqaUK12cnGtEUe7f6EI1m8IGdoVTzszrgxZkmxs7NYAkqvcBclq0X4F60xnSaPYh64VSrSQvceZ6XP6VjC_agKbPacEYQFDJYoTAw5oaPfPgvzwtI1Nj6M07FZAps1_wgkQfsjYdgCjUE2NSecQuIseoPFp3bkbiqjaKmCk_7O8MHIsPPhg_uYqn7qGw1kRLXOA2aLJNoWlZvcl9E33iakFpgza_4L7xApYmjYroqeXDhF-YZuzv-SzKjuqfJ84mYI-pFx9PUIWELGPxwU1EA6xCjpo2t5au_rKOBsnC0_lhAPx1w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
😆
حامد لک: مشکل داوری؟ فوتباله دیگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103836" target="_blank">📅 22:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867654e00.mp4?token=DPpCKiSAQ4JAzFELwUcAO4qlHL4p4awbqxTdbYAghs2tZ1Mq4rl1T_rDUdch47NHyLxIuc5p0-p0Jz-I2gCJf5ojXpTeoH7dNHG9c4vPVfSTL65NwQ3T1F8rHBqRU-sGzJ9m4UN_IloFuLrCrCQ-x3MEeSVJ8ilqm552oabVfm65TWKaBr4XVFdokk32SaCN1qPoXAxRvN9Bg-640R41c1ipo1PTarFLXvRI8oNKmQ1297nXlbR2em2d9kxMPVjDI_nWw-WVh79JZZFV9oU8DqxkuYAcQLkkRvJVZ-TPpay8AP5rzod_2u5fbu8H1375XXWn_UqKcpvRtch-V2flIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867654e00.mp4?token=DPpCKiSAQ4JAzFELwUcAO4qlHL4p4awbqxTdbYAghs2tZ1Mq4rl1T_rDUdch47NHyLxIuc5p0-p0Jz-I2gCJf5ojXpTeoH7dNHG9c4vPVfSTL65NwQ3T1F8rHBqRU-sGzJ9m4UN_IloFuLrCrCQ-x3MEeSVJ8ilqm552oabVfm65TWKaBr4XVFdokk32SaCN1qPoXAxRvN9Bg-640R41c1ipo1PTarFLXvRI8oNKmQ1297nXlbR2em2d9kxMPVjDI_nWw-WVh79JZZFV9oU8DqxkuYAcQLkkRvJVZ-TPpay8AP5rzod_2u5fbu8H1375XXWn_UqKcpvRtch-V2flIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/103835" target="_blank">📅 22:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103834">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd00ae5ce.mp4?token=toLAIqK32yp546p04DIFLVmzEEGV8VRIN3NPKuipX3jPrptCs2PjpTM1JbMPcjQ5gy_q7O0OwKOrjZc7Kh-CceBu5NfadHjJhq2byHLBwpyYOOHrW-OKH84EYbiOIhClwSeMXmxKcn7DySSOiGrbJdrdD_GYR4DcFAYWQuFMU_ehS9YGdLrpxMZSkG6qK4bORExOjJA3veGfxpjD5vOD0punVe-OQYlGQDe2r8EA6lUhI9jhdcQ35V3jVgIIiEW9QgXY5VdUzTzkczA-iHHMv67QGHG9wfyVXEJ8dGkFf_eb5aC8eNn7Cm3edGF6GbFJ33Z_HR_DrfZvP0ocYsqtp7jNsE2MfVRc7h-6YsMGKNi-cLOBfcTu2HrXr4bZNbfkj0xRGT1U01kr7hhxEcGCCTl6X5uj-TOcJ8mtQhw_zsskuAfwu2Jm3aDFe69KOt0o8kbRRQfGcE2zuLNa7AtEiCbCZNyU5h_iq9gBlvJL2AJP--BZcEbWbf95sEU_iLksNknPTc5w7fjk6tFNbN_46naMWxXBotbd3MtPmRr2nWKXRKtu0l7UyOiiVt9_B30u7O2RrMtmY8_R6YE47GezfWgaHaWOBcZVq5ZCU_2RMBhXKpo51Pi-VqjYmLr_OzMjyiuefaUCgjWTZM7iG7RG0R5GX7Q6dFqAylt_SBFeGVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd00ae5ce.mp4?token=toLAIqK32yp546p04DIFLVmzEEGV8VRIN3NPKuipX3jPrptCs2PjpTM1JbMPcjQ5gy_q7O0OwKOrjZc7Kh-CceBu5NfadHjJhq2byHLBwpyYOOHrW-OKH84EYbiOIhClwSeMXmxKcn7DySSOiGrbJdrdD_GYR4DcFAYWQuFMU_ehS9YGdLrpxMZSkG6qK4bORExOjJA3veGfxpjD5vOD0punVe-OQYlGQDe2r8EA6lUhI9jhdcQ35V3jVgIIiEW9QgXY5VdUzTzkczA-iHHMv67QGHG9wfyVXEJ8dGkFf_eb5aC8eNn7Cm3edGF6GbFJ33Z_HR_DrfZvP0ocYsqtp7jNsE2MfVRc7h-6YsMGKNi-cLOBfcTu2HrXr4bZNbfkj0xRGT1U01kr7hhxEcGCCTl6X5uj-TOcJ8mtQhw_zsskuAfwu2Jm3aDFe69KOt0o8kbRRQfGcE2zuLNa7AtEiCbCZNyU5h_iq9gBlvJL2AJP--BZcEbWbf95sEU_iLksNknPTc5w7fjk6tFNbN_46naMWxXBotbd3MtPmRr2nWKXRKtu0l7UyOiiVt9_B30u7O2RrMtmY8_R6YE47GezfWgaHaWOBcZVq5ZCU_2RMBhXKpo51Pi-VqjYmLr_OzMjyiuefaUCgjWTZM7iG7RG0R5GX7Q6dFqAylt_SBFeGVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🚨
🚨
🚨
🇮🇷
نصیرزاده: اینکه فسخ برای قانونی شدن باید در فیفا یا فدراسیون فوتبال ثبت شود اشتباه و ناشی از بیسوادی است!
📝
من قبلا در باشگاه استقلال نبودم که بخواهم از این تیم حمایت کنم یا در جایگاه مخالفش اما ولی باید حرف حق را بزنم/ دوستان باید سواد حقوقی داشته باشند که در این مورد نظر بدهند/ موسسه سیلا، کارهای وکالت آسانی را انجام می‌دهد/ این موسسه به باشگاه استقلال نامه زد و گفت به علت اینکه مطالبات آسانی را پرداخت نکرده‌اید، این بازیکن جدا می‌شود/ هیچ کپی از این نامه در اختیار فیفا یا جای دیگر قرار نگرفته است و موسسه سیلا این نامه را مستقیما به باشگاه استقلال فرستاده است/ اینکه برای قانونی شدن فسخ باید فسخ در فیفا یا فدراسیون فوتبال ثبت شود نشاندهنده بیسوادی است/ فسخ یک اراده است و آسانی می توانسته فسخ کند چون مطالبات داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/103834" target="_blank">📅 22:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103833">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce26cb22e5.mp4?token=QYgYTbA2cS6EfjvaczMFP7DbIPOXAk25qHH-8erVjfQ-cYApukCQ_5b4YZadEXZ0Z-AR7wBll-1020o1gog-gv4VEER6RKqlud2Fq3rhctswIjZbVTXDwTP7kdEEnj6D3Y4hipxtf7MzsLTxRmnZUcaDH3jX8xUn18rf5pyGyEjeoJZb1FwyLw91waxumI9RqSetX62QnMZL5SLuGU79eqF81dJTHOHmzpMxZlt9b2qxZsp81pwulFWN3BbH4j1knPgqgp0uADpv1ZbZxS2bu9qLwRILnOyuicau81OIaZt8abtZaroyEMu-snCVnGvEGyO4XXb8iegTwsIdQIEFcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce26cb22e5.mp4?token=QYgYTbA2cS6EfjvaczMFP7DbIPOXAk25qHH-8erVjfQ-cYApukCQ_5b4YZadEXZ0Z-AR7wBll-1020o1gog-gv4VEER6RKqlud2Fq3rhctswIjZbVTXDwTP7kdEEnj6D3Y4hipxtf7MzsLTxRmnZUcaDH3jX8xUn18rf5pyGyEjeoJZb1FwyLw91waxumI9RqSetX62QnMZL5SLuGU79eqF81dJTHOHmzpMxZlt9b2qxZsp81pwulFWN3BbH4j1knPgqgp0uADpv1ZbZxS2bu9qLwRILnOyuicau81OIaZt8abtZaroyEMu-snCVnGvEGyO4XXb8iegTwsIdQIEFcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
از خبرگزاری ایسنا؛ ارونوف بدلیل ناراحتی بازی نکردن در شادی بازیکنان پرسپولیس شرکت نکرد و مستقیم راهی رختکن شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/103833" target="_blank">📅 21:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103832">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx5FkKP5nYXQTqzA74rJpKEvky4nh9_zQKcVeRnqmk6G6jiS6nc9FlZPHM9iXSG02K0hBry49Wap7GFG8HCht9wm2Ak1FVf51XVkAiSRMh7poPXiYi7pFywZ0Vc6EgfXWLbJF8oh7Ls0CqGYjHWZ_dsWveA4kATP0sgEVMQZoxy_daMJiWV-EGUJiiBLkYloSZQ1O4AD_BZuu0m9mKanYKMTY6h0xb7CG0azdyncn7WDSsaD5zw9JlO3FhQDtj6AeXb2FfqGW4im245CpObzrynjeY9KStnroFvCD461A_aQEVXRwzEldDyxDxHIfK1tI61qWfL_R5CprtDZVcNEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
برنامه بازی‌های هفته‌دوم پریمیرلیگ ایران؛ روز سه‌شنبه و چهارشنبه بازی‌ها برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103832" target="_blank">📅 21:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103831">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKpIiTSg1alyb_dBZdpw1OQ-A6hBY-DGX77WAGiozggd978eyWbqEMOkz33Qn0eTHwQryABV8AOFwodKWni_Mp1f8Nagmxzz6o3FHVv8SGLONwE9YdIZ3qvOMM-Z0otFLNT4U8JNhl7CUqTBD_AfVi9uKGu85m9At2vqYDmcmrlcIybiHWNq7NNcmgZpBy7XwQ6rNlFG3T5eoIysIg7qyXxwPWWpumrMUMprgxkZta6A_j46oWg0QNJ4OUwYqkEiReEugRDCRmCUneHAB3XczTGE0hv8_lzembMq1JpmPLOpXfLnEWpN10RkspVcKgDTuz7SBJyPqU-DDeQuQLDfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
#فوووووری
از لپاریسین: لیورپول میخواد پیشنهاد فوق‌العاده نجومی ۱۴۰ میلیون یورویی به پاریس برای جذب بارکولا بفرسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/103831" target="_blank">📅 21:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103830">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpOl5O-jekJGmywl_D-7AMYl1LoDWHjo_Bthmr5S__FxbOAxW_Sou-csNrpBUSNv5sBeqfNiXlpSG6TmeL49pWn5mueGS0FQN1YPckg0OwdaJq0q9jtzvqyGSVZhMlxZvWGBx6jfOFh7Oxv9WL_xay6QqxhgJTm4MJvRWS7eXDjRRF4DHnkZE2CqO8PWQQ3N4LhkpvKG5jNEL61BX_7ET8Wlf0JsHBH2RBebbg_T_0W33vmL9l2aE-WAcSSA1Vfjb2xkR6J9AEnQuTPXncpNkIIKoTob_JIG1HnG7lrloXNg9oG7uxT1nERsHA9gnenb9O4skmYYkrv4r2p30D4m_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید نوید محمدزاده با لباس فلسطین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/103830" target="_blank">📅 21:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103829">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgx-NYioOiNnuiHA__379NWRHW4nsQyuJEbbeNvHe4e5IgLSOcsq_X-KYoimGZuJHKFu0sp44qK1k4Wd9V70xKBSHzXYdej1esTJKYHazlzfvzxF82GG4I7zQ9XVO6DsOMjgaN1du3vQinaxBk6OQ64Kl9ZakiD6qIfld4aT622XNW1cD5q-7Iie-kMx3thZM_xkZEpTSGTbYrPCW2NedwHnFiLir3Cpkk_sKW2GI5oXCbw-5shEdxt6U4_Z2ORuO_KSr6a6pa6cIhSIi1yMINTX72J-LK-AD9Z_5zQkeEg6etng0JMYvBZZXxmEEWatBkujiIOwE673Wxd_1AD9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
هفته‌اول لیگ‌برتر فوتبال ایران؛ نمایش اقتدار در قزوین؛ شاگردان تارتار با صلابت و یک نمایش درخشان سه امتیاز را کسب کردند
🇮🇷
پرسپولیس
😀
-
😏
شمس‌آذر قزوین
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/103829" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103828">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3eimCDag1JUhZQUQ8wvlT4zhDBJVmuOD9LZCkhWquWAhWbn1jX-rYsrjF6RCY_sTHkK-T6bYF4QVJOcX6CQSF4M2uzxkEC94aVRMzFqLPs7ebAB72J_GHskHoL1aabTDO4j-R316dBYqN7Ag0UIKWdmIMOQEni6ylUunnSzTnDVnveR5w2nMf6dS08G4CMMJyRM6ibBmOWYOvRvUeOP_FtlXJ8TT1be5zGEpUNRm5Tp1hOGiJuptHcSexTquEiXWXHoYU6A7AahkzfzhnllZlDZuwimZguoP_Hf1C7XPSGXsqF21udlUhY7ZtMX5nKxnsDoKf39Cf7wLux8VBfUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان یه استوری گذاشته از صحبت قدیمی مهران مدیری که گفته هرکی دست به افشاگری بزنه خائن و بیشرفه
گویا جریان درخواست نود رامین جون درسته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/103828" target="_blank">📅 21:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103827">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe1kFV-s1hiH67rQ5k5aMmNb9wXDBC3QoAHPa9Cv3rdH2zHC9Si7DNS9z02sA98qSYVinjLIxjCSs5hRz9CamIdtffDuD1Wv_5xbJ8LfeP48XQBNMa-HTfTkDnOhtw3QljPUYsF0xqLkSQFlDbAn5DwvJC5g26RwReJ6lcZb4eyk85QULJ6bi2Gfoc_IwLhPm9R3gCjbAkgiegWlrpOxiUPxOot-Jk7b5ObTWiNLqR-UgLZ-kUVIPHY3UeeOqC7sqHrf_Z0U3VeG-OcllVzU2F0dzkmN5MLr63C8BKWv_BswdeBFaccCawjsEgBMuJ4xMuuftAr0ZAzPHt_XFcK2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
الطلبه تحت هدایت علیرضا منصوریان در هفته اول لیگ عراق با نتیجه 2-1 مقابل تیم دیالا شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/103827" target="_blank">📅 21:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrEcOFEpi8JGr2X0mV2Njrnu8zX7hcgfLLf-cZNa1EMabb21P4cWGwPq1i0V3YV8F91QeRR5wqhEGY5B21dJPiABJodAhIZN3cme8BMO4pNnTYg_g9Grt7VI2Nlme1lUQJQWSxa5YQ_PJt1C61pee4HaheKK-fXRGq1XDuSx80nPk9iVgcLZCC-Han3Mium9Yxa_9nDyGHJxod5G5xc1uh00OxbdWtQX9wcSVjsXTBOrCGAu3ZU4xdVvARbvcLVOHnAeQPqnvWZg4wFEE34GKiezk2OftnihnCRF7mURH68OOJZk5aOV85BvemJI8FQn5358pcB4-K5Ixr61yiCtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از RMC:
❌
منچسترسیتی سومین پیشنهاد بارسلونا رو رد کرد. سیتی گفته فقط با ۸۰ میلیون یورو راضی به فروش رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/103826" target="_blank">📅 21:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e246017a9.mp4?token=Pnb1GOoUK_ZruXWSMTA20Drhc7Oo9bcpg3g4-27uFmGx1smiJ27iCRqekNzZeKucQ5jtbhfyNHvh052ClNVtGbCtoZFsbPFbg8P2JssafC70zz_6pXCtKE-kw2cC6PJqBPbgpFEY49BbcXrlFTCto5v21PmE0ixESVqpejdMWGzJj0HWa1EjjbBl24cU9VpGyk4ZKPlOeYYRddcma63V3ki5HaZBggMDZn7WSw6u-QJ9BFYpsUMSNCNLcBTU-tYA2c969xcQfv0zoJpaG7MAiVyZlkFwILXukKMjaWRBzrmm9ZLmT4gvStWeTQRlJScmdLt9TuI4U2zkTd_EOBiFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e246017a9.mp4?token=Pnb1GOoUK_ZruXWSMTA20Drhc7Oo9bcpg3g4-27uFmGx1smiJ27iCRqekNzZeKucQ5jtbhfyNHvh052ClNVtGbCtoZFsbPFbg8P2JssafC70zz_6pXCtKE-kw2cC6PJqBPbgpFEY49BbcXrlFTCto5v21PmE0ixESVqpejdMWGzJj0HWa1EjjbBl24cU9VpGyk4ZKPlOeYYRddcma63V3ki5HaZBggMDZn7WSw6u-QJ9BFYpsUMSNCNLcBTU-tYA2c969xcQfv0zoJpaG7MAiVyZlkFwILXukKMjaWRBzrmm9ZLmT4gvStWeTQRlJScmdLt9TuI4U2zkTd_EOBiFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیوی‌بیفوما بدلیل مصدومیت از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/103825" target="_blank">📅 21:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4096d1153.mp4?token=ERxXrLKcoXVKf9-6Cmmo1mvp-Cue3lc46EKGv32_wSuPHB1rMa2gSaXJ79GWb2MD9mu7vrvTbJ_huKL6Z-AFrrBzZDF54XwEIKjGSNY85Nd7EqZ-J6K4VTq-c-UISo9bGoBFIkV3M5pGHmmMwaZmjsAmU6SzN6aNCsiqcRKHD0wVQiPPo2QWw7qfehZt8pYPF1OuFBValjBghoojg1Y5YDJ-zXIyLW5gM7qdFuObLWAuCJCMkshOHqJWMNtm39gkmMImEVjh2gBPhYOjqoXkyFqSSknkjKTQyR8zbLika3qTU_DI6CugFEQMQcIPElbjff1LNOfDz2ZQuHDEhWCUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4096d1153.mp4?token=ERxXrLKcoXVKf9-6Cmmo1mvp-Cue3lc46EKGv32_wSuPHB1rMa2gSaXJ79GWb2MD9mu7vrvTbJ_huKL6Z-AFrrBzZDF54XwEIKjGSNY85Nd7EqZ-J6K4VTq-c-UISo9bGoBFIkV3M5pGHmmMwaZmjsAmU6SzN6aNCsiqcRKHD0wVQiPPo2QWw7qfehZt8pYPF1OuFBValjBghoojg1Y5YDJ-zXIyLW5gM7qdFuObLWAuCJCMkshOHqJWMNtm39gkmMImEVjh2gBPhYOjqoXkyFqSSknkjKTQyR8zbLika3qTU_DI6CugFEQMQcIPElbjff1LNOfDz2ZQuHDEhWCUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اولین بازی محمد صلاح با لباس تیم ترابوزان اسپور؛ ورود محمد صلاح به زمین مسابقه در دقیقه 58
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/103824" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHlVytNMsN8pxX7yUDvtS75ZBded8IZrLfrdbmiX3Ocf1MGN3AaeVEGNF_xdrsHt8nfUAUxibmnryaeIthmEig2zVQR5OxHrrTI6ulyT8eLwQWRZe-oYVjIrlqGOcbZJxHrrWmDWqVyCm2arXbUKImr0uwshNrOCDfTpy_74F4BKihP-XxBwxA4a4E0tdakSc2AosljP3mOSY8DGfc1_DREC8S0Sxbo96ol6JEkgphw-p3xBoK7IBMpJDYdZBru3PK_qZNyaXVmWYDpIA2y5Ic6mi9M9BGCIuRoL_P2F-NyLFIEIh_BZhMTHovYE-eOFy0cA47NDEYrVfMhACVsWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در غیاب رونالدو؛
🟡
ترکیب النصر مقابل الفتح در لیگ‌عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/103823" target="_blank">📅 20:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639cd87b79.mp4?token=mRo_BSL912MZ3vjFC7-Ab-nlRtYEdW33HeoBeR71DrNiybdJ0HUe9HsczgDPWmVv9jCJPt2zK15yXVHQuViCjQk5-yZTNgqZqwjUhKCPbTwgsM4uRnEB4DTGRWa6BV-dIYhw4AEqIpx6IAC48TUFX6JPecOb7zHKMAtpA_AAhjDG62E5Pq4CRFFLrDedy9R9qqpaBKmeqsk94bZRJ9l64y23mVSZ71rDDPi23GYzVabcdghaB-T7jZHeSpB173pW8W02wJpTs6TfKCgerSiKbRfPjiAGcn4y1m0UBYHNwKVLEaY8fleCDqKI7fQPaqt2SqK83z_9-ckPFZuH5wcvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639cd87b79.mp4?token=mRo_BSL912MZ3vjFC7-Ab-nlRtYEdW33HeoBeR71DrNiybdJ0HUe9HsczgDPWmVv9jCJPt2zK15yXVHQuViCjQk5-yZTNgqZqwjUhKCPbTwgsM4uRnEB4DTGRWa6BV-dIYhw4AEqIpx6IAC48TUFX6JPecOb7zHKMAtpA_AAhjDG62E5Pq4CRFFLrDedy9R9qqpaBKmeqsk94bZRJ9l64y23mVSZ71rDDPi23GYzVabcdghaB-T7jZHeSpB173pW8W02wJpTs6TfKCgerSiKbRfPjiAGcn4y1m0UBYHNwKVLEaY8fleCDqKI7fQPaqt2SqK83z_9-ckPFZuH5wcvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
سوپرگل صنعت نفت آبادان مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103822" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6e07b20f.mp4?token=hxvMVgG8aUUDPklm4DetFoKM9_IV598SjM1HnTTIkCJRyA_YOgrEPHGZslZh_mL3SD9wX5ffzUNuLMQiwo2ypjs2mtWg5RM-1X0YQtvGBvTW2QbldJZZU5w1yOXiTAy0p2Hdh38hCeG1LiQu-W7gfbaERLzSBOB-kNONfCCqt1U4Mq2gbmm9qPW591oH2SHKWL7wEPQ-2J7ItnysHUKCNY6FRNPT8h04ahMkVLq8TggfdyIUh5z-p5XvFeIFJO_MNDg-cJgOivlzR8r5xHBIgOAsz4Nl_seX9v2B7KDJWJ7Fo01lL1EPCtnNrtssPKcbHDrL9Lnyk1mrQUGEd0CRzkg3TergSgHOqCCzK9a8wdG2ACXFn4PfvkBH-RCbrxOvIsucksUkJG8j3m9XepGeV1_FZYkqIl0oIFoGh5afPr4phfzkt_PymtJ-6ooOOEBqzlXVvaKgrA0zzbfKfLtvnfFFq69BvRQqirfiyY3PU21LwRllEDtlsZBh6DC5zRq0Ft1MAYi0n37XYjfnivPt-lg4A0j6wlsZ_a-cgPUiYPvDkyWvh_j5djsoElkeDn5kTZfypo9IbRz9jm0KdMdAMsRj3botJlIt-DfZ8d7TK8hVXd00FOei8r_ZX7e2LfgsMHXMQh4FH_GO_DBkWB4Ch-FuAstbTpVIbNEO407FGuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6e07b20f.mp4?token=hxvMVgG8aUUDPklm4DetFoKM9_IV598SjM1HnTTIkCJRyA_YOgrEPHGZslZh_mL3SD9wX5ffzUNuLMQiwo2ypjs2mtWg5RM-1X0YQtvGBvTW2QbldJZZU5w1yOXiTAy0p2Hdh38hCeG1LiQu-W7gfbaERLzSBOB-kNONfCCqt1U4Mq2gbmm9qPW591oH2SHKWL7wEPQ-2J7ItnysHUKCNY6FRNPT8h04ahMkVLq8TggfdyIUh5z-p5XvFeIFJO_MNDg-cJgOivlzR8r5xHBIgOAsz4Nl_seX9v2B7KDJWJ7Fo01lL1EPCtnNrtssPKcbHDrL9Lnyk1mrQUGEd0CRzkg3TergSgHOqCCzK9a8wdG2ACXFn4PfvkBH-RCbrxOvIsucksUkJG8j3m9XepGeV1_FZYkqIl0oIFoGh5afPr4phfzkt_PymtJ-6ooOOEBqzlXVvaKgrA0zzbfKfLtvnfFFq69BvRQqirfiyY3PU21LwRllEDtlsZBh6DC5zRq0Ft1MAYi0n37XYjfnivPt-lg4A0j6wlsZ_a-cgPUiYPvDkyWvh_j5djsoElkeDn5kTZfypo9IbRz9jm0KdMdAMsRj3botJlIt-DfZ8d7TK8hVXd00FOei8r_ZX7e2LfgsMHXMQh4FH_GO_DBkWB4Ch-FuAstbTpVIbNEO407FGuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
احترام نظامی ابوالفضل جلالی مدافع پرسپولیس پس از تأثیرگذاری روی گل اول پرسپولیس به شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/103821" target="_blank">📅 20:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو: جد اسپنس از تاتنهام به اینتر میلان پیوست.  𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/103820" target="_blank">📅 20:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
‼️
🎙
پیمان حدادی: اعلام قهرمان برای فصل گذشته منطقی نیست/ می‌توانند تورنمنت 5 جانبه بگذارند که ما هم شرکت کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/103819" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad592f134d.mp4?token=Vllf5ERml1PPjMaEvmwInNQNbNV0UIDHT7U6C9Bf1sswaHmq3dldM-0ZbzJtfRueHMrcNZSyRo8mUzOUxvnnPbheRsiaUBobrfpmX70_VkaI4A6dkw0ST5fjzM3jkv2MnLOsbNyqx-AIdya8tLG200kM1WHNxGGLQvENuCR-qU5q_mOORASm4C9PkFYkq0X4xC1bCGr0KhTD4MOWo7LVDMfvEERc6fY-qpesDlv-dd1Ovw7DeNxiYQOfrZeTMz9NUfYuUILe9rWODYuklD_KVGUnIFqQNTBggDSimfjK11Dr83iFhREBgh4_qq1a8KVu-egPZLbqEklKEkYtnd3uMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad592f134d.mp4?token=Vllf5ERml1PPjMaEvmwInNQNbNV0UIDHT7U6C9Bf1sswaHmq3dldM-0ZbzJtfRueHMrcNZSyRo8mUzOUxvnnPbheRsiaUBobrfpmX70_VkaI4A6dkw0ST5fjzM3jkv2MnLOsbNyqx-AIdya8tLG200kM1WHNxGGLQvENuCR-qU5q_mOORASm4C9PkFYkq0X4xC1bCGr0KhTD4MOWo7LVDMfvEERc6fY-qpesDlv-dd1Ovw7DeNxiYQOfrZeTMz9NUfYuUILe9rWODYuklD_KVGUnIFqQNTBggDSimfjK11Dr83iFhREBgh4_qq1a8KVu-egPZLbqEklKEkYtnd3uMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل دوم پرسپولیس به شمس‌آذر توسط محمد عمری 15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/103818" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=piDQfwcdEMJQp-A7YBkrlqjoHLjyu3VEFIpQfhEB1CoLpG4YXgqRqAq0qP0Qit1spSMQn_mZdJ8AAsdQBTe9qJkv77cO7TingVqj0IY07GIYG1Bfjq_DlO8ss3MhC-fOP-AKLG6CML83bUYm7J_EHJefRPWIKv9tUAgQFO-Pn9nUs_45K-MCb84mEcU9naRDDXms4g2R2QJTUOzN9EqiqMAofKAX5WyujaqcSkC5aGRtOHfcwJqZARdckV620jLwlpVCLzbdeCYFnHS7bqBLucj2V3DfZQ8Mje9BV2hjp3UxL8KFy3-xHQxJMpjZ408v9ZExLhwEPZNCnNc7RU0PPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=piDQfwcdEMJQp-A7YBkrlqjoHLjyu3VEFIpQfhEB1CoLpG4YXgqRqAq0qP0Qit1spSMQn_mZdJ8AAsdQBTe9qJkv77cO7TingVqj0IY07GIYG1Bfjq_DlO8ss3MhC-fOP-AKLG6CML83bUYm7J_EHJefRPWIKv9tUAgQFO-Pn9nUs_45K-MCb84mEcU9naRDDXms4g2R2QJTUOzN9EqiqMAofKAX5WyujaqcSkC5aGRtOHfcwJqZARdckV620jLwlpVCLzbdeCYFnHS7bqBLucj2V3DfZQ8Mje9BV2hjp3UxL8KFy3-xHQxJMpjZ408v9ZExLhwEPZNCnNc7RU0PPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به شمس‌آذر توسط محمدمهدی محبی
11
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/103817" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6baeb89aab.mp4?token=ZAkYWtjhP69nqVNRRcemsyeSujlBz64WuNGe_KupaUlPbcJpgc9TFZCoynKp-6XvNZuYGfmAcLPh-oD0JjZu5m4YRXECfGqqvgxuevyYJkyvr0pa0aRyFbA7THJb6NhsoNVKcvCgU7xSRfokfUESZaRXqJ8qCknklYXZ38ZmCq0mznbRzb3PfKTAPYtzrn8GQhivY-zxNcB3Yxl-moN7CK7r3Kaku321MUtnmx2QyeCgxnZgm3_3rzYBGSd67ta4jpifzARg7VjWmA1irpJMtlreyQ6GBnq-x4RDFTtZOcQXJZdmPyUMiJUhkVEuJf4oA2Q0X7oBZbgtToIY1QnlqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6baeb89aab.mp4?token=ZAkYWtjhP69nqVNRRcemsyeSujlBz64WuNGe_KupaUlPbcJpgc9TFZCoynKp-6XvNZuYGfmAcLPh-oD0JjZu5m4YRXECfGqqvgxuevyYJkyvr0pa0aRyFbA7THJb6NhsoNVKcvCgU7xSRfokfUESZaRXqJ8qCknklYXZ38ZmCq0mznbRzb3PfKTAPYtzrn8GQhivY-zxNcB3Yxl-moN7CK7r3Kaku321MUtnmx2QyeCgxnZgm3_3rzYBGSd67ta4jpifzARg7VjWmA1irpJMtlreyQ6GBnq-x4RDFTtZOcQXJZdmPyUMiJUhkVEuJf4oA2Q0X7oBZbgtToIY1QnlqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
پیمان حدادی با کنایه به استقلال: یک باشگاهی فصل گذشته برای پول رضایتنامه بازیکن ایرانی 2 میلیون یورو هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103816" target="_blank">📅 19:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae65e3495.mp4?token=H4CQfZwXDDdWMEwQWfWKp_ky3JEervPxMNOIPVRk3RmdFBIqqpzUgEv3MKV8HPackw1zYo4-k-pcht4JleK7zSQcCnwdK5LQ7MmFUW61oPbwrp087HXeus07xao0oz-YWafLi-y4YT7g3dR5WavdmQ5HQ1PkX4KdiH7JcVWWfyKgw6kVTLSslEAjTmS25x-m2YoTLB-1ZVOTXZAhZkjWD8A3mF7NVpHpbzA2MIbVUn2cTB1B5IjO__fzsbsBs3sexlbcZh5nIekguDint_6zpn46A5tIXa8E7ltCgV7B8BEsx0j_zYLpkL43XPmDOlfgQTrXBxgV_HGFe5GEJtdyjo7vZxBQ0gA18t2q1DRaFOYuMIru8PPHLYevJMaZ5B_NwrXvo_OM9Wmd26_jzmhRF2mlcm2PoUZip4aBMRP0gpB_ZgAIyfUa9kiCzwieLnvBJwg-sxTkVKyEVpL-T25bxf53a6FVQqcLVTq7Rcp89wzQwBxggVMaUOdENYvoR6CwiQv2ou0Wikpk7tX2CBFOGtPtWmXpdOGfo8rVnsHgxiwj4FCYBL6rC4XyUUqRCeEsOfD6lPGRRKoxBWWR61GW_OqRMuu3LB7y1Mo0lqlo4bCgje1LVO_Dw4YRRgLju0sb0gKIT7sJ7WR4NdPnEkj4aS42GMB4gsIReLZAHHOc1HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae65e3495.mp4?token=H4CQfZwXDDdWMEwQWfWKp_ky3JEervPxMNOIPVRk3RmdFBIqqpzUgEv3MKV8HPackw1zYo4-k-pcht4JleK7zSQcCnwdK5LQ7MmFUW61oPbwrp087HXeus07xao0oz-YWafLi-y4YT7g3dR5WavdmQ5HQ1PkX4KdiH7JcVWWfyKgw6kVTLSslEAjTmS25x-m2YoTLB-1ZVOTXZAhZkjWD8A3mF7NVpHpbzA2MIbVUn2cTB1B5IjO__fzsbsBs3sexlbcZh5nIekguDint_6zpn46A5tIXa8E7ltCgV7B8BEsx0j_zYLpkL43XPmDOlfgQTrXBxgV_HGFe5GEJtdyjo7vZxBQ0gA18t2q1DRaFOYuMIru8PPHLYevJMaZ5B_NwrXvo_OM9Wmd26_jzmhRF2mlcm2PoUZip4aBMRP0gpB_ZgAIyfUa9kiCzwieLnvBJwg-sxTkVKyEVpL-T25bxf53a6FVQqcLVTq7Rcp89wzQwBxggVMaUOdENYvoR6CwiQv2ou0Wikpk7tX2CBFOGtPtWmXpdOGfo8rVnsHgxiwj4FCYBL6rC4XyUUqRCeEsOfD6lPGRRKoxBWWR61GW_OqRMuu3LB7y1Mo0lqlo4bCgje1LVO_Dw4YRRgLju0sb0gKIT7sJ7WR4NdPnEkj4aS42GMB4gsIReLZAHHOc1HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
حدادی خبر داد: با رضاییان  مذاکره کردم
🔹
او بازیکن قابل احترامی است ولی در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم
🔹
با وجود تخفیفی که داد رقم درخواستی او در بودجه ما وجود نداشت
🔹
عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه ها بود ولی از سقف ما خیلی بالاتر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103815" target="_blank">📅 19:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca7dcd99c.mp4?token=KgzZjUwt9S2Csw7cjedWkUkOqBjKd3KYIBJ98uXzUzf-_8h-BlXQWqgxlUu9kJTdp5twj1_dnY9f2gxqxPr0lkiqIH1gr0JbaldqEJQFm6s0drRySiSRgB_2Wa_PYpmbVwF_MbJzPDDf09swM2s43glzoTRremPE_Kr0JDLbG_TfDYyapYTzHLHK_E_i-gdTVVmicZiWjNXur_o0TXXGQyFHLeuA9vulSUjY2KkXyvYRMjr7xgxx7u2vZUh4BXv4g27ZqKmTbyFCf6_pmkM5maP2P0a1C10jCL71sRihBYO74KQ0YPDvsuzofiw5E2AZwlLXIegC4aIx1p8zk6As9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca7dcd99c.mp4?token=KgzZjUwt9S2Csw7cjedWkUkOqBjKd3KYIBJ98uXzUzf-_8h-BlXQWqgxlUu9kJTdp5twj1_dnY9f2gxqxPr0lkiqIH1gr0JbaldqEJQFm6s0drRySiSRgB_2Wa_PYpmbVwF_MbJzPDDf09swM2s43glzoTRremPE_Kr0JDLbG_TfDYyapYTzHLHK_E_i-gdTVVmicZiWjNXur_o0TXXGQyFHLeuA9vulSUjY2KkXyvYRMjr7xgxx7u2vZUh4BXv4g27ZqKmTbyFCf6_pmkM5maP2P0a1C10jCL71sRihBYO74KQ0YPDvsuzofiw5E2AZwlLXIegC4aIx1p8zk6As9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کنایه حدادی، مدیرعامل پرسپولیس به استقلال: فصل گذشته لیگ برتر قهرمان نداشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103814" target="_blank">📅 18:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDbns9F6Rn0O7jD4z56GzZ_6g-2Z4bIRVKBDY6RbOhzEQrIKVY8VTqyqHzTii3uGvMa3jRQHOj5aqI0TyHkhbQRNyV-oFYN1LcRbfxHLgSNcwi-nmlcR0JlfOOw9Z-l12J9TQiYVzOl4Cw7faP9Ok1vT_aoX0V09uzVHurDlSogPdx-yMLrg23INh1ISfG9JLLc8GBRi49VJmpybu01-cVYMUheEqv4J4YmIMzTex7YEvgFEPrjAmv1GMJYHhStVdR6RjEAfylwRQd5Tn9oBmVM0QlEUQNLJSXx-khT8ltC3lI6ZnnX8grrNEDqLaRXrAubwGfKz_phgb6FGUvDzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
هفته اول لیگ عربستان
🇸🇦
النصر
🆚
الفتح
🇸🇦
🗓
شنبه ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103813" target="_blank">📅 18:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHWx_W3Mx6Ixs6qTV45P2kKV-S5huYsFwPRzeTraLB1XE0cNKVJK0h7FtTIm8LrHQKHMqyDsbXPvfPoWsNARbFs4OLJFKdlFTObtOJ0udac9ISdUYFzdqvFTLb87n5yapf7FRF7E3zTAZBS4DSYsxh8_wPnK4VlDhB0674hgnjOFHepqdfVoL69PVjClye2WF729As9uZrAQGpVWy0FrtpDpxME2gRCBAfPmdSGgq7SGX27huYK5Z8AzE1J7uzvyZSrvhO4dHOkFjOUDFwk4AfSo-DpSiuF9tInn-Gv8yzmi8GB7NsAuwR_UHjiEXPRVvx36ZN3jRFLqx3x0H-N1LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیبببب پرسپولیس مقابل شمس‌آذر قزوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103812" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103811" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjWy8SL_LCZZpfQT7hfVgtfTGvxFyJ2QCgVU0WUT5hEqt_zyvwR9IFH9p1rvn4nLeqQMb8XW3s9ccX6p0hL6HWF2CF2cRpaSBYaRPIucrJAGbxWfY5rO2JC2BtoB_S6y423KI2crr3e3L2At1DvyqiXW4Q8SaaC5osK9uTd_AoMUb_F2-qmlAVMP4yC-WixZnT98LG1kpN31d0NGP4Kr-ialIu3gHwrNTtNPLqtvnaDTzcxdW37lvDAkPUtdSyHrgLYu9JITfocOX3geTPbcKqFn-kP0XuSty1bA-NBMTdksgbbPyqCG8tH_HnEB2ErTofRnjay2IwDWCe40b0gLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g24
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103810" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb39b1afd.mp4?token=QrKP1nBpP1lTH3FOGec2nRNcldVXvEFFVdE8KFDHSfLGvDNv8TMZ5SN13MG5gWPdiRK1vqE_3DL-iNyXPPcvr0yG-VX1lfN0DPI2aR6Oe0xgvA79aXgeXM5uCEDOt-6AHvC0Z4lpnVOaVoYE6KRTsdT2GXQjUpZdJaD4U6dFWOKPthi6zsILTr7d0GTuDltbXD715AHChnuLp8vHWrEnOJlpz9FyTuBK-VTDJWJamjO6n3ZR-IfuBDKuAoFxj7NA4665XcbPysmkeSt4fdPTOjFLLpINwpLesTTwZOX1bZbKaxLgPcVXHKsD_vJo114lTbu-2kAuVZgr5yYvn3lC6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb39b1afd.mp4?token=QrKP1nBpP1lTH3FOGec2nRNcldVXvEFFVdE8KFDHSfLGvDNv8TMZ5SN13MG5gWPdiRK1vqE_3DL-iNyXPPcvr0yG-VX1lfN0DPI2aR6Oe0xgvA79aXgeXM5uCEDOt-6AHvC0Z4lpnVOaVoYE6KRTsdT2GXQjUpZdJaD4U6dFWOKPthi6zsILTr7d0GTuDltbXD715AHChnuLp8vHWrEnOJlpz9FyTuBK-VTDJWJamjO6n3ZR-IfuBDKuAoFxj7NA4665XcbPysmkeSt4fdPTOjFLLpINwpLesTTwZOX1bZbKaxLgPcVXHKsD_vJo114lTbu-2kAuVZgr5yYvn3lC6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های هوادار شمس‌آذر به مهدی تارتار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103809" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f0533ec8.mp4?token=o6SN4Xe5zoYe9n5YGhcueoinGgXLaF_ykKkl8Wp4xykX4FXjwPJd4WnGHpKwhLGTdL-I7_18Yy8RON3mdsprHi3ejPsseqS4bX3sh4nUEWacjTeo25JfP6itlaXjKJjvDSVKO1nHDZq4FsIiucKk63c385HA2QmlBO2rDCBGb0Emk-97XtTgAD9IC3PgS2CXCJpwhUOFyg8_yU85vOfA8hvS0HeqlUj6OanU6NL3j4Qu7MhJUxH8lSiZBTGt5m71H8Gio_1vxhLx2EsROiQxD5o3haGiEynGUf04CgLsCTDy0hNMvxn6wr8hK-yIVReuf-WMR60jbIFiB4_gGk1Zxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f0533ec8.mp4?token=o6SN4Xe5zoYe9n5YGhcueoinGgXLaF_ykKkl8Wp4xykX4FXjwPJd4WnGHpKwhLGTdL-I7_18Yy8RON3mdsprHi3ejPsseqS4bX3sh4nUEWacjTeo25JfP6itlaXjKJjvDSVKO1nHDZq4FsIiucKk63c385HA2QmlBO2rDCBGb0Emk-97XtTgAD9IC3PgS2CXCJpwhUOFyg8_yU85vOfA8hvS0HeqlUj6OanU6NL3j4Qu7MhJUxH8lSiZBTGt5m71H8Gio_1vxhLx2EsROiQxD5o3haGiEynGUf04CgLsCTDy0hNMvxn6wr8hK-yIVReuf-WMR60jbIFiB4_gGk1Zxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
اعتراض
علیرضا محمد، مربی پرسپولیس: چمن استادیوم سردار آزادگان بلند است و باید کوتاه شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103808" target="_blank">📅 18:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBIG_SnTMgs9qaw4vGDPG8nWxKKxQ61nIWSNGutO-EnwAIjXBt-zX36ApSYBJ6Xa_l7heeSPAKa9_n0h3iKfOPF8veRGLHuIHT3A_IVaLYTIAQTdMvncA_bQJpaIxo5NShX5wiM5ACsRUg0_tpXTJ938jFZCVTVmfRccByGUoFiuYNXmXfxLEqQKX8eKrsarewgArmXxvMyOK8c8ijVq0O2O6OOtmtrdx64ymA7cUvHdND5Z3ktgGqSxvo_svYPNGh5pPu9CVQPxNSShtnQFzmKBocvy2lNDVUO5pxA9hbda-FP9iD_Z3BvteWpu8HMB1VwogIi0_sOE7j2QTS2S8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
واکنش کنایه آمیز شدید باشگاه استقلال به استفاده مشابه طرح شیر در لباس رسمی پرسپولیس با ابیاتی از مولانا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103807" target="_blank">📅 17:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103806">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bdaff9e3.mp4?token=Mm5D4HDdmOGFMfShlsviMeai8GLABaxeouVYc3piX4t4F17-BSzMxwgwf8fzRsg4ENTM9lhYQhMVZ52II9IRupeNeB5A_42C3-NkVGlye3F3xBx_5GXWGSviHYkoopgQ-pPNXu470U2MFJFNmSjHkdCWMUWI-OcPUVAgZ6gJY_0zCEK784aHiK-qUbXJX5TUlvHT19g_nDDa_Dsx8PzlyZD44IqB25SGK3xeSDPZW9u0pRBI-RMCZYgGSCrw097dQCsFZ_G5XG16Upe2Snufube9O4bypIeDkzjCiK5Wn4t_d-sHzLxvYfwjrIjH0MxGc1kqxVMJ47JnXSyc6VOBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bdaff9e3.mp4?token=Mm5D4HDdmOGFMfShlsviMeai8GLABaxeouVYc3piX4t4F17-BSzMxwgwf8fzRsg4ENTM9lhYQhMVZ52II9IRupeNeB5A_42C3-NkVGlye3F3xBx_5GXWGSviHYkoopgQ-pPNXu470U2MFJFNmSjHkdCWMUWI-OcPUVAgZ6gJY_0zCEK784aHiK-qUbXJX5TUlvHT19g_nDDa_Dsx8PzlyZD44IqB25SGK3xeSDPZW9u0pRBI-RMCZYgGSCrw097dQCsFZ_G5XG16Upe2Snufube9O4bypIeDkzjCiK5Wn4t_d-sHzLxvYfwjrIjH0MxGc1kqxVMJ47JnXSyc6VOBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
هواداران شمس‌آذر خطاب به پرسپولیس: گلگهر سوراخه گل‌گهر سوراخه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103806" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64759a3704.mp4?token=mfLS6TBY1pvPeHTyYFrKtkzCa-ZvG-oBUzHv-4yoDFZm0LyLUC7CuRy5l9cgKFZ2fnxOzVm7pZwqbNCu3tN8M6n9LKpTG0wPJ62yqQWk7PeP95C-FpWXhWx6_PDbd8TCp2_pEo_8_xvrrDeMUziS-x7dXUyaA2d8UMIPY0ROUaewW0c8tQinEHaeev_MwAKWiHRZyjyKTB6TidREoLFr8sKHbnlIBLVfRgu3UEa36X-NafoEJiI7quVjjcniStU1pDuJ9A8TGGjb8X_0DYl-n9bHiLSPktBscCbm8hSAvDTPS_LOcpDRrz48yGYqMY-XS9Z4X4nxGs5qizqGKONnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64759a3704.mp4?token=mfLS6TBY1pvPeHTyYFrKtkzCa-ZvG-oBUzHv-4yoDFZm0LyLUC7CuRy5l9cgKFZ2fnxOzVm7pZwqbNCu3tN8M6n9LKpTG0wPJ62yqQWk7PeP95C-FpWXhWx6_PDbd8TCp2_pEo_8_xvrrDeMUziS-x7dXUyaA2d8UMIPY0ROUaewW0c8tQinEHaeev_MwAKWiHRZyjyKTB6TidREoLFr8sKHbnlIBLVfRgu3UEa36X-NafoEJiI7quVjjcniStU1pDuJ9A8TGGjb8X_0DYl-n9bHiLSPktBscCbm8hSAvDTPS_LOcpDRrz48yGYqMY-XS9Z4X4nxGs5qizqGKONnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
کنایه‌سنگین هوادار پرسپولیس به استقلالیا: جام تخیلی همش برا خودتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103805" target="_blank">📅 17:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5F93cgmm4zujiq4_FZfJH-PEm7DNDLQgBoQjDySETTK1MPg_tbD9snbGyvE7J7FvsC1hOVTwc2J7ze-3tggff5F0GQjwf2AvK2HtqWGPftWk2QTRgnuG5_l3J9En-vuXkLvfEOfHqhCxrdiLEia4fHDNXcKy9qaa5QKByQgqbdSnA4puwldfFQw4JDVc2nddMttofUnlY_4WfLPQ7TzJpdNLOWl5KhqAmup_PsFpIrcCXOU3BKlyRQVBkd_mtfTHQkay_0p6FKNTG4muANHxt4jjHAf41EeDhX9GFdUSgVL11EtfEtu4tOLsIGfZFJgL0i4mzVoj_PIe2QBoo_--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbP41aUATSZ1agBSxB3ier3YzohKtlVnkOoDHT1UQ1uPT9mmgTKvQeCqyeL1RxyZ-iVH1zcfUNgqcvHBNgSJJA6PgyHIA2Oq7TuN-5hzLGKzSulw2n9tChYc0GU0DK0MNpVo_XG-xSjLL2S41Jys9xwA122besOvAJxCc3zkZrmuJ3aipPTswQYyqGqZ9DdQSRj1gipWJthIiAd74p0DD2OgivfTSH9waA1sx-kiEkiYFMl3V215sAi4oM-eEIYiWyazRePZazSO4WWe7yIhZhsNjHtZHVHYYYTXCgNRa7XdF5ZVoVUYMvgFmQV-Y28gDkmBwY9ZyScZCnlaNmjnJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAM_yHZIAWyCay8I9uZHQTqtNzZGO5oLby61cHz13CAOt_1Z7o3y-FlO2TRYZpuDbKxHaVqYaduKF2CPB9JoF-G7ONmAxFWRmlbpF9uqzJuvyssfInknSgIA89Rpgpt9kSnDC1-I1NY0wmUozxi58-nkEriqeL9YbeWXQGy0QBgvBVvbsiA9crn9ITlZLiGak9gHnZ3O614vdtLIeIFfaFwINhZTXFhqcj5DheXPEwDpgp-nwIUu_xgGTAWJnW9JRmjXxlIkpsfRnJPEXiKNDMTZF69VkoWWuxU587L1i7mQTNgkHgDuVyzkyiZIfBWjF2LCQR1rGEjA2wdzwjgjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9k7kssBL5AvINrfmiG8cJCxDNeCWg4x_cn5VR0XTR29nttGznAaCaFAhKDxHSC3Si4lU9sl3cpY2FIP1lke54Ck6CAwiZV8Jx2WpIoQZsZK0zLxoVXOuJDRlRWDcVnyVETk9sQ6XHWqbGEwC9eqvOZvVfsniS-oS2zTZbM5tjzJlHMJ1qk3j3Z4tcHHkCc-a_OVxe60xyvAnEC7KvEj-GZl4_FwTGbkdxTI-jdtXs11uTFezxKoQg1qqJHjJiVqGa6J-RwzxKajGAlJrIjmjhhO3Im_-L_GKquJgFcEE0UyiNFoE9pn7hYg7rFv9wpjPP3jz4LUGIhe2yAO0ajecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHEz_M5BHgO5wxOa-sOsuN6BToB__ULFMXomxX63gyuynjGhyl0Rzg7CQ6syhmgiCG85uOa5T7cQXPGOKJRxw-ahp-3t4QliKu2GRqix-7_02QD1BUutxqqtc-aJwW8mWPd226BS3f4UC0YLqgH2ghJtVW-Nv7NXrsedr5l1IG0ZaMBdx76QYMQBIgXZLB4C4DIIDhlGsf9jYVlhYeWUiFNAdHIqOkMFeZZ0CABO1XJ5ev9ihmU_6LZxXUC9fyYqrt9HCiM2YPqHofOonCm4sgboKWG1m8_bKZhbpjPqNDa4rG44BI6CVpOCX2uA65Dr78gFY5S-lx3EgMYFMAXU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nl9VWQ--hxMqXSF-UJEAMn3wYBvDf8XCQBzV0DXhIm_rkxLeNNifLUHQpasc0XOTitx04HNj3QwiuT2sonj2-Wsavpas7miFACnjQE5Hige84z9QUlxV_WF5vKf2ZwlxmIUyyMOmIW7Oi_-NFqrFB6PCZmRgGSPq7i75gooORgCFJvWVNVFWCbGSvTRPhQ7Y7UaHra85URoZEO3vxB_sa9PZ5Ej0eXbQseGjcW1rBdZlntyRsi8uZcg3W8oPqfcpvfEBX2CGwTUKkm-6Nugk5u7Q1-Lu_Q7Z4r3sXopt8eQ4SmKDLKoQTLeC3Snf0mI3AM5FSRD3GgGxAm6xZdBpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IzUqz7RPOkDAo7hGSkDywRWybikKtZfW74CUOm7kNHZ97L8Co1oU9xs1Oz2ItJsEqT63_mPBN55RWUJ6oYeObgw0G1OvdiQpT0_FVY3vTJ2xO1SuN-cjmWvlDcRyJeFENmd6VqJSdeRAiSBO7AiGXYbbyc73MgOIsy5G5epYGfyeRIw0rtraI3498hOTTnIcucRKg7_Sh9VDPC89XKcMx6ZJiCXzjCxfsQwW0yWsKWGYkhSd9NmNlIyi9bt-hwEW9gcm1YOsHdI8u3QmxvEb0i5gI1jHPOh6oqZ5PgrAQG-2WJbcYUl1OVTjUB_picVWosHOlB_ZV9DXGYuUOCvOLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
کار خوب و قشنگ یک هوادار بانوی استقلال پس از پایان بازی دیشب
👏🏻
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103798" target="_blank">📅 17:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935fa0a60e.mp4?token=Axs_E-PhfmQHPg-08m1VV03jeop7OOq3aK79Oq1v5YSFTh8jnAiIRmtig-rLIEXIe-SDiXyrvX9dXkgmC7jrrA9j1VGq_BLUNDc7E2NygRNNGFVsBIhsu4Q8-WFtDhah-NMcioNlSxQeSAeruPjuVTsKD4LRbxTQViqdtTUGH5ERcAcfoUAEpoX4VRVtYkJra3yLGsAO1MVCnJrrfLFhiJroJyyW_-rwjgtmcVE0xSSbowndM4VMA0AffYSB73blLiYMtGnrJFyXFYVRYOFb3nlhHF_vwLf71u2bkMqHPy9vhTokH_xu2FfgJOJlgImN38h4pEt7H6tUfWKxjp9FM0i7_B55d6IysHIDgcHJphepWyMoK1Qd1N388LTX3d8KQsgMQgFQADAIfFGxUt-WAX2EB6LOqTxqWnftX9foe1NW7CapUkIhPiTBi-PTXjkXjgvvLDr6PgMlaqqK_CVG7c_884JaJHM-CqILbZwTs2gdQOD_azycb0lp0bead9Oh5aEEQ8wvYBWAr2ykAaA8SgagBYDFkO4jQF01-jpVcHB9V4O7rfSBZVvboaXNXbCLaCiHru3YkqnNq5wC1Zl8KJ3rUNzbPZAfip0Tp3SfcvVtm59veBXp9LmqyKdTs8VkCxqzVa_atApgrld_ivdqgo54Lrg3k-6oTBffxG9r97s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935fa0a60e.mp4?token=Axs_E-PhfmQHPg-08m1VV03jeop7OOq3aK79Oq1v5YSFTh8jnAiIRmtig-rLIEXIe-SDiXyrvX9dXkgmC7jrrA9j1VGq_BLUNDc7E2NygRNNGFVsBIhsu4Q8-WFtDhah-NMcioNlSxQeSAeruPjuVTsKD4LRbxTQViqdtTUGH5ERcAcfoUAEpoX4VRVtYkJra3yLGsAO1MVCnJrrfLFhiJroJyyW_-rwjgtmcVE0xSSbowndM4VMA0AffYSB73blLiYMtGnrJFyXFYVRYOFb3nlhHF_vwLf71u2bkMqHPy9vhTokH_xu2FfgJOJlgImN38h4pEt7H6tUfWKxjp9FM0i7_B55d6IysHIDgcHJphepWyMoK1Qd1N388LTX3d8KQsgMQgFQADAIfFGxUt-WAX2EB6LOqTxqWnftX9foe1NW7CapUkIhPiTBi-PTXjkXjgvvLDr6PgMlaqqK_CVG7c_884JaJHM-CqILbZwTs2gdQOD_azycb0lp0bead9Oh5aEEQ8wvYBWAr2ykAaA8SgagBYDFkO4jQF01-jpVcHB9V4O7rfSBZVvboaXNXbCLaCiHru3YkqnNq5wC1Zl8KJ3rUNzbPZAfip0Tp3SfcvVtm59veBXp9LmqyKdTs8VkCxqzVa_atApgrld_ivdqgo54Lrg3k-6oTBffxG9r97s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
ربات مخصوص‌استادیوم بایرن‌مونیخ که در محافظت چمن نقش داره و کار مراقبت‌ رو از انسان‌ها گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103797" target="_blank">📅 16:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajF8gODGeKVmnGVcLeHrUp7GU5nbGp_YXOjTrsnVU2hqr1Yr1UOKhoSqip99qe4veldxlc7KSW22Pop0MBF8ts0LwDE4h3_ucTUQInj5jOn1wTnuuJ0g5miYpiIU-NFQFTCyrlijbbaG1Wq0807Chitk3pJ8ROU4rVsuBTMdbGlt0zz3G9WxASj_kYUI8WpqBeFpbJPxibcmo36e7KPmAXahhjyVlJNyUjGW3h6uqBu1MWC_UiVgQ4lMsexpniomF2lnINzXVryScwmap8ywCPPFHfklpr5Do7TNXY4L2_3btiivvR97P7nHhs74yKq6tw23uiAA8eeOAxUyesMZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103796" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbEAS4W-2666XI4G0lN0oIL7xPJb7cpa-F4WpuSD2rJInlA43iL5hqM42YxvPt7HGW1jQQ1aoloXJbJgfjWJOAvfwl-qWjk96vVvsikV8VKToqKHebY5OVV-JrDOV-mYxuwpAAueK_dK3U9UDzwwm_b4s1o0zTZDiGb72r-v8sIukzIRbi-1iSJpQ-ATkrffFENCIom11spDtT_17kAlB9OWHctPqEtN4z7QVKBjxjoDqJ1YCNgKPjpdjPrt1kpEpSqSyhN1tqJvNppkDTpUbdWUpX7czjKQ-bhNHgUw8EB-kFeO4UUB-sdUDgra-EfwA7pOaTAHzZ2pJjQvox-Biw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غلامرضا محمدی سرمربی سابق تیم‌ملی کشتی آزاد هدایت تیم استقلال را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103795" target="_blank">📅 16:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfNCqC8-n3kcd3M7z9i21IN2sVEKdjLEvA7G0dqG7bM7xEeJDSRg5aM43vqfF1YhwLTpjuE9AwLujJQkePDsaiIe_bcg_aGd4M0HGt57XsB-hV1V5ktfCSWAytRxqSHOQzraBc4N3_f5fVDKxlYRXX0N4keWXB6hgMe9Oo-HhNe1PS8RkPNQ9NHMPAuGj4XSbdX6i7e014dYnTi5X_isDs4kNVM0Y-iKOxgE4Z9rERbPALWOvF0C1b0zpAoprQ1TylA14I66w794YZc8cWDlOB4x7TXjEPNVggTXPgVmYIwCNznKY1MTHX321W1Y0VFmywDS41VVrJD8j-oq7jVHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
جزئیات ازدواج رونالدو و جورجینا
🔴
در صورت جدایی جورجینا ماهانه ۱۰۰ هزار یورو تا پایان عمر دریافت میکنه
🟠
مالکیت خانه رونالدو در مادرید، به ارزش تقریبی ۶ میلیون یورو نیز به جورجینا واگذار شده
🟡
جورجینا حق دخالت و ادعای حقوق در اموال رونالدو رو نداره
🔵
نقش جورجینا در تربیت فرزندان و مدیریت خانواده را به رسمیت میشناسه.
🟣
در صورت جدایی فقط اموال مشترک بین دو نفر تقسیم میشه و هیچ دارایی رونالدو حتی یک یورو هم به جورجینا نمیرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103794" target="_blank">📅 16:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103786">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRmOzSz2qwHsJ2fqYMIzm-dVau2WZU20ZtQk8_PWTgBb0qQYFRQ5bcS9Btnvj3xLXp6jRfeDvAZc7dYySBIVxaPqUSLs_gOhJEBSyIwKJwOngc5813OdW7yluU2egYFhjg-gN6ZLYQ0Sf_S3d2v_Bha5HkhYkWxCyfwDg4PhhkpAMS--RRgHyIto8eDDFLIJsWtkX8-pay223fujtgLUyfRZbVrbN_Lm4JwjskGGMMV_AkgBnA020ERDxVD-qU9fJcmbeb__uxGxszI9hubchF_Pmx7qdjg_El2wkGsEdrQqm4wz1DGowIm-c7wjEMkCRdcbmjalcjrVIaxRkKYEkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpZscNDL9_vivoGx84GOAb6SGyae4KICqIV7UX_WiZWyFLNoWcw4_3IxuKzcz9KxXVtq0wTeXJNZxPyeqt-bWuIIscF8X2nomJmQyzbfOCmI2maAMKvMdrX7s-FcFl6CQDKiiWSJP9bBjlZp_uo3MnLtaZOAaC7Jf58jWeO7RXETkqqshUdNlVdUBKSDfRg0AJNQWDDwNFhP41XpiJWKUVZYDnXbm4J4zQLj3JCw8ND0vfvZfCBAyNwqSKVwB02XoiaV4Jp2zTan1UKG-ubqkzyUIkqyrIhM6YbVmXtt9jJprQyKTxaHGAPiK4p3b6lT8jHhBO5pjOOoVXNdl92L4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUKySrE6Qe6paj7redc0QfEYl2WjkeQFQ9f4r7ryN5qm1IRnvg_O2GirgXOz_AdqgX4u6mweDIoow11aJ8Ofy16tWIvgX3ORssY5S4tc7giNUCuhAj8ZX4hdz4lkdFsr_JDz_e1nJ3DfyMuUeXpAmxgKWgzAx-jLOjwKvA9AqRN1ukjO4WeQjHwcbeRjttvt2oHpuOTD6fnMLXX-RXBqeYT-hvtO8QkX78UEuSYUMzTVxANnHTrKl-XdhuSSYUDp7uj68ZJR1_LxRy9IOZaK4XLxeDKOCvP46PaQ3o-9Mpl4i13s-Hd7vLLI6PFgIftTVy-fiRDziddXGQ5-VnmWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IuLCE0bOp2Jimv0V_GfTcW1THn-dj1A1LOfjC9DePcwECDvzfFN7WMzZhWkf-HkJLB_FiN1WcGzTcidABj277B49797CTWMV5m5TOdzp4H-rQGitRuOn_-YPfC1nVNPjZup_5pbA4AMKWaFYGUO_ocP2sL8qG7nHp93-Jd_rnHVR4OrZW64hr6tsKULByFBrs0f6NsgafvRsUACTVVr8fXkHxghQ_o2cZBPkkZLYmWzeNSGBP9Mmj3J0ABuDl5yIhsq2lciyHTqtt6iVQss3fYAUzU0UYHCkuyUouuLXchtsnpwzoiQf6BLFAMfzS_7suIfvCgJ_7kuMdGzAF5x03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fL5JAL2FLaYESq9vm5GwlkMybnoSW9PXudCIvTV4aZmUmhuJFI6x5J965nLi-f9pRN4xfPLh7jMIA2kHAZRDSrluXfy95iAiNN74c8ToCKGVp6JW6TpMFwJ--vPfQmQNyrOT9NhdNtrxTYHBQvMrMa3zMhlGjA8NNzCE_p0bJeWala1KcOr1UApyOykf5Tt0i9ozPMqeHGv8ng7uVC7upLRNELW-CXn7evbOS-J1nUeqaAyd7jmxXYpcu1UGC7ZJLotyhrOZCh4Tod3M0amIg-C1TgmupwARCnG930eqC_Y4tUL-jNm77nHwajkDsu9lnl9fy-8jBYEc5OoL_yWM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAjFi4EIY6IoqNAWirWf3BMXHaeTCUGSkYP4yuPlvjXTyISPYcHgCJJEbmmbVQqRRlZnVctj9_WzYraW-w_Bi8NT_9Iw8riKbecs2B2CeH8BaGwLamYmXwS2XbUM4N42E6yS6Q0zTAj9Zd8GhN8w11cCyElr3VzBOxOKL8niMVh-4v6P1O9nw-GwBZQP63tmNe74jodxXlWS9styQhjpDBkKYdyN6IediaWk4RWT91-8jQiqSbh_Zo9E5i-McNrekNDC5cBKNZG379fHPY63qBcq316y2HLwnrGjQVyaim278N0fq45aMD1pMypvPUFL4RFbzfv_aNw7eajrO22iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-NxXPlaiKBxJYfgXJU2vyhjYPLu9yB9IjkE29reF_hG95IrvanCrnmouqXGd_djwT_rgnGUmB1MLq-ZaqL6gexyxKuXDvRJGAeGpRoCq19FjounHmKJdcNYlPqHpD9pHj7rB-oL0pfT5aVzROjq_PD9eE9VDzxXcJhlNPsl_ahVieCg2y5xHj0e58y9JpN_89XpnL5GUcE1HivWRZToPW4bCxltBN6IHVexsifIp9ohQiiTpQQQOvidcSupnnt7p-maZKKDkrVZO1F-9O_Xe5Ldau8w7hBPVHD32_YptRuk76AjYUOlk-BaS5lmi-06q1tfcpsnbiGZkBeRKlE1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6ui7SgtW6uFnQe7uq_uaSOGt-4TzrFa6RXGxxsDxEF3uF9O1VF1drXBd1ZauYBfA8u-BRWAEPPU8eXbddOqhuplSkXmkzmRd05DANfpyOhHSqQYCu6ovGYWozZCQH9rnauIBOmezoVyzf_fHXyRLzioq4bUMr1DEvkauKrW48itbH0TdHK5rqfyrgzlVdozCYli1q70Ndc5qCAxO6Fei73molGxN_nUCz_shMe94CRMibmpPSorUe8LXoQUbqG84UIUwRNbH-nGFANV2FquwocjS_q4Er_yhb3zQYxhn1A2iN1QEnjCqYAMFjMPRXr3NEkcaAYh30CqAfmcsgGprA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رامین‌رضاییان خوش اشتها
👈
😂
👈
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103786" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeP9zwcEg995hJMsApblJsp5YLmM6NDZG73cCYSR840I0nzc7pGKlIH03SOTUute5VETo8Q63QULZTiPrKH94hN3GJtkWVrB9GrigRkfTGDKhRMQYtimDraP-ZlysnFvgvzoqJW1rhTeyPehfynRQDZLx0vvKPVHVjFBF0QkDRHElDttc1atdD4Nx131ECN0v_IDnG6OXa2wjDqIZU-oB3e53ayJoyNw7tdEKMNpowkM6ju8j7nJeNymk7biUIFELEZ6-wU_QHnHSJCRWGyWkDL9nLLDe6lrIkmjp4UR1dLM7Op46WlISucQoKyvJ2bFP1Dbc5PPG1bsnc2q9b_gWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMQ6foCFsIu-kSAWX-IfacG1Tn04rpw6cZyRm6p496a6w717OjUDCoi4LSq-D3P1Qtt2dFPotEqVwzL0Qjc6ZIghngxs-spZG54BzXG-Qe_fZ2H2pRLevVBNbL-3KCgEDx0L2DPa_QS9dg2Ai04SJHsg5RX91tm3-SVpn2YG2sMBp6T4Xegan1p1k3VTuNjq5vciaNgVP9lmPi-hVJ577X-UWywHY4_4WL5Veaw8fgfIUoEIkg0kq0mFFPDRezsxuTerSjDfovPkEjgKvHaH3oFtxZ8qa0fyX8zUE21fvavmn-t1IzKzkcWP5lN-197YOg6hEw2e7NhheFVW_h8plA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
یه مدل ایرانی - آمریکایی به اسم جول فرشاد مدعی شده که رامین‌رضاییان تو ایام اخیر بهش دایرکت داده و خواستار بزن و بکوب باهم و سکس شدن. قراره بزودی اسناد این اتفاقات رو منتشر کنه
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/103784" target="_blank">📅 16:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggUDLQB9_41ltAz5FdGmfl4OxrkEo3p0Giw0TWKOANaUVrdDeOqvNgz440Rp1sAsgoDABUCsjQ4Ic9bcDO64tUuR8EiBc2JMRlW-Wk1aB7G2v3exROsF51ET1WYhsO0EQg1aGgsEnAd_JFkL9zPeRj1QTZTWAQ1jFc2I_2rfNNH-9aq-5BRefJ2QaA3cO0GlfJ0Feg3V_hUxjvjiA2LZl6_KRSKafOAgpCcPG8TIYqrNdy03mcygQvqD2Iix8ZTXLzLBearFT4kGcqERgV2tvjkncIcdhwBt3ffGgAgDExnLEer3wv5rbsh6fug9rZVt3RV74nPQc0KIRgo700Cpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
عکس جالب و تماشایی از تمرین تیم فوتبال خاتون بم، تنها نماینده بانوان ایران در آسیا
🗓
برنامه دیدارهای خاتون:
📌
خاتون ایران – زسکا تاجیکستان؛ دوشنبه ۲۶ مرداد ساعت ۱۸:۳۰
📌
النصر عربستان – خاتون ایران؛ پنج‌شنبه ۲۹ مرداد ساعت ۱۵:۳۰
📌
خاتون ایران – اتحاد اردن؛ یکشنبه ۱ شهریور، ساعت  یکشنبه ۱ شهریور ساعت ۱۵:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103783" target="_blank">📅 16:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103782">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cebqu2CsiZuzgYRX8yxG0L15mGTbXerNTZzTwlq1RZlkBVbTcRkdlsXP7slQy9j0kXMLQWTqmZDUWS5G_UWyu2pk8gs8KZPXaekKwbsJmSp5ZLTbTmH7mDlq16w0iDr-rYYAizduH-H8XeWJ5qiBmAeGb2RydrSWByiQ7P_gSFwvBP19Bm_lVFvhNwXOobTYdX0NCCF7bVDXcJt5ZCsEQSjMWdAhhNVZ6-5sUaHKMjPIbj07F9CNI0T6gVKgUqzT4Rh8I_3kANPj3SR9rx5iXMuBbz4BeCuqS7pyyHN9rR0Oyy3KJKMSVg3EOcWjs1-FtOCRUGAm8ZoQRQm8rss_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
واکنش کنایه آمیز شدید باشگاه
استقلال
به استفاده مشابه طرح شیر در لباس رسمی
پرسپولیس
با ابیاتی از
مولانا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103782" target="_blank">📅 16:14 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
