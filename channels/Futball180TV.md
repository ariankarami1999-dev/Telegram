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
<img src="https://cdn5.telesco.pe/file/eweV_Z2jjHsC5rSKawF16m150WJl9x66cOShk79XSUttpKOtgwAutl1ZP_IaHKFvOpIyYCcod0xSeuBGpVWtZeLdQNfD29WfMIVWMF5EHTvbeXQ_t5CowmmJK7GzYcxAdM8AT2MLUHxVnbjYumPkkInto33zw3IqBSzR9Uxjd_sHPOFywqWjTwBL1MBoHBsGFwgIIs01VEqczDD8ZepMI9YUjtJmtZLHrgpjONr5GJsAgajdZy5_AaltA-JTFiCQq33MEMCYMRE9izVN01IkQjksztq-Z0-c1hAwyLcay1pm-vD8x6H_xLrOta6dncYswGfUYhZnchKYKz2PRiwQ_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 438K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 07:44:06</div>
<hr>

<div class="tg-post" id="msg-104975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
سوتی فوق‌سمی یاسین‌بونو و کولیبالی در بازی امشب الهلال که منجر به پنالتی برای حریف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/104975" target="_blank">📅 02:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=R7J6cwfpg16Zn0vVazuPxjl5kglClGWl7b3KvjxLQXXNH5idK8f5DwIIvbBEoj0pTPJg0Dlwc_AH5fqHuYjy8MlAhrss0GVPiSVJ8sWbikNc9weB7HBO4vRYxmKtVbqZhmWmkre6XLE7NZVfqEqXMnLcxoOPn2m64Xrwa6nejV7Doyqcs-MM9uo-kBoWkOkR2mmtoh7BgB50FH03kgSL-N1HlLYpp4RhwaHW-K_vwt9GMsBPEEiurI7ylYstjI_Y1H84WIzf_FiS-_pOu4yhEtQSXnRCJTQg9q_-WHXdOmd7jiZlyUtV53m-9dF8GCGxcnZqRxyOTmw37XnP8fDgLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=R7J6cwfpg16Zn0vVazuPxjl5kglClGWl7b3KvjxLQXXNH5idK8f5DwIIvbBEoj0pTPJg0Dlwc_AH5fqHuYjy8MlAhrss0GVPiSVJ8sWbikNc9weB7HBO4vRYxmKtVbqZhmWmkre6XLE7NZVfqEqXMnLcxoOPn2m64Xrwa6nejV7Doyqcs-MM9uo-kBoWkOkR2mmtoh7BgB50FH03kgSL-N1HlLYpp4RhwaHW-K_vwt9GMsBPEEiurI7ylYstjI_Y1H84WIzf_FiS-_pOu4yhEtQSXnRCJTQg9q_-WHXdOmd7jiZlyUtV53m-9dF8GCGxcnZqRxyOTmw37XnP8fDgLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
🇮🇷
مصاحبه با خواهر صالح‌حردانی ستاره استقلال بعد بازی
: کل خاندانمون استقلالی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104974" target="_blank">📅 01:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQB7JuSl4nVQUpAYBMNYRjgRp1a14W11AD1IJZ20JzVjDBEopNzKW9FPaT02vic1r9_Z98LEijPzcuQ9dtwv-0IJMbF_IEfwVz7Yxgn8DiYsjJwdHlSdljvwTo2Iec_sEaa9mnXaFpWs5iMwnE45tqNhDqzdEmg-Jon9aZ3Di28drKFr4YOwpyjDCRiTWkKB7Kl9e6fkEp-8YfKWvB_BUsJKkd4k8lxu94KeEnv6a1S_1AbgakD0sQ-Wv4kYCU13EkcVQyZHHHQArcQYWMw1qVjvRDTy3zl_UVMRUAo3zeYWuWVaR6c3dzNdrlcPWU4bOJpQFKmvBRjPgNkw3mWmygns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQB7JuSl4nVQUpAYBMNYRjgRp1a14W11AD1IJZ20JzVjDBEopNzKW9FPaT02vic1r9_Z98LEijPzcuQ9dtwv-0IJMbF_IEfwVz7Yxgn8DiYsjJwdHlSdljvwTo2Iec_sEaa9mnXaFpWs5iMwnE45tqNhDqzdEmg-Jon9aZ3Di28drKFr4YOwpyjDCRiTWkKB7Kl9e6fkEp-8YfKWvB_BUsJKkd4k8lxu94KeEnv6a1S_1AbgakD0sQ-Wv4kYCU13EkcVQyZHHHQArcQYWMw1qVjvRDTy3zl_UVMRUAo3zeYWuWVaR6c3dzNdrlcPWU4bOJpQFKmvBRjPgNkw3mWmygns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فراز فاطمی سرپرست چادرملو:
🔺
آقای پیام حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار نرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104973" target="_blank">📅 01:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=Xn8lgU6rc5a24O0CTnGaf1nouT_dXQB0eaDJYZ_mmWC2jPNrUthZF6LYPEyk45_RR4Lm8DYxc0jN7qAEg-zyJSmjzuEZIl_CprCeEuk6gkFkCOsIThRLri__iHbpewFrcbcS1RPAOBpe6jIL2QVPmYWoFwslKtdjnyEhXV7DtW1yYnFSavnciZLJ3CQNsn1Dp_HgPnLJVYVD0Llp-Vn7sah2UD7LdObi752ISs-m3baXoANpRMcYUoGwF9vND-Hv2oHZ6yiUWM2Qjf64JupbY9A-xRFgtJeoZCOHFez5atVveibuW8bIGpohJrLgfkiZN0u6FVk_0YR5DQ0g8oDx9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=Xn8lgU6rc5a24O0CTnGaf1nouT_dXQB0eaDJYZ_mmWC2jPNrUthZF6LYPEyk45_RR4Lm8DYxc0jN7qAEg-zyJSmjzuEZIl_CprCeEuk6gkFkCOsIThRLri__iHbpewFrcbcS1RPAOBpe6jIL2QVPmYWoFwslKtdjnyEhXV7DtW1yYnFSavnciZLJ3CQNsn1Dp_HgPnLJVYVD0Llp-Vn7sah2UD7LdObi752ISs-m3baXoANpRMcYUoGwF9vND-Hv2oHZ6yiUWM2Qjf64JupbY9A-xRFgtJeoZCOHFez5atVveibuW8bIGpohJrLgfkiZN0u6FVk_0YR5DQ0g8oDx9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🚨
معاون اجرایی پزشکیان: شخصا اگر میدونستم آمریکا قراره رهبر نظام رو ترور کنه، دست از ایدئولوژی‌های خطرناک برمی‌داشتم و غنی‌سازی رو حذف میکردم چون عقلانیت حکم می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104972" target="_blank">📅 00:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujP37uQHlUQ0R_LgJ28kwkMcgMjtJcchzRVbDG0Phf8SwRqS9o-XgW6adNTFmVffSPqiVv9f_EMMkk8SNmKEyXPLs022eLkzi6CtEDZBZkFbcB4pgTIc8EKYDkHp_iEvZifGv442BkLeGFDrfzbZdNf-VC2soD3lmPDqrxSxoazKcBopGYtPR2Ah9efwM6Bxh04hc_7zceWXtX_YChTZq-VbsJROcnPBT71I7DsLp7jjCw7CtIDradG3fm-rG3BIrsPnsvj3hCWfmVWsDG0B98b3ZYJffZQR71XDe9yLG28VMCWI6zHdCa2l0sCi9anpk0sFgu_2Aeh05aJfrfbKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
هفته‌دوم لوشامپیونه؛ انریکه همچنان در حسرت برد؛ لیل موفق به کسب امتیاز از قهرمان اروپا شد!
🇫🇷
پاری‌سن‌ژرمن
😀
-
😀
لیل
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104971" target="_blank">📅 00:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzminsONL_Xj5y-5xiXwnkZroiSlGxMbiINqN3w53867U3LnLvwN0vmbIxfDc4x7TlxSld2mWDOotrZXX_WQ2oZRfrIiR6BTpMfWa9etLPwhBOrPQuzAYSiUxk7-jxPHAA9UivEIsyBMFdJ4UjP2WFR6omIZZaZzWXtJa-eVuS7t4J4_hApp66hF8ak1QgH0uSuTosjPvDzIwh_Okb3j83YlQ_bG2Wt44r2_d2GtIXuLhrheCh7DGFgqbkMxEvnbfJOoH4eOS-1ZAdVb0FlD4GGUjmugtot9BzFGvKb5x9SXOx0J6hO4idNJPyPD0212jHmcww3KP5MZt-y8nycJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی پرگل در خارج از خانه؛ موتور گلزنی هالند به موقع روشن شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
😀
-
😃
کریستال‌پالاس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104970" target="_blank">📅 00:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA-wip4WFJ5P8_Nqt7ADrD3hIhTN5s77gXa2dem9Uhm4BR03PtEhAEILfaG4nN9eB_EaoPpSsoz2bRELBgcHzebbn9OcgpLyJVJM4k0Zq7GntAAjxnWClbjdJZpbEuNQYoRajJGTmzA1onbM3kj5FqFk4hbMOO2CT6uB9eYOcobXJzv1nGvRnFAislHhtbJwWgLUodF3TVtFz_0mnoJiWEqHhA_XgUyCKx4P_eCeZYZza2_VzwoMiz6eaN56NIwFjIsErzg1bO9pa0Z3gR8EVO9SR1Clp0x3Th9kIbUJfuUdx0RDF8ILOkGj5JRnW2Vy3681CMNeq1bnwgjrZ-ASjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
هفته‌دوم سری‌آ؛ پیروزی راحت در خانه؛ روسونری با مهاجم جدیدش دلبری می‌کند
🇮🇹
میلان
😀
-
😏
ونتزیا
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104969" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=aN4q7m30gUYdERjYvY1qTZ1MKw04J6te_31aNQhesLeBpMaE2nDknFLJARfdme2LmpHoyCtxErbrcGMBveRQCDP88aFNAuKCZpebevAWbt_WpPlbigU3b8dAITDyi8g4RneQca6TjQfWW-B-sXVWFQwnTeI6YXYojBm5Ta0FJ_pvRm9LWaddHV1Akh6wauhv9MhBALp5WsM9RCBQB6LuvweBZ-8Kms3Naml4rm07LRiNYDhRoK__b2qtvVmZJQmJF_bkEzrebusrD26lfWftIuVZidrtG01OKdq1Vph__vKvpVids9Blkm3s6yFs-A1CuJZtnDmA-vbIUBwvJIERHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=aN4q7m30gUYdERjYvY1qTZ1MKw04J6te_31aNQhesLeBpMaE2nDknFLJARfdme2LmpHoyCtxErbrcGMBveRQCDP88aFNAuKCZpebevAWbt_WpPlbigU3b8dAITDyi8g4RneQca6TjQfWW-B-sXVWFQwnTeI6YXYojBm5Ta0FJ_pvRm9LWaddHV1Akh6wauhv9MhBALp5WsM9RCBQB6LuvweBZ-8Kms3Naml4rm07LRiNYDhRoK__b2qtvVmZJQmJF_bkEzrebusrD26lfWftIuVZidrtG01OKdq1Vph__vKvpVids9Blkm3s6yFs-A1CuJZtnDmA-vbIUBwvJIERHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104968" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPc2Fv1f-sVMg1-WQPALUs372wqWvgy37HxUIVc1j6-YfD4Jo3ubfnKE6BXgHZGtgGBxTVwbc0LC0ycDk_DkVpdwH-1ZqTkptFJ2jaNqJuJRv664O2JTsSneqB8S7eDrf-74yGRdL_5rrmxXygDdIr9UL5g4KfYNpcQrVMgGFS6fx_tZjdVLTdsvMIWAuCnSf0jVIGm-Y9ebVgFxxyKpaKaBoLguaVpJpl4klFVhqCemnA8YrJLCLReUjIIQCRwZEIp6ALd7XjfYVb2Jp_es73t1h3XBEOSGbMOFEYIWsthHlPNzuEZQx5NgO6E63dotjSWkP9farmi6ftFSJyEKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
هفته‌اول بوندسلیگا؛ موتور گلزنی خشن تیم‌کمپانی با قدرت لیگ‌را آغاز کرد!
🇩🇪
بایرن‌مونیخ
😄
-
😃
اشتوتگارت
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104967" target="_blank">📅 23:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=d1GiOyR-_vuFFtI0h3P3TG3AtUa-1fJ_tTamOhNHU8oovRxYP1VLRioo_3qrunoTAHUPgUHVGJj8eaQjt7HIsVxDArYB5h7gBOK0dzrGhRpDOmxWsXi1LNw8CAV0ZGFgea9K1bnaSkALUN-K2nq9RLi1SmYbf-viuqvWoBAHTJ3jdiLAIIr99ifbbeOT5I6ZQSTZFnAhCcjDVGyumnYoqHAjFt8HV6UEwRIta-LWiCUmpgQTnhhdzDu4dfArZ3AQ47WLlS6VOb07vg-Z3B3gY_ntH_hQr7iFs2BaJ5w18pnRUKq-pTuZy1c5Vwj0SpowCX11nXFVewsYpFlRqzzBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=d1GiOyR-_vuFFtI0h3P3TG3AtUa-1fJ_tTamOhNHU8oovRxYP1VLRioo_3qrunoTAHUPgUHVGJj8eaQjt7HIsVxDArYB5h7gBOK0dzrGhRpDOmxWsXi1LNw8CAV0ZGFgea9K1bnaSkALUN-K2nq9RLi1SmYbf-viuqvWoBAHTJ3jdiLAIIr99ifbbeOT5I6ZQSTZFnAhCcjDVGyumnYoqHAjFt8HV6UEwRIta-LWiCUmpgQTnhhdzDu4dfArZ3AQ47WLlS6VOb07vg-Z3B3gY_ntH_hQr7iFs2BaJ5w18pnRUKq-pTuZy1c5Vwj0SpowCX11nXFVewsYpFlRqzzBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇮🇷
محمد تقوی، ایران‌اینترنشنال در برنامه هت‌تریک درباره تساوی استقلال برابر فولاد گفت:
«غیبت آشورماتوف در ترکیب استقلال باعث شد تا عارف آقاسی کمی با مشکل روبرو شود و نزدیک بود با اخراجش شرایط استقلال را در بازی عوض کند. همچنین بازیکنان دو تیم در ضربات آخر بی‌دقت بودند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104966" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104965" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104965" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spa9MByUMNf_dr9OIEqJIrgBxA4rOEmXRPSVdA0zzhJNIbbXqeW3bBm7Ruv5y9ZAIcppdYBGXDOZ50kAq5tCpLk83rIDPgy7QMqfbRbTIjLmSUrUKLYQwnqbg3rB-SDmOgX9cx3lvIE0HYXZv3lXkV85SHK04607F80vOztIHZIkcSKQ8OIojxZ7xk-hc-VrrBmvrNv7p2WgDSLzDsfxm5DE1YoUptNZ1m9QFXCMSLvyBvCCr4Fk82-GpOzYSbcsgKs7hV292leoVegr9yHa_Q2Cs5sNLN3vA0MRAUZo8mIz-egjhSPLOD3X-7ErsImKi4wgTtEvx2fj7wkrKEybow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104964" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196e7e0a8.mp4?token=PrHEVkPmNZsLqekTya7Gl-E3gRE0r2tFwHxzvN98RHW3NKvEpR0B4UfPJhk5lTUL5UNJ7CkKXMeYj1Ue7-41FncfxnZqPvCrH7x5HinICdMrVyVXhnynDyu2nJw5VgI-NneY0dVZsDXglN8ExqHp64UAjLyi8_b1IBlkF16r_aEHn0LEgAsTsqgcrWa5KohEhB-u2vp65ECkiAe6-4ZpKctGJchBVV4kowmS2TtSSm0vI2M6cQVD85tyw-iCvvcRwrKDIUJp_s_lj8LJL1g-jtRBTPZimPJu9pc2uq5pouBfXifs1qRwlFOla_wo_wURh-tXVFQr1BK_BGSw9byfng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196e7e0a8.mp4?token=PrHEVkPmNZsLqekTya7Gl-E3gRE0r2tFwHxzvN98RHW3NKvEpR0B4UfPJhk5lTUL5UNJ7CkKXMeYj1Ue7-41FncfxnZqPvCrH7x5HinICdMrVyVXhnynDyu2nJw5VgI-NneY0dVZsDXglN8ExqHp64UAjLyi8_b1IBlkF16r_aEHn0LEgAsTsqgcrWa5KohEhB-u2vp65ECkiAe6-4ZpKctGJchBVV4kowmS2TtSSm0vI2M6cQVD85tyw-iCvvcRwrKDIUJp_s_lj8LJL1g-jtRBTPZimPJu9pc2uq5pouBfXifs1qRwlFOla_wo_wURh-tXVFQr1BK_BGSw9byfng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مسعود پزشکیان خطاب به کسایی که میگن تحریم مهم نیست و آمریکا هیچ غلطی نمیتونه بکنه: نمیدونم چی بهشون بگم. فقط میتونم بگم عقل هم خوب چیزیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104963" target="_blank">📅 23:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc25ebba85.mp4?token=GJnOYYKSR8NEUFvAvjbpnuuy7mb36t1gN56_ooiDEWPAd-PrBUuWmfzY1AgNq6acQPTVOZT0otoGY3hJI_cziG3SKgMGiimCqJlqDqLrjX_t9XOI7oTw2NCAW3BgG8eaF3japqkayDx0x4XnxrhiJ59MijwM43GA5oDLf0lvLBRyAagrKuH_bFsioGMMND49gMBo8lBxgyLsS8DzGL-WoLm4jx6XySEjBfosXzKuypiRcvZ5yB6nJOQkPU0VLIqIM1KS2EXA6gmH16SB_cuuP4i9GlQde3bsQKPeC4vbj94uYEiZfLga8fKznBpp1-t5yE7gwPsvZdtfQMP4dOzo-Bu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc25ebba85.mp4?token=GJnOYYKSR8NEUFvAvjbpnuuy7mb36t1gN56_ooiDEWPAd-PrBUuWmfzY1AgNq6acQPTVOZT0otoGY3hJI_cziG3SKgMGiimCqJlqDqLrjX_t9XOI7oTw2NCAW3BgG8eaF3japqkayDx0x4XnxrhiJ59MijwM43GA5oDLf0lvLBRyAagrKuH_bFsioGMMND49gMBo8lBxgyLsS8DzGL-WoLm4jx6XySEjBfosXzKuypiRcvZ5yB6nJOQkPU0VLIqIM1KS2EXA6gmH16SB_cuuP4i9GlQde3bsQKPeC4vbj94uYEiZfLga8fKznBpp1-t5yE7gwPsvZdtfQMP4dOzo-Bu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
درگیری شدید خداداد عزیزی با خبرنگاران یزدی پس از بازی با چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104962" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssz1Nc5_JkCTLHBsZ-8XCwuGtzDuvHCsVq9yErH6aqzsX7ztOCjkquiv9MPzhy7oriWCazBSWzmTlcocRDeNbF6Yf6ZoP2F--YEdlSlV1J1GAHCiURKmzHPklfg0GMo1PoOV67rV0hv3lfLIzV0WJ5_RhmKtR2p9Un63aAGhEi_SP5TjXAodE865CjuARLrgfQRpENXrDo3_-i0fAIzewXHiyl-FY0RpbNJoqCNkXOqXhLRhbn9wMsRLfP7ZanfDqPfaYjD2nXq_Rygz2P8eF34tP0Y1I-6IwgFXwI1ZqyWXRgerzmAabxBEsGkQXgS1hWdc0ztIFH9bemFRZNE5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
هفته‌چهارم لیگ‌برتر فوتبال؛ پایان نوار برد آبی‌ها؛ شاگردان سهراب بختیاری‌زاده با تساوی به استقبال دربی رفتند
🇮🇷
استقلال
😏
-
😏
فولاد خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104961" target="_blank">📅 23:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwB9Z3VmDwQB_6TTOTIE-KiFmLkuvdxtPUO7Cf2fjd7H1jqTQmgGzWXQYkIWcRDVR-96RRiBgvUq5_2ZyR-PhLfp8Sugaqz071xhi1NOZ_MHVYmZZE-Hj5qy4f2UsSXTZWC5ZFex0En7r7quUd18hnoXKAM1F7TDKn4uBYkAOJv8eR8e2z8Tzpbj0j-6wG_vEs-u1frwi7smfGT9Hmpl3aaKA1xXU_pztA01rgo8rWTXXFLZDPxyWTCjSE8kLz9-F_bhsneSFX265EI_9rzcr_BHt-VnoVc7yslPEYMGMfTK17WSZ-B5kLDMTu3LtAtFFU1HHuAJmFitovuH59inFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
هفته‌چهارم لیگ‌برتر فوتبال؛ پایان نوار برد آبی‌ها؛ شاگردان سهراب بختیاری‌زاده با تساوی به استقبال دربی رفتند
🇮🇷
استقلال
😏
-
😏
فولاد خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104960" target="_blank">📅 22:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇮🇷
🚑
صالح‌حردانی در آستانه دربی بدلیل مصدومیت از زمین مسابقه خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104959" target="_blank">📅 22:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed2d489407.mp4?token=fTC7QN4IJZWcrvBCn1Ij6PgWhxLbtr7NffqMkpD2m1dJWtQeKBUjFmkk4NObpdX90jhm_KVa2BRjTBEyv68a5XGYnQ8sC-2MzXRgb3sjg1fKOiSAIofqiJ7H65FgprMGD0p2fNJTWh3NsC5ZtM_JpvSCAB2PFewJlLFkXLx57T5CEt4H-y65gd7FV1W_GpxsKFDxUPT59YWy-ueSUVzkhvXHNzoZwjZmz7hQUHdpnxcGo9Eby-cvA3WnZcCE5EXMgqL7JA7d2opvhTythWMo4bPNjzwFajgKnFLXGQ3i__TBKZamingcjew7mZ65WPre9YCAsAq1UsTIdRyl_CFzyWi_xmsHWfBap-YJ_CLPkX_RgJ97iNTS_LRm5n83s1V_3z2J_Qz1LB0UmrEw6WcPIbrC1twiSCuwm53795TZHYd0g46Y7Vrefvsoubqw72KgbCMREPzcrDKuSIRlt43ZCXndLkBRKMgb4wSAaApwobKgmYZAIKf033LpR7eDl5DlJHjA-axE9MvHEIiR1HzzzBJXiyU27uQfOCyaFyW_5YcDO4hSZ5RYQ-OC_gK7DDV03mZSoID8l0qohWWhVB2QLgRhU8puDOWcioLsRf65tnnG4DCi-TiWgr-BgnDEK1-NJtslkAA-vzdqzjRnfqFRrOOaALlIezDaIGqw-JwtuFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed2d489407.mp4?token=fTC7QN4IJZWcrvBCn1Ij6PgWhxLbtr7NffqMkpD2m1dJWtQeKBUjFmkk4NObpdX90jhm_KVa2BRjTBEyv68a5XGYnQ8sC-2MzXRgb3sjg1fKOiSAIofqiJ7H65FgprMGD0p2fNJTWh3NsC5ZtM_JpvSCAB2PFewJlLFkXLx57T5CEt4H-y65gd7FV1W_GpxsKFDxUPT59YWy-ueSUVzkhvXHNzoZwjZmz7hQUHdpnxcGo9Eby-cvA3WnZcCE5EXMgqL7JA7d2opvhTythWMo4bPNjzwFajgKnFLXGQ3i__TBKZamingcjew7mZ65WPre9YCAsAq1UsTIdRyl_CFzyWi_xmsHWfBap-YJ_CLPkX_RgJ97iNTS_LRm5n83s1V_3z2J_Qz1LB0UmrEw6WcPIbrC1twiSCuwm53795TZHYd0g46Y7Vrefvsoubqw72KgbCMREPzcrDKuSIRlt43ZCXndLkBRKMgb4wSAaApwobKgmYZAIKf033LpR7eDl5DlJHjA-axE9MvHEIiR1HzzzBJXiyU27uQfOCyaFyW_5YcDO4hSZ5RYQ-OC_gK7DDV03mZSoID8l0qohWWhVB2QLgRhU8puDOWcioLsRf65tnnG4DCi-TiWgr-BgnDEK1-NJtslkAA-vzdqzjRnfqFRrOOaALlIezDaIGqw-JwtuFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلزنی رونالدوووووووووو برای النصر
گل شماره 978
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104956" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccdc8cb72.mp4?token=WBpTTNiDScxdAzvi-kqkcJWzA4PkfHAM74-PXOah-rXhAOJdq4nYDT14zfeYZgCgwk3QAdMHOStRfIAE66IXwVDgKD8nFBLM4g0WS7d5tBad38M40jTjIQqflBFGzOg2nEtpPKotqEqIWdBUWkPm4ve9jSc65ql0XM5y5TEDxGgrBDrxA5opz0gn1w19APL6U1aXrYIkVNPPtOmNE8gXkBAy0dSEMzY3_4IAhlatAIMTaCh_pRcvYtjBR3luGHG83wdKXhc1t613gmtPSptfHHoYZsXmHG4cuo2053d1Z8UBtdRkVM7KWQsf5ZPmSAryo13T-bmOzYcfp31OMPw6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccdc8cb72.mp4?token=WBpTTNiDScxdAzvi-kqkcJWzA4PkfHAM74-PXOah-rXhAOJdq4nYDT14zfeYZgCgwk3QAdMHOStRfIAE66IXwVDgKD8nFBLM4g0WS7d5tBad38M40jTjIQqflBFGzOg2nEtpPKotqEqIWdBUWkPm4ve9jSc65ql0XM5y5TEDxGgrBDrxA5opz0gn1w19APL6U1aXrYIkVNPPtOmNE8gXkBAy0dSEMzY3_4IAhlatAIMTaCh_pRcvYtjBR3luGHG83wdKXhc1t613gmtPSptfHHoYZsXmHG4cuo2053d1Z8UBtdRkVM7KWQsf5ZPmSAryo13T-bmOzYcfp31OMPw6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
لک بازهم مانع از گلزنی یاسر آسانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104955" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=Gg_yYtNmGPCF5hbdiBrqQ8tv5KFL5gdUHs3e48weZvNWNBppJIB2DrHDgA-CmQRMWVctewEJOTyZvFNsOe-qS1P4IqrTSvmBqby9A_rmkR5qXU3emahDD-Qs55aTo7HYgecXTJZx3jdfDnEKmGqof7xNYjVJlvYfSaFy0rRScYtN1k9k1JJxH9tl3RaDGCcTBoF1GETZ3eHuPmc7p7SWv53MznkYgcNg_heecTZOA9X6oZxmoZvwP9qNDMO6sgKi6VggTSmk0LfJ6Ug1eozSiOKdja8aA1F2rebMNRfOib5j4TPFzdTXwNY5WM359cpX4060gisJegag-mOZP6CeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=Gg_yYtNmGPCF5hbdiBrqQ8tv5KFL5gdUHs3e48weZvNWNBppJIB2DrHDgA-CmQRMWVctewEJOTyZvFNsOe-qS1P4IqrTSvmBqby9A_rmkR5qXU3emahDD-Qs55aTo7HYgecXTJZx3jdfDnEKmGqof7xNYjVJlvYfSaFy0rRScYtN1k9k1JJxH9tl3RaDGCcTBoF1GETZ3eHuPmc7p7SWv53MznkYgcNg_heecTZOA9X6oZxmoZvwP9qNDMO6sgKi6VggTSmk0LfJ6Ug1eozSiOKdja8aA1F2rebMNRfOib5j4TPFzdTXwNY5WM359cpX4060gisJegag-mOZP6CeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ با اعلام پزشکیان نرخ سوم بنزین از ۵ هزار به ۱۰ هزار تومان افزایش پیدا خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104954" target="_blank">📅 22:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_t09t4COU2LbU-LjVGj3xOp5u6tPISODIDgxepxiVGQpqk3_86bAGTAPVfxGdLIqeDMXGIvvtspQYexmRL0UbFCcI2w2hbHvX127P_vNQxHlSD8NjVs9xYtcQVmx-CFlxAJ1F8xV2meFPLJDzjfJLfJaGJn41nTmkXnbNHvSKYEBH2JB8IawO4Ru9tA2C_IXchkehiRPFuSVVCOsh86uoVJtFG_X5MzZczUp5tqr5EQqNs77ktxcofpoxpLGgbtakuioXAxIPwx6lOgq9FP0mmkio2seKptFjrfXzmIaSx_20OiN9YhF3yg30c6kcDGalDgT1SMaP-SlDGCC-OuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🚨
🚨
🚨
🚨
مارکا:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طی چند ساعت گذشته، منچستر سیتی نیز به کورس رقابت برای جذب خولیان آلوارز پیوسته. آنها در تلاشن با یک قرارداد قرضی او را به بازگشت به منچسترسیتی راضی کنن
❌
🇪🇸
آلوارز هیچ تمایلی برای برگشتن به انگلیس نداره و همچنان روی خواسته خودش ( بارسلونا ) پافشاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104952" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
❌
🇮🇷
اتاق VAR اعلام به آفساید ساسان انصاری کرد و اخراج عارف آقاسی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104951" target="_blank">📅 21:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
عارف‌آقاسی مدافع استقلال بدلیل دریافت کارت قرمز از دربی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104950" target="_blank">📅 21:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
عارف‌آقاسی مدافع استقلال بدلیل دریافت کارت قرمز از دربی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104949" target="_blank">📅 21:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmS8Ph0UjiJzS7VQRoO30gjEz0BLJm2f8kOJf6OAXqOiAhF_qxcE62LkFHDbHjbtQWspo3gvI0T0XVUTUWK7FrwnwQlux0hltlA6_me_CV6apP-EQXfuaZ9qWEXyfaaKbCqdLPBOiu-cWCffVKrZoBIIjKH8p_6PQDSyeyz8ZPFBHBcMlTie7uUDPmjMZClQGAUBGg6gu6Ira7pjFvdHhPHJF77l46OIpDY_mfWn_2dFUdIMIXpSjoOWDv4T9soqjuUaZb4qG1g1dEUW1v5JxKE_m7c6Kg5tAKWrmq-CUKL9zHPzuvobynTQ7DoTkePQ3kSG8aJcQ7ElLxH9oP0eRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ نیکولاس جکسون با عقد قراردادی تا سال ۲۰۲۹ به ارزش ۶۵ میلیون پوند از چلسی به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104948" target="_blank">📅 21:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcFh5IO1GU5YvhhfIywAoQHYzEdVEUgI6H54zQn75N9CpALtqa7ZbK-E1caGsEIozqv-zV4YGqmH_kCRbtzFN_wxHBDTMtutyljGkxiHWIj1ux7f4vdBWg0fGxI5EQLdsSPWHsrrlYvBvW9fw37QU2efqurCXpmrzxqBdZKgGtVisAG-twpOTNBYVPgQujm41Taps_7wStYOw9B8mNomnogFIoZXexkFjlAZLUZ8dwAkh_7ZMRm_nd8gRk_AG1Ky44J72J6kzpjxG5O53I46Jrh07YHc0KUh_eyYm-Y7M-NwPbr0p8Ds1ZcmhG6Q2uPXLwPtyBUJLU3C88dWknebPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم لیگ‌برتر انگلیس؛ ترکیب منچسترسیتی مقابل کریستال‌پالاس؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104947" target="_blank">📅 21:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1abe2b073.mp4?token=e_ldZYDan998xJpSiQomU7kRrzHQp-ozTlQIPnZB7aYELsWGWjnA_KP5VOhEuun-bTIZh-DULgsuD3GamfT5x5Z8fgR1y-JakaV0LblWIGcMLhd8cC7sx8Nh_zC2XQK1IgWkMihGinleQHutsM5fiNmOuLsLp_nJYUX5Q4kxMJKuHEUWrh7QjHW65kLqzVp5ff482rCS8RukI5n1YTF3M63CL9Dn0LsRuxGsss1C8ZVMVn4KsW6VjK9gJwnNtFi0J2d6lDFER4pnBrLAEgTnBn5s6Er-xB9v9-f4OGdD3he2hQ3VM-6hx1AlE7Xiiie_Ao-eT6EUCMQZVv1ewVF-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1abe2b073.mp4?token=e_ldZYDan998xJpSiQomU7kRrzHQp-ozTlQIPnZB7aYELsWGWjnA_KP5VOhEuun-bTIZh-DULgsuD3GamfT5x5Z8fgR1y-JakaV0LblWIGcMLhd8cC7sx8Nh_zC2XQK1IgWkMihGinleQHutsM5fiNmOuLsLp_nJYUX5Q4kxMJKuHEUWrh7QjHW65kLqzVp5ff482rCS8RukI5n1YTF3M63CL9Dn0LsRuxGsss1C8ZVMVn4KsW6VjK9gJwnNtFi0J2d6lDFER4pnBrLAEgTnBn5s6Er-xB9v9-f4OGdD3he2hQ3VM-6hx1AlE7Xiiie_Ao-eT6EUCMQZVv1ewVF-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم تراکتور به چادرملو توسط اشتراکالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104946" target="_blank">📅 21:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF0l6Q6dXKUnFSpYLj7zCVHeaL3l03R0xBHfDQ1ThLV09Rvckh66wTBKsB7s6ZsTQtExR0xItsSp0-nNmbobrIEe6rG-fMMmm3wXTMLrJCPzm65VFZ1X17OGNcoVJ5DY_-2GwBwLP2IN57ubRk40PzOIc70XEX3q54i1qhtrc31eQzZWcd9PYwUEmhT140VkdTuKcR4ynOHl8SfCSYovMLkNUhSdg4BTi7TyHv5w9QP7lTrrNAFWrGVMf_MkAD5TlXOEMl_FdL2wtE4A0lGW50x_lUZHgXYZmJGnxNGqTNjMxWoUURCDKPr3LjSk0lm5A1AJ9RcxVyy0kQM0oI6LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇩🇪
افتتاحیه بوندسلیگا؛ ترکیب تیم فوتبال بایرن‌مونیخ مقابل اشتوتگارت؛ ساعت ۲۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104945" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2abb732ba.mp4?token=frZHf29uRGswvlMW73dH8syyD6Ha5wfTQLmUAdNxoqjHW-ECAcnD5kYuEiCNGWuUMGJUdpyNKt2L2_X_vpDLxAxmixn2veau2InBmd9sDdEw7wXK0-yoigSn_IBl0Lq-xXsb3wSq1ya_ZxR3iBKKrnEUk7ZQVe2pGd2cFjaI7Fn0YXnJsH1EC2cH2I1BTdTHALjzZSR3SpNHmFC61b1WmyTfV-ZEkhrBaefe6q98peZiKtpNCgPEeUhb0Ztcg8EXNfPa6FpCOrqkJdKKxcZ7xqFtSlmI_4cBPpFrXIRgChBRi_oYprdaID3ZwbfgoS66hzkq1bsyYAa1_XlFoR-xjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2abb732ba.mp4?token=frZHf29uRGswvlMW73dH8syyD6Ha5wfTQLmUAdNxoqjHW-ECAcnD5kYuEiCNGWuUMGJUdpyNKt2L2_X_vpDLxAxmixn2veau2InBmd9sDdEw7wXK0-yoigSn_IBl0Lq-xXsb3wSq1ya_ZxR3iBKKrnEUk7ZQVe2pGd2cFjaI7Fn0YXnJsH1EC2cH2I1BTdTHALjzZSR3SpNHmFC61b1WmyTfV-ZEkhrBaefe6q98peZiKtpNCgPEeUhb0Ztcg8EXNfPa6FpCOrqkJdKKxcZ7xqFtSlmI_4cBPpFrXIRgChBRi_oYprdaID3ZwbfgoS66hzkq1bsyYAa1_XlFoR-xjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پرتاب بطری به سمت پیام حیدری و بازیکنان تراکتور از سوی هواداران چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104944" target="_blank">📅 20:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b801553.mp4?token=KD-caf8smT6hU3OAFOKJw0cljdseLSEbpROpwIBF6ZJmfkH0sqZEG2TtteVL-XINT0L8IY3a17bvpmdw0MnUUBIIzOx-Kwq4VyknUS1XUg9ZFrQMLBROkFSR-T5kZKISCWTqYxFf9bqYFrhmHEmIBgkc2v_vbxIWeh2GSEKJYgqGPKR04r4V_lro4Gehtz7DYbkpOF9XPua_vsngalt_mRofYwBdHooOe3hF2Nuk9qj8gpY3mrGFP0OvLgi8KbOCBRl8bC9U2nrLbdtBMObc2S9NoCt3BGzxYr3iaLFimt7DxIyAX7R0hEiQ7gakXQyzZbvP_EL6BjXs0VmyVFNkfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b801553.mp4?token=KD-caf8smT6hU3OAFOKJw0cljdseLSEbpROpwIBF6ZJmfkH0sqZEG2TtteVL-XINT0L8IY3a17bvpmdw0MnUUBIIzOx-Kwq4VyknUS1XUg9ZFrQMLBROkFSR-T5kZKISCWTqYxFf9bqYFrhmHEmIBgkc2v_vbxIWeh2GSEKJYgqGPKR04r4V_lro4Gehtz7DYbkpOF9XPua_vsngalt_mRofYwBdHooOe3hF2Nuk9qj8gpY3mrGFP0OvLgi8KbOCBRl8bC9U2nrLbdtBMObc2S9NoCt3BGzxYr3iaLFimt7DxIyAX7R0hEiQ7gakXQyzZbvP_EL6BjXs0VmyVFNkfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
62' اخراج کلباسی بازیکن چادرملو به دلیل خطای خشن
روی بازیکن تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104943" target="_blank">📅 20:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a01cc820b.mp4?token=YB4O6MZIM0aUQRHmofp14rocl-q3s6n16NTm_PkbXFT8bDDWqiH20TbrmUMWBFKQHReRctY4aq48hmUCstW_t7s-DJuhFJ87ssqSBQFYGpI5fgBO3Bg4mdiAXIdnsab0k3bEct5RSZJy6MCUdbr-kcfKDCERu6Vb1VSnpyj-8ALlOHLuWqV-AQdNbn40xoizbLo5A4O05tMjsgZPZgV9rVyRsu8ULRfkWy8H-jFag-adE7XxQyMXzkqmqqI96kQHWCDEKIaPN7-8hGrhADdcnfrvlPrhYGB4nAvE13N2cgoVwEvjNmWvhc_IEyBWvnibiFDwUos2FzsL21ULTmYNf3YzQp5z73eg6PcVZ6j5dRQDmPzz_UhuRZSwTIvs0VBfKcQpa64-aSVj84F58v88b8jj9v_1s1nKDP6OxGKTB483t_66KkUkW09LI5lfiMSWX3Jaw628pgG5neljrECkYqqzemKmL_gNAD56xPtEszXHqz97FYSgn5e2AShHaQzi_gwc6-otrPvWipl30-NK5woinfhPWWlvGC2vr4IjYExkIXgq3EfdAeJV4AoJ-x9kBMIoa3J6Lqav1RjvmHoQPr2hzJbXZJd8L8JHFHzKLCGQWQhWIxfY9SWzksx5k0Ig4AWSzWjd-l2CNeq5-vjtS05t3HLQ-wn_FiAGdFxWgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a01cc820b.mp4?token=YB4O6MZIM0aUQRHmofp14rocl-q3s6n16NTm_PkbXFT8bDDWqiH20TbrmUMWBFKQHReRctY4aq48hmUCstW_t7s-DJuhFJ87ssqSBQFYGpI5fgBO3Bg4mdiAXIdnsab0k3bEct5RSZJy6MCUdbr-kcfKDCERu6Vb1VSnpyj-8ALlOHLuWqV-AQdNbn40xoizbLo5A4O05tMjsgZPZgV9rVyRsu8ULRfkWy8H-jFag-adE7XxQyMXzkqmqqI96kQHWCDEKIaPN7-8hGrhADdcnfrvlPrhYGB4nAvE13N2cgoVwEvjNmWvhc_IEyBWvnibiFDwUos2FzsL21ULTmYNf3YzQp5z73eg6PcVZ6j5dRQDmPzz_UhuRZSwTIvs0VBfKcQpa64-aSVj84F58v88b8jj9v_1s1nKDP6OxGKTB483t_66KkUkW09LI5lfiMSWX3Jaw628pgG5neljrECkYqqzemKmL_gNAD56xPtEszXHqz97FYSgn5e2AShHaQzi_gwc6-otrPvWipl30-NK5woinfhPWWlvGC2vr4IjYExkIXgq3EfdAeJV4AoJ-x9kBMIoa3J6Lqav1RjvmHoQPr2hzJbXZJd8L8JHFHzKLCGQWQhWIxfY9SWzksx5k0Ig4AWSzWjd-l2CNeq5-vjtS05t3HLQ-wn_FiAGdFxWgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
صحبت‌های هواداران استقلال در ورزشگاه
❌
ما رامین را نمی‌شناسیم. این جام را به ما بدهید. پرسپولیس با تیم‌های ششم امارات و قطر مسابقه بدهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104942" target="_blank">📅 20:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104941">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a93dbbe2f.mp4?token=F79XcFuD-ACLfhN7ppbl6UUKqXjz4UirHm5SY1hoC-tOUHVxnDE9ySLRVvNxxhW9K--dz_gmVUPmvq49fA7btqRWN0kPxJmeN4kSzca6_vCkY6xzAJL5RJCkqYqaVbhIgFqh40dl6pb4sZAN3Me5oij9C037HJLsFqtZxMGh4ckHZfqO9t5ktfFfS3Ba20xBKptSKg24Yb1i4rKLHDGcS-jJcR9nFBfP-R61A2j0ClNTIwfiHniSqLwmhH82artNHa9noj8PpEzM5M5yADJv4WICATsIiy0952IpKKFM4wu_R1IzI-n4OLnFbH5RYlRo0xh6DVYzDhLLIFT3ORksLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a93dbbe2f.mp4?token=F79XcFuD-ACLfhN7ppbl6UUKqXjz4UirHm5SY1hoC-tOUHVxnDE9ySLRVvNxxhW9K--dz_gmVUPmvq49fA7btqRWN0kPxJmeN4kSzca6_vCkY6xzAJL5RJCkqYqaVbhIgFqh40dl6pb4sZAN3Me5oij9C037HJLsFqtZxMGh4ckHZfqO9t5ktfFfS3Ba20xBKptSKg24Yb1i4rKLHDGcS-jJcR9nFBfP-R61A2j0ClNTIwfiHniSqLwmhH82artNHa9noj8PpEzM5M5yADJv4WICATsIiy0952IpKKFM4wu_R1IzI-n4OLnFbH5RYlRo0xh6DVYzDhLLIFT3ORksLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول تراکتور به چادرملو توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104941" target="_blank">📅 20:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz6muRenhdzT_dXDqtVSEckHIhMyebkPvlIDbpy6l-cKV2KnekH9nqRF3D-B0kVrRE3IUsmvf2KsL303DzqrpcsRNjoBOLZhJ5EjU2zd0riKAs1xYY_wyh0cP7qU_NAYqR9zYD7YdBay6Gx4C0O6dmC46uCvuSsPBaLuRB9t1VWRyqdCTvjCz6BZtJxn32i64MCN5Ro0dMIEg0S7fPQG_CgPUNNLXHHX4dFZ6drfUfEWBXr9eMAP6CI80j5Renm0biNd7hzY8T4AtJjPFaFifAtt524qC7kSaCNvQN_LmrZ356op5U1Y8Y2Lx4aEMv76GPMoldyZKJl7MaERy3b1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس‌النصر مقابل التعاون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104940" target="_blank">📅 20:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cdd650bf.mp4?token=l8eaX8hn0nUjfSee3JzHw_0uuNPmO4olDTcH--YCF0IOILHOrcdLqvweyTgaJW5Q_1Um1Nehrq6q_C_lmBtYFU-X6jZaWAZLpns1L4Bcf7P6pOhC7ruETL9QJJHmEVTfL9o1JzMSi7lr9O026dvTlkjX8-kxSokLCX_y-ZbDiwMTFdwhSKcsBOBP3ZTQpldTi_5DhdTv1IJTsa4m72ty8mwIRIBC7vruM-buSiNR1o4W7bq5tkeNACj9Cj1mmjVCCh4HNDNsVlxqWxy2Kz2mnbnbVVXrwhY3G61wGclWfwQQoVDyEVbs8fazptNRc2Plbg4ZpAXAwzheTdtsM-MGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cdd650bf.mp4?token=l8eaX8hn0nUjfSee3JzHw_0uuNPmO4olDTcH--YCF0IOILHOrcdLqvweyTgaJW5Q_1Um1Nehrq6q_C_lmBtYFU-X6jZaWAZLpns1L4Bcf7P6pOhC7ruETL9QJJHmEVTfL9o1JzMSi7lr9O026dvTlkjX8-kxSokLCX_y-ZbDiwMTFdwhSKcsBOBP3ZTQpldTi_5DhdTv1IJTsa4m72ty8mwIRIBC7vruM-buSiNR1o4W7bq5tkeNACj9Cj1mmjVCCh4HNDNsVlxqWxy2Kz2mnbnbVVXrwhY3G61wGclWfwQQoVDyEVbs8fazptNRc2Plbg4ZpAXAwzheTdtsM-MGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل‌کسری طاهری در بازی امشب سپاهان
سپاهان ۲ - ۰ گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104939" target="_blank">📅 20:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ca3971a9.mp4?token=glr07yokultKBOE__NYLw3RyC78Gmi4k7hp6ytkNOLGLtXVTiakBUT-DdHjF1DWaQ4WFmzTV3bHPziMnwWEM3M2woS2ck47IO870NtuSBm0E90UFoPmLapPr21aIV05g6XVMCSnhtX9EM8AfOEr6DJGQ5Hj51jpfm-lqJGp-vewWKtzmti1v_5svxV-7VQPWQVULLFthe2lIr8Vef18Ea-HEB3plRzrJlblfiRsmqbv1xXWnNDtdCaD9ryJhQ9woeA3uoYS0aPoYGLYU6vc964zzX6gaDOZz4qO7Z0sg88LtJACUwUTUZBnh1D6tbB_WQJ9hJpcKtJYeATvBPVd1_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ca3971a9.mp4?token=glr07yokultKBOE__NYLw3RyC78Gmi4k7hp6ytkNOLGLtXVTiakBUT-DdHjF1DWaQ4WFmzTV3bHPziMnwWEM3M2woS2ck47IO870NtuSBm0E90UFoPmLapPr21aIV05g6XVMCSnhtX9EM8AfOEr6DJGQ5Hj51jpfm-lqJGp-vewWKtzmti1v_5svxV-7VQPWQVULLFthe2lIr8Vef18Ea-HEB3plRzrJlblfiRsmqbv1xXWnNDtdCaD9ryJhQ9woeA3uoYS0aPoYGLYU6vc964zzX6gaDOZz4qO7Z0sg88LtJACUwUTUZBnh1D6tbB_WQJ9hJpcKtJYeATvBPVd1_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
هم‌اکنون نمایی از استادیوم فولاد آره‌نا اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104938" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD0dX8vlZYvqvx7rPrh6XnR0a-rdlqlLUoz9vwvuOy7DRB6iStCVr8xFv3Tf7144qdjUK4wI7EACVi1UKn_htdJmtqJTX7XZebVq0GXV-W7Jf1db2J3Lie-hsl3LQaElScm-isEKh38D9zXmquljGa6PK-IyKc_sQG9y8x7j41kDRSnBVPtQ8O0eosun5qEQkWWSQigDZnonNHtgXcx2j3BMWu_5FScIbOx1EAYzjT0_X7tVypEZ-ejowWiMM9_kqP2g-7RZ56gBRRhPob4gUQUsxXqeUtte6_sZ_kwD2fB7LAXl7CP9xtFCOOWulcV8qFMdF40yuTLSsYN1A2lRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل فولاد؛ رستم آشورماتوف نیمکت‌نشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104937" target="_blank">📅 20:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLLX57tFQ-d0Tu8VWnKHLBRfzQXN2WEJrLTyUcsFZQkDXk_IGQidDjaruup74Doh09fkdWudgZkrvv0AIUcoRHo825eLUZibrzUB2qCfeCDzNBm0RSY5KAa7LOxRExWSlP7bfvSpxIDfyvBHi8twVJdyg2YXN_-3elMHLmPnSMSUUQtZIZiI2BLjjCdiKJL5A2zyjWy9Hl-dzIFZThEKcnAUJzdl-kJqwzGbO-Mg8iGR7opQl9r2sKn21luY1nJYC2rhCnnZGbglAPltkheg7Fw1aer3FLULw8ftcmVU8Tr2plpgdccAH2PtRLyvEKVGZnfcXeB0mFH5zVxh0KcWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل فولاد؛ رستم آشورماتوف نیمکت‌نشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104936" target="_blank">📅 20:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2f021f29.mp4?token=i6XyHn-XabOdsZmIWqmFVWhxlODRQ5H2ePKy76Fb_od1kNXBmu3kGptTM3wl_If0HzKwM8ldIk-7L4J5n8zpzEkaCl6oHzTOQR2qkAuS36XazFXb40OCvnyBQ95QB7i2NWCkQ7x2vohXujOt-CrcjvYRhQcEv1LUM1qubowOCRrlE5uBE0Wr9RQXzO4jv-0O8vVJMIjfL3czZpEemKbhkjYoZqhzVby_VXcBd7E53M0VwtVcrrjRnV-wLCdlw2lgW5QAAB82fPGXghk9mIeNBlysqiu19d56rK1FtE1y13Mn6iSVtBJB7M_MouZhhocaF0Ho6MJ-MGsw2VD8AJ-Ncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2f021f29.mp4?token=i6XyHn-XabOdsZmIWqmFVWhxlODRQ5H2ePKy76Fb_od1kNXBmu3kGptTM3wl_If0HzKwM8ldIk-7L4J5n8zpzEkaCl6oHzTOQR2qkAuS36XazFXb40OCvnyBQ95QB7i2NWCkQ7x2vohXujOt-CrcjvYRhQcEv1LUM1qubowOCRrlE5uBE0Wr9RQXzO4jv-0O8vVJMIjfL3czZpEemKbhkjYoZqhzVby_VXcBd7E53M0VwtVcrrjRnV-wLCdlw2lgW5QAAB82fPGXghk9mIeNBlysqiu19d56rK1FtE1y13Mn6iSVtBJB7M_MouZhhocaF0Ho6MJ-MGsw2VD8AJ-Ncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✅
👍
تیم ملی والیبال زنان ایران با پیروزی ۳ بر یک مقابل اندونزی برای نخستین‌بار در تاریخ به جمع ۴ تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا ۲۰۲۶ صعود کرد.
تبریک میگیم به دخترای عزیز کشورمون
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104935" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3zIuw5Db36lZtJHT936C70cA2wqVM-3CHCHqC_saqELMn3q5b643Jac_S_8j7YiBruDlcf0XnfSfiaheUVTGjYWGE6FZJO8VvAD-_tnqUQAAFCBhKEiqkwJ72z2XhmfLR2Tv2xh4DkdA8FMkjit4q4DsUn-SPBq80uWjRLKJTV411rmWeq2LC1p-_qshmm2DEEq_aKRMrn3i41Ww8GUEpB301rYPZKN7RzRhtYOoD0HQcT_Sa94Q7PIwZ7BYhLMs6ELftS-MlTM6WZ7IrorxjTMkJEPMemB87jD9Z6NNZ2l0St27waeGNY5maHBjBVTdQ6opx5pfALaF0hw8Ae9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب فولاد خوزستان مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104934" target="_blank">📅 19:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded8751287.mp4?token=HwueMZjP5VrLZdWQ9F5zkPmY7MaCN-RZjhGu1nVlOsiR9rbtH7Dtmv3YL7yas9WXEcG_j3ccArztKWuDCmtaDcXsbRcKTHzzkBZdQ5nXpmGvDpqBJVMKDsHROBctQ5RTDSviZw-VLSHntJdUCm-jkN5i350RzoHdIFBXv3ZkcAqUQfShzpLYGVw5FWof9nE9HdlkoH_8kc2y7iIcFLt1LVQs1bS5Kbqame4Y7gBMN97aAne4BYe5D0B-6usSlDu3c0Ga-h_oNCgXWxqmBrdXoZ7CshZOdb7a4zNG1aBUlNNzwhqSrWAq6duKFarzQ37zDDqUELcZwYYStKCITWSPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded8751287.mp4?token=HwueMZjP5VrLZdWQ9F5zkPmY7MaCN-RZjhGu1nVlOsiR9rbtH7Dtmv3YL7yas9WXEcG_j3ccArztKWuDCmtaDcXsbRcKTHzzkBZdQ5nXpmGvDpqBJVMKDsHROBctQ5RTDSviZw-VLSHntJdUCm-jkN5i350RzoHdIFBXv3ZkcAqUQfShzpLYGVw5FWof9nE9HdlkoH_8kc2y7iIcFLt1LVQs1bS5Kbqame4Y7gBMN97aAne4BYe5D0B-6usSlDu3c0Ga-h_oNCgXWxqmBrdXoZ7CshZOdb7a4zNG1aBUlNNzwhqSrWAq6duKFarzQ37zDDqUELcZwYYStKCITWSPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌تماشایی خیبر خرم‌آباد مقابل آلومینیوم اراک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104933" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fddb9c4e6.mp4?token=fhY8vhgXdwllPlle5BZF_8xFIEfaLDUAe5lV6vywmTV6CUXXaYWh4m4_ld8KdKYPfLxF8tLq7EYsTYeCufYa7-1VoCneZ1m76oU9P2vK6XekDIeCUXHHNKMqWOd1IT7M9_Il_6wqTbCpTopuPno2GcGmgTOXE31NBkwA6sz9m602EnWyU30FlDFB_fXrP3EEvz1RcL6O5gvDACawNQkGoluHO4FsKzIe7R2LXHozFGk_QILnYexD4LGyCIKSctVLZYrxofzmSjpvGTZrQTu8TMEmNtOH-OkmyVXVFmosXew4EilDOrqy-dsSUXSiV2G-W2b7t27wujI_kNBmyyCTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fddb9c4e6.mp4?token=fhY8vhgXdwllPlle5BZF_8xFIEfaLDUAe5lV6vywmTV6CUXXaYWh4m4_ld8KdKYPfLxF8tLq7EYsTYeCufYa7-1VoCneZ1m76oU9P2vK6XekDIeCUXHHNKMqWOd1IT7M9_Il_6wqTbCpTopuPno2GcGmgTOXE31NBkwA6sz9m602EnWyU30FlDFB_fXrP3EEvz1RcL6O5gvDACawNQkGoluHO4FsKzIe7R2LXHozFGk_QILnYexD4LGyCIKSctVLZYrxofzmSjpvGTZrQTu8TMEmNtOH-OkmyVXVFmosXew4EilDOrqy-dsSUXSiV2G-W2b7t27wujI_kNBmyyCTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول سپاهان به گل‌گهر توسط کسری‌طاهری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104932" target="_blank">📅 19:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b835e745.mp4?token=CCUGVKPRAkoKpXvr6fFWHB9ZdM7YqmR4CAIdaSoar70mK1sL0gOC6NV3sHzXGlWMPlB2YCGv6lFsu4v6ryw5-rSOhRfidGhmvXvkS4mEB-CO_hJ8dBnQkGztGyxyylraK7hjhzBDoKwbVNgZnx89dGLjP1aTUuwmIptIeT3De8g-GOAFz4F41_nfsMWJHka-lDA-J7DUqRXLJhM5UeqlMHbIktDJhZhFk35-Y74SEhJOUFkcEDNwpgtsNmk7IQa8XbIr9VDjGnPxx4hst6wrJgIYSprmw2M1087p8apbbaDc_fuoWoQ9DkG4zeZB7XjA7EbJu-xGAdArxmW_26BhjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b835e745.mp4?token=CCUGVKPRAkoKpXvr6fFWHB9ZdM7YqmR4CAIdaSoar70mK1sL0gOC6NV3sHzXGlWMPlB2YCGv6lFsu4v6ryw5-rSOhRfidGhmvXvkS4mEB-CO_hJ8dBnQkGztGyxyylraK7hjhzBDoKwbVNgZnx89dGLjP1aTUuwmIptIeT3De8g-GOAFz4F41_nfsMWJHka-lDA-J7DUqRXLJhM5UeqlMHbIktDJhZhFk35-Y74SEhJOUFkcEDNwpgtsNmk7IQa8XbIr9VDjGnPxx4hst6wrJgIYSprmw2M1087p8apbbaDc_fuoWoQ9DkG4zeZB7XjA7EbJu-xGAdArxmW_26BhjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
دریافت جالب و دیدنی پارسا مقصودی لیبرو تیم ملی والیبال زیر 17 سال ایران در دیدار نیمه نهایی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104931" target="_blank">📅 19:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104930">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b2bd316d.mp4?token=crIPox-NSLUjKb5IPTXw2O40_mcqD8DQTpi61PDx2ZlhNu53l5-lPgniAmGt5FOezlSzNQdnD2jAPODHp8hiZUzMRXhNFujvF_5ARcnNvr_JOxXO3nIkMx1bpu8y_pWFLyc6ncTD5V6Kd8izHchcd9qdG0KAEAak_JZNwRGlf_rlKQo3t3IXsWUv9kqkXD3NMdRXatmUjngm40mx75dHJEEbFz7UFtFscKDVRreZlW7rc4sz3aR2qbSqr5sDGhGvsbOvLI6StYNI9rDOyNMS7WhL4S4vFeteE0ECQmwOVyQ6Q0AXLBUCp9qmMELrIAI-vEXoLh7KWmniqGpiK6QD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b2bd316d.mp4?token=crIPox-NSLUjKb5IPTXw2O40_mcqD8DQTpi61PDx2ZlhNu53l5-lPgniAmGt5FOezlSzNQdnD2jAPODHp8hiZUzMRXhNFujvF_5ARcnNvr_JOxXO3nIkMx1bpu8y_pWFLyc6ncTD5V6Kd8izHchcd9qdG0KAEAak_JZNwRGlf_rlKQo3t3IXsWUv9kqkXD3NMdRXatmUjngm40mx75dHJEEbFz7UFtFscKDVRreZlW7rc4sz3aR2qbSqr5sDGhGvsbOvLI6StYNI9rDOyNMS7WhL4S4vFeteE0ECQmwOVyQ6Q0AXLBUCp9qmMELrIAI-vEXoLh7KWmniqGpiK6QD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سکوهای استقلال در اهواز تقریبا پر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104930" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104929">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b980e101bd.mp4?token=sL9KkI39Woxud71K5z38l6_f1OtUrOSTTvmvHtWDH53AuSKRX0BSlHLYkPhoOFdKVB02oCGnqLQemDZMtGzLiF3KJGUyOHYqvE6hRqRpH89372Dz7Fs3cLsnINIFi1xI1aw0FukH_oh6CodIdbiAIwXNHuLG7KvZO6e12ZUZcPAopdBcozqsEWhh2aVU3z39wyElec8oTYy-WhKYKtfDICSYgZsdicgMnm6erpJoFIQINhOhOCgZm9vJ6HE58zjfHmKGPAN6Dgk7iVVywANIopHECX5Jnl4G8IF8HH3HWWap2b8tZpFZ11aAOb8gfp7WR7U3I3u9a1CEHI0CQKancw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b980e101bd.mp4?token=sL9KkI39Woxud71K5z38l6_f1OtUrOSTTvmvHtWDH53AuSKRX0BSlHLYkPhoOFdKVB02oCGnqLQemDZMtGzLiF3KJGUyOHYqvE6hRqRpH89372Dz7Fs3cLsnINIFi1xI1aw0FukH_oh6CodIdbiAIwXNHuLG7KvZO6e12ZUZcPAopdBcozqsEWhh2aVU3z39wyElec8oTYy-WhKYKtfDICSYgZsdicgMnm6erpJoFIQINhOhOCgZm9vJ6HE58zjfHmKGPAN6Dgk7iVVywANIopHECX5Jnl4G8IF8HH3HWWap2b8tZpFZ11aAOb8gfp7WR7U3I3u9a1CEHI0CQKancw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آغاز درگیری‌ها روی سکوهای فولاد آره‌نا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104929" target="_blank">📅 19:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f2a045c7.mp4?token=GfXC38RP1VgGq7gCYN_JEIrMjyfuHJaTZEPCvSKKk7vrpZO1G9-7TVKbCBhtBiH61TLEY66n5e8U8dLy6sNetao8ugJMgPIoIlxK84xcnuqqf4BJXRiMk6jGLZwvHGP82LktDYq-AhcIaoHvTw79MGkrKh1TRZ5bDJPHHy7yuCqqWweGZasuFwskPDzQR5wY8VfKxmymV33XCNtuXMYmLorLDqEEXj6BUGsBxdoKM6PDD1bVoxBxNBHQ3dNuZWrc1uN9wyU3dyQeGmrMAW9hUEwCo5MX00_IEQodTCg8B15kqozM4FQOuC6Hajij7sSmQP_YIcocPHNyD-xR0gYcVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f2a045c7.mp4?token=GfXC38RP1VgGq7gCYN_JEIrMjyfuHJaTZEPCvSKKk7vrpZO1G9-7TVKbCBhtBiH61TLEY66n5e8U8dLy6sNetao8ugJMgPIoIlxK84xcnuqqf4BJXRiMk6jGLZwvHGP82LktDYq-AhcIaoHvTw79MGkrKh1TRZ5bDJPHHy7yuCqqWweGZasuFwskPDzQR5wY8VfKxmymV33XCNtuXMYmLorLDqEEXj6BUGsBxdoKM6PDD1bVoxBxNBHQ3dNuZWrc1uN9wyU3dyQeGmrMAW9hUEwCo5MX00_IEQodTCg8B15kqozM4FQOuC6Hajij7sSmQP_YIcocPHNyD-xR0gYcVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
شعار هواداران اهوازیِ استقلال: فولاد به شهر ما خوش آمدی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104928" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqNoGlEUldJ4UbynHZlpx67zxLqYIEzZIFoeorp56VyuEFIqLD1jBAn4Hdw3LalQpCf7DhQ6IuMH4OYvy0-Gy1yzV767jv6lqladb3DbZFhR1gbGlEpz7QtNjKnk5GcV8bEkWPydwu2j6oBW6S8cowhw7EcHvB8hi4543ke3VQqnTGWWDXlZ2VgDR1ySmvfhgHKPYWDTdQJxaOvdUs7a4wZS7xYeqGUNij1CcMLcXe214sIy97SBjCYPGBVatL6Spzwejt4J5FSqQxDDTe6p79aSsCxZkTjI_t8qlXcg_fjiVjHggQiqJ-_AO80AqCW8BhW-38I-WC4xl5ZHQKp7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از رومانو: رافائل لیائو با مبلغ ۴۵ میلیون یورو از میلان به گالاتاسرای
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104927" target="_blank">📅 18:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04a994664d.mp4?token=jZpIM1cxyghtXH3P6d4BRS0fWXaoaA9X7iSgTLUcluSGF3CN5zIFztDi_TUuAZmqG1K9t-l4tM5zzNJgAq35cS3jTb7Jb4ffsvuL66GggXqTJk_qV4GBSUdGQAnFmbECt5pvuDK-oi4xP9Xzpxl00ARI4rdqpy-mpbI64XUh6sGyHXCKI9VnsXLGUsqUgGZIoHZy3TToHAkVIWKh_rSOKn0u5s6AfbU_LOZjqHZxvnzBbU02F9LkbLz2nGKgYpQIs9rs6vkZn8K3l-yn8Q19fxDNYARCCyUPLY-2lXkEpcmbOe8YG5NxTWqvmXbSDNft86qDjkCU_fvSWyp-BLnyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04a994664d.mp4?token=jZpIM1cxyghtXH3P6d4BRS0fWXaoaA9X7iSgTLUcluSGF3CN5zIFztDi_TUuAZmqG1K9t-l4tM5zzNJgAq35cS3jTb7Jb4ffsvuL66GggXqTJk_qV4GBSUdGQAnFmbECt5pvuDK-oi4xP9Xzpxl00ARI4rdqpy-mpbI64XUh6sGyHXCKI9VnsXLGUsqUgGZIoHZy3TToHAkVIWKh_rSOKn0u5s6AfbU_LOZjqHZxvnzBbU02F9LkbLz2nGKgYpQIs9rs6vkZn8K3l-yn8Q19fxDNYARCCyUPLY-2lXkEpcmbOe8YG5NxTWqvmXbSDNft86qDjkCU_fvSWyp-BLnyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
شعار هواداران اهوازیِ استقلال: فولاد به شهر ما خوش آمدی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104926" target="_blank">📅 18:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqgPEsCKmDc0FyN_lzwxkYgmMZ37tN9gyIL1QAfuFbsRzW1oM9muapMUb6nzlkoqQLD6rKCxtgH8YJmeoMDgJCP3jpPsQYl0Cqddj4tUcM1DUSlcWQqfAHSzgWWORwro52y7xwu5hHZRrqpB2rIy1ow_qJh1pwAl1Tuv2DSuD9__XMqXgJkggr0V-3pCjTy9sI8nAwae4TY6uIHDrIAmeqwuraC5aR9azckrSo0N7r1nJXnumVe7P5dZinCfrB_6hnniRq1z5ofJCo7DbfG_n9H7NShMMHbGh5Dc6BeOaZXjmjYhKCoxhiwgX8Emuo1vWEYHgT5SjW13-eameI4iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ابراهیم امبایه از پاری‌سن‌ژرمن به استون‌ویلا پیوست. مبلغ ۵۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104925" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31b21a19d.mp4?token=nn4x_uAw-oYyzeqQ64dxcjkKxmmaRDlhCs3NL5lOx1B4LIqHuxvradc6GG_Wt-J0QBEqcDGL0f9isx9wg7WJYemLAjBdX1up8E1gzgIAws3_hx2Dhn2fN4R2ZPN_UcEbDz3cc542ghQFQSl4HScO16LWNsJJfOAZiZ7N3JSuxBs5maE0s9rwO0t9mWWln7tapOViSqYbyGJGdNvUh4KCsH7IFQMoE-bPaCX_QfBJ9mRvHmoYJH1xzkirDyUGegwD-dTEq0vQdNhI9I4iUTqlJKD9tzEPYiDXAJSMh1Z5XfyxT6H7OSfrfJ4z2F6bdMozj2jFdzJ17tkMieOwfe-rSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31b21a19d.mp4?token=nn4x_uAw-oYyzeqQ64dxcjkKxmmaRDlhCs3NL5lOx1B4LIqHuxvradc6GG_Wt-J0QBEqcDGL0f9isx9wg7WJYemLAjBdX1up8E1gzgIAws3_hx2Dhn2fN4R2ZPN_UcEbDz3cc542ghQFQSl4HScO16LWNsJJfOAZiZ7N3JSuxBs5maE0s9rwO0t9mWWln7tapOViSqYbyGJGdNvUh4KCsH7IFQMoE-bPaCX_QfBJ9mRvHmoYJH1xzkirDyUGegwD-dTEq0vQdNhI9I4iUTqlJKD9tzEPYiDXAJSMh1Z5XfyxT6H7OSfrfJ4z2F6bdMozj2jFdzJ17tkMieOwfe-rSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
امان از دست هوش‌مصنوعی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104924" target="_blank">📅 18:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a984f5caff.mp4?token=nGAS_an4VFlp7DBcxnnMmlzrq44CrbyxGKNiJy12Qp0ye9ykGbvWoQJwFydkNDsjSbUT09aNzHSLuBB2vZsvgPJwWgkgafhWmiZmxzlnDdMEG00Lsf_At6Wtzdr4BItfPfvfaCrIUeAoOsV1BPWo5ET5kUdDqQV7kc3g-yr1I9oLbaajPIv05jhWZ371vuDSVk1yEfDrDZ0FFSReOfPiB84IQW9rY26o81ls6SeYZ1mkl_bCel35rQKaNx1YX18UcuAgrJf76C5xj989GX0d9frSB55l-E9JDRrs-7pSfgguG595GIlNsZbcZisYSJehtKhwZuGKyrsa1WuddfoYwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a984f5caff.mp4?token=nGAS_an4VFlp7DBcxnnMmlzrq44CrbyxGKNiJy12Qp0ye9ykGbvWoQJwFydkNDsjSbUT09aNzHSLuBB2vZsvgPJwWgkgafhWmiZmxzlnDdMEG00Lsf_At6Wtzdr4BItfPfvfaCrIUeAoOsV1BPWo5ET5kUdDqQV7kc3g-yr1I9oLbaajPIv05jhWZ371vuDSVk1yEfDrDZ0FFSReOfPiB84IQW9rY26o81ls6SeYZ1mkl_bCel35rQKaNx1YX18UcuAgrJf76C5xj989GX0d9frSB55l-E9JDRrs-7pSfgguG595GIlNsZbcZisYSJehtKhwZuGKyrsa1WuddfoYwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
امیرحسین صادقی: مطالبه هواداران و پیشکسوتان استقلال، اهدای جام است
🔺
یک تورنمنت شاهکار را به فشار باشگاه پرسپولیس برای سهمیه آسیایی برگزار کردند ولی وقتی به استقلال می‌رسند همه تغییر می‌کنند/ هواداران از من خواستند پیگیری جام قهرمانی باشم/ احکام وقتی درباره استقلال باشد زیر و رو می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104923" target="_blank">📅 18:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/877443a39e.mp4?token=vQvZ06wmdvDh-5J0p6d7oGTlkhZVYGrAhsWLVcrecGCgkZUs2qjk8eMsoaph18eajKVSWJtVR7P1wYQSW3cMvH4UkBBQ-4k5Fp3kSlcCj9W9Z3CPL-FNGk9FRYKDlrzRk1UN-yOcsjRf2mvodisrCIo1f0L1R-fHtOHQ_K0TKRAbaLY8mjmGaOYyggZSFg1NtqoJbCVHoAZYSDZVgRonxhj7g_75rkXUDKVqvokmf_RaKH4bMWmDpHCwtCU98lhRRZogOlUgjePiP7bzCsBaQTet1x70llZTKKwHlWTj7XlHnp_A2hOWR4HHfMOVCLwoBNH7_Bq_PS22r5PQloJXVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/877443a39e.mp4?token=vQvZ06wmdvDh-5J0p6d7oGTlkhZVYGrAhsWLVcrecGCgkZUs2qjk8eMsoaph18eajKVSWJtVR7P1wYQSW3cMvH4UkBBQ-4k5Fp3kSlcCj9W9Z3CPL-FNGk9FRYKDlrzRk1UN-yOcsjRf2mvodisrCIo1f0L1R-fHtOHQ_K0TKRAbaLY8mjmGaOYyggZSFg1NtqoJbCVHoAZYSDZVgRonxhj7g_75rkXUDKVqvokmf_RaKH4bMWmDpHCwtCU98lhRRZogOlUgjePiP7bzCsBaQTet1x70llZTKKwHlWTj7XlHnp_A2hOWR4HHfMOVCLwoBNH7_Bq_PS22r5PQloJXVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خریدهای جدید بارسا دارن از حضور در این باشگاه کیف می کنن.
😍
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104922" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104921" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihVX9pIW5kgSrpD9foES7Ag57-TNoUXbDJ-o5ThFXlCMlGp0H4KGlaAGF6Gj8ueJst-N1HIKATiue31f3edswtPwUdfzgFOGvshV7eT4OmUTG6jdxNDRU6OkWINPZe7ISIVbfkNK_VJn4lvoE2IgmeVPhsWEXCdz0IudYA9rMXetJeBvWcwso0y0q-yMLF57B_WG3KlqMZC0AMizRk_687EAVi4aZzXaqVx35basi9f4DPcSwyxLIeIdi6Id07VZ_yAYyI6214aIyJmWaRaC7zLpVN-jGqYHU4RfcpCl7Z50vsgX-qn0Db8qTYzfbITDZIQ6w_YvJIUhl22FnuffBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104920" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8qhX7trwwLAqsGmpNq8IUec_ii9wjpytrorFaRqBMO1V1gwXH_Czgga1RkxTSxetrYp7kWon2yjtKbSpuBBAbZhwepLecfEKN-1BB0sY0-E2fV_-uIKKE-dTaIKVfVzl8HxkCfDOX2dbyZ8ExyDcStIxTcLUDMFdnWS3dAM66OgM3L7JaXQDeMXVQyyHe-kcB5vbM2ZgVcL_0IY4zlW4Q2ZimLBRp9RGCHWcCP1KZBhLeC8x3coOUpe5jO0M3cai-2fU1GW1BDGX5M4ae5-_wSLQmxC-aBwznjyhnnQ99s943AVD9AHLcFIDWf_Wn8NuMC-w_7Wv7jPBSKb0JGLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104919" target="_blank">📅 17:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146c8ac859.mp4?token=sYnrIpS7alrh5E9GPv3Yf-L0MtSPnhsO68_sRB73hew7CRS-eHjLZ2oMuPGRdaKe_vdq_yK2WnijgjgkuraLqZuMRF8qskO8l1AvJHjSgtEZU2HjAe3Tl9XELUYSfbsbdx63WDxi2W4GSnPEA6wDX_ZcsiBrbUWlu5pwU_un9SvNG8oB27b3McmNEiECtRGpopiQThCFhdLrTihbzsUkLKjOGwRslo9Vf0tmwIKydGELTFQWI4gPonowlIhCnmNcl2lpGnLCFk7na-KCHkX9rkYNkqiDvcADCn40yC1czjQCVh-XplTYB0dFbSq0n-amHm7qodsb1awELL9SY8IVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146c8ac859.mp4?token=sYnrIpS7alrh5E9GPv3Yf-L0MtSPnhsO68_sRB73hew7CRS-eHjLZ2oMuPGRdaKe_vdq_yK2WnijgjgkuraLqZuMRF8qskO8l1AvJHjSgtEZU2HjAe3Tl9XELUYSfbsbdx63WDxi2W4GSnPEA6wDX_ZcsiBrbUWlu5pwU_un9SvNG8oB27b3McmNEiECtRGpopiQThCFhdLrTihbzsUkLKjOGwRslo9Vf0tmwIKydGELTFQWI4gPonowlIhCnmNcl2lpGnLCFk7na-KCHkX9rkYNkqiDvcADCn40yC1czjQCVh-XplTYB0dFbSq0n-amHm7qodsb1awELL9SY8IVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇺
لیگ قهرمانان 26/27 قرعه کشی شد و تیما رقباشون رو شناختن.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104918" target="_blank">📅 17:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f229668d9.mp4?token=IqtSDVp4rxtZYQGcOGkUQOxcIyuigpf7_zZoZpCSFTuC9pvVJgsRQ1jhOXi0pvq5hBhmXWHdAkhaZ14JoRSP6BNt7LOfPjyf2qUG_AlSD7O7tCiBl6tAXysYEoRRcO-PwqliD_MmLkp_S8EH5akpMaOKfyRa5dGMoz6kn-1XadHHEnYKWa6OSakRGc96oi9nDWc_3cT_4jCsTHc3EFQ6hOQhPSKFfs8Vj4KSOA3gz3BcdDmRicyoJ86xPQPAR6qrzOXlcNcSX4Ro54q6x-UX6Ru-cVpAhL37b2z-83YcsNUI6X4VHFfLU_f9cEXOPlQFpfGAPgFh7MheD6Nnp8tkLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f229668d9.mp4?token=IqtSDVp4rxtZYQGcOGkUQOxcIyuigpf7_zZoZpCSFTuC9pvVJgsRQ1jhOXi0pvq5hBhmXWHdAkhaZ14JoRSP6BNt7LOfPjyf2qUG_AlSD7O7tCiBl6tAXysYEoRRcO-PwqliD_MmLkp_S8EH5akpMaOKfyRa5dGMoz6kn-1XadHHEnYKWa6OSakRGc96oi9nDWc_3cT_4jCsTHc3EFQ6hOQhPSKFfs8Vj4KSOA3gz3BcdDmRicyoJ86xPQPAR6qrzOXlcNcSX4Ro54q6x-UX6Ru-cVpAhL37b2z-83YcsNUI6X4VHFfLU_f9cEXOPlQFpfGAPgFh7MheD6Nnp8tkLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
🇮🇷
صالح‌حردانی کاپیتان خوزستانی استقلال از هواداران تیمش خواست که امشب در بازی مقابل فولاد حتما در ورزشگاه حاضر بشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104917" target="_blank">📅 17:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl-cDtnp9-fkYOHe5akcklukvvdxRIA7-2IJqu304Ier0Xfx4mJJBVeLl7HWHdUMIuGLZjCL0xaDhwqGEtcFqt4DCDnK1pSc8K-Qqr-t2k5vYA8gru6KRCQQklVYiQHjh9QGFKSJlxPDVYImx80WZELxpFEhMQRpcGbzKJOvzvJu9-s_Dwz1y1GJ76PiSicnc4Dl-X1LnIAVeT_WLA6VmUGs3SI_B98ao-0dvP2Ag5-HVb9MtI5fhuxW73I_mc6wL849pbAWySlX3zFrV7_JYdYRA0tQBRHAj8BXut-un43fHtkJPyqRY-qDbPKlsQgdVj_umdd88YyipptZLEj6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
‼️
کادناسر: خولیان تصمیم خودش را گرفت. حتی اگه اجازه خروج نداشته باشه، هرگز به کمپ تمرینی اتلتیکو مادرید برای تمرین کردن برنمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104916" target="_blank">📅 17:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=fLjKyT7ydhyD0WIuOnMduyOd8rXdPaRc3vEPh6ZEdKUppV0tef-teS99feZIwokMGkpOhsyZl8sj8-DuCJKc71gNzpk0ZPLI9O9ZsUV4S7HTuoKXyJc8HuaNZ-rqY-AOlaQdzTu46fvUEKhrKgKxNtPjlVMGLval9mcdJyTTcczjg6NBDCqOiqS0xCnLgJzFgnp8gcKK6d0iKcWtWwyawyB956elI97c7Df459xnasUr682QS65TVtkmM-LCYuXDWb8Mr1rrtJrp7d1jbPmPdfGpmrUDmW6Zzv7RV6fMpqRtSaWVvKkVqTbWIQlIFYgIowPWb1Cc2YWCF4GsaaPiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=fLjKyT7ydhyD0WIuOnMduyOd8rXdPaRc3vEPh6ZEdKUppV0tef-teS99feZIwokMGkpOhsyZl8sj8-DuCJKc71gNzpk0ZPLI9O9ZsUV4S7HTuoKXyJc8HuaNZ-rqY-AOlaQdzTu46fvUEKhrKgKxNtPjlVMGLval9mcdJyTTcczjg6NBDCqOiqS0xCnLgJzFgnp8gcKK6d0iKcWtWwyawyB956elI97c7Df459xnasUr682QS65TVtkmM-LCYuXDWb8Mr1rrtJrp7d1jbPmPdfGpmrUDmW6Zzv7RV6fMpqRtSaWVvKkVqTbWIQlIFYgIowPWb1Cc2YWCF4GsaaPiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری شبکه ورزش : دوست دارم عادل برگرده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104915" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTbFn2aCVKtZ5PAqyP2Oc3zW39HEnFI7oxBqPGaLm77SCHwJjrtJDYcAKzszsdnTriWcTMbtHRlkyke-gge10qo-2ATfNtoPJrMr49AW0VmDCJ6mBPxOpPRr68s7YlqbLnRSJ0mZcuNa4rVtf0dZdel6SFq-HS9Ib8tJjbowMth4OZ2VrRl50RZnymyOylBbsKT1nqsrlpNA212_SfgmCTdfdwUk8qFhyZV7w0OMVTdexaJTKQQQIacX53yvd9I4XxTSmSZdElyfZZ4t8zK3lWhUd4W8w58PQ85x3dUq5S2n1meE4rT8CZ-x82NXT8DUDfszYQ5bt-KlY1xLG1VXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
پیام هوادارای اتلتیکو در ورزشگاه متروپولیتانو:
«هر جا می‌خواهی برو، اما همین حالا برو.»
«اتلتیکو از غرور تو بزرگ‌تره، خبل مارین.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104914" target="_blank">📅 16:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04262aed7d.mp4?token=GM4Kz-f9tczAtsi6PamcUjZfVYuGjAveZnYLxKY4gOWoY9J-2yhnfEku1QqdjwuUTzVuHYuXziA_HNTeeYMaBrM8TltGUU9iBdNXmd0dookJRMuanVwBeA8JtDV4mTDtrXCxKW8OZ9hpB_eOc9G065V1CXSx2FBqbKf7fhGdQucszH_E83uZKRnKvffripSgn_XEw2ER_SCc8SluJein9hQy2tH5VKFqA2Jk6mi51HT7lrvKbdlMJmO3aQtn0DpsKf1bPRo2FKOCjenfQmJQYiDPs1Ok2oZIxm3lQ7dbfwYYgp3T3BY4gyMjOLOp9z2gl3k7SqZTpyohClgCPdoE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04262aed7d.mp4?token=GM4Kz-f9tczAtsi6PamcUjZfVYuGjAveZnYLxKY4gOWoY9J-2yhnfEku1QqdjwuUTzVuHYuXziA_HNTeeYMaBrM8TltGUU9iBdNXmd0dookJRMuanVwBeA8JtDV4mTDtrXCxKW8OZ9hpB_eOc9G065V1CXSx2FBqbKf7fhGdQucszH_E83uZKRnKvffripSgn_XEw2ER_SCc8SluJein9hQy2tH5VKFqA2Jk6mi51HT7lrvKbdlMJmO3aQtn0DpsKf1bPRo2FKOCjenfQmJQYiDPs1Ok2oZIxm3lQ7dbfwYYgp3T3BY4gyMjOLOp9z2gl3k7SqZTpyohClgCPdoE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
#تکمیلی؛ تراکتور تبریز هم اعلام کرده که امیرحسین حسین‌زاده را به هیچ عنوان به اردوی تیم‌ملی امید نخواهد فرستاد.
‼️
🇮🇷
از طرفی تارتار هم چند روز پیش مخالفت خودشو با حضور سه بازیکن پرسپولیس در اردوی تیم‌امید اعلام کرده.
❌
حالا مشخص نیست که زور و تهدید فدراسیون…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104913" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=mhDU1dv3u9TrhWHoTHm3t9xu3y5EeWZp5isjy23PsSAEztzwa_nOXQZwMc2Qc595atkfVxIzQ4eaxhexbrJPY_F1w7HGw52FG4oL9z_F0NbQxsSqCquJa3c1VovbETHF4G6iIw82EUTje-6DfygPdmpoNvoivrOrgtds4Sr0ZQaklW5X9xzGs2RsP2IkW91-3CnlFzn58g3z4_5-KA8b0TDmXx1IXb2h08q7em7R32QIUp_vkZAih0tmhNTfwWSjVF6VXAQg6zaSR8-kMzcCp65SBkeJprIuNNLv_38xLyxVvJhoEkLnlaQEIZCvCYoLjGUKPhgqSWyrhb6F48kGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=mhDU1dv3u9TrhWHoTHm3t9xu3y5EeWZp5isjy23PsSAEztzwa_nOXQZwMc2Qc595atkfVxIzQ4eaxhexbrJPY_F1w7HGw52FG4oL9z_F0NbQxsSqCquJa3c1VovbETHF4G6iIw82EUTje-6DfygPdmpoNvoivrOrgtds4Sr0ZQaklW5X9xzGs2RsP2IkW91-3CnlFzn58g3z4_5-KA8b0TDmXx1IXb2h08q7em7R32QIUp_vkZAih0tmhNTfwWSjVF6VXAQg6zaSR8-kMzcCp65SBkeJprIuNNLv_38xLyxVvJhoEkLnlaQEIZCvCYoLjGUKPhgqSWyrhb6F48kGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تارتار: زمین چمن یادگار امام تبریز واقعا استاندارد نبود و کار را سخت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104912" target="_blank">📅 16:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5141cf449f.mp4?token=usnJRJzaC6rMwTD6hSy3bzbKrT--teiTb-oYDR8Xl7U1PV5ghA9z5qAlYPHwdaoS6WXQhkilgxIyIP_RFhWBLXmLjf6w4y3DY6UBsTgfr87wvcfzE9CO65S8qZFY4_pran0SyIjJQ4-M6ki23t_eBreuXJoXd49RnbXgYMUTm8vc26mz9QaRiH0sEbWRfVQ-OtMF9qnfW3oBKOyNEzGmUmE4inYt-0tXgoCEg7ZEyVEvHepz7Tv1ly3kYZs4JWPirSUP2GJtyYjKXi4AkIcwjytPNhtoBHpQeWpgVyHshGTS_5qVjSBVzVUXBTAcchM1FSmaySBmjhs-MsyrPIC2DWE9CzO9qOpSdLcfZflVBqL5qel7Nmh-P3b9hPXtJEfiMu5wDbm06c3EkDrTnsaWlPycxX-VRiCYSyIH5X9Zc454OYV2yVRycPPO1CRvbNaPvKFjpII0m3YGZCmdrR2z-aQNS-Fht2lYUx3-dbac_ozQg-odb08f4lyDcvtewbLcZfbaB0nk885rDwEgnL3tAXwsI75rtBmY0-KvrSaGQR5DDTd3Y0wriTppUBdJSWM7jaylgQFeJlLeKkWPwR1T6rDQy8ihZB_Z09FS61TGAiWoI2Y9QZgkv0YyET66uhmWIsGQOfsvljODqoZNX7zqtX7AXQVH60wW8puBT6nern0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5141cf449f.mp4?token=usnJRJzaC6rMwTD6hSy3bzbKrT--teiTb-oYDR8Xl7U1PV5ghA9z5qAlYPHwdaoS6WXQhkilgxIyIP_RFhWBLXmLjf6w4y3DY6UBsTgfr87wvcfzE9CO65S8qZFY4_pran0SyIjJQ4-M6ki23t_eBreuXJoXd49RnbXgYMUTm8vc26mz9QaRiH0sEbWRfVQ-OtMF9qnfW3oBKOyNEzGmUmE4inYt-0tXgoCEg7ZEyVEvHepz7Tv1ly3kYZs4JWPirSUP2GJtyYjKXi4AkIcwjytPNhtoBHpQeWpgVyHshGTS_5qVjSBVzVUXBTAcchM1FSmaySBmjhs-MsyrPIC2DWE9CzO9qOpSdLcfZflVBqL5qel7Nmh-P3b9hPXtJEfiMu5wDbm06c3EkDrTnsaWlPycxX-VRiCYSyIH5X9Zc454OYV2yVRycPPO1CRvbNaPvKFjpII0m3YGZCmdrR2z-aQNS-Fht2lYUx3-dbac_ozQg-odb08f4lyDcvtewbLcZfbaB0nk885rDwEgnL3tAXwsI75rtBmY0-KvrSaGQR5DDTd3Y0wriTppUBdJSWM7jaylgQFeJlLeKkWPwR1T6rDQy8ihZB_Z09FS61TGAiWoI2Y9QZgkv0YyET66uhmWIsGQOfsvljODqoZNX7zqtX7AXQVH60wW8puBT6nern0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
تارتار سرمربی پرسپولیس: ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است
.
بحث مصدومیت ارونوف جدی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104911" target="_blank">📅 16:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a61739d98.mp4?token=V5KIyZdBDrK0yR-Vmax8dawe5Ra_5SNN4wlWBJ-WM1ECvakTfP711G69uPe8mSXDEZmLPnWayKkXTtq285FFzDaVdVdAc_7ldkvmeryy01-QbAFjWDN79etqQxyrucRDll9cLnQSJgCgM4OD7rupDyaLn-a0Incp4LVxF89jzQ0hFkldwcGNExSRRuzf16PmOVfUVY0yNXm2RpFxQb7SHNxStMQyssA4QUm9mzkqxjXS1AxDJ6PBh0vd9Ba_Er-gNpVemVclTSuVFLCwL3Q2gydmH4kfF7sK6YTXSV3SbXmNq7XPWi6YA2jyA_4j2zNzYhPHv70Qgc0EQ71MwIjpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a61739d98.mp4?token=V5KIyZdBDrK0yR-Vmax8dawe5Ra_5SNN4wlWBJ-WM1ECvakTfP711G69uPe8mSXDEZmLPnWayKkXTtq285FFzDaVdVdAc_7ldkvmeryy01-QbAFjWDN79etqQxyrucRDll9cLnQSJgCgM4OD7rupDyaLn-a0Incp4LVxF89jzQ0hFkldwcGNExSRRuzf16PmOVfUVY0yNXm2RpFxQb7SHNxStMQyssA4QUm9mzkqxjXS1AxDJ6PBh0vd9Ba_Er-gNpVemVclTSuVFLCwL3Q2gydmH4kfF7sK6YTXSV3SbXmNq7XPWi6YA2jyA_4j2zNzYhPHv70Qgc0EQ71MwIjpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⁉️
داستان پارسال ماتتا امسال هم برای آلوارز تکرار می‌شود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104910" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🙂
🎙
از سری نکات شنیدنی امیرمحمد زند :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104909" target="_blank">📅 15:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104908">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0c43226f.mp4?token=isoihpUZsFU1hgBRoCLMWh50GYNaWilXTsQX2IzGuxYQfOauOaoq6zRPSqEyKWfAjYoCC_FY8UfKXtvLx9NsMsqH9f6wud1xEXYIW8oppjkLwImMCQk1LQ3QoOnKuAljbh-efdwXkOvu74oYzc5cYw6OJhhSDWTUGt3hip8KgNp0BKGMzCfWFYA_yarzQCL4SwByHnpMxyDV8xGNxAtunKdYd0rVBJ8hLEX3n2rEALDhkaS_HxHTwIGrhe4H20bUCPSqZUvoL5QnJg5p_2Alyx8WIw4zzASlMOdjh6szMbdwf8P6fFp1ZC79x-MLDj3INJU4MQpxdJk9m4tEF6SMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0c43226f.mp4?token=isoihpUZsFU1hgBRoCLMWh50GYNaWilXTsQX2IzGuxYQfOauOaoq6zRPSqEyKWfAjYoCC_FY8UfKXtvLx9NsMsqH9f6wud1xEXYIW8oppjkLwImMCQk1LQ3QoOnKuAljbh-efdwXkOvu74oYzc5cYw6OJhhSDWTUGt3hip8KgNp0BKGMzCfWFYA_yarzQCL4SwByHnpMxyDV8xGNxAtunKdYd0rVBJ8hLEX3n2rEALDhkaS_HxHTwIGrhe4H20bUCPSqZUvoL5QnJg5p_2Alyx8WIw4zzASlMOdjh6szMbdwf8P6fFp1ZC79x-MLDj3INJU4MQpxdJk9m4tEF6SMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
هنر زیبا در ورزش جذاب هندبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104908" target="_blank">📅 15:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104907">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های شنیدنی نوید استادرحیمی درباره سهراب بختیاری‌زاده و‌ وضعیت‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104907" target="_blank">📅 14:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc259d7726.mp4?token=kOCh6yOR72DJjUBclZ-ffCGrB2a5Hdcmu3ECPJ0mdVnUt-g_fPKeKpzXawZjdrGopBR9RIfDiRMykv6wmJFjTGGr7qFwUW869_2Dhyn9AENF5ihjDF3wX_orgu1GVw_6ncMlf97F9xiR3yaVtPASVcAZ4SQnAaGt0cTD197R12LlZEy2wEzh6j06vkyr2J7Jkx3lmpnMTTBDIvv53lMwNnVspuHIRVAe7S49McoLhitQsYttbwxwp0RZiWUVWqEstmgUcjIaXG2O0TAVSlLK7E1hIfvHBDjfHjpsuPQ8JouKTZixGtCOIjswUG1SGRYlMoYZ_B0E4BW543QI4XK_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc259d7726.mp4?token=kOCh6yOR72DJjUBclZ-ffCGrB2a5Hdcmu3ECPJ0mdVnUt-g_fPKeKpzXawZjdrGopBR9RIfDiRMykv6wmJFjTGGr7qFwUW869_2Dhyn9AENF5ihjDF3wX_orgu1GVw_6ncMlf97F9xiR3yaVtPASVcAZ4SQnAaGt0cTD197R12LlZEy2wEzh6j06vkyr2J7Jkx3lmpnMTTBDIvv53lMwNnVspuHIRVAe7S49McoLhitQsYttbwxwp0RZiWUVWqEstmgUcjIaXG2O0TAVSlLK7E1hIfvHBDjfHjpsuPQ8JouKTZixGtCOIjswUG1SGRYlMoYZ_B0E4BW543QI4XK_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما فقط این هوادار کوچولو رو ببین
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104906" target="_blank">📅 14:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104905">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104905" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104904">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCNE8bTX53GTIkSIiWUQ0o83CWZSmNSv_kv4sdSp9apKBq0aCffdxuKGlmQEfxeIGApqlco1rZQWiF60NJ5G_ml3Ktn6u5mLhNYW7Fqgd9OUJdFKzIm1Sx7pfHb9yuYxW15iINaQ2dNvlutJ9EFAfKa_1tb7Xkl0fblVsoafnlG1-QmpD33wa9lrRZKb6hodP3EIgLhYMV6Fcz8A4f8d-07icXAth_pblK-b10xNY8cZPGYuMnWcESO9671w0T26nNulBmMslP1l63Om8i6T5Sy5cu6TuPfdPJIEVJx3H9NqTd8zKSJu3dYz2WISHf1WkA-GYuVITgYUhHwG0HKu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104904" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676a532a06.mp4?token=HNqoLbjd1I-NNRdLM4eplkRkvZWsXQS5NwHKIAkszMyOyC_2e9qfHXPMIpPOyXLetGsCpqqqxSZA6ZfPbqUTCxTcUAlUxyZAGb13uygDLd54y-dVMTKATsJrqlBgocs8fjXipz82HeKQ6U3pMkKa8ik4VwC7J6FBCIBEGuJsxi5RTI-6Xw6SvmBtQXh2wOjKOH-_9TvdszX_aexw1RhHQ71vE8TGFYs3LjewjZQZdu7SLakmXRTNKyoOPKOIMPF8JWL1TuAxq5PvLV8qOQXiPno7UME65Y6lkIzjTBK4U2AvBHnvyG5G5JqP1XJgUqGA44_9SQ8WN5VqYAcRUxXcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676a532a06.mp4?token=HNqoLbjd1I-NNRdLM4eplkRkvZWsXQS5NwHKIAkszMyOyC_2e9qfHXPMIpPOyXLetGsCpqqqxSZA6ZfPbqUTCxTcUAlUxyZAGb13uygDLd54y-dVMTKATsJrqlBgocs8fjXipz82HeKQ6U3pMkKa8ik4VwC7J6FBCIBEGuJsxi5RTI-6Xw6SvmBtQXh2wOjKOH-_9TvdszX_aexw1RhHQ71vE8TGFYs3LjewjZQZdu7SLakmXRTNKyoOPKOIMPF8JWL1TuAxq5PvLV8qOQXiPno7UME65Y6lkIzjTBK4U2AvBHnvyG5G5JqP1XJgUqGA44_9SQ8WN5VqYAcRUxXcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
پرورش نسل بعدی بانوان ملوانی
🤩
‌‌‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104901" target="_blank">📅 14:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f9954ef8.mp4?token=lqZwKUQ4C4whqbaM2HGaLa0vuPca7iOhhGeYcY9QOgac1TorOJFPhi2KSlzfJH46eCjG4cgBbwNUFZJ2-gsbjgrT03TD6IHFiJKDYV5zPCSu7CGaeCvo0tnN-vSNcxc-aQfvfgKUEqkfSSmypGsliQT8NKWzGS77GWXkbAT_F6SMbX1ixFQMWuMriIFdlfk0RKqCdvDPzwETZfwfo11qeJRiPqHJKB-yYM07iogk7rNKn2GA1q8Dv7A6-Xwwv6NySNuQsTdm2z3_sLs2V6SW3tHcOAqmn_LSF_LIVklJ4RFnvn5OWZaNTVs_jy2VJG6v2cnov4GVkTYN1gS1yMegbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f9954ef8.mp4?token=lqZwKUQ4C4whqbaM2HGaLa0vuPca7iOhhGeYcY9QOgac1TorOJFPhi2KSlzfJH46eCjG4cgBbwNUFZJ2-gsbjgrT03TD6IHFiJKDYV5zPCSu7CGaeCvo0tnN-vSNcxc-aQfvfgKUEqkfSSmypGsliQT8NKWzGS77GWXkbAT_F6SMbX1ixFQMWuMriIFdlfk0RKqCdvDPzwETZfwfo11qeJRiPqHJKB-yYM07iogk7rNKn2GA1q8Dv7A6-Xwwv6NySNuQsTdm2z3_sLs2V6SW3tHcOAqmn_LSF_LIVklJ4RFnvn5OWZaNTVs_jy2VJG6v2cnov4GVkTYN1gS1yMegbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
تحلیل جیمی کرگر و گری نویل در مورد شیوه مربیگری ژابی آلونسو و نحوه اخراجش از رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104900" target="_blank">📅 13:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQi-H9LEFqOZghtD8ItpMCxgZLKW9-NS8JJ4B66QtbzBd1JI28w16RpctuZAfYDbeXKb6ouo9DDHz73yXQTJHgUXye2ky5A_i3aHU__hN09xDtP-oQZ4ZbKVD7RtrsOL0_RIxWuBKKWj59YsqHRMzopn2rDcSynJUilUABnBypVZEablHeshNbfM1WeD4Qst_wn9kcxs_0CD0RepygcuEjCoH-GLlMbMcpvjIEh47cp1Ywu-b2msbUfjQeEKAw7LW-sxCmgvueaJyVoqKPIZw6GA_r8V09KSW9HBhRYuMYkixeA_m1fcRvOWbWf57QeYWljaJxqqqigjeXjfHS4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار هفته دوم لیگ‌فرانسه با خط خوردن دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104899" target="_blank">📅 13:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
🇪🇸
🗞
رومانو: آخرین پیام و شعار آلوارز به خیل‌مارین: یا بارسلونا یا هیچکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104898" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXrzFgb6VeADC1-abkFV9k1nQwZFTE-lQU78cUAsUm1shJVeM_aJvaOZH6VowfefUclBOS_fUMIHUs2iFFDTgCgnXcoK52XwKj77FgvT5V3-N24wySQW4vOfFW0puNt882BuGcr327dM6ln9CtJDx65ndcWIoZFA9gi3srLHAh1BKMwaix5rKayH8fG2gLJQOW7wJTPswoFpnQcpnf-_H9qx0E1W0o7lP8a6GIUuXKGTM4CZudcRW-s9v0atqsmQIEa2w4Hocd1xF4Celb8z9IpHkSYbeucdtWyhUoP-usIr08wk3YxA-cuU2NCDaONpTy0KPIaIeg-i8Bl45m1OZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
✅
رومانو: موراتا به لگانس HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104897" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b74cb03b6.mp4?token=gg_bU6GFhuwFYVNKZrp5_PJC4q-XFZdYwcS5FHkxrJxxFu1nykxvKHAuIc6aVUWb4gyjpbcl7DEZkzi1FkzPR-DjMu0l-gFKYAz3k22WoXSB7hqsYx4lR3wMn0cX7EqNIOUEhlQFMs-WhgP3RdALPsULFIXlC5sj53HI9tlfC8ZgvrYPrCz3orcd-6YlTB_dZN4_X-a5QeJXhLbVg2BPdsw-yqh9-ODiSpPFVXANpXwfudEq6FQmdSxp_I66YEB-MastQxnfmZUhX3nHc8kipu0mZvMDXbHWFZ_nFGHZUxCPeQ9uOmkWe7BSRsl-pb2-TFm9SA-Kc5FebEaojt8NlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b74cb03b6.mp4?token=gg_bU6GFhuwFYVNKZrp5_PJC4q-XFZdYwcS5FHkxrJxxFu1nykxvKHAuIc6aVUWb4gyjpbcl7DEZkzi1FkzPR-DjMu0l-gFKYAz3k22WoXSB7hqsYx4lR3wMn0cX7EqNIOUEhlQFMs-WhgP3RdALPsULFIXlC5sj53HI9tlfC8ZgvrYPrCz3orcd-6YlTB_dZN4_X-a5QeJXhLbVg2BPdsw-yqh9-ODiSpPFVXANpXwfudEq6FQmdSxp_I66YEB-MastQxnfmZUhX3nHc8kipu0mZvMDXbHWFZ_nFGHZUxCPeQ9uOmkWe7BSRsl-pb2-TFm9SA-Kc5FebEaojt8NlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
🇪🇸
ادین ترزیچ سرمربی بیلبائو:
🗣️
باید مراقب انتقادامون از لامین‌یامال باشیم. با بازیکنی طرف هستیم که سه هفته پیش کل بازی‌های جام‌جهانی رو تقریبا فیکس بازی کرد. پس توقع نداشته باشیم بعد گذشت این مدت کم بتونه هر بازی چنتا گل بزنه. باید به این بازیکن برای ریکاوری بیشتر فرصت داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104896" target="_blank">📅 13:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL1-Uvn3EcFYlK-LgYL4mo3p5gTqX5tTS8MSht1eo_HHrhbvopgde0-7Rx1jeBm0j3D0w4hEmHhoqxAVtrc2o93RyPTCOksfJ68dcaEdpo9mN0jiZxjRnISHno8t7K3adv_jG05d0pf-Tp2-qauBFxz4GH__sXyLf6rdDCFxnpnlFWTDyD9IBg8MD75R4GgkJTlHdrr6QLQ6__sIPFIxCjuA6xauO6cvU-y7uB0W90V7nOXHAqItpPHwn1CbCDIlplqojfaAbiMfyYxUrZEZKEDZVU_0xsSRY0PtcSgP-t1WISJOL5MbGZDDTtm1Tck4KC8kTxTAAJML2pq6KuOgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚬
🇪🇸
روزنامه COPE: آلوارز پرونده پزشکی با ذکر دلیل افسردگی به اتلتیکو ارائه کرده و تا هروقت که دلش بخواد میتونه سر تمرین حاضر نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104895" target="_blank">📅 13:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHUg-EU5vD-vAEURTFHIrlH_rXDcN5qfCFndguSRaWmSgoktQwCf_5AQHIxqW9eo0A0bYaU2W88uxrrPgdtq4Ww8ifb0FCgMZwYHvwe7XGEDSvFOUHdfuiVRZILHsICiGKTbag3yq133hNbhbKgdYkyIs8kuHoEqrjpwlY9d1fIiFLfHuA9nvyydMPnxcZHhGUGglxYTy0J27z3ilYO0nrGUnbbJUaXQLq9_AurfzH2JmAZdXRrseYOmbHbP06WxA7oRi884vQlUK4NHO8JbFICwwlwhb9vjlPHYzZSgxFId18OBzn_BRkAM3Jkn7kxPZhhdXXU4VWz9iHhPGpp3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
❌
خولیان‌آلوارز برای سومین‌روز متوالی در تمرینات اتلتیکومادرید حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104894" target="_blank">📅 12:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d697485bc.mp4?token=AqS95qMCIYjw2z7A_keBWcvzxQT_k1E79dIMRzh1X00niHb_uMcMN7dUKVR0OMwDSH7BWErcUiX2hY65Thrnrl8uJT6TWEjlJgsp_IFvANxikl5NtCRjRKTvJhQmFlkplDOFl9JPgqXkA6HxkLDIrOQWGnT62HOZ6AcExgTruqjrtH_vxPnRLs40UGFwGKsxg13a_2PObMTu7dDs0EGrWBVK24zUAm1r22qnpn4B9aZFn8qS81_-Kzr2jkBQOqPlF0k8wVdDFnCcjOz641yqDWP7TMJljNuR8COZdhu56TW9avPRDR_eMATqvRg59DTSDohzQdQaw64cPPyG1CWhTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d697485bc.mp4?token=AqS95qMCIYjw2z7A_keBWcvzxQT_k1E79dIMRzh1X00niHb_uMcMN7dUKVR0OMwDSH7BWErcUiX2hY65Thrnrl8uJT6TWEjlJgsp_IFvANxikl5NtCRjRKTvJhQmFlkplDOFl9JPgqXkA6HxkLDIrOQWGnT62HOZ6AcExgTruqjrtH_vxPnRLs40UGFwGKsxg13a_2PObMTu7dDs0EGrWBVK24zUAm1r22qnpn4B9aZFn8qS81_-Kzr2jkBQOqPlF0k8wVdDFnCcjOz641yqDWP7TMJljNuR8COZdhu56TW9avPRDR_eMATqvRg59DTSDohzQdQaw64cPPyG1CWhTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه ویدیو کاربردی ببینیم؛ با این روش حافظه پنهان و لاگ های قدیمی گوشی سامسونگ پاک و سرعت گوشی بهتر میشه، حتما بعد این کار گوشی رو ریستارت کنید. نام گزینه :
Delete dumpstate/logcat
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104893" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cca0ed089.mp4?token=aQ_h2xqz4_9gPodSykGDuNyJiZVHoOFPDxvtvH4hSUbTKna-iltfnvY61nYsd1SYpM1la74gDP51joiKXePBEofGF_dBe6CMWoLRXdmJgILoF8oleKzyDsAzgz-R6Wm9wFrRNGKSmw9ApVA_YGLvZtS3wh2uOICJA5XGYCPG-cNcSqRvqRvK25DXYCiS266wbAkPCwL6s5Fwt8Foe0Z36iuYlezOstVCtsn64zVGckW0cKJMs5YdpZYuDQiMlXB2d-kQopC5DSiYgZ5RGwvlOWMgJKCzH5DIG5eIeLkj39Jtmap2HMs80uYTrffvFyy37dHPpITFtXIau9fP7jaHmaiLwvQ4DMH1xlU9bNmF-UfcdLfB_jK-0h-l3VlwVp5OpgFvk95vP_A3t1b0v0U-r-bYQIdVBM0oEVZBG2AQjQafDyMptcAlSAx7nxOJT6e_D8JvTs5rSm2F9EhhL-6tZ6aY5yzwxST15YVu7KJw9fisOP2FLmGmgU4pSu4jPiGzMFp6bN_cflXo5k3BXpw3mbLr_DjP0Vp3ZWR61CT4CFhZ594KmwOeADAo2z5I5gG7CqPxhuEuFyMchYNZ7y_1x1K-bt4GY2TYEqS7tWxCR3EuMrhXBX3ETHIwo9DF2uxalTot_1oq7O4vDLukdoi8kiXF-GvEet7WsynIF34wHVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cca0ed089.mp4?token=aQ_h2xqz4_9gPodSykGDuNyJiZVHoOFPDxvtvH4hSUbTKna-iltfnvY61nYsd1SYpM1la74gDP51joiKXePBEofGF_dBe6CMWoLRXdmJgILoF8oleKzyDsAzgz-R6Wm9wFrRNGKSmw9ApVA_YGLvZtS3wh2uOICJA5XGYCPG-cNcSqRvqRvK25DXYCiS266wbAkPCwL6s5Fwt8Foe0Z36iuYlezOstVCtsn64zVGckW0cKJMs5YdpZYuDQiMlXB2d-kQopC5DSiYgZ5RGwvlOWMgJKCzH5DIG5eIeLkj39Jtmap2HMs80uYTrffvFyy37dHPpITFtXIau9fP7jaHmaiLwvQ4DMH1xlU9bNmF-UfcdLfB_jK-0h-l3VlwVp5OpgFvk95vP_A3t1b0v0U-r-bYQIdVBM0oEVZBG2AQjQafDyMptcAlSAx7nxOJT6e_D8JvTs5rSm2F9EhhL-6tZ6aY5yzwxST15YVu7KJw9fisOP2FLmGmgU4pSu4jPiGzMFp6bN_cflXo5k3BXpw3mbLr_DjP0Vp3ZWR61CT4CFhZ594KmwOeADAo2z5I5gG7CqPxhuEuFyMchYNZ7y_1x1K-bt4GY2TYEqS7tWxCR3EuMrhXBX3ETHIwo9DF2uxalTot_1oq7O4vDLukdoi8kiXF-GvEet7WsynIF34wHVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⏸
آنالیز فوتبال استقلالِ سهراب بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104892" target="_blank">📅 12:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTqx0lYO11NjwrY6ZjaxZkjAn8F9xDxclnqSXndTcqf7ywnjRPpIslji8GEZtlxScA5QxDhjjy9b8vMwC3pVE5zuOxqLkORhVT9zFBBLJNEulbW6-6Z9cy0O-IzS9x2pixLmmR8-nSPedtUkun5uHZtezUGWXazMlnwWxWVXV5e1Zb3eZ6JRZdPf0xl-rmL1n2R4_2lLPx6k4mIBqscKxqEfzI80G8kDvpaQ3_OX-6RNF2m6thP6OOMvK92utrjleySbLiFGD_EA8H4mIeGPBDRSRTAmhvIX2v3Gci06nVw8v1P21hf5P6x9ez_RAaOVirgDygGg2bMhYnKeTWVqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
بزرگترین بازی‌های دور گروهی مسابقات این‌فصل لیگ‌قهرمانان؛ سیوش کن بدردت میخوره
❤️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🆚
رئال‌مادرید
🇪🇸
🇪🇸
بارسلونا
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🆚
پاری‌سن‌ژرمن
🇫🇷
🇮🇹
اینتر
🆚
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
بارسلونا
🆚
پاری‌سن‌ژرمن
🇫🇷
🇩🇪
بایرن‌مونیخ
🆚
آرسنال
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
بایرن‌مونیخ
🆚
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🆚
بوروسیا دورتمند
🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104891" target="_blank">📅 11:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir2sBgs02QCyFO6XiVwiZcHyBM4Y7_rw_7nHBxterpyL_qS77xdFcHFuVBbJlJZfpA_gZFvcLTV-HtbcDoU5xVFEvaS75VTfcZ2Kxs28PlyefVbeBGrzstrPn_uMzGqYnNa6wC7AOCr10drVZMcKdHLe8y_ZaL7m9ibCL7hIU99DFRla1ly13e6Z6ZAeW486WQ2n-zk1TDXLxBhpQhtHNlp8xIC1jhgMOUsAdaA-4Ck3UBd8sFlxB0Jrx9WfI9L5rFOdr0J9J_d3ljAL_eRsRbd3Of1ytcvnSB_hNuXZ2knONPkPtkbgJVBHHn47yvmx_95vz3bKoxCXpXhPo1kafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
❌
خولیان‌آلوارز برای سومین‌روز متوالی در تمرینات اتلتیکومادرید حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104890" target="_blank">📅 11:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9611757770.mp4?token=RCVLRoMk8jeVvhqdRAZZvHU5bMZDQyxBaXDuo5SDmxSN5lk92LPgL2TkBHP0hOQsS49kOLD0YORUwTZJjg5TzICR6kWCu9EDlL3uee1kl5J6NDAFIl3lXQhEUS32fBGa6QR6-pIFMqw_3vrJoo5twsHW8dFbHzay0uMsbxWy0KvekEc7TBosS0CK1VeU1pAm_OqLe1V2-XA7ndjMP2nHwcE9c6sdmLg7YDlEV6zspNh_fEVDN1oBfhS8zTJmIFx9xSz-DoDZ8dN1R00iUmgBeh736f35Ie4-84eisZ_XthiRnMx2WZ7JHbxG4XeSR4WDDr5o_xdwLWbg7Olisg1iKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9611757770.mp4?token=RCVLRoMk8jeVvhqdRAZZvHU5bMZDQyxBaXDuo5SDmxSN5lk92LPgL2TkBHP0hOQsS49kOLD0YORUwTZJjg5TzICR6kWCu9EDlL3uee1kl5J6NDAFIl3lXQhEUS32fBGa6QR6-pIFMqw_3vrJoo5twsHW8dFbHzay0uMsbxWy0KvekEc7TBosS0CK1VeU1pAm_OqLe1V2-XA7ndjMP2nHwcE9c6sdmLg7YDlEV6zspNh_fEVDN1oBfhS8zTJmIFx9xSz-DoDZ8dN1R00iUmgBeh736f35Ie4-84eisZ_XthiRnMx2WZ7JHbxG4XeSR4WDDr5o_xdwLWbg7Olisg1iKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
❤️
سعید فتاحی مدیر سازمان فوتبال باشگاه استقلال: موافقت کردیم  سهمیه هواداران برای دربی رفت 50_50 باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104889" target="_blank">📅 11:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a80b61109.mp4?token=oGloFFKPnruG4Hwmc9oxvxWPw9lAhkEDr6CZf-trdZFa87j2IH_1nFBJp7Qgup8JCLJyofE2xcFQvw8TJlgxknBRZLj_Jydy8ypEwVJ5oo4e66f0i0CydFdAEUpnVf7OJLgubY3a1tPGemVZb578KaVPl_ChKSgvzfM9oxXeCfyY4NNWZdEYLVrQTt23k0ikRDW11xrMWrZag-DLj3GT95ShzXNr58J_A730v40SVSGCKRClwo0oXpAcTwq4EY7ojCspsT72iYXduoRX7qryMD7E0dW_519hxm_r15j2fzGOtbo7maJMvUUlPutRC-b7fijHeGfsKHxymhjqT7Ru0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a80b61109.mp4?token=oGloFFKPnruG4Hwmc9oxvxWPw9lAhkEDr6CZf-trdZFa87j2IH_1nFBJp7Qgup8JCLJyofE2xcFQvw8TJlgxknBRZLj_Jydy8ypEwVJ5oo4e66f0i0CydFdAEUpnVf7OJLgubY3a1tPGemVZb578KaVPl_ChKSgvzfM9oxXeCfyY4NNWZdEYLVrQTt23k0ikRDW11xrMWrZag-DLj3GT95ShzXNr58J_A730v40SVSGCKRClwo0oXpAcTwq4EY7ojCspsT72iYXduoRX7qryMD7E0dW_519hxm_r15j2fzGOtbo7maJMvUUlPutRC-b7fijHeGfsKHxymhjqT7Ru0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💙
سعید فتاحی مدیر سازمان فوتبال باشگاه استقلال: داریم برنامه ریزی می کنیم تا هوادارانمان را هم از خوزستان و هم از تهران برای بازی‌های استقلال به بصره  عراق ببریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104888" target="_blank">📅 11:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb886e60fe.mp4?token=UGA0sH-AlRNdkzcPFSpLLbrdkgn-ohZJPTA5yKtXhjYg4CsAS12L8G1edlfDCp4r0IIZe8g-Ds_vSyoeqi1O7MUVyC5w6O9kc7stKC5ZAO0kW--xdQNb1by79fFduLpNcvmQrsAiKh57RIzRyAcb8aSkltoz3lRnxVX6M594WK_YlFi5TqEDmlgG5SX95PisWUVJ5wDhc1JzYImHpM6igFNZShcPkLrL5F6dTeUIgIZJlXU0rct7fUBwBr1I656-coH2h2svh7_7DSMoyAQQp0DcbJwQkeiqafTDetzum6o1GJRoqonYWULdTVO8cXbSvtJipedH_mIm7SQZNc6MpoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb886e60fe.mp4?token=UGA0sH-AlRNdkzcPFSpLLbrdkgn-ohZJPTA5yKtXhjYg4CsAS12L8G1edlfDCp4r0IIZe8g-Ds_vSyoeqi1O7MUVyC5w6O9kc7stKC5ZAO0kW--xdQNb1by79fFduLpNcvmQrsAiKh57RIzRyAcb8aSkltoz3lRnxVX6M594WK_YlFi5TqEDmlgG5SX95PisWUVJ5wDhc1JzYImHpM6igFNZShcPkLrL5F6dTeUIgIZJlXU0rct7fUBwBr1I656-coH2h2svh7_7DSMoyAQQp0DcbJwQkeiqafTDetzum6o1GJRoqonYWULdTVO8cXbSvtJipedH_mIm7SQZNc6MpoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مروری بر برخی از گل‌بخودی‌های سمی لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104887" target="_blank">📅 11:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d3f8f817.mp4?token=sMm29lSKUu7SHD8nhY3WHgz_n0uaBjwYnY7r4q3ih7RLRYwXC4KMA-JKd12ZLlSudCD8RTwao2vgw3rSipleWD9isWCEMHLd6o4NPThp0-rJzUTJU47PAZqh73scP52EQRltVW2DbRnlmkr0EovXNxrzDAcJ5dHZAVeiLQl1k-CHGGLWAEIhpsechTHbBbMOvXBvkVYC8YY0TRd-xnVAw3JrA8_6OgBBSGG3W9naI-BbLMd0_2Zp2413gRIDvbTj9fwdXAQBo2WJUV-Q5UFUZia-4JU96IVcQ49z6hgBpV9gn4_Pw3_dVeGHxev3dCbSfBSQEDZq-SABsQAL7HiZfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d3f8f817.mp4?token=sMm29lSKUu7SHD8nhY3WHgz_n0uaBjwYnY7r4q3ih7RLRYwXC4KMA-JKd12ZLlSudCD8RTwao2vgw3rSipleWD9isWCEMHLd6o4NPThp0-rJzUTJU47PAZqh73scP52EQRltVW2DbRnlmkr0EovXNxrzDAcJ5dHZAVeiLQl1k-CHGGLWAEIhpsechTHbBbMOvXBvkVYC8YY0TRd-xnVAw3JrA8_6OgBBSGG3W9naI-BbLMd0_2Zp2413gRIDvbTj9fwdXAQBo2WJUV-Q5UFUZia-4JU96IVcQ49z6hgBpV9gn4_Pw3_dVeGHxev3dCbSfBSQEDZq-SABsQAL7HiZfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت روزهای پایانی نقل‌وانتقالات خولیان آلوارز و اتلتیکومادرید ببینیم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104886" target="_blank">📅 10:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSOMQExkkzgxFFRQ9Bf-6_FvXIYEYTuYUZr8B2R-rDiAxAHmKWeF7AvOdk28MwgAzS_z8d-zt18bDgC9iDI45CQ65aLmsIh_XoGXgY2dEAerjsadLIn0egemK6I7msKx6w_nefREoBI_3i1fbgQBGvwAD0Kgftl1w3OKHvENe1D4qKHTjSxOIOf9IT4OerqQXoREH4UkAQ78PC579ndLgP0eH5dGHAhI1_eFmkgYKQIWk7dCO18HH_dL-t6MLoJS2iuWFHBQLsaQUPIRROoaBlFdhCHoY9zVcsVSmbdkuzHEiSvTx--m-WFwMpsrRH8JWrSMQ3tORX0WhFzzWY41OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇮🇷
میانگین‌سنی تیم‌های لیگ‌برتر ایران؛ پرسپولیس با جوانگرایی تارتار در جایگاه دوازدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104885" target="_blank">📅 10:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/347df9f824.mp4?token=dAKZNBolOeqaSpv9Zz-tbrwJqtdgvW3nKQnHJsew-_YqIG7GDHlBeX6tIrMot0Gj5fT99_zC4TBb_p5NSOv_WD-EXX8EKKNuNb2yg6i3kotYcodVzViTLOzCSVUr_qU0OKoVAvgzy4XKsP9NlX3R3cWoJv3tB0L7G-AmsipP71jFEYnAPlYsRF6o-_EOoSy45-vOnHkOnNQ7pAf1_9cUlzqxoOQn3P9R5rtyETwV8XopSsKlnp7al3W8BDQCGw4AiuOpNYF5psl7uA6JwUTVlh2-_l5laNmakLt5wOEs4x53NIcuDNLNN_eAE81PhTaynmUxvb3ru94iF6JjJa5S2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/347df9f824.mp4?token=dAKZNBolOeqaSpv9Zz-tbrwJqtdgvW3nKQnHJsew-_YqIG7GDHlBeX6tIrMot0Gj5fT99_zC4TBb_p5NSOv_WD-EXX8EKKNuNb2yg6i3kotYcodVzViTLOzCSVUr_qU0OKoVAvgzy4XKsP9NlX3R3cWoJv3tB0L7G-AmsipP71jFEYnAPlYsRF6o-_EOoSy45-vOnHkOnNQ7pAf1_9cUlzqxoOQn3P9R5rtyETwV8XopSsKlnp7al3W8BDQCGw4AiuOpNYF5psl7uA6JwUTVlh2-_l5laNmakLt5wOEs4x53NIcuDNLNN_eAE81PhTaynmUxvb3ru94iF6JjJa5S2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏸
باشگاه استقلال با انتشار این ویدیو نوشت:
❗️
خوزستان همیشه آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104884" target="_blank">📅 10:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8d86050b.mp4?token=ie4txEakY9cLbYGLHTyA7sMoq2Bx7WL1siSj6s5pPU0mXMzHLSSZC55asRLAkJ_jTaanvtQK4ddpAaf2s8CmHRaW0uzimVu5dyw-6B80Qi6rIIEywrWPe2pxymwa2CaJV1kJrRkgntJY07GvCzVwPXjvzV1Ov3NzhW1b5MsMyCfX8eRhSab5sczvJz-6w1wK-tOTGPdtjanZIc8d9hZeYEhVPkc48d8YwgKw450mjdbqgP9xb16jZCwg8cEM_YJ2d2I2vCQOYgHNAUGABdeVc-9FwRsQ5ncwrMamw77aeMdBINULe1F_hXUSUDrOw5IrM5uPrY4-fW2XCkcqkAbzcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8d86050b.mp4?token=ie4txEakY9cLbYGLHTyA7sMoq2Bx7WL1siSj6s5pPU0mXMzHLSSZC55asRLAkJ_jTaanvtQK4ddpAaf2s8CmHRaW0uzimVu5dyw-6B80Qi6rIIEywrWPe2pxymwa2CaJV1kJrRkgntJY07GvCzVwPXjvzV1Ov3NzhW1b5MsMyCfX8eRhSab5sczvJz-6w1wK-tOTGPdtjanZIc8d9hZeYEhVPkc48d8YwgKw450mjdbqgP9xb16jZCwg8cEM_YJ2d2I2vCQOYgHNAUGABdeVc-9FwRsQ5ncwrMamw77aeMdBINULe1F_hXUSUDrOw5IrM5uPrY4-fW2XCkcqkAbzcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🎙
واکنش تند مدیرعامل گهرزمین پس از بازی دیروز با گیتی‌پسند: به قول حاج صفی یک جام بدهید به تیمی که دوست دارید!
❌
صحبت‌های حاج‌صفی مربوط به دوران حضورش در تراکتور و بازی مقابل پرسپولیس بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104883" target="_blank">📅 09:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c607f6634.mp4?token=BWDfKQ0-Ca74q6lqDszOqhMx9T4HZnYLQCDjcHsFoLnOMLzfbROWpqIT35UpHN43qFOPN8DHvr4DZyM9LK3AL0JbW45NeulbJ4xruEsjnpmYetJfclaNN8rFxDu4evYEjrLLG5mNvmByzPix8nwoAneCGphT-XDi94CA7QvpORAsqkBKUnceoaBwdz7f3J9Rkf0w4rw3aNR5d4cMTatGBB_bH3Zvu0CIg4TYghx2OzJSslFitq7XqsIfv-N4hJ15-lX6bN1-kfye-n-9BfLJJddvItz_lkhHVaG4oiLpCYo0lC1-6Nwbt29Gcm0tuqofCpik30ixLzjlQPpJ-9XXrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c607f6634.mp4?token=BWDfKQ0-Ca74q6lqDszOqhMx9T4HZnYLQCDjcHsFoLnOMLzfbROWpqIT35UpHN43qFOPN8DHvr4DZyM9LK3AL0JbW45NeulbJ4xruEsjnpmYetJfclaNN8rFxDu4evYEjrLLG5mNvmByzPix8nwoAneCGphT-XDi94CA7QvpORAsqkBKUnceoaBwdz7f3J9Rkf0w4rw3aNR5d4cMTatGBB_bH3Zvu0CIg4TYghx2OzJSslFitq7XqsIfv-N4hJ15-lX6bN1-kfye-n-9BfLJJddvItz_lkhHVaG4oiLpCYo0lC1-6Nwbt29Gcm0tuqofCpik30ixLzjlQPpJ-9XXrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رضا قیطاسی
✔️
رستم‌دستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104882" target="_blank">📅 09:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8FdI9KQE-QFsBkkuYZqHbW3VqgNhvh7u5V60tBVFJeq7h77sEZvocg4m7qWeZAW-C_aTwoy1UXSN5jOj59GvE5kWaOVBFItvbnLiabwWlX9cmzrHKQxENQYc98gBM_IY0yoZTXfjbYXxmmJwQC4L5FMlJXdZv_12Oy1TJjLqvJUG5OBHcvqheJhwropnlG0c1p5NKV9VcIvQuFNvrp_QQdULYja4P6MaPY1Ao-ir4qxnukAxzmsOhOd8O_LH3XQjvp-np7LVVxLr2sUDJJXSzwgG847FMscl9WHCesUBwme8mOqFztgRNK-VqZum0FJOaSusF7xPTnS0XIoGKUdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ 9 سال پیش در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
📊
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104881" target="_blank">📅 08:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2d8d92ff.mp4?token=qffIp9GOiNV2Jonj81Q8nLwa6FqNUqlQoKdLoTfOkq9q38xLwQK8GViAuXPRW5FwHb6FYJeNH2z8AHrusvINCfWDafwfR-uzSe2xNOLIKYXR39xqw0ltal6o4qznm91RqDpgByaVzFnOuhIphLwslSRqTu3gMHI-rNUmBPj6g-C-QrvjrskbDA8NIsohVM3wjQJeTXpapa5fy-Pc4e_aCJwYsEz1ekkP_1DOTcknE-zzCLm9QQUH2Mq9Ln3lCKoL0fFYae0uIHNeVWNuM_rpTK26-3x1iddSGAMQHY2zyqm7dJ51tIje0XUAHxkfgTv18hfZ7f4gz9si51Mrj_6xEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2d8d92ff.mp4?token=qffIp9GOiNV2Jonj81Q8nLwa6FqNUqlQoKdLoTfOkq9q38xLwQK8GViAuXPRW5FwHb6FYJeNH2z8AHrusvINCfWDafwfR-uzSe2xNOLIKYXR39xqw0ltal6o4qznm91RqDpgByaVzFnOuhIphLwslSRqTu3gMHI-rNUmBPj6g-C-QrvjrskbDA8NIsohVM3wjQJeTXpapa5fy-Pc4e_aCJwYsEz1ekkP_1DOTcknE-zzCLm9QQUH2Mq9Ln3lCKoL0fFYae0uIHNeVWNuM_rpTK26-3x1iddSGAMQHY2zyqm7dJ51tIje0XUAHxkfgTv18hfZ7f4gz9si51Mrj_6xEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇿
شادی‌بازیکنان صباح آذربایجان از تقابل با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104880" target="_blank">📅 08:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IveRPsFXUh78tgd1ryM8vNxFqpvNXkiJm__25Cah5t0zd9lUEcH1fqz55Lq3mZIcZYcmrG0vszQPaJF200_KHfdhpn36PkgcpNaWTpz0xTJO-KnaHhG8PVRAc8qgWskhlIrpPII6CLEbtltiMSYKxsF5i54YBIVpmUAWU_7yg2mWmLs2zL803M4gPANOhWFycKwSc-RZMbjWbNmj1HO9GcUJLbq0W-_23llO_-22bmDBdgVKuPgt4FC7jeY4zil9U5lpXgNbMyeimVagz4v_PQacjYuBiYc0FWK1ocxeP3rrAEFgx0TX9YAKs7rWKpScn-HY_kqDmhOuV2clwwLHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دی‌مارزیو: منچسترسیتی تماس‌های اولیه خودشو با لیورپول برای جذب مک‌آلیستر آغاز کرده! سیتی قصد داره به صورت همزمان طی روزهای آینده با مک‌آلیستر، انزو فرناندز و کودی‌گاکپو قرارداد ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104879" target="_blank">📅 02:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
🇮🇷
دختر استقلالی: کوشکی امروز ۴ گل میزنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104878" target="_blank">📅 02:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UcRXu2ot9IDGYLO_Hj1N7Dmyt8HbrDaWfSxtLRqnE-dnflL6Ju_dmGCCDGYZSR5oGPu5mX9nUh_gq-cBpezIq58ZSQceUAhLtD-sQnjXvMnt_c4vVof00t6wkQfctDJUw2PtkUwoMKaLbFhBf97MED3HyECPOcrwjnojyLoBQIRlwOwagX84mvzJsxMpmwijbzEtUXjKAUYYLtcgvhqMI1g5eFw5NdZ6DwhKSwVSjx8rT8jq4SiDyP69prcoBvrabyxPIJ7wviTZIxGz6gpYd1xI2VjQ7DL17CB8XLuZ_3UyGOVBNV4MmYhslQKii9wVHMj3nQgtG3WTRrvr68q-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehkn-TuqtslZXlsEHW_PuWNsDT6ZsY9X_ErFi4zBvDCmhUU4YBBcxZfWXVsKsR7PHw-RdM2STx5cUuCMM7iKflN11fBRpIVlAxLw7Maf1lEM1jUVGqXYcfutYoF63PewdGCJfrqGPZlctxI2-T71K-6ZUi7Xdhr1msQAKn9uHubrlWJj54wltLB5rhzfOho3hH8Ir-ix4vEiFmRNvbYoFmIrKOUbUKlT98oiVq1AN1jQ6BLh7KZBiFCTV4VvEW8yi4Bpvmo6HpeITw3-fc7RZ08WIN37QFAEpKl2kQaMh_PvkUg_AdU6xUifIw30NaCSnuMt2vKUeNML9Fqme1JflA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
🇪🇺
🇪🇺
مشخص شدن تمام 36 تیم در هر دو رقابت لیگ اروپا و لیگ کنفرانس
؛ قرعه‌کشی ساعت ۱۴:۳۰ امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104876" target="_blank">📅 01:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ad7bc72b.mp4?token=MjPfQqBjvqcgbi63KBNOm0L1p2eBjB2v4vPvKLJ_VwG97OLQ0GbEsuosUZ1llhfmhgLVlJGLRlEXelR2ckQJ0RDy-3VMtfJ6-eRax13wbPg5qNzpO4Cxw8jGvdSEoD-62Sj0QbptsZ52rSNJu1T3C_GRUB_5kEGYCG0VdA9dQkJyV4UQtRY5eLZ9BHepzQYKnF2YHEdkWeXTavMKkPKmLOhm1upMSbkWrmepgR3CJ8SwPfLMe1wBJUnDoYCGuviNOAeW0_BJveOQuyaY4rw3LigPVbDdfgW-jrXkb2WJKq3BYzea5NVkTgzjk6zc4AuuUu38I9dkpJOIBI3FcNBwN1o_4icSF5jpKremhA9U-0si0NqfAlvaZF86hhW9K7hdI3BQfYpcmfZDrMm7ES5Bf2QWoMB8GKlc8lgYg4f3N9MuEqeDVmWfD4LpGZfoLIqVTgS25Es3OPsS399QYqBu3_MJ6aXda9UQXNXDvzrBdF-lIObn3SYiuqeAoKLU-lA-6TzMDJsmyAksJUWVzyPUw99StbPNOSQ2_Cvfo60PMNYtyt-H3WbAld54IqClxxRjcJHacMNLJ8rYgUEp47A66EBihBfWf_E86mpWZrLG3nY0glTM0ECDrGubDyNzmfslZPGfVmw21RBxasAHa3z8IOyg3qGHzMpdnxgE3xzNw2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ad7bc72b.mp4?token=MjPfQqBjvqcgbi63KBNOm0L1p2eBjB2v4vPvKLJ_VwG97OLQ0GbEsuosUZ1llhfmhgLVlJGLRlEXelR2ckQJ0RDy-3VMtfJ6-eRax13wbPg5qNzpO4Cxw8jGvdSEoD-62Sj0QbptsZ52rSNJu1T3C_GRUB_5kEGYCG0VdA9dQkJyV4UQtRY5eLZ9BHepzQYKnF2YHEdkWeXTavMKkPKmLOhm1upMSbkWrmepgR3CJ8SwPfLMe1wBJUnDoYCGuviNOAeW0_BJveOQuyaY4rw3LigPVbDdfgW-jrXkb2WJKq3BYzea5NVkTgzjk6zc4AuuUu38I9dkpJOIBI3FcNBwN1o_4icSF5jpKremhA9U-0si0NqfAlvaZF86hhW9K7hdI3BQfYpcmfZDrMm7ES5Bf2QWoMB8GKlc8lgYg4f3N9MuEqeDVmWfD4LpGZfoLIqVTgS25Es3OPsS399QYqBu3_MJ6aXda9UQXNXDvzrBdF-lIObn3SYiuqeAoKLU-lA-6TzMDJsmyAksJUWVzyPUw99StbPNOSQ2_Cvfo60PMNYtyt-H3WbAld54IqClxxRjcJHacMNLJ8rYgUEp47A66EBihBfWf_E86mpWZrLG3nY0glTM0ECDrGubDyNzmfslZPGfVmw21RBxasAHa3z8IOyg3qGHzMpdnxgE3xzNw2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇳🇵
‼️
⚠️
جان جدت دلشو نداری اصلا نبین؛ وضعیت فاجعه‌بار نپال پس از سیل دیروز!!
🦾
🦾
🦾
🦾
🦾
🦾
🦾
🦾
🦾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104875" target="_blank">📅 01:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbpa7Z9szcR76GWVXyEYT0oedDWPG78NbRZ7TDsLmo1VOTxRCO1rPOivmoja3FtpIGKd1SfSj-CzZT_vwp-7xYRTywpMCyMSuBHK1C51rqzwWNFUK0mZJIMplR5Xrg5GKXCQBizSByKSQGQqopv7scnHfQYmq_OeBfKC35zwU3oCaKSKo6nPZgPe-ZESYbsXMWkk6umjUo5dxuMW7DnRWXgN_AKc-cq-zP-WjbW0b1FDpzsjkaH1-YsyZLujHSmfFyjXIuBFQGDgrT8ZMvLhB3rnRQNL2x_G0rMJLQIs024MxFNsa7dhGBcDlZGyXlVYDx_NCO7cG_rTzloHjSVlcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منبع خبری indykaila، مربوط به لیورپول که اعتبارش زیاد نیست البته:
آرنولد به لیورپول باز خواهد گشت، اما فقط در صورتی که لیورپول بتواند طی روزهای آینده با رئال مادرید به توافق قرضی برسد
🤍
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104874" target="_blank">📅 01:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEDIEBcBqmlTZsEtDPkMnEzn8vLb1nofntXyYdgZykUPm71PDDPyjoB6Z4t1ubjxVkjNzmuacPYuRJIonekVqnQLchp8JOqtJE-cqeiRoidr96PqSGEyEPC28mrf9cwQgJbJ46HM0bAHgk3WQb_eoaBsLm0UB1Qrbu4WBDXvJMQNfFvX0woMGQZ2TIggZSWGMPLAIi3A_WZPhVDAn-C_FrfoLIce6tObks4gAv9JvSCISbeut8BlEX7kRZy0Wn4qonx4hT2Uv4r2apHB5C_LUl__K3zDcpdCn_xq4WniFBGkyIvTAnepDKO57qj76255ggqp-WQgvyqzAE3abFl5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7yGq2HhZgGqZHfkf1kR4KzmThAnxYqQCV_VvREzEq4TI27xMRM3ckvtyJKog0VSm_HFhGgxkkJN2zGdSfOfK-AzEe07N2XWaLxjcRue5T9sLT9wOZCOzUSHTt-sLeLymhAHnH_MA7pUb3of_v9pVaxJjgtsg8DbBwLLSVzPS5LyEUwFlLeQGT97jjKJPtFWXK9-3Yu7hNgFy9tFZsOhMAT4lk6E4jLUg_f5X0njd02Xyh0hq4_0CVFU4yxrGptrVLOF-L-kg2znopVT5NMypLQHBbRDvb_Qpsl9mJQdipNqWfXTiuhCgJj5HGepgTBNlELlvYkZBnfJxHEH66p_Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🤩
💔
🇪🇸
آرشیو‌وار: ژاوی‌اسپارت در بازی امشب باید دو کارت زرد می‌گرفت و از بازی اخراج میشد اما داور باهاش مماشات کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104872" target="_blank">📅 01:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAvk7X8i647Rx1fjLJw5C5jl0FBHUnrdtRdNUqothWotmtwR4Ise79egmeRs3k-wB_fLvmhRDTTGaIg3OavvDO85ZoUTgdbHOiAFqgCerFClaePc94jxO22P9eEGhyvX7vViEj6jo6KtWf8ICFLvh2Qq2vCZu4FpZ5-0lwni78lnlwEOejl9cnLOD1zZOrHSxKfCrrSf-QV6SWuLXcBTVDX9Ldl_ntecnx7iL1k7XfrJiTBhDvUw1AtYX6YRqSSMzFnfQeAReJiFj909XYn415AXfD9jZlLEFLhXwIBTUOjOCpwzdu_PSuT8s17JG4_eUohJ3KX8azQy4XckDH-6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
محسن نامجو از نوازندگان و‌ خوانندگان ایرانی پس از دو دهه دوری با استقبال مقامات امنیتی به ایران برگشت. نامجو اخیرا به سلطنت‌طلبان انتقاد کرده بود
📲
پ‌ن: توییت چهار سال قبل این بزرگوار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104871" target="_blank">📅 01:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104870" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKpkjfNK7e6WG1CTvjHwXDsIq2X43ePdMlbmf70ULyzz_-KTThhaVxE5XtZEIT25E3foZroASvtStTxG0mFQRncPfKIM0dAFIq7vCUy0alBp8u8fdr15UMyhBKrz3x-qZ4aZaEdYMcrvhdAqfdeVRfezIRdQ9wicni31Gor7zEzD39kFmFfBcHg1trgAyj1Ob76D8ci816oE2Loiq6pmg4SiBTjgaxUxh69HLr9k-4qng8_eLNO67baluJ77x8jZb_Yxo-8HLmvV_-gvMidO3ftNFdiuXMTNiQGVB8Hp6pnbTMUessUb7FpCK67Gm5v-UwyZPMrFqoBRYqq-goiMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180
؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب خود را به کادرفنی تیم‌امید معرفی کنند. از طرفی فدراسیون فوتبال به استقلال هشدار داده که هرگونه عدم همکاری باعث محرومیت هر سه بازیکن از مسابقات لیگ‌برتر شده و هیچگونه بخششی در کار نیست
🔵
آبی‌ها در نامه‌ارسالی به فدراسیون دلیل عدم همکاری را کمبود بازیکن در هفته‌های پیش رو عنوان کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104869" target="_blank">📅 00:50 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
