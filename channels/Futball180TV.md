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
<p>@Futball180TV • 👥 596K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-99522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=XVPY9ekOQ14HWq40Vd4lVMzsPfi9vuLIcIDo5qD4gCKWrVB3tUCUJa3EI9cEnO7LxcDxKlenNessv7X0knv7pBIWeJS2ZtNyt9RcQszjgjrov9uVoxyfJV24qGINpSsl5Hqu7M6LM723_-DejqkewTgBsjN2SzJsJHGwB68UVmwxIgV8B8Ou7WPZNtf_nL8CDMGFynxMlrVyffLWlndqG2pQWTDhQuTk8h8jVqbjCAoA3icKH3JZp5xds7DqlfXaR9hmJQVlacq7TiohlTsmTP-7gEwnmqGxgwqk2sbVCXaXFSDwtvHBEFausgq6c5OJc1hPkSwPvoUSF8DkDvOA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=XVPY9ekOQ14HWq40Vd4lVMzsPfi9vuLIcIDo5qD4gCKWrVB3tUCUJa3EI9cEnO7LxcDxKlenNessv7X0knv7pBIWeJS2ZtNyt9RcQszjgjrov9uVoxyfJV24qGINpSsl5Hqu7M6LM723_-DejqkewTgBsjN2SzJsJHGwB68UVmwxIgV8B8Ou7WPZNtf_nL8CDMGFynxMlrVyffLWlndqG2pQWTDhQuTk8h8jVqbjCAoA3icKH3JZp5xds7DqlfXaR9hmJQVlacq7TiohlTsmTP-7gEwnmqGxgwqk2sbVCXaXFSDwtvHBEFausgq6c5OJc1hPkSwPvoUSF8DkDvOA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
رقابت بر سر توپ طلا هم امسال خیلی جالب شده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/99522" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
⚠️
شکیل اونیل ستاره سابق بسکتبال NBA مهمان برنامه ناتالی فریدمن بازیگر و مجری آمریکایی شده که برای او پدیکور فوری میده. هرچقدر از سم بودن ۳ دقیقه بگم کمه
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/99521" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🎙
🔵
🔴
جزئیات قاپ زدن علی‌کریمی الماس فوتبال ایران از دست استقلالی‌ها: فتح‌الله زاده به من گفت دزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/99520" target="_blank">📅 09:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ud8_GGUhIrhTMy23mm_xqAwW-_PVFfw1enFg0po9ILGGJRnlqikZWuraW2bAHVXVA5au88uWwHEwPPeu4vGRQdVBQI3BQDxEM9fvFBOTP-gkJWAI728E9Yy8TNNHqToJFg-bmEIE7XoZL5rhU7GdJ4EFOb8uj4tl8fs0FCzuIWAV5ZhtT58JJr48mAXh4-F1Qmx8HgrjmSgVyhyoylLdiiI8wGRBtoeVBUBVr5LIrM_yf8I6gdlP0wp2Hwz7B4FPfe2Bgbb2FvKTMc1Z-0BSlzMz0xggMt2D5wB24fQR7VurL7V3p0Xd1pjCcSNiaLLGMHIauxfJfLqg6LRUbYtWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ud8_GGUhIrhTMy23mm_xqAwW-_PVFfw1enFg0po9ILGGJRnlqikZWuraW2bAHVXVA5au88uWwHEwPPeu4vGRQdVBQI3BQDxEM9fvFBOTP-gkJWAI728E9Yy8TNNHqToJFg-bmEIE7XoZL5rhU7GdJ4EFOb8uj4tl8fs0FCzuIWAV5ZhtT58JJr48mAXh4-F1Qmx8HgrjmSgVyhyoylLdiiI8wGRBtoeVBUBVr5LIrM_yf8I6gdlP0wp2Hwz7B4FPfe2Bgbb2FvKTMc1Z-0BSlzMz0xggMt2D5wB24fQR7VurL7V3p0Xd1pjCcSNiaLLGMHIauxfJfLqg6LRUbYtWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میثاقی دیشب ناینگولان رو آورده بود آنتن زنده که یه لحظه از دستش دررفت تبلیغ شراب کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99519" target="_blank">📅 09:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=S2JY59v1yJgKlez8AMjHjnffvh7yaBof5ez5u6AoLTUwrfAiaOCW3nCPjMUSy-XGy0bLHTQvsc8YkTSKjnlavy-qAoldt0AJ2tI35ynXTr3yl_ae8PJGCh0lnzP0I3KlwlF4eozTCOPrtMCU7aVL5KFe_o5Tk98wZF5GCCKIDLVnLalXKphsXD1TKRqxQeuxLh9tkNkUvozmbEss13JACZd5IvIdhpQ9RfSZWDPnI5eiTRzrLGXMU6d-QQaTXwZg4gHQ3hboKo-G0iiGiufYOw7xkqm_94aTSgCgS7jvoWX4PMVZvjKHmz3qgNnLp7QR4BtJC8Z4NPDrgmTacDB0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=S2JY59v1yJgKlez8AMjHjnffvh7yaBof5ez5u6AoLTUwrfAiaOCW3nCPjMUSy-XGy0bLHTQvsc8YkTSKjnlavy-qAoldt0AJ2tI35ynXTr3yl_ae8PJGCh0lnzP0I3KlwlF4eozTCOPrtMCU7aVL5KFe_o5Tk98wZF5GCCKIDLVnLalXKphsXD1TKRqxQeuxLh9tkNkUvozmbEss13JACZd5IvIdhpQ9RfSZWDPnI5eiTRzrLGXMU6d-QQaTXwZg4gHQ3hboKo-G0iiGiufYOw7xkqm_94aTSgCgS7jvoWX4PMVZvjKHmz3qgNnLp7QR4BtJC8Z4NPDrgmTacDB0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🏆
تکلیف اولین دیدار نیمه نهایی جام جهانی مشخص شد: اسپانیا-فرانسه!
🇪🇸
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/99518" target="_blank">📅 09:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99517">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovu4gkPkjRyHC8ttvoTuq0JSBKkMmQ-BrG83v2FP5ndm2wZGvY1WXyP5f4D5fwkCzRvNt2VC_LIxHI8V8grihAm5pouh4UFruhMNApSz87zSq2RCZ0bdQ51kL7jNml5ZaB50IhQ-07LSaxH9JTQw5ln6BetPf7-tM7Dq_e63x-BSHIQaBSA5l21DUC-g8ez4_CC6ZIDdF5gx_l9e_iJaHcTY3xqYU5VQ9j8UFPYo-rWCDODhoxjZX-cBpd3r2nvsyZmHaeVju7i9YAx8cbTuAVhhI1Mn3VMbbDdzojVUjQzQf-zRHSKL5RSnXmxNihLnIYwSKTxrQGRBlRgxZIxCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
نیمار دیشب در تمجید از لامین‌یامال یه کیت با امضای خودش رو به دست ستاره اسپانیا رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/99517" target="_blank">📅 08:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99516">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=Ou-H-ugxpNk_JMhM_By6RPi2W8os0Is0uatYGTqCPgUWHNuxNQsIgUkrdITPI1J1auWjUq4ddnrB5YojSQ0ZUdRJRvyTp4j9oMvVtC-EKRunrhjYcWXL3-H_JfX9QayNzLfIijJdroFXVYCmmbKYaVSd6XlaoYugZiBXYGYpt5o9O5Ju1k4LCec8WNgfwtyMcO9TheXnd55DkbqstwYKrbFpls5j70PFyKCySbfzXfCTeZSLqtGPA1VAxZw7Pe9-Wrc5laAhPGA9W27VZ8fGBuj29qLR1uR6GXAikPPgF-vQT9YVdW1mLM7ErHwDC2m6EJtfY3eIiZP88GYfnAwtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=Ou-H-ugxpNk_JMhM_By6RPi2W8os0Is0uatYGTqCPgUWHNuxNQsIgUkrdITPI1J1auWjUq4ddnrB5YojSQ0ZUdRJRvyTp4j9oMvVtC-EKRunrhjYcWXL3-H_JfX9QayNzLfIijJdroFXVYCmmbKYaVSd6XlaoYugZiBXYGYpt5o9O5Ju1k4LCec8WNgfwtyMcO9TheXnd55DkbqstwYKrbFpls5j70PFyKCySbfzXfCTeZSLqtGPA1VAxZw7Pe9-Wrc5laAhPGA9W27VZ8fGBuj29qLR1uR6GXAikPPgF-vQT9YVdW1mLM7ErHwDC2m6EJtfY3eIiZP88GYfnAwtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم لامین‌یامال و تیبو کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99516" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99515">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99515" target="_blank">📅 03:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi2xn7TvFn-e8-j7tzPg_43W8UV0G_5gpRwzDxAnye7eWV5VOe2WZB2pxe9ImUwzLOoTAQm_-rk_yALN3VobD6vFFqc9nOKICLOIqDkcD2P8-fZu3efPxb7JFqccweJ4gt8WNdV8hWRz7jlLDXtp1Mbh4tuFhfNzGizBevGYufMeuEDpkxRLpVyJEwYO9ZJ08q7lPC1A9rnVLMxp3z6KT2oBh4ekvX4Pn99_I4a_H7kx_-IXP45O_A3BZWNeB9Su0kUxmycKtFiBOClpRabt1MV9g5yHbEVj5Z7mLYLgSAhYgGVQvUkcvbdZyXzWLujyQgewhIZOeBnUssAEMUVzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99514" target="_blank">📅 03:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfNx7ANWIxc7-LQJuVidzlUbw432kkw1FeeFRackU15ymPtsxVDgQd0nPaAn34mCBPrfCUESjpzKVDzgRxd1tIIOtdpyMpwWTYJhzCEKEiK54cTznZsI8U7AYkD_eVDthbo1lfZT-aY8NbPBzaTrCk9Mn9X88xTi-2ua0mWJg2RC6ur7OfJ8cRDaFegq32y7Vk2sNvSBHQCqBNeYwmmI4SExtIAYsUIc-ECIqA3utfYheupl15zccaw1BbiO2Z-0onuggPWLCiIQfsO5XB-WKmY_EUd2RciCjUX1u9gOgejix94m1E2zw-CqVOSsZTeQrLU0R7l7Mi_KpPHVD_tJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
رومانو:
پاریس سن ژرمن به شدت به جذب فران تورس علاقه‌منده و اونو برای جایگزینی گونزالو راموس زیر نظر داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99512" target="_blank">📅 03:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pziDmPVadVDxwSCuJi86xylSPw9yNp5jX7jeCvdTQ3j58xePPXgOnEoubb2J21Z3fXAgQAxoH-TMF2xvTPWEm0aEGNoxWnZddOU9rH4HQP1SpFaQbdUzU0gZpc1RzaTZVvlG6-cBFJQ4heKz0220yBaOUQw87dniZURg4uwBy1oVldKo_9m5CZ4SFV5D-EUd5eb2bdLckT9q6ySNBK5whrZKo81B81AX_zHktSsBooTKiQDCMgHYVoIBUA-ZTs38HL3VitEu0ibiplP_4FJ0VH7Bn672DrJSTXhPqNpiNfN-8a5CziCWgELdlg8ig5D9tmMNQhUEjm7xcJMb5aK2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند پیش زیدی بوده که یکی یواشکی میخواسته ازشون عکس و فیلم بگیره بعد هالند زودتر طرفو دیده و از یارو و زنش عکس گرفته گذاشته استوری و نوشته هی یو
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99511" target="_blank">📅 03:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
گاهی پایان، با یک سوت آغاز می‌شود...
🔻
امشب فقط بلژیک حذف نشد؛ آخرین جام جهانی نسلی به پایان رسید که سال‌ها از آن به عنوان «نسل طلایی» یاد می‌شد. نسلی با ستاره‌هایی مثل کوین دی‌بروینه، روملو لوکاکو، تیبو کورتوا و اکسل ویتسل؛ تیمی که روی کاغذ، توانایی فتح دنیا را داشت اما بدون حتی یک جام بزرگ، صحنه را ترک می‌کند.
🔻
سال‌ها امید ساختند، لحظه‌های فراموش‌نشدنی خلق کردند و بلژیک را به جمع قدرت‌های فوتبال رساندند، اما جامی که شایسته‌اش بودند، هیچ‌وقت به دستانشان نرسید. اما بعضی نسل‌ها با جام‌ها به یاد آورده نمی‌شوند؛ با خاطرات، با احترام و با تأثیری که برای همیشه در تاریخ فوتبال بر جای می‌گذارند.
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99510" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN1Uff_9ILyiPEo7cw8ujHxsAYOIm22Jrz6Q2jXqKzuy5pHE5y2TacdxG7sJs1KqnUn7KrE0IADmk-O41bjodp9h9Z97_RW-98Mdhw3HCBZMmESU2_QFD9-5AlQ6JCCqNN_cqr1eIg6oEHQtZhcBC4utxJsODxM6-hIw94s3cfwngqahL9YUzbp6eHcZ7hkqHnrG1t_Ep8KvEkq9zlbLLMhWNR5-PZX3pIMH1kUk8sOUs76Qc6Nji6_2IcWwglR9MmG67aZU4aoGdisdpWAgh2YXL3odNSXNWGa24yeVl5Tipa2U1V6FU24prXMV9Y-3QorXi_gC3Ec6EB3P-3IJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99509" target="_blank">📅 01:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99508" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9snllZUUePjLsclFdwdvSXXhz1b-3wIudxBcVbCHPA76DE2dR1Y6yriWc2IFfGKaLxLuCY5ry5RvHxzHClvG3YVNvTS70MM_p4qxhXOpplyrOuAefn2G2EyHED3sfYzbTl648002iQytrlrfE7wkcZYggx8P0Qnm-vvoKjsp5bhPujV__iRWUDUYD2lFzPbTYZnUJdSXKlGml0aPEbO4HEHbgCkS039_i0DHuzjpO4xCAcTaitvnN2KTvxggwZx7Kd1KXoihU8tzGDQo_NumFsaGAJ5_SbXpnCYiB44IYqUkE4pZw4Q-Jtu68bEZRSnF38LLC-xKFMPnLl6iV7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
16 سال پیش تو چنین روزی اسپانیا با شکست دادن هلند قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99507" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLXN0HoXo9pLliHkqLdaEj8sK4HDbQCDVa-l7T1pBadMe_hvnz-ZnUDXg2DQLvBk54GQeVcadcSagl_mXzTWwa-FsqGesYecw3WjRZL0NbC4lM-_2nmQHizXfhG-HdimxI2StGXBMcIxe55xaf7e0OCip3UryzLA_UtIbaO5pL5yj2aXN6zpJdsm-LEZ07gOVsUMkrV5wRQi24_smt4hjoIm7xKPf8qqemP-FPCiHvxPzhmfIdV7XsisdL6efTJMfbNEMKB1MRA_DXcbYt56LPjka7A1_kDmqCzQYRpRM1-rSqjBc8o6Paiq5HhpEUd0fonoeijwXD_WDiO_YwLbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇧🇪
تیبو کورتوآ: «می‌خواهم یک سال کامل استراحت کنم و در هیچ مسابقه‌ای با تیم ملی بلژیک شرکت نکنم، و سپس در مسابقات مقدماتی جام ملت‌های اروپا و خود جام ملت‌های اروپا در سال ۲۰۲۸ شرکت کنم. نمی‌دانم که آیا بلژیک با این موضوع موافقت خواهد کرد یا خیر.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99506" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm_E1hxn6MrrYhYfu1tGX38mg5Itoz0eMhxmtAJcX3EJSOoylTQE0rra_EPYSBC1RHqHsK2bz2Gs-xoRPQ-wYNHIcFGsWsLTUIc0rnhY6jzAhHCBw4dRI5GQMuPRwOPhGuEBQugRrJ_O6scVur92Dc05hhfiv6HOs9OKGjD67CKZLiAWHnqAFNXaPyPTtRAjiTOgeYVAdqYMWsznKXephL-voqHcmZqsCJzEuv64zrWIQrB3uBhCScgw4RS6C0OQi9NJm4BT4IY8VDK4sHjzLWS8GIxeIskcpciLVtJC2Nn1RZjLP5ROXcc1oKmnH-ZNbVXAd1f96NtLnidxppGQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🚨
🔥
🚨
🔥
🇫🇷
🇪🇸
لامین یامال:
‏فرانسه یا برای بار سوم متوالی به مرحله فینال جام جهانی می‌رسد، یا ما آن‌ها را برای بار سوم متوالی شکست خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99505" target="_blank">📅 01:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99503" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqpNpKAT04G9W2yWGC95yAwcvfvDx7Q7EX7OaTJGXLcfW4IFUJt57OnttByk3Eyyjrwe7soxNJMi5znIIeIhMQ1eXD1w7g-N_TgFRiRIeX94uVYn0UCl6Bwu3SxsdelfAsgcRPH1yyhnyueL1i3b_bWUSLhdTkHuRIhJ0D_M1JfOIes05fahsfigqKOYwATPuzLjHl2irgzQ8Y0J-rLN-xO7wUKUa-8qM8mzQ-b5uy7ebo7X0vhu9Mw7VMyHT0VtWlE0Wf1pTaYpClBxEpM8b10vvT0W9QG3zyszPoIwW5pzHvDk2ZGeAeQPe7opam4wiI8n6m9rkgIvrgwhGKf1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
استارت رجزخوانی لامین یامال: « فکر می‌کنم اگر فرانسه قرار باشه از تیمی بترسه، آن تیم ما هستیم ، چون این ما بودیم که آن‌ها را حذف کردیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99502" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا اینجوری میکنه
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99501" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
MOTM
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99500" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3hGOt6vt2ATwBWqHA6PwyQcmQrPit-5CfjDvEvs-GM_K5N50vmtpb1JCX0LRCx0jeigtP1QsgRMSn6JIBXGrvlCLPKhyaK7WIUyGtbt3VZt1s-Q3SwWBtQ_yyfX7uijB3F8tu2h-wCy8a_OjGU5RQ4k7PL7FTyI8HNXv6lFZ6YCaLqQ-DoGTjj49_dETF5FhC1VSM5ljEo6CRtL6xWlnrIo_w51sjHv5JIp8VHhsITGzq_eEvinTp7x1We0cl3PiKWi9uZXa1LiDy3AOdxvJlxGZFjW3tVYESdhIy19WYjNqW7DM0jFTBzbAnT-mnyIuk_rZKjDbGYHxHx4bntyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🤯
🇪🇸
فابیان رویز تا به امروز هیچ مسابقه‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
📊
48 مسابقه؛ 33 پیروزی؛  15 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99499" target="_blank">📅 00:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99498" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQw9-x08b7-dzCEsaYxfWP3vV8-lj_xKmH3Q3_oq77AHVfSYtGUWWq88xq8fW5AWtUS9PGLwvmvGy0TytnnaWHHfs03r9nQ0nCxF6Symn9vRRF2M4Lr3Q17ewAWiq4WWa2uNiriDdqmhCgQ11QaqVhb6sTkaZS2nBbNqDmRhhxhvOU-cUMmrS7kao36EBQnPaaACqIog9V78A4y0N_mrNhHSXdbnoNb6np7rNXk31lZ5j8rArKbTBG4XriIolEj-s7gd1_gkE_rg-O3sLO5rv3LGya8qUtZYxe-VNgR3i7PfoXx3jkSQywMMiILpF0C87yCd0NsvewLLS9VldOGQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
اسپانیا با پیروزی در این مسابقه، برای 36 بازی متوالی، بدون شکست باقی ماند و یک رکورد جدید در تاریخ این تیم را به ثبت رساند.
✔️
‏آمار این روند: ‏27 برد؛ ‏9 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99497" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99496" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99496" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZWOSisUuQFXXlIyBXUs34SLKCDjnN0ewF1L4EeGxp9f-gRf_sw10GqVj1_7BRt_Fiujqje9QgZDylzPHe_F1MjenYMufJZPVCdcrf8u-76MP2cWMDb3g-9Oru5GITRN4jPkMLOxq8qXHq-mA84Qf9XxdttZjgMbTuJX1goHmqLadendVWNlPCH_x6cdenk1XM-xAMvboJuSpv5tEVOc7qtLAbl1vvNRbSSbiR_MPoOSFfQ9zkQU-rnMc4Q75ZohmtD_z8653qrOZL303XtPWxoOjcn6Xs66Nk65bPmn-OeSXbeimKjiFbMrit0UvT7D-Bx_2qZt-uPDQdtJkNFeEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99495" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOjMWq2tf_H4_Lv3fDjBLZ5VKkfZNJMtos6vfHxyPgNFv3i8qgKhmj-O4wJ4HXN7KaGc01kMrXbelCN3buuvbDJnLnMlZGv-GmA-WI2r5uuC_pyi68V69SIiTkCBbsFru4mai-Z-JfB-G-pWcRkA6G_1t-YSQITteN-DUL1BqJ4PhkvwuZtWXpiNq-DVjgkVUSXRPYevG3Dfp1lzzXIF8SUofhrhWUHfQavuUPuy-054vK12_twlj0sVqAVYCTY3Rne0_MciQhAVqcTW1vq4W3eqOFlq-eORRSsH_Eri7PNZbrZOVsDAUTdUulyCJ_hULszm9BbsIuJ3APjM_nvfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
در 11 بازی اخیر که لامین یامال از ابتدا در ترکیب اصلی تیم ملی اسپانیا حضور داشته، اسپانیا در مسابقات بزرگ (یورو + جام جهانی) پیروز شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99494" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ دکلان‌رایس، مارک‌گهی و ریس جیمز در آستانه بازی با نروژ به تمرینات انگلیس بازگشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99493" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGC_1qtbeUkckq6-wh35rp1R1xTimI_9hgh9Ua8944CLtGPbJfbQ1-lNGTsN1WzRVbWvond2FSpWo-uC-Xbnh3N_wcpvY4GacWCD41hesbkNK369AlS_MQdqSenHMqQW_zqexC_91iuw_x-AEfGyf6o52EkOGYqipmKcWxa4DYbpXHdQ-UYaXLks9ZDiR8W_Rln0o1bPkCpebQu_SzFoA0xRGCNgRUvDBUA4ulxeEO1bMOLqCqBlvw-NcHoRUO_qmCTkq2GXfFh25-6fuVQdptSqSMOwDVOlN79KI3G97PAJbFP3TnSDhLj8C1Qax_NVu_4x29bq96WqN4lScP5t7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99492" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bajbo-_OEVpm1SOc9t8QExwmwNP41gQb1v4-WVqK9wmYIsuLfPk-Nuil_dzMZ-2ps5l0FYqcXgIX1OeANgwoKtExr4M06cGDQV9rnaprVoThS1vA7YKK7e_KJZq8hk9bLZxJ0le9dqR_X4vsOlEJnjzU7bONz33UGikYZNvBpsPyU3uxoIDh854mQCPpeq8HsDB-1eZZwYKZjnX2N1aDsOwrnflMpYUEIQnDLr4Mt7127Db5uwPel0rm21rck7gUmvA7n8i9VBKHcfUUjVjZB28CHvMFC-jQ0aARtOXgcAz1ZzHxMZK2kHZvOMk-cjFSZVZ9IlrvBfhhfq3I05OrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا پس از سال 2010 برای دومین بار در تاریخ به نیمه نهایی جام جهانی رسید
‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99491" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aS8ShKb3REDeVL1b5gMRxCvbt-cHcwyfmBkPFMjkREoRaUc7I9ILmqpf8ZpWN2G7koHqIRC6QRKu9gTJCNLB4eexKy8x7jv0V_wiDdRGfcHtu7PYNGXViuKNrU23aJcuiPWs2urAHZyLyNZ5cpkQlK0ibt1JOgChlLTphAPZxSPSy3m67WPZgTKMWKUSSPuUvWnNQlBvAVL-xdZXo7EVH5qW7rIx7u2MeCu_BmUqS0l9xG0X78o1WXgm_P_iLS3HubYpcZSieRDu02kKrKUATf6j-SepTDYzCYyH9cOUxx-3KtTJOtnnHxRN4KY2Z77HFVA_kb461M7IixRx__hCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlJ37RLbzma1207oUkZ4a4hnkm3wu9ETxVJBnW-ICSg2Y4SNcAmYmB-9yg4ryvA-JFLCKLKYLUU0BIwoF8H53qCU0_LR0lgSD1qoeOtx77Do5yTrbt2zzS5OQPHJKWMySIv8Wo5XeN_s6Pfr8MKiR74uIqLGzq7cJ1TbXli9ue-hOkdNXGENOYap6WTWaFtLIqG_heZ12TL5FwPCUZhF9KAz6j21eXmmec0k6dtKvr4Rvs7AadDZSM-U2UB0_K-lSonu8o5dKfDa3gFWDDxrk0dEhkIaQxPliJHanGO5SYdrix7gjII-_35jVM5Pj_7r2qMILfDfxgv4632MgCO4Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داش یامال تو استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99489" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqXbkVSsNODsZDD4ps4UAIA1PEUhYSA_-p_zkzVfDwAEAl4m-a-2Yltlc60WRiO2pu1QKhd38KReuNrQ8PgsEwB33uybRKJ0LTyRPIf6BhnKwT_QmRjnkpNVcPJiMxhN5gnXlVwwbqf44El7U8pIQdvukYKNfj6amqsJ4IJ4kHrUxlxjalnS80ZH3AkqNa1LsYw1BJp-bQkaXVkXvZl9yZ2hNGVwNDwoiQAYDLvGLaZeBZ1sXsxvyKOUSzjStEQMSlsCkbmw0SqbtrNnI-X3W5Vv2TkYk55eeBjdcqopXdrGp_HBLnxwSrcWtiFhlug4bxKDBlPFBiE7A5Tk7nLOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
🏆
🇪🇸
آمار بازی امشب بلژیک و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99487" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnyQ_dIq1Vpf1hM6K8RYA7iiHlzyxuImXHu0CxHSq3o-04m6WBdQyRgIwSdz7coihDD6Xzd0Uf_rIhA-vNj2gfy2KLWmnZWuYgxSSyOAaprWotwZUWqdnhOx80JQRsERVP-2bqdE1jdC3F6L6q-SyE_MujJ8g61bypnRvyhc1IteaA2XXn1nH-v6jwa8CCBf0v2DtIcvQvlYW48fY9rL3vNP6mL9y_AOSYDkxlTA9xfa-mvthwgm6bZ7ReXzae8tMsGEtjw98fuAj-rmOhwpKoPEhk_PPWMToesxlTwgo_2PHsiFPcXvcSVcoMcv0JlBYqux12zMRt4EbSVZMklYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار جام جهانی؛ این سمت که واقعا جذاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99486" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYbQsajnCohoKGUP--80-DCyTsjRkKev3ljjry0uTiCta2BYcXiAmFpCTqF1QC03xip_UunEbPwAhzUTVzeBMm-_V6FZ3Nx7oOz-Qr7YDN8YODyHOg47_axVyZbSUyWy8JY2soYwdvKZZTVLCNhaV9BDwG_XEJr-cR7Z9crmOOjoWhcOeUtehNu-R8hO3ct5Fr16QCxIYlHdl7V7JhfQmvj6OTS0uQ9zt4EaKR0ref7p7n7PmuyA56756TxVktZv6HHomp-wpinhUMpFdzIy-arEB617uMiJURWbT6ADAEvpWsHYrwyJdNhprQXWTUW47XNz1sDoKuMfUUaWK1G78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99485" target="_blank">📅 00:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs7G_XvckzLrOZPomnwH3Wse_fB26wV5i860EWxTkB8pPx2NAdWWjly6ZwoyqYOTR8JtgQaOJbwe0bgb41g7HRNQRxMXEzQfQCpoHRp2Nfk_UXSlhPOZMcLA9flyry3nIQ9oyMgH_ZO2y6QQG2iyIJ_PsczDB5iznsJFNG1CE9-iyZBBenQLiVqm18315YD25q6f9r6o5GouRlY9xFuTz1w6Np3-LQlQujsunyP39Be0J0NN8rqL5LkX015V-r34Czp6lL3strlrWjYI4EuDOizym5AWBm3djEAkJRu-5pEifFVJlqosjHrUL3TxjFVTJZgp26MeNW8M-wacs5i1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99484" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0gbEyUOYEErl7BKUSERFmMN7qvm3w1lLeqm9VWczU_IPjQ1Ygff7sCUj6518gCNHQf31hbdfHEZOJ2Jj0FhoDtSWajKXCnHOnQOlDvAuIKbjwKEdg0kTqEdMW1KNy0bey7DI-WKqrVZUAqhWdUQr37kakSnoqlrZBvwVOesSu2NHohUFKaP_XALCDgseMrbkTRuUSBnuABAvN0k1d9B4BEBngKHHfHPzXXlJ_-DVa7KSK4ywDk54nK17CWlGKw6ZqecHTFt4i4OKTvyKYeHK4qZ0LkLsYzDw-ktJZj4iGXBDGqMyzW1PWZO-TlTsV2GB_WXrHPlZpNJ1BJ2eGsjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99483" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پدری ریدددددد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99482" target="_blank">📅 00:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چه توپییییی در آورد لاپورتتتتتتتت</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99481" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99480" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هفتتتتت دقیقه فقط تا پایان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99479" target="_blank">📅 00:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بلژیک اونجایی که کورتوا مصدوم شد بازیو باخت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99478" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XGxNgGyWrgFA2kDrnO8KV8iR1ysqttE4ghLSG5yRuVGiQ9dHBFEm3KYIwk46myIE9DD2OnrKFEgSpDf51agLAJTEc5AvnGsFzJYtlqv3HjpnxSEhJxg4FG27O7jh8TOievHm8xWj2e6MYUiE6tLU0VHYX_4ddvFgFNbV7dv6nsK2j9aJEs2jPfEhhhfe18Lp32KP8huA2XbLyA1rWENczHZSooAN9eu7IAGJflcLOpqikeF0zuO69v7J9X8mgnhw4e1QKbyE1BxKA7rVH3gZPswvax07-o66PF-K23OeP_bN9XqX8Q3oVdESxFsy2iB_3BYaGuodkNZLNo4yC909DU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XGxNgGyWrgFA2kDrnO8KV8iR1ysqttE4ghLSG5yRuVGiQ9dHBFEm3KYIwk46myIE9DD2OnrKFEgSpDf51agLAJTEc5AvnGsFzJYtlqv3HjpnxSEhJxg4FG27O7jh8TOievHm8xWj2e6MYUiE6tLU0VHYX_4ddvFgFNbV7dv6nsK2j9aJEs2jPfEhhhfe18Lp32KP8huA2XbLyA1rWENczHZSooAN9eu7IAGJflcLOpqikeF0zuO69v7J9X8mgnhw4e1QKbyE1BxKA7rVH3gZPswvax07-o66PF-K23OeP_bN9XqX8Q3oVdESxFsy2iB_3BYaGuodkNZLNo4yC909DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌دوم اسپانیا به بلژیک توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99477" target="_blank">📅 00:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مرینو عشققققققق</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99476" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چه شاهکاریه این مرینوووووو</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99475" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگلگللللللللللللللللل</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99474" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگللللل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99473" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گل دومممممممممم</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99472" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسپانیااااااااا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99471" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مرینوووووووو</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99470" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گللللللللللللل دوممم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99469" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99468" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مرینو عشق پرتغالیا اومد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99467" target="_blank">📅 00:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=pjbjVISQejHRto4x8zm9UteYGcuQfqLTgH99IMPEv2pdWzyS_7brYjee8FiJg-_ZhgnpOgdi83TR2fdqY0qyWB5seU2WXHNYj9668yh4wB_-GAJSw2nCswUMseUSCe7e3og0buqGfr4KlTbfVOD0qfub-zdkgyRMwovLDDCpnqPqxx9owShE_lvIQFAj3Ao954uN05G6io92PLJ_8WlfRsBEkSRtZaUbBb5hW_7IHZYKLRAnyx3AvzYdGpbohqyolC9iTqRDD1h4QWfCbcMGLfW8qqDUKJF2XOrmM6oWoeMZXUZeDb5iedbys9_vsFMq7DSfhuGrnuWPyrEmIGbfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=pjbjVISQejHRto4x8zm9UteYGcuQfqLTgH99IMPEv2pdWzyS_7brYjee8FiJg-_ZhgnpOgdi83TR2fdqY0qyWB5seU2WXHNYj9668yh4wB_-GAJSw2nCswUMseUSCe7e3og0buqGfr4KlTbfVOD0qfub-zdkgyRMwovLDDCpnqPqxx9owShE_lvIQFAj3Ao954uN05G6io92PLJ_8WlfRsBEkSRtZaUbBb5hW_7IHZYKLRAnyx3AvzYdGpbohqyolC9iTqRDD1h4QWfCbcMGLfW8qqDUKJF2XOrmM6oWoeMZXUZeDb5iedbys9_vsFMq7DSfhuGrnuWPyrEmIGbfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99466" target="_blank">📅 00:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN8MJod6E1NEcBGBpSDxW_5HoMYL5d8fbKwEmXqBEZ41c_AohbkpJtG-1sGXHPKwsm_o45bxHLeRntGcfSykNjs3RbVih3DOuHMqrGGJ3hgqhHOhEYzsNhOcZA9z5PFU-CpQBq-c0EgD47ip6U_qQ_hfl24KmBV6GxmfXEIRbtP1wElNYG5hZHaVYCqifuFGchRmqj1dexsEl-XuFK4Ycu5zA6_7rcVOX19YW_5qG9MuaU_2LFMebIM9EPgD7BhY-WvrOg1t5f6GPh0CJ4Hdvgy_WbZDa8OHzNOS1xNMX3Mr2NYfUaGMxvBVPwQtWp9lwriYBv_M4Jitbp42L5NdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های شدید تیبو کورتوا
🚨
🚨
🚨
🚨
😐</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99465" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کورتوا تعویض شدددددد
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99464" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دو تیم خوب بازی میکنن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99463" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بلژیک چه ضدحمله هایی میزنه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99462" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آغاز نیمه‌دوم بازی اسپانیا و بلژیک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99461" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99460" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99459">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99459" target="_blank">📅 23:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDzI9PTcCvDiLs4VHsK0RRjOuHFUjxqYji5bo_n5cOfK9o-ZVPCnG7fFgB8Jyi7UwPPB3ewnLpTZa27V0Xux21WcSbxFfvXuTeyFYHl-m7ZaSloErak0hQQ5xLprDgWY4SfFkibMILT6MyTBDr_qh4DgmAG7DjgQZrLQOV7a8bPHUBGnOb3iJpc6fQZ_qBuinTjn79ncFxXmV4GsfWBcG_1PFodmMGO1qrTMtTtlBnxUyKDQeaReJeeVMuk-cD_SYpi9HpJrtPpXjEId6WKY0Gx08o654FrsKGXsVBOf4ugoJEuf4GRx620kh7tfc9UIq4KS4n5ksgMrHt6APkggNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
دکتلاره (با ۳ گل) به عنوان بهترین گلزن تاریخ بلژیک در مسابقات حذفی جام جهانی، با روملو لوکاكو هم‌رتبه شد.
🇧🇪
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99458" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 بلژیک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99456" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🔥
گل‌تساوی بلژیک توسط دکتلاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99455" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گل تاییده و موردی نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99454" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه ضربه سر خوشگلیییی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99453" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مساووییییی بلژییییک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99452" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99451" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mycia5TNNGungOTDd6LvJJzsj9BA8qnUImJi77NfoUommcE37oRSte-W2DhrIgNllWI_i7btWzuVQ_8KS9qiq1-tmMgX7g3ehyzSNBpbGsNkAonsWUteAKrfReQv8JfMCth-6bgXpMqpftAVwgo-ULkYTi_p-tyLRIWcyh-XqndYv5V9NfyZQz5ImOc7b8btASVDOFxkPCRryTk3nlnArVXj0apY3tKZrNd3LW1kquftl2zFuRPsUVpO8SEwmHxRY51i8QI0CpaxD-R8Ps5n5oQFTbRQmfbYBznQdCoS0POMzhtrdEJRt9C6-gKYn_V073Opjal1CfkHtYkuOhAYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور برد پیت تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99450" target="_blank">📅 23:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خوشگل سیو‌ کرد کورتوا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99449" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چه خووووب زد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99448" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99447" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چه بازی ای میکنه یامااااال</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99446" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یامال دفاع چپ بلژیکو کرده قشنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99445" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خطاااااای خوش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99444" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🔥
گل‌اول اسپانیا به بلژیک توسط فابیان رویز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99443" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسپانیاااااا فرانسسسسه داریم نیمه نهاییییییییییی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99442" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ببببببه بببببببههههههه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99441" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بالاخرهههههه شددددددد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99440" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فابیاننننننن رویزززژزززز</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99439" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسپانیاااااا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99438" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99437" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99436" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3yj9GBzN1CZWbABwPMc7tZBXPLvFUqUj8xNZALNcHQjCp4Hyu__ioQLQiRayGA_x5XTzHPsLlshUOJq9rP50tuuZtfMcEDJKeR4qhdwqde8DT_g03XnLHi6w-KJZ2wnDNGD5R98YdOLCLD2fiGM3muMdWZkOu5YtMJ6CwOUYOFwG3fuUR5tJPhKtVVDJF3chpldg7ck1BLYfAw3kMg3ikQ2QKwo9Mkrbqdjms1ZxAfmq92tMI3Tz8g6mmUTdvp2d_bB02b0EejKw0jh2OJxNfpJse3B-FHYcLiMT1r13jDWsXppCGxxISZwTsGOpb-KFEWxLQo03wHOsVVFcs5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
#فوووووری
از آرشیو وار: پنالتی اسپانیا مقابل بلژیک گرفته نشدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99435" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHsFAip2rxfYQ6zH00asltNua_CGOlfEZKrZl0LJzo5_n60c2wwS0jEjWXc3jLnhUaoH2ax81EoHJFxhpczLPdjCgj5BvqzVt9bqR3wf3l9_O9CGy3ik4GSPiyuOX9sX7ObyY0ljwOwkvz3HnZtH9ouIB0Fylsinx8VIB_vJmHZAgnxSQ7CkEv_8EXl-4GLm57EUNMvrZimt3Z5bhY6tcnIoNDzVUKw77z2gIlAXQ2hXwSHTGmZuFc8pzXj-5_KmsV_3v_d-VE05iyK1OMID6JWYSio2F2z3ag_14i5S2crME5frQno44XN_MbEcm9x8iUE4tSzDLME91qmTolBMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پست جدید رونالدو: یه پیروزی میلیون ها میارزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99434" target="_blank">📅 22:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAW1VqK7X4WlGdpPHU5q7tO-eNXWMoD6ky2VkPHh0cfQtKCHSfdbQ_eF6stAB-_-1aP2c0aHOyrBqjECSvfus2qy9PadANvg5Dezug5YZOCXbvOFTW473mvsnqHK4kBMdQdHl8DmLbVHwFMSSJ0ZjrtXEBb923swoKXzUIiRlmV2rvoeJ-o0eTa_Ddp_m75XqnojRsxBYUK7p_WoUY_V9VgEnMUNu5DoDuCVRZxE8G_dlEMRXAjVEU-XgrRwj4hGa2k-yABWjTgE85azyV10Q3s95dwa-3IInros5VvJ4GKsFqdD3UeBJp9shf6-XQsEhf9Jt0WVA_kvuEY0xpcoIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر یامال تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99433" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bet_maxxx</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99432" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDQBNBYtWHUYylmpb-RVxVI3TV9bvwlIZG4-vjw2bEPBJdTnSyOnMlb3VglE2T4pdTbFhhzljXw2vQuetdy41us2t6o-cIg9owrq-FsI0tRBfJSnRwrgQil1Ok4zlGJks2D5XLa1qoORYMoZMGgI_7RYxKhM_Pl0q_5gzZuZnTzPZaFEEvAFnqd9rdC4XiGnpUjWghLvRSUfIC2z777JqV2vM2pCLBOKcTsYS-FpF0-B4VjgjYLRSxoOUw35LWets2SCDcpa7ay9Ys4N42Qr6JqL6S6h9xgpdkizZqt5OLhrQ89nLXe1YIcRwTfwJshbKaHv__J5V8V6zjDkptx--w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99431" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بریییم سراغ بازی جذاب اسپانیا و بلژیک
🔥</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99430" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇧🇪
ترکیب بلژیک مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99429" target="_blank">📅 22:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bepeWV6ro9-k2hED-c-PVvFhw6YfLFM8jRjj-ShzoaTYRBE-ics5pk222Oo9wTZXQl857pAWyHIK7UDTYvAVAigWegggrE4-zby88MQbfT00LOyEb_lIh_4vw8hdDGlgJMRoeHjUFciG0xRhXCbh6-cU9_36Y1O-VhfJ1t7bHKxR-N5uf7OqHwJBMEHtsJr8F8jWZSPiVgEDZCZHkNCKjqlUXnwf32NEnl2WABYNDOCjBcVWk51VxFFRtqBDMZ7K_SqNQVVb8eDYeu_5irXmuJqT03aaBS7usGEGUbwRFIWuaEq8sRJDQrG2_fKFpxy9tvQ1_qyLjXLDDgzuNFWhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به خصوص آسیب غضروف مفصلی که در فصل گذشته (2025/26) رخ داده بود، و همچنین تردیدها در مورد سرعت بهبودی او بود).
تیم منچستریونایتد از نتایج معاینات راضی نبود و تصمیم گرفت این قرارداد را تکمیل نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99428" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h55RwHnMSA1skw1rMdhFhfjwjajMnAPauGMMCbg2PMg6yrKPryT_zPiVz0l3OoZrjTBu_jqlcswoFBy6aGv1mcxocQZ6iSzZPnavAbe9lIyvs1FNUeAXXNaAU9-2zTDVE5I8mKxY042LcH6OpZ-X5nA84FUySubCSAPoV0a4siTR1u6f2ovgBjo6Z49EWTjKfTo3Rb1SWMAJljKtiaIHqQedtKw9h5-WQZLxhcIKF2hB6CFO114x5rjOWOh3LIy1S4t5bnptdLzXmrfgX-tIJUG0jg5aP4rnzr6woeNnIAqw-FKnUhRo62B2uwrOcRJWj62tedYp-_EKPO9u3Yu7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
علی‌تاجرنیا مدیرعامل استقلال در آخرین صحبت ساعاتی‌پیش خود با سهراب بختیاری‌زاده اعلام کرده که پنجره نقل‌وانتقالات آبی‌پوشان تا ده روز آینده باز می‌شود! هرچند به صحبت‌های تاجرنیا نمی‌شود استناد کرد اما باید تا اواخر تیر برای اتفاقات…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99427" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99426">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=lJEi2eUbhyBcISbzRKqLUiG5ksEDfR2NTiERZBOtDRffa0MJfyikbQ1Gb7kh3NHFNAR9h2Ms2OPugtXHEZ7Otmx6hAxY0VMZChJRzu0ZYkib1vyTqRJfHxfeqv-_3gdH-GIUBtRQE3S43Pu0wgG7P_iblvdvJuq3Ze1-KB19N0OnfYBknm2p0fajDOGerYPFJSoF7yJMzIiLa1V6Vqld0QidnytiVH7bZyI5DEMaFStdu0tqYtp0h_kmddXxVzUtTrk2y1aB-T4OFBoABRnUoirmX0jzY1pl0vnWIQIzGdqBmBH5bHTXohiPYqii2uQyRbhgTR6oQPuJdXg_hx42Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=lJEi2eUbhyBcISbzRKqLUiG5ksEDfR2NTiERZBOtDRffa0MJfyikbQ1Gb7kh3NHFNAR9h2Ms2OPugtXHEZ7Otmx6hAxY0VMZChJRzu0ZYkib1vyTqRJfHxfeqv-_3gdH-GIUBtRQE3S43Pu0wgG7P_iblvdvJuq3Ze1-KB19N0OnfYBknm2p0fajDOGerYPFJSoF7yJMzIiLa1V6Vqld0QidnytiVH7bZyI5DEMaFStdu0tqYtp0h_kmddXxVzUtTrk2y1aB-T4OFBoABRnUoirmX0jzY1pl0vnWIQIzGdqBmBH5bHTXohiPYqii2uQyRbhgTR6oQPuJdXg_hx42Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیتی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99426" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فکر کنم کیش انقلاب شده خبر نداریم
😐
@sammfoott | پروکسی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99425" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3rly1OOwYtNM__5wdVWyJesRGUATwhH-xTvfvEYDF6ISuDHlPfLvFG7LZPCEhJ9peNdYyCBco2JeDOXWChKsg2kLAQcBomP3RNiXfIMKQB2tJWN0hRtZp_VKggS0qm_DHeuhVXwr_9Ei6XM9qy7rLJwkO8MJL3fNea8iEaTTUH9Dk2oLp3OHZicgN4yehVcLb7DS35xcmLw0kCTDYePWPrCVX7J3h4h3QlnEZGNXVJiNN_XrN-YwFeYobCVR-hYxpIZ2Vgxteo5GPmlipcHi_MhsRl9C60KHHGcGb6FBu_Hncrm0sCnNIJlMXwW-T7cdWE7btxGoAXC6-1YVvGdhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
هدف مورد نظر بارسلونا همچنان خولیان آلوارز است. قرارداد آدیمی، تاثیری بر تمایل باشگاه برای جذب یک مهاجم جدید نخواهد داشت، چه خولیان جذب شود و چه نشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99424" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY0219tm9zDvtertWLQV2LxEyCcGPvBKPMRlDtg-4flwnneaPkoLrMPpl1OlhvNfildXDCA0MJcC9rouMmvtr5mxxp4wk5fLRkT6vqhp_AclOPoL9kLoJFlKtAYYtrD_lJ2sR207kxBk0S8E2fgXKbNi48JjYPkBAA6uf9oNQxl__FyomDP26bT1_hqedWnTegOY23CCAnUK2edMt0UDzly_bFksb52xM6EbSUuu7bDDH_rx2luffbEkBZ6FdshbAdDij_TBdND7gZaqiyJ_oCIJcaZOd5Lp4b5iEwdF3fUYOyKFuFoWHOaT3Ekbk7Rgkq2zVke78CsaTj2gZeBpfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99423" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRy5hdW2qan2ov_n5dDQr3aXENXTDaqaKX62Q6dECEAIvjHlnA4LR71ANoaoSHge8ffIXSB7r7wQCsfJJoaNJJ0lD4WA2EAVS32AxL0lhGxw7UtgkrrszlcExSUbYfmA62PUFLmew_fHTHCXq4Sxp4JGH-zqka7i6NWsZNnBc4fx-JtaXmCLGNODHLibKLTI9XfhdjlxdFqFz5mMrC00lkn8OQvL6L_AVB9ddpqs-Ek6DISkfD-37QcPqr3pRWl9DXKL7RstRIuC_Bq0hJESdxppWs93eJ9lFoottVrhWfb9MK2uJTMJYN3wB45DQME7LjCicp9opNQVYCa6R9v69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99422" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=WTaX6wLnTcYyUpm1y4KbTqjX4igoYT0phDVsEizi3NMVkIJlENj5tkgzKr2Hy8N1a_TH78-c73xT82BFM3BRGhO-p94nwQFiP1U9a-IXd1EEj64VXQ014f1Dm5FluEK-IuxfI18w9CWXFwOATF_64BSQCqTJhUAdIj0FS79n9b5AAtdjktgjkkO7PBfbtH_HaYT7bQaO_Mnr5VILGcIUHAc3pwpr6Fj5dIn17gZgVe5Dc1KR15b4Uq8lBYMsjI4vAi7jPrrdMFokfw5luJazB-MkaxsekPfVh0OfWcADJyVHIxYifHvmeoxB3savg0yai2xgqggzprdpYcpT6D_Pvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=WTaX6wLnTcYyUpm1y4KbTqjX4igoYT0phDVsEizi3NMVkIJlENj5tkgzKr2Hy8N1a_TH78-c73xT82BFM3BRGhO-p94nwQFiP1U9a-IXd1EEj64VXQ014f1Dm5FluEK-IuxfI18w9CWXFwOATF_64BSQCqTJhUAdIj0FS79n9b5AAtdjktgjkkO7PBfbtH_HaYT7bQaO_Mnr5VILGcIUHAc3pwpr6Fj5dIn17gZgVe5Dc1KR15b4Uq8lBYMsjI4vAi7jPrrdMFokfw5luJazB-MkaxsekPfVh0OfWcADJyVHIxYifHvmeoxB3savg0yai2xgqggzprdpYcpT6D_Pvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
سرقت‌ گوشی سینا سعیدی‌فر گلر سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99421" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olkAoiQmHqjmgJlmFfYsi6YdM3BCQkGE6BwlWDnoprTRu0M_SfgU3v9z37aEbli9cPq4fa4X53zV_jDk5vDwETyfQ5cfHJz4OKSpWXBQm8Xpli_VMEFXc1FFmZfxBNdpNPGRmvZ_TMHsW4OMabFiBzqW93eWKfdXov75JnqCHJpxbVRmW2i6QuIZQLVGXaXd-sntIUxmRyuL9zGSdPriXrwB7DnWTbf7GJg3MtM17LHKVMOpDo1kuXWo4wA0i2vmU5qh9Cogt_17qEr4rh9MLoYb5eIY9FUTdTMy-Om2VYQ6bsomql5XXEQA3VEZHOlm9uqaJJNdrra0OBdXY7yEuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99420" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKQM8OrTXEIn5Hd2cHwdGDPAYkAadS2usfFzL4EKCrYUZA-pFOj4Uz-cL8B8zhjCfVimX3LlrN7gDN4Nv7qoSKD5Bhq4WzWnhMAwVjszB5T38Yhq9_FT_613nIJFO_zcyOVGCat-vwNIHLmQtMTpruS2CI_H0Hv_VUg3kId2cuzJz5FEN_4XCYTFMRUaQqB46AwN3eMZ9EWuY5M8Va6apiMPfqRVVkgcYRJL_bF4Nvh2-neUpIWumjFnnUXzP4pmVFnlKYbJIseJSxVj4d4oDSw60Jip22E0DkgYPnu96gQ3jDap9qOV1wXCrUrYKxVAwE1VtZ9eRTpoZDapdUx3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
👤
استوری رامین‌رضاییان که تمریناتش رو بجای حضور در کمپ استقلال در کشور اسپانیا پیگیری میکنه و اعلام کرده که بزودی اخبار خوب در راهه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99419" target="_blank">📅 20:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HankeB6AM5NFiMBsGQAZrHUjV6JUFuVsYzRabjUWbBQnfciBr9pWl2t0-2xen4G79cwa6onGF4VRe_20kyRraRYpKRE3cREq_T4lVL9UZaXeDuG7bhvn2ziK29yBZw5DHM7RzCT7L1fvFxAFmp817DATCfVnlUS8MUbPNfKiwuNiH_Hmx_jZa1K79lzwe7-YxihbIC-t_fo6G3lb4QnIsFhygQhMiVcMWJj7wSZTugevzVZ7MYQbOMmAjvmB0V9neBssfd9QbjrjpbdV8uJSrU4PoXrByTU29YJFxWjpyqAIKyOyin8TOe8jHOTs49NTJH7V2Re0ufkRHE0uXrmMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مورات یاکین سرمربی سوئیس غیبت یوهان مانزامبی در بازی با آرژانتین را تایید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99418" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
