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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 632K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 01:23:25</div>
<hr>

<div class="tg-post" id="msg-98421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0jwZEsDlfbnZlZOSCJZ8qDO1ABda9TL1nhkWgXUT85I4dmxmA8pARFqxUAkAAI5oG8Nb01uZlTUYF6-L7xdmbIrfZjImgyn_z3xqjio-eKoEEnYqK_uZ0OnBG2-a8vh2unAKu2HT3hwzwRXXQMj-Ki1eIOw9UMsz9GhGWGSV6mri7OrypkpchLblXZ8OG_Q9NIU9Jf4Sfl6Lpm8prL1Fz6tSpt9-vRgJSDeG__51BPhjqlOaQLsKEUjgPg_RVclEvnR-MSc_dK4IUzSaOkyhXiC4enLmPNmUUU7MIM8lD6xnsuLkE8nN1IsYNjD7aZJaXSe9thJCvf8aIsNjODROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AUUUURRRRRAAAA
🥶
🥶
🥶
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/Futball180TV/98421" target="_blank">📅 01:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تیمی که ژائو پدرو بهترین بازیکن فصل چلسی رو دعوت نکنه و بجاش یه کصخل که از هرجا دلش میخاد شوت میزنه رو دعوت کنه ازین بهتر نمیشه
برزیل پررررررررر</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/98420" target="_blank">📅 01:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f2e0732b.mp4?token=loHdFh-d3Oy10gU7Az9AksMOqICuz7ukc88-57VPhN19VBgDIHdHCOf9qFef0s9f5R-Fx9qJ3M7twY_K9s_7prk3oWPMH7buhYSSzFNxSgrrUU3tdtKoNMKayXkWtB6T4-tSFyxcdnnpevQxp0wgiO0Sv6XrcQrxq0jUP14pp-SAlQaq_96TJKUmmdydjKtA2GVmTNT9geJ4Qxsy2wVESnM-Zlaferfq-Tzn09DH3QbMu_DcrUYVidM_rLohEtl377zdw4GoPwnkCxA8YFLGqowHRQMyg72rjk0gnYG--j5xO0B6V-1ToLUk17cY-zKXhdhy0aS_62231_WQiRMs3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f2e0732b.mp4?token=loHdFh-d3Oy10gU7Az9AksMOqICuz7ukc88-57VPhN19VBgDIHdHCOf9qFef0s9f5R-Fx9qJ3M7twY_K9s_7prk3oWPMH7buhYSSzFNxSgrrUU3tdtKoNMKayXkWtB6T4-tSFyxcdnnpevQxp0wgiO0Sv6XrcQrxq0jUP14pp-SAlQaq_96TJKUmmdydjKtA2GVmTNT9geJ4Qxsy2wVESnM-Zlaferfq-Tzn09DH3QbMu_DcrUYVidM_rLohEtl377zdw4GoPwnkCxA8YFLGqowHRQMyg72rjk0gnYG--j5xO0B6V-1ToLUk17cY-zKXhdhy0aS_62231_WQiRMs3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇳🇴
گل‌دوم نروژ توسط ارلینگ‌هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19 · <a href="https://t.me/Futball180TV/98419" target="_blank">📅 01:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🍑
🍑
🍑
🍑
🍑
🍑
🍑
هالندددددد</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98418" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پرزیلللللللللللل پررررررررر</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98417" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برزیللللل پررررررررر</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/98416" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هالند گاییییییییییید
🔥</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98415" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عشققققق میکنم با دیدن بازی هالللندددددددددد</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98414" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هالندددددددددد</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98413" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پشماممممممممم
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98412" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بای بای کارلتو</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98411" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98410">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98410" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98409">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یا خدااااااااا
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98409" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دومییییییییببی</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/98408" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نروژژزززز</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/98407" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگلگلگلگلگاگا</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98406" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc_coRpdDAyl_FsJQ0kJO-j5o0j9cL6nDhnwH-58g9-1gJXHttXnqeXEcVcu6inlg_fh-WmF7gTZrHbOA12GBIwzZm6QZkr3ihp_xE6uymNWGRuLg5EgAq4uNSl10ORVBIp0sTw8FbzWuOKYxShjIj822ZPVUi2Woc6Z8c-GubCj8sVDodssXBig9XM-VppztDvGiO4xFXwG0c91FynrCydvQTbb4i-w6pmlY9Sxeb_NVjTpkPhE5wke2xWKwqzGNJC9egASecwPzfIhCmH71dRiaua4yWB_vt-6aSczFMkjSQKRy-ykxmMij5PH86Q7VIYAuxaOVWx-0O7DOgq6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
رقابت برای کسب کفش طلای جام‌جهانی همچنان پرقدرت ادامه داره:
🇫🇷
7 گل - کیلیان امباپه
🇦🇷
7 گل - لیونل مسی
🇳🇴
6 گل - ارلینگ هالند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5 گل - هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/98405" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برزیل خیلی فشار میاره</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98404" target="_blank">📅 01:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6cU1nYQ7vq_7810jJepFBp23_48umWzsJIliNdlvVa7BobC98AR1aovVHJYdNu8kjyH4_GSwInjBMMKymGULQoRIVOMMb4kJRsdc6vXkGfIyWoyMedYk_rot42QxP0xQAnwbiMYnE0tAhsjkEywaCqG7B09cWE3fFR6UBddoWpwCXLVPY7YDNyMXLeZvcMeRJZvIpB0zppBObCIayRL9kCu7Hutgm9q-O8Ql1hoR_b7uprL2j-oQJsEZICRdO8VUzVxq7PC6m_7557iiQ0lQhUjDlsm3-w4lIT6uQpWSxf59wFL31Sk7fA0Rx49_O7Gzl1cWeSKrCLVr37bfWq34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر این گابریل رو انگولک کن آقای هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/98403" target="_blank">📅 01:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واااااای چییییی گل نشد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/98402" target="_blank">📅 01:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/698b2b9218.mp4?token=ohgx7GBGGNj0oYMdT4NLaWmkMYjyJ6pdVUxpMDWQkuxyuNjYeKgvgtqA5m8B3DQRVT1_7sa2iVdinWLjzhk9DZHeJ7fU6fFRQeHHe_Ay9UqczLRtoxquhK3ofrVRPYvG4Isruxg8JH5O3dEfwMmGEvV-wGckydOASj-DpQMnAc1qSwZk5-upLGfJznvgIb5SY48NYGQzq0kkskMskTbntRNxdguq3t7s6Fq-J1fnWhn9iNHQMvqXDwtkuhVmIZZVgZxsRUbCCbgAAKOWKpbSiNGw7F36Mn7D_ta3-0WZYRR5IV8P5yG6gDVRq5ZzGKqOkgB-AJiWJAT6w-EoRhX6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/698b2b9218.mp4?token=ohgx7GBGGNj0oYMdT4NLaWmkMYjyJ6pdVUxpMDWQkuxyuNjYeKgvgtqA5m8B3DQRVT1_7sa2iVdinWLjzhk9DZHeJ7fU6fFRQeHHe_Ay9UqczLRtoxquhK3ofrVRPYvG4Isruxg8JH5O3dEfwMmGEvV-wGckydOASj-DpQMnAc1qSwZk5-upLGfJznvgIb5SY48NYGQzq0kkskMskTbntRNxdguq3t7s6Fq-J1fnWhn9iNHQMvqXDwtkuhVmIZZVgZxsRUbCCbgAAKOWKpbSiNGw7F36Mn7D_ta3-0WZYRR5IV8P5yG6gDVRq5ZzGKqOkgB-AJiWJAT6w-EoRhX6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به برزیل توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98401" target="_blank">📅 01:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برزیییییلللللللل پرررررررررر</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98400" target="_blank">📅 01:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برزیللللل پرررررررر</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/98399" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هالنددددددددد</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98398" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گللللللللللللل نروژژووو</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98397" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیمااااااررررر اومدددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98395" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G672myeAEWNBgrehHAIjzQsLAgD99Zga15DwpMPr4LpRiqROo-h-UvgYDNdMq3WlaN2Lt07_U8N7FT3xfu4_rJ6H_cZxdymqyWTBFL6JH8TZEraV2wTMyVOZIhaYGxBRvfyR7rrCe1ZKcsgWLf4SAllNzgZ1s-_wBFGfyMGLNftL6W_-IGYVAr7vT-MS22P_xDPH6SA7g9NBEZ4wFzhpRUkwNBrx5K49N9KjSliNQ3BspGNft2ID2NJtaj8TyP0thRZpTu6njdYxEA-x0_7uLLuD2YRb0VUljfW9Zcrt4QdtsSYGHUXSxlWRDIaUM7NRPLN-eF4KZ9d2vmnlY_10ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اندریک از بازیای بعدی: مهاجمای تیم مصدوم شدن میتونم بازی کنم؟
🔻
واکنش آنچلوتی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98394" target="_blank">📅 00:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلر نروژ واقعا عالیه</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98393" target="_blank">📅 00:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98391">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qr0rl0ittwmc5tuWd0USpGVksVSQrA4soZaiRq9hKMImUx6LVB_bkaTUciZX3rXbngfu5VsoJ_C2QZJjH4U0RcrbtGXi0spC15TA3N5a8nXxu6YeUEG6nAA-HN1EaHeyjNuKC83aBynbczo-5kOV5Ug-LuBddUlQw-iJyvasxmXX6Unwq5ghczJ4sPv38c3fwyBl_r_MiGTq_-nNa7y69nN82PrgIehRjkVVAlQ0J_5pFODDwKFeOcctbu40y4VcvIHemO20udlvH_7DhVfJ4b4mYQXEQjSc27o893BfnOr5e6_IjAGgGViN5HzoqhwvQcj8FjKCjpKJhdEER_DmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HilMPmp_sBbv2tLpaaG3it3D4U6hX7zfzYtmLSlRzsqVpIZ0oT-xV9cOjFLeKwWjTpe-b_eQqsbMpxpR1Oej59xkykW1zllndmkUmcwVEtQ6OngeGTg61J6vH-7p8JFA0rzomMliKDATGYcqKX4iwd-mYGMPSfpsyGLF3DTGeVY-L8PVxYWFO5kJsm7dPGaHdoZwY5J7occHlNuvvT5goAaODkO6cCPHsqXbRt3FVysIJV5XrSZX7SfktvRgFvles0mXOKjuReYrTh7hJz4qnOZOchiPUnSUEeq2scNwV5W2Fe7A4VB3gda11z0nfLuB6FhPoYXYgmoGF9naVN53XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عجب تک به تکیو رید اندریک
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/98391" target="_blank">📅 00:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98390">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اندریک واقعا ته خندس</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/Futball180TV/98390" target="_blank">📅 00:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98389">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این چه شوتی بود پدرسگ</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/98389" target="_blank">📅 00:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r113skapO1s-QSiSKRWKjybIMm-oo5pMMo6W_Eq-7OtedQ8M5iWC8HV4c1G4hXBYcdXHoUaM7nYpWEWhZ8Fq_761M6p2faHNyPFnIkU3h0_0lpO9f15ekVAFcSa8Q6y2DCYVCLP6x3scZvFAhX5R6Mdal4BVWmosBY7gvEgefnbNTUnaLGk6cBZiTlZZ7M-pclk1jwdbLEFMiw6-Jd8oXGQstoo35UBaCpJg0GPNvvB9DWffbVcxDFk-u8sgcpp7ZBC3vHmH9LEf3U8QSlhBG0evsKHgqJRmuy7td4FpHdp3dZ9zyiRFL6siu1lt5dWlB_TXucbsXIDfEK9DRqv8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYqx7TNFy7C4vxf-NQUeA7ngckJSqbnW17wg2siqgj0WdoVZAJfOmdB1mvC59c_F3dfNjRKebd4gzrFBC4SzzfPxjp6knUMCC3gNGWIxiVEg-u8B__Vj5JP-aKN0JfgneaqweafEdOs4PIsGp1W1gX4VhnS4-AJGWKOypK0N1pCtzlutwLiMnQse__qzsGZ2jzsZ9chSST62tATumtPBbasGwHIi4SHotruRu4sdwSfUgOYFfEzasY4jxDgigIi9QguaI8YRIjd7XqgWp5B5DkP7kwAaot2w0TppMGc1QZHfiOE-_2kHHycTCGk3GtsAb_lChvs8A45WgxgS16qP2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سمت راست : 150 هزار پوند در هفته
سمت چپ: بدون تیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/98387" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عجب کسخلی بودی و هستی</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/Futball180TV/98386" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وااااااای چیووووو رید</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/98385" target="_blank">📅 00:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اندریک اومد کارو دربیاره</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/Futball180TV/98384" target="_blank">📅 00:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGBxTpLjgh3Jn1EKjo4wdSIjKvG9kHLrAukVmXzTsrqAgBRZanTcjnwaCKOaoiq6TcinPvsiJhPzT9TK-fpl77V4BpQJce0ftIGD3Et1DSw7Fp0449CLo36W1kvZVOa6LaeRz0nNwr4K1tkFn6p8rIw_6mCQ8i8nHUIkFqMGwBVvD59rVsKg9HrEoArbFbDDtggsTJFdwAGMEvUsBnjvb9t8dzipbUjyHmbGhBpjonsIoAZIgPFs9fiN-31_TRhYjfnlg9aNBeKqNx3SvMJ7FF9qFesDO3CfaFsI5p9fyB1APWSpvqSPpgv_Zz52txCWh_qwKfBfzNaT2H76Q_02Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLSRNHUeg44fFcFXTmZcNKwcrsBDJzsEOkRwcjdVKVXcPMnhe9rDtBUO_RIxYsd0159EaUA6ImKxBs9RK3rknlfFZNzF4QBak4Ks_FeFN3_MIkJGzzRstE9j4wnxp9WHqLxJyUFhGHWLo4-Fspeo2qk39YYy_GwymAv32hsJEU7ImL6vcYOqryIOJR5BzxkaVmKfPZmFIHHFJjWbjlzHv61uWnQQPpoPp_L6LuiOmSHuHlopGwqoeleS40ScWgqSK4HDEFvKf3_6o1jIPcUZk2O--K48IGxishBtDRJqyOJYgJFNKJztEcif1sHOSQkU9-my5dZ2nkg9lRh4EdUoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcbhWcIOZSdOn0dk4S8M8bLT50XIhHOWfjsMaYhlnC11hjGEik21q2MqHlSjdsiANy3kWw8nv0szoJroA71TpY1aL5WiuG0CyGfxclO7O7SyaiSO1RVmpeSDL-3r4PQ8ezgFd1n0_ICmckkZtQfxMNrdCNyiGRnOf4hrUmtyiIFoT_2RkYIHaHxOYDpgwqJT751y-j8fQGxKUeaWO2q0El8Jyqh7lqQ3chgf_v5qKXaG9St0aSg5Stz-r8qVwf4Il9QdgUvfD5J3rs4ea93Ltu-67cClrtMOk_IipB8TstTw8wN9ItemCDWi2o4ywjSIIUpM8kg2FzC1oLepdA35Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز افتتاحیه فیلم اودیسه نولان در لندن بود و بازیگرای فیلم قبل از بازی امشب انگلیس و مکزیک با کیت تیم‌ملی انگلیس که پشتش اسم شخصیت‌هاشون نوشته بود عکس گرفتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/98381" target="_blank">📅 00:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/98380" target="_blank">📅 00:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پایان نیمه اول
🇧🇷
برزیل 0 -
🇳🇴
نروژ 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/98379" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پشمام چه توپی رو گرفت آلیسون</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/98378" target="_blank">📅 00:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igZtKM_QDsAuBzOLw0jyOSLlGFHB9UxEQ8gla2yTPvOyDtWnXUuEDfG5AuwcZS7k4zNKsHpWYYAhZB7OlruDzXm6VgRHOSdhbhFcHyoN6NfsnGerKS8VcawGpuqojhuFBTC6JiEp0lcUcYNk8vWuYzFlnump39azamd1Go_GqzwwOhqiUHYXPi_HU4uyDzjSmuBJZJPdOsIyZp1Aj3flUvtY01LZAQFX8b438fP-g_cUo3kNspBVtyBRz3u0cqS8J2bG9d-hjBb7r4iOYsG8SHlLcjLqj_sn_ZsfsKOx4BDB81gbkDWXaRq4IhPaYe4a8LK0EpYGaRA-Tyd3aLz5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98377" target="_blank">📅 00:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98376">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8883504b8d.mp4?token=Z-WH33FYhrivVir4UvgcaCqEvTElH5opXQEYdazP_d8Znw8XpcgD3NMs5GEVUffnfuAdkqu-M7o1dsurDzSYGVrwAMKwgw7FMfKMVLzRwVKRmpc8w_o82JY_x1VXSvKNrc1FJIUT1xrLEqdOTrzvRjI7bJUGC1me1ma0_6lq5PFzgsCn3yttHjPhq_v3TFWywizBXVJ4PNwDYyKd9-ha4Wg2mMXMjHu1YTr4ZJ4UF5l3aUBpTfzNsGqsN4JOCWK994HLZaXRfMDylOeIpycr8N4ZJBgEVoKtP5Pix_T4ujs6V0XN9apvKJSocabxzxHxSDeYdRkyzlCDVQ6N2DAUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8883504b8d.mp4?token=Z-WH33FYhrivVir4UvgcaCqEvTElH5opXQEYdazP_d8Znw8XpcgD3NMs5GEVUffnfuAdkqu-M7o1dsurDzSYGVrwAMKwgw7FMfKMVLzRwVKRmpc8w_o82JY_x1VXSvKNrc1FJIUT1xrLEqdOTrzvRjI7bJUGC1me1ma0_6lq5PFzgsCn3yttHjPhq_v3TFWywizBXVJ4PNwDYyKd9-ha4Wg2mMXMjHu1YTr4ZJ4UF5l3aUBpTfzNsGqsN4JOCWK994HLZaXRfMDylOeIpycr8N4ZJBgEVoKtP5Pix_T4ujs6V0XN9apvKJSocabxzxHxSDeYdRkyzlCDVQ6N2DAUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تارتار: قطعا در ترکیب پرسپولیس تغییرات باید ایجاد شود/ به بازیکنان جنجگو و پرتلاش نیاز دارم و از هفته اول یک تیم دونده و سختکوش را به زمین می‌فرستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98376" target="_blank">📅 00:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98375">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdfvVJeYs9fh72NYYPxQlOvnOawBwq_hD_7RY3eRRlqImXPBVRl7ISg7WtT4MUcl3j61nLMm9XvKArJLdpLhN8rYPTh7vPqe_U6r9hShS1Ensakr4boCDNF32mcLtUZ_zC0BVkqMM0xh13yEBG54LzXGDdbytnfWIO9oM2IXu0qzNYkFfOGWjjjT620Ci-9lPQ-PRlwdG3WawiTIg_CB0WUkPD5CN4M2o40pIUXhrzxg1OxuE2ksE-XNBU2x9IFBH2W-Mg7vjoOqT1Oqq8UUtrajbFpFo1sZoH6-wGxcRXdFBJw4eLSNNQEN9NawgK2d-hWRwYuwUTBJSw4luBtxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برزیل تو 40 سال اخیر جام‌جهانی در جریان بازی هیچ پنالتی‌ای رو خراب نکرده بود. در تاریخ جام جهانی برزیل فقط 4 پنالتیو تو جریان بازی نتونسته گل کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/98375" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98374">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دلتونو به این خوش کردید که کونیا برا برزیل گل بزنن؟</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98374" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بریم برا آب درنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98373" target="_blank">📅 23:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRjlns5fjocBhXr76mdifeIAq1uN5Z-Le44B0QES83gx79d4QHpJNRfWGuO2LyT1XNUODfjSsAVTxIdhN1zvM-P1t0VfJTQ9jz0HQ-xODkxuysSuWhXG5PytMKQiXTSB9hwNHKW3N1gog0vNGKfkzvuEmdkXTal64Hm-cntmFS67UoEdtePQK5thYDAeQ3-I13PFMjy3fDhRdPBAlMr-_5AAN2xQuTxO6_p6ol8ES9ocWrf6FbarSTNjEhk83fyeF4SmH4u4yh2ppgZIKs4_EJiXsOS3qupp2RVgDtcyUvcfMFur4IsKB4HrumKbomcY2jSI9evWUjK-HK7MFVWCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که هوادارای برزیل از اون میم معروف که جدیدا ترند شده آوردن ورزشگاه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98372" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98371">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjRCOtwCSc-rDBE1F7FndqC468UGOtdO618mL3V3pcpsDIcreo-ydEdukwT81JjoKk14v2npi_hEwB192j_LORgCwsyaU6HbM-OJgkXvvtmWYuZAkx-Clv6KqDGMhwWqYBnpmtGTCo7sqjkJFd3YXXnF05zY4gAz8fscPAt-sfwuXm_Py4vg3PhTxnuo5eiibQtrL3jeNWGNY3mD0otOGzjteXGdAISZ-6o2oM-W9UqVXzCJbWRhhfjm5jDvT3XZ3OBVxlvzEqkw1wuych1qD5qPBt76civTOYEkxaTozxBqNFlL4G5OlwV6zpjZEQwfttAWZe4b2QZ2NYqVjnLj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی که گیمارش خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/98371" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98370">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84350ae9cb.mp4?token=Nb7hPtYuVzRNxhfEbM953yepdxo4_RsTnTAKDDsE9p-Sn-WRxw53SZweERSqOhgvX4AoyIHVgN3cVkNvsXPwI5lj55CWJ61PWUeRnKghSfrN8w5b20QmieloN4c0LHujINLIy8B1bBMXhuzj2MxtYI6etscIp1F90uflQbrDn3OwKk67O9_glJKSSx4fU0MuvODRLgXUJH_AEQ8iHwpRSDtiuRfa8ehxylPSK-SWXJckcdFm4fBiaXsSDVBa9bptP-S7tcyReiqghDl7MG2nm2Lmhb0N_bOLXH3jxELvhqR8_RSR0p1PGSW_ZUA2SALj69kYOPaEz_wCCvZpJDbgWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84350ae9cb.mp4?token=Nb7hPtYuVzRNxhfEbM953yepdxo4_RsTnTAKDDsE9p-Sn-WRxw53SZweERSqOhgvX4AoyIHVgN3cVkNvsXPwI5lj55CWJ61PWUeRnKghSfrN8w5b20QmieloN4c0LHujINLIy8B1bBMXhuzj2MxtYI6etscIp1F90uflQbrDn3OwKk67O9_glJKSSx4fU0MuvODRLgXUJH_AEQ8iHwpRSDtiuRfa8ehxylPSK-SWXJckcdFm4fBiaXsSDVBa9bptP-S7tcyReiqghDl7MG2nm2Lmhb0N_bOLXH3jxELvhqR8_RSR0p1PGSW_ZUA2SALj69kYOPaEz_wCCvZpJDbgWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی که گیمارش خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98370" target="_blank">📅 23:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98369">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رییییییدددددد گیمارش</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/98369" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98368">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خراب کردددد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/98368" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98367">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گیمارش پشت توپ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/98367" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98366">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پنالتییییی واسه برزیل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98366" target="_blank">📅 23:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98365">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خودش رفت ببینه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98365" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98364">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پنالتیی نگرفت</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/98364" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98363">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miMDrKIDEcL_Rc7Zr-b8zL9YkXByDB3ZQ979R4PO6E6GTSodHZ-ADLfquWxYx7hY2m18gdnHQcY3cMAbn1A1mIkRSAj_PsBK_HMOsls9gzRixSq7pTyHHcclrTpQ8EvEweA89qLzSZJBaJhkPC4FuQSEJDo-TiCWJtcrJ-lJIr6___36rPC-cv1GskzK_bjgE91nrOjZjNVpE42HChXWfCVZm1mHPferJqt4I4KDoS3tsq3mTHOLxNxzwaxV_68aku_PdFhtbZuKqKWzTghXgtQP5gOn5pbORUJoXrC5KPPeKRLVo8uBBddZecPg3H3kvrdC0fjG-Ql-gzTzdV8KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98363" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98362">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee365e6e16.mp4?token=GDuJF7Jb_H5WSuvXRD1TSViGNAe9cQF1c7x7jLGVdv5RgGkNvnq_hz8XNmTrmlf4ix-RGOIZioL9nwEms5WyYswzT44JglX35scXBpfpnqw0UIaKK7CocN8ixqU5lRzStx6fio_kwQkKYI3J1BXWpjBv3zLH6gVer2-3pZNa2X38G_sLBtz4OxcSUX2J4i4BcOBnZ83lHcgpPaLNurTJk7mZWpm6hw5xVfA6t1gLg5k0kaDu_g9uAO8a62rHNzOwSjHrrLM8QKUjONspuoauyewSb60wPDxLYQ-yOZUHijc8NiAaVsnCO5HatZ2x_2JdeNc9yWwXRgF6wj8ro4309Utn8xzyqIPXNKt18Duc1yCLf6KBnh7miZV1iy7tsWkYXtfm52WVUrBAeU1PZlQ-Utm8-jCXPPwQrxRPySyJxhTUvMLPmQ9TL-iHxrpSSd8R6Mqcxys9gPt-LTEt15cImaRDpM7s5yp1Dc9hqj0UqMaft_rfxrSEfyCEu_aTqYEF_s3YaP2gcMCZXKoEWZtNJuWYe9YsPRj82qu6vWjcMkhuKufblc4_2RHermLDkjwmlBFfO54l8XmP1XHvvRT6JKslox82WTYB8i6nmMgbFRBe3FkQCMh9iE_QO7ZLPH7-1E23A22wkW88kWoGHN3ygxcwu-vLDAOxiahAdLYiA3k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee365e6e16.mp4?token=GDuJF7Jb_H5WSuvXRD1TSViGNAe9cQF1c7x7jLGVdv5RgGkNvnq_hz8XNmTrmlf4ix-RGOIZioL9nwEms5WyYswzT44JglX35scXBpfpnqw0UIaKK7CocN8ixqU5lRzStx6fio_kwQkKYI3J1BXWpjBv3zLH6gVer2-3pZNa2X38G_sLBtz4OxcSUX2J4i4BcOBnZ83lHcgpPaLNurTJk7mZWpm6hw5xVfA6t1gLg5k0kaDu_g9uAO8a62rHNzOwSjHrrLM8QKUjONspuoauyewSb60wPDxLYQ-yOZUHijc8NiAaVsnCO5HatZ2x_2JdeNc9yWwXRgF6wj8ro4309Utn8xzyqIPXNKt18Duc1yCLf6KBnh7miZV1iy7tsWkYXtfm52WVUrBAeU1PZlQ-Utm8-jCXPPwQrxRPySyJxhTUvMLPmQ9TL-iHxrpSSd8R6Mqcxys9gPt-LTEt15cImaRDpM7s5yp1Dc9hqj0UqMaft_rfxrSEfyCEu_aTqYEF_s3YaP2gcMCZXKoEWZtNJuWYe9YsPRj82qu6vWjcMkhuKufblc4_2RHermLDkjwmlBFfO54l8XmP1XHvvRT6JKslox82WTYB8i6nmMgbFRBe3FkQCMh9iE_QO7ZLPH7-1E23A22wkW88kWoGHN3ygxcwu-vLDAOxiahAdLYiA3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تارتار: از کودکی هوادار پرسپولیس بوده‌ام و به عنوان یک سرباز تمام تلاشم را می‌کنم که پرسپولیس موفق شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98362" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98361">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98361" target="_blank">📅 23:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98358">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلللللللللللل اول نروژ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98358" target="_blank">📅 23:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بریییییم سراغ بازی جذاب برزیل و نروژ
🔥</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98357" target="_blank">📅 23:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF_SbUUXvAj4GH1Yi9xcCqfTXJU7BNNUwWZDAmBn8JybkbH17OWu7f2mSUs7r7HAsJ7IwiL0Tar1rtpOI1vA-k9e2gugukP9WVMepjvWlg6mUAW36MgCd5jCeUYW6bZj0D8ZRNC9I-AYB4tIoGwCsaljad_Be7vFRfeCXVeWP-pSzljPy94FlZiFWDPdynFwlqRyQGrYLOgALKF8e5G7GAiVndEssLq_079pMYSP3070sLhwfMLN5Eyagd7qwBzCJNNoCChPHvd7BgaixOZrA3Y_has3HL4ajQ1VMRWZOO58JkYmN6D0SjFYh163Aw-nxQnc9B823ysM_ENYAC3cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پدر ارلینگ هالند:
شاید روزی انتقال هالند به رئال مادرید اتفاق بیفتد.
چه کسی دوست ندارد برای بهترین تیم جهان بازی کند؟‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98356" target="_blank">📅 23:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrACBxusC_g45iarAfNxAHqtWxsacpJ_HgJsKz9P3j-t2mbc-BbPJjiQ2JCMGRi8ZEOu9BqWlpNi3LyndrbfMioFnMJjhvs4akOj9769fM2LtlHgjg_bOGSUXUEdwGIdUChsPy16zhw6TE7WRrzxSq_TO6kPISPP4IPwLywd31mAJKdwocEg1vhfHw_7rMwCswm6zKNXXo_HCS5yeWwKTOtbaa_scSD5TCfWGazWsvVCW6765ZXezUe3rtKNNW0DbIvw6woVeq9csiQXlircs5ypqd5YalCw-PLmb_f8IOU8hTPnAG_bK_kZLHeaQ1T14B5bY-DfKyFdr3xRQdDY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD_wRfKVPCC_nRcQw3cvbr61vJfZTUottLW59Pvl-MYzE6dP0VxZK3o9q_U1Q810iXnDwNAljSyJvqgHjVuf5y4CPE0O47V3zAHtFb-Z19AOVockqdelI0CysWXpJLLr-6JKKD8wjLetFbxlhYGpEA4WsqN1wCWnoOZbsKU7VzDdEcWe8RMo1zKD1e44JK5gmop-jJn9BLOO_IBfYbOv9_pWm05OgLTB5YYfCiM88h2MEhcYdM2z08YR5CUEHyx6np4_VOCh6wlfv-Kh4KfonlFS-TNPKAM805KZum9nRXTMWEx4oDzcxA2baJn5teHCUBXPnzY7keoJEIEbwxpWWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
📊
آخرین باری که پرتغال و اسپانیا در مرحله یک‌هشتم نهایی جام جهانی به مصاف هم رفتن، تیمی که پیروز شد، قهرمان جام جهانی شد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/98354" target="_blank">📅 23:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddtdYqNig7VfFPx8fC4RNcgFBfWvWuvz3w9h_--mytznaseqhwEcvN0Jpw_59brtVtsTbfsVa1h0cShThi_YIkUJC5COOESqX8PkWdktMyG43NHgANzwgm0jdP-V2SbPlWlnJECczuzEjVgS2A9U0D1jQ0jd30HKpMw_mTnvx20mEP7AM9IqxF0p1MEk3rOMYeyUhnbvFi9SKJTmpqr-fTAdWvyx8jFb8sje7I027k5vG2lMidY3dpZncrFNWe5OO3Xm0P048rXAq62TfG4Su2ACdlojta1EBAX5SpO9KeYhCabwP-163WHqEYbJQBEzLu5hlTLNs846oCEyLh5FsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مهدی رحمتی سرمربی گل‌گهر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98353" target="_blank">📅 22:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeXgW2sik8UdZazHNH8H5FjXlQi-nxDQ-tggNunfLh12hnQQ3daUC5yZhpuvr7Kw0meYW8BjFchYZ2dQ5qgdTgSvSEwjH2mAId8NNBoU31ttZKKzSIyGQCdbpXaWiGglEf8NeJmD4BleA_RVueovk5v48tk7ZPHIf_FDKFY2QaCDO-ibhPAzzngbwox-7o1kBxp8XchJEWbg3wFRJZDN_EtjHiTUfqMEpSUla_5Z35-lC5FcWjbrT_ap89Adc62I1YlfSxVzRa4svhBCshSVpNf8rVHG9pTl2YlkPNalpYLHlRQuNsTwBRNlMLh32CBWAuUO_jWWTq1uyyt6BxdOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bF99ZlzLxljdXp1ZfJxOO-VJ26DLXfipe03j1Ed7CbiOh0RNpgrTzBAgoOoB-C6ufKYmUDqSS_YATn8-RgxFnSqpKN2xIber-haEnn2H6j0CZAkmnAA9z4Fh7-CEk4bJlAY9qTjgeCQhINDc0aXPdWTQvIbTDmCC8HCOvIu6QiuU1SnNcR1WqxuRouODlkFf4oWgIob6WFRavefSmZk4ohlWlkdVXMTNAgJ0USIu1gmDwimLrPW1f_5xRsGBGa4Z1KS3xDE7qJxDszzRgDZe1v_kiYD8HtkCmVpcSOiCfZ9P62j6Y2jTziQDsRtskR4ZJ5TxKKpQFwWj_Uz8tZX2mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇪🇸
پائو کوبارسی:
همه میدونیم کریستیانو رونالدو کیه و چه کارهای بزرگی برای فوتبال کرده. اینکه بتونم کنار همچین اسطوره‌ای توی زمین بازی کنم، یه خاطره فراموش‌نشدنیه. دلم می‌خواد پیراهنش رو بگیرم، ولی می‌دونم کلی آدم تو صف هستن!
🎙
🇪🇸
گاوی:
اونایی که از کریستیانو رونالدو انتقاد میکنن، معمولاً طرفدار تیمش نیستن و از هوادارای تیم‌های دیگه‌ان. هر کسی که کنار خودش داشته باشه، احترام فوق‌العاده‌ای براش قائله. معلومه که کریستیانو یکی از بهترین‌های تاریخ فوتباله و هر لحظه می‌تونه نتیجه بازی رو به نفع تیمت عوض کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98351" target="_blank">📅 22:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇦🇷
خبرنگار آرژانتینی خطاب به کریستیانو رونالدو:
🔺
من آرژانتینی هستم، و اولین چیزی که می‌خواهم به شما بگویم این است که از شما برای همه چیزهایی که برای فوتبال انجام داده‌اید، تشکر می‌کنم. همه ما از رقابت شما و مسی لذت بردیم، و این رقابت یکی از بزرگترین مسابقاتی است که فوتبال در طول تاریخ شاهد آن بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98350" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrIfDKTRQXVQ6H3S-O8vOCW-9rJZVJs3CnTDsvAYw5raf-NgWjKZpiwMpxCe2r5BB6RNmLkkXa6HKjmlx3m6IJ4wDS9yA7BpHsdQRxgdwPBkXaPGyWpiE8sbdjxzzNMHkk18kvhcvEhpvD2P6NzKIk7OdsIjulCLvG7JHmuP06PdoqXztjwrCBykba6Op4_tqqvowDx42K3bjET9wT7rhwOyieUxYzAryGx8ztB_Z9GCzX1j0i9-OkzNmM1-3712kNqHpDJa9PbqJ_BV9l3UNVsZkQuPNI3u68xzprK4hOUT27l46iFWGRG8cVLx1VxZe4KKsuMy5iElg3Ewq1NVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
ترکیبببببببب برزیل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98349" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRMW215iVr258td5lTF3jaElxW44nI1H3c0jI3O0uGSLkaZeFtZHkUiFoyQE35QgxstzhmFqXhBv03Hg9ug_rJPUiehNAuNPBSHS-kP_2NgKchLm3Wa8YDLixwuFaLHRrx3-ZZyrUwHbuKHI5ezW5zc_OpmjOllu90KpOsdL-Zk0ekLAkfqLVqUBUlEjZ8u9EWt36eNFpQnHQRF70mlt3gCRto97VTFOqqPVs9D9sXKIhufzaNOF2Gpn-LAXdUROACzwBIvo2R6Q1zXfztTQITjIee9uY0T7Zq2hXQZDuZWOxMSLaJSadWq0ytzqu_2vfcVmwZkk7KODCeFJqIBgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
ترکیبببببببب برزیل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98348" target="_blank">📅 22:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTxjXyY2oMwlQ3Iw54abxbMYxW8haKsJe0NzhWE5xOvjAKMBU7J2oWieGb-rtR6I9liEO4sDPfobmEfbz91Q3ZkWx4ttnX5sjy979qcJIiK9y7-BKtVkX5AC5Ic-nx45pRIQ12bFpt9LWTS8la_jZGm3c1cB0nYehyhiDU0FquNQS4nTjkEX2fQFy-N2aFgdEwbAguWPL8u8bk3jBuLx_oaH2_-FNBTu-7SD4wxkeTAFZHfby2ZTBhhlg7sECVrBFQpM3J9GoZ92ddTNoHKZKXR8OOWO2LMYgvuZl5KpWWMP8uqHipRyxjIckne7J1u8TLn6VlPeliwJXa0UjP8ZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
کریستیانو رونالدو، اسطوره فوتبال، درباره لامین یامال:
• سوال خبرنگار: می‌خواهم دوباره از شما درباره لامین بپرسم. می‌دانم که شما علاقه‌ای ندارید روی یک بازیکن خاص تمرکز کنید، اما پیشرفت او را از سال گذشته، از زمان فینال لیگ ملت‌ها، چگونه ارزیابی می‌کنید؟ و فکر می‌کنید پرتغال چگونه باید جلوی او را بگیرد؟
‏"او بازیکنی است که آینده درخشانی دارد."
‏
"
صادقانه بگویم، هیچ بازی کاملی از اسپانیا را ندیده‌ام.
"
‏
"
فقط کمی از بازی اول، یا دوم، مقابل کیپ‌ورد را دیدم، اما زیاد نبود.
"
‏
"
با این حال، همانطور که گفتم، او بازیکنی است که آینده امیدوارکننده‌ای دارد، عملکرد بسیار خوبی ارائه می‌دهد، و فکر می‌کنم آینده‌اش روشن خواهد بود.
"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98347" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDN3uqE8rHSTIX1WAZH2QPC-gYIqO80kHO04N041_iavjtlH5cCG1WQBOlrfn-UHSZtdmH2KqS_VmbgH3pcOijVNr3CsDvnIBptWtTbWxXP7JqYt8zQVKDBJxYbSbO-HKuoK8eNPx05P2Fsa2XNnmjYJBZqjyyK8IaK0VRnvm1-tkzhGfzyoaGuKT1ijh8Osgu3KLupIlYqUNnMeqFH3Ym4Ny1XlXjiucrGA66UneTJAWfxTU4UXI7Mc7e5HeJt0UlKfBFfmVH1gkxdzFZ9VpySJ9sK0KSprarxE7Zd-1bE8bMWdIZT6JCHZjVW2SllsRgd4vxYEGzB69xAJFx8ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇯🇴
جمال‌السلامی سرمربی اردن پس از حذف از جام‌جهانی از سرمربیگری کشورش برکنار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98346" target="_blank">📅 21:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq_dNXbcW9tIwQeSW5u1JYIsy56Vkl6li_78qEXFeeLuk9NZvjM6HWzWxDybMCcbNkA9cfiYVEUiU3KcHcVZHZuuXSLlGSTbFKM8uTCzwu2JWUYj8KUKjB4M5AgyZM6D5V3FD3CkeqSPa8cDc5mc38aVg0Loq1eSjJ_IxqZ8HI3IQuQcyq-dVmVoxrtBwwNjTc8N0sXHJ0ksymX89Kp1JhPXGOHFCb0s8n-OmU93jZTmjS8147mt7G3QdEDkWvxKsJ_Wu0Kmv8LFZCzTHhcneHkrasGmAjyUhmjFQ6nkyrXs9cJ3EiUyKqk5AqNBy3x7D0vT8mrjWWsywbqp3N8z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظر کریستیانو رونالدو در یامال:
او آینده روشن و امیدوار کننده ای در پیش دارد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98345" target="_blank">📅 21:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo7ULaN8_O2cWPaekOaFtlh5auYroCv0DnDcD6Z89kqxmV6iWXeuWp-105KCG9ANl4HvbnXDntpwo1qxlg1vO_Ah4YM-vLFGyOneTFQRirZeYqu3dGgl7csIOKm4ZXzB9PE1qllRNSxwvt-jAwf622X4v_WBvzRSXi3t4v5VbqGVW3WPhWe17LQTfIIrUoHoXJQjs-T99KyDPxPOK1RfNw_AZeWnlEl_5O27Q6iKcPV7OegTSyOl75YzADXwJYFuu6jFZJeTfSl3uZwzUnzstc_OQQFBKhliEGlaQFFLukThbz5fLMR9AgUbRrxRWxrV7zuc9xWHG52cxeSCMr9r9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رونالدو: من زمانی از فوتبال خداحافظی میکنم که خودم دلم بخواد نه زمانی که رسانه ها دلشون بخواد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98344" target="_blank">📅 21:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys_Hc91sYFkFgLLGN1IhyREqBgZ0TYgJ0xRGoHIL93VONCUDcxuUPXkQNxUJNYsNcYS1n3tikOwJ5LjYeN0wGlaV5yPff82PiAAtPG9CYcIqMBkvttshTuVNM2mEE_ID-bMG3J0ZFZocQwZ9wtHLPHgC75UNrUOm2Rgpt2Ff877-JmQnZXT74ul7C7KzA0EdobT9GFLxmMne0V9s0WvPo_exGrG7gxhglbuH4m5zttTWAfDn5b4NR2suBq5ykLG9AqZLFUERqE7_kUpJb-SekHbuUizspAqKxCeLiFGM3gqVAWECdbAQCpUvSiY713A1W_wDzzfICNQuLkhTFPUXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رونالدو: من زمانی از فوتبال خداحافظی میکنم که خودم دلم بخواد نه زمانی که رسانه ها دلشون بخواد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98343" target="_blank">📅 21:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhJ7N0qa7YpP9-5DUmL1ItoJHVJHxPgjBIPPFFK5LrWN6L7cqheN8jlH8HdSfPupoKAvzGKNCZxr6q0_pzTuyPR1tXNlwYzi7HwvLjQPalJTUhMpvBIULXcmBqI969V1CMNRY36Lmd-MCn-Na-OTWmSey1VU2NLoR0GXuRd3_Nf0tI9J-BAOEP82iA4Az3llALuVliaQOU_QNpp3oJX66UP5tycKuQ_iNM7wUilDJH3qARyWbt1szbxjfXboMnsOrjVZncCJwjDbxMREIMT_iLvfRtWIOnu4b6dqaVf3O_-icOho0oUvx3qyoeOC2NAea7hngt-EawjLAHblxJgOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
نخست‌وزیر کشور کیپ ورد پیشنهاد داده است که روز سوم جولای (روز مسابقه آرژانتین و کیپ ورد) به عنوان تعطیل رسمی اعلام شود و این روز به نام "روز کوسه آبی" نام‌گذاری شود، به مناسبت عملکرد تیم کشورش در برابر آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98342" target="_blank">📅 21:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha7dRAk-2VvXO3g-hudbpFuvuhwBwwRw_oF9VvFOJT47UXSmfJBDd9ab1QS5u28LObf9FVNTQc4fYS2ZGPFPn1Gf1oIo1jWORw2dLm9EGPV-VkQb3SwBbkF5kzO7eMJivAkEAlzeWmmgM5r3GmfCB88rE1fvus_JMjsfRDhcmYka5jtdCleYb2Ku_4-PA3o_xv6nN0jgKP7F488dg4VaPFnlDSjIGuSuNr_OhNEd_VYMFpe5Ov0TjIwjF8IpH1IWLn5xAoeRmqkQEMAffNmI7kdCHQBSggvcAg2TJdrPXx425MOTpaUX9zrxu-v_q2gYZjN_ly89BEpzN1UD3W8ZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
احتمالا عمو ترامپ بازم دست به کار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98341" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFjGqv5j0qBl6M_N8uQQdyxCHtuB4VSexsjxFlrVa0__-RihiZqdp-gRn2FpJ2KCCykWGetBag8Elqp4flmKXCYzNFYbjDZMlYfqcOT_7AVZ1XGPcYktnSmFElHzUDVfPz2KXFlzpqmg-aumKCLWktT7QDEdvUuCHVdk045iAZ2JFWuzg8eJVSf1Z-Knizi6NW2_Mz4RaPqebvA4OchHkiX0MY_puOU8qGa9gQ_njly0aQN9aHFiI4gQhE0k2fsSuhf_S4xpIJmofipukgI_2AuhN7OilwhqmbAR89WRdhpbe99uDCwmsIXh881KuQ8_BUZf_kmEx5-viArLacg-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انریکه:
بهترین تصمیم زندگیم قبول کردن پیشنهاد پاریس بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98340" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98339" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0amoO0AIe-_QzSwGZvjF4l2r9DteHpIL4xI2wynms1BZ7ugpASDs5Aic99b15geXEzgrD7Ee4wbYG7dfgz464FnKHyid5TJC0UapVP7O4C3PSKzVem-sB81v9Mlme3c3_eJXjY2hS7DQqaA-7oTF3YC2m8YCLKIrORdQ_bXhElr_wWxyyWYz36-1WijjV9nSnUTm6fy9OOXuVj9lBuT2Il2TWaySeec9GDyGR2wQgguW7qQc6jFuqN2XBLuEoJb6NX_Bu2Dnohf2F8o4boO5Oya3YotRj8gNOi5l63anCkZw2go6Q15PQpiqXVau3yxTvQDzFqkGVmEHRVD4jQ-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98338" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b463de3d6.mp4?token=Ine9SPejCNsV9hR7RjC4tTQTtpTcy85JoGBuQhqgYBLsYfmpt7BiGjWD6_UgvvAG08rzrUVEHk2euWKix-dQF9B9iPyaOj7fW9CrZVzaFbBLtl4-Ty6jYWvLeN_UXIwO3ewcKFMQApnFcIBKfkbvTniZn-ncoqYah6UcXyfJoSzTelCjdi70ZfITdKct4hCPWAtqHt3ErfDWC3q0z50zQr2VvfCHKqOr42LrcwetH-yyDyFVKsPIMVABelOeSkGH5hDHyKLAjvJQHHX77qDuSIxHb7HFDDGgGXHBWvtF96Z1cCni_cjtvymd4WKoq6XvLaoXwM-dqzEgl4MLrznEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b463de3d6.mp4?token=Ine9SPejCNsV9hR7RjC4tTQTtpTcy85JoGBuQhqgYBLsYfmpt7BiGjWD6_UgvvAG08rzrUVEHk2euWKix-dQF9B9iPyaOj7fW9CrZVzaFbBLtl4-Ty6jYWvLeN_UXIwO3ewcKFMQApnFcIBKfkbvTniZn-ncoqYah6UcXyfJoSzTelCjdi70ZfITdKct4hCPWAtqHt3ErfDWC3q0z50zQr2VvfCHKqOr42LrcwetH-yyDyFVKsPIMVABelOeSkGH5hDHyKLAjvJQHHX77qDuSIxHb7HFDDGgGXHBWvtF96Z1cCni_cjtvymd4WKoq6XvLaoXwM-dqzEgl4MLrznEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
سلفی ماموران امنیتی فرودگاه آمریکا در بدو ورود کریس‌رونالدو پیش از بازی با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98337" target="_blank">📅 20:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98336">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
رونالدو در کنفرانس مطبوعاتی قبل از بازی اسپانیا و پرتغال حاضر خواهد شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98336" target="_blank">📅 20:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98335">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaaGVHvQzkjHQiHGtQ06VqtCtijvka3Kv6DQerB9rrWpGYEIDKq0hEoEJGs-iZZ8YNbkaRSAkzfQHXPMhY3Lm_SjaaTUoECQ-P92ld8eUj34dI-SozWAe3p79ufUOiJQXb93bCk183tma0GVRA5kwZyi80Z_2eyHhoeqMA1y4lgU9IvTlMc0drLve7BD1rPqs2KpoPS1IgDU8z3AyO1bgyLC13a65Lal49YqyFP7ZO9I-2ew5006RLAsrAdVjMBCcU1gBUZOvny_BEOadc2F2E8amg10Eh6pRmabCv2DmuPayMZ29w3A5jRlAPbr0Cw-ARTFSRGL81zE2Hvo0lE13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری و #رسمی |
🇺🇸
❌
با اعلام رسمی فیفا؛ کارت قرمز بالوگون بازیکن آمریکا در بازی مقابل بوسنی لغو شد و او در بازی با بلژیک به میدان خواهد رفت
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98335" target="_blank">📅 20:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98334">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW04WFGxa6IDwBTU4ghaBDLiJaq29PUHBZxM2oz7dF9txgacRI32NJueNFcsyGRB92_vNsmCc3pBR0pagTK-jJqZI1p6yb5cxUJuPJT41E1okfSw1UTmlu0Qgqw1IqrFcdmZ3P1NWiR51ar6r_3M5mbiC-r-73VeRAfXPyclBqgSKvyfSmNY2pdGwzcYYsNKqKvOW6l1z71uNMPXW9rJ181FJRKDIi8o_g0po-x2fy1bUIViVm8o-loIo4MJiw7IE1kjwGRzWJgCiVdRaDMIjyRIVBNkz-idXN8ETIs1O-XIY8G2Vn1yr7Ips2BxvaW9WV5Hwaefcdq_QIN4wCa89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
و
#رسمی
|
🇺🇸
❌
با اعلام رسمی فیفا؛ کارت قرمز بالوگون بازیکن آمریکا در بازی مقابل بوسنی لغو شد و او در بازی با بلژیک به میدان خواهد رفت
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98334" target="_blank">📅 20:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98333">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBl0vKiDG8PrQho9fyzQxUhWdYQVq4685yWP8GocJgtRFMBzvK8BEXrm5SbS1aYH1tNjx5STw7WO3udYjMO7fyEDCpyELHr8cSQKaogMZmkw640XwjRjH8o3TbtcpDTYm1XibhSPvMjbfuptcXwJERpSdAj6M-bpKCI75JnHu9KvypXuJS68RvkjRuA_hoL4F6P1oikNxwBKqbcWvEtQyD_h0QTCCYrCTA-uDqCx7LxPgTmjNN3biV_GJYePNQRLosxTWcg3K3zk9m1RrL9mcRP6FXpo2n9diVzgFzE7XcUhpN-_zfivBAXCvaAj_sEImTXPqwkt0JgkMbatKOBTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
برزیل تا حالا با ۹۱ تیم ملی مختلف بازی کرده، اما تنها تیمی که هیچ‌وقت نتونسته شکستش بده نروژ بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98333" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98332">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🤩
#تکمیلی؛ مهدی‌تارتار برای تقویت کادرفنی خود بزودی یک‌مربی اروپایی را به باشگاه پرسپولیس معرفی خواهد کرد. شنیده می‌شود یکی از این گزینه‌های تابعیت اسپانیایی دارد و در چند تیم مطرح لالیگایی عضویت داشته است
🔴
همچنین تا این لحظه کریم‌باقری نیز در کادرفنی تارتار…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98332" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98331">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGhkJuJWyKmHVKCuxIKNUV6FtkU7aYdbEvceqoUXq4_yW6wUKyb9uac3DKqeGAkV2oqwEJzczpBZuKOLCQTatSfD6MD5GK5JDZN9h1XvjvqzckTR22dExqCnPOyBIumDGFKbVI41tAWGfr0Glb5sl56fRS-MgUrgQVwVhDU9JBPXEHVlRh_i8OVLGPDpurTz0cKwayY4jSYqXpq8KtSU1RIDseoeuB9-MjCX-Gf7m9VPog9RcsRtLLSP8QWHuIhEuzOYjOPsmxzg-1aAZIex_qX8nXrixICeK82ACE7UmX6liHBo43PhzjFYYF52jBC-k-rIDhWZ9pMfq_Vui9X9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
برزیل تا حالا با ۹۱ تیم ملی مختلف بازی کرده، اما تنها تیمی که هیچ‌وقت نتونسته شکستش بده نروژ بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98331" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98330">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHZtblVgry6yC_PW-MIdaZeW3q86k1TdIWAlmLE4cXLvKmlWqKepDYel44amg_7ctXXT-CIAQR_wXvhZtdUB70PZKFZag2U0M189inQEZU5xnT2nrfqk1doEUXttbB1C8nOCqtP65N6Woeo5Iwam--C-q9C2FugfU5fZMbkRAsDZTMJ0RD5x63bVV5wbLmHpGxV42WZjLO1_iEpVnl8VlszyHtUzg6HlJS3-s2MG7jSj3OXg2-IJKFJgF2CO3aJjWEjUUR1eIqR14YVP6UWSIBBJ3YZMeGl-v_sub3GPlmonLqjcO4oZQgWOsL2Z1llUXlV5WACh-12XETj0s4nmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب مشترک بازیکنان انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98330" target="_blank">📅 19:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98329">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_PQ1S-zSxqrVpzyvo4NwIohrRid_LkYhMOyXNgNZ9MTbZZPHsiA68sbmlw32pdVT23fTisYJD14Jbg4H_hSshLnrCqs2jW8Qm_oC2o8PoR0NqTGCVoSj5zHDXUhlALkxUTnF1sQ6GUhXKf3jWL4EA4QwpQjQ7U1nTeBQF6QMheAbgLC3wC9JsY4AoBm8IGMSwVlAzNGAx79L4YFBFS0PONaSAXaExTtprc1YSuQRxtgWllqma0Sp-QxS91zLWA209TE_RPODcH3HaNnIuHPCGAhAsXs4y4iCAvll0eUMoNY1k2O9PnBvHQ9EThAkNbL2VsRcrq3hSFgdvhd-0XeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇲🇽
عملکرد تیم‌ملی مکزیک در استادیوم آزتکا
🏟️
• [89] بازی.
✅
• [70] برد.
❌
• [2] باخت.
🤝
• [17] مساوی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98329" target="_blank">📅 19:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98328">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy-TtPi1EX9TRBjoSbel_WDQ7H79XCr9yNBAW893ztSYzqESeZynbNOW7nPVZihwRAoxdD62wI19xnKKLKOKomg2w_DG-IXNDJ5CFLdNtcC1KFeCZ_3CXYpZHXeij57nw9j37kouB6-Thu5rcWwBzl-UwsHIMDTRlIFRV97SHawtfOt9-cMVgqKhRLr3zc9sRA9LHWOLWo2yTb7xKdpYH0PemTPT8vKd4fZRxi83xVNj-mdyqMRGw3p9sfM5yFNlmcDcx_GhaPRPT_vKdP_j-YjnsPM1QQmHi390_B-kPAV5dKAv7XZb5qqzv4YKCaOLU3DzUozkOSmE7b6Q0i-yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98328" target="_blank">📅 19:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98327">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7mhbs-fkHeVcmYC8teJL1xRuxbEQCWGrMzzUuX5GrOHsH8Wnc1TXp3nRpu8SuS3SxkR3a16PnirqKwligl-WUGvkpJHO7VODggIoX7F1WWXRnAHNGBltVLsj3JfIiP79qgedocwYbqw5ussfUCnGT1v2laYL3FogW116j36TMVjvbu__ucCLI3tblisa-Wz8lBFF1TFFU1Mc7NM8xTqqQqoAFf-WszJC2dsMyPhpAs_i-8Xgtv7vVzIGo92te3ujxg-U58uwLi_xdjstQEOSjCs-VpO23Z9IeDs108hc6yHVE91-3yzW8zo7FRd82CmbJzW9mCCrKebvsGnezdbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇺
🇩🇪
یک شهروند آلمانی پیامی برای لوکاس هرینگتون بازیکن استرالیا فرستاد، پس از اینکه او یک ضربه پنالتی را در مقابل مصر از دست داد:
‏"آقای لوکاس هرینگتون، اگر روزی این پیام را خواندید: یک قهرمان لیگ قهرمانان اروپا، به نام لئون گورتزکا، 31 ساله، که برای بایرن مونیخ بازی می‌کند (تیمی که 6 بار قهرمان لیگ قهرمانان شده) و برای تیم ملی آلمان که 4 بار قهرمان جام جهانی شده، بازی می‌کند... هرگز جرأت نکرد که در زمانی که کشورش به آن نیاز داشت، یک ضربه پنالتی را مقابل پاراگوئه بزند و شما این کار را در سن 18 سالگی انجام دادید. شما بسیار شجاع هستید و در چشمان ما قهرمانید."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98327" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98326">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_tWOCzSVaGBav7-QdxxSoWZWsp10pi7KrH521nezScAGJ_WgloFSLQAnIk3IJTZ0VXa3NNEk2FSrC7MwfATIm7cfqJv1rHR2BoxHKW7_u8Dgm1fmTabvyWVZ7zMqk7t0vD1qrEpA9wYQJ78Mk4qrqZTdecTGvvHmqKBN8BD9Nwfy-iPA41WJ1T0Swba219n9g1ZIPMd1TjQYLQ6AWwtJJEKHr2e2-l1yKK6428GHTUYmAdf62ro87_hs2lVbnCjWLnpK5nYP6GKSR41cFomaxR544Ft-wdVITzFGUGbJKaKvJXFUHBVHT5YjYrC6N-5UTOu8FM_-eeGowXkXGFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانس فوتبال اعلام کرد که کسب توپ طلا بدون حضور در یک باشگاه اروپایی امکان پذیر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98326" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98325">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a3889ca0.mp4?token=EvBbiiaSCCc1E9XskB3zEgGKf6_UznW3jYBYpab8jeidO_mVYZegPpQP-CSVgouXue1ycD2LA6CBiXg3aHjwEHtq3lHatHXSs46qp8fPudMe5VBpKWHGY0RKIStOcG17boYLVLQYyo9JfU1ATMYEKzzn1pceHpZD1kN70z2bHDopnHWBHZcxITdZFenFr_TtwMk2wX8aNFD-MmQo1Yr0-x-ccpSe9n649ioQDRLOaqgY0Y8mF_vfTidrEF03b35ab6jJyH3Nwee6HDotdKNJX14_DBXdAh2RA9aZDkN_7a0bat294ILRFbiUR2KBXdLJXcdcAr_m4QE43YpstLMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a3889ca0.mp4?token=EvBbiiaSCCc1E9XskB3zEgGKf6_UznW3jYBYpab8jeidO_mVYZegPpQP-CSVgouXue1ycD2LA6CBiXg3aHjwEHtq3lHatHXSs46qp8fPudMe5VBpKWHGY0RKIStOcG17boYLVLQYyo9JfU1ATMYEKzzn1pceHpZD1kN70z2bHDopnHWBHZcxITdZFenFr_TtwMk2wX8aNFD-MmQo1Yr0-x-ccpSe9n649ioQDRLOaqgY0Y8mF_vfTidrEF03b35ab6jJyH3Nwee6HDotdKNJX14_DBXdAh2RA9aZDkN_7a0bat294ILRFbiUR2KBXdLJXcdcAr_m4QE43YpstLMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو آخرین تمرین انگلیس مقابل مکزیک، رشفورد لاشی برای کونسا شرف و آبرو نذاشت
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98325" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98324">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6563ff0794.mp4?token=u7CL4zMYdcx8Ng7v9VrMwDZTBSHeBDp3BYaxCl0HsU7c4NUOz92o7pAmZjSPtZ_nnsqjlQ2LRi1jVyGPFSMJ37MsNJy7kNXch98X2fK8XS0bhgmkXWyRDrE35P6R_JP04du91DMZwTiQqYwocbld9YyJF64J0OhrTqh0afoqW5sNrS-9iarzuJieI7eNqLQ7qIczvrw0szqAPQp8E-OjGxn41MuIk1O2T9pzRZJ8ycuHrRR85oDVbptyTUeEXSN6sJ4XRm7in6mHOBcSRLpIjlWqvzy8nbTjESdKrt-Ws0YHTxWIbHFoawsqEKhMLEV4fpnnrqCU_Mc60c6axJXMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6563ff0794.mp4?token=u7CL4zMYdcx8Ng7v9VrMwDZTBSHeBDp3BYaxCl0HsU7c4NUOz92o7pAmZjSPtZ_nnsqjlQ2LRi1jVyGPFSMJ37MsNJy7kNXch98X2fK8XS0bhgmkXWyRDrE35P6R_JP04du91DMZwTiQqYwocbld9YyJF64J0OhrTqh0afoqW5sNrS-9iarzuJieI7eNqLQ7qIczvrw0szqAPQp8E-OjGxn41MuIk1O2T9pzRZJ8ycuHrRR85oDVbptyTUeEXSN6sJ4XRm7in6mHOBcSRLpIjlWqvzy8nbTjESdKrt-Ws0YHTxWIbHFoawsqEKhMLEV4fpnnrqCU_Mc60c6axJXMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
مکزیکی ها 80 هزار پرچم تو ورزشگاه آزتکا قرار دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98324" target="_blank">📅 19:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98323">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmriXZ7w2gqHdkT6s7w3e2v9meO4muP_ZukNzaMmI4nlarlGBE3XQS2hdqh-j5op2Si98dqNNJ-jcK0t8GknL4LpoAEiUsKn1kZxJaAk7B4XEhW4GrwiGsHx0TIJvFNEC1IilmzXQxrtvmAkTQAFBuEmGWvAkPxvVjOViS3NiCDEIH-pDfCTuyEfSHdYYjkD78hOtP8w0lSAIRLRphBU-HfNNVXuPw3UZA8HEGMF3Z2e-6GdBx9_m0T8SWyMUq3Uwoi8I-Zg3YZTUAXH5dw3avWvDnUqBfl5Mg4MaZrQZkwTa9STP_YYybiVe5XbS1Vb5DV7qokc0GSYOtD-Y4iMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇳🇴
ترکیب منتخب و مشترک بازیکنان برزیل و نروژ در آستانه بازی حساس و تماشایی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98323" target="_blank">📅 18:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98322">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJsOBo1rKV4rd3uB4mNqJ2C_8BKLYFPeTuwz1KCgr2UVVb35D9cyNbXqBj5vomNgNQn6W2Vy2cBlIHAC9n6wecpSVfpKydseCg4N-dU1h1OY5b67hf7gem-huJNPkJTkXAtVTaIkceYI4O2iHzPJcIW6B7L5M2sS8-z3D6lBnrUO96ZLk7VU2Q7L6b8YaWt5ySJ3htDfZvFzekuJpPinHJrFtmQybNu21x4J6NKpYmNdVtrl_gF8tL7U34dlqeTQpeLNv-E_O4n9K8xyQmNhzQvhhlgTF5n0H4tz6KgjmXs8UdOoxCJLDFyUNUxSBIJKf0v2PwbheI80D9aeNkz2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بیشترین تعداد بازیکنان از کدام لیگ‌ها در مرحله یک‌هشتم نهایی جام جهانی 2026 حضور دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98322" target="_blank">📅 18:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98321">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jovvk8XhU6dlGWYjPhaQBky0_hFjdYSaOjOFHBsjt__RQu5ZqeNHJbAXvM7p1yZGuyqDo92WLG6WZiCGKI4OQun2hsVhjm4_lTUlZF22LC8bTLh7NnprhuXR0m3NEcSG0GExEyDdQUvcIf3OAX17fN1PQzMe8ROfAX6SnJPpe3wz39neG2kNuyhswtSgDFrBOFS7OD-73-Ivb9XB87bQnsAAaKdaq3sG1IGxkLwJoHdCB2mH1k8XEdnPFsd223I_AsiM4mNPugiJPJwTNv-VR91V6We1eoFLxo_JcsqTqF7j_lziF2HYAaCD-g869B6xe74MANUAaJAhErAdIrA-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه الاهلی عربستان در آستانه جذب فرانسیسکو ترینکائو به عنوان جانشین ریاض محرز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98321" target="_blank">📅 18:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98320">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eab4140fd.mp4?token=P_nVDjiMyFh72ychm7aHgpN_0UEmH-Erbk1JpVyFLmQ0pCqrCpl4YmNjKsg-7dh9A0iJPOX1TCke9zygxFos5RkIVn-yFZcdNn0eBKRgBCfLAzqiEIPi9N7NYiDmc1FrKX880BljxA3qp6hb8-mVn7fdh09tywvDG_UbD-HbPgT997tV_inBNCtAdsfdcWqBano1twBqM65oD6FBKurbH-fMW4zzH3gspgqjfRYuxwXOsZhPo_3CvMzJFrEAghZJu6RQbje7lVBg3UMbpQSouUzifRj1gVN-Y3PUTY9cHXUV3lybiyHxfyHI5wuyECIMY5dqDJioRWTpnaGJgVR9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eab4140fd.mp4?token=P_nVDjiMyFh72ychm7aHgpN_0UEmH-Erbk1JpVyFLmQ0pCqrCpl4YmNjKsg-7dh9A0iJPOX1TCke9zygxFos5RkIVn-yFZcdNn0eBKRgBCfLAzqiEIPi9N7NYiDmc1FrKX880BljxA3qp6hb8-mVn7fdh09tywvDG_UbD-HbPgT997tV_inBNCtAdsfdcWqBano1twBqM65oD6FBKurbH-fMW4zzH3gspgqjfRYuxwXOsZhPo_3CvMzJFrEAghZJu6RQbje7lVBg3UMbpQSouUzifRj1gVN-Y3PUTY9cHXUV3lybiyHxfyHI5wuyECIMY5dqDJioRWTpnaGJgVR9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آماده شدن استادیوم محل برگزاری دیدار حساس و دیدنی مکزیک و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98320" target="_blank">📅 18:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98319">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
🇧🇷
هوادار برزیلی و آرژانتینی کف مکزیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98319" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98318">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98318" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98316">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpGwN6SrM3MCS9fDrOnSqgZRjk_IwmfHP98pj5Y461lbnUtoErPYRqdGyMMdVhnVsamZSZjXqDI2vpZpYBBsxMUOc4-zVCF71tVZq_gIeBwPuGpmSEAf3ZXPdj2pF4CbHQc151pkCGObLq2aOV4eGa9JXXPYQdM1fTPBLHebNdmDbB9cl9ftMWYNyglpEKDyo2B6l1UdsF10POcDNoqlqvnmNVYvwU891Tda_ED6GcerYVdLroKZQBWJy-ngzqEJrHWRsUyxc20iUweEwJr3MdFR7u6uAhokXUA2kVS7sV4-LBcvoLO5FWesDO0VnHjst11rl7LvTdKq0pfpWCw2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
💥
گلر کیپ‌ورد و یکی از هواداراش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98316" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98315">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY6hvh1uWpKgYOADa9HaeUGqDLa4myVqv4CS1uNJrmKOafGEYuxGRBd-2W2Dyn5FJZpqOXq47AoSFW_756a9-Ll0PkZ_90OgNDGXq5fgb0ILMYrzj-M2MRL0_ERSdjPMGaDhCn1lHUUu8Ruuz6Q4HW8JvP9Y4gnGS8jTiW3HxmB-5Kbc3A_-Mf0aEBhVkz_tY_MAvKxRPltzhlAOHhK4GUGqgbvKSh-ai4T_PxK2Ab9QA-Gz1IQFY9lmEOu2SAQKHhPziWdbD2i53BOWXBobxjV6P5ObZNyc_TZCA2wyMNwE8-Bg9D3iZpRvOFYVHGm9wZRiiSGUZPLhRAxsOCptXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
دختر اینفانتینو رئیس فیفا دیشب حین بازی مراکش و کانادا با کیت مراکش رویت شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98315" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98314">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=BxuTBgASFy1KEY8_ijxvkqC8-4UFIIfAUKoeUh3kBnySzMcqTt7oEu186BW3m0kyxQlhOMLCA6MKK-nGytX7Jqf2ZKpElQF_D8TETrwgTWchufmOd5wFTBirXidLm0E8fvAJqxb9MrdFQF6BZe3L_at3zhE71w0Nw5moPY7JNetmzkCEg6j4eHNkIx-EmEmOuc4IVjhjHQAKLLxfHgoZ4z1gYOCy4GdihUNHveWkByCj8-SNcQJM7Nd0ZXQ1tf9mbBcGUAyRwD70dwpOD1mdBPt3wcT6Lf5B4qL3lzl0sDhb6DMOfCxkdh6a6jPLIReUvnbBPWLqfKG6IRQik8j1UFyGd2neqkPBQkti00IdAp4LukclxZtgs0U4RsW526vk1wJZ0y7ncphrBEWJ_lXtLOpIKhKU83bpxxj3g9ruUzhMcrgi8g2FSSxDSfU8kMN8uyLPuj9vcPMCiwWAsoOxSqZCd-J5knBG_QfUzAyuGcFkhew9X3MHQs9cZABNZZEGzl_YHAqUKuq6Hw4DrBQz11HNl01Wqq6L7M-hFsJvgTs_4T8mar4seQ4zUIPhLkaaE1xcdmPkbK1eSEW4o1--N8bRwG4ELmNb0VtuAvy7Ff7Ym5QxazYzoCCXaWhRGbldMT3cU_V76-I3E8vgRMWCFFWToNJWXi2Eax0ULXBEkdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=BxuTBgASFy1KEY8_ijxvkqC8-4UFIIfAUKoeUh3kBnySzMcqTt7oEu186BW3m0kyxQlhOMLCA6MKK-nGytX7Jqf2ZKpElQF_D8TETrwgTWchufmOd5wFTBirXidLm0E8fvAJqxb9MrdFQF6BZe3L_at3zhE71w0Nw5moPY7JNetmzkCEg6j4eHNkIx-EmEmOuc4IVjhjHQAKLLxfHgoZ4z1gYOCy4GdihUNHveWkByCj8-SNcQJM7Nd0ZXQ1tf9mbBcGUAyRwD70dwpOD1mdBPt3wcT6Lf5B4qL3lzl0sDhb6DMOfCxkdh6a6jPLIReUvnbBPWLqfKG6IRQik8j1UFyGd2neqkPBQkti00IdAp4LukclxZtgs0U4RsW526vk1wJZ0y7ncphrBEWJ_lXtLOpIKhKU83bpxxj3g9ruUzhMcrgi8g2FSSxDSfU8kMN8uyLPuj9vcPMCiwWAsoOxSqZCd-J5knBG_QfUzAyuGcFkhew9X3MHQs9cZABNZZEGzl_YHAqUKuq6Hw4DrBQz11HNl01Wqq6L7M-hFsJvgTs_4T8mar4seQ4zUIPhLkaaE1xcdmPkbK1eSEW4o1--N8bRwG4ELmNb0VtuAvy7Ff7Ym5QxazYzoCCXaWhRGbldMT3cU_V76-I3E8vgRMWCFFWToNJWXi2Eax0ULXBEkdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇻
بازیکنان کیپ ورد در بازگشت به کشورشان مانند قهرمانان مورد استقبال قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98314" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98313">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=K7NQqeZIFkODHcn1b4NQtPnnt7oMvZZlEotsfhkeq8aUWCd6N7UCZkOf0Rb_HjUzBwOpupSl3GX_KVt4HkGQR9dmD5ZZhJD82lcYVmMzuEudS3HlmFEJi93NCDC2XSDm4F1gJ4j2yJUemjJmeqcAcmk4-PkEiIkZFFIJ2FGxKb78O8G8UD-jZevZbRhlQiJ4A3zQxj9zdIszV64vjW6KTUqUuCipIt7fQO-7EN9wDRJFp-SG9g0MVWyh9LmAopFWvO7q5QdhsJh0xNUQtp6aoMHcTscfqZR7kPxPlG5Kxv8DCZ30Ivmgs-cGns1xZNnDhrGvR-DSy2HiE-2BNbaBKUQ2LgLPaXrLg341mi0g7XoEv62nchyMueA_jRdZqWBHcuucM_s3kWvU2NAvOH8I_oZtqnPdrccwAeO6DKrLtc1ln6zigf9PWeK7MiG5p3hUIv1EJk6BEIaYxWSWADMfH_ycDMhgorNvpB8XKy36oJ3wLrXxgj_n3hpxpvxTj8Y0eSmUi9M90kTahfFY53-kFYOWcLs-Yt7v59nNDSEI-f0tg8vcI4u_-wup2NNdMW5iKpsFPrqZMzkh7-rS-6IzSs7AfpW69KDCnyTLBRN4M0i_SJ4_XDwPQXcLEwYg3Q7ASZd7WLyY8DPCj82r-XzWJ15YhBpfMe9At9hmN_eDQKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=K7NQqeZIFkODHcn1b4NQtPnnt7oMvZZlEotsfhkeq8aUWCd6N7UCZkOf0Rb_HjUzBwOpupSl3GX_KVt4HkGQR9dmD5ZZhJD82lcYVmMzuEudS3HlmFEJi93NCDC2XSDm4F1gJ4j2yJUemjJmeqcAcmk4-PkEiIkZFFIJ2FGxKb78O8G8UD-jZevZbRhlQiJ4A3zQxj9zdIszV64vjW6KTUqUuCipIt7fQO-7EN9wDRJFp-SG9g0MVWyh9LmAopFWvO7q5QdhsJh0xNUQtp6aoMHcTscfqZR7kPxPlG5Kxv8DCZ30Ivmgs-cGns1xZNnDhrGvR-DSy2HiE-2BNbaBKUQ2LgLPaXrLg341mi0g7XoEv62nchyMueA_jRdZqWBHcuucM_s3kWvU2NAvOH8I_oZtqnPdrccwAeO6DKrLtc1ln6zigf9PWeK7MiG5p3hUIv1EJk6BEIaYxWSWADMfH_ycDMhgorNvpB8XKy36oJ3wLrXxgj_n3hpxpvxTj8Y0eSmUi9M90kTahfFY53-kFYOWcLs-Yt7v59nNDSEI-f0tg8vcI4u_-wup2NNdMW5iKpsFPrqZMzkh7-rS-6IzSs7AfpW69KDCnyTLBRN4M0i_SJ4_XDwPQXcLEwYg3Q7ASZd7WLyY8DPCj82r-XzWJ15YhBpfMe9At9hmN_eDQKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
هواداران مراکش پس از بازی با کانادا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98313" target="_blank">📅 17:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98312">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id8JTjgEsBPx9k8N3GbrsoK8auh2n3NHTObvwkdCpiPMSsqOiYEHDxd9sygQa9HPFSGIlWGeln51CO0FTHuYG62yUUW2gZ_hgnbulHIB_WlMY17endDdP0f5URr7egoxu51cdM48h7jHdz916uyaEWHhJPvFgjEpmDLZpJ6mMx2J5gCjjg2R_ZOxFjQMTQvpdcccxaY83490va2YujMHTKdbqa4AWF9Y37xVgeC49CY7AgI8_cKA9RQBgRBYcM2Y6W3ERdYXdPaEm6ZplzE6F6lbKjdPZrWd0FD5OnqbGcXkeFYdhqxK6T3iBIXzfxD5h41K2gd4ubvReHwGQRb8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
💥
دشان، اولین مربی در تاریخ جام جهانی شد که 10 بازی حذفی را برده است:
— در سال 2014:
✅
مقابل نیجریه (مرحله یک‌هشتم نهایی)
— در سال 2018:
✅
مقابل آرژانتین (مرحله یک‌هشتم نهایی)
✅
مقابل اروگوئه (مرحله یک‌چهارم نهایی)
✅
مقابل بلژیک (مرحله نیمه‌نهایی)
✅
مقابل کرواسی (فینال)
— در سال 2022:
✅
مقابل لهستان (مرحله یک‌هشتم نهایی)
✅
مقابل انگلیس (مرحله یک‌چهارم نهایی)
✅
مقابل مراکش (مرحله نیمه‌نهایی)
— در سال 2026:
✅
مقابل سوئد (مرحله یک‌شانزدهم‌نهایی)
✅
مقابل پاراگوئه (مرحله یک‌هشتم نهایی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98312" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
