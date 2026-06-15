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
<img src="https://cdn4.telesco.pe/file/kSSYCMxRQ3ZabGWMtc8p1Rp023JJtPm5kAYcFjrM9zVT4SNACixkbA8cdT66mQUl8UzwYU3Yl_VqRYa4UOO-PDssssI3tJNoAA020W5ucMEWtF7GIpQreeoqVJgzfsqyYbuLF4ziGCfXo7xxBUN7Ff-xuuu1gGB5KFa_YP7K1pewm4WbRJCiCWRmKOeG0sxqGo9cqqPBVqCrLwEGfL_Mo5mT_0zYjj81ndUiW6M497nJmFq5O7h3G8NPhWB45e9xKj745-t3NUhMVSehJ-Y100deKGTZOIx5SB2hQVpToM23XjDeMNTyUrr1_EqDVjGzkSeM39Y7G9Wl038qciBeAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 01:29:10</div>
<hr>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=E-jd5b7twkM8Zx4HDkWmYAzJBs-o6qKMC3RNXSlOfX1tltpBYzjl5AOs_8b-IWWuOaxSr5GOEkfu2-iHf3_eRqdMLkxQVH8ibnJh-dAbiYF4XJinYZElAWdV_8FIhIgM886tT8Uh4O_ONQRPOtmDsJvPhFHq5QsbpNzROGR8O5sUeCOeytiKLkc8McMq1vUWNEIu0dN_R6n_BPhRfq84ZOCADxssoRRSMh8QMk1pS36f7g7fIAJ5-oYzO6RTqDe9cbiZCME6nnbaeA_kM9lvwBX1lUNYSPX36SfHaQX6oI5EOpgcMxeMehhhItWe-_btk2rQA4HKTkhF718kEf5UcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=E-jd5b7twkM8Zx4HDkWmYAzJBs-o6qKMC3RNXSlOfX1tltpBYzjl5AOs_8b-IWWuOaxSr5GOEkfu2-iHf3_eRqdMLkxQVH8ibnJh-dAbiYF4XJinYZElAWdV_8FIhIgM886tT8Uh4O_ONQRPOtmDsJvPhFHq5QsbpNzROGR8O5sUeCOeytiKLkc8McMq1vUWNEIu0dN_R6n_BPhRfq84ZOCADxssoRRSMh8QMk1pS36f7g7fIAJ5-oYzO6RTqDe9cbiZCME6nnbaeA_kM9lvwBX1lUNYSPX36SfHaQX6oI5EOpgcMxeMehhhItWe-_btk2rQA4HKTkhF718kEf5UcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=i7_E4logdc-FcDF9A_VlSSjmWvddgGExd0AxiWJga0mhyh4SX_2dpksXB99aczuG_o1OZJHmgxZkDprX1-UaK0PYcB523kEoUl_1Ptx7H3v2HzbuOEbS5iMXTz1b7p-xOcuUI81ps6CBskW7CaVFHtzSTj5KhrpapwTWVL69yq0VkaoFWFCmN61qHtIogsTTBlDsVwa5pDjjsnAuUr-X2xqnn50pDgnnbrnChc7nTWmvlslnulbxXwdSW_9eyjbpUMxj1UKwwbNjfzInMNLjyWLruq_yUu4KSsk-qMocB89FfIGGYiE5Ra8B0eLLdIXdJNw15LoSXgDMCsczNPT6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=i7_E4logdc-FcDF9A_VlSSjmWvddgGExd0AxiWJga0mhyh4SX_2dpksXB99aczuG_o1OZJHmgxZkDprX1-UaK0PYcB523kEoUl_1Ptx7H3v2HzbuOEbS5iMXTz1b7p-xOcuUI81ps6CBskW7CaVFHtzSTj5KhrpapwTWVL69yq0VkaoFWFCmN61qHtIogsTTBlDsVwa5pDjjsnAuUr-X2xqnn50pDgnnbrnChc7nTWmvlslnulbxXwdSW_9eyjbpUMxj1UKwwbNjfzInMNLjyWLruq_yUu4KSsk-qMocB89FfIGGYiE5Ra8B0eLLdIXdJNw15LoSXgDMCsczNPT6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=OnNR5opWUHZBrxNunIiqRiOAU1AHZl0NvS3bAtzwrH4Bn1jtZk2TPN-uMS2SIt6_ZznccGwYqf26AOYvp_qczbk7Koq-I-QdkvfUEmyjXMfYL_yN2j0R18PACqB6PJcSl7YGsEiU075X47K_NFeZWcV_1F3WwOdUdBkGBkZop6JcbaMylqDQkPI9f7v5a8uTw1KJ_GfmV2XNXRcgqQ2IQqlqbmG8cpNGay69Aw8T767psTqMeVJKyJ3TGhXvHOCqa7uXWfwzNQ-h3Srs7Hl_q-LNbueGAl6Ef0RD2SQmNE3YGQpmeulqPSQc4DSVlHyMG1a5m0UIYuHB49j8u979zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=OnNR5opWUHZBrxNunIiqRiOAU1AHZl0NvS3bAtzwrH4Bn1jtZk2TPN-uMS2SIt6_ZznccGwYqf26AOYvp_qczbk7Koq-I-QdkvfUEmyjXMfYL_yN2j0R18PACqB6PJcSl7YGsEiU075X47K_NFeZWcV_1F3WwOdUdBkGBkZop6JcbaMylqDQkPI9f7v5a8uTw1KJ_GfmV2XNXRcgqQ2IQqlqbmG8cpNGay69Aw8T767psTqMeVJKyJ3TGhXvHOCqa7uXWfwzNQ-h3Srs7Hl_q-LNbueGAl6Ef0RD2SQmNE3YGQpmeulqPSQc4DSVlHyMG1a5m0UIYuHB49j8u979zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66216">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYncUEsVXN98Z9dmhbrV5Fv7eNI-x6opyK4rGyylb2MwYmjQYhFF5at473KHQUXYRnP4C54coO8_-Wckev37sjYX_XOfLi42AB_peVEoCMAlrqccT-tpnNoKqdLV9Q20BrZV1cYeqrr84H8c_RbTt5qUNbsaz61qrSjWLLysD9jsFV-aUb4Fg5c2Sbiak8KD9vlcEiNoCR3l4z7bTIAoolhbRx9jdUHUsnHq3BiosHDUad2L7OCn0E4JwpFfGqaHhXrIKYBsATUqnh7kFcRrSMtLdVFMMFSZ6_466IH1TdtNSMFYD-OFvTPhWOT1xGfa49khibHWYKbjuqO433z7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66216" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA0Eyc_w-ODFVcjTKLqZlKLnpoZYaYxPzLd3jU4LmWsvElV_52fRdJKpcY4GzV2V2aJVrSVBwOFvYZN8L2NZvFytsZS5t1pOz0mai7B6xz8iwnqrd-M1QNCt5XQkbTlFB2Sfmmt-ek3FakWHd1MBYkl20myCWoy-vbju6H6kIY9A3qfHr7YzAsr0YsY-SDZ6DkhzVsQsCZb6uzfkgJ9PLpotLGdFDKotr0tj5XW-6BmulcOtVUikLAoE9PPXIVwc0d_ADu3uVlJUveLCCSQlLUpSwstSAcN5Z-NNJA20TjVcIbeuFRDJ3uhyT4LsWuDEGnbSDbjWauoCnXCeA6OJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2Tbkwx1mL37p63biNJJYlZ5LWlZXCEW5Obxd87vmbUtg7uGxIMQUJPRODAogAqNgPVXZzn0inEAQ7_Kh646vA8oLw5GVGobvmQZ-_5qWH1cHfljtf6DbJalMhfukZPM-y9ydJH61149Du1mm3_07imPkB6UzJ2g9Ma7dPmrbcG2HLPSy71nGVZuMlIae-oEDAa3CVmN-5tt78roEKGx_ABzswbyzcrpOu2pYjEAMuNrPZ0KocYeGfjV3X46ANw-y7-3AFtalkUKY87ypilLI34_10YetBPiA9ovdGna42nQTUXqzd3YPvpI0xtr5FBr9QZWSGsnyo1bxMQVAOvLjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=S_e2H4c9NxJ9aLZXUXujXdWIqt_OSI9brE1_dPAs1Z9S37YTAFkna--CKl6XByGeVmJdpJ2aGZeqnGZXQLO5a5gsYrfiSLyCGc__dgI3GGZv6qDYzSjjGSyIwqqBeKEeFgyFSEO46S7cDpWlENqyRBbKzW_qP0F5SUUUKgWcsLtRz63YR0xOUc4VnAvtoX7GR24Jg36ReFHb2serbC37lbHa3hCoX_93ZC5uvS3N8dKEDaZHo50xdNWAhwNzQUKgkqKYsDnHQLmpi_LUuoSAysq9uGcDcGTcEoqjbeiVaefk9KbwGpMVAUVVucPbuB3oz3HTDLvLUkEeJhyn7VN7xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=S_e2H4c9NxJ9aLZXUXujXdWIqt_OSI9brE1_dPAs1Z9S37YTAFkna--CKl6XByGeVmJdpJ2aGZeqnGZXQLO5a5gsYrfiSLyCGc__dgI3GGZv6qDYzSjjGSyIwqqBeKEeFgyFSEO46S7cDpWlENqyRBbKzW_qP0F5SUUUKgWcsLtRz63YR0xOUc4VnAvtoX7GR24Jg36ReFHb2serbC37lbHa3hCoX_93ZC5uvS3N8dKEDaZHo50xdNWAhwNzQUKgkqKYsDnHQLmpi_LUuoSAysq9uGcDcGTcEoqjbeiVaefk9KbwGpMVAUVVucPbuB3oz3HTDLvLUkEeJhyn7VN7xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش‌ها از سقوط یک بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا خبر میدن.
این بمب‌افکن دقایقی پس از برخاستن از پایگاه هوایی ادواردز دچار سانحه و سقوط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66213" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6_H1GloIOqtez2dFGZIDMzRX8fy45E5YVtCJ31aeyP4cJJcSBnshunbm56NQ0ytyCuoDXyFkkYxHpbf-rtvJeIZOe4_OBd1KfZkuMiZkBiudjtKixu4TbdLS1jLDtF5QepWw1-eAQdm25qKBRnYzEeq3C8A33S6lnsDxfkXv55rTjKhru9mYWR7DMS-fPSGdO-Qw0I2vMLzPvmfedHYEcNkyvTWmJNbezgq95ZGfHqjfYVQ3vkWUH4Lh8w43bzzJgx2X2vtdY6WFAPygRhCB7iviJz_3W7dXO8wTEQVEWXYYDn5azULryBdZKnPyG0TLrsFVvMiA7i9NTAIQOh6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66212" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=gUOHxxatcg_wy7AqQSTE4mPHCHxoPaU_Niw0eL_LpTc3z-ABzrLeYcXv56GXxPJk-HlifR51uT854_SsnzjCq5d029m2xhEJ2WG5nbTCDjBm-7dD3yNp90rrpnXvWkkCZ3h7QEio5w4DudJADGaV08La-2lD2R0gHdwhpuDJXg6hahebNmmiiHaar9CBBDoUCSrx9psgA1iBwi5FUUCyblNXch6juBk-4hexNtkqyLBio7SfU1I7qdtNIy35HSZAAEG4W8JNof9IjCRYUEM_fQeON4O_hVMBB9V-FMaWajlIkJImTDyPK-D7j9tBrMacn8w1oKZNLiYsRQwH6EKGmZR4B4mBY_BEfY1dwm-OdIwPyONPeWBrkJuLZsj6mEGYGaUpb-VfDiACUmTzveR8V35y28u_rz8S_tnUP501OQtHA0EOWNGgmGwlDW546nE2Pj-j9z3N_oqiWyw1iJOeySO-BoA_FyfeuYJkfQznfVRs1ZbgZ0QzTrOZ4eFcgj9rFZx_Rxx3LDYPkmrAoRfFz_1vh5_oSLo5TPooR-rVLIgHgJKkB1vr1j5qCmWfsKl5RQejXhqm8rtjjn1SzehqUEN-49XDbagKLLMQwWSy1oO48P7rVEdM51fpbzdYRQHncSusINbMI847DxtE78bjLKelqJzbNW1x3gwsH4vZi0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=gUOHxxatcg_wy7AqQSTE4mPHCHxoPaU_Niw0eL_LpTc3z-ABzrLeYcXv56GXxPJk-HlifR51uT854_SsnzjCq5d029m2xhEJ2WG5nbTCDjBm-7dD3yNp90rrpnXvWkkCZ3h7QEio5w4DudJADGaV08La-2lD2R0gHdwhpuDJXg6hahebNmmiiHaar9CBBDoUCSrx9psgA1iBwi5FUUCyblNXch6juBk-4hexNtkqyLBio7SfU1I7qdtNIy35HSZAAEG4W8JNof9IjCRYUEM_fQeON4O_hVMBB9V-FMaWajlIkJImTDyPK-D7j9tBrMacn8w1oKZNLiYsRQwH6EKGmZR4B4mBY_BEfY1dwm-OdIwPyONPeWBrkJuLZsj6mEGYGaUpb-VfDiACUmTzveR8V35y28u_rz8S_tnUP501OQtHA0EOWNGgmGwlDW546nE2Pj-j9z3N_oqiWyw1iJOeySO-BoA_FyfeuYJkfQznfVRs1ZbgZ0QzTrOZ4eFcgj9rFZx_Rxx3LDYPkmrAoRfFz_1vh5_oSLo5TPooR-rVLIgHgJKkB1vr1j5qCmWfsKl5RQejXhqm8rtjjn1SzehqUEN-49XDbagKLLMQwWSy1oO48P7rVEdM51fpbzdYRQHncSusINbMI847DxtE78bjLKelqJzbNW1x3gwsH4vZi0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
مصاحبه با رکورددار عمل جراحی در ایران: بالای ده میلیارد خرج عمل کردم که همشو دوست پسرم میداد!
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66211" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=oBG19kfbsvrW_wZxdekFd8SLyJYUUKAW1NUuW2O8Q5zvEzzCK6lB6YHUu1yLRFelpT6gEHgViykb5s-PGhEkYXUd0OPcILwm73L5BP9Xaz4GXgXs3RSlh0aPf0Sk3VcsgIUFEXv9i51A0NtCPQd7N3jrHnwaG6IYbi0X85q37CDIl5nqI4zLgEGC8uxtBKFveccu1adMV0I9ueZA6My9PuigyEuP9d2Bdwhdaxbd4hoa1k1EXuB3vU2QKifgi52pUcXq8SNlNTCn5rSqwKeo8IcHd1g-l1xL7JYzc_NQdaXJENSPT7YxjudfyIpoEBlicKTtfZBVMrtLxpXgrWRmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=oBG19kfbsvrW_wZxdekFd8SLyJYUUKAW1NUuW2O8Q5zvEzzCK6lB6YHUu1yLRFelpT6gEHgViykb5s-PGhEkYXUd0OPcILwm73L5BP9Xaz4GXgXs3RSlh0aPf0Sk3VcsgIUFEXv9i51A0NtCPQd7N3jrHnwaG6IYbi0X85q37CDIl5nqI4zLgEGC8uxtBKFveccu1adMV0I9ueZA6My9PuigyEuP9d2Bdwhdaxbd4hoa1k1EXuB3vU2QKifgi52pUcXq8SNlNTCn5rSqwKeo8IcHd1g-l1xL7JYzc_NQdaXJENSPT7YxjudfyIpoEBlicKTtfZBVMrtLxpXgrWRmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پای تلفن به دستیار نتانیاهو:
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66210" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین  #hjAly</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66209" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
🚨
🚨
نتانیاهو برای استقلال نظامی ارتش اسرائیل بودجه دیوانه کننده ۱۲۱ میلیارد دلاری اختصاص داد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66208" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین
#hjAly</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66207" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=ErNE6wkOdVnN79NlIbiZuq7XjH3cLR7OfeAYe8Xrx6ETneKAMni8nrg70zdLKMJf31hf8pw1s4DG9i0PEwc_PhrqLibDvkSj6Iruc1Fz5BeXrx_pbVvGPGyVguE-W7v1yIA_O6oTxRLsgQBkySqEkLvQy_yI3zt2NqrY9J11muQhIUwWg4iCeBQTbuevwYcG-Q0ecUtL6mPGo81nxE1z5bYxIHCDZQdrymklkXT2n3v34rgsMtDZfRpLP4xkAdSNVMODHL93bX-bJAJxqDxYd7GAAtQp1Jj-_udFtY13bskNXLzGs8SRDZdBgxmS5vQ4Pf1t2JhhvChz4MIWgwzHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=ErNE6wkOdVnN79NlIbiZuq7XjH3cLR7OfeAYe8Xrx6ETneKAMni8nrg70zdLKMJf31hf8pw1s4DG9i0PEwc_PhrqLibDvkSj6Iruc1Fz5BeXrx_pbVvGPGyVguE-W7v1yIA_O6oTxRLsgQBkySqEkLvQy_yI3zt2NqrY9J11muQhIUwWg4iCeBQTbuevwYcG-Q0ecUtL6mPGo81nxE1z5bYxIHCDZQdrymklkXT2n3v34rgsMtDZfRpLP4xkAdSNVMODHL93bX-bJAJxqDxYd7GAAtQp1Jj-_udFtY13bskNXLzGs8SRDZdBgxmS5vQ4Pf1t2JhhvChz4MIWgwzHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
من نگفتم هدف ما سرنگونی رژیم ایران است
بلکه گفتم که می‌خواهیم به ایرانی‌ها در انجام این کار کمک کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66202" target="_blank">📅 22:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66201">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
نتانیاهو رسما اعلام کرد که عقب نشینی نخواهد کرد؛ نتانیاهو، در پاسخ به یک سؤال:
«جمهوری اسلامی می‌خواست ما از جنوب لبنان عقب‌نشینی کنیم، اما من بسیار، بسیار، بسیار قاطعانه امتناع کردم—و ما این کار را نخواهیم کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66201" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66200">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ترامپ توافق را با جمهوری اسلامی منعقد کرد و این تصمیم اوست و ما منافع خود را داریم
آمریکا به تصمیم ما در مورد منطقه حائل در لبنان احترام می‌گذارد.
روابط ما با ترامپ مبتنی بر مشارکت است و نه بر اساس تصمیمات تحمیلی
ترامپ رئیس جمهور آمریکا است، من نخست وزیر اسرائیل هستم - من از منافع خود دفاع می کنم.
مواردی وجود دارد که من و ترامپ با هم اختلاف نظر داریم.
مهم است که از منافع امنیتی اسرائیل به طور متفکرانه و مسئولانه دفاع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66200" target="_blank">📅 22:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66199">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349807e03a.mp4?token=DEdy2cXzf288V5skbmWDY5QmOJQX76QCHzesEFeErw5d_yz_SNQdpBrb1jwBx8VtXIAFlvXWwMOmyvlGqGcr6iIbIexjIgZpDYxxwT-5VbRwCU0_nffRpqVYX8H8QxMV7wr0Cq3Uyeob7rZ4GRE5iNrWLhlz-ff2UEjuh5THbKK5yZcWZ2NDZocxuvWpRnVAaf0ewjUkIu2GkXsVLl1sy_R90RR69POONMtx2J4sTpGg9BReCODDknPDJRNFdI8EJoSFEyxty2pFS5AC3DdGq9JeL9g3zuZ4At7BsEX0E7FNruJmkdxPMp3Hp7Kcht0qPnxbsd6NMYnVCcL0e-uLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349807e03a.mp4?token=DEdy2cXzf288V5skbmWDY5QmOJQX76QCHzesEFeErw5d_yz_SNQdpBrb1jwBx8VtXIAFlvXWwMOmyvlGqGcr6iIbIexjIgZpDYxxwT-5VbRwCU0_nffRpqVYX8H8QxMV7wr0Cq3Uyeob7rZ4GRE5iNrWLhlz-ff2UEjuh5THbKK5yZcWZ2NDZocxuvWpRnVAaf0ewjUkIu2GkXsVLl1sy_R90RR69POONMtx2J4sTpGg9BReCODDknPDJRNFdI8EJoSFEyxty2pFS5AC3DdGq9JeL9g3zuZ4At7BsEX0E7FNruJmkdxPMp3Hp7Kcht0qPnxbsd6NMYnVCcL0e-uLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏نتانیاهو:
ما تا زمانی که لازم باشد برای محافظت از کشور اسرائیل در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم، باقی خواهیم ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66199" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66198">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=nLBQelRDRhUCeqagUZb5KWL_EiNOZqgH1y9S77FbbQlBmElvMXP2HQTPZ1cyXeewPj_qgU7ap-CUdnrz5XfFFfPJyQ2rpUmokT1xDiBc3o5NhRs6eje9HthdfmuNmKQRVede2MVeX6mP5pd1j0tCikrxp09TWErrNTwg6pSQLx7i2jtAUqdwvy5KCUQEZXXhxbKio2xiaInQhaM4xgHV_YAoB37L_bttltlO4NzJ-ZdSyemGeEwJU0ctlF0f3Hzr_wFyV5vmsUppWczO_cziKIPJTotf3M-JAHJLSeJgm7JvSlHEt9GqudTya7ZTNTPS9xrg3fy_hJN3x_GRIHgEJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=nLBQelRDRhUCeqagUZb5KWL_EiNOZqgH1y9S77FbbQlBmElvMXP2HQTPZ1cyXeewPj_qgU7ap-CUdnrz5XfFFfPJyQ2rpUmokT1xDiBc3o5NhRs6eje9HthdfmuNmKQRVede2MVeX6mP5pd1j0tCikrxp09TWErrNTwg6pSQLx7i2jtAUqdwvy5KCUQEZXXhxbKio2xiaInQhaM4xgHV_YAoB37L_bttltlO4NzJ-ZdSyemGeEwJU0ctlF0f3Hzr_wFyV5vmsUppWczO_cziKIPJTotf3M-JAHJLSeJgm7JvSlHEt9GqudTya7ZTNTPS9xrg3fy_hJN3x_GRIHgEJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما آسیب عظیمی به اقتصاد ایران وارد کردیم؛ برخی این خسارت رو یک تریلیون دلار تخمین میزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66198" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66197">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=AI1rqTFv1YkDW1gE0wFoqxebO_zBKcJtDvDL8RM_849zr7B9qVejlB5AuLsbAHWb0OKhYBm-9m3eVH2Hh-1Id3NK8xfpXdOfdEgU4YqTaYDDhR98qxgoycNsuU1uaqt-7NmSlnsj0WQ4X6_RQO9WXy8ELXygzVp9KfrW02hAKt1pHg3yp3mGufOu6uEun-TnZ9nfD2D5GRdpnQVToMRQAulbOlX5bk4GFD5nKR-Hq1nxveRi3tX-VVNvcv4rUSVy0AsmBZM5DqzSAHqvir5F6aHhtDVMwwn0JCSZ0vXV6-R94av2EIdwBrUgxCLGIY8mEb0rDHAQwKPPClLflrreTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=AI1rqTFv1YkDW1gE0wFoqxebO_zBKcJtDvDL8RM_849zr7B9qVejlB5AuLsbAHWb0OKhYBm-9m3eVH2Hh-1Id3NK8xfpXdOfdEgU4YqTaYDDhR98qxgoycNsuU1uaqt-7NmSlnsj0WQ4X6_RQO9WXy8ELXygzVp9KfrW02hAKt1pHg3yp3mGufOu6uEun-TnZ9nfD2D5GRdpnQVToMRQAulbOlX5bk4GFD5nKR-Hq1nxveRi3tX-VVNvcv4rUSVy0AsmBZM5DqzSAHqvir5F6aHhtDVMwwn0JCSZ0vXV6-R94av2EIdwBrUgxCLGIY8mEb0rDHAQwKPPClLflrreTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
هر زمان که لازم باشد اقدام خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66197" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66196">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=DlLXHVvek1KOy-zoe5zDnQ1z-OgrjWTHnwLMHEG79tRIYfhobp2c8azHoVCfexkS8mRWZ7Mes4F7IO73A_DPneJkPHxaYqP7sRq5tsfoZjYdAyHuxaBaUAAcMVmn_tODBKUdOJ2V668U-KWt-YpKoionkWdQg8NVDnCnMypIijw0zDsNQ6JBWGO9-4H578Rm2pMf7KmF26LvOMQLMMpUwD_PxCNIqrE08XeUm-KJNJ2RevQTTbeGhzyfDrIAcO0urMdn_c7kiEZMKluotNdtZ9DK3t3YmbRAmZRJdOd9YFlsB-LOhrzIInFB7egIb9Te9YfsAEQ7r9YeZm1gTDPDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=DlLXHVvek1KOy-zoe5zDnQ1z-OgrjWTHnwLMHEG79tRIYfhobp2c8azHoVCfexkS8mRWZ7Mes4F7IO73A_DPneJkPHxaYqP7sRq5tsfoZjYdAyHuxaBaUAAcMVmn_tODBKUdOJ2V668U-KWt-YpKoionkWdQg8NVDnCnMypIijw0zDsNQ6JBWGO9-4H578Rm2pMf7KmF26LvOMQLMMpUwD_PxCNIqrE08XeUm-KJNJ2RevQTTbeGhzyfDrIAcO0urMdn_c7kiEZMKluotNdtZ9DK3t3YmbRAmZRJdOd9YFlsB-LOhrzIInFB7egIb9Te9YfsAEQ7r9YeZm1gTDPDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ما در لبنان خواهیم ماند.
کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66196" target="_blank">📅 21:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66195">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66195" target="_blank">📅 21:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66194">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695d77536.mp4?token=GbBt819Ly5cmRSLuEz6ELuMvWHiRx22gICb1XV9q81ITAaInYVU_lhPJ-AgJWoYy1U7VBFDFa0F2R6RRLS_CsoEkylUxj7aBmUDKfWZgoS9zwbCli8y4_rCkvfAzPYwNk32YSoJYJVf2ss1CBIza-ltnMHTtolCc57bAIjkOzRBFRJwJirpEimx_s2-yi3t_8cOiuMvhLStzgxNflONPBOKqamYJah4Qc1wymKLVvk1ZM_cEnt0Jjw6WVIcYgsJ9zTdPE8yV15KCIDyUVYA7Fl9bFH2ZQ6qlkjzt-TUnRODS19L4EExztMGSmKGM-G3rtJ7cNS-3WHx6daCfTJIlbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695d77536.mp4?token=GbBt819Ly5cmRSLuEz6ELuMvWHiRx22gICb1XV9q81ITAaInYVU_lhPJ-AgJWoYy1U7VBFDFa0F2R6RRLS_CsoEkylUxj7aBmUDKfWZgoS9zwbCli8y4_rCkvfAzPYwNk32YSoJYJVf2ss1CBIza-ltnMHTtolCc57bAIjkOzRBFRJwJirpEimx_s2-yi3t_8cOiuMvhLStzgxNflONPBOKqamYJah4Qc1wymKLVvk1ZM_cEnt0Jjw6WVIcYgsJ9zTdPE8yV15KCIDyUVYA7Fl9bFH2ZQ6qlkjzt-TUnRODS19L4EExztMGSmKGM-G3rtJ7cNS-3WHx6daCfTJIlbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه جنگ خواهد شد نه مذاکره خواهیم کرد
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66194" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8zPNpd888jJcWKyVa-BvyGJmEhmuNkGOs7IiwOBVwZXLWCC0pOi85bg26pCoZfScEJj4DYE8xieeaT1GQkbIPzSMkojoo3_z7uU8QfPTlFE5z79QBg96C84coAR-J9-0lU5WPxBpB2cJl25oHzBXweDBF65HPXtNyuHTq24qqhn1AbDDv3HH802wToRpe6cOPAdEGpKrPouGsxp8TF0CcIB4nd7u8N94iH0wqaxDpSrAiHd3Ba7IuNADIxpi5vGuS60lOR8piKkSPt_SozZfpTBprUBjCeNBQdg_RmOgn9uW6ILDW4gQfzENKPpnaGqoZErWRFBXRd6cmlSgPLYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66193" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24683d102e.mp4?token=GbvLkpfyXuft6_xw2vvrhBi5Vp3ODSqhov-lgUP4j1d6IGcNnGMZwCyq39ALZ8sZuN7zYd1MrEpza2G_RnLCGDgimkS6isWMLfi-OWWTc11NKvmKW2RP3ocpnQEyiBHRjcMHYDPEnXDNENIQdCLK74_5-_KaIP5d6uwG6w866N2z8WUuULGQLDryaCqBNIYdtENhfGfWHAJ1vO2kTare13bJn4zr8XR4jsZJJH-eLz8mpzjkpmgwYwaqpFw2hInkCGaviNH2sM_gAKDn6ZgA0CzsyFy-LnmlpTgNYURON8X1ORgAmN7rlV4KRiYTYq89drXgsmtedTwpVc7d2ipf-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24683d102e.mp4?token=GbvLkpfyXuft6_xw2vvrhBi5Vp3ODSqhov-lgUP4j1d6IGcNnGMZwCyq39ALZ8sZuN7zYd1MrEpza2G_RnLCGDgimkS6isWMLfi-OWWTc11NKvmKW2RP3ocpnQEyiBHRjcMHYDPEnXDNENIQdCLK74_5-_KaIP5d6uwG6w866N2z8WUuULGQLDryaCqBNIYdtENhfGfWHAJ1vO2kTare13bJn4zr8XR4jsZJJH-eLz8mpzjkpmgwYwaqpFw2hInkCGaviNH2sM_gAKDn6ZgA0CzsyFy-LnmlpTgNYURON8X1ORgAmN7rlV4KRiYTYq89drXgsmtedTwpVc7d2ipf-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
آخرین مکالمه ترامپ و نتانیاهو بعد توافق:
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66192" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=sspYWlQQuttdVPFj-AhQ2AUIqksIluIuY3qjMHGLbLIysiFLeR16MZmOVJWeUaOs3zpnip6xDMlu4kh9kk-Um6RmOq5cYikeX56vhfyj1okheOemNRa7CafDkxf3MUXCcmpYw16_tp9b5Tr-w3ZbFUDLC7tBeKsQ1ouDIlYhGTonNG_rlTt5xioLqLwYEUmG9Db5PF0wJDtHePLAiWNLt1FxjcObnsxlwRwpIOKgM13ucKD241ra-w5OgoKT5wegvhweCEv_6jSGdSG_3ilAi5RR31jQB5p5Mdfi8DbMfGRBBFs5ymVfyDeuimNnaKilPNmDOfSvD9acfIWpD-FLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=sspYWlQQuttdVPFj-AhQ2AUIqksIluIuY3qjMHGLbLIysiFLeR16MZmOVJWeUaOs3zpnip6xDMlu4kh9kk-Um6RmOq5cYikeX56vhfyj1okheOemNRa7CafDkxf3MUXCcmpYw16_tp9b5Tr-w3ZbFUDLC7tBeKsQ1ouDIlYhGTonNG_rlTt5xioLqLwYEUmG9Db5PF0wJDtHePLAiWNLt1FxjcObnsxlwRwpIOKgM13ucKD241ra-w5OgoKT5wegvhweCEv_6jSGdSG_3ilAi5RR31jQB5p5Mdfi8DbMfGRBBFs5ymVfyDeuimNnaKilPNmDOfSvD9acfIWpD-FLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: توافق شامل هیچ‌گونه تسهیل زودهنگام تحریم‌ها برای رژیم تروریستی جمهوری اسلامی نمی‌شود.
ترامپ در پاسخ به پرسشی درباره احتمال کاهش یا تعلیق زودهنگام تحریم‌ها علیه رژیم تروریستی جمهوری اسلامی تأکید کرد چنین موضوعی در توافق وجود ندارد و افزود این مسئله در نهایت به رفتار رژیم تروریستی جمهوری اسلامی بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66191" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66190" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUUani3EnjYN7oO7fGoXQh9rEKUk7ODbNIiHkvLSIPAZWptDNb3VEN3D_KHBKkNvGaAX3z-R__RgpPppobF-tUjTYsz2dEeErweBUaHmgHqg77uObPCU4Bq9LbVxgufaYcq3vPN2iso_-ei8_AmxsPqB7aHGhEEPk_rzHYxcYqk5K-GLVwP6_w_ezuz7xl_twuocdmJnonzhV60gRR46ScwGK_dDD9e_Z8ASIIRCTUtdS1Vqu3joeCzMwBtGRwvIO1H_UUCXTvKPJ9rmfqqqBNYOlQpYBnnLH_UYqakKfRim3KtU5AQvfaQ_amReRKZ7mLt_CcGeE9j6HfMsq5YG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66189" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=eU9dwYb8RrEPUOiX2l83HynWFkl6kNd2jkzv_8-poxUIGs6XKVn4As4Ywh8beIyDPuU7ncnLgy_AYluMRu-G8voXkUf6JBKcctK6_AmZQkArrKoPe2t_irv1v95r_onjLhVT3QIRJ4qU_9z8jas90v-0MRKZpfOtP7IrwgvPm_S4Oka-TwKnUv9G5dFDYzTQfMirJLA5Qw8TjPNrXSZpCKsq1zv7WaypFSz49vZy3uOGXTP3d8HlFUyv9m4jdGLz9hLBhQWnPGNlKkMlu6AvEkwha3Dt46iLHJRKA1dmCWuv-yhfz5Fu80ExKwAfKBKyNykC0c9x8qPQ6oBRJkiHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=eU9dwYb8RrEPUOiX2l83HynWFkl6kNd2jkzv_8-poxUIGs6XKVn4As4Ywh8beIyDPuU7ncnLgy_AYluMRu-G8voXkUf6JBKcctK6_AmZQkArrKoPe2t_irv1v95r_onjLhVT3QIRJ4qU_9z8jas90v-0MRKZpfOtP7IrwgvPm_S4Oka-TwKnUv9G5dFDYzTQfMirJLA5Qw8TjPNrXSZpCKsq1zv7WaypFSz49vZy3uOGXTP3d8HlFUyv9m4jdGLz9hLBhQWnPGNlKkMlu6AvEkwha3Dt46iLHJRKA1dmCWuv-yhfz5Fu80ExKwAfKBKyNykC0c9x8qPQ6oBRJkiHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
متن تفاهم‌نامه به زودی منتشر خواهد شد و سندی بسیار قدرتمند است
ترامپ در پاسخ به پرسشی درباره زمان انتشار متن تفاهم‌نامه گفت این سند احتمالاً خیلی زود منتشر می‌شود، زیرا مایل است افکار عمومی آن را مشاهده کنند. او همچنین تأکید کرد این تفاهم‌نامه سندی بسیار قدرتمند است و آن را با توافق دولت اوباما مقایسه کرد که به گفته او سندی بسیار بد بود. پرزیدنت ترامپ افزود انتشار متن احتمالاً در مقطعی پس از روز جمعه انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66187" target="_blank">📅 20:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66186">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=oIcpfTQ6_9_-2uwa44tgbNVETvW0ArK_67azmtdQtsj9jX9mzV3FFrIgQI68qiGN0AJZR_D5en7vGrUMzDg1nsN7tR1CJpODkLNL9rhs12o5QoYI6hYoJL40BfZA5TaVj3SK5_BxLR3jJNP-wQ3NUuk02KQbPUyL8a8sw9GWHsE4vIDgdcGM_SW6f7wmMTeQY_VpbdXPkf0uKa7o1byBNNhVIQJQv3_NFyXYHZ30Y5FM8bf5qEx1XWVqbDpP2VyrOTwnzyWFqNJfTnzRSh9tqTWVnUCTrGpgLyWEzxjsFk_Rv_Dl_GIuH8W-5XG8IRBaXgScJZUd3SA9eLWGJRbj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=oIcpfTQ6_9_-2uwa44tgbNVETvW0ArK_67azmtdQtsj9jX9mzV3FFrIgQI68qiGN0AJZR_D5en7vGrUMzDg1nsN7tR1CJpODkLNL9rhs12o5QoYI6hYoJL40BfZA5TaVj3SK5_BxLR3jJNP-wQ3NUuk02KQbPUyL8a8sw9GWHsE4vIDgdcGM_SW6f7wmMTeQY_VpbdXPkf0uKa7o1byBNNhVIQJQv3_NFyXYHZ30Y5FM8bf5qEx1XWVqbDpP2VyrOTwnzyWFqNJfTnzRSh9tqTWVnUCTrGpgLyWEzxjsFk_Rv_Dl_GIuH8W-5XG8IRBaXgScJZUd3SA9eLWGJRbj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: می‌خواهیم مسئله لبنان را حل کنیم.
آمریکا به دنبال آن است که ببیند آیا می‌تواند مسئله لبنان را سامان دهد، زیرا این بحران به نظر می‌رسد هرگز پایان نمی‌یابد. او افزود این موضوع در مقایسه با سایر پرونده‌ها نباید دشوار باشد و درباره گروه تروریستی حزب‌الله نیز گفت باید گفت‌وگوهایی در این خصوص انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66186" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=Fw779pdsyWexSNvQ3UqwjjMfqA4uZGSelXaZFy2bwCufNnbicApyhsOHI7eaJGfbSHyKSRrCY-jjgR1r5obM_569zltqtaqyw6WUbQ4DYTmcgk-ODgCFXQ9QhDIt4X_dpcXa0yBBiW7G2Gw1P8DMPdL3L9jQ8YHhTkF3iUibXIWv3rASdBnnVdY0AirzagfxJUvrseX1jK50dGryHTYHEKNkjjhoWBrT3h38YfFpHdNe_-su2OqiXGkcgfCUleFy9_EoAInr-rsCAKhhUKGBGT67l-ctf-wT4cxfCD2BqcJJFmc9bcxP8sU3OzapopdhDb8Rmvivgui2I4I7K-zrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=Fw779pdsyWexSNvQ3UqwjjMfqA4uZGSelXaZFy2bwCufNnbicApyhsOHI7eaJGfbSHyKSRrCY-jjgR1r5obM_569zltqtaqyw6WUbQ4DYTmcgk-ODgCFXQ9QhDIt4X_dpcXa0yBBiW7G2Gw1P8DMPdL3L9jQ8YHhTkF3iUibXIWv3rASdBnnVdY0AirzagfxJUvrseX1jK50dGryHTYHEKNkjjhoWBrT3h38YfFpHdNe_-su2OqiXGkcgfCUleFy9_EoAInr-rsCAKhhUKGBGT67l-ctf-wT4cxfCD2BqcJJFmc9bcxP8sU3OzapopdhDb8Rmvivgui2I4I7K-zrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
درباره باز بودن تنگه هرمز اختلاف‌نظرهایی وجود داشت، اما در نهایت عبور و مرور از این گذرگاه راهبردی بدون دریافت عوارض انجام خواهد شد. او افزود آمریکا احتمالاً به کمک زیادی نیاز نخواهد داشت، اما حضور یک یا دو کشتی از چند کشور دیگر می‌تواند مفید باشد و فرانسه نیز یکی از گزینه‌های مناسب برای مشارکت در این مأموریت است. پرزیدنت ترامپ همچنین تأکید کرد هیچ‌گاه نمی‌توان از تحولات آینده کاملاً مطمئن بود، اما به باور او تنگه هرمز باز خواهد ماند و رفت‌وآمد دریایی در آن آزادانه ادامه پیدا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66185" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=Dh7ROOuRN-GxbdC2QKe2yFprWF_iY0NpvliBuiid5X2h0Zph_ETmZDRpEdQsw0YVzsGQs-PAUZt5HWtTk_nEanyXR970zbhp_LE8iLUM5o__TDCkhOWfsezQVp7oNoQsFwjRY4I9kgx2TsMtvqVkVKVwlGTj72Y44PYtKYHm3xoFtpbDNl57DC-e4QofW-y7SGHkJAWLI7a_O4Bu1PD3lOs2L85ul_x-ERnobU0Re--5spceRIaA1G9qQYjUpHDobvVhT49wqWTuzDLae_v-HWcGGCdzaMyMpTT-AdFKL_GZ5DxLOMYIr_B5UWJzKJnU6vAnYzbQQjmm0mE9FlM0Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=Dh7ROOuRN-GxbdC2QKe2yFprWF_iY0NpvliBuiid5X2h0Zph_ETmZDRpEdQsw0YVzsGQs-PAUZt5HWtTk_nEanyXR970zbhp_LE8iLUM5o__TDCkhOWfsezQVp7oNoQsFwjRY4I9kgx2TsMtvqVkVKVwlGTj72Y44PYtKYHm3xoFtpbDNl57DC-e4QofW-y7SGHkJAWLI7a_O4Bu1PD3lOs2L85ul_x-ERnobU0Re--5spceRIaA1G9qQYjUpHDobvVhT49wqWTuzDLae_v-HWcGGCdzaMyMpTT-AdFKL_GZ5DxLOMYIr_B5UWJzKJnU6vAnYzbQQjmm0mE9FlM0Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره حضور در مراسم امضای روز جمعه:
پرزیدنت ترامپ در پاسخ به پرسشی درباره حضورش در مراسم امضای روز جمعه گفت این موضوع به شرایط بستگی دارد و در ابتدا قرار بود جی دی ونس این مسئولیت را بر عهده بگیرد. او افزود ممکن است تا آن زمان برنامه‌های دیگری داشته باشد، زیرا قرار است تا دیروقت مشغول باشد و هنوز تصمیم نهایی درباره حضورش گرفته نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66184" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=I7n3cDq1fglB8rUOUw8aal-oG1imGeHqPGsA3lOCN7h8cP_Tnb0rtd2Wd1_FoyKNn7WTA-kASBv5o0lfsY0B0mGoM9NULacV2ohTp_8H37I2S_gVigZsxd_SOLHgJRS6izGQfZEWVdKW9pCaOLPr108KYWYNFGPdA9Y5RvZg7rGmZL7BoG4G4KrNEzyzeLhv0lwAR2HOwKrkhNtpja7RO_Ao5UlVx5jteme743AUFfGIHIJmgrFNXLQGISQGFsM7f7Exv69CFhwAGEBSi1NRTgEdpg69mEMrrO-JYyP6r2_wSGBgRh4SLMgORuA9ZFiE6mBq2XZAQ5omowCK8W7ITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=I7n3cDq1fglB8rUOUw8aal-oG1imGeHqPGsA3lOCN7h8cP_Tnb0rtd2Wd1_FoyKNn7WTA-kASBv5o0lfsY0B0mGoM9NULacV2ohTp_8H37I2S_gVigZsxd_SOLHgJRS6izGQfZEWVdKW9pCaOLPr108KYWYNFGPdA9Y5RvZg7rGmZL7BoG4G4KrNEzyzeLhv0lwAR2HOwKrkhNtpja7RO_Ao5UlVx5jteme743AUFfGIHIJmgrFNXLQGISQGFsM7f7Exv69CFhwAGEBSi1NRTgEdpg69mEMrrO-JYyP6r2_wSGBgRh4SLMgORuA9ZFiE6mBq2XZAQ5omowCK8W7ITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
پرزیدنت ترامپ گفت آمریکا کار بزرگی انجام داده و امیدوار است روابط خوبی با رژیم تروریستی جمهوری اسلامی شکل بگیرد و دو طرف بتوانند با یکدیگر کنار بیایند. او افزود اگر این روند موفق نباشد، شرایط به نقطه شروع بازخواهد گشت، اما معتقد است نیازی به چنین سناریویی نخواهد بود. پرزیدنت ترامپ همچنین تأکید کرد توافق انجام‌شده با رژیم تروریستی جمهوری اسلامی می‌تواند دستاورد بزرگی برای جهان به همراه داشته باشد، زیرا برای مدتی جریان نفت در منطقه با محدودیت و اختلال مواجه شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66183" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hrr4tauXOM6GaBpMRyK_EDNB1qwQ3pNAE9nxXZW3htJlAOtq2sLYRH_wvoOOU2uUZ4Qx4Kh36yRwRqEU6BJaPK43-o1ZGnkXgqqyyvOWouORNRIXmx04RoHuop2rE_OK-JAafnveZhW8HAKWKzvrCDuStqr4BKagYlplxZkb-3duFOxRn_bV3WjWCATvdHhXIm1gJB-XVjHw22dbX8UaaIjQJLBwGkfhdiU9O-W2_zxfDjq8YhKymszyA3zS4AGdIw4PTSMB0hX3IxVLjSUD2TPqy0UYAOI3QD8C7H9mStsx4jf5jrs7L84uMw3bEH6wr9WtEF3wD8yz4gLbFiyVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
ملت دوست‌داشتنی و سروقامت ایران! با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.
ایستاده‌ایم و در نهایت ‎
#ایران_ما
پیروز خواهد شد، به لطف خدا.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66182" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66181">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=kj2u1enTqL_V9P0ioHmh1We4qWOyfFxsWQPG9D7NKAnxjWqtzqnQWxn3Ut6HzZE4JlgPh451QZ9G1WuF6k4V47sjsD4ofTRYhZG7mduDs4XsCkiN_Z105J_PRTmfmivik0EXIC-a4orOALNFZZfENraIRESisQBJ7r32Yg2gu96E-Gz7E3UpBY-Zvf9zxTrQ4QkcfkwNkA3bl2X3B-5d_aBNIVQy3y3TLJdu92Kc2wDVHwj3hucYP9DVKQzqf53Bs_2ZBrHH-b17UR-PAmshyKtE0KtRTmh_C4hMYNmMTQKB7l77W5egbEJ8yDwGg_QcTazj2T9QXC76RifeUjsPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=kj2u1enTqL_V9P0ioHmh1We4qWOyfFxsWQPG9D7NKAnxjWqtzqnQWxn3Ut6HzZE4JlgPh451QZ9G1WuF6k4V47sjsD4ofTRYhZG7mduDs4XsCkiN_Z105J_PRTmfmivik0EXIC-a4orOALNFZZfENraIRESisQBJ7r32Yg2gu96E-Gz7E3UpBY-Zvf9zxTrQ4QkcfkwNkA3bl2X3B-5d_aBNIVQy3y3TLJdu92Kc2wDVHwj3hucYP9DVKQzqf53Bs_2ZBrHH-b17UR-PAmshyKtE0KtRTmh_C4hMYNmMTQKB7l77W5egbEJ8yDwGg_QcTazj2T9QXC76RifeUjsPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف بعد تعطیل کردن مجلس و انجام هر کاری که دلش میخواد
😂
:
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66181" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها 10 گیگ — 170 تومان 20 گیگ — 340 تومان نامحدود — 450 تومان (ترکیه)  برای خرید بهشون پیام بدین
⬇️
…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66180" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها
10 گیگ — 170 تومان
20 گیگ — 340 تومان
نامحدود — 450 تومان (ترکیه)
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66179" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6fIAksZz86UWQbY3VtCY6WfLXy8RdH6LGNOrIZadeWT26S-ejnw4zMaHeyMtI5Sr1RQPImyPzHTy3HdxLyiA6d9N_0eXiMfZLRGZ7Iy2Rj5oy_2bzAEq8RI6oV5syf5DBRecztsH1NI0KbdaEZGA315EOdbgHH3i_kwpiKo6tmWgF2s78qfy3pWvjBL-s0CZPImPXvjocg9kRxHpHxFGKPCNmNUg9noyBkv0kSINELhtfiy7XWDJroxrBvvHF8nK5w491q1q5CuhHijVL7ejo9NHY4xynV88AM_9FX_Br2boPQOvO2xgJKZjEr9RyqPN1N5b_vSwI5kJKVfE0vTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnH9YSvFSQ8M6ijebgLZwy5AA-v3aXDjsjWUybtYCgjwnb5N5WeMOKttVQ1NxNQ5fV_-TxjVWuHILU_e3ZqiyXNkxb41BHO9dqI0h6dx4cBmonJTq2Lu8AbepNpmBQcaEUVEf51-NmIEF_PueQ0Dvd1aLP6FE3OeKf0bwjMoWUik29m-m0UZc--JCRL54dlO0Andv0IJfGfmE1hhLtRx9vNV7MRIoDgyrAY8te-VNa_Sq_NS8x9SbGQc9vTifTlWdu4gWgJTfd0dDG_HVEG4clP7gU9756aBTVOX4YlLnJkfN9eTqp4X4AKR3-kQzQQde3FTqKPlPidTzP3WaVpwZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=kDcVGgK0u0dd7yt43LIyTsRksLLCWzlj7M_PZ07YG61S9mgZQBBbsn02UKthmbjMeP0zFzmLy9uXCzHHpDYLBr8r2T9kMGaAS0uGfNHIyYdHkUlynOUN2xeqIkLt_nkw9s8CVnA02a5X_zlVeERPE2bp3ZiyNdP9me1WrCVjOq_7JgWlSN6kI9EJB4GncubBvqP0IMrXkut1TPmj3XrHdQUh-Rkq_cc024AHV_Xcl686JQad2tOduiok_9PHXNBwrc-48SRwjMfH-7MayphzqXbteeqme6kx8noDRlZGIpCxfxLKl8OKlsFM3BM3YJR3H2qhgPDClJ9bXo1NQpN5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=kDcVGgK0u0dd7yt43LIyTsRksLLCWzlj7M_PZ07YG61S9mgZQBBbsn02UKthmbjMeP0zFzmLy9uXCzHHpDYLBr8r2T9kMGaAS0uGfNHIyYdHkUlynOUN2xeqIkLt_nkw9s8CVnA02a5X_zlVeERPE2bp3ZiyNdP9me1WrCVjOq_7JgWlSN6kI9EJB4GncubBvqP0IMrXkut1TPmj3XrHdQUh-Rkq_cc024AHV_Xcl686JQad2tOduiok_9PHXNBwrc-48SRwjMfH-7MayphzqXbteeqme6kx8noDRlZGIpCxfxLKl8OKlsFM3BM3YJR3H2qhgPDClJ9bXo1NQpN5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از آتش سوزی گسترده، میدان تجریش تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66174" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
نتانیاهو قراره تا چند ساعت دیگه سخنرانی کنه و این اولین واکنش اون نسبت به توافق هست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66173" target="_blank">📅 18:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66172" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66171" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=Lu_yAtEEugog42AlYDQjtkWIMOXJmZ5v04VSYRcS8TzrYC3IadPyLbyrb6yPLkmlWGDuaFMTmGxbewFJy04L3tfMDwPHTPnyJbDX_amVMF-47lkLUzqqKZeT91BlltQuQS1gc3fr4yWbgXwFYtafepr_isyccbSo4EPbwMoxolicCkMDj3q23Y2uq2nLOQoU1jEhlrPLiNqGWjQ35R_xDJKtHKcVL1fS3Z-vJoPbmVpHd9C6nfajlj6m6HaE4Ebzbl29koKp2ICf8XMdWlk2Ca1S6S2PJj1NhWLM2nxG81GOImyR6Yr7lByBbv_or-4XGQBez8nQHQ5Hm4FyMqskUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=Lu_yAtEEugog42AlYDQjtkWIMOXJmZ5v04VSYRcS8TzrYC3IadPyLbyrb6yPLkmlWGDuaFMTmGxbewFJy04L3tfMDwPHTPnyJbDX_amVMF-47lkLUzqqKZeT91BlltQuQS1gc3fr4yWbgXwFYtafepr_isyccbSo4EPbwMoxolicCkMDj3q23Y2uq2nLOQoU1jEhlrPLiNqGWjQ35R_xDJKtHKcVL1fS3Z-vJoPbmVpHd9C6nfajlj6m6HaE4Ebzbl29koKp2ICf8XMdWlk2Ca1S6S2PJj1NhWLM2nxG81GOImyR6Yr7lByBbv_or-4XGQBez8nQHQ5Hm4FyMqskUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ونس:
تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66170" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66169">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=kL7HvHxd-3nZDcnZQFef_Vul7rHmHAcMmwTCUQ6bbSvOEOPZwOaYH60OdjDu4bioOl7bnfJUqnsoCNo4zEvHU25wbCzSJQn2Jznnc1D9IZpgbVDa3s2Ff_aqpBBDaDWenJrHGyv3GHMUhMOARxGmpK7R_3XokU2sDxkFbjR4u86Mcx-hS843RfdqQPKUZKda8CPrxS8PYGNXYGyNbwpdsIaLJClIAvLY9YNqqQHHqXXYfn5sW4XxMhnSu-mXc032GOQxvmI6m2R8ogdf7Yqc8Xpw-g0tGd3O3l3ZjzqhcIbXHkqawo_fPXhbm4ho4sKTmWoNcLwht1T042Nwp29rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=kL7HvHxd-3nZDcnZQFef_Vul7rHmHAcMmwTCUQ6bbSvOEOPZwOaYH60OdjDu4bioOl7bnfJUqnsoCNo4zEvHU25wbCzSJQn2Jznnc1D9IZpgbVDa3s2Ff_aqpBBDaDWenJrHGyv3GHMUhMOARxGmpK7R_3XokU2sDxkFbjR4u86Mcx-hS843RfdqQPKUZKda8CPrxS8PYGNXYGyNbwpdsIaLJClIAvLY9YNqqQHHqXXYfn5sW4XxMhnSu-mXc032GOQxvmI6m2R8ogdf7Yqc8Xpw-g0tGd3O3l3ZjzqhcIbXHkqawo_fPXhbm4ho4sKTmWoNcLwht1T042Nwp29rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس درباره ایران:
ما اکنون مستقیماً با نظام ایران صحبت می‌کنیم. روابط خوبی در آنجا داریم
دیگر پیام‌ها را از طریق کانال‌های پشتی منتقل نمی‌کنیم؛ در واقع با آن‌ها صحبت می‌کنیم.
وقتی با آن‌ها صحبت می‌کنید، متوجه می‌شوید چه چیزی واقعی است، چه چیزی جعلی است، درباره چه چیزی جدی هستند و درباره چه چیزی جدی نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66169" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66168">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a8610027.mp4?token=eRDA79guXG6-cKy5UZc9vNbyBL7cXIn4tHWPApdRu397ddmTVgAPjb_T1XVpt-HliqWnliph9KnZ2LMyF_pI1I8lKRa6gPyBc-ewism1H7N-KS-8ZAuG0rzel6clRV-FN1OK_Bvq4l5jjZ2xg2R9ttL9FyNmzmV0n-nKmpIcL3AxiOCYutoAAFCaw0dUFJoKRpSciklue8O9XQhugQH20mURl6CdSn8kpL1sqpORS_DWuuEywp5Vsny0lUpAjHYXD0h3FUz3ig5H8ioxWM_gJzmkymwCNbeUAMUOBEC7K3mi40JEDvqROymPqxPp_PJsgnL2Rdb837-BPzaq5Gys7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a8610027.mp4?token=eRDA79guXG6-cKy5UZc9vNbyBL7cXIn4tHWPApdRu397ddmTVgAPjb_T1XVpt-HliqWnliph9KnZ2LMyF_pI1I8lKRa6gPyBc-ewism1H7N-KS-8ZAuG0rzel6clRV-FN1OK_Bvq4l5jjZ2xg2R9ttL9FyNmzmV0n-nKmpIcL3AxiOCYutoAAFCaw0dUFJoKRpSciklue8O9XQhugQH20mURl6CdSn8kpL1sqpORS_DWuuEywp5Vsny0lUpAjHYXD0h3FUz3ig5H8ioxWM_gJzmkymwCNbeUAMUOBEC7K3mi40JEDvqROymPqxPp_PJsgnL2Rdb837-BPzaq5Gys7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد ایران:
ما دستمان را به سوی ایران دراز می‌کنیم. اگر آنها بخواهند رابطه‌شان را با ما تغییر دهند، ما هم رابطه‌مان را با ایران تغییر خواهیم داد.
این پیشنهاد ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66168" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66167">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=lfbuu4TFJdWjXtlcjeBDreUfguwzsW9eVDxhUb6gEgxQrctkG3UBwmzDiX4jrX2bm2UaVl3BrfEc40uMPeMUOs76aVEkgOQUE3sbQat3Cpgbp_M0GEYsBa6HITe7RwrGgODMJQ5NBqmjN_-EwQCFv2TRbPNPMza8XKbfGNld6jY91tJdjSRPtCsbTSUn1Ew4vGvYuBboXRf1_eTTSd4zBbUHK68r_PYYEW__NsS5Mj3DoWMIL-Lh9G8i0Cn4mDkeAS7ry1FGcjWVhnYjVPgj4m7QIqGq2R09qXbxOuR1SmWY3bocLCtym8oWTGtkmp0Q8u34L1hmFwJlayo9QK24Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=lfbuu4TFJdWjXtlcjeBDreUfguwzsW9eVDxhUb6gEgxQrctkG3UBwmzDiX4jrX2bm2UaVl3BrfEc40uMPeMUOs76aVEkgOQUE3sbQat3Cpgbp_M0GEYsBa6HITe7RwrGgODMJQ5NBqmjN_-EwQCFv2TRbPNPMza8XKbfGNld6jY91tJdjSRPtCsbTSUn1Ew4vGvYuBboXRf1_eTTSd4zBbUHK68r_PYYEW__NsS5Mj3DoWMIL-Lh9G8i0Cn4mDkeAS7ry1FGcjWVhnYjVPgj4m7QIqGq2R09qXbxOuR1SmWY3bocLCtym8oWTGtkmp0Q8u34L1hmFwJlayo9QK24Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شده یک فروند بمب افکن Tu-22M3 نیروی هوایی در منطقه ایرکوتسک سقوط کرده و به گزارش وزارت دفاع روسیه تمام خدمه موفق شده اند با موفقیت اجکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66167" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66166" target="_blank">📅 17:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66165">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVkSjO3H7SGq7cGiXtiKycy8GEmJYwIj1i1NxJ4_uA9Q1wU1iJtLbVDnPCsCPNtnBMbZTVfIADiqendoPmByx1ei2-S1mnksp2UE8XACls7TUMJdBSDrWhJscTO-HteS6We4UtZgywUu8Ycxf17a4_9-GTEdwTdw98VXgOGNOdjmLmLHzwB-3xuLJ8VH9QZuuiF0RqLtH0I_rLSg0lL25VR_vUToDSqWAYitKtbRFj8cl0TewNu2GcPiMQISD8EJ0iFWHSXw0eYQdieKv8RC1heck4xImz7nx-lPHjGhI3WcSQ75UnjoQDLWZqVnBV73VYxQE54CX7q0ywdnmR9wCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل شروع بازی اسپانیا و کیپ ورده فاک بت اومده لاین داده ضریب ۲.۲۰ الانم میخواد آنالیز بزاره از بازی های جام جهانی نمیخوای بیایی سود کنی؟
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66165" target="_blank">📅 17:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66164">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOdgRD0W576hpQ76SpAAfoMrDYjW2QL9bjj0-yHg_5DpMd2TVASmpuQNAoYdzYcv7odKY3gU9KOMLgETd_1zkweadIEM2ZRqF1flWtWvdzv37Gg6AXdDTqeVgxTV-iMd9Cm-cYKg67VOpgIJ6nqtSqhM6MzQPk59mzCFsGkEwPKwq_x9wIeIv26-X2b_9ils5gIeFhGSXGRWBhGxbHagOSQEoSFvcuUxU9bSuFpZYaLjq1dfM7B00gaf8XCg3Apfa78n0U6LhaENg1JnPapfg5bkpsFvh_wM-fjAEqRqGwvqgkwLi0r8_JZKvSVoaLGJuPM90RtTgsa1V9l8mcjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ در تروث سوشال :
پس از توافق تاریخی حاصل شده با ایران در آخر هفته، کشتی‌ها شروع به خروج از تنگه هرمز کرده‌اند، که بسیاری از آنها «پر از نفت» هستند
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66164" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66163">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
صداوسیما:
تنگه هرمز تا اطلاع ثانوی بسته است و سپاه بیش از ۹۶ساعت هستش که اجازه عبور به هیچ شناوری رو نداده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66163" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66162">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=nN2jOWH7MrL0Ol9Mz0UmngVF5EyO3Ia9GBske2FvFgXCsc16KI8FUU8235_8Fb8o4IpByI7deSoCFvoPXKT1-aX55yYzx1SYmkx2-40OmCP4CokYMGkAmhnqxHls2MKb96AaHfWU9DvylGi17WsIi2M1_2mZT7VadrCH7KBpY-XAtvQU-iSD7D16L6KH3b05SUYahP3_ULS0BrF9vgLGjql_A4qeLMnAcORhEC43yFi8_z6ulBGx6WD6jMK1qXvg_bLzlJLA5SUt-lSlvn-NWMr3gqFLsSTurne0IrTCsFtZZk8F-J4vWNmfLwaECQDi4HMfl6oHJ9Q62ptkl8_xOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=nN2jOWH7MrL0Ol9Mz0UmngVF5EyO3Ia9GBske2FvFgXCsc16KI8FUU8235_8Fb8o4IpByI7deSoCFvoPXKT1-aX55yYzx1SYmkx2-40OmCP4CokYMGkAmhnqxHls2MKb96AaHfWU9DvylGi17WsIi2M1_2mZT7VadrCH7KBpY-XAtvQU-iSD7D16L6KH3b05SUYahP3_ULS0BrF9vgLGjql_A4qeLMnAcORhEC43yFi8_z6ulBGx6WD6jMK1qXvg_bLzlJLA5SUt-lSlvn-NWMr3gqFLsSTurne0IrTCsFtZZk8F-J4vWNmfLwaECQDi4HMfl6oHJ9Q62ptkl8_xOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممدباقر۲۰بهمن۱۴۰۳:
با قاتلین قاسم سلیمانی مذاکره نمیکنیم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66162" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=p1byDDkYnePTYEqNrAlKA1WDehPhcjsDhOWTlEQtdZ_hSbmkVlHQrnz9t7mUDsbFryAQDF9tBIi4zg_ft6sLCeB8w5iVL8bTq_Cg9bugOSgQMb1JzxlePNLRYFGidYI0WPcOBlPn84aqvAFT4jIL8xkoMx3ty_TzRG9ZxSq--xHbIwoTaADeCFhTJq-3VtFcNdMxwyMrsZE3no8QWZIYqLEQrE2Wbw3XxvYBscH8U7Ylfrbz5PIX0-LcucMdkiKSVfR9bL4ZHTxSaOm2dN_xRWmfhTbxpvt1A7aaJBNxk06-F6lBtQ0iMB7Yp1k4Nzn4wdOmvBP9suZW8wq1jFgqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=p1byDDkYnePTYEqNrAlKA1WDehPhcjsDhOWTlEQtdZ_hSbmkVlHQrnz9t7mUDsbFryAQDF9tBIi4zg_ft6sLCeB8w5iVL8bTq_Cg9bugOSgQMb1JzxlePNLRYFGidYI0WPcOBlPn84aqvAFT4jIL8xkoMx3ty_TzRG9ZxSq--xHbIwoTaADeCFhTJq-3VtFcNdMxwyMrsZE3no8QWZIYqLEQrE2Wbw3XxvYBscH8U7Ylfrbz5PIX0-LcucMdkiKSVfR9bL4ZHTxSaOm2dN_xRWmfhTbxpvt1A7aaJBNxk06-F6lBtQ0iMB7Yp1k4Nzn4wdOmvBP9suZW8wq1jFgqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله پزشکیان به منتقدان و اراذل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66161" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDVLCS2onGIVjqMRE5SgPyMLN19Jyz01Md9Q6mQitZDpurpp28QXfE-mw-27rwr1HsCEtFvcIeu2arD-dROlYEcX-jPwH5i3cV0dfQWieksFJnV4f9bG6OUn_lLsJetLv0xrVtqT-Fy6d5oxy4ZRnV6gPRGZVpu2z4zWmywVG1xACpeE72Nmpdc7CycEgpQ2hhlp3ppo891lUc-Cw9XEvEbfkCDZq8J_BmjYGlVCAkw8S8qEngwVdwxV0HWokEX8Nd1MSKRLd7EqozWB70Tlp22QZ2kEUFfJUpPelJNHB8RH_v_NBezwH_jUPEYaTnHmFzeAJfqxH1QodvAOj0Uetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابوالفضل ابوترابی، نماینده مجلس:
استیضاح مسعود پزشکیان مطرح نیست، شاید خدا شهیدش کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66160" target="_blank">📅 15:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=c_7DmwlHMPokEUbjxUqxVWINabvUY_0GPYNj8JDZXn4IUFRnrjaZKBK37GJwOABhxChG7rYPBKh7sYVDtm-D0biz_NluLmrLZnbQM_NdidinU1bWgSqjHsHdZK-jM0KT1mVk4UA7rgRGsq3t5gld0nG2pN26ZHsSUBsAJeecJc-zoKCZny5hbrp7K579cnYvvmoifXLzF5J4Qz41Bmyka38IBswma-bmalWkB0Ny-e6dIWRKCpHY2t7J4yImfDm1Ajq6LB_SsNcRMvRfLv8PGx5FqD6xlOjTfLW4Yf2C8Zh6qkpq-3gwize1cIvhsSXuhuOiLsUANJl9iCQh6FOFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=c_7DmwlHMPokEUbjxUqxVWINabvUY_0GPYNj8JDZXn4IUFRnrjaZKBK37GJwOABhxChG7rYPBKh7sYVDtm-D0biz_NluLmrLZnbQM_NdidinU1bWgSqjHsHdZK-jM0KT1mVk4UA7rgRGsq3t5gld0nG2pN26ZHsSUBsAJeecJc-zoKCZny5hbrp7K579cnYvvmoifXLzF5J4Qz41Bmyka38IBswma-bmalWkB0Ny-e6dIWRKCpHY2t7J4yImfDm1Ajq6LB_SsNcRMvRfLv8PGx5FqD6xlOjTfLW4Yf2C8Zh6qkpq-3gwize1cIvhsSXuhuOiLsUANJl9iCQh6FOFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ برای شرکت در اجلاس گروه هفت به فرانسه سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66159" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ2t3cYImXsN9GAxQaY0ZmBg481IwFCtFIS20oTRB0iwQaJNjdedO3vZO-RdGpGt1b2g0yegFGnFL4V9QxllHBs_AIUv5HXQDfKbw2OFKiBsRI9zyQ-DOWEXV2VqkvvaxKO5w26h-WymvUrpX6xlFRoLzwb_OindcjZyo35JvanA7VxM-5Rkpn22boH3oMGbrs1jKp0ZFfRmMMqMIVYp8BnSDgkWqDUJI_9xPpxUsZpRipd4YE-I5LEpuyNl9ATHrp73HUX0612Nzo8QqqAkrXjJSbhb9G1CD1Nb32dSdN0XoqzMvtg6qLQGxikpKJREusN8GWJX-NzaRVb9Nu2ywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید حساب اسرائیل به فارسی:
یک سال پیش در چنین روزی جمهوری اسلامی با ساقط کردن چند فروند F35خلبانان اسرائیلی را به اسارت گرفت و ما همچنان در انتظار پخش اعترافات آنها در صداوسیما هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66158" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66157">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=ksFlLNufGMBwEuVTJW5lUjpdtq0cPt2HPKsY_dKxPmt5n6FAAuvDlwIjT8xjP4u7MmWQ7KW07foHrHrv_lvzShnkYVrqPIruX0tvll4UpoZbbli4QvjcbV1zhyI-VLlC0rphU3y-9seVcBBq75tuEc65FIOinjQqZELeRoSQTurTFPRp8yb6RO7SDis_zch_IZf6Q7NfLIQp79PL-DbD7iN9Ox-yEbHBSNZQU1M5STrWFxJHJXZh8QMQweYhsZ-ptLjzeZ403VxkAf46nkYF0aJFM4j-UqJyMX8TNfGo9DtCjHHsve7f1vF_fD4_afI7bLCsZd_dF9-IZWsWBlvu2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=ksFlLNufGMBwEuVTJW5lUjpdtq0cPt2HPKsY_dKxPmt5n6FAAuvDlwIjT8xjP4u7MmWQ7KW07foHrHrv_lvzShnkYVrqPIruX0tvll4UpoZbbli4QvjcbV1zhyI-VLlC0rphU3y-9seVcBBq75tuEc65FIOinjQqZELeRoSQTurTFPRp8yb6RO7SDis_zch_IZf6Q7NfLIQp79PL-DbD7iN9Ox-yEbHBSNZQU1M5STrWFxJHJXZh8QMQweYhsZ-ptLjzeZ403VxkAf46nkYF0aJFM4j-UqJyMX8TNfGo9DtCjHHsve7f1vF_fD4_afI7bLCsZd_dF9-IZWsWBlvu2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت«
ال ریسیتاس
» بازیگر اسپانیایی از اتفاقات جنگ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66157" target="_blank">📅 13:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66156">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=TA9KD9NyhFc-PxDPz9AZqT05baxUB6KHZJYRR2DRbwviUJ1sqTYcD11wNymyD6TkGu57XzH9woKU6LQZRve-iJxWHM3e_UCrLw8byliRy-GIYsPFAqyPAs1IXnKeXoB8U4_jzLIGwCwNrVTGcDnbJrhL-CLl56UcwV-XInqLolttSoCs7ymGUmVXAY-urDYbfew7ATNdWRZ8PektdogyRcQbgnbbi_gYzxw1N-exvzGx4_Dr6YHgRsq4zRh-yRBJ67YMECzePxy6q_4A13yRAtsP1W-RAMJI6jIy7nno6Kpy4NkKhsBvqq2zBAd8foVbGZryPUqbXSTE5zkLBTueSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=TA9KD9NyhFc-PxDPz9AZqT05baxUB6KHZJYRR2DRbwviUJ1sqTYcD11wNymyD6TkGu57XzH9woKU6LQZRve-iJxWHM3e_UCrLw8byliRy-GIYsPFAqyPAs1IXnKeXoB8U4_jzLIGwCwNrVTGcDnbJrhL-CLl56UcwV-XInqLolttSoCs7ymGUmVXAY-urDYbfew7ATNdWRZ8PektdogyRcQbgnbbi_gYzxw1N-exvzGx4_Dr6YHgRsq4zRh-yRBJ67YMECzePxy6q_4A13yRAtsP1W-RAMJI6jIy7nno6Kpy4NkKhsBvqq2zBAd8foVbGZryPUqbXSTE5zkLBTueSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حمله اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66156" target="_blank">📅 13:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66155">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1JE2sb8pHs-_D0B-udhmsY1NH-qF379bVadjVRKmgsLISSS6UQc0urn7CgH_mPVtqV43iBctY_aELKMUQtwmshWzCGEW1WMGlCWPglIgQsM6R0O5tkqUvcMZG4asTPkCFKmxhWLuOS7MuDGRzgAqQjL9kbTu3KYe0ZZjO_Wr1yJYI2-23tGapk_H4DQsEDVEPIw1_QW7KFKJCI3BpLGM5IxxB_1hvCACyPruh8uiY3SckC07YLuooZEmkgqws2taOG9KbxF5PYLnJBTUtR5xCLDNnIrhx5oHSDayQ-ZPlllPnr4rzk1khy6iJMW5xkT10FItmK6r5f-qsKMwLUOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیس پزشکیان به تندروها:
متأسفم که به کسانی که دارن با مأموریت قانونی برای حفظ منافع و عزت کشور کار می‌کنن، برچسب خیانت و وطن‌فروشی می‌زنن. انتقاد کردن حق همه‌ست، ولی تخریب و له کردن این آدما کار مردونه و عادلانه‌ای نیست.
دولت باید از نیروهای خط مقدم که جونشون رو برای امنیت مردم کف دست گذاشتن کامل حمایت کنه. نمی‌شه ازشون انتظار فداکاری داشت ولی امکانات و نیازهاشون رو فراموش کرد.
ما جلوی هیچ قدرتی سر خم نمی‌کنیم، اما در برابر همهٔ مردم ایران و خواسته‌های درستشون پاسخگو و مسئول هستیم؛ نه فقط یه گروه خاص.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66155" target="_blank">📅 13:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAZiXWqxWOzUs9W9Sb8jxCSyQQZX13kJGlKuKm0P2QldgfQSVv3dv3ADEN-4Y8bwYkQc1pM-XrOBgpj827ELiyOA378gKufqH_lFRsnuKVsbi2A1s1Htv1on6KbYSadGcKrpridMmcdoliIt4VQ9AU-A17CUMRXClXsufj313fq1EDJPU0pvD-AOpWrb3KajjWlRRMorO1ZmyX9r2tzmZfkjKJAgXAv8eYOSWftfcHbgHnaqpbYf7Q3QouadIH9xgGlHU0dug5F8xqYn3d2M0CZ-FH_VWTnxmdMf0kqrZ5p_33FgEd2w6sQW-tdYZ6pnENZr7aNTYCuyLqrt59_H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elwCJw1cVbi2i4b2d7yHrTimDTc0aL1vAtDowGClAShlU3exsVMAEnIVBG0GwFChgL0eomyTUFfda25VYuzb-EMbo4E_9jHeaRW0X0AM4VmFT4w15Av4ANwjCoC5_A5O9afBiW6zjPvMzFXLhN--llLumtmQuzcbhnhJ91poRvNU1bX9Y-LwcqVbr9kM38Bp4KlEurpI7XAuY79lzFMIx2Oh4DN-168cmHUve5o-2OI7O_1CDfCfh7dMf2r00y4Pww9ovCgYSaU-7GXL37drsp_Bu3zd8QfEY0ngYAVTjQgF0uz23ECty5Smzf4Pka4Lkbb2wqrGM7j6HAWJ5uJedg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حمله هوایی ارتش اسرائیل به الخیام جنوب لبنان!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66153" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66152" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5dZ8tp7Z2BnvEsqJrDlaOIPvlP5DqFeRIP5dum02_ZheScE6iV2VXlrbAcNutaYZJSdgzC_xXO3DUjFFwKgrG79IGL1IAPJ0SZHyIxIgBOHlbYg8n1VnB8gaaKoALkeZLwi18bxnWmn9WcpaNb7CTGzqVSFU6VMKHMXL2HXioIZy_lSQE6cnFdRHAE2lOZp8SKUisF4NMCcLtd3-tSvASerCyGjtwOkOgakazju8fiBe2ocQrlLqG5l5_IKlechUATXhMVR_oZoxI_SaI3INYn84wWSYeUwOjomb9yeuMxh95fAmB_T3Vk6IUwEX2vn_iBddEw_xlEhdix4VjRjwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66151" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWnHklLKoP5f4kXHee0i8MnFdL51X2lf-7NM2MpnC0wnnTE1n-KHCljt2_UEI_bjUNGUe1zrJQb3CuMiEHj96xahiuLnTDuR_OAFWk8w20VifAl3-V4MRQXpoif2wxKgm-Dl9KAAp6hNf48o94Kg677L2LaOPOYsoMcIo0_hGrfLPqkV6OewxVaHP4rp1ZhBW1dXsL9f7IxZrrz-q3x2z4XZeXMMBW7blj01__RnHE2I5sAvgPVLUnxPvKlXHRX_FDnM5sl0GJILsb6Jpoul90M32g9_0b5pJ3Qo1zm8yjnXE5nzSE3jcm86JXF1FzZ7VWEcs5bo_X6shjCoRTtHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیده شده در تجمعات
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66150" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyV-3NeicdZBVYQHbSLp8PSHOqxwoGnnHxBQMSRwsSg2R5nXFWsNrxD9fIa34soqW3hbQotlPaTTVWHTWOfbkx1tasqIMzXm7YCBgW4udXBs5xk3XfCEeOU_NjE4jHtAfmPdj4sy2U3njPnaN7lc2fIBLeagh1T3Xc7V2rjkMOX2bEjfeVpMGxzrt0E9YLsLmVP-HP3A33GZLPyummd5KW3JtEHHWtlwOl-PNgMjAUaSAVTwLL1HEME8SuwrQbpUCPbJjB1NOIc_JS7S5BBqvOByobJliQXoI7sxKpAvJXksMxZtzZAd80ALOXfTVyXGJaJ_ylmdRuGrVbf_9NCDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل, کاتز:
وزیر دفاع اسرائیل، با رد فشارهای بین‌المللی و هشدار به تهران مبنی بر اینکه هرگونه حمله‌ای به اسرائیل با نیرویی کوبنده مواجه خواهد شد، اعلام کرد که نیروهای دفاعی اسرائیل به طور نامحدود در مناطق امنیتی در سراسر غزه، لبنان و سوریه باقی خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66149" target="_blank">📅 11:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=LAGvfwNQwGDK3mgd0Kiml7iKOSQXitk6U7KemxtiXK3tKIvIsyZ2pVm6qxUogA9CxKx90oOoZucxpHaZspg8qEddeVwztyPeawHilI5ITOHHaCotfhppTKPKDGoav2L8bcyJp3DN5sgBnjvevMiQs6VqHYz2BOICjwrIsiTTG-WE0_iMdZ6x0VNDG8Gw16CUPFXlWGUR9Xxvg0iC_GaY8YBG3rCRSbncHoiNVvcrmsw1KdoeCqzyLFQ0FAsymYA_rYAkDrDGEYNmee7c01VLQp-zZ7Bzh-AjWYwESvUH7tT_8TbvAd-JhgebA1O2tRam1o482LXzaxIl7jdJRHcofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=LAGvfwNQwGDK3mgd0Kiml7iKOSQXitk6U7KemxtiXK3tKIvIsyZ2pVm6qxUogA9CxKx90oOoZucxpHaZspg8qEddeVwztyPeawHilI5ITOHHaCotfhppTKPKDGoav2L8bcyJp3DN5sgBnjvevMiQs6VqHYz2BOICjwrIsiTTG-WE0_iMdZ6x0VNDG8Gw16CUPFXlWGUR9Xxvg0iC_GaY8YBG3rCRSbncHoiNVvcrmsw1KdoeCqzyLFQ0FAsymYA_rYAkDrDGEYNmee7c01VLQp-zZ7Bzh-AjWYwESvUH7tT_8TbvAd-JhgebA1O2tRam1o482LXzaxIl7jdJRHcofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان مقیم آمریکا طبق درخواست قلعه‌نویی واسه حمایت از تیم ملی ریختن جلوی هتل
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66148" target="_blank">📅 11:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJX32uFKBAJ_Ad7csCUm8rbdUmluidGHbkbzju1sqDZdypgVLXFHZddjGk5IpWj6b-5cHMSvgzGx1_EaqWztZ0pDfOypph0QZXU-_LKh8AmMM2F9wh876TDG91tLSCZcwcDDO4-wRnTH2J90rV0CAOZxmxFSPl0GRbwANwWWg2SrGNeZSJJLWCQxqEkP9uSYzdnWLHrNjFlB3fty91_7biEGA3wabsUUFvgGADN_dAh-fMeAWmM5EISlyuN2koC2fP_xpUFbXbSNOYtcGX-phjuGTox7MvDRoutqTvyc2hTodzlprdXZ781JawF_YwP4LF_LHBSKzanhI7ZoBCP-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت عرزشیا هم اکنون:
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66147" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwYve5hzumFoRoXbFtCMYsirJVBA_TCgTXvkllP-LRV_57HqCQ5L1mvkjrHB8_cq-JYhIuXMfa-IUr_xaJg5g2f_FKF2bPr7ABgQTV0Ku95WSaydLba4HHiXVmspVEGAJOOhKS0PvEsYG3_UFAvrJV28rIQYdiCv6mr6lOagjCLclWKnGoV8W0xtGPAsYkV2aUCwGqtHXTAYDwAW4j20twqzz5deQIfXY1DDspHB_uA5l8TsY2MobuQElufPLkkEN2Z5n-frXP6WSLoBsMXt95fFb-xLGYKDJ_kZebRi9_bALELlyzOiKnlcJM-b1pW8sUJk_HQjXlhXJ-UlgOWdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عایشه قذافی دختر معمر قذافی در کتابش:
به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66146" target="_blank">📅 10:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccd116404.mp4?token=oQYuE59ol2RQPFfuWsI0JGAZoFocBXThBbDZZcNjQekWUunZymSQ_T6_teOMHTVunDl7GzP5m-SDwSl7lfiVgtqCPPeUyCBb_R7hZToWa-UyBnVzKi5N3s06EW3Poqj9w5b8mQ-68mt88u4Rh2KoQkR6dm1tAkm3PEGcjNoHgYJLBHdmvE-EsIHDQfaDc-7SAOEsHd-OBoKGluOClpNCiBpoCqXR4oWfPav_XWGZX2oGSQR9U8M-Qqv7jyA4keQKrxi7CpGsDXGWfHAeFxIgF8zTIFxmoqSkfA_lFLtiN6Zw1rnhcT8N698ruZuvyTSmEI6S_B3mx6UPaDihuVgp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccd116404.mp4?token=oQYuE59ol2RQPFfuWsI0JGAZoFocBXThBbDZZcNjQekWUunZymSQ_T6_teOMHTVunDl7GzP5m-SDwSl7lfiVgtqCPPeUyCBb_R7hZToWa-UyBnVzKi5N3s06EW3Poqj9w5b8mQ-68mt88u4Rh2KoQkR6dm1tAkm3PEGcjNoHgYJLBHdmvE-EsIHDQfaDc-7SAOEsHd-OBoKGluOClpNCiBpoCqXR4oWfPav_XWGZX2oGSQR9U8M-Qqv7jyA4keQKrxi7CpGsDXGWfHAeFxIgF8zTIFxmoqSkfA_lFLtiN6Zw1rnhcT8N698ruZuvyTSmEI6S_B3mx6UPaDihuVgp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس معاون ترامپ:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66145" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=TRGOF9cdZxYmmClgCcNrYkxUrfj9jXO7jgY1zRW8YfVZlFCXQzJJUQ_plPVMSuE3TZAY3t_bKTxqXXz3Aem-BM_f-EqIPG0xNWdc2c_Xf0lVeN5u2xkRdCZOsnIfl6EHfncrvkDWM4Z4EBDM5l_si3h_TcKR3fbIEdbIHNiuJGmZ_tWP8BUwewBsthpkQDdJDs_eStD13qX6xR7w6wBClcZEAi0QGDobZFGeDTXTdZcTy1M5pL3FuNuEflAZGnsj6ikUhT6dCAUNTETR9TRlX8YQustfgBcdvqV2qPl1pR6qtg7Gs_nOTSK7kVv_cU5w5xmT-lj161cWgsL48CCNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=TRGOF9cdZxYmmClgCcNrYkxUrfj9jXO7jgY1zRW8YfVZlFCXQzJJUQ_plPVMSuE3TZAY3t_bKTxqXXz3Aem-BM_f-EqIPG0xNWdc2c_Xf0lVeN5u2xkRdCZOsnIfl6EHfncrvkDWM4Z4EBDM5l_si3h_TcKR3fbIEdbIHNiuJGmZ_tWP8BUwewBsthpkQDdJDs_eStD13qX6xR7w6wBClcZEAi0QGDobZFGeDTXTdZcTy1M5pL3FuNuEflAZGnsj6ikUhT6dCAUNTETR9TRlX8YQustfgBcdvqV2qPl1pR6qtg7Gs_nOTSK7kVv_cU5w5xmT-lj161cWgsL48CCNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی خطاب به بسیجی‌ها:
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/66144" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
ترامپ به نیویورک تایمز :
اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به نگهبان منطقه تبدیل خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/66143" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=S7zDJZ1DimiP8VKj5Zzp8g1WGOvkgD0R_D-jPjr20xIz0foWkZwWkeHqg_E42vcBJ2Nr7QcvdvqwUbE_8a_1ztcxFE9VTebyTZwvEXe-Lur3Mphx4if5NhtI0RKJvzoBo1QCWaE5JSpl9o5wAqdKbZBP7CyqRdQBjDBfiQusZu9bOGjXCnQjeNOThdILblwwGsgU3bsUmj8_k40hazA3eOI_tT8_E1GAg_CR7g0ethVPO8YxJrJL5eTM9xGMCbnAVCkQf9eCuM_OaATsLH4nJ7r_CNpCe6yo8VXcOfPuHVYtDO6VYNid-RgsOqgOQJc6tj9iHclRrd1P9hKpLTVzWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=S7zDJZ1DimiP8VKj5Zzp8g1WGOvkgD0R_D-jPjr20xIz0foWkZwWkeHqg_E42vcBJ2Nr7QcvdvqwUbE_8a_1ztcxFE9VTebyTZwvEXe-Lur3Mphx4if5NhtI0RKJvzoBo1QCWaE5JSpl9o5wAqdKbZBP7CyqRdQBjDBfiQusZu9bOGjXCnQjeNOThdILblwwGsgU3bsUmj8_k40hazA3eOI_tT8_E1GAg_CR7g0ethVPO8YxJrJL5eTM9xGMCbnAVCkQf9eCuM_OaATsLH4nJ7r_CNpCe6yo8VXcOfPuHVYtDO6VYNid-RgsOqgOQJc6tj9iHclRrd1P9hKpLTVzWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم لبنان و نوچه‌های جمهوری اسلامی پس از اعلام توافق ایران و آمریکا
و عدم حملات از سوی اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/66142" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
جزئیاتی از یادداشت تفاهم ایران و آمریکا:
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
آتش‌بس کامل در تمام مناطق و خروج ارتش اسرائیل از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/66141" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV8ONIeHNwsO6Tjwghl58RZDGW-tDW4lIafFnXsEYrdbvdZksNq2m4bBBKbQ0g3B7wKgtDueX5tA8HYGp_J8EUxYJJSvg1DnWRZ3jaFi0VxzSBdTf6N_i2VKZoRjLXG3UUW22-krU2kAAarmg33YRxrs4meMnzMAPQU2daTQgS-qlmy7VXNWsvvkT71snFixrDSfW2GGkKfZW57AuE_0c8hPQ98nZDQfqg_mWN3t4MPzE9fFNZZIWAsX2noxq9Lhq_BnrKVMW-kW5QOJjIcLMLZ6yq4iNR092MyWEUSJzhn-FS4FD9h79-gndpJlluWmXccInMC3qxmxXoUT7RByxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/66140" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66139" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSnUhsY0KC-Ger8_Gv24gJbFR17blR9_KTZe07WgeDUp51j2AS2eH56ong6B6xdl5Ru3AlLe30S_C-IC1pPFqolge0gXw-0FM0UaKmdtwlbYqiz5gbl_gglm3yU96kRQP1_q_Aei3fyNImdBPGHK_MqRgVWxg4r96qMbX5K6LHS6vw-BHHNxKJotS-dUOP6gOnPYgG-U7TCAhWuX3P92wCGQv-6RxCZDUmy3PfNzLxTLieN58Cqg1_TXuTIiWGeZ18HE2m09b-p9ZPZEniTMN-4UsIZn-WyX69uwTs_SxsxwelrWRznwidAoiX7raIia9KdrvMqOVULLv_g64Z9L6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/66138" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkXGIppYc-NPVQtGIM95pVL7tRaAGrzfbgXWaQCxOpMcGaxaeqf5u4Yl8fZB4ANjLEQdF_jh9vQWwR0aUR61ghIHY5Z_Kc6NtXyBaKkGBViiR3yllvQ3uWZNd-yW9zRHxyzLRqIk46v4rtNAZyGa3Kgu_n6x5g_d_IigMZwqM9kIr22elRlpirGiVGbUi-Iw1lngHZZq5VD1kx2SilQc604W52maXvgrM2hEmOG4-p8p0EUFZV99komuChJ-BBG5zdo23Wx8HX3OPbzS1GWGH0zqcv8vBor4POEtuKSMx-oxJlYZDxV4UGrdGiW44CdCYgwyXPTZCsCPGryE-JMSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیتر شبکه خبر همراه با این تصویر
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/66137" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=jirpHWhDAUiXd0ERif0hTesgRkaT7rgLaEdyxzLdFJ-CxaWnRKnp1Y-QTA5izSE1S9CTJR3PDOEEQwhSWenLQmvUV5w8YAv1W-0CNeg-N8IzCuJ8LC3bwVmHLlv098mw0WyiMSf0omICHp0tma0LKjM0e_J1VsmuicwGwzbsbMGY5MLOurTKGCS8ou5ZbOeseJrYbLfd9G81fqsbQVryqHg8EShZib9ywWxSIs7OqIC1G98IBebJCAUim-0jytaxd-HGQzK9sPvjfNyiRqZLA2nmJT6i7MKrb-VbQZ9nfh212NhNQKFRCcBCGkKLBZe6beRgLa6H9S0j1n_u-TRk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=jirpHWhDAUiXd0ERif0hTesgRkaT7rgLaEdyxzLdFJ-CxaWnRKnp1Y-QTA5izSE1S9CTJR3PDOEEQwhSWenLQmvUV5w8YAv1W-0CNeg-N8IzCuJ8LC3bwVmHLlv098mw0WyiMSf0omICHp0tma0LKjM0e_J1VsmuicwGwzbsbMGY5MLOurTKGCS8ou5ZbOeseJrYbLfd9G81fqsbQVryqHg8EShZib9ywWxSIs7OqIC1G98IBebJCAUim-0jytaxd-HGQzK9sPvjfNyiRqZLA2nmJT6i7MKrb-VbQZ9nfh212NhNQKFRCcBCGkKLBZe6beRgLa6H9S0j1n_u-TRk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی‌خامنه‌ای یازده روز قبل از ترور:
امام حسین فرمود کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/66136" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66134">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=J2wlPzUYoggHzmJwhW0guBhqKL5zLFul0i1jDjJQJfJW0_wJYw0Pci-sjpqUOjyAc3NG96xxQf0gdb8DsSxdOiPFE1sF7Ab7AktfhHN0Z-NUzytQTUVzgbpVJgWjFULj0vKCemSGfJeddirnXROl3ifwZGd1hKVRUa5fQL5HitoHIxbn7aY0MfdM0JsKKqbOc-wd3QkAhFLP4KpoUPEdNmGFdd53cue_CLLN6pwccpiWGA88-5V8yB8di78rEFKcH4Qb_A2MKop6tgdmtOcmaUmxjRqY6fRbQDxXKutyUwYrtQHzl8tH963IHKa3fz56fKYi7AAp8Rv775ufS_b1Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=J2wlPzUYoggHzmJwhW0guBhqKL5zLFul0i1jDjJQJfJW0_wJYw0Pci-sjpqUOjyAc3NG96xxQf0gdb8DsSxdOiPFE1sF7Ab7AktfhHN0Z-NUzytQTUVzgbpVJgWjFULj0vKCemSGfJeddirnXROl3ifwZGd1hKVRUa5fQL5HitoHIxbn7aY0MfdM0JsKKqbOc-wd3QkAhFLP4KpoUPEdNmGFdd53cue_CLLN6pwccpiWGA88-5V8yB8di78rEFKcH4Qb_A2MKop6tgdmtOcmaUmxjRqY6fRbQDxXKutyUwYrtQHzl8tH963IHKa3fz56fKYi7AAp8Rv775ufS_b1Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگر این توافق جمعه امضا بشه تازه میرسیم به شروع سناریو زنده یاد مانوک خدابخشیان.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/66134" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66133">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
‼️
دبیرخانه شورای عالی امنیت ملی جمهوری اسلامی
:
آماده حمله سهمگین به اسرائیل بودیم اما به درخواست ترامپ و پس از گرفتن امتیازات لازم، از انجام این کار منصرف شده و‌ توافق صلح را پذیرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66133" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66132">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd274791.mp4?token=bHKkTDMyQE-ZwaFHq1VDBK_G-dtp3h0KOfxppdX-hfzeXEjRVCwpH8sZ0GG1K-vHyS-sn4tVIrAWTwrwTtMzoLqv7GnNMt4rx7_pi5Gls2g_qjhP-F8D9IALMioxPJLx7dF-3W7G-rLCO1UYfPNFQKDZo9-VziAMW0XMXqIM27WnLs7opc2-imqJiEmOqljeeqbvO940A1CKMFsDoqEvyE6Sb6rvVdsopoqlKa6F4JtPrfu3nUBV4zQ_0f41qM_m_KQe2uGGFbT8upKO3nV9vfn33S-t1KDCzmWBbofO-7VwGNGJxrHgkjZBStOJ7DfcTn5qICVP_AXHASw3sO7k6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd274791.mp4?token=bHKkTDMyQE-ZwaFHq1VDBK_G-dtp3h0KOfxppdX-hfzeXEjRVCwpH8sZ0GG1K-vHyS-sn4tVIrAWTwrwTtMzoLqv7GnNMt4rx7_pi5Gls2g_qjhP-F8D9IALMioxPJLx7dF-3W7G-rLCO1UYfPNFQKDZo9-VziAMW0XMXqIM27WnLs7opc2-imqJiEmOqljeeqbvO940A1CKMFsDoqEvyE6Sb6rvVdsopoqlKa6F4JtPrfu3nUBV4zQ_0f41qM_m_KQe2uGGFbT8upKO3nV9vfn33S-t1KDCzmWBbofO-7VwGNGJxrHgkjZBStOJ7DfcTn5qICVP_AXHASw3sO7k6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دود سفید در کاخ سفید. طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/66132" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66131">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
📰
تسنیم: تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66131" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66130">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_hdnZIFGQrS_b0RLQkKAUIg0d160EnNPONA7OGL7NEKFFiaSxPtH2h9Q-pFh6O630hjIuRiqRu0-LQtu92fGpdG9ztaP0ne3yrcKW7xgVBs2hVakx4kHgbf1xh1vetN6c3NbvYgi2eNsqBrhSLzqM0FDNS1qIAQG60pjucfWiDLCFnS2E42AWdsIZb91K_D25_RqmUJ7K0Y0Anvk16TkLn4H49u14G9W_ugdZS_YOEszS_fQIWZk2zcu1b6y_-gG-3rRHgiZI7PgT_Fpx9FlDYlnzz_113VwhVds77WrTD9C47I-lTCD7_xdMqde7A7550AyKtvKSXfrY2y034msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
یکی جلو صداوسیما رو بگیره. چند دقیقه دیگه تیتر میزنه آمریکا رو نابود کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66130" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66129">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWdZsvVijAHKukYq3YLz_Sl5ApNSJUMOELLv0UgypErDUdnznTEHqMGatjvrKpBgNUOkH7oj6TQWQt9pMePzE4Ctxdw24AqHZYkzs1RWCay58xxxXNPnNJ8Lp77vXCX8trvGKww8y1tYioUgHWRBdNBo0GHexRRKm_p2LdCzTPh60gM-6uky0P6F0WN0BsaqyjY5KQ2iMg-1uSRIUl3dPRKFY7QCZ6sg1iDZKs688EyTgZahiF5whlkKw0rPXrJO_oWRPvjU90EsHEwD8FDnHDhUgqMahoPrs6FUqZI8bsEjfLMidohHK4R-2fwut4HYxfRdkUfOq9Clhd_BRiQBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان وقت چیه؟ آفرین حمله به ضاحیه بیروت
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66129" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66128">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66128" target="_blank">📅 01:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66127">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRVLEzVeKpDeI-Ewx9nYK-8XshLdolK7uF1T_Iq83R_A6Ul7k0qbyjnh4qKVIErlBk0sO_wtmbOa4Xq-YVHNImyIVUhE5NzVVCjOoUkCteLOB-NE8sAEK1YhoD3sqg9GZ8PAddcHZaPwF-mov61x1DznoV-FCxiVMKFSCpToAoD9Bdy3pCmV__aGpV3SIbng8W31DKrWiFJ7TjyWr4QUkE50opxcSbJA4xWu199n0Fivh2VFFJ76N-hKG9loB5yRJHjibk3tzmdISDs-kbJwcm0qUe8SCOe0Andg0f0MaBta3Kp6BhJ2VbTF2NGfpok_iEOq0GusGvF9JrWvIO6B-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام خون رهبرتون گرفته شد برید خونه حالا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66127" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66126">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=o02Deg3CcxOJo6x562DYupgsDHCqE0UTOIplL9x7KwGUmla06owAamLD6I9kToVOFSdapC_vJNgLm9ZgoMuScKLnblDnRb9jYQDiW4SgnlrFko5vdL5NSk2dzqIwKMG88Cj0dQemIBIZtkafwLWJInitL7DxKGNyqBV6JjT-MWzzVOvZjJYGUuCFD_EhD85yYKuXzSLWgD7BZH5sEuf-4N8NE_1IZ-Syj0HKBJmSveWW-XtyLgkIAqNDQooiQI7mt6dfNSwpNPmJWpA3khsXiv11G7KhJ12SI_y9pbhoSvu1tcu_McyYa-zk8JSypBnVmMzMv7zLR0NiB98ONSQu3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=o02Deg3CcxOJo6x562DYupgsDHCqE0UTOIplL9x7KwGUmla06owAamLD6I9kToVOFSdapC_vJNgLm9ZgoMuScKLnblDnRb9jYQDiW4SgnlrFko5vdL5NSk2dzqIwKMG88Cj0dQemIBIZtkafwLWJInitL7DxKGNyqBV6JjT-MWzzVOvZjJYGUuCFD_EhD85yYKuXzSLWgD7BZH5sEuf-4N8NE_1IZ-Syj0HKBJmSveWW-XtyLgkIAqNDQooiQI7mt6dfNSwpNPmJWpA3khsXiv11G7KhJ12SI_y9pbhoSvu1tcu_McyYa-zk8JSypBnVmMzMv7zLR0NiB98ONSQu3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش مجری شبکه خبر به امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66126" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66125">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDffhK5s-vup_bL021xuDA7rw2kc4VWK6E65xLKzqnoiOgH881QgoSQe5wET409JWO9hCJPW5wVbnkrCYi4HVBqA2zgdMl8iW7VHkWUR6ZiuyNvq_yirNKidI3fCVJ10IyFT8SHAi9MVwaFcsyOUoFhxoz3IUfh53Q92lkuymE4al_W6DMJe1ZZhHtSJnKQ60PcyALidXKquzIGzOkQBuWpmgTRRdEKptWhPbGCNlOqYH5VNAC4WHxixR3q4vK86z6dQGPRwgAqjK9YWA_WkfWp2-q0Bh6XLhwHUmOt0bAmHazSuL5iRrCcxCpo5sC1dHSpdj5mHlGRxaWu0L9GKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری
؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/66125" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66124">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueeGnFcfokTYm7J4TntV3EM1B3rVu3tT4CjaSTkMlXn_evmUOzDgg3QBHh0TiAaEq7UWqYmNG9tGVZ4BZYlyAl0eFrUjdqEHScUz49CwHM9tYwO2Z73UkOVLe6bBljEFneYeNMoUaQZlx7ZUqX2CK3jQwPw67K32kQpgCt9htwXU8BXaEtby54ozqiB-3i1_utMoxpiI9bAYsBD3nKGaIUxq-32xwMni-ja3CXl_O2dFrVjY2wFWM2pE8ruS6Ll7y0XdbBx_DEHYSOANK2koUCEOQKjaR5aHzD5vqewSfRUvFhIBcP7xGiQKPmEgAU67gus8oAUIT8YIvIjZGYbm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زیر نویس شبکه خبر:توافق با آمریکا انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66124" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66123">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
مراسم رسمی امضای توافق روز جمعه 19ژوئن در سوییس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66123" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66122">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇵🇰
🇵🇰
شهباز شریف نخست وزیر پاکستان:
پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران دست یافته‌ایم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد.
مراسم امضای رسمی این توافق‌نامه روز جمعه ۱۹ ژوئن در سوئیس برگزار خواهد شد.
از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این منازعه صمیمانه تشکر می‌کنیم. همچنین از برادرانمان در تلاش‌های میانجیگری و رهبری خردمندانه کشور قطر برای حمایت‌شان در رسیدن به این توافق قدردانی می‌نماییم. به طور ویژه از رهبری خردمندانه عربستان سعودی و جمهوری ترکیه برای مشارکت‌های ارزشمندشان در این زمینه تشکر می‌کنیم.
پس از امضای توافق‌نامه، میانجی‌ها تسهیل‌کننده سلسله‌ای از جلسات در این هفته خواهند بود. این بحث‌های مقدماتی پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم امضای رسمی را فراهم خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66122" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66121">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
نتانیاهو از این توافق حمایت می کند و این برای او خوب است زیرا تحت هر شرایطی مانع از دستیابی ایران به سلاح هسته ای می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66121" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66120">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
محاصره دریایی اعمال شده علیه ایران موفقیت‌آمیز و قدرتمندتر از حملات است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66120" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66119">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
من هرگز به تغییر رژیم در ایران علاقه‌ای نداشته‌ام و در حال حاضر با گروه سوم که منطقی‌ترین هستند، سر و کار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66119" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66118">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: ایران در ازای توافق پول نقد دریافت نخواهد کرد، اما ممکن است تحریم‌ها کاهش یابد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66118" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66117">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
ما وقتی آماده باشیم، مواد هسته‌ای را دریافت خواهیم کرد و این اتفاق ظرف یک یا دو ماه رخ خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66117" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66116">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi4jGPB3iUZKrzSpoWuoFeeNEzl1maNPK2zIj3AWY3zwTgkgkojdpU4BuAaTPKJr5gEy90ZvY4CYII6GsSL3oShElRS3s6gmgr98W2_z696mU-NaK1F0I7raKBn1YH2H4_l6W7yZdnPaIbZalrggfuZUZR9DUPcnBbgRwtWSlg3bxg8bI4OoOOHcQu81hDpWnUsgYofYml3AJpUnRiYVpBPhP2SeaQ2locsBZgwrBxUo-cyhcW7vGbxK7l_02M_Ar3aazM1nvQ9qHhmOvJ106ofpyJ1LKyqLbZCx-G85SIcyIJQAy5D6ESbdrgbLFejZ4vBKdZheyjuvxFud59ILRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتوای تماس بی‌بی با ترامپ:
#hjAly‌</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66116" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66115">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ و نتانیاهو دقایقی پیش به صورت تلفنی گفتگو کردند
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66115" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
