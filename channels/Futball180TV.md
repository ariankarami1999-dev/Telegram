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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 636K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-98287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/Futball180TV/98287" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7kWIz8YqysUp_tfgpKdGZH8_iOd2taTJm885NgdE6Z_y3N6zJ9vYIkQ8lOKIA1wTNBgAyytHspCHEuiILyj8nEmH8VKy1sHX6WOdb433EQCCUHAjgv7IshUE4a7xQg7_t5q-mkSlHkhLWxlmz4F6vbLtBO5QpHU7SS1llrHng-ougD0WN7nw8Rmf3HLRl8qmM9L7BAWli16_J2iUzm4uRiDctPIozQtdhhYL7RYENCEIqdutEo7--i8pOcTu1g7gplFJbto3ByQODeoEBNCwy4unXQsqkXT0WsvEOl-Z8FreVl9rdcBibU0SZeAqoh1O99Ixeb0fQ9uxhhW3VB_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
🇪🇸
گاوی‌قبل از بازی با پرتغال:
برخلاف اخبار و شایعات، بنظرم بازیکنان پرتغال با احترام فراوانی با کریس‌رونالدو برخورد می‌کنند. اینکه می‌گویند رونالدو در رختکن محبوبیت ندارد اصلا درست نیست. همواره واقعیت‌های یک‌تیم در رسانه‌ها بازتاب داده نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/98286" target="_blank">📅 11:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
جادوگر غنایی در بازی با کلمبیا!
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/98285" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GffH_tjK31GGdCRUXpjb9g76eGU0VmzSsUprV2ENK0jkhDVBNwjVWcSm94RsjDFETRmoE_dSwn-8vqViUQ29fRqoxb5Wfot6Xh6jFfX_JLV8zcLBbnB7AAxJ0FqJslLWOhdmzWoa2QQbvMn8skP_u3osWErE_BGt4NoXk2eeZdNv1z1KuhjJUfHjlSTz7OHbbMBxk3ZmDCv0Z2p1eMqKh9li0F0SM1cCHLtIAddVHVMogiysDgx78FmX-vA7ZRsqi8vQ8cMkemwo7KfSQB6tSdoPWL_N4IzLpTRpuIMET08hw-PQDgI569oT9Q_dQXuklYPbdms5vad-3K3QZJHSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
دیدیه‌دشان
:
من خیلی حال میکنم وقتی مردم به امباپه میگن دیکتاتور. دیکتاتور همیشه کلمه منفی نیست و وقتی راجب امباپه اینجوری صحبت میشه، ذوق میکنم و بهش افتخار میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/98284" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=CtTB1kKXxsf7xh_Cj7GQY7m0pUNVgEkIxWINnUKbXaNX4ZUVfjnBFCl7wkc-DEut1NMarLqqJzLQ6uLIX3yMS8Cm80k4JeEONtkg1jqf1ziIpxK_qEjvPdAtpbb1JZKa58aIXahU5eKNCjJgn2hr6Zu2gPPqwWglf3Hx5QmmOpWxKpZnlVuqLyguoHgs3OfOLDZx2C6bjAnlOVEiEDDq8397qWsGhNbgLfkWpU4h7ZoywgVZ1ZTuMdd_qz4ZwP0eiwnWwG3IOwT1_fqss3FZzFb1D5ushZ92375v2xiy-dNFmBPwkl7kcBVIcPPE95peRYWZilMF4HbmIzYtNR35_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=CtTB1kKXxsf7xh_Cj7GQY7m0pUNVgEkIxWINnUKbXaNX4ZUVfjnBFCl7wkc-DEut1NMarLqqJzLQ6uLIX3yMS8Cm80k4JeEONtkg1jqf1ziIpxK_qEjvPdAtpbb1JZKa58aIXahU5eKNCjJgn2hr6Zu2gPPqwWglf3Hx5QmmOpWxKpZnlVuqLyguoHgs3OfOLDZx2C6bjAnlOVEiEDDq8397qWsGhNbgLfkWpU4h7ZoywgVZ1ZTuMdd_qz4ZwP0eiwnWwG3IOwT1_fqss3FZzFb1D5ushZ92375v2xiy-dNFmBPwkl7kcBVIcPPE95peRYWZilMF4HbmIzYtNR35_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: بعضی از بازیا دقیقه ۱۰ تلویزیون رو خاموش میکنم  و در این مرحله از زندگیم تا ساعت ۳ نصف شب بیدار نمیمونم که بازیای بدرد نخور رو ببینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/98283" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfO9wEecFZT1TICqOUb3iezoSCExIhrVOFt7uyt4BOFA6JHjWbfHOBHOYaN43_NnhOHtivN6uZofmQNEbCpxtmPEca7IimuA9ONLVxO2ygqYtu2e0BvaKHkPFE7j9OuPK2YqB9psngMCA0LNGdQ97BDSXn9Jw4LI3EiLrUg_AbJufeibpVtQbs55SSgkL8DS3F4VBp1gJDRpH4YbmQ9eHARjeGmYRgvABI7ZJr6YQzTbnjepoTQR9fUXDIvbZYzC20eSEUypmkMFl5pOw4S-RQpA3c22VxjNa6BXzyILPZsA_zOOImd__g9OAoX4fTWxqMPxjPP9uAvWgE9f-2P4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
📊
گلر کیپ‌ورد در جام‌جهانی از حیث دریبل موفق از رونالدو کاپیتان پرتغال پیش است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98282" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
خاطره مهرداد صدیقیان از تماشای بازی لیورپول و چلسی در استادیوم استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98281" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=aTnNDf6xwrJHDIIQlaiOYtTuFKuEC-3nsDdtunZNKDd0ILigxRRPy4lHSUsBRfvmoYDCDYSQw2xX8xnxYmW_DPAPeMcZEGza8s8pW8lb_Bf1PwmU_zvZ866abKskpIP4Gzxnu0X-g89rFwFV7exU6rhPdhMCbRH9NYnvt8o9I4Se8ramV3kUS4OLl4uW8eke-T1W64RN2nfWBa62JxfrFZKFUtOnXvRs5l1x-2b5N28jZ4W6jbGSfmMkDnFqCvXYcjZI8MIXWhTXR3NJYaojZA3-0iCAPeU3cWR4F25FlClyzekw32wUTeX7uH_ilkRuKloeZz6aIXc308mOC7YDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=aTnNDf6xwrJHDIIQlaiOYtTuFKuEC-3nsDdtunZNKDd0ILigxRRPy4lHSUsBRfvmoYDCDYSQw2xX8xnxYmW_DPAPeMcZEGza8s8pW8lb_Bf1PwmU_zvZ866abKskpIP4Gzxnu0X-g89rFwFV7exU6rhPdhMCbRH9NYnvt8o9I4Se8ramV3kUS4OLl4uW8eke-T1W64RN2nfWBa62JxfrFZKFUtOnXvRs5l1x-2b5N28jZ4W6jbGSfmMkDnFqCvXYcjZI8MIXWhTXR3NJYaojZA3-0iCAPeU3cWR4F25FlClyzekw32wUTeX7uH_ilkRuKloeZz6aIXc308mOC7YDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گارد ملی مکزیک درحال تامین امنیت هتل محل استقرار بازیکنان انگلیس پیش از بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98280" target="_blank">📅 10:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522d669236.mp4?token=aLgZkvza-zmsjdOdi1ZXB0wkLDKa0plazI71F5tMC7B4xusJG_u-6tdbANj-4iGQzA0bxaGX1wwF2EMs7b6GTxFs-0YSQaM7F8DJi-1ppigcJhku0G4SKyN-wMFODN4jtVdLChuOEFyfHcdlkhDlDZzyJVwzMQfgEUF6XJYs3UnMXto-FWiL32P-k6UfWkB_iszj3xh8jw38_iFXbF2kYtL_peHNzHFxC-aaOZmeCzznd41VoWvshS7s2o2SIi_oMxsI8AltuHD1tD5C_aExILzxf28_sIxfavTai4hAi4wBxlXhITQnBg8wazHB3X25lCHASnBo526fV5XIKS44LbgOH2S73rCIa8W9v_fHuIdhu8O4G8EdG3T78LJcELPNXpuD0zmqgNlNuExFw9g1gqtgeRjK2ous0aEF19MICnGfsxVYvFZJfuf-wCO0dn5RL06uIQh3NzuDuADo5RweE10JMGL9NXlpddiUE6Eys2U1YG4A3hdx7LKuFghLrROQsUlNc03Qi0_8CAiZJX20DlZlVVmDzHwDPk09bFp2WJV5W3mq8ENVjapwJe7wQgPLYW0xhG_jd2N_EomzkGanswlowiWykyT6Zn5C8bYKRabELBRO964_T3pHfkQemDnlJc2yZPQ4M6xTQqPbjfc1BpxLZ97o6OPXjv1rV1XqdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522d669236.mp4?token=aLgZkvza-zmsjdOdi1ZXB0wkLDKa0plazI71F5tMC7B4xusJG_u-6tdbANj-4iGQzA0bxaGX1wwF2EMs7b6GTxFs-0YSQaM7F8DJi-1ppigcJhku0G4SKyN-wMFODN4jtVdLChuOEFyfHcdlkhDlDZzyJVwzMQfgEUF6XJYs3UnMXto-FWiL32P-k6UfWkB_iszj3xh8jw38_iFXbF2kYtL_peHNzHFxC-aaOZmeCzznd41VoWvshS7s2o2SIi_oMxsI8AltuHD1tD5C_aExILzxf28_sIxfavTai4hAi4wBxlXhITQnBg8wazHB3X25lCHASnBo526fV5XIKS44LbgOH2S73rCIa8W9v_fHuIdhu8O4G8EdG3T78LJcELPNXpuD0zmqgNlNuExFw9g1gqtgeRjK2ous0aEF19MICnGfsxVYvFZJfuf-wCO0dn5RL06uIQh3NzuDuADo5RweE10JMGL9NXlpddiUE6Eys2U1YG4A3hdx7LKuFghLrROQsUlNc03Qi0_8CAiZJX20DlZlVVmDzHwDPk09bFp2WJV5W3mq8ENVjapwJe7wQgPLYW0xhG_jd2N_EomzkGanswlowiWykyT6Zn5C8bYKRabELBRO964_T3pHfkQemDnlJc2yZPQ4M6xTQqPbjfc1BpxLZ97o6OPXjv1rV1XqdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
غیرضروری‌ترین بحث تاریخ:
خداداد: گزارشتو بکن
خیابانی: توام فوتبالتو بازی کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98279" target="_blank">📅 09:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=Zd7R7X8KBqYYnSdHYi0VpWvbK2W7p-eQtR_7ou--o4Pcz4Jo23zgxJuSbeBWZabROPIGJHFMS-NwB2HxJxL00rf0F7-xkJvpJGddzYb87A562Fefm4DfPObhaOu0V7C28Qxu0Zf3jpzJlGpymDMvfkjXaJwfggAa_AYF81vACaRi6pUfzzZPl1UzAZnvtNCRUklV-QxdKfq0RrDoV6M03_UTFAu11szgMVy0QesMj8Tk6UJ6ilm6UXFKU0lhHvclG8Zkjrstzmfa_73jFDl3RmmpXIaqdsBY0SB-VFmU3kQLKmgp6l9blKmvBY7OcW5FpHQdnO9b1wpKkjXdn_6I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=Zd7R7X8KBqYYnSdHYi0VpWvbK2W7p-eQtR_7ou--o4Pcz4Jo23zgxJuSbeBWZabROPIGJHFMS-NwB2HxJxL00rf0F7-xkJvpJGddzYb87A562Fefm4DfPObhaOu0V7C28Qxu0Zf3jpzJlGpymDMvfkjXaJwfggAa_AYF81vACaRi6pUfzzZPl1UzAZnvtNCRUklV-QxdKfq0RrDoV6M03_UTFAu11szgMVy0QesMj8Tk6UJ6ilm6UXFKU0lhHvclG8Zkjrstzmfa_73jFDl3RmmpXIaqdsBY0SB-VFmU3kQLKmgp6l9blKmvBY7OcW5FpHQdnO9b1wpKkjXdn_6I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه فوق جنجالی از بی‌توجهی کیلیان امباپه به گلر پاراگوئه در پایان بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98278" target="_blank">📅 09:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98277" target="_blank">📅 09:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897a264b10.mp4?token=rHLLvOitQFlsqqlGcnhzHmQCEtZS8jlIFMAeA3u8LisWhBzLSYuLNCSCzp6EhZfX3D1TtMmAT49AIh2JZYZBY1CjG5oYCUyGNS1vb_BHhOO_P6mJpiFrDmZeZ9QQns-BnefsaC4fw7zBqMynpKl8CNgWzPNMLIj8EP2uR8V5mvoZb0isU46hoUQbrjXwKYyKViOIvPw4pyL7vDDoE7axwetQm8O3vQiqnNZ4522LBLVJEMvmzldQyD94ySBePq5JkobEHEmoUAFR-zXsmaBUmB3ueZIwrE4GfZp9IEc-2pFcjOlNyyDbAI2-EBm2_SansVNQlYXJAYlr73K942J9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897a264b10.mp4?token=rHLLvOitQFlsqqlGcnhzHmQCEtZS8jlIFMAeA3u8LisWhBzLSYuLNCSCzp6EhZfX3D1TtMmAT49AIh2JZYZBY1CjG5oYCUyGNS1vb_BHhOO_P6mJpiFrDmZeZ9QQns-BnefsaC4fw7zBqMynpKl8CNgWzPNMLIj8EP2uR8V5mvoZb0isU46hoUQbrjXwKYyKViOIvPw4pyL7vDDoE7axwetQm8O3vQiqnNZ4522LBLVJEMvmzldQyD94ySBePq5JkobEHEmoUAFR-zXsmaBUmB3ueZIwrE4GfZp9IEc-2pFcjOlNyyDbAI2-EBm2_SansVNQlYXJAYlr73K942J9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
در پایانِ مسابقه، امباپه بسیار شاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98276" target="_blank">📅 09:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRCDxs5jjiXtko0q9SXbsdq31O6kOKQwgXq4DmtptIxh_5ZedbuARIhGJFWlRhV0haSo-ojQ5YcQe0CVqOVmSal-56nUdSEGCLJ_19za7S7U-ho5yW4wlAy_XYt8McGw1GyhWJRyPUN92X6lKr98sms8OEZ-kfusLxnMS6FFh5pYg83HCnlMF2TkKI7wSEZqsYhM5WmVxh9Di-y2xhvPZHudF9inNNiruksLWkZsoiOQ9Edkc4qoBprA_HWQkey04IreomPRm60moi0fDDVBvpFCBJzMkuo8Lv5lqivCu0ga_morlVSTVLsuZPL91IyYofgXYd4rCkbe8SjNyfiqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAFQPryxVkkaV9tTigZeBHDOfqUGuNqnZj0lHDdPGxN8USorCSgyyJCiQhz9YoksxmgRzdRcF6XqcF0mUQZpt7L7k9aTCoUYBtgKW2WtNOH8h6NgbwQyJW5iFXbHTNw94yetreKa_xtwG8eWvo3w-ePFnsV0p2gUNkaLa8QqBmivPeWtmP61WVjif2T7j5VoovF7W71v8HwR_TQpSEt9Oeky-cannno4q7F6KHeU9ZMsMLYFGlRZvdS-Pqi1gLiW59nQKYqh_TbG2VU2e7Z_kjEA5wrbRgKmUREudGw7moRKcs9fVQymvm7zgvK4Y-ATYApBQNw6ha2ws6tTVbi55g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98273" target="_blank">📅 05:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98272" target="_blank">📅 04:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efwdKA5DsSxMOFPuA3uA3_zyp_Hi9dRQpuXnVABTWZgRbQcK_nQr3lk4glQcRfAgYocrxQ1gtWQvMeC6MR5BZEuyqDsy0BDVkqm_GUnaRxe0gKt6L4jcCxlwsYx3zCJO-cHIcIUCqwQaVCoELnbMhfJHBgt_Q8va6wMRbUTkb-C8212KHwnRNk-ReqaeZuUKx8oeqSLDzJMAdwIzCPYSeXYTi9BidLosBY5Ur2BwdZeCqUL2WlOU-w8RSakJSXkt4L3r3d_h4K0KVjh5gDaB_i9udhH9iIX7jPazkYkzBs1X-dd_NOZP1ptw2XYHdGVspIUGcqfbuF-SO-4jimdteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrP0KP8bI5XfS_CyCMe5nK-sq1yYZCdg34bSqlaJpKAuJzTfdbLGPmbyIoHDX4DVZ6Iy41G_Bh_dtKKXUa174wCJtGHXLxHqj6Abvx2FnAv5R-J5SDFqkBcrrUtOiy3T1a818fm5fLnNgbSG9sMGuklj-Hjc5vmJEeUGjXFsUa5e15J0G1zJhMRthCg7e87BgEWwsJh-Km6zhvVwQzmSGT61yiJkA4QXp4SOtnZQwk6KpnKjPZy1t1kWorzgPumRRmcA7kCO2VHZZgk_HdQu2XCYAPr9NRAX67x_k2afRgpXdFKwdciYc_R3xuYdcD3Df-gmhlsYjRsEQ0cfzRzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wbEydqJJ3J3ChwWlMAA8o5H8lrwE5lCCwOAgWETRKmIr23tgmGReVaFltGDuDTZkZ-AOIXFtARAnhIJ6TJZuiUMIdAQW9pJoPprUnFzEXYNerx9SDiWRJBoUMeWjMu6wx6iYxhVpIwJshi-u4HbKhgTnhL_m6unMduFHQFTdSGhlqURUtHrup6LGWOsHctjFTC-lzLQmRTPoZT_MP_ALvc3wXI1598Qs2gC5xRQ8lIGMObUVqS7mb-9Ti5NJGpHiPC8KoBCmJ56obbuX21O-QZUIZw4FSj-Acl9rpMouL4v2LmrTHe1Bes4PpIqG8uDOgzaBN3C2MjyYhp5usgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUQgbwUbB6_83TDEUElC3k450HHRppv56eWYxi6yWz0VaEu0pI0Hd8Smvh03jcGhMkNwgIipwlqUwGSKb97pQooakAn-tKFl_T-gAOwBco_IKhXCJTQe5oAylbnB3PlPTD1BQ4YruhfmIOo-hBt-syuTxXyKQruDaqYH9GkCN2OTXrCn-Vh0rRY9k5-0SQlBIJ2amk1RDJgVP4LFLZ4pABr__RLpyoI0Qnwgu-mKpPoya-VisFJrdwntxCHGRn3y5UjpT1OKxbiW_APMjfDsCENTpjBFOys0FxmaFJ7lqbI6Pcukw0CAd9FSJqNihPcsFldBwDxvfPPY26Pn6kaubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIA_X5Pb3Hll4BPS9yBquyeKixhZXZkgGjxJ7qd-HtwbPwqPpuhiocZX9xMsyQgPdJ83bPbBRJMonvFLpDxGzNCfarTPFKVJtaugdvQF_t-CfcNeef3d_cFvzn5UlDHJhUFJIvfPAymrhCELZiz-Q_qfSApF094CJu-mihG5LQzAS3GpgQxaHNzshTKcFPDITH_yvueHwn-rL9tAqwuoh1ZhkNFM0t1ZmlGp7jTgqFkniDRrTiOYPJJEM4XchSnic69st_1nolUynMvnC_UQfswnAuXDPswk1oNbHsSOkS2nSLBLUYHqSLX2z9k4RdbjG5Uf5TC6Bb3DtDasUYoiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2KLyuThRYnNqoUwjenJBOclYzA3NAlfkpyO0BemSegRDgNazJhEkhiVUjLjKsuhkUEG4I_rCbY7gwGO68jF5T7-0VHouelgjgEjP8NbEv_zw9wDXq76_bCNKbenYoC9OT8LylLNd2Tw6zwXadC1lFtD697WbplPg5wH6G4vUU7N1GHaSzYUhErb4krBGwyGcOpAS22kEoZWxZa2vXMyt39zKUqJ5T-Y1VfhWyxfIbdT1b4ekkjwLv2KT8iEcFYK2nMKxH0O3SfiyFONsmjpS9Yi9RR4N8gUOU7NJHlBLCKuMau6V-lGbG3ESBL8cHaPjvMBIp08c_9vMwaqOkj2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBiKEu8PHllL7zOPfpRWVnzuhuhI-m5_0uTqNxckwfaiuICBjDxDE7c7A0SC0o22VtgV5HSL_QuMXtqlZtl5aGtp2UGWOF2aUr6vzR-M01Cvund3_0gUYw_by-FXh_6iozBjZfe6_IcxxUMOZcwX6OFAEpOFgeLNecFvxEooA4BfG-ZslqO1flGAt4GKKESVlKpcLRFTEjUOmM7PtmOG01q-_eMZVRCVAifhiv0eHEHiZCqV-i6RjYJjESkWVhry4fb_FLZeXkqRTfU2392mCfZSxfrHS4AsRwkYvXTgj71CEhkTqA_l8jJEczY2e82Iqham_shnundZKVmA6_E83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxTLRXRVArKWiN0mtN2XsDrRmqRvIadihgDyiumINFVQInUZwLlrDqouzUgMBkeODVx2PWeV75f1Nn8_0zaUvs4tEFh-tAu-Uuy8xaoQfShCQetM2K0c2Wy8ii5PVClnf4qpEK6AbP8Eo4GVSTh1JqOv9q_XfxBecJUXrcfDp77XiUQRFKtIzrjdetjAwJOsg4VwcnzwoDp0meX2maOJGigl-BSI734wcvNbNEcDWHSuFGEjQ3L2ya_330qTSnbKJXMuHaCJXVTsy0v-leqMqGSg5hc2K8Vs1qlnlu5D1q8JPxTVvRMRpJ2jwPkEEN5V3SnGE5C_VLs71gMa_mhTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDATdFfoK4bUHhB1CMnwXK4NCmphtiP8VNZcnuLuMjcpuXs3eNi8PV4O3FwdcIrSbZe2VeE4RPRs42H0smVxYdGjKh3VBaMic-vhprGGxKfwlucVe-k0Iktj5hyN2akULUId8mUCgZfZHnKuRrbTyrH49EDlRnjyiPt3nYh70QuVsOMDZCTj5H0Z2Yi0x518MY8j7F6Lq-yfCNaolKMDYJuXxkq0kPqTCG6Cq2KPh_WiQcktvd11VOambA_kVQiBdYOzx2RQKwNMDsHWgp5pLqbSfe1QuLX1rgBCQbBgc4ds44I7asBbsdTtT3OcRH150ZOYOQhrG5U7V0PgEUmTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP2PzxJE6NY42U1ocHU8T1bjS8eBc96OdyZgVwSVsM5_MjYcKlVl-gGFkdy-iZuYUciXtx6onojYcy7FR5BR_XTjN-6EkRcIkr2zPXSgZp2H1Jxm4xgQVNK79RKQTRLY-YSVxmdj-LPP1f6AICvhcGZDQaWO559-y6ZPYCDwQt86E4fyqLFopTqTCUmWdaz-ad8U1nlkptDLTs5XiS0e02kbvg7NqZURJPfE1C6Kf5wgpsUu95_tx39DWTYHmBQFc6m98G1xZirHXfUF8lIhl_eRh60XTAUuBxkXIc5BeRhOCIT4RvCYSxv-j2E_E9fCKhC6uTc61nNqtea8soGKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX5D2eNDu3JUsshuhQ6qG2S0Hm0w4XXYICebi9CQLYgtCZBn32q-_try4yKloIhBg_hZzoFU6JD_dLips-UOXPIsLUUyLqNbliMW5-fKOnXpkLTz_Zj8kUso8NJ8dQPvkUC4zerGB7sIVR36syjegcDnzBPbHoMCmkNbFc7bdXH91FQPd-OWrrp8d--ZNMrcYtSVTCXWulbZt3WAURtHc5d_9cBNxrg3cmQ990h1drtTJQ_3hQH9ADP42bwSwznS-SYA4YFGCW8IJakqDJ5UE0Klm0Ej4ckVdeFrer30b8HB-VWKFOu9ehNwSLPjbhp4I8A4J_VHQfPjN9TRG72BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcQxZ0p4L3rW8nCSnRCwBoJ0gz-cuR3WnRhgTsOu3WdzqRGO0g2r8dERoBRBta_cZpA_4Tc-Y_rfI56lBDivj6J1UujnkndH7ZyUCimR9pg-abOidzhKwzYThRUHAbEDSnvnHoGofRtsnOkWTYObDD53XMBfeuSHITCsVVadRqfkGbsxeyFTKTZls2U2GIp3X_mcJojM354RZxsCELqCPL4Nzf58gWhg1TdHa6lGcx2VWHWQzb663_gR_KqomTVoJ_U_qvcIHjubhYKv5alKe-uh6C1ZI9ZkcRFifsxDvN_de3fYdbSgREeDYS4GEl--3TfgtiZWEnf4ADedxk0iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwnS_yr0tTWQwrZWn4F7ZpooAqZMgHjlf1HMULYoAAAlLPTYzHoNlN6kO4C6huaeKUYdnSzMndK_A8fewmv9YXz3ODr7u_GqaXDpd4POkQPzTAp6mt6Rp6eTqta-rO32H1YvFcrjCjaYl-bBxj76SUJIEm48csBQQwSSVaYZ0wXP7lnDnlsF7AbAMe5DvNSqzCL6OPoPF_cL1cXUnDYrQaeckWD60rqRqaClplvcFra8CkY3qwJilaJmCXctr1bxj-4qaZGlmqTBN6Xi0kjC9mO2uh9jBYTVf7tJGIqoIVcqJ4tw0Jbue6NowSUKw8T0KeCIig_JCPfyTAGsf7xv3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKg6lEoMEXiXjd2rp_oliuFt8PyoMXCD6yA_Km3GExPnNU5HntOtbhNIIsFBeyPPLPhvadX5HAGRsEq1zTBVgodc_3kbTR346D5B5oadeDsS6In3cAoUtAfeF2DlmIUR2n_m-j9T1JDVedG1AG6Poso391yo_ieobtd3kA8vXdw4Z01fE0TcEit-mcqZeeaFuXdDjSq3NIXJWuYWboJtJsXCd2vCsWdvLLrYAREEHujOpIKbSbNPZAVNEcwk84A-_4z_yZbxbbgLXoRxqEfbmFsCe3u1SAb8GhIv5U2iKtEx_EbKbx-WyjdG6XUj3-VnToAbIoQKdRELOKnjItRTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFKfZmp3U50RXITh7KP46uourlmoe68kL9dspzgUswiJoy7FI1LiEwXk3kBHAqk116TWMkiCay0JOJWehuUdgc6aEi1sOtZzBSgBQnfrKGjIHelL8VN_yrAJNgqxJBp81L6Svma8aWsxWwasAm6xcY0DvzvMvr2Q4iQOC1LFrS3GmrbVGreUf2-VKdxdqQ3b8qAX1XlEU_2REsLl1CgDjgQgZj5W7sX07mM2RZ3PPH4eMr8PGEaGyyB17-ewe5IoZOgmag04oMY75FXlLcc8BYeO16FQnzfpKbJQgQMdZWPYqNNAPrRZhMMUURFOW91_w2KFOhBgEhJybJDrd0711w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_O9lBFcc-pUrH7035w92qiEZtKSl_MK10EgM1PccnFpbmzG08iQxlFY92YIG7c7fj9N9mU-AjzD8eSVuu1cTv_2Od4wXB9a8JJIUiPEUsmFQZ-jW0wAzgwm7Cs0FbTpd8YFt0bX5hdIe7lZnIPNNgtDNax8g-bpssyF7E9rJg20NQ5owcTStMZdyFIeqQtifoaRGwOYr7NPRY8zuJoJnRSKny4VY1UIKmasV1gf_O5heFK8qWlyRtLV5kpxiwZkDyH2RF4Q3qzuwa5J2vzhuwRBqp5d2dxjb4amiOssiQ_cK1wZpJKFi9HvX7lxO9nX4vmGF2QlJXhVbJKWEGF0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFbDDx2vKT2NfF51Ddul0fCH7SPyia356kBP-t743TP4e8Lp04RzbphbXpGkE0v6jtg4jZmIpo7K2RvFm3pUNGcV2H5Su3WaB4SJCYmrgWYTW2pVygQ-LffHssN2SIyphKBSNB5mo4k8WaCLx69-H5SVu03toRnjXh7F561y2MfGrkBnK7F8i5zU5su9FhigCT7BkyTixAGUPkVn4ijj__6JavJ8u1nDFrFW7JpXoqTFB0Cy_5mOMzJmmD3hXsAWc5uWpMmPatPh2Bm-dZUKzilUO23H1PyLKgoKL8lF3HJCbzt0gD-AyWjO7uIqvnMLuiUHIgC8T5B2pitAsgn1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJpANK-LJclw1xliaGxDotT1k6JJGChDBYSU_p5kDiRjCYK7UAbsQRFj3lEUMNVityZ8z5CLpecagfAl8nWbrs-jplF3icy82-LynLby9kPpGvgmC8hRQiC8s6XfwRIPCZI7WAMjzYJ3cwLsC-855hXEL7n_n8UJlkoAE02frSn9F1H25I9PUKL3gvSnv9SQY9uYh-VyqigsnvQZE3PKLp_WDm0EXAcobtvd1rScm44uYSIumedg6eBXBP9PJ1juJyzASc3MBKiKgWAIvXFNUyYqrPtxBpRf3IaKV5SPAsU35BMoCl7UIbBb2AgfdU7LrDTzJFAIm2VeXSn3hZ6BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkX1Ug81x9d7PciDJ6BTNu_PuSvUZ3cC_Tr7yS_1e73JVOW4Wl3a0WjyNiEGhQp_e513MowkN2LeuvuqZbPZh6zX5UuFSyeBfIKWSCal75PgOarRCX69XiUD12L2Lsj0HeEy3ymeUHgvLm0ER7a_06oTJXB5Oe4pKXyXM1etkNd5WCAIdDH6JeSeXrgJF4Ue1E7F4bnzcN4GOsVtY_nLUb7Llib4i3wNvyubeE7QUkAuvg28m6_dtc51IaW25ZtP8JljIT_oDh_KVzjl2P3I62xR9ZTeGHhpkUyKgeyWNsvM3QTFealLkwXaQ0Jx3B6vFA-QXNEYd55d3GJfNbcylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YaE6mqdRcKdbre8wdidYib8SR_BrHIO492312UIp3TVU9Xb_C4_0vq_34JVUoNi6i0C3XiFuxwmuze_TZ-EEC5c89ZQS0GL9DP8lFFiqnBH3WiURKNFML0cWnjVOM7MpS22laGSmn-R6zZ1uCd-8REJqxTQGL-Cox8qNnS6XhzQR2bBeqcr2zItTEXg_ycdf36hYMQ-VO7jE6dpgGaKaLgi3LTa6zLpMIzXJ69kkV8TE_53zfOWrjAXegdKL9huHjfku899ze6r1D0XwJZ-VP468XGkj75cDn6kHJv_TPQjJlJuZc2kLN0OxkUtqRSS-pWIdp2pAsbVYYDRCTUOhsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auhXF4FkNPemVB10LZl3UH4rdsoZFFxX-cNtza2vq-VaHiC1lbS338qj5kHb_HOZctrXQDVAuQrPqA9xLkUBc-oBbTT9mcdkMIalZwVojYYerhokKSMAz5__YCJqgZ-jMBqkIWVu66OknI5Ke8Qro0e7N3ZhSZkQv9CmIFh_Nt-ZJRDwDLq_PX2UYoN4au2LAPb1tn2__Wslt5na2wf8u4REp88R4L0bvST5jEncqV3nj1PTqKM2MSp_B-cruAgKbOncnTFee8itquTfva4wvm95eFH2FODmChsCZOb4D1-OTONwLAzXVDqdVuXAWcKlyrzOv4-lzTlztCyqOZaiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBxZSg1gsSe7A62v4__tpWjeaRWGoYMgTA13wcuRGd8H4MoZRIM9qkA0hfrIS_b5JTMD4jCG5VPzy2jDOurOV_76lb4keYmcYb5SfbAJdOmDihTv4pBEBcBF3FNlXJsovvk2bz-wAN0Pe5iKN13vvhFoSZlPdgKxvtLPolwL-vrZo7sPYfAM7z8FBgVScXPuAxySVogiZmj1ESH8U0Wv462Geu-s-TVci1d8l-wgaMJbMLgh1LBP4kg4SodM8X40jNkBCjG9GR8yrGD9gRrlG07ZZQr5QiFMUn7IGrOKdLO7YD5lAnK8ltChbw0lDuDKGf2x6wIymYirZmPI-Fw4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbfzw4yk-h9SVyLfaOX759i8Zg6SPz2-frZq3AkP7TJ_xxInDszHnT7PsvqY77xySZ0FXrCq0RmXi7sWu3AYL-5sxQTDACiotPYeaEg3PgE4GINJ9TFfwN8SdI55RMNd9nb0PHprSJvdI8ON6qf5buE1p1ZfYOC1O9mQYTlycnViIZO700VNucE1c-Y6OBDg43HEww6k8Njs4EltiHIF98POAGrNEFwKXeD3RDOh0gwKUwET4nHsCw0-Gag3Y681uzpsNPPGB8rkgi21kYC22VNHNEehB98mLvFDioTN9gQHvPKsyGAwHTEUICbF65_oGbH2BUB4uy7Q7XSONvaDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdh6Ly-BxH3Ggo6m21FR7C7LrN_ECNQsO1l_QkYrDNBi_3mrFOBiIRczP0-KTENUHaVGIa2qOqGrKXcpFzGpXyLc0W6uw0HSkS2KTg4I0-BcINtvie9x0EWbmp0c3vvG2nVdNEJx81ha1Xmn1wzc0S22Lc7qZZjCFpHfpuLiramaNuhaeCPAYoh3y0BgSyCkolcxtL06_e2fRggs1GB414N8gbQSjlK5qDiPvRxqghh6cxJVnhLFPBr1agMqO1dSlM38q0pH8HphVTg_XhO-L1a0H-dU-7yjasa2w9TNpA6h_w3gbumhncPCbsJjMDT6U2UnmcdgMvFUxxjYdkiVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MoX9n6Umlzc5lgrh5cOc-cVAB6ZENU-YmgV5XXvrH4SMnpLykP6D0qzZcJ03EMqCOomkEnep1Y1-OIEqzhMQeM61veSdJdjtZlTcbnod-nUgYEck_vMFTySzVNGl_cFgVCnW2faxj71364c-3CmTpZV7JQOwNs3C4LTqMC1cpf1xIbvIDt-wSe_9y_dcyl45fgEvfNh_58C0UMI808QbWNntWzVJTPuVG12L3mCurQ56nnpMUIkEjhux6YleupyyCApfngECIgWXQGafAphUwso19wq33lNcBrjTOStEP0zFhGZ2cTknchRoE1MzJ91Haz0zf-9Q5kChB6-vVK6Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-sNnHYNQOe7IgeedHFfY9dVvR4WX55yyjb-UwvmdLAGxUykjHLPlZvT1xdmykmuYoDMGJi0VYULSwZBbL4hxeE7uG3rp0uGGhJL_dR1YYJzP2H5Kly2HDWqDmGJWlHIUH62ZTZufCe-va8Pr8WD89qbWd3uPb-DXEwndxjUNcmsuOqK3XMX35L-NTHuyLU6eoVFxBiaTURC88QYtFUqygftOlPBv4dQ0CZuH24G_J2IZvdsmt8-_nMXlyq1YSJ-RkhwBnkbG7bBHeSE3AyBFKpGiZ-B6PWHAkPm6up8yXobWjc8IUel48ilSZBNKCppSncpiaPBc4xHLr5V_NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0fENN8bzoFSkuUKRWMFYpjrokZDu_hKKsmyxzWTH2GlpUIoUDOSVFfj1eVy3r3DqDcr8f_-NDrQKfcEh6WX9tPWsspWJH10Dc2XtzfnMXDn1jFrOBj67rj4Pxp-kbKnRngo2xZgQC1uN8Ao_ED-S4Iarp4hHxtCrlndjqjnQptiQzoENYJOj9InUSnd3q-NMjVw5lVgK7VQjWCVZ3ovVl1OoLoCUpuuGLPCKX5B5O1SVhvQu-pgD22ENa77Fh9KLRSSa0hCSGd9SL1u9p_JW97DRAGD1coHHZMUq2Cxgi-Rjqwq7JSYebIM9EJcvkWvx4s7XJl5myalmTta8VzEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QydzFA6HFTwJ5qjhHwEApYucKRpMCONDYlH_uV67i_-HOSvhOzUFGN2xzgpRVjrFbQKUG3yOvmba5qzso4zBrSLwY1MwYiXDxSVyFgdJTd1uDnFPAKE9e0D7tlceKmc6lSASwOKkcI7W36whPgIvfDdx954LHV8_Gp_H2hgrgNipq5zHb2dDlKDNaIalAjAuTo8yCR7ZzL0Hsxdfdg5fARaNnSQQOTi-4ww68ZtvhUeTePl0qiNrPqcKKITlthG_pqb3Rdrr9nm2zL_iWooAW8-CWW1g0Mu3w1z5ijSsJOzBXsyM68GNMzPDM-GYq-d5zf7-BwDgZY55j7USZV_y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kszl6Umw6ria4_EyrRUcl1KmYPGQ2jVsCTwuwKTUDHBbvv4-J5z789MLtwFWgMexvQqQfd0Oo5u63UAqv4sh-81mE0r7KGCeJM0yXEwk6wYWIjDdYFLnb8zxatRkTnnnmS0-xjo4XvYx1TaZUxTui37kfhrIPKC2gRxH4otRbRh5g2jIUOcfZSuZC_Pjnl9cQyX6moERuFSfuUyiQJbpOGHibC6DAz8srHU7DXzXBd8kEI7qzuudlx0PKcJ8hueDVjbu1ngxhannQ4UBbKBGoikKFWZrCuJ3SaAdDnCL2JR_4mjSX9Kewwn0ZtGA33lreXDWKaSE_EcUc6Z7jc-m8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qirishs0wukp0yWKz6G1opFDT79Ba1Mmp1ZOoRZB-NYjmFRMzFMeJ6Xk2GAj6gA_Damg8x1_oyaPmDm16siLBWU8ro3crS5GWzpLPZpLAOXHFl1vn0czDTTbnpKPW-eENhtNuja5yxRfbaHGxUWnSrCVvyafZQYSKkAAzoACklwT1gVfnqn7assBxk88YT4uljc9Y1C39fRz0MRAlXsgjYJojqdMkBF1tbALKQogg-to-2heh9yMr5xFewNO-o1ZfQoBJCPSUqVTR3bodjOxY4EYIZEtCiQ_mi2zPf1lkcCMVR8uNHFK7S3M6hzHFeUOT6W40jp9hKYPkUl3DtblwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFhd6AW-JrZ2kgwqrwOEZhjADT7tTYftsRjwaHVm82F1I42k4qIkMhjmIjp1SxVu3LVSHcbtj1H0cfM6dx4AL1AsZaKRYRuYbVmERAmwVBP_QpG6AN-Zad8QME8aUmwnF05wKMv_LTCujdljEw_mLDGE9xb0skIyHsxuSocB4MBUW2L0gcu5GUTawkOP_h_GnBGaHsg7PvLbyLOHB2cYm8nOJtJFIHdo0SF6u4HypIJ3GzaiO5fCvp9GAVoAKxqiOJZGN5v99pBj1WZZ0kGG0vHiBM8UiaqQspfmmPqePnTfThXAIptvwv1wpmFKMtChoissPQPEBzEf0XIcuvTZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm91RdOavZgfctHFr7okTrjfkMe2IbK7CPinefCZc9lGhO7jFauth7nWvea0SRnmGPF9ihvcEhuxSAXwAxGBwBwxCUqK-tRZavyO7m70YKUYvz2iBsDg5Oc0Tq93dU6Fz6OyTiZSyMb4z6AitjDrfvBv3RhJ4mNM0xQmS76uhs4esMFt-JJA_WaXh9sCWYTsEaWF0PnVo-kFUyq5j_MKXWDGXbLWx0v2DT94M6_deqZ9TSBhKSyHzPfb6o8yD15iiI1Y2lLW43LtcriP0E6_jlT4yPQlZwTf3vTCNBsdBUcZPrZBZ5oUfynWPQbhi9ZWxweFeDk62l9gII_WMe5Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rgb4EiQzl5UJOfopPpKh363h5UGD8wm_TLvCUB1bE_DTKBxRxLZEIwPDa720KemoU2jeXctA_HM4TzwO3DDEqJL5OQ-iaWxsb29vqxmQO3Q2Wa1a9IMcbQ62KipY8ana9OMDDWKDkX_A00vzG_-RUXlZ7HmzzixO-pp4YVhNIlkdYvZggBt546vbfzOvMF2TmJLC6LPHBSS2OjoT1kIJwf4iW1OuylCv8P6jL7vVa-vK9KMH_E-DMxyq3dHlZiuCkYed23iqnvEJ6Zp9mFZSUdKialnmy3iOJr7gL2Ppx_S38VMb9YXC-dANZvVKS3IriwxBhtqrAMqMXKw1zDKrGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCTb7e07ylR-tc-lCYIXDe32BdovWTsa3A4GmmVl7zDqYKJrbs6NDb4-zdlTyJueA5kALTZQRx_Q942loyOVXXvckDkk52sIpuzPSYkvCNqh8a5fvRlHb2AVeWksolAqpMbC9qkFhPmWRVn82gz93yq2Pn0fKZKGIqQvC5KZvROVwWu7JdnsW-MaxTuEF4u2rcGlIkSH-QiCyba_1PiSq3ogSZJI591C49EffcghN9JG_dtR5kbCshaCQZ_sPR0f_toMv2mwJkdEt3mLgSBeA8y1X6xWyrhRH5SuAQ9kyS8-hv2igOPGtzWhko829c6kz39mPp9MCgmz0N_I13UbxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYoWDKPJS69JDt2ptai-CmzCjF99DuLsx0MseKP5bkf9c6znZu5U-pSjZhGYlbQ1sNNMCRcFNB-uthvkkNySar5kz6nlQu7Ze4iINpA3qjwEPTr35oo5RpQQ3XnjAnW2gKPEQFa4Q3EOtq80tR-RsO5IG8nEv18xazW2-oRZUsuzkNWikNigUzRgZBQO0yXdhfDPSVSSAtGAjjVEurDkPXugxdZ_mwbYdcTzc2_it4U_gSxz4oAfRbxO9hz9_sGd_e9ECdLDRMaLVOGCGdf4bV9EZ_Q4F_ryDVG1ZFmh8Sxy9uonF_ftXm7OR4CLj-2pbFalGbl3Oxh5R2ngsg9YHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln30nGsH7bhjuMrgY9w5cvpIFt4W3mJdsa8HVstGpZ7ESG6CoTydXFzBUuGc9QFGunBu7sWpmuD-HF4HmIRon80Ynv5soe07SbIC_9HSPNHVGbFZw4dJH73VRAR0eaXxuuxzppMLGvmkk_8fypj-iguAGFirjrmJlwqyu_nTrPlQKv3TEFg0Qm1w04OWsXd3YHalKA8BDhcaObUp1dKWgNHFdNSjraYmoW_X_0zqOyTycv7UFa3BrGJWPUOSfKY9id-UKCe86c0fVWN1gNHKV-BYqLTLkihioNXCLx-5Ksr9LaDLHtOKzvfQyTRRfBpo94mD6b98ATt9QpI_CmhD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGZnPFwbYMUJ5ZTMBEIzKRNrvEMcDxosKUy3jYW58kMAbf2tkXgsiDiFfDqNEQCvH6uIhZ1C2iY59e9NeG-iCCf18p2x_n8gefLVlfIpq7XesX1jMWZFq16Fv3bHzbcq7irQ0W1or8fQq16YCMdlicH32cc7I5X_g6k-TPxGiWpfuDv4LeIYzsd_POJgaH2xFgyMcrUv-RX8YS4UOrm5YfaGkyfZ0E8GniyMACrVbsYcIRV2a-6t9ym_FwQGIHBsv6Er0gt_NARE5BiiU3dZTVmwyJRZ8dajaxrlMz7YUO9yGnL7hNaZslQvQ6iIK8ZYusQjcTWh7TQ7OCWdQkKxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCoqqsyq43FgzokfGRa31k5f6Jvd_vfVKtFVbVq1ytDlfnxTP0V3hcCpc8C6cUNxbuG6AklXRq4JOOo7Cs-wyrmMvC6cqmVQu1QqpDBFS-0tl5h662jO755TUo6267QZmPz3FQr5Fevg4WmAY-Rb1EtbPLTisGU4uVIQ63iS2VwOp15v1GW1WClWFkbowHBh-xU-Y1_c9P964M0p3aGomHfMVcVBeaTH3TjcTpK1ve89f0Qxw5mHAe6xEBWw_8WlD6dMb1UjBfKVHU5mg84D59wPx3aMoZpoUH83eYbaiyLKjqudEW7EfnQTCmC7nIyUA8yMxRK_PJTqKobaAV4UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9vY0TwmJCjjmPJcRrqms-oEeDUcLzN6WSPryD4clNCtL4OPcMzctcoZ8pcgoJlq0jU6MBRBXR-VAfyQFuOChVu3Deh8n7ZL9m_4UvgLca3dMeLE35vAEBnIczgV7BktTyOpZnk2lYMQ3cNc2vDCcN9LRv-LDfbqFjCtPsBQr6aOeE5pd-VipnHYSdBozjYyozKGfirdqYKi62wAft6htw2vcXO7ist5vAf7WdFL--2iPKDkjkUoRSoO4O7YzyQExABktgFUUMIlzi5E9pcxeYVsKgYeeh7WL4YlNs3OeHY9t3iC_xRGyJjJc3-f-ksuVoEZInmKjtqMYzOEbMUFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn8dI_ZRNwtKGk_nY8ksXGuYHN5ryHG4uCpLngdW0UbMCWq0MvF8xip80EKOFfIFw6dRWcXdgmfkQ7SHRPUk4jfe43C_FDAqLHHdUXCdE5a4Oc5tA4imHkbiDfv5Q7Dy23Klhs4KGJebSwG3cVbm8WBFwjzke5f4O9ixY80z77OYqgS0XlqAo-1dQ4JOAJD-Pdjx4B5QwDBPSXcnaQ1hzCss3fnDIFz9NZLJarqaJeEnExEzT-2pRSow3EpP8btR8_nk0wXUbTCY3va5n3DuURZfFJIpi_8WzQP3WZbyuM70BDgJ_z4_y6pzwR7sxiqYsepzXnBksMNmJhNHq_rpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibwV_KUNtKpYvP8ZRKZ9GLAMoPDHGf40ILEvry9Z4v7ZHkEDFyGYoFSw20Aqd6fDQPt1jdyB6U5GfiWOGwORjvzofBiU8uLbew97m9snD2SzF4omMoEX7XgbnA-561mWaLZhzaVO9Sb89lsbuykxDQiN2lkSFfPNCcdj4WuTnee0m4yYaf07t3FT9FY-2N7mATkxYBIgwrRJnSt0825ucp9vqhA0Jtisn5Q3mqdfLu2m8epQQZ8rVvbA6jjMhIyJdBCf2cPYsOG-Cdl7997NTV9LFxoNyxigpcovGp-orsr1xQFmuxZBOS36tNmEQMOsR-L72gTtXzwz2N7VAeFu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
عزالدین اوناهی مقابل کانادا:
۲ گل
۱ موقعیت عالی ایجاد شده
۱ پاس کلیدی
۲ شوت
۲/۳ دریبل موفق
۳ مشارکت دفاعی
۳ دفع توپ
۶/۱۰ دوئل زمینی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98213" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98212" target="_blank">📅 22:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8zBFyd5ph5DjpYNUg7S5OdQCqh5AzagUWE-AheUKfIgYD5QT3p1UAIiTNN1T1mWb6HuhspWKh0Kp9thxsSvzm51MMNz5yuQZ0olzd3Vewpg9rq_iT-6teF5whRdLvo1eZDiU0yecLtAc7v07nQ3CTcdOg3vQmGO5BEM27Ko9zdItXPnO3Gw80GbIIoDcdU0k0HtyyXHugraE9EskO2XSLiC5Py6LLXTnbXHCHioscokzBj2ZHbTs0rn1B2JkH0Tjs1jPfuxrZiefOcOCeP2t9dNRlRMQGP5_S_Ohy8CF4k4ER95ued5xOoag10P3izTeUYY8cex81GJm0OWLLEdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98211" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=k8BtIiNboo86QY0m2PaHp2rQVIkAmzkH3mUmu4w-7pvTDhD-5rU50BxiVAl4e7kSXw9qcwffW01gCsRAUzVjx7AxeGAaLQRMiq0pdAkMDP4hXepDEaIMwxe5j7k8QRz6TZTHmsOG4zngAGkI-7VNfef1BBn2op3wStEoLgClUE5iPhLm5GKOcexkbxjBd7UeFvoDK1eSMGHpIBSOoRBimyGQEmSWCipj4GKl1NWhGvMqfAAD2DNg3t4JUJyd1uVC9_Q77MzVv1Cs3beJRA-Zpo1EpdKifJGeooqIIn7B8yY6QehAdikitJtTP0wPoo5jjkZCvEwtEraM3V0K3OAXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=k8BtIiNboo86QY0m2PaHp2rQVIkAmzkH3mUmu4w-7pvTDhD-5rU50BxiVAl4e7kSXw9qcwffW01gCsRAUzVjx7AxeGAaLQRMiq0pdAkMDP4hXepDEaIMwxe5j7k8QRz6TZTHmsOG4zngAGkI-7VNfef1BBn2op3wStEoLgClUE5iPhLm5GKOcexkbxjBd7UeFvoDK1eSMGHpIBSOoRBimyGQEmSWCipj4GKl1NWhGvMqfAAD2DNg3t4JUJyd1uVC9_Q77MzVv1Cs3beJRA-Zpo1EpdKifJGeooqIIn7B8yY6QehAdikitJtTP0wPoo5jjkZCvEwtEraM3V0K3OAXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل سوم مراکش توسط صوفیان رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98210" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلللللللللللل سوم مراکشش صوفیان رحیمیی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98209" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhxeB3IvQGlr8z-Sb383QwQArTpAqj8WkUPmkueAgIQagpGZzdLbx3PiOLbko7T00rD2EG36q97rQ8DPJh488XZ8oUJMEgwJ0d7u-UaOVKcM69RIQsv8o2GaPNUOz0WQr3k7TpR2K76FpEn69JCFzis_9Z9AObgSzt_byvp476YfeSMybuqIuspPoiHQvHGYMx7CC4bCTXv3GSwZPVfSUWjNLp9GKx39PFy_kNiiVZOk6A3Fs6QncTtwmjfS_oKDuTlURCx7sX8meOesxs-yiK8hn7m3xKbISgHKX4poCucha4fIsdf-ov415-czO_0bHJYCC5rJt-4uHihnOYH9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان عزیز مراکشی خوشحالن منم خوشحالم
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98208" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=Vt1JhiH4f1EVd3In6N3229eCk9LDolpWuObMdhSo6na3PjilDL2vcCdGWmJZIN-7DlHbT8ZYSTavKo5vk1iJnzsXVn1xrL8exPQcBknr4J9CGWB3SCem70Dojz5m561bWgh3qmDoNosAWGjRaOqKlnC6QJIMiGjIzeqZWv4b9AYSH6HwdYmMCbsScoWttb0GCSXCPbTrHmutLMArhmgshaYOMm92BrlIg9X97jnMMg8Sg4lLyJhxGQRpjqqKziW_ZkyIjMzVWCw1RSGTJKB-IcN2J6wQhL3wGDCqk7j6HtAZVqFYsqBf577_qQKWGi6T4iUhnoRGTVV4CrvwhfzSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=Vt1JhiH4f1EVd3In6N3229eCk9LDolpWuObMdhSo6na3PjilDL2vcCdGWmJZIN-7DlHbT8ZYSTavKo5vk1iJnzsXVn1xrL8exPQcBknr4J9CGWB3SCem70Dojz5m561bWgh3qmDoNosAWGjRaOqKlnC6QJIMiGjIzeqZWv4b9AYSH6HwdYmMCbsScoWttb0GCSXCPbTrHmutLMArhmgshaYOMm92BrlIg9X97jnMMg8Sg4lLyJhxGQRpjqqKziW_ZkyIjMzVWCw1RSGTJKB-IcN2J6wQhL3wGDCqk7j6HtAZVqFYsqBf577_qQKWGi6T4iUhnoRGTVV4CrvwhfzSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل دوم مراکش دبل اوناحی با پاس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98207" target="_blank">📅 22:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلللللللللللل دوم مراکش اوناحیییی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98206" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cipswXVJmF9rdawj8wFYmNLv8ScYP-nZlCriISyT80XVG0x5g54C5gQJVb59suRPn4dxNnyJ-kygGOPTRygRoLL6oV1iUmuZUAEsqv5N2KzXI3sDVkEojxFILjRa9dKKG-t2lvk4AqyfoqaYmydeTOgITJei7I-C4PB-bsk_9ybFhpdMO_CeyV7aMCPxeZ08ZEZZZHOC21Q9T5_5P7gjbSfEF0_cZTIAze89Ifl6oXadWzt47PKSB_7R2a1mMZ8LCE7_57SPdc9cPuZg9L_iw11CZyQNT2W6sPj3wMORS3aeEc4dppl6eoe2XAHEvdaGfrTaP10p_tJnU1LGH2cChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98205" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98204" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SG-kcDTgslKCQ0oA45UI4vA07N-joLjTVJdlzgBwnwQh9dDtD2MWMfdzmFpaQCu-0Qw7a_XTmpijW1kdpPh70JRNdJHoy0iQ9SYTv9Eri6dbT-ccxclxO-QoV8-lZTcH6KJomb34vHXjMvte8RLWKLszrmtGGUvMACuWf0IgqbEEmlyuyqEOTxNrAIl1QhUN6H5ZK_B7mSSmJAsP-8-SJy9X-Kllbbv0qCc9obkOyyVRBimK3s8KFZe6rf07q362RsXLevpIAJ2qABu4gnbUiMNnfGOc8yKGfG1CiQhJ4eFn0NVUwwjJkrqs3jywXUFmGKKLIEJwk-ryRoDQ5_S1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98203" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=adNXQME964BpKXz9sOQeRYJ7mdauoS66HsfH3X7e_rJ368yMx0uL3fVS92WMLBJIW7Xcj6oRsqN1vGGWOv5x-sdCznbDZYlZ5kZI_Gf8405dP4wXbtGM40wTsHpF6QduGIxK5sRdVmiNKnLejmjJ7XhkLlZyTHvEJafTNeOfsLR_pcpABn8cT-iaBjQsA1EPHTxB40G_OEakgsVwATVaaBvQPDq2EUFyt2OC2bo2SQJ_UT3SV9TFd6T2QuvNdEEycuzUdfkj1c1AmVg3hFsPbVVKPWeoLYFcCDpggDZX2CkhlYhsFluOmg1RdT7tq3ixttZfTiOVFxkDoQ8G9206CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=adNXQME964BpKXz9sOQeRYJ7mdauoS66HsfH3X7e_rJ368yMx0uL3fVS92WMLBJIW7Xcj6oRsqN1vGGWOv5x-sdCznbDZYlZ5kZI_Gf8405dP4wXbtGM40wTsHpF6QduGIxK5sRdVmiNKnLejmjJ7XhkLlZyTHvEJafTNeOfsLR_pcpABn8cT-iaBjQsA1EPHTxB40G_OEakgsVwATVaaBvQPDq2EUFyt2OC2bo2SQJ_UT3SV9TFd6T2QuvNdEEycuzUdfkj1c1AmVg3hFsPbVVKPWeoLYFcCDpggDZX2CkhlYhsFluOmg1RdT7tq3ixttZfTiOVFxkDoQ8G9206CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به کانادا توسط اوناحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98202" target="_blank">📅 21:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98200">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مراکش اولی رو زددد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98200" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98199">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98199" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98198">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98198" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98197">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPLHVszTeeh1fNDsDaRT-or3XflJU7l77MqAjjzyLdjsC2VhGQa-o_HriWrH5ix1z6t3wqHHth4ugKVWdVcIqBsREYJzzxBFfpgKJkCR73A5OeFArEI5xmU6jgmCqOruDa_-hnSq-BDNygNgv_JSCtXvkFNstbCuFOyYGHSZC7t-7okOzSJBNapeiUdMV4mMTPWthaC1X5F4g-0x1C0LoUmHJDnhurfW_I4tOzKGaF8fJsaOp9gdg4-1-FMOjODeLMWGp0Hue0F7Db2EPHb2rkuMomh4sKevkS94_zhv61jO9Bwihs1VyHBQI0Cc9uNRoC0xTCP8VqPR5eSEeBKTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول بازی مراکش-کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98197" target="_blank">📅 21:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98196">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ_Bnw1HmUiAaWhCtb76dt7c53tZ8bPwNPxLy0_1ef-upb-Z8ACsXR8CNH7iwYMV85hp971Si6myjDf88j1Yj3h8alUz_6VGGjJXFwHvfjzpmK09d92XZ9mZVkLu_rROguBXPf_Yh4cNjWVhkeK-JXI7VdCJ3X3-HRtTFOohZcNtp2CJbDeUfAg3TZbhW7jyKvb9VD0t2XFqTdJn18kTXf8fGJYUFmURUZwNBI3g_a7j7PIoK37Jd_3n0G2WS4-N6JZKgIFjs2IYI1vyL4D-OP7kEnCPoQHI_QEI59HYDdZGLiAHjxVHPDISqhD87VPVkyXlL0u7jcuFQCUWsdM51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی اینفانتینو هم دیگه خسته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98196" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98195">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پایان نیمه اول؛ کانادا 0 مراکش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98195" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98194">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oICVrI3FBvyIypJvMyl_5q_PshE53ozRc0C2eBIO48yFpPkrIszSmQe4RCLsDIO-uXGSSFf7CO58yqQPOIJervEiCc2rnFwYP0isxsMsvA6sHppefeNx8JOXvMVOJh0lFOyIdIJbTG3nJcDbaMe27Jp_5DQ55E1A_-uFsraKFOTG8eDFzUaRq1M50h0YroSuulJ2UkC5oWRvB3kRnu_4n3YJCRZHvKB8-t1Rj2-MFkt6vFTwsW_PxaAGY9LUvGYIV_9-sl1XQvkuasLOzaJNi39eb_IQtMntHIyHOYQZgK9d5fiEYsIroy0fKXPOXGFZqZG4W3ixgMgLRM37MeF0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایباری مصدوم شد، صوفیان رحیمی جاش اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98194" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98193">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDePLlHiZ5kK-l39LbDwyJimB1dCNK0_fIK3Q-dkxYl7jEiMpL4Hd5N4F1LZRXCevVdWrT4UxPGIEZA4MkNrbHRnjsIn1CH_JoLBH9uCxf2uC05rgQuDIhEDtkmO9Lnww70Rm6pqnHtYe2K6u4cfYBiW9s5-k3GK1VPRMjygQK1MI0AEJO2uAL5-vW3_JfoWFsyldoUe2oNs07hS0u0leC2CYFCj5YKnMmW9apu-BCvrG67pWHwkkKmT0vnqPtQ8ZVtMQSxHZLq5WqVHGFeALMrumK3ghbNAXy6jsqjwxodU8tQpDM03pV56iDtB8zB8dhT98QkmZ8b5HkXAxNX0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98193" target="_blank">📅 20:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98192">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9BIwQtLUgKNiUG0V235KKZuh4mQt3uVkJI-utoVkqkodpurdYjPH2lglLtqRv1QnHmj_T-d94SwmuXajZB3n3bNjVolBk-oeXAbsE931xkAZ0BRW2hAJrmtuFxH_tTq_tbJC3CqbCinScxpIYKC9PcPnrh5gETVDiNLhIgoIyWVY0jkFtBKBPNCmoDp5J6BxzZZ8FmuK0J8EGBMsjbMKlwYeMizClmQ6OPRSUfv6ZABY1MiVIgAHAZS4IcmmyKaZGbtRtB8HCR7pQNzBSrQvMwn5t1LM1dRoPCWcZB9ih4DqfxsbW0R69te1Lw6YnNr0Cj-5oWo4edrtPXrbcct6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گلریه این یاسین بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98192" target="_blank">📅 20:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98191">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سوپپپر سیو‌ بونو</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98191" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شروع بازی کانادا و مراکش</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98190" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIGZxn3CO9MCVX1cQkq2jdxrgvnqqgGuI7Ny3rsoLu5SRe72fE0b5JeEFz4amewTGVEsPibaxr0UVu5NojFlBKDCHYT_EgxXCtFZfIwvnengU18kYEOf60uu1l0pRJfxqANRIdRNK13je77U2T07oOxkNg7k2TY_6sqptncZcfTgr7b-7DPYegx2URf1V9c4efoXR6XGbZhx0K0Q1DMFHsHXHyYWpZZvYZlI3Cte39j1txkGv6NiMFrS5TfjcybpRfW35TAFfe_ussqI2WKUbCysWAqlDnwYWRPmYAcQ4I03b7u0mvAxIBUtg8e9uwZhmV15HoopBQiQ1TgJFz-UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آنتونی تیلور داور بازی اسپانیا و پرتغال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98188" target="_blank">📅 20:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBf31ajNOjDkKgzjU8JctgmMykwyFo_ZQY0Fxm3OZlgowEW6xYZLAwT5XrvjsLu9fmnW7DwGTNlgJqOyfe8CSpLUA4IlLSn5HOMMOSZ-xvEYl8c1kKIg1_b0Bzyd1BpCdVhBnFUorV86sy2ZdaxAz-d6noOeHWNxZUwFRnnn0VjTZsde-NkgAuIrneVjmKDMuuJ5Ai0E8vpcT5lXfppubSKfE6VM6UJe3zwOr-xj-pmXJkW3XkiSEWgAS4FpBNJ4fTbmvOHMQk0DjJrW8oQ15t9PtdCm8M4FFh4odm_Q994v7As3-wNmxYv25S5XBl4R5vtyI48cUOYAY5cDQC2r-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
پدری، هافبک تیم ملی اسپانیا و زیدش، الکساندرا دورتا، عکس‌های جدیدی از کوه لی در لس‌آنجلس منتشر کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98187" target="_blank">📅 20:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWeSzyocPwAJQrO_Ep76MjpmR6QVi30xSeIcSFSE4Def4gInAYLBO9e15T4cZGi6sTLFQmokFW4PmKu40abw0XSGAATtrjZdgw7nuEEE_2M57Fgk0nwrvnwnyG4TIBlTqo__sAyxnX9jhHHBGD2UeRadz8V61PxProoNkC1SV9EjKt2g8DUBP3wgxKImeQIB-pqWU12YW6L2IL9RITwjFA-rgJ_-zbqAV1Y95y-yRdMlvJ48cpWrOAWyMNwRxSC5MjYA3ObuWepdSfjS67ghhDpCEZcz05zINJVEoEANd5KZJBCfUkkJn8ReioaPydf8Ew9FoS18Vo7NV_Ehpwg8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
: بشیکتاش ترکیه با آرسنال برای جذب تروسارد به مبلغ ۱۸ میلیون پوند به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98186" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-vwLaEZ1St1ANM07nGfbhZZ5r5WgUPmTN6sK4RRuKMUW-z8-vmCEplvUV_jgHsDklNdfzTNZUnZmy-auQQWcQFfpyI-dc_cJONYAOW-iPshX8F5nJ_7BD9hQE5KwEtSj70srE69sg2qpKZ7KqTPYf-hEeMnUDpyQCxD6RQ6J6oE3YlImg2IKB-0kCgvVSIf2V2NtIKiDz9MxLzrA8KGN9EyQka7JP3WdmhEsthMpdM6mpx8_B1FJSAoYtoIQbbVXzfkb6iclDQMjxnJSA9OD3-G3GE-JFQfFawHGNB2KUPm6KGpxfsrUiyuciuNBnR5FlotxNGISY5ENpdKh3X4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— RMC |
🇫🇷
🇵🇾
فدراسیون جهانی فوتبال (فیفا) اعلام کرد که به دلیل شرایط آب و هوایی، احتمال به تعویق افتادن مسابقه بین فرانسه و پاراگوئه وجود دارد.
‏"ما وضعیت آب و هوا را در فیلادلفیا به دقت زیر نظر داریم و در حال حاضر احتمال زیادی وجود دارد که به دلیل شرایط آب و هوایی، این مسابقه به تعویق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98185" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=uThIJ9bRYQZcQ67jn813lqWb0UvKgI1ab1bTukVzC3gXH86ap0wANcAuoJ8sg-wbiQsfN0_AFbdtVBuh5zlKX3ZrBhmBJKMx1NOtKod4qENCPPVZ0U6sXtfpnvu2Kh4uJWniDRsFlhj_XFGQ_-A7Djlsd6kTUrekaUDieUp5UNRqgetsGl49xxKLN4Okew7-8AyfZS_xYTafi7yLJaI2mlvm1wAnz0O23piuBWTc8PPUm2_SQFxymEviYB2I1G4MXfmc04Jl8fnGkmz3kNZAeWDsWeS2S6Lybl0kacCGVgcCvmd-xiWPO4JbugdHTuCv-IeWlC0LL_PU0eLTEf_3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=uThIJ9bRYQZcQ67jn813lqWb0UvKgI1ab1bTukVzC3gXH86ap0wANcAuoJ8sg-wbiQsfN0_AFbdtVBuh5zlKX3ZrBhmBJKMx1NOtKod4qENCPPVZ0U6sXtfpnvu2Kh4uJWniDRsFlhj_XFGQ_-A7Djlsd6kTUrekaUDieUp5UNRqgetsGl49xxKLN4Okew7-8AyfZS_xYTafi7yLJaI2mlvm1wAnz0O23piuBWTc8PPUm2_SQFxymEviYB2I1G4MXfmc04Jl8fnGkmz3kNZAeWDsWeS2S6Lybl0kacCGVgcCvmd-xiWPO4JbugdHTuCv-IeWlC0LL_PU0eLTEf_3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
در کمال ناباوری و سرعت، به یک هشتم نهایی جام جهانی رسیدیم!
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98184" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=Mxrs689BqNNjpZzlDIP8X4olgCww2136k3zGLSKMPjRhBUyiYdS6Uw1JB32DAT3t_M7_fW0kHZ_tyKdi1nOV4g6y5y-N9HuLxylCmxCzrFbU7UoErQCq_jaQNhqLnfRUpptx8CLItnkrHO565RAEIMo0noB1yAFNpB2yQ1_Vu1dRu8GPuymg9mpdh8TJbWSamH8H3JFkYNnrGKAANMKYKRnvF769zPakspPhDg1DicDHt1JZGf1NChKER-gNQ14MRGbXXmcjVj18ynUAJ6Gn6nJgO0Nekl9_1j53nuOG5VSB14Cb1liH3Ai8NZCiMN28DXMrcqOxCAuiW2822-HoJ6GChYQNVObEcH6Ehg6NEXXgadbLwlzWirv8-UpZ53Wzvw1IMApPfC2x7HQx5i6KBbN-25ZhSSKXMaOeYi2f75l57f_pb8kj6kr6ztonvVwDKqtOqGmKX4ZhuHh0H-0-rve0fDDRRhZGk7wjWjIWUty7kinL_Z9BBRA3Q62v17w5lNmdKQkPoLdJSQlKEgNIqjECDIUuxSve-W_hWX_enmqQA5u74n9WUhF3la_LM1CDAkbjWtzls2yq4HgnOye7yx6Lw74szy8PZxxubqErSiCq5LY16QTygeGsAbuveab5h9rCifba_P_eoazFzNf495pDrMfS7fJ_GoXe_hL4BbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=Mxrs689BqNNjpZzlDIP8X4olgCww2136k3zGLSKMPjRhBUyiYdS6Uw1JB32DAT3t_M7_fW0kHZ_tyKdi1nOV4g6y5y-N9HuLxylCmxCzrFbU7UoErQCq_jaQNhqLnfRUpptx8CLItnkrHO565RAEIMo0noB1yAFNpB2yQ1_Vu1dRu8GPuymg9mpdh8TJbWSamH8H3JFkYNnrGKAANMKYKRnvF769zPakspPhDg1DicDHt1JZGf1NChKER-gNQ14MRGbXXmcjVj18ynUAJ6Gn6nJgO0Nekl9_1j53nuOG5VSB14Cb1liH3Ai8NZCiMN28DXMrcqOxCAuiW2822-HoJ6GChYQNVObEcH6Ehg6NEXXgadbLwlzWirv8-UpZ53Wzvw1IMApPfC2x7HQx5i6KBbN-25ZhSSKXMaOeYi2f75l57f_pb8kj6kr6ztonvVwDKqtOqGmKX4ZhuHh0H-0-rve0fDDRRhZGk7wjWjIWUty7kinL_Z9BBRA3Q62v17w5lNmdKQkPoLdJSQlKEgNIqjECDIUuxSve-W_hWX_enmqQA5u74n9WUhF3la_LM1CDAkbjWtzls2yq4HgnOye7yx6Lw74szy8PZxxubqErSiCq5LY16QTygeGsAbuveab5h9rCifba_P_eoazFzNf495pDrMfS7fJ_GoXe_hL4BbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
هواداران مراکش در آستانه بازی با کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98183" target="_blank">📅 19:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGUJoyysShXlJp4Swa-VeAdKzwWVawuabtHx9ndoLvpx3N7JfgTT5-uxek61WJaJPpIlPnkbKjNiHztgYBi98rl6EuPijs87cOr3GAEiIh6xC1y1vaZK-V53KQ5n2-kQQ6aP0K9G4QvidzGLka5DjzHVMCjkl2wSjLmz37hV8p2EJtXbiIox8220-vMf9xUxyI_4tez8bk7O81CA05tnDq-IeBbM4XhMA4Btf_bFr7KGakLTqKYNHcjluJByawN79ejpI19Vnoyi4oLYGK_veFVlD_duyCgoHafYBko7unfgO9gfmFmTZnocIsYpGzWGjDx0MTKZg7McmPgMUsW7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
ترکیب مراکش مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98182" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBISd-Ht7uM-7dR4CvYQsq09-8rk0w7f9WQxbJLpjld_UCQWbuyUxDZcD23tHrBxqXqpRQPz0Y3u9tyoWXUUrCXYtBqzCQi-RoePldwNV11SyTXonRkWGbhfjekU1KJs0VlVUYp6j2XaCZgP8Tkdz5mG8F6rfX_VHkpSkVv8TRnmstzQbXVwo7t7TUR2NJP5Ga-2ssRuyc6f41A6K2J-vsMvj_NrOLcyeZykxi3ppby_uGKNtFKaP_jN3cpkOepmMa9NpV7dMGa6rmI-JbJd5eLSxvSehC3EoVoqJhIG5I4dNtnwsIVKm4yb9z8qgiTpc1cIY1gAFXJdWyfU_wzG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇨🇦
ورزشگاه NRG برای دیدار مراکش و کانادا آماده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98181" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
