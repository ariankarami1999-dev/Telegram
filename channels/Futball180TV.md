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
<img src="https://cdn5.telesco.pe/file/Yaaioy3-UDqBCk7s4tO3E9ewiMdgWfCc9iQxWU9z7MHKIUiN-AVimL0JU4zJQqxw2yzYACJUeucjostgr_PkYt-zmzoJxbP9pIDFtVtNp7Dotzl4TiCCbaxpY_HSEKfbeB7zu0WO5u0DKTZGc9tD65EWBXepATbPcvtMmIjAsYPolVHa0eCn7XH_DyxPkl_UAgwEHRU1JlKD9GGOLqUTYYF3qgUBoSKIHGVUEVkv0cbX_Db6TF7UanQEN46O6haNaAbteKs5AOjA9sU7deAehfR4LJNvZSehtvGRfXo8QMKXEbRQoA6DxkjCrJWhPuPbSZVlVR0VBQT-lEaUlZqxXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 422K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-105900">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=MvUDdQTMXDqDj7L-3QacNkMTmrh_SHuTA94PcLlmOXUxkLNbFEG8I580MDYJGhaNgPa4vs7B-ca_S398IaRX0QdYY-A6v80MTQUdDNSB2wCXN4LmfudOIN6F_mIxZWUT8KZ_OLHfA_qf_Ga1GvUKA13FhG5GyfGBfXUxB0_J2654Mf03MICi5bNqnHSeMF9YD6EWNOWdy0D9zvzvhPSIoiMYjHhX25iUg464CMxfxUzFz7PZ3r7ZdL958_77xYtyEiCWrRah9DQHom30fWxrbBSXF-u1FbLwUoNZS9PXqnXBpGQRbG_4NmwDurJZXytKJ3sLo08QfD13y4mhLzigQ2-ei9KpfBMtSUmFUjXV3zOg04mYgYUuNncud6pAsK5U9rD8NGiGDmjzB3x-6M4m0zb9wU_APmGXyEu6_yZkJ5k94sOnF3ley4e0mP6wgBvuxtG5G_-lkb92He1rYllSmsQZF_7jS9KpcR1JwoGC-p8LRkzDGV9qLkyOej00XJW_zEZmB7y_0ndHODT7hK0MsIixSX99opUR3XOCxFMKOcB0V782HQw7KDuT0mYE73PmGhlPZ9QgjAAvyiPO7E_XkPMjTWT4mSwF24Hd0eadUA_X1i8WNLwdSd_UeU6v9CBW2VP1JC4HUqsQ7j3mguK7opOWLMr7cMIz_m-DKBFMaOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=MvUDdQTMXDqDj7L-3QacNkMTmrh_SHuTA94PcLlmOXUxkLNbFEG8I580MDYJGhaNgPa4vs7B-ca_S398IaRX0QdYY-A6v80MTQUdDNSB2wCXN4LmfudOIN6F_mIxZWUT8KZ_OLHfA_qf_Ga1GvUKA13FhG5GyfGBfXUxB0_J2654Mf03MICi5bNqnHSeMF9YD6EWNOWdy0D9zvzvhPSIoiMYjHhX25iUg464CMxfxUzFz7PZ3r7ZdL958_77xYtyEiCWrRah9DQHom30fWxrbBSXF-u1FbLwUoNZS9PXqnXBpGQRbG_4NmwDurJZXytKJ3sLo08QfD13y4mhLzigQ2-ei9KpfBMtSUmFUjXV3zOg04mYgYUuNncud6pAsK5U9rD8NGiGDmjzB3x-6M4m0zb9wU_APmGXyEu6_yZkJ5k94sOnF3ley4e0mP6wgBvuxtG5G_-lkb92He1rYllSmsQZF_7jS9KpcR1JwoGC-p8LRkzDGV9qLkyOej00XJW_zEZmB7y_0ndHODT7hK0MsIixSX99opUR3XOCxFMKOcB0V782HQw7KDuT0mYE73PmGhlPZ9QgjAAvyiPO7E_XkPMjTWT4mSwF24Hd0eadUA_X1i8WNLwdSd_UeU6v9CBW2VP1JC4HUqsQ7j3mguK7opOWLMr7cMIz_m-DKBFMaOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: خلیفه و گودرزی از نیم فصل بازیکن استقلال هستند. بحث انتقال خلیفه و گودرزی از آلومینیوم با مدیریت باشگاه آلومینیوم توافق شده است. این دو بازیکن از نیم فصل بازیکن استقلال هستند و حتی واریزی هم انجام شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/105900" target="_blank">📅 21:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105899">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwfoDyVNySRetp3Pm-OQ4xxrvmpHntW8o8zuRdW3UgySDiIZuhsC-2AGro6sGqYWrdlnq1aMEv3kgrrBlR8-gs3o3FkALuAR0fA269MtqCWt7MnNfPSnNCTGsay_S80OSmN4QRCfh6YKDUmO_x1xeWPKycWrPR9G9ZNMbG_LUJ2HcC4hbkXVzo5cxeVhWWtawYLefc3kavNLVvWLQRfBJxQ9CocqJzA5W1E_OybMOQ3Tqh95MQ1x1O91ditthiO6sh3iYFp_2tmYDCz1pGtkT2EmAvooC8lgSkLnPbS9UVgrIq5z6d-ruSQYQSq8_1Q-KlkPrshLh2RstJgDWBJr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇵🇹
ترکیب منچسترسیتی و پورتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/105899" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105898">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5hYn6ZK9mcKd2BVFwW2HhI7_ATCskDa_Mmi5WqK87BQiRVzJG5KiOZd_ePB5lG_df93HHKQAD2mjX7qtd-VwAjtVIJ2B7G8OKZj537HHxe3OQDMOH4mjv2EIjrrWgXNtVSfStwErTc5dK2I-XbDkYxDQGKiK_3VJJzvuC7n6sL3SMQujyNIKDJUgbKnasmghrGcyrC3DktuQxjmsR2x_F8wUh1Wrg_ezW0BSSAKxNHJWDEYxouhRxcSYd0sbO5jJR6Ke5jYvbGxDGtL7R0-2GLrx9f8JDD2GCC_ul91o4gBZxTb02wkPvUqbj62JGj9TMjQ6eCveMEaJm1NJV8F_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/105898" target="_blank">📅 21:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105897">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiYPz4_77N4FBzE3yF9ndxmOVfROv9dR2r9cUJrJHKej0lRnlE2VtiLiD0RLi0iyiyirVY96JIVKdmRjYzH6ZjXwzplcWcbs6aNrCcmkxpSH9qXtnJMAKvNIc-SoyjalEiVSh8LRxvVLHKMXLxKIGTU8CeaIDRMMlsfmR7gJppHh6QvYul1zQlUvkj7LsnWMx-2GuRpOqA5HSvShWT60N6cOTWEwukY47dtIIFPpM_OU7WUnvs8EVpPsWnMoqlxLtNMpVvjRM4eR8jswG_by7XDaMEIB0_-zUedr5cE8-f35X-DiKAynGqpzDaiU0wP-UBBS0qkF-Sz1lJ4BHYpLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/105897" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105896">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy0hZ5_wcRyasZlfeCAHveS0NOBfnYOdPtanlxiImVK1-3qOhrEsCVShdmaEBSThcNeTevHg4PRZnHkH9gu9Pz1UgmnqSCzx3J5uil_GnDh1CeE1dOwkcxf4lhRALSl0dYBl0JsBSyvW3WxfzzVrYFqNyps_qsCUwRS0rKpQ8CfAwmMhgai58dJ8-0fH3vky4aXur6FHJtVhDBVwrRkBMra7IJ3JVQzXCU9KTCpmxflx7_aZjb5g1C8EXhzKWRrRgmEtDQ2sF0muW20j8hRjLbeSS3bjdd9zD6awBss2DWnsTyMb2BjYniJ9Le_aEcJu6au7YvIIDi41fYeUTNpxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/105896" target="_blank">📅 21:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105895">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-KHLnyIxhRmDbvSWdbKkJcitLJSkN-cfT4sSniXNtU9Xsc7mH7dCrHJU8N4czBrTmFmNwHpnVKi_FHdHMxU2uxlbv9z04rix50kEeAWq_mVBWMFM-irnpneHhAmIKzOCJKmjFfPhwc37C0SxMiyaQre8KavHfqPOUzdNXrxM5h_tJCqTq2x-P_PRdHnG7aAiEsP_eoCjs53NsB5fFuucjsJbN2piaZlZOfAqTG9Zi-ij3hluBTo26YVD_PmaeuJeXhWgpoxusV4eqaTE1fl-ScV1PYkTaqnbCHQTXRmNJ9R9M4mxMcnrtOIbfXWnwG7UBqmGHSWQfdQUMxr584rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
رئال سقف برنابئو رو برای خیس کردن اینتر بسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/105895" target="_blank">📅 21:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105894">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBxD-sJOne6wJJF3odaGyXxL6YDsyst8rG_YHcR73ZY3FuTliiiE4dRk3M9dnbqfJdzAT9n-NhcoJatFakoGMvCf0gKNceFeTXxwh39WUwl_Tp9PNsCBPx0J_eDWoNmxexBUxUVRnbS7otK00usBW0stWYPiWH82lw9hMvjCpXoMelMd0WukyZxpVKafeDr-1InL465layeFh3UYtbdQK09qEvHsWHMf5cZ3pv_LdmLgbeAg8OvcaNkIrNdAfekGvSnE-zaDMPwrI1dJzbr1JoH15J877TajE4yqBIiMKF3KQkVFVov9_n4HQP961cPQ1SBleyMY0G8BMJtzkU7pTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇺
دیگو سیمئونه: خولیان آلوارز جایی در ترکیب فرداشب تیمم مقابل لیورپول نداره و باید از روی نیمکت بازی رو ببینه تا شرایط روحی و روانی درستی دست پیدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/105894" target="_blank">📅 21:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105893">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d57gWs3hVp4Tufsa8rcO9TbwLFEiJ28SMjNJeLH10a3MKde5Dv5pvStJvgFZXR-wQcpaHqDIXceArVhlpVK8fLlL351cdTebwVrQUNsEyfE7z6F_HO55mvvtoco9l4jeUmMB5M7mfsGMVpZiWmwEUcZCACh0HMwn0JX2llK3ti-4mGHW4vYy3F-iTqf5Wu131cHP1vdkzP_RrjXwMSahUnZeOWPXWPSmdtQRBuKZ-UUAR3lXx12SMYt8bA8zA_Ubh06mYAIXU_P_nrSMZ3dGURBlejMkcSgiM83TkvA_n9_xvDkZcifWg-I3Tmi-zD-YgilDU1WCoLw7Xl-uxKJt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار سال ۲۰۲۶ با باشگاه و تیم ملی:
🇧🇷
رافینیا:
بازی: ۴۰
گل: ۲۱
پاس گل: ۸
❌
نامزد توپ طلا نشد
❗️
سادیو مانه:
بازی: ۵۵
گل: ۲۴
پاس گل: ۱۳
✅
نامزد توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/105893" target="_blank">📅 21:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105892">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=XRTUUj0T-r8MuqifYvRsccdrjhK6LUou9lD67Ew_icGbBTJZNNQkz-SZjcL9fooIT-aWUP4gm1CbyUR2K5p55Jjs5eZZgd8MnkCn-vH6oSGAXzchCEYnhr1mRurSt-njGn14FZCUwNyzsqVzVe-AVf7OXgc0hEjZOjKv5RBpZLBKBsaRa5wiTqdOojHdUNS_FRbL7gOayWYK_Cji6abvt7Crdwi5pvep7ed5JJLsNyXdNiWVnufX-r42kc6SoNLDgJvbjQbMzDQUQxzmpiU5PfoP_WksMA8-PYsxrT4x5aUheFROmiVCULP-sOQbBalbY60-Pbe2xGu4Ig5hPtFivg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=XRTUUj0T-r8MuqifYvRsccdrjhK6LUou9lD67Ew_icGbBTJZNNQkz-SZjcL9fooIT-aWUP4gm1CbyUR2K5p55Jjs5eZZgd8MnkCn-vH6oSGAXzchCEYnhr1mRurSt-njGn14FZCUwNyzsqVzVe-AVf7OXgc0hEjZOjKv5RBpZLBKBsaRa5wiTqdOojHdUNS_FRbL7gOayWYK_Cji6abvt7Crdwi5pvep7ed5JJLsNyXdNiWVnufX-r42kc6SoNLDgJvbjQbMzDQUQxzmpiU5PfoP_WksMA8-PYsxrT4x5aUheFROmiVCULP-sOQbBalbY60-Pbe2xGu4Ig5hPtFivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل تماشایی آاک‌یونان به لاسک اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/105892" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105891">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=H0p9s8KaPddUmUB_xCLnLN9e-9FqNxw0ooQes3yNYZ7FDlcGKLTAONkR6ChxO24DMo5Tzi_6c3TF6DIg82EXqPGCJLNukaynK44y_Td6k-ZFsYhJj3IbtK1ihbYj0Yvmi-7iRMb08l_xlDKq6ga0NI_RGSqR8a4n-iCGCnvKfio6Jd5eToiK0S5hWyKiH4WTlz2JeOJhUy7u3Hq8YP3cwRENu55qB5VAsUXVcS-DbEoDS4_lxyOwdCBUgmtNoMDuYqECMUT7RTV9dexe4gVkLl6IESKwxyOjRNqpyEUY-1pc9GCpADsSitM6IOgvTHMSiBN5g7-vgwxOgye3Bd08-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=H0p9s8KaPddUmUB_xCLnLN9e-9FqNxw0ooQes3yNYZ7FDlcGKLTAONkR6ChxO24DMo5Tzi_6c3TF6DIg82EXqPGCJLNukaynK44y_Td6k-ZFsYhJj3IbtK1ihbYj0Yvmi-7iRMb08l_xlDKq6ga0NI_RGSqR8a4n-iCGCnvKfio6Jd5eToiK0S5hWyKiH4WTlz2JeOJhUy7u3Hq8YP3cwRENu55qB5VAsUXVcS-DbEoDS4_lxyOwdCBUgmtNoMDuYqECMUT7RTV9dexe4gVkLl6IESKwxyOjRNqpyEUY-1pc9GCpADsSitM6IOgvTHMSiBN5g7-vgwxOgye3Bd08-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇺
اولین گل‌فصل لیگ‌قهرمانان اروپا؛ گل اول تیم استون‌ویلا مقابل کلوب‌بروژ بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/105891" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqPGviY1xikDEVtjIbQzIAFNpwTIL4GfolwXH2qUl2nrAVxVNzRHfQPFBFJsylgQOGgxN8B1yiFgIrwN4wc4aiP0bhPxTe98vTnUPcbBmjv1-z6BQUzculQDjp--J4V-YSvQ2LJr8GE8tJMc1AyAnuiu40EyTXiIp7FqVKKSXoHEtEcKicRQQeDYoeGJWfZE4xyHvGoEdXJOjD4N-f4VSDZ6b95d29zk1N0N-005WztjU508mllPIdgAb1jd2Y-gICtf2zWb5J0NJ44_C0SQCBzvJtLalupEDCjTBK2KrOGTL7lO-aIOoCashqirUGOPmjokYKAWFZCPXyfMJASHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
غایبان پرشمار رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/105890" target="_blank">📅 20:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105889">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC8PdzKnMskI7OARpVf1q87zKBz_9Vit40w8HDxmNj0zHxynjxzPYtzLwHjHe9xN6_4-oNFzOR8trNMNDINbO8D3u2aHK4HMlV7ZdSorlJUIlAWonpBb5Rpvi5d7Y4zP5ESlS9DaulK_2EPoINkXpxjjiLBMu0EbXNpkraZ7Peyj8pF9Uvux25glH7ZHTLkAFzfp_Oc6HkaGJmnB1rDsg16RT0wIht6MaV_HyV-6Ps2XoHsYfE8pIi5aCMoKUPIEPCvNu4EKDcCUMgYOaRi2UZD9RxMllPglaarmsnZY55dIyhw6kjb8pIqTwW-tzDEBSVKhfjmy_hUDUpvyAj853A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
محمد مهدی زارع مدافع پرسپولیس بدلیل مصدومیت پس از تمرین ریکاوری سرخپوشان در حمام دچار بریدگی پا شده و ۸ بخیه خورده است تا شرایط حضورش در بازی آینده پرسپولیس نامعلوم باشد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105889" target="_blank">📅 19:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105888">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7IgZpxy-zKpklGaDS0hziMfRMpDE792ARifx2_4pNt1uJDjQJ9QTVH5cWVhuG5borWhDy2SFcOz7pZTkcZ_tCiZ_eny0jvLlOHfuYpfC3XTH6--RQk6t7Rw6x5dxyd48g1Sv_wvXIjpoOnFlOLv7Z5WMEecfswb4_B2BtOPNSLS12D_gTBCTtC1m0zkSuUvZ5wYmVC_MAF0Nc5JbYx2Dp-EsvG7kbop15b96zdVJzQdDqLwwc7ou4-ZGY_8rl4ogZGfkPGfsZlzX_nbiekCch-pg3lWeSnSZm5noka9hyDKc3_X-F3Bb2LqlypU3t0W-qv24HVNK0IxCohWq97Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
برنامه‌مسابقات‌هفته‌اول لیگ‌قهرمانان اروپا؛ از امشب تا پنجشنبه بازیا برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105888" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105887">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca32d4904.mp4?token=jnBLmwYY06z1cc3QscZzjZiSh25pCefjOMdvzDL_7-AvrJjIZylqNvlGaxNAXRAV8IYy6mC0ssytkC_Y0UiCIl_NkfJJgAtukWc3E_rI7X9IBY7PPWkTOpfyuyNAsVzrpLC5yk4jeGAjyTD1SaP1TYMzw3HjQa8M1uLLP5qOEwXfxrYK2qfMmj9qkDl1mDEiAegyc8jCYcytIMux-Uw2omW4BPVTC18sf-t13hdyqyw7vL9lkrUFfs_oMdtdjsrMHQNqb8RBNc5Q_zWFs_x8hFCqGFYR_TmT_FGrd8pxCQQIZYzBRd9bsvEdKwvP0FEXt4fXx3-Da5ayVPU7VUt3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca32d4904.mp4?token=jnBLmwYY06z1cc3QscZzjZiSh25pCefjOMdvzDL_7-AvrJjIZylqNvlGaxNAXRAV8IYy6mC0ssytkC_Y0UiCIl_NkfJJgAtukWc3E_rI7X9IBY7PPWkTOpfyuyNAsVzrpLC5yk4jeGAjyTD1SaP1TYMzw3HjQa8M1uLLP5qOEwXfxrYK2qfMmj9qkDl1mDEiAegyc8jCYcytIMux-Uw2omW4BPVTC18sf-t13hdyqyw7vL9lkrUFfs_oMdtdjsrMHQNqb8RBNc5Q_zWFs_x8hFCqGFYR_TmT_FGrd8pxCQQIZYzBRd9bsvEdKwvP0FEXt4fXx3-Da5ayVPU7VUt3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره امیرحسین صادقی از شکست استقلال در دربی با گل امید عالیشاه و درگیری شدیدش در رختکن با یک فرد رده بالای فوتبال که منجر به جدا شدنش از آبی‌های تهران شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105887" target="_blank">📅 19:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105886">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59df1af51.mp4?token=J-NhzeiBXIfsrBzVBdMsq1d5sqbuXfIbtTZ8abi9w03_mtf2xr0W6aB6LjQ52t5k9n1FeTSXb8kMZ3U_CvR58utfBNKWzZig8k7V2UDie-RJv0zbwnkge4gQB7Iv7Ywk25XMSCONGO46QX5slQwXu6coTt3BF573z5FRDg8SbZLIwimJmMNWAqawFOzaAQD7q9NHCYe1jXguygbUjICyYK_8U5pdSKqzIxX3oTFgh769_smg0zuhV1fEEERzVulagypBDvbKZpebTZp0L3XkadnbWUjSK2h0kjZBzt06tFiDNydCt0WKuUbMr9A0rOA9Pe3L6Oi-ExNioSIPPKoEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59df1af51.mp4?token=J-NhzeiBXIfsrBzVBdMsq1d5sqbuXfIbtTZ8abi9w03_mtf2xr0W6aB6LjQ52t5k9n1FeTSXb8kMZ3U_CvR58utfBNKWzZig8k7V2UDie-RJv0zbwnkge4gQB7Iv7Ywk25XMSCONGO46QX5slQwXu6coTt3BF573z5FRDg8SbZLIwimJmMNWAqawFOzaAQD7q9NHCYe1jXguygbUjICyYK_8U5pdSKqzIxX3oTFgh769_smg0zuhV1fEEERzVulagypBDvbKZpebTZp0L3XkadnbWUjSK2h0kjZBzt06tFiDNydCt0WKuUbMr9A0rOA9Pe3L6Oi-ExNioSIPPKoEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشتِ یک قاتل خونسرد به لالیگا برای بردن کفش طلا.
☠️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105886" target="_blank">📅 18:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105885">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyGOy8MNHj6d0MEJJXQczok1vBHZTuaiGkb6kl8igBlyuL87aRSaDm-4-Nz3njJ-rho6twj84rKwGGtvzmkY2m0m0JjwCj6QrCDY7FUcEKfvQ1RKfTvgO3DsGdOqGg7JcZeVpt1HQpofg1Q_gexK9tSWVevWbIf_-_-erXbGK0QrYfsmI0KgaX5w4OlWfBkwv7QF5LxOa6r_6_7XgRPiNfoyylvSsGMzjDGkmJJS66-N9C4PSxo_q65clK_xkZwhOX5eLDvt9YV7OladSp357IMkocYJYz21M2hRGtg5oSzjfjLYZWG7RkcUC2Q5cN5ExVGPD85oRYg2Lm_YVbDysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
فهرست نامزدهای توپ‌طلا مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105885" target="_blank">📅 18:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105884">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a86823169.mp4?token=iWluwc1Xji224NXXOKUVGEMWPe6IMHOS1FO6aTGfoq0f4BQGvPN93BkCMPdTHUCE6oM8s9c9VAQeW2uSHc0ci3S2h5EsMMBhnvpQcRCM8nERANv3j8Ywj2_x9bOZs_m5nGqCKsqDblQ_St8cKZ6AvgMXPjEouSWdEhx8Av_izANuJR-zV7IeONA6G9sDXehVGerOhkraee7prKFeJNQ1UjvdnP43KLmcE-LSs6Y-5OHT40ZZ9srRCo2Q0gNJgldFhS6zcY5i8UqXUOhDjdqeR4HWZrjNF5ObmEvA9gTFZbVzpJAazjM-aIR6nK8DYY7AsLYXowz6a1jb-ztGCVO-sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a86823169.mp4?token=iWluwc1Xji224NXXOKUVGEMWPe6IMHOS1FO6aTGfoq0f4BQGvPN93BkCMPdTHUCE6oM8s9c9VAQeW2uSHc0ci3S2h5EsMMBhnvpQcRCM8nERANv3j8Ywj2_x9bOZs_m5nGqCKsqDblQ_St8cKZ6AvgMXPjEouSWdEhx8Av_izANuJR-zV7IeONA6G9sDXehVGerOhkraee7prKFeJNQ1UjvdnP43KLmcE-LSs6Y-5OHT40ZZ9srRCo2Q0gNJgldFhS6zcY5i8UqXUOhDjdqeR4HWZrjNF5ObmEvA9gTFZbVzpJAazjM-aIR6nK8DYY7AsLYXowz6a1jb-ztGCVO-sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمدخلیفه: دبل‌سیو مقابل یاسر‌آسانی با اختلاف بهترین سیو کریر فوتبالی‌ام بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105884" target="_blank">📅 18:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105883">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwKN9smNh7vgP_kjKhgC4SevlvkkZiSLNsuY1J_U1nPWXilnLUh8Uess9yS5VarDdCWmIfMuYX-zBdC_VgJC1rrNx-IkEO_aGKVhhrcvfEmhZassWUAgOCBqM2jspj2G7MuwlQatC6cdH3wnGicJDfRKsyXjVZh646Td5Fl-5MAM39Ybj3fpXIy87mVKgON7Z84T0DLUH8SZTvRwc5dMeiMfB2n_pTw3K7mFPiky0tOF5YnKWLICk1XxXtoFfahUxZ-pkVneyqm4lPz0KcOzuK_JUalyMQ-Ls5svw9N2KG1BmyftYGhhIvWgiUdZ57bs5OSroSzVY6clgChtiSnyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
پادشاه مسی نامزد کسب توپ طلا ۲۰۲۶ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105883" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105882" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105881">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT9-vF0dzd4hR92gkKy_2F7E5x63NNcScOl-bTUvWXDgvAUFmIz7htGplMh_nKpFtfVXI1PxmN_aTHlVdUHlezfH_fCf-PMHibysb2lUp_5_xGicFH9mr5UZgZZJIDq607zM9aUHJHE1_DXobRePnzGc_gaVw0ed5qdEKEvXDe2CoapA7asOB__i6VzQYien1kGPBqtZVKMsO0LOBnkFQhPGMUw-CimzVGNrAwS_RxlEO81XYIOKMOgVT75cbOpc08jP9Pzr5N1Am16KPfnqVla4DZ8askTrwgO6ts3pT9LyD-6Uf-_AGC-Klr--fkoBCHja1xoCpC8fvxY59wu_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105881" target="_blank">📅 17:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105880">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG4xPk8nYlVUOldWIh2AX1x83uFc4QVOAZuYwCncDzCTkDyxbhGsMT9J-49t4GWQmn6nNxflKSm-jdT5IuF7lTVjB8o3X1_XIQYYGJwdFjsJUqEFMqdpjia0nDmMNQfVjVGKM5ZjnPm58akBIX7FO21iK1Cemmivmq6IiNKvXGyMBv6_XWeyBPP6PJ0EtqSgFxhddLDVqb8DEke_V6mXm1QpTrZUL10JSmQSiNngZp3IkfO6qDivACACSwEiuCcFUfxgguXr9OO-AN6FHoI10UqExtnKadFlzGo5Kl5Ijq2QhSHmp52NdlCHiPStcYPWkj4E9bVSZ5_ySP-ZfvfDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
ترکیب‌احتمالی امشب‌اینتر مقابل رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105880" target="_blank">📅 17:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqmicQoVY0T6peVmCCFjRe_h7I-e9Zab4WDjQ2aZwd3T8Qvof8ytLjtpDRpaG9j8D8R_fAaiC0sfDVnGBP7Nc_AL2xzWnHxs3TCY6oEJ_FBpHO3cDWqEvcY_kiT7f2Ia7Z_IWXdoA7FP-aS5m49TBbMxa6KjIXEULxmy8hdYOlUb2dAqCIgszNOr3UI3H3RWv9BEfunCVngC6GEzhBS2-DI82o3SNzBMC0nmVhkdN5ff4OyC4CANO75eQJc5C2R967E5d6LgM-vZZDeAeQ0Vjcw1kHTIappWXQVE-ir6yB1vaREIahKmnJo3-UTMmtmRh4knDE8MR_OutECb3es6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
نامزدهای توپ‌طلا ۲۰۲۶ زنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105879" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNMoZMJ1yvPvdN8hDOncoDrnqkBvKJ1UeTCXBRKrTSapt7vbLu-Rf1XMxYb6zSQDucKfG8MaDnmvwbgB4blER5kDPDEgB-SbZI3dmcLyPNR0S8wpVKPtmqTcLg2MekWOMM1yqSnkAYmkfaH8W88IvgJwdNyNbZRgalIaG0OTuR1-RUYxA4akKegPGiiQtScH0hRiJ24DG2Rj0JtDEc1Xakx7wyMLOm-phYZetff9x0mhwbUPxiiUUv39oJnUYoLPttJe1AdHiPd-zV6MtXgVt7aaQNkfAvR63fE2gJgMmV3i05SWj5iMpO3ywE_dn75f9DUXtKkWV3GUL5EaQeIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
پیراهن اصلی تیم‌های حاضر در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105878" target="_blank">📅 16:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پیش‌بینی یک سال پیش خانعلی: تنگه هرمز و باب المندب را ببندیم نفت ۴۰۰ دلار می‌شود
پ‌ن: قیمت فعلی نفت ۹۷ دلاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105877" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105875">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEoGK3PJBa08ScyTsLQu3EHWtQk5vIZqcpbSXjckvYAg9LdjtxrS7m0tWYcd83KUOqHy8RylpNduRpNLe-U4xlhZuRrWinLlPISp0O0Uo-hUADxK3oFxyqDPlpG-uMtFCWtbZ8yfsQsY5bK3xeheB5iyhqc73aJmyMnj7dSyc22oVpJ6JSV6UK_X54X-RzT8he4XaUEApSiC3sb1-Ia5o6_Jw4di7GxYJjeAjRPyCKCoRfk4mIHXsh6JlU9SQItkJbdf2u1rBRyk83Rolrnxe46lqeYpt9DM_XrNdKBlELZh4pQGWTxZodriFvSQbopgRmIG-SB3UehIcrH4lzacGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mbiu_fzaRTNDVNonC2uPOQoCNa1OiIPsAMWbjG1R1kCPElyYNOptbMCkT4bvB8Ec2bDGc4tqoKSUNUFBD0OSz4BYjmSxlmUbtWPPovqtUo94QwpNpAWHWN56UXFtxjDlSWdb3sFBMRknG2Ginq7g_6FPey7q60DmrYAIXs3iLjSlAgFbVsLv_fNO3UCzqrg9VF-fdKmx7P75MoQGQTMDhEuGAWRZTdlSWswUx2mzPkRzNSWkOsWMJgC9aNmlRDWOOnkYjSQ-qPNe_vy7d9V3t3HONdPqUtX3gqd7FxSo2PyEPrsvA_IHHXwE6rFK3rHC5VDdgs7yf6MeAQvm0gWtiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
نامزدهای جایزه بهترین بازیکن جوان سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105875" target="_blank">📅 16:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105874">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابوطالب یک‌سال پیش خیلی قشنگ کفت؛ تا سال‌ها مغزمون راحت بود اگه علی دایی اون پاس رو نمی‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105874" target="_blank">📅 16:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105873">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
❌
🎙
مجری شبکه‌دو خطاب به خداداد عزیزی: فحش دادن شجاعت نیست؛ و خطرناک‌تر از خودِ توهین، زمانیه که به اون افتخار کنیم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105873" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105872">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
یادی‌کنیم از روزی که کل‌ایران به هیبت و بزرگی اسطوره علی‌دایی در جام‌جهانی افتخار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105872" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105871">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ8-3wD_xHaaosK1tNIdzUGea9iRnN3qEiPQGI3gkQ5ujXhIbLNrRzeG7Irj-kHTs2GOv85vS69Dks6hT2Nu6k6ikRyEFGQAILyR3NWfIHTMhht2NvBfCJZWxdIVw6GhNk4RpuuffLvKtO_8oixcU_gexcKp3GKlYjsppVJ-OGMhdcl2PlUYCvnpwbRNdhKEkUrHFIS-pKS76LwdzTdHXNUo7LXcHlWzhlUzXtNrr4pgiqvon9_55o4IMzxN3BfMur3vcFAUAvt4yld0f9dgSIN8eSX7GzSFczA7eXaqQPTDmQYbmm-lCV8w0w7bBQpBgxfWT66WKZLJhuKaNKUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
🇮🇹
نتایج ۱۱ تقابل اخیر میلان و یووه در سری‌آ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105871" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUwfIwJeLpVK54YvwFA8HKwvWgBWay7ClP80c9F306Gk3DrODfR3RO7Q1pw5wBra7GwUQJfYjAxoSKHmql5Z1ls3ydh7zwb6pPchkhEqzIpE1nFNmMdboScJC9ZGjFcA-KRLGzCz2goQ0U1bbPpv__zEOnRbgaujdnzm8aIGQr6g20h1M1M5d7tAFOLI4SE1wqdt54WPBvj2HH2Y92tJYJnI5hu53m9xp_BjX88Fwx4gkA2c-mCkqTCMj12tByqNKlix30EWKvBm77bHHaCgpPk0mUoELPXXS9Nbsv7goDZPKxukKlr5DfCywBZx_GeV5ZMwLyaN_0JJ9B9s6s0SBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست نامزهای بهترین سرمربی سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105870" target="_blank">📅 14:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSgm37HzCULf-HXApIb_HCU3-sEFrsWjGW1MMixXDU2zosXSpdaVwU6e6QOVd4FC1UCEAtf7MkV3DRs-HMTIfNpDIOZ5AjcnJXfnMER97F9fmWNfrFjwnicdD5nYWQr9Iyh6qSb_akzOQPC9ihfSoxrL_5A7cHEKCH769QfqQxcu3C_d7JqAEkADra1GG_x-u4kkqpTgu5W_lOm9uGS2o5Z5L-48eJE1nwtQZPwBuRpkuA2Dg4Pt1072sfe7v26ikW0v1SxqE0lqEm-bRAGZkwPgNiU3aex713pifWu79nkT5E5BVfER7ZThNudX6ST2NSNXzEXezgtDsd5bzn6s6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج سه‌سرمربی اخیر رئال‌مادرید مقابل بتیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105869" target="_blank">📅 14:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105868">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeAICC2sSnv2NKeJIYswwyCR5HmidkpxkJwDL9W6MR6ucpt-X-Jc4DIkdSwjS__H8doKMRbbUzhh80J43LCc5-ePejp3VMihx9pSdQoC6c2OohjF00bZrkm-MGcRZIX8l8uWXczEeoRgz5fUIfoG6Rp4QkrIMVb4Wxx6btAx1e3m-8yLsGciCrAPf_oSBYCjRz4LI3R6axoAaO6RGkx4M8tFYXNlkRxu6xkyrTLlqf77cbmKL_6mAZDaxpDajdElAjkyMKzmScqGMXPYGX4LtG-uJ6rpLyCnSPy_vH9hXgvxT52-lfc025vJLKJ6ebVqJ_1XP17_bWYTASmmX8RoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد خط هجوم بارسلونا در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105868" target="_blank">📅 14:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105867">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKukd3IZGCzEUUN6daKkMM8L8MeUNCUR5DQKoctlv_IvdCcwtzKq8ExTuPFZd7pAc3XqZcS3JRYZioEdd76iDrhkc6Z9eQ6mY_N04vkHhl2gHBEyrCkM8lhl838GBBCPld4tzqK0TKpyrRT23CmqcXJ0rcb6JW1U5rDXRYkdujQuulWxYUeuPZLhKm7q4FqYLZSk8RO-8VZLPKU91Hq3uwi3DY5OLLiScj0zm7-Qmdya8y6EnEI7Ky5SN6kEQuL7kBxvldngRJ3LphXahZi6zSTRr0kpnETRbB-Jdhu-eFtx4P89mVEwParGAEcttzEBjXfWZ_VPyoOXxiKvAUm5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
🇪🇺
لیست رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105867" target="_blank">📅 13:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105866">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoQWVDJSUp2nEp9RogVnVnJEYK9sHaucgT0BAFaCUb3-ZF20bXYCuXP-r98fhp1Ja1s6pmr0eH3AoyWmD9akPoLcRO1deCHfduY7GHes9hyJa60pOYFEf05K4h_5_AMExmVxdgI9LmDhz-lt3nTqK6pHEzeDDLR0U2yuvoG148hVUhBqiFWGZrdntexzejzAx_3jZBaUQ7spy9kG7gl5ysZLiSZabxf6Ag2sIbjfF2vXxeAyZiuhhsNE_Jq0aznwgb6M5mmC2lkJV1PKqw71tQK0rLg9TeAaRtWuWfPLe0tdDz3JkcgynvQRLKuMOkPUsCp2GyhLtC8rwjV8Cq8HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🇪🇺
در آستانه آغاز لیگ‌قهرمانان اروپا؛ نگاهی بر بهترین ترکیب تاریخ این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105866" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRsr1NDlP1MkOizfQCkQZzEwLcAtaAZLn13Is_2D3X1KpwejI_C0gvO6EzRDclHcv-17zxzVD4gbxXjMO-5hZuf3lLDLWbLTpmTc2PrpQR-JBdQVNgf8TiOARgPeriWsikksBhgD17Dqb_aigMG043PjzjbotZb2hJWVKKozihSmslWkUrm6bYrGBaXGvlgPO27irP6WqL5DGFMj2OLDs7S5oIlLHEwqtz7XygV9Ov9ohqyZnCVMFTsoxfotcqoFA1xkmbeAexnIw48klMD7kNWWZ1JK3exR-3WdQGVvnj3PQgQ8Etl6j5tsnHMm0994nOcYzi5h-fQv4MRsBedAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
نامزدهای بهترین تیم‌مردان فصل‌گذشته:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇳🇴
بودگلیمت نروژ
🇧🇷
فلامینگو برزیل
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105865" target="_blank">📅 12:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇮🇷
جلسه کمیته‌انضباطی باشگاه استقلال برای رسیدگی به تخلفات صالح‌حردانی فردا برگزار می‌شود. حردانی در بازی مقابل پیکان غایب بوده و احتمالا مقابل السد هم شانسی برای بازگشت به تمرینات استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105864" target="_blank">📅 12:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubyFpayDrNhtS1Hl1Ht2xaZUtyOIqN_KZFoOGzwf0v5upUFxnX_VaPfgizStmctKg6BmPEdQMy_Q_mwyyuMwekGa4o7f6bBXkg4eYYgHNlALv8MXY6s87MNu_42v20oeu57-VfFjg6a_MonE7heQkMPxWOX_Q7-s-Ie4WZ1Xmf9QjSTc1xLl5OUXCWz-Fg-5AXWX72KPT-0Isj2jGmRLgBOtu7arXsfCPUovjTy6G79LuAoIPJiA0jKAF3ZeDb-uANH-nx3qxf6DlJRwE7If1qR3CwKTwYSg9pK2xEtAX6JOHfndPT5lS2V6yXCA2oULuVjTs7JfrfuYTqU47saWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نامزهای کسب‌عنوان بهترین تیم زنان فصل‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105863" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🏆
آغاز اعلام اسامی نامزدهای نهایی جایزه توپ‌طلا؛ ابتدا بخش زنان معرفی میشه بعدش مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105862" target="_blank">📅 12:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hfeoz0AJJqB0UP4JP7-p7bJUBZ0H508xaw7lggg4WX60pXDk-0x9RJet7vbfzpeVz6a5-diQV3e86LODykX-gSBmkAQv22gf3PdqBMuluWe-ooDveKlTqSF8CetfAPIpKwtSHL0UKXk7UjAcdHSJxrfM9WR6LDZem4mMq1O3gnc0mDsC79p-W8u0UXqfyQVgQ0cL-rA7vFXhrMKfaL_FrJkheznidnGz7XczsCAHEFGCmIupLlKjzervbzC64B2OH-wqP6f_MOwTxDs2UbVioDtbTMHo9P-1A7CSfcHKSTm3HW-CltOFdFYvn9kg1OQT0Mu3OVl86e87njT0TWG_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
آرش قادری مدافع ذوب‌آهن ۶ زندانی جرائم مالی و غیرعمد رو با پرداخت بدهیشون آزاد کرد. با این ۶ نفر تعداد نفراتی که این بازیکن طی دو سال اخیر آزاد کرده به ۲۰ نفر رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105861" target="_blank">📅 12:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=rYCi6ZbZ3saB3iULPWufC-J77YCcM9U68x2DmUpRiDXVdRu5m9wIDsM4EEZ8OTXCLMON95Qu5HhAbk_Bn1eqZ9HbATAqcFwqojWoUAw31DBZYB9JfAPCHNDMA8ZOoL3zd_IYjK1Yc6_7TuWHCRwC0kxdM7bPZDTqsq1ZRvswMzOhbK2NGXp3441mowUBD1i8mwI_nlDRrTwZmIBUQQvpJL-_Acob8Wl_UIc0tobDZ4Knyb9q2YPpCTZXGWs0NwZ8FdLWW558zy88WqoAAByKNrcgvfz_uovrSKkbkmKZreYjY1ByTCn2p0OchwfXbfW9JNXDuSKwSYJiZEREKT3nFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=rYCi6ZbZ3saB3iULPWufC-J77YCcM9U68x2DmUpRiDXVdRu5m9wIDsM4EEZ8OTXCLMON95Qu5HhAbk_Bn1eqZ9HbATAqcFwqojWoUAw31DBZYB9JfAPCHNDMA8ZOoL3zd_IYjK1Yc6_7TuWHCRwC0kxdM7bPZDTqsq1ZRvswMzOhbK2NGXp3441mowUBD1i8mwI_nlDRrTwZmIBUQQvpJL-_Acob8Wl_UIc0tobDZ4Knyb9q2YPpCTZXGWs0NwZ8FdLWW558zy88WqoAAByKNrcgvfz_uovrSKkbkmKZreYjY1ByTCn2p0OchwfXbfW9JNXDuSKwSYJiZEREKT3nFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سون هیونگ مین در مقایسه مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105860" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105859" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHPiucW3hqXUFEwQ2SkrHOS7003hKm2MlCpGG5Oo3YAdO4MpqJpTf6yACf5aaONrcTHZMt2fxurGZNojN0WaJI9tnxJdevlJwac7zDmO2P8KZRsRwb3ksrzXzCjIcSscLvE9xu8sMzExU0ylmqmPahqjOb0Pj_NrJUA2cfI7Hd0Hy1ZIrT7vON9URVAdCLPKxSPlnwjNnlrsL9kG1sQCBply890G-drBOmU-n52tSaKxTwivB6DlPyjKrCOsGd6hG8io24Q5GBZ80e6u4BlCvMqtQohnXJJ5kGGKuz1YgvODgPEuH-aXY83kMT9E8fW_2Y_yTyfw8A2V_gIy9af5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105858" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105857">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hae78R3ZA1CPU0wRfWW_DZ1FUndFxqQaBxewGLquVD4pFETibnpY5H5izmy5IYHogI02KWVuweG4lYT7mC1IPvYlXt5NcdZ2_8KJ0YXUXEdz4TW0V47-vzYQh6Ul93SbW6pX2BX1qPSIAYmTbsB36T0_6OvzEe4vybTBjfQm8pcJvdnOmkEtRQFWMAkqzfFUn6RoWK3_-jzz5aOAqvbH4S2dd-MX4JKlHtoxNgUvz7tTSoSWIMFDh-mxK6EWs3ACg8eEL3QYcg5VRxthg9Wz5WPvxor1s3G_Qp6gfk8Emdy84fBJZ7NhQXW7FJMuy3HiSOEbw80wba_BVeZtI6O96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🇶🇦
🇮🇷
نتایج بازی‌های اخیر السد حریف هفته‌بعدی استقلال در لیگ‌نخبگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105857" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105856">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSIVCqwi-hqYt-1cjuJmIKVvZTpWe0T3qfoYwiV5iTVgf10TvDdHPFce7e5N_DXKeH7PBUdSYghhz-bQn104ohucIhdUoAftPLYvNLG7A3-xu7Be-nz9oqXcbiHD9hTRw4w7aIHOmI9TwO-6sMpjiZrGnpedRV5rAsI_jViQ8Fm6X7zY4nLbTVrC--CwAdcxCYVCdlDtiXdzvnvaBMzcJ90NrFZ6fLXGNGTftoAUr3vgD0rzBDoswN-OM3_zISz4xHbKqmyBkqZfLBcusdi531t9S_3oZLOmZUJCFc-ifQnBAb2mi1E1BegbaJGTkD6Z36cwVt2chuqkgcT4LZSIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
لیست اتلتیکومادرید مقابل لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105856" target="_blank">📅 11:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105855">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=uM9kPeooTBell81V5zaYKCpumBD_6HBHcklt2qM1UumFdA4qwU7fhCnfG_OC9XKrb957T3lqj_vrIKSTQPvJpibCp_JQuFdENLv3d3ELy7AnFDzfPtfYYDXjs474IYxdzTBfj033Lpf99f7quiTgASBmHR4F5XuqkggIoo3X5ierQDk7ic274huBy-kyZZuAMRFs7R7Yc5sOGn2gVF9xm071hd5IyYQnw1oEUOcqCluZ0_B0NSn31pyb5cHOJzwCFaycP5JbkCFUzl_duz8Zojw7t00brJjtO9mWLkcc3EBKnlN89suSF0zdhKMy97t88FnPSavMgaalENjlJkpGjpmZVB-dDWt2UQu5t5UGWf9_SBEqjmasfRyAb6i2TTXyGfGyiLwOIuMckOvt8lqOl7hDCjvNbOAsmu50mZltIF74GqW3YEOJLBv4m6plZd9jEABIYd0zIZXxPSne6udGTAQT_boVVkp7KqxyHAqm1O-RyGdRkhxgfMXMe3ealP3iIW_DlTVkzH5NBjnPx1NIR8dvL64tSl7JF1MP465JXyCz7Nd7RWnjAgnaG1XHdyE0u6Cmwan_Gt-L1hwvXQCXIgDDK-pcooATvb93refBG1YtrBMqb3ATG_RzDPcP1Xsi4TMlD_N-l2r39o0mTrPZRf0xDcHb9lpXLz7pM4jvE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=uM9kPeooTBell81V5zaYKCpumBD_6HBHcklt2qM1UumFdA4qwU7fhCnfG_OC9XKrb957T3lqj_vrIKSTQPvJpibCp_JQuFdENLv3d3ELy7AnFDzfPtfYYDXjs474IYxdzTBfj033Lpf99f7quiTgASBmHR4F5XuqkggIoo3X5ierQDk7ic274huBy-kyZZuAMRFs7R7Yc5sOGn2gVF9xm071hd5IyYQnw1oEUOcqCluZ0_B0NSn31pyb5cHOJzwCFaycP5JbkCFUzl_duz8Zojw7t00brJjtO9mWLkcc3EBKnlN89suSF0zdhKMy97t88FnPSavMgaalENjlJkpGjpmZVB-dDWt2UQu5t5UGWf9_SBEqjmasfRyAb6i2TTXyGfGyiLwOIuMckOvt8lqOl7hDCjvNbOAsmu50mZltIF74GqW3YEOJLBv4m6plZd9jEABIYd0zIZXxPSne6udGTAQT_boVVkp7KqxyHAqm1O-RyGdRkhxgfMXMe3ealP3iIW_DlTVkzH5NBjnPx1NIR8dvL64tSl7JF1MP465JXyCz7Nd7RWnjAgnaG1XHdyE0u6Cmwan_Gt-L1hwvXQCXIgDDK-pcooATvb93refBG1YtrBMqb3ATG_RzDPcP1Xsi4TMlD_N-l2r39o0mTrPZRf0xDcHb9lpXLz7pM4jvE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید اسماعیلی: داور باید شهامت داشته باشد و از هواداران ذوب آهن عذرخواهی کند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105855" target="_blank">📅 11:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105854">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97326bc667.mp4?token=INDgq7TXn3EM6nDt7UW1QUX3FplQ3AdV9G4ws3n8CPJwavxEo-DkCn47eoIRAg1vwKI3byV3UckLywiJzLfBteLOvD6gSHqniGL0x84MHi7kKWpSYB4ZAvY2pcLHx7UIZaaK1M-q3-jK8Zpwg3dNze42j7clbLL1pDO4pSQRPmOojbSydTb4LnnX3H5NWcp_YOFSYoua6WgIbrkfJnmqEU01UxWQK5CyBWZH9Iap1qZ4zwH_f3R7y-EpN6C9Wh7lq1AB6skonR2CQAdPly2ybWwSYLIAHU7d97YXKFd4NalbTfdSV_EX4jEHHgBKdEBZEymqdwuzZaJUfMP9HU6MKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97326bc667.mp4?token=INDgq7TXn3EM6nDt7UW1QUX3FplQ3AdV9G4ws3n8CPJwavxEo-DkCn47eoIRAg1vwKI3byV3UckLywiJzLfBteLOvD6gSHqniGL0x84MHi7kKWpSYB4ZAvY2pcLHx7UIZaaK1M-q3-jK8Zpwg3dNze42j7clbLL1pDO4pSQRPmOojbSydTb4LnnX3H5NWcp_YOFSYoua6WgIbrkfJnmqEU01UxWQK5CyBWZH9Iap1qZ4zwH_f3R7y-EpN6C9Wh7lq1AB6skonR2CQAdPly2ybWwSYLIAHU7d97YXKFd4NalbTfdSV_EX4jEHHgBKdEBZEymqdwuzZaJUfMP9HU6MKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🧕
مارک‌کلاتنبرگ: گل‌اول پرسپولیس مقابل ذوب‌آهن باید آفساید گرفته می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105854" target="_blank">📅 11:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
واکنش اینستاگرامی خداداد عزیزی به محرومیت ۴ماهه از حضور در ورزشگاه‌ها
:
چهار ماه محروم شدم و الان دارم میرم مشهد به یه زمین چمن سر بزنم. خواستم اطلاع بدم فردا کسی ویس صدای قدم‌های من در چمن را نگیرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105853" target="_blank">📅 10:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
پست باشگاه بدبخت و خار آلاوس بعد دوم شدن در لالیگا پس از هفته‌چهارم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105852" target="_blank">📅 10:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105851">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc1-PlnUL3ANpS8t9Qxdm7NZE9UktnWdWc2-cnn3_4Q35qVnvK_GpC2hjCEF_F5VOO3tPYMUxyNCLsBNVpqJqYVWzNioG-IMKHcXVCu6f4snFzCLvq59OJzVJo9xDEpTgXEpwYZi4aFaX3IsenetGZJ_fGlU_djFXfu6ZKbWcwkpMRrP57OPvAfymNM1m_UxeartfpHvFAS1kfsByu9j9PCk8xRpkkTNXZernIyY9YNvHq4OuD5Zf0kvfxduHeS0zy3N7O5mieGbMkr-5jbF6HIzO6nN07-XdWVQ32_OpMHGG3D8iddwvMby4Q9EY7hOzH5gwmUGXXzHumzGfsmyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز برومند پیشکسوت شریف فوتبال ایران و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105851" target="_blank">📅 10:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105850">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=n7a2gKmHR6EU42SDBpgaBswYnDxRGN83SeqsQQx_bzDAUl4YeNgukO3woYoggscFs3YwEd9FXM340YlqGFVXntb1hN5A5gA8VqDsOrQxNkeeH6MnAqV_75x04XkIu7WGyNVAcATUCaRwLSU-j9s_UW31G3rBk6i28vcisXaac4M7OqmnenJv4rjcEkEDmX6gg3Q9B1Jp01SFCHNI8sd4PBucJuRnoAN8LYjGjqdO8Jc-iYrYie9h1LZzffvna8ms3O2w7ZN01YTqsdvwPQG7WuZ1xwAeaHGqHjCs7zKmIQE0MSPaw8iWgJ5OT_fWEuln-_HYsn7RlJb92vzNllTcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=n7a2gKmHR6EU42SDBpgaBswYnDxRGN83SeqsQQx_bzDAUl4YeNgukO3woYoggscFs3YwEd9FXM340YlqGFVXntb1hN5A5gA8VqDsOrQxNkeeH6MnAqV_75x04XkIu7WGyNVAcATUCaRwLSU-j9s_UW31G3rBk6i28vcisXaac4M7OqmnenJv4rjcEkEDmX6gg3Q9B1Jp01SFCHNI8sd4PBucJuRnoAN8LYjGjqdO8Jc-iYrYie9h1LZzffvna8ms3O2w7ZN01YTqsdvwPQG7WuZ1xwAeaHGqHjCs7zKmIQE0MSPaw8iWgJ5OT_fWEuln-_HYsn7RlJb92vzNllTcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنایه تندادموند اختر بازیکن سابق استقلال به رامین‌رضاییان: فاميل‌هاى ما سه تا جت دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105850" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105849">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=EO-U_LR_aABUbpSL0rg57HXVP8mqA0P4bgCRNwElVJz_IjXD5LC9_N4F_oM-jMWQiAL9MK-gQR8u_oQCJvPwKxKJ49uuCcAe3NsB5v4Tm3__sej-YIN0xyURH-_lEVV-0ILp8jaq4dCRzR2wLmBdYW7kUGh9oxz9u_2fr4ekNDHKiphx4l7vkh3fbSAXfUJgQJTTmtm-KeF85WuU7_oOIQeEWGiBmaeyU8YPPWyVfjsG5x7vML4SPxMkB6ugKLwH0E1ASn0w7dL9_PAwykydzKttJUkDfI2aYVA9uWDqCwWZ1GnpDhDKSl9KocXCPNhTbW3gLymmf2Xrfew13Ksusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=EO-U_LR_aABUbpSL0rg57HXVP8mqA0P4bgCRNwElVJz_IjXD5LC9_N4F_oM-jMWQiAL9MK-gQR8u_oQCJvPwKxKJ49uuCcAe3NsB5v4Tm3__sej-YIN0xyURH-_lEVV-0ILp8jaq4dCRzR2wLmBdYW7kUGh9oxz9u_2fr4ekNDHKiphx4l7vkh3fbSAXfUJgQJTTmtm-KeF85WuU7_oOIQeEWGiBmaeyU8YPPWyVfjsG5x7vML4SPxMkB6ugKLwH0E1ASn0w7dL9_PAwykydzKttJUkDfI2aYVA9uWDqCwWZ1GnpDhDKSl9KocXCPNhTbW3gLymmf2Xrfew13Ksusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ماندگاری مدیر رسانه‌ای استقلال: اگه کنعانی بتونه با شستش گیتار بزنه، واقعاً از نوادر موسیقیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105849" target="_blank">📅 09:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=pqZwN06nzHVq70wUwgB6gE1nuxy2r7dtE1FwotjT-X-Sd1IHQHSr-6Tpi2p1dSQT6_XZ3hV8GFK4cSPN5Wt0e-jzTLKFLlQN4hDQ_0pcudfmuXuvIi7EFLipDaUA1O5G4pQl9m9gOVxiw_LI7SlA-F6MdPIEg0w6D7pVXr7zlA4NMhbUxNBzXeEW9hjvlsWbyRHzFQpAHQob4PoXtpCfP-UciDYlGVwPn2tmCxG7PC3HHvpXYStxe6nCJX_QkaERZwPf2tXkYfjIsyoVEfd0PglI1uaZoTko9NQzUF_gzIseHgRItiTkIaYIaJyVfXONdSNCg_W15O67LEzwuRw7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=pqZwN06nzHVq70wUwgB6gE1nuxy2r7dtE1FwotjT-X-Sd1IHQHSr-6Tpi2p1dSQT6_XZ3hV8GFK4cSPN5Wt0e-jzTLKFLlQN4hDQ_0pcudfmuXuvIi7EFLipDaUA1O5G4pQl9m9gOVxiw_LI7SlA-F6MdPIEg0w6D7pVXr7zlA4NMhbUxNBzXeEW9hjvlsWbyRHzFQpAHQob4PoXtpCfP-UciDYlGVwPn2tmCxG7PC3HHvpXYStxe6nCJX_QkaERZwPf2tXkYfjIsyoVEfd0PglI1uaZoTko9NQzUF_gzIseHgRItiTkIaYIaJyVfXONdSNCg_W15O67LEzwuRw7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تصویری از کنایه امید عالیشاه به داور دیدار تراکتور و گل‌گهر: میخوای بهشون جام بدی
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105848" target="_blank">📅 09:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پیام جدید وحید قلیچ به خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105847" target="_blank">📅 08:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=SnKVEwoPnaWFjai2yXQwSc86bZ4jzLHGWHrRLdJbJ6TUckwY3P9fRbsdM5VwfRfDCn73JupblCR2HYoLe3sLNBL6hXs2VkOKwdxB8K4wYgQnNAssGbVx7HkcS50hvpbg3SkOhXZkfoBBmT-VR5EZwrRkXfBL5NC6KM6cNR7ZXdPI9DeXEm5Ip3H-dredD8NIBiky8t2OAWiBDMtqRGEZM1tF4UzWF-XeAFZiknPtE5jdxnycqc664zzHDQRB_G3jrG2BM1mQI4NQldYAG2NUf3mHWRa688MqmqgocOlSD-UaA3LAjvwEpjduofuTIkgp2cvxppKSgXljlqSJvTI0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=SnKVEwoPnaWFjai2yXQwSc86bZ4jzLHGWHrRLdJbJ6TUckwY3P9fRbsdM5VwfRfDCn73JupblCR2HYoLe3sLNBL6hXs2VkOKwdxB8K4wYgQnNAssGbVx7HkcS50hvpbg3SkOhXZkfoBBmT-VR5EZwrRkXfBL5NC6KM6cNR7ZXdPI9DeXEm5Ip3H-dredD8NIBiky8t2OAWiBDMtqRGEZM1tF4UzWF-XeAFZiknPtE5jdxnycqc664zzHDQRB_G3jrG2BM1mQI4NQldYAG2NUf3mHWRa688MqmqgocOlSD-UaA3LAjvwEpjduofuTIkgp2cvxppKSgXljlqSJvTI0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💙
میثاقی: با صالح حردانی صحبت کردم او توضیح داد که اصلا قصد حاشیه سازی نداشتم و هیچ قصدی هم برای حاشیه سازی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105843" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=hF9G9-Tfaf-pBLYJsQzvtZTtVnYAkkzh_niVt1-O-tWgPH1a0UaPQIF0-ppDWIG5UDqyCvNWuHbvl1eYQvDEijVQHCs18Nl1YkOeQXgni-_bIrh5vkgpxZqlgIFoqJEBfPFEyazHaIwCfOAvw96uMqid97mio9YS1i3a-JivnGnV5hkfBMT9sRPQOE5cG8L8-wsuLJpoaqY9jFeHiAHI7K3HDPkP5CSQYh9W4-3LTWTV4Bmnipv0ZWkC0S_hUvWmGIWRpuupyndNB0-DAnl6ocmeHGNeQp80COGaXJO_glyO9XRC8lcVkFJoddkRZY-r0OFylCmSCgQpT-a88UXTmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=hF9G9-Tfaf-pBLYJsQzvtZTtVnYAkkzh_niVt1-O-tWgPH1a0UaPQIF0-ppDWIG5UDqyCvNWuHbvl1eYQvDEijVQHCs18Nl1YkOeQXgni-_bIrh5vkgpxZqlgIFoqJEBfPFEyazHaIwCfOAvw96uMqid97mio9YS1i3a-JivnGnV5hkfBMT9sRPQOE5cG8L8-wsuLJpoaqY9jFeHiAHI7K3HDPkP5CSQYh9W4-3LTWTV4Bmnipv0ZWkC0S_hUvWmGIWRpuupyndNB0-DAnl6ocmeHGNeQp80COGaXJO_glyO9XRC8lcVkFJoddkRZY-r0OFylCmSCgQpT-a88UXTmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💙
اسفندیارپور مدیرعامل گل‌گهر: سندی بیرون آمده که یک نفر از آن طرف فحش داده ولی از طرف ما اتفاقی نیفتاده است!
💙
میثاقی: پس چطور عالیشاه 4 جلسه محروم شده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105842" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=A05-3Yf8N69ohU9uP6ys3kXSf3vZKYN78UAKifowJsS-dAa1UAlQ35hHuaQw1i_VYppVPaQXvwEKInSzONfIEsdXoCWMyY7yTrZGnrmJfRP24RIQqr1FFpQEjS1bV6WHME2t-ALLGu1yyD4GRwkwcGyTVgtSIr9z49Xe56F173wJhnK5wu81zR4d2TuZ1BbglDvAx7VRgUNF1mrIeOkBsXkc1PFxlg-18DsqzLXrrEawcU6gBod1fB9BAyZADPU7XsoubSAwxfT2RMncEeQsfBSn8ZJhZZxHi8DiAv8bJcHjlETSyBUCMzW66qmR7KwZ5kYDxsGC3pr9NJrnRsyWyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=A05-3Yf8N69ohU9uP6ys3kXSf3vZKYN78UAKifowJsS-dAa1UAlQ35hHuaQw1i_VYppVPaQXvwEKInSzONfIEsdXoCWMyY7yTrZGnrmJfRP24RIQqr1FFpQEjS1bV6WHME2t-ALLGu1yyD4GRwkwcGyTVgtSIr9z49Xe56F173wJhnK5wu81zR4d2TuZ1BbglDvAx7VRgUNF1mrIeOkBsXkc1PFxlg-18DsqzLXrrEawcU6gBod1fB9BAyZADPU7XsoubSAwxfT2RMncEeQsfBSn8ZJhZZxHi8DiAv8bJcHjlETSyBUCMzW66qmR7KwZ5kYDxsGC3pr9NJrnRsyWyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
❤️
حجت کریمی مدیرعامل تراکتور: حالا حکم کمیته انضباطی آمده است آیا واقعا باید خداداد عزیزی را در استادیوم‌ها راه ندهیم؟ آیا این درست است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105841" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=cjJ0urzYsi225sZ7gibTi0YHIRYg1C8uGWy2JtThuJDI-81khlEY0DOj3WX4JKDabJloIRalkIb_3VKHOlIpI6kBYHXAeiyp7zhHeAGNNRHwkKH8RvdJjUkQmz-TOalSSTtiewRwOA_Zw6nKcA13wnXHHfI35t87kzxdCcsmJ8SadZt1ymdGk9y5gonJV0IDNcC2SNFjwz-dl6SHPC2y0cd91oKTu2aXcF-v24zFDBwLHVZ4otuesO6ghZl7pdCed9aS-6rO_bWZVgac-Vv0m6zQQ6c7VmzJICltGFLvreQIIXErKnY9u6xmlfl5mXtsKBHQ-5-SIisV-G0whyZrWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=cjJ0urzYsi225sZ7gibTi0YHIRYg1C8uGWy2JtThuJDI-81khlEY0DOj3WX4JKDabJloIRalkIb_3VKHOlIpI6kBYHXAeiyp7zhHeAGNNRHwkKH8RvdJjUkQmz-TOalSSTtiewRwOA_Zw6nKcA13wnXHHfI35t87kzxdCcsmJ8SadZt1ymdGk9y5gonJV0IDNcC2SNFjwz-dl6SHPC2y0cd91oKTu2aXcF-v24zFDBwLHVZ4otuesO6ghZl7pdCed9aS-6rO_bWZVgac-Vv0m6zQQ6c7VmzJICltGFLvreQIIXErKnY9u6xmlfl5mXtsKBHQ-5-SIisV-G0whyZrWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
گلایه عجیب خلیل‌زاده از حجت کریمی؛
🚨
‼️
چرا به تماشاگرانمان گفتی فحش ندهند!
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105840" target="_blank">📅 00:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=fH8XEFnakdpqyoSflO6CsinJ9N9cK6IqxJYfw8PQp4NwaUg2hXXP4KZv_adR08HnsT2VgHb3lH0l_9iLnqOF0WyUq4YW4fcJXNNsPgdCbpmveL3GsSvw5woGizMraNZ4pjRVWgGIDKL1jYl7yqndWy6UZNo9E_OOHKRHlTwBImgsBGzjJmMWEUaTlwRAbOVzhvhzWE6twXPg6KJlxUUM2vtABLKP5xYMJACANwUgrEnyemlqtTMbT6-pKczOan-MBBEl9oGHrsBSkvNRiUgjxjy6uLY_Sso8uCnOzUliUqsRJdpKjGaV5PNfPl1f0rdjndzBcQd7O21wDYghK5EnOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=fH8XEFnakdpqyoSflO6CsinJ9N9cK6IqxJYfw8PQp4NwaUg2hXXP4KZv_adR08HnsT2VgHb3lH0l_9iLnqOF0WyUq4YW4fcJXNNsPgdCbpmveL3GsSvw5woGizMraNZ4pjRVWgGIDKL1jYl7yqndWy6UZNo9E_OOHKRHlTwBImgsBGzjJmMWEUaTlwRAbOVzhvhzWE6twXPg6KJlxUUM2vtABLKP5xYMJACANwUgrEnyemlqtTMbT6-pKczOan-MBBEl9oGHrsBSkvNRiUgjxjy6uLY_Sso8uCnOzUliUqsRJdpKjGaV5PNfPl1f0rdjndzBcQd7O21wDYghK5EnOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
به‌به آقا مبارک باشه. اولین لحظات بنزین ۱۰ هزار تومانی در ساحت مقدس جمهوری اسلامی
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105839" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: آن کسی که ویس را ضبط کرده است چرا به آبروی طرف مقابل( خداداد) فکر نکرده است؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105838" target="_blank">📅 00:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=E-xIXXZ7XLsXAH1QFCllkK4cS0xiZWvzvAVKC2RwsHKdQa89ujyUlr2_fAbnA2B7IworMGILTqbCPfo7S_gY1jsrQh4A7DgxrJz5clseupmSqy8uN5D_lyTAhCuXYxeJQP0fJInAzS4ZUK1nhIk8Pef_eoU1XB2DhLfqZpxUpKdRSHWlDPQdGCEurs9Ar6ZqSKSheejKdCexdJ8otE2jS_kNYJE7DO3gKeVI8W_w1gdF6AntwzqpVeQxuU9w8NSYs9UhshES5IKfXe7crCPHBkqx6noYap759491hzZf4aAze7PPng9eFrHJ_euIp80mXHQzoOiL1w3lozGkwdh2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=E-xIXXZ7XLsXAH1QFCllkK4cS0xiZWvzvAVKC2RwsHKdQa89ujyUlr2_fAbnA2B7IworMGILTqbCPfo7S_gY1jsrQh4A7DgxrJz5clseupmSqy8uN5D_lyTAhCuXYxeJQP0fJInAzS4ZUK1nhIk8Pef_eoU1XB2DhLfqZpxUpKdRSHWlDPQdGCEurs9Ar6ZqSKSheejKdCexdJ8otE2jS_kNYJE7DO3gKeVI8W_w1gdF6AntwzqpVeQxuU9w8NSYs9UhshES5IKfXe7crCPHBkqx6noYap759491hzZf4aAze7PPng9eFrHJ_euIp80mXHQzoOiL1w3lozGkwdh2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
حجت کریمی مدیرعامل تراکتور:  دیشب بچه ام از من می پرسید بابا قضیه خداداد چیه؟ من نتوانستم جوابش را بدهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105837" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❤️
حجت کریمی مدیرعامل تراکتور: حق نداشتند که آن ویس (فحش های خداداد عزیزی) را پخش و جامعه را ناراحت کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105836" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=R4WPtiGLFXJh_bH-TjRE3OJoOsG_fHnh1q2MnF8gf2up_eOL9t5v9cn9H_nuzl3YFdYqJrTM0meVcH7LbkFx9VBWaMF1qMVSfuqhmJIECWOicYvjZ4Atn-7_J2mvsCnX6eyjmQ3zHaLrPGdJAl-hkMCS1KW1sWoaeuQOfcQbabSdFgpwHmRalte92doSInXUBEDKgwc0XlJSBen3EJYBLCZTp4Sjxh66-jIvc1KiVKrPjh5TgTz3DRrnpqDzjttCWYsuc2yD5fiIFYbQySWTm4Mf6M1FrIT109YuProi0XA-UPiNt9-_cBZhnnzLvWtFded8mS5MVdUGmHGtaBmUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=R4WPtiGLFXJh_bH-TjRE3OJoOsG_fHnh1q2MnF8gf2up_eOL9t5v9cn9H_nuzl3YFdYqJrTM0meVcH7LbkFx9VBWaMF1qMVSfuqhmJIECWOicYvjZ4Atn-7_J2mvsCnX6eyjmQ3zHaLrPGdJAl-hkMCS1KW1sWoaeuQOfcQbabSdFgpwHmRalte92doSInXUBEDKgwc0XlJSBen3EJYBLCZTp4Sjxh66-jIvc1KiVKrPjh5TgTz3DRrnpqDzjttCWYsuc2yD5fiIFYbQySWTm4Mf6M1FrIT109YuProi0XA-UPiNt9-_cBZhnnzLvWtFded8mS5MVdUGmHGtaBmUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
😆
😆
عادل خودشو جر که فحاشی خداداد رو تکرار نکنه بعد همون لحظه واکنش سخنگوی گلگهر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105835" target="_blank">📅 00:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=kwvYsXoLoyfP7JzeMSzJN4EX-qdLOt6ROq1tB2lkxKPG1KCbxNXAKoThKrEzocZcXK_h4YKf-DeQrx5ynNar74YgL-dTQtOxae4DO523o7U8IoSlagTE3caDY7BzSzqMTI8btGcuYySdB7JTc78jYML2sioKDvZAv9t9WEwhYsoCd0Dn9QP8no0brEMdFuGi00PcUkknNPD2Z0IzdpjHiCpmXdTBJNhJU8aeHf9NprPsulmpajbhXOTUpKZOLcgVRkCmodtlBkSzW5hZYu8_ps3OAJZnO9Iqv5DAUh75_KOKy_7RDz4MvjFb_Zi9-t8hcaW38y8-QMJV8ozl7JEosw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=kwvYsXoLoyfP7JzeMSzJN4EX-qdLOt6ROq1tB2lkxKPG1KCbxNXAKoThKrEzocZcXK_h4YKf-DeQrx5ynNar74YgL-dTQtOxae4DO523o7U8IoSlagTE3caDY7BzSzqMTI8btGcuYySdB7JTc78jYML2sioKDvZAv9t9WEwhYsoCd0Dn9QP8no0brEMdFuGi00PcUkknNPD2Z0IzdpjHiCpmXdTBJNhJU8aeHf9NprPsulmpajbhXOTUpKZOLcgVRkCmodtlBkSzW5hZYu8_ps3OAJZnO9Iqv5DAUh75_KOKy_7RDz4MvjFb_Zi9-t8hcaW38y8-QMJV8ozl7JEosw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
❤️
حجت کریمی: اگر خداداد عزیزی فحش داده است حتما یک نفر یک کاری کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105834" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=Tk6Pm_KNvcISZc2eF8YIb4s_twccP79HNSZqPuwgwt8cuV0_1eXwbtpzC064qftFi-JxRs38CbqeaV4PZCvC_g-2xtoaohRZnBfOWTHjla1xuSj9pa6LQ0uny1k5bP47io2OFKBVSrHhmrBZ45x6wTPEsBO0zeU3w28SHLgE-_kADoDQx9FItVQD_3bah2EkBcWhby5YsS5kGghZbAvhV-JTNzC0Gf6q_rpqLQ1RFdo-iaA48y0jduiQtozWD2__nxskxw6RCGEXD5ZnGupj7RKfgApa3FmatI5dXN6PjRHJB6v2EaCz-COkODrrYNr9_8u4JNTe33oDs6BegjmFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=Tk6Pm_KNvcISZc2eF8YIb4s_twccP79HNSZqPuwgwt8cuV0_1eXwbtpzC064qftFi-JxRs38CbqeaV4PZCvC_g-2xtoaohRZnBfOWTHjla1xuSj9pa6LQ0uny1k5bP47io2OFKBVSrHhmrBZ45x6wTPEsBO0zeU3w28SHLgE-_kADoDQx9FItVQD_3bah2EkBcWhby5YsS5kGghZbAvhV-JTNzC0Gf6q_rpqLQ1RFdo-iaA48y0jduiQtozWD2__nxskxw6RCGEXD5ZnGupj7RKfgApa3FmatI5dXN6PjRHJB6v2EaCz-COkODrrYNr9_8u4JNTe33oDs6BegjmFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: به دلیل اتفاقاتی که در تبریز و در بازی با گل گهر افتاد از تمام مردم ایران عذرخواهی می کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105833" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
با استقلال تفاهم‌نامه امضا کرده‌ایم
🇮🇷
چیزی ۱۰۰ درصدی نیست!/ توضیح محمد خلیفه درباره جزئیات تفاهم آلومینیوم با استقلال؛ که حتی خود از بندهایش خبر ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105832" target="_blank">📅 23:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های سخنگوی باشگاه گل‌گهر در خصوص فایل صوتی جنجالی خداداد عزیزی؛ با صدای بلند فحش می‌داد اما کسی از رختکن گل‌گهر بیرون نیامد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105831" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‼️
آدم عارش میاد بگه به فوتبال علاقه‌منده!
مقدمه عادل فردوسی‌پور قبل از مرور پرونده بازی جنجالی ترا‌کتور - گل‌گهر؛ این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105830" target="_blank">📅 23:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=cVxwAGXafU84S3Pj4S2XVbkr6RGpMS6fnF_y1t9bV_S-5op58u0d0Z9R4jGzW4sPjIYL38dMlMy6x0Yx8yPZLjskTdvqpn2koHTQLpAnjtez0Ted8Ik714hFqpBEdP7NdXwUbfOTmXjY7nzA8PCE4iNe9mPP5VKZJZGfcVpewEH77YweW5DOkFmFi4Ci6P2ri_6Pp9dOLg4qDAuSR_Ifr1OVxdHaI_sDSrOOtW2Y04tXF1BV_fKDuXTyXtaR4qCc98WHlvPOf-uG11len3ih8YbgHGyiFl64lgOSc1owQ47S70k2x9sZCSe0NICP9rgZa4es5dyD72ny7xYttS-gcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=cVxwAGXafU84S3Pj4S2XVbkr6RGpMS6fnF_y1t9bV_S-5op58u0d0Z9R4jGzW4sPjIYL38dMlMy6x0Yx8yPZLjskTdvqpn2koHTQLpAnjtez0Ted8Ik714hFqpBEdP7NdXwUbfOTmXjY7nzA8PCE4iNe9mPP5VKZJZGfcVpewEH77YweW5DOkFmFi4Ci6P2ri_6Pp9dOLg4qDAuSR_Ifr1OVxdHaI_sDSrOOtW2Y04tXF1BV_fKDuXTyXtaR4qCc98WHlvPOf-uG11len3ih8YbgHGyiFl64lgOSc1owQ47S70k2x9sZCSe0NICP9rgZa4es5dyD72ny7xYttS-gcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
فولاد خوزستان با گل دقیقه ۹۲ احسان محروقی مقابل فجرسپاسی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105829" target="_blank">📅 22:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=IRqlzK3-URldfVd32Hnzyzwm8wSxlqa-GdJ_YCS2daIA789zjvcAbAfyvu-C60WJU69_uFGGuNQb49ZMYcpaA4TVmjqy-XwJgdup_hU3cJvTt_QpA4wjuR7hhYfH6eS58ysTrCI2Qdt83TlmbiYlKAuUAQTSMzPrLg-A4AdW2e19xrGiltLjtT1KKoVgC7MsPeaIPdOXWt_qIVuY1FUJGLU8TtlhDy0R-Tqk3D-cuPpGMvCa4FPRFkhrbNuWldkkV_RPbFoMh7aO9rvHujbrTAFtZQ0_U1_g5TQX3BPgGz8op8AMROpPPR8BvMv8EbgJTlR4v6EBavVLwAzA3J2gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=IRqlzK3-URldfVd32Hnzyzwm8wSxlqa-GdJ_YCS2daIA789zjvcAbAfyvu-C60WJU69_uFGGuNQb49ZMYcpaA4TVmjqy-XwJgdup_hU3cJvTt_QpA4wjuR7hhYfH6eS58ysTrCI2Qdt83TlmbiYlKAuUAQTSMzPrLg-A4AdW2e19xrGiltLjtT1KKoVgC7MsPeaIPdOXWt_qIVuY1FUJGLU8TtlhDy0R-Tqk3D-cuPpGMvCa4FPRFkhrbNuWldkkV_RPbFoMh7aO9rvHujbrTAFtZQ0_U1_g5TQX3BPgGz8op8AMROpPPR8BvMv8EbgJTlR4v6EBavVLwAzA3J2gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
واکنش کنعانی زادگان، بازیکن پرسپولیس در مورد حواشی دربی و ضربه اش به عارف آقاسی:
در فوتبال اتفاقات زیاد می افتد/ نمی خواهم به کسی توهین کنم و یا ضربه بزنم/ شما دنبال این هستید که حرفی زده شود/ هیچ کسی مشکلی ندارد و همه را دوست داریم و به همه احترام می گذاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105828" target="_blank">📅 21:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82451c129.mp4?token=tpBGsUB0jcrctbto8bVxTfl2JmCr2Gl86MAO0CwkYlTsiuT5vLzhFlpkwMsrUvkZbvIlqx9YBZrsp0xtUxk-0-nw1on_dFHJZvVXeGBY3oYV0B_hUU9rjJejBS-bBlPbNHpLXbS2nPunovpMYx5CntIIPCQssuZoCXoDGIC24cksnsmqKSmfv02uFCNhSYtXC63zXz8EHVPmHN6pdPqgV75GRBprHfvPC_pb0CLalBtf_rt7CzSVBL-b-pREvRdGnhjVzqtrxEriGHztBX1sjhc5-uWGfunrnqlqyLeiA7bOmDgwnqDwxbncQjhDREK4OttKFTaAHSfgwzHTCGvjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82451c129.mp4?token=tpBGsUB0jcrctbto8bVxTfl2JmCr2Gl86MAO0CwkYlTsiuT5vLzhFlpkwMsrUvkZbvIlqx9YBZrsp0xtUxk-0-nw1on_dFHJZvVXeGBY3oYV0B_hUU9rjJejBS-bBlPbNHpLXbS2nPunovpMYx5CntIIPCQssuZoCXoDGIC24cksnsmqKSmfv02uFCNhSYtXC63zXz8EHVPmHN6pdPqgV75GRBprHfvPC_pb0CLalBtf_rt7CzSVBL-b-pREvRdGnhjVzqtrxEriGHztBX1sjhc5-uWGfunrnqlqyLeiA7bOmDgwnqDwxbncQjhDREK4OttKFTaAHSfgwzHTCGvjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
❤️
کنعانی زادگان: بازی امروز خیلی سخت تر از بازی با استقلال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105827" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=DXlsGN_3eMpmV8I21v83YIx1UHUozyF-F1WQruuN64vnHAD-EYWrf9n67NLfDaynFG6hlPFxQzWNKrCZYNcOxsEMHVK-H8WcF5Dd9_hzx9DKJGNrQekRyYJFXJKyIkYNBXTYSBCM13ZS9LhIsGfd0IlBZWL7t9eyhEf3tb3c87Ih_bv3pOhFiUsMARGdaTo1UdVpXX-Bu4_wskhkcC0rw1rwyEyzW0SlW_T6eWI_xOCxo30WkaSoZcnlsvHCmUDJYmGHtixb2xxMCDB6HMUYPOOIn69km-mxWvMRsTiBhzFFnGHNawMg_Uc0rmOTEey_bl8pSqDQ60hpa-jcI_T91g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=DXlsGN_3eMpmV8I21v83YIx1UHUozyF-F1WQruuN64vnHAD-EYWrf9n67NLfDaynFG6hlPFxQzWNKrCZYNcOxsEMHVK-H8WcF5Dd9_hzx9DKJGNrQekRyYJFXJKyIkYNBXTYSBCM13ZS9LhIsGfd0IlBZWL7t9eyhEf3tb3c87Ih_bv3pOhFiUsMARGdaTo1UdVpXX-Bu4_wskhkcC0rw1rwyEyzW0SlW_T6eWI_xOCxo30WkaSoZcnlsvHCmUDJYmGHtixb2xxMCDB6HMUYPOOIn69km-mxWvMRsTiBhzFFnGHNawMg_Uc0rmOTEey_bl8pSqDQ60hpa-jcI_T91g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😢
🇮🇷
واکنش جالب هوادار پرسپولیس به عملکرد تیم
:
بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل می زنیم 3 تا به رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105826" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پیمان حدادی، مدیرعامل پرسپولیس:
🔴
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105825" target="_blank">📅 21:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBHCjdZ1kUbb-GR2Qjrn2OKy7ytv7MkTdPpJIhdmFLQxYzP8v3eno7GVWXOlFWhR2NiGIXwFw3fj7U0AF7jzbqOuxIgi7cRFcOCiSv8DxSevrNEQD3v63DYZt1g03ugsYPkf0tSseEC_xL7USSm_etZl6QLAdeLyPSTXU5NWbqLiybEwlrg2CU0OWtS41LHCaHCfeTwzhWQSBzaJe_X5Ufi82PEFcSmlMyQM0FW70hgDhXlWBe5qVQpi6VPUjvp-pjfb51Lpfs3pBv4ljYa2I0xjqA_UOfFhNTaOQ6zE7YNoj60dKRLzGHazU-1zwIvvf_Pxg0U5DOLRUXA6c6BLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
عبدالله ویسی، سرمربی ذوب‌آهن پس از دیدار امروز مقابل پرسپولیس از سمت خود استعفا کرد. ذوب‌آهن با کسب ۶ امتیاز از ۶ بازی در رده سیزدهم جدول لیگ برتر قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105824" target="_blank">📅 21:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105823">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jay9ZM3LGuEdX7_c9_AgVsuVlH8fCDL63lhCUMfi_pm2woZzrx1hvHqqtRZQNZPTlVKYj2UE9tyhXs7V45cz8itID3KzRb2RDcPx1c44_kWmhWlVAT4sWJFTzk3JWmQNYQgriV7RRGr7zALuia4tL7indePYbPAzRyEno5f_uS4A19zwY6P0ibbdF3TtR3BAKBozpY2d-m3rVVXLKoFLTL-V0Dsl_5OShMJEWyRReNDk4pLuwA048kYsmuAUnbMJyzl0-fkevG53-Kt-v0Zs2kkeKfTOq0ACJtw8vZGXpwc31K39HUjkuA7z3vowEES8PAbY6oaBiTqWRbyq2l7Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105823" target="_blank">📅 21:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S83MfD99Hx3sHLVWMkfg5muAVYf3OTSfiqt_OZvaG_VVHxiq5tW0yy0ziT3joJibMABIorzuWMNydXfpV_ZxuwrfP-33D_6yx92prm2RYzzJ9xAOs79j7uzi1hYqvoIXE2BJ9LeCJTHcTQlNFsn1C4Iv2XMh1hMr2j7MLUnNj-W_m3D-wRgdzfg8Oogi0s7x11x0Rk_G0g2Zqhvlh2pe6l7NAhnmgNCeUlO8APR3IaE09IRDXh3XFvsH1HspBQAWwRGyoqFFSvXyb2HcxcYLK1-C_ZcKVSSVfKl5M7FAqhDdge6RoVPpWe6KHE71H-MpFT4K7NVLBtf3RRQrL2dbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105822" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105821">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=mf7jLXnWxqOEV3FnXwDSIaXMKzYLJq3choijuAkUoiUab8bPIlJgIHFZsKj11qm0TYZCZILgfkipbjIP2FkAdmegHzGHGXMaVYV4DN9vxoJhj_nfVs5rdgzgIZDfCOiSH4pzUFKUuedAGg32xh7F4pCyfgSPGVnSbSvT0e6NEn97azXn8iGwGU3QnlDN_cxgb3Uu2H4byxwyzt4pkKgabLc9Jcy4n1b9fqwHrA9i4rgFoQ-NvuHGcelWwmEE7z1HFFLbXPpq62kQOxv7opx9OzxZaGWmxTp5V083aoRN_rqQEXZHJ_Kh8gHKrmH5dFSTww0m8G4m6lfRBqDdThfrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=mf7jLXnWxqOEV3FnXwDSIaXMKzYLJq3choijuAkUoiUab8bPIlJgIHFZsKj11qm0TYZCZILgfkipbjIP2FkAdmegHzGHGXMaVYV4DN9vxoJhj_nfVs5rdgzgIZDfCOiSH4pzUFKUuedAGg32xh7F4pCyfgSPGVnSbSvT0e6NEn97azXn8iGwGU3QnlDN_cxgb3Uu2H4byxwyzt4pkKgabLc9Jcy4n1b9fqwHrA9i4rgFoQ-NvuHGcelWwmEE7z1HFFLbXPpq62kQOxv7opx9OzxZaGWmxTp5V083aoRN_rqQEXZHJ_Kh8gHKrmH5dFSTww0m8G4m6lfRBqDdThfrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از مشخص شدن محرومیت 4 ماهه خداداد عزیزی، پرسپولیسیا این شکلی عالیشاه رو تشویق کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105821" target="_blank">📅 20:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=BVIGLLtkUS3QgJn6hPi4HqW60hc9OibdEpWXDFW9-9OTKN_5DGADLoi2VIFynT6G2FHUdzH2PfMlV9o14lkJaS6zuhKaBlMtHS8g4a8xRCCt_I3upIy_BxfJAMAnubz6boETTP1I65rS_5h42FBa_JzNhcHn5ZD48vwCYZVZ8JOXChgD0jZntKwo5XL3ROjtANDzChmFti3-W-mg6mlncmHx8BSdpxBep7LsWuTVclZrFJFxOA0E7daqdCNhM6WHE1HNejM2VvGc8YoWmczw2clCKFdHNUQeB1p3cq9DET-qJAbp317WxiVpBE4HWNpFrNIior2rd51AuQTtSoFZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=BVIGLLtkUS3QgJn6hPi4HqW60hc9OibdEpWXDFW9-9OTKN_5DGADLoi2VIFynT6G2FHUdzH2PfMlV9o14lkJaS6zuhKaBlMtHS8g4a8xRCCt_I3upIy_BxfJAMAnubz6boETTP1I65rS_5h42FBa_JzNhcHn5ZD48vwCYZVZ8JOXChgD0jZntKwo5XL3ROjtANDzChmFti3-W-mg6mlncmHx8BSdpxBep7LsWuTVclZrFJFxOA0E7daqdCNhM6WHE1HNejM2VvGc8YoWmczw2clCKFdHNUQeB1p3cq9DET-qJAbp317WxiVpBE4HWNpFrNIior2rd51AuQTtSoFZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی
64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105820" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105819" target="_blank">📅 20:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkmP7R5s41ahk01KrxiE4gsG8MFG1EDsegoK9s_WZW8hF128ZSrM9_23xGz9Pr3K6UtPTJba7nQvP6LOtcHHRXKcl0sFLjgjaQKwfKdAwGsz9nlpIFHiHKBhN-j44Sc0XegEnSeoLCQoEGgCg2WJZkIavvjCxH_ex8uKEKUTzI9VxC-_OVnjWMCIa5RWIlERoOnMc4hN8qLi_7Sow_lQvrBIMeCwxuv6LDux-rEx_SFqIb-aerud0Tk1OsUcz8zV8CCWg-E0rcrFFngC51cxJgJ4vXJCFdxlkBXyYX7L73mw4_k7rUwwZ5c756UFfe8tYrG22jJfdOh5bC--xEO3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105818" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105817">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=oOEXo43T2x0xUy8a6VbitCPsjv_kLIKMRDx5IWSnEehtAAtGGOU_0IxnioChZZ-I55l8liScfIv2kR_r_OB8dCyYPFfU3T9sSinKhcGzAS4LJPrU1N6EMUZXT1BkFYSoe8_Yy4yTXGHzcC7nV8YgLaKeuor-xo_F5OxZeP0AFgjkb9eI-KWrOD_GEHQ37Fp-QtGGR6vgsSrU5lvlDy939NgqSpaXl9H1IG0dMIun41-HdahfloabSlBN7mfwi0f0z7BW2oSbgpRRtu01zjK834RLsh3gieHJYWGzxvJGLZBB8eARCVUPaIHMGYABNfCINQ1lA7_bbg7PjO9AVMqEJFo5zyyYRVcWPj5OQ2W2d5bW8KgJyM1zWNw2zlEivE4dC2nGo028vWJo7FG-wBub0vqDfgbMcAG-ORHDheK_rBGWAZAx-FPi1uTNTK4VPv6chRMG8VZJnNI1JqxuONmvROgNk1bzSP25fVx7GSnMhJ0LD2SvvIminXVMx6O3cSUoLklZD1iLom55cCmebnnuNbNA7iBKqZAYjRfzNr96B7eBWExpgS-kdxF49uK12xN_Evb52GYGmXGqtcN63P-cdDwwElIk0p6DKAGtQmclsP8hCmKDi_UO71mwv0ZxoTLNTOO5gLo63YGz5zZ1JRudXH427da2l6DrydeJHT8b2oI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=oOEXo43T2x0xUy8a6VbitCPsjv_kLIKMRDx5IWSnEehtAAtGGOU_0IxnioChZZ-I55l8liScfIv2kR_r_OB8dCyYPFfU3T9sSinKhcGzAS4LJPrU1N6EMUZXT1BkFYSoe8_Yy4yTXGHzcC7nV8YgLaKeuor-xo_F5OxZeP0AFgjkb9eI-KWrOD_GEHQ37Fp-QtGGR6vgsSrU5lvlDy939NgqSpaXl9H1IG0dMIun41-HdahfloabSlBN7mfwi0f0z7BW2oSbgpRRtu01zjK834RLsh3gieHJYWGzxvJGLZBB8eARCVUPaIHMGYABNfCINQ1lA7_bbg7PjO9AVMqEJFo5zyyYRVcWPj5OQ2W2d5bW8KgJyM1zWNw2zlEivE4dC2nGo028vWJo7FG-wBub0vqDfgbMcAG-ORHDheK_rBGWAZAx-FPi1uTNTK4VPv6chRMG8VZJnNI1JqxuONmvROgNk1bzSP25fVx7GSnMhJ0LD2SvvIminXVMx6O3cSUoLklZD1iLom55cCmebnnuNbNA7iBKqZAYjRfzNr96B7eBWExpgS-kdxF49uK12xN_Evb52GYGmXGqtcN63P-cdDwwElIk0p6DKAGtQmclsP8hCmKDi_UO71mwv0ZxoTLNTOO5gLo63YGz5zZ1JRudXH427da2l6DrydeJHT8b2oI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به ذوب آهن توسط علیپور(43)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105817" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105816">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بالاخره پرسپولیس زدددددددد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105816" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105815">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علیپووووووووور</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105815" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105814">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105814" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105813">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=ncR2gUUl6pjfRDAvoGxdAskVrmrhBtPydMFYfQdhga4-cpJnbd7_3Rn090KbIi3F1TAE9Ql1Hpsua8WxQ5xENHc9isbtLHVMLV2q6pAEQq5mz2PlWeB2wJ-cqFjoW7U028EpxgefBnJ6ge7ZnAqts6JyxVpEGWbVgdk6LgmEEylQ6tZv47UQIEWeMZbDvZCfA45_oZWjk0Itw5yRbCtYQrrIzuxze6VsBFGHADA6HKAeRxw191OwBiLdxZI7MzqTEZqlLq6SWNrVYUDg3LWxUAcfFavOmzC1zTyI2NMJ4Zikrm3tv94rrLwU_PQUNkIXT5JtNotb0cmTE2ge6ApSFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=ncR2gUUl6pjfRDAvoGxdAskVrmrhBtPydMFYfQdhga4-cpJnbd7_3Rn090KbIi3F1TAE9Ql1Hpsua8WxQ5xENHc9isbtLHVMLV2q6pAEQq5mz2PlWeB2wJ-cqFjoW7U028EpxgefBnJ6ge7ZnAqts6JyxVpEGWbVgdk6LgmEEylQ6tZv47UQIEWeMZbDvZCfA45_oZWjk0Itw5yRbCtYQrrIzuxze6VsBFGHADA6HKAeRxw191OwBiLdxZI7MzqTEZqlLq6SWNrVYUDg3LWxUAcfFavOmzC1zTyI2NMJ4Zikrm3tv94rrLwU_PQUNkIXT5JtNotb0cmTE2ge6ApSFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جالب عبدالله ویسی به خراب شدن موقعیت گلزنی تیمش مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105813" target="_blank">📅 19:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105812">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=tfJK2B7RNFdyOwt-DNKZss281_xkmN2hPcN_Z-NV6vGFknpxUen4wBU3wnKQiPydxy5Q_hX9TsQ5zDVZHy7aZ1CIOb6zUNXMHo70uI25GFRHGk3KZXib4sew95PKgKNSK9AilVQxBhoNhNb3rwQ0JObLu0hZJB7cZP0BuXB_lp68rHWqoA4SzFLB5GO_5CToTE5Wrbgh4Yr1MUU5lIsE8AHMQKG_qOzAeztDXSuuU3aPC4UDsqCRs7BVRJdTbrJZPpTRUnVsaSQ06bbE7fvH2z1-kTD_tg6QL1viYxqSPHlNtu7pNDbb4dysytDlTTTx00TsrNZN-No2Q6hcaxgvqhdmNe6OpZ8o6u9koLWl7gidfj3Cn2NiSis0C0HtjvPGowytAsuN-8Sbc-Bxi8WE14c7opHFxiEaZ7m1QSiJfMgsYk1OkYKx_VI9xzhBiAtm-3HjoB1yvoAYhtH1REZgsR-aekmY0lTnr4Bus1a9EhapLLBmpcJyz_uotuTgBY3Kj9RqkT8KyBgcfr1PMxlm2cQrYuvTKjqULZ2TJJJdcc30w_qZfaTA3wUb7smzWUoFVWum4QEwpOaj09fNzu8zJmK_4YRMFTjVraHvihir1mcKmIeTH5IE_zOnY3O2K6TjPqRACuoUXfhMHQawc1qTjui33kIKEPDL6_QekrgAMfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=tfJK2B7RNFdyOwt-DNKZss281_xkmN2hPcN_Z-NV6vGFknpxUen4wBU3wnKQiPydxy5Q_hX9TsQ5zDVZHy7aZ1CIOb6zUNXMHo70uI25GFRHGk3KZXib4sew95PKgKNSK9AilVQxBhoNhNb3rwQ0JObLu0hZJB7cZP0BuXB_lp68rHWqoA4SzFLB5GO_5CToTE5Wrbgh4Yr1MUU5lIsE8AHMQKG_qOzAeztDXSuuU3aPC4UDsqCRs7BVRJdTbrJZPpTRUnVsaSQ06bbE7fvH2z1-kTD_tg6QL1viYxqSPHlNtu7pNDbb4dysytDlTTTx00TsrNZN-No2Q6hcaxgvqhdmNe6OpZ8o6u9koLWl7gidfj3Cn2NiSis0C0HtjvPGowytAsuN-8Sbc-Bxi8WE14c7opHFxiEaZ7m1QSiJfMgsYk1OkYKx_VI9xzhBiAtm-3HjoB1yvoAYhtH1REZgsR-aekmY0lTnr4Bus1a9EhapLLBmpcJyz_uotuTgBY3Kj9RqkT8KyBgcfr1PMxlm2cQrYuvTKjqULZ2TJJJdcc30w_qZfaTA3wUb7smzWUoFVWum4QEwpOaj09fNzu8zJmK_4YRMFTjVraHvihir1mcKmIeTH5IE_zOnY3O2K6TjPqRACuoUXfhMHQawc1qTjui33kIKEPDL6_QekrgAMfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب رحمان جعفری مقابل دروازه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105812" target="_blank">📅 19:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105811">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dXvQ7D4uMdbSNNh_1m9bV1pZMUsd4j_EO49m0fih2hud0nMQkggH6uiiOz-ZyPrK3yZjHC7TxDbc3XiobU470pRcv_JNnJ6mEZtimiFSFsAHtqlpDoZv42-8-jbJfcQH1u92LmA1nhGZXYLbub0fgGilQL_61Z3fsw5UnuNcKinLt-xJN4RMnr04YKl3iVZP5j-MtkayCVjqcnONudNvKhONlagMBICdVcRlvAraaZ4YFOMUBmTP_5BIc9UZ53a3Irw9rKfSa24NqbeUqVsZeZVVSKDMr5Qggqrsa6nwhsqAzaQvS8MIS8dH2e5o5iTH6vZwjAXm67DWNy9cD7DaY28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dXvQ7D4uMdbSNNh_1m9bV1pZMUsd4j_EO49m0fih2hud0nMQkggH6uiiOz-ZyPrK3yZjHC7TxDbc3XiobU470pRcv_JNnJ6mEZtimiFSFsAHtqlpDoZv42-8-jbJfcQH1u92LmA1nhGZXYLbub0fgGilQL_61Z3fsw5UnuNcKinLt-xJN4RMnr04YKl3iVZP5j-MtkayCVjqcnONudNvKhONlagMBICdVcRlvAraaZ4YFOMUBmTP_5BIc9UZ53a3Irw9rKfSa24NqbeUqVsZeZVVSKDMr5Qggqrsa6nwhsqAzaQvS8MIS8dH2e5o5iTH6vZwjAXm67DWNy9cD7DaY28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
عایشه‌گل جوشکن، بازیگر و خواننده ترک، در گفت‌وگو با مجید واشقانی در برنامه «رُک» از ماجرای آشنایی و ازدواجش با همسر ایرانی‌اش گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105811" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbHei7HUw4ZJkYS17Cz-aSbQaDeNvu6Rol8mD3AR4FgrtVlnGQvzDQafguTkqCSdeEiD2NWqOVbnpgSmeofGKAOTAlZ3Y5AszUDs50a6zJpC4iKzW24O0NCM4wwVROAX0xuEX2xXo_Ltk5Sp3qwmin7RG-zxkZgWeIV7HS-0cO_wmEaMrmU5rKn907Fc80MHVkB3u0oED-n22RQ-YVwAnCtFPzs621pIdvm8YQQflNOMcbYZwt8IABr-01hObzQriLnMf_tKQLwXB6iA4eA3FbC9Xn5E3lI0RV5uCQyI4_KS-cZhd_YXpaLzTv4RcSbM3GafdfFkWXWQ2fCyF3ej9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
اگر حق رای دادن را داشتید، به چه کسی برای جایزه توپ طلایی رای می‌دادید؟
🎙
کیلیان امباپه:
🔴
من برای خودم برای جایزه توپ طلایی رای می‌دهم. این یک جایزه فردی است و باید دید که بازیکن در سطح فردی چه دستاوردهایی داشته است.
🔴
برخی می‌گویند که من یک فصل بی‌نتیجه داشتم، اما من هرگز برنده توپ طلایی را ندیده‌ام که تمام معیارها را داشته باشد. آیا بازیکنی وجود داشته که به طور یکپارچه توپ طلایی را برنده شده باشد؟ نه. این بدان معناست که همیشه کسانی هستند که فکر می‌کنند بازیکن شایسته آن نیست.
🔴
اینکه من بهترین گلزن تاریخ جام جهانی هستم، چیزی است که در ذهن مردم باقی می‌ماند. اینکه من بهترین گلزن تمام تورنمنت‌های بزرگ هستم، جایی که بهترین بازیکنان بازی می‌کنند، لیگ قهرمانان اروپا، جام جهانی، نمی‌دانم آیا کسی قبلاً این کار را انجام داده است یا خیر.
🔴
من کسانی را که با من مخالف هستند درک می‌کنم، زیرا این یک دیکتاتوری نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105809" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=pGn28mw8NiZ_P-GqIi94VJvo6iYcJWCZII8opnwEeTGcCe5ZxXGKxXikWd7Os_ZeCsQS3W7aKbfz7IWLPtcUc8ApKvakjAdeHwD-aCgQmoEaW-3qCfpY7oCr5kPXLzFoNZV0ELjcmMgpTf7qyhwDIU6nc61oVvaZozX3qCFH2TE0cY9AXSEGze_rJb35FUDeqcF1ELu5IuJPuV12QgbOGwl_XRp2o1GcbqOgbtw_httZvowKWxRc8AwvTyeluPALfkwLSDTa__elUGcK8HCXZHY2D-KtHNfkgSgbWecG9q54CTIs72gILVc8RS1G5GU_DTaOM5PzyoQuIrP7jpyZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=pGn28mw8NiZ_P-GqIi94VJvo6iYcJWCZII8opnwEeTGcCe5ZxXGKxXikWd7Os_ZeCsQS3W7aKbfz7IWLPtcUc8ApKvakjAdeHwD-aCgQmoEaW-3qCfpY7oCr5kPXLzFoNZV0ELjcmMgpTf7qyhwDIU6nc61oVvaZozX3qCFH2TE0cY9AXSEGze_rJb35FUDeqcF1ELu5IuJPuV12QgbOGwl_XRp2o1GcbqOgbtw_httZvowKWxRc8AwvTyeluPALfkwLSDTa__elUGcK8HCXZHY2D-KtHNfkgSgbWecG9q54CTIs72gILVc8RS1G5GU_DTaOM5PzyoQuIrP7jpyZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
بازشدن پرچم 6 از سوی هواداران پرسپولیس و کری برای استقلالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105808" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=G4wV3koG7cD6y0FX3quXUItmkp_8KXTQw0zMTUSkN6zt2E6SIP0anIvGnd-Gx36b1lo1eFcbgrlIrSCBz2QlGx59L2UsmfYYkM27_YO6_cOkhPZr4sY887O0BhwNldUgnFlzChVA6_NpcjzetJ2Q3GRWSISIreNFKsx1q2lRst2Ax1y9TDg3FXUGEAslM81bBWYXX64r3S1n7eTEiuEzzFGcuRoV901Um1HDSnqh6mPFb9t3wCE9s27hSsJQVL8d6Frt4p3-MoY-1PEzwY71LLz1k8hRwzKaXDuPteFeUoaMeM8QWBJfZlfx-Cr5XZABUf5xBv53ONSbOPdJuSy0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=G4wV3koG7cD6y0FX3quXUItmkp_8KXTQw0zMTUSkN6zt2E6SIP0anIvGnd-Gx36b1lo1eFcbgrlIrSCBz2QlGx59L2UsmfYYkM27_YO6_cOkhPZr4sY887O0BhwNldUgnFlzChVA6_NpcjzetJ2Q3GRWSISIreNFKsx1q2lRst2Ax1y9TDg3FXUGEAslM81bBWYXX64r3S1n7eTEiuEzzFGcuRoV901Um1HDSnqh6mPFb9t3wCE9s27hSsJQVL8d6Frt4p3-MoY-1PEzwY71LLz1k8hRwzKaXDuPteFeUoaMeM8QWBJfZlfx-Cr5XZABUf5xBv53ONSbOPdJuSy0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105807" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADYqthiQVyk0CDb_Pw2q13WgFkl_dKg-YimDKHS7Q_NF6C3hbJLL31x9t2zzjyIxjwhBIfo8KvXgxor7e5qJCcXmApGcO-eO70RgVaBwombc9LJBwozK2xmJB4ORqvFYt9vcRqDTmIUMEp8_vpG1_MT4cepvVMmc68FVnF8hCpIlXwjuq5QKiT-Qhuo-Q1l6BZGtjjZlLNrx68pQjX8-ffv6sScplCxq7KhNrBzJHZFyJdtXit_jn6znRZAt5YmkGlOIjrWogw0ia99tN8GnRjoiufmE4v-P7-mdfsxjow6yYp7jzVSIe1b_jzG0JqqD8juFgGeEqAqGyZO_bCR8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
شماتیک ترکیب پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105804" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66914acac.mp4?token=GdJatZdZK4Mj6vZ3JNQIAYgWHjpXiaQ0OSY5b5AKxZDHZWyzb1mzVh2AZJ0WdfwuEL9zXtx3_yRv4nzneLm0kjR4prTipXPLT4O0d986OV20hfDhMHif1nfZTJFukV_XgfERgxL74aema0kVFmt04mzEHVa6N3Ydhe-1ib2VrHgerXN7MLppUdGaDgNNIu7faLoPon-hrm95Zo40gvxJrjlkqBz2xhx5HGYCAtTiSQmKLBEgn-Avmf_EBFebYvkV_bhkhmqqfEY_6FswLJ9qu52OKIQ1lVwkD0B8h86b1otFQgFVVgv3WmIOcp-lo5rci07Y6JZLbSPooa1gSkErQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66914acac.mp4?token=GdJatZdZK4Mj6vZ3JNQIAYgWHjpXiaQ0OSY5b5AKxZDHZWyzb1mzVh2AZJ0WdfwuEL9zXtx3_yRv4nzneLm0kjR4prTipXPLT4O0d986OV20hfDhMHif1nfZTJFukV_XgfERgxL74aema0kVFmt04mzEHVa6N3Ydhe-1ib2VrHgerXN7MLppUdGaDgNNIu7faLoPon-hrm95Zo40gvxJrjlkqBz2xhx5HGYCAtTiSQmKLBEgn-Avmf_EBFebYvkV_bhkhmqqfEY_6FswLJ9qu52OKIQ1lVwkD0B8h86b1otFQgFVVgv3WmIOcp-lo5rci07Y6JZLbSPooa1gSkErQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇺
🇪🇸
خولیان آلوارز در مراسم عکاسی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105803" target="_blank">📅 17:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=DexNvsJ2qZROh6G_xTrHoYOsN2sbQgbhkzPgHsyShQcID22_owraMWL4AVGHPtvMRUXGt0g8HVnVjfxFOrCYskrPYUIjVn_KyDxZ5NqdRbEx-dNTH7h9mmoS7hEd9ACtS6kUZoMAcpnkexWE0MXd0G5Gblc3ubnT2ya15TBGyGwiCYelxidEcRrGQYRgHoFvhVgtNqrvmDtfJFnCY1fBIRQYYltfpaEpTVCwuRB-KY8_Z6UrkQrNyIPJ9hB9YLDU90v9RWK54ZdDqxg61p7GILvpW6tVsP9g3aHwOUY035i8A6akJpk_LBDxGS5HD18zBeLgz0xKlG4p3NwERsemTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=DexNvsJ2qZROh6G_xTrHoYOsN2sbQgbhkzPgHsyShQcID22_owraMWL4AVGHPtvMRUXGt0g8HVnVjfxFOrCYskrPYUIjVn_KyDxZ5NqdRbEx-dNTH7h9mmoS7hEd9ACtS6kUZoMAcpnkexWE0MXd0G5Gblc3ubnT2ya15TBGyGwiCYelxidEcRrGQYRgHoFvhVgtNqrvmDtfJFnCY1fBIRQYYltfpaEpTVCwuRB-KY8_Z6UrkQrNyIPJ9hB9YLDU90v9RWK54ZdDqxg61p7GILvpW6tVsP9g3aHwOUY035i8A6akJpk_LBDxGS5HD18zBeLgz0xKlG4p3NwERsemTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
پژمان ماندگاری مدیر رسانه ای استقلال: با صالح حردانی در ارتباط هستیم هم من هم باشگاه، ولی باید زمان بگذرد تا اتفاقی که بین باشگاه و حردانی افتاده است حل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105802" target="_blank">📅 17:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=PSESBBx8ES8il2PYaot04IQmb7BRsFSbBdxd8sXADk6VMZwLe4C95Kk0NizkdTH2U2dYUCvR5u0JlWRrvTCJ1X0amSI2qsoP_LzXOwhlQtDK_xRuvRHzRetrLNc3Fzo99W7N3nOEUseO6Sv5iSZKXnr70eeEUrQ73SP9jGmrBXWdL6MokFoy-qIoSXV19kUVkCyEZtZrXEJSovRbE1qZWABNaL_hTUOV899kveMYTbYAS89N5v2mZIiLgjBHtuAmSAjeonb1y_ATYJRcltV0OEu8DtYVEmBEjumRphGLboZPmzJVk-8CdVMaYWAwk9d8ebXsnWuNboljv8BeNbcUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=PSESBBx8ES8il2PYaot04IQmb7BRsFSbBdxd8sXADk6VMZwLe4C95Kk0NizkdTH2U2dYUCvR5u0JlWRrvTCJ1X0amSI2qsoP_LzXOwhlQtDK_xRuvRHzRetrLNc3Fzo99W7N3nOEUseO6Sv5iSZKXnr70eeEUrQ73SP9jGmrBXWdL6MokFoy-qIoSXV19kUVkCyEZtZrXEJSovRbE1qZWABNaL_hTUOV899kveMYTbYAS89N5v2mZIiLgjBHtuAmSAjeonb1y_ATYJRcltV0OEu8DtYVEmBEjumRphGLboZPmzJVk-8CdVMaYWAwk9d8ebXsnWuNboljv8BeNbcUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
پژمان ماندگاری مدیر رسانه ای استقلال: در خصوص ماندن یا بازگشت صالح حردانی جلساتی در حال برگزاری است اجازه دهید خود سهراب بختیاری زاده در این خصوص تصمیم نهایی را بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105801" target="_blank">📅 17:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=VPXxn6EV5KGCBkb9fXmPi_6D-cr6DJgPypIaVoDhRnlZMsx8FUbp2faqnq-M0Ioo220q1nTAPd84fSxUDbWzY46pPgBDjBLUf5SBm3DpOIlxKrN-06LJ9Nj7Ky5j3Bi-g0iIqpzUt60rILZE9vKheUaYbPIuiCxPKuHtT30QqdtjJ7FfERmcJeHEooaEu7zlZLOZkx4TeFcL5ZkRaXQpswWkTp8shWVjWOaqJa8IVdTFjMOib5P4Ka8t2KEmuXTb0AZ58fLD29u1ejmRR2qV-SMg39DDLLoKbhmfVbjkzTaSnZg89H71iz-weFwDLqMe6PTiUDEbHow7mbFgo3MZuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=VPXxn6EV5KGCBkb9fXmPi_6D-cr6DJgPypIaVoDhRnlZMsx8FUbp2faqnq-M0Ioo220q1nTAPd84fSxUDbWzY46pPgBDjBLUf5SBm3DpOIlxKrN-06LJ9Nj7Ky5j3Bi-g0iIqpzUt60rILZE9vKheUaYbPIuiCxPKuHtT30QqdtjJ7FfERmcJeHEooaEu7zlZLOZkx4TeFcL5ZkRaXQpswWkTp8shWVjWOaqJa8IVdTFjMOib5P4Ka8t2KEmuXTb0AZ58fLD29u1ejmRR2qV-SMg39DDLLoKbhmfVbjkzTaSnZg89H71iz-weFwDLqMe6PTiUDEbHow7mbFgo3MZuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پژمان ماندگاری مدیر رسانه ای استقلال:
🔺
مصاحبه پخش شده از بهاروند در خصوص قهرمان لیگ تقطیع شده بود/ آخر مصاحبه می گوید که هیئت رئیسه فدراسیون فوتبال می تواند دوباره در خصوص موضوع قهرمانی لیگ بررسی های لازم را به عمل آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105800" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=TwBFLdn3XbCXtcNs3NZOQxixMiYQJNRudIDyC5vqQoFaoXERzde1nkXgjLMhjsFyCEOmS0bZ0Dg3mekYhL5ONp29KKESF3gYRs2OR6EWgM3dmxGPe0vqbimYPz8kInmkThIwVBMN_GUYt0XKALOh9O5B9WvIC7xYG2lLATMWBUCv1E4pHSt1w97mDxvxSkqgLWAwI2PREFVSdsffIkpEvuhTn9C_7aNTxHrn17PjZkbGqwrGugkyYLM8sKakppdN3c4lr0YFzq9Ao9tdZeVrntPjLLWb3TO_u4ES-GQxCUixh_M6vZ4fm1SvA4MhuO28mfvjUqYz_6HxGaXuYvte0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=TwBFLdn3XbCXtcNs3NZOQxixMiYQJNRudIDyC5vqQoFaoXERzde1nkXgjLMhjsFyCEOmS0bZ0Dg3mekYhL5ONp29KKESF3gYRs2OR6EWgM3dmxGPe0vqbimYPz8kInmkThIwVBMN_GUYt0XKALOh9O5B9WvIC7xYG2lLATMWBUCv1E4pHSt1w97mDxvxSkqgLWAwI2PREFVSdsffIkpEvuhTn9C_7aNTxHrn17PjZkbGqwrGugkyYLM8sKakppdN3c4lr0YFzq9Ao9tdZeVrntPjLLWb3TO_u4ES-GQxCUixh_M6vZ4fm1SvA4MhuO28mfvjUqYz_6HxGaXuYvte0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس
: ای کاش خداداد عزیزی سُر می‌خورد و آن گل را نمی‌زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105799" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=toXRr3plm7O3AcQEYUV75p8QqWPSifcgu4ZIiJM_yAd-Lj2jy84bqDorAqB4b4rsicdMyxKEF7k1M7Lp-jrknXZWxcxvUdr00u4PD4krGKpQs_HmkXpaGLoiPU-Utt6jmhBVwJNudm0--FsnRshQ8312itUzXiPj3beQpwf9L-cVe9f4QIFt7h0jmW3B9lLJA_HJsl8S5-BnlF6Vxv8C1psJNKMFd3k_REcg6fAnGnLKa1DUkW3woJtoY67cUiC8E4OwLi1Id7Hmfvt9ExJnQ26kDOpM3Mo9t96ZqRvbStbmEOECC_gankDZ2Hm50oZ2X71sGhgWTH3uDDoI2qcREQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=toXRr3plm7O3AcQEYUV75p8QqWPSifcgu4ZIiJM_yAd-Lj2jy84bqDorAqB4b4rsicdMyxKEF7k1M7Lp-jrknXZWxcxvUdr00u4PD4krGKpQs_HmkXpaGLoiPU-Utt6jmhBVwJNudm0--FsnRshQ8312itUzXiPj3beQpwf9L-cVe9f4QIFt7h0jmW3B9lLJA_HJsl8S5-BnlF6Vxv8C1psJNKMFd3k_REcg6fAnGnLKa1DUkW3woJtoY67cUiC8E4OwLi1Id7Hmfvt9ExJnQ26kDOpM3Mo9t96ZqRvbStbmEOECC_gankDZ2Hm50oZ2X71sGhgWTH3uDDoI2qcREQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون‌شرح :)))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105798" target="_blank">📅 17:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=FdXXvNEUWKCUANPeuN7JTBLDmqHOUNfyW6RFX9nxQTaRb6hhINjYugfJPh_E1FlfdMiSoI-P2dTqDKRpUEacCzhFKQNRA72MXywLeU9YI8neH_Lz7gQtjPufr2i73GTQt1SiL9BtEZ7Osbz8PkS6Xu4iQK4V9iP4gRsk9kzUYFPoaIZkmypAhg_ijOPPXs8lYKD8-C8-W1YPQqdG43dg3t8Shzqf9H99s698536kXnGsAXpzCrKreNu18u1pQ_EkI6V4MDR0jf9cryTU650PxRQNVaLAbG9DwfxFzD9BvGYpqxxf-URlFZ5qlluuofVmK5u--pOQuTP0YpU6dISyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=FdXXvNEUWKCUANPeuN7JTBLDmqHOUNfyW6RFX9nxQTaRb6hhINjYugfJPh_E1FlfdMiSoI-P2dTqDKRpUEacCzhFKQNRA72MXywLeU9YI8neH_Lz7gQtjPufr2i73GTQt1SiL9BtEZ7Osbz8PkS6Xu4iQK4V9iP4gRsk9kzUYFPoaIZkmypAhg_ijOPPXs8lYKD8-C8-W1YPQqdG43dg3t8Shzqf9H99s698536kXnGsAXpzCrKreNu18u1pQ_EkI6V4MDR0jf9cryTU650PxRQNVaLAbG9DwfxFzD9BvGYpqxxf-URlFZ5qlluuofVmK5u--pOQuTP0YpU6dISyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعد از دعوای خداداد عزیزی و عالیشاه آدم ناخودآگاه یاد این صحبت‌های اسطوره علی‌دایی میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105797" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=dIB9B7se7S1Vxr0PeCqOVgYMrxqehfryKtRRYBZmGztULIBy3ky6Ej0JRDrz-vjldWrHQmIY997es_vaw1UzJNtIFI2LwkDmzyAcU_FZKN9C6K2_m_TJmG32vJOQAdWZhnG1HiCFNJV4t0w4WVW1C5KhgbCTBx_9bA02VNNYlyiCe-9EgZBk2sJrbL7GbRHqQi9X0-nQZag3cyl8DU13AfhOcq47pf8HpS97IqReRWn3IEGBBdCHZGQK_WQToceN5yoKHdBLjGLFxU8U9YTp2qebmBmADfLZxP1FA3UF41kr7wBFjeAFCKKc0we51tNkOzhJD3t-XCivYsKimUQ4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=dIB9B7se7S1Vxr0PeCqOVgYMrxqehfryKtRRYBZmGztULIBy3ky6Ej0JRDrz-vjldWrHQmIY997es_vaw1UzJNtIFI2LwkDmzyAcU_FZKN9C6K2_m_TJmG32vJOQAdWZhnG1HiCFNJV4t0w4WVW1C5KhgbCTBx_9bA02VNNYlyiCe-9EgZBk2sJrbL7GbRHqQi9X0-nQZag3cyl8DU13AfhOcq47pf8HpS97IqReRWn3IEGBBdCHZGQK_WQToceN5yoKHdBLjGLFxU8U9YTp2qebmBmADfLZxP1FA3UF41kr7wBFjeAFCKKc0we51tNkOzhJD3t-XCivYsKimUQ4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بزرگی و مردانگی یک بزرگ‌مرد، با حرف‌های پوچ و توهین‌آمیز یک آدم بی‌سواد زیر سؤال نمی‌رود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105796" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=OGSd9MJOFiV57jy06HYRgR2wyYJrstJ5-1bNTDMVAIWBe1M-dHeNCITVu6T0JHxI9pPRR4G_SVYE9VonQJzLzqlZt47v4y9cYiHgJbT4S_Ia3SIbr_dExBqxXyKrLWBRSiCi_a0lZZ25iJuvkewKFtIfXuR7WlJyTcGOqUMFd6d4e5OhjdUtvshc_pGGGVCqQ8NMG2SmFsDpgXKYjpEsrhULnOmqQtLTEC5k3GJ8ZFWFAOFo2p3VnYHPD8d0g-FrSVTGWdkPVcSJDRaSw_snW6TFudepNAxWFDeN6L6HeqSr3aiZK_NtbShvIoBtHv8jLZmaAuSjHDIeTSsi6LHAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=OGSd9MJOFiV57jy06HYRgR2wyYJrstJ5-1bNTDMVAIWBe1M-dHeNCITVu6T0JHxI9pPRR4G_SVYE9VonQJzLzqlZt47v4y9cYiHgJbT4S_Ia3SIbr_dExBqxXyKrLWBRSiCi_a0lZZ25iJuvkewKFtIfXuR7WlJyTcGOqUMFd6d4e5OhjdUtvshc_pGGGVCqQ8NMG2SmFsDpgXKYjpEsrhULnOmqQtLTEC5k3GJ8ZFWFAOFo2p3VnYHPD8d0g-FrSVTGWdkPVcSJDRaSw_snW6TFudepNAxWFDeN6L6HeqSr3aiZK_NtbShvIoBtHv8jLZmaAuSjHDIeTSsi6LHAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای خداداد عزیزی و امید عالیشاه از این زاویه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105795" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwUYXv8trRpZvltgwf7IWCbOb8-ENIB7TzqjmXl1b6-_3-v5wIGWPGMm0LC1gu0HzMb8mCdY1h6cNf-z_ONL56wAVNbbMqGVHdPqTMhlN7yeVIpfN8AchjF4Z3_HBQDAtHyAEy1qyK1d66PQwgomOfeRKvNmPiTFUV2vnajc2atVWCpagj2TaDZ6myPHIL3GquMDAJ9fZJykiU-Gt8Zi0Ja-LIUxPetKAAGdQAvIlD0yWy448zXp-OO2r8Vc3mfDCHPlTmj0Mmu5p6CqpeyG0SoSvAfyj2ZhxKOzYnVTDTaG2LkZjFllJDZsxM2MFelb5hUa284HMMz7l-4VXEgixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
هوادار جذاب و شیک تیم‌الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105794" target="_blank">📅 15:40 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
