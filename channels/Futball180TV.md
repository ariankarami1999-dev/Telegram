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
<p>@Futball180TV • 👥 601K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-99370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=oBY2h-voIJ79mbhuCbDOYfuZZSMbp3JyNttHb0DycjtuiduSe6tyQpNdeUNjGFPUde3D4SQopNFgO5rQGIB2aGSnmKqq00SVMKIAN94-Td9PffkzU96S6Gu_fsztXNemrHM5A6OQMeeAmZfEUhbO8VdEeY7TyIqhkmzku4IB4kXVGExZV6mVMocTFPvvBgDlFYDHZMbzBYCR28qkXT8gWZOo5uSWkMX3OSeTfh8GpaMeEoEfy0mS9MU9ToHlXmszLYU_JuORmZAUARjnezbDv8nWfOfeHelKvocOHSJSm-ViEjcrbOcHhQhGeecC7owRCWDo7wFqMRuI_cP3tWqLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=oBY2h-voIJ79mbhuCbDOYfuZZSMbp3JyNttHb0DycjtuiduSe6tyQpNdeUNjGFPUde3D4SQopNFgO5rQGIB2aGSnmKqq00SVMKIAN94-Td9PffkzU96S6Gu_fsztXNemrHM5A6OQMeeAmZfEUhbO8VdEeY7TyIqhkmzku4IB4kXVGExZV6mVMocTFPvvBgDlFYDHZMbzBYCR28qkXT8gWZOo5uSWkMX3OSeTfh8GpaMeEoEfy0mS9MU9ToHlXmszLYU_JuORmZAUARjnezbDv8nWfOfeHelKvocOHSJSm-ViEjcrbOcHhQhGeecC7owRCWDo7wFqMRuI_cP3tWqLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرانسه به نیمه نهایی جام جهانی رسید.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/99370" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99369">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
قرعه‌کشی مرحله گروهی لیگ‌نخبگان آسیا و لیگ‌سطح دو آسیا ۲۷ مرداد برگزار می‌شود. استقلال، تراکتور و چادرملو سه نماینده فصل‌آینده ایران در آسیا هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/99369" target="_blank">📅 13:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBdmGXHydkJEJlYCR4xZ1Ht0KJm6_B21n5TllIp2kmAjKSzOqJ2YpFQAXgZeEjMen7y8A8ba165rS-ShpokPMSko3MCH9TwB3eU_rWqKRpi1s9sOWBQl_YJkNwRZG1ZXjC-3UHZLlFBoNjjYa_DkRWVw7YexsBSaF1y5510wts-80RflpZva4kgSerFPvxWAtl7dYyTwYfSfP8AEYj3cOO047jGY5HRxG2-gyNEOZtgQGCOqQBtmSjsdsEr5EIcgkWFoaQBL_DoyFoqF-cSiYxFqNHTepyCOiYMwsFwxhfRTQhj1bvqtD8BNKy_Yw5W9UkktOUNxT1juveuEQ1KzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇾
سیلیست آماریلا، یکی از اعضای مجلس سنای پاراگوئه، ادعا کرد که حساب اینستاگرام او هک شده است و او مسئول پست‌هایی که در آن توهین‌های نژادی به کیلیان امباپه وارد کرده، نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/99368" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99367">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1Cfw_zq8gqQP5JjDwUKgBvevMa317UJ1BzUu5_6jgKJu4V08umoCL0O5mD7dbWh6Q3uYJZTbC3DfGWkY6Q79NRorapJQSl7e_BjRqmEIffrD-y9TuZw5QW3t4-QqDUfok0oBRBpfnqXdoosilUa3YyqiDR33LBF49d9QcDpQPy0RLL_0KXjWrqPD1e3Npd6VNcc6Frgh0mApqaSwAPcEHWQTvlORZmfs8fzQD545l22S8ijcEq1SZSHsgP-qh3cCjbETnGC4JrW-G3syu7JFhZWelH6vDY8lHscB0-d1UN60-Ef74DjPCGIGJGyy6nw1XdhldTmp39gV3jIAmXQMBII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1Cfw_zq8gqQP5JjDwUKgBvevMa317UJ1BzUu5_6jgKJu4V08umoCL0O5mD7dbWh6Q3uYJZTbC3DfGWkY6Q79NRorapJQSl7e_BjRqmEIffrD-y9TuZw5QW3t4-QqDUfok0oBRBpfnqXdoosilUa3YyqiDR33LBF49d9QcDpQPy0RLL_0KXjWrqPD1e3Npd6VNcc6Frgh0mApqaSwAPcEHWQTvlORZmfs8fzQD545l22S8ijcEq1SZSHsgP-qh3cCjbETnGC4JrW-G3syu7JFhZWelH6vDY8lHscB0-d1UN60-Ef74DjPCGIGJGyy6nw1XdhldTmp39gV3jIAmXQMBII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
بازیکن‌سابق پرسپولیس نطق جدید کرده که البته برای اولین‌بار احتمالا حرفاش درسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/99367" target="_blank">📅 13:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRbJuYKeRBTrw0nEnKKhhH6ik3n7st5m-Nc6I-YblVhZhRIfDnjyJaV-WteP6xKY4PcIigmva1L62GaIg1C697cO9lL_CayA5-so035ZJ5lRs_FAu7Y9BC6A3Dblh9KLoOSmx9jb0mEHjhjd5W5rHYW2CeHM2oQ8eb_aOL_s6ih51SFJjXnzmAHWlsbHTQgu7adQ8SuEaNCKIhShUSJefWs5lJAfHw-b16AdNv8C5C4loZR-sGhZg9NjE6WgsRst03lPNyHLqfMvqQNW436RL9Dj3lAKuaUzxdfTvuqzCm1l7fgEOUSpiENl-tppTeEFHjwouLZi6S49kPGvcEVVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
موندو دپورتیوو:
احتمال رقابت بین منچسترسیتی و لیورپول برای جذب ادوارد کاماوینگا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/99366" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=iXnBn2_QXqeiHzlKimeavSgnpnrsmagq4J78KIK8Jo67iyxTDhGurx4Mm7WhM7pBDoweK5kK29laXW5hLlQi5sHXYALcyNtddWvxRUs_YSCrZwZLSC2ibdkivdvlIQl5NjYZ6N5n4lzIV7pmeDzLHORsO0Z0QdJ-dAhFGPIhbQNU7Ybx7DasGNaLr3a6iIEZpvddDR5lLWklNVESz2aiXM_SBifuhHwMw2fZ67khhsnPrKZVVB0QIrYJyptSuqn_eB3HxuLReovEWIxeC_AblvCyz6Xvj_ZM9dbjlaP5_EFADt1oYA-r2zj8oojJQDziTUlAdd6g_kIput-46LcNYB6VkEpgIG5FWgrmOZ1AIkGNEjKmZ2R11YVZvuBRahlonzhsW_DrviWP_XhkimK78S0zfK_QjY3j15nw_oWrGRbmOBC3Qmr7Z35vf21Ar6eWUMrGlJwszPGOJModYPzf_3UUuHBBUDT-Xzsj_Yjfl6y3wpxKt7OzKm_zlgDqgLwoMpY8A9nHIEQhcL3Ef6dMM2nTedx0RXCv6KoGMJSthGcsG0zPIl4qhSYgpAGG94lta9l6XAl1B1mNRlW0KewBXVI2VzsvongVF4q9xQd55qnfPf3xIfrepai0A9ra8xKBEKE2NWM6V5r9_SqqCcLHsUndbrQxacpkcnnNCEt3mRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=iXnBn2_QXqeiHzlKimeavSgnpnrsmagq4J78KIK8Jo67iyxTDhGurx4Mm7WhM7pBDoweK5kK29laXW5hLlQi5sHXYALcyNtddWvxRUs_YSCrZwZLSC2ibdkivdvlIQl5NjYZ6N5n4lzIV7pmeDzLHORsO0Z0QdJ-dAhFGPIhbQNU7Ybx7DasGNaLr3a6iIEZpvddDR5lLWklNVESz2aiXM_SBifuhHwMw2fZ67khhsnPrKZVVB0QIrYJyptSuqn_eB3HxuLReovEWIxeC_AblvCyz6Xvj_ZM9dbjlaP5_EFADt1oYA-r2zj8oojJQDziTUlAdd6g_kIput-46LcNYB6VkEpgIG5FWgrmOZ1AIkGNEjKmZ2R11YVZvuBRahlonzhsW_DrviWP_XhkimK78S0zfK_QjY3j15nw_oWrGRbmOBC3Qmr7Z35vf21Ar6eWUMrGlJwszPGOJModYPzf_3UUuHBBUDT-Xzsj_Yjfl6y3wpxKt7OzKm_zlgDqgLwoMpY8A9nHIEQhcL3Ef6dMM2nTedx0RXCv6KoGMJSthGcsG0zPIl4qhSYgpAGG94lta9l6XAl1B1mNRlW0KewBXVI2VzsvongVF4q9xQd55qnfPf3xIfrepai0A9ra8xKBEKE2NWM6V5r9_SqqCcLHsUndbrQxacpkcnnNCEt3mRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
قصه سوراخ کفش فوتبالیست‌ها چیه؟ این ویدیو رو ببینید نکات جالبی گفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99365" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcHsy_ULNojM5DQIqMHFGa89LeJpAXCLvSrk9AHbzVc_AaYL814zXACYI0HT_HSSE_lRG94qlCLoOpL5JciPZ7bgBpnCIT_ngArTPkYpxA_s66IYME8hyyWRkjq3ivIyBYiIRXtOfrCiajX1XbL6zS8-16v75G7wmjZZEGzbSCSERjVQvVKsJ7VocAY0lp77ren2tMhpJdxzr34J52QNGEPPZGD15tgPGzfojBRn-6ILun46BlaTMVxLMfbU5gSHEphM2SSoJ6I0-eVZiVmd-XB8lwS7vqf_sKqnwPv3Kiv2NzPT7AyAXx2FW9Kz9H8Sur87e9WyCLPPnsgi9wswTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیلی میل:
دکلان رایس به ویروس مبتلا شده و برای جلوگیری از سرایت عفونت از بازیکنان تیم ملی انگلیس جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/99364" target="_blank">📅 13:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99363">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs9he_3i2FeOua5ky1BBRqbM19wlVMY16W6DMirGPabYMbeEXPPyfnGKT19IFGiBcWCYFCXa78T-2xZmD5fbUGcrXy5H91QHGLSY2Z7hhnZTwCx4g-1HBcXc1-eRmrrqv4VlRxG4I6usVsgwQS5bmzqcHI1iiybNhh4IAD-DH-3kjeh1-DOMJl4w4t6BAXPvEFkqUZ25MevV4SlZJbTRFCyyCLCJueGiiAMsz2hWbMflAwJ_xrH1QN7j-u93TicbIl92AkMveBHpzgvE0v6K1mau1-4A13LangezB2B6BY83XQEF8s8onSGes2wn-cOYoeH4TztvkACzRisSUaE7EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99363" target="_blank">📅 12:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99362">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiyJPK4eJwxqEuO-8XURq35rz4jEFjKnj4lBNlYdKDJfLqRjk7yD6gfgM-jvG8t1yMqnM70cae2iZUekxEUzv4AqlMldNU94rUu3MVW4qNUr_qT-oaBESD4q_soc11sVcRApqZNIywSVzBCczARRzopCPzuotgRLgg5I10-XNH4_xpUhCvgrM14Een1X92JPevkCBuK0jnXB4JXypLxJjheVuC4DHq3jKKP9yDslT9HLzAA4S6nIeIlU4jJuReB1TaO8Q6k5z8EanDMNTs6-H6LmYWQDxD-SRaA0F8HVdusJ9UKJG6HQ08ZG9ai6os_95_QvnjpAkzZ9wtuCPenS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیکو ویلیامز:
در 19 جولای قهرمان جام جهانی میشم. دوست دارم در فینال به مصاف آرژانتین بروم و با لیونل مسی پیراهنم را عوض کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99362" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99361">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1-OyOrbLdotk4DZ4C9ufpuhRBhFLCBtZtuEj463R3KLB8qrBs92wXjnp9ws2g90G3E0AzNFAL9quyQP3UvCJyex4RPUBGA7Xf7WOZQHadpqy1cMakb2A0K3SWlvUWu5ibv1YfY9qyeMKGRjBt6D5wm7lnHem0EdrUZGGFZXorgxjsdHx4iGbg3WOmHfusOjJIQ5wkaL2YueHLwZEDl433J33WoAVfIrPl7cpgaT4MBCWnTp6w4dB6HrXUyh-wY7yeEWJ5tXrBy1YERLoEMtZoCe18UOoen_UbNGDQrrnsBhwVv99j8tKpznlZKwuGgC9CpTqzQ1fcHIowhtK5EruQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99361" target="_blank">📅 12:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaxWpvNs36Km71XxonJGyYvemMl0ypnWXhcx_g_wiO2jIe88zZRUVyNNZXyBn5cWKHvRR9Nk36hckNn-Zo9f0rNW18sY-StKBPxEO-soKQzGGLa5DmCgyKLub9aCWBzltUeHWunDvAvgIRGl5DJ1WlDhCuuODCmWueP-iujgLHuW1k4xEKCzw2zgr932Fx-NGEulN8yvsphUhnhkuXkmOVxzeJKiyL1NDv9IujQFWp2270CmCOBDZ58ZnOUkFzyIx2g_rgcqTz2RVHLGceSwIDsH3thoqTIJ4tZVAH9ZmUPyx82kFqMPc5srbqC4Ur4BSt6znTo7IrctRyauRPfheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
استقبال مردم مصر از تیم ملی کشورشون بعد از حذف تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99360" target="_blank">📅 12:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99359">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN8_6g6SsGI0ygRsVRdDhFE_AvwXK7KTrGu95Gsgy3sxEFY9GTELalwdVsknqExMcLdTJIA4dcFvXwEIXk3Mo7JZknAECWoxGSvwC7XVzl0bQ0ae_2tWVBt0yY-1QMr0TEfVL88jLiWVONU1U_T_Xl9DnQI8oNt2px0SA0BU6OGzGJG0pDXQYkRY7D0e_EfHTAnaG69ax_SmRSLDdhYvxlvQWlmyFsyVFi6nxJPQ2t8B2lT4EUymMOd6wgGpzK_w1q-WkUpylWM6_RO-HVKyi50nSyyNUVh6DKjkGlqOUQkXHzG79PIFP3EyjhMxs12dhax0FzcHtEKsHwwUA3b-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📅
در چنین روزی، ۸ سال پیش؛ اسطوره پرتغالی، کریستیانو رونالدو، باشگاه رئال مادرید را ترک کرد.
👋
🇪🇸
📊
آمار و دستاوردهای اسطوره کریستیانو رونالدو در رئال مادرید:
🏟️
• [438] بازی
⚽️
• [450] گل
🔴
• [131] پاس گل
🔥
• [44] هت‌تریک
🏆
– لیگ قهرمانان اروپا [4 بار].
🏆
– لالیگا اسپانیا [2 بار].
🏆
– جام حذفی اسپانیا [2 بار].
🏆
– جام باشگاه‌های جهان [5 بار].
🏆
– سوپرجام اسپانیا [2 بار].
🏆
– سوپرجام اروپا [3 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99359" target="_blank">📅 12:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We0Y2kp0hEVACnnUl9SJJqPjC8FtObufgdNaRPGmqz7ntyIwYV1VvsJCZF9nxKPW0vIu7HO2__V8PYQ4_nWj_1mJhMfLwU_ddPhWyLUtTYPvgy6Twy45rTJdIiLR2aPQK_VHM4RGaBpCMQnnZA2HqVW2jrYj5lCuKjwEGkCfmqjWyno20la6_pYbc0aH7F1buOSLkq8aPAFJD49RtzGKpcE2YKjCNemxVdSilHZUVJaQBvGer38SaTwbdU_6D5JvcA-VnqWz2QPat6AqBmMBKD2YK6JdRXMuS2kDRuDzvUK6r_qoOr3jBEZj8qsxt4EOUc-21Z4sniUKAWgMOJRddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇫🇷
کارنامه کیلیان امباپه در جام‌های جهانی:
🔺
🏆
۲۰۱۸: قهرمان
🔺
🥈
۲۰۲۲: نایب‌قهرمان
🔺
🔥
۲۰۲۶: صعود به نیمه‌نهایی (تا این لحظه)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99358" target="_blank">📅 12:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c816ba371.mp4?token=HNfk7jtvutu1q6KSgJCm50IfWaOxPkgPxlWGTlPCJ_UJhpBZ1vLRJUfuc7SPg54s3cnj-gwELwGIxAmDE_Jyr7Pcn-SUFPAqDdFbhb8YZw2vEVPNrTpVbu7ZEouq1KomPpbdsuoJmuG4mKrYiElYNJTS9d9dMpYvZO604Q0lN6OLo_4DFeY-G-1JPIUU8tN5dwcTXGiX6y2TWI7nuzYbKXEdFgYhrSB4f-xRJM8KiT02J_Xnt03j-d5NwbmlzZavCYOkqQhkmpofd_SvbQv2_LG-jo0HS_joIrgVlb8hu2VBrEJrX4bXQ3fWzIRe-H0qprrHf5KRfN3uMiwzBOVKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c816ba371.mp4?token=HNfk7jtvutu1q6KSgJCm50IfWaOxPkgPxlWGTlPCJ_UJhpBZ1vLRJUfuc7SPg54s3cnj-gwELwGIxAmDE_Jyr7Pcn-SUFPAqDdFbhb8YZw2vEVPNrTpVbu7ZEouq1KomPpbdsuoJmuG4mKrYiElYNJTS9d9dMpYvZO604Q0lN6OLo_4DFeY-G-1JPIUU8tN5dwcTXGiX6y2TWI7nuzYbKXEdFgYhrSB4f-xRJM8KiT02J_Xnt03j-d5NwbmlzZavCYOkqQhkmpofd_SvbQv2_LG-jo0HS_joIrgVlb8hu2VBrEJrX4bXQ3fWzIRe-H0qprrHf5KRfN3uMiwzBOVKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مهدی‌رحمتی: دروازه‌بانی در تیم‌های بزرگ به مراتب از تیم‌های کوچک سخت‌تر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99357" target="_blank">📅 12:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d32845b6.mp4?token=rNNCzUHpoCz_o4pUPgGnA7kxWhQhmNmhXE3efXiV8TlDsjywJMyWelsdv8winDMpee8cR3R6LPcYNfIKSpM3n3nEd7mbN77q6ve5YSDkjZ6eUDazJ4gS438ZLJqNwZOj0iWAHU4BpCsx7YWvfPhN-nFJr6viNmy4JDZ3hgfwJmB8--fheAA23dcQKgKVg4ah6qBJziwY8jMC7og7yF221LhX6nOlTembheHWVMDb34PjbyXeJ0jGrJvRtdjMhUU3OhnzIUMETz_jldKZbDriQbp5DXU9ckkcv0Ieqz2hYRar6-psnob-gQ9wChpEAVQmpFPsO5p3du-i_1IO5TyC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d32845b6.mp4?token=rNNCzUHpoCz_o4pUPgGnA7kxWhQhmNmhXE3efXiV8TlDsjywJMyWelsdv8winDMpee8cR3R6LPcYNfIKSpM3n3nEd7mbN77q6ve5YSDkjZ6eUDazJ4gS438ZLJqNwZOj0iWAHU4BpCsx7YWvfPhN-nFJr6viNmy4JDZ3hgfwJmB8--fheAA23dcQKgKVg4ah6qBJziwY8jMC7og7yF221LhX6nOlTembheHWVMDb34PjbyXeJ0jGrJvRtdjMhUU3OhnzIUMETz_jldKZbDriQbp5DXU9ckkcv0Ieqz2hYRar6-psnob-gQ9wChpEAVQmpFPsO5p3du-i_1IO5TyC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایتی از اتفاق عجیب و جالب در جام جهانی ۲۰۱۸ روسیه در بازی ایران و مراکش که برای مجید حسینی رخ داد و زندگی فوتبالیش را تغییر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/99356" target="_blank">📅 11:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxWIpbB7YwznhgxxUhkwRStKfnx_JaYfT1H9sx4paMEnQmHGCkqmkYSjT1ATgrTy1_rfzQJQycSSstMGnrwqVLYXDHqcxJH_XYBMN7Mx4Tcx25emF19yzsFAf4-SOirKIvqEkF07GZ4bDunIshzCzLlYbc1ehHuI6getatqRwABW0LysGDONyJ2TzYmwRcvOnoqFwYE3jdiINZ8RABFhHiOjHP5rjS7GNiWpiP0gwnSMkuAg4VV2Erqj72CLQOvDAGitTUO87BCJ-fQpeP86HHZ1rtjMdorLBlkknvTOqsMvopZgWEHWHhw7is2mcICK9pdDmeyaosvxo39LXj7dzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روی کین درباره جود بلینگهام:
جود بلینگهام یک بازیکن سطح جهانی است. اگر انگلیس قهرمان شود، جود بِلینگهام و کین نقش اصلی را ایفا خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99355" target="_blank">📅 11:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c176e8c357.mp4?token=GneNDriKK0xTfR9mR2X6K846-q0YORrwgtpaVPqal04o3E4bC_vs8QOt8_WNyu3d4jwq6TUkC62C9b7Sz00eRlQYuid8Lxj_QfxT4-ILl_S-vSj4OywnAVEq4eQrfQge84h0leeGDDX6s0ZF-pzN_7CMy_kmtzIWMUcC_4FxTGW0bs6EV90bkKTjCtT-PFf3NVJBM8oyOclm_1YC2RdfL_BoYCuFRWHM302VrvPtgUMuQebKsFNZcgItWha9gqAmEUsJ091b4lzxErPnKrHBP-IInR542v0tlBu5eOhH5lc2ZpNNrQy8QChPHly7b_uHDpwrdrk7zmpgL7khjiRStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c176e8c357.mp4?token=GneNDriKK0xTfR9mR2X6K846-q0YORrwgtpaVPqal04o3E4bC_vs8QOt8_WNyu3d4jwq6TUkC62C9b7Sz00eRlQYuid8Lxj_QfxT4-ILl_S-vSj4OywnAVEq4eQrfQge84h0leeGDDX6s0ZF-pzN_7CMy_kmtzIWMUcC_4FxTGW0bs6EV90bkKTjCtT-PFf3NVJBM8oyOclm_1YC2RdfL_BoYCuFRWHM302VrvPtgUMuQebKsFNZcgItWha9gqAmEUsJ091b4lzxErPnKrHBP-IInR542v0tlBu5eOhH5lc2ZpNNrQy8QChPHly7b_uHDpwrdrk7zmpgL7khjiRStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق‌وحال جورجینا در جت‌شخصی CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99354" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da77d29953.mp4?token=uBiLlbsdcvtV8dYQydluzUvL32aK3kZhvMaJ4uSDVZBEPtkQd0hNODID_Kcmn4OwsqkkEbECZT5XB1A11XbmlGS5O2O5bi4A9MSI6qTeiiLl1dQIuNcGmgu2y7xSIAB2KE7kKUodcVsWB1X6QqmeKAwT35jGR7DWL5I_F3Js2yAcAlt7l4OtMHPnXRdSAa91uTB4ndYpCsvOpXhGYoNCaMTXpfzb-V6GoNrRvupcHGdGfHz4gmQK66sGGably140WFaOmqxkW6K8KeiDkH_QlW6AHp7vFfVRmYIGsQsosv-bPvqTzTZO0coxJtdQDRrYa7VMyobajMdUtI_dK1RCWE65O6OokCzp-tJWBXz77ywHu96Q-ZOH1Rz5Ehscgp2x531JM6N26bVEyO_MLnoX7nRVlIbfrdBdxzZ6Su6YY0fwPV44LLZF8hBI8admXNqpNis59unrcBmcvVubjqiCfI5DZ_gNuVzXrD6cqut8Hc5xVuA4jIVRnlGNpLtJa8ygzXMFXvuDvAKN8GuwDCzt_hoZVpTWKl2tmdeea5sgq9v5xGOur7HOfkJlZccwBFPUCu0shAzj5RD3q4ZIDSZs6MiJwIVLQmhTwLXYA4WZml68Q2AiXq0u0TMZ-Fu3H5iGVv7K0q-osUa0DtUTv0yWtyrBedtPzO6rIrPPFrzgfI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da77d29953.mp4?token=uBiLlbsdcvtV8dYQydluzUvL32aK3kZhvMaJ4uSDVZBEPtkQd0hNODID_Kcmn4OwsqkkEbECZT5XB1A11XbmlGS5O2O5bi4A9MSI6qTeiiLl1dQIuNcGmgu2y7xSIAB2KE7kKUodcVsWB1X6QqmeKAwT35jGR7DWL5I_F3Js2yAcAlt7l4OtMHPnXRdSAa91uTB4ndYpCsvOpXhGYoNCaMTXpfzb-V6GoNrRvupcHGdGfHz4gmQK66sGGably140WFaOmqxkW6K8KeiDkH_QlW6AHp7vFfVRmYIGsQsosv-bPvqTzTZO0coxJtdQDRrYa7VMyobajMdUtI_dK1RCWE65O6OokCzp-tJWBXz77ywHu96Q-ZOH1Rz5Ehscgp2x531JM6N26bVEyO_MLnoX7nRVlIbfrdBdxzZ6Su6YY0fwPV44LLZF8hBI8admXNqpNis59unrcBmcvVubjqiCfI5DZ_gNuVzXrD6cqut8Hc5xVuA4jIVRnlGNpLtJa8ygzXMFXvuDvAKN8GuwDCzt_hoZVpTWKl2tmdeea5sgq9v5xGOur7HOfkJlZccwBFPUCu0shAzj5RD3q4ZIDSZs6MiJwIVLQmhTwLXYA4WZml68Q2AiXq0u0TMZ-Fu3H5iGVv7K0q-osUa0DtUTv0yWtyrBedtPzO6rIrPPFrzgfI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ایده‌های نویدکیا برای تغییر قوانین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99353" target="_blank">📅 11:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnEdIWjOTNyvKx9Z9Vd9fue0V9re4EbHFzlUKYSApd0avOnP5BIfhna_AbB1Y-MsTK4KjdSeoXhZgj81zuiv43TfrVXCzvUVIDlDwTlu5OGpggkpdbpTQNylY8IMwJ-ZuvSFIjN3jgaxnNM2lUx_dcHKAcNlDkNZqmdThzSyEt5vTKtyDuDj9j6HhyZSBop395gmgx7H9Nv39i1MK8L2qc7x-gnT1Otwd3u4kJb1zQxyh3IOjglKqCeuvPQKVSspre3bnfQLgKsBhn1sibMA_K4ZtTeAovhPW838UlHqa2Bbr4B_RM1cXLnxNo8EfEjfMmsIv1mS0DF3YzYw70flNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو در مورد چلسی:
این یکی از بهترین باشگاه های جهان است و در دهه های اخیر به موفقیت های بزرگی دست یافته است. این افتخار بزرگی است که بخشی از آن باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99352" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc842a555.mp4?token=kd7hpIxU215kCutcVz7fEVUbUbCK7hgpE8aWDjAE54uFq8TqU0RGZKzTqTtjMQwOJvWouTGAJwz5qhxjgdBL0vEOkCpXr_LI-kVuli3TCCAje1wk-5nYD3tW9ZRg6byDqnpBjRVt1bh9seL9zJ6aNnLwAql__PaNmJKJkgtye8EClhVZpp2YiTrDckEsBcoD1LYopdj4k9nhBOYndz7lFs4t1GIhZns8mSsSSZ0e2btTut2VnnxY2YLiZM4oO7ewvZTsWAA7Xvogzk3u-qMi3J8F1xcB9mEUBYn3Yy69EOioQv5xBAnqfFPD5RjMAOJNDdUDkDPZkcYzms-kV7PVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc842a555.mp4?token=kd7hpIxU215kCutcVz7fEVUbUbCK7hgpE8aWDjAE54uFq8TqU0RGZKzTqTtjMQwOJvWouTGAJwz5qhxjgdBL0vEOkCpXr_LI-kVuli3TCCAje1wk-5nYD3tW9ZRg6byDqnpBjRVt1bh9seL9zJ6aNnLwAql__PaNmJKJkgtye8EClhVZpp2YiTrDckEsBcoD1LYopdj4k9nhBOYndz7lFs4t1GIhZns8mSsSSZ0e2btTut2VnnxY2YLiZM4oO7ewvZTsWAA7Xvogzk3u-qMi3J8F1xcB9mEUBYn3Yy69EOioQv5xBAnqfFPD5RjMAOJNDdUDkDPZkcYzms-kV7PVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
ناهید کیانی: کیمیا علیزاده بهترین رفیقم بود، هیچ وقت نمیتونستیم با هم مبازره کنیم حتی تو تمرین‌ها چون صمیمیت زیادی داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99351" target="_blank">📅 10:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99350">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db66dc2928.mp4?token=E2xpp2u6Uj2bJ4f5DUCkvHcAM8aR2goxKRK_2FxrIJ486Jtg0FqbQHFZirhEmvV139tG_sH9oyNj8Qi--kxV3t2RASyg9rTMOVRSPD4kuP9LKD56kiiNRqlZO-XwbnVaEhz5a6hbe442VW_o4Ji2s6LCNrOzMy9urFl2IkyTKIib3u_HoEvEJYMKNRwOqTmYpb78EFChsu67ArhE773Q26U02HQe2tYGHr7N2Bhi2ysBX2UoRK88PvvSrlWLHuOGTHbo2GySDkA9wDbkq3C-y-QuZtXNcfmVHcfzxaATGS6U0AEoJByfImnzCa9Q1GtXZuxwj_2oWPVrbJCpcluEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db66dc2928.mp4?token=E2xpp2u6Uj2bJ4f5DUCkvHcAM8aR2goxKRK_2FxrIJ486Jtg0FqbQHFZirhEmvV139tG_sH9oyNj8Qi--kxV3t2RASyg9rTMOVRSPD4kuP9LKD56kiiNRqlZO-XwbnVaEhz5a6hbe442VW_o4Ji2s6LCNrOzMy9urFl2IkyTKIib3u_HoEvEJYMKNRwOqTmYpb78EFChsu67ArhE773Q26U02HQe2tYGHr7N2Bhi2ysBX2UoRK88PvvSrlWLHuOGTHbo2GySDkA9wDbkq3C-y-QuZtXNcfmVHcfzxaATGS6U0AEoJByfImnzCa9Q1GtXZuxwj_2oWPVrbJCpcluEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
احترام ویژه طرفداران مسی به رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99350" target="_blank">📅 10:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99349">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6YFJx-Jbx1WnCdjjNGJB6iUh6b2yZccg9oZHU9ErsvciMH9CZNoHS8u0YNiEv0DXqNpcJ-gjwdS2ccjCaso2cXaA5fsECVCCdRs3th1Uyinl1VSaMFHFnVvMfvHXUPEBr_qLnyI5tfuU1egPJPY1vAXv87n8CCn1NcdC3Qs093SBUXKRyzQ6733vcYsV84f3V9d4LV0b4zCRk5PxawJKOFy_BhCV8enp_WLFuh7pfr0n-Afr-sTVHALmvlxjJW1MomHoqU2Fpn0UasbRmAUJxoE93_2ngxwx5y30KKdH1VN0KZGL8Rf8bWxrnheGTZahxeVN0DNDssx-b34iFaTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
🔥
🇫🇷
آمار تاریخی دشان با تیم ملی فرانسه در جام جهانی:
‏• 25 مسابقه
‏• 20 پیروزی
‏• 3 تساوی
‏• 2 باخت
‏
🏆
قهرمان جام جهانی 2018
‏
🥈
نائب قهرمان جام جهانی 2022
‏
🥇
رکورددار بیشترین تعداد مسابقات انجام شده در تاریخ (به صورت مشترک).
‏
🥇
رکورددار بیشترین تعداد پیروزی در تاریخ.
‏
🥇
رکورددار بیشترین تعداد پیروزی در مرحله حذفی در تاریخ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99349" target="_blank">📅 10:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99348">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a112d5bf.mp4?token=fVTvQb-2uns4L2ScYWSC6xCAFi1KwISa1VYKJTIyjFdSq2QVjmUIy2mblHtRTP4VjbeawLZkCcAQDqRzgnFueeTdvp07ZvUgVjfX69J3vO9X4DM0Ii4F6KU4CiaQYGG5iPYTzb5K6Sx1obhjtBCYHrD0KGcovWOPVYxf5GvQ7tGmrEn9h3kqBpIlPE3aCdkYDzppKpsaK47qmhkIkkXTLKS-IFiaU1rpV0jPfv2j1SLVFKS9l2pVxA363ppK0DZa9KyU3t0cG6Onid6mU1AA1VgareBGAFr-WYe1MfuEqCGboskKoTllB6xNh2paUEE8UoIF6hbry97BeA2mOsLa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a112d5bf.mp4?token=fVTvQb-2uns4L2ScYWSC6xCAFi1KwISa1VYKJTIyjFdSq2QVjmUIy2mblHtRTP4VjbeawLZkCcAQDqRzgnFueeTdvp07ZvUgVjfX69J3vO9X4DM0Ii4F6KU4CiaQYGG5iPYTzb5K6Sx1obhjtBCYHrD0KGcovWOPVYxf5GvQ7tGmrEn9h3kqBpIlPE3aCdkYDzppKpsaK47qmhkIkkXTLKS-IFiaU1rpV0jPfv2j1SLVFKS9l2pVxA363ppK0DZa9KyU3t0cG6Onid6mU1AA1VgareBGAFr-WYe1MfuEqCGboskKoTllB6xNh2paUEE8UoIF6hbry97BeA2mOsLa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی یک قهرمان ورزش کشور بدون تعارف از واقعیتی حرف می‌زند که میلیون‌ها زن هر ماه تجربه‌اش می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99348" target="_blank">📅 09:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99347">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2516de958.mp4?token=dyGVe4wLI5z1lfkNLXg10u6SsWlhfGBRwrbpAu_BUhedDiBcHaf-Afb3TSS6nVfAj-Pf3hlxR5Lf8XezvxgL84X55Cz4KyYJLHMlCvvKPQr94v8ds-_Nx2_vvmiajddxvOGg9lm53CRw1m0PKCIPhV2Da61yph5HU1msDCoF6ikD3z8JW3TCIdzchiL74Y8WDUqXem9HRcsDa6DXr6IOzYGkm0B2ATks9_in2o0grvKsaZL18MqHCIILGZJ2wKTkNU1jy6UCiG4qZVn6dpMcv3a_uoYK3oSvTdVY1aPSwPpG2h6A576ZBMZQA_yvaTk77OE3xQi04EX7fxJlL4Pqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2516de958.mp4?token=dyGVe4wLI5z1lfkNLXg10u6SsWlhfGBRwrbpAu_BUhedDiBcHaf-Afb3TSS6nVfAj-Pf3hlxR5Lf8XezvxgL84X55Cz4KyYJLHMlCvvKPQr94v8ds-_Nx2_vvmiajddxvOGg9lm53CRw1m0PKCIPhV2Da61yph5HU1msDCoF6ikD3z8JW3TCIdzchiL74Y8WDUqXem9HRcsDa6DXr6IOzYGkm0B2ATks9_in2o0grvKsaZL18MqHCIILGZJ2wKTkNU1jy6UCiG4qZVn6dpMcv3a_uoYK3oSvTdVY1aPSwPpG2h6A576ZBMZQA_yvaTk77OE3xQi04EX7fxJlL4Pqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇦🇷
🇪🇬
مردم غزه درحال تماشای بازی مصر که البته با باخت مقابل آرژانتین همراه بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99347" target="_blank">📅 09:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99346">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab94d8d11.mp4?token=qdHqyuulBjMMCiZ1bVkt1rObSWJrjwSXPIuz_ixGQvQ7-kQ4vl7M2xyaDLTdmzr8ik2oaBtBPGxTUZVxAbOQ3mebbWgPirLZUTtFHBJuWDIjxOY4vGz2ByNLo-MMDY7MKjbghY-Lkd0KiCCQVoN9I2Q7WTNQPVcWBazqkMpk4cQDusf6Lczyg0PX9rUlDLgqAkq5KkPxc4ZbfvvQ1NvL0AtLfAf_FwL9xl8idjGczwkjkAz3csX7KXU8bZqFbXjEPz68sZ8hEFejEZ9wrxrG4mvgQ1kT7G84dH1A-0OZrLwT-7ke3SUKbrtyzK7_aoa1MmpO6N_kVNUuT67qbD6zhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab94d8d11.mp4?token=qdHqyuulBjMMCiZ1bVkt1rObSWJrjwSXPIuz_ixGQvQ7-kQ4vl7M2xyaDLTdmzr8ik2oaBtBPGxTUZVxAbOQ3mebbWgPirLZUTtFHBJuWDIjxOY4vGz2ByNLo-MMDY7MKjbghY-Lkd0KiCCQVoN9I2Q7WTNQPVcWBazqkMpk4cQDusf6Lczyg0PX9rUlDLgqAkq5KkPxc4ZbfvvQ1NvL0AtLfAf_FwL9xl8idjGczwkjkAz3csX7KXU8bZqFbXjEPz68sZ8hEFejEZ9wrxrG4mvgQ1kT7G84dH1A-0OZrLwT-7ke3SUKbrtyzK7_aoa1MmpO6N_kVNUuT67qbD6zhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخی از پنالتی‌های از دست رفته جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99346" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99345">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw6XzimVPJusUSeR0HKtfRxKcMKZHtFxyeotaD4oSkUnpyo5OgzjvgX4ZVWlRIQAvYkvPDscT-OSmXxHgfGftHu59vINeMoQotoTiIR97VwmcUtOLMfG3HjSGJqUyjpI1Q4UkdkP8kMEFWHwzeRAUELKdTCw6upBUnubEkkb7KlLfcpYDgIu3DWDCMF13s0O6hY304hYtjcRz4RPFrCZi27cK4B08It3ljefox0R4kXFAjh5E0-N983_PggzfSOFuRvB17zfj3wOCJMT8IIL3o923Yuc0EZ3DS9AEFznyZ43nCYqpDlRHIRZ6fHsXh258efhrdzF2gTT1qR10zsJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
نیمار قراره هفته آینده به سانتوس برگرده تا در جلسه‌ای سرنوشت‌ساز با هیئت مدیره سانتوس، درباره آینده‌اش تصمیم‌گیری شود.
🟢
نیمار پیشنهاداتی رو از چند تیم لیگ MLS داره و
احتمال بازنشستگیش هم همچنان وجود داره
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99345" target="_blank">📅 07:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99344">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2abecac88.mp4?token=Qa6kklQFLMzwg-WH_hjOJQw0Jlk_bruLleiAHTDsE3pbHJhNZiziBM99xKc9Y_PoKEgX6e0kPuz01jTpItLiO7cHG3Ib3Dr8WgQ8HPFqbP6eQXhXY5PEwkbktSs2p2Lc2aAnK4zdQh8vRfQKxtVuHp4Z7V4AwYQ3cGSyvx1BDFG4M3p6AGd--wnoG3A7H-9I0RkjPgPoKk15rR4z9xY2vgMjicY1T5t-CLomyxXkwebafq93PZdnbbLHfmDMe_BJ1qaeoWTtsW4sJ8p2zFyDRG24TkALyUo3tM8dp5pt5gN0Hac6V_WrEbStfI03L1Fabi1sk5LIC5SPMpo7ID-z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2abecac88.mp4?token=Qa6kklQFLMzwg-WH_hjOJQw0Jlk_bruLleiAHTDsE3pbHJhNZiziBM99xKc9Y_PoKEgX6e0kPuz01jTpItLiO7cHG3Ib3Dr8WgQ8HPFqbP6eQXhXY5PEwkbktSs2p2Lc2aAnK4zdQh8vRfQKxtVuHp4Z7V4AwYQ3cGSyvx1BDFG4M3p6AGd--wnoG3A7H-9I0RkjPgPoKk15rR4z9xY2vgMjicY1T5t-CLomyxXkwebafq93PZdnbbLHfmDMe_BJ1qaeoWTtsW4sJ8p2zFyDRG24TkALyUo3tM8dp5pt5gN0Hac6V_WrEbStfI03L1Fabi1sk5LIC5SPMpo7ID-z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
📌
افشاگری کلوپ درباره انتقال امباپه به لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99344" target="_blank">📅 07:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99343">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuJRzR0QMZRjAmVoPyTRCY2kPdGIDT1AJJctpjSNQ-VaFvC39h_gMzyb618QKo3wlf1Q2VEbmN9XONjYMeQ_h2cvN4XA6poJ74dh8-S70O5x7e60U8k1gKkRbIXLwsya0n3cFr6pTRRCfH6gaJwhC-6BHxQs-hV-OX9eMUfuTaesiskGRskVY38GNRuEaLBZQSPQZgl9ukI5cSkyuFmItmOmQsCRTE5TIhZF2YjN7nBYhhRGLYa8IwKc86yBDxeKH5TqgsjTRoxanv1yyQij1gobe3lXCIYgQQgc5-ZtCYuvcnvPaH4xGdP8DY-GYmHt_E3uInsYZsojmnVAHJAJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Legend
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99343" target="_blank">📅 05:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99342">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnmBcbspDEVWB33cY7t7K-a8KRp2dyO9p5Sw-K2qfMx7UScA5Jr6l1IdwslHvueA7oHf84AGePIjDGzXhjNHitxNuotrm7Z02EnMJIaAwP1rXv2GYAmtRiHVjS0ZMTYkcKpOIbhNKIJv9Psi6DH4X8u8Ci7pWwwhP-wLGzdDsxVX-ucUnuDkFXBLMSD-a_7TxqHdvxyeIqnTeH97NM5FKcw_HizNIWTMnHjeVceLvf1kEg62U-zfyK2Iojirwl9zStdPDmEKtw6cTnJ-V2UlzOGYeyfhaIiqvZvekKIqhxLdM1ALH2ECkaqhj-DDDnf6iBQnIel73JHGobPwGAVB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
مصریای کصخل بعد بازی با آرژانتین یه کمپین راه انداختن برای آنفالو کردن مسی، بعد از 511 میلیون نفر فالوورای مسی رسیده به 512 میلیون نفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99342" target="_blank">📅 04:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qut_ymDc6ynM857jX2XdiDbcde_lnVC76PTJXCs3YRzSLC1VrUH4yZFrd-u84knHRC7oBUNzQ5mdmRAEjx9UgxNsAi6Uka6P-AoW21hllsWjLUIQmZ8YygQC3Bz54unrvF_xpa_ks1ueUa71y96V7MvARl1YiI54F8bxXXJ3b9bSKtl6z030zpmsCbvJ5v3Fz2UcWlmjhNTWubmp2ndqu3RPzWyzjW-NP8fgNoS3IhMsQw6a1q2rYbiQNXuGZeXFqqX822qxv2fGhp00uzVEZyGJUaCbUwey0FoiTxcpS9xrA4r8eTBo9rOLrJJyvp7gYpYjd0RcXwSv0R98nvk8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwpYhskUAEkz1uL3PnLvcJC2sYPmHE4DFVOXoa1VRZ12BU9OTb0nELqCJhjjmw-N5tj8T-Af7SOo2-rpixe65PFSMIxw-wrN7aLzQtrWVSilzKuBt4HhN6vRUmzoGpniJpOjxCQ1laJG4ojffaeLDdoa6AAjmgav1Qu5Y9oEpf63AsJV9zfkhlxlNsDd82GPWNlZSfTNHWQDD4scYHuXSevWV65eBrZMi82FbmqfiIAbwDG4KunDqF_q2p2btHF1hW64fYTyylg7LRtDkSDylZXB-66zVXZWXTAjf74NN9sxG54o1jAyCuEivzxHGrxqJey0Vi9J0k1YMDWosVVBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkU6V79P8HOXbIM4_Dzfqg1osp7XeDKgsC8lzMdzmW4Qi_syITLqPpFUpn5s5tGgkw8ZlLG07EfVipdMGkXKmw__JtPfKSt1ZyB5Tq6JkEOPv5cIDvgr8ETnqW8dUqwPaQwBzePYhIvTnIymwu3rnxPuSUUSGBflGHOkc6QlnEEeDciB6E19nhDxltfDf57lb-Sqf8F1g6L6P3owafNkFpiaCvwIvRXqisy75OENVxRA7pBr-B0vLuwCXcxyYLaLqZbEzz-WU54SC_6xWK-mgfCPvzBbApXzUPecoP9N-5OOpz3ht2snVSumXNC2_puJwt8E7MQsH8RJZjj-gS4cKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7eoIftTRpi60yar21dSzoQn1uciKpcFp5y0cqPAG2OV9S7nHaSzCqBy4Sj6kIRqmnZchIGfe3zcPBOrFBI1SaQnD4gapQQAqb3h9MHA78Fo25a1xlAjTRu-xtuMW6UuPd8dz09xzgwF_licLSrz3vCfAI-Z6vDtcGpJwhoOMS2Hrpd0jNRG0CHduHnaRv1NMVRX65b84-miNMs9pWlgJIWwy-26v7w66KYInKzTjQGjccBnr8Ir91F12DrkItiksuxW6VS88l-YssX1CW6RbTGAMk6v082Ltqs_bL31Lu5EsSgnuX4zaEIOslN-bvldqynctZUXibppR5DLeqmZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbYBDDD2f5Fh8Zb6WlKv9CLPKw7Y9nl5TYo93esJhV2JBTsJ6YpyN69VqxsDteH5LMPotGuN3Yy6BEliwsdjKFFlzvvL-mcSf2m1hi6YZmRxJE31CBh9lI-zq0ebwrsQ4Qv1baYmleTa-Tpbc5GjDfNIidd4Ro92U-K8qpsTgnYAoPT_7FM4H-oyYE3FrNfcVpurxBkw80Kd0PKjWVCZBc5proihmqkCo17X2PeuIiP9ga6ghjWnr08fvOu7-qoX-gj1pp4XzZPDMX4et8HjbDctAlcNOJ5-ZEekAfURBYJhb0ooRRFponvsulwUNg2gmwT7f_PYm3E71jGtDeprpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99337" target="_blank">📅 03:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=DLn03WCJdDM52nm3hPFKMUfbZRTgypnq2wvKYSkgSCXqC0hs6_XatiRnv6hbg5r7EalPfJMqF4ub-FbG8dIv6gxboUsVL2CclA0lo12sdTGg52IQD8MNjgGY40m3nR37Vn31moyvVKLkFvJBCxWqOo6aDdZqUjwOkMxv1A3wFtBO5msBHa_mcDOpCbrwQltze5eO6cUDlN8rBCXn_xVq3cvJufjmKU9abvYTHEJHwyFNHaLMFuYoui66hKfwy1jFCqx6ijdKSakSwy5O9r7xd5ZQZiUhLHBv9RvVyX_wgmvNzj12hPYOmQ6XMUe7swtnjlpTg6sDaj181cVLqu6eAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=DLn03WCJdDM52nm3hPFKMUfbZRTgypnq2wvKYSkgSCXqC0hs6_XatiRnv6hbg5r7EalPfJMqF4ub-FbG8dIv6gxboUsVL2CclA0lo12sdTGg52IQD8MNjgGY40m3nR37Vn31moyvVKLkFvJBCxWqOo6aDdZqUjwOkMxv1A3wFtBO5msBHa_mcDOpCbrwQltze5eO6cUDlN8rBCXn_xVq3cvJufjmKU9abvYTHEJHwyFNHaLMFuYoui66hKfwy1jFCqx6ijdKSakSwy5O9r7xd5ZQZiUhLHBv9RvVyX_wgmvNzj12hPYOmQ6XMUe7swtnjlpTg6sDaj181cVLqu6eAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه نداره از دوره بعدی بیای آلمان؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99336" target="_blank">📅 02:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f8503771.mp4?token=FHlcjMrfos9KR3avcdWazgrVH9WXjE5C8m39ny86iEHwC2g-rsn8FPaEfojWTGRhbbobpAc71i1ueCbnsoywBm0DI1_R5kb_3xEHkIDxkii9SU-SfQHUkyiSxrvcWlGtFx1LQSctyCBLlLygTcpombcQqsWn0tcN3SZwEjKZWQhuVTbF-3WqHLPW5JO_BO4JOKRvR4pQgxDouY8NNjuxphFUM0xkjw3mfeyvdEAYf_5wB40yFC85RZmkpNXKrQ5w1Bylt_HRNnXhYERZARLJ0lAxMSmFk9Le_9Sm6zgte5OkizhESp_7sJuRuvEkX9we-JUx00Bk4VT4oiXV-gS9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f8503771.mp4?token=FHlcjMrfos9KR3avcdWazgrVH9WXjE5C8m39ny86iEHwC2g-rsn8FPaEfojWTGRhbbobpAc71i1ueCbnsoywBm0DI1_R5kb_3xEHkIDxkii9SU-SfQHUkyiSxrvcWlGtFx1LQSctyCBLlLygTcpombcQqsWn0tcN3SZwEjKZWQhuVTbF-3WqHLPW5JO_BO4JOKRvR4pQgxDouY8NNjuxphFUM0xkjw3mfeyvdEAYf_5wB40yFC85RZmkpNXKrQ5w1Bylt_HRNnXhYERZARLJ0lAxMSmFk9Le_9Sm6zgte5OkizhESp_7sJuRuvEkX9we-JUx00Bk4VT4oiXV-gS9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
😆
برسونید دست گزارشگر صداوسیما بازی امشب مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99335" target="_blank">📅 02:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sL4NkLxQIasg_NzgicRFffN6UXKtPdtOZtDkcHVpL7qFn_f-aNXrwBYLlULRpd6rPo54v6F5mAxMi-qngtCj6UY61pYSYIgEEFoJqgTK1EGsqPaFC6f3Lak4I3vXqdxwIl9IKEkZ0R1iYNtoHjmqNiJ8v6bYReweNn5rYrVo1xLUUTKvPZ6iPNMqqIIGaRlmlkYu6joZfVGjDalFNlCOp2r_ojywledX_T4TWHMPorqZTpjUwYE_bxPmW7rLWarcv9fgJD0ExfZhw9rZp9FSPEUFGxd2y28X2pwbjts0YaBvG5ikvaU6Y3ZoBL_Y7QdUB1pl4vGxhefPbqRsf-eM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_O2VtGjtG5_QjHrMehHG-VXPmFckwfTVq5BlO_xiFbBqDkEwBtCGPQHJGcNqW5kmjkN5_u9vbvfGYMwzub4mGg0mZFPo2YYicCUL_UU6z29Vnngb-d6NV6K_JRyv5o96cOfO2l94e_c1LzTUp5LNt1GJx2l9N2Z-wgVGpqsWEFDJVvH1P0BGOs7pajI8nbWSdwcc9w_hLJOG-S3vxjmxSUaLg-5d1eh9q0km3s0TrI6WbHjR4BDk2lHw51bNaA98-WqBHydyCCp0L0wipEzZMHAlGh_Qlb-l0_SG_fMuHX-IuFwvf-tzVxcaLaa4ruuFqwbtp7UNpbyodFI-uyNcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
📊
🏆
در طول 60 سال گذشته، تنها 4 بار پیش آمده است که یک بازیکن در یک بازی از جام جهانی، هم گل زده باشد، هم پاس گل داده باشد و هم یک پنالتی را از دست بدهد.
جالب اینجاست که 2 مورد از این 4 مورد در 3 روز گذشته رخ داده است:
🇦🇷
لیونل مسی در مقابل مصر
🇫🇷
کیلیان امباپه در مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99333" target="_blank">📅 02:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
🇪🇸
#فوری
؛ بر اساس قوانین لالیگا، بازی هفته اول بارسا و رئال در لالیگا بدلیل داشتن حداقل یک بازیکن در مرحله نیمه‌نهایی جام‌جهانی به تعویق خواهد افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99332" target="_blank">📅 01:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzcybzkO6bfaXHXXatx2hYNfva5WmnKgREgK6m4RXU27rSTEDGzqkq32IaTsyX8alZ0XnQu0opsp5GZUheKxmd9Cj40LWK4eDv15LxKqD9plTcAQgbQU5vvcS5M4EvwM8yVi7jhIeWcCKpR4XdJGRgPvuDiiafhVZKkPLDs-S9YJrB7KkJti9LXhHUowAMtpUPDqEGZebLzLkVcjtz98WERbuzqulKf30OiLuu295CKt2VVKu7Rh34QFUQCJFqhxbKfqG8jxcpnZPT8Mn9Bi6WXSCgh_lMh6XMEYKoZ18y8_hrD0nDdcuGBCrk7J0-4enH_vn90l1eBsL13raAmacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🏆
| تیم‌ملی فرانسه با قضاوت داوران از آرژانتین تاکنون 6 پیروزی در جام جهانی کسب کرده است، که بالاترین تعداد پیروزی برای هر تیمی در تاریخ این مسابقات است.
🇫🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99331" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKIlakhCytDijIX6L5x42ZtAKtO3VGVxBYk2uYKfXoL2IR_4WohNTXm2yevwDmmtRbo_JryEWqXSS_EiY9cJQrv34K_C6LQ7YRQxJoKu1G1-d639ku6sNpHnkSXYBw2HSmh45vbP6xwhsx1MRgMGmYrFsrGX5tfg6hBBTo-eER32PatGDHYe7-r_vEo-t_kSSxxRWaTvH6GxLhBG_TJ2uz9Xy7qIQaXXYMh7KKYKKp6JdKCUJBKupG34O8NsSd2WvF7yvvHZmu7LI1QdVtShWQlTi9JisXiTqvaK81ZRboIQVH1sq1RgKQs75lRYmzXWUscCw-Upj5Ec-OyEmxwmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
کیلیان امباپه: از ناراحتی اشرف حکیمی اصلا ناراحت نشدم زیرا در زمین مسابقه چیزی به نام احساسات وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99330" target="_blank">📅 01:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏆
Man Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99329" target="_blank">📅 01:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC8mHO2gJ_x782oJGVuaFT9736KDXaE3P5AXwNQ44AaW-YLc8CIU25kr_jIDE3jJjjO-xbLtg4DMgG5kpTBFJMhWHQfzWpgX6CWTOETSZ7SSBO7HiGl8YTVOXNvgAzWGaW7JZWRTWHWhkhy-04SNdkMdQUjcMe2xGnkrmuoJ_aWz2r69zENlL30LGvA8GRTZnUq9JZ_hGOsQZI5WTlJUZkZPTF2jIqPE7EB3AMw5AFyqJiK3mBUFNNeyIul-Q6sKQ4Q8Wup3DLelvp40tEJPrd4EVkHBB98QDmKFgN3dXn_y2H11YyxzwDADxP1q64zwghhko_raic5FG0OaI_Kpqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
M
an Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99328" target="_blank">📅 01:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOBYE15n6yPZ8Gu1ZhovhscfPI1rJN_20n2wEMTD9Sa4OCUjtPRHo2C2pyF58lMoopAYuJTQwqGoZIcyUvczNyfrvOcabO-nbd7i3xv7eUU7u_aq0VjpId2nJN5G1DjukTXYlUpcwTV_vnk-9ZrRqYb1GBACK_UF7ztnINWqvCcM1LQQp8V_7EYkjwpjIgdA0m7hQdz11uDv8k-IL7BNDTuRx2W8tdCIa1GuYUt5cyfWipzVWgy-SLrsxsPRGHe2oeq-eAfT39Nh3KhIM0CRUbJRCqGG9VEafCiZSRtG9enxUJ1jgDTH0MoJKuNsHt1dMyUbfeBN6LP6KkZy5gTkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/99327" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OexAAJlZ4ap3QhWFjRc9O7oBF9PfrpIr23GDCcVvUlrempWdgrFZzsPbJpbSKgmBVCMigAluQezbyzWtgEnqhcoVKBmTxk1qrX0qYDEVY2DjsK7N0p19KQGsb3Sg8G2QklMxzaxAoNVF3z_4LUQAzcCdDH9VozN_jiuEl2wYd8cE6RV3-i37LOd-bUCFmyPAbcV3Z3TheRxeSGymNYFQcNd4SGzWYMPzTz9v_iXfO_KJqPc1OYNJmJyX2aJbZyxcuxbAPtyqrCErk_w5KX5cV85jMkt7OGHYVgr-JNgBIkplZhGPO7aCA-o3zWNMzW2c8x-R-aycwLM4zQncGPiKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمامی تیم های آفریقایی از جام جهانی 2026 حذف شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99326" target="_blank">📅 01:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFwEGvuBEgeMfrcXXBqZbIRQ7wUDLBQt2QaqY1OGjrDZS-GZa8Xryxn7MoH74e7gUr20F7qaZ4XmtRv9rGg1nFcfTcmmEsKUiA7O2pWsTA5hA-tjR3b6mwbRE6wSCm04m06MjlFjvT_WxWveowal1jERf8BIg3r9r2mhkioclxjYZPP18dw_Q26mDpSKzurBvzCtEX8xofkIwa96gUwQlpC2C4ioM0Dxs9A6ahhCcv-Ht4rDiAgalWpZ4xqvGvcbakIjN25wmrNVOyeBpR9JV4sLiG0IiyqrWryCq6EB9x9_otJznkh6QNmFWxkGeGDrd825JNDsmST7FB4H-6PhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان با یورگن کلوپ بعد از پایان مسابقه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99325" target="_blank">📅 01:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-RvFYt4ydZCcgQ_lZiZAvqb0sDYPu6at0uGcH0pKGkTkbsDOsbWDv_1hVg0Lfzk-clZSSX5IxIJo0dXC2GKlHq_ArreK37648R1Nq_k9JcIfE5--y8fUynjEw3QTz9l51_LYpKe20uPdcYwick9_fhArfyEhwAempZ_DBcM4S9ENPnpbQU3GemM_6wae9WJ6qdfuQspwabC_wK7l4b4Kn1KKBD3DgCnpjsKVESD2w7G152sZejh6Hwn3vRzicDeaYlJ8CZmXuvyKeGHggAowfvr2utzz-VqpK-BP-MLPpXDcc5qwScfRp4lrTW9jqhUHY3DqYq0aweBNSJ-e-d0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• کیلیان امباپه در رقابت‌های سال 2022:
🏟️
— 7 مسابقه
⚽️
— 8 گل
🅰️
— 2 پاس گل
🚨
📊
• کیلیان امباپه در رقابت‌های سال 2026:
🏟️
— 6 مسابقه
⚽️
— 8 گل
🅰️
— 3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99324" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBmixZMSmfKwBM4qTI70UbunnINA7gbupYm2oNtYHr3piQEYRYvaauAr-_M0wRNRZS3i_PN4znPpY2tISfVJZX4SnBZBOEzR3kyn2zmfe9zHY1zvck4mD9tTcquBC1jJaujTIEmBXL93jXHvCq_Bx6mdIhScM_ewl0cByg9iUvydxoU-In3OiEbnn6CvGIIXX1zBGsGQDkqIud7T3i5CYrjqKuwA7iyaQcWIQzEQ8T25BXJSg1R6lZIHVOSdQKMHlwllnJL9UOzpxm61PvmLfEppa8Ri3_7Kf4MCfjIKFPBXH7UINqJywNuKoqzgtumaNQuWr2dEbv807oK3fD0aEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آخرین آپدیت مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99323" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snU7FqEGxUr-qWn1NMjaPpvupeQq_RN68GyFy-o2gDh7m2j30AfW3MJ3Bczzg8H0N9psrtIcWxPhpcd8cmRPAb2jlEEOb6RtEujlWOMnpDSkMh73p1F98B0VLW3qr7D2Bumu-ZeKGOQgLhwGBJXHcbqdQ-hu5s8UDk5uV9zjGE4Rtkp4Gm2dp2o6_9uYiDwCEQfSS08ZESrI60ixR6ENyhyi3lOeYOW4ojKMGZNRO4ZCsPduacl_5ppfIC8ffXi0LiVkTaSQjxz3fHQmakISBb0-auJWOHdLiM50k1LYJczcXBP5snxpNehFM2zT4RNGlLSc2WS2BExSYyosAPOwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 بازی در جام جهانی؛ 20 گل، کیلیان فاکینگ امباپه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99322" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTc54q-TXy1Pp8k8Kiy2-IHYyMuApevZL8gXuyplXOy6AijC95vbhtyPzp3fPkSOUHkvCw76daRXaYHAar2IL9bdFxzXmSKlsabbdqADtmpp_0MP9jYk3bOr5bI9dX4RjE85wU7kBDoFS_yrgW9vHhmARIuqyQIlIpQah9VhIhftu2Kg_72R8mMBUic-OrFqm5Dx4D7SDDSlZ21lm4oXHPkIxVcCE6zFBeEMRWLSwZ7bPPHyyLgE9I5oiaqazWv2rAdzDSna7o-EDtHXgdrRUVbFoETVdc4JeSgEIWiX995EHaDUqe_oj4djUkwabGGVuQT0trD58uXZOluRpEgSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfcSaEl6ZDXSXD9Oyw5ckoIJ3Y5yupp6m160eqkstNOvJu4eIa9Mb1F9YxuYNRzCs3NQChd0H7jcP_le-cK9gZAsU8BNKWS08mDtNBk5lxUXZuSFXeSi-XEIf-kh2-krAFNj-C9JTXmjyydByL8UjkOxpUK6meXhBy6QvPH02848xOq01aMG_FiYgW8HA1_7wei9FtgZ5paFJWG6eYiMpkcYWrAqzt0ssAs31pxSsZpfrtQZ4GxatXxB9GDFE2ZJ8dDATgwZ3siArLEb3K-3A0USuc4yF5J24QuerALEfBHqzAXAHjNPgZz0p_fy-JS1CeoOCESZKweSzE9b2O3mfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1lohrNWHlCDBNmsDJiqAlFiih5zyaYeru9yc5a8FpDNh2dY8abMc5EQFy_pOfNU_rLPhpLQeDe4BQlGPKYKR6gXSZI4liqlyJ2r616ShVOoT1Y0I8G50JQZTqdjWVANSZu7ZSnvBYR-1uUoQj0gmDS3gdwO7cheYZ1JL3NCKVjs6WxFCdcNdSmPLVLx14isRNHpEPFHsOpMZpaVjia0RxeN9OaOjPSPB7N1DTdjsF38G_kk6revAj_l_cwAHKZtQUQouZZSvPKj5-n3AQCUf4rWMBaSkMsZl18n7a9JZfTBlDuDCDWzF9W5BFmrKxAA_FsQVKzaGnZOSXyJ6oEWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3B-Gj2qJ_eEl20vz4i2I_WpoGvEbQ1RAqstTvklA4kJxHCHRy1Ir7e7Sgx0ZVZAw8BtF1E0144j_B-87OWvuiti2QXKx-60_pEO6d55fKn4Gaa5YCkV4zARRkzbwBG93jC5mTe3M17O2DfZ9RRe2vFhR3BJz_Dv5XtmPazM2w7ZFUISEjsfsFuRmJSNjdwKeUwLcIC1TUzgxZwKJGbuc2ax0hKJCSpeT2V6W4FfNnioWYeW1bptCIWiOZK79-EqHN2ZPFOtX8BrpxMDSzkiUi48ISz-z_eAXQYhbdQZXfDU93ueC3dwPu70idO_eA0vbFYjNgZrACix-ZQzQ0Z0_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🤯
📊
🏆
آمار گلزنی مهاجمان فرانسوی در ۶ بازی اول جام جهانی:
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
کیلیان امباپه
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
عثمان دمبله
🎯
🎯
🎯
🎯
🎯
اولیسه
⚽️
⚽️
🎯
بارکولا
⚽️
🎯
دوئه
آمار فوق‌العاده‌ای از خط حمله وحشی و عجیب و غریب تیم‌ملی فرانسه.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99318" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9k95oxljQs34B1ZO4YkaySoWc2jZzNok5ChbcMYa7dvKnwrbxoOpFsgvAQ27zrg0T8VNDt-ljZ6nzoSENn4S6fvFS1unAgpjAptj1D0i9Mf6TdGWSnUdEiUMBpKRrIsXvOAmfgCa1UUEA_KRX62QHcN4dVVaj0up2E2XLqOkZWrauV-eXngV3d5i2Xt7FCO3Trk6RMGlro3mIO5_ZjAoAIjauZEUa_FSswyal6zhrhDXtrFVdTDcLy-Wt_cNMqOg862qyV9WNFDTN47xzpZTu6P5M0-vadRFsUa3iZh363Sc2Cn49j-7SR8fHGPrgsIandw6KOrzt0E4I-AoZxT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه در 11 گل از 16 گل فرانسه در جام جهانی 2026 نقش داشته است.
8 گل
3 پاس گل‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99317" target="_blank">📅 01:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXfRS_qY3GA8sd-ld4BPpU8XT-BmnksL0WJdWiObnSkegu9iD2WYSUQa1M4cIpmSitI7nhp7WPq6PzBWg0Ofah7gYJvsJb5KC-V3a20l4l5S1EriFocCWXRahUEGPBgibl7UKdDjv8jXIprqh2sXaqGijMJw9wQnHHwnF9RZlx5njDdWcy11ICIX7eNZ6fcvaAvyQ8ycoVG3vRh3wZy7_bbE1ULMk6cev4n-9CkS8OnWrjWg_sM2Prl8lygAOHErYW4ZZTyIiNqmAhdVXA6cvSNjYRDaFWQLVI3ijpVWcy81oj76_RsSMj6Bhq-g2LpzN3cWoSWOG8u85_kczMN1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
کیلیان امباپه همچنان در حال تاریخ
‌سازی است
✅
اولین بازیکنی از سال 1970 که در یک دوره از جام جهانی به 11 گل یا پاس گل رسیده است.
✅
اولین بازیکنی از سال 1966 که در دو دوره متوالی از جام جهانی، بیش از 10 گل یا پاس گل داشته است.
آقای دیکتاتور کیلیان امباپه.
🇫🇷
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99316" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99315" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWtAkXizy_Mo3QaxL09IDfH1jAbtcQo7IkoS5aR-iSqCyptyTRzYX7diGZ-2kYWUBLabTKV2ctMZvsCaDGP9x43pnrlyPwP16VJZpfTtFFpMY6Iqg3vt5xHYr331tmDEf7ACtak0veK9CBCXyGxUxZoVW3inhzvHWFyYLb-RZAZN6NdC0vWP1R88ueu03J9kNSsuvbsCsFnpU-hWONPauU4BypvWEEJlqJ48Bwz5S4KQSPrSsyJAwZ-NRMtL-PRIZ5bWzwbvb0LhWKWfDcyU_Sz6jnUETkxH23Fu5AqIvTdKkE0pYdkzjD7mwG2Bow0nISpy4bxR4Cc01Qn1DHw0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99314" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDL-tyIVILSlUkSytMf8Y0JJXz9tvCld3DhCBz0TCOSoBWWNAegYJLL7REEV8W7RSbLe9caL9VU3yT6Xi1i-c_ghxLCyDDrCXdUb4Yx-ejvHfdtqRQKklWfcN5bwzMrcExeHhoHzKLLpf8MIcnp1eSEkmJTq6lXJH1RW7XalcXBPZf1GRTYdmShY1wR5FLXGJC7nF3Nmy0mNwrcSjw9MYJt70ZDVUgy7sb-tOYWyl5HkvAtpiO2hP2-8p96XJQN2JLRXzV12sQPKW7HrjQb4t1sJ8ec-vBSqk8K9yE-CLDx6qOsiN_wHaPH2PX0mK5dVACYyEdthPBCBz0J15dDsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
کیلیان امباپه بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99313" target="_blank">📅 01:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En2blP0VeoSSqkku6NDgzMaznRmo5YxQ5pIY7x_vivvdUb1t7e2-JV5FupbLnxNLdIOUiLdC0IncQEFvveI46CuWLChkw8Xm3bkIyB8bTa-UvBpfLQXNMfpPsK3iU3-1qt8kugAYoAnjlyNAo_Y1bl1j7ddAxIChwEBYvEWw9ON4hw57uDoZGDaMrHr6Bq6xxH_C3CixHLn5pH62HrwPC44xEMGSKnnXgDrisfmKLTPj7Ml1DcMgc31SZTwJKPeYgSzmSKdCOO0dZntOZIGmSNUcIja_gLwNWd8IvO0a4DOfLEdNbhiQpFg9_nnW4pdQbNQXYeM4fd2hkjxdoQlwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنده دیدار فرداشب بلژیک و اسپانیا به مصاف فرانسه در نیمه‌نهایی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99312" target="_blank">📅 01:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZP20OD93Qyz9hMD4sH0wYDcFuvKpwPWa-Rqqf8Dmdr8gv12gg2gD6O5jUePahQAva7d8nyuIHtUdtNjcrFxRmPE0-LI-z85AT3nb7VhykXY-LpcuxYpo_0cPmGB8ZclFAdq6QfmN2xOAoRv20OTEPxyalWjF0qGfYiaVqwzZjC0SLLZBw32NhUAqOneoVrf_Ec6ApmX-HQpo873fKPBiAsMJklGIzw3fnG3TbNDZX0xaIkxEW9zWRLwk2a4afiLy-HfuFzScyakrJZiO3mVlPD15cqnpxHD15CzVaR9CFujeHtLJzwaDzne54TKcHHZLWX3XuAQndhj_zxNbKcC0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|اولین تیم نیمه‌نهایی مشخص شد؛ بوی قهرمانی شدیدا به مشام می‌رسد؛ فرانسه به رهبری دیکتاتور امباپه با برد مقابل مراکش برای سومین دوره پیاپی راهی نیمه‌نهایی شد
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99311" target="_blank">📅 01:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl9rZ2oAfg9dRgV6qE-1wN3R2_D5XzMIb6DW9-1M96qUEJOY9sbYVnvjpuyO8sZpDm-z7rJscyU-5bd0gqidZKLL-KpwKM_83JZS2cYnTkI-cdj8eSjMxsVjVF329JE0g5idpvC5PE4cW_9gQ7M-3TqW7tImQBGwemigVARhw6_8TtjNZTBsU4QrR7Rr71CXnZNVcop7Fp2B6FYqmJ9p_v8d-omHzK8sNbqnkv4LuM4EKXM9awC9y_JqyEpnrtfLD-CL1JjzTbguph5n7hKo6Ww1MS9ZnhSp3WVgjJaF8y_hqIwjBLBdoZ-mn3CCTSQwHSxrKxFOYBZVcPFivueczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داداشمون چرا ناراحته؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99310" target="_blank">📅 01:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXDzthJmfARGpEm_HJmZGTgvMb6mHSX6wiEnIagNpT6-yuOjjEsvTXHjNkjKq5iDMoTDq0SeG3GobXXldEfyDnqG4YrjZ9_gxOP8VlT-oH5rQ0HTviWp_-YFp24KxzsBPCcr78AKXgi2OTEzbyUD03dw-ysXGnWzLPhJJXKibpoM4QrNbLXNfqcPbiPk-YKLEJEzwe7T7NuWFHfAa-KzWSe_iIMUPYEV2hLPXF_lfOoOevj8ChCk8Vb3n8BLR-1JoI4s_Sh-BBkJU4gORmC4o0SKOT3wivws6y1mMjfvUJDOSF3S6Q0nhtg8HN5QCEcpdhLPnKprFYmNp2HwWqf4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
کیلیان امباپه در تمام مسابقات این فصل:
👕
58 بازی
🌟
68 گل/ پاس گل
⚽️
56 گل
🅰️
12 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99309" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">باید یه تحقیقی روی آربلوا بکنن بفهمن چطوری موفق شده بود از این امباپه هیولا اون شیر تعزیه‌ای که تو نیم‌فصل دوم دیدیمو بکشه بیرون. این همه نبوغ نباید یه راز کشف‌نشده باقی بمونه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99308" target="_blank">📅 01:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5N-epY4b9-jDJp4KshPBqcTpHsuij0XAR51BDtRu1T77-_4Xc9AjH-p9qjrrrfF_AomAKMUD6gbLAZtfDThutF_7gTHzqoIrZT2LX7xrbjstbVAl3JGMGAEAqFAIzeAImbMaMIr2eX9UgMeaIg9lEA_JetL5xQZ9yOJxJ4En9YEVFxZ4Aqp6Uv_1iIfjMJng7_VG_fZT-_7tusErC1Kj12UkntBdaQrT0G2xBbLKN1CN17k3JKWB1XBDT27ZAnnbXM1IZWmjkw9rO1oXfaHETDS75wNvnrMKC5scjpnZHP3yl5ae1ZoUMowiUDN4a3eDtVh3TmPyHeXnBNxihT2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لحظه‌ای که لاکشپت درخواست تعویض داد
مصدوم شد یا خودشو زد به مصدمیت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99307" target="_blank">📅 01:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امباپه تعویض شد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99306" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plr-t52_ajc5rupRAp9fQwwTp5HG_Oyik9jBnb_v4RNFmxgUh7g70N2iDS_DkGulZUo9wptfC5MhQjj3DWaWXCLF8-nk_GZ56D7YSYHpegiJZAdzJD1R7M7_gqcPB-ibqmBxQLx6Glpvw2nLE5SQZvE3PzNgqlH4K4UXMPfAto8CCKO81Z9BeQ7gnpSQdbKNs3eVy6uxkKttvagUFJpWbeQU7Tis0ZZrS3X79q216kiPNX0K0LErf9rpgd1cdhdyrjFnnhpEQ9E2DDHgEvgYj9LQj74gfHtPfY829st7bgKjGHzMz6fZvm1CdFgf37G-j8VfbG5cgKgUZgqV7aGlCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌎
بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
🇦🇷
🤩
[30] مشارکت برای لیونل مسی.
🇫🇷
🇫🇷
[24] مشارکت برای کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99305" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f95dc0a96.mp4?token=ZAMoiCaat5EOzmKWgVeNCUNz1MblDdeEvHkUL2YOCUsNLUfI5DiKE8azG1e7B_sJ2RvAFd-LS8YAeLOmuPifPj9PqS-TWmSrMyACu-nq1YhZklKQ8PRAQEJTUask99LsC56LuBJMUNGoo_J0UC2NtokyMrOnzGSNExpApXHdA4tQOjcIxfY6UZHhY-xCAHFMU5YOLwkWQf8lDR7UUpR5VLjD8GvRqPZe8oqCwGbBuc5nPSLpJvnn5W9t8ITFP_zb7ifiKT6zsQBUeGavNnCvOm9VsupveBBID5b5_WiBizMy3CISdnlfcONr-HsyfVH6zRuNbn6D_oxIQwoB2gUNdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f95dc0a96.mp4?token=ZAMoiCaat5EOzmKWgVeNCUNz1MblDdeEvHkUL2YOCUsNLUfI5DiKE8azG1e7B_sJ2RvAFd-LS8YAeLOmuPifPj9PqS-TWmSrMyACu-nq1YhZklKQ8PRAQEJTUask99LsC56LuBJMUNGoo_J0UC2NtokyMrOnzGSNExpApXHdA4tQOjcIxfY6UZHhY-xCAHFMU5YOLwkWQf8lDR7UUpR5VLjD8GvRqPZe8oqCwGbBuc5nPSLpJvnn5W9t8ITFP_zb7ifiKT6zsQBUeGavNnCvOm9VsupveBBID5b5_WiBizMy3CISdnlfcONr-HsyfVH6zRuNbn6D_oxIQwoB2gUNdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌دوم فرانسه با گزارش عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99304" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICV09RR6h-X1ZvnsDpOCRxRL_1ojqT-3k4Fk5eqAUpwv3ZqJjsNgHBiGfBNvdrjpGcVaU7py4AXckMPzPFgx6Dvh6RufV5brXaCRxbUsU75rHJ-A5wyAus5BpNkfJv8S2kVmIQqLO_Uu2-VfEz6Nu6_IcIgBvmpdj-yqmCOyYZpIRK4jyEp4_V2NMXXdP_pN3_KIrlT-3o7SH7p1YTNdsGBXjEzLgy96XXNd9_o_1PCYuO_mE5Sba_QK4fOC-GhbNXx_2uICL5r7uY2bD0NX2Fu1vqIyTh-DINTPTlsBf_nmeTAMIPP6l0F1Dx-OOGbVujOejQ3DEvGXyB0dB27vww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار کیلیان امباپه در جام جهانی تاکنون :
20 بازی
20 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99303" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99302">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آرژانتینی خایه کن</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99302" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چه سوپررررر گلی زددددد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99301" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دمبلهههههههههه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99300" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دومممممممم فرانسههههههه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99299" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگگلگلگللا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99298" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3zYBJL4Ywtr9dPsqzeIFgNKaT5JbFeepvTgPYzaWjrG_wH9b54WGkfbQTC3TI3xN2lWh0YCGFfVupWg7vYVwaNpxFIdFN_ku8QvilOQBwgm--SwdSVBKxBnV_z7cVFDCyiVXK_MpTNL-3Z_6PpbUtcAv32eOg6JA3WIWnkERRXSfne6NLXIGa-ifoVoB0XZE9uTNdpnNJv80b1jRkghJN6I7gdinEnSjQkWka14cIWwiMPDUiLcFWJRA4iVnP8jPQJ0MrSbohoSaaw_oFVX6AGxhqciB0jOLDPiOtBpxRRraU0tknAIim7AYPr31JrD9GeLknM1cdx8EG7PUcOSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گل‌اول فرانسه به مراکش توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99297" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1SvG6BCy8EMbVf3PGRu7-CcLO9QMdZ58RNx8hs5ZIDeMPZP23WeRd26Dr5yh2P7zMp7OPDKuRbPsbmNuF4Xk-m30KMsc16iXkiZfa8v6YEGRo78GYZa7uJ0g3_WH_sYLWS8G6hUgxvgSw1K4ly4u7BYdXboIOwa2LjsbhF13UPogs7c23LUGd_5kwkoyWBbWqVuriashJzCo_YDN3YOtTPowqBhGZsKHjttHHAidujbaSxUU5mUoKSbJprCm5xxVszss8YFJQoMChrzM8cd6qU2SxJEPme8EKrBFhdlCEXpHjlmHCPWdvH8NhOrKJTu0NtIqRNDngxKBLjIURBP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره بعد این همه موقعیت و 16 تا شوت گلم دیدیم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99296" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3ab125a3.mp4?token=e1b8XWze5c1GDf_QZ_t93v1ElmQWBR0pwi_fkWi35fefyVo86gmW3ylyU2KQ0nRWYaxjeq0CgFmvTt9TI8nAHKfdAZJCjKfnltyxIOEkub-tFn9an5wszIpkeVk106MFyuX34BANplZfVqPUy_J-xTa89pGg4FwXX5s0sx82zCb5EFvDJoAYC86FbMemgGzTCxuQ6lsk5WhUn6K43o8YP7ujldgv-UnOX2gw0l2iQb_xqJhW2-szvGuJmJzN5dbV-7cYCuCY8hseWDI4fN1r2BgQ5ksxEwMMOyUnpqNMjKWzmVPhAdqnjWn9v8tLu4gKjXjfSfdIFG9KC9j1mnWzCJ3H2vAeC3GFJAg9oYJwwRZhuP0KzGwAjReXu7SDGpWUnjMb60JQZf4VKfImeJOkPk4GmudTQjWwqAtEKzqBZM-Q7Tky63ZOXHhq8qq75Fg8WBr_m-qf2XEk6J8i4fDjVggC4INYjUpAwLDYXPdHIeQd3ywHludeIwf2hI1gURO-HnCGurlo3xIF3pQQE_gXOjg7vaLQX4ERwYXCtBE4jevbiZ177yKCOFXEw7aiU0rAkWdEvrTj_UOmrItXZZiTCSPGVtGTgr-6Uyvu6h51nte4nmtmtxtagd6weetLU5hREdkAZNSuWiNY3kJ2dGa3QfeXwxsxxwkZjSZF2TexHUU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3ab125a3.mp4?token=e1b8XWze5c1GDf_QZ_t93v1ElmQWBR0pwi_fkWi35fefyVo86gmW3ylyU2KQ0nRWYaxjeq0CgFmvTt9TI8nAHKfdAZJCjKfnltyxIOEkub-tFn9an5wszIpkeVk106MFyuX34BANplZfVqPUy_J-xTa89pGg4FwXX5s0sx82zCb5EFvDJoAYC86FbMemgGzTCxuQ6lsk5WhUn6K43o8YP7ujldgv-UnOX2gw0l2iQb_xqJhW2-szvGuJmJzN5dbV-7cYCuCY8hseWDI4fN1r2BgQ5ksxEwMMOyUnpqNMjKWzmVPhAdqnjWn9v8tLu4gKjXjfSfdIFG9KC9j1mnWzCJ3H2vAeC3GFJAg9oYJwwRZhuP0KzGwAjReXu7SDGpWUnjMb60JQZf4VKfImeJOkPk4GmudTQjWwqAtEKzqBZM-Q7Tky63ZOXHhq8qq75Fg8WBr_m-qf2XEk6J8i4fDjVggC4INYjUpAwLDYXPdHIeQd3ywHludeIwf2hI1gURO-HnCGurlo3xIF3pQQE_gXOjg7vaLQX4ERwYXCtBE4jevbiZ177yKCOFXEw7aiU0rAkWdEvrTj_UOmrItXZZiTCSPGVtGTgr-6Uyvu6h51nte4nmtmtxtagd6weetLU5hREdkAZNSuWiNY3kJ2dGa3QfeXwxsxxwkZjSZF2TexHUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گل‌اول فرانسه به مراکش توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99295" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گل کاملا صحیحهههههه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99294" target="_blank">📅 00:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امباپههههههههههه
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99293" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بالاخرهههههههه شددددددددد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99292" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرانسههههههههه زددددددد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99291" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99290" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uRWV49TogguBosFTGGt6RWBNGQtK3rfuGMeS8KK2635_rRd7lb30g5PSIWnj_2COGMWu-iAR2_UpgOBI_NzDVeuUlhrydGZas1vUXPTBehfi0-rvsgkdyvHPVrfWSJwawjqtQNZP_y0BpjjcT3Kql2SnL1TpeBqMPc9jHA4BlmgMgLQIXMSK1Sz0681E3sdFuKztRRzGm_muDNxgu95Opd8Gw5LE5yhjoViegsTQUxgdg7S52apPeM7dCEAiwM7afLDkBSQQsZ5yChHlM3McgDBmM3z4bhD_Q17fA2iVTN4hzCxitYOaEIc7EBYYbbQN3bQ3NHRAfU-N1QK1LXUP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99289" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرانسه چییییووووو ریددددددد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99288" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99287" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بونووووو چی گرفتنتتتت</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99286" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99285">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99285" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آغاز نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99284" target="_blank">📅 00:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99283">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vARQToXwRHLZzjmZawRFQSclfgQdWfUji299q8OFWcBt1gklM5m8L3HaPODbnBFv4gGtiZNIM7lhH2dEnHwUj-NSkl3r8_y5JclZP7AqmK4YTPnVQeFeMYkskLpfCkH4z8tKlSoI4aBpZWxE2I1ztzBxlEZNU0yy6WuHptW4USTObqM9Qp_kC7CE7Ideuq4_M3Or2Ffrg2CyJf4GpTaVfaERDGDYEtc5Akb05T_RGQZ8ntfZbo946-0O6mkxAyALFklBvPK4jNnYlg81v0DMfd5oeoH6EniCzES6LzZ1L4BckW5PWldGRrVqtyoDAbBKQsJVryiupbEVobnUKDXxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✔️
حمایت هالند از اعتراض امباپه
5 دقیقه وقفه برای زدن یک ضربه پنالتی خیلی زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99283" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99282">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">😟
🚨
🚨
🚨
#فوووووری
؛ در پی تیراندازی در اطراف حرم مشهد، حداقل ۴ نفر کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99282" target="_blank">📅 00:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99281">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN6XBMp7bnJu-rJhrTCtsjKKRBzM1PEucdDhcnrgF-EgrRl-SoRj4RAE3LGnjbjiMeGxDhWPMV8lRDMvO6_C5j5-LbRpEBvh_xL6sxR-1sZZ_UAZrbxEf2eSJLb85HnoI7d3v_dn12GBoo4eOdrTaTrq9hht6O0-C2s6HDXnUOci7NX19LH6Tmt32tKDp0QiHuYU0iyBY82gtq66O6oWuHC7Apmf1EQ7lERpMNBMjTAa25cYjikFuKgRuvBrPjNXD91yWYyPxxycMe0V8l46eVtmaQykdJDXEvfBFo4d0I-Pmhmcd8MkhjK2V3inOx6B2Ic3TxQ3SaQoaf94Q_LmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌هایی که در تاریخ جام جهانی بیشترین تعداد پنالتی را کسب کرده‌اند:
🥇
🇦🇷
آرژانتین — 19 پنالتی
🥈
🇪🇸
اسپانیا — 18
🥈
🇫🇷
فرانسه — 18
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99281" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99280">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
پایان نیمه اول با تساوی بدون گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99280" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99279">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHlMwY2R8ZZ7vtNxFDXRGayOvxI-_UQY8mIAGBV5Hmt4bTD0j8HVfC_XAWasRB2jaBv9RvXy6KmFX3wvxRQoT1IVm4juFUWGL807aw5RpTpp0bwQwgfDib5OVtnF661E6BwsT8Uf4akek02r04iYKwkBZMqyO4_DihSB4fI4Hv8JWjMqAFkrc21-7N6_uilflrn2mHciqAqrrMSZ66HiyeU93DiYav8WObkSFAt_iCKw1PXhPPnKJ8ykKYoqptw1IUcFT9N7Tfq79TOaOmM_mbNy8VJzWdsLQIGqa1unueCgb94BT03CGVWirb-IQ-hLphtUSvMdwwc-Tt9qWAvy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه مراکش مراکش میکردن همین بود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99279" target="_blank">📅 00:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99278">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQXzOTU8sBHv9MMcbL-UGaon3L4tErrHylj_-C8ejZEGjey0CZN8h7THNO5aNLSriXZjkAWZ8DGlb89oQLQAKivJi_XRONvPusPikTa1L7gi9cQuGGDUEfLL4GUI05AXDC9c5N7XhYqTHL887WfR4tSGrngkSgcyJdyosCCyU5YL8zgPx_DrZrEOaHIgZXwZYj1ibpfAxD1keZVZHvubRxahwab3gtdCQ4naLAeofIWGCH95TImNs6sPAo1UvLq2LU57-xTb_IOCptXTyl_eYCtuDN3UcNADHiruNH9CxrOdwQhQ_m6S1hHcwNhlozwteIWCIvNv2BmrZhcuVVtk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم شکیرا تو ورزشگاه
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99278" target="_blank">📅 00:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99277">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG90K4JG8mQ808QeRIjAxElV2yko9fkzvTye2nhi6QDY62nWBYwB6rqD-TncKhr4ZXYG8gD_RqLI9RZXmHPDYfzXA0ZsD8P_O4v2UsXP-aQsDmj0Sp1fBM0XMD0c1jPN6EF4o9AdVjx46l91JU_vj5wIoctcBiPnpmCUv1_uz5_V_LSL9yUdXZvUCQYNvmCRR74EddheGqdFda1tUqzbJ4YoBPZoI92JffPI59PpjoR7BZs4IugVAf9i6ROjCJxwrDDPL8Fey5R-Jy9M06iU5LwGv_OTucZ6NeZwu_TQuzIfn6r7d3y5fdqgPMq0__Vk_I61v5tAIU8ncz7meaZumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم شکیرا تو ورزشگاه
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99277" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99276">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/df5b3f9b34.mp4?token=aDKYke4HxbSTMfSk1mEnfIJR5lv1DKX8zclZI9dJhhoTljAXTvhxEHk1u_36aETpKtj-zmtES9xH1N6A_j5qwghqBwLlrd74xB2Dcy82dDKIjtRKdKy3UDNbJCGCxTP0DHAKe90uOW_C1_pGiITMIy3XV5q2WUIzj1AoySj5HFLXP-l_gT8eU4cQ2KZfXP0cw3vDXlf8MSdOrMzNRxoQ5crO2J8xahlPqd4Io2GVLFwtBffCYkzoIciuFzK1-vtw5NwJUOaW8my3Gx5-kYTmOgEOVLNCibY-LLP3SWirGA9KH5swP0wBUnTf0glvh_-aISt0P-r5Au9Lv1QKnZFcdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/df5b3f9b34.mp4?token=aDKYke4HxbSTMfSk1mEnfIJR5lv1DKX8zclZI9dJhhoTljAXTvhxEHk1u_36aETpKtj-zmtES9xH1N6A_j5qwghqBwLlrd74xB2Dcy82dDKIjtRKdKy3UDNbJCGCxTP0DHAKe90uOW_C1_pGiITMIy3XV5q2WUIzj1AoySj5HFLXP-l_gT8eU4cQ2KZfXP0cw3vDXlf8MSdOrMzNRxoQ5crO2J8xahlPqd4Io2GVLFwtBffCYkzoIciuFzK1-vtw5NwJUOaW8my3Gx5-kYTmOgEOVLNCibY-LLP3SWirGA9KH5swP0wBUnTf0glvh_-aISt0P-r5Au9Lv1QKnZFcdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحنه مهار پنالتی امباپه توسط یاسین‌بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99276" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5NU45L0rNWbFLYGMDBBg9sBgzDtd8kEoEhsF_Vz9CdbWioXqQjkGiqAcoXz4GCtXCbVK10TvqFvSZ6Zh8z7GZXmrktE3ffZWxjpWw1cHT5-iYNe4DicSvo21N1KcV8_hOb6yUzsJ7uNESh9Iu2uYcxLnJuFDTKJpJv5qSawfksaXIY2Yd1m4zgSEX9u56ENJioD7ToCRcctAQ51CMaXJp2ngAmDkjHCFV-L4jgD8NeiEfLdKfzCBCdqLKJ1TKyqiES806A-k7SI_kAMnaE86sgnApV8kr8Aov72lY6nH4CYmJzdLcUdZNEltcWZlP0HQYjhS-mF7evd4w9fxVcoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید که تو بازیای قبلی کیت هر تیمیو پوشیده اون تیم بفنا رفته امشب اینجوری رفته استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99275" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بازم بونووووو</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99274" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99273" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuWr9eEjTKZMuPvLuv2FvIqHv-8GSJTFGWPmtO47Xz7-l9KRQu6Ay9dcoR9KGYarmPqvr538X_VAC8LbqrHRf5XNgAwipJBJeS_6hbQ3ljT7AmDYStcJY9EEggm8sPfQAtKkz6vYoV3FT0V_we1Zf7l2MxBd-NiyY8-rmV4KxFElDXIth060bZ50vF5b5J8t-PWtUHOnF4IMwSgXJxQusM_y3VEyXC0aed4R60h0fa8ysky9pom4XdnN8N4wiXkDtBKFXw1GjcMxWckzfWQMVkEFAiK7SjRofSX6AoIeBGg2kVgjPUkxiRA2JKFX5e_t8F9fJGpGcVHXB4CBSLBguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کصخنده‌هایی میزنه فیروز کریمی تو شبکه جم اسپورت
😂
😂
😂
مجید نامجو مطلق و پرویز برومند هم تو بازیای قبلی کارشناس بودن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99272" target="_blank">📅 00:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آب درنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99271" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99270">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چقد خوبه این بونو واقعا هرچند امباپه هم بد زد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99270" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بونو در نقش گلر مصررررر</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99269" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رییییییید امباپه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99268" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99267">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گررررفت</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99267" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99264">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیکتاتور پشت توپ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99264" target="_blank">📅 23:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99263">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">برای فرانسهههههه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99263" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پنالتیییییی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99262" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99261">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازی دست فرانسس</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99261" target="_blank">📅 23:54 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
