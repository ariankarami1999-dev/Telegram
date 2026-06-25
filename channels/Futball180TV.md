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
<img src="https://cdn5.telesco.pe/file/cv7jVK8Vl6vgifbZX9sOzIMHsn3Vr7zsBF3F20X6V7-0eXZ6wJSrZ_f68NCWpXY5SIRg45Er9-IDf04K7DMBUrYf1e4YCEo24aiU6t4kPcFKZ4xR772S-Sh8AMaPvyX8Tq1-DxwUhDTI-yizf2JtIk4eX2BD7ZaCG3R7BXzZjL7aI2ZiSA-M7UIsQsKdkb5A6grdABeHERZiwA2INKYW60qRPShAiaulEMKfb4ms8DiTs9ZC-0oICj1e9rVc6UPUUs6NKy_ZsvInR2Yk5OrQTu7jWbdFl8MnWQMEU0QeFsycjtiOAlDdXfzljTgFNaaVsjOLmlWJk1mKlG1STYgXQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 706K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 03:29:47</div>
<hr>

<div class="tg-post" id="msg-95789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaN7SuOW2MX_OTYhTuORAwhicqI8Qumx0McRsiSNpx_8sDtILgfD14ssPnNh4WwEkJeHPinhtxkrRHuuEv8iBxzZhqiFEVpmbhGk9DGhy6AHdewztNDopADKoje8BJsul4LE26meU2-F-HR0UUvedWEVM1u9m8Cgzq0ijaRzHmFmUmJl2JT6JOWy-bLiXb4GbV21Slp4IK6VxxqVsPykntBXVpBMejwCcw0xvy-eTjvv1MHqaz3af8-54m_Txo0W1QmUEs24i1gJt8EGktuAgQ2a0GV0QlG5D_B58_RqAwQXMSm0Ctru6b9mt-e9RC_aArTEK_UB9cBKtid8yVjO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WV7zkXi_KHKhVEolXP7dFNJoz3Kh3W_uEoTmyV7-KXIIFLQKr2rYuVYOVKfQKu9Im_3PP5Zb-ApLJKQLgh1hKjy0Oc72p-tjCzo3qQdMzKc1JRT3KxmqCqI1Uo8udWcZWdAy2-OfY8pNLRHdAZMQ3GmS0f6g9D4WNsahLLS2b5VrdTJtMvoHdZMR1Gfxcq2JTJMDdi6neaF8WfoAuz6Uhp7yuygJEavqd5XoSbL91KfzbbUNNy_NQ0lS4WiC05o8uMVRsduSZHOOXdR5qt-K2V53JK-trvmsaEWYPtV6N780ATbXcgZ9JWttawdNFbKveAEx99jPyynwHoEtoWCJqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🇨🇿
ترکیب رسمی جمهوری‌چک و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/Futball180TV/95789" target="_blank">📅 03:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M55HhxrMqtiirArd89XjbypjlF1-Y2Z30Y1H6XMeg38Sgu015Eaqx4MG8Fh45kg8d2xr1Kf3MNAGPsKojn4TK1y8V547mI6cqXV1neSJ7rxYKdtYGTTOBgOiRJI0xDKDsSmncEyipGRuKnHU7BnzD-xZvaHl4olmQYG9wqNZF68KAHE_saIfbCbHw555QgLeS3R-sfP6V79argae1yZN3CBwkIonAnkCmNWN_FR5TH4LZCbuMfsklWxPR5XLfpO-hP2VYHW9fGgSjclF9n9I33l50L_iMo1yk4EEFjNNL36D0N_hvv88eoFlWwxvvwYl4_1j6AtLEECbfjy5zA4wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/Futball180TV/95788" target="_blank">📅 03:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=szIgMXOlxsRwXZH5I70zN1_A7Pk_28rtplpuvo3TG4l_Qe7EHQ9jZ71Wc-a5DnrwMH22jtHpFRsHH2weGioHvqYdNouObGkvYeZ6qWkKMhuOUBT7v-J84zzHZk-QKl9ziqT1oXUmi_xWZYbfM2jSq2ACefTMa0JL8aJfLwYTyIXrehUVk5_pBwUYNcaMaaYuWLhpgbWtfYEifKbG0vyPaKjWVQ9-brbsbse8_s31hu7S5_0qkJTmA2WVmvvtdRP11k45XrYV-pfDRgYPpr-5MhgNv-aeYZmeqoSfiNev-fwN58W6bxASbhygzKoldPDmS5xvuaF-_4IJGOv6J-0qMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=szIgMXOlxsRwXZH5I70zN1_A7Pk_28rtplpuvo3TG4l_Qe7EHQ9jZ71Wc-a5DnrwMH22jtHpFRsHH2weGioHvqYdNouObGkvYeZ6qWkKMhuOUBT7v-J84zzHZk-QKl9ziqT1oXUmi_xWZYbfM2jSq2ACefTMa0JL8aJfLwYTyIXrehUVk5_pBwUYNcaMaaYuWLhpgbWtfYEifKbG0vyPaKjWVQ9-brbsbse8_s31hu7S5_0qkJTmA2WVmvvtdRP11k45XrYV-pfDRgYPpr-5MhgNv-aeYZmeqoSfiNev-fwN58W6bxASbhygzKoldPDmS5xvuaF-_4IJGOv6J-0qMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/95787" target="_blank">📅 03:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مراکش چهارمی هم زد</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/Futball180TV/95786" target="_blank">📅 03:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اندریک افسانه ای هم وارد زمین شد</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/95785" target="_blank">📅 03:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=kAd3TYBCmAAtQcwsDvTdnqXbjoRc0Sfk3Sq87baYbYdhyPSwrhBXWlGzIpR5W7AXwHOv1d8O1sL0Ihrsma4EuMc-3Y5FiU5_AeKx_zig11JvqVrdMbWqhEnvhptZJwd1gGsTnc8Gpjjzhm2MkzOSpaaD6C6pcBOtC8OT8ptS983kOr4yuifgl8EMHKGGcyYS5kRqAUGVqDKQO07EByo9eWmQgWHKoqMFUNUVD4nVUR5ZEFA1FceOvu2DLAow2jbqoLka79mkSdS4pJGqL7txuWuZeBhHVY2-SfmkusdMeKc7r9NFDdUZd93KFfoefl8EyA6KAjmU-WqLEgB42W-8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=kAd3TYBCmAAtQcwsDvTdnqXbjoRc0Sfk3Sq87baYbYdhyPSwrhBXWlGzIpR5W7AXwHOv1d8O1sL0Ihrsma4EuMc-3Y5FiU5_AeKx_zig11JvqVrdMbWqhEnvhptZJwd1gGsTnc8Gpjjzhm2MkzOSpaaD6C6pcBOtC8OT8ptS983kOr4yuifgl8EMHKGGcyYS5kRqAUGVqDKQO07EByo9eWmQgWHKoqMFUNUVD4nVUR5ZEFA1FceOvu2DLAow2jbqoLka79mkSdS4pJGqL7txuWuZeBhHVY2-SfmkusdMeKc7r9NFDdUZd93KFfoefl8EyA6KAjmU-WqLEgB42W-8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم مراکش به هائیتی توسط رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/Futball180TV/95784" target="_blank">📅 03:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مراکش سومی هم زد</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/95783" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/95782" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=RqyOf8Zl_CT7eFm2ow4_B_ZYVwezon90EC3_XyYqTp69OZNP3ejWdYfphWVkm56rN7RexH3OP5T4vGQgAMgSSr36dLyvUFkqg_PvsdcMXlB3mypmk91ZmK1zMhtI1y4VYpKOe_j_GxPgQZ4BmYkD-NtaWhcf_fMMhbgusgwoANkhq7F5-3MsR2sUcJhm_FqvRprWMw9kSWTtl80q2fwZoOzvy643HUoXNQGJd_R3sYozUJQbaMgmzx61ArzKuARgTZ7-dDn0kmeUnXI3JJFS2op27FxiUZE2xFAp1p5LAeUfz46cRgrmnqcsbTHgoflVmuzinqdwue7JyMdxXtnerg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=RqyOf8Zl_CT7eFm2ow4_B_ZYVwezon90EC3_XyYqTp69OZNP3ejWdYfphWVkm56rN7RexH3OP5T4vGQgAMgSSr36dLyvUFkqg_PvsdcMXlB3mypmk91ZmK1zMhtI1y4VYpKOe_j_GxPgQZ4BmYkD-NtaWhcf_fMMhbgusgwoANkhq7F5-3MsR2sUcJhm_FqvRprWMw9kSWTtl80q2fwZoOzvy643HUoXNQGJd_R3sYozUJQbaMgmzx61ArzKuARgTZ7-dDn0kmeUnXI3JJFS2op27FxiUZE2xFAp1p5LAeUfz46cRgrmnqcsbTHgoflVmuzinqdwue7JyMdxXtnerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/95780" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیمار بالاخره وارد زمین شد</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/95779" target="_blank">📅 03:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95777">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhDEUbmuGMqwFSN0QAGbu6JBkjacnuVqAdV_aNJ_oH8fsXynb8xll3yUeUQGrLtZpPA6EmhlOXsmHE9w-fmi7jfPi8cHddt4ecFSRsatZEiDEAC0HohZSLFCk9tzsBWzwxWJp1FJOuqwY5nmAYszU8o2iZnCeekHpzdaVGV5kKnIPO0tME9JiZ-Mxo-kgYU7AcS1_2SAVAdwfqdLZCj8_t1U7GQGn040W_1GKPPaPPGd9K0W9aDbg5chk5y9fI-sW85YpnPw_iRDFkwe2So0veTxrHurLo1GAlGPhnsp5XRQux_H3Pj5Lwvr1OGRSuysJcyDT4t-F4uSCuqIyJybAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nr869GgRIvZZsSgIsxoiMw3UYGyB7RDLY5ccSzp7AGRtz0ZDMJrWwgIxnl01M9X3gOXXLX4iAavAKrLpsIotJuHBq5WNW4NfbEtTziH2TnO7qVBzKvP7KmjMfwVMEATGI-Z610f5L8G32ucDzVRjvCOncdZJf4-AGACFrv7L59K6vCFem7LhAiLyiYsW08i6o3zFa8d_1yQSR8JTyH600tltBfsVv8nyOTqNgxR1rBVflB833-bQ444EmSc0KXCIMreKHLNtTu1-m-J4EDe1ktBl5oGbcPBv2Ym9J01iP1FRwbbtILFfoUim7UDBfXgukODVh1Xx9iB-k9ZWtD3TQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇰🇷
ترکیب رسمی آفریقای جنوبی و کره جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/95777" target="_blank">📅 03:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95776">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2gOjYMEpzhD1hvl5fR0eKzVn-08qFAdvFrmIeiRGmDUsw1MdXmfMH-osigFfUfdZ6wcBpa2DePSHUIdgLOP8jR-1vYfUSiEiWIcpyxGRhaGFUVAICHUp-ftxWzRN1aovO8Ax6ZPztVVhsepuNd5gxe2m83MvSGpUHfidYIPYjpwRPRDhOP09TIdxU-tJ-m4BqNhVPbOB66_NoWYy1tYOCOb0rvOt3vAS_ve0yj_gSKVpoIqlkJxWrWKO0hwIxUEM70XRavdV_dU0378rhlZwQf5f7WAQ-RLbS2QvqApCxcMWbdHdRvvSSJRz1E2GoViXm3QoYZR8UHVMcatnPGjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرفدارای برزیل تو ورزشگاه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/95776" target="_blank">📅 03:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95775">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=UcfLsHzXgTXkAxs4z7944HUPZdinJRruaT72vc7BYxL447Hv0eA4HiGG1_iQopAQ6AYN1J2-8pOjZX5gIIQN9rNVl6y3aoKlrfOF_e6snn_0wpyQ2t_hVl005JlsY75GOKC2yQloNGg1iUtctdVqZ4P5briby8PcKfBeg2ShHovj6PY93rSGM9GeGsG0WoIZFBi3mcK_dgmMLAk7S_JVVzA1lz7YJWQuKnMFz1VvRPF6GkLwDwLRGpi6OW7UMydlVi1Ud7rztMsVKY9BYMw_iAkLKgneEgYt6Ebunony2MxHlGdBWgxCRKR1Lv6LIsEmWdk0XzNdZn0KzJzlrF6V0jX82sEdgddjbLL1wNqVStHJwXUYxm1_D-j-FtKlWdVTn6vZ2c6NpINTZi0EdylJmtIaxxlrJKagittgWCuWUG8sb3k-BS8sYWl8KMvqmAIo6Hf0FssaMwCTCv4dJdrZNTgL0YPanb6miERECIg0niPUi8L7XqGUhVl2r29Sib9AJ7p_gCNfIw-eNP590s4cnzQe29lwIlynkT4e_YYnmv3Ck5SsRjBkfDuLM1fRy8JT2f8GWYhUnswIOC74GWYScBJhLOMUbmbtKYqU6sRH3jh3BgN9MGvjIYfXr_VeoIpp-71dpqRn3D-f2QkayVtNDKcBBhBJrL1npc2uBNWxqds" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=UcfLsHzXgTXkAxs4z7944HUPZdinJRruaT72vc7BYxL447Hv0eA4HiGG1_iQopAQ6AYN1J2-8pOjZX5gIIQN9rNVl6y3aoKlrfOF_e6snn_0wpyQ2t_hVl005JlsY75GOKC2yQloNGg1iUtctdVqZ4P5briby8PcKfBeg2ShHovj6PY93rSGM9GeGsG0WoIZFBi3mcK_dgmMLAk7S_JVVzA1lz7YJWQuKnMFz1VvRPF6GkLwDwLRGpi6OW7UMydlVi1Ud7rztMsVKY9BYMw_iAkLKgneEgYt6Ebunony2MxHlGdBWgxCRKR1Lv6LIsEmWdk0XzNdZn0KzJzlrF6V0jX82sEdgddjbLL1wNqVStHJwXUYxm1_D-j-FtKlWdVTn6vZ2c6NpINTZi0EdylJmtIaxxlrJKagittgWCuWUG8sb3k-BS8sYWl8KMvqmAIo6Hf0FssaMwCTCv4dJdrZNTgL0YPanb6miERECIg0niPUi8L7XqGUhVl2r29Sib9AJ7p_gCNfIw-eNP590s4cnzQe29lwIlynkT4e_YYnmv3Ck5SsRjBkfDuLM1fRy8JT2f8GWYhUnswIOC74GWYScBJhLOMUbmbtKYqU6sRH3jh3BgN9MGvjIYfXr_VeoIpp-71dpqRn3D-f2QkayVtNDKcBBhBJrL1npc2uBNWxqds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم برزیل به اسکاتلند توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/95775" target="_blank">📅 02:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کونیااااااا زددددد</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/95774" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برزیلللللل</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/95773" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگلگگلگلگل سووووومممم</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/95772" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=DTW_yPvOqHSUOgdfVHj_fnHXq7FVaMx-oaGTHJlHjJNB5BR5At3MV4P1UPpTTD7jclKxTcv8MWYx1HihG827dxCLQ9kOriltpUbBL1cVqqYJKsO-PknNUb3OECO5KnpshPKVqa5yqP-VqHBbFsha6lVqAs-sFF_h0OVHQ0cY0eBCUmrVNZXJAsDmaXPOEeNAP6CzY8OkvcL1-YlmGY3469eMENGYZRgVzSH49VLCvUb7WX8hu2A6f8QIaqrCC5p40ovKJR8XtbbgsKqr7PV8n6WLtU1XmQhCcQkpC6UCpeQJ_i1zzG-5dJFCoBM-xae_FCKY7oEdZTKvA5ZaiDZLCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=DTW_yPvOqHSUOgdfVHj_fnHXq7FVaMx-oaGTHJlHjJNB5BR5At3MV4P1UPpTTD7jclKxTcv8MWYx1HihG827dxCLQ9kOriltpUbBL1cVqqYJKsO-PknNUb3OECO5KnpshPKVqa5yqP-VqHBbFsha6lVqAs-sFF_h0OVHQ0cY0eBCUmrVNZXJAsDmaXPOEeNAP6CzY8OkvcL1-YlmGY3469eMENGYZRgVzSH49VLCvUb7WX8hu2A6f8QIaqrCC5p40ovKJR8XtbbgsKqr7PV8n6WLtU1XmQhCcQkpC6UCpeQJ_i1zzG-5dJFCoBM-xae_FCKY7oEdZTKvA5ZaiDZLCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشمامممممم زلزله رو ببین ناموسا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/95771" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=NQygvVammspE1L8-7sCU73NmLMek_pPPnlzAnivGFsrr_8B9hKPYuiA1lfBtW-6txsZ10gL05Y8Mk8CMi0IJOnC0n4KiQ3_oI4QwKGAnwxDVwLsCRXCr_O3m2ymSlWFY39mL109roNqlskI3S4_eeRto9svR1iaCVs3f1rrk1XCPWSSW45EHVhR-w3mAICHEJTmoBC56ROicCCYSFkyCJ2lPAYUr0G3FzcbD4IezKwNgRx-iRvwKiaM1uTHTC_BxMxzLFPma7RZbdq-V2wGumqVqMWtVaPSjGiO027FokHECMJz12wAFcVtcHAXR0-LkEtHMwHqp2c7YTfIEBCvhZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=NQygvVammspE1L8-7sCU73NmLMek_pPPnlzAnivGFsrr_8B9hKPYuiA1lfBtW-6txsZ10gL05Y8Mk8CMi0IJOnC0n4KiQ3_oI4QwKGAnwxDVwLsCRXCr_O3m2ymSlWFY39mL109roNqlskI3S4_eeRto9svR1iaCVs3f1rrk1XCPWSSW45EHVhR-w3mAICHEJTmoBC56ROicCCYSFkyCJ2lPAYUr0G3FzcbD4IezKwNgRx-iRvwKiaM1uTHTC_BxMxzLFPma7RZbdq-V2wGumqVqMWtVaPSjGiO027FokHECMJz12wAFcVtcHAXR0-LkEtHMwHqp2c7YTfIEBCvhZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو کاراکاس ونزوئلا زلزله شدید رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/95770" target="_blank">📅 02:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هوادارای برزیل از آنچلوتی میخوان نیمار رو بازی بده</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/Futball180TV/95769" target="_blank">📅 02:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شروع نیمه دوم بازی‌های امشب</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/95768" target="_blank">📅 02:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95767">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این آدم فضاییای ما چی شدن؟</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/95767" target="_blank">📅 02:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95766">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhFD1k-6tIX2aHLClQcKNSiqZUGkXBJ_WfMarMDtUfY7mVJc5cSHR3XmXhJJW2TtWx55dv7xbbVZ_2L1V-vDUWvIXxp-VSKgoEYeM0VyZYNo_ZqyX3r0jZ1YYp9XO7KE6l7fWRZSxldBabUrcMHRY1S2K74VaE8fjbiWsTtLUVQErSYCkNv9QtJbLjZDM1NkO32mYb8BDQiXeHlQimez1q6mlbi_ynbBn1miYiNd5JxzHIL9ys29E7vngJyG-4b32xQVVHrqPYji9q5hwgHT_BAtQf8LCSRwP-i8-qt-HM6-5C5fSmHa37RtT0H6L7zdraMHmdeAG9eV6tAeAYAsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وینیسیوس جونیور تعداد گل های خود را زیر نظر کارلو آنچلوتی به 97 رساند. بازیکنانی با بیشترین گل‌زده تحت هدایت کارلتو:
‏
🥇
فیلیپو اینزاگی — ۱۶۱ گل
‏
🥈
کریم بنزما — ۱۲۱ گل
‏
🥉
کریستیانو رونالدو — ۱۱۲ گل
‏
😀
آندری شِوچنکو — ۱۰۳ گل
‏
😄
وینیسیوس جونیور — ۹۷ گل
🆕
‏
😃
کاکا — ۹۵ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/95766" target="_blank">📅 02:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHB-Qr3VZ3ZaIb19xedvzchFucPRprcWDW7oEPx2ips7ML36caoJxeW-fxdGAHJQWNFL6Da30h8ehiQ25TA5CL2q_by_7goH9KbCJLFyA1A1xSQ0nmQ-a2SlLFumcZNvr3lm34sPRmX3ELpWM3WEOcrAnhnKszKwWAOVSF-FmQy9fzsW9BGHO32hj8VBQ6X9ffDs93JW29h_rE6W1d9dgGr_dYPnyQDsnR4nsUlemWeuL7bZ0X7PUDZ-mitz3wtYF9OQZsLJYeEXK1lwBfag9WySskegAT-Xu5gA4oWNABQIH8qW2XNkivZsQlE2Hzk5hDxsdf5uKUiJFFAp24padA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇲🇦
عملکرد درخشان اسماعیل سایباری ستاره تیم مراکش و باشگاه بایرن‌مونیخ در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/95765" target="_blank">📅 02:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osj4otaPrtMnDGdRXP9KLYmr7vLUv5UVeSEGJZQSk1FVequMrkm9PMfIigY3SwCyNIXhNvOSDxiDSWGRSV7yhZz7QCFPRPRFWpt9WRJRgjzzqtatvNzAIdSms1CbsP30DAIpiP-brsHKjNn45b8r4xk6TgVlZjr5sH09Y9KLWmhWi_2mvgELEAhAYMnDk8igqwUzHAMkmOM7Jxh6m12NtPS8miMbNCzhLSkU3YttaeYQbnLhkRv7afobjXcnUe8rUxrOcoO3HPF6guk6Hv3aIW357urzvnNMZ8YgDfxraSwGnQqvCh3_d0iUnRsj2vgJUgQL3Q9DBBDQ9k9wjQOazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس تو جام جهانی 2022:
• 4 بازی
• 1 گل
• 2 پاس گل
وینیسیوس تو جام جهانی 2026:
• 3 بازی
• 4 گل
• 1 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/Futball180TV/95764" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/95763" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N3mvHIQaJO1O8kbtrhnKHznSWixS56ZyvV_3LYJBcQV_9j191ah39ZXwfc-voOYgQgKs4WGYt80efX5SyXdG9ylv2ib0gIwnzPD9UpV8KwkeuKG35uqALm3F7CvTqg0Tnp-p2sHcCr-exo9NHcn8JC2dkN1YpQU_ya_-89GfemRMWFdIcrcpPrQLARJZYYXFiLjTFavpTBqOcSGlumi1afS0ciRI6NneZ9u2bph67ng_aGyvWOcwviqcz_K2Wk3-vocktW0cUTJgzE78g6kjSNpP9iSCzFBxD0J5Jp-mJcZv_dFg3c2qKHXqL6bV1mQGe8zyTbHpKt3RoVP98vNV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/Futball180TV/95762" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پایان دو بازی در نیمه اول
🇧🇷
برزیل 2 -
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند 0
🇲🇦
مراکش 2 -
🇭🇹
هائیتی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/95761" target="_blank">📅 02:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95760">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=lFMF_Ybxq9dNsVjzb2cufU42M_sdlHjCYtzRYHXrxRCr_o7s4AKinFx01yHDPCy4zwmGJgo_USgCx9bgVxCv6_Kr1G_OYp_BcAkXIwJe7KTw-WtVceZGlIU7nnNjaRdTTWtIGEV5akN8qcMN5eyaeiTOxqMoTB8bXsfMzwPSlyXVo5ZNOLaBDFvUuQPQ5D3Pq5-Qx_wtV1McxdPmNXnv9NoTkGe_LpfDBok-5IetSs86HJMD9scObl5DIzgWGXj8zu0s0mKrDGGeHnv0i5K8ik7JXFqHSHo9OW3fdlv7Rof6fOWd9a04iopgSZZfZb9GaM0g8EAWqYJ9io1P4ALYsR5FlwNIInyK1etUOUzqIYDs6gz4HS_THPGvqFmoVocr-rCJpcWxIsH5uQ-hG0cVbkrQnmw9QWF3qxn7npMTQe9WNPmNeQNlvhxZwm-AVMgK5e-WVY4-f7wI_ocI15on6EH5OsaEJ5PELnJfUvwAkSYiFTwPhHtU_l5K2QBdrZ0sYgyFYYpCDG2XQ2sKj-E7NSLDhJKYCZDCLTQN88TwNBv3wUGKLlFxu7IgnjLBXX_ZNtr8Yr71K4bMb640BtDUaPDqPo5_W-26TjAp_znfZBo4TRMDvvDJIpEOB2nq7TtO8gJMWq0B6_4bvWMoKDdq-nsXfOP9a-TlNrEN7ZOJz9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=lFMF_Ybxq9dNsVjzb2cufU42M_sdlHjCYtzRYHXrxRCr_o7s4AKinFx01yHDPCy4zwmGJgo_USgCx9bgVxCv6_Kr1G_OYp_BcAkXIwJe7KTw-WtVceZGlIU7nnNjaRdTTWtIGEV5akN8qcMN5eyaeiTOxqMoTB8bXsfMzwPSlyXVo5ZNOLaBDFvUuQPQ5D3Pq5-Qx_wtV1McxdPmNXnv9NoTkGe_LpfDBok-5IetSs86HJMD9scObl5DIzgWGXj8zu0s0mKrDGGeHnv0i5K8ik7JXFqHSHo9OW3fdlv7Rof6fOWd9a04iopgSZZfZb9GaM0g8EAWqYJ9io1P4ALYsR5FlwNIInyK1etUOUzqIYDs6gz4HS_THPGvqFmoVocr-rCJpcWxIsH5uQ-hG0cVbkrQnmw9QWF3qxn7npMTQe9WNPmNeQNlvhxZwm-AVMgK5e-WVY4-f7wI_ocI15on6EH5OsaEJ5PELnJfUvwAkSYiFTwPhHtU_l5K2QBdrZ0sYgyFYYpCDG2XQ2sKj-E7NSLDhJKYCZDCLTQN88TwNBv3wUGKLlFxu7IgnjLBXX_ZNtr8Yr71K4bMb640BtDUaPDqPo5_W-26TjAp_znfZBo4TRMDvvDJIpEOB2nq7TtO8gJMWq0B6_4bvWMoKDdq-nsXfOP9a-TlNrEN7ZOJz9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم برزیل به اسکاتلند توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/95760" target="_blank">📅 02:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95759">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=HNhUxlaDqDK3BGOnXa2rbeSgTaamdKFv1QZ5rOSJEllF7RYqhA-L3tNloQKtk0_BR0cegBHUfOSVYSqW4NtVBpri6UaXm3awzrJxSYhXs2tq2NjCE4kAIrV9mmgedqFfYNAV2huW0jUp6s5w36oyqwxYPrqIzR8sb3NleX0lpOfWxHz8cFGHEkUvZMKIKJdF0tsnx3wip0EA8b6AmirJJHoXdCWlYYD_gbzILRN2zQkihsZe7-MYZa9ToQbMRWkEyWxYjW5LMy5BazScP6pnKAC3W1508mhOFOT11O3tpOObNu7zTaWSvTTDDmvHcZS6fsipPqqIDjBZULltt1MjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=HNhUxlaDqDK3BGOnXa2rbeSgTaamdKFv1QZ5rOSJEllF7RYqhA-L3tNloQKtk0_BR0cegBHUfOSVYSqW4NtVBpri6UaXm3awzrJxSYhXs2tq2NjCE4kAIrV9mmgedqFfYNAV2huW0jUp6s5w36oyqwxYPrqIzR8sb3NleX0lpOfWxHz8cFGHEkUvZMKIKJdF0tsnx3wip0EA8b6AmirJJHoXdCWlYYD_gbzILRN2zQkihsZe7-MYZa9ToQbMRWkEyWxYjW5LMy5BazScP6pnKAC3W1508mhOFOT11O3tpOObNu7zTaWSvTTDDmvHcZS6fsipPqqIDjBZULltt1MjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/95759" target="_blank">📅 02:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95758">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وینیسیوس دبل کرد</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/95758" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برزیل دومی زد</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/95757" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/95756" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f68707a5c2.mp4?token=WGDA10np2-TIa9DiubFPJFb9V8MaDB6xUNLZy6884HZ96n6Zke1xstwfGtwckvf3MAAIDWbtNjIUPBmgP9Kou16gqdVqUF277-bZdCUo83dsKGRZlbaBPNYX9poz99HRfVeeXICxYIYyfbA3kfGu7o5zY1LuKQ546SUm_rfrgIdnst6hM_efGM2j64VRMVPZS2cjcii4rJbNL4JN3fyuUOZCYsAiTIdNVARZXsj3rpYeY-srVpMLXVK8DgLyJA6vb0feRdw1gmw5hvB1q9WbadnYX6gYIeQYwho7GiKFO-k7UpIKtjVY0eazVBcUeP1vR7djbe9PNL7B8jQjuQhbTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f68707a5c2.mp4?token=WGDA10np2-TIa9DiubFPJFb9V8MaDB6xUNLZy6884HZ96n6Zke1xstwfGtwckvf3MAAIDWbtNjIUPBmgP9Kou16gqdVqUF277-bZdCUo83dsKGRZlbaBPNYX9poz99HRfVeeXICxYIYyfbA3kfGu7o5zY1LuKQ546SUm_rfrgIdnst6hM_efGM2j64VRMVPZS2cjcii4rJbNL4JN3fyuUOZCYsAiTIdNVARZXsj3rpYeY-srVpMLXVK8DgLyJA6vb0feRdw1gmw5hvB1q9WbadnYX6gYIeQYwho7GiKFO-k7UpIKtjVY0eazVBcUeP1vR7djbe9PNL7B8jQjuQhbTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل هائیتی به مراکش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/95755" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95750">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مراکش دومی رو زد</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/95750" target="_blank">📅 02:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95749">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/95749" target="_blank">📅 02:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95748">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عجب گلی بود جزو بهترینهای جام‌جهانی تا این لحظه</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/95748" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95747">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هائیتی دومی هم زد</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/95747" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95746">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/95746" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95745">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b2bcd3a28.mp4?token=Vgd_LQ-UL0nf5W6haVkPzLFdjwOJEQqqJDFOxzm8AKEplCwa7yRBXj4jCjTAYnCZJ4FScmN2F9d1mbMglH39wP8vDMg4vPYxSldBwiNhzEvsXOyXXtP52eIUY1vltn7C0dc7BvcP8pJvkHu-u4lb-BDHxBDuzR1NWSGKzjny06fYgLejPUvtBbjuKJ6b3ACUfaJ_moVFCSd_rAIXJz7FRQzPHoIGecknOMk85DMbRJwpM0nTk4xujOpWmoTEo1uPqoLWTT1it4TdIWlEJlPSprj0j9-jbW0Y3Q6z_SQl2WGy-amX98R_0vknby4NWjzu9SqtGv3fUI0YsEXZWmrkIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b2bcd3a28.mp4?token=Vgd_LQ-UL0nf5W6haVkPzLFdjwOJEQqqJDFOxzm8AKEplCwa7yRBXj4jCjTAYnCZJ4FScmN2F9d1mbMglH39wP8vDMg4vPYxSldBwiNhzEvsXOyXXtP52eIUY1vltn7C0dc7BvcP8pJvkHu-u4lb-BDHxBDuzR1NWSGKzjny06fYgLejPUvtBbjuKJ6b3ACUfaJ_moVFCSd_rAIXJz7FRQzPHoIGecknOMk85DMbRJwpM0nTk4xujOpWmoTEo1uPqoLWTT1it4TdIWlEJlPSprj0j9-jbW0Y3Q6z_SQl2WGy-amX98R_0vknby4NWjzu9SqtGv3fUI0YsEXZWmrkIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به هائیتی توسط حکیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/95745" target="_blank">📅 02:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95744">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واقعا من واس همین کصشعرای این خانمه بیدار موندم بازیو ببینم اونم با ترس و اضطراب
😑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/95744" target="_blank">📅 02:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95743">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مراکش گل مساوی رو زد</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/95743" target="_blank">📅 02:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95742">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/95742" target="_blank">📅 02:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95741">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/95741" target="_blank">📅 01:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95740">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وینیسیوس دبل کرد
🔥</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95740" target="_blank">📅 01:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95739">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلللللللل دوم برزیل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95739" target="_blank">📅 01:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95738">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3gcWFvvo_feqlJijiiYaoREdMnqJLn3ceGgNxIUQ3QWcHaszIYm5iU0ODWLsQQxf6-f08qqpL15EnrTlZzxaz9b4MLMZXSoS2a541R6cBknhkuquraQwE3OSv8vYW_HmuVF7f9VucVen6KtbwcS1CdRTRJJJZ2K_oxotyCItlFo50HmN36GgnRVCGEmsebfPVuu8Ifu0zE2FR6szXKjrqC8ruabKaYIW_6YJE0dkIMq6TBr8dm0OccGKVU-e-kMNPrwlaxW4NCq1bjwnFVEPvPpvNX03wiccAsXHUfshvvAnQK8gwMbVFBaqLrGtb2379GgKLNFok4AU7rqg4IpWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع همه خوبا امشب حسابی جمعه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95738" target="_blank">📅 01:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95737">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/836ef29bfd.mp4?token=KvUJNv6BCuq4gOv0b9xkrWg9nmBhIj_e5nV7pNRXn19e_QLPAHCNQnZLgQj4G43xOylISIdvAvyC-GkogUyfPTm2kmrPxXpN8-upekAt6-JXY1fwQZVnyzqFXhsA0kWJb08ntvA16S6pEm3VsGjkm7qS82A3RITcv4dBXeAQrmGtphqlE61cq8QbOD4mq-Y1uuzO8RQz5yDU34N1DSZc50ZunN-2lET26Gb5Zf_FotM-X575nCtYc0c-1Vng0O4RX7QZUGCWICoo2OpuTVxAkKZNB2TpCOFDIcamhYrwKOydlF6ackieAFb4pIPxljnwe1g5W10EfqwcgBuMorNTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/836ef29bfd.mp4?token=KvUJNv6BCuq4gOv0b9xkrWg9nmBhIj_e5nV7pNRXn19e_QLPAHCNQnZLgQj4G43xOylISIdvAvyC-GkogUyfPTm2kmrPxXpN8-upekAt6-JXY1fwQZVnyzqFXhsA0kWJb08ntvA16S6pEm3VsGjkm7qS82A3RITcv4dBXeAQrmGtphqlE61cq8QbOD4mq-Y1uuzO8RQz5yDU34N1DSZc50ZunN-2lET26Gb5Zf_FotM-X575nCtYc0c-1Vng0O4RX7QZUGCWICoo2OpuTVxAkKZNB2TpCOFDIcamhYrwKOydlF6ackieAFb4pIPxljnwe1g5W10EfqwcgBuMorNTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇭🇹
گل‌اول هائیتی به مراکش توسط جوزف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95737" target="_blank">📅 01:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95736">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f3b95bae3.mp4?token=anDdQDgopLL7_EUWeNLLc2dJI8Cx9Ekct3ArIUjyBIHbj1BZDrV11WX_lmGBOvzOz6evGSBspr6IB0bQgE-ncl4FnsoH6U9L9-xISSTpjbKrHymqRkMY4upW93hgP8rraFhQlRTM6InYZInxJLSABG2fbCYGTR2SNnTklA7lCEsu7rfyTb7I-Am2QxAH6cNqX5YBlHLtRxISGLF3dbHfRqO6yeKgE0_JwNRqsAXVdLm85i1wZzzJ84VY4iPsMJq6R4CIs5eQoxzOa3mmcLybdkL6bytH0P1AbS-QUsGOLek-2PhSUGHgOh1bEQr_0Lpd04oMp9DgzV4a9xiRwek6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f3b95bae3.mp4?token=anDdQDgopLL7_EUWeNLLc2dJI8Cx9Ekct3ArIUjyBIHbj1BZDrV11WX_lmGBOvzOz6evGSBspr6IB0bQgE-ncl4FnsoH6U9L9-xISSTpjbKrHymqRkMY4upW93hgP8rraFhQlRTM6InYZInxJLSABG2fbCYGTR2SNnTklA7lCEsu7rfyTb7I-Am2QxAH6cNqX5YBlHLtRxISGLF3dbHfRqO6yeKgE0_JwNRqsAXVdLm85i1wZzzJ84VY4iPsMJq6R4CIs5eQoxzOa3mmcLybdkL6bytH0P1AbS-QUsGOLek-2PhSUGHgOh1bEQr_0Lpd04oMp9DgzV4a9xiRwek6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇧🇷
گل‌اول برزیل توسط وینیسیوس جونیور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95736" target="_blank">📅 01:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95735">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مراکش خوررررررددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95735" target="_blank">📅 01:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95734">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">همه از هالند و امباپه و مسی میگن ولی ترمز وینی پاره شده قراره بگااااااددددددد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/95734" target="_blank">📅 01:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95733">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وینیسیووووووووس
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95733" target="_blank">📅 01:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95732">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برزیلللللل زددددددد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/95732" target="_blank">📅 01:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95731">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95731" target="_blank">📅 01:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95730">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbzk3l65dVoQTufp_weSnxdRm7jOpX0lT0OsCS7PPHQUw5FNZxL0HqLwDwFiUAwbOSl6fHfH5w5P8mXLIDMY2UAQdQKZTUqos61HvNbo2Be-7qFM8-lyjYH1kZC6dYnIIfuhjaI47XQxAs0gwbq7jVdwVxyXaorpRW0jJazVTqUbk2nXKgMbkR_APqVD6ZLWo7nbvza5kCMo_UKLuWukieXOU36MyLaaBjVbLhEuUeGuQ6Rt5C1_o1ft6VrmcCX2Z_LomTYuR2vUPb_EuTq6dEVbI1y9I0MNfjTeIvOuwRo8Nh8HFLktYqg0mCk6tJysLIhCIFR_ucGlaw94oui1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95730" target="_blank">📅 01:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95729">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMeuISd2mohHWA1GEZv7wzZJKjK1rdz3qoLDmSKM3QhyAzxaLaWp4ojePapZhpIahdIHzLdLrZ_K3HwjDdpowMJv-guZcNc9p6YuSY3oewH7ouk1rEVbvFVbfwuMiQNd8HpHF_EiGPmwRISp3G1_wCIK_otNdClRIdVo_eCnpVfm1xX9fnmth4xNpSHMrBY9CRvC5RgbafxFDE-3McQL5NXRh4Nj-0xsqfXEvGSHhZ_hD20HH1A9GA8QTdZihFXzCiIZoLP_KpfYD-HGrLfD8J0Z4Wkdp1Ft-B9YUYe-vpzlrSURSX7eDIjziYdW0qNf7tp20SY1c0udb0btYb5XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
👀
🇦🇷
برای تولد مسی هرکدوم از بازیکنای آرژانتین رفتن یه عکس از خودشون و مسی روی تیشرتشون چاپ کردن و اومدن با مسی عکس یادگاری گرفتن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95729" target="_blank">📅 01:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95727">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شروع بازی
هائیتی - مراکش
برزیل - اسکاتلند</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/95727" target="_blank">📅 01:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95726">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcqvriQ-Q1uSiBqN49pORvrzgql9opOSgOgq_bclG-_3KZJ6314ROFhZHpZXMhr0tROJL7SZfYpWLl2kGyZ7Clasv7HWsC2myVflVUEMpkTMCBY8lU7rjKTYZ8DzS67JsG0Ysu1tcBtzKCnnEk3ZB6wnaDhlmuwCCII2haZ016HOWxgQvCLxhBM3X9HFKBm3nGEKvnS_PbKsjOZ-FvDUpTP9KL5aR1Tw_QRmUSyLMaVY5GvCAD5mVOTZ7VYkm0vYjaoJgiSzRv7P9UDZnUIPdmizxN664FqgqTrOGqfpTr1H4Wu10solyOG-yVuwaeMTCt3Cl39QM7M9F3Q2mUfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
اینترمیلان آماده انجام هر کاری برای جذب نیکو پاز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/95726" target="_blank">📅 01:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95725">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fe1759a1.mp4?token=UX_CMHLIDSNoLKCEN2971wytsATW8iRQ4ZhXZRMutrSKrm3R8YhoPTlok8HfUysm0xYrhP6pGh7Rdtj3YoWxtHnfF6jBFNM90tlF9dVnoN0uXyOlH8-JHqB9noSvjjaFy1Y9DyV3D6tEOQ0LIyzvon6TPhdXCiEWKYslkrkApF-77e0Vn05lqQo0krS7HgbgF_l0mcDG2L2eDi8c93fOc6yMBRaI7FC1xo8DeAHxSx34UUS7bQHHtyxbVSh0ULRVtPF6eHypM9VNto_XzJ90NoZHPqgRuUGAkC0gF1YS8zfC7OBbSLdCTH_lEVu9Q76mebFBGr3fHybg2QCMEaycbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fe1759a1.mp4?token=UX_CMHLIDSNoLKCEN2971wytsATW8iRQ4ZhXZRMutrSKrm3R8YhoPTlok8HfUysm0xYrhP6pGh7Rdtj3YoWxtHnfF6jBFNM90tlF9dVnoN0uXyOlH8-JHqB9noSvjjaFy1Y9DyV3D6tEOQ0LIyzvon6TPhdXCiEWKYslkrkApF-77e0Vn05lqQo0krS7HgbgF_l0mcDG2L2eDi8c93fOc6yMBRaI7FC1xo8DeAHxSx34UUS7bQHHtyxbVSh0ULRVtPF6eHypM9VNto_XzJ90NoZHPqgRuUGAkC0gF1YS8zfC7OBbSLdCTH_lEVu9Q76mebFBGr3fHybg2QCMEaycbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آب درنگ، جایگزین فارسی کلمه hydration break:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95725" target="_blank">📅 01:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95724">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC4drjv8cFKjlhpiUDjUmoDCuPB_qXiqaBiDn1L2g4bWhXsspe14wavoGU16GeaZXHZ3jkfbRQ9AIy_H5YM73wYa5IxBtV9v6mUiUYTnTPUcD9L2_lvIukUY3NabB15IkGkFLgwO12Z9INWfeDg3I5RnTARFcA807haJQKgUjtGEM287WG0zI3WmClPO_Ap_ueFRpIoWMxotWLip-3yyctxjkzmyItmlrsehcKvILcn5Yi5k7XJnQrmUrxTpX35dARxl8J7CYRKmw9J8CnNPa8ZkaMFRjqqDpwKZfgvcOXkQltgL1px8lJQfOW0vhhBiJEMbO_Wb0rVatCxEoJ1oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تیمای عربی تو این جام جهانی
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95724" target="_blank">📅 01:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95722">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پایان ست چهارم  فرانسه 2
➖
2 ایران
🇫🇷
25|23|25|24
🇮🇷
21|25|21|26
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95722" target="_blank">📅 00:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95721">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS7eyR-5hhBtt4utsxmE3Jmg7fNGf98_gclQ37Xz1fYhINw9NfzoO7HYi4avrmh-5Zgh9z7sU08DKL3hpGml8DICKnuX7LFeTFsKHUeNR2UPaRbBJ56dw6AZwkJNkvCLBBeorD1x0JJ2tyTh_LCgRZ6PSoHunvUZkfJTVd-wib-Q6M_z4vzwJJayPV_nfveXxmdwm__gNfOaPg1F0MOz5Z3eC780_UIF0E_cczstigpd_UccWACCZGpOCfVdL8Vq5rwyCAaoprLBpFfjoTubJwTmiACzupRSxPKU1wiKAOLnSZZMukkNN-XNj93ZrhwaS3CnWr4mSit1ErTBD4sUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بیشترین تعداد گل خورده در جام جهانی ۲۰۲۶:
۱۰ گل -
🇶🇦
قطر
۹ گل -
🇹🇳
تونس
۸ گل -
🇺🇿
ازبکستان
۷ گل -
🇨🇼
کوراسائو
۷ گل -
🇮🇶
عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95721" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95720">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF38v919t_e2_sBnv8M1lliLE6D-QH7TNr5bjmm-BvB5GFU5A3UHKDVXvIx-RBM2Bt4lORzOXj2SOK5FrtD9HV96MoXYvrFnA8O3GR1M8ixP2sRYQME9flDkwpEpKY03SQHnMqLkc2wAyHEArRcaSX_TtohJGFpSOEQa9QBDIvjEWTSk05Ne6SCptPYyQMUDUy4tPSWlofauBaMqWFRF5yfSHTTzbhH9D8mw9zWZw2NZxn0zzZ_R-OUefBg-IOiOzBebWsjhrW59lstvBkvPIvUrPetdUsfV4KkJzihZQUd1y2oYGKGYR_rI76mU4psGFsy5u6Fo-X_b26vzt7fBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
❌
قطر قهرمان آسیا رسما از جام جهانی حذف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/95720" target="_blank">📅 00:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95719">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95719" target="_blank">📅 00:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95718">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9jqWNOXaD-T5IbltgO8X-bRRvXLIuUk5AKlun3v06MduLH1VRN-33nTdqDxRu_iiopbuAfd8XOJdp7q8-7kx8OWlwg1dNefY9PEM6rjtEnNHhSPsnuHxfUfL054eurMicGpp4k2H0FKoJA6m48U-viIwoG6uvIKy4xJgY_0rv6Lg0mcXMNxTzsLguCy1dAB9M4vbQYfpdSYNlazxS_SbYuKKA60VwKZcQiSX09WXTsTJqgnXLRH0GCfM-81FRem5Poc6MXOjynQpiG1BKvi0ix1fa1KJnQWyIpktDDHv8LeGWc_zqe5Jb7nsNOSp2_zW1sy49xBIjPo1e8vlN-Qwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
❌
قطر قهرمان آسیا رسما از جام جهانی حذف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95718" target="_blank">📅 00:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95717">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkD6tMTYA4b_FIJ1VeGtvORgBknkIQeyqawCr-Ny0SdA9Z2ngiEeKr3QmDcD8k-mJLf_OWn-DZ9lJ3Ta5jA5xykD09HMNkkqY1z9dpZmDn_KfCGT-nbakzoejEJOzTm708x4IbfdzLB7xXVCsceMYKAIxg6G-eTYfffp15ReLH7gwiF0TNe8yQKjY5XKshB0lJBBubMpA-MS5pI5AfcVmavVevcDlSHmGfFG-keS80SliDlg2LNjGGM_5875YOij6pVksO8STKWnBE4F_cw8tWomXF1yPzNPIgCCiyWrAxUZk4qBCtIUWFsbxVcmsGiV_Vh51d0jkoPyy1hiqHWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم هایی که تا الان صعودشون قطعی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95717" target="_blank">📅 00:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95716">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پایان بازی
|
🇧🇦
بوسنی
😆
-
😃
قطر
🇶🇦
؛
پایان کار قطر با شکست مقابل بوسنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95716" target="_blank">📅 00:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95715">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پایان بازی
|
🇨🇭
سوئیس
😀
-
😃
کانادا
🇨🇦
؛
سه امتیاز و صعود قطعی سوئیسی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95715" target="_blank">📅 00:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پایان ست سوم  فرانسه 2
➖
1 ایران
🇫🇷
25|23|25
🇮🇷
21|25|21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95714" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ceb81d53.mp4?token=EWfEU2AeUk_si2cvlutyj8xVy9p4PIa4GQheQbzZo8cdD_bv2RFIdS1FOev6otQEBDy5mKGECF99E19yiKxZrNkT5DIFG2AAPq-9tSiHbE_jLgWnuubnAEYBKkKF2vpxAkUZ_9jKsaYZ_IDMfMqnstngCpQ2sGtkM6aUsIgNy-efILTVfwtJSngqG4gwHeT_dLtZTJ9YTznhjEjwNCUB_3G63hKyVSySjptfT73oGb6D1BdEAC2JRWmd01ZuIKaxSy2e2UTyuvtDRoUreRNRAyNGBjYnwt_gOuprewGVn8smYw_rjJkzGpsz220hRpMcowATkOir9TM9Ei3BMgU7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ceb81d53.mp4?token=EWfEU2AeUk_si2cvlutyj8xVy9p4PIa4GQheQbzZo8cdD_bv2RFIdS1FOev6otQEBDy5mKGECF99E19yiKxZrNkT5DIFG2AAPq-9tSiHbE_jLgWnuubnAEYBKkKF2vpxAkUZ_9jKsaYZ_IDMfMqnstngCpQ2sGtkM6aUsIgNy-efILTVfwtJSngqG4gwHeT_dLtZTJ9YTznhjEjwNCUB_3G63hKyVSySjptfT73oGb6D1BdEAC2JRWmd01ZuIKaxSy2e2UTyuvtDRoUreRNRAyNGBjYnwt_gOuprewGVn8smYw_rjJkzGpsz220hRpMcowATkOir9TM9Ei3BMgU7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
گل سوم بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95713" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95711">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YC4CNtfe9w8dzX7DgeV8ARj85BsSgxaxaGHD9nsG1xLdAwxrq-m9tiPGg5InRUjXxv6OrfoHo2IX-H2jAzFOzLSDxL0SoMaM1XptOggTEeXUM6XlTsIw012yVcKOBmx1SSP1V3LMUJQLlQk4XuGS6RqOd7Q14Du3yuFnrSYyKhNNCfr5OQA9pUlE3VUoxs1TczB-x2VW-H9HuGjq-WdohDLBJGSSE_tuV4oAKX9GyjY_EdvEllIpTfg6_QVAKFPEd2lcdEoGm729ItpgKIi6OP3XlgTkyhuL0wWBq9YXWSashpyb8rWGZ57lhOmVemnftN3Zkv_oReos82C8EbXOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fS_jnkbRgsT6cGstvtpMFuCZQFrYJ8w0e2A_HbiboOHvw9BaAzXtNvtGU2bNcCd4EJDCcAn-zG0Q8UmMGIP3t3uDXOWgbC5KaWV4dberTJ0m-RzaJ97k6iNKahGGSCiifWBq_G7emmlZxlMnuHUafF9-p1yvdQnV776lUf2vL2FsIjHA8zKWt5_0-xQMycgpP2xyXGnawbZbh0PJgd2D-SrFazB_hxsyLX4hDVOSVPdmO8aXuoBR0a8el-8OFbPDrD-bc2TQm35bRdLxPNvRN_ynxakWD75tjzJdEgFyAQXIrA7uiBgBxDpsD3LNLplf41Xf3jLRe7GmQLsqIkfmQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
🇭🇹
ترکیب رسمی مراکش و هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/95711" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95709">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بوسنی گل سوم رو زد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95709" target="_blank">📅 00:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95708">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d46d4a5b.mp4?token=hhsvZnT96Y5LboZuBhHOLMpnw6ABCByBNo2Fp9AS9SbmZGdGxdYV_TRQZmO8MkMDaK0XkUAUZG_BM8_vudgaNNJD5R_7vQilxn_P_UH3WW-uztDlmVdefrqctsIC_ABOw5jGE7y0K1flx9SXbZv4qfqHx6S5gd5Mhrn6r35pJyGiYUCjfaUd3gxRyvkGkoWdg35ueIUidKhZF2p4sFQIJBisopqPNTfHM0z_Hex103tbCgU70JhQnRUI08yXoPsdAa254qkA4-zEqWOyUGX3hyH3j8ik4Gv4V_S7YM5mi34m1wYqW6gQgMr4mdV3Bn03WrQfEgx6OPKxZ98DMsLQqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d46d4a5b.mp4?token=hhsvZnT96Y5LboZuBhHOLMpnw6ABCByBNo2Fp9AS9SbmZGdGxdYV_TRQZmO8MkMDaK0XkUAUZG_BM8_vudgaNNJD5R_7vQilxn_P_UH3WW-uztDlmVdefrqctsIC_ABOw5jGE7y0K1flx9SXbZv4qfqHx6S5gd5Mhrn6r35pJyGiYUCjfaUd3gxRyvkGkoWdg35ueIUidKhZF2p4sFQIJBisopqPNTfHM0z_Hex103tbCgU70JhQnRUI08yXoPsdAa254qkA4-zEqWOyUGX3hyH3j8ik4Gv4V_S7YM5mi34m1wYqW6gQgMr4mdV3Bn03WrQfEgx6OPKxZ98DMsLQqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل اول کانادا به سوئیس توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95708" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95707">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلللللللللللل کانادااااا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95707" target="_blank">📅 00:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95706">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdd2JZ_dXzcAYjl62HmZKTEGkQUy_BWPt6HSfSeCrqqSQ511hWTQNPHLFayi09B4Xt7dVuHPqKSGRfTYDgoNVq6FNk9zb0PlOmzKPjJ06C__LWeLk5IBBiuDluFjV0DF5STqlqQXh-fXE1sw0SVLTZETjyvpIiVUy9BLHIsuCLf2SZhxV0B3Rrg1fy64bBaVlWM4xcLwujHT9IMcIg4tE0xoD2YcQ0T7AUrRq0xFFVL-IsB35AYQMIeP-goHOd9fheQY-T9FDxoUG9WT5_jwNnsHL0iAom9BPA0dmcwWBPwvZu1PNkMDz3AGKsw0jShyiBDXsV879HcD5TXfhW1DIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
حضور نیمار در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95706" target="_blank">📅 00:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95705">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇧🇷
ترکیب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95705" target="_blank">📅 00:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02624180b0.mp4?token=akZaJd-PIqSJjJ8io6R2rWTBSHZDwpp728eotc1fy7N9Rp3oFiqoz3szLHrtQCWHay2QtM0vPdPSaru6YJ76yLhPkZXPqhcanEK7Ze18yCznO_K9pUPzQNYeRa8NNdHVhQAxSjK10S9aXVRQdaRlL1e8iR9oLcjCjUyEcY14TUsMZUkjiDZzj8PMP3CKsP0OxINL4FcAS_-zPPWAdNaklG7gRgQrkPaA3is3lgvjW9nMTpav64JK8V_fbX0ojnzSA17SWOViEc4Ln5PaOf4krc0ZRV8pWzfI0z_YPNOkl3XuxwtI6OhWFea_FrbV5P50KvOZLRA0w8IJbIG13mtQLlaycBXi7-XMm6qmCSaOjXYF4kZOLtFz-1XxNl51ouPCN0aBV-bPsUCOERPSKcH2oz3ze6jT7oxktsHNIjtoC49jnCoxv9qVQT1lVVztEqawJ_rlhfbiJet9P1G0eToPLF-q-aGy8bt4OZt-QYru-XI0hBqU8hMJ1Q3nmCL6L8AhgstUQIS7jGQwU-WcAGY9R0FskHzB7Cx1DsPU0_wCXOVbMe1h26jhKU_bqL--nAYLgi7yzK0aGbvBloIjexzkVGi0QrCqsAhDfKiaPok8CBGYDxPMx7uoam4hvVeQ0A__V_ifBiD_T9EYLInujKGzS3WHt7VzRwk0nvhT849cGvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02624180b0.mp4?token=akZaJd-PIqSJjJ8io6R2rWTBSHZDwpp728eotc1fy7N9Rp3oFiqoz3szLHrtQCWHay2QtM0vPdPSaru6YJ76yLhPkZXPqhcanEK7Ze18yCznO_K9pUPzQNYeRa8NNdHVhQAxSjK10S9aXVRQdaRlL1e8iR9oLcjCjUyEcY14TUsMZUkjiDZzj8PMP3CKsP0OxINL4FcAS_-zPPWAdNaklG7gRgQrkPaA3is3lgvjW9nMTpav64JK8V_fbX0ojnzSA17SWOViEc4Ln5PaOf4krc0ZRV8pWzfI0z_YPNOkl3XuxwtI6OhWFea_FrbV5P50KvOZLRA0w8IJbIG13mtQLlaycBXi7-XMm6qmCSaOjXYF4kZOLtFz-1XxNl51ouPCN0aBV-bPsUCOERPSKcH2oz3ze6jT7oxktsHNIjtoC49jnCoxv9qVQT1lVVztEqawJ_rlhfbiJet9P1G0eToPLF-q-aGy8bt4OZt-QYru-XI0hBqU8hMJ1Q3nmCL6L8AhgstUQIS7jGQwU-WcAGY9R0FskHzB7Cx1DsPU0_wCXOVbMe1h26jhKU_bqL--nAYLgi7yzK0aGbvBloIjexzkVGi0QrCqsAhDfKiaPok8CBGYDxPMx7uoam4hvVeQ0A__V_ifBiD_T9EYLInujKGzS3WHt7VzRwk0nvhT849cGvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95702" target="_blank">📅 23:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مانزامبی واسه سوئیس گل زد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95701" target="_blank">📅 23:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پایان ست دوم  فرانسه 1
➖
1 ایران
🇫🇷
25|23
🇮🇷
21|25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/95700" target="_blank">📅 23:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f2acf61e0.mp4?token=t0YDY_uPO-N9lhEhWq4UdNQozCDEW0QDVEWeFQqeVgsd-n_L1OYji7a0OLISjLzc353Df0kFoq7PIfK5hesX0WfH8XBp-MpqveSgjWNbo_zhyF8OvtyZa-jvwg9ggZo0811Qyq0BTLiqXX6xZkbMtr9JwyNaDjPCsXqNMfrvOnKY4AcHoygu1KYdQd3ubBAiQRxDWwsAih-7sB-0w3-gpzbBrtlxlLu0d19pnb4b6NmeJeRY1PVDfx8HtJBnU4nq55j3IecfINh0cJDbe8z5eL6E-G3NireAYehItGEwNquARwfEJU9Z72ko39yTv00mskSHdJeCGhxJncjELCFe9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f2acf61e0.mp4?token=t0YDY_uPO-N9lhEhWq4UdNQozCDEW0QDVEWeFQqeVgsd-n_L1OYji7a0OLISjLzc353Df0kFoq7PIfK5hesX0WfH8XBp-MpqveSgjWNbo_zhyF8OvtyZa-jvwg9ggZo0811Qyq0BTLiqXX6xZkbMtr9JwyNaDjPCsXqNMfrvOnKY4AcHoygu1KYdQd3ubBAiQRxDWwsAih-7sB-0w3-gpzbBrtlxlLu0d19pnb4b6NmeJeRY1PVDfx8HtJBnU4nq55j3IecfINh0cJDbe8z5eL6E-G3NireAYehItGEwNquARwfEJU9Z72ko39yTv00mskSHdJeCGhxJncjELCFe9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل اول سوئیس به کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95699" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سوئیس زد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95698" target="_blank">📅 23:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95697" target="_blank">📅 23:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیمه دوم بازیها شروع شد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95696" target="_blank">📅 23:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95695">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdwKX3Met9VxBUfGBR2evkiXgYZN0XeWO-UiA3108ummnITwN12yZ-maidyYU5RlmTA03Pv6nPTS_3re6Ap4bJVXn6Ci63ly1oQFdPkY86cVrutS35qtZZNnaxCClUECNpjqKWmH1jSQlHAK2RrM6uZ-wES5x4bOXk6KuxG74XpNpIsQqxLLwKQtp9YbU5DwP3mynnaaZF64mTpkWK0EzVwYLQELRGxlxn8wXxWP-qiWfgTzAEl3CL7HiUeoTptuqvl5C_twzACWeuXsHawOXlxMQpx78wa-ehMhn7Q3x0nwFAuIdrIq6vEwJ5blenSKyVD6I2hGOOYj09kaOUu97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قطر پس از بلغارستان (دو گل در سال 1966) و روسیه (2 گل در سال 2018) به سومین تیم تاریخ جام جهانی تبدیل شد که در یک دوره از این مسابقات دو گل به خودی دریافت میکند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95695" target="_blank">📅 23:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvrUABZZYRSssHON5NfWxNxOeYl8v4qaSo7zSJlE0TGIijn3Qd5tzTcKeh9UYvhHgQ8ozVg_nxUQyHYQmbhDBRWfgwR8p4xYroZtPAJ-sjDZhDJOXfg8y7xayawVqGmXSB_BXL2SrJ5NBdXawetvsXNwc7y3WqWjw0IBr-urMND6HJaeNYovyoFSusckUcFsgotRgLuHE2dHRrR1iMSzg9N86nLvhdGbJSFyiXEiRxspX6rG4SM-NNYROa4ZnMV4Uvs5zo-p3gkQR3BvP6EgbcU3Tv0zMn_gsTpUvKoyNJ0LmU00zJysgFkUp3_QfOHHe0s-UY9FohiC0taZBLw_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل اول بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95694" target="_blank">📅 23:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان نیمه اول
🇧🇦
بوسنی 2 -
🇶🇦
قطر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95693" target="_blank">📅 23:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پایان نیمه اول
🇨🇦
کانادا 0 -
🇨🇭
سوئیس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95692" target="_blank">📅 23:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd323002a.mp4?token=Uc9htXNa6IyPBINv-TJ0ZebilZf82vkDPrdFew9nrTtAjbU1fIVaJpJ07nchFo1IkpbGZlozz1zZeLIiphgyWWGk5WJpCgdXmjg-ICa3X_XVjCHEqAszdFU6Xw74ajUMP2oufkmMem_f5qpUhaAJpJhpPfyNusz04ZgIhgN3MGY_8QI7MZC4YUa5nTqhxYLgM8yHEA4b_jguBCK6cTE6IOZvJMW4ZaOjsi7sKnXmcLoX1z6YPO1yZKvSlEfBRTzMyfLq0duHDtbfERYicL9C1X1h2XCBn-rQSxYj-D814sVprNcWu75ypQkeI6ZD8fuD3u6S-E-AX0QFUCWXY559rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd323002a.mp4?token=Uc9htXNa6IyPBINv-TJ0ZebilZf82vkDPrdFew9nrTtAjbU1fIVaJpJ07nchFo1IkpbGZlozz1zZeLIiphgyWWGk5WJpCgdXmjg-ICa3X_XVjCHEqAszdFU6Xw74ajUMP2oufkmMem_f5qpUhaAJpJhpPfyNusz04ZgIhgN3MGY_8QI7MZC4YUa5nTqhxYLgM8yHEA4b_jguBCK6cTE6IOZvJMW4ZaOjsi7sKnXmcLoX1z6YPO1yZKvSlEfBRTzMyfLq0duHDtbfERYicL9C1X1h2XCBn-rQSxYj-D814sVprNcWu75ypQkeI6ZD8fuD3u6S-E-AX0QFUCWXY559rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول قطر به بوسنی توسط الهیدوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95691" target="_blank">📅 23:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قطر اولی رو زدد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95690" target="_blank">📅 23:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c442b447e2.mp4?token=sloo2ok2TjHLT8C8JWDsY07EB_tX12R9_IQ_pbeyyq0cbL6F98HiF0sK7sHyxozxztw-niARiL8uhv3bEzBBTPvVW3dw0z2vCBF6OwAWT1K_vkvBo2x0puUGqIMYcs2_zY83QnEvCUeIjYN84pMgYIF_VOkv853AmcTnZh_NrtYWlkirCl_fIgWQlrYlbJMGVwrhAF7X-QVweM7RcY6mfj0D6dGiP_MEpdaL3dBd0MyFlUVIKMuR3WbbwZK7sp-SEo8NhUj59SoJ1lKWbicxZbW6Nu81QAqe__ZbypARG-RGQKxZu5dlGtcDqpt8vXUiclzmL7MW7XSXsqdvneOuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c442b447e2.mp4?token=sloo2ok2TjHLT8C8JWDsY07EB_tX12R9_IQ_pbeyyq0cbL6F98HiF0sK7sHyxozxztw-niARiL8uhv3bEzBBTPvVW3dw0z2vCBF6OwAWT1K_vkvBo2x0puUGqIMYcs2_zY83QnEvCUeIjYN84pMgYIF_VOkv853AmcTnZh_NrtYWlkirCl_fIgWQlrYlbJMGVwrhAF7X-QVweM7RcY6mfj0D6dGiP_MEpdaL3dBd0MyFlUVIKMuR3WbbwZK7sp-SEo8NhUj59SoJ1lKWbicxZbW6Nu81QAqe__ZbypARG-RGQKxZu5dlGtcDqpt8vXUiclzmL7MW7XSXsqdvneOuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/95689" target="_blank">📅 23:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8b44c8d2.mp4?token=drxtdSux1sHGvQ5m7mHARvL05wvZtGzeALF_Hzd3PHs1Q9fu9jTOjBbU-v1Lnnlu-aTIj7GtM3ftfZ4qTxnMOLrY2mk-9R8d2MM22iQ4e18Hqtv4UnyR_XT_JeX0Zp50a682-XmYoVOxxHfbG3jNV2GlZhRj0UfbWGGKEuoNG8Hu5DxgzpFJoniDtd1TQOCTrXxj4Ozq9eBX6L9IQMB8fLzcEfcDglBDZHVoyYlhqnyijE9ubLHToBT8farE2B2pQEUcI8i7F2xYojs6lTB7qOf7I_GNhaes83kaZYjHorAuSXLiM80WbSq73q68LmBNjenGOlzMpsQVJKldjMR1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8b44c8d2.mp4?token=drxtdSux1sHGvQ5m7mHARvL05wvZtGzeALF_Hzd3PHs1Q9fu9jTOjBbU-v1Lnnlu-aTIj7GtM3ftfZ4qTxnMOLrY2mk-9R8d2MM22iQ4e18Hqtv4UnyR_XT_JeX0Zp50a682-XmYoVOxxHfbG3jNV2GlZhRj0UfbWGGKEuoNG8Hu5DxgzpFJoniDtd1TQOCTrXxj4Ozq9eBX6L9IQMB8fLzcEfcDglBDZHVoyYlhqnyijE9ubLHToBT8farE2B2pQEUcI8i7F2xYojs6lTB7qOf7I_GNhaes83kaZYjHorAuSXLiM80WbSq73q68LmBNjenGOlzMpsQVJKldjMR1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95688" target="_blank">📅 23:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لیگ ملت‌های والیبال / پایان ست اول  فرانسه 1
➖
0 ایران
🇫🇷
25
🇮🇷
21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95687" target="_blank">📅 23:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95686">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللل بوسنی دومی هم زدد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95686" target="_blank">📅 23:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بوسنی اولی رو زد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95685" target="_blank">📅 22:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95684" target="_blank">📅 22:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4b0b9366.mp4?token=bnoxWS-eBeW0Io3Sb8bZdrQywnFi5ip63hbwSWR7C3hJBsXR_iJHV4fpEzjI1EXz9_iQ5_PjL3o_4lJb4Cy0U5KnUXYQb-cjhlvfztFwFAcPeCfxlaauGFTwxvZa7juirfSkn0cQaTT_ybxfCtQT1D42ggUsTkvKEIos9Lf1h1QTrqOH3Zt2ppVvoPNBV384qACY8QCAOyyqG462vuNMY-lnRT3hd1RMH7J-zjAJ8L3_5vBbRKkP_-EbT6IXZ3vwpgjVTK4Lm9easXoPpPHUG8ZS19xw_z_CgDe-08KBMJj8J68njKzFtsQNQDp7BmIJUnHvDbmomYZRRiQ_ynVNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4b0b9366.mp4?token=bnoxWS-eBeW0Io3Sb8bZdrQywnFi5ip63hbwSWR7C3hJBsXR_iJHV4fpEzjI1EXz9_iQ5_PjL3o_4lJb4Cy0U5KnUXYQb-cjhlvfztFwFAcPeCfxlaauGFTwxvZa7juirfSkn0cQaTT_ybxfCtQT1D42ggUsTkvKEIos9Lf1h1QTrqOH3Zt2ppVvoPNBV384qACY8QCAOyyqG462vuNMY-lnRT3hd1RMH7J-zjAJ8L3_5vBbRKkP_-EbT6IXZ3vwpgjVTK4Lm9easXoPpPHUG8ZS19xw_z_CgDe-08KBMJj8J68njKzFtsQNQDp7BmIJUnHvDbmomYZRRiQ_ynVNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکسل بابا امشب عربستان فنه
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95683" target="_blank">📅 22:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH0vdUiTYSYQJ_RoCwM0deH7fxxBSwOonaTxCRWNuXJe0oyjwJYeuRp7gzIxHrxZURYQ0LA-GKhAsfz97NUiDFpJZ6WQf6vq_CoUeQ-1zJwQpGF5M6VIcjXSmi3GX4TAYr50oulsl-d_kdswLC9Vgze_jBhVuCaekoM47uRHXixPBLPV1vQOQRTbrqnCcrifz0zYsuGQUG7Eb3Y_tAw7Obfa_YB78y4nmRdj8FAA_I3ULIRtfyRNUYGpPUE9Rtb2Vc9_3y7afcc8H1EPmlSjl2P6YxTfw1rYT1LOHbl6JQ8Xl_SebqN4Tjd5FQezBzI8-o0ZwSPsdkiYbSRszjnkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان تری و هوادار غنا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95682" target="_blank">📅 22:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeospXER6x3s4GGAxAYD2BR4PaK5a7UZoBb4EnyterMDhoZj8cMWTBbyHsFUg9uo7e0vsnReTEJOZ_m_n5xX5-0bNZJCpEWGM8h9c48mTrGbzPyds6qUrXITpcXMIR0J4AE8xukvQ9HECDBpHZvlKnmve3IfvZDT78fNMzRaGJXocCMqkNXhBMvxqRYhsjhCMOO7PCMeUiaAu4kJI1BcTzYs10ba_pDXmgGFE-ZUuF0Tpap9dPqoRMZEPSR7zjUwPVnwBwSQ4EU8AbnJZRTz1jqPV6ZlKTow7b4BPrc8lsBAgPa6WtykjuYBACM9wSLKUogHLqWb10smsL0R990lHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست رونالدو تو 24 ساعت 25 میلیون لایک گرفت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/95681" target="_blank">📅 22:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95680" target="_blank">📅 22:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1I0FopIAcubPscUHwXBZmK9MdFxfkaR2BWui0RqlV-i-FXG7FNXM-SPK5FGc5WlcA5DF4gcM0nTmM7YyTf9KOYWdPhpaRLBIifiGMe-XjaZB74CO-6My8Ugdya_mwV_5xhgQ7DcjrmqzolfmcaHurBHZR_2vMvgPbvAvk3mJ8yZnBVoyetz1GDNrPhkGTELoBUPBju_J7JhEAAPz3ZKW5PlEhcAWX4qhcU97FvjFTvLqb8LVouvWMSMt-Y6PVPIkyerrQnaidrBglnk5pVZRwoRimzg27Xyk10qjnd9i40jz8Zry4nFl7SZmd4p5lsFl4213vRS6-joMHLRSLlHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95679" target="_blank">📅 22:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازی کانادا - سوئیس و بوسنی- قطر شروع شد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95678" target="_blank">📅 22:31 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
