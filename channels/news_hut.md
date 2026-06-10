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
<img src="https://cdn4.telesco.pe/file/OVmEd3_krpBPPz52Ay3BjEMPIvFNtYYtnEpNUqj6H57cVFgOOz0x4A8_tqojEk8LTGIHXG2izU4hwnWMol42fHmDR9dhpweat4v7SVjlMPTHApmIeCAjydF9WHhAILcdGIFEkeXWWve_RsGzKSBbk5bwWEfHsNRYKWZeWbRtQsrRQUgIEYTVrYiMPBgNbwJSLhfsgRE9GgyprpygdV1kDsR_b7cpGNMlHI83VsndwE98JyTnN9mT9zqwAx_DGg7CDJ_6hhBFLTU9wYRTe8Zv794p-wzY3-UbDK2POAK5SwnXaOKIo4szAubNb2j_eXUDE0dSkGktcuKq0Txd28iAmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-65704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
ایران ما، امروز بیش از هر زمان دیگری، به اتحاد نیروهای ملی خود نیاز دارد. با یا بدون حمایت خارجی، سرنوشت ایران در دستان خود ماست.
ما قوی‌تر از این رژیم فرسوده و ناتوان هستیم. ما مصمم‌تر و استوارتر از حامیان اجیر شده‌ایم که برای نمایش‌های تبلیغاتی به خیابان‌ها فرستاده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/news_hut/65704" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
⭕️
⭕️
رسانه‌های اسرائیل: ارتش این کشور درحال تدارک آغاز فاز دو عملیات مشترک غرش شیران با حضور مستقیم ایالات متحده است
@News_Hut</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/news_hut/65703" target="_blank">📅 21:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OY2suJPlbEOqhVV9-vHDw2Xc5wYR-HQonb0myILZhLuclO1zQyLJFfMXHMYt291J9uhjQpfXpfzQz9gKQOw_wJVD79uwFV0m1ijhiaAc1bQbD-So23C1ozVZNlABgU6ChN1gjYcY1lBonnJ0uSXUq8aJRW60IP90ddeT20j3i8-7tdcsZCc-QdkvsOykWv7HeyMTq17dC5hpTBOxV7FzWaGzIn695wc8-M-LhG5nAEwz07NQYpfVSeb6Vtc-HEv1YjxZJIncESzDTj7zKXCvhtQwJpPSeAlL2_iMhDZEUQ2pYP-sTDBsga9C8Mj6qFfDvmfQ9--LEcFQ48ajcFOff-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OY2suJPlbEOqhVV9-vHDw2Xc5wYR-HQonb0myILZhLuclO1zQyLJFfMXHMYt291J9uhjQpfXpfzQz9gKQOw_wJVD79uwFV0m1ijhiaAc1bQbD-So23C1ozVZNlABgU6ChN1gjYcY1lBonnJ0uSXUq8aJRW60IP90ddeT20j3i8-7tdcsZCc-QdkvsOykWv7HeyMTq17dC5hpTBOxV7FzWaGzIn695wc8-M-LhG5nAEwz07NQYpfVSeb6Vtc-HEv1YjxZJIncESzDTj7zKXCvhtQwJpPSeAlL2_iMhDZEUQ2pYP-sTDBsga9C8Mj6qFfDvmfQ9--LEcFQ48ajcFOff-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
♨️
شبکه i24News :
انتظار می‌رود ایالات متحده در ساعات آینده حملاتی را علیه طیف گسترده‌ تری از اهداف ایرانی انجام دهد که دامنه آن از حملات شب گذشته فراتر خواهد رفت
هدف از این حملات ارسال پیامی به تهران برای ارائه پاسخ فوری در مورد توافق پیشنهادی روی میز است و به معنای بازگشت به یک جنگ تمام‌ عیار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/news_hut/65702" target="_blank">📅 21:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=ZKjEPfWTV8gplY9Gfv7Eh3oYkPAovAAi_gqKvo2ELLV0BmmGanEnd451m0yZb3viBK5zKb6JaSEilJPn5yecLmMb-TKTBvny-YEzsouI8aD1b6KRmhaYw72Ws_R-JaeDxDwHtoYQN1-lSLH2S_ghl2sL5W-JTAtAcbgK2wa_Sq3fPXSCXkvvXGLiU4larDX-OKsbB5TgS8vwfXIszsBC24cNkQh0csPw3Mw_CpxbTW-Gm_5k5E_DD2z4Q934T-Eia8ZNTvntn3Da8fAzYNdVNQ2eE2opeisFCjqI628hrVwSFnG9QvmI-4srsVAMKemMI3PySzXHaItEtmMlqdVAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=ZKjEPfWTV8gplY9Gfv7Eh3oYkPAovAAi_gqKvo2ELLV0BmmGanEnd451m0yZb3viBK5zKb6JaSEilJPn5yecLmMb-TKTBvny-YEzsouI8aD1b6KRmhaYw72Ws_R-JaeDxDwHtoYQN1-lSLH2S_ghl2sL5W-JTAtAcbgK2wa_Sq3fPXSCXkvvXGLiU4larDX-OKsbB5TgS8vwfXIszsBC24cNkQh0csPw3Mw_CpxbTW-Gm_5k5E_DD2z4Q934T-Eia8ZNTvntn3Da8fAzYNdVNQ2eE2opeisFCjqI628hrVwSFnG9QvmI-4srsVAMKemMI3PySzXHaItEtmMlqdVAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام ویدیو ای از هدف قرار گرفتن یک نفتکش مرتبط با ایران منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/65701" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گروه هکری حنظله وابسته به سپاه:
به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند.
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست.
ضربهٔ ساعت‌های آینده تلخ خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65700" target="_blank">📅 20:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65699">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سخنگوی آتش‌نشانی تهران:
ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65699" target="_blank">📅 20:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65698">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pReXK04u7JrubxCGaohXEj5gnMSJqg74wyHpjM59FH8qJIiT_58szZs8vB_3qbXVbcMKHd950NY7Z5tW7o8x_k0MZXEkpOMamnctkzJ6K5nk_to3aFQEoQcqyMMmDN3P-JDoZ_3it_JqBAAZj9i81GiDb6PDVGGACNqT--oQKI9jzynVp1aPVDDj9CwKNwA6Jiemus5jCzH1Or0Wt3JSBWkKB3YIb3Twhp4gKxngu7rpjNItcl19SFcOA3HLDByw3b4w1Lh3BTmiLRgH4yI86ukmQjbCjTXXP6umDk44CiGELPJ-gr8w8ND28dopBJg3v0QqelepfOWmKLRotQKIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ساعت ۲۱امشب «
شاهزاده رضا پهلوی
» با مردم ایران سخن خواهد گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65698" target="_blank">📅 20:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
رسانه های آمریکایی:
حمله به ایران گسترده خواهد بود و بدتر از قبل
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/65697" target="_blank">📅 20:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNZeUbPcCyaaBeByXjS2C5bSH74G5JrR8-QbLmTJs-HgNLQUuHWx9WNJoGyk_4nS4UFBHm99e8WJMa7KWK1IpujhK3t-DBRt28Pr11D2b8LgvD0RqLeuaT0uUZjB1ynmrxrto6EijTXUzlgZHI-TUfVH9bapfn9lR03RDaRoa0Zxvzper7SSbqaN4Bn0nFHe-e299r2YDsdO1pnziHmjAVU-bIOX_FahojuTb4ZcOKMpVaeADysdtiTiqoZDBjrkCdNT4b0YZAI4qivOvUpQqiUDGRgQPxlmvu3Ubiw-9fHf-WxX6YaXNSRpSFZCQhrAhoQKW04RX_n3Gb8PlbNzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در خیابان قیام تهران
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/65696" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65695">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است.
حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65695" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65694">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ آمریکا: عاقلانه نیست که جمهوری اسلامی بیش از این آمریکا را به چالش بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65694" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=kSJHplVstW-Hal6H3m2xVWo2aKSzq1q6uZCREeQvV0KxYCEkHeglGSKFoqqmE_Ekhea-Yr4c_aRhOrD0EMkQIu6HSlOb8bEY47R_nLdqxmM4nICYgTKYgIpnOMnaIQEfxpmDe5zkPy_Yb-GjZivLp4lPRlm3beJ4Jihsr1GJUwoT2e-Y9FbiWtUDt7j7XOt4_y6gurEcRtmnfw3f5QUAipHVTpgZJtRyRRQrENCB4AGI1Irq1_Ifwmw8XoPgvwEhtqbVtTotDllXJed0QecWJNqn5IUnASPcpgHPIOYl1qFeM7ryOT0A4mCWjb-x9yzR14u55iHHwEDRJdGKqDweQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=kSJHplVstW-Hal6H3m2xVWo2aKSzq1q6uZCREeQvV0KxYCEkHeglGSKFoqqmE_Ekhea-Yr4c_aRhOrD0EMkQIu6HSlOb8bEY47R_nLdqxmM4nICYgTKYgIpnOMnaIQEfxpmDe5zkPy_Yb-GjZivLp4lPRlm3beJ4Jihsr1GJUwoT2e-Y9FbiWtUDt7j7XOt4_y6gurEcRtmnfw3f5QUAipHVTpgZJtRyRRQrENCB4AGI1Irq1_Ifwmw8XoPgvwEhtqbVtTotDllXJed0QecWJNqn5IUnASPcpgHPIOYl1qFeM7ryOT0A4mCWjb-x9yzR14u55iHHwEDRJdGKqDweQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ :
به درخواست پاکستان، به ایران فرصت دادم.
فیلد مارشال و نخست‌ وزیر پاکستان افراد فوق‌العاده‌ای هستند.
ما جلوی رفتن پاکستان و هند به سمت جنگ را گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65692" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65691" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDPHOwNSwi8oSZAADCcb0ILHBRgwK0Kp30dA2mLMtv65AmN64nUkYpAA-4XlR7oIz6R78VtROIKfh66cg64Q89ocjr87oVGOMqj2zXCOkxbiXfjRvswryiFJ--Jv1evIsCxHWFdPZgWdKX1XY9sTIQMQlpeJ60Xp5Zs39ERWsHt2t6tYtJz0IG2T6-54Mi8vS06s4oZu7h22I9yNb6CNDzuqPMShERZdKxVqRK99GdS5AI_9S1GU8MbjZNkkUASX2Xy2kCZdz54IrkHhKEqVSpS1CLZpwzmQ8bV8Gu7UWL4R7M00tLVHMDF5WB_mlV0Igz0vLCQqjP3UQNsv6sMkIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65690" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: همه‌چی سر توافق نهایی شده و فقط مونده برگه رو امضا کنن، ولی هی وقت‌کشی می‌کنن و امروز و فردا می‌کنن. منم میگم باشه، چند روز دیگه هم بهشون فرصت می‌دیم  @News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/65689" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: همه‌چی سر توافق نهایی شده و فقط مونده برگه رو امضا کنن، ولی هی وقت‌کشی می‌کنن و امروز و فردا می‌کنن. منم میگم باشه، چند روز دیگه هم بهشون فرصت می‌دیم
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65688" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اونا فکر کردن من رو هم مث رئیس جمهور های قبلی می‌تونن بازی بدن</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65686" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19aca716f.mp4?token=Hfi1A9d5GWLsLA0EGop11GTgsYj24XOAS5YQLmuJjrDU7Wl5pTZ4fqImDScYAjuLJUI1S9t7VzWcK4_Z50o0nTFnBrmvEmYNea30uS6iBQRLeSkrCQZTUWaCiH85YE1OFkn9OEBei3e-e0OI08SoCg0y8v0844iKhpTIOCMeb-MOJfFeYKdIOUlhshycm2AJqyHtL8TSpINc7wJXSo0IssXUw-XRV9f7WABFvy_WuhCjxhAgHwS0AdllblUewtExdWyew_g005jxn7OjuN52XG_7yHEJy-HMH3VpZWyZrPGAl0KtFc_jdZX4ppogDIIJByxInnRB2qMuwjWD7Zuj-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19aca716f.mp4?token=Hfi1A9d5GWLsLA0EGop11GTgsYj24XOAS5YQLmuJjrDU7Wl5pTZ4fqImDScYAjuLJUI1S9t7VzWcK4_Z50o0nTFnBrmvEmYNea30uS6iBQRLeSkrCQZTUWaCiH85YE1OFkn9OEBei3e-e0OI08SoCg0y8v0844iKhpTIOCMeb-MOJfFeYKdIOUlhshycm2AJqyHtL8TSpINc7wJXSo0IssXUw-XRV9f7WABFvy_WuhCjxhAgHwS0AdllblUewtExdWyew_g005jxn7OjuN52XG_7yHEJy-HMH3VpZWyZrPGAl0KtFc_jdZX4ppogDIIJByxInnRB2qMuwjWD7Zuj-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: دیروز به ایران ضربه زدیم و امروز هم می‌زنیم؛ اونا فکر کردن من رو هم مث رئیس جمهور های قبلی می‌تونن بازی بدن
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65685" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa5IL5KeZ7pZgSePlbvs2oxaC6nAZ-ApfIMLom4iaE-rPtNcbsVYslsuE2eLHnjIzc1cZsK4WcCK480AKZNgjfk1pncpfEYQKNyT5bPhPF88z9WE-EQEdbf5BP_Ysib1vjb8x7aVGtCFaSK2caDLMh4Cv17VOCCa8O0wRHr06W70szUPDaieemxQA4jOVP4rl5jLYS3wy7IXYcFwG5sr3azvteC7gyCSkBQQ-hE3AF_w5DxRcYcaBxsk-SaJ5TTumZPxhXMedmsmbthw9sjCJNoniHJblxrvtN-BAe3PYkzaLq2lLClG7QTZjtMJS3irU8CqOXnmYerK7tBaaqaKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امارات متحده عربی روز چهارشنبه، حملات موشکی و پهپادی جمهوری اسلامی به بحرین، کویت و اردن را به‌شدت محکوم کرد.
وزارت خارجه امارات در بیانیه‌ای این حملات را «تروریستی» و «بی‌دلیل» خواند و اعلام کرد که هدف قرار دادن پادشاهی بحرین، دولت کویت و پادشاهی اردن هاشمی، نقض آشکار حاکمیت این سه کشور و تهدیدی علیه امنیت و ثبات آن‌هاست.
در این بیانیه همچنین آمده است که امارات همبستگی کامل خود را با بحرین، کویت و اردن اعلام می‌کند و از همه اقداماتی که این کشورها برای حفاظت از امنیت و ثبات خود انجام دهند، حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65684" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. بمباران را از سر خواهیم گرفت. ما حق انجام این کار را داریم. آنها هلیکوپتر ما را سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/65683" target="_blank">📅 19:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBWP8t89BwTJmgxbLgfu0naZsLcCTWzJORYAvZxQ7NG3rw0ISvccXZsWrsoJIM8Y0A1X6FBCYKW_NcnmzI2cPqYD-PwVYhy8nQqOqo_BI2YXQOrabX81mryDIYQ9FAYy8WvOLztvBfhkmBlNA4qEd-XArcwruS5fjH7eqEGCYGmEnO0hsKN3I2BVowTKQnHLBzHelv9A7DId8Zsr_GjWX0Zf3mPCFh9VtROEXCYtstdMros-wadX93_YF5rIeOjiNdgWOAbMh8Vc3DShe4N4xhYoLVEUrkQOeyU456mRc4BrdUixBtKhsUeg2pkGOHpx0sXKGSilKk5vSJrh4ql5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZewzgGt5P_CROBzSY1cpV0xVDmqMR6pwQhhCWU4paTEjU9M9vUMoTJFBWPcuJhUllxr8--s16F2YAP4M8naTHgEIq6MZV56jX5E8Lptmn_mUBxE6lfd2jujJu4iGWiNow3y3bZCCmpiTl9owMKVyfGTzyamFbW3x4U9f9oPYdmET6lrXL9pXGM7LZfOZWdRa8NSo2zyGsfglKqmyznkFFcAUPCmgPLDEjnAsMSZRusXCulC0Qhju4CaPcdFSyAsU0t-fnB2KPiijDPks1UqojdebO1dH5JDIG0GX4MaDUQ2Jkzb2cM-PSdZOFOHsN55u2Zh8zzBckX6pkNTIDteLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت (خراسان شمالی)، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65681" target="_blank">📅 19:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW-WFHvUIQDOUwvfHc547DIz3LfphibI-xqu2PLouUiusBlMKhfoWFCHbRYNx09HFnp6R6FsDqcBs7Jsu7dFDX9nuB3wsK9OHHvvPzyWxt7fWuzMfZ7MNCOZ9lg89BHgxS8DKzXjdMgc9doAuXi7LGUvDNFE-G_8c1LpRFL0LDK4yCliAhpjuuQqqNxCF7sB8WftoOU5o2lDluZY-n3ZeAtH1XHEWNT8yLvTxew6w2NMxD1yFp_oOnSdSDsDB7mOobRT6SfWD6WB5cwWLQyf1TgEZ9mc2pmfPk7smDvcSd3WwvKGiNocPszP9ljD_jztSaV9CvhIYgoBE3h7klroyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حمله هوایی اسرائیلی در حومه شهر سحمر در منطقه البقاع غربی، شرق لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65680" target="_blank">📅 18:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
نیروی هوایی ارتش اسرائیل ویدیو ای از عملیات ها در جنوب لبنان و ضربه زدن به زیرساخت ها وشبه‌نظامیان حزب‌الله منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65679" target="_blank">📅 18:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
؛ تصویب قطعنامه آمریکا در شورای حکام سازمان انرژی اتمی علیه ایران
+یک روز قبل از جنگ دوازده روزه هم اتفاق مشابهی در آژانس انرژی اتمی رخ داده بود
.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65678" target="_blank">📅 18:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT42jJhYlox83F4PY-FMLPWVX3J59o4akijI7LNID4KnUUKq9C4LS-lYca50g9IM4vxMW6-djJDOPKj3vMxzSaGgT2kquOryKLVxOUedaoJXCFV81mo3V_UjNBslmvWIIVT4ZNHiSwV6GBh293uMg_DGARKrPhu67OzuMZKFsllJhmfYaP0wrMHPA3-YWumv0mUHKUZgi7tQ0nkR0NZsbd0oZ8SzyD728ZumBZKcF_3CHAdS-m1plDb_YJNeTMs4KlTfTMzJi-bieJo_QrT39Xa7hy4AebdLM7Jxr1jHpZ1mY6QmsebxQ4O7m8ibiSYRGtjutS_l4QBcmJqfvfRkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انس جهانی طلا هم به ریدن خودش ادامه میده و امروز هم سه درصد ریزش داشته
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65677" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !
https://play.google.com/store/apps/details?id=com.barkovpn.app</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65676" target="_blank">📅 18:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا در یک سخنرانی اضطراری با رسانه ها و مردم صحبت خواهد کرد.
جزئیات و محور های این سخنرانی هنوز اعلام نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65675" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC6ObM7Z8jbMWh8SF-GemDCve8OYD3rBohgBHdSZr6qhSEKpwXDi9y7K8AAyQ3ozDRfVv5g0gR_1fh_ZN0Mt-AHtlVg_Xa0o_SWP78YYo4i6tc8d5G-j75ecg6ApwUYfxeDj0lWsBY-_R5zfP_LTktpKs2fkfPmsf1E33C5eSW289_i625RaLewMJW0DxsTKgOi2XhgIm8_9cHbgqgO-h6_YOi0vdl4NoJet1aGpAT0VK3pXqo6HWSnaGtWHu-NlXf20u_JrHIBQnMzFclNjJF2ex6A8qc-3T-j3CtxuoUNbBRfRCyvOzvQmfbPupaM2s_Mm4WuVdkkYJucjgz4rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو:
به اقدامات قاطع خود علیه جمهوری اسلامی و نیابتی های آن در منطقه ادامه خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65674" target="_blank">📅 17:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwlUIOCQdrE-LcXRuhJhqQ46lFG1rogpBsKrnYXybwHdCV7SRp524zmHyuguVnU98BXdhua4Wgm09MSjwgMPIZpJCgfM-yun0TCThTWCy6fFn6FzZVrnrVrgKhdIls-Ox3z15eDGozi8-MGl7RDz29zpI36LNOVeCnSwO2FMZ1rPI84CywXejKPpj5mQeriS5sro8SUXswOkFL-ahOGXIazUHmj0XkPTeuu8fGo64TN2Ek4Xy4Rb2BhkVtffTACH499Bn_p8VCJF1ZCGVVj5nlQbGm7Fe8m5BVatz61cNrhRdNh9kgTsrsMnQJ8CDKUnmhUXXDyjs1fOCKCBGy4hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب گذشته یک فروند بمب‌افکن B_52 نیروی هوایی ایالات متحده در پایگاه هوایی فیرفورد بریتانیا فرود آمد.
با احتساب این بمب‌افکن مجموعا سه فروند B_52 در ۲۴ ساعت گذشته در پایگاه‌های نیروی هوایی سلطنتی بریتانیا فرود آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65673" target="_blank">📅 17:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/j9c32D7vm2iEKbphB2vsY4yTMnVwO_d__GEh5U3Mj2YNkUvC5bEMOCpTLGTBbfUx_HKZUVN11Xqyp8xXo49EaCsvJ1riWkeg7HJ71XZXdGPCR2Rb8h-B695JoMe5h5r5_LhC2Mgq3AmaLP2d_auMjCp23naX5cSrVt80GJ89TBfTiBieSZi43MdSJQLrVOZiQJMK9Qpj8UwyG_tKuDkRGyT3dkXL1lM7O5XPMZ9KPRxRuWdYC9agnZj9km1Y2D1iljfByTnRsUR0ZfJoYzX3gYCbN5UqgieEHS2kpgp98tnUIdnyhwAFqc-C4tAdQkE0PWsjIPv9Rk4pimR5RmtQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۶ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🎁
| کد تخفیف : 40
▫️
5 گیگ 30 هزار تومان
▫️
10 گیگ 60 هزار تومان
▫️
15 گیگ 90 هزار تومان
▫️
20 گیگ 120 هزار تومان
▫️
30 گیگ 180 هزار تومان
▫️
40 گیگ 240 هزار تومان
▫️
50 گیگ 300 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🗣
| ربات :
@OPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65672" target="_blank">📅 17:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a9aadfeb.mp4?token=Fu_v7F_cME23fyfkQaXnMl7yy33US6RrKuq0GtIcXuqF89Pfys2JkcUJqs1Jf_2lleEfZwfLvmv7eDGvm0DS5cdSTwFtGlhelb41dRhK6PB57_zMvnceFxjITNePPa43gi93nczDD4t742zwgFhTH42U61k3AkziVka73SwDjgZE0kPpejN3MAw5pGDK-H-l3fQmptOTzLEKyhnkxrwYrGjcppSvfOHH3SJieaBpPBbz6ZsWAfEDBL_kfXwIy_QU2TZ063xGXEqyWhnZ5XRqPZ4fFgbOPsbupt_2D_8ywQkdIzWORzF8pCxCi_iaUmMP87JzoY5X0KavOR6dHeM9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a9aadfeb.mp4?token=Fu_v7F_cME23fyfkQaXnMl7yy33US6RrKuq0GtIcXuqF89Pfys2JkcUJqs1Jf_2lleEfZwfLvmv7eDGvm0DS5cdSTwFtGlhelb41dRhK6PB57_zMvnceFxjITNePPa43gi93nczDD4t742zwgFhTH42U61k3AkziVka73SwDjgZE0kPpejN3MAw5pGDK-H-l3fQmptOTzLEKyhnkxrwYrGjcppSvfOHH3SJieaBpPBbz6ZsWAfEDBL_kfXwIy_QU2TZ063xGXEqyWhnZ5XRqPZ4fFgbOPsbupt_2D_8ywQkdIzWORzF8pCxCi_iaUmMP87JzoY5X0KavOR6dHeM9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🚬
تو مکزیکوسیتی شورش و اعتراض شده و در فاصله یک روز تا افتتاحیه جام جهانی، معلمای مکزیکی به خاطر دستمزد پایین ، حمله کردن به محل استادیوم افتتاحیه و ارتش وارد عمل شده تا جلوشونو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65671" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام. ما کارمان با ایران را ادامه میدهیم و به جلو میرویم.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65670" target="_blank">📅 16:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef101c520e.mp4?token=emIwQvQNyCMLynPSyKtZoHCP-GNjLYIIT8rsu25ihzq2utKO7tNkAox5Dl40bvB1MKRns4cxj-sNDVl4HI5wrmFipQWFMn7FC7liAw6GLFr8UxN9QIpMvWPSYLobISeUI6zsQaHkF5Rf7bo3EpkpqJZFxgPTiQbYxzzX7ZJuNXjKnYhEcFvqiK-6KdciT-jp9hrdesQjnQOcK33cKhFx6TcAA_izfxAkO3snSGovnT4QWwpcaCz-xoRBqcElH_XduULRhp6j7BDj2ybNbUjTcO9UqVMzyW2ReGMURypKzR_UFTuIKjlm8gd_SidPicenqFsAi5TBIcjgDFxn9xGI0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef101c520e.mp4?token=emIwQvQNyCMLynPSyKtZoHCP-GNjLYIIT8rsu25ihzq2utKO7tNkAox5Dl40bvB1MKRns4cxj-sNDVl4HI5wrmFipQWFMn7FC7liAw6GLFr8UxN9QIpMvWPSYLobISeUI6zsQaHkF5Rf7bo3EpkpqJZFxgPTiQbYxzzX7ZJuNXjKnYhEcFvqiK-6KdciT-jp9hrdesQjnQOcK33cKhFx6TcAA_izfxAkO3snSGovnT4QWwpcaCz-xoRBqcElH_XduULRhp6j7BDj2ybNbUjTcO9UqVMzyW2ReGMURypKzR_UFTuIKjlm8gd_SidPicenqFsAi5TBIcjgDFxn9xGI0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جزئیات عملیات نجات دو خدمه هلیکوپتر ارتش آمریکا؛
جنیفر گریفین، مجری فاکس‌نیوز:
مقامات آمریکایی مطمئن نیستند که ایرانی‌ها قصد هدف قرار دادن بالگرد آمریکایی را داشته‌اند، اما گفته‌اند ایران در آن زمان چندین پهپاد بر فراز تنگه پرتاب کرده بود.
دو خلبان توسط یک «کورسیر» نجات یافتند؛ یک شناور سطحی خودران ۲۴ فوتی با برد ۱۰۰۰ مایل دریایی و ظرفیت حمل محموله ۱۰۰۰ پوندی که توسط شرکت «سرونیک تکنالوجیز» ساخته شده و در زمان وزارت دفاع لوید آستین، تحت مسئولیت دولت بایدن به کار گرفته شده است.
این اولین باری است که ارتش آمریکا یا هر ارتش دیگری از یک شناور دریایی هدایت شونده برای یافتن و نجات خلبانان سرگردان در دریا استفاده میکند.
«ناوتیپ ۵۹» اولین ناوگروه عملیاتی مجهز به هوش مصنوعی و پهپاد نیروی دریایی آمریکا است که توسط دریادار برد کوپر در سال ۲۰۲۱، زمانی که فرمانده ناوگان پنجم بود، تأسیس شد. خدمه سرنگون‌ شده پس از دو ساعت شناور بودن در آب، سوار بر این شناور خودران شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65669" target="_blank">📅 16:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
صادق زیباکلام از اصلاح‌طلبان حکومتی بدلیل اظهارات اخیرش بار دیگر بازداشت شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65668" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
ترامپ:
آنها فرصتی برای امضای توافق و زنده ماندن داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65667" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۳ اسرائیل :
احتمال واقعی و جدی وجود داره جنگ علیه ایران رو از سر بگیرم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65666" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65665" target="_blank">📅 15:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZtnSaUZYqlL3eR8Dr9PzLkiW-DZ1swURc4Hs3MkItWBfInoNtea8TKmMUdvJZngR4pk_EGysu_DcBDDD2nzjdzp7N2gkVPh_3JeDP8cgOQ0iGnB558E8m6nKr5seh_mbMo5bSYnXzOyxq3clE_5RQglbvL75nSnaARbiMPdHS4zaVMa8VwyMbah8M5DqNkI_BqCW417B1NzUB1DRlEHBzHzPczhNMpK52uSg9qceYlPTyPPXVHb94opDn_sgAwZkdlouFvpeORvDK26Yl4alhIhvIDtRNFxW-bCVfLPkemfTLdvny2KGVQmqpoLHhQICOFQB0zQJ_B10BiciSqcHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید رو بیدار کنید این کاکولدزاده دوباره شاخ شد #hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65664" target="_blank">📅 15:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHeuWMsUXHwFbFz2K4epwx3gTEr3_UVoiGLRguZzsldK0I4Ebc3vs0gYOi7K_KIwRpkFolEixeeJRwNhKYKJvMEfL_r5NJGWddadUmQGDh6QqUmxNQnjPA8g0hO0IovqwGeu2IOVRRAKke4xjltJzmoEPrkXYU6pWVMeJVeGsJyC-pXBw4ujoXEvdxffLj2_4ajl3XRUvkOof_OLsuhuBQ__3Q2ka4bOpu6XPVHOvBV-n7dQ39txTbCj_piRB_heiWLeqi44TZqahIVUr-9wfMnRhCEq6-pmQtfFE03jUeLSKFiMUzwtyn5hZtRqtlCrx2IV7SrMKAh1-E93aKetHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
رسانه‌های خبری جعلی از گزارش دادن درباره میزان اثربخشی ایالات متحده خودداری می‌کنند. محاصره دریایی موفق‌ترین محاصره در تاریخ جنگ‌های دریایی است. هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران تجارت نمی‌کند، ارتش خود را تأمین مالی نمی‌کند و هیچ یک از صورتحساب‌هایش را پرداخت نمی‌کند، و به زودی به یک کشور شکست‌خورده تبدیل می‌شود! نفت زیادی خارج می‌شود. الحمدلله!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65663" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام. ما کارمان با ایران را ادامه میدهیم و به جلو میرویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65662" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:
به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام.
ما کارمان با ایران را ادامه میدهیم و به جلو میرویم
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65661" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65660">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ:  ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65660" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_GIcUY73luqIrvpCGgabSl4rzd1PSibBLQSIpVoLtYM4w4dRuY8aIhQJkLD3cI__yevV9Z1nKq_Mp6XReyHOg5m1DmjWOIkLaP9oE28gxEeoBZWnunUkFDpGZTJzb-UuZlAL5DjojfrwWVZAp0NHDrVIijDBGrfhW85Yfji3pwBrV5raTX-uoKndhbFkrWuTulVFwZsjvYXCylYiz8hVd9eNwa8mVpuTeIfttnY6QW0F1hMfk6_MiT160A1hClJ8qMUU5gQPVAl7fUEf5PG7SIG4El0dQIHS9rIP9Xct5IPoLPyVGz4uqPcQInetf9kL-zvPs4mNXyZ1xFAGCPKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ:
ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65659" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=rYfP3A7fM94vhQCmjF540_e0Y_6CmDpKCcf7pDxp8KMqlwPtM814SS_zF1mxKvQviyF3FANKJNbPyaTQdL4Xjab1nacmIXJrXgWGc--pw8T1gMGvt9KJjN5gXCV3ApveVNvJTxVjt-Tx6A7cw5-5uT9EWaqOqVsTsSTKoibZOqblCqqxeF85bFCTJeyt-3pSZAPXAoRCNpnKjIORFYhS9OyHe-MVAOuVfMUVeJknPeSrv-AMKJlDHImSGpPGZmnkDrfgVpLAniXaAAgakWF-L5zItMt8djkHNltoG_sfF6y-dJMPf1sIOjNhS5P4_g8vASp4RKD4GMJv46bgDUhIgjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=rYfP3A7fM94vhQCmjF540_e0Y_6CmDpKCcf7pDxp8KMqlwPtM814SS_zF1mxKvQviyF3FANKJNbPyaTQdL4Xjab1nacmIXJrXgWGc--pw8T1gMGvt9KJjN5gXCV3ApveVNvJTxVjt-Tx6A7cw5-5uT9EWaqOqVsTsSTKoibZOqblCqqxeF85bFCTJeyt-3pSZAPXAoRCNpnKjIORFYhS9OyHe-MVAOuVfMUVeJknPeSrv-AMKJlDHImSGpPGZmnkDrfgVpLAniXaAAgakWF-L5zItMt8djkHNltoG_sfF6y-dJMPf1sIOjNhS5P4_g8vASp4RKD4GMJv46bgDUhIgjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگ جدید تتلو بنام "رفتم که رفتم" از تلفن زندان که آخرش می‌زنه زیر گریه....
⬇️
دانلود ورژن کامل و MP3 آهنگ
⬇️
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65658" target="_blank">📅 14:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65657">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b931b462.mp4?token=CUi8jSzLLdp-nSbLw9H8WqebZe87eO1f4yIEAIPg3zcG6MwS3gNNMwbm6YASXnDFErn34EZa2H6wyqHBrPerDXJOiVvtHpsKDJnaC-5GC6_7hTbfTYMJLlDImzswKvFE8LMotj3sUnKs7D3sJli0gsdv5VDqe-Y2R-6e5RWclNQvxRg8-svbermQrl83ZmwwDq4qzAbJMCTV9Dw4pmcWtn2YnsgasmEr4aJZWiDJWhwwiSbT9vn5kXaiEfnnL1mgFsByJwfG3xl4JMwDdz5ft-Vfn0d6A3B-FpBEauyWJBW13-T75weMxXXauZjuulaqWUp1-E4tDm4_Zrzfwvjssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b931b462.mp4?token=CUi8jSzLLdp-nSbLw9H8WqebZe87eO1f4yIEAIPg3zcG6MwS3gNNMwbm6YASXnDFErn34EZa2H6wyqHBrPerDXJOiVvtHpsKDJnaC-5GC6_7hTbfTYMJLlDImzswKvFE8LMotj3sUnKs7D3sJli0gsdv5VDqe-Y2R-6e5RWclNQvxRg8-svbermQrl83ZmwwDq4qzAbJMCTV9Dw4pmcWtn2YnsgasmEr4aJZWiDJWhwwiSbT9vn5kXaiEfnnL1mgFsByJwfG3xl4JMwDdz5ft-Vfn0d6A3B-FpBEauyWJBW13-T75weMxXXauZjuulaqWUp1-E4tDm4_Zrzfwvjssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که این خانم از خودش منتشر کرده و گفته؛
«دختری که مدنظر پسراست واسه ازدواج»
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65657" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=Dizrk0Z7dcMGvNgO-0aFK6jqMqrcYrgn20hWT81btIXU4RlZbS7iEe2XEtqhzoIXmnESd-kG-9nI8R0zZn6R1N7Kak1tbUSVXTnYgiFVCZkv9J1XF-OjxbgNyjEe96otHjV9VF7-MCXI6MK34w5x-yxMLr3WijAnK6Cb9D_871SC8rsxc1M1R1p9tv6Kp9JiZfoZUrw44U9GbqOcitIUe5Etn9hxEH5zjUT0H2IcQiNNzziMzvHrqkTp3477qq0zfiy0Fw0xW2dviVty4NiWm4Ucfz57WZ-bxC4B4HAFxJtAZdy11o7IIcs9oiUVFJoQqgBfdHO2UgEP6fvBEXeeSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=Dizrk0Z7dcMGvNgO-0aFK6jqMqrcYrgn20hWT81btIXU4RlZbS7iEe2XEtqhzoIXmnESd-kG-9nI8R0zZn6R1N7Kak1tbUSVXTnYgiFVCZkv9J1XF-OjxbgNyjEe96otHjV9VF7-MCXI6MK34w5x-yxMLr3WijAnK6Cb9D_871SC8rsxc1M1R1p9tv6Kp9JiZfoZUrw44U9GbqOcitIUe5Etn9hxEH5zjUT0H2IcQiNNzziMzvHrqkTp3477qq0zfiy0Fw0xW2dviVty4NiWm4Ucfz57WZ-bxC4B4HAFxJtAZdy11o7IIcs9oiUVFJoQqgBfdHO2UgEP6fvBEXeeSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران شهرک حومین‌الفوقا در شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65656" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65654">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjBQNMXNCtjM13RNx-gBoCc751fw8w42jDrf3_rVDUwrwIgwKcKunSq3NlIZGWL9RnSmCpa4m_hwRQwRhta_9mzyS2rvH5wef46Fyp8_EszNC9Nowe3LPeIDzdoTGQsGjjewL-5O5nGtjauLL5oVU0JTvO2gujP-eQcesPEtv67Ocl1Z-Op-yOT66aIEnZT11iH0DVVzzDqowT1xTA5MmYIQMeLQn-4CT8mevpJUtx9kwKLKiNLWVUkJy4WR7n53_1YcesA5bpN0eVG9UhPR7LM7wO4ZjcbW0ybropsFnobh6XTwF53JrM4M5b3aOAdqD5zvIWLS6Fj-rJuPOY8y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان تجارت دریایی انگلیس:
یک نفتکش در نزدیکی ساحل عمان از ناحیه موتورخانه هدف قرار گرفته است و ۱ خدمه کشته و ۲ تن مفقود شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65654" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65653">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65653" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65653" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65652">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5-vQjoxRsfzqHpRZ0njOMkxc_khBcJRuNO4omMwaGuyrX0ORZt9CMIRi6i6egNNHpwZ2LREV6Ky1ndupVdacktwtbLk8R67jdOSdGChzGsbioO499-J5ICF1bME3AUih1v3-GRyAAdGHr19FRzoNXB0ky9MHItHSwH_fRq9RUMKYWy58vRog2n2joO5HzEp2a7yg63fkOQ0t_mm0Ecwa-uTe8z36hws4-TvtbGs3uaxUnyBvrU6DxSX_fX43fwVSA3roTp1PXu-OE-cdocYNGUONOQLaklJtBWtC-4kaoHZ8kgn4Y2t2TY97NnktIclVZZIuRwYC8tg_Q-fXKTrKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65652" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaXmpoX7TeW0cUTDLSA35rABosPDOIJEOF69PBcW1QpGwCAn3JwA60WG565KgeZjedfaZBZnxuFPMQbAUpL2DF3h6xR1Hkf8I0vW-2ZUSh5Sl0N2bNK0F7PrLRyvFh3k09COgRYN5ApVKVtQWoEK3dnBR2vDt4RWytkaSBHMAgtsGLd5w3QeD5HOkerjPnqGLhM-7G_jvS8h5gbhdsOs3WkxiHRClYT2Z-YmaH8UqUxVDi9CkrUwKVius-vEBLLk46kZspFxE2dHbbU3F_ko8CLRHffg42sbEsuNzZCjyusVY2a9nuHy7iLIMRN76ZDVipdAWgcffMryKBh8TptyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاتو پاک کن عزیزم
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65651" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم  این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65650" target="_blank">📅 13:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=gdeCtsxPzzGwWpqnz3AYAu4Vc2vM6d_Ka6X-RsyQPTvR67yzfTkuXAY4WCnMsKuZhpNmOpbdDFr-YJDYeGNiIaIX1NNwm4z5YEEpbfZ6Qguh5bCxINRCw-aTT5-20-y2YgI8BslKRFj7z2FB6NAVg_F-OmHyFqKatHcERRlEhJaNJnhXsNSTVlkZg-gUdCQKh3m2tiI1PWAk8YQgaBKsEWOkpI6kKKgRctZ3oOc5XiM6XfKCGLB_NXT7qfKjqJ2ui1jnIIm6qb2_O56AqiQPyv7qPP5rmPZdrAaI7Pea3WhGE7bvIIRb4Al_NxtOKFz0thVgUQ9CEUl8suPJxY-0nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=gdeCtsxPzzGwWpqnz3AYAu4Vc2vM6d_Ka6X-RsyQPTvR67yzfTkuXAY4WCnMsKuZhpNmOpbdDFr-YJDYeGNiIaIX1NNwm4z5YEEpbfZ6Qguh5bCxINRCw-aTT5-20-y2YgI8BslKRFj7z2FB6NAVg_F-OmHyFqKatHcERRlEhJaNJnhXsNSTVlkZg-gUdCQKh3m2tiI1PWAk8YQgaBKsEWOkpI6kKKgRctZ3oOc5XiM6XfKCGLB_NXT7qfKjqJ2ui1jnIIm6qb2_O56AqiQPyv7qPP5rmPZdrAaI7Pea3WhGE7bvIIRb4Al_NxtOKFz0thVgUQ9CEUl8suPJxY-0nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده:
اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65649" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSmJK5qcOWT5pqFOa_haESPbSNq3lgQ-VatUln00Rx_4nAXBZNxgHiDpkIrbKbn0rS1sfKQMAvNvHJVJSqty8-b0-22GMH9x8GDSWdKF2x5swEInsVHY0G6ufnXDsUus1RZJaV9lxXNe_6dZJc9UmjrU70d7RyfTCzVpZEPSfTyBwsDk4BTSDc5wtF--gyDKM1YYAjmjp0KBJhrKCK2OB11l7B3JYMK8boyBl__OaQDvUijQTDYUyI4uVT-M0IW4oSojrgMShDP1XnbJsLST9PlG9M-hXbokdno7AZu3jLNsu6WDvG6qyFzHOcHqms2KxJKwxejRT3J6vVao13Aaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOuCV7fWJC4MoPI6rd5Y3N-W8Cu6sRkZEzbI-UEd9Nvw2-xF3CIXdoDT1RwRLvalyIL2ZBkMUA1uEMXvUrNkjyyc4rnSWMq6HXTpVPGSsd3QTKQ9bRO2CC3T7WBljvvahCPKcRBNs5gsroG5wrIGIXHhyxPZvgkIWlOZpAZTMsLtDqJlR9slrGdkdtdKSL80hyjnEY_Py0dMlzYC3axa53gwGOdTd2BCDbaIYbID2WPAEh8f-7cQw4o41Aw-nsSZx40ksk_R5SIHE4vkmcbkqDLrp1048A5gPXj23T1BCL42CzHt0nkxv2zByoVkiC_IN7mP8hJKS4MGFu9JqKeSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJMzZQMETQts4XdJqVrtoNvGbzveSHE84VJwqADxOXn1_amB0W4PJbjSFwku76hgWWvSVfguxHMkjTs4066YQaZNEj1NEa7PSQx8K8D7by7piP8N55CiP5JN7Nbl-_-m6LkeSPDDJwIAzM9h8mq5LvDNKNxbH7eCpVAds7eckMS7CHB-mSQdBrR-Q47NRstJzXifOoTWuJD9XmHB5DkFbjqsQFFP8GBSj0ImZqTSp_YRFWOVPtfwoKVED36OfBof4skMjETqV2jsLK66AHH6vKu_Op1Q-7WsvGgcM4HscVLQpEFy2geYJfI2L_NnHa6rBCtCoggNqrKjxpoMohcQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RV2Jdujk0jTIsA0YHZlCj1sR2ct4J7SlH5ZYSpj7SSeCFcM1vFcNSMF_JGO5ex8KSdXhATXJGy7WjRGItWDNuWNeEv9u6TL47grSYEqgzRL42s2j7Fo50CTP_5UFNeqv1Dy4uyxXK6CPrgiTOP3AuqpQXzfvMpgXxgpGFIc4OtEbVpCPErAhcq_kmPDKIFYkUnRuKYZjBT0uOTVFr2hpbYpVU94dxLuJ9Bq4LnBSKT_kVYLdlUyzUK_DOrmnEI8XzCde2g4wl0rnxMWckY73cRyR2U_3zWBYB5rd761ZftDrIN38KbPiMfW5MVwgcYTtb3MBWYEzivl7RdC0O2nX-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حمله به منطقه طیر دبا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65645" target="_blank">📅 12:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=iBG8fuCMSYAyjYqYyczMaYuVAyM3K9KZt0kxHhtsk_aD8Kw2RlQMJnLMPUmp0Kdme4W1PcTV4BKP_AtYuCEH-ChoUeVoSmnvOe34UPgDc19iciVdCSgLuNg_ZIMk059YStwA1Pi3r43W139PTcbHEeBoisno0MEtS1nkmdlGRKYq-jSGg_z1psL_spp8-X8_mdRfWqLhwiVEBLnBsE3k4Zbg8260FdbaLn1T9Z3VICMxM_vKeZ29fXp-xCcOKQzSeAXfCzWsM9NGMtJICS4mo1vmjk-16BStFz1rWzTaow90o9hROFVstKerRtDNzKs7iay597QKeHB6OyHsOxuoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=iBG8fuCMSYAyjYqYyczMaYuVAyM3K9KZt0kxHhtsk_aD8Kw2RlQMJnLMPUmp0Kdme4W1PcTV4BKP_AtYuCEH-ChoUeVoSmnvOe34UPgDc19iciVdCSgLuNg_ZIMk059YStwA1Pi3r43W139PTcbHEeBoisno0MEtS1nkmdlGRKYq-jSGg_z1psL_spp8-X8_mdRfWqLhwiVEBLnBsE3k4Zbg8260FdbaLn1T9Z3VICMxM_vKeZ29fXp-xCcOKQzSeAXfCzWsM9NGMtJICS4mo1vmjk-16BStFz1rWzTaow90o9hROFVstKerRtDNzKs7iay597QKeHB6OyHsOxuoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
با توجه به اتفاقاتی که دیشب افتاد باید وضعیت مذاکرات رو دوباره بررسی کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65644" target="_blank">📅 12:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=R0HrcdBR3bfwOk07g3J7W6Qckxs51Boj5VS-YBR7izFMzQ4psE0cI6yXWSGqV1LkC65rp4s3JASqik8VDc1ua7uYAw8OQmDPfuTp_cnF-cNPQWMHqQRBgKuJK7vD40ogSxZVCid-UQY1TVa4TEViS2Eb-nXHUwZ6eouhxTzymjW_mLkfLoHWeBdlUC7yIWZXd7HD5lbv3vt9n-CHJp8KXUViz6eoeEEEJattonmo7RXscfKtOJTxeCIGxw-qzElTuWJ09VQEt9s_SIBZDuGBykgLLMdFbi8T1tv8Nt9DePWwf_Ko_uU1zM5wfnXDQOcwSj4GzZMXU2XIQj6k_wW89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=R0HrcdBR3bfwOk07g3J7W6Qckxs51Boj5VS-YBR7izFMzQ4psE0cI6yXWSGqV1LkC65rp4s3JASqik8VDc1ua7uYAw8OQmDPfuTp_cnF-cNPQWMHqQRBgKuJK7vD40ogSxZVCid-UQY1TVa4TEViS2Eb-nXHUwZ6eouhxTzymjW_mLkfLoHWeBdlUC7yIWZXd7HD5lbv3vt9n-CHJp8KXUViz6eoeEEEJattonmo7RXscfKtOJTxeCIGxw-qzElTuWJ09VQEt9s_SIBZDuGBykgLLMdFbi8T1tv8Nt9DePWwf_Ko_uU1zM5wfnXDQOcwSj4GzZMXU2XIQj6k_wW89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای از صبح امروز که حداقل ۱۱ موشک سوخت جامد دوربرد به سمت اهدافی تو خاورمیانه شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65643" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b78948a2N2FQwXwf_5xAhLIrYl4ktcphzLzbwncYa-qkwT5mhP9OpgCknlZRHjPcEjUl0kgfKWpHxZFhzgJuwY3Pzi79ReG9LCvjm1tXsIr_ae7Cc_Xei0-mwFy3IbjvHLIh_vy5l7DuFFGMUYDXWsPS0AUjLnwCsuKbOnF74qlDeftIkxzyAGy8PLUAT-ImuZ4yGoBKtxFI9wHgH4iIb0NmrvwtpGOOFQRp8sDk7hwWCY-kPDEVitgaw8dIg4Cdr83I22NxUwdMAVFcVkTgvU5rkH0Gp307OviNB2wbEElOuBuAeutEkMnOF84nmBLLWRmYvzjIWp2F_a3hKQvo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTdtrk2PCOREsxCGsUvIyfH7Gf3Yk6K8aQMIjUXzo95BBkrmiBBvvSoJUmNu1khasjMRhlqxpePJ5kuA1VRAqGQ2dYhzZJe-EUlZHlt-gkXrfMVc0KUZeqr4r13JwoHdFn4fAI7ODD012Qn3m0i33uyX-UAH9xhZzow0uSkt0IrsMTiy6VfqPVXX1gchSj36h0D2zlgaPfkuOfmcTp_4LJU_tH_UIH2Z5SS1yz3O7pkApf_rtCnMnEBdQfcGjzjrk586EKbcOU5nJxBpr5nGThLcpjAXaXUgAwBePlip7dQ0cvwCYKxNsGEcr6t5QSSmc_XPVqIQYo7xh3ng4nKOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5bS45onXVrV6cPxDL_KNgV4ezl55ekuyvtrFdueWR9LKnVkYfNd8Kic9j09P5kyUkwD4Ig4ETmRgLRzRGNKL06bJkomFB0gOaLtR7IY2pDc4VIokNVKTmEVxJlw9skeZbf8ruY_pW_stuBP57TrOvVreHQU2epyC8xjx7qHoBL305XjwTscdJjCekF_FbOMfXR7yn5y2kTOPanX9JYz2_sg7JUHjOlSL4yVbMEbbEhPB8viMSmqCIIGsxfgHHKtFdjrk4QYp1M02uMk0lS88SNn0TGIsS6wC1gDhuq70-Fksb1lkTQT6vdD0tZ8pIPtEe1f7wMmZP4GSLxrk0lnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_4Y3oQ9_SI3KwS81M90trDmWGnJwWx59J0TckGIbIILra_VF2VCIWALaQZ5MRsObIdVsjHsylP7h0Xv6j35C95JhxUCAqloC2cOWEllt73QHBesfimcv8PbiK1zzamX_s6LquMe4y4TohlWO6KPSZ3KAOdqECS4R1nBDhjlJ-LFH2YmL1DLfwVKpPBMRJp3CABg-mT3xs18AEH2p60UnKlIlNqh1x8UMYHui79GA2jO7O4iO7eI7ryIFWi_OunEWXqA0gPgVaiH1S7ZzBxJBTK2cKmr4tvccbCtWBEPWMhAAjQQDbrIGBnPQCMut4Al8ZrrIxMZHok_BI5H-Xy7rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حملات صبح امروزاسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65639" target="_blank">📅 10:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دعوای ۴ دختر تو بابل
😐
@sammfoott</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65638" target="_blank">📅 10:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crzGWzFyxDsPFNPT99xdlFEYodlg-LHVR5GhOwsY6gT0nQi9LeTVQFWtQceeegdm1C82SfHAPDkHhHOFy31s9qyjVFT7kFGdGRP7kD24IQ0jrV0UzZcgQKOrZRLvQ5A22Q06GxQygx4-LBOFHgCNzzvY8vxQ3Y3L1z09jnU4WdBg2rQ62pBC-uucuzIbHOlVvQKtBpCcu-vD85_EEUHbfJDo4NtqX9GNorYFxy7Ui4qpRLL5yyEUmBohkAslQ8LzcAu-jugKWX6bgeZ__3ExGl8bGm_nS8t8-v0765ucsH0cJhCZOJgpXcvXGMJpp-KnAVS2RbTs4TcxNgm-Knw-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری که فاکس نیوز از آرایش سنگین ناوگان دریایی آمریکا در منطقه برای «اجرای محاصره دریایی»منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65637" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">😁
برا رفتن به باشگاه بهونه نیارید. از بی‌بی یاد بگیرید با چنتا کشور میجنگه ولی ورزشش ترک نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65636" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JABd6lR6Ftdev3T8QkejodSQCzp5bVqu2B6XxQpw-NRKcY658uKz1NOgNAT8lWS_3fkWOwM49n-t5ek4Nue4PHDaMI6IVa5JlxNYBRl_jl8dz7fg-2WY2EbOAz6ZrCKw2Vz3dS5Cd88KCCSaGkSizt_Iy4Uv3FOuJQACJj7fVh4-BhSDNPtB_2pTiomqvH0v8BQ16jjXxfL8IMiJG5F0iHPxaNFupGaSay-y7NqGm-TU4ATC1HkzbJX7dsLxArS9Gfq9tzl8Nm2dg7HCMN_ZZejOyKv0IIvOab0X9QEB38mOj314d4hpvzjL2kiXHm2j1mOJ8CCdrltN-b4_p1fyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
رضا دالمن، دانشجوی کارشناسی ارشد مهندسی کامپیوتر دانشگاه صنعتی شریف‌بدلیل آویزان کردن موش روی تنه درخت‌ در ایام اعتراضات، با حکم شورای انضباطی این دانشگاه به اخراج و محرومیت چهار ساله از تحصیل در تمامی دانشگاه‌های کشور محکوم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65635" target="_blank">📅 09:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FczyT7WDTPXb160r1tvsa75jal7I3-HxUSsz6I-eZtEdDMaMGpnzSHf9zx4VufPxilfCpWxWAaNU0diPli-rkJWedde20Ua6sdH9AK2dUoL0gry7UExzvtQjrZhClyCsPJ7Y_Op0eR4bBMN8RHLqhPlEJ7lytQp-cgjUrrzpVFPKQ97K1GL1ZXcybsSrTNUTOxMhaRL5PKVbxbSu4PBMKH5iwN0AJzJCC6TxlK_RWV3aSmFqU9ptJBDRjELxuIQ5Blzojy1Dly_K6u0YMjEz4cznXQmIzYf14X3l4mySyMPY9WMoZjOscH2Xsklb0phyqkrsp8YXDiHidPoHIFKLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویر منتشر شده از شهر قشم
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65634" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=mmMSSCxR_kxtefdLmRJiX6SsWTkUeMgE3uhXBuaYaSfXuibp4de3s6FcTkc3oJ4DBWoih1unZwDrEqOmc1L0bZxDLoL6yXqqEhyXBCU12CThvQozN2DNFByjOmvxSo-FMR57v0DvOWJxS3W3tPByOgiaY9p_rKIc6kLKyi_bp--LX_e__U0p44MPfFNju-8ATv9XVwtCmzPeyJHvwkfmGFFs8KYzEGp86j6bQjSCG8R1E3TTTSDLKSThYkUm78K4cZ6lDgeAtML_KuwfBpNBmE8VmLRkTcEo2bFAyUutiLbRWbBD2y0M3B3Yy_DRyHUXlAlcqZTLE7rWHpDXU89zZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=mmMSSCxR_kxtefdLmRJiX6SsWTkUeMgE3uhXBuaYaSfXuibp4de3s6FcTkc3oJ4DBWoih1unZwDrEqOmc1L0bZxDLoL6yXqqEhyXBCU12CThvQozN2DNFByjOmvxSo-FMR57v0DvOWJxS3W3tPByOgiaY9p_rKIc6kLKyi_bp--LX_e__U0p44MPfFNju-8ATv9XVwtCmzPeyJHvwkfmGFFs8KYzEGp86j6bQjSCG8R1E3TTTSDLKSThYkUm78K4cZ6lDgeAtML_KuwfBpNBmE8VmLRkTcEo2bFAyUutiLbRWbBD2y0M3B3Yy_DRyHUXlAlcqZTLE7rWHpDXU89zZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک‌های پدافندی سپاه از جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65633" target="_blank">📅 03:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام ارشد آمریکایی به کانال 12 اسرائیل گفته؛ هم‌اکنون موج دوم حملات آمریکا به ایران همین الان در حال انجامه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65632" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQXaGzBStZZjZN2IUgPlE8h4OwsHmTLciSOcPwrbcv5vz2XRPoNSZ21OM5xxGu1E2kf45qz0YUuLh8FJw65OOC5LeV230fL7IPgoYCNRrN1--08F-OpqgprFiCjm-egVBjDecxmIFmCTffgO0BM-0Xyd0d64ZW4ukLiKFzxBvsXQN0KYlVTOFNzTdXqC9d4LPH4PoAvRsJXJ_T_M3pAjGjbv7n1PdgjW0YMyp81QTRCfuPqgC03kPD7QjaeDSSZjNVx3VdP4yZUg-lqyI4gc1dbn5ga1RY5P9AHq03-mbsol1q24UMyptJcB_QxkO2VjzIqqQbzibxnxYJ0JDsH56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🗳
کانال رضایت ها :
@AtlasSmartTrust
🌐
وب سایت رسمی ایران :
AtlasArbitrage.ir
🔥
ربات رسمی  :
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65631" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65630" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhGUdyUyEoUEEqp8XF-gh1MaZIfmQv_93fQSpTz51fI8xxSjE94FkrUxKtrXUTddmMd0c_O0KXFw2rrnI4XNusSBH0RFcPhHkJwou1AvmYzhywPhpcT2g3WXl9KGtcufp1aq1byHrynX427rCJdOP-tOFEXrrev1yWxs_hi1r4mqwJz1Zqpk7z0_-qYWmr83HFY7ocicO77D2YypW6FaLeRSqzFyf7XmObkfo02WYfnUMOOS42RupJub68JyaNsnFfb03TnI03Z7qgRNt7v_pt6RN5xbA6hdSzoc_w34RLinhGacfdIOhEvWLb9oJp72GmbbORZoDuchkVL0eT-87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65629" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
گزارش ها از حملات ترکیه به شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65628" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65627" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=YTyUqcjNm4XJF7CNZ7dkvkMjJyVFc7-CQKhsk1V-cTmjA5jj8IJ3oL_0TWbhOeZhw2z4sRMrJOozKZXVCwwK5HlfjLm41vMj5LCQOsmQU5nME4-XPY9nTmcMRDEyJxy4GXfHBq7wPR178jgurdItYKsoMuChWC4k5S71HLtYCHE6eGLmI6lVbRHY_fihA3HnaYmKbyvvaGOzS8scgztcexgHxAsp9mX0rARAl6WLhkrGVKpvvo0lg4t6t5pGbREbjluIkDdrMbAOtB91PpQOa2w1JfF-QuytnkwkrlT_eIpsWX5Qly1k_4xZ4ZWs-RpGumCa08qlzAyQAY2guKbEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=YTyUqcjNm4XJF7CNZ7dkvkMjJyVFc7-CQKhsk1V-cTmjA5jj8IJ3oL_0TWbhOeZhw2z4sRMrJOozKZXVCwwK5HlfjLm41vMj5LCQOsmQU5nME4-XPY9nTmcMRDEyJxy4GXfHBq7wPR178jgurdItYKsoMuChWC4k5S71HLtYCHE6eGLmI6lVbRHY_fihA3HnaYmKbyvvaGOzS8scgztcexgHxAsp9mX0rARAl6WLhkrGVKpvvo0lg4t6t5pGbREbjluIkDdrMbAOtB91PpQOa2w1JfF-QuytnkwkrlT_eIpsWX5Qly1k_4xZ4ZWs-RpGumCa08qlzAyQAY2guKbEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پهپادهای سپاه در آسمون عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65626" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_JY4heXs6A0Wd1CBMuDT8QQ255W5-oKz2LGD_Oo3bgNTx1V1c6EQdFf8zq0TL-seONVSHbIMYW5sO-om9HFl5ARqm6QAEqMwEmkjRXpNKYsSNpa9VjmEQTuX5g7jBxGSGc6bTrrM8eGtGJpsDKOo73sTJHqGPZzUqAKN0vieJgl7ooIhXX9LCzwsyBFahmS3zIOe8H6XPgHfIMka8Zh2H8Vp6Qtx9Ur2GyK6DWx3Da4xYD9Xif78KK5hcb1Ril35xymNkxZZvjXE5ciEg8LTT3oCK60i7akUEmiMFhU2kzNM9lm6Uits3IRMCO57RzCT-kCdyzbCVGQ-Z1HbSGrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار تخلیه سپاه برای بیکینی باتم
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65625" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn3F3zNbmjzDujaQbbCKCRW6uOW5HdipxKlwZ5K2hu2g7nwBZ4kljumW1gzIRi367Tc5wO2wHo4XbD55crh0G8milvjG4KkoeGfBtwhgifbXYauWlJMImIG98o28dm7CJPu2xSWMhg-Zen2lDSjc5gzcQGwMMa78cE4GQEBlmuxytgNU7SuqCivRD8Z9GzDnLeFk8jVV_Ug21OUMXuTvR-Q-vadoGrxvM4-NYJu6Dc4FGcvttfWq-8bWBYq2QG90cOxgW4n9qrd9PbdgVhVMt8gH0eMAIPgtkZA0Duz0s86anOzXEd5lKvbeaqRswv535OJBL8nBqME2HY6bYUpSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
علی قلهکی: برآوردم این است که سنگین‌ترین پاسخِ ایران پس از آتش بسِ اخیر به آمریکا داده خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65624" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL1_LVh3eYSM2GwUZ-VCzBA5O-F7SM2LRiArcjCML5SJxAwv3LpeJPXREdext3U_vnEWrWCa7wry22KcNCSxMu-gpsGf3yQl3X1ahMesTheekm4Fot9C7bMfrrwhyvqP8cDP6txMOWgBq-VEvTKRWWI89ZQ03p0SCOJw-Qv0QOKgup8u9JQPBcNDmkDhh5qXTg0eOMRWehGDlwIRT9UKl0ME1fMtveZje4WPNnjRS8Y6Ow9qABPUb_K5WfMlfZIUH_vsMTGpviqwOVpgBV4Ao5JD2Oi9L5CmZHwBrmKM6XWjs8GXQsY89coKFvYcKkw3iaSt77Ly0Cb5Pw5dRFV3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شید برید سر درستون کنکور به تعویق نمی‌افته
✍️
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65623" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65622" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
کویت و بحرین هم حریم هواییشون رو بستن
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65621" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
حملات پاکستان به افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65620" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2z2Nj_mji1S8oL5wgeKp11aASDIU0hO7Bh-B1cJmTbyVJUoEvjxVLA4bLq-NUn853HOTQFup4t9Eo7rQTyB-gIYfQPJnzPg-ByKoYaGiSjn0ROajpRVF9Fs-ZxkxX-WPWO8wd9dOiHucRRKcvCkl8K4DEdTbB4oMw5urqlB_H4vT4y-Usm_8dbRp29UixdRC_51ZNWUC6srOLZ_TkVLkg76-rSzUnF4eLwl_ELvbIlOJ854hDtBybRRlC5_p15VYbt9GJrrp-3SJDxEIX9_qluEhUnAr2jUWM4SomgbmQ05oOsY0sqdDtZ5h06wnSSeFmnfYCFpOyOuOsh9_IubmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65619" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65617">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی قطر بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65617" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65616">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇱
گزارش‌ها از حملات اسرائیل به لبنان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65616" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
سنتکام:
حملات نظامی علیه ایران با دستور مستقیم ترامپ انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65615" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65614">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود! #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65614" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65613">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛روابط عمومی سپاه پاسداران:
ارتش متجاوز آمریکا به ۵ نقطه نظامی در خاک ایران حمله کرده است و باید هزینه سنگینی بابت این گستاخی خود پرداخت کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65613" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65612">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ناو آبراهام نه تنها نرفت قعر دریا بلکه با موشکاش قعر مارو داره میدره
🙁
🙁
🙁
#E</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65612" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65611">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیمای جمهوری اسلامی گزارش می‌دهد که در چند دقیقه گذشته یک مکان در جزیره قشم هدف شش حمله هوایی قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65611" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65610">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از هدف قرار گرفتن پایگاه دریایی ولایت در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65610" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
ترامپ :
فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65609" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
گزارشات رسیده از حملات به مراکز دفاعی میناب
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65608" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65607" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
آمریکا گفته حملات با موشک های کروز و تاماهاوک انجام شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65606" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozbnLFGUvJQvMYd-DeuXGLIXV79eko1E9Fl54bLpKlRpbHieAtVZk_piHcHUIT4iD2PRmeBW33odvTa5OVRqmvMz3q0NLpFeiM6_INVEz9bM-vt7EXprryURpVmLSgbP5YgG3tiEckA8EKZ1P8zLI0EoqW2EXBpRm4UftTHlbqtVvpmGyNUGhNA4WUhpOQ7fM-2eZY1HneZCl5Kj6nFW8zOm_A-U7TSVDpz0artSni4d6pACPRdTSfO3JEt1SnHBQ9ZWc4zO72n-7rmtuc5U9B9NMqMoLnqS3evecqP3z8cbRzm1z-tJLhDc_2omHUC5plD4ppRNSCv2ndkxENJwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65605" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود!
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65604" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaleh</strong></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش
اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65603" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtbPsB8OKGx9c_WeQXVWbB0_sBIsYhiZxmRODhuvrpvYEUZ-2kLHNXtT_nK2Hi5mh2vDLiK6uSBNV2znu8cgdsgy6I4t3RxcALgD6PIeiWJd1xOkHspI-542cVt8vZlLzc2dZFG7ulxWw6UHl59YqHHeTF9IWQekCb7_MLi_GO6iA0YBgutivmbWoqMLNpvEXGW1LAW0GJ7QWW0zRFjuO1Vato3hqZTMro6ZStPiOB5997-WvpZK8-ixPb_rZ2bEH4gvvHfN_-9wQRFooLLWb9cQQckId8CZDla2Yzko5FQaT6qy75TlaDF4U0DkdlvQtFLNxG_YB3ZFF5ZyE4xBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65602" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
گزارش ها از انفجار در پایگاه نیروی دریایی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65601" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci7Hw2xCo0ViQ-Opd3s7_LPjeb-Zs0HEtEQSq4jpN_r1DHvqsuMbC17h_HtIZH7sL984LiBdhkF9dLeNZ_pQRiqlWFi7NeQA1E1MXQcgS8VMgqhLEuuSlVCEFKuXOnYPlLzm9nd0VBaK_f_1alCP1lZS7STp9vp_HIglHPtNTN5UrO9CwAOrvVe9vwXaYDUBpbxOFcs3vdV_uhHLaKz1PMbQjBRcMFMFml9R7N5_SYpjmmIharDnMVAi0pHlyGc2xk-sqO2bLSo5ar3pfaytcSNCqlCmOrj73AyWARZb-sAm0JhoTrtthGbieIbST6XowXZ467gmLhhcHz3MTjA1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65600" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65599" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65597">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65597" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65596">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMvGrCrEME-SRstD5D5dmHEzJ4eVpvi9cFQqwqa5ja9UymzA55JVzXZ8UvxZkWxhERbQdWkKCaN329eGBbUwT6tFrz_YfyznvyHt3zi4KoqSTJmlQ8fc0U3S9jWpYwBhcWsrV8hc5MMPgdP2oULLuYwxVcpYDhnhug15PtAtag0NzGCdqzajaIw9p2rXy6skfySEOe0YT_MvQ4wQ2KAZ9ldufjKI72NVl76kCkQ1D8f4rFecQikbkUh-F9-xzogzelSSWMK6iZwqAy15VXPFI86Q1kM_t0PoQr0CjId0LqLOz-hgYzisFariMY1UvqZLh3V9QyP4FbhbpWmPzaUUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده سنتکام، رسما آغاز عملیات در جنوب ایران رو تایید کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65596" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65595">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65595" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65594">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
انفجارهای شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65594" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65593">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از هدف قرار گرفتن پایگاه شهید راهبر در بندرعباس حکایت دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65593" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
