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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-65778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWgI8HsaOMs9e0MeQt2BOK4NK-F-MM_OX9f7lJj1FMyX7W2cyXsr7juXxxxIYQxzTMRS9C_wpT-XCgnWrZO0QfjI-UVmcWzmmkwBxAbYRlO0dVdAcdqH8uTF3A3cuIpr188Z3dDsX1vNLNcdq3AQBs-4KlhY9wYQZZt4mA41y5gF-Mxml8v6Kf6UyKPr4cROZUtJGJJSLYe7J87oUVpR5gypSyEYiOuAnHuV_m_ctnbSz2LR8aSfBZxZJ_kefuDhijaeXXFnXuhUDhiOUSiY5cUWGE_rSG2JPrjF9GFaxiWbRwfkNSxeatYdCU9WVi84_ZXB32oLBzblFwT2qugabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت مدعی است که یک کشتی جنگی آمریکا در تنگه هرمز هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/news_hut/65778" target="_blank">📅 01:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTnZiFbmMP6i4MeJTSkvl-DlepY9z6Ifou_ZqavCIwdRJz7g2hR44u1vOBf6cX4ISpx2TkAGhFaFOZzh6ULzNgW_icD79juoMOKsSE6koyy20Y-WmbuKMxxQoiHKSwW8GDIxSGPjUNMHswgTs23eFPfeeUCeihmJgTlkQRKbKFX2iWHTj7CG5Q48umek4pgGvNkW540I_fBZJPmSpVKNgeVbqVoObjbYr3ePxdxkzMsyTecbdFJpQOjMS5gFDfjkg42qQQn81v7t4_EoPgxqusiNN679HjoON8VNMtC34HOu9pvCpuwC0xGaaT8TMMjQ1gZ4H8hmyYW2jPyeE1a7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خبرنگار المیادین از درگیری و تبادل آتش در تنگه هرمز خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/news_hut/65777" target="_blank">📅 01:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65775">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2C-4gOBRu15OzSP8yYzUHvWCU2Z9jLZ9xW2U_4F9QAovQ9mwSsLQHATN9cIvFCIqKV_FpiBzSj8cVrV3rnYZ3Xqnjv7iT5ASHaz8RoqHPx_S93lq9EBVbcA82fw3hqzf0_jjInK7gs3fuDnG-XcOLCT158i1qBS2aicdO11J3zjKSV6MF4gmgIoTGkHCmX3rayn9eAL-WQl200dMBCKRkTl_pa23OcnItQrxn1gn_RzKtER0SORNApT9A2LDBD2ntjG1U2n4U2k0cffk1TjOCuNMwAJzRrp1OZI5S2ZLsZjETSOdGcVaFcUCFo5Sz6s_4G5PuzHb7qc7KMuAwE87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzvRyReV-YrqdcQle90sxmWkXmHSTwC3193pxRZqqb2VXiDrYVzdqc_pCobrgQTHtHkzh7HUD03p7M1gYZroPUi87sSRsl0CrCzpEq9Pi13-V1u7Q9WqYfyAEAMbMZ8zTpu1j5wNonzirh3-uc1JgVebZsDmVAPTPDSWeBPwQAWjUgXUveogDU2-6krKnfacDooaj5TxtCq-EaroKmSu975besElU6r7IUifDNDcyTBh_mKNeSZ_7zlAP6C8yTukwYuYm_556aa61jTfSsHauI3DQ-kqDFVcLq2qVxaxyOtZHyvzXgj2jLdJxuzJETs79YRT5zrlWUY9z8mPZPz8-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
دو فروند هواپیمای سوخت‌رسان هوایی KC-135R «استراتوتانکر» در حال انجام مانورهای سوخت‌رسانی در جنوب استان هرمزگان، غرب تنگه هرمز هستند. این استراتوتانکرها از پایگاه هوایی پرنس سلطان در عربستان سعودی برخاسته‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/news_hut/65775" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65774">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB_eT11ZU8C5Q6cZgXZ1Oc_Gc9xDFqyyPxvQ4YvzUgGJE2lVJeEF8rGIrscDRfCClASPtF6iN_qUdX_nUCrfcCHxFCKkRjQ79PSbk8O4qyVJ9fkFEco-bM7IH4F6YciQ5Fg4ULszv6cGPuas7YEGqOiWmupJ0Bzg9QM1fCs5luHkZy2RiEsVWcd9lRnNNBe9hdb6jCnxSluUZJAAuZ05FuEXyQD_NP_MwR2R9J78nqqVnEt0qN_kM6_FUeZ18mSpj7VnyQfHQ0wUQEYL8QllYyMooy9ZQyyQQhRaPZ25legM_sReH11EqigaOQbejpgtH14fxhoTjlNHzpfM7Hko8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دود انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/65774" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65773">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=GTTBUrz8S-i3V82lYRZXlz1rOEVbe_QZki2bOSLA-vHQ7_7bYRARVgNCs2MB8kCP8pNhSWJGwtnN_KB_XE8C_4sgtZ6Yf59a0fhCWMji_Vo_VjnVadQ8aWrRQknpZBio7R0WTqqwTjuBhQpqqH40ZdYBcjMe5x2CZX9Yj9L8ifJnunoMO87k3xIbbhjarOClqUFkf_imLOrJsvCGB61nMY_1JJX8qqUVp6XQdZ7FAiyKoWVb0b6XYETkKID9Z7N7wReRJh9KsgKywuNgKwCu_I18F5scKTl3hrWH_4RE2vcbmlCqD_4DVQgQUIdqo60nRQsceMO5ez7MmfXBL5tRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=GTTBUrz8S-i3V82lYRZXlz1rOEVbe_QZki2bOSLA-vHQ7_7bYRARVgNCs2MB8kCP8pNhSWJGwtnN_KB_XE8C_4sgtZ6Yf59a0fhCWMji_Vo_VjnVadQ8aWrRQknpZBio7R0WTqqwTjuBhQpqqH40ZdYBcjMe5x2CZX9Yj9L8ifJnunoMO87k3xIbbhjarOClqUFkf_imLOrJsvCGB61nMY_1JJX8qqUVp6XQdZ7FAiyKoWVb0b6XYETkKID9Z7N7wReRJh9KsgKywuNgKwCu_I18F5scKTl3hrWH_4RE2vcbmlCqD_4DVQgQUIdqo60nRQsceMO5ez7MmfXBL5tRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/65773" target="_blank">📅 01:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
وقوع انفجار ها در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/news_hut/65772" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJajVGqy7l5dvNdmn2Ycj9quzexE-feSRYZ6eiBu-YkmsDx5WZRMKbkkT5zPWQM531hbsFnh7K5Jfz0BJqqydtSZog607iDgjko0GhuaWX4tof6hMBJSBkyKsNy1MVO94brMfSVuqPj-7aZC9izlBY7XRqYbJlRVmcsOrrCO9EFmh5vXnhXxTnpbcpid49VSlbtZ9liSa52vVeQjonsYCqMP6kP0700SnzAAKMeTYNlLtZwtZ0havVGxBFARhdlHfR6BbxU2xXgxCgfP6xxiORZOr8UCF0jw_p-Oo2ru-fu_Ba8tmjMvKuR1MJe5vNMY2sOPMnmnGR8Vs2EvfV_sSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توئیت جدید سید مجید موسوی
@News_Hut</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/news_hut/65771" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
گروه هکری حنظله وابسته به سپاه:
آغاز پاسخ ترکیبی، قاطع و ویرانگر اتاق عملیات مشترک فرماندهی سایبری حنظله و سپاه پاسداران به دشمن تا دقایقی دیگر رقم خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65770" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
حمله آمریکا به پایگاه شکاری بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/65769" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HD8vZMxvSps466z0pcnd2pQtrBoIRkAnSUkysz5NlWy5LG47KNn0YtQQC6hc41nrsDalIoKi_3aWuxbLXY3r3432PlhmDQrfr_mIHRmEPM0er1CXvNOYtfW4L-AxmtUSCkwNy43BqapnISvqpuD48u6FJtp4z7lp0eZed4XhOVGKO9dvsOpCfqaM0AwACVkzQxkc3jS-gAOHIWRt8KTSlhYig_9Ox4j2pisyDV2jKl9yjsL8zrjSh4qlUvlzhPYDECKdbUI8SpGFebYFkJ2Ov68YgWHXzAGR2ODA7S4eUhHTEXOAifURGBMt4buRn4RXEX8QLIRedTjvGuf66IPk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا قدرتنمایی کردن برگردین حمله کنسله
😖
#haa4m</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/65768" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری مهر گزارش داده که میان نیروهای جمهوری اسلامی و ایالات متحده در دریا درگیری هایی رخ داده
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65767" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHhoI3ABU6r-euvhU1UOLTooDAlJ39l9ireTxjJtyFN7jDf0zRryAukb6JbmtubyUGc7hunnhwExiKthYbvjGZC3h7LLJofnN8Ip7Je8R591--nGgfmVdsm1easYJTVoVP02YRlGCIGZZVu6OSwJ_w9_ZIQCNYOIRqYOB8kMA23_mitImcSrp7--cHMXlyi5_FeUyypmTysiqX9AXxSi7Edp3vWJBP9hObVmPqVQnE78Y-PQALgEHZ15MgOxiesz6JRc6FCUocttkpc-yI51SXpw3mzvrsd8Q0vIM_qO8no5ONTJ-B9Q0IxSYE432-dUZp5Q-jcaG7hwzYqrQ7Cmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد باید با موج انفجار کوبیده شه به در و دیوار، نگرانی چیه آخه
#hjAly‌</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65766" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
گزارش ها از حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65765" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
منابع داخلی:
تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیاء در پی جنایت آمریکا و نقص آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/65764" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
وال‌استریت ژورنال به نقل از پنتاگون:
این حملات نوعی اقدام از جنس «دیپلماسی اجباری» است که هدف اون وادار کردن جمهوری اسلامی به ارائه امتیازاتی در میز مذاکره‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/65763" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
موج‌های دیگه‌ای از حملات در راهه و درگیری فعلاً ادامه داره.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/65762" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده #hjAly‌</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65761" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه انفجار شدید تو بندرعباس همین الان رخ داده
#hjAly‌</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65760" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65759" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3VLTyCu1y5DJpANhkEo51BL_AsRsFqdNPvYWXhu06RhI-fU7RLEguDtysHLFCkHdCu5CWgEzpDpIaZJ3Ql9X0xosLbOL1O-mpX5cZyCacKo-01-iNs_hWJCVrHiDW-cOzrql53q9u1xwnxrMjzpcwXtpJzLBOIvCAhArecBriNm90IEDh_gR_8tf3SPilzmZdjv9yk5yTgv0PKwC6-qQX_Dvr-DH-br1jfgLFKFadJZ735lbg85M38ZyY7EeSJ2S61tvobVlL2mvhpBkCl3Qz0-z30ZuQosQuk4jy1ejEv-KCVVlUULOTjkDlJFcFB1nBrEVUHx5QfzIOhq1FmK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا وقتی یه ترور کله‌گنده تو کار نباشه واکنش سپاه شدید نیست، مثلا دیشب یه پهپاد فرستادن بحرین گفتن خب بسه دیگه #hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65757" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65756" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
اون طرف اسرائیل هم حملاتش رو به حزب‌الله شروع کرده
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65755" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
حملات مجدد به میناب
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65754" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تا وقتی یه ترور کله‌گنده تو کار نباشه واکنش سپاه شدید نیست، مثلا دیشب یه پهپاد فرستادن بحرین گفتن خب بسه دیگه
#hjAly‌</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65753" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
مقام آمریکایی:
این دور حملات اهداف نزدیک تنگه هرمز هستش ولی گسترده میشه در ساعات آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65752" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65751" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی غیر رسمی از وقوع انفجار در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65750" target="_blank">📅 01:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی؛ سنتکام:   نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، چندین حمله دفاعی دیگر علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمیِ بی‌دلیل و ادامه‌دار ایران انجام شده…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65749" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از شنیده شدن صدای انفجار در اطراف قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65748" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5U1Rp2v5_A57NoTF_bVA7LVDTzWZrGBHTudNoWU3Zi2c43aU76cQ2nktGzVGNMKzKfUvJvnBZicS_UKAZDg9aBZcHvg4j1p9t3YZZjh5I8XMdS5FSHJw_uaDOsVDtf3pbDk70xAkF59iGRyedtda_VrTCQwweQAugjDBgqLumAxOY3aY8SJoRcF82W6_-vMbTKjdUxJgwAEmG8pwoSEfVI4NBbKORt1q957eNG9H47KiNTpc9d9gNFlIpJNWqsndoBA3IXOBNzNXKt8aNhdbVk7jxr5wZ-bpIuA5h_0yXcxyd5JZv6Dk8uKuXg1JzJFY-KEUf9pgI5GNiVn_rnuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ سنتکام:
نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، چندین حمله دفاعی دیگر علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمیِ بی‌دلیل و ادامه‌دار ایران انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65747" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
مجدد، انفجار های شدید در بندر عباس  @News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65746" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
مجدد، انفجار های شدید در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65745" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
انفجار ها در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65744" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر از فعال شدن پدافند عسلویه
خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65743" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65742" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
تا اینجا تمرکز حملات به خط ساحلی جنوب کشور مربوط بوده
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65741" target="_blank">📅 01:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در میناب
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65740" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ رسانه آی ۲۴ اسرائیل:
شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65739" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در میناب
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65738" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65737" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری ایران اینترنشنال :    جنگ شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65736" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
فعال شدن پدافند در غرب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65733" target="_blank">📅 00:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست اهداف فرا منطقه‌ای رو هدف قرار میدیم  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65732" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پاسخ به حملات آمریکا دیگه فقط جنگ منطقه‌ای نیست اهداف فرا منطقه‌ای رو هدف قرار میدیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65731" target="_blank">📅 00:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
سفارت ایالات متحده در بغداد: از عراق خارج شوید
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65730" target="_blank">📅 00:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65729" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65728" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65727" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:   سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65726" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuwZETNtFFZTqow_eg4Y4u92bkTw6TBehtm8sbcji5XXoeg6-BiVjqnwQhKFoN-tghqgMlEnlYfJNiRkuXHdRzLh9uu_T2ht3rxf0GFVrExQlaJn8TtbDoQ2YtgWAIkMDqjIBvRQ8AgDC7vgntG-xA6GbgoplqozdVsQGZ32LuHnjwCBwJNaY6f0uIC1gQnk2H1PdgQLtRojJMlOmIptysRGIYbjab6syl-MUxupxP765tvSrZxRCgqffaqvpulV1KHUjRS5SIGLrT763VaO-kkNS8HFvA0aCQuEbWFazlOwwU3zIGyfp3d3Ox9kr6fLgikdMnDXs62GTqvKts_bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجور مذاکره کردم که تو آتش بسم هرشب جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65725" target="_blank">📅 00:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=Dw5pF1YqJ8vngPYKG-IzHVojiJUQxnSELq8DhkLQsltUYSdem5lqTJkisbranauTxc4nFBbKMgSjGV-6egZfr9K7P3ei1I1-xAPt01NUCFFNiXddr6FnS-E067BU9soBgExPIMSoibOuy0F5ur8kYMy2gLtgkdLpWEWYqCgkQgAicZphQC4gmG52GZuQy9CK_TEjKKfXXJNy5OPNHgIOHj33R-K-X6FGuU3ZPQlhmEcawjB0x5iF_a0JMHnUAiIxZsdBnnS1YH_G9hLk8wpLS_9pNTAKgMVhRcUev9PBsVEwwt6LhZ_qtwfqJIQh49JvAmB8fbrfFsnrvScdtwvKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=Dw5pF1YqJ8vngPYKG-IzHVojiJUQxnSELq8DhkLQsltUYSdem5lqTJkisbranauTxc4nFBbKMgSjGV-6egZfr9K7P3ei1I1-xAPt01NUCFFNiXddr6FnS-E067BU9soBgExPIMSoibOuy0F5ur8kYMy2gLtgkdLpWEWYqCgkQgAicZphQC4gmG52GZuQy9CK_TEjKKfXXJNy5OPNHgIOHj33R-K-X6FGuU3ZPQlhmEcawjB0x5iF_a0JMHnUAiIxZsdBnnS1YH_G9hLk8wpLS_9pNTAKgMVhRcUev9PBsVEwwt6LhZ_qtwfqJIQh49JvAmB8fbrfFsnrvScdtwvKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:   سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65724" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431e022a4d.mp4?token=RLVur8brdnVnVODPoW7BmT7fDG6a_R1S95nG6wsS64o_erkqsgOaibgUoE9SWX1ZWping5AnyKWzt7ZrghHegdVHLy66LNxtMl2HaJ_ormwc4vHSvTWKkWXbOys_Rv0JVw_Zus4HKpy_IhyV3Tf8uwAdfXI7t_p2Xbb_DNf3eJxyJfOI-q7tRKlIqv7RJLt5oniMv7U22d_0Kvi4KH_XA0_kU2MXKqaJxNLCn6b6gDOYtzYToPKraYDOrdMv2zqA3fR-Be8W4r7piQJmU02y9yHH3gVisaqxaKrTOcW-7VtUQ9Pg7Yj8xTbxNjknqgW3qFvzeMhCzZcya1QO0Syutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431e022a4d.mp4?token=RLVur8brdnVnVODPoW7BmT7fDG6a_R1S95nG6wsS64o_erkqsgOaibgUoE9SWX1ZWping5AnyKWzt7ZrghHegdVHLy66LNxtMl2HaJ_ormwc4vHSvTWKkWXbOys_Rv0JVw_Zus4HKpy_IhyV3Tf8uwAdfXI7t_p2Xbb_DNf3eJxyJfOI-q7tRKlIqv7RJLt5oniMv7U22d_0Kvi4KH_XA0_kU2MXKqaJxNLCn6b6gDOYtzYToPKraYDOrdMv2zqA3fR-Be8W4r7piQJmU02y9yHH3gVisaqxaKrTOcW-7VtUQ9Pg7Yj8xTbxNjknqgW3qFvzeMhCzZcya1QO0Syutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فوری از پیت هگست، وزیر جنگ آمریکا:
سنتکام امشب حسابی سرش شلوغ میشه؛ چون ترامپ گفته قراره ضربه محکمی به ایران  بزنیم، و دقیقاً همین کار رو هم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65723" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
ترامپ ساعتی پیش با تیم اصلی امنیت ملی‌ش در اتاق وضعیت کاخ سفید جلسه گذاشته
جی‌دی ونس، مارکو روبیو، رئیس «سیا» جان رتکلیف، رئیس ستاد مشترک ژنرال «دن کین» و استیو ویتکاف در جلسه بودن.
موضوع: ایران
@News_hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65722" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه دوش نگیریم؟
#hjAly‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65721" target="_blank">📅 00:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پیت هگست: بمب‌ها رو تق تق تق روی تاسیسات کلیدی ایران خواهیم انداخت!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65720" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65719">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnz-8GmQuDiZ5KsK_w29ncGXoE0JN1r51Lo5emsYDBFtYBvPrbeFJoqktrRRMvGEmtkdZRVZtF0KE1rFD5gSRpfWEJIXG5LT727boIQxotorhFLtqiGJSo8Mc3GfjwuYo-Hroe0AuOwpEvABrNrny9Dh-aidKxOjbvqsdVhuexERxhbZbDvqPmWoztnwjM8rvd1k47pdDATHjuCXS2Ci-YO42qC6HZy8BKAto-kshG20aHgdu2eu5UPnwXRa_tbk-3XLEIN0OBEj5t40NalbMKtnWYnGDm_ZfoLiYExpyy_ouAsCN9ZqvWpI8KwqueSOn4O3fzqh7MsF3ymK9X1DtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری؛پیت هگست:   ایالات متحده تأسیسات اصلی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد، شدید و آشکار خواهند بود. @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65719" target="_blank">📅 00:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛پیت هگست:
ایالات متحده تأسیسات اصلی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد، شدید و آشکار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65718" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
پیت هگست وزیر جنگ آمریکا:
همانطور که رئیس‌جمهور ترامپ امروز گفت، آنها معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار را بسیار خوب انجام می‌دهد، بهتر از هر کس دیگری در جهان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65717" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨️
#فوری
؛ترامپ :
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65716" target="_blank">📅 00:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
نورالدین الدغیر خبرنگار الجزیره در تهران: واسطه قطری تهران را ترک کرد
به گفته ایران، سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است.
واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65715" target="_blank">📅 23:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
باراک راوید خبرنگار آکسیوس:
ممکن است مذاکرات در چند ساعت آینده کاملا فروبپاشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65714" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
آکسیوس:
عباس عراقچی، وزیر امور خارجه ایران، به میانجیگران و ایالات متحده گفته است که برای دریافت پاسخ به چهار یا پنج روز زمان نیاز دارد.
این ماجرا به یک بازی انتظار دیپلماتیک تقریباً دو هفته‌ای تبدیل شد که در طی آن، ترامپ به طور فزاینده‌ای از پوشش منفی و حتی تمسخرآمیز رسانه‌ها در مورد وعده‌های محقق نشده‌اش در مورد توافق، و همچنین انتقاد تندروها مبنی بر اینکه او در قبال ایران نرمش نشان می‌دهد، ناامید می‌شد.
بدتر از همه اینکه، ایرانی‌ها در ملاء عام و خصوصی می‌گفتند که انتظار دارند برخی از دارایی‌های مسدود شده‌شان از قبل آزاد شود، علیرغم اصرار ترامپ مبنی بر اینکه این امر تنها پس از انجام برخی تعهدات صورت خواهد گرفت.
این مقام آمریکایی گفت که ترامپ از این اظهارات ناامید شده و موضع او تغییر نکرده است، اما خاطرنشان کرد که ایرانی‌ها می‌توانند با شروع به برآورده کردن خواسته‌های هسته‌ای ترامپ، میلیاردها دلار از دارایی‌های مسدود شده خود را آزاد کنند
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65713" target="_blank">📅 22:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آکسیوس: جمهوری اسلامی امروز به هیئت میانجی‌قطری اعلام کرده که حاضر به برگزاری نشست سه ‌جانبه با قطر و آمریکا نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65712" target="_blank">📅 22:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
خبرنگار الجزیره: حمله هوایی اسرائیل به حومه شهرک زلایا در غرب دره بقاع در شرق لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65711" target="_blank">📅 22:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65710">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw8-BO7j4bK4a3DNd59AoQPwpwCJET85AsAFMjoF-1_16AGMikGxrZonYQwzclLYmvg1YPTaD2NOfvBkgWJgcctRPn-9Mchk_rYRno3rSKRkiM0bqJwkscLEjDbU_9hrNY4t2G3I4_Rima9sFvMmN3_w3ZwnYgICjegf0Fp4QtUu3c9wWq8QqGmy75YAjEXoEPPzOobOGJ2Bq44mEJEGltVcn5ZLebny_ONU4qrQ0DeM89rmJybVAjw1EziOvdQE65fs3LSPKqNawLnBw6ep2PqwrJxYnyRKIhDiU4E8CoB8PBwMfEcs5hpU3L8aDDM6jtkp5AcKX0lfPJXU17nm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم عزیزی رئیس کمیسیون امنیت مجلس:
ما از جنگیدن با بازندگان نمی‌ترسیم.
تعداد تلفات آمریکایی‌ها بسیار بیشتر از آن چیزی است که ترامپ تأیید می‌کند و افزایش خواهد یافت.
این بار، جنگ محدود به منطقه نخواهد بود.
خواهیم دید چه اتفاقی می‌افتد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65710" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_A8IwkdDYpJkZwakK7aAorFqOUcXhkIX2YGbH4KDA8Y_bVOFnqR6GkErkUmi8Vzdm7K5YXIu_XMoSIDt48HvyM3_GU05CYromp4eH-C19oXnQA6BNcTNIXMhBy4LyprBaOUjRm4BfyTc_pTgX5LGnROEToh8ExgMZNPL3qc5Srnb1EfGKhlm7cziq1p2aCv1k5iPTQe0vNJ3kgMuKLVk95ko00ORQ6g8_KzBiYJpR8umiUoTblqeWEdKmF15VtYnZiZeSc-epgLFv7KM3ZVZPDlw-URgl7A7cYrflG0qvqezhzll415dIjOWb6VZayAkTor3kI05z6q1TK6i9gx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
آقا بووووو میااد
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65709" target="_blank">📅 21:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‼️
جواد خیابانی از اساطیر فراموش نشدنی صداوسیما میلی، اعلام بازنشستگی از این سازمان کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65708" target="_blank">📅 21:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3p5SPCfIiMUq9rvQQowCXN_li6EiGkVfV31tP3j-RLPobi7KDoLYuEgR0N1vD4enGWt0KjrRaNs72ybEp7sdgv_kwBmmNr9qOZvR_K3XsbMTJ1DUkBV4-9T1sn17J8iylQwQoPIZFb6jBbhjjYeqDZ1PhCIH0sZ-HCWw5kv2xxb3pVWTGz9bBqybQb7BmEFE8HqGTFug_KlzfM2EFpMxqEnec9QXNEFJI7uLokR08p_Q3r3-tXfP_lCxrMQ9LRuTxHTAa5dSkpYY-HyrD8HO6To39YvvU7m_aVSzzstVPPK9TX1zvBtrc0C0a519Dp6Mk4U3XaSC3iONpNOZkxT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پست ترامپ:
ماه گذشته، من به ارتش بزرگ ایالات متحده دستور دادم مأموریتی محرمانه برای حمایت از نفتکش‌ها و دیگر کشتی‌های تجاری در عبور از تنگه هرمز اجرا کند. امروز خوشحالم اعلام کنم که این تلاش باعث شده بیش از ۱۰۰ میلیون بشکه نفت از تنگه عبور کند و وارد بازار آزاد شود. بیش از ۲۰۰ کشتی تجاری نیز با ایمنی از تنگه عبور کرده‌اند.
این تلاش به‌شدت موفقیت‌آمیز به این دلیل است که ایالات متحده آمریکا تنگه هرمز را کنترل می‌کند — نه ایران. ارتش آن‌ها شکست خورده و اقتصادشان از دست رفته است. کار ایران تمام است
!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65707" target="_blank">📅 21:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک فروند بمب افکن B-52 بر فراز آسمون عربستان داره کص‌چرخ می‌زنه! #hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65706" target="_blank">📅 21:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک فروند بمب افکن B-52 بر فراز آسمون عربستان داره کص‌چرخ می‌زنه!
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65705" target="_blank">📅 21:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
ایران ما، امروز بیش از هر زمان دیگری، به اتحاد نیروهای ملی خود نیاز دارد. با یا بدون حمایت خارجی، سرنوشت ایران در دستان خود ماست.
ما قوی‌تر از این رژیم فرسوده و ناتوان هستیم. ما مصمم‌تر و استوارتر از حامیان اجیر شده‌ایم که برای نمایش‌های تبلیغاتی به خیابان‌ها فرستاده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65704" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⭕️
⭕️
رسانه‌های اسرائیل: ارتش این کشور درحال تدارک آغاز فاز دو عملیات مشترک غرش شیران با حضور مستقیم ایالات متحده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65703" target="_blank">📅 21:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65702">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65702" target="_blank">📅 21:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65701">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65701" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65700">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
گروه هکری حنظله وابسته به سپاه:
به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند.
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست.
ضربهٔ ساعت‌های آینده تلخ خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65700" target="_blank">📅 20:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65699">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سخنگوی آتش‌نشانی تهران:
ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65699" target="_blank">📅 20:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMYClbAA5_VuN1IxaxRCU0hqxV6pFftu6W9XPC_4aj65o8q-hbAFQreqmphDbXTVw0Bg5osvP7BEV9ZsSkWEj7mKINOaYDADEOqO8KW4xQfEQKU4wKgYOb_T88ZUnlT36QVtH3rOzCDu9S3YoLlVIXLEZtrraBLtP0LScGCHnqANNDbHa8-z-NMAoVI6xaTsFGhV-I6YoXad4GNiX5xiZDRpdfl3PKyMNYS9e9QPHyv3SGELCf5BFScyqk3M6wWBFR29dFOB9AHBipjEGOEMS7pD-VrzGRbKimixoOyV0IrMLt7BxBYNSa57lYa-QYvEfkf81qnGzH3rxJtDWDJ37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ساعت ۲۱امشب «
شاهزاده رضا پهلوی
» با مردم ایران سخن خواهد گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65698" target="_blank">📅 20:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65697">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
رسانه های آمریکایی:
حمله به ایران گسترده خواهد بود و بدتر از قبل
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65697" target="_blank">📅 20:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBIP0qHD6C6PnwLVfLiOQdFEOP5YhfLMJFEqnpyjoJQPrhEq4CwlPfMBfjwBVD4YEjnHlayjwvtiKFG0wATpcT3biaKv6tECllMcGFxYItkVTRbfNMvru4BKeMnJ0W-VN1GJJITLwLM_UAh-tKFcRepv63zuoyPxf_hMchW0dSUn9Ga5JJD19tVFWaD2blG3RZ56udGA3r6qSHThzbeshdeHWnJgCDGTT24cPlv7lFJ18ztkgMaF6YEYGfyVKxArMRQtR2r7vI5Dq7LlNNGz6g8g4CBJnvZMgePzmpFEsuRBQUhGfYJOhSR8AIBeVrJmSWzPk7-4vik3eV4yTZdVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در خیابان قیام تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65696" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است.
حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65695" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ آمریکا: عاقلانه نیست که جمهوری اسلامی بیش از این آمریکا را به چالش بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65694" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=lQUVwguEGB6bu22o0KarYmouGZaK9VFMSPX4-jMnECbd-dtdDHDKYJc6Ln-uwZcyANXm48_0YHFub7Mxheu3Iw_980s2ve7xtlLeAG3YQZdoXt4XIPFBnAFqGkEjl---5V7oXD2kipbMSZB19A7pRYKlVbVTAZR9jUzzBt1nT_cfE7PHHqDlDeiPSVtyic8QYC6vwWaVln8l9wUJ05sFy58PJBWDaf1PIUO_WsjxLZGiLHQkGsilHpWpnIXxe6ifbH-YOzhCCEXzJVnC1PLR9cB8eFo4gcUY59Ed-Vi9FA17wL_26hDCFAi1PYYGLU5mLENuVH-0r3UnRrHsxLkREw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=lQUVwguEGB6bu22o0KarYmouGZaK9VFMSPX4-jMnECbd-dtdDHDKYJc6Ln-uwZcyANXm48_0YHFub7Mxheu3Iw_980s2ve7xtlLeAG3YQZdoXt4XIPFBnAFqGkEjl---5V7oXD2kipbMSZB19A7pRYKlVbVTAZR9jUzzBt1nT_cfE7PHHqDlDeiPSVtyic8QYC6vwWaVln8l9wUJ05sFy58PJBWDaf1PIUO_WsjxLZGiLHQkGsilHpWpnIXxe6ifbH-YOzhCCEXzJVnC1PLR9cB8eFo4gcUY59Ed-Vi9FA17wL_26hDCFAi1PYYGLU5mLENuVH-0r3UnRrHsxLkREw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ :
به درخواست پاکستان، به ایران فرصت دادم.
فیلد مارشال و نخست‌ وزیر پاکستان افراد فوق‌العاده‌ای هستند.
ما جلوی رفتن پاکستان و هند به سمت جنگ را گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65692" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65691">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65691" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65690">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65690" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: همه‌چی سر توافق نهایی شده و فقط مونده برگه رو امضا کنن، ولی هی وقت‌کشی می‌کنن و امروز و فردا می‌کنن. منم میگم باشه، چند روز دیگه هم بهشون فرصت می‌دیم  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65689" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: همه‌چی سر توافق نهایی شده و فقط مونده برگه رو امضا کنن، ولی هی وقت‌کشی می‌کنن و امروز و فردا می‌کنن. منم میگم باشه، چند روز دیگه هم بهشون فرصت می‌دیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65688" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اونا فکر کردن من رو هم مث رئیس جمهور های قبلی می‌تونن بازی بدن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65686" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65685">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65685" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMu7Hk-_b1nPr4IZUi-5X4Qru0EVSB2C7VHCQT0uECbcJhxv6gY5m8QlGugRgSLqYhxWeUhjZWgIdlWXgOFWo5RqjHeF1PIlqTuSOdmZ27i4wUW0mfXyIg7DedtcYA4TH7QaCiLt4heB7FUG1trHJ3gN6oYz8M7u6H-T2VivEwTrbGYG6ecEg1ubjQ4iyNRgl7zylWN_Q62NZZzJ5DEAQPz8jS8D-w0ZM82FcH6UTaanCQFO2KKOvmJozQJyZUiyVXn4dyaIO97w2VISFnrFUlKkNVyEK6vVgXsFnRriSdsc-lvvWLTJ43Pm6MBYr0fYY6qv_176P3EclaPbuE2Cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امارات متحده عربی روز چهارشنبه، حملات موشکی و پهپادی جمهوری اسلامی به بحرین، کویت و اردن را به‌شدت محکوم کرد.
وزارت خارجه امارات در بیانیه‌ای این حملات را «تروریستی» و «بی‌دلیل» خواند و اعلام کرد که هدف قرار دادن پادشاهی بحرین، دولت کویت و پادشاهی اردن هاشمی، نقض آشکار حاکمیت این سه کشور و تهدیدی علیه امنیت و ثبات آن‌هاست.
در این بیانیه همچنین آمده است که امارات همبستگی کامل خود را با بحرین، کویت و اردن اعلام می‌کند و از همه اقداماتی که این کشورها برای حفاظت از امنیت و ثبات خود انجام دهند، حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65684" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. بمباران را از سر خواهیم گرفت. ما حق انجام این کار را داریم. آنها هلیکوپتر ما را سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65683" target="_blank">📅 19:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6pPA07ui8zYnVHftxvJVm6oA3P3t_TVCgqRmscK7sV6rRaA_XSJSs--dSFUZ1rA86h5AMftfrOIrIWBBGXOGFAL8Eb7uUFaMYTZaHO4BnJxKaiNa5TEqFtZJIcvKwMzKild1FcF-nYBuYFcXEWQZ8zJyHMVKuUGlMk1zqh7SSPS6NB-yCKgftm-Vf9pCltsWZSd0My9EuYKxEzXL8TcwZXIeez2HPG2F6ya4Voy7D0VmPIdd-gMM9CdFQNQjVTKhF_rM1OPWb3CnSA-EG8cFIctjBWCs130ZrlUj0T9Lz5NSG31B-BY_sGh8inyMYaNq5uXdo0ivJjx_uIKddfuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxQtmSb1Km0TeEXmct_qEns2YsFIkzh9t15lB1wkvj5pjLOqgNaG7UJhGd-sS3EcJjc9-54b9VbkOaSrrFCvU_tg87H_iHmP897UBO8I4A7dxTgaB3rlWOMAtm2Q8wkgGXRb3gxIfLhDeOVcT_thCqVNPl-QSeggwmBbxiOS2rnJTwuPs5rj0UoPt50BeyNEmX0-SVSYYKrlzRoCUeU5EhM7VBvPlXRFqAvts87FF62D61hTA5DdwAVvubCJBV5uoYNqQNtGHVohpbqWSTrzN8eGoHVl0nYwCskg_UhtII5ZtYcR3EJTzYF2Z781CBH4sJA-k2MW2cVx-Gh9P9TS1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت (خراسان شمالی)، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65681" target="_blank">📅 19:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maM4OmT8Ek8vO7VWfnkbsAiNNnMyD8-W4f2I10rbnMuCDBNr4CPgXcbZsD5LbgU-Y7227vEM-7z18l_--xH3bB889Qlw-gszxwJJXdYb8fBuSuO4msPIUKhAQ8Afju0eH9WkSZUSJmWcIvFXZpoTOwvTgXnSTY8CXlU7P7E7zU7gWVs2v1QC8vKkHdr5X7DJMbqQ8izDeKC2NiYaSklArOnmCGkc7MyaA55cBwU04k8x40AV6xPNMBVzv0Bz4FQ6NDwexJev0mk7a9JA-xJdTu4qZWXgvZgeL9VXVmucAHez-8E4wA8XicIpNcGYKqI9ekn4AAMDbOd6gzyXCCa4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حمله هوایی اسرائیلی در حومه شهر سحمر در منطقه البقاع غربی، شرق لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65680" target="_blank">📅 18:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
نیروی هوایی ارتش اسرائیل ویدیو ای از عملیات ها در جنوب لبنان و ضربه زدن به زیرساخت ها وشبه‌نظامیان حزب‌الله منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65679" target="_blank">📅 18:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
؛ تصویب قطعنامه آمریکا در شورای حکام سازمان انرژی اتمی علیه ایران
+یک روز قبل از جنگ دوازده روزه هم اتفاق مشابهی در آژانس انرژی اتمی رخ داده بود
.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65678" target="_blank">📅 18:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT42jJhYlox83F4PY-FMLPWVX3J59o4akijI7LNID4KnUUKq9C4LS-lYca50g9IM4vxMW6-djJDOPKj3vMxzSaGgT2kquOryKLVxOUedaoJXCFV81mo3V_UjNBslmvWIIVT4ZNHiSwV6GBh293uMg_DGARKrPhu67OzuMZKFsllJhmfYaP0wrMHPA3-YWumv0mUHKUZgi7tQ0nkR0NZsbd0oZ8SzyD728ZumBZKcF_3CHAdS-m1plDb_YJNeTMs4KlTfTMzJi-bieJo_QrT39Xa7hy4AebdLM7Jxr1jHpZ1mY6QmsebxQ4O7m8ibiSYRGtjutS_l4QBcmJqfvfRkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انس جهانی طلا هم به ریدن خودش ادامه میده و امروز هم سه درصد ریزش داشته
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65677" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65676">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65676" target="_blank">📅 18:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا در یک سخنرانی اضطراری با رسانه ها و مردم صحبت خواهد کرد.
جزئیات و محور های این سخنرانی هنوز اعلام نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65675" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDkc7dsGMoCOJPGbzRXFeX7b_O35iUiTCIsh2LSohAxng2wObpgXys_M_ZFF7UnmWC8Ku2z6jwOgfXxEyLoE8FgGRmRIGAcpQHcer14rCkLHzCgem7wQbmjnlNc_S4NNDj9DtkfEKDgpdhA470PAQt-_CzfhywybLz6NvHpF1A7ShRcdPBOKy4B3EfZWLgpVJGiTeNsGxKOtlMf7nZXo0M9btqoo7DD0CpiLMeF6mHpRpGrU93iqhU83xMCg1dlIctNdTClgLiL5qPhIWk-ujnx-uB2nwGM2VqxjWB-Ud3LnahNe-Rbg2aKzQe23wB0oNdDy3e-KhwBUrN6kaOkDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو:
به اقدامات قاطع خود علیه جمهوری اسلامی و نیابتی های آن در منطقه ادامه خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65674" target="_blank">📅 17:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgV6w-2Z7S4_KGpvPEPm9qfuWlCnoKvY5KCHZkAZs5ZwT32-WeHfnnnfreJ4qd5pIXWCOOX3ck2N2o2sX2UgdLWb0bNtsh2avT1HxjZYTNGo0yFeKS4VQ44mfTRGm3l5k4D2WUpjDDV4_LY4ymblqC1Fy9LU46wU0LwudMZjY52pnCMsnr_cGcEx6bHdcB1dMMXN5tpX-il8VmQ6mbSPhSPEBOGHBvzxXDoB57jEfird2VznFJB-aPOMl8gCqe5hYyvicTkA7LbKJMUTWW8Sm2SgBQgQEPnGydYbqB5VrmvmQSE8kpWX7YV3u2Wwzsw1W8xCsKrq_BSshLV8jc2ZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب گذشته یک فروند بمب‌افکن B_52 نیروی هوایی ایالات متحده در پایگاه هوایی فیرفورد بریتانیا فرود آمد.
با احتساب این بمب‌افکن مجموعا سه فروند B_52 در ۲۴ ساعت گذشته در پایگاه‌های نیروی هوایی سلطنتی بریتانیا فرود آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65673" target="_blank">📅 17:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/j8vs8wyAo05ncrByOTWEs1uT7zVw-x96jNjVWoLb_RbZV3-CibI3ZOKiJZdyejT1uQgxjR_k63L4uJZPYULbzg-AKQLRODzs4ooRazOJQ6zIOd6ZCvouf1f9kyL0ekhp4kTGFwWsiiYSjeFrxrVrmYGy_CKAtEwQIQcENpF0aoOX1DKt967eRZ1dbSx2END6b2ykOOX-O3PLX6t2IDtzruCQwv-Hpdr78y6hjxD0T6YmVVaGpezgIE-Pe8B1CGTBlG82Q_DwGP840M4nn2xcjBBD1G_gWy35VFvagJ4cjJcMrApI6cxocDRcbAjNjRPZBFGjb_KmDPma0HtIw5Bgow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65672" target="_blank">📅 17:08 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
