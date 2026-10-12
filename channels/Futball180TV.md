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
<img src="https://cdn5.telesco.pe/file/QIVchQAkDXl3F0gYn7lZkrjOFCrVseHt-VyFf7_40mzy3nzceP7-mitfJU_sUpxaf1GVTmsv4XStI5rYKrmqW4PRoXBMaHmqy8RrNPFFJg1zzIkrEFxJT7craE0EwhAYiNLZMGadGDllEuwaJ92aYWmJzCU93b0oxRfRP4NYWBfNtz3fzObtlzWQ8rrU9wgajcrRHpudbh50qVF24fvstt6ZWf6MOO6XXDaTIg7XJ61Jva9cRpAuK-YCj7T100qona4vi4fhEN3eht5ilFYmhVorXV0jtfPNFk_PoURYTNMi8dY7971TxkS_Na2ggkunipr95aNbMJcolNOhTMi6Mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 384K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-108424">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/Futball180TV/108424" target="_blank">📅 20:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108423">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUAoBnTVVfzZL5C3HQAOm4lk1azxyjcoxUZaucRVrYgttObZkpOHnf4abWVGawLGOHaz56xC9Gw-UEl1jTGlgCZi5kEqIMeNfHx3O8ApGmmChzg359hLofG9avowR03feFztFSywprg5Wy9-6RnciHmcbKZ2PG6zn0-Ccy0xrmBEMNCEb3rJpGLEaTDsrQAv-ib7-OevpnuPmzh9WKH5Ijz6Lasvvm2MRZJrPsBCzvhgugJSbPpURn7vVTL4gwFuYQ8TWU0OsV3jT8sFDwrEL10gL-dP2Zd7rNxbBbEztB1yspoXutzV2cJtnVpl2X8pScEkZWeY9CbXLvBeSDUJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/108423" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108422">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6QkXfVAdoInOeQOfqxPoGy56EbLYJLTXgfmlML32se2cLXUvZ8kW0wLPuvi72iPzxvLGP621Fh4HYctpv_hsTAWDTQG7Q-I0euEz7MdvNo79Ei8Q4pCEIB9LGsf1F_vmWWujk4G4IDB7lZ8NYd-UNKjhlKLW-qbbKDkiM_GSUjL9RLU_ERmR1VTGSU1tQz3ATQd5ZjNoM5xEPQmdwNIQh4ixzeVvA9v0EHsXw_eL627TAfzkW075fJ3TdGHrDax6ri4VmRG4X5MHtiRVGfvg9JIaazU3tWjDA3toJB4OuQm5ho78Bc7OoAMz8ywwtb-gzOSBiviUkFpbDdlUahPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو در ترکیب فیکس النصر مقابل نسف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/108422" target="_blank">📅 20:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108421">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8U0h43wuO3NeeNrOHSI9vv1EEucIJL1naiIQqc530cMReI7p9qGRm493i9gSSH7tm-KXNg6xeJNHwQ7_eN1lOqACWwbgCRE2UtxGgEwul1wV0qPDTRKiDJpBHhI3wM2oAbQpm_MdWZE_YUXhtcRldRQ-RECeQJZ9cMvvfL89hyvEGFhqAvwzL269hLT6wp2Z6TeaCvE_wEGMMpxRcVGqO5JQeaMI0P511rsEskgbn3yChOwb_Gyg1rwrlT9LktWjLyBCZohaDBv2Bv_zc2F2tldjkU60LH52w3dUob85KjVFttO-Iurdy-ELGhGKVgbRrVhJ4k-73AtQ1B1aYtshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
پنج تقابل اخیر استقلال و تیم‌های قطری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/108421" target="_blank">📅 19:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108420">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74e558890.mp4?token=bOrKd8ljcIt6Qd9py5CCTtPEOpNgwJL_MdcK2fwe2tai10jaX3nd4dm4KCOK5M3V7S-PgBqKbjjM-d23eqP-CMvU_X1cyoduv2WA9EcnClmjo5U2tocyrqeiUArAJa9XHsznLP3Y89LcYxHcJjm4UsTSqGJOVit_MvaOXATKBN6HEPTSylzmWYZrUzxXTmeii_XS7F8GyGZGPtVriA2ND6Ldv8lWPktByRaYI8H1Ue4QUCcVcfIdBkJbCxGBJ1x3WwC18dVmaRyA58M2GbGouiBH0LTlA6s7G89u6emYcFy3DY-h43Ayl0iQT1ERY8qiBA_4cJDmBUYtebHq5KVhcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74e558890.mp4?token=bOrKd8ljcIt6Qd9py5CCTtPEOpNgwJL_MdcK2fwe2tai10jaX3nd4dm4KCOK5M3V7S-PgBqKbjjM-d23eqP-CMvU_X1cyoduv2WA9EcnClmjo5U2tocyrqeiUArAJa9XHsznLP3Y89LcYxHcJjm4UsTSqGJOVit_MvaOXATKBN6HEPTSylzmWYZrUzxXTmeii_XS7F8GyGZGPtVriA2ND6Ldv8lWPktByRaYI8H1Ue4QUCcVcfIdBkJbCxGBJ1x3WwC18dVmaRyA58M2GbGouiBH0LTlA6s7G89u6emYcFy3DY-h43Ayl0iQT1ERY8qiBA_4cJDmBUYtebHq5KVhcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ذات علیرضا بیرانوند به‌روایت قدیمی ابوطالب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/108420" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108419">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108419" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/Futball180TV/108419" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108418">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAGLpM_sj1-mt2tXMr-CDMsTNvYi5Nr4nlJRuvq39aLK0LZvPUF8JR5pKPqzKfC3liaQFvgM67YaqPcznZLuVMnqUmVF6djLjRp9O4pF87iczj3byurscfEf53UePlCnCh5nIGZgF5IO11wglQXxyKJdrKlivI5XCeFMSWBVJ4hFeiGozt5i56a3j5X5Min_pU0zZvn9IO7VmgWDHULW4Bl5umIJ7m3r1u4txohTDTbAvX8E4P5kE0wDJooBGc3jSn91SuRIgcl05kca4Ot5QW9stlg1iYyJqOJZtD27vMYtR6uIeC1uu4PTfa-q2FTM-BPlk_F2tXM0csf3JZb-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/108418" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1781669ce0.mp4?token=rHYcxlMweu_f0BWEhptCBaD-GrSQf_D-h2JcaAZ2UW9cctG4AsopoMkcp4qIeL7yE93rD71i36sJpHI5LTy8-opbuMTSegKPLmCgfEyOsfJfg2FjUsnhmJwVJPMF5HRu8t-xviWocaBZSPNsynPu_UUPM9RBKhiIcz2Nt8vLilJOYYCjmoBmsEMk8oukN8t2MUoRRkmgdVZCp2RtEgVvSqR0lWNOHJr1KSbSOOAp-w4CzoBre86zt7Ye6mGSHLgq6djELwEXBj8WUhbfmZlDRjokrzgjGG4axlxAkNAmFh6m8Yqn9RAnYMslocOZmAcSwmq3EdDwahHQqz2W1jA0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1781669ce0.mp4?token=rHYcxlMweu_f0BWEhptCBaD-GrSQf_D-h2JcaAZ2UW9cctG4AsopoMkcp4qIeL7yE93rD71i36sJpHI5LTy8-opbuMTSegKPLmCgfEyOsfJfg2FjUsnhmJwVJPMF5HRu8t-xviWocaBZSPNsynPu_UUPM9RBKhiIcz2Nt8vLilJOYYCjmoBmsEMk8oukN8t2MUoRRkmgdVZCp2RtEgVvSqR0lWNOHJr1KSbSOOAp-w4CzoBre86zt7Ye6mGSHLgq6djELwEXBj8WUhbfmZlDRjokrzgjGG4axlxAkNAmFh6m8Yqn9RAnYMslocOZmAcSwmq3EdDwahHQqz2W1jA0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پیام آسانی از قطر: امشب برنده خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/108417" target="_blank">📅 19:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7be6fed2a.mp4?token=IFRoEUlUGkf8N3Uiz99O2jy1Cdvz6mimPJEffGh7lmqcuMy0apkUI9aHKpHFQ-NkIE8qdMQYG2PzHpbtPjJW_uxA8dM0vvHSAA9nlmqN-EeQzgnO1R6WEf9X9bn387cALCLG1s6FEXK2EtJblRWZ1HA1WLxhRZcdL1LFwRe_OVXEFc0qNhHUQbjUP8g-BZhJtDWFLnLZUBw7QVjJp4ZcsohVedvabVNPu7pgBRrZ7LSMF5MA7gwc1SLPZa8_N2ybjtnl-Pee8Ni-qTch7LUljQtEzUvTtGWkuYS1QhuIs6MGqYm0RGsuIXir_-s-We2_5pFb2V08zID1NlMOv6aOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7be6fed2a.mp4?token=IFRoEUlUGkf8N3Uiz99O2jy1Cdvz6mimPJEffGh7lmqcuMy0apkUI9aHKpHFQ-NkIE8qdMQYG2PzHpbtPjJW_uxA8dM0vvHSAA9nlmqN-EeQzgnO1R6WEf9X9bn387cALCLG1s6FEXK2EtJblRWZ1HA1WLxhRZcdL1LFwRe_OVXEFc0qNhHUQbjUP8g-BZhJtDWFLnLZUBw7QVjJp4ZcsohVedvabVNPu7pgBRrZ7LSMF5MA7gwc1SLPZa8_N2ybjtnl-Pee8Ni-qTch7LUljQtEzUvTtGWkuYS1QhuIs6MGqYm0RGsuIXir_-s-We2_5pFb2V08zID1NlMOv6aOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دیس کنایه‌آمیز امیرمهدی ژوله به ابوطالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/108416" target="_blank">📅 18:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9elr-epnsgTeFN1GGEBxE9NxI5V0rD3Px8Jptlp355klxe4s97gWxh6n7_Adm7zuhZh3CWN-FxNBVUUkEbAw2x3WzJn1T9rieOaEVWRiAfa7iM6BanhWivKFejy_h_mjG8FofBLL7WdTwW4s1lCOWDtrIRAcjvBdhv_Xsz4GODyVhabJqsUsxyrKWMygWSPM8f2Pcem6KH14_9GK_gbZ_RlpJ30bl3UuQCBfCvj2BSBRv7igercA4IPrChlRFzttzb_BEKfppJDLztvAMsQjwO-qKsqztlues2Zdt4azETZ0AW1phSTknNGWOzhY7aTCp3ppL_nMihrEfnmcenzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
هادی حبیبی‌نژاد، وینگر تراکتور به‌دلیل مصدومیت بازی برابر الشمال را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108415" target="_blank">📅 18:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjUl34KkQji0PPGWkuJ2W42DVdFHQPckmbjcUbkBFzZOCl7c07nXzzldvuUpG-yCs-fUMe2OxEPITqa6eyX695mmtWSyZUESt9JnuknsvsCNoqUDND1PvjMTRSDWfXvoI5nn20ouNyWF2wQa9iNu-xW1qubT3woCTWxn-7tIuv7Qtq9cyPt-ineGYicTHk4LnJHqN8mkIaH8ZwGccZhKGgvjT1P0DiRvsSDRRyM0QEvrfR0W7vc3LiykYVCGrmOEIctepXG5VUfaUYDvXDltPKn_q6eaGsiUzEX1rTQ2jsbtMVclybF_NG9NyZ99BEXRDj3xwPz1WjzqaG6VGjXhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
هادی حبیبی‌نژاد، وینگر تراکتور به‌دلیل مصدومیت بازی برابر الشمال را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/108414" target="_blank">📅 18:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9fa51c9d.mp4?token=PgU10y0zK8BVopaqMB-BeEFrjwXYlhWbCr4AM46wtLmjdBOhcX4pIEyOA15xw9ysQQnI-eoEimi1_UQ2dD3-7nN9CFcxn_frAeqa0ZvtOh1b3yBKiQh1ZkODcvxn1luZgl6eet_IRAZn0YIXhsFrQO54FjOGAfVwCgKujJt7TN72PrWNx-uX_Vv8cxrPpLOi6Q57KWWmG9k55kKR0zY8X3IVYOHpk1HIAyeGskH0zerGjyBobUOzixjgudMmz-_Sc9CURuzSrUplEEsZx63rQUr8yQdOk6ON7ECnVHo93BmwIJv3v3H787JpzO8DRgm8ouNDoFc1WInjDE3hFcNeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9fa51c9d.mp4?token=PgU10y0zK8BVopaqMB-BeEFrjwXYlhWbCr4AM46wtLmjdBOhcX4pIEyOA15xw9ysQQnI-eoEimi1_UQ2dD3-7nN9CFcxn_frAeqa0ZvtOh1b3yBKiQh1ZkODcvxn1luZgl6eet_IRAZn0YIXhsFrQO54FjOGAfVwCgKujJt7TN72PrWNx-uX_Vv8cxrPpLOi6Q57KWWmG9k55kKR0zY8X3IVYOHpk1HIAyeGskH0zerGjyBobUOzixjgudMmz-_Sc9CURuzSrUplEEsZx63rQUr8yQdOk6ON7ECnVHo93BmwIJv3v3H787JpzO8DRgm8ouNDoFc1WInjDE3hFcNeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
گزارش جذاب عادل فردوسی‌پور روی گل‌های دیدنی چرکی و دوکو مقابل لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108413" target="_blank">📅 17:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG9D0pblyeZXeEfqd5wruTC93oXQhihmUtLTy-yQjbgg4oOR7711ri-MyWL6ZmQ49ShzCzXGe5w6S1cgM7oE2l7zdeD7l2uIH6ybFpfLAp6-LzL648kdjjSitej9bM0_7pMDPjSkmEBlwwUafoC-kyN4JzH2OC1vDzAaZQyEv03Wzpa2ug1ZDk9MoMQ63o6b1nTM-zua7vU6yl1uvfU_xdH67pE_fxsLELtTplarXX_nuFX9CT6Zduu-G53054029ReFh41vIi7X2klsPwsXThc1AYtA0vOcgWO0ZvBNBhqFzv3_aBNGPHX0UVIA5JHfT6A1Vm12naeh77NVMtQNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
متئو مورتو: پس از کش و قوس‌های فراوان، انتقال دنی‌ کارواخال به ختافه نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108412" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3a35ca6a.mp4?token=rS4VRl0jr_n_uduISUUbnOJtn3UiPi8A0foWAyaIRB89t90XL1zKTyBjaprIkBFZyxyJAQNMtgpaR11XMX-R42B_RZOp5GXC_heFp0uNKgeLksc8BhZuel3XiHsKw_YdroCDUYMpwLuFHLaht_4m0RSxclG9JCXsjPsMx8Wr6fnIUmm4BmrqoTTBZgx3hOcy0G1mjUb67J5kVrUULDXUO-KGw3iKdp7chLkqfsQmvudJm1lBwOnCiXpRjMdLNjPDvp7-Hnslda-g0sy-wdslsq2TmCOYcNDLL1NooXFNztN-szM3vOsPHA6a5VenFQ6ODSi4c9mnN5RyMjv-Ie5NSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3a35ca6a.mp4?token=rS4VRl0jr_n_uduISUUbnOJtn3UiPi8A0foWAyaIRB89t90XL1zKTyBjaprIkBFZyxyJAQNMtgpaR11XMX-R42B_RZOp5GXC_heFp0uNKgeLksc8BhZuel3XiHsKw_YdroCDUYMpwLuFHLaht_4m0RSxclG9JCXsjPsMx8Wr6fnIUmm4BmrqoTTBZgx3hOcy0G1mjUb67J5kVrUULDXUO-KGw3iKdp7chLkqfsQmvudJm1lBwOnCiXpRjMdLNjPDvp7-Hnslda-g0sy-wdslsq2TmCOYcNDLL1NooXFNztN-szM3vOsPHA6a5VenFQ6ODSi4c9mnN5RyMjv-Ie5NSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودش جمع کرد رفت
😂
- محمدرضا باهنر می‌گوید آن خانم مجری که گفته بود «هرکس اعتقاد ندارد، جمع کند از ایران برود» خودش مدت‌هاست از ایران مهاجرت کرده است ..!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108411" target="_blank">📅 17:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭕️
🇮🇷
برای رزرو تبلیغات خود‌ در مجموعه تیوا، در آستانه بازی حساس و مهم امشب استقلال و تراکتور مقابل رقبایشان در آسیا، می‌توانید به آیدی زیر پیام دهید
@Tiivaadss
@Tiivaadss
@Tiivaadss</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/108410" target="_blank">📅 17:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5e45f75b.mp4?token=v4od1mTRG8dTslsSWhMu_pSo1HmcE8OyMxDdUdDTnHwi38fiTEuauD02UbjHAEXqyz4aEKf9bq4o2rhW2vAzI4dWNiGOxMeUUQC-DJVL19eU1ACU05i-jhLILt_LAsv-dulMGogFDKHnuruLJuccN8kfvwlGjwYqNP3PicqlZLfjcs5vZUYLGk7ydOkzwZxZi8klLRunt7u1tdzK7Nm50UUesiookeGZgR2y4teNM5LU4riFuC7mvnpMoWhk03xtTNkWtw7URdy6eJh73q2cMrU-mqV78JAe73QqXQp0nK38DNWD0lXezZjoqlIek_CoX_mO9D4zYpNd9Ei0CHr_1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5e45f75b.mp4?token=v4od1mTRG8dTslsSWhMu_pSo1HmcE8OyMxDdUdDTnHwi38fiTEuauD02UbjHAEXqyz4aEKf9bq4o2rhW2vAzI4dWNiGOxMeUUQC-DJVL19eU1ACU05i-jhLILt_LAsv-dulMGogFDKHnuruLJuccN8kfvwlGjwYqNP3PicqlZLfjcs5vZUYLGk7ydOkzwZxZi8klLRunt7u1tdzK7Nm50UUesiookeGZgR2y4teNM5LU4riFuC7mvnpMoWhk03xtTNkWtw7URdy6eJh73q2cMrU-mqV78JAe73QqXQp0nK38DNWD0lXezZjoqlIek_CoX_mO9D4zYpNd9Ei0CHr_1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
▶️
شوخی فوق سمی ابوطالب با حرف بازیکن سابق استقلال که گفته زمان برانکو هر بازیکنی 5 میلیون می‌داد تا بره تیم ملی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108408" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6a06bb79.mp4?token=fQa1fjkPzwoy7bgsU552BkpxoAfPZiZ1kNBp1bKg2eeU4pWUL-bOVjx2dcfUUe-eN35YjQve__Ym2dh7YVPFVFuzQ5pCH7sQurCsWsS0Jeys2mJKPlKZ__m_TnxbmB8hlb2M9uX8at6jGAvy8Offzv8QXToy5A7dfQDLLbX9ZqS4QV1sA4X1JLJRRkNJS4EzsDISWwf16KfCWh0k1auzvkDcO6lg21CMpHvpPixs7ePw_q8K8xK5myerHjK1WqzKLS-orgRa8vVkdXyiUl8xZSTj1IRkWHAQPV7SNZ27uu1_1tCLSM_QRHMfSwKeHLVe7A1K1qWFAGmMxz4lpVfhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6a06bb79.mp4?token=fQa1fjkPzwoy7bgsU552BkpxoAfPZiZ1kNBp1bKg2eeU4pWUL-bOVjx2dcfUUe-eN35YjQve__Ym2dh7YVPFVFuzQ5pCH7sQurCsWsS0Jeys2mJKPlKZ__m_TnxbmB8hlb2M9uX8at6jGAvy8Offzv8QXToy5A7dfQDLLbX9ZqS4QV1sA4X1JLJRRkNJS4EzsDISWwf16KfCWh0k1auzvkDcO6lg21CMpHvpPixs7ePw_q8K8xK5myerHjK1WqzKLS-orgRa8vVkdXyiUl8xZSTj1IRkWHAQPV7SNZ27uu1_1tCLSM_QRHMfSwKeHLVe7A1K1qWFAGmMxz4lpVfhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکوت رونالدو شکست؛ افشاگری طوفانی کاپیتان علیه ژرژ ژسوس!
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108407" target="_blank">📅 17:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/108406" target="_blank">📅 17:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwCgyOI1eGG_SMP9Ns7ONxbUNRJh6681eiCW_oZFEAkWcyp8d71mdGs_gvVBdgTzQ-xpSMl1Wgb0k7TTaHdyzmmtsMNTgBnHGQD-gEigywxj2Ifegh96bZ1G4y0iTpnhw1CZ_as96M2CbCkjOsSB8plyWE467bizMvSPsQ6OG063kl3MCHDoTb-MbJ9T4amO-WQG9_arqrN0DEGJxF8_2YRSVAcogXwGbH-9-P943Mk1AOVrqSLIKYpNNMqUtJUEWmcHFhr4hKCycWZk9c4qiqUhqNE4pH-NIsD5SUC74gfAlCs05TotbUz1g-BXzxj8tBos_skn2smgt7zZTMUQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108405" target="_blank">📅 17:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e243d4d.mp4?token=AaTfaQtf3ELki-rSlq1Y7ARm9hl8rr6RcodGtNUge8fdyu4p7AK8H6Z65TMF4YTIFz_A-BIlsQoAklGXovHAXIZcAjIJY1mvYYGEgIp1Jjq4Q8EsB92INh4A2wNB98qastGOns27obwj-wlfg8m65eyGD2KdJYYcvjH2SXQDa9mky5-ovksEb_uQjw0O38ewZdJpV1Tf0anp9PtrATk_TmKvCRn760g8rwb6Gw0HTs3lUdI0RTH_H-p8w3FMkQaOzy6CwsIzOhYbiKgV7NJ3yHvb09RQGddCmz9E3yX_MyGaFf4FIHmM1bBx3jfUCQleUVZpx_H_J5RyYyHWuAJSsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e243d4d.mp4?token=AaTfaQtf3ELki-rSlq1Y7ARm9hl8rr6RcodGtNUge8fdyu4p7AK8H6Z65TMF4YTIFz_A-BIlsQoAklGXovHAXIZcAjIJY1mvYYGEgIp1Jjq4Q8EsB92INh4A2wNB98qastGOns27obwj-wlfg8m65eyGD2KdJYYcvjH2SXQDa9mky5-ovksEb_uQjw0O38ewZdJpV1Tf0anp9PtrATk_TmKvCRn760g8rwb6Gw0HTs3lUdI0RTH_H-p8w3FMkQaOzy6CwsIzOhYbiKgV7NJ3yHvb09RQGddCmz9E3yX_MyGaFf4FIHmM1bBx3jfUCQleUVZpx_H_J5RyYyHWuAJSsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تکان‌دهنده موبو نیوز راجب رجیستری سرسام آور و۲۰۰ میلیونی آیفون
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/108404" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c1f436af.mp4?token=O5aOvufBxD-bdLVF9KFBvv45vq9g49xiPEtdCwtQc1n92l9BoVYMBSTj63-G44JzLvfalPhn6mCVuvCCwLhlGp6LW5bcJ7tWlux8BSP0Yuvm8T6bEO_ZGl1vMchWM-YZfkuAmMnsj7wSkCwAKpZiAi7HJhksF3mgOQFHIvKjO4APgCEMOr3H7WnLLg41mSo7bpyDC3SugySIS052lkheYKFvKcbT6Za8OIAzGjX1wBVKH1_NViK58PpWVagr7BaXpP2CrtaRfDtjeR4sWkGdxGWz0QbqcBiG9YCB7Kr2AAxzauCudecW4WVWODhNxYBOnbe8XmcjHTEwmRXoxWY2mAe-UcH-mwe24OCj3T27G1kbXt8KfyO3IgUu1ekD4i_IMePn78S1u1En4zW_g9QivFUU3EfETZKc0o3yG91MTlwMvRQo8bNY-PxhvalJlS6xkc62zIklXikr-Q3oYaitrHxOmL1R88RJbsqnvMYY64l2Pvn94TFNGefguU5ad8AF2uwADEryHs0Nwgovo-L-7YOZIBc52AAuu_DeT0q0dugRiW62F4vDeeCMMFO3yCsCJXF7U7C1mJwvoJGFI59-K2iFyo2C471XZcprjBizwDvV_a1c3kP4pfsTmucGrg_exmwFmBbLRSQL_6r0-dzqs550mIYaB8BBzJcr3zq20D4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c1f436af.mp4?token=O5aOvufBxD-bdLVF9KFBvv45vq9g49xiPEtdCwtQc1n92l9BoVYMBSTj63-G44JzLvfalPhn6mCVuvCCwLhlGp6LW5bcJ7tWlux8BSP0Yuvm8T6bEO_ZGl1vMchWM-YZfkuAmMnsj7wSkCwAKpZiAi7HJhksF3mgOQFHIvKjO4APgCEMOr3H7WnLLg41mSo7bpyDC3SugySIS052lkheYKFvKcbT6Za8OIAzGjX1wBVKH1_NViK58PpWVagr7BaXpP2CrtaRfDtjeR4sWkGdxGWz0QbqcBiG9YCB7Kr2AAxzauCudecW4WVWODhNxYBOnbe8XmcjHTEwmRXoxWY2mAe-UcH-mwe24OCj3T27G1kbXt8KfyO3IgUu1ekD4i_IMePn78S1u1En4zW_g9QivFUU3EfETZKc0o3yG91MTlwMvRQo8bNY-PxhvalJlS6xkc62zIklXikr-Q3oYaitrHxOmL1R88RJbsqnvMYY64l2Pvn94TFNGefguU5ad8AF2uwADEryHs0Nwgovo-L-7YOZIBc52AAuu_DeT0q0dugRiW62F4vDeeCMMFO3yCsCJXF7U7C1mJwvoJGFI59-K2iFyo2C471XZcprjBizwDvV_a1c3kP4pfsTmucGrg_exmwFmBbLRSQL_6r0-dzqs550mIYaB8BBzJcr3zq20D4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
▶️
🇮🇷
آنالیز جذاب از پرسپولیس سرحال تارتار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108403" target="_blank">📅 16:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4fbc61d.mp4?token=uKifMRauSTtRJINkpjIjS2yMxHZlPasiXjruCTh6Y-KQP6KDBohFY8OyZM9Fj7bzm5xNq7_1eAtlXjeBOY39uLky5auZTKyRqaT_1pNWnbn2FuA7-ihsIwRpqNNVqFmT56QydODuqOwW5qNWUJQqVggtjZBGBFYA9n01g-7hckasu4X-xzVlPFZML2oJLQStNU5aDav_y8DAVRwBubj8Z1H-CqWRodGuYgyyGeUpxv94Qpv1cVnCX1nQv7Fld2KYO--bOAByAXt-xFIQXEygdxYPYrsW2KbtvxbQp6d3gw3gvjIh-QJ58cQozMJhc6pfuTEYsvdDtDvepLb6rmkGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4fbc61d.mp4?token=uKifMRauSTtRJINkpjIjS2yMxHZlPasiXjruCTh6Y-KQP6KDBohFY8OyZM9Fj7bzm5xNq7_1eAtlXjeBOY39uLky5auZTKyRqaT_1pNWnbn2FuA7-ihsIwRpqNNVqFmT56QydODuqOwW5qNWUJQqVggtjZBGBFYA9n01g-7hckasu4X-xzVlPFZML2oJLQStNU5aDav_y8DAVRwBubj8Z1H-CqWRodGuYgyyGeUpxv94Qpv1cVnCX1nQv7Fld2KYO--bOAByAXt-xFIQXEygdxYPYrsW2KbtvxbQp6d3gw3gvjIh-QJ58cQozMJhc6pfuTEYsvdDtDvepLb6rmkGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول 0-3 منچسترسیتی
مارسکا آنفیلد رو به آتیش کشید.
🔥
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108402" target="_blank">📅 16:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108401">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3846e1615d.mp4?token=KNOpFC3Xt8x4MoQNedLjDXYxu4huIkS4lgUqE7tGfX1jU3aBPgtdzSTyqNORA68xbt7MT9mQZMJW0YOvCOozRjMbnc5FLTus8klR_pAu6oMODeiwt-KZGE26hRqr2JA6gkxDEXKGl8_cYOh9Sz_3j6qS4WiPBjmzpQT8otOPhhhxfJ5koRwyL5GT94XHlHE3rq91x7ZC0eeMc6T6PuYxuWlo6goiUOCffCcwg06IbmfBOKWaO0_uadjClE16J2KHM-LIuTvpgLLpYrFgLzgwFXFtNp-Ht58JpAvACe0-KawswpHGZUKdFvWqzV2qgRBybtp0hq64lg7Pz6wQZOcrDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3846e1615d.mp4?token=KNOpFC3Xt8x4MoQNedLjDXYxu4huIkS4lgUqE7tGfX1jU3aBPgtdzSTyqNORA68xbt7MT9mQZMJW0YOvCOozRjMbnc5FLTus8klR_pAu6oMODeiwt-KZGE26hRqr2JA6gkxDEXKGl8_cYOh9Sz_3j6qS4WiPBjmzpQT8otOPhhhxfJ5koRwyL5GT94XHlHE3rq91x7ZC0eeMc6T6PuYxuWlo6goiUOCffCcwg06IbmfBOKWaO0_uadjClE16J2KHM-LIuTvpgLLpYrFgLzgwFXFtNp-Ht58JpAvACe0-KawswpHGZUKdFvWqzV2qgRBybtp0hq64lg7Pz6wQZOcrDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
فلیک: "ما برای رکورد زدن بازی نمی‌کنیم. تنها چیزی که برای من مهمه اینه که بازی‌ها رو ببریم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108401" target="_blank">📅 15:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108400">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add4134242.mp4?token=QCSPQzaSIcX8eljMJcpc7oV_LO4kd2x2MnOzjH89lDfZsrZ-mWn-T2FIf7knl9M_gluTHCMhlVLh389mHR2XL1sQ3pFMQS44sJy_GTDd_lbhivpcuy5okg6XVN3M-N_cqK5y5u6mVAhyD-FrR-R4PKK0XFMF4XvW4tEJkdZXEKBbVie8mP0TTrkUc3aMmcFRL8VJb2FfNa4Wkykhk8IUv3Oa5RrfDERZaGe6af_8UMtkezxzBWZRZqofE8lGYKGasyydmtwsP0rDm2ACC411F-3kOstvx28QxtpP1maaG6NbbxSFgdOaoBssBB7GyoqyIEfFFpkr7kqyDSgKUVEUCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add4134242.mp4?token=QCSPQzaSIcX8eljMJcpc7oV_LO4kd2x2MnOzjH89lDfZsrZ-mWn-T2FIf7knl9M_gluTHCMhlVLh389mHR2XL1sQ3pFMQS44sJy_GTDd_lbhivpcuy5okg6XVN3M-N_cqK5y5u6mVAhyD-FrR-R4PKK0XFMF4XvW4tEJkdZXEKBbVie8mP0TTrkUc3aMmcFRL8VJb2FfNa4Wkykhk8IUv3Oa5RrfDERZaGe6af_8UMtkezxzBWZRZqofE8lGYKGasyydmtwsP0rDm2ACC411F-3kOstvx28QxtpP1maaG6NbbxSFgdOaoBssBB7GyoqyIEfFFpkr7kqyDSgKUVEUCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش عجیب قاضی پور به عکس قلعه نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108400" target="_blank">📅 15:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys4cg-UaPd3DGgtSq_wdnqfM9MYQR2xqaPYjmFOzDD0tGcd5QjZ-2lM2aRaBYA7gu9fnIiVIydDa61dLYGj52tKutxkURTQgjUwDMAlfVkPfjDZQxxRxgvD_mnjlKoWH5yHr2C4qNDikkBVYCJJ5pk78FMe7QcF3X7zAPF4hllfOAoCEY4_XT92jB1jLCOwk7GJe_CANOZpzCwZzUXg2NwdQvtFG04Am_i95Q55y0YhIJ9MQvUBRMFc3YwxDryZUi4QpRILjXykYFju722wNvT5Fe_Xp75k1PFTeRQNhMte4eKPZ_PE_tulLHxcDs6ZlydCHlids2iE3Q4tTjhaMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه حضور تماشاگران در بازی خداحافظی اسطوره لیونل‌مسی و اسطوره پله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108399" target="_blank">📅 14:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-R91GlndOBGlmyqpCBs9X-bFye291i9e4Xj_h8CYU2xADmaC2UKg_U4u2L2w2DD3nD_sRLSyJW7vrgLusAM4q1AqGSjQ9KCsheFX_ZPUFSn8GbPObB4jGjXR2eoutJmmt3zc6se7DkwK7qVwZ-sbYM6I8O41MXKSmDYqxxV1VWvYGDdB0JhWd0WtrThrIQqcz_Nual-vuhRyki0oOXfKjS8IpmY4QC3gXoyiss4CYOAnaITe99iPngWl1SBgbTFeI_KXIAlQT353Z8JNkIE7JG4jTvtD85dOPFjwWjANpoCQdRvceC9q9BkEIDMKb0jYZOzqlFgKzMTTxO8Pr6WOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ورزش رو فقط دنبال نکن؛ روایتش کن!
آی‌اسپورت دنبال علاقه‌مندهاییه که دوست دارن از مسابقات و اتفاقات ورزشی
خبر، گزارش و محتوای اختصاصی
تهیه کنن.
اگه به ورزش و خبرنگاری علاقه داری، به جمع
خبرنگاران افتخاری آی‌اسپورت
اضافه شو و محتوای خودت رو در یک رسانه ورزشی منتشر کن.
📌
فرم ثبت‌نام رو تکمیل کن و خودت رو به ما معرفی کن.
https://zaya.io/23gzq
@isportapp</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108398" target="_blank">📅 14:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108397">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDuKp2TeEQbOZK0Q5CeWAqDv1ssgm8OWoNW2l0nbPvy2fOKMb8V4ds25AOZc3Dy2zZSoxJn3TWUsph7-SUtxy9txty7EUrwamdKIrX9JYVi1_MeRTVrOok2wzoqMFzGem_6szHtEVCvG7jTKBoWi7pjLmMTOOadsGyTJDCvrpV_APjnOEdY98uSAUtvJmxhQhBY_9Tkq3egxbmTVEvd0WuUH25a40D6r1PapqDZzgBw9y8vv7RlEg6PtxLchghQesxxMaZ_2Hdxq_RAh_LIOrrovVwkfnrbWO8UzICOYdD0Z0b0vslELWm_r8B46wcP3rdUP2VglJ7i0kedaHF1KUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: رئال‌مادرید با تیبو کورتوا برای تمدید قراردادش تا سال ۲۰۲۸ به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108397" target="_blank">📅 14:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40807887e5.mp4?token=qOcslJTQPXBmZmdiDlVvHij-Rq5g05yUS_WArQsg4N2I4Z721hyh4YBZ9lpOC_JFomECp6AVRPopkw3cT6VD6t4a7C7y6ezfyY2aDAX98QjrhCk0ocSQk_ne7xPJIq4XWmTqirOwPKp88R1h0C-fHs6H2d1GSOqqMt2qgB-UBHFVJQCWk55Vb5NwcykWk9GRBx7PMpa9d7MsbxF66ZCcPCyUnGSeMC9hA3QN9smzd7WYNRtbjuC2-nYC1Qhp8G2jWod2JWhesMZrYMHkUszcOQ-rpfruL1pqC1PeDQlrqZR-yZFOVgT58At1kWLbk-Z6s0rLl0sSMcnOaMiAmf8Y6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40807887e5.mp4?token=qOcslJTQPXBmZmdiDlVvHij-Rq5g05yUS_WArQsg4N2I4Z721hyh4YBZ9lpOC_JFomECp6AVRPopkw3cT6VD6t4a7C7y6ezfyY2aDAX98QjrhCk0ocSQk_ne7xPJIq4XWmTqirOwPKp88R1h0C-fHs6H2d1GSOqqMt2qgB-UBHFVJQCWk55Vb5NwcykWk9GRBx7PMpa9d7MsbxF66ZCcPCyUnGSeMC9hA3QN9smzd7WYNRtbjuC2-nYC1Qhp8G2jWod2JWhesMZrYMHkUszcOQ-rpfruL1pqC1PeDQlrqZR-yZFOVgT58At1kWLbk-Z6s0rLl0sSMcnOaMiAmf8Y6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با مفهوم علائم درج‌شده روی برچسب لباس‌ها آشنا شوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108396" target="_blank">📅 14:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5ccef6c8.mp4?token=lvEEMUIFVhiJDxE6b8NSCAU_xWj1JYes9nddgYBr0QLJdocqfbOIf5O5aMkIoRZpjheyft_c5WSNdeTA7dKXhkWSWXAvD3_3ZIC2d3uNgRbcvVgfhwlbnYk9jQx7RYpoY3ClPchk4cUkiRLWgVhNV8FaUDKpYPdoWan5vBS4Nqu9GRC4AGi-dUR-SPsIe_cgzjSGAVFT0IEcwZm3cCavcgZfgtyfWbxILNz3FjhM67h1t5A73T5liunAVnWiDNROq-QtxkErML2IuB9klnHQQm93pnFxRC_SROhnJatiWKYqeVKVb1wF2s2P9vWSYOAHbkzz67KfX2LPoWm7Xkp9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5ccef6c8.mp4?token=lvEEMUIFVhiJDxE6b8NSCAU_xWj1JYes9nddgYBr0QLJdocqfbOIf5O5aMkIoRZpjheyft_c5WSNdeTA7dKXhkWSWXAvD3_3ZIC2d3uNgRbcvVgfhwlbnYk9jQx7RYpoY3ClPchk4cUkiRLWgVhNV8FaUDKpYPdoWan5vBS4Nqu9GRC4AGi-dUR-SPsIe_cgzjSGAVFT0IEcwZm3cCavcgZfgtyfWbxILNz3FjhM67h1t5A73T5liunAVnWiDNROq-QtxkErML2IuB9klnHQQm93pnFxRC_SROhnJatiWKYqeVKVb1wF2s2P9vWSYOAHbkzz67KfX2LPoWm7Xkp9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه‌گزارش متفاوت در صحنه گل زیبای رایان چرکی در بازی دیشب مقابل لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108395" target="_blank">📅 14:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108394">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31cf9bb67a.mp4?token=Ie6t74lCtu29ZLvMYhskC7vlYyMcLmens1NimcGF2Xmi15JAfJh9VY3EWuxPe8bex9edz4MhNhfjdDxaBsmKNpiGe3Chaq3EBRu7kWYF1Ib5ND_OOPYMLsw3E5rp4jCTHFhteY-g8SQ4u7JvHXxyHa8bn4psHVaOwxDx_n7ZAa19wQlVNLK1RrlF2nrzoMRI-wZ9lMl4RBqd99tUzsYXXpA-U3kvm5rFfOQhq78Kh7-0CdWv3BUjLcjmmse_PjDy2jg0DCUAa0fA_K1EkEfBqfEsnXIJhHk_Io_hHZbgM2J3pPes4g_kNG_bX0gUnhbx2pemUfj1R0guBKvf7eod2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31cf9bb67a.mp4?token=Ie6t74lCtu29ZLvMYhskC7vlYyMcLmens1NimcGF2Xmi15JAfJh9VY3EWuxPe8bex9edz4MhNhfjdDxaBsmKNpiGe3Chaq3EBRu7kWYF1Ib5ND_OOPYMLsw3E5rp4jCTHFhteY-g8SQ4u7JvHXxyHa8bn4psHVaOwxDx_n7ZAa19wQlVNLK1RrlF2nrzoMRI-wZ9lMl4RBqd99tUzsYXXpA-U3kvm5rFfOQhq78Kh7-0CdWv3BUjLcjmmse_PjDy2jg0DCUAa0fA_K1EkEfBqfEsnXIJhHk_Io_hHZbgM2J3pPes4g_kNG_bX0gUnhbx2pemUfj1R0guBKvf7eod2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
گفتگوی اتاق VAR و داوری بازی رئال و ویارئال در صحنه منجر به اخراج وینیسیوس جونیور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108394" target="_blank">📅 13:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108393">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda41cc68d.mp4?token=Uszj8Goj4FPIDTejHulmCG23EiUsDKRxpwFoBAdiQuC0K8AFnjMWNEo-2eXgNZuuAMQJ5rYhks8htRKJqPwmuWjnpI25zLed3Dfex1rkEV8fFfTDr9QYY92RL0vY5TbdAg8Cjzhj2wf6yCZGeEUSxQeDIoq1OfAGHAGhPIngFkce9k_jbUjJMo7Bf03sBj8CBsDbfKShYSRTb6UAWQVK73wT9Mx1hWwq2cH5vQwuACbyo-9KkZ8PrcblBkNWn0g0sB4H7D5IxPx6l913xdclcqC_wB39odQNSCtsuCCGNfDhTI_sKif1DuG_vTUiny-fmNvzkxdPk39LNbTQ1kOKSV00BeTS9-UfhNsGmmQ_yL2HQ0e6ZoOVahNigihzJaxsRwB_dpQfTQN2mYrhcik437qLlsgQyQYRJ7o8qzy4SvpaJoxXqrYCBxSfZck1Iwjov1y2IWIaHl_uqV4l6uNUEX1y7y84jcDK3yL4TkSAJj5fEnw_uDg3M9YRtOTSDs7FKrOZbUM5NRDMH0CQsxVziMlULLLZhHWbQa_mcE8kUIfXUHwKMGwJ8vnMBcCaQJ8WoUIgPbthclOB5z63BwluhNcIJt2Zu7Mn0YzD2ilUOx9zf-GWoZtxjO25UP79SnaikHvWyj1wWenGcgVNWyXNg6k7KAFMwdLhT1tGAYdWubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda41cc68d.mp4?token=Uszj8Goj4FPIDTejHulmCG23EiUsDKRxpwFoBAdiQuC0K8AFnjMWNEo-2eXgNZuuAMQJ5rYhks8htRKJqPwmuWjnpI25zLed3Dfex1rkEV8fFfTDr9QYY92RL0vY5TbdAg8Cjzhj2wf6yCZGeEUSxQeDIoq1OfAGHAGhPIngFkce9k_jbUjJMo7Bf03sBj8CBsDbfKShYSRTb6UAWQVK73wT9Mx1hWwq2cH5vQwuACbyo-9KkZ8PrcblBkNWn0g0sB4H7D5IxPx6l913xdclcqC_wB39odQNSCtsuCCGNfDhTI_sKif1DuG_vTUiny-fmNvzkxdPk39LNbTQ1kOKSV00BeTS9-UfhNsGmmQ_yL2HQ0e6ZoOVahNigihzJaxsRwB_dpQfTQN2mYrhcik437qLlsgQyQYRJ7o8qzy4SvpaJoxXqrYCBxSfZck1Iwjov1y2IWIaHl_uqV4l6uNUEX1y7y84jcDK3yL4TkSAJj5fEnw_uDg3M9YRtOTSDs7FKrOZbUM5NRDMH0CQsxVziMlULLLZhHWbQa_mcE8kUIfXUHwKMGwJ8vnMBcCaQJ8WoUIgPbthclOB5z63BwluhNcIJt2Zu7Mn0YzD2ilUOx9zf-GWoZtxjO25UP79SnaikHvWyj1wWenGcgVNWyXNg6k7KAFMwdLhT1tGAYdWubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
به‌بهانه سوپرگل بازیکن فولاد در این‌هفته؛ نگاهی به برخی از گل‌های از راه دور لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108393" target="_blank">📅 13:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
⭕️
👤
نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108392" target="_blank">📅 13:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108391">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8ec15e67.mp4?token=p0PwcExCn37Bo21VU3s9XNdWn7Eop0DuzTEmkrDX5AQDhAyJ6hOS_DOX3NhTx9EhtwUau0QvxyRivZ5LviVzTJE_UMA-j9SXj0WDk75sMEducNavliEe1iDNpLwvfJAYE18LBrWeVQi9QXqrYTRyu8o9a_IoDrAG5hAXTiiEJAUuK5GvVaRtz001oIticxxEWQVbMp3H2LEvEo6N4FkQR3phZnvAn0EZzww4NcUI_D5VPe8QB0TbZljKgiGuMZ-mipwZBAOC0086Ql132rk4pV3nFeDhT-AamtRasDiGPrHRr-8XwSZGjOnIR6yjzzVS_wRE6dflBem_rFiWc_jv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8ec15e67.mp4?token=p0PwcExCn37Bo21VU3s9XNdWn7Eop0DuzTEmkrDX5AQDhAyJ6hOS_DOX3NhTx9EhtwUau0QvxyRivZ5LviVzTJE_UMA-j9SXj0WDk75sMEducNavliEe1iDNpLwvfJAYE18LBrWeVQi9QXqrYTRyu8o9a_IoDrAG5hAXTiiEJAUuK5GvVaRtz001oIticxxEWQVbMp3H2LEvEo6N4FkQR3phZnvAn0EZzww4NcUI_D5VPe8QB0TbZljKgiGuMZ-mipwZBAOC0086Ql132rk4pV3nFeDhT-AamtRasDiGPrHRr-8XwSZGjOnIR6yjzzVS_wRE6dflBem_rFiWc_jv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش ژوله به اتفاقات عجیب بازی نوجوانان استقلال و شاهین و درگیری و زد و خورد شدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108391" target="_blank">📅 12:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtC7-9x1S9sztXnr92cxkm3ZJS4cUjxMZU2EhRT-VwuQhUMMdFQryWye0mDdTiTUgUtyyj-TZMjp6KaKlvdBOSDNCaGWq5jILozhnh6XuzGba9m66G6RKv3cm-0FvvjRojKANoDkC55msQm7YOKaO9OI1AMzwE-44pmY1FXFyhISxpgXa_yXeCkh2BmP6JSSvTqTOLKoF25eNRcmsmDRp-W_W3ee0DsE5Opo2rIl-Q5S00Gzt-H_XsPRZTKHFj1USAFBmXULK6QuV4Xe_CE0QOGJyqPJU13_Dxhs4ZHrwZ68zpOaDH0RWf0oEU7IKrqnShu-6Tj8ASf-P5PPksvvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
👤
نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108390" target="_blank">📅 12:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2B1u1g2lxjeF0I89W0JXsTAUPMFIhwxmf70Lm9-05LK6RTYf5S6OQL1Wn3xXkToWwBmen0ijxrMNZM5jhVjGo7j0JyutucQkIH6eFXr7zAhIrTece0VVZ8ogjHWjdQNXSyhDJS85Gw72nBsWpoMDyRCfiU9SGbb9xd-BKDXQAPx6NMVG9nLlaWz000vvHQZkZ5JHgtIxfl-TdjeyKHV63M8Iqg7FW3OETgBrIJHCrVRJpVxI_ogoydB18CEt0Xmad_dykHssCJY9mdC1fXxaMrsXx5M9BGE24jEaUvvCaGWyKy6AtwO0mvcjwQ2ujE85KY8seLu3RD3TxEkOVf4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
کریس‌رونالدو: من بهترین بازیکن تمام ادوار و تاریخ هستم و این آمار گویای این مورد است
🔻
مردم به اندازه‌ی کافی از کارهایی که الان انجام می‌دهم و گل‌هایی که می‌زنم، قدردانی نمی‌کنند. آن‌ها بیشتر نگران این هستند که چند گل دیگر تا رسیدن به ۱۰۰۰ گل فاصله دارم."
🔻
"من این را دوست ندارم. من واقعاً این را دوست ندارم. اتفاقات باید به طور طبیعی رخ دهند. چه من ۹۲۰ گل، ۹۲۵ گل یا ۹۳۰ گل بزنم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108389" target="_blank">📅 12:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWIEH__6cOuIXsd7GJYcwtZ6R3HFWUee0rRRlEjlo3DCQzqnKCptqVSvjje4iq24RpjdGlnz_NaqSJYH4l2EWcAV03YKkvKqzWVrWjaVO7_Lcz1fzYOFE0zHNlDmm5bbYfL-B9dzuOTxeMQsMKVmzZII8dXfNP8hmw8un_gy-N15AvNeVjKMesZALGN5nN7UXA9Liqo73Kwr52AAbwn2xKpIhckCwmMT0qA-X5-Nu4gqPS_ADyvG5kvg73ZlDLFklKWnOGIM71bs3S7fHT5wfahoBvvBBUUzHAMhBalRMSJNwPX364_uzGc0-SaBMnQryCBWhbVRbejkSo2TUQEwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری علیرضا بیرانوند برای تیمش تراکتور پیش از بازی امشب مقابل الشمال قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108388" target="_blank">📅 12:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adaf3d60c.mp4?token=GqigJbpKhpZLrFsFuyLxRHj6wVDc4Qdn1JOdlMrS5_yJzg933e0HePIKkWXuo3uzmW7RbJuA7QZJW3w9c9bOChvefT-NPB6mTDeXNP4qojJ_56HqSZqW-yNtuzSQjHB5AN9s2soafjrWM5ETQsBeZE9HJjliVcPhx9njd-yVFdsRdDzJremr2_fx_scY8WenByFCkP_OE9oVntinyHkbs-fiSg4RI2z2IS0h6kcI1y5oewCYOy0mAYjYReH2xJPtwOdYRFK2foVC65r3HDUBvmlIKG0U_XAfAbZqeNALqgXsGXTCDkU02Db5oiVbDHGIfvkIbF_JiI9IFtet9mMapoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adaf3d60c.mp4?token=GqigJbpKhpZLrFsFuyLxRHj6wVDc4Qdn1JOdlMrS5_yJzg933e0HePIKkWXuo3uzmW7RbJuA7QZJW3w9c9bOChvefT-NPB6mTDeXNP4qojJ_56HqSZqW-yNtuzSQjHB5AN9s2soafjrWM5ETQsBeZE9HJjliVcPhx9njd-yVFdsRdDzJremr2_fx_scY8WenByFCkP_OE9oVntinyHkbs-fiSg4RI2z2IS0h6kcI1y5oewCYOy0mAYjYReH2xJPtwOdYRFK2foVC65r3HDUBvmlIKG0U_XAfAbZqeNALqgXsGXTCDkU02Db5oiVbDHGIfvkIbF_JiI9IFtet9mMapoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز جالب از تاکتیک سهراب بختیاری‌زاده مقابل تراکتور جواد نکونام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108387" target="_blank">📅 11:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d331ea1d4.mp4?token=ga6wZDwiy9BlrdF3JbIi46_qJ-QbFQjp9vK8EWBI__QZaGdXgX4t6HF8FiNLB8OTOCD77_cYcwMpfn9YeYqpAUmHsWn0QUgSZ8aSf9HiKmO-t5c2ovNT7DtLsSCJAyA05Sjabc-Png3uJ31rnUW_gzGUCm4VJ9kQenMviTFW2teNN-LQrcx1nkPytUOJq8yZc5vuX_lt1rcbA8sscajjhu4v3amyi5w-cf5M0hro5OleoYpSx2uuEc5DkR5e7vOvtVJ0i6xuD8IVFnJem9yBF6ixcTMQqGCBwe0MmKKmydweI0yWDaGqooYFUckzKITszNY5qtFlUAid8VuxvwX8HGyu2Ft7CFZnnbG4zEB858PiwOnpaS7nV-DEec44b7q4RLwLG5IeavKFiKJUl49cjHS9gknslU_EsNIy7KOZRy-zHD3tFJb0olbOMBbFtXcG2fY3UF0f2eJa5sff5y5N7sh04HMqcktoXtjdMlAxjJpH6zwZSXXearImZEwEM2t0TovACqb66MumVimb4TTpkvuduJX3GmSobgFPetrEmDeh7dVtCrKvS71m-MIwJZpTLJ_LvVqhpaVEejPdWkENMoiy0QeuqGxS7dSd-0U44MrzQvST2BznbLOGYm2YZUxdrivhncCE-URO2LCtX2kvGcSMr2IWvTdLcgjEp4WqBWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d331ea1d4.mp4?token=ga6wZDwiy9BlrdF3JbIi46_qJ-QbFQjp9vK8EWBI__QZaGdXgX4t6HF8FiNLB8OTOCD77_cYcwMpfn9YeYqpAUmHsWn0QUgSZ8aSf9HiKmO-t5c2ovNT7DtLsSCJAyA05Sjabc-Png3uJ31rnUW_gzGUCm4VJ9kQenMviTFW2teNN-LQrcx1nkPytUOJq8yZc5vuX_lt1rcbA8sscajjhu4v3amyi5w-cf5M0hro5OleoYpSx2uuEc5DkR5e7vOvtVJ0i6xuD8IVFnJem9yBF6ixcTMQqGCBwe0MmKKmydweI0yWDaGqooYFUckzKITszNY5qtFlUAid8VuxvwX8HGyu2Ft7CFZnnbG4zEB858PiwOnpaS7nV-DEec44b7q4RLwLG5IeavKFiKJUl49cjHS9gknslU_EsNIy7KOZRy-zHD3tFJb0olbOMBbFtXcG2fY3UF0f2eJa5sff5y5N7sh04HMqcktoXtjdMlAxjJpH6zwZSXXearImZEwEM2t0TovACqb66MumVimb4TTpkvuduJX3GmSobgFPetrEmDeh7dVtCrKvS71m-MIwJZpTLJ_LvVqhpaVEejPdWkENMoiy0QeuqGxS7dSd-0U44MrzQvST2BznbLOGYm2YZUxdrivhncCE-URO2LCtX2kvGcSMr2IWvTdLcgjEp4WqBWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو امیرحسین قیاسی از بخش سانسور شده گفتگویش با محمدرضا گلزار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108386" target="_blank">📅 11:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d6bd8a2da.mp4?token=nL83nbCZBmiFl6eMN3hXjObVOk5cgSqO3pvrI9sylRmg75vCiR86Cgy5dzbmzSoASC2b7XbTR2dhA_FlBPOXYLNTRvSkVQEFbZhWXryqEnQlbmdWB4rfAMbVldqxGhDQe0bviH6ZJ6zzMcdIkOjlCNu_5jV2OLGo3MzDSN_J2CZN6FB4NxVzknlYgmhFxpmPZGa81fucHszsRZKDzikEBcu2E4THCpQjrU6myujSMpVPAmujY2UbWjvkbZtNeNamUPkpYy9iWNXQPk_wvKVeDhf9ZsEp_fWHuzHvkkjfMB3upOGGgJENVPoUIeF3YZTYbP4j3Eo7c3LwTl_IuKUZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d6bd8a2da.mp4?token=nL83nbCZBmiFl6eMN3hXjObVOk5cgSqO3pvrI9sylRmg75vCiR86Cgy5dzbmzSoASC2b7XbTR2dhA_FlBPOXYLNTRvSkVQEFbZhWXryqEnQlbmdWB4rfAMbVldqxGhDQe0bviH6ZJ6zzMcdIkOjlCNu_5jV2OLGo3MzDSN_J2CZN6FB4NxVzknlYgmhFxpmPZGa81fucHszsRZKDzikEBcu2E4THCpQjrU6myujSMpVPAmujY2UbWjvkbZtNeNamUPkpYy9iWNXQPk_wvKVeDhf9ZsEp_fWHuzHvkkjfMB3upOGGgJENVPoUIeF3YZTYbP4j3Eo7c3LwTl_IuKUZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
دستورات تاکتیکی عجیب از شهاب زندی مدیرعامل نساجی مازندران به نیمکت تیمش!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108385" target="_blank">📅 11:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoNlAYHQzc9MEBMUjR2v8qS3OArRLtaoUOH8iNTjjjzH357OQRYWpwWjzje_3Sfyjl9Xw-gemyv6G5woYDYnI_W3A2pG0rN3SCeMGs5HHrNLRyLk_kY8w--kqYU7PVGGnrNedsuO4oNWBCTeZxNp2riesaUbe47RQ2NYGLJkaa9Spgl9VcSVAs2SE_zc3nEuNwFDBDwE6XCpMrFbTbtuaWRpfK_jx9jKi6wr4D6w2gg_2IKHcsXJVWwa9uu-a6CIfBRuG6BZl6_uJBzns63rth54mc_fCd7nYI3K71j6rM96M-Yvgqr1QLLNMwyijj2XMdgOApQl837708FHRwIZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
لیست بارسلونا برای بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108384" target="_blank">📅 11:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDm0mFeTwSN-Toje_kKW2oHIXJ5vufQkLGvBElF7QzXRpp2XdSXSbnEYmfukeNreuQWAeG4Jg98huM9hT-VSTeUgcRjnK2uAjqDQ9Znn-sFr_PKIAKhSMj2JlJyNM4IuM0TzWLOLC8ZTj0xak6xgIVpoIUALAkLarJciZtnncjGyoMnLXBeu-dUtRH6AljsVrfkBtoWnBZ-IjdxLj0H0x0zmqiVk_gQ36OzdnhCpqDPFATyFdsuEEQe9dAr-mO84verLYlLntbpsJyvD6rqsL6K2ycKLrrA9XIGgYfSqwgar664pJwrGRcve_LYjFZ6NryEoxovRoUyxldQUvhgpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر روز بازی استقلال مقابل الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108383" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108382" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLh9ruKfovcfYCTbIWYOCkiUdcmAk3iUOC6VBCQXJ6mYCjLu6pD8S8HGnsSW-OEbTnnuACneuByg5760MskQqmMqQ3lDVLVGisIFb-T0eQBUjHzCWUhCDAK-uTPz-Pga9VoTLYxWeOzKGz3eym6nziKf0kUIZ-I18iefky4wyseTtzaZIP58MLiHYcunSAuixMtgDPjLmwJiX29vm0d0ismFh7CW6ZfE004ocst1wrLQtPFCPjl3nXxRI9fr2A_cfE0n1XW41bXIBbU656XYO9eMR0Z7RuOU4yBI6Xg8MG75KJ1P4RtYRmsabLD7zbykvWn7Dlv6q6VYUFxp-Xn2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
کاونتری
سویا
🆚
لوانته
ونزیا
🆚
آتالانتا
اودینزه
🆚
تورینو
نفتچی فرغانه
🆚
النصر
استقلال
🆚
الغرافه
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
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108381" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
‼️
🇮🇷
خداداد عزیزی: اگه دفعه بعدی مجوز پرواز مستقیم به عمان نگیریم، از ادامه حضور در‌ آسیا انصراف میدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108380" target="_blank">📅 10:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b833840a70.mp4?token=JvdGjZPa0exVnE_gkIxzXln7bMxXW1idvGjS5tJ0vnB6RN0pYtv7BrVwG_CKpUgwgZ8fisTbop2VBgvvR8DZU79d0q0tBXLOxOGKPsQLKw2a7Dxj3kaoSQ8M4qnDeMQBe2Ty4miJx6FNmpdbk3CK-0rrJjlpoOVv3mTiIEHKDlixEhqY9Ne-Dy5w2zJm8uLZcCIkmpFEALUV0M94OW01yelagqDMXLf7hsliEbqtBMAUS34mjbMmWMTNds-oyNDJ8-Mb74LhFdIsF_5xm5KaMcAA-Xv1r6zX-TsPa3XDpFh7iq4RzACOEIVItqXQfzPblsGrt-oRI2DK8peO6ujGJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b833840a70.mp4?token=JvdGjZPa0exVnE_gkIxzXln7bMxXW1idvGjS5tJ0vnB6RN0pYtv7BrVwG_CKpUgwgZ8fisTbop2VBgvvR8DZU79d0q0tBXLOxOGKPsQLKw2a7Dxj3kaoSQ8M4qnDeMQBe2Ty4miJx6FNmpdbk3CK-0rrJjlpoOVv3mTiIEHKDlixEhqY9Ne-Dy5w2zJm8uLZcCIkmpFEALUV0M94OW01yelagqDMXLf7hsliEbqtBMAUS34mjbMmWMTNds-oyNDJ8-Mb74LhFdIsF_5xm5KaMcAA-Xv1r6zX-TsPa3XDpFh7iq4RzACOEIVItqXQfzPblsGrt-oRI2DK8peO6ujGJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇰🇷
گفتگوی رئیس اتاق بازرگانی کاشان و معاون وزیر:
فرش راوند سال ۱۳۵۲ از کره جنوبی کارگر داشت. ما سال ۵۲-۵۳ تکنولوژی‌مون از کره بالاتر بود. وقتی هیوندای اون سال ۶ هزارتا خودرو تولید می‌کرد، ایران ناسیونال داشت ۶۰ هزارتا تولید می‌کرد. ما اون سال ذوب‌آهن‌مون از شرکت پوسکو کره که الان شده بهترین فولادساز دنیا با اختلاف بهتر بود، الان ذوب‌آهن نابود شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108379" target="_blank">📅 10:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8cwgE1cN8pxSjEpnOhJYRqQMt4whQmydwaDkmNoldQrFcdeSxROnc-tLoO5k8zv51i_YCRLZpDYtJOOukTACRI7HE4CBMc4RirxyHOOYMxYfWH_ilQouRbMnhUxAnqh7pQI4UMaU53kTx2oZuMRoJFnl-BAKwVSROYvajnxUfll62FM9lJaCV-s31rR0wACq3l89-WCLRTlEVX7b21y8QC8iCK-Z25CFsCBa6qLPs2p9bARTsTwFBLdzemfwkKSq2m1WHkB3N7DSd9UEl-Zw3zZEyICUiXZYQ3NcLsKeOKpKVziM0jsAVPHKgs78ZMH1MZ7HL-UTZhfJRtaq5cmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه قدرت خرید ۱۰۰هزار واحد پول ایران و امارات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108378" target="_blank">📅 09:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c44921ed.mp4?token=c7WdJLajoYP9_4_lhfTJpgAq4PS5SglPv9ywSnresZV5ikF2DYQyb8OkffNJipf-dATTl3rqXaK86EFDoT8POrNgDpP908vcLh5A8nCpxJVa2z0xRAa4_k94-rLjBXAiFC29hsT7laVcCZGuKkOFbXr-_5rdswZkZvI8ZmBWS5KsboX8LwLPc9P-Up59pwzxNIGzr2DEItNOgxR5swG9cnSPCAgDp4i8wVumP_4HICywiEEYoz7dn_38-bzG2hoo-Bfm9jIqPbMRtFu0xj7IiNy-pKKbvxDxvgfotRbk2NGUSNo9T2pOxY8hDiywd1UFVx5X5IO8g16hsK_RAvwjtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c44921ed.mp4?token=c7WdJLajoYP9_4_lhfTJpgAq4PS5SglPv9ywSnresZV5ikF2DYQyb8OkffNJipf-dATTl3rqXaK86EFDoT8POrNgDpP908vcLh5A8nCpxJVa2z0xRAa4_k94-rLjBXAiFC29hsT7laVcCZGuKkOFbXr-_5rdswZkZvI8ZmBWS5KsboX8LwLPc9P-Up59pwzxNIGzr2DEItNOgxR5swG9cnSPCAgDp4i8wVumP_4HICywiEEYoz7dn_38-bzG2hoo-Bfm9jIqPbMRtFu0xj7IiNy-pKKbvxDxvgfotRbk2NGUSNo9T2pOxY8hDiywd1UFVx5X5IO8g16hsK_RAvwjtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان عصرِ مسی-رونالدو.
💔
😭
شروع عصرِ یامال-اولیسه؟
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108377" target="_blank">📅 09:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6ef29c07.mp4?token=ZaL5v6TNa6T-8GpKEt2W0gmNwLpXsyZKh17mLddHGt60oYj7SQ5E08NqLH9d_8dqSEAA2AH4xzxHp0GBtvYv_cuF7bil4OSSNn_5LfdW84rEA9Z9erTmSW5Ik3gT7UM8RuDEyBe59YhveE1rChuIUfRfzTOcY5VckzeyTFggINcQU4zP_eZaIdzTolZVjSnwQJRJiYxPySM7L0kY9dPnTMDd57hUkqNEohT3KyEe05KricMidRr5vQZEbbGBpmSu1VnDETWbLUehcvBZ-tlRlmBI4LyGIi3YOm_S_ljXiCyV4qfBy5cZKehIiyiOATh6wxLaU99d6boYSY52fh1fGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6ef29c07.mp4?token=ZaL5v6TNa6T-8GpKEt2W0gmNwLpXsyZKh17mLddHGt60oYj7SQ5E08NqLH9d_8dqSEAA2AH4xzxHp0GBtvYv_cuF7bil4OSSNn_5LfdW84rEA9Z9erTmSW5Ik3gT7UM8RuDEyBe59YhveE1rChuIUfRfzTOcY5VckzeyTFggINcQU4zP_eZaIdzTolZVjSnwQJRJiYxPySM7L0kY9dPnTMDd57hUkqNEohT3KyEe05KricMidRr5vQZEbbGBpmSu1VnDETWbLUehcvBZ-tlRlmBI4LyGIi3YOm_S_ljXiCyV4qfBy5cZKehIiyiOATh6wxLaU99d6boYSY52fh1fGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
ویدیو جالب از آرزوی سلامتی کودکان جنوب کشور برای آسانی ستاره استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108376" target="_blank">📅 09:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری شدید پس از بازی دیشب سیتی و لیورپول که با دخالت خشن پلیس همراه شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108375" target="_blank">📅 08:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108374" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdybA1uYWFyDA7scREBeGooXkGHNvisiLLmZ8nEcrC904vpnTYK6xN_raCvVVOfaR5QTqTah1PZQPkCJ2mzhUHq9m26p3rSky9_4UnqUntrS0_i7SJdYFENSVeS7JswrCYqBnflP0M-YSeE5C8tIY0XFtcLpK3OCUY3Q7WGtf4kmIsUYYb0ftcvmH-jrJT38IkR3AWaNS8Tpp5x9MT7C6_w6V7T4WwShU9xByUh6j03OfHGCfZfhUwGL78YAZ8OZQaWnFPBiXW7iSEAw6H1zKqLO6AYuJuav3ICH_KMd94UJOEBg1gXxB6yrOEP8qYgEUY4IGGN0xgjtqFoh25ytqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108373" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108372" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC2-gdODDViucxo4SKcp4dIqJzDAbofZxJJgByxxIKPRDkB8kaM-xzZiAxkvMAIv1mXfIPHVHQNb6OH4T3ul6R4yIdJ4V1ctRvm0oW3pfrlcowd4s_pD0kna_LqzB-8Q95aFNkdJrZMVMOlDr7DYG5nv37kdPHiiPjNj-xYqSwI8neQFx-rATm4oLs5nLUGGoUItSXDM7u_gHoX3gvzIeFRH-sASe1gvm6dWV6nrmQQplz13Wo5zQSf-ucnsigu_2M-StgaqkxsxQSnnN8q_61f_E2DBlHe-P3T4N4i239Qx7BukQpVC3bVwjrHqOguQSlM0L4B6y3OWHVMVJBFUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🇮🇷
📱
استوری یاسر آسانی خطاب به حبیب فرعباسی: داداش رقیبت برات پیدا شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108371" target="_blank">📅 01:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gs6G5qO5nLCSDJe9i2_PJUC72GmXQVq0-XKUcriCRazUzPC1fDsYtBWSc7V6BhvyAl_c5yzzlK2piO92o8ONo5bxFrgR7B2Zcne8Q5ezwvxmSscEoQSwiJJXI3o537wKL-YG7JoG6X-gjlg24bHlQKlRQN7oSHGlvGJhLs5gJKXsqeulg_D8FGHb3H4uCUHGlMg1Tpu9UixJE2Xo_9DQRwu4AK2VpS4uS7SLfo3tdAui25A6SCKLeOwEhfnEv-oOUuCFtypD8JSHaeA38mU5q7XmvO-8StJkJLouIHXCPVfZBojy6psW6Mj-NkrHqvfx3_cvr7kp0qDnkTQ8j_C1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
حجت‌کریمی مدیرعامل تراکتور
: زنوزی با وقت و پولی که برای بیرانوند گذاشت میتونست ۱۰ تا کارخونه جدید بزنه ولی یه آدم بیشعور فکر میکنه همه‌چیز پوله و اینجوری تیم رو به حاشیه میبره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108370" target="_blank">📅 00:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108369">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbIjIY1ENLgPDpXZ8qBfIwevhDkdVyoYpkLmKyJbCyC-J-6XDXuGPC1mutUbiab_uiMeb9dAItqKqiMBooCafZjxKswHQPW5UBqjB769I8BWJAMk4NkGs89ZFhy9Y4uEpO_LFvoEt5SsK6WXlijQFMZaxvJZnkEO5Vor1uWVs1W6s91Gp_XwZgke9QdXUcQWnepD1O0VXU4CLuQb3idY1y5w0_XAkzNZZLF6yETNs_2vkn3kHIlbGFTWzarnhn543HuETnLb3QvmWFY_1vcUdvAeXx94vp9fiktuM6_MoUmG48Ic3G3H50LZZQMy4W2XH9Gd015_HhD_y6YVl8V8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصویری از یاسر‌آسانی در تمرین امشب استقلال پیش از بازی با الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/108369" target="_blank">📅 00:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
⚠️
لحظه اصابت موشک حوثی‌های یمن به ترمینال شماره ۳ فرودگاه ملک خالد ریاض که روز گذشته موجب کشته شدن ۱۳ نفر و زخمی شدن بیش از ۳۰۰ نفر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108368" target="_blank">📅 00:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108367">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/108367" target="_blank">📅 23:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108366" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108365">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt0UC63smuTWm3EtNGDS8Wegy3HIaSZyzvFlSckF_QgFY0ZndKnMjBBJk-JEEQZAN04PHBIm1dLhwwDdClq2ZwE2_HgBGA1sOF0Il4sI545XG7xjyo3ma11pNtkdXFyoKkA8_jSW6ngoTy8-38JsXfx-MMW5towjsQBtQHxSNnkXJOsZ0I-kNxU0kaIGmTZrwBAWIlv4XoJdxj5QP07rbQwzcJcmN5q6Szul0IrUioM3gWjP55dpgb_aVGtMpuzkbIbQ9SE0gtGMpjIJDaLhLbQ7z6w4TVybd20s3_FQx_5HXJGVWzjgNHaivcmRFbq5aRSATDHqIzlBMTy6c2O2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/108365" target="_blank">📅 22:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWFUqu2PVCzE71-8TnPNb8JawlngyLlvU44vc68OEdTAJ9St3ikJzZi5cprhsELBpIdyD07jGtpREReb5pBOAB_lT8ZpI7Lf8Lei3nn8-I6bnZpg4UhtgonF1pVZZqBT5b6xpq6etvN2_ltuLte8l-B_CbxqdJm_9PcFUtw_-4o714RYeECdhWfQV-4aiKuKviVKHuAmJA4gp2U1qRqNV-AnK2dCDi15cqw-6EaYb8xDe3Fpq_eW4gprD45csxGiwhQw11PpEsfUjhXLEKKtSO_keZSx1HW43O2V9VKv06phSVLF6pNAWfZilbmOAkj95LnNvkugw1I2zpHO7z0sYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🇪🇸
🇹🇷
ترکیب بارسا اخرین بار جلو گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/108364" target="_blank">📅 22:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108363">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go4Uk-ZIJolMq067JK0hQYOWpzEGHzCRK2KKBnDJnZpezWTw1XbZ173xhwG5ZfDg9AGl2EBf_XPW6dM7-QXsoeiGBrOaOPz98ChoWyOO5WgDJGBNqfsPccYowC8byetxw2JucPjaWr-Isbw7-6HaEeLo-R7jSwDCop4gJmRYa2e6gkwRXPr4E5bi3Adai_6mhF5Q701nz36cSqIK0uoxtnftI6rrKVKKjt6zD4f11Ham2-x7op-Uyx-mq2Ne9ThH49uk7CsKLh0Rlj7djyUzMCy7yJYdQ3TFRW_hZxhbKGEMNAebEqlSJ5_UWkLotDBf1RBnObnAhNJzxIzH4Qsmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
جدول لالیگا بعد برد امشب بتیس و سقوط رئال‌مادرید به جایگاه چهارم جدول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108363" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108362">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9324bea2.mp4?token=Monkxi20QJx_M8ENnlVLOTjqR0YfRpjQFEPXaax0RYMTDx6c4Q9d2gWGzh7x9LP5jLC99YmvUl1VQ6uH3PKeEHpMQ58R1EwAUA4AxHFU1bwWwSoZ4s8APz-4hPXESTbNfwbU2VSRlHVinIm3ivaKadFb0kuSgHl-dQxbf8couwJDfZf6mSnhIo36hK1R1t6VlcT5mgq7_TlhyAjnJVM24n1PP22U8FLeSB_Y3CIkEGSxvVzQXr_q7BmGsnJdYBBxhUoGpzA2M5RgWj-TUwA65JioqUH1jBGs0nhR5aEz2UiXaksx7aGqYBIDVGOTBfBd3UiJ7nnTk-D9h_5YK3u3nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9324bea2.mp4?token=Monkxi20QJx_M8ENnlVLOTjqR0YfRpjQFEPXaax0RYMTDx6c4Q9d2gWGzh7x9LP5jLC99YmvUl1VQ6uH3PKeEHpMQ58R1EwAUA4AxHFU1bwWwSoZ4s8APz-4hPXESTbNfwbU2VSRlHVinIm3ivaKadFb0kuSgHl-dQxbf8couwJDfZf6mSnhIo36hK1R1t6VlcT5mgq7_TlhyAjnJVM24n1PP22U8FLeSB_Y3CIkEGSxvVzQXr_q7BmGsnJdYBBxhUoGpzA2M5RgWj-TUwA65JioqUH1jBGs0nhR5aEz2UiXaksx7aGqYBIDVGOTBfBd3UiJ7nnTk-D9h_5YK3u3nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
یک پیجی تو اینستا هست کلا یارو با یک بیلبیلک میزنه به مانیتور و نسبت به دروازه‌خالی خراب کردن بازیکنا عکس العمل نشون میده..یک کلامم حرف نمیزنه..انقدرم بامزه انجام میده که میترکی‌ از خنده..خیلی هنرمنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108362" target="_blank">📅 21:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6vZfrhDJ6zvu3h73c_eYk13AagGJTJdVOb0H0voaRbng5JRk7DOPYVHJASNx2lSlnK0GFU1oXHQ_-tdLkyxoGe5yaVpfl9EVO2MHvjlN5vn--DOvLI6sB70kr4J8uRMKzLa5WSdi_kwCwT0PULN3g3BranhxEBeqg5u1J9x71JQ45SuWFX7eBwqWJdm5D1QkcfmNXicZtKV08c_kn3sbz6Lg_9Yhwo_pUXVhkm2QjfLiFpbFlLYDHfRP40sE60IHgHap9EPrLNwyBd5Qh4CIStrY1ACXFTyXUTN364QoquTUJuwafaeDjKLT74CSeyu8l425su849H3kt3Uv0-M-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/108361" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=YOHqop4t_iXA0LfX-XjvPB7ekDzCQv4uATa0GJNT5l43R5K_lxkn1XcGLNx1ihGwtCxslF24B89Gm2VUdsDr_vYQnFDgVnk5jjBK-bdF9bvKZPuJGMVvB1CdVb7aUDorawMUaqNHGMDGRgpUECjLIylsh0Vyf97ezk2x6Ab_PSLk-kVpI51K-hHvHCb9XmD9UZLdYKn0JBtANcCf0gzo5uEc7-2z4Vdg4VQguE_K4PFcmsyyR9tbQAeTpXIfqXkbqKLNKjEMMv_nhsJKvQ2B9v6cnHsptclzHS4dsxaT5apB3CBT_0-z7VLw1kTKwlOt1yqQ5ciZmYsyaEACPcC5s64uqKlBV1vAwgwTtAPaZjD8jCfl2foE-dchwVzISlusOEXiArVbzFs5uPFzgDACrPHwFP2c6DA894WLvWQsO1MEWqAYsQD-Mh1cAY5wFXx8v97VWCdRmalMCm60E21eH-pAMiW39BlblYwyffZ4OR5r3HasVIq03sR6F9gHoZ7tusqsXf8a-gOOCVajcwrzMZkFNNB_8upNLQD_iPg1Otm4iINNdg98cPklIw0CmT7Vf4h9Z096Y5p7fFr2_BEFnwp_MEn7nDYihjbvKdNur922mCOJRCMrByPM9mF4ouP5M4fYPX2MRLMDkd1_ZDM4yxu5325o7z2QlFKc94UPIts" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=YOHqop4t_iXA0LfX-XjvPB7ekDzCQv4uATa0GJNT5l43R5K_lxkn1XcGLNx1ihGwtCxslF24B89Gm2VUdsDr_vYQnFDgVnk5jjBK-bdF9bvKZPuJGMVvB1CdVb7aUDorawMUaqNHGMDGRgpUECjLIylsh0Vyf97ezk2x6Ab_PSLk-kVpI51K-hHvHCb9XmD9UZLdYKn0JBtANcCf0gzo5uEc7-2z4Vdg4VQguE_K4PFcmsyyR9tbQAeTpXIfqXkbqKLNKjEMMv_nhsJKvQ2B9v6cnHsptclzHS4dsxaT5apB3CBT_0-z7VLw1kTKwlOt1yqQ5ciZmYsyaEACPcC5s64uqKlBV1vAwgwTtAPaZjD8jCfl2foE-dchwVzISlusOEXiArVbzFs5uPFzgDACrPHwFP2c6DA894WLvWQsO1MEWqAYsQD-Mh1cAY5wFXx8v97VWCdRmalMCm60E21eH-pAMiW39BlblYwyffZ4OR5r3HasVIq03sR6F9gHoZ7tusqsXf8a-gOOCVajcwrzMZkFNNB_8upNLQD_iPg1Otm4iINNdg98cPklIw0CmT7Vf4h9Z096Y5p7fFr2_BEFnwp_MEn7nDYihjbvKdNur922mCOJRCMrByPM9mF4ouP5M4fYPX2MRLMDkd1_ZDM4yxu5325o7z2QlFKc94UPIts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108360" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=pEUHs6hKaU_YI0G60EUk4tBsuM-NMYyfN9FW_Ayalyp2u_RfuI969n3MxRKJX1xwBwN_CUTCsuxmIllbTRJBD8sHjbCEw1XZwUM4K5sxkGLAeLai7fayIMNAJCnHBlnHlh21BEXgp__BAsyDgfhiTsRtBCg1zvNiQfBDeg-smem-ydQWFPe03bHzy_b788F4Hf8vrfNMw8wKHDyBFMy2BBCNx1KDM06Ks4cjpyqeZpWEnnl71tRzAQS5Y6nu1caEAXJVn-mjgkSBVZ9G6PJOd4XyBDjU7PJjuB3WW3qHp-G_TEehukE8FW9v2PJRQPn6uC0_uVn9TydiXfoojXWU6QdEhtdbgWgnedy4IiCuwMo5ZzTz-6CHEq8V4D2xwRFWSxuJ5PN-orLAXebgKjmeu-vPDrzcxbVdfNjFQnBI3Oe2dO-spoDK4dIrFOVrd-qDRhFkyJaPtbeKhsnMxcMbVPUE6kUwbh22nCrodukZaPWR3ljfDpDzRspPadBdXJiRE0TS8yELKM7aOmDPR-Tuf6kKiHDc4-HLdPMktb2XWu6PMhHy12NzpR_egKMCBJFthd8cALnpBEc7XtBTN2WLKnsrHEDVwVuYAxjHEb6dQtxCZdylUHwaSDRE18Wn20su5roqO0hWDRWUDIs1C-4C4l1tQXGlyfTfKDeA9mdAl44" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=pEUHs6hKaU_YI0G60EUk4tBsuM-NMYyfN9FW_Ayalyp2u_RfuI969n3MxRKJX1xwBwN_CUTCsuxmIllbTRJBD8sHjbCEw1XZwUM4K5sxkGLAeLai7fayIMNAJCnHBlnHlh21BEXgp__BAsyDgfhiTsRtBCg1zvNiQfBDeg-smem-ydQWFPe03bHzy_b788F4Hf8vrfNMw8wKHDyBFMy2BBCNx1KDM06Ks4cjpyqeZpWEnnl71tRzAQS5Y6nu1caEAXJVn-mjgkSBVZ9G6PJOd4XyBDjU7PJjuB3WW3qHp-G_TEehukE8FW9v2PJRQPn6uC0_uVn9TydiXfoojXWU6QdEhtdbgWgnedy4IiCuwMo5ZzTz-6CHEq8V4D2xwRFWSxuJ5PN-orLAXebgKjmeu-vPDrzcxbVdfNjFQnBI3Oe2dO-spoDK4dIrFOVrd-qDRhFkyJaPtbeKhsnMxcMbVPUE6kUwbh22nCrodukZaPWR3ljfDpDzRspPadBdXJiRE0TS8yELKM7aOmDPR-Tuf6kKiHDc4-HLdPMktb2XWu6PMhHy12NzpR_egKMCBJFthd8cALnpBEc7XtBTN2WLKnsrHEDVwVuYAxjHEb6dQtxCZdylUHwaSDRE18Wn20su5roqO0hWDRWUDIs1C-4C4l1tQXGlyfTfKDeA9mdAl44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دوم منچسترسیتی به لیورپول توسط دوکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108359" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108358">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=opO_u_co8IGuMNmnR29WEQAQ_joOWbV0JWbCbDLJOxhuc45WPXpk2gB-thp59O4-SS2q0MdTq862GedFTG952OKFAjZf1__wWeNSn9sy_paLfbBIBAnv5x-drA1Ikt7gcbY72DmJ-PYWdyRn2o8k4lbz5sUTHC1KCt-SwvI03QiK1c0Ywnn8phna1wNnexUDM9dxVGF5l4DsUeIcek6c2_8NrO4GW7YRzVXoI106UGzhWDgSn_IwfLW4o9SCapksnBCHnq0kO9MEKpjbRqXQZTQqYrVhS1RtyRopMvPJGb5i0k4MaSkeNkdasVPEXy0Ms99-pHt88fI98sAMKEUEHQy44Tx2FH899GId8_9EL0uwieDoij9K8JlimhvbAK6Z6bvxi3j2T2R5M7373cw7J16kXYQG0w-bs957ocrAct9eB7fQdK-hpAOgN1EYknKSxxCZkYeQjZgwzV3ExXL6dFjuDG9SaC-Rrnr0Z1LF5AU_feHKFNQ6_53fz-gPBSBtFiwxVhtniLgHegCBLtwdQeuBtoDatHrlOLsEOzsVJxav1quzwgeuyBaFaEk56YTJnZqZmeOy_Y4hFTl_-uhBrsD1uzqFgbe_3Utzkm3i2-rQ5lAXhz2cbZNV-6rNZniTHf_2Q2YoSt5Gy3F_hp_P41_YzOgASu-ImoI5Ot0MRK8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=opO_u_co8IGuMNmnR29WEQAQ_joOWbV0JWbCbDLJOxhuc45WPXpk2gB-thp59O4-SS2q0MdTq862GedFTG952OKFAjZf1__wWeNSn9sy_paLfbBIBAnv5x-drA1Ikt7gcbY72DmJ-PYWdyRn2o8k4lbz5sUTHC1KCt-SwvI03QiK1c0Ywnn8phna1wNnexUDM9dxVGF5l4DsUeIcek6c2_8NrO4GW7YRzVXoI106UGzhWDgSn_IwfLW4o9SCapksnBCHnq0kO9MEKpjbRqXQZTQqYrVhS1RtyRopMvPJGb5i0k4MaSkeNkdasVPEXy0Ms99-pHt88fI98sAMKEUEHQy44Tx2FH899GId8_9EL0uwieDoij9K8JlimhvbAK6Z6bvxi3j2T2R5M7373cw7J16kXYQG0w-bs957ocrAct9eB7fQdK-hpAOgN1EYknKSxxCZkYeQjZgwzV3ExXL6dFjuDG9SaC-Rrnr0Z1LF5AU_feHKFNQ6_53fz-gPBSBtFiwxVhtniLgHegCBLtwdQeuBtoDatHrlOLsEOzsVJxav1quzwgeuyBaFaEk56YTJnZqZmeOy_Y4hFTl_-uhBrsD1uzqFgbe_3Utzkm3i2-rQ5lAXhz2cbZNV-6rNZniTHf_2Q2YoSt5Gy3F_hp_P41_YzOgASu-ImoI5Ot0MRK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به لیورپول توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108358" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108357">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=FxPuj4Z_Za_sQZkQpQx26fZIWhlHy5N24CylWj9MOAbv6_Hm-QM8souzXk_ll__dCCOB3apMqXkJjyggsphot9lMQxqDjTi4whbfy_YhxJX-zv0iMete4Hpg1OTCoTxL-emXr2ESbRQuP5wr9ufGlYWtLuQv-v3QaCvgtGhZacVhK38OjMbREHSewK4GhZtppltIOayvBklPK6VLBdiwGXsgFLtHtZWT_lPcghWHedQ7GYxbw4ZfJ2sdcZ8YokXlEeJa-Ch2b4uIUAggpNIHZIvYYYa1-QV8AFHxqG21EdnBLygR08EPt2bIV0LzSn5bBFUzxTxomx6FhvFcJBdmTr-IkBtnvva10srB7wSBjgR1bcdVFSNz7AFVZBMOpmC4bB3UY689-7TgoSyDahnOAW-laW2IG1Yc5S_7I3uNK68OnwZBt4QcLW-1UbAkAPHKuF763p8_7n5EA5zFqXoYJyfUpMrqB1VOoYzf4x49fElIREnteA3sUyP3Fs93428-NB6NMPxYIjQeOqKhvnxwBDYkrvkdKXmwyspinenY-pnORmF0uxPEyWX8qfSKOq_CV745VDgUbFsHInixeyZBCel8xDJbhsdL-4egKcQfGdM1kKmbrVobgrZQfacXrdOFb2iqQF61k4j94_ymElq_JXtL5-dNHkHvwxhq3fd9wIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=FxPuj4Z_Za_sQZkQpQx26fZIWhlHy5N24CylWj9MOAbv6_Hm-QM8souzXk_ll__dCCOB3apMqXkJjyggsphot9lMQxqDjTi4whbfy_YhxJX-zv0iMete4Hpg1OTCoTxL-emXr2ESbRQuP5wr9ufGlYWtLuQv-v3QaCvgtGhZacVhK38OjMbREHSewK4GhZtppltIOayvBklPK6VLBdiwGXsgFLtHtZWT_lPcghWHedQ7GYxbw4ZfJ2sdcZ8YokXlEeJa-Ch2b4uIUAggpNIHZIvYYYa1-QV8AFHxqG21EdnBLygR08EPt2bIV0LzSn5bBFUzxTxomx6FhvFcJBdmTr-IkBtnvva10srB7wSBjgR1bcdVFSNz7AFVZBMOpmC4bB3UY689-7TgoSyDahnOAW-laW2IG1Yc5S_7I3uNK68OnwZBt4QcLW-1UbAkAPHKuF763p8_7n5EA5zFqXoYJyfUpMrqB1VOoYzf4x49fElIREnteA3sUyP3Fs93428-NB6NMPxYIjQeOqKhvnxwBDYkrvkdKXmwyspinenY-pnORmF0uxPEyWX8qfSKOq_CV745VDgUbFsHInixeyZBCel8xDJbhsdL-4egKcQfGdM1kKmbrVobgrZQfacXrdOFb2iqQF61k4j94_ymElq_JXtL5-dNHkHvwxhq3fd9wIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
دیشب بیچاره شزنی سرش محکم به سقف نیمکت بارسا خورد که همه از خنده پاره شدن. فقط واکنش لاپورتا رو ببینید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108357" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TA_kgtQXDDXlCWENgTzKBrrzZtHv7UfP9o9HPVf9ZtxIzd48wEFLLcRqVBM0vCWmSahWkANbNPP_8Y7sIU2yA7Yg4lxOgvuk4JaS_Qk3AySey_y94a1hM9r3CxPmxQObPdJB98rqXCLjj9_eU8riH2LKrzjDOeCJN-qidnGnF_Lk0ePQj1mnn5qGQVdMCNj4-2G_QuyMoB13dpwUyU8V7fyXowI9FaGwFt99vYrD24zxVO3iTPM7oqfa6ylEDE2fwAceGN0bi2Me3Sy-EQ6J2iZdGA5zIE1g7q0Khnzvw9PuWHnglrIuap1sIzqL4VCMlQdDFU3h-jVx6NA-2setydA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TA_kgtQXDDXlCWENgTzKBrrzZtHv7UfP9o9HPVf9ZtxIzd48wEFLLcRqVBM0vCWmSahWkANbNPP_8Y7sIU2yA7Yg4lxOgvuk4JaS_Qk3AySey_y94a1hM9r3CxPmxQObPdJB98rqXCLjj9_eU8riH2LKrzjDOeCJN-qidnGnF_Lk0ePQj1mnn5qGQVdMCNj4-2G_QuyMoB13dpwUyU8V7fyXowI9FaGwFt99vYrD24zxVO3iTPM7oqfa6ylEDE2fwAceGN0bi2Me3Sy-EQ6J2iZdGA5zIE1g7q0Khnzvw9PuWHnglrIuap1sIzqL4VCMlQdDFU3h-jVx6NA-2setydA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد ربیعی: سرمربی تیم ملی امید نمیشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108356" target="_blank">📅 19:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=Z7BVeFBwKoZwxL1phHYjiKziUwNMCWR6iSyqN2fYGT-cbJr0M9C0azugXn0b7GRSZY-ww4pj813ARt7iDNwUn1WvE5-vlPWXPvcruhdQB4_ojnQwtaGjFmNJOgmIiUG02-qzMvsEIk-q-uOzePoJQUVd6FveTq8vPJ3mK5NfEh5TRThIcmLeXaOQOZWqkqvUm6uo-4_AsOg6QC0TCfON7aEEaUorVIWkLfy27ecljTavLtgXBjoLvGHCazR4cQUTpQIlr4OCMcpuBVxbNu6idfxbgowfEPc3uOr5F8rBL-dZ9cOC4NVYD0VJIFi6Oo5_0ldpSZXB-0i-o92JeD3fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=Z7BVeFBwKoZwxL1phHYjiKziUwNMCWR6iSyqN2fYGT-cbJr0M9C0azugXn0b7GRSZY-ww4pj813ARt7iDNwUn1WvE5-vlPWXPvcruhdQB4_ojnQwtaGjFmNJOgmIiUG02-qzMvsEIk-q-uOzePoJQUVd6FveTq8vPJ3mK5NfEh5TRThIcmLeXaOQOZWqkqvUm6uo-4_AsOg6QC0TCfON7aEEaUorVIWkLfy27ecljTavLtgXBjoLvGHCazR4cQUTpQIlr4OCMcpuBVxbNu6idfxbgowfEPc3uOr5F8rBL-dZ9cOC4NVYD0VJIFi6Oo5_0ldpSZXB-0i-o92JeD3fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رختکن شیاطین‌سرخ بعد بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108355" target="_blank">📅 19:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=pnhdvMHYCnoB8Pec_tgiUGb8hSTRiuTTMdvEpdOcRChPueaaHQpeNQUvDEtBEH2Jdw7bJ417rKVbNgCkjuRrd0kwi-5bGyso192gvUz__vP-J6aGkjanezwgT7Kr6SRBN9ky8SWxfpJK8b2H7qqwoAcLazq7X_gGSQcmlhRqPvdPVUfx7WLx7qCFnijQ2QyWDOnc9i6JpuESg19JHVNUqpmHCyjl8x_rKvC5QAA5DRN5BrXPxeUkfLGx4a4yKXe2COtPS5zvtekxhc-iO5dF2pUm90tqV86Zuh6KhSw8dAMzRHz9SQrY4aJiKVXoUKRRqcRCQ9FjuxJP4Ff_weQTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=pnhdvMHYCnoB8Pec_tgiUGb8hSTRiuTTMdvEpdOcRChPueaaHQpeNQUvDEtBEH2Jdw7bJ417rKVbNgCkjuRrd0kwi-5bGyso192gvUz__vP-J6aGkjanezwgT7Kr6SRBN9ky8SWxfpJK8b2H7qqwoAcLazq7X_gGSQcmlhRqPvdPVUfx7WLx7qCFnijQ2QyWDOnc9i6JpuESg19JHVNUqpmHCyjl8x_rKvC5QAA5DRN5BrXPxeUkfLGx4a4yKXe2COtPS5zvtekxhc-iO5dF2pUm90tqV86Zuh6KhSw8dAMzRHz9SQrY4aJiKVXoUKRRqcRCQ9FjuxJP4Ff_weQTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
بارسا با 9 برد از 9 بازی به دیدار مقابل گالاتاسرای رسید.
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108354" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
ترویج گل‌زدن در صداوسیما و مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108353" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfOXqzUw91FF_EqHK41fFB7cPRfJ_zzReUZuJwU9Jqa9TkJ0zDm8JTHFL2Q4KD9r3vv5d9jgtJt4Dig7bgZ7pTqbzgoBiOrJ7-FW1FUpUDQdqJ4iKdWrYg7nNurKrgwwS-SsXr9pQnK_uhBmbvSWOvWORyidEHU1hDJk74_D8JG5h5i4OKFAAi9IQqaEVOIchwIF1Xftgi5GwcijXuIAIQxeIxozRyyjTOjBUSSk6L0aMVO-WnDyMDApZAT00__5rUN0P_zioO-WYWeKQGKxOW5Pib01yBqdG6HcZdAYqZWyIharCnnaGdZUfq6VRgwsqf2_eUUHcIoWLWHAcfohgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلارنس‌سیدورف از شاهکارهای مدیریتی تاجرنیا که به مدت چند ماه بدون هیچ کاری چند میلیون یورو از استقلال دریافت کرد و از ایران رفت، سرمربی کورنتیانس برزیل شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108352" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ama7bq0lrPW9JuiUqvZI-wp-GzHyxdpz0nwdDtQvICJnALNN3hqh4Wmv8wreHIKqc8iLfgERbKbTPTT5BG3JVy2Z3F3x_eXzjpjx0YiB0Ha_k20FmG3VP1OIDn_B3AFAUB-T6XJ5NLm3Wbg07qvCeNrLMC6eIadIa9APBK-0e1xKMLpK6_qqKjgbECcSUN-2ia1GaiT5wLX0y_sftp_xCRE3j2UPVuHm3jy3hLdZluXOSL9qW5hyfWjqIRIxEIzNzZZC8SZaBi7mA20pvq7SxSIvIn29vIMpb6qOFRG2-bzryMXAPADjxX-KbfGCImzykC63PtITmodjeEKSPbZe0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dycTM182M22NosPTGdsihTR4-EJpRY8PehXijmS3y1YTUST6GwFfCTsoxw1tye43R-PrRUArwAk1NanslJyjlfGW-Qeij6AqkibbbUP-pbrKlBpMJ3fRz0qFswdfUoT3e0ofX1VdAU8NlyB6N1qKhctuW-ngaewdULjcBeYinhTl7E2hF090rwidkSNSda_hy7566E5QKWJv4ADmhwmk9SAIBATWHg4leth3vcTK8YhOt68fCoe56k7ZRq9nmSdOdrDTE_VAwPKySEzfRhiJVVwP_MVSSIe3nGAXequQmAVqMxuOrtmxQqDIi9ARkYuQRhd0JgwR8lybguIc7Z_4SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچسترسیتی و لیورپول
⌛
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108350" target="_blank">📅 18:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT5tgwsdIfMHhHwBxpC1AStiRdRUKHEDcdfkak4ECEC4VbSNTVbgWatRL1ZNIc9zFnlzJftkrPWU0RA0ALOZrFqS7aGiFgcQRL7CvkVEJrA3zjD7Xj2piSPSCcrOF5xpiZAD8jgqArOZWb5dhKD_LYQ_5DCnlQISfmv-55x3Sj5BucAyl_UmfwM0h1QT4crJpvaMbr3Bf8RMS84SliL_Jf9fgN_PMuoZagDbKBDEDv8DlCF44zekMtQAMgs0GVXWhfrOJkG_NkIt1jKVDeAU_8VZpvmZnKuFxPbaI4OP_o_tU468YjNyPwTDIzPw8x2-1KasOv_N6yFeAgnz4XhdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیر سفر گل‌گهر از سیرجان تا بحرین را مشاهده می‌کنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108349" target="_blank">📅 17:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=GCqdc6Onv3YoI6Dlcbapg6_KsuKqE7fo4LZUaooM9cjMFUiibNSW_YBWRgkzW3BGxCXorSBF1YgGbB2c8ne68R_V5L6OCGvxMUShjP61hyeD_3dszHcYRg1dnt0yHY1FLkfvJkwoLceIGG3Xs43iBc5WfEtzWbwZfBeHU1gmDGq34hc5yrBfsH2hfuZocGFH1zIysuZzGqNoSqT2YdsfK_3nEYZdrbd4BPmoF2t9HSl3GbEtVDhNHkeVO9vh0YZOd9WzXvPzPOzxmtXn5AbafPdetARkpRfwFfGp7pbIHfwHFyK1SqAmBrdZlKMCfs_QbRbi5yEUhZy2sP6neozprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=GCqdc6Onv3YoI6Dlcbapg6_KsuKqE7fo4LZUaooM9cjMFUiibNSW_YBWRgkzW3BGxCXorSBF1YgGbB2c8ne68R_V5L6OCGvxMUShjP61hyeD_3dszHcYRg1dnt0yHY1FLkfvJkwoLceIGG3Xs43iBc5WfEtzWbwZfBeHU1gmDGq34hc5yrBfsH2hfuZocGFH1zIysuZzGqNoSqT2YdsfK_3nEYZdrbd4BPmoF2t9HSl3GbEtVDhNHkeVO9vh0YZOd9WzXvPzPOzxmtXn5AbafPdetARkpRfwFfGp7pbIHfwHFyK1SqAmBrdZlKMCfs_QbRbi5yEUhZy2sP6neozprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب خیلی جدی ادای آخوندارو درآورد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108348" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108347" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108347" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFm_ymk-SXG1f1e0fJuXwCLnsXuSzaUpm8rHYgZ_2UWMDSrmfOdSHnf7qkeP6YBCd2HrWU1xov3ph1i6Pw7MIlSdDZavArAeaZ4L1pawix5rspvOWaTzzPLO6SLU01e6L3rHx_aZGOBJSs8Be4PVCt3NsoHkVOrnD3J8rvgwx7oZDvruwm5DuXJcA8K7BcRWaWgSzrAJ4-PIete5P5cE8H2MNyQn21qeCRXbHe7zhUSmFpCOrT_7Q1hEFMtMr7yy2dyux30cqEjHIGNmxcpMH-Sak6prlTOq0Vgt5uGIRyaw-IUtoBtk_eIeZmsvmW8UVDD78Ld9BXFJWzm8VZ0NoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108346" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=jVfzmInEsl0cHf9i76LOr-yCLnpJimezDcJJQsz8N8A0D8xfB1nxIche7Jxu2vJmXOGnaIpE_z-0UXD5LIoZ3J8g5HgZJxDQRwFkBGAolgoUxYoci9FHYiXEQRrS5kOcamFLiWqU4DrkBK7cb7xKZiOUmSByQKMBz0fhGTbus8Lt7Cdf3pqioRiz-Z8fTtCh5PMgHD00UxWIMoJoLraAmgf504n_P-7Wga_jYbTCyVH9GHzDlObJiUTx8lP6UBuk1F9Np_KKUJB_vNF5rzy5f7ogddnWZjRRviX5juP7IYRD4QoPthgsEGocHEHbrPRcHdR8G9yvgV76VEKYL9dx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=jVfzmInEsl0cHf9i76LOr-yCLnpJimezDcJJQsz8N8A0D8xfB1nxIche7Jxu2vJmXOGnaIpE_z-0UXD5LIoZ3J8g5HgZJxDQRwFkBGAolgoUxYoci9FHYiXEQRrS5kOcamFLiWqU4DrkBK7cb7xKZiOUmSByQKMBz0fhGTbus8Lt7Cdf3pqioRiz-Z8fTtCh5PMgHD00UxWIMoJoLraAmgf504n_P-7Wga_jYbTCyVH9GHzDlObJiUTx8lP6UBuk1F9Np_KKUJB_vNF5rzy5f7ogddnWZjRRviX5juP7IYRD4QoPthgsEGocHEHbrPRcHdR8G9yvgV76VEKYL9dx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس سمی عروسی گرفتن مسعود شصتچی در قسمت جدید مرد سه‌هزارچهره
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108345" target="_blank">📅 17:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842c49b387.mp4?token=DaS_AJkER7-ij_fy1fmFr7bvldymDNqMu1vgqfebvx_qrzvuc9uTLA-llf3R9lVEx1rYs0j3Y7axKJT7liZs96eJhJ1KXVN1a66ONyZnIzJDtCJF5j4aPv5OpYJdVn2JoarrmPiwt1oJ94WNlrf8tYSmfu6Nd_knrY750RIm5u4Q6Gz8djdtrmkX5kbDNas8Uhx7pj10F8pUSEP-oc15Ys_iA-EHMdbcgtpjoMmfhMf5ln4kC0oWtZrWj8FIN_IhutZSuOKKpLs4bAbFQ3JaEcbzMsTexWsdJThP9JyR56C9Rt9ewSTSu3rcxks2Pzer-49IwsX0SZ2Pv_bIXdUuAXnFm4GXeJ5qCUXgo0exM99haggGNfHnpCtKg6glyYS6g4P3MWmqi9TJWOD1bY5ZzEyXZJtR3p5SmPELlcutgCPON5_YJ8A7YvKmhySDF9ggCq7MabLvMPQB-nm74S4cBQUNFAZCmWutQlVnqcZH8AOkwTmdC2lD_E2Ofzg8L6eoX7AHhr-FlECi6PObqy4bwhydHPTM6VOQ1X8zV6pZp-iSiQmhbHJNPvj3Xeld4TNdOutKZ8zLle5Q5m323HtejtnY7OiSsywbpC9vdb7Hz0WTogKBAgdUawWssV0xsePxBIeZIlxLafhkZkojglJoX0BhGtks-u8GrdUwlif1cT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842c49b387.mp4?token=DaS_AJkER7-ij_fy1fmFr7bvldymDNqMu1vgqfebvx_qrzvuc9uTLA-llf3R9lVEx1rYs0j3Y7axKJT7liZs96eJhJ1KXVN1a66ONyZnIzJDtCJF5j4aPv5OpYJdVn2JoarrmPiwt1oJ94WNlrf8tYSmfu6Nd_knrY750RIm5u4Q6Gz8djdtrmkX5kbDNas8Uhx7pj10F8pUSEP-oc15Ys_iA-EHMdbcgtpjoMmfhMf5ln4kC0oWtZrWj8FIN_IhutZSuOKKpLs4bAbFQ3JaEcbzMsTexWsdJThP9JyR56C9Rt9ewSTSu3rcxks2Pzer-49IwsX0SZ2Pv_bIXdUuAXnFm4GXeJ5qCUXgo0exM99haggGNfHnpCtKg6glyYS6g4P3MWmqi9TJWOD1bY5ZzEyXZJtR3p5SmPELlcutgCPON5_YJ8A7YvKmhySDF9ggCq7MabLvMPQB-nm74S4cBQUNFAZCmWutQlVnqcZH8AOkwTmdC2lD_E2Ofzg8L6eoX7AHhr-FlECi6PObqy4bwhydHPTM6VOQ1X8zV6pZp-iSiQmhbHJNPvj3Xeld4TNdOutKZ8zLle5Q5m323HtejtnY7OiSsywbpC9vdb7Hz0WTogKBAgdUawWssV0xsePxBIeZIlxLafhkZkojglJoX0BhGtks-u8GrdUwlif1cT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
رونالدو این‌روزها کلا اعصاب و حوصله نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108344" target="_blank">📅 16:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwanXk8YFW8CEC917Sci2C_RiTucdnB85Gbm9RDB1XqHqaI19dTHqWZO5LVDJkmEKI8SQXovuwsz5oxEFr6TZhauEWFAi4Qc6-8jFBiQ_yCdgkqPzjh85hyxjL0SM3KaDMcFrC4lbZM0E5mJ8B-24mhy3hMkCoAOGKE7-0FYqUauzpfEp8FHFDONAGq9yND4JopnGv4pCkIF3LsjK66FOgtzWte9_j9Eh0HEiynKW4qKF8Yk0IDZEkqaqss7u-4Xlg_0rQyB0JzUUchrvgx4sojc0NVMC8KpRpSObtYMxOfoglgT-exfWPtMLAFf7uQhK3m_Fot1HLf8i6rMY-SDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
با اصرار یاسر‌آسانی، پزشکان استقلال تا ساعاتی‌دیگر تست پزشکی از این بازیکن خواهد گرفت و در صورت بهبود نسبی امکان حضور کوتاه مدت مقابل الغرافه وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108343" target="_blank">📅 15:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTQycDxqaQPpx8c39gjEJ-9pQOuzm2IS1-mSmyrLKI2jRJOnP20JokUJNWaU3W7MhYiL6i8RcYmugJmXpMd344q977Z_jt_0igch5C4043FSoQLGMGiJieCYz1L_Tw7ktMjYfapoOWxrYmk9hw2OXq3yEZZ4Mez7YVTX4Lzx3zx9jk4mLiVycC9xTvuuSoh1aSHWO9SZttKaB6UvsgvsrTb0Ho31y1zHXjL4nrcfIuBC1GCUp1Benyrv2HZLzs20vc50aIzpUPQzlO3AQUZ3bs1KJp-7xPiymUF2LEU_e-VyDTy-FBnrYafoibf2PVLyyWozwZ0x_gC9sjYeYofAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108342" target="_blank">📅 15:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-stbdE6AnHip7ymhWzdPs4j-VHltqpozj9aTMnu42nN4b_TATNdBKkeu5YeVLIfsY84IyTwFuLSz7tBFe2eZaWGIEDJMsButr7qrutNFVw_6dAoswB-3eEgo0d6fcnivwy6gkO5hGD6sdt64n83bjoKAosBYQp9M1k6zfRWD-H7ChhkzH4s-zU9Fp1bmcevS5zbh2_hgHaZI4d7707YqYtEeRGs2udOPq1jLcoqxikYSyXq3mtkc-TaSaoXgj2lAtwurf-OYeNR4YiIUHpMznanscyDlH9mrdQvNI5O6SxGY7ZowrGAYmGtuLtPZb7-Wt_3X4T8s8ijF3UcSwbshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آمار تقابل‌های رو در رو لیورپول و منچستر سیتی در طول تاریخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
110 برد لیورپول
🤝
58 مساوی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108341" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=ZlvzaId32VED-AUWic4WcxswB16x29kVs15N357rHRtWA7-hHZBEwOv8IHkeGj2ial3Ln4gEbETiUFev65LdQj-eNnHiXnYxmIjg6KkvKs0O4Hd7HmMppy-rNyUnRjIw6LYPgA4noeeCGjzufdIDmhvqt2q4IP1nijIwwn6wzIwLX2TnwZflniuVJTgCiRs2ouoFvzwdi6E0tX9rqko0Tt8zhG4scYVqFbROZmR_iM8X3mDCLnIUKgxTaJD3GVGybfpAFb-2y3hfTKJVdU5BzKPmHduN6s1h0bVm8W348NlfzmiQbO7hQcZ6mSQVN1Kazxp9zJubIeqvAdKEankwwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=ZlvzaId32VED-AUWic4WcxswB16x29kVs15N357rHRtWA7-hHZBEwOv8IHkeGj2ial3Ln4gEbETiUFev65LdQj-eNnHiXnYxmIjg6KkvKs0O4Hd7HmMppy-rNyUnRjIw6LYPgA4noeeCGjzufdIDmhvqt2q4IP1nijIwwn6wzIwLX2TnwZflniuVJTgCiRs2ouoFvzwdi6E0tX9rqko0Tt8zhG4scYVqFbROZmR_iM8X3mDCLnIUKgxTaJD3GVGybfpAFb-2y3hfTKJVdU5BzKPmHduN6s1h0bVm8W348NlfzmiQbO7hQcZ6mSQVN1Kazxp9zJubIeqvAdKEankwwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش مهدی توتونچی به مصاحبه علیرضا بیرانوند پس از بازی با استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108340" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=hKHKGrdIhwDTtBTw3oaOS3Zs376_PYveu0cfJdL8qkMXvs923OHEgoQhBsNQUJjToDle4BTp2IgwrHLK7Riy_LGqyqU5Aq_oM4Q54Sh5qvV0gh9lzr2dL31eZ8lncn9v9avZx7WT_eNyZEHrbzZf3biFcqMh8_5ITwtqP2anE_Yv8XsBa442vTfzsNj-jfAxq9Mq-sU20YyNI0TcjyCSrGptoAl2MrPEB68cqx8k88Lj0EdmS6mrnbXpleHdtJNcLb6i-P_JNOMmM6S2J5fbMKvrgdGhbDGCjsFQsfzQkGpOoFukG8Xou2lPAlTRMxjDhLjHZzLRQjUksOnZaBxTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=hKHKGrdIhwDTtBTw3oaOS3Zs376_PYveu0cfJdL8qkMXvs923OHEgoQhBsNQUJjToDle4BTp2IgwrHLK7Riy_LGqyqU5Aq_oM4Q54Sh5qvV0gh9lzr2dL31eZ8lncn9v9avZx7WT_eNyZEHrbzZf3biFcqMh8_5ITwtqP2anE_Yv8XsBa442vTfzsNj-jfAxq9Mq-sU20YyNI0TcjyCSrGptoAl2MrPEB68cqx8k88Lj0EdmS6mrnbXpleHdtJNcLb6i-P_JNOMmM6S2J5fbMKvrgdGhbDGCjsFQsfzQkGpOoFukG8Xou2lPAlTRMxjDhLjHZzLRQjUksOnZaBxTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه‌سنگین ابوطالب‌حسینی به ژوله
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108339" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=tB8Lw8TPY2cTkn_N0PdCjhdWLjzIXCMiuygDRmdB2aZ_DI3SpjRM_2k5i6gJkQF3TXRMcSJoRFXhKPkaf4wlHbwAqogIIk0NsiAzrUj5oSSJL-oeIv9m7DMEla285u2VcN83OlzCyYwdAeuB104Z4Z44WCjA-sBQ8WK7NSs7edFgsL4OBLeQsoEWp1khPa5GaJvlGNQucRTd-Fwbs8F2fxj8GJMgOHrd7yQiIbNDH1mxeIWH3hrsOJVpE-KAsPq3-gbYwa3i7ROLiyZuOdy7VDxtLtNzaMWDyrvRUgT6rV2uXh5RcE9Aq0PZ-ijCG_OqHNLi53F7boLYjGi4A3sSbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=tB8Lw8TPY2cTkn_N0PdCjhdWLjzIXCMiuygDRmdB2aZ_DI3SpjRM_2k5i6gJkQF3TXRMcSJoRFXhKPkaf4wlHbwAqogIIk0NsiAzrUj5oSSJL-oeIv9m7DMEla285u2VcN83OlzCyYwdAeuB104Z4Z44WCjA-sBQ8WK7NSs7edFgsL4OBLeQsoEWp1khPa5GaJvlGNQucRTd-Fwbs8F2fxj8GJMgOHrd7yQiIbNDH1mxeIWH3hrsOJVpE-KAsPq3-gbYwa3i7ROLiyZuOdy7VDxtLtNzaMWDyrvRUgT6rV2uXh5RcE9Aq0PZ-ijCG_OqHNLi53F7boLYjGi4A3sSbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
واکنش گلزار به ساخت کلیپ‌های هوش مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108338" target="_blank">📅 13:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108337">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXeB2tzKyyJyx4E9QchBir3tR_lhgSfBa-IWgESt2RffS8U2CrmABvu3toS9Pwi3hla_lpaaOPtE63fLbkkQqgk69ut9CRy0Aio4Qz0YpBZA0rFg4G-MzovaCzALCeipSlKt9B4JokyB2oiRs53eDc7Bx-EimGsORUhYu3DRoFhSN32vDpKgeJfZHk6DGfoM-HNMiHuVjKtqy0A3XEaET-nzF3IbZQ-yTx5PMLmKmMX7KVxVzvfSc0_lMxY_oR0Sd0RWD4Z4lO5l7jqTxEaCpAhg5Rc0LtFkELAkg2kweTJab75k0Z6mAhXZVrIhvgAxkbEAUAGaXpEO1AVfK2tZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر باشگاه استقلال ایران برای بازی الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108337" target="_blank">📅 13:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108336">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=H820Ge4lf5oNmL1FFBcf_aIXTxleVCwBr2ujoLEZ0MtGOSQH5kcx9LZZrSxZoTRPHu9tBPJJ1Gc9I92sP5_zl0gGv_wM3ijtfdMot7r8xiQoJAX3Rml-fvUDxL0i_BENr6pKhI7lYLbVc6Qn2vsIJQ73kljQzMMZN0tQUySgGul1xfRRMx0NS4yt2Y8qwZVGTuHUXTXiq9svH8NBeeNtZbeueV_8pzR4xfEyXUP40EkhhZmedvgt4GM-6sYCPEfWwQ5LRSjf0TP9v2_Q6xdhsW4QlkMb7Ze4eeXyir5fJmAXym7mgI1FnCWWF_zOtflpXRAK9selCVbZNjrTIufMAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=H820Ge4lf5oNmL1FFBcf_aIXTxleVCwBr2ujoLEZ0MtGOSQH5kcx9LZZrSxZoTRPHu9tBPJJ1Gc9I92sP5_zl0gGv_wM3ijtfdMot7r8xiQoJAX3Rml-fvUDxL0i_BENr6pKhI7lYLbVc6Qn2vsIJQ73kljQzMMZN0tQUySgGul1xfRRMx0NS4yt2Y8qwZVGTuHUXTXiq9svH8NBeeNtZbeueV_8pzR4xfEyXUP40EkhhZmedvgt4GM-6sYCPEfWwQ5LRSjf0TP9v2_Q6xdhsW4QlkMb7Ze4eeXyir5fJmAXym7mgI1FnCWWF_zOtflpXRAK9selCVbZNjrTIufMAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تذکر تند رضا گلزار به قیاسی درباره ایرج طهماسب؛ گلزار با تاکید بر جایگاه طهماسب به‌عنوان یکی از چهره‌های باسابقه و پیشکسوت سینما، از نحوه صحبت قیاسی درباره او انتقاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108336" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108335">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=Of8UiEc5fVf1sY9MzXmo2USheD8UQJ6GMehL8ze414E69oNW-skjQWYdl7SedNy4fjSjBVPKSQ5oTLPE7I4oo-EuJ2PhpY0EOQc_Hs-cmEUvBGDuXI_EdKOutKAoKJ80vHVoUfsPhdVVL_fsTiz7Mj16NClDPbXyHSv1ywzmiJ9B5qwW8chv9T7ep090nHyorX7D7LI9NHFKQQmrhavSP6fRHM3rxlE1gt3an06mKCr-maWzRrA8tPhGfnrhKcnszUkylGwu78iYA47xR4Ylf9TkpsOL03fllhLcNfau2QtCMIUYozJS6ns5nkS-4npdXsalNOhKHYm8DwuEFAkL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=Of8UiEc5fVf1sY9MzXmo2USheD8UQJ6GMehL8ze414E69oNW-skjQWYdl7SedNy4fjSjBVPKSQ5oTLPE7I4oo-EuJ2PhpY0EOQc_Hs-cmEUvBGDuXI_EdKOutKAoKJ80vHVoUfsPhdVVL_fsTiz7Mj16NClDPbXyHSv1ywzmiJ9B5qwW8chv9T7ep090nHyorX7D7LI9NHFKQQmrhavSP6fRHM3rxlE1gt3an06mKCr-maWzRrA8tPhGfnrhKcnszUkylGwu78iYA47xR4Ylf9TkpsOL03fllhLcNfau2QtCMIUYozJS6ns5nkS-4npdXsalNOhKHYm8DwuEFAkL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینی داشت به فوتبال برمیگشت که ناگهان ...
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108335" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108334">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1QfR-hEq-4H28daNVlYUdNrBjNz2lbeOgPQu81UgbJjjbMabV3_ocg5SqNgpsswZz1QgYYChSsSg70v9ku8OBSNtA6kBTIqCyZFDy-GbgCOiZtYGkU7j2Ld3bl7b-oFg78Vo9fnAq-Yp0qBh6CWu97L3yzOndRNSbaBoC2HT4nSBZ6SQcspznd9pBPNnhYs0Apa_rwsgk16_HPs1NojXA7dgvdBcSoR_uIjDXO_NuF3q-FW3CoJLzgZimXd57WYeNJ9il9IBoicJatALfXjts9tzo4IwON-dUFlvJvLx6uQBsEPVud5mE4flI3C5FBliTJ_uYhQ5D9jhphqZYJygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108334" target="_blank">📅 12:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108333">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پشت پرده دستگیری مهدی طارمی و سروش رفیعی در جاده شمال؛ رویانیان ۱۲ شب به داد فوتبالیست های معروف رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108333" target="_blank">📅 12:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108332">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=hwIHa0c5EyC0bpN_GyP9BG-XoxMbUD2TTISLIHZJyX3DbdosUkSpbrlU6OGxWP35x320yNWLPuOOE8YHPxhJyrUX2FtjKS2n7IET3yu65LDZ3AAeTU4p4yEF6Mz4sQjcee3pHkNhPj2QpzL9Ee6aPjKwEWSaZ0FxGBXznrXLC3EBGgzZmKsnT1PNwCcorronbjssJVwTcMOeV8EUJFJFxPQOK9c_3LyQlJgGEDnji1N9fF-hB3ehoWtLTDfPNkc8BRL5kegNyC59k1tFdG_Ui0yvQ7AAS9ZrXkxbw7-4qVAvtqgLC9SMDQJHgsWxJyrQeljlYN7smcRTfdJEs8Z9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=hwIHa0c5EyC0bpN_GyP9BG-XoxMbUD2TTISLIHZJyX3DbdosUkSpbrlU6OGxWP35x320yNWLPuOOE8YHPxhJyrUX2FtjKS2n7IET3yu65LDZ3AAeTU4p4yEF6Mz4sQjcee3pHkNhPj2QpzL9Ee6aPjKwEWSaZ0FxGBXznrXLC3EBGgzZmKsnT1PNwCcorronbjssJVwTcMOeV8EUJFJFxPQOK9c_3LyQlJgGEDnji1N9fF-hB3ehoWtLTDfPNkc8BRL5kegNyC59k1tFdG_Ui0yvQ7AAS9ZrXkxbw7-4qVAvtqgLC9SMDQJHgsWxJyrQeljlYN7smcRTfdJEs8Z9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108332" target="_blank">📅 12:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108331">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=dROHUh2Ia7p-aiN5fjMKscoqxpWx8Dx_vaTson-nF4GpLH3-Jvrz-_6Y2QFryPOeGBMx1hAXXuKmTZZH97FcRuwmVDTV-rfW7oUYA5q83XgxYc-WbYEO4KxYJ7TkWWg7SWBi3g2sE7Soi1h9j6iD2IatwUTEptrnVt09dPWW-i6sF5_c9KLAjVhSQFiJHbNFKV4o6xxkTaTb7eVcU1C28EttMikI7Bs4lBDIxxixwyyAXve6pdFEKmFolD2KI7w0-lH0AIfxSZ7CIm6QKf4azvfhbLG4Mx1jsQcs0NnHIXSmSNG3Ss9Oyst5IwrixLvCs5VhJBLbn_mmEma-aYAgbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=dROHUh2Ia7p-aiN5fjMKscoqxpWx8Dx_vaTson-nF4GpLH3-Jvrz-_6Y2QFryPOeGBMx1hAXXuKmTZZH97FcRuwmVDTV-rfW7oUYA5q83XgxYc-WbYEO4KxYJ7TkWWg7SWBi3g2sE7Soi1h9j6iD2IatwUTEptrnVt09dPWW-i6sF5_c9KLAjVhSQFiJHbNFKV4o6xxkTaTb7eVcU1C28EttMikI7Bs4lBDIxxixwyyAXve6pdFEKmFolD2KI7w0-lH0AIfxSZ7CIm6QKf4azvfhbLG4Mx1jsQcs0NnHIXSmSNG3Ss9Oyst5IwrixLvCs5VhJBLbn_mmEma-aYAgbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای کروس کجایی؟ رئال مادرید بعد از رفتنت دیگه پادشاهی نکرد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108331" target="_blank">📅 11:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108330">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=V8V9wuLEpA9aZBbdwllDnWZcuJKanrwCduVRh3DKLc5d05_XAWhfgAS-cXkidR9X64TJRTsqtFk0DOr5CyGJimLBQgxDmgV9kQFKHD-UA4jmLmvWGJsiS9xuHLM-Ob6T3WbZAvzgEeYWFpqoYvpkqGqF_DQWhf8zMJ6oVTU2vJUyiu7Q8zzqlI8jsLRN0vgSNxInER6wUmXEUihgURqe3baVD1-0gDWW4hhzER4MgkmS4YpihhhcBCDLnWdqo-ccmfVnGx-xr0nUgP3pxCA8-sNNKDb5cf20Ad2OOhw5jAX1LmnfE7HrtJI9LZJLRR19msQwAd4P5FECUzU1RHOmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=V8V9wuLEpA9aZBbdwllDnWZcuJKanrwCduVRh3DKLc5d05_XAWhfgAS-cXkidR9X64TJRTsqtFk0DOr5CyGJimLBQgxDmgV9kQFKHD-UA4jmLmvWGJsiS9xuHLM-Ob6T3WbZAvzgEeYWFpqoYvpkqGqF_DQWhf8zMJ6oVTU2vJUyiu7Q8zzqlI8jsLRN0vgSNxInER6wUmXEUihgURqe3baVD1-0gDWW4hhzER4MgkmS4YpihhhcBCDLnWdqo-ccmfVnGx-xr0nUgP3pxCA8-sNNKDb5cf20Ad2OOhw5jAX1LmnfE7HrtJI9LZJLRR19msQwAd4P5FECUzU1RHOmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ختم چالش رو اعلام میکنم
🦦
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108330" target="_blank">📅 11:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108329">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=UsjhRb7BLsMcFTTvtau9iq7BBbMyn37nlG2dw_bHKQawnvWhkd4gH6vn7oQ3LD78R5FkwXUTBmxBjSgH05SxIAlTVMGx7VpoqIUb5Uam_5YLA7ctWvUm_Vy7buZQN-zS6h2EciKYRROAJ6mrSsJIqs8KNIT0Wi9DdQVJjQbH1glsPY5Bt6KjcaUcf7l6pAOTx2DYgmgAJXwbOWEtPjpHmYjdBBV0MkGinwoUnPPKN9IA1aRyyNKYm8Hi48tlfw-69BkNXREG9PyX3qLjY07qqlM860HtK0UkwC8UiK4IsIlWhtYcR3Sfpxt7LroXs6LEsJN4QHIRckRgc6jpYI_iAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=UsjhRb7BLsMcFTTvtau9iq7BBbMyn37nlG2dw_bHKQawnvWhkd4gH6vn7oQ3LD78R5FkwXUTBmxBjSgH05SxIAlTVMGx7VpoqIUb5Uam_5YLA7ctWvUm_Vy7buZQN-zS6h2EciKYRROAJ6mrSsJIqs8KNIT0Wi9DdQVJjQbH1glsPY5Bt6KjcaUcf7l6pAOTx2DYgmgAJXwbOWEtPjpHmYjdBBV0MkGinwoUnPPKN9IA1aRyyNKYm8Hi48tlfw-69BkNXREG9PyX3qLjY07qqlM860HtK0UkwC8UiK4IsIlWhtYcR3Sfpxt7LroXs6LEsJN4QHIRckRgc6jpYI_iAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جادوی دیشب اسطوره لیونل‌مسی در اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108329" target="_blank">📅 11:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=HWa5eZwqUhea5D4MUlAoxrYQv122FpMARAlZaY-roI7TgB4nZRA1_lcKn5tK15aHf4L-E3paolP7RL7WYv2Ro0LAAcRFRJeT6G23NYIHOKB7tLiRxFdsH_-ic3onVsDECdVtzYXYlwVVlgicprC1cqiDt7ahxrDuzq1G5stc0tLn6GFL-FsKmgnqW_Bx-FAqDD1hb2ym4xTYBCXrf8vghFb51rT_hfCAG8DM7NgHWp4bVb0Af2PmYsX-V719wMBOZfjg82C8hNnFi4jd0KC8dCsthxxIHk2_ZmVIlGr1kf8fVsBj_iCUW9d8poS8l6vpiC2UewODKbGM0Cbf-YOBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=HWa5eZwqUhea5D4MUlAoxrYQv122FpMARAlZaY-roI7TgB4nZRA1_lcKn5tK15aHf4L-E3paolP7RL7WYv2Ro0LAAcRFRJeT6G23NYIHOKB7tLiRxFdsH_-ic3onVsDECdVtzYXYlwVVlgicprC1cqiDt7ahxrDuzq1G5stc0tLn6GFL-FsKmgnqW_Bx-FAqDD1hb2ym4xTYBCXrf8vghFb51rT_hfCAG8DM7NgHWp4bVb0Af2PmYsX-V719wMBOZfjg82C8hNnFi4jd0KC8dCsthxxIHk2_ZmVIlGr1kf8fVsBj_iCUW9d8poS8l6vpiC2UewODKbGM0Cbf-YOBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل یک فوتبال
❤️
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108328" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108327">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108327" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108326">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4sbStShXeoXG-kaGaVS8cA6CoN7jfzhCTonrsnQdurXRct37Qe7deXhYfZllQ5TpGrXrFWD7BdACEp8qXkNPWaBj1OEGKNCRlL3Q2614rJb9fQnyosfZDwzvI9BKqp6sNy_FUF8yMS5spYBpsnKz80Nx2-s02GRvUn4eakC9Lt_hkphQAyOo4b_VZKLJpt7he8remqoOw6CPxM8EEhAHgo20DedIEB3fNyHp-uc5-0aATY-OerGFbPW-Q9XbMg5EWIejqz8r9BICTnoBNK3f0d8gjcRvtKnXE3Mr5r8xdtySTsSbwFEcDCyuIDmIIuyP0WxxSGOUFFiuea0v1buRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108326" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108325">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5qHobXiwArahrVkYBxbSccMrRwYrVhfFOOcjAzkt8ZoDd4CYCiTXvzwqalAh_VT2BgDQVGdgZ8FICk7o5ve5O1w6kpnJ_hWbpxbCyeDH0xzW_vHZABZ6shHRtoJcqer-OK6HOXn5XUESSU8_WvEQ07JkhSFzyB1oyZjxDxa66POqJ_lWEooduGQEewUxlpMxP2RAZdEf5ZdbcuHOLMXw60AnPmkEZWQTkKRswnYxVTzThw80BgbTGO3XFoYeZfoa4zvZkfhdIQBhOkBtGnHdVnR0oXlGCJ7OM7jTs_G5Asj0iOrfIpsPgrqt6Wgry5Z33NzJX6jjWwnp2eoao-idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108325" target="_blank">📅 10:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108324">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=O8uiaTAw4JsdShEHdCVJer3vubP5rM65KLdStCpX7TdmL63xGwNjdppQdSgdy_al6vJV_jHJqWyDo5ppxkMqMdMAekHEM5B_c-Hl6iYLqFo9fVYoHoZlR2e_faa0LckqzT5VILXl4ChzMi-5Gv5bsJi-cmWTIQK3_7qbm0lNb_W4oOAYcVPxr_hDLxgK7mpG_1i9Owybf_OyObgpqFw3Zi9bQCDcRk4fuHRntvl-DG8lIPlVDaFajnTtjQFbCwohfCQuz_epAm_5tRDrVZYQJuPkaaBc6wk4LxA3KgmsY70loTtonJD37veVtH-huNIgbP87kK7R2BhAX86wATnl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=O8uiaTAw4JsdShEHdCVJer3vubP5rM65KLdStCpX7TdmL63xGwNjdppQdSgdy_al6vJV_jHJqWyDo5ppxkMqMdMAekHEM5B_c-Hl6iYLqFo9fVYoHoZlR2e_faa0LckqzT5VILXl4ChzMi-5Gv5bsJi-cmWTIQK3_7qbm0lNb_W4oOAYcVPxr_hDLxgK7mpG_1i9Owybf_OyObgpqFw3Zi9bQCDcRk4fuHRntvl-DG8lIPlVDaFajnTtjQFbCwohfCQuz_epAm_5tRDrVZYQJuPkaaBc6wk4LxA3KgmsY70loTtonJD37veVtH-huNIgbP87kK7R2BhAX86wATnl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نادر قاضی پور، نماینده پیشین مجلس: تراکتور پرطرفدارترین تیم جهان هست. از رئال و بارسا هم پرطرفدار هستیم. کل مردم ترکیه و ترکمنستان و آلمان طرفدار تراکتور هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108324" target="_blank">📅 10:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108323">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=GynAmkrHGWyaM3mvmjro_FQxxZEXQkdrs6g0wIyP296jFOlQR4Rrh_zJex2B_4QVcyBeP-PHczfBj54L9Vm-43qBT8imdI2n7vgQxsvGcPcgS-e2d7-iyYvxBdiFfwd_2Oh2NrVLPN2uXYry98uobD6OcsBZXXADNi5uSu8aInXgoF0r7G4JdN6lJ9lq5BJV5DU1sLmiRu7ZLftExHC4k9HWvLLtJTtoSw4xno7ZAHpmtaxmt9nMGtj1zCBtAnPaylCElbXFKriTdMJCg1C6-a3fx3E3OhNdS3y9iV1DZheEb9kFaka148L4Qm0BAP-1p52-tMtjU9Bo7gajFUyVqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=GynAmkrHGWyaM3mvmjro_FQxxZEXQkdrs6g0wIyP296jFOlQR4Rrh_zJex2B_4QVcyBeP-PHczfBj54L9Vm-43qBT8imdI2n7vgQxsvGcPcgS-e2d7-iyYvxBdiFfwd_2Oh2NrVLPN2uXYry98uobD6OcsBZXXADNi5uSu8aInXgoF0r7G4JdN6lJ9lq5BJV5DU1sLmiRu7ZLftExHC4k9HWvLLtJTtoSw4xno7ZAHpmtaxmt9nMGtj1zCBtAnPaylCElbXFKriTdMJCg1C6-a3fx3E3OhNdS3y9iV1DZheEb9kFaka148L4Qm0BAP-1p52-tMtjU9Bo7gajFUyVqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
بیژن بزغاله 2008 روزی 4تا رونالدو و مسی به عنوان صبحانه می‌خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108323" target="_blank">📅 10:15 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
