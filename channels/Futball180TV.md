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
<img src="https://cdn5.telesco.pe/file/huH1SWU_PLgyH5k2JruYd6cOsT8i45jhkbxv7sNCIZIr8nuOTWLcpE9L-qNO2UpXxibztjQ7b1Z-GE0YO_qrcmHNYtMzh_qmvgswTbLJhuI3mgIcBLWAbPIC0QW_zm5WnPFwAtBC0LGA7O-oic16q1WyA0IpJS75Na9PKqO-dAjC0AmsthLfutcq2nJOZ0OMr8K79jRwxaUYGU3zYIUGUJaKBlWV_ntGFeeyBy9Xjxm6iyoVwrE4Z8Q_vpcxKdwbFck7m4hIxWs1ai6hpPfBhlPVrscwK7_KmcSbxstWXfAplWOm68xEzNVlTpaT4HusDPqD4olQTQAh21hoaHVp-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 598K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 23:45:05</div>
<hr>

<div class="tg-post" id="msg-99461">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آغاز نیمه‌دوم بازی اسپانیا و بلژیک</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/99461" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/99460" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇪🇸
🏆
• 10 گلی که اسپانیا در جام جهانی 2026 به ثمر رساند:
6 گل در نیمه اول.
4 گل در نیمه دوم.
🇧🇪
🏆
گل‌های تیم بلژیک در جام جهانی 2026:
‏4 گل در نیمه اول.
‏9 گل در نیمه دوم.
‏1 گل در وقت‌های اضافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/99459" target="_blank">📅 23:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh-JF8mJqgrp2_yqLMYg-zEE1hJb2T6jKQR_qIukYiluTHoUUDJbvq9ok_iqRbU3Qvm1YVCVzmuykUKj3JiDZgdPYJYAy53AGAo0Y40OgkGuf9ITvlXB72qMEaNnEvrNgWFsjo5DfQsARkBVVglB-4bAqagmxBhx1Ns1XVswQD37pTXPNPMPLUmSkm1sop9wZzpDis0gI8Ur1HTqWary9rbsKmGVFtDnMeMRPQVxJn-pGPWw2GOGbOoGrC6AC0RRANzijT9DBvGPj9D5xKFOetzzfdAT3TO9t0WUTSNDWzXVy2hm5uSV2wvUlsDaRErBvhHW7A05XhOtZte3fx9HIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
دکتلاره (با ۳ گل) به عنوان بهترین گلزن تاریخ بلژیک در مسابقات حذفی جام جهانی، با روملو لوکاكو هم‌رتبه شد.
🇧🇪
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/99458" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 بلژیک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/99456" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🔥
گل‌تساوی بلژیک توسط دکتلاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/99455" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99454">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گل تاییده و موردی نداره</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/99454" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99453">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چه ضربه سر خوشگلیییی</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/99453" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مساووییییی بلژییییک</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/99452" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/99451" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99450">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7LHZ82iB5-UUn1bAuT_v9RlQrkfGw41O7DaSeaJdw41y1_9DnNkq_ox0o9kbT_fMqjB5S8nS_yaddeAGLXU32NXihTuTvDv9vqxOltkzDft1MGtU6ul-R1bs0Z0d0D_3Y0anZxboJ7tyF91vTvsBZ0_lG__Tx-wBkLnlqtRkxjNvscIZqNvb35n11abDw8jGfMiNTuKsEVJ7_RNRpyaK23WlpPSp8388e8HKkz4s29KxJQYKeKebeiuFSeLc6Dq5uaC4zZd_b-vAbWf9fnsoWsHs88Tgl7E-OeuQxFBuEnn7p4EpFyaST2ngwngTJ0IwDUaLqm-pVm7T0cj4ymaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور برد پیت تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99450" target="_blank">📅 23:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99449">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خوشگل سیو‌ کرد کورتوا</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/99449" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چه خووووب زد</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/99448" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/99447" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چه بازی ای میکنه یامااااال</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/99446" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یامال دفاع چپ بلژیکو کرده قشنگ</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/99445" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خطاااااای خوش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/99444" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🔥
گل‌اول اسپانیا به بلژیک توسط فابیان رویز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99443" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسپانیاااااا فرانسسسسه داریم نیمه نهاییییییییییی</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/99442" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ببببببه بببببببههههههه</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/99441" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بالاخرهههههه شددددددد</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99440" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فابیاننننننن رویزززژزززز</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99439" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسپانیاااااا</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99438" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99437" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/99436" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEYvYQH4a18trmPAM3INIl1uSH2sgFjUMIwVo9sPsgJjcKnDgha5N4rZUY9qHqQFbI1b0EB7KxBdexCcbGlBlUliikPiyXjMbGgJ5XC4OWpWPKSlSD0fH6HJ-iD5J5bwYjuHkGm3sAIOExFl497AsJBRrJfnal2J3j21g8K5h4ZppQhz8PGYAbL18Q1i4KXkQJrNI-nUewR5n3nPwYdezk6eVpgvdula1o6MNMcZdwYkWbHUAxJcECHJyz2tJoVFAiE51dxzXqe8dRwp8UzE3l--pU00r-yfhdA25-3ABk3VI3QqqL4yaan12ZoxgSsxNlCIXO3HN7JjvgHuXXu67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
#فوووووری
از آرشیو وار: پنالتی اسپانیا مقابل بلژیک گرفته نشدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/99435" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlqe9J0iuUaKbDIY3OuwwHAwx7ADpEC0rJVVqBNIZDrNhizsHuMhM3l5t18aD_AaImZ-s0pE9xkuMvcHQyt3D8IvT7bYKqrfYhympatOI_kMNvtYWkNANOsRYr4j1eUgpHfSJALN3R8NiUCGpNqWyYqKlYPZS6b-VrDyhu5xSdS82UF6VBLCykfhBn_rUQ8QRUQV1DG240SVMxUNH_ExLgeZ6psmEknNWX8Nxmb-RqUFuUQNn_ZCAGEvejegwbjJLec_GwybOrXmOrUNO74uRmnrP3NM8v6kZXl2S1bPyrkDtBD1lItzHTpW2mp4VMsOFyihDdwUklTwDqlSRZGgkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پست جدید رونالدو: یه پیروزی میلیون ها میارزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99434" target="_blank">📅 22:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKtKfmwHxZjid_ywrdEZ8ttzWOpEl3xMQuURFxEnL_LXtWTbK0CX6jZ_4zR82mClRR2-QOd16FMT4HQesZCOwu9ErhuoALezH31YkFUnJGrs30aWKu9AsFePKGo-CA0V_7CdyA0hNpMB_t25A-jEdNBGrBZBmTFjfKl1Sv2dDm7nvn-ixHbq4RRbVY4kn4LMj1Wp7QpsBAdqycylZHYsyFMuKYMq3jf9bIVuv74KDvjmpSfuENoyo3RqHO9EojzRtrt6S9YIwRdArHtffxIsAj5ZhBy-omyAz7FIF9HTG95W8uI8NOMOKPQPz3QrxAkNeZ_rNoiRdTEU4N1fsnNuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر یامال تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99433" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bet_maxxx</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99432" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAZK3Jqfv63Z6CpcRKjogyU4MYOzpSMI7ptsidAYgCgVcRL307cSzF9RuQb6TLx2hdg8y0Fa14JHkIIGhx1DLtOmHR3rgR2FHWkI4a98Zl4kqvF_VZyJc360KJvy-5zfd5sKEDyxQQs42AW1iCsudZz0PEdUFSso_QrE2nkg717a5fbodAzN9Cl29JJuMhNr8K19zwth8rFfmUTBAmr9A3KBmWwX0-8899WO_NPu3itE8SOF4z1ZMzqX3KtPcBzr3MuuTuYAl2wYewAtO9K6MyeiEmF1eqTsS1tdPNCIzC1NLeQjDNemXR8qzTuWkNPTHvFhvKpdtCb5_ezMZPbipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bet_maxxx</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99431" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بریییم سراغ بازی جذاب اسپانیا و بلژیک
🔥</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/99430" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇧🇪
ترکیب بلژیک مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99429" target="_blank">📅 22:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDqUO7jevOOMQ3JKtqpCEerlsZdVLn6T5L6iqZ4SIzHPsBfCHRP98exfS-r2gDD3BHYg6yJiANEnZnXAS7foJLOy-WxUadPFo6TL49sKUckcTF3MCiYO-iSyZTKXSdz9d5B0r4Ss7Fl7k-knK9jjia6gAPd6OfY8nftFY0MGqGn6djE2NFTyGfQ3l86T0ZSguO-LgPVWzF6itb7Xj61tqj6WMekMa-2VcbG8HxsPntsnbJUHfrZ__0QCOqS8-6ABd6YZRSmAgsq0w01hrkqLgqTC_Zf4V6wNFTVD__Tke2t0NRY5xuaK8VEn2NAn9janagUcTwBnQifxMbdZ2Q3JSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به خصوص آسیب غضروف مفصلی که در فصل گذشته (2025/26) رخ داده بود، و همچنین تردیدها در مورد سرعت بهبودی او بود).
تیم منچستریونایتد از نتایج معاینات راضی نبود و تصمیم گرفت این قرارداد را تکمیل نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99428" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99427">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUJBQZA4zRlZTQ-o0ik8dMi_cAzkR9psGZUJg6VyXOrqg4EBDSJqA9h7yxRDBBlSEoOTCQsHZEO9CScnr7gBhwOQ7Z88X76f8k8NUY9YH8eOFsJmGMN_AGZkqkeN5dnrCUgEiiodyBbdpt4HWKE7_c4bjN6yxJOJVHE89wu_BOnyuww2yYXVnpMMqbOef1xTMQ-22sEDgs0I4QNoTXspA5HCV_eSy_spYGXO2Tbjw9iEqHBcmZFkhfE-e4Yehq7mPHvTkKnxWiiP8dwuD0KsWG_3O_8OIvyaObXd_NRjSIQz21nPyBHE1h3F_jO_R5_XkpmSpcdoob4Vbn_qMh_SEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
علی‌تاجرنیا مدیرعامل استقلال در آخرین صحبت ساعاتی‌پیش خود با سهراب بختیاری‌زاده اعلام کرده که پنجره نقل‌وانتقالات آبی‌پوشان تا ده روز آینده باز می‌شود! هرچند به صحبت‌های تاجرنیا نمی‌شود استناد کرد اما باید تا اواخر تیر برای اتفاقات…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99427" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=f-xN2eDaJvoiehptJ15C_rscm7uxtGFBG7d8W9N7SMWxgYwob1l-G5gZOxXYlhpaBX0LgwD1OYupd12tFzJKGOo_CVa71e59lnjKY-EvwpHLwXIewK6Xkotgr4zpjKicO_t0u4ZEM4jav3z8vTAY581zqwTZQ_WcE3aImEv79RF5-L4nq0dcArAQiUSLE3I6oCHN3nw_VExi91nSRb-aBVsFWw9enFSsCi15ef2VBUPQCvi1GTBjkhHRCBo35fNoiMzI1fNkZUNAaALcBXe_alRiHE7mEEOpIhToJMlW4DpAkigupbtxsZ2wUfyXVxs4WUeE1OAdpD8CD3AcpUjJLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=f-xN2eDaJvoiehptJ15C_rscm7uxtGFBG7d8W9N7SMWxgYwob1l-G5gZOxXYlhpaBX0LgwD1OYupd12tFzJKGOo_CVa71e59lnjKY-EvwpHLwXIewK6Xkotgr4zpjKicO_t0u4ZEM4jav3z8vTAY581zqwTZQ_WcE3aImEv79RF5-L4nq0dcArAQiUSLE3I6oCHN3nw_VExi91nSRb-aBVsFWw9enFSsCi15ef2VBUPQCvi1GTBjkhHRCBo35fNoiMzI1fNkZUNAaALcBXe_alRiHE7mEEOpIhToJMlW4DpAkigupbtxsZ2wUfyXVxs4WUeE1OAdpD8CD3AcpUjJLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیتی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99426" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فکر کنم کیش انقلاب شده خبر نداریم
😐
@sammfoott | پروکسی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99425" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siWeY2AQv-qqTWNs8gR1DztvIWKXSPinw7l9NNQJ1ejkAof602-FhRO6IJXaQlxj1D_7ehSesHf0MjB2f2hpAM5QTb8wrG-S7QDIRzcioeOW18nGvv-4eVBhYC97CcNWHJUW2O72kbAKrwprunzCPSzynnowqAa8EboKEO3HExEMD0ipDDor1T0lAJeiTM2ev0r7k6H5eqFhDe9aq3sExeYFF7e4XUCHtbRwSlPqMllQ4cBW6vDPjZRqHyLzJlUFCFvYeQdc-hn6_GsPmmv5z4MLmw9bV02RVzmV9QUPwBL6DoaGHi1PqjHA7hGrmsJBnXVimaQlF3VxzYBQcGa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
هدف مورد نظر بارسلونا همچنان خولیان آلوارز است. قرارداد آدیمی، تاثیری بر تمایل باشگاه برای جذب یک مهاجم جدید نخواهد داشت، چه خولیان جذب شود و چه نشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99424" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emPMO3fGjO0REDAKspT59lJdw_d9errWIz_xK0HpHyBEC7jNJBITltqdjEKwsypwR2PfZ72zc8UYJMT84WbHyeAiYBFqYMXCQRGlA2-Br_UBnzKT3FY5F3nOUjptJQjczpF8SNE9Pd0iEIBobn2C5y5AwOe_ZGu2AHY1llGMVKl63cd9oMfKH6Mk9UE4MjVZDlRoo1wjN7QgTdK6xClm4jFd5P5qSckollokNQZOn8vY1y4_EWo_VaxsXGhSyIoBEtOD7169gqkMvJvyowuMdFeRO7_WLcjEt5zDZ0VBLpQgUvuvU-0SVwcByVXCLHE1SzWA25B9Mgcd5w19QTOpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99423" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvICFF2grlB1DJcCxgL2s_0C8YFmm_n6yuWx4ImYHFU7c_p-nRZkSIa4UHbsrtxDPlEPjEctcxsRxJOpPRR-GFRTjX0G61e_jpbAUMIfRolgm655a1oqVwCW-9s7zA67uoStLF-d_naZu1w_MxdQ_mlqSBbdj1D9XFElcYbCVmM6tD7CLLJEZyFPqW21ZAmWFHf4OGGQoec3uUvKR22nx4mbyvPPnkd9mnUzF58gE2PTVAjwQBkg0PyKlenyhdgnx6S9iYNDBd3e-VRTL88xMfmlBsJr5u79BB4UoguPkxyzalFR3d1fSl3vAppAz5AOxu4iw-nrg0UXUoPPDTi8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99422" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=g1FCzizUEjfBrQUX3QZWnMgIbogEmVV24ejQrmYtYvJYiihlNpT-wBnzOCHA5xng20zW95GG_CKemqP6lJ_owRk9K3V8M87ZiX6CkIaQkuC5wK4d5vKFIAGGAPdNc1KiQXeQgdx_etN-QZD3C49qMWzYpa5oosOYPGDYWe-ajsHMwU9nY2EAvBfbC2x4AAOq_WMvnkXAg4_MKtuKzgf0YyVqyeFiSRKVfFel2d6Ht5Hl_J7h-ApWSxzxMUxkklaNATsWrJD7cuIqhz1cdXpwzP3_YQHJRiiNflfen20uzaVdAepqRsUwnPcWWahb2deCpyur4d5A4DuqCbSMmcBgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=g1FCzizUEjfBrQUX3QZWnMgIbogEmVV24ejQrmYtYvJYiihlNpT-wBnzOCHA5xng20zW95GG_CKemqP6lJ_owRk9K3V8M87ZiX6CkIaQkuC5wK4d5vKFIAGGAPdNc1KiQXeQgdx_etN-QZD3C49qMWzYpa5oosOYPGDYWe-ajsHMwU9nY2EAvBfbC2x4AAOq_WMvnkXAg4_MKtuKzgf0YyVqyeFiSRKVfFel2d6Ht5Hl_J7h-ApWSxzxMUxkklaNATsWrJD7cuIqhz1cdXpwzP3_YQHJRiiNflfen20uzaVdAepqRsUwnPcWWahb2deCpyur4d5A4DuqCbSMmcBgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
سرقت‌ گوشی سینا سعیدی‌فر گلر سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99421" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0HdIVlgHJ2nyWevNIM3uf6NypSGoGez2_PrR_Prz7fJ3sd0pvY4JZiOorrE11l8jANRHnllUjPQ0wsRIcbr8cxy7LJF7F3BogLQFT0kUUwk0YJ_gVwJ-Bf6uDYXoFgcLPsVD4JLWrLB6vtQvQkLStKxFPQYrJRJ3tsJHVjCJ0OQXZ1onH_NV6Nmd8CHjt1oyYjL8R8xPKrIHv6UM4kdbSoEMbY9EXVtehP8ZzxNFHD-41cKohxqegRKxld0CA-pGmDgsq9Zd05XDFz5Hh4reISRgXfWiodr8Aw25Atcu7fzAGLguZHokACpUQs6maY5sH4HxBme3moEJLCnLbfkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99420" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZxiPiKdcvncQ1ZXeV_5mexnXZ99vicN3BrR20h2oCabiFGjMiw0Psp6Ca_ktX5mF9I9kpZ4qEK2rPxZSCJLCAegnkoiofGas5a2m8Yo6GC_8fHIBWYgT72Jz868XEmeoW-KmZ9pCyXfuXE5ivJsBA141LmMJt0HuOLdG0GqXVkfffOoAhcQXkybWAFSjnmPo4ywl8g6Vm8VXrgO_C-sGAwFXS44Jz9C4QIWWccK-cjCYO0uasOSsjE1smRBk8lrzIXfEs0gV85FLvecoYYHIRlBOQ-KtcabmuamJ7PtDMCU8V4hmbyY7qlspqxMmyXFCe2o-UEN1z2uCG-T5lI5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
👤
استوری رامین‌رضاییان که تمریناتش رو بجای حضور در کمپ استقلال در کشور اسپانیا پیگیری میکنه و اعلام کرده که بزودی اخبار خوب در راهه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99419" target="_blank">📅 20:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBc9Z1aEE_Neb1AyCiFNIdCE8VJzKiK-EHsj8PZJojr268ZJyMOtZqJt1zNGoa0TqD4KKovXvhMkx0dkmd75bqTCVOTn3LZ14YvXlsbgh6wo9CCpV3j-pJSC-WRQUF46eWnUAnoViqY9WaTD1thzfDI1UYiq4ZJpQEctQmLeSHSMDzp6W4CXTizMgiV0GPOYTmIe1IuNz3a6hsLiSNjT8TBYiuoNbFv8HO-hDCvjrPrIOTvffoiMx-FTW-HFttcpybHGXlzpwS8UjuuiuHLLiQaTPaiZSD41f0igwb-n6ZLrkzAjL1K9w6gvglE9T_W4k2g4bT8OriFjuQvIInRH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مورات یاکین سرمربی سوئیس غیبت یوهان مانزامبی در بازی با آرژانتین را تایید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99418" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99417" target="_blank">📅 20:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔥
🏆
🇪🇸
🇧🇪
تیزر فوق‌العاده از تقابل امشب اسپانیا و بلژیک در ¼نهایی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99416" target="_blank">📅 20:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=UoQPpbGZ4sjzBdG61pApJPGJzQfJl9B8GJfslfQEkt6lTN6yctIntBbRqhoEdWXSVnujIsZ3UcD9kx4qn8marRk-5EkzZK-DNKPJV_ulN_1erA6Jk3GZ1WpWXWEUVksOkiK_sRorLcHqkoDLmnxVF0Oaga_zSLn44VdOBqc6AabGNgJZyKUDNnVYCnhtqmjhEK2YI5MjaunteD_RDAlRnHrD_Ui7WCpjHmydF2K4y3NkVdr3EptbQ_NkxXC5rCj19YjX3bzL8ZbMmKfO9Z42k8ddXgjPKUbRbSX1UHjC9S-MAHN2w2-zwvQgVxhJcBRF8Epl0thf78FO9uQjUkhXfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=UoQPpbGZ4sjzBdG61pApJPGJzQfJl9B8GJfslfQEkt6lTN6yctIntBbRqhoEdWXSVnujIsZ3UcD9kx4qn8marRk-5EkzZK-DNKPJV_ulN_1erA6Jk3GZ1WpWXWEUVksOkiK_sRorLcHqkoDLmnxVF0Oaga_zSLn44VdOBqc6AabGNgJZyKUDNnVYCnhtqmjhEK2YI5MjaunteD_RDAlRnHrD_Ui7WCpjHmydF2K4y3NkVdr3EptbQ_NkxXC5rCj19YjX3bzL8ZbMmKfO9Z42k8ddXgjPKUbRbSX1UHjC9S-MAHN2w2-zwvQgVxhJcBRF8Epl0thf78FO9uQjUkhXfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هدیه‌یک هوادار برزیلی برای کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99415" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=MykhkX3mE5yY4HVCLzXt8TnJ8PzOSTqTSEs_JQK6KUz2MytIfz9p8gKIwD39VR6BYEHYLCkZ0ts1VLlbPO-cd_sxi2mYTgJ1-_cFW1d7WtJnCqmaLa2CC78K_W2_w3fQ31FBEbURZv_9bEuGzB47r0wOlUZwOqUurI0QW5EsJcfGwZ6vEUeBIs3pwq86uj5qOedVu12Ns1YYnQs3Ncc8n1dXW-JA0rWzcba7IiaaqzBBSL8LmE6P-zZ_XS1Gx9eIFLwuzjs6ywvdPcHZZY-sR92zhdK7hWUPzdMofq0inY39Gk61J21-CIbh3bm03kYL-xI6ymInori63Pj7553KBRq_D4EkH77MC3u7ioDEq8bC4wn94ThwkLW1ypXAd8jePdUrgplZjF0qXAZnXM5rar2yDbo52PNtsS69vGmxjJt4bI_pAhaFwWjkDl7znpFXYCP58o1dPzOnkJEl0Rww8Vaa6P1uohEIDHXhQpyWRDDqcVIukgGFBULYl1sxQpAibKYRe1pJzoKmcw7SmMpSIYikXghMpBM0oQ_fZC1g35z72R_8A8y0gOcf8eNNPufP5PIRx_uKc09YadKHcLiRKS4xB4X216BJeMsQ7t2zy7j3-6fRgv8dkC7UOoucxxT3aXldJKb2A2pVj_8gic9w_G36T1eDb57ROtGK3qLJp7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=MykhkX3mE5yY4HVCLzXt8TnJ8PzOSTqTSEs_JQK6KUz2MytIfz9p8gKIwD39VR6BYEHYLCkZ0ts1VLlbPO-cd_sxi2mYTgJ1-_cFW1d7WtJnCqmaLa2CC78K_W2_w3fQ31FBEbURZv_9bEuGzB47r0wOlUZwOqUurI0QW5EsJcfGwZ6vEUeBIs3pwq86uj5qOedVu12Ns1YYnQs3Ncc8n1dXW-JA0rWzcba7IiaaqzBBSL8LmE6P-zZ_XS1Gx9eIFLwuzjs6ywvdPcHZZY-sR92zhdK7hWUPzdMofq0inY39Gk61J21-CIbh3bm03kYL-xI6ymInori63Pj7553KBRq_D4EkH77MC3u7ioDEq8bC4wn94ThwkLW1ypXAd8jePdUrgplZjF0qXAZnXM5rar2yDbo52PNtsS69vGmxjJt4bI_pAhaFwWjkDl7znpFXYCP58o1dPzOnkJEl0Rww8Vaa6P1uohEIDHXhQpyWRDDqcVIukgGFBULYl1sxQpAibKYRe1pJzoKmcw7SmMpSIYikXghMpBM0oQ_fZC1g35z72R_8A8y0gOcf8eNNPufP5PIRx_uKc09YadKHcLiRKS4xB4X216BJeMsQ7t2zy7j3-6fRgv8dkC7UOoucxxT3aXldJKb2A2pVj_8gic9w_G36T1eDb57ROtGK3qLJp7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
استقبال پشم‌ریزون مصری‌ها از کاروان تیم‌ملی فوتبال کشورشون بعد بازگشت به این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99414" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/99413" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99413" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHkaqOwmRCl9SiHWV5-CM94OPN8QpXxc1jbMk9DS3tok0z4CgJAaO8TCP9n27qqxlap7Mykpg3grCMUp8QYGMfXWumSV-TM8cpNJCeq5wNKZgWvYTSh03QmD_X4va3a8NoAc9oWRZi-OZWZbtzKnf2yG5Trww-i_EoTyNnzeGf5S6ewWcnXpvF4J-v8oo8Dk4nK6T3RjwbCGIxi6gKHiRx-Kzj2k2wUvarCxLV4H9bZymG6ISAEoT49OXL1WAdI6qZYd7JRkCDVrMCwKAX44JTTIq3fm0FCKKQw5hCUOR0wKCp7YWwWW33tHFTs8_Rr0x5005KiwNCP4vI1d-W1fsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《
لینک سایت برای کاربران ایرانی
》
👍
《
دانلود اپلیکیشن اندروید
》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
19
🔤
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99412" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0G6j8TuJFN9Fkva4u_7QOa97wymoLPRkVBPyDjTnLgjbWlRGi1BGz5cCs85SBK57i1q_zDKhSFIDg36EEhaqljFygRlhPZR7nMmcSUPBpMNt2ckUdEO6uLBigUWmcHf8hM7IBgoDPcqS7jhovLG8R7Ju27O5c0X-EC_kvNC7S-G7-wR7YzvTur2zeKWusB3_FrfV0_wplYzsmxTlxAd2yAQdSB0KdguELsKVWKeC0-XHnRF1f18ylcGkD5HBpE2xz7NoYQvzZW6TGQeZgUtmbbfJjwbvimxoQjip3VOfNL7oSoYX0IQo8TBVrH8hni6qtB51w-npPpfl__tJE-Fjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‏
🎙
🇧🇪
رودی گارسیا سرمربی بلژیک: رویارویی اسپانیا و بلژیک اتفاق خوبی است، اما زیباترین اتفاق، حذف آن‌ها و صعود به نیمه‌نهایی خواهد بود
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99411" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99410" target="_blank">📅 19:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfRHVW1phdqLX25BElwyS3Fko2UHaB6_WajR3pI0rmrZ4fVoyxD_F7lQYEmSccEOqdRWgx_fJ0WtCkbKGkMHPW3_9nkrD8ojunHzg66WpumRew-vRxOGuo8Bn5H9mxW0m7nonYWMLCvxEYHNbCgqPwYzP382yrBOjIU9-jJ3faWfD-uHPRGtNJOO7cVguZJ37ufcFzL5tDrmUQneAbf2HvrMGMx7HVpmS5Ryw4Wt8sDGjfe_vfmmgaTqiL8hgiSWKD_dgOrk6hWPYWKuG8_GmRUzGq8wGkeG_O_gZJts9HvjEfq2UJZb4fCFUUQj0QxRXukgdR414cSYbEtU7k-Zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو:
آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99409" target="_blank">📅 19:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFu6muvZKfrLN4Ol1YM44N2zX77_1Vut-f_utrLPP3pqg6H6dfsMOWnSmfa2k6G_altzxsepIevWcgvu2xw1rbIQtZBwWsugj-IaIdmamE-wVaJ0LBKRGZsjmxXQ541_I_lcaB64fIjlComBOCvS6lyLS-xZ581ZpkzRlTMqYtZEWM9J8rnGWNGuL4ZwQVIC-mCiJG6mf9f-t-1jRCvNIfHj0mZDZTXWNs73_d6msG0IKULYBej3tRI249AHxpm0y8HW7lBMqSuCgBRdrX_t2_IUPTAgVAS_fZR5Ss4qrgSOK0yyGwMSn1ThUjQZY7nCVtgZGYbWA01gNOeBXIZL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
ایکر کاسیاس:
- رابطه‌ام با خوزه مورینیو بیشتر شبیه یک ازدواج بود که به پایان ناخوشایندی رسید.
در سال اول، ما بسیار نزدیک بودیم و رابطه‌مان پر از شور و اشتیاق بود.
اما با گذشت زمان، رابطه‌مان رو به وخامت رفت و به دلایل مختلف، از بین رفت.
امروزه، اگر با هم ملاقات کنیم، احوالپرسی می‌کنیم و حتی می‌توانیم کنار هم بنشینیم و بدون هیچ مشکلی صحبت کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99408" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC3i39q2Kxf-78y7dxUNiBGyOvwKZgqjqBHi-GWHYpns7XEUxpwA652aUCsV86mYd7kvjYec0nvtiTAppGDNj-pBUvoZ6lwaY4TDQHHMQ2PsXk1n6MXY8oxGqm_Yp9oVRpbjyRgq1gEA8-5EC58-Upr3Osr-6GD75lED-YtoV3O9wGg0q4ZwEJmJmnLovLlr8ISwm9QjIVUVEt1ra_5-dOfhXJL-ujx2-n4hVsgd9AkD8TQmxFtkzDUDT2nUJzLFj5MIqe_QieSpVhoTgyNoPD8RvHyQwo33QN_HzcdGW8oi1XDh_HOz8LlbyUoE6rvw3WTot7DPhxh3p904aWVAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد سادیو مانه در طول بازی برای سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99407" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnWS_BOj8GwhmxlLSByQNoem3AWbBNsheCzijQbsEBHuhEOhbEyu_8hl37rXysPRJ9mISsDzPECf_Yh56D3or0WaxgPPSiWjnwHdpdA0zKblF2Tl0rS7yzAqZszHLkpgM06X4Mxyqu3_N4RYZ8v8rlsM__rKk5P7v1z9cCjtKEQQMdhzV4KlHHSELWFwdlQxPIlNEGTMsbVqGIR_kP08rttHmg2bOJnGIp9M2DtMx1KIwmILsypk8bU5yR0Y4vR1YuMWtL5CEW_iiJl02gC4KK4COz-nL0dMPy_JpsCQFlteq-FAFKxAxRjLqjWx6tdd5NlOhnRB2Sli0fJFFdKRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99406" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v68KAnF-L7DY0JNPqhOOt5UdUvWEBxr3HILrtX963ra3qGxaJJ4RzsOY-bTgXhcOw9z9stJPjJ4nzrI54lXs6QgUkHXHhr9cfSFK2QM3LWiRCudDYdK2ALFXzL4eueHQyQ2HW-ggxtJESSO4-BJLX6wIox2eC9pYBxRxtXrWrzIhALhhdDlG4NgXn_smMZtHlco7HQUp8CCjqMv8xZxCO2dg65XipS0bBgtC3DFoa2fAdQ3SAio104HDt67nwP6-JOW1zonWdfizoqtjrwOj9lc6Ir2lyZcoZDHc9MtjaR6_2MadqBShTN1a9X3cvVqPo4Wkad_VFTBdTuZchllX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
اسکای اسپورت:
بارسلونا پیشنهادی به مبلغ 20 میلیون یورو به همراه 10 میلیون یورو آپشن برای کریم آدیمی ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99405" target="_blank">📅 19:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj2rz31vgUnenkpibh0eEUOq4t46h-zV18c2zuPeXuD6jEboclh0PTka-VqhNnruc6pi9KAjzuPKgtTTbNMOtJsFfvc9g4asHm03h4bizC4BDfMAFSNhiG_Kj9jmvgTf5838sjG2YNRp7e2ranI6SV-xJHKZaW1YyFWQp8iazhe2PBrSGvWM-i-sNSGl84vJuWYHU-47EdH5bSpesZmYD--FIQuDt_FuJYWWxjLW91U4yLa-OOHvuA3AoJzi6R6jYxG_hc6HxWtdefKT0ZLX1zboe8EPZ_HuFHBaOpo1IBdsF_PcqJaFF-UXK0UXUDFmj9idhDJryaAKqjrFmTCN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇵🇹
خورخه ژسوس:
کریستیانو هرگز مشکل تیم ملی نخواهد بود، نه برای من و نه برای تیم. کریستیانو نماد فوتبال پرتغالی است. او می‌خواهد به پیروزی ادامه دهد و دوران حرفه‌ای خود را در النصر به پایان برساند. کار کردن با کریستیانو آسان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99404" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECu7ywxPTFYGn1SlxxF75gAn_HDTOU36itdfpjKksqhQ33jDSglRefqhNybnuiJpxcrs6SiIEAu3wWNlgxMjmZJaWLkZDXsvRj226VwfHOWI4jVSs6H8TpH2hgSipfytXoC8qR3YcO-JRS6X1BFz_8n62zrDVF6irSV14lIx5OrPVo5lOXDd4zm6KulQhPBMUbM_MzU7_GWtvO8ZVQsFf5Dr5R3zp-2PxpRACP3XyyU6ynZeWqpOUGkZFf6xJQ-JY55iEcf98_VAnAPbBWIZRPUBn-TXWBASacBWiQ93ZKZTdI6z34l-iV-isJea7kUGbsKkmGwNtxNHd6IlH2W6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی اینترمیامی برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99403" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99402" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqtUYLgR7msF2j3Q03eGvz2msE-_XU5QAV23ZkDRRMBxvUVAu57FzTfgcoAOcC-8xvnZYHiEwxukfiA2VWUr9wsv7IzkiLA1WIQHz5zR9_CnIyMXkFYyZnVVH2EMTfmgqamt536p3xy4vbJ7jDNBFBViweDXdFCmrdnr9PFbRj5fA40CpEUMSXjZtg-GsRH18dI2udBN1N43xeSaU3XvmlbVbVizq2XpmZhJXa15mKxi8klOixJZfKJ_0tSrNkNplqYyuL_fhIY2DYxnqz7dMy4p041x71ZlF0jlNTuYGHxqaoAcN55YAzIYG5_fxRNG2zhSyxU7F_Dge7_SJgw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین ربات  بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو ربات و ببین
🔥
@TNT_Winner_Bot
@TNT_Winner_Bot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99401" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnJSC96TZo4SrsUkwjR7LsB63B5TMHsdJMSeHa_RYFcRAncDjHS6gS8xfAmkhWPPPH3R6ur2VGVzeFHUfyl0x9EuOSb9oMTJMhEZ1mtbRVfOPbH4SPEhz7u-SJRDsw-2iiAihS7-Tb4Mhp9nqHBOmGZBH4ZRdizJEmzH8sGUtVtyuA2rmIe0-3HlwaRl6IKD1LgIhAI2CqjkJCARb9vRFNTDQVnAtOPrcVnx8ksCWltYrRx0C4r7VRbBfQV9l11HqDipA4bhMhiCB0Yn-3H1c3I-foL0MbXX5xnIanKBdUX9jjjtPkENUOt8RN9PgdMYxRmo1RpHmh6EHb698FD0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر گارسیا، دوس دختر پدری، دوس دختر و خواهر گاوی، دوس دختر و خواهر کوبارسی تو امریکا؛ همه خوشگلا تو یه عکس جمع شدن
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99400" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4zspXmnrFoQ0muCRbLXwfu_6YxSvMsQA6mwDlt18vliFLcspuZagnE0tNhhO_-nlbKLpBji_PjqLAKxLOlNlDuwhE58ixMWByu8qAO9Eca2-YsbofiYcfuW5hbBkotu1AbKadNfuyATAScHUHwWDfmxU1AhfRoW2vJh6NpNOquAkwSIwRkXJVFF5IwJ_MOtCIH8Xi1aDby-vgoPL5Y5qo2ydWAaR2aE4DMLAKBzqbH0-gFInYFQrYxnuPtnUM8guDb_-6bODC00gpZhy9x_v4ZqJnW85uc4Y7LJTYKRs3k_-Ts_aqqsFeKsTu769su7jSzg5she_wtueZejlHVUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری
؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99399" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99398" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/626fb89fc7.mp4?token=sOLxAm_7tN3nSbk8DK-4I0j83xngA6JSrQo5Yph4V21Ij2pAIVvqy4p0IQDiMo7bHCwUk-S4WJzFTmq39muaVCdxSieVRasaDuOxvEGH5XW7XFY8o1vS3Ru_9hMDcNksc_Hh6PgsTeeGqdDnGiJWyfP2924x_tHuq8ku6bGAFdrU2X0-UghcEWQldZC9Kligk9jOWIbcgzyX4EZp2joJALJa9wzQhSoBCaZcprHdGI94VqXvyBpsTcpGchl8ItHLKY10Ar4_1_UdGDSYLOuCzFSP6KlLqO3-oowgqUF4k4u_euWM_N5oOodIcPwDSe5v7h7YoZ25Ugqiw4ykDnhopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/626fb89fc7.mp4?token=sOLxAm_7tN3nSbk8DK-4I0j83xngA6JSrQo5Yph4V21Ij2pAIVvqy4p0IQDiMo7bHCwUk-S4WJzFTmq39muaVCdxSieVRasaDuOxvEGH5XW7XFY8o1vS3Ru_9hMDcNksc_Hh6PgsTeeGqdDnGiJWyfP2924x_tHuq8ku6bGAFdrU2X0-UghcEWQldZC9Kligk9jOWIbcgzyX4EZp2joJALJa9wzQhSoBCaZcprHdGI94VqXvyBpsTcpGchl8ItHLKY10Ar4_1_UdGDSYLOuCzFSP6KlLqO3-oowgqUF4k4u_euWM_N5oOodIcPwDSe5v7h7YoZ25Ugqiw4ykDnhopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
گل‌زیبای امباپه از این‌نمای تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99397" target="_blank">📅 18:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40b511411.mp4?token=qc0I7gMVBD-OLFSiict26OOUuJgUJq82EuvAyI1k-5B5bu09aWPNqAc-8WI-2Y8yV1lEVav2H8HVyjDXaeYxB_CktHKR4PaxeF-KHeBHD2R_-djPbJDKDdHX59kLcYhk6KCto6PFWC8uwdzYH-YaEoY8heuKuqkT01p36Dl0bH_1K0xFoDXU12y_rLU6ewNfK8WLu90OvZcJnDpjiVUfMLKR99vSIOpATsyicAZoKVFvYF0TiLwJc7GYlyp2fK6ehHKcs3KAHU1z6r57_qs5gPZMcptqP1qzmORYbf3lMkOOwpq-X0vQ2wJIjH053-LLItf_WLdej-C-GB9d-DuEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40b511411.mp4?token=qc0I7gMVBD-OLFSiict26OOUuJgUJq82EuvAyI1k-5B5bu09aWPNqAc-8WI-2Y8yV1lEVav2H8HVyjDXaeYxB_CktHKR4PaxeF-KHeBHD2R_-djPbJDKDdHX59kLcYhk6KCto6PFWC8uwdzYH-YaEoY8heuKuqkT01p36Dl0bH_1K0xFoDXU12y_rLU6ewNfK8WLu90OvZcJnDpjiVUfMLKR99vSIOpATsyicAZoKVFvYF0TiLwJc7GYlyp2fK6ehHKcs3KAHU1z6r57_qs5gPZMcptqP1qzmORYbf3lMkOOwpq-X0vQ2wJIjH053-LLItf_WLdej-C-GB9d-DuEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇫🇷
هوادارای مراکش جدی‌جدی باورشون شده که امباپه دیکتاتور هست
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99396" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0602625ec8.mp4?token=obGNUTGwuxpByhrLt228MNozNEsbq_hu0SM2xEpzy7hpKK1ml8PYf-gMDFRUREUqWYptUJQAl8ajhLh4I_RgsAFyIfsKsEEVmU5VTuzj4LCrNx-Y3vGszStTSYxsbixRfTGPCCK1vY88etTFHRkFhnBtYTDdWYrf2sVjjNh2DDauYfzKvrc0Xx4_6yPu82MkMsXoSjaLPDoWUSF5dHVVdEgGItX9EFZwigBfw60Pw4QvjLjECG3b9M_kFR4LaC1oLzTPtUxJM3PAcwe0uJG4O7Tzy1TIplJug0UFv_7Vphaf-3cgwRrQ0EAuqIPBBQdrNeB12qZb-NdnwU1zodsw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0602625ec8.mp4?token=obGNUTGwuxpByhrLt228MNozNEsbq_hu0SM2xEpzy7hpKK1ml8PYf-gMDFRUREUqWYptUJQAl8ajhLh4I_RgsAFyIfsKsEEVmU5VTuzj4LCrNx-Y3vGszStTSYxsbixRfTGPCCK1vY88etTFHRkFhnBtYTDdWYrf2sVjjNh2DDauYfzKvrc0Xx4_6yPu82MkMsXoSjaLPDoWUSF5dHVVdEgGItX9EFZwigBfw60Pw4QvjLjECG3b9M_kFR4LaC1oLzTPtUxJM3PAcwe0uJG4O7Tzy1TIplJug0UFv_7Vphaf-3cgwRrQ0EAuqIPBBQdrNeB12qZb-NdnwU1zodsw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه سردار آزمون به میثاقی:
آقا عادل واقعا دوست داریم شما برگردی به جایگاه سابقت، حیفه واقعا کسایی جات بشینن که لیاقتش رو ندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99395" target="_blank">📅 17:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE8l1uO5RGbjE5Ianfx5heefrlsYdABxcp-S81SlwLcXMCvHcFWKh5Q5tK2HjluO4cyYK2NPybbRbIkVSJRNJPVkgGzLvSURUOMlrOaOzs-30Tj7SWuV8Mo9SVEGQ1RN1UKWtw7PlM9V1hLGkZQ8j8wyt26xiVrbKwxicGjak4cGlTRpXtsJ_CnQFdMBK1R40P0hJ0CxY_pPneYUJbuzAHQcorlVZwNbUhHfBETeA6IfhUPzT4iZdj9HlXKt3XysieCLySVDUYMXceUcdoyhB88tXVedP5Uh1rncgu7cojV_1_c5RPKlC3c5oj6W6a_7yLbsOi9oBrUi35_b3aSD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
خورخه ژسوس رسما سرمربی پرتغال شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99394" target="_blank">📅 17:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99393">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b97dc0ec.mp4?token=Tm3m7UKJrQfkHbq5H0nsPBKp58MRhKlBuf8N7k0afaslhAQ8TTjFOhAMYJVUSK9zZnASWCex4Rqs65WcsTFrc3gLmknWqfS4YCzDoYGVwj2E-1CPnLFpSBic9dYoWUM4rbvGx-sZFjeZ_OryIrMbHUaxodDsSBRaIMeVeLWvQrOF6Vd04bUZp19vm1dqaqICUKDjrSkNlej7RYV9cZpp7vZlO2qR8QKeDqqQB2G5q3ArE5dP_4y0Pp7ZkSm7zHn07KyDWRcgviuUrsmQ9ltynL6L8hixe6WQ5xTdrty-BABMeVhAsKZFEFs-cxgxMlpjjnrv3pwpVJY_U6RWCxLdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b97dc0ec.mp4?token=Tm3m7UKJrQfkHbq5H0nsPBKp58MRhKlBuf8N7k0afaslhAQ8TTjFOhAMYJVUSK9zZnASWCex4Rqs65WcsTFrc3gLmknWqfS4YCzDoYGVwj2E-1CPnLFpSBic9dYoWUM4rbvGx-sZFjeZ_OryIrMbHUaxodDsSBRaIMeVeLWvQrOF6Vd04bUZp19vm1dqaqICUKDjrSkNlej7RYV9cZpp7vZlO2qR8QKeDqqQB2G5q3ArE5dP_4y0Pp7ZkSm7zHn07KyDWRcgviuUrsmQ9ltynL6L8hixe6WQ5xTdrty-BABMeVhAsKZFEFs-cxgxMlpjjnrv3pwpVJY_U6RWCxLdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
نظارت دیکتاتور امباپه روی ۶ تیم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99393" target="_blank">📅 17:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb018ba05.mp4?token=upW1UU09YuJyacpOtZw1Ayj1opi-IjGGNCg9HAOCtT2g63Z9Vwef_E5VCm23LwLr_VbVpZEHbJlhFoSDrvrW_jo-UxWRwurB7HQ_M_hDRbF4redcXXIahdDhiwYHjT0KToG1kfPn1ufYWzK4HTwemhhOPOBgWMjfw39ViR2vBA1EAGNExiuqVCbclA-dWnk0iO46popxTbd7oCtS9kCcSqbLDzqnN1y2MrbduOJgQIavHPOeNKpiwkkR5MtkNydqRbEUCEd8DZToHL9mL1YtgK-3fekW8aJ1fah7HFiO-JEESho-EKhNsDp4IQqWlvEZTE6qjCfkg05qSOZ9CVSpYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb018ba05.mp4?token=upW1UU09YuJyacpOtZw1Ayj1opi-IjGGNCg9HAOCtT2g63Z9Vwef_E5VCm23LwLr_VbVpZEHbJlhFoSDrvrW_jo-UxWRwurB7HQ_M_hDRbF4redcXXIahdDhiwYHjT0KToG1kfPn1ufYWzK4HTwemhhOPOBgWMjfw39ViR2vBA1EAGNExiuqVCbclA-dWnk0iO46popxTbd7oCtS9kCcSqbLDzqnN1y2MrbduOJgQIavHPOeNKpiwkkR5MtkNydqRbEUCEd8DZToHL9mL1YtgK-3fekW8aJ1fah7HFiO-JEESho-EKhNsDp4IQqWlvEZTE6qjCfkg05qSOZ9CVSpYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
جوری که جام‌جهانی برای آرژانتین پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99392" target="_blank">📅 17:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI1mjeSPp2onJthtR_G05FZi5zcDlbCwuPhNf8o4EQEwejBQImiVaLuHSizsY7UQc4R4erDagwtaAAazm5_h36tI_xYl8kZyBqN6MsTKF9rHArg6gtwnZZuNJC3zCkkRt0Gbgfc3cX8730djuPtJK8gl4PrT66lE1g57_hnZXwR3ILoQhfHHwRi5qdgsmD4oDt824AfgzLTHj7kxwy0AIdd44QuMMdEDk-FTeUZfpJ7ahEYWMaMA1_gUS0D4gcAqf_k-VTubsqgghgIGFW-as0p5LhhLM7cVyX_NRObkYp4LXJ2GVtb27Pd2cM4EjVLccKPer7ohtPvfIoiIhf4URg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
دوسال پیش در چنین روزی فلیک رسما سرمربی بارسلونا شد. آمار و دستاوردهای هانسی فلیک:
🏟️
• [117] مسابقه.
✅
• [87] برد.
🤝
• [11] تساوی.
❌
• [19] باخت.
🔥
– [323] گل زده شد.
🫣
– [134] گل دریافت شد.
🏆
– لیگ اسپانیا [2 بار].
🏆
– جام حذفی اسپانیا [1 بار].
🏆
– سوپر جام اسپانیا [2 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99391" target="_blank">📅 16:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE3BtUnDrVwkRrlc0r0_w6lJ2308oloNT0m66zMYaGCWqx7aAeGjjNTSehIC6nDuCQh4QSIreqSYrQfrX5u-WSgV0XoWSy4jCoflLPwn7W7xvoXOdbV9joakXpFGCukVkjDSSIqhiP5GKPgblji35lbvEb5gIsOcPjz5-PUabbcQWUHJjYOZ_Zcn4tsRjpeg1o2LLEkzHc6PxiJsSOPUOGiYUgNyWRRcOuRF2CNspMo6nZH0X1Z_6kov-kLC0xnvzblgA8dyZoIjn0FYRqmB6Qxyawn3vVSW_AGtiiQLUbbYTX4X5Cy_DxfGj1fjQX8tdbmTeYfP2esxvaIscNj_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اردوی تیم‌ملی انگلیس بازیکنا و کادر فنی به جود بلینگهام میگن Unc یعنی همون عمو
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99390" target="_blank">📅 16:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👍
▶️
🇦🇷
خانه‌قدیمی دیگو مارادونا در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99389" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC4Ex5ER1S_zUMGol7tim1dFUi5E3I9B_-vPfeBvTVN3hynVu9ou5hVBGcWBMHiOOU73Tf7GFXpssfsA7q1-1RFp-IeE5mBy2vrE0YylG0VTRYrQiPYh7KKXcqK7Y9L1lOGah7l5CGBEO2LwMyC_9jvBen-CmEcyHwtOEc51pE3powyccZH_LFqMwsuM90Zb97JK72c97vprmnNQX_mm30JnEOl-k8keXkxUSuXUalHNLSO4ciF0ufMAZ4CMFviZ4jg98ydh70AfgMqsb-gnukGPI2M8GhCdeag_LXOgO71t9qXn8cxO9zPPn9OLXWp0S634Xbgu6ZtjTcfVLWb60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🏆
در چنین روزی
اسطوره تاریخ، لیونل مسی، اولین جام خود را با آرژانتین به دست آورد، با قهرمانی در کوپا آمریکا مقابل برزیل، آن هم در خاک برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99388" target="_blank">📅 16:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99387">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoBO8tmhr31k5zDQbNN7IlYIHxg6oa27RbS5re-elHrawPSR3qJ1NVY-hmOSK90nHAFRrVg50hrkffSLk1zFrdalUBS4EbGvKzUOKK1lDMGga1qFdwGG1GH2LfdlNKglTqEToQ8HZind5wy1LAZlDuZ2DcGSEAphh_ZL1wFqr4r5XH_AnWG07-5ocOLMKoYOA-eCSnOgdWBV9dU6cP6jCeAh0kGuqMx85Qov8cHDqPtoQh9vcWgAz2qOrXdPjSTEWuyvylCwXGJjHfAsAKnFB39d0x-8fNWDVpw6u4aPH6aSUMP_TDyKzwP2yxVWgk_e7cIcra7lZXNpieE4P0kX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚫️
برونو گیماریش به طور مستقیم به ادی هاو اطلاع داده است که می‌خواهد به قهرمان انگلیس بپیوندد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99387" target="_blank">📅 15:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e356e0dc3a.mp4?token=aFhwumocTI-QCA-2bwTXMSZK73pjxIqQzjij3g25qS1vGS-xtiSD7pebKJ_BmwkWkiCaaSDO8bK36DWvJgqqaqVDnTDFTpsHMBVwNbJGgtnhgCdmRWm8zel56oJ53qk2KoqjHkOTfIP12_soYxv120aXBEqcRR5zbSyd2MOApCSOWHLDsa5Vs5XUhR2_8HP-DRVc-GYPEXiblen9YhNe2k8Rq9vEZbjgWywbFAIPDsnzgNWJ4aaTU7oaw1Oz9Cdn27QcUNxe4W3TSKzuq33nr2fblieuPQwTwCVX_raBn7LMWMkd9y88vYvn22FkmmfQuskLZVoisO7yPlPsBw3DTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e356e0dc3a.mp4?token=aFhwumocTI-QCA-2bwTXMSZK73pjxIqQzjij3g25qS1vGS-xtiSD7pebKJ_BmwkWkiCaaSDO8bK36DWvJgqqaqVDnTDFTpsHMBVwNbJGgtnhgCdmRWm8zel56oJ53qk2KoqjHkOTfIP12_soYxv120aXBEqcRR5zbSyd2MOApCSOWHLDsa5Vs5XUhR2_8HP-DRVc-GYPEXiblen9YhNe2k8Rq9vEZbjgWywbFAIPDsnzgNWJ4aaTU7oaw1Oz9Cdn27QcUNxe4W3TSKzuq33nr2fblieuPQwTwCVX_raBn7LMWMkd9y88vYvn22FkmmfQuskLZVoisO7yPlPsBw3DTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
صحبت‌های ناهید کیانی از تقابل با کیمیا علیزاده و فشارهایی که بابت بردن تحمل کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99386" target="_blank">📅 15:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4b043e06.mp4?token=OdaAACDkRh6W0a0yaIvAuSf2aaNMAQCZzjSawLEb-Ms43zT9JSTxXTrUpLL0kElZM5H42yieE8cTJ7RAlGu0Rrj9u3g9XdmokM_Awkwd4HE7EFwGFQudWUYznfVDO11qgV9YWpjERwBz2Je1d_WKvckzQJRZeefRwBMbkhmkpnT3CjeQSDvOWCbBTgctureK66TJLemeAhD3cKhFRPPMDg4etJfGylfP2pgTcl0VLkbZoAeow843cABZgawx9XaEanbvAs9mwWr1eMzlZQmmFb93D6ieuL_VavbAMEh5jJ2WJRwBcZhQiATRcQlJbss3iwdPjF-6nHqmEtjbshQ8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4b043e06.mp4?token=OdaAACDkRh6W0a0yaIvAuSf2aaNMAQCZzjSawLEb-Ms43zT9JSTxXTrUpLL0kElZM5H42yieE8cTJ7RAlGu0Rrj9u3g9XdmokM_Awkwd4HE7EFwGFQudWUYznfVDO11qgV9YWpjERwBz2Je1d_WKvckzQJRZeefRwBMbkhmkpnT3CjeQSDvOWCbBTgctureK66TJLemeAhD3cKhFRPPMDg4etJfGylfP2pgTcl0VLkbZoAeow843cABZgawx9XaEanbvAs9mwWr1eMzlZQmmFb93D6ieuL_VavbAMEh5jJ2WJRwBcZhQiATRcQlJbss3iwdPjF-6nHqmEtjbshQ8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
افشاگری رضا جاودانی از دلایل کناره‌گیری از مسابقات مردان آهنین پس از سالها برای اولین بار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99385" target="_blank">📅 15:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlWRQqSyRwiGESJULgIu2iRvsYEJVXxw9f3RBuwenk42reZJtsopmH--dvb9FxvdEQ5eWwhLanhi6-Q8LaGohM7LKW8DU4QA4hQPq60tgzJMFmJz6IBsDh5-WaitpZMu71KWJRty1VlUPaLV5RwoITMTf-6SlfxYozIMvnZTYDwjxBlVuJwjrHYWnFfHNaiXuaMyBQtG_7r5Czel3Q5EmQVxtS8AxnndQsB6yM-xRrofAXPcwG_hs988Qq8mhOsVReG6A14z9bMo42_9k3k6lId0xgQpXL0WMgnez3z_WlvIwEUVtNoNnKQk39sCo6lbzOlC2St7l5eTAZd6pgN0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
بلژیک رکورددار بیشترین گل و پاس گل توسط بازیکنان تعویضی در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99384" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpQ832k54Wrd1dEmb9dug_oMtstp5bvYIafBQu1Lg1LjFG2ECgoeewN5CSkuphWUVo6DacMTRxw3tytGjTLeAk_pJZPbscnthKey5WAY_JXfTO_5VcFeUAmuIJukjYqVjuKVd-ff0dDrJF_IlNUlXltBFIujTfdO5TEsjka8bKUH2m2SC66Bw82-A0sVrlMxnyyxB-rRr7fv4nWGKys8AvIoA3fvbzlqekFBL9tOnw4QUeaYJy8Fb8tourNCxvEahgalyu6cxVJF3ZA5O5FU96VynFWJye2rk8EoNV05PmtXd0wZgWz3xjBjQ1_aTe2nClFME7kXnOdcGAWXdW7j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری شکیرا در کنار بابای امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99383" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99382" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvSE49ZYG8Vn5PcrVLtMlTUKJCV5ZXeqGLqana0CYayivI5eCpulWHPMIR4WHyIbf6JIBrVHznVseJaeMAlC5ChKzb6E3saSIamMGcAMc9MXZfImUZ6uDqjC581DrP3GTOhvzBoBJ-nyBVjTE5ecu7z_OdUF57F_YEFdJUHySxv0PYkQtQ4Vi5lU1xo3jes8iBMly2FLDSk3f2qftnOWxPdOKRjNKonbG3p1e47biO3LlE3m4xhTV_5_sZ1MHhUL9hPn-KZzQm_HJlfL6vgi7e58DDbWOerAvhmQKNnWLsImtcrFAOURuLjj8f30vZa7DpsCMoG4tRZIBbPkhYGrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99381" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99380">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d05baf7f.mp4?token=eZjfWR5lDTKNzpytfMVEGEK1woP-lo3rYTblTJPiDWDurk--D8R6nAvUmJBLXXDC6EqdTxsawRLbRn3LaXosfvFtFbkCFHsXJ0RK7UpB5qasqmdPDD8m4vUUdha5D-G3auCq8LHPcYU0AWY14ub3yMbK_1sapKP3tSiAE-yqOWXxtawZ14X-YhIKqj2p3xRAO2F05wtSYWdoJYH_e6mQBKu3S6zTJytMSeods7yJDvFxIigFftlzkBRJBphb06xhxBgBT3w7P8Hv7hVGymLEarm8HxMlyFKamFhbdLhHBqwHNBqsDMYact02iEuaYvrfatcEA7ycU3JBUQnsfHtt7Hqvn13Bc3P50Hjzav8ojQIUyOUlVGF-5U0xPelF4WYMs8q0OYzH7A12C1bwTqd67HWtXod4yLmyX-JFmI7vcdcAJ8MXNqBdRKW7d5WO9tfQHdd0qUJ1yQv6d0RAqRkqnBYtjwPmBCHXiknTiP5iWIhq9EsA0LwVlvDOm4TD7CCtqCqWbNmxlbvfeEX6AwKEaCFEgEXYD144E1RrDD3p08oKDquucTfV4G-a6EO_yPQ9U7KN0NnftAZBEvKAfTtrkkyTejKYV94g04GMkyKorR_FzJwcq8tNHuAq6p3D6oEJdTwAe_seaNcRt-BNqj7aiDiTyHVLnPg1bjC7Lf20O1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d05baf7f.mp4?token=eZjfWR5lDTKNzpytfMVEGEK1woP-lo3rYTblTJPiDWDurk--D8R6nAvUmJBLXXDC6EqdTxsawRLbRn3LaXosfvFtFbkCFHsXJ0RK7UpB5qasqmdPDD8m4vUUdha5D-G3auCq8LHPcYU0AWY14ub3yMbK_1sapKP3tSiAE-yqOWXxtawZ14X-YhIKqj2p3xRAO2F05wtSYWdoJYH_e6mQBKu3S6zTJytMSeods7yJDvFxIigFftlzkBRJBphb06xhxBgBT3w7P8Hv7hVGymLEarm8HxMlyFKamFhbdLhHBqwHNBqsDMYact02iEuaYvrfatcEA7ycU3JBUQnsfHtt7Hqvn13Bc3P50Hjzav8ojQIUyOUlVGF-5U0xPelF4WYMs8q0OYzH7A12C1bwTqd67HWtXod4yLmyX-JFmI7vcdcAJ8MXNqBdRKW7d5WO9tfQHdd0qUJ1yQv6d0RAqRkqnBYtjwPmBCHXiknTiP5iWIhq9EsA0LwVlvDOm4TD7CCtqCqWbNmxlbvfeEX6AwKEaCFEgEXYD144E1RrDD3p08oKDquucTfV4G-a6EO_yPQ9U7KN0NnftAZBEvKAfTtrkkyTejKYV94g04GMkyKorR_FzJwcq8tNHuAq6p3D6oEJdTwAe_seaNcRt-BNqj7aiDiTyHVLnPg1bjC7Lf20O1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
خاطره بامزه فیروز کریمی از تاکتیک معروف «آفتاب‌پرست»!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99380" target="_blank">📅 15:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99379">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94688a21.mp4?token=iCXfkqIxteYAlguAuVetz6_ii48oAHCAWkluE3dif01XD1ByS3Z6vqK9tHhe4V1a89ySiEBHrJ5rGJ1ETJ0H0Vl_WOJ1ujkJSXWfMhFYaSJb0Ihc-6VBsySMA9s8hKQLfJWSg90eXnYI_2vsmlDfoNJFJQfmHGqssD3ca-4EP5l97mVb5_QQ9XnmVQiWvXV75cR3DS-vGHf7hcFw8JhAK8j961zFrFko6ClOMTeIZpj9aC4ZLrYnqvLsaiG1jy4q-8J4oZ1tYDJ7wXNJvpfXAzwqeg6UUbkJo9T-XaTe9fwARctTWq6dMiUm4bqkEEwXUYFnLKT3ijqncOndasmhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94688a21.mp4?token=iCXfkqIxteYAlguAuVetz6_ii48oAHCAWkluE3dif01XD1ByS3Z6vqK9tHhe4V1a89ySiEBHrJ5rGJ1ETJ0H0Vl_WOJ1ujkJSXWfMhFYaSJb0Ihc-6VBsySMA9s8hKQLfJWSg90eXnYI_2vsmlDfoNJFJQfmHGqssD3ca-4EP5l97mVb5_QQ9XnmVQiWvXV75cR3DS-vGHf7hcFw8JhAK8j961zFrFko6ClOMTeIZpj9aC4ZLrYnqvLsaiG1jy4q-8J4oZ1tYDJ7wXNJvpfXAzwqeg6UUbkJo9T-XaTe9fwARctTWq6dMiUm4bqkEEwXUYFnLKT3ijqncOndasmhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
لحظه احساسی و نوستالژی مصاحبه جاودانی و زنده‌یاد دکتر حمیدرضا صدر
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99379" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99378">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtYcA-KlYNV5oNO9olrkPKNsdqkEi9xsNWEyZDNiunlQ2CXwchnZVO00gWuPUqRuvBDRyigxGupKLvmrG77H1-qqWhGa57ftsQrC9deOvr2E32rRP_MhvyLPFMSUjvONvkaaFe6N4vMM4OxGeZ8JC8RZOMuJBqMAmdSQPvmI5RaqhL8OXm-N39INiFsgG8506Ba6-RmDFgGW-SaVWN-1eWUZEKNnC1eS5sebu0N_PDpb_Uf9jVAyWLEbAMjkXGtPZ9BP8BVDQsfmThsDEi_s8oX48xNKimtt1k48OMmYy4DLq2g3aQofAoaLZnDJ7qJGLvNVHGbat7F9YgS1yiK58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کلود لی روی درباره جیانی اینفانتینو:
وی تنها یک ویژگی دارد، اینکه به چند زبان صحبت می‌کند، اما یک احمق چندزبانه است و برای فوتبال خطرناک است. او هیچ چیز مثبتی ارائه نداده است، بلکه باعث شده این ورزش در نظر همه، مشکوک به نظر برسد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99378" target="_blank">📅 14:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7bfe33636.mp4?token=LvmqYLxjWjQqJevqWEdwUlZ3i3fGeqRerZITMpPYLvR9XPDJ5VWUPR_z1aXBsMp9i1Sb8R3qG15NukTrrClKu8Yh7-PdQW_fQY5VutKdzIIPQER5WBxrPCwxcm5IZKSzwxO_TvTsgCaA_GaIC2s373E9ozTBEV_9U2fB4apEkIVkghHlRSq_COo4VPg8WilIGLjeofr3UdSobODh4KtkuC5xkcsevkXF9n6wJ-D5ZT9QxVSc1aja97bHgEE6KDCJ0hyqevhWalCBSY3HfC4wptSaMLDRbQFCKO7B6iIkXjfhEciYyefmgE2nLsH3yticYnXWwT8fPA4dUULOUubV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7bfe33636.mp4?token=LvmqYLxjWjQqJevqWEdwUlZ3i3fGeqRerZITMpPYLvR9XPDJ5VWUPR_z1aXBsMp9i1Sb8R3qG15NukTrrClKu8Yh7-PdQW_fQY5VutKdzIIPQER5WBxrPCwxcm5IZKSzwxO_TvTsgCaA_GaIC2s373E9ozTBEV_9U2fB4apEkIVkghHlRSq_COo4VPg8WilIGLjeofr3UdSobODh4KtkuC5xkcsevkXF9n6wJ-D5ZT9QxVSc1aja97bHgEE6KDCJ0hyqevhWalCBSY3HfC4wptSaMLDRbQFCKO7B6iIkXjfhEciYyefmgE2nLsH3yticYnXWwT8fPA4dUULOUubV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💥
صحبت‌های شنیدنی رضا جاودانی درباره عادل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99377" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze7hxe9gL22EesEBUIAv-pJiFkxsgAR3GL1epFTNALgssIomhyLn2EzTbC-Q1vzBwiXsIxyT1Z7-WSRU9gBFiGPScEtjvoV-XkiymAdZc44RxNVfRcftupethQWUzgiv4OEO01wYEBph4ZTZCEcRwIDgcmv5klTLZ0T7mQMkxadUfmwTzCQUxqU5727GK1wscV5PbThKn1KLTkgqOeVWIUfQIk43Rezn6fqAAMqUFplsIJnho9mcdJVKgamIswfM74j8SRUEivFV42j5Xu1yfIZk6u3srLurkseVZXjbDSvGeHenNBgSRcGMI2ZB-Vh0BR-Shn1DgIr7qEZaPwD8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کادر مربیگری جدید رئال مادرید با حضور سامی خدیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99376" target="_blank">📅 14:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZfM_G3L_PDkg5uYtIUCKKL1IATXTNKLY5M2Zjrr0dpwoyJFeOy2pZzqGXHIFWFjqaHN7VGOAdVtKEiY6y3wJSujh6faIy_N_ERpq-6igXDi1GCJOgXJhwbh7bk9DW6AGqQQcmGQwbEZvqc-dc-cL_Ipq9RjlxQwVFU-sX-XAkjUrEZbapfGtqnV6UIDq2Bu8TLyoFU4Qt7qO334yNagIeGK8iYi4C_Zng52dnh9UQggJy1IKQ1FmqJjo1SPh2h5SfFYG10HXlvVcxamPUQbng4Dgq4lhbT0LzgsWVJJVrIQHbCokzDve7-e1XV1Z9U8bkV9W1aj8m0-4GSs1m8LMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇸🇳
پس از حذف از جام‌جهانی، سادیو مانه ستاره سنگال بزودی از بازی‌های ملی خداحافظی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99375" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99374">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsZSgK1d5aKwdnosxK_EFoi2xv8C6VCdMpqTmwfPcS41cTUIxBdhKzkF4y5NOrjUj4W7DhNCAV39OCPAIOpQz6On3YEDtdeDRsimBibI6IaYIH5AK5nENU4P_TmuClOEcw0hf_WMFqckj8POu3PArrU1k_pg-tvDSOQ0nGqGCZuePho0qQVjN4VROj2miuji_8OGpkU3HSxM_pNw4I6HKZQRzWrhaEgyRPAaTGqa70SmphTH4hY-JgpqN2AkQKJu9Lrw_TqtgBAF9qSzSB-s1fmCqO0ALzT4EplsK62ZpvwCyl7jY2cAjivhR7eCH-TKd6eBcTZxu_dqvf-JaiX9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#رسمیییییی
؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد
📊
👀
🔵
آمار ابوالفضل جلالی در استقلال: ثبت ۱۶ پاس‌گل و ۴ گل در ۱۱۰ بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99374" target="_blank">📅 14:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0kUH07O2bN2fr-e0yYx5NLF6l6EFb1FuMWm7w72VniVhoLrylzM6v_uK6wg1l1LqckIMcI0UHQ2SEr6aHmltiwNHyj0wCQghfCys1cc0QdV6RHGVw8uLxHMU1wucEtcxPT5Ff1zH1iAVuqkYkDdllItwfjVQzLkEs-TtYfH-FelVZVn5eGlh8iX_pu_-yaSK7XyC3ET_XDa3Qr200DicdlR1VlJv4uLf6q-447iq7RUgbQ-hIWogmzC-H453WJVZAueloASjku6ZhTyM8SKkvs-8wmtSman7Exha4nlgtXjVF7aFR14htWK_m_VSral7eaN0Qp3JznGQ6Fke13-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
🗣️
لامین یامال: "اوج اقتدار در فوتبال چیست؟ بنظرم کریستیانو رونالدو."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99373" target="_blank">📅 14:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3897abd1.mp4?token=kABxUN7MKZd9qHe3gSOKQ0JL69SL8qumdZtZqMO3hAMhKn8eCxlJxIqMzofXi5BYKBpFN02TZHbpVBe9FHp6kLniqPcE0gUVyWJfBROT5BnTp3JPVtBclXxPrIgqc-6tWXPmQjrmPyUgVA084Zi1knaHogM9es-5dYkhXriQ3cRjEPDzRmTDPLOUrfg7XMXU78IAwV2E9MDxBiI9rrVquHtYh92Dk0nYkQeLuo8o-j0q7D6ArEo-5Ql0Hl9AXmqs6t7atuE0Uh9bTvzdroJjVtQNoID_xDQTgq7oslBD1nnuH6GjL6MJq6ipmKZ4v_ip15pg8HP1g5Plxl-XKT5C-gUI1JUNWstAcHyoVaTc8XiY4MDuiwmZnWTneuIqC5n-cK6JlaRmi1kXzSltY2--jIdztErz7-ZgSoA_Xu4DwS6FMuW0-XVjDT_fBnKWNvNrs_FwIZm9uae-7b4x8-USzObcok6sDjVQUv6GG_IL1IXfxsn5Hjdt6Ejq9gfuVq-z41-IGnGxnL10pm0huPAqNWOyWewP1A_qTkwHygnywkij6MQ8bqg9vQ-FFPfL8bhgkaRRVYv7LEDlnZu65p0qm7zJa6mnIUpOLu6B9UDahLQ3TxXlNcOut8wrgRpq5wRPWod2EEm0QV2cs0D7vNO-7m4LOZKEWYtTcyEHa0cSsRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3897abd1.mp4?token=kABxUN7MKZd9qHe3gSOKQ0JL69SL8qumdZtZqMO3hAMhKn8eCxlJxIqMzofXi5BYKBpFN02TZHbpVBe9FHp6kLniqPcE0gUVyWJfBROT5BnTp3JPVtBclXxPrIgqc-6tWXPmQjrmPyUgVA084Zi1knaHogM9es-5dYkhXriQ3cRjEPDzRmTDPLOUrfg7XMXU78IAwV2E9MDxBiI9rrVquHtYh92Dk0nYkQeLuo8o-j0q7D6ArEo-5Ql0Hl9AXmqs6t7atuE0Uh9bTvzdroJjVtQNoID_xDQTgq7oslBD1nnuH6GjL6MJq6ipmKZ4v_ip15pg8HP1g5Plxl-XKT5C-gUI1JUNWstAcHyoVaTc8XiY4MDuiwmZnWTneuIqC5n-cK6JlaRmi1kXzSltY2--jIdztErz7-ZgSoA_Xu4DwS6FMuW0-XVjDT_fBnKWNvNrs_FwIZm9uae-7b4x8-USzObcok6sDjVQUv6GG_IL1IXfxsn5Hjdt6Ejq9gfuVq-z41-IGnGxnL10pm0huPAqNWOyWewP1A_qTkwHygnywkij6MQ8bqg9vQ-FFPfL8bhgkaRRVYv7LEDlnZu65p0qm7zJa6mnIUpOLu6B9UDahLQ3TxXlNcOut8wrgRpq5wRPWod2EEm0QV2cs0D7vNO-7m4LOZKEWYtTcyEHa0cSsRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
عظمت تخت‌جمشید کهن و تاریخی از دید هوش‌مصنوعی؛ چه شاهکاری هست واقعا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99372" target="_blank">📅 14:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgDwohT46Ja1Rp_AG4qvN1Q40bhVHSMbFM1YJ4lEr2aStwDIW8jFU-il2tukWSshaiWOuwPk3UV3HL5e51W80MJgs9KksNXXaSENYUki7_YGDNmzqDOYHZlgwhWyx8D5pEDQyIUeUskAFLKkyopHE6-K81CRMaTA2Wq0qIjqI3VXgdteaU_Qn1QGszHxAPObwu9u5vaFy_c9MMd7tHiTWrhPcFDIdCX7YwQIu2Yv-IqjqNdV9HIvOTPH1wdWCEIFmqK-ysQRXRkHCBRpNebEEUHGhUVEibilPRngPIoMk5Mff7Fu64yU4rty0pfJmWlRIH_AhfhTkt8EPfK6zOFc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🦠
دیلی‌میل: دکلان‌رایس در آستانه بازی با نروژ مبتلا به ویروس شده و در دو روز اخیر نتوانسته تمرینات مناسبی انجام دهد و محل اقامتش از سایر بازیکنان جدا شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99371" target="_blank">📅 13:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=orhI_akFtZzskjTVxb5UEvioCBdJeav5MBkT25jIIPu20BpLDXwYnvj3JAqfr0hHv6t8A_3hdxi2TwX-PgApgsWz3lUGNDAz_O9D6QpdIlaVyQYLRgzc2RKd54eO-k8wyrz30SBLFpRbyPTM9RcbetqfgEpDr8WcYm9aGARntCfJvfxLLBlgHTfC-zmX_gqSyJl62ndo8mYpCiSh8ygZDhGZVsIBnRXdz-RgoIu-W-RQ_62dh7zRsm2U4uRcnze4PsZW2qDqQZVzMgBvWQ0x2VQKMCniZkGQ3r5AdOsS0yuAqZFKaNPVuI9H8VvHiaFQyR9kulVeIgtpZlGVzM5bZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=orhI_akFtZzskjTVxb5UEvioCBdJeav5MBkT25jIIPu20BpLDXwYnvj3JAqfr0hHv6t8A_3hdxi2TwX-PgApgsWz3lUGNDAz_O9D6QpdIlaVyQYLRgzc2RKd54eO-k8wyrz30SBLFpRbyPTM9RcbetqfgEpDr8WcYm9aGARntCfJvfxLLBlgHTfC-zmX_gqSyJl62ndo8mYpCiSh8ygZDhGZVsIBnRXdz-RgoIu-W-RQ_62dh7zRsm2U4uRcnze4PsZW2qDqQZVzMgBvWQ0x2VQKMCniZkGQ3r5AdOsS0yuAqZFKaNPVuI9H8VvHiaFQyR9kulVeIgtpZlGVzM5bZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرانسه به نیمه نهایی جام جهانی رسید.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99370" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99369">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
قرعه‌کشی مرحله گروهی لیگ‌نخبگان آسیا و لیگ‌سطح دو آسیا ۲۷ مرداد برگزار می‌شود. استقلال، تراکتور و چادرملو سه نماینده فصل‌آینده ایران در آسیا هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99369" target="_blank">📅 13:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz3muK2L8RrcCCBqaJ6YB0CUbXMqG7ORR92M2l3Mj72imC8-Lfbe7hmc24JbXJMHMs_x53Oc-jJHmeMNHdj80ZLomXxstiz2WetJmKdtYgfJjkGtVweIFfUXbE4qsslBmYaO7KLuE43C_AwGQFqpeVauvBLDH0NQ3pBoGAhBRH-bE8bk2bz0tdY1KsJvGbuQFpJDf8BwefA0j3OlBqGMI9Ker28GNUdUJ5ETyuNluILt11CGzX_YG3CqfCwvpH0NGtgQpsS2haL5FXroMnOdE9wcAR1FXJ2nMs2S-_EKhRQkroFf4yhN4XkXhbGHfdff4b5Yj8B6ebRyXpbWhLu-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇾
سیلیست آماریلا، یکی از اعضای مجلس سنای پاراگوئه، ادعا کرد که حساب اینستاگرام او هک شده است و او مسئول پست‌هایی که در آن توهین‌های نژادی به کیلیان امباپه وارد کرده، نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99368" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99367">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1L6e6OnfJd6qhm1udCWTUCe6WhkVMjKWdKtpD4hAtgQF0GYB4A_Qw43yzdCk3RgInvYcVsZAbPMjnqKFj8xCqJwmmEWALR9N-zvLXBMD1yauBUAAbkYRpKLMC7C5XzYskLym8kP_8pRFr8L4NLhVn1MXpItjr8B93TX9f_kB5v97zIUMKyc9dXtEUmw78Agvazwdh2ZtqOpYivw1OM2Jvq0n-PkYZntSkGcDaCtK0Za1BsMQ-QKhI2fDpRISFsvn_RM06iLFWg6Pz70yWVRG-qr3cgAV1WzaZtmKvDDt-utUYYwqAAnFQXw5taw8QFsGmslOWM34R3Zbzb6f7cuQ6j8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1L6e6OnfJd6qhm1udCWTUCe6WhkVMjKWdKtpD4hAtgQF0GYB4A_Qw43yzdCk3RgInvYcVsZAbPMjnqKFj8xCqJwmmEWALR9N-zvLXBMD1yauBUAAbkYRpKLMC7C5XzYskLym8kP_8pRFr8L4NLhVn1MXpItjr8B93TX9f_kB5v97zIUMKyc9dXtEUmw78Agvazwdh2ZtqOpYivw1OM2Jvq0n-PkYZntSkGcDaCtK0Za1BsMQ-QKhI2fDpRISFsvn_RM06iLFWg6Pz70yWVRG-qr3cgAV1WzaZtmKvDDt-utUYYwqAAnFQXw5taw8QFsGmslOWM34R3Zbzb6f7cuQ6j8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
بازیکن‌سابق پرسپولیس نطق جدید کرده که البته برای اولین‌بار احتمالا حرفاش درسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99367" target="_blank">📅 13:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99366">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHsHRqrBmqCDjNyFTrJG3kBp0Ep2JiyY-u6diogfOqgPkVu8A5y8mLRJ_VWTnxuomVWZK5GFHVpGYhdlR8YnUT7W-AYSpW3HF07b3PQ2d6VJxpCTLTOaxdIlfeqczf5n2PbLrU147Vazj27274TeORSQ60qBm0pg8-Ekd-gADOqi6JI3dMIMCvKWF9OsWjx_1HW0Jbzk1sB2gID0aPUKuvBMbY5gq01GwBiTaxLplXumXL5uePbGKJbbdRTlJf9_1NHd1ofLGF9m7B9MaZtuLPV63VQQO7KgSigvUnaoRgiWlibb268zrq2HIuHrHNQ2Of6TmOr84xKD53PwwzgKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
موندو دپورتیوو:
احتمال رقابت بین منچسترسیتی و لیورپول برای جذب ادوارد کاماوینگا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99366" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99365">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=gqwfokU_LSr9GgSV4fw3fThCNeRjiAZ_eHhSAJJHnZn6Zr0gB_VXgK37bc4GhR60hwnMeRdyyPRFiih6fyLbRegKkWmiHa2f6VUHZcK-DSh3U3RMFWt2sxBg2V65ueSqy9CuVxsk8qySqV1aedTBfxBdcKOUe8ieFoIPL93qAncwXIMIZ4IFuazrI3iZXF2bzUuflbYeia7d-g23lKAbNv-mGWVoU8bgsSJwWbvvWcxyy1dkh_0wujT3RNFVe9V3IQCW-EnTYvIj4PjFYOY_jlQpjIFzJfvcoGSgJDTjQvdRjmMoDphhPXdCI_6cPvokkUmINxTJBE4a3xhv_8Vb-CO-vr-e_2Zs3jtG-KS2yqQ04Tz-h2ldAzqbmKHHTafv-elNFvT3N5ozOx3bS5Jha4ZDUQTOSApovchK8E7wk6r5g011xf9h4nficxU5KxN7YC9KLZLnadDVVEXJKzuiZB_iOKyM_AYDG3YpUR1OizQ4rk6HKj0T2tgln0ulicTNdRpRkfJdK6-_vooXJERmr4AFcSE9nMlhOBvNmm9gzncYhDpNrawyNMdzf3wJB7ugkbNNmSGskt_o0n-U9DcPIk4CsR_xZEzOLkdOdibxTJN3UFi7sSDXNlOwquud9I8sTnjnxEKMkK21i4MYuLIfBl8x_gq_eT9THbLH1fnAjuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=gqwfokU_LSr9GgSV4fw3fThCNeRjiAZ_eHhSAJJHnZn6Zr0gB_VXgK37bc4GhR60hwnMeRdyyPRFiih6fyLbRegKkWmiHa2f6VUHZcK-DSh3U3RMFWt2sxBg2V65ueSqy9CuVxsk8qySqV1aedTBfxBdcKOUe8ieFoIPL93qAncwXIMIZ4IFuazrI3iZXF2bzUuflbYeia7d-g23lKAbNv-mGWVoU8bgsSJwWbvvWcxyy1dkh_0wujT3RNFVe9V3IQCW-EnTYvIj4PjFYOY_jlQpjIFzJfvcoGSgJDTjQvdRjmMoDphhPXdCI_6cPvokkUmINxTJBE4a3xhv_8Vb-CO-vr-e_2Zs3jtG-KS2yqQ04Tz-h2ldAzqbmKHHTafv-elNFvT3N5ozOx3bS5Jha4ZDUQTOSApovchK8E7wk6r5g011xf9h4nficxU5KxN7YC9KLZLnadDVVEXJKzuiZB_iOKyM_AYDG3YpUR1OizQ4rk6HKj0T2tgln0ulicTNdRpRkfJdK6-_vooXJERmr4AFcSE9nMlhOBvNmm9gzncYhDpNrawyNMdzf3wJB7ugkbNNmSGskt_o0n-U9DcPIk4CsR_xZEzOLkdOdibxTJN3UFi7sSDXNlOwquud9I8sTnjnxEKMkK21i4MYuLIfBl8x_gq_eT9THbLH1fnAjuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
قصه سوراخ کفش فوتبالیست‌ها چیه؟ این ویدیو رو ببینید نکات جالبی گفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99365" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99364">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A56CvTuv3CGaDD-LWW9GVm9tXhfZvxbbtWyRLu4217wH9bNLt0p5pZdFxbyPg1xdj1jYWYoSNiD97i2Yoj7i_kQKkFjg0hWcj9QwxNxi2VT7LIbb4MQIhcHEh7m53AX1LWmXY3bzxhZPJ1hkm3TCiAuJgRcE-Do2E1-bPx5Hxscr3gAbRuYUyXhQWSe7zSRxnvbuzewavy25ZRIZJTRQJkpgxFT-XJX8ILQyF5sGozE2tPwspzoOsjrY0Ywhmukgb-oXAZcvquHkwyvumqfgFpPkopBlujk07SYH3406VsQBbVq5Ct8Tm1l-Xn-7HRvglWWZ6u0-3lid27C4q79Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیلی میل:
دکلان رایس به ویروس مبتلا شده و برای جلوگیری از سرایت عفونت از بازیکنان تیم ملی انگلیس جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99364" target="_blank">📅 13:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99363">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orG_akkYKKAGoHKVgOW5CHmSFNbHj2nHXBiBBILgSNv18NS56yqliwYxGaEHBKjrkFYHLghWjKDCv5Gj5fwktGPHsHBhWUC_3xOVjUSfv6sO05DMeYKLPzOePELTTauegW5fv8QNsbZS_E_WBXIjNJZ7-0bFmG--OzxRW-ZwAoY5Pgn8c5guiypDTQxT9WWDyO5N1bz7NnTyG4F63I8UBXuoc4_O-Ebffp_NTeRbXgEY0YNGsPGqlBqHS_mjGf3yhFQNDzeYM1JdcETzF4Of0Dwj8mUiRo860-Bdo-yL88l4EVk3Jqrtgvt0wWRSnrOR-b1wZZeZhfplZ7dtE5qlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بیشترین حضور در نیمه‌نهایی جام‌جهانی
🇩🇪
•
آلمان — 12 بار.
👑
🇫🇷
• فرانسه — 8 بار.
🇧🇷
• برزیل — 8 بار.
🇮🇹
• ایتالیا — 7 بار.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99363" target="_blank">📅 12:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99362">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHO2aREpw7DaPnHfiFHdgAQwy8BN8c0hlKDBOWqaRqXsi3C7s_rRhRGPbUc3wjxSTeKQ3KwljcLmtc2byM924JIyDb5NxnbXNGyolYR9MRQHndPqZDm9hE-PpCW-NaulDP9ylmbLZ5hVudS8Gmh1UiE7vqqHoUe-AFoi2pgxZCZDdxGdIPhie036BDycduXO0EIYptEBRP69pdH3wAUp8ipYXKhnnRTN8jGdQTY7qNwHozaA8beXbX1Auym2AOhaC2-GikNL2STKYDdbYISP3WztCrJM81L1Vxcg_u0tVjHLUVLZXC0lTFvGz6q0gwCRYH3Rew-_7O1fr_3wJQ_3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیکو ویلیامز:
در 19 جولای قهرمان جام جهانی میشم. دوست دارم در فینال به مصاف آرژانتین بروم و با لیونل مسی پیراهنم را عوض کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99362" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99361">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MND6mjZEQuEHRRxTMbDV3-Ti4YhtwaQsQc4UpgZg_X9o9JAKl9MpJoC1Y6IANi5aiB_SkWzTFxwJlCZrTBsySKqly4CkDKEMssUdF8gfIkMOO-jXB8J7rb7WEF3YCEDSAacn73wJ2o20lVdmpK00rw1ZvLF0lFeXAW7Vqy6ee2-FH0nGgDkP1JjSShsGc5tEsT77XvMIduzhTc-Y4ETKoclcBVijiJdS_4OhwVPFaPg22aEvx_jFsjpT5apqXkD0kiFRTRT8SyKbcl_cIwG2ExIflIrpLpuALF8kAIPqgFsKUbwULNUJlWqOWZJ6a-8WGvth-Iggg9_v_MZOf73OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📅
در چنین روزی، یک سال پیش؛ اسطوره، لوکا مودریچ، آخرین بازی خود را انجام داد و از تیم رئال مادرید جدا شد.
👋
💔
📊
آمار و دستاوردهای اسطوره کروات، لوکا مودریچ، در باشگاه رئال مادرید:
🏟️
**• [597] بازی.
⚽️
**• [43] گل.
🪄
**• [88] پاس گل.
🏆
– **لیگ قهرمانان اروپا [6 بار].
🏆
– **جام باشگاه‌های جهان [5 بار].
🏆
– **لیگ قهرمانان اروپا [5 بار].
🏆
– **لیگ اسپانیا [4 بار].
🏆
– **سوپرجام اسپانیا [5 بار].
🏆
– **جام حذفی اسپانیا [1 بار].
⭐️
– **جام بین قاره‌ای [1 بار].
🏆
– **توپ طلایی [1 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99361" target="_blank">📅 12:20 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
