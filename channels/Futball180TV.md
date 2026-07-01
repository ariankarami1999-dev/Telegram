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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 666K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 20:12:33</div>
<hr>

<div class="tg-post" id="msg-97396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">داور تمارض هری‌کین گرفتتتت</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/Futball180TV/97396" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پنالتی نشددددد</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/Futball180TV/97395" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انگلیس داره گاییده میشههههه
😐
😐
😐</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/Futball180TV/97394" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97393">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کنگوووووو زدد تیررررررر</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/Futball180TV/97393" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/Futball180TV/97392" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 319 · <a href="https://t.me/Futball180TV/97391" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpWOFkzC-mYl9jkVn1r4dI6BlAL7OB-K4e3XGGSZuXN2q9plDYtVFSshbNLEtsSAhe6e80gcK17aoTTpn0agMmkgV7YrDb5COJvafr9SDuWTQrVuXeJsNP3Qj3PJWYGYBCD9EqxyyCN-Ud9rzo4De6Gvq2uFiUxExCDSvTI4i1cSET9bDPuF1n2hYBMhQY3x3p15unhZLrTQby6xqS2W7lslGYOtfxUEjGL-NcogA3O-_QZLKt7Y_w3C7RGWTI7UECjKbOc5oGr34vSfpcYGRqouqqXqUKDZfRAXDXr4XeB5eMlZ9OrWzBKd4h8a8XceT_V6fRvNUPlsF2zngq4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رشفورد اینجوری ریدددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/Futball180TV/97390" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کنگو خیلی کیری سخته
پرتغال هم اذیت شد جلو اینا</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/97389" target="_blank">📅 20:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چه تووپپپی از رو خط در آوردن کنگو</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/Futball180TV/97388" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/97387" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کارت زرد برای بلینگام</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/97386" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این که کنگوئه اینجوری حرامبال میزنه حرامبال کیروش دیگه دیدن داره.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/97385" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O15XWCyvTF2HwAj6KXuSR-BivwY3IfI_wGFzEke3rV6W8VUR4H6nOaE9u1R3l-RXTpc3-YtDPue6ypg3X60Gp36D5BIMatALT5KIh86GJCI3IG9y-qYsKtksFPBBZ3oxspxDzBa4LqOqjbirWm_LYk-G4chJ4F0U54Coy23ccyv9BTbolHhqz_S3jCK8Ak9xViwQiLPkTlSBmZhBWg1S0RZMFI3Fu2dWbc8UPydHD5WTK_i8jaqVpFchUBZgcWMXV1_qlZVzas6kZkBj3iqDkEJKoP1trfi4k5Pa8epbLlEnaIn__jE8vjulDFoa-FOAEpG5vwn06dKcgRxjIut8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار به روایت تصویر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/97384" target="_blank">📅 19:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8df51f9cca.mp4?token=R_5YWMldhqLUKU2etuxlnfV1w5xwSq38ZrNWyXFF-NHBXeVnyDc6168pirI4kg-d_avpTHC4--Ll7EnTHWGExj4Gan4nyjxfskU__oRapdFRZl1oZav6ZssiG7rxV07QiskrPEDLfn2I1i8_saTBQZULvPdHYmymqdaT0-2fduco2sD_t2jbfWnrqArN8CGOuo2HTdVF8EbzWpROhpdjdRatKfQ2iGHR3uMSmB0WcWG1VRjfLzgg_toWzLhFs-9cS7adKam0zSiqTcr8-SoPq4vkbOEJff3I5AdvBGtc6zWV7OVcUpCsJVqM7WkQknIsKNgzCAx5hH6JjRsb2ZxIGpURzjgRBRc6ByAMz5-2VfPmQbBsnc-fd4khURlKXWLjfGISrll2au_1U3zQjZg6uC1X69cxGt65KJ71tZmhu9fSSFFZUEUi9Kfag4E6wlNW4Y_EBdlUHK2O49WeT8o-MNzSvRbbylNt4ebfbIQjLqcVOFC77Osg5wrHsMORL8jquS0vjtEN2l8wIzfAQYXGo5l6dDzRADjmxAI7cvv3-6M4LLgX4Z5VEt93h7zEIbWLSw3qT4S12-Fog1wFAuHZfiZkD7sPkGwniiyUXlGWzGIp9BhURys6PdcsJiJmnduvesOURxnKF19EiG1_p4juN_MTUQqZUICBoMBSxDdqzUE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8df51f9cca.mp4?token=R_5YWMldhqLUKU2etuxlnfV1w5xwSq38ZrNWyXFF-NHBXeVnyDc6168pirI4kg-d_avpTHC4--Ll7EnTHWGExj4Gan4nyjxfskU__oRapdFRZl1oZav6ZssiG7rxV07QiskrPEDLfn2I1i8_saTBQZULvPdHYmymqdaT0-2fduco2sD_t2jbfWnrqArN8CGOuo2HTdVF8EbzWpROhpdjdRatKfQ2iGHR3uMSmB0WcWG1VRjfLzgg_toWzLhFs-9cS7adKam0zSiqTcr8-SoPq4vkbOEJff3I5AdvBGtc6zWV7OVcUpCsJVqM7WkQknIsKNgzCAx5hH6JjRsb2ZxIGpURzjgRBRc6ByAMz5-2VfPmQbBsnc-fd4khURlKXWLjfGISrll2au_1U3zQjZg6uC1X69cxGt65KJ71tZmhu9fSSFFZUEUi9Kfag4E6wlNW4Y_EBdlUHK2O49WeT8o-MNzSvRbbylNt4ebfbIQjLqcVOFC77Osg5wrHsMORL8jquS0vjtEN2l8wIzfAQYXGo5l6dDzRADjmxAI7cvv3-6M4LLgX4Z5VEt93h7zEIbWLSw3qT4S12-Fog1wFAuHZfiZkD7sPkGwniiyUXlGWzGIp9BhURys6PdcsJiJmnduvesOURxnKF19EiG1_p4juN_MTUQqZUICBoMBSxDdqzUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇩
گل‌اول کنگو به انگلیس در دقیقه ۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/97383" target="_blank">📅 19:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چه گلییییبییییی پشمامممممم</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/97382" target="_blank">📅 19:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پشمامممممممم</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/97381" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کنگووووووووووو زددددددد</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/97380" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/97379" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇨🇩
آغاز بازی کنگو و انگلیس</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/97378" target="_blank">📅 19:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjBSXDToBeAYLVeM-8nEsoaMgH6EKuGkTkTa8nxqQe3H_aaz01qBa8wKunjUK6IQYlfRO_NrQlhvGR1jPgMweIT5vtVcb2eDp1R0xlyi86R0rLlGxXXBOXZDR2hAWpJkw8ad-5PYtFxhwR2lSP3fbEIKc6WxZw4fwNrHN9y-BZ2hWXgqhtgA2prgpaCKRGh00aSbHdBLCl_f7JBoXgf_TpOqma9X28LGEoNiEygGieC9XKwjtYeSlw_-sW6iQjrpwSH5OgQ7j6QvxIsaY2OzZtOqZWIQCzWFY_2woS-tDJQT4dEqOoRqERsIp8pdUKGoifGYLu_zs59tSXfmmm2Kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسماعیل سایباری رسما تا سال 2031 به بایرن مونیخ پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/97377" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84477c6b89.mp4?token=QMzJ2Fhh9FhXBpxjF2yOzOCDQE-rZX67Bo2iVb1QlAUV1uDSKzXk0O0RRZKuqO8vVo0X3fX8mhMUXVBLR5jFXvJOTbLzRB-hAQ4WurODErs5I6vWHPyL8PsooxMVfRnPm4NEVN-9H_3h8yKLw7o5TxvBgJ3dCDDv8Q0Ov04SqLbmQ58BnTq4QBMtHo9eQL33jBj9beT5pOqJBx12ex6W1R_z-ZeEsAOc9w_Ngwhf8E63-jLjGUAjDjS-6JVBvlxVK6ydbC9rNj7mfrdpN0XAfTw3jYV_rPGBOp0WMw3hsZ_ZvASV42WIA8T-lol1C_55RDTVBApexTLP4pLeliF9rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84477c6b89.mp4?token=QMzJ2Fhh9FhXBpxjF2yOzOCDQE-rZX67Bo2iVb1QlAUV1uDSKzXk0O0RRZKuqO8vVo0X3fX8mhMUXVBLR5jFXvJOTbLzRB-hAQ4WurODErs5I6vWHPyL8PsooxMVfRnPm4NEVN-9H_3h8yKLw7o5TxvBgJ3dCDDv8Q0Ov04SqLbmQ58BnTq4QBMtHo9eQL33jBj9beT5pOqJBx12ex6W1R_z-ZeEsAOc9w_Ngwhf8E63-jLjGUAjDjS-6JVBvlxVK6ydbC9rNj7mfrdpN0XAfTw3jYV_rPGBOp0WMw3hsZ_ZvASV42WIA8T-lol1C_55RDTVBApexTLP4pLeliF9rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
تیری‌آنری: حرکت دیشب دشان موقع تعویض امباپه نهایت بازیکن‌سالاری بود و اگه باعث ایجاد دودستگی در تیم بشه مقصرش صدردصد سرمربی هست که به بازیکن فاز دیکتاتور میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97376" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd23d495ee.mp4?token=ZojSwSCetxv5upUPtIoVMUcoz93NR5b7BQH-bNuPJzQYCJoWNIYRGCF7hPnoa-_qxfcYC6bFjirzf29JZpcpR5as0hxapjXnRte1vFg3pgE3dTIxnSH3cm9ayUxRcENCDv1m0qzA334Zo-piEEKjQG2M3WFOO2apLpz0xqka-haGDqFSj91JFRB1HDxDUB86o0YShyCWlCJjm2JkeRPyZkI42GeGQr4SsLr-SNbM-gspQCnnSliGma9n989INscCJj-wi3fdrMDdAmgsedcmi-SmspvngaiDe7XVwLMkn_pAehtcM_Y0o-j9nVPaZD7EOUvzTPqcVy-N-FqpNWuMcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd23d495ee.mp4?token=ZojSwSCetxv5upUPtIoVMUcoz93NR5b7BQH-bNuPJzQYCJoWNIYRGCF7hPnoa-_qxfcYC6bFjirzf29JZpcpR5as0hxapjXnRte1vFg3pgE3dTIxnSH3cm9ayUxRcENCDv1m0qzA334Zo-piEEKjQG2M3WFOO2apLpz0xqka-haGDqFSj91JFRB1HDxDUB86o0YShyCWlCJjm2JkeRPyZkI42GeGQr4SsLr-SNbM-gspQCnnSliGma9n989INscCJj-wi3fdrMDdAmgsedcmi-SmspvngaiDe7XVwLMkn_pAehtcM_Y0o-j9nVPaZD7EOUvzTPqcVy-N-FqpNWuMcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های عجیب محسن‌مسلمان از ازدواج ناموفق و دادن مهریه کلان در سال ۱۳۹۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97375" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVso6LjG5gXzLIDWdyt9yNTBjDuBlj0vwPqV-NBZRKXAO6zie8sSA8O9CBRwH23tEbNDnAbV9MODObWsXhGNn2dqzHyhD0ONXyjY4VBl5irJoBO_Jx4mQ_ntEDQnYLkEs5Ckh44Lar1Wnk0YwYJR5cMUl5YfUcpnwQMTnORbsKaOe7Ip0FTORwjmbp484PwWxL2X2bIbnmAXv0mV5DduNzmnm3WMhPxv_qfeloBRnkcXmfR8I8_BaluihujJogsL_SVZRMMAg-5vosqG9-NeJ3c-RFCB46tnteiMe-J-6unIFz_NWpYLa2_NjrZf2dvCz4z1HJAQU08vxj6zfV9Afg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل باشگاه چادرملو اردکان:
اجازه نخواهیم داد حق باشگاه و مردم اردکان ضایع شود
به گزارش روابط عمومی باشگاه چادرملو اردکان، امیر سیدین نماینده تام‌الاختیار مدیرعامل گروه معدنی و صنعتی چادرملو در باشگاه، شایعه معرفی تیمی غیر از چادرملو اردکان به عنوان نماینده سوم ایران در آسیا را یک شوخی بی‌معنی خواند.
سیدین افزود: مگر می‌شود فدراسیون اصرار بر برگزاری تورنمنت سه جانبه داشته باشد، ما را مجبور کند که بدون تمرین وارد مسابقات شویم، چند بازیکن مصدوم روی دستمان بگذارد و در نهایت بگوید این تورنمنت بی‌معنی بوده و تیم دیگری قبل از همه این ماجراها به AFC معرفی شده است؟
سیدین ضمن تاکید بر دفاع از حقوق مردم اردکان و استان یزد، افزود: مطمئن باشید ما زیربار چنین ظلمی نخواهیم رفت و نه تنها از مراجع قانونی داخلی و بین‌المللی پیگیری خواهیم کرد که در مورد ادامه حضورمان در لیگ فوتبال هم ممکن است تجدیدنظر کنیم.
سیدین در پایان تاکید کرد: مردم ایران، چنین اتفاقی را به عنوان نمونه‌ای بارز از بی‌کفایتی مسئولان فوتبال کشور به خاطر خواهند سپرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97374" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhKnR-eBfUoAGoUCEFY7hlcg9K-061hEPMcsHZdm2dR-sns4_ppGn4zTbCtiOtPpYi1yPa-tg2sUAe2b_pXjn5zB3INqg-1e9D5Jo9O0sBGbF0VbWP7zTudSV_tjolN1XAMaYHQ49hB61zr81vp_llz2MMKm78_58Xcwo1pHQMNgXMGrkzugCJLw2vgtuXE86P67PQmHvcTd2-I14zKQJ6Xfz8gBfn11KYjchpun9G9z1BnaiCo9b-jHsgPz3Pzri-R4QJcPdx0d-4KTXThOaqLh7HVqcLbyxbX0UR76joM062SHo1QnbLUD80tz8lxak554vsx71tB_xVvSYL1D3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
آپدیت بهترین گلزنان تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97373" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq-KRRVChTNywZJVdbb_wUJ5q1CRfcsuSl1wIHYb6PkVXv0-Y4Liy9MU8yiZCcY9HapjrTPYYoHK27-YT86asPf26d6dQTuw4nkWIrR4FOdbly4YNsppMsJk_WBwZplYD_bAW0YM3Oqp75zCSjdtlUXxA4zPeVhJrpwcXutsj-xsK353KjVA5nkH2ZIzLFdoS9BFHVIVZVi2gHDvAtd4NbNZsmp7bkH8EoA8higGYLqJ7TUI5TLW1E9J4PBLJRVjFQWTAZJCOuDoRHxn2WF3GzA8-5o_Xp1Bq_D1RiDufRXIUq3vh2dSHlcSZNQ3et7GvxittHqXWqNRg7f84kzuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه نویی در بدو ورود به فرودگاه:
دستاوردهای زیادی داشتیم و الان همه دنیا درباره درخشش تیم ما صحبت میکنن. گل شجاع صحیح بود حقمونو خوردن، با آمریکا جانانه جنگیدیم ما عملکردمون عالی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97372" target="_blank">📅 18:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQwHJH2RKbGMjojTSavaTcuCWwXhml0Lc0IVBx0jqLA5OtHcLIrkRLeGkdWmSz5MrtIWjzVAT3wyGmCDnRds6bkjgwMKDEsnlKm_c0QbrzL22GDuHLv98dumJ4Edw8j2u34XuFswgWOf9Gl9gA_HYKdW-OPjF3LFZP4uGWwlXTS0MYErh8TrJkY3NlAsmRNNHXatRm3Vn9c-u9_IgTQe3QY-z59EdJ2w_p6Y_iaQmDCdKrGSCjhczkPG3xjVARbt3V0QtTkd74VpGgDsmXOIYchOnEOCjshkKSQYkWz0tGqfIxrRvC2go9SJr_xiHVxmYiWWLFLbPP9eFKT5bMfrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
مایکل اولیسه فقط 1 پاس گل تا رسیدن به رکورد طولانی مدت پله برای بیشترین پاس گل در یک دوره جام جهانی فاصله داره. و این درحالیه که ما هنوز حتی به مرحله یک هشتم نهایی هم نرسیدیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97371" target="_blank">📅 18:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35fd6c28be.mp4?token=qvtV3jgXMBkfHLqloJhV174S6LXAf0nFpuX-94bXocwEOOaegiMAOUHknT9RnUp3pmqVUm5-rVxcG2MiTX-V7OZtBV3cPuvi3JYFKjy2aTgQgbSQveqAVjG_YuTSZxBkq1cR69JePUIUhN5Me0boTUs9Ry96s69k6Pwbr8iIrb61CAv8A1Vnb-NK2hfwYic46JrWNVE60b52x6sn99AXJAACAdfXMEBDx4SwaKiLow_dYzIUGUH9cM77CEincTeWf1pZYFKAMa9MISq5gIAxnA4yLmAOmwDHQdZuc-dDKBldIVWWIT6hpu6WahnXb3y7UWjH06dCIp6b8wD_zf5KWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35fd6c28be.mp4?token=qvtV3jgXMBkfHLqloJhV174S6LXAf0nFpuX-94bXocwEOOaegiMAOUHknT9RnUp3pmqVUm5-rVxcG2MiTX-V7OZtBV3cPuvi3JYFKjy2aTgQgbSQveqAVjG_YuTSZxBkq1cR69JePUIUhN5Me0boTUs9Ry96s69k6Pwbr8iIrb61CAv8A1Vnb-NK2hfwYic46JrWNVE60b52x6sn99AXJAACAdfXMEBDx4SwaKiLow_dYzIUGUH9cM77CEincTeWf1pZYFKAMa9MISq5gIAxnA4yLmAOmwDHQdZuc-dDKBldIVWWIT6hpu6WahnXb3y7UWjH06dCIp6b8wD_zf5KWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇴
سوپرسیو گلر نروژ در بازی دیشب از این زاویه که واقعا فوق‌العاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97370" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzwghB03s3bORbfQQ-TFr6yLd1KVKrU7IieIaZu2OZF97zt9DBHt9WacBR9Di-0cPflVtG2Ktu6HOS4g5VZlSd-Bk7FfVlSFJHICdHxj7Rf5fhHRTwix8m8T_fGVp2ntUZvSQ4DuKyk2hmctATuId3IJ3tpEMIK8jHQK5P7-5k7VnNqxoxw2oIpnTiaQ3bLEjZ-tPPG2e6vDVrVgA8W56-y_8Lo3T1MG3k69pd2p2HRjflZJabGapx0xO__7jCRpDuraY2Q-X3CSU4bqU4wWMQqM2wthPkzZLF9tvlzNAQapkCFh0UWO72vM_WShrXNx2vv-Ng1RYUEAddEki8aCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPantQJPgV4MHR9GIFMNAUPrv32p7BYwoi5Z7hukIfHuZxdiAQRr2te_NbzD3fu-k9JRta4cIwYcVT6EJuKzXRHcoMfupEPurOZGYfmSOf_yTgpoQ7jHEFZumdZiDTmFLB4Ne1foPIKta-MZgZgLkNt2hQ_FktlB_1i6A8wL6P3hIky75dNKhUQK1YtlY6Hk-FOinBTSOFrN8iyuinXd2iECzAzBi9jB1PaXAA4TMuxJuIj7E0fcBB9MPRuIO3fc1BANb1J-inxsHSka3BjLLdue5sZj-0_O7NQ5a9k1Q6A2yA-YyQx0KJePBI706MSyq6LroCgWqptFxXLLxv96Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇩
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس و کنگو؛ ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97368" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97367" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d8b32dc.mp4?token=ozxoE-Egq2MykVltRXSiAt6i2RH6ZI2WMa4Sa9Hg90tTIC3uMZnhs9jYAwMKGleeVHneODETcqrxKYXXrvpCfPkguzqSeuicsTo-vEPIA02nOwxLc0FQ4DPsDOFkU2MDdagvC4j0bUkPdoIIzg2ccnMlj6ztWFXBW714Q9t-_6XyaDSh-TSS3x67kSTUepoX_6J2VD_ZibGSYUGjA2e3dUzeSLF7zcxqo-NYVUaNT762_3JRw76FdwwB0S7JTWvq-lm5yEhZ_fIMXqzc-uYX4dsH5p_Pp7Qj55py-CBmSTLuaq0YKWeOLoSNjMFDCgcaPFS85afIGXd0TW9YYcHfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d8b32dc.mp4?token=ozxoE-Egq2MykVltRXSiAt6i2RH6ZI2WMa4Sa9Hg90tTIC3uMZnhs9jYAwMKGleeVHneODETcqrxKYXXrvpCfPkguzqSeuicsTo-vEPIA02nOwxLc0FQ4DPsDOFkU2MDdagvC4j0bUkPdoIIzg2ccnMlj6ztWFXBW714Q9t-_6XyaDSh-TSS3x67kSTUepoX_6J2VD_ZibGSYUGjA2e3dUzeSLF7zcxqo-NYVUaNT762_3JRw76FdwwB0S7JTWvq-lm5yEhZ_fIMXqzc-uYX4dsH5p_Pp7Qj55py-CBmSTLuaq0YKWeOLoSNjMFDCgcaPFS85afIGXd0TW9YYcHfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇫🇷
ویدیو وایرال شده بعد بازی دیشب فرانسه که رایان‌چرکی اینجوری سرمربی تیم دشان رو دایورت میکنه و از دستش عصبیه. دشان هم هرچی از در خایه‌مالی وارد میشه جوابی نمیگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97364" target="_blank">📅 17:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQPt9x8iwmRfnVHK6lK4tz-mjMkYoEEJNY4v6s98J5VDksDmcI_DzgY1X8vPdx-5wPETzgNUH1LOznWQsc-SRE1lHhipo0UDnLQAXqWDOPo17QiZlBYX_CucCmtcvKWYTBqOll8UgZ2iCgfyrQxqM4k8-N7mXm3PlgxqlPPUML3dCr69Ok1dXj7zXHXdnLYKtx3dbpZaVuie-Xb9-Q3Kkg1uE0414m_B8w3xDNfmhfZ3AJTLxKKHXWJMt4grWP8E7XZz99-s6zUpkxKVN-HCHTOrJHQ0eCxzT3u_7AmMFaw_OX4H1cFdly0znMeufsqpoxs_73jhihkA1szykUt7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
دیشب بعد از پیروزی مکزیک مقابل اکوادور و صعود این تیم، 1 میلیون نفر میریزن کف خیابون و جشن میگیرن که در اثر ازدحام جمعیت 3 نفر بر اثر خفگی میمیرن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97363" target="_blank">📅 17:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97362">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgFjfLO7WChKbVA4znt6teBUmAJddqTbpxEt-8DWcHhuQTpYY4fR3eaoF_Y_g1tTLxflNfICJ6yRiM9xjq2m8k40xzWFykx3H7pN_chy87NENl4emjw13lwoFqyvW-PzcfF9m-VInQ-EnE1K-3u8OBNlA26Syw47wFp8OVoeCjuwZyGBbEtHwW2hhsMZECPrT36ag712dDiXJKQFsiwohLtWIXqGBpRsLH8TitqTnY8gPUQ1kkwzZh-qqDoAWIQ5emBbdfBrYrO2HWWG9KYoYgoxPXpcvFPCM9XQq0wNTyju0QMjMPnMUKKLvIZj4ydMtOg9mZfXyVdpOlsrU9e3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97362" target="_blank">📅 17:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97361">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=V2guZ1g6TCCaSxxcF8WvnJsUSypCRPG-by46gTkBQFhgeyal8TipE8EnZCCUrOqhKkg3WXW-p5DgUt3m2bMEEPZnohqErjaMF3Tje-17v9jg7rhSp0o7mlSJ1Dv4AtU4hwJOMI31giqRKEBfnn1POc_JGmzrTcN7FEctohjPdYcg8dn9HrstbDCC2m31Bd8tx7eQesBjCgXpgvLhT8kVD6K0Fcera6L89OpPnUBNCdbrWDNMg3tPk6sZXqBKwLZqqWYGPpUsoiRva_rSudaUVKrUEb04sG9o3WhBOaiEcj6YbvF0qaQrd0cV_wUih2qDiq_qGeX-yirBIN6VURF_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=V2guZ1g6TCCaSxxcF8WvnJsUSypCRPG-by46gTkBQFhgeyal8TipE8EnZCCUrOqhKkg3WXW-p5DgUt3m2bMEEPZnohqErjaMF3Tje-17v9jg7rhSp0o7mlSJ1Dv4AtU4hwJOMI31giqRKEBfnn1POc_JGmzrTcN7FEctohjPdYcg8dn9HrstbDCC2m31Bd8tx7eQesBjCgXpgvLhT8kVD6K0Fcera6L89OpPnUBNCdbrWDNMg3tPk6sZXqBKwLZqqWYGPpUsoiRva_rSudaUVKrUEb04sG9o3WhBOaiEcj6YbvF0qaQrd0cV_wUih2qDiq_qGeX-yirBIN6VURF_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
دخترای کم‌سن‌وسال با دسته‌گل رفتن استقبال رامین‌رضاییان تو فرودگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97361" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97360">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aToDUyyj38bs7KB5WgODfXJEUL7C2mQT8Ev8TbHQOnzGNXEc-IwupyMwviYM-1RCvC1hA-f6StlOVUChEyRQNp5py6zthtgEbagJ4sM8zP4HqTyz1UGat7ZjlQxjlr1845V6KP2VAJ4pa2X-XhHCCBjAzrJx3GLebJCf0coyp2QQB16wksSw4MOGQuiLaTVAkSWZLDvsIaFE1qQIFaVjW3t95iepl8iC7rNjvqoVtkqLCJGUM0A-IMFVv3sl0FThl-5lRz7dJ5ZrsLqAx6CL9_9R-pbm43QiTBYhuzC_WGc9zu4ttSJeV8Fne_Lwh73XH9jJKfT805d6RQAJfiTb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#فوری #اختصاصی_فوتبال‌180   باشگاه پرسپولیس به ریاست مدیریت بانک شهر پس از شکست مقابل چادرملو حکم اخراج اوسمار را صادر کرد و بزودی این خبر توسط رسانه رسمی این باشگاه اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97360" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axxa-gDK1dtwGNtsFYGxnjyYA3ookymESIVNtmCzi-ZWVdSunX4kTu-tl9gOSr0443TG2WC_36sbtT7HsxCL2vaU8MFOUjb5qO8Rwd6-KWtO_sAOpENyfnCs0SDh4yQyNW6-48HIKAwAxKIRYGTLyMkT185vvHQkG5LFSnuvEQ6emLNl9AD20XDoIfYUqomYc6lkOW4Tz7owfBvZS5QXo4yDs45kqFYpjY3pw21h8YAqFr2xrkUaMELh8GY-uOKHIsz-lTLRwFJojc1ECAMg4R3BYEQax-1BY6s7AQOvY25L9jLElHn3eoOOK56u2P6yNnaodavLlFKRZOrr9szUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇨🇩
سایت Score 90: ترکیب منتخب بین انگلستان و کنگو قبل از دیدار
امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97359" target="_blank">📅 17:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwqAgSGQjGG2ww4YzYH-zRaHd8yMkR04kRUzPNK-GeNmUVybfIklEcLhSli-8Sq2--iv2XRcIlVb-FPw07e1V4iGWe77FJu45-OKXcOnukU0lQAB4G7OhNFIixkvo0wpnj5uLCXSmFrN7sEXAqfz_JpVR9OP6zy3uHWwQycK_8-4Wh-qU0El0V0zOGEYEnZp5lrHS9CGndWzo0ikFIbQYrgyT8-vdb8O7GrvIQTQmIxMCwtGQ-LyjHNjl8AuR3_xiKLjSuO-rlO4FN2MWQLGd7CDUtBaJJdGFYjIIR1w_bcJhF3m88PgjUHRNlwFbnuY60Q2dAwGBBTSMGl0ujQScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فووووری؛ لاپورتا: ما برای آلوارز پیشنهاد جدیدی فرستادیم و امیدوارم در مورد تصمیمشون بازنگری کنن و این پیشنهاد قبول شه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97358" target="_blank">📅 17:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUnlTfHgfuZ3ReHy1cEqZGr25wVcrfGpJm6Jif5yXd84SX5vHWQad7KwQT4bZ5r0ImH8Pw08NyX8vNd4XXiLW5vvaFEp2H9rBVNchGELwQIZ32rHoxBZKtipxij1zYdFD_pF4JyCgCk3msORpV8V5aRa634L_xFCMTbNjn_GQLzzo7IjFrjYO8ricaCxv5uwfgInfT9QbbezOTpL35QdAbMLMdJ-v-XGIOWhPBYTA-9MZfzqKHJl7mHkIYWfFGGajl7HT0vFkv2Fi9uv9KVlBjYhDOqAJfsynKi1BtKU0Nd4a1X8CGOX1qnO3apgjdFpudBPdAqVLca6GcE6ITaQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فووووری
؛ لاپورتا: ما برای آلوارز پیشنهاد جدیدی فرستادیم و امیدوارم در مورد تصمیمشون بازنگری کنن و این پیشنهاد قبول شه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97357" target="_blank">📅 17:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbd905f72.mp4?token=vGfUQu8VeOwzl-Z52v0-9Mss-24NsWYLZF_zX9b1gwCBFzfbZo_ZPDr5ql2vKVEDAknwwwkRX3kaXkbEI78nVTArX_GdiWoYzFxEiaEiWTll0rlgzhgCWJIk0r_Z7VlIDetB2fLBv5FCV3_WhA3CYyOaY5HZbOuVG3EaCSlSlakd1XXDF-LxDS13QDhirUc-T7AjerxZVtGUwv9MY0tko9-kDdCH7Hv9k9fgOWPkJq_PlByKm-_2pppZeM2Cwht7PFv5CuceameeX5hed7k7bpR4xIqv8NMmlrJUNbMz13gdmmwAhAq0TtXPULwMR46bRlxVGACo0xXUdPrGwoev_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbd905f72.mp4?token=vGfUQu8VeOwzl-Z52v0-9Mss-24NsWYLZF_zX9b1gwCBFzfbZo_ZPDr5ql2vKVEDAknwwwkRX3kaXkbEI78nVTArX_GdiWoYzFxEiaEiWTll0rlgzhgCWJIk0r_Z7VlIDetB2fLBv5FCV3_WhA3CYyOaY5HZbOuVG3EaCSlSlakd1XXDF-LxDS13QDhirUc-T7AjerxZVtGUwv9MY0tko9-kDdCH7Hv9k9fgOWPkJq_PlByKm-_2pppZeM2Cwht7PFv5CuceameeX5hed7k7bpR4xIqv8NMmlrJUNbMz13gdmmwAhAq0TtXPULwMR46bRlxVGACo0xXUdPrGwoev_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ارضا شدن دسته‌های ارزشی از دیدن هواپیمای تیم منتخب ایران در آسمان تهران
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97356" target="_blank">📅 17:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAixx9vEGUYdjEMR0bBYQxKzpoMo2sLt2XCN2c5EpsDdM0SsU-u9x96t_NSmGf0LoHXt_pGKRiFLM6FilVbmsqkvzw7VKqyvQ6SS8kgwLNovpy3BA-BiKCEyJuKNYaKU1DPJaCghl-yAyTo3h7FuOzbKkGtiU1V9ge2shbiJsI51qo2LjScAzQdbZZgEF1ebjwcTsrSeuzmEiDLTZzzhgYWfmj1rj1SE3o_uKTkizqULc6m1lglhyElaurMJSc3TPhxdAC6_mHPBnsbkDsWaSwNcszEiF2rQuZSx5ZUR4HX5fgRc2SU4r4qEn5IjRCC_0tVYCYMQ-QSuCGyWF8cvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونمایی فدراسیون فوتبال پرتغال از لوگو جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97355" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97354" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plupn60FEKHo_PNLYoSPd31BHg7nzIBBZ9YMjUwUaHNY_DGrIQ3vMFj5RvwOGeyfpHlUqMLk298_NjA_NOP-FdTHTtH--NBaeTay41274QAAthVSNGcUe7HKpt5n9ORz_FSAFobWQofZhoSwXO19OviiOczaNfxCJTXFwKa15xptrqZQYPIFptElEYNyik4to4fWq6GUQ3zZqzPIFHBz40sRatAb3_jl3TgBQpsSfmta5Kj0uImCc_W7s0F2BIINtsxz5KGmHKKtVnKZ4UXkwRIfEHG374gUuJETo2lK4E14k1Us5a667mqeCs47h77VgDuZheCX931xQ1cEyGGjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97353" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=Ls2Hl-MPfDzvSa70zWWQMLhXGgEWn2jkGzSzk17zXPj7d_-EIwzhMIbtE0k_ByCwtiTYI-I0XChPr7kik_8hKEjxrLQAT24P6lJCk73OXh7d15UA_t_4Fu49tGCDWQ0GWhP5twd4gyqtNeMc-kl5AxrTktuRGvuPNeTAfAH1DpEcjxbF-d8wo6X1kyCm7-x68A1cMJ6KAAtglaMYbLMC638epj7XrWD7fnhNLTdodR-i879-rxH1LyR9cn231ejB7k8DyiNT6W4_CiKAl-K3Sn2zqS4pRRSG-cEhRRe7K7eo9Qw-gv1OTmpPKCyzWmfEhZDWn6hKK26o0ZwREjDH74zHmcn72TS8C4OBm-TE5ug17WBB-VBXOuJiKQs0NUEYAiiew9kKMaFGTCNuYXmomhlK0UFw3U7qlkD38280usDYkXdt4zGsVRP_-q0dsPIDwCnpmA8a9oPFMt49gyt06HGsRvSaKpfsSfdTz3YzfnH65tb397MWCVuKupQd0ZGm5ngHgn9f2Qx-yoi0yrk8dusSVhVUTBnFbD6FHLEBWQBGfTdndHerOlk3MlS95dryVLAr2gzlK6NtVS5IyvJGuIJ2sMsJY2Z7ymTswrwO738j6_3VSlIm8uAmntHyx3IRkTwvbrJ2kw_-bsgSWbFojhbpGxAyR14FOofRdy9xXu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=Ls2Hl-MPfDzvSa70zWWQMLhXGgEWn2jkGzSzk17zXPj7d_-EIwzhMIbtE0k_ByCwtiTYI-I0XChPr7kik_8hKEjxrLQAT24P6lJCk73OXh7d15UA_t_4Fu49tGCDWQ0GWhP5twd4gyqtNeMc-kl5AxrTktuRGvuPNeTAfAH1DpEcjxbF-d8wo6X1kyCm7-x68A1cMJ6KAAtglaMYbLMC638epj7XrWD7fnhNLTdodR-i879-rxH1LyR9cn231ejB7k8DyiNT6W4_CiKAl-K3Sn2zqS4pRRSG-cEhRRe7K7eo9Qw-gv1OTmpPKCyzWmfEhZDWn6hKK26o0ZwREjDH74zHmcn72TS8C4OBm-TE5ug17WBB-VBXOuJiKQs0NUEYAiiew9kKMaFGTCNuYXmomhlK0UFw3U7qlkD38280usDYkXdt4zGsVRP_-q0dsPIDwCnpmA8a9oPFMt49gyt06HGsRvSaKpfsSfdTz3YzfnH65tb397MWCVuKupQd0ZGm5ngHgn9f2Qx-yoi0yrk8dusSVhVUTBnFbD6FHLEBWQBGfTdndHerOlk3MlS95dryVLAr2gzlK6NtVS5IyvJGuIJ2sMsJY2Z7ymTswrwO738j6_3VSlIm8uAmntHyx3IRkTwvbrJ2kw_-bsgSWbFojhbpGxAyR14FOofRdy9xXu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرزشیا تو فرودگاه اومدن به سبک نروژی ها تشویق کنن ریدن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97352" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTH2XRPqRoPEkgbGY9fidogUKMtEW1xlRTm01JaYaaMNLzli8cuRWpP2sPfp2BGifUt4erNaRn8K46qtJiriB9LjT54YItbElj0moQ-zDCbQo1uRC8Yv9mFXEjfHujm5LfYjMhP9U0VPRBECWFDhy14Ucz5UGzqe0hz35Nl_qepKY-tLyapBm_9uEQ3aMJMYPDX9K_FZ4Zzd38FpQZEBHyuG1hLkRyLHkfcdCo-N6QHCIZMcNURdFT17gRIkDvBpweNdnOILlHDFQS7NKU0rC308u15vO2u5KnoVrBGKpyJbYMuRR9jFnRceRrloGvVWiHVGbvvlKc4_OK9Cmkl3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونی کروس:
ما در حال حاضر هیچ بازیکنی در سطح جهانی در تیم ملی آلمان نداریم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97351" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97350">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a746294c0.mp4?token=M9uTiO-mYGdCfivUapi-OngipmIzavUkUSPU78LoVAloVUHPgepOvsj7rh6SCrwfBft_yssltH6qqbfK45tKT5fzcTQHHD70EaD4_CgHx21Cq8noiS6Vl-b2URJITVwCkWynaHsjvKyMhVWAzcywxwqwzK66s3Jj9DjDzmVGCOLZL_O_lqjVtoiuRaHydKhfH_cJUf-yMu3tZAG9YYPHGxtDrbigb45SKvZEVgH1zHlI-pr24dlzwMmHTlN6oRJhWHdh-R7g2_b9_UcIYsHrdcYpWVuOyPOw2lNm43trEagt0XnlJINUPEH-G5k7uEKXWSavdwXXIXeavslVhWZopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a746294c0.mp4?token=M9uTiO-mYGdCfivUapi-OngipmIzavUkUSPU78LoVAloVUHPgepOvsj7rh6SCrwfBft_yssltH6qqbfK45tKT5fzcTQHHD70EaD4_CgHx21Cq8noiS6Vl-b2URJITVwCkWynaHsjvKyMhVWAzcywxwqwzK66s3Jj9DjDzmVGCOLZL_O_lqjVtoiuRaHydKhfH_cJUf-yMu3tZAG9YYPHGxtDrbigb45SKvZEVgH1zHlI-pr24dlzwMmHTlN6oRJhWHdh-R7g2_b9_UcIYsHrdcYpWVuOyPOw2lNm43trEagt0XnlJINUPEH-G5k7uEKXWSavdwXXIXeavslVhWZopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تبلیغات داره به جاهای بدی میرسه دیگه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97350" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97349">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PApNHDINxuCLJMcUnJ-2IXMrs_kOvrCM-BwHEFIhYaj78iTQVgDuIdWFPCs5Cp5mnCCDCiqqA1fhnNglPQGSqUOj7LT9DcMjgSFYrcfXjfhZp2URwhx0nQwLayR6vy80JmijSJ0isWcXsufQ3hDKNivrqK7s4NNmk8T2buPkYzQjCIJ0reuOGjn9VbD9oBogAk95iMjkKbSZzcUvb8FtYDopw0u5rP6IvWolynRz5JfAwfDP6XhhUrl99Ts9u3H1K0BSMvj0EXsrdFKVcvn-_mZ6c6FEaC_bwwJxhHNA1kZdshPMXsDL8gMXy-7VgLvUc3qKWDyO8NzC4A--2i_54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس اتلتیکو مادرید :
آلوارز بازیکن ماست، حتی اگه پیشنهادم واسش بیاد قرار نیست بفروشیمش، من از اظهارات آلوارز تعجب کردم اما موضع ما واضح و روشنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97349" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97348">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97348" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97347">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97347" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97346">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91afe7d0a4.mp4?token=KmxOEREcPOu6NN4R_5dQXCLofepgub-JjgErHrfTdTRS_rBiBEWzipJfF3yGS-2zyqU7owQsPZjkdDX8XjolO-DYa7ssnNRAiokbmWT2ndLeS_0865UuvRr18NTrYcazO_JCI4nyr45VDB7I-uCXKoTiL-EV-xbbYqsu2b-NnSxxmckroYaTSe4jWykwTml_UPEy-OqPsH0IEJ8wITqxqNI2cG0wEu3P3YUoz9FsnB0Z6qrYtiDm8oJWBkypN8FSN-Cwg_7lYsB-E_k0yOwPvEXp0JyrBxddU_w15ABD7xc3IB_gmiv9ZoEmVJGgepXMDlCBT6oOZ516H6p1n8IORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91afe7d0a4.mp4?token=KmxOEREcPOu6NN4R_5dQXCLofepgub-JjgErHrfTdTRS_rBiBEWzipJfF3yGS-2zyqU7owQsPZjkdDX8XjolO-DYa7ssnNRAiokbmWT2ndLeS_0865UuvRr18NTrYcazO_JCI4nyr45VDB7I-uCXKoTiL-EV-xbbYqsu2b-NnSxxmckroYaTSe4jWykwTml_UPEy-OqPsH0IEJ8wITqxqNI2cG0wEu3P3YUoz9FsnB0Z6qrYtiDm8oJWBkypN8FSN-Cwg_7lYsB-E_k0yOwPvEXp0JyrBxddU_w15ABD7xc3IB_gmiv9ZoEmVJGgepXMDlCBT6oOZ516H6p1n8IORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
شادی مردم نروژ در استادیوم پایتخت این کشور پس از برتری مقابل ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97346" target="_blank">📅 15:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=rJbHuVkjVwY7XfO0HAxXgm1tFs_EtxA1--CO64GZMn0lxDmbF-wxtJRxnONweN2kvJ0gRZpjymfJ5BAs75kVISIJaX0BmSnyb3VZvT11SPJA7DPJK08T0Xc7gjtH5XYslahdN671LBEYxjZMIisWvCJV_OJYozs5fkbyZkp_AyQZsCOPDcq_2so4CM2_mQGdDQ66qXnjt8rkq7qw-RksLOHNJ1BEdATWhphgKbTcOdLQfsW6EQj5B7zeHkkFAVJFBaVRJIoPtbgYrLA3GZbqW59h2ULJlspX98eMEEcVqugaIAli7bV70Sel9iJaWULcrJMd5FZ3PzvkhTceChwauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=rJbHuVkjVwY7XfO0HAxXgm1tFs_EtxA1--CO64GZMn0lxDmbF-wxtJRxnONweN2kvJ0gRZpjymfJ5BAs75kVISIJaX0BmSnyb3VZvT11SPJA7DPJK08T0Xc7gjtH5XYslahdN671LBEYxjZMIisWvCJV_OJYozs5fkbyZkp_AyQZsCOPDcq_2so4CM2_mQGdDQ66qXnjt8rkq7qw-RksLOHNJ1BEdATWhphgKbTcOdLQfsW6EQj5B7zeHkkFAVJFBaVRJIoPtbgYrLA3GZbqW59h2ULJlspX98eMEEcVqugaIAli7bV70Sel9iJaWULcrJMd5FZ3PzvkhTceChwauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👶
🇧🇷
بچه‌رو چرا موقع فوتبال دیدن اذیت میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97345" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bece496424.mp4?token=U5Of-ySc58pDdFOrLJUuc9Vd549A7cQt6fzQcCwK1l16-rqqR04W5OhO-gZs7gWn9uQykeHd-2TtpNEbpmYAUOJWalnFa0gLmHMzJa-cxO8Biin_ioxVVz_e3Lg3PiLEkDiYtXsA1XZg3SpqR5nRIbljL-t5cIhUQW-IkcsgwAc2hiiqWAjkYvdOuCEa1mvVBrw-Le9j-2F6cLP7-H8c04DLwNEhG-Mf01zoDu6RDdaN9bk8RnsRxNug8JwGz3m6LEMYSyhL4kNPp4cUyB7JYo0WOPriXvYT4wz0-wq187Ts2BXlZIBSN5VbFWV8ANhmjKRiSt-C_9UZ01OdG-X7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bece496424.mp4?token=U5Of-ySc58pDdFOrLJUuc9Vd549A7cQt6fzQcCwK1l16-rqqR04W5OhO-gZs7gWn9uQykeHd-2TtpNEbpmYAUOJWalnFa0gLmHMzJa-cxO8Biin_ioxVVz_e3Lg3PiLEkDiYtXsA1XZg3SpqR5nRIbljL-t5cIhUQW-IkcsgwAc2hiiqWAjkYvdOuCEa1mvVBrw-Le9j-2F6cLP7-H8c04DLwNEhG-Mf01zoDu6RDdaN9bk8RnsRxNug8JwGz3m6LEMYSyhL4kNPp4cUyB7JYo0WOPriXvYT4wz0-wq187Ts2BXlZIBSN5VbFWV8ANhmjKRiSt-C_9UZ01OdG-X7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
‼️
در سال ۱۹۸۳، ریک چارلز و چهار شیرجه‌زن نخبه از برجی به ارتفاع ۱۷۲ فوت (حدود ۵۲ متر) در سی‌ورلد پریدند و رکورد جهانی شیرجه از ارتفاع را ثبت کردند؛ رکوردی که گفته می‌شود تاکنون شکسته نشده است. چارلز با سرعتی بیش از ۱۱۶ کیلومتر بر ساعت به سمت آب سقوط کرد و پیش از برخورد، یک پشتک سه‌گانه اجرا کرد. بدن او هنگام برخورد با آب نیرویی در حدود ۱۰ جی را تحمل کرد. در حالی که بسیاری از تلاش‌های بعدی برای ثبت رکوردهای مشابه با آسیب‌های شدید همراه بوده‌اند، چارلز به لطف ورودی کاملاً عمودی و بی‌نقص به آب، بدون آسیب جدی از آب بیرون آمد. بیش از ۴۰ سال بعد، هنوز هیچ‌کس به این رکورد نزدیک نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97344" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=YLeAHx6wCBuSrfuDGIKwQqUaspK-fch2rWL6-CbDVcpyfmsCx0cDtIS35lhX886m8kRFJ3l6DroobhPyYoeI2OLIvp27gvW8tmVXpOQ5G5ZKwqYWonY8T3_dnSTzhTU7QnhbZpUgDXg0cs7lpyfr5yAVoHowrtstVfTv3jaKLj8aoY9a0ktPff8HMSY3JIT14uh9uwfzyePFUlDH15TTpxHs1hZYguAw_d2ci1W5orZZcR4eJd4WNyT0sszSKtKTE2tDovr0N7BtCINxaUjmXtyU_AioN44UT9zICc-mgwdNqjNpMXLIxXvjJurEEk8MNfmZAKLM0hT4H5KV64fJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=YLeAHx6wCBuSrfuDGIKwQqUaspK-fch2rWL6-CbDVcpyfmsCx0cDtIS35lhX886m8kRFJ3l6DroobhPyYoeI2OLIvp27gvW8tmVXpOQ5G5ZKwqYWonY8T3_dnSTzhTU7QnhbZpUgDXg0cs7lpyfr5yAVoHowrtstVfTv3jaKLj8aoY9a0ktPff8HMSY3JIT14uh9uwfzyePFUlDH15TTpxHs1hZYguAw_d2ci1W5orZZcR4eJd4WNyT0sszSKtKTE2tDovr0N7BtCINxaUjmXtyU_AioN44UT9zICc-mgwdNqjNpMXLIxXvjJurEEk8MNfmZAKLM0hT4H5KV64fJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌رحمتی: بیشترین ضربه رو از کی‌روش من دیدم ولی واقعیت اینه فوتبال ایران باهاش خیلی پیشرفت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97343" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgW0yS-qBwLxV2oR83CJiBZOIV-yxTWLm7uqfzdjw723AhnSxOkJo8GlwdImfwm6ydPWYklWuiAmx69sY9mTdUiZP1lbZKJ1PdOIKuGKKDfGmi8uy8Bhb8QNxCmERg4hrPVlwJpHO4ArshAJ5n-G3bwoz5fL-bMuNaOHeWKsZlLrOLX6v74WQcIsE7pZHC4slIdFNxh9Ye4OORUHVXKAek5M-4WMSV5bs_IraqwOWMYdC84mwAFmLfmg6Ptp8WN3oMRKlNC7qcifUUJwIP-Bcw_KV2ov13yWSxhsgv8siHEQ9JLiIAkb-6FcMRmnH3oWykYMWDzL3u2gG4DtEc9-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
هوادار نروژ در بازی دیشب مقابل ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97342" target="_blank">📅 14:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03f28112d.mp4?token=A4kb-NcG5Qja2f0T5xkGlALEgUNYvf5tZerg3QL5sHJJAEFp4PKhlnkB6lHJNPfZn5LqN9PmjdXYNp3kG3ctCGP19uuMowofHxtK8xhjQ7lPAIPcmGwWq17xxCXM-OO0pmBmnD47cM8NIARoLo2nAwOs4ZXej7C86zZM9boV3LENwk2mnyk6sDxox-yNxCnfpPWENImPvJLEWQTJ7Y8OYkLMonM2H_LA0AZq568janjc8Q-R6o7j0E8w673EjJDPzQ6sYHLUJDhUlVDntIPoVf6U_gXLWWY7UV7Sbv2Tv8yNAIEuexahiyuQU_cujNoss0efIEN__O5ygt2BTeZIAWSMzDH2o0ZNJG0vKJQ6iMkEyL-Il2FTm4C62r8Qzdlj0cBL0xlI_8Dsf64BAFfWnMKnGE9gXt0waF3UAKam-IFa4Bo5oDUnDB8sGvGzF_vWGIzOGP6uOTP5ddEXoRjqggFju1qxzdDEAX8yaKS7Jyly04JAox04bf49vSSfkYOBcz6Jcew8DarRec3e1Z6t535XTWVq2spxcyIpoPoMuJDXXntnDDIpMdv0gdkSv6vFpYWw99ISWFDk-XWJ5N8oIXuKPgIikSLVcv0HEBDKxu9U6H8R8hC7w_lB43gDPHHSZ1Jt7z4yTxQXzlbT20OHMSR1a2mH_-Y-TB5koMQ_pIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03f28112d.mp4?token=A4kb-NcG5Qja2f0T5xkGlALEgUNYvf5tZerg3QL5sHJJAEFp4PKhlnkB6lHJNPfZn5LqN9PmjdXYNp3kG3ctCGP19uuMowofHxtK8xhjQ7lPAIPcmGwWq17xxCXM-OO0pmBmnD47cM8NIARoLo2nAwOs4ZXej7C86zZM9boV3LENwk2mnyk6sDxox-yNxCnfpPWENImPvJLEWQTJ7Y8OYkLMonM2H_LA0AZq568janjc8Q-R6o7j0E8w673EjJDPzQ6sYHLUJDhUlVDntIPoVf6U_gXLWWY7UV7Sbv2Tv8yNAIEuexahiyuQU_cujNoss0efIEN__O5ygt2BTeZIAWSMzDH2o0ZNJG0vKJQ6iMkEyL-Il2FTm4C62r8Qzdlj0cBL0xlI_8Dsf64BAFfWnMKnGE9gXt0waF3UAKam-IFa4Bo5oDUnDB8sGvGzF_vWGIzOGP6uOTP5ddEXoRjqggFju1qxzdDEAX8yaKS7Jyly04JAox04bf49vSSfkYOBcz6Jcew8DarRec3e1Z6t535XTWVq2spxcyIpoPoMuJDXXntnDDIpMdv0gdkSv6vFpYWw99ISWFDk-XWJ5N8oIXuKPgIikSLVcv0HEBDKxu9U6H8R8hC7w_lB43gDPHHSZ1Jt7z4yTxQXzlbT20OHMSR1a2mH_-Y-TB5koMQ_pIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ادعای مهم و قابل توجه سید مهدی رحمتی درباره وضعیت تیم‌ملی و تصمیمات فدراسیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97341" target="_blank">📅 14:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiCqJI3zRSFHnpZioiTe4sI1FMB-2-7H_9cbxWqBHToo14ZzdHp2IiZV9tlLd60tNXox3X2U-LCI_NDn9kFcvPE_nZ2u53FWkfWDzQTpymC9Ak8eAEzr1w6C0Fg_pwPUuTv_5RCmI97v1F86MYh90AK5yqBUxoS95gj4Rbb-QdRpTft_yXNGY44O3l1NxvpABU9BL8fkOTVeyaLpCY_tdKWaeVhmZB8Bk3dpuIOO6K89AHdSzSgfeIQfd0ZJv8ohByPeM00df0Eix9lJW-oGD0ozApMfcDMuDUWEzHd2FNsiHepg1pA_6Ko-i9PpR3X1ToaBXzTmGR4XSrrmQ5Wn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🤡
کوکوریا بازیکن رئال‌مادرید:
🗣️
امباپه یا یامال؟ تا اطلاع‌ثانوی یامال اما بعد جام‌جهانی نظرم امباپه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97340" target="_blank">📅 13:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLLioSWl-j03ajAZjpCpNZRL4Zj_T9gT5t2VXF01cXgYZM02934vI5-xT6NM4SX8EwmNMq6wmp9jve3Fyuv3ulPVCS6iG04zLTATzsOmtFRzP3Xf-W-WELgdNBjZjL6H3NkrLxuHyh8TlAaZBtr0Blf9rCMB_kO-xO9nIW90sgpLyvQUXbh4GuKYpmJxuUGl_1iyJ-g7eYGaAQfj_JYYjYLiT1pwJSKT_jq-6CWhuMqydX92jPfj3Ol8YylxJ74NQ478ScFTbjwZeRna6STLpsJ4A9y9aUBqOa6Kr902tr1oIiJqoylDdSGYL9-yITBGI7QTTHojKOcBSn_FWmkQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اخراج‌ یا استعفاهای انجام شده پس از حذف برخی تیم‌ها از جام جهانی تاکنون :
❌
🇹🇳
اخراج سرمربی تیم ملی تونس
❌
🇰🇷
استعفای سرمربی کره جنوبی
❌
🏴󠁧󠁢󠁳󠁣󠁴󠁿
استعفای سرمربی اسکاتلند
❌
🇨🇿
استعفای سرمربی چک
❌
🇳🇱
استعفای سرمربی هلند
❌
🇺🇾
استعفای سرمربی اروگوئه
❌
🇸🇦
استعفای رئیس فدراسیون عربستان
‼️
✔️
🇮🇷
در ایران اما امیر قلعه‌نویی و مهدی‌تاج با اقتدار به مسیر ریدنشان ادامه می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97339" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhdKLwLmAosBShYCL7SLK6qRreyo4YSMwu5tmFRw-Y6gAyauvHYUg8fro5CTbdk26wn_N-4s2KickbOvhpM3lWbUDuAQRmpUOzshlRUNa2ZyHlXRrvlHVkv9K2kOs23SsvNZ_dqeATqy_xyA5xg_ONKmsyzphIKZ47s1alkHalBqv5pJgaNIvaoTKT098QgUOFUpmQCRIVG-ux_qiQAn6e-12dueKg754XfVbb7XxlFqo8eN6nix5FfUi6dUG7r2R6XrSqlgwFLQmAONWFTf8QmkxaK23t9eNHXSK_hjAP_aLIABZ71XndZxn-Eqs5MjubvXWS11WJMcE7-IY1jUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
🇪🇸
#فوووووری
از الچرینگیتو: امباپه در اردوی فرانسه شدیدا با اولیسه درحال صحبت هست تا فشار بر بایرن‌مونیخ رو بیشتر کنه و به رئال بیاد. کاپیتان دیکتاتور فرانسه به اولیسه گفته حداقل میتونیم یک‌دهه تو رئال‌مادرید جام های اروپایی و داخلی زیادی کسب کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97338" target="_blank">📅 13:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0e1d128a.mp4?token=jiwGOtq97nESYAyZkkIXsyubr2cWFv7-RzDPeCPLRGTQwrYtcgFIm6iX63C4WS-k0KjccvuT8dyOLBN-cCiXYRaS-t_QOd_Lnb7i6TKKAR7qFKRbQXvMYl0tiWp6lDZKsFe02Q3rmRjcS-um_vcOZAKCQtaX142cQe2EKCc1olWokxzfvtfBIlkxS4thNimA1A_McHQ1D8UlkvO8qJYFSrNF9vGyovAIZ-BlXtYz_xMAmK1wvt_lLi1WQegmQ6gbk6YQBmTqRsME6Cfiq9jG280xuFVkeX4jhXUPAydJUr3JBguxC_dXKyXoVkxhj1-oACAjHsFBrBdqOJ8VFWnJVgh4uYeDM0Gm0itFDa5YqMaLlwvGEcSTThM8MpXF5PuFpm1z9My1hPjZJhxOZCqgtoG7jEAkdXMquTMOAowD4cxn58lxxhvZhIbEhp5s8Cpqsn5it_UUbX66CViC5NtrJsNSyIPa4VP6FAqaEtHYeqIKMIwhNthe3OoBKIol0F40bL-XZkuRzudGbTUL3ABbgOas8K45WAq3Vt2ljDNWmHsS3jad_B1I7THLj7p4YSkc4EV0pWtCVrl98H5yU-nYJnlYZFBY1AIVUcLWowclSSwzlHcMzBwBbuX6z-Tf--aOeNzp9V44hKNP1y79XnoN32FpDhberCYtfXVP96sR5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0e1d128a.mp4?token=jiwGOtq97nESYAyZkkIXsyubr2cWFv7-RzDPeCPLRGTQwrYtcgFIm6iX63C4WS-k0KjccvuT8dyOLBN-cCiXYRaS-t_QOd_Lnb7i6TKKAR7qFKRbQXvMYl0tiWp6lDZKsFe02Q3rmRjcS-um_vcOZAKCQtaX142cQe2EKCc1olWokxzfvtfBIlkxS4thNimA1A_McHQ1D8UlkvO8qJYFSrNF9vGyovAIZ-BlXtYz_xMAmK1wvt_lLi1WQegmQ6gbk6YQBmTqRsME6Cfiq9jG280xuFVkeX4jhXUPAydJUr3JBguxC_dXKyXoVkxhj1-oACAjHsFBrBdqOJ8VFWnJVgh4uYeDM0Gm0itFDa5YqMaLlwvGEcSTThM8MpXF5PuFpm1z9My1hPjZJhxOZCqgtoG7jEAkdXMquTMOAowD4cxn58lxxhvZhIbEhp5s8Cpqsn5it_UUbX66CViC5NtrJsNSyIPa4VP6FAqaEtHYeqIKMIwhNthe3OoBKIol0F40bL-XZkuRzudGbTUL3ABbgOas8K45WAq3Vt2ljDNWmHsS3jad_B1I7THLj7p4YSkc4EV0pWtCVrl98H5yU-nYJnlYZFBY1AIVUcLWowclSSwzlHcMzBwBbuX6z-Tf--aOeNzp9V44hKNP1y79XnoN32FpDhberCYtfXVP96sR5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
چرا فوتبال بدترین کسب‌وکار دنیاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97337" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfacd704b.mp4?token=NEHpsOypSfuUH05Y-mZZIds_Or_aGPut1LQ49FytlXyvRV-PcIkhPfDcvY2gEKcEhzsFq5w9Spt7YJVYe_BNxqWmvwQSW72xLEzYADYsqsum1rukwfF3xU3yknkmFQ2fZP3qCp2Vx6xYoXfMcCa8fz4EatV0YvYhuQclBz_edHMAj0VDhxztOrtndVD1dUyLBahn2LGnnvPp2jzUK92zMUDjzKJ4X6r9mZvxf3hUBsUeBX2vAuPO2on-Unm3B-63DT6Jzhp1llv3LBhf-pM9ympiR11GwxadLEIgcVUgSrl7tpIlRZjZcKjNXNSPUEjjLZs6N7038_cmQ07Jb_rdEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfacd704b.mp4?token=NEHpsOypSfuUH05Y-mZZIds_Or_aGPut1LQ49FytlXyvRV-PcIkhPfDcvY2gEKcEhzsFq5w9Spt7YJVYe_BNxqWmvwQSW72xLEzYADYsqsum1rukwfF3xU3yknkmFQ2fZP3qCp2Vx6xYoXfMcCa8fz4EatV0YvYhuQclBz_edHMAj0VDhxztOrtndVD1dUyLBahn2LGnnvPp2jzUK92zMUDjzKJ4X6r9mZvxf3hUBsUeBX2vAuPO2on-Unm3B-63DT6Jzhp1llv3LBhf-pM9ympiR11GwxadLEIgcVUgSrl7tpIlRZjZcKjNXNSPUEjjLZs6N7038_cmQ07Jb_rdEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇲🇦
مجری خانم ویژه‌برنامه جام‌جهانی بازم تو معرفی بازیکنای مراکشی سوتی ریز داد
😂
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97336" target="_blank">📅 13:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdWNPxa8loRTm-_FW-XOB83MJByGe5Nmut4qbdMxtWMB25oRFDwk14IjwVpNJDL3RxiZtgrEGhfZo3zGCDcbgIf87UuKg4vWLstjvR9WPh1EXlvjoEdKzOChc1cKku516gG6DobznE9SZd3BvubLEhlhMVfuSVHejS3lAzYMCVvgJgFKZNHeYzW5FlwGqMbXFwx4ImJdVh0sVhBCW1ucQznvGpqmkLqSZT2AflNDgJnKCA73ZfaJwjOIoh2curA9s1XRS_cpJMlLD1Oqlb8LT7s5DE8ZZMsNog6vQx6avg7b4vsrtp4Jb0i99fsS4xiOJ1sAb4ZhmEjsS17lJOf-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛
در چنین روزی از سال ۲۰۱۶: منچستر یونایتد اعلام کرد که با زلاتان ابراهیموویچ به صورت انتقال آزاد قرارداد بسته است.
📊
ارقام و دستاوردها با منچستر یونایتد:
◉ [53] بازی.
◉ [29] گل.
⚽️
◉ [10] پاس گل.
🪄
🏆
لیگ اروپا [1x].
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام خیریه انگلیس [1x].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97335" target="_blank">📅 12:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97334">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpenddXwayOk569OoiVds7O4RCMBOuNDzElhCrwdm9HroJR39cd7wo1G3dBeKyYCyP4Rvhyovzg9XfTiWRZaf-ABLJHYTBFZpvwMZ7ITjz9feVJQNKOcyzJ3pyInOSaIGQ1Xr2UsVDIdnKGY0Ys43-WP4YvK06EAYZmgmL4ysJTNuUlpT2NQF3V5JhBtsp3LsojAH0PSXlx2zMIqp-v69E7iEjH-kwqoCNTt42CtsI1Z3dZ_6bODxQWGIoEkhlBzIRf47QrOWEJHhtuk1tb30CWvlJ487q_8SleP9ktLUTEgIlviacSiOZB1zGDZx2XD4-2VABdLy07LNnohoEE6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ جرمی ژاکه مدافع رن با قراردادی به ارزش 72 میلیون یورو به لیورپول پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97334" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97333">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f803ce8f.mp4?token=NRvLkjkrmgSZTDvn0R1ky9RyQuSesaYYCCmaBPA3wOfTgguPr2DaFcZfBvj3WjT26Bk8bxFeirVo102dvMAMhaIxwH0IZAgY9402q10ApxTWKQT1BlAVUm1kTVRw6acBIQkc8uA8u67dYzMepFvIbZPJ9UQ9jOcyw-IoZ9OIwmmcNGOfKtIPEk-3JHPAVlIfwsCTf7NwCb3s7zNmvRqPVMlaHtkR9r7dxSmCW4ZeefA2eJ4ERzlyvvSJfkFVQqc1xMEHEU0zLBaSFqUiw8e2vn6kjPyAbzmCghdVbMRj15hLSZrfStrQr_0aOIkQPt4HWIHL_lK9BjMe0Nbadft-TaYPDIuDOd5TnKaVHnOqQESFkrjyPMFN25f2Ibqq0lsXiz5FLLuu0i6HTA4vomm83lON96bhA2t6fwb3zuZO8YgxSUb5HUKpju0xjjr1rxeB8gR6EW3q-whj_tDAV__2tQ0V7iwWvKX4gN1plLs7YZ9wTsjN4YvsTHyB1YfqoD5kkHGTI4kLPsZzXxp7S_VLSvOjaNFSR2GW4L76TP_qYHaG86BT0qhzBs7h8H8N-Af_ODIOzriVcYtE1nj3V7mneptFPQf4jyC-EuonK8X61dxwIgdsStB5TcS8SCe8rhwdZzTs-39T1i-fip36H8zRxXe4PYCBL98a1xW3EDVWSBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f803ce8f.mp4?token=NRvLkjkrmgSZTDvn0R1ky9RyQuSesaYYCCmaBPA3wOfTgguPr2DaFcZfBvj3WjT26Bk8bxFeirVo102dvMAMhaIxwH0IZAgY9402q10ApxTWKQT1BlAVUm1kTVRw6acBIQkc8uA8u67dYzMepFvIbZPJ9UQ9jOcyw-IoZ9OIwmmcNGOfKtIPEk-3JHPAVlIfwsCTf7NwCb3s7zNmvRqPVMlaHtkR9r7dxSmCW4ZeefA2eJ4ERzlyvvSJfkFVQqc1xMEHEU0zLBaSFqUiw8e2vn6kjPyAbzmCghdVbMRj15hLSZrfStrQr_0aOIkQPt4HWIHL_lK9BjMe0Nbadft-TaYPDIuDOd5TnKaVHnOqQESFkrjyPMFN25f2Ibqq0lsXiz5FLLuu0i6HTA4vomm83lON96bhA2t6fwb3zuZO8YgxSUb5HUKpju0xjjr1rxeB8gR6EW3q-whj_tDAV__2tQ0V7iwWvKX4gN1plLs7YZ9wTsjN4YvsTHyB1YfqoD5kkHGTI4kLPsZzXxp7S_VLSvOjaNFSR2GW4L76TP_qYHaG86BT0qhzBs7h8H8N-Af_ODIOzriVcYtE1nj3V7mneptFPQf4jyC-EuonK8X61dxwIgdsStB5TcS8SCe8rhwdZzTs-39T1i-fip36H8zRxXe4PYCBL98a1xW3EDVWSBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
عادل فردوسی‌پور: از عملکرد تیم‌ملی و قلعه‌نویی اسطوره نسازید. خیلی معمولی بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97333" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97332">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65d18e2b7.mp4?token=qlyRaLlEx_pLbRIZNSq691AJ6hQ-EWyu8o3Ne68_tlv1dNW08_x417bJXBOR0jPRarlRfwZu9EeWaYW711HXuO7EffiuHDDZ79j_fvajEwEPkh0pvvfptyg6UU_OMw8lQfzdtLQdcyr82ElgBBRsRiZfA_bFSsZ2-29uevXHFnE5z3oeAJSNojDc6i2Yv_i1XlOz0e-4SgOkye8Ttm5LJBIDCJEXAVKOuuG09j9zj05bqvOnpFroGpxCbq62z0_bHAGSRbG5hJd6CXJ7JOimafQJaFy4E2F3NUT9PTjKejH94Enbu3gHHeSRsX7KP3AtsltghkAZZqRQ6xPaG7aN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65d18e2b7.mp4?token=qlyRaLlEx_pLbRIZNSq691AJ6hQ-EWyu8o3Ne68_tlv1dNW08_x417bJXBOR0jPRarlRfwZu9EeWaYW711HXuO7EffiuHDDZ79j_fvajEwEPkh0pvvfptyg6UU_OMw8lQfzdtLQdcyr82ElgBBRsRiZfA_bFSsZ2-29uevXHFnE5z3oeAJSNojDc6i2Yv_i1XlOz0e-4SgOkye8Ttm5LJBIDCJEXAVKOuuG09j9zj05bqvOnpFroGpxCbq62z0_bHAGSRbG5hJd6CXJ7JOimafQJaFy4E2F3NUT9PTjKejH94Enbu3gHHeSRsX7KP3AtsltghkAZZqRQ6xPaG7aN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
چرت‌زدن پاره‌کننده هوادار مراکشی تو دقایق حساس بازی با هلند که سوژه رسانه‌ها شده
😂
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97332" target="_blank">📅 12:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97331">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvmKWTE8bo6bNLTK7YVuLEQKdf44KLaBf34dsmkssgaVRc8REL2IlG9BBmB1glDU44wdI2phjPaVgzolBfdvow5_oYCnZdjRDE5dWtKO6nb0txw8TaX-q9gn-BJj4UTOUzUeIZKOVWaFYWg2OTo8RCriZhrMLYOHuB7mLP72bZYIDJmoH2HyGCk1wXQwRsbivsLXnpxKK5L5PuBRyx7A_0tOxARQsQ3d149HfpJoaaK64KhrniDRMDYrjj5AcoSeGN1JVroK6KR7T-_iiIPmxJGJjnMBBXTB4Wrg7e7rdGlGEthmjsyJ1gnjK-ECpL-prLr3nmU0ePPOzx0xNRs4P12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvmKWTE8bo6bNLTK7YVuLEQKdf44KLaBf34dsmkssgaVRc8REL2IlG9BBmB1glDU44wdI2phjPaVgzolBfdvow5_oYCnZdjRDE5dWtKO6nb0txw8TaX-q9gn-BJj4UTOUzUeIZKOVWaFYWg2OTo8RCriZhrMLYOHuB7mLP72bZYIDJmoH2HyGCk1wXQwRsbivsLXnpxKK5L5PuBRyx7A_0tOxARQsQ3d149HfpJoaaK64KhrniDRMDYrjj5AcoSeGN1JVroK6KR7T-_iiIPmxJGJjnMBBXTB4Wrg7e7rdGlGEthmjsyJ1gnjK-ECpL-prLr3nmU0ePPOzx0xNRs4P12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
تفاوت سطح‌فکر سرمربی ژاپن و قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97331" target="_blank">📅 12:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97330">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvjp_D8QhIytU-MuLV-XEoGhPmfUr1ulPOEcioWQDPYfIYOzsrAX_I9Vm21VRwnS98r_57JXUTAPK_JgdT98j6P4XVnz3XTQelrw1YuWXKVYqz0DB9ObkSBYoMoPonks9TNkK1FBBrH_m1Qmm1n5zK3pQPOqJivZTRq4RvVyIBgUJyW0nvSsTIeP9oEjbhRDh-XMTDb7KXuglRJ5VkeQUg4i7L3MuGkW29TdnSM9OTX7ogwp0w51bFhL0acZGyL_Pp45CvBgaCkD2dqD464TcvD7XapKV-k9Qa1KrbpTil58HPV6AzHVBoabFyTEAkvgxw7X64G1l6eRVJchPsBm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🇩🇪
تصویری که آلمانی‌ها از جام‌جهانی میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97330" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97329">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhDbGZrxmJF5od8hS1ggFrwz8oMIMyqL5SduyiK7CfvO1gZSmPG1hgSjWb1Dde53eUzzM6yEYgvjIz6WWoPJceQzXvZL_1oC1avXaEOwppe-XdgKhRCIVI-kqsRXTV_jdPVX5vh0MsQxFUSnJNSjdqDA3f6ni8vcrDE8QPB5qZCeY0j4gUXFew-_1JXJ2VYq-J-qj6tmX4Zr0euFwAgAzBPi_5ma3JCfhIZ3UtOvzvPxabTuM9-GOXXe0_EXhrJcQMYqms77G1LS95kqxBBNy0s-Jav4S2MxGFQ0iosXq7vHeNmuDROltXpvy2HyOhht4eF5Fm10W__ey1GJyvagWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قرارداد کریستنسن با بارسلونا تا سال 2028 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97329" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97328">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=h0b_M3QLDXw1yolK6AVUaYquv9z9KSVjV7JYK4yhExg9SMMqMvWAoWGxfz1zy-6MJ12JWYD2AnsNei2gXFMkvhW0930oqthlZ52JhYqq4bIXrYYgTKH96LPRw9AiZzG8z7EXZmuhyzx6Z1wShS_ihvaBDW-mAEiuObVPbpnAqNlwFODxT3WXVOhgrdzABqt7rslWy-JlW_CECGBlivH3fcjHxOKCD7p18UabKhR_aGDp5X20d8rlpuFnSshIfpnOASbFy-RM7-8_trC80UJHFlg340DLSCCd5XCld8Nk11A0C5TV9tITaZoyAKwx7mEoxhA2CCnasGqbXryJ1va5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=h0b_M3QLDXw1yolK6AVUaYquv9z9KSVjV7JYK4yhExg9SMMqMvWAoWGxfz1zy-6MJ12JWYD2AnsNei2gXFMkvhW0930oqthlZ52JhYqq4bIXrYYgTKH96LPRw9AiZzG8z7EXZmuhyzx6Z1wShS_ihvaBDW-mAEiuObVPbpnAqNlwFODxT3WXVOhgrdzABqt7rslWy-JlW_CECGBlivH3fcjHxOKCD7p18UabKhR_aGDp5X20d8rlpuFnSshIfpnOASbFy-RM7-8_trC80UJHFlg340DLSCCd5XCld8Nk11A0C5TV9tITaZoyAKwx7mEoxhA2CCnasGqbXryJ1va5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇦
وضعیت مراکشی‌ها بعد بازی با هلند؛ خیابونای کازابلانکا رو ساعت ۵ صبح تسخیر کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97328" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97327">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaOXW_r4ilm3LGOCrYQJVQjpYBVccZCrP0WghpnkDeScsF8FzU4hjWvog7je7fr1kQZ-NNcYP0OwLgT9CySZMibDtbcz-GGe7nPy5JlJmrhgrvHNl5z293FpMLg3RaRIinDPclM0NoFOKsyCV_UIVZd_AOWsW-nzMQ454ooE1t2PZIq528zPK1yAVOZhgaNvup8bmWvu82wXZYh4SEqHeOm6--uWFADN2c_bEeS3qXsHAhzffaDOP4bzCnfaiSJ3_lDBva6Q7D15hP6N5YCWixWBuIRhKlpq00R5WiGel8nJ7hpUf53NxMOCpU7R0_kFIC0FnqZA81BK0I0VpMDTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرمربی اکوادور پس از حذف از جام جهانی توسط مکزیک از سمت خود استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97327" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97326">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=C7MsE52Znawzau8ZhpYJ1HHZOj4BxKWhCtHP1kNbkN01RvlIm7qVtahtuFaCkq_JOehLqzJfochv8PMWQKLy3YecP7IoCbxNOSOaFlgRvZFwcpEDx4xComlOlPxWjz4FDbQKE0li-J4S_EvG7-OdftGIlD-gOQKI97k3Hb1sLklO3goayMYT34UrmYebLpMtjz6F_D7CqXbhe0OLjIUMLi-zrLAg58smwTOG0lIa6yTsxGEWKX6a8EK_CwPD7h5DNYUt-XYbdmX2jjSydyIpF-Lpb-wJSRh5-vVg1iv-27KOk8NNKWtWlkH5nsJQTf5NFBqciB3kqQ3Yv4r4Bs2mmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=C7MsE52Znawzau8ZhpYJ1HHZOj4BxKWhCtHP1kNbkN01RvlIm7qVtahtuFaCkq_JOehLqzJfochv8PMWQKLy3YecP7IoCbxNOSOaFlgRvZFwcpEDx4xComlOlPxWjz4FDbQKE0li-J4S_EvG7-OdftGIlD-gOQKI97k3Hb1sLklO3goayMYT34UrmYebLpMtjz6F_D7CqXbhe0OLjIUMLi-zrLAg58smwTOG0lIa6yTsxGEWKX6a8EK_CwPD7h5DNYUt-XYbdmX2jjSydyIpF-Lpb-wJSRh5-vVg1iv-27KOk8NNKWtWlkH5nsJQTf5NFBqciB3kqQ3Yv4r4Bs2mmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار مراکشی وسط جمعیت هلندی نشسته بود و سر صحنه‌گل اینجوری کون هلندیا رو جر داد
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97326" target="_blank">📅 11:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97325">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=no2_kKeo-ivFWDGJfWkt384Stsn1EgnY7OoBxCeyfr1cBv89rsm5k9Vtex1c3UhsI8b-SDvbb1qN2w_YTnws_P43Gd3t7OWEQvkbEzStu7JQVnk5Q5_-B9hx0P2QGi7TbzDlThlDl9SaF9Wc1LeBFqkA9dIeT9MiWD9bjka0540kycEJdmUAJAoBXUWR6cnXn2Dtt4mk12l-WwEmP_nx0s-cLGhswg_gjJP44BofHRM00qKuTp0hjK0PjjdVGCfydvtXCpRd83out1h4lhhLuY6ungyGa-okL6lq1YkgFfRp41Fru-rOjF33tJZLr28D7Xw7h1eHvkgMTSV0TmYNGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=no2_kKeo-ivFWDGJfWkt384Stsn1EgnY7OoBxCeyfr1cBv89rsm5k9Vtex1c3UhsI8b-SDvbb1qN2w_YTnws_P43Gd3t7OWEQvkbEzStu7JQVnk5Q5_-B9hx0P2QGi7TbzDlThlDl9SaF9Wc1LeBFqkA9dIeT9MiWD9bjka0540kycEJdmUAJAoBXUWR6cnXn2Dtt4mk12l-WwEmP_nx0s-cLGhswg_gjJP44BofHRM00qKuTp0hjK0PjjdVGCfydvtXCpRd83out1h4lhhLuY6ungyGa-okL6lq1YkgFfRp41Fru-rOjF33tJZLr28D7Xw7h1eHvkgMTSV0TmYNGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
خانواده پاراگوئه‌ای‌ حین‌تماشای بازی آلمان و شادی فوق‌العاده بابت صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97325" target="_blank">📅 10:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97324">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
هواداران مشتی پاراگوئه بعد شکست آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97324" target="_blank">📅 10:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97323">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=Y7lnDK7hEG9XlrBa5w8NvfKIvGvaqe2QP5JRUzcPs6UovubB2oxbpXr_IpzPT9rU7VogtU0DeF6eEK-LnOGXiXnRLKTaPYkASYO12Ru8N-CEKnm0T1cRz41GWYmO6LYtUbfjtQF0ok_nxObHwn5n3C5WYsr0KMLWnewMhrT-a0lmokdUOocx2gBS6Xye4uGe35DWmRW32xFo8f9L_RqIM96WckIrJCGTiu4Dfq9sp_IEdNStiRrsDokzA2W8D4m-YA0MEp3yxtaNjHZb6cKio6XUYU2AITse8RGuSfz9-IyUtn1_VDrt_3QG7t-UUVeNqglbmqlJMVFp7fFtTJMFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=Y7lnDK7hEG9XlrBa5w8NvfKIvGvaqe2QP5JRUzcPs6UovubB2oxbpXr_IpzPT9rU7VogtU0DeF6eEK-LnOGXiXnRLKTaPYkASYO12Ru8N-CEKnm0T1cRz41GWYmO6LYtUbfjtQF0ok_nxObHwn5n3C5WYsr0KMLWnewMhrT-a0lmokdUOocx2gBS6Xye4uGe35DWmRW32xFo8f9L_RqIM96WckIrJCGTiu4Dfq9sp_IEdNStiRrsDokzA2W8D4m-YA0MEp3yxtaNjHZb6cKio6XUYU2AITse8RGuSfz9-IyUtn1_VDrt_3QG7t-UUVeNqglbmqlJMVFp7fFtTJMFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
این‌قاب برای آرژانتین حکم دین داره که حاضرن برای پرستش هرکاری بکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97323" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97322">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37351875f0.mp4?token=Qgmi2GWzuJIfs5Hbgekr6i-jmKOxMlwwkCYlX7Bkt_cb1gKEnOMaf4OaYFK8MyakPh17YhdZbh_EzcoEwWquwZidqrPgMZB4GBlWKGHa-mkq3T_ks58R9gbe56T6vTi6zL58JyOOiNLR8Zo6-gf2XEQafSoNWB3NkRRAwM08TsZ4Qr1Biph4_i-ic3puWO9b3hzLdvMQ6fce2z8a-3wgCMWxs_aaBWWYdCmYgIY-jWXUtMs5vuE1_NJXnWIOdVBx00o2awTAqTqwyonZyZvRsSjuzOAx2XZ2bapBnUrBQ2Ac5rAc4aoa9HLBZtZPvbGqXSFqDakb3T-Z60rugPHWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37351875f0.mp4?token=Qgmi2GWzuJIfs5Hbgekr6i-jmKOxMlwwkCYlX7Bkt_cb1gKEnOMaf4OaYFK8MyakPh17YhdZbh_EzcoEwWquwZidqrPgMZB4GBlWKGHa-mkq3T_ks58R9gbe56T6vTi6zL58JyOOiNLR8Zo6-gf2XEQafSoNWB3NkRRAwM08TsZ4Qr1Biph4_i-ic3puWO9b3hzLdvMQ6fce2z8a-3wgCMWxs_aaBWWYdCmYgIY-jWXUtMs5vuE1_NJXnWIOdVBx00o2awTAqTqwyonZyZvRsSjuzOAx2XZ2bapBnUrBQ2Ac5rAc4aoa9HLBZtZPvbGqXSFqDakb3T-Z60rugPHWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
آزمایش فیفا برای شناخت تکنیک های ناشناخته ژنرال و مقایسه با بهترین مربی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/97322" target="_blank">📅 09:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97321">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIOZWfLwGrMGMhf8DfyMSamKyd9Xolz_rFGaJOWbEv1xAIs4jYcMQW3X2kys1KfoEczDEyj3s2zTSw3uduA2Rf_dexc2KeIUc0E-5uDG_du4dhqkDgl_bLA3CSCxcI2QWJW2Gi8ErI7pwMEG6uy8EtLEbK9UfiJyu-g8pnKEBGb2Bo4KFsZkysu7QVV1OYbHUuvnhMi3ibf5nramRYLLqT22LyXSu65S_QGjbcvtHur2vv0jUfKQAg_BMGX3aCduwpRdCnLDZU4m5ZY_tHwSvTuY3SdfH2amG5TZh6T-CnA_VfZkZGALTO965hdn1USmZ7FpOHA0MNXkGPaboWpMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇳🇱
آمار ۱۶ بازی اخیر هلند در جام‌جهانی که شکست‌ناپذیر در وقت‌های عادی بودند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97321" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97319">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1_GSTWlu-wwpize4IbT8y7DKkM7Kn5gD-ePvx2fzWmhINOcy_30xrWWGYPIRwi97FVrcjFxjt6p4bcZUV_4PZqSKfh38VcMPqWBEmKO_Bj8HlL777GeC4txGKVJ6PIN0qFzyN24VelB6wax0P0riV0tk9hlMSf8VBfbOtcmOv6xmDe_zpLmSMKTiwzrMa4WCKUIEGgtr4NwJEKu52EGcJ0lJWjRjCEsp5YZxnnHj6zmpQcyrb7ksIFidug0iG7fu3jRD5Q7PY5i1v6HYqns0kObPvejsZqOObel1Tv7unzx5AIkLs08QbJH5e5OjzojFGPo7ZoErMmof-6fjN-o_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXzQAwKhpfcLd8G0C_xl4JurFV_NE6HY9ckiNWSk6NMgpYrwxXF9MQUiMTbwQmuNT2A-60bzYl4A4yBVyvftla3oh8UZY2RNc3XUOOKVGVPkJgzm4ddX2SBbnBhHEFSkInIohfFSMPVoVwsDrZiqLT1rgK-Qe202TRSKjqZtdzotpZoWlaV9_pMjhjhBZ2GaA0Db7dEXdrjF0AzGZL9mi4IqI4z5F0ixPq5Kbym-3T1tbS0D39QK0Gs8CNQQBcqWEcm8-y6JO9rbHqG3Od9aHujINl1rCxvuIMVN6OZmedlDVtTEThhbifSyAfXGj9cZPykqtyrkVKAqyRH30H7sjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❗️
🇲🇦
وقتی اسماعیل سایباری به دنیا آمد، پزشکان به خانواده‌اش گفتند که به دلیل مشکلی مادرزادی در پاها، در راه رفتن مشکل خواهد داشت.
👍
اما مادرش هرگز دست از مبارزه برای داشتن یک زندگی عادی برنداشت.
⚽️
سال‌ها بعد، سایباری نه تنها راه رفت، بلکه به جام جهانی رسید و پریشب پنالتی تعیین‌کننده را گل زد تا مراکش هلند را حذف کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/97319" target="_blank">📅 08:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97318">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV4u0yHjn5VXbZENN9gmSdZsxsDzvw3UUGNQPQK2r8vn-DMkJ6Y70vMYR6CIaFdYCwpaOarX9hT8uO8QKYUAg8VpbUkMdw7JCaQeeMJov7aC9xCxPbWp1fKs_Aesp-hmXZ9DyL_NVIMK4pzBd3_omT3Wfv9XmGhiPHdA-Z1moNmD4CKDqp1lDhcVi7eZ1_HitI1whLfnp6BBUnGM7m1fNiCAlDlTGQILp8ZelXBpBY6tbaEXCsZ0NX6JQ038GvP2ELeREs44pQKwa1fFp1Clrw3GZaT1B5A0SopRuCMjcbF56lO-x8XQ6o83xDZC1LCdfGU1Yxy9RPtg2FGIkE05QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
آپدیت نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/97318" target="_blank">📅 07:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97317">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-S36QHjN55v33QmEA8x4rQBFb1f8n13LY1CpsJXwrnZ5THerI9x3yK2hVFVfIlEPcxfpef2y72VwYwl33HdMhtJuXCapg88G1VdEkD3ZmqFNOfiBeOfnV5ewSuVPGC_-gJA0IwIfHMJNRMsTYk96uOh-R56RfTeOmkjG_Up4xDj7ZZeE7tfMXLh9zqc182tLp5eCW64fFNW7YZeRBH9rnkbAje38JrduCdJ7j_xAiCn4fXtHgKuYISl7AN2e9iGtlmXQZVEBE5Jq-qWgjok-4YvIBq5DZLJEP4ExY7E2Oa46Ra3m8xpkib4v3IUgcwSlSm9ytSUBs_jiVh-xZBecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:  ۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97317" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97316">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZjrUE1bp4-SQfgkckgjMR8GTCekLMUSfUubEQYCnPccTZoS1cHCUZIYWHEuPn2VvFQogzok83UwTctLZU4YSK_Z3qlN2ZEGL9E8kPqZl4pKyE8umnTE1POkTy4lLq9s4gEDH-ovZijmR1FXqc9MO3qzycBelBSPz3jojP0MqSS8IBZVKcie28nJLwBAAq7nFzFm6-BUJFwi8Y9ZF9Z7S1F9wWaBbkJe_elD2k-Yu-sTJLPsha384bKaNz9nc1o5M1Khaxtt7v8RyL0S5EcW5p0Do7eqMBvixUl8pmmmnqnx1xVscr9XIiFiZA4A99YOS2ulz_K7x1Fu4SSBsLpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:
۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97316" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97315">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZjJy72KKmGs-10b-2cmcTmdezW3dFM9bcclgaznPnv9fiwdwoY8So7S6aINVFDvp7tcgizsaAUY5kfmWWFZk-G4vyoyFKQLrxg5r4ndPfc1tOWXqBF4EJQpxdOj7KY-GR2Hgu1v-nAHodIBHWHJoL1jIs2Rra3Vf_TbYYzK6wxd_Dsc2biW1V68jnHSpdhlikoUzVLGU9wOaAUHRQfnmacATXVTQW9FnIM9y_mbHSVDYAR7M8taxe22kbOkUf0g4UBdWzNjepip0GSj_iW6G4yZjbGYcUenwrprihtsyrsiihISMFEfRskUmbj29MCk7b4CFxS-rKqa2Jkv_O_PCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
قانونی وینی(پرستیانی) بازهم قربانی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97315" target="_blank">📅 07:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97314">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97314" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97313">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm_SNLVzuRenvJTOFuWwZLJ01H4rJbgnfFPbnNOwiYGuiAtVWdm2SeMzrz44EFOyov7vsLLg5Uimx20ny_E_wHm8RoL6iJn6tV8V0cvlqmwWOvLINS_nHFvJ2_lSCLY5w6xhUAqMxe_djRmQAKZSH6KZvTl_MCgKPQ8kY_kjewU7SDZQwo_I1Y73CuDWaDLp3UhC_1LW623GSm8K6gkYSX3uZ1PovyRNccoW2S8d5vZmPdmi1gGMPB7uVaA6aT9qFUmAKiQ6mMPQnTVmM5fCVroHZNJnVMo6kiel6xvCBfRF9_3yB1U99h7UbCysnCA8ynWtmJ9ZU3efqsysqWC-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97313" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97312">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دقیقه 95</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97312" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97311">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هینکاپیه اخراج شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97311" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97310">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=h7SmFb6mtqyh1nDWfoGnvdhFgSyJYhwaue8IfuInj1U2IFE1XlX4zTx9CFQoojY_OzYKhIpagDkLa0vW9xZDFTQQLfGfWFXTAOsaY8frSyFrVB0cs6S57SFYNZgEXbf28E2C04ozZxmwqsBhSs8QzO8BHzNG9c748H6Mahqi97IpEZrEOI9B1W8lS-WpuwH7PY0KtkCEa5JaaVC24D3WFoBG0zc-YFaOl5jMD0-ZLXpNB9fPrdSGYmIG3UUWzgNT56ufmf7gjn04cZANvlU02GqG4OynnRuicFeotnLW1f5FWPeDRK6pg2Gm1WAu-hYk5YdDs3QRPhIRzgO-gMrEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=h7SmFb6mtqyh1nDWfoGnvdhFgSyJYhwaue8IfuInj1U2IFE1XlX4zTx9CFQoojY_OzYKhIpagDkLa0vW9xZDFTQQLfGfWFXTAOsaY8frSyFrVB0cs6S57SFYNZgEXbf28E2C04ozZxmwqsBhSs8QzO8BHzNG9c748H6Mahqi97IpEZrEOI9B1W8lS-WpuwH7PY0KtkCEa5JaaVC24D3WFoBG0zc-YFaOl5jMD0-ZLXpNB9fPrdSGYmIG3UUWzgNT56ufmf7gjn04cZANvlU02GqG4OynnRuicFeotnLW1f5FWPeDRK6pg2Gm1WAu-hYk5YdDs3QRPhIRzgO-gMrEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
مانوئل نویر در ۴۰ سالگی، پس از حذف آلمان از جام جهانی ۲۰۲۶، برای همیشه با پیراهن تیم ملی خداحافظی کرد. او که پیش‌تر بعد از یورو ۲۰۲۴ بازنشسته شده بود، برای آخرین بار به درخواست کادر فنی بازگشت و آخرین فصل از یکی از پرافتخارترین دوران‌های تاریخ دروازه‌بانی را رقم زد.
◀️
۱۲۸ بازی ملی، قهرمانی جهان در سال ۲۰۱۴ و سال‌ها الهام‌بخش میلیون‌ها هوادار؛ بعضی اسطوره‌ها از فوتبال می‌روند، اما هرگز از قلب هواداران پاک نمی‌شوند...
Farewell Legend
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97310" target="_blank">📅 06:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97309">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شروع نیمه دوم بازی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97309" target="_blank">📅 06:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97308">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏆
پایان نیمه اول | مکزیک 2-0 اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97308" target="_blank">📅 06:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97307">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مکزیک هم هوادارای خوبی داره هم تیمش زیبا فوتبال بازی میکنه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97307" target="_blank">📅 06:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97306">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آلمان چقدر لوزر بود که به این اکوادور باخت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97306" target="_blank">📅 06:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97304">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رائول خیمنز
🔥</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97304" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97303">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مکزیک دومیییی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97303" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPdG_ISt6wYCQ-YHMd6XmEKcHVjgezbPV_H598bHuHNPLAz09MBgDWA5RBNZnfsX2sglSeMnHLw732JeMlUQys-c9lqOmezgFUX4QYH4fP9lKdH85W14lwTGDJ3HNxPjyLdD15Vea2v7j8DEk7pwGNkqBUdIoGv2_MrDXanQMPkz9rv__OMAa6XV1QXEQJJGCSJZ0fwS7kf2hj6Hh8cu5ZFL7FMGfgKdrpBmHFlZIFISBNZVv1WyvNFtgB45wbaEkcFpzSnw1XCX17oB12IJ3aMnxhBJqdwRJjHy0MY77-mM2JAs6yLr0AgLVptP1g3a1n_Jt2AwJFK39FsjNFllFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRFuiRmsypU-k9zxA0dJCqQLeI5fxAUh0taacyMc5Cs6mKZdOQMAMgwxK1LP_EfYlg2fDDjaRzDZmLINjIe5A23FU092GqpKY2MMkNzADTkUscWFfDjy9P9iSuFaMM4bukzIQucx3zHqRF3YRoNYslw11hl8GpyNKLxguu1R6ytwh-fxxSDRKMZYsekQblff2O4dWovCfzmVQUIsgD_t7QDLcI5HnfilpPsz9d9TD0wU5HE-qtji6EbyHDUe4HimD1STvbUVt8_uvb8923w-tYchjVnUkVCGhghYIxmCkQJospx6GAzw5ticEPWx5i4KJjFbo8MNExAjC8dkGB_fYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تمیز از نظر پسرا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97301" target="_blank">📅 06:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwZLS5y6qoA7q3ce3mUoLFgWGL2qCzj9sKox0VuNKtBWn_Ud2quCRCXG1UOyypW4dc2nD70olkUFB6ABgfJaISKSW2ehxCt0RN-bvdNHWTVz_JerhxzYViaV_sy0a9e9VSQ4rYiWAbBUwEQtSWsc0ByUkb82EI3SOSE-DeqJOL1HGQNu5e2lfM4n6O7AiLIPt5iOs0jWGDHzaDzO9tOyo0UF2nZQl8PEqBiXSDZwjRLAkkS0r_KOalJGLtHecbhV33c00h7WW0N7CwJ05_2UvfKd63hauzBceFA4NQG20ohQR0gpbkdnwpn7EBVQfbDB4V3h5sJyvl-n854F7aSdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خب خب یه شخص کاملا جدید اومده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97299" target="_blank">📅 05:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بریم برا شروع بازی اکوادور - مکزیک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97298" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnZllbTn7AjLiLfWVZZUEgPFYuEcO2kN_OO3ZGGSKtB-mdr5fi0aTJBJIpOtuy9HKumh7_UVsiRjqs78VZaUaP08RYvUD58Q9v-kuFYKtmUBSxvSALIYOrxTP7poxBbqMtJf--DS7MbpA6fSS-SNF0VAJ0vcKAX40NpkcO2TO-NdbkgUJtdxhfwnB5RCIFqk58r8Ah4inX50qN-As7V_dnm22iXA-xPAexZGialqpTlCdxd5IJzXrwirTcrqPzkIbo3NTzi0XKGRzk1EhT2WgZhgcufehIlb9Fg6w3K8CsjpCrAUjRW3guxjipsytVhp14AfM_Y1e323hZDjHK4nQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
امروز قرارداد محمد صلاح با لیورپول به پایان رسید و او رسماً بازیکن آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97297" target="_blank">📅 05:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01873d097.mp4?token=RdnIj7TzXJD4fNGnmFnq8W64D3195AoCopHDo9GEoGeUG7cQ6qjde1bKaOdtE3jerABJx0cEC7INNiTpgfHrJxKS2rmph0BgV_dwAMDb6lK2eSvjYreu4TgpxoBQaoSQtNSl-OvkTUPrt5iooC99EaEIK91vuMMxx2nNcYcOqY3AINlQmEx_d50YvMRzLeKpH3p8hk8uIy_-4PO8pgLLAHm6JmLduURr83W9PnATCdv_SGz6oYq4peFAy4GCdCXjhDRMWJuM4UDmhUr6OUIFxG-4-pIVNXdorI6-i0f4ZZ4EzFcGFBrO3wHmBiD27NMHp81zvWjDn1wcTrbBBYg_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01873d097.mp4?token=RdnIj7TzXJD4fNGnmFnq8W64D3195AoCopHDo9GEoGeUG7cQ6qjde1bKaOdtE3jerABJx0cEC7INNiTpgfHrJxKS2rmph0BgV_dwAMDb6lK2eSvjYreu4TgpxoBQaoSQtNSl-OvkTUPrt5iooC99EaEIK91vuMMxx2nNcYcOqY3AINlQmEx_d50YvMRzLeKpH3p8hk8uIy_-4PO8pgLLAHm6JmLduURr83W9PnATCdv_SGz6oYq4peFAy4GCdCXjhDRMWJuM4UDmhUr6OUIFxG-4-pIVNXdorI6-i0f4ZZ4EzFcGFBrO3wHmBiD27NMHp81zvWjDn1wcTrbBBYg_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97296" target="_blank">📅 05:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhTAyF5Np9lp4cltgZnXfyLHJbtgul2Of1tk7wsbLcKorNw9dVIshSAYv22oFWgirP4uzOk3yKfO6siDMt26GJ6CrEI6zTRhXz0UF8h8HfKLEvq0Y6UZzD8pxYW8efwXeWaN9ypcXD8V5QKWYBjyipK_JNmtbo01HLzer3NydmAwhakxMMn2Jx8Tt30hVJH9cCpBcVIxpxLsnb2vRTPNSwclshWgr8IoLnLquWKx60VehOALOdMjHUCPHf-AzLEhzbOOn3XYw9y_6BesYlKjegYBdkML1JycLwhyFVUdT429sACaZ-gOJua-AfqTdsAygKXTLvzyceGI2qlYOAu_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه حاجی رعد و برقو
⚡️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97295" target="_blank">📅 04:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNzgE2TzO-2rXYKKVUbR6LMSuC-OjkfGpl5rIfAuizMuPhK4iCF0G_cgwx_o2ckdW-wqDmHriCjWGLHWLmYcD_OzXAWQRNk56_6NadzQpbZcxZReyohqj5vVnINiUmmWSvKn6AfvXW7_xkPpZUPdFPkkF7gqh8qXBxoD610MThod89XsAw7vfyt9xKWTN0i2BotwmVfEGNQoWQ6L8UuK3n79yGF5uVejfd9iiKweH4W2hzJ1p1KclVTZFanSakGupefDpWgNjYL7Y0XZhckmIlle5qcKinjoD6NCjk1n6bnrF5fqJVaaQglsA30FzGajSg0iG1yvBgRQgwtjBS7CYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
| از زمان اولین حضور امباپه در جام جهانی، تعداد گل های امباپه در مراحل حذفی جام‌جهانی برابر یا بیشتر از مجموع گل‌های تیم‌های ملی انگلستان، پرتغال، اسپانیا، آلمان، هلند، بلژیک، اروگوئه، سوئیس و برزیل در جام‌جهانی است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97294" target="_blank">📅 04:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=gmiViZpxwhYe_laGL6Xgpw6yaEsn4bwUFRMySARi__YUoSQGQvdAOS3OrwaOmP3SZ7zWJGM4N2BOxIg1tzw6U9CqA1KmxAFcR2905oJ0mVALK0KcdLggo8yuJ6mo_v6MOvNZqIUO6pd47hskvK07JFNzNFUaBcZSFAdAPcIdCTbz91Hf0XKQ60JcMdMtYxCgzdLMhCYWTYVLNY9LxpiXKk6AH360SDwoVHjNSQ5P3iaFQDPKoUenMAwhcOyGgillpHU6tQ1JubeKjIccOOy43IaiUxI7tQ-VNnriXW9J7Y-AcksLFWMAvOlBO8nhTYUlYxCKpbdlijHJvmeLzCnRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=gmiViZpxwhYe_laGL6Xgpw6yaEsn4bwUFRMySARi__YUoSQGQvdAOS3OrwaOmP3SZ7zWJGM4N2BOxIg1tzw6U9CqA1KmxAFcR2905oJ0mVALK0KcdLggo8yuJ6mo_v6MOvNZqIUO6pd47hskvK07JFNzNFUaBcZSFAdAPcIdCTbz91Hf0XKQ60JcMdMtYxCgzdLMhCYWTYVLNY9LxpiXKk6AH360SDwoVHjNSQ5P3iaFQDPKoUenMAwhcOyGgillpHU6tQ1JubeKjIccOOy43IaiUxI7tQ-VNnriXW9J7Y-AcksLFWMAvOlBO8nhTYUlYxCKpbdlijHJvmeLzCnRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی دنبال دلیل درخشش امباپه تو بازی با سوئد میگشت؟
🙈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97293" target="_blank">📅 04:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKOWz0IdkKFpomvJJ5p0s3pxQENyaF-WM8izZCssFr7yt2pEEHaTN8fkaeDnqwgeUQvQjX5LV6gnwH1H2oolsWLEH6ak80sNIdL3xBsnC5aHfe_OF0cVFXrcayFMxhu57hCn7bideFBk-mJK7nTvx89XAdEqywLbzGsHfRGHtF2csKCOYwQA8WrNOFsndNfP1OD-GI8tgjUoYr6_fkj5KPy9nx8pCCd2E1vl0fRp5_3qu9Yr6x14mLNJjHoTV4Yz3nlHyHQmmaDXZc6gXyGeT-Db3ERTINHFZVsb6h9MS1M1OtSpKZV_KDOFL4dTVR6PTU9_VgLc0H7mvo4lZDzrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به دلیل شرایط جوی، بازی اکوادور و مکزیک نیم ساعت به تعویق افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97292" target="_blank">📅 04:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksboB5NC_W5B4RUro847fwz_s5hrrN-SHfVBwk434uJnrFodVwJ4TI47xq8t8FZPPgWvg_1ZPUMz8A49uN5AJGSEOfrIfOmrhtvA4iI54R4dfExa_rSQG7xXWoZYiWPKzRZN0nyAtZIC678JjMgsJh1s8EJTyO9ygAy1oYwFoW6TyEpmViIAUuNfrM8D6omu0p1_M_SFUAD8P6TYic50mBFalqM5MyjlBuM-7DppA77bsyrjnA9AdTFAZ1CaDxaCLYbGaLgJ0OEeKR40AX-YryEbPiHTmRQnBpiXgurUJto0twZ5oyowvjPPjm522CvsqK732MeChd5X7vaZF7_57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzyGNJ3XS70xL0Gx6Xn18NTrI4MaGxk0XqcF-EamJ-9IPFJdhmhN0Yko4VD7WMFR_njzXP_NAtqYTTM0nXHp0u5Iv6MiyaaA0NeP8_QzfUwz7Hq_vv8vep5Gxz5TeQ1MEeP51wytBfCbIqA5J6VF2U7fQqtdlQmG2twAsq-9-zyE8hpnJW2lT1L6g01VM6uqhq267PkvU4PZimqwbIOqKZ1as2wOev8QOdX4c4osqdwHNbDS3pjstbu8r3AOEFEniUILBSnTGwE7DgUKLla1LvkE3TAoJ7RbspoekpPvR7L6zovBjDSIWPIliz_T7DVOYJ9-h1EvBt1cfosc1Y-NDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇨
🇲🇽
ترکیب مکزیک و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97290" target="_blank">📅 03:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZW4GqNIX5STgO15BPoIUmTAfReZIgY9DDasO3Auzd5_-h1YkCgtzhjWJgdiF0F3SzMjHNdQhKN6Up3r0vLIqYJegyPZJnSll-8L9txVSPnSnv7zEdXKvI5JmCfzNkG0WwvPALYo94EDPoED_ByXUF2P8hvlL_6vFd896yO42zug1uY7WVPzGD5xrjLForyPIMq32mA34G911Yxmo3OljtDaow-3WNo17BMjgHLhLV_55l1k19IgQKwybOwc8UgToj1Ebi8vMe_vHsxRIH2nS7YZDUjTNlgUvQvrrzZS4BXoUYUVxTB36WvZzx6Ae5EqtlPNBz9-I5EExSGsh5QEhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d10hGODYHcXzR-yCZkRQXTQTuGbcEJZ0PgH-ED1j0hRWquLijkgMPtjJn0c1qxbYCEnw8b9KW3058HrK7EXY6W5jAUPeeNz6fF7nK394XF6Cm4MbhdVF5rFuM4tswgJFhqGszkMiePPejTIJA95LwocmoqLkIqJms12LfDe9tPhqHOfcN1FYPD0GjRaK8OXNzixNt-jTwLl2MQM8ZOkiHXaVkZOIWgki5F2bCunwTcqGL8P15s8Gsxy0MCSckbjyTdCeGqr8JC_QGYCX08YHdObjyVwmguTKiXbsBUvk1cfSzzN0rivc425bUllTaHWMmAySuaagtvrZ0axniQg60g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رایان شرکی که حسابی کلش از نیمکت نشینی کیری شده اینجوری دشان رو بعد بازی به تخمش گرفت و باهاش دست نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97288" target="_blank">📅 03:11 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
