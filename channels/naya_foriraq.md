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
<img src="https://cdn4.telesco.pe/file/O3VZugERr3gM7CQiSTcVqj89hixXkwZw9cpdU05JpmpRGBg-Y-60U8JyZs-qratoAIxlg-qVUYkA4iAv8nOZBIeboT950jFN-J1fH-GzRmlK77o0KtipIBru0WjsK_0tGJ1vMLXlza_2F0QXWj0LaiiMAm5DJGeayzoZgXaq4Rul0fukZua2VBNh9TUHiOe0mx5pLRbzU4eUEmkTI_WBv7h8A__92AXbaRZ3EHiIONdZejXNh25DdPisBjcPkR9j6Nb3F-NaFkCI_I5K5IPmu14IGY9cs3o3PDr3nk2gKgXtA7zbUP8kBtcEukYQEXXfTBqMnvOHicqtARUPpWIRaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pM5E9XwMogmfsnPhHi60kAM6kqVAP-o45lILqJkwAydHJfzAWp4EmZPSzGtyim5le-hfMkaYgpIPxeItDDPCCy7lR_Hu8jsAbsaj007OqXWodEnhEOIHOSI9l4YCA9Nk9Ic2Bq-T05iWyA-h_Q3LouEQgmPJlQhD8T7KHtwsv2N8xJ9NwPlxV3Eb9LD9WexDhFoDnbpsHXPqDcUSl-MmLpxDuOVxjwnTiIR9Ay-U0N3TbRHKXbfX8EiFZPaCvVLTg6PtAVYABPi26aNWwINIwNApPtj98eAV-6Cdft-fUlF_upxLyf5r9XvFtAGaxNk-YXoZPP2UaKC5XmonMMXoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu--B_8qOznzV0xwBCSyVkqFnwR3BOWcQOWD6lH8kvUZK-cjs_sSl3uamhNuaW2gjDayTMjx7FisOPoRA8U9ZBTqXpttJHOYJgKEqcbM3aA64d4gIVHPfYMXuUTqkI62u7nQWIl1res1xX0MVpLl2pMQeFKWOL9Y9PeBHrKgKRlt8UvAMMLH7FfpxNtkkZyXF1J4dWuyTUas8khEG9sxkLRZkbgw0VZfGRpeYt7s03ZmsyjlgdUVrq3Bq4KrVdV9fGFdq3L9LF4lgWySP5Sp4czBr--xzE4AQ9ae4HAT_7VIyupqjTMkfMLcKJN7z75JBXt6dto-XYSxLZWJL0rLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdEGF3YnFDHuksbL3mOIo_oI7NSfGAuc-jImAylCAjzHxQjbk9io2h0y-1pGwqu4c_94tlcXaApMDIaPPGJ9-PZKvF0jArNCqkHfttHRrwmDqvDn9K9alTwW1tr-fW5Cm6L4-n3fY6T73dpWtdS3m00JgHcVJUATyy69y-xt4QTEoOLNTT_XS95hfNNlMW_2sKsaZUCqxr4KfcRft-EM5Q3hOUWlJGSw2y8fMb3bHv3bey87ms9yKxusqK_fbn_RdGx5Ap36NwCP8L9Kynwp61bOIm7Svhla9osWXksF4ACv21EvPCHFejLJsSZXjAtQ2kC5XE6O3ifwraCh1BfaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/naya_foriraq/76855" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇧🇭
قوة دفاع البحرين: استهدفنا ب 3 صواريخ وعدد من المسيرات الإيرانية</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/naya_foriraq/76854" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izc04tDLRLLfAvoAtrlEDsS51fe3hvAmCIDSBFDQusfiAfk6Yofvnw_C0nZ73IAm2GpGeF_QO81584ERXQOtrHqeGBxVt-F6iGL0DySyUfUw2_qaVLsOJCWM9MDe4G5-CvURY9muWPfaKoTAeetFkmxjQldP223cJnZLD3xt6_cvel5YDOk8tmZnpWlRju7M27xQvjjzw-lflMk-vbTOfBAxJ6RHLNwvf06_1wrJTddyoubYcx7ArXBn4ccdm3WvTQwUR86Sk9EwuugbCyweVevljRcG8Rl9bnnCqhWnqLy_Xzg1vbT1HgcYaQHwgsko5f4pi7uoNnNd-dtNLpvTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السلطات البحرينية تعتقل عدد من الشخصيات الشيعية في البحرين وذلك رداً على الهجوم الإيراني على المصالح الأمريكية على أراضي البحرين.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/76853" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw3_4JNt4vvZMZxV0vZESztk9MG4Pnp0eM0hAnYCtTl6vQZqcKUBau-QxGyL8OhNefcUwR77jtNXnoo29FInHcWGctHmD_fUpIu2Ezgp8koWhuul-ctHlSXQnOhOeHM7nfMhL-bVpRWeqbtz-pN-2qCqW_YeHoN46J9G9VXLxYs_vhDxpwEqDswnVAa1hVmkMcfV30EJyrRTSpqx8RFuAbg7mqQQaE5V0J5UgbuRjob5SjvcK0HQNsG_boVeVZp6Oci_dtnybqoPExfIH_SAWZiMUztWfbupmUI3rRCEE-9X-qrYXQOPPYEHWJ1cnbdqhXyN1296DoW1o1ox-9I7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة أقلعت من تل أبيب تطلق نداء الاستغاثة وبدأت بالهبوط متجهةً نحو Belgrade.</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/76852" target="_blank">📅 09:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/76851" target="_blank">📅 09:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76850" target="_blank">📅 08:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5KsrGEb1MIwm8EUCIRVkMW9WPUmWWXoiOnCS09xGXqEv7QNt4gae_ziaXtseSfYboQkrdMgeCus9TsOPyGmF6w5gKpzUu0fNde4JteE6Zg14PW1NmVlvvmrJsM7WpbSJeDWg7Ug2mQUq4DmkU7kOBe4Ja_WIEKwA05LssLBF6dDRjuWx_F_cI_gevJDX--fOSpD1Veot7HLqB3TADvY0W_xvcAU75-184QRt6CstDQorKQEap-kKEHOKpjYOqlWLVC9yqkV9cdA8Dh-aLf1msQVNJHQmVc-skN5Vx1VI891VqyMT7nNjO4sK7UbJTcRftsRRzKple8s4GagbpubHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🏴‍☠️
طائرة التزويد بالوقود الأمريكية أقلعت من تل أبيب وتحلق الآن فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76849" target="_blank">📅 08:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76848" target="_blank">📅 08:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76847" target="_blank">📅 08:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الإنفجار الذي سمع دويه في العاصمة الإيرانية طهران، ناتج عن انفجار "خزان غاز سيارة" بإحدى محطات الوقود ولايوجد هناك حادث أمني.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76846" target="_blank">📅 07:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=j_oRFWilZzM7jr_mwqqW10VaHEunhIGBTY0B7oYgafpEyNkLkUqIuA8HB_L8DkDlw9OrYrPWdAZuDmIO1G2IsMj_2AkIkUvBJikCUJeX3X8d0oXbxYd3qycr4prPB2qJiZLKVYeRpE1jlgRDJhearnQH7qfLbK2ynAlCCTifCltCJMgYWvI3eilkUmGEQP_0e6ZIAhhENMKMaG4k_t6Fma78pfU03Oqhm3MSHS5Nzeib7-KeCpPa5k1IJRJxn8aKdJzJto2zzRM6Sh8edBIh7FaObhSm-zQ6sfqahGi4AhJGc5ZBk_zkT61jW7YYyv2JP9_GDXW7zpdtSV6eOGf6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=j_oRFWilZzM7jr_mwqqW10VaHEunhIGBTY0B7oYgafpEyNkLkUqIuA8HB_L8DkDlw9OrYrPWdAZuDmIO1G2IsMj_2AkIkUvBJikCUJeX3X8d0oXbxYd3qycr4prPB2qJiZLKVYeRpE1jlgRDJhearnQH7qfLbK2ynAlCCTifCltCJMgYWvI3eilkUmGEQP_0e6ZIAhhENMKMaG4k_t6Fma78pfU03Oqhm3MSHS5Nzeib7-KeCpPa5k1IJRJxn8aKdJzJto2zzRM6Sh8edBIh7FaObhSm-zQ6sfqahGi4AhJGc5ZBk_zkT61jW7YYyv2JP9_GDXW7zpdtSV6eOGf6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم أوكراني على مصافي النفط في مدينة سانت بطرسبرغ الروسية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76845" target="_blank">📅 07:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇯🇵
‏
اليابان
: ميزانية إضافية بقيمة 19 مليار دولار لمواجهة تداعيات حرب إيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76844" target="_blank">📅 06:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf856cab38.mp4?token=ulXfkZZpwLJBYtlNq5sb6yT6NMGCmePmXUJs0AKDxePtIQS9w47unhWZjJOYyK7Qbyr1yBc1ghxIoQP2jKbH00XbULeYbUqDB21wfaEmwr9uyPhul37AEVic6zHn9KILpPmr6bhwWKVNxds6kkmzhq7EZgRPtnWbf7yQDuEBPzowxweuQO03outzTrKVmavVeX9LGZDYGC7CN09xQ-qFukZnYi8Gsnd8O09-zsBwM4EgG5H0Ud8qUMWxfuShcO67P6yoAW-VPVlERZACT4vSpaoGCXEEi6XziYEIFtUbzP6aLnoki0Png16e0_FIPO2AIqSkgtlFg__Oxen7INxpJL5uB2UlKd_Hx4YSuLIYV9g64AAcuF1CkVEVkqJxGrwsgpZFaovFOFp9YfaMX2MzBmaoUz3ICeh6lSGbfbhFydCR7YjX5lCXfaeb0JDmHBy-5wL563-a7G7owSG91cK8wiE89hROnaKHJnaYFJFGcu-L9qxYiP7l3BoZc5d9fh7cz9KZkTUeAGAhne_Y_Iozfn-erqKi4t6V3QIaDG6nw8zyX4vb9-cccfsohtjdPKK5lksLLrPK-UBJBm3HmBP45P7zgzyqdceu_NRTXUl_K93LjLKPiopfGdfak2BXPlwmGrBCypNshppwnhzHuETA7ZjSgjqqRD6P_iCOX0PdlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf856cab38.mp4?token=ulXfkZZpwLJBYtlNq5sb6yT6NMGCmePmXUJs0AKDxePtIQS9w47unhWZjJOYyK7Qbyr1yBc1ghxIoQP2jKbH00XbULeYbUqDB21wfaEmwr9uyPhul37AEVic6zHn9KILpPmr6bhwWKVNxds6kkmzhq7EZgRPtnWbf7yQDuEBPzowxweuQO03outzTrKVmavVeX9LGZDYGC7CN09xQ-qFukZnYi8Gsnd8O09-zsBwM4EgG5H0Ud8qUMWxfuShcO67P6yoAW-VPVlERZACT4vSpaoGCXEEi6XziYEIFtUbzP6aLnoki0Png16e0_FIPO2AIqSkgtlFg__Oxen7INxpJL5uB2UlKd_Hx4YSuLIYV9g64AAcuF1CkVEVkqJxGrwsgpZFaovFOFp9YfaMX2MzBmaoUz3ICeh6lSGbfbhFydCR7YjX5lCXfaeb0JDmHBy-5wL563-a7G7owSG91cK8wiE89hROnaKHJnaYFJFGcu-L9qxYiP7l3BoZc5d9fh7cz9KZkTUeAGAhne_Y_Iozfn-erqKi4t6V3QIaDG6nw8zyX4vb9-cccfsohtjdPKK5lksLLrPK-UBJBm3HmBP45P7zgzyqdceu_NRTXUl_K93LjLKPiopfGdfak2BXPlwmGrBCypNshppwnhzHuETA7ZjSgjqqRD6P_iCOX0PdlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد توثق لحظة إطلاق الصواريخ من قبل الجمهورية الإسلامية الإيرانية باتجاه القواعد الأميركية في دويلات الخليج الفارسي.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76843" target="_blank">📅 05:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
فشل محاولة ثانية من المسيرات الإيرانية في مهاجمة قواتنا في الكويت.
الدفاعات الجوية التابعة لنا نجحت في إسقاط عدة مسيرات إيرانية ولم نتعرض لأي ضرر.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76842" target="_blank">📅 05:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66acdfd3d4.mp4?token=k-EGt4sgPrt9Bydl6kIAa1g6PJ34TlUt3rHyTWcWa6WkXh0gTqdr0QNzo5fZfv1uOGgd-sfZmsfQgXMvMAonPiDQD_TcKKl9Gwt06xOBIVJWeA3cq4ZJFE5pezhVBbUui2RG9le3OTEd1bRkOkIS7Kwo25lVm4ffTAjC0hnqPCEVZYc-6epem4D3fjCs5G_ZRhdg5ui03EAyH5XLr2CpSeDsAQnqiQb29t0CcwlZZx9bpnNIMJZlgJa3HzX2fO5yi2SyKAPsCMiBNl31T-ChgZoSBZ61u6mDylFcTOE9nF5VD7pDY-rEk4QLIAPnaQQ-NroNk2MXSPjZnH7CbsC5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66acdfd3d4.mp4?token=k-EGt4sgPrt9Bydl6kIAa1g6PJ34TlUt3rHyTWcWa6WkXh0gTqdr0QNzo5fZfv1uOGgd-sfZmsfQgXMvMAonPiDQD_TcKKl9Gwt06xOBIVJWeA3cq4ZJFE5pezhVBbUui2RG9le3OTEd1bRkOkIS7Kwo25lVm4ffTAjC0hnqPCEVZYc-6epem4D3fjCs5G_ZRhdg5ui03EAyH5XLr2CpSeDsAQnqiQb29t0CcwlZZx9bpnNIMJZlgJa3HzX2fO5yi2SyKAPsCMiBNl31T-ChgZoSBZ61u6mDylFcTOE9nF5VD7pDY-rEk4QLIAPnaQQ-NroNk2MXSPjZnH7CbsC5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای انتحاری در حال حرکت به سمت کویت.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76841" target="_blank">📅 04:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241cbfcc80.mp4?token=iVxYIzhV6Clhq7ky9N9ic7fPcGTqmpvJFLq8nENvQTfrMy4AwrXU1TGK1kLgohj4mxZ-PuHs8_J3B_WJpukRkaoU-OWC-IJOg4YpokyrwRVxoarMMq0eR-8-4Ro33QNyiN5FtHIuRQINopWPIFkgs8q0gNViLvdHaQT2nYg4nYk14Wu_MGhkWMeBko1az_SH5CmXQ6rM3o9f7aHeMQVC9dq9TwLT7Lep-CO_lBHWC3Xuu7OORBs6Kd-Ii-DZ5ybW6Dkz2YFiHHzIbSTxIuOAAyqmavdXk6vdmd5FpO4x_0oZPPi1zDPXYewiHOT8MpttuQ5ZQ9tb0yvqHYQlSdzOiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241cbfcc80.mp4?token=iVxYIzhV6Clhq7ky9N9ic7fPcGTqmpvJFLq8nENvQTfrMy4AwrXU1TGK1kLgohj4mxZ-PuHs8_J3B_WJpukRkaoU-OWC-IJOg4YpokyrwRVxoarMMq0eR-8-4Ro33QNyiN5FtHIuRQINopWPIFkgs8q0gNViLvdHaQT2nYg4nYk14Wu_MGhkWMeBko1az_SH5CmXQ6rM3o9f7aHeMQVC9dq9TwLT7Lep-CO_lBHWC3Xuu7OORBs6Kd-Ii-DZ5ybW6Dkz2YFiHHzIbSTxIuOAAyqmavdXk6vdmd5FpO4x_0oZPPi1zDPXYewiHOT8MpttuQ5ZQ9tb0yvqHYQlSdzOiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏انفجارات تهزّ مقر الأسطول الخامس الأميركي في البحرين، عقب إطلاق رشقات صاروخية إيرانية باتجاهه.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76840" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82785218ec.mp4?token=Jqgvu4WBfW3Jdj_WuRFmVY7I4EOgRJGX6prlhozDN_bNDyiqkZmJmrQzGEkUKRtIJ8GuLeErlBj7J7FVpo1rFEfpr_p-KC9XlJamYhbYfvK74tC7hw0nWixTcCVZvqRBpocokfdvVuGUe1ysphRrGWtoTDmx8kDE5bdmUkIm16POD3fliiybDgOSnBWJWl7zLZ0NaCjS5E5RjASGg_wwev7r4epkm-Ge-cBqFaJPILFAk0q5aCK-4cYRmHYQqvVaNp1OeJ3RUl9J_A7gS57c_U-wgQQAYeOoxfQMhqoHKCA_pNhSGvOuB_XOQA5PTPk1BbkOO18qkOJ-CqbSBTrpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82785218ec.mp4?token=Jqgvu4WBfW3Jdj_WuRFmVY7I4EOgRJGX6prlhozDN_bNDyiqkZmJmrQzGEkUKRtIJ8GuLeErlBj7J7FVpo1rFEfpr_p-KC9XlJamYhbYfvK74tC7hw0nWixTcCVZvqRBpocokfdvVuGUe1ysphRrGWtoTDmx8kDE5bdmUkIm16POD3fliiybDgOSnBWJWl7zLZ0NaCjS5E5RjASGg_wwev7r4epkm-Ge-cBqFaJPILFAk0q5aCK-4cYRmHYQqvVaNp1OeJ3RUl9J_A7gS57c_U-wgQQAYeOoxfQMhqoHKCA_pNhSGvOuB_XOQA5PTPk1BbkOO18qkOJ-CqbSBTrpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای انتحاری در حال حرکت به سمت کویت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76839" target="_blank">📅 04:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyOBVCV4r3XleeVeKe9rh68HcFIgseN4i8V5SfjUSYmygTBzZzGIrM_3M2yNSq6sX5FvxyNpRxvGJTbvza4KJsf8Sna6PDce9ovNwr2SPoH8gsEXD5fE-OPbyl9HMg85uCf7O9ZvCU_weIFzNBoNF51rQUrVBFmTuFsU_zzWw_1_vG0Ic8yaOLgd28sZqRoYo7xl7qf4mz_GgKSfyqBLnbj8h9nxJ-QGg4Pg3flQHNVaV3Zv7FsPpFyKoGYyY7L5ZkHANZ-JDKIuIhKy3G7q8_tj034QvlI5Qu-TU47reNBqJ5i0pliTuY4iENlgwZi1w4CkvzxSV92-NwR8uN0c2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تتجاوز 97 دولار للبرميل الواحد بعد الهجمات الإيرانية على قواعد الأمريكان في دويلات الخليج الفارسي.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76838" target="_blank">📅 03:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">من الطيران الحربي الذي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76837" target="_blank">📅 03:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8563b797f.mp4?token=UG86OfDRlhI0r1F8UTtmiZfodsJUKGZsJqD7baMAR35VvErBVu9exXQtw0RVOIV7U5Xotc82c6MdIjNebdmt-ifzPokz7NgECEELHe4PzvNqvdX0JJMRzvEXhJopmKsPGHd-oIMQBqA5YHymNNqcqx-zX-BN-RupnPHqzjG-buIUcj68k_PDGW5plkrEMsCByZieEnPielxK3yao3brVKBffj0-J3hOaj4_m3z7qzD8Xkwu0l1_7guXD3Ao_WQ14lM3RmV6tL5Rr3TfmH0W1yD34f6R9aAyG4Hz_u8VhNKeh-4NCxztks29gLnQBYF047uCbqapuZL5PYp6lOgPT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8563b797f.mp4?token=UG86OfDRlhI0r1F8UTtmiZfodsJUKGZsJqD7baMAR35VvErBVu9exXQtw0RVOIV7U5Xotc82c6MdIjNebdmt-ifzPokz7NgECEELHe4PzvNqvdX0JJMRzvEXhJopmKsPGHd-oIMQBqA5YHymNNqcqx-zX-BN-RupnPHqzjG-buIUcj68k_PDGW5plkrEMsCByZieEnPielxK3yao3brVKBffj0-J3hOaj4_m3z7qzD8Xkwu0l1_7guXD3Ao_WQ14lM3RmV6tL5Rr3TfmH0W1yD34f6R9aAyG4Hz_u8VhNKeh-4NCxztks29gLnQBYF047uCbqapuZL5PYp6lOgPT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76836" target="_blank">📅 03:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192564c0d1.mp4?token=CpC5BNgagnwpInP1PL77Y2wjMpKBIjB8alg1-FF8kR9vnTCwz2Qzx16sRUspObXo4Ibt_2LgAoR9pkeAhsOmu_lT22vxSUFmhPudtBnuPe4t_9gUiCrMsTf7faGzo3BkC5hc9MS-liYqFKPNADpOfi8CSV4hQ0UK_bPR6DNbXLcLqmBrtSZGavs7ug8XS-A90CH3VN4ka8A-vafVoG3bESXTWwDqN_p-aRR-TdTGFRkIk3lEqVW4vM-xP_aKiTxsl90plZvecakZypVQyPnW6fa2scid0YemVXWouedl04y8aD-lFOq8EO9NdKwwAl2g-MpxTKJ-3Z1Jejq2x2IKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192564c0d1.mp4?token=CpC5BNgagnwpInP1PL77Y2wjMpKBIjB8alg1-FF8kR9vnTCwz2Qzx16sRUspObXo4Ibt_2LgAoR9pkeAhsOmu_lT22vxSUFmhPudtBnuPe4t_9gUiCrMsTf7faGzo3BkC5hc9MS-liYqFKPNADpOfi8CSV4hQ0UK_bPR6DNbXLcLqmBrtSZGavs7ug8XS-A90CH3VN4ka8A-vafVoG3bESXTWwDqN_p-aRR-TdTGFRkIk3lEqVW4vM-xP_aKiTxsl90plZvecakZypVQyPnW6fa2scid0YemVXWouedl04y8aD-lFOq8EO9NdKwwAl2g-MpxTKJ-3Z1Jejq2x2IKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ باتريوت أمريكي يفشل في اعتراض الصواريخ الإيرانية ويعود ليستهدف دويلة الكويت!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76835" target="_blank">📅 03:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ecc2e200.mp4?token=jhEnPV8lNAaxX0XUCxY6oZNFLhHrHotnaciVMvB00S-Ste_GQ8VCKGYvdIzGg-Ty9G9WWA28hvRfQ0JlWUjmJGuxEyKNuNIVi-WzCSpFdaFuKGhTmGu0mg-dHt8IyVGk2EJXMWi5hjQpVcaofQZxUZ-dmQr-DMQf7d8DEZUlP7BG3YhW6D4iRshy8o_edVBjgNhPWEtt-RpWIxQs5oQyD5I-IRGiOYH0jw0LqTr7Zue8iozTJCW6hfBM6JwKJS5r-rJ08Xo1l4ehaLKRMruemVfBYNOVvtNgtgMWBIj0bPxTV1PJQi4y6FreZIhazqV9GSVJVBYbmEa8Hv8o15DRYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ecc2e200.mp4?token=jhEnPV8lNAaxX0XUCxY6oZNFLhHrHotnaciVMvB00S-Ste_GQ8VCKGYvdIzGg-Ty9G9WWA28hvRfQ0JlWUjmJGuxEyKNuNIVi-WzCSpFdaFuKGhTmGu0mg-dHt8IyVGk2EJXMWi5hjQpVcaofQZxUZ-dmQr-DMQf7d8DEZUlP7BG3YhW6D4iRshy8o_edVBjgNhPWEtt-RpWIxQs5oQyD5I-IRGiOYH0jw0LqTr7Zue8iozTJCW6hfBM6JwKJS5r-rJ08Xo1l4ehaLKRMruemVfBYNOVvtNgtgMWBIj0bPxTV1PJQi4y6FreZIhazqV9GSVJVBYbmEa8Hv8o15DRYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الذي طال دويلة الكويت</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76833" target="_blank">📅 03:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سماع دوي انفجار قوي في مدينة قامشلي السورية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76832" target="_blank">📅 03:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طيران حربي في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76831" target="_blank">📅 03:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">يبدو ان قطر والسعودية قد تعهدت لايران بعدم استخدام أراضيها بالهجمات على الجمهورية وهذا ما يفسر عدم استهدافهم بالجولة الأخيرة ..</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76830" target="_blank">📅 03:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fedd33a5.mp4?token=HxRV0uujCuiCp8vo07NV3GXWH05G35imel07bPhU-oBxbQkwTKvc3ipIDuzjlbEVfcNVZ6Cmk_70Bggk8Y1C427DhSR3q-ZBWSSyCv77By8_9WRimnTy-eL57T2G33VysAY5LdqUI3oJdneiWflC-ZIYKIe4fmW7xsAYTqmx5LMb_nL3H3K_aOj5tT2cJfxOQc59dxyan68zhg5jPZGaSax3KVb_kbsxvnkjpeiNstnBIKCboWcssmm0YlElgamGLY7F89x1Y0tRzqQcatvtiV5qKHibC-hpl_kU_inkT0VhizE54LhQGh5-A2CZeC5bwsvSlDPMA6SMqV1m2bwgmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fedd33a5.mp4?token=HxRV0uujCuiCp8vo07NV3GXWH05G35imel07bPhU-oBxbQkwTKvc3ipIDuzjlbEVfcNVZ6Cmk_70Bggk8Y1C427DhSR3q-ZBWSSyCv77By8_9WRimnTy-eL57T2G33VysAY5LdqUI3oJdneiWflC-ZIYKIe4fmW7xsAYTqmx5LMb_nL3H3K_aOj5tT2cJfxOQc59dxyan68zhg5jPZGaSax3KVb_kbsxvnkjpeiNstnBIKCboWcssmm0YlElgamGLY7F89x1Y0tRzqQcatvtiV5qKHibC-hpl_kU_inkT0VhizE54LhQGh5-A2CZeC5bwsvSlDPMA6SMqV1m2bwgmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق لإطلاق الصواريخ من إيران نحو دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76829" target="_blank">📅 03:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXe0GpaqIvj92DkR9yBIZZJ0c0A2tYaBzkRG6VGgBdEOdLhDuDjrCeIuKXAsgx0vFWCD6EUmU6pji2MnJZjmNR1jkWIXVr4j4SJKCxaYBqgtRz2ZkYz8EHM9ldPww6BK9PcFENcuwSEvWd3crwg4yRf3pw-Ats3RoUHKiGCcbL6RIn5BMOLNe6sh8XnM7dtLfeSp-qSytMVlsupgHOyPgDEMQMh6S6ZKBvnZ7sdJkDkRYT0jSQwrKJsdn524XDDM1O6GI9y05BT4FCZnIdnOtd0r89IOANP3Z-7Ao9F3jzgPOHKVbaYKioggDjxlJpD3sglB-G9BZpXWysuoak8vnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها   بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76828" target="_blank">📅 03:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/540734d971.mp4?token=AHy5JoTDBjKF0H-zUI4PmyRhL27caqeLo2R9e2BlYghj24adtqXF3FPrkVV7JewaXmNPo4j2V-VQZ597gnW46068yF1tmyXvxHsyeRymYySh79H7vNKwI48eD_4_fIHIMlT9MseTuOp0YYMt3YbgE-sfGkKdRAkMtkEkR8b7xXaNeOVkqmk5USPs1UD2IiXc-2N_8uePPd8aRppNdVikm3t0IjC70PO6BXDrHuNEhFDiLxdEScb2lHnjIPLp73bXPCKaTpiYHG0emHtwZL6eAQH764qVF-5kHreQR4srRuE7HH_MWD1fx-CGag2pbOS8abAC213tAP3_JqsGqZ4C9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/540734d971.mp4?token=AHy5JoTDBjKF0H-zUI4PmyRhL27caqeLo2R9e2BlYghj24adtqXF3FPrkVV7JewaXmNPo4j2V-VQZ597gnW46068yF1tmyXvxHsyeRymYySh79H7vNKwI48eD_4_fIHIMlT9MseTuOp0YYMt3YbgE-sfGkKdRAkMtkEkR8b7xXaNeOVkqmk5USPs1UD2IiXc-2N_8uePPd8aRppNdVikm3t0IjC70PO6BXDrHuNEhFDiLxdEScb2lHnjIPLp73bXPCKaTpiYHG0emHtwZL6eAQH764qVF-5kHreQR4srRuE7HH_MWD1fx-CGag2pbOS8abAC213tAP3_JqsGqZ4C9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76826" target="_blank">📅 03:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
🇮🇷
بيان العلاقات العامة للحرس الثوري الإيراني:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
في وقت متأخر من الليلة الماضية، استهدف الجيش الأمريكي المعتدي ناقلة نفط إيرانية قرب مضيق هرمز بقذيفة جوية، مما أدى إلى إلحاق أضرار بغرفة المحركات.
ردًا على هذا العدوان وانتهاك لوائح مضيق هرمز، استهدفت صواريخ تابعة للحرس الثوري الإيراني سفينة تابعة للعدو الصهيوني الأمريكي، وهي سفينة "بانايا".
في عدوان متجدد، استهدف العدو الأمريكي برج اتصالات تابعًا للحرس الثوري الإيراني جنوب جزيرة قشم بقذائفه الجوية. وردًا على هذا العدوان، تعرضت قاعدته الجوية ومروحياته المتمركزة في إحدى دول المنطقة، بالإضافة إلى مقر قيادة الأسطول الخامس الأمريكي، لهجوم بصواريخ وطائرات مسيرة تابعة للقوات الجوية للحرس الثوري الإيراني.
لقد حذرنا سابقًا من أنه في حال وقوع عدوان، سيكون الرد مختلفًا وأشدّ، وقد تصرفنا وفقًا لذلك. كان ينبغي أن تكون هذه الردود درسًا لنا.
نؤكد مجددًا أن زعزعة أمن مضيق هرمز ستُكلّف الجيش الأمريكي المعتدي ثمنًا باهظًا.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76825" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7f9af40f.mp4?token=cNFNTR75yJfd0TkW6VhyV4NtVwKoLTuWxcJb07YxHNC7yKCQ7Lu0EzG7RKGbHbp-vCpDnt2iSTJgUHKKxSAv1JOjgzQAnIetkJbB3_4ZOdKx5joRpChoV9EhNn1WbqqynyVz5bwJeJ2oIYn3dEWTS-0tElt00GHplDeIk76R2cQc6OxUehGxJ4ayiwWFYfpR7NmU04dopijk6-UP2Iu0I46EeSjpyj7H0zF1O8lJ8PNseOC_dpUAd9621_Hm9V2ILnQBGj6qgy2IEDzgxSHnJ7Mxbj6UEMpk3ilAug8vrxbOppHeFwOxk4V9IAp-4BsM5IDuALYPFEEoaaX9nTNBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7f9af40f.mp4?token=cNFNTR75yJfd0TkW6VhyV4NtVwKoLTuWxcJb07YxHNC7yKCQ7Lu0EzG7RKGbHbp-vCpDnt2iSTJgUHKKxSAv1JOjgzQAnIetkJbB3_4ZOdKx5joRpChoV9EhNn1WbqqynyVz5bwJeJ2oIYn3dEWTS-0tElt00GHplDeIk76R2cQc6OxUehGxJ4ayiwWFYfpR7NmU04dopijk6-UP2Iu0I46EeSjpyj7H0zF1O8lJ8PNseOC_dpUAd9621_Hm9V2ILnQBGj6qgy2IEDzgxSHnJ7Mxbj6UEMpk3ilAug8vrxbOppHeFwOxk4V9IAp-4BsM5IDuALYPFEEoaaX9nTNBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الذي طال دويلة الكويت</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76824" target="_blank">📅 03:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
‏انفجارات تهزّ مقر الأسطول الخامس الأميركي في البحرين، عقب إطلاق رشقات صاروخية إيرانية باتجاهه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76823" target="_blank">📅 03:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">القيادة المركزية الامريكية:
نجحت القوات الأمريكية في إسقاط عدة صواريخ باليستية وطائرات مسيرة إيرانية، ونفذت ضربات دفاعية على جزيرة قشم ردًا على محاولات إيران شن هجمات في أنحاء الشرق الأوسط.
أطلقت إيران عدة صواريخ باليستية باتجاه دول مجاورة، إلا أنها لم تصب أهدافها. وسقط صاروخان إيرانيان أُطلقا على الكويت قبل وصولهما إلى وجهتهما أو تحطما أثناء تحليقهما، بينما اعترضت قوات الدفاع الجوي الأمريكية والبحرينية على الفور ثلاثة صواريخ أُطلقت على البحرين.
وقبل ذلك بلحظات، أسقطت قوات القيادة المركزية الأمريكية (سنتكوم) ثلاث طائرات مسيرة هجومية أحادية الاتجاه أطلقتها إيران باتجاه بحارة مدنيين كانوا يعبرون المياه الإقليمية بشكل قانوني. كما نفذت القوات الأمريكية ضربات دفاعية على محطة تحكم أرضية عسكرية إيرانية في جزيرة قشم.
ولم يُصب أي من أفراد القوات الأمريكية بأذى. وتبقى قوات سنتكوم متأهبة وجاهزة للدفاع ضد أي عدوان إيراني غير مبرر خلال فترة وقف إطلاق النار الحالية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76822" target="_blank">📅 03:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4ap6kmODTLCYolfMXZReEjKlJtuKl_2qPpPBjKoHnZYSYNGpwpv0cDOsLLaXeZANn8MEDkCrjAZJ4cZNsMhU38fMwtb9ZdjKNP9dsbSS86_rcBN3mHNVTtxDpNGx6t3V8dpZkBlLp14B1drC3510siX9-6sffAITZxeQ7UsSyRg8g1se54Ou-5Y3GLQIlRbSUSOSOF3c5_ERm1dgWMmB1TexlaEtfdqcUqacXlU3_ozzBrVQjVYoFMkSyTACtkaqnVN5r_8DmtzMziTdM8PCX17jYdPBTALFbps1KUqoA9lsPBpq6NiAi6fhXQGXF9mHJwrm6Z7j0BYsBQ_BZ0QVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إغلاق المجال الجوي كليا في الكويت</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76821" target="_blank">📅 02:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76820" target="_blank">📅 02:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76819" target="_blank">📅 02:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توقف صافرات الإنذار في البحرين
رفع التحذير من هجوم صاروخي</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/76818" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم الايرانية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76817" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd6NSPq8v8Bp9gVKgOOi5FcCldhzhtfWmbPWqaVYuMqGQAGTgXhj1_xW-HuCg0wFsIB7nDGIG_HJnwfSJURKiFP7lXeyNgabiv8jLdwR-60hrvD023cPrnkz55n89tCKYJPfkCgV2gqAnwAjOnxaTOFkLeLoC-9SRgmMH2OxCvsegXupimL-seg1jINZmari15D9bs6ZjXdGaNpLxOfLmzwlUjhHWLAPWsF2e4eC2Jd7K8AP-27uLzSkD490eznQdzYOw70o_5_WupQSIOh2MmqQ07fU57C5FKjf_K7xibED3pg1viptOXfa3osXvs0CVwo0rwvaQLPwSPHAaiHkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تم إغلاق المجال الجوي للبحرين بالكامل أمام جميع حركة الطيران من الساعة 03:30 بالتوقيت العالمي المنسق حتى الساعة 16:00 بالتوقيت العالمي المنسق، مع السماح فقط بمغادرات محدودة معتمدة مسبقًا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76816" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76815" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osyb60m6VqS3jibRbCDsMiQ9zIMwF21M6dP9CkYTOJ7RNsnJhzzU3iDOvre34W1HvJLOrqbkhyq6_TgeXWuHLZ7aI5HzabDSrO49_nYQPXIfu4s-gyfjFaN2IUtWEJXrwsZmBlwX-tfsYAkjJ918FGiBo19X3iuw59_MzP9u3XILa7Hfiyps9CECij36cOs0XL3FgkUdYOzslVuctt45FyKo086qaKhvjtSEpsq48RTbd9-RSD4t7nJPc7LNIO6IT6N-ymj1k1QntCzqCOIVUKFeLbG2wA0aBRNdsUER9dL8EpBiBhBcYzyfMGJGFx0EhhZz29JW8bv4XL4RJGYPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف نحو مطار دبي</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76814" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قصف نحو مطار دبي</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76813" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76812" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الإعلام الأمريكي : أفادت التقارير أن رجلاً يدّعي حمله قنبلة مربوطة بصدره قد احتجز رهينة واحدة على الأقل داخل فرع بنك تشيس في بيكرسفيلد، كاليفورنيا .</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/76811" target="_blank">📅 02:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvBbCOablZJqwdtzX8KipcF3KtR24qVZ9DTa5fw5SD3PzXbZqHqh6YLuyvz3hXLjUSq7aMWp9TptQUtuEVkdtJLGw1dT6hCM2x_9GOJDrfC-T347E2iKttwXTiyS2K4M_uz0BfMmxa0nDssw0A3-5LgOIxlVB8rM_1OJdz_AJ79i17jH2e70ricFiXCB_G_XDFsyL4LRrtUBRTAExOo9dYvGCkK1gni-X5eNa4UbMAuNxVtYGFWiUykFNTCxzS21bb_2g7zhNmEFwDFb9FEH7WQtjWPud72GB-hYp7oRiONmCLaAZ7jilHd_TaNc6ys6qyf9uEQPJO-0lacev97aXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف حركة الطيران في سماء البحرين</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76810" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=dRw5EzuiLysTJYqy0GCZktQWqipGO8Oe2nUGvSVgIeOJnqwAtgXZZr0KMKsnNUPZMItaFcMaS3uhk6mSCYw2IDxGstRlBQDmSn8ZBoDLCFv7twW2ULJPL0OSfOwgXJ2HfyczMDRGfVkdUztEZBAktkIcE6nH6_0KJDAlv6bnaytdojRCQaBlvmFDoWSHHQLmKXVGmPcoUACDdBWBrvjrPQsnIJRB9U5h6bSiWLTUtV7NG_wQRc5fZDq07ktLQmYraxPfIjyDJI1pDH7npcm9Q4hjqAvjAzwZiXOXMWtAS53owsqkW_xm1wiaZ7W5rqJLBLfKEprBrUiuPJvgApyCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=dRw5EzuiLysTJYqy0GCZktQWqipGO8Oe2nUGvSVgIeOJnqwAtgXZZr0KMKsnNUPZMItaFcMaS3uhk6mSCYw2IDxGstRlBQDmSn8ZBoDLCFv7twW2ULJPL0OSfOwgXJ2HfyczMDRGfVkdUztEZBAktkIcE6nH6_0KJDAlv6bnaytdojRCQaBlvmFDoWSHHQLmKXVGmPcoUACDdBWBrvjrPQsnIJRB9U5h6bSiWLTUtV7NG_wQRc5fZDq07ktLQmYraxPfIjyDJI1pDH7npcm9Q4hjqAvjAzwZiXOXMWtAS53owsqkW_xm1wiaZ7W5rqJLBLfKEprBrUiuPJvgApyCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صواريخ جديدة من إيران نحو دويلات الخليج الفارسي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76809" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4d84fc6b.mp4?token=RwHbFaqiRDUTMdNsErvI6WQqZhVeI3sA-voYeZ3LJtgi5-gmTj6DQvVTzy3Ozytyo0lZDkQ_O377_2kMnWwLgNcT7656XJtmXi2JnxspQIsbYFdgmqR3IixOEpPaxB3UPhRIPPBJ86FplcJW4nNkyzobf3wLfi3mkq_myIYbYYqz2xEDTsjQUymwKKH7hFyO-RO96HbUn1RsNAo3_-xaomRsYQZ7PTdvS9odnqRoYROFgoGk4FInVSK37a0sBqhH012ITlQwuuzCrJK3CwrXOZUQQQFLc1e9whoS1RZNHANyoN4BlzTitIcow6wKLjruKSUNqsgSxqIwxnaPvg4XPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4d84fc6b.mp4?token=RwHbFaqiRDUTMdNsErvI6WQqZhVeI3sA-voYeZ3LJtgi5-gmTj6DQvVTzy3Ozytyo0lZDkQ_O377_2kMnWwLgNcT7656XJtmXi2JnxspQIsbYFdgmqR3IixOEpPaxB3UPhRIPPBJ86FplcJW4nNkyzobf3wLfi3mkq_myIYbYYqz2xEDTsjQUymwKKH7hFyO-RO96HbUn1RsNAo3_-xaomRsYQZ7PTdvS9odnqRoYROFgoGk4FInVSK37a0sBqhH012ITlQwuuzCrJK3CwrXOZUQQQFLc1e9whoS1RZNHANyoN4BlzTitIcow6wKLjruKSUNqsgSxqIwxnaPvg4XPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الامريكية في الكويت تدك بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76808" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">استهداف سفن عسكرية قبالة سواحل الإمارات</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76807" target="_blank">📅 02:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327aa8b74.mp4?token=hCTdYxEdXZrOuDO0c4oTgnlz0fVo5mSuNKmAnbtntG9fsF5OHCYTiKU-mDCj4UBj-s2d39XmpXrAK-7ZvT8y0SpNXOpyhnTV2NwpaDYvdeP2AqiT8PGj8GOuHgOVB2pB_xfjqTqyNLsQ7fYW8HOYGdTBG4Z_IMX9p8D1n1Mqoklw3YPLKLnV692Yah8g2Kt_MEDAVCvknlFRvrO0oA3OzlT092TXujukrXdHfVxsRQN-So7XJx9Ly2qHBQHImEVXKDswfea7FWcOnB7xKyFKGc6FMCZq9EQP_3k34iAsVs5wugNjN_dTC5o2Lpcs_AJID6rr1xOopFnfE_Yx5uXTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327aa8b74.mp4?token=hCTdYxEdXZrOuDO0c4oTgnlz0fVo5mSuNKmAnbtntG9fsF5OHCYTiKU-mDCj4UBj-s2d39XmpXrAK-7ZvT8y0SpNXOpyhnTV2NwpaDYvdeP2AqiT8PGj8GOuHgOVB2pB_xfjqTqyNLsQ7fYW8HOYGdTBG4Z_IMX9p8D1n1Mqoklw3YPLKLnV692Yah8g2Kt_MEDAVCvknlFRvrO0oA3OzlT092TXujukrXdHfVxsRQN-So7XJx9Ly2qHBQHImEVXKDswfea7FWcOnB7xKyFKGc6FMCZq9EQP_3k34iAsVs5wugNjN_dTC5o2Lpcs_AJID6rr1xOopFnfE_Yx5uXTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف قاعدة الجفري الأمريكية ومقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76806" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز أربيل شمال العراق الان مجددا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76805" target="_blank">📅 02:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74abf9487.mp4?token=TvjORGow1udcXsGYVX8c0TRgfc62gMna82y508IN_Dv7689ValgWWMBW9Al7UWUQ1Bc-XA-DJVGmpZOgqlFerEu1XmVrL9TqiaSY69_uMFjNh-PkF6et32p1jugpvDyNyZXrfcN91Mfz0NOTZh3GN7lv1lw5nFx164TK1XcqGBmKzNIK1QAMhjMAEtma4x0nFzB1Awqb69zNOYwGFZiHU-ksTm3ipd-pPpO5g72EFcKxHV7ymb9cF0rPkbsMvttS7khZwt-wFyLQQyXpItQj5vDUbwgLlO_Fdqmzl9-qBR3PQFLk4iw5md-YIfZzsB0VYNgz0mB0koZtpszt0CPVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74abf9487.mp4?token=TvjORGow1udcXsGYVX8c0TRgfc62gMna82y508IN_Dv7689ValgWWMBW9Al7UWUQ1Bc-XA-DJVGmpZOgqlFerEu1XmVrL9TqiaSY69_uMFjNh-PkF6et32p1jugpvDyNyZXrfcN91Mfz0NOTZh3GN7lv1lw5nFx164TK1XcqGBmKzNIK1QAMhjMAEtma4x0nFzB1Awqb69zNOYwGFZiHU-ksTm3ipd-pPpO5g72EFcKxHV7ymb9cF0rPkbsMvttS7khZwt-wFyLQQyXpItQj5vDUbwgLlO_Fdqmzl9-qBR3PQFLk4iw5md-YIfZzsB0VYNgz0mB0koZtpszt0CPVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76804" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cefcea39.mp4?token=Gq3ZwxtELhROqQ1iKsFS8NHaEU57bDyIFgP68ix9VhwDQf3rKa5F4YKnBUQqNAPeLiOLmj6Sf6jXhNfB1CO_-AaWOwQwO77x2Ph5cbk19QV1EgFOQkMOcJNISY8LPP8UVxEpoV3_rv4dCuLKWUPQeVkbaTHhkn38kQeJuwoCtVCC6-iIws6WzYyTQk8d_oSufBQxwcdZqmIF4EZMyAAIq1O-UZLczcsqxITJtS-VUyp56Ty8BNLkumobBswP8OjhrAWEv8BazG6npy1moRLRDdDzoZQ8bgdWhmQ1nHiNcSwqPx3uIaePrdU6kJS9bJrpbeSxsIAkzaqU1v3ze1IMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cefcea39.mp4?token=Gq3ZwxtELhROqQ1iKsFS8NHaEU57bDyIFgP68ix9VhwDQf3rKa5F4YKnBUQqNAPeLiOLmj6Sf6jXhNfB1CO_-AaWOwQwO77x2Ph5cbk19QV1EgFOQkMOcJNISY8LPP8UVxEpoV3_rv4dCuLKWUPQeVkbaTHhkn38kQeJuwoCtVCC6-iIws6WzYyTQk8d_oSufBQxwcdZqmIF4EZMyAAIq1O-UZLczcsqxITJtS-VUyp56Ty8BNLkumobBswP8OjhrAWEv8BazG6npy1moRLRDdDzoZQ8bgdWhmQ1nHiNcSwqPx3uIaePrdU6kJS9bJrpbeSxsIAkzaqU1v3ze1IMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76803" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76802" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76801" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تجدد دوي صافرات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76800" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صافرات الانذار تدوي مجددا في البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76799" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c006192776.mp4?token=aGXitVGlzWpDUwZN3lRjT0fTazyTTGy4KqDVgSdiUHX-ZNI0KQKgSROTPXRCzfu9vXA-xDdWXH_3YXCjtHXRSRgB7qFe0t3fTcdATfxUIaUp5qBMi6aHfSTn_-gvvcL6PlewNnhZDMR-DMJaIX3KAimYOCtdFEswwTsZevH__p137di6AWNmvMQW8LMoOyyIS9yHmXhBhiqQB_I2EgSjznHntHSsHmjV8rVoIihXmnc3CxcASDhijsTg1_qEBs-s-Ztu-yL1JUL9gVmtZTfnIu1WgiH2_qVJKNoLRpF3vw3z5H5haD4Kw2_dD4tnjXdyVxBcv-diMBmqkyMqt-POrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c006192776.mp4?token=aGXitVGlzWpDUwZN3lRjT0fTazyTTGy4KqDVgSdiUHX-ZNI0KQKgSROTPXRCzfu9vXA-xDdWXH_3YXCjtHXRSRgB7qFe0t3fTcdATfxUIaUp5qBMi6aHfSTn_-gvvcL6PlewNnhZDMR-DMJaIX3KAimYOCtdFEswwTsZevH__p137di6AWNmvMQW8LMoOyyIS9yHmXhBhiqQB_I2EgSjznHntHSsHmjV8rVoIihXmnc3CxcASDhijsTg1_qEBs-s-Ztu-yL1JUL9gVmtZTfnIu1WgiH2_qVJKNoLRpF3vw3z5H5haD4Kw2_dD4tnjXdyVxBcv-diMBmqkyMqt-POrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجدد دوي صافرات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76798" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuxkaRvvA6IffZfUMjxDxUqB_McZCenyswS3lEUwTVYxREm89X4aWeIHdl221jV4qURMFfYIEHTNny4ueQWUQfTTu3klOXF4uLSeOyvN21uWyObApsBmcbMoqInlVQcdgOXI7aSKiS9L3c4gR3vuiX1PebhJZKkaqH2I2YiMFuQ5Cq-kqK-Vro_ZEG7Wo9nYhzTXifXdTwQFU7qFNahODrr5GTjEOjd0mSYf4Ip1YXF17Sbq_QkHzXC3AJzfsV9x15zE4UM8a1kMPs6zQASLFx08mxeIKpiWykqPOOg1zPYDukbN8dcd2S_BOO5-y42Zgbvd0h-0g0U0DAKNMMrWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76797" target="_blank">📅 02:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bbb3482d.mp4?token=PTcQBL06NzJk7t_u4yB-8xJ24G7tnYLP5e-Otj39e_jKz9mj_W0n0G0h7lerxk5tLAxinZfQIgD5nblHNWAxDmIa2EFl-i1gr1y-5DVMjGztC3WQLJnT44VV7MEWTCCaDO0Yiod0DIWelcONIkUYoJGE27serGs4JveiMrUaquaVLF52dn6ezjfm07eBR1cIs2aohkSjvHIizNAJrqkeC0Qbk0fv7KWKFO1leGABzvd81ZwUFROFNyY9iEoUvvFhr-K1Mdc0kahIby04tEal0QMVWRVjGpTLIgc9TyfLnTkxdOTV4HW9U2-mSUqLIDcuvxZCsYuN18ueyugZ-FMo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bbb3482d.mp4?token=PTcQBL06NzJk7t_u4yB-8xJ24G7tnYLP5e-Otj39e_jKz9mj_W0n0G0h7lerxk5tLAxinZfQIgD5nblHNWAxDmIa2EFl-i1gr1y-5DVMjGztC3WQLJnT44VV7MEWTCCaDO0Yiod0DIWelcONIkUYoJGE27serGs4JveiMrUaquaVLF52dn6ezjfm07eBR1cIs2aohkSjvHIizNAJrqkeC0Qbk0fv7KWKFO1leGABzvd81ZwUFROFNyY9iEoUvvFhr-K1Mdc0kahIby04tEal0QMVWRVjGpTLIgc9TyfLnTkxdOTV4HW9U2-mSUqLIDcuvxZCsYuN18ueyugZ-FMo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الكويت</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76795" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76794" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cc4a4ac1.mp4?token=YfOI0nPOMR-Wf044sl5pGFJNHrfnKPvO4fUdDU85MswQtKjTpunjN1NN-wr8yFAZ4nkQoilh1jlpiP9uhN_97rPsWOcpAkYQc6JBWbapBZD_JRyl0aghOeZyb9bX8bM-c91quryM8DePNE1AcXLVUP3RLoPsMfMkmlGKzFcdnIYxzem-DKObTdQhwolLsUVmDTr5MmboYfhmBLcF7nKN_hVSACX1W3INtzONxZVTKfGl26A95jMKKHAwfyCw3ZuhBKK0VQKu5rk0_THz8szAJRje1vCIx2LHNHax7xebr3zps41aFJtNT9llnSKd5xPhKEu3Gs9IkbNSx7C-paO03Hj9Y4xBNIQ0d5SAks96sNqHb4gLHrsEYzE0ujEW1ZLku1LUwbP0dEpkbcuwhdBPtmrxoJxtZXueRBV90oTnxPKTYvMjuOvaOr3AhIgVexzJRgpBa71t51PjpwelNob60ObfS-bmIhQV8qkUyNTa1e2iOHbi7b3HgOeApxTVY23UD2sggAYhDIy16LNG8EnwJZalgOXd-UiIdk_xv0_fuzEkLO6v74W98lMMyt8mgbHmpek6c482jzck2tA4-ff1RWnvWsRmgsKrn4A4gOYE5J5uqWf_2vUKdI-3HjSs9XMzJn8XCDF6DWmALUDK6AOvMdTQd-ukTgO0kmwuL797O1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cc4a4ac1.mp4?token=YfOI0nPOMR-Wf044sl5pGFJNHrfnKPvO4fUdDU85MswQtKjTpunjN1NN-wr8yFAZ4nkQoilh1jlpiP9uhN_97rPsWOcpAkYQc6JBWbapBZD_JRyl0aghOeZyb9bX8bM-c91quryM8DePNE1AcXLVUP3RLoPsMfMkmlGKzFcdnIYxzem-DKObTdQhwolLsUVmDTr5MmboYfhmBLcF7nKN_hVSACX1W3INtzONxZVTKfGl26A95jMKKHAwfyCw3ZuhBKK0VQKu5rk0_THz8szAJRje1vCIx2LHNHax7xebr3zps41aFJtNT9llnSKd5xPhKEu3Gs9IkbNSx7C-paO03Hj9Y4xBNIQ0d5SAks96sNqHb4gLHrsEYzE0ujEW1ZLku1LUwbP0dEpkbcuwhdBPtmrxoJxtZXueRBV90oTnxPKTYvMjuOvaOr3AhIgVexzJRgpBa71t51PjpwelNob60ObfS-bmIhQV8qkUyNTa1e2iOHbi7b3HgOeApxTVY23UD2sggAYhDIy16LNG8EnwJZalgOXd-UiIdk_xv0_fuzEkLO6v74W98lMMyt8mgbHmpek6c482jzck2tA4-ff1RWnvWsRmgsKrn4A4gOYE5J5uqWf_2vUKdI-3HjSs9XMzJn8XCDF6DWmALUDK6AOvMdTQd-ukTgO0kmwuL797O1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق اخر من الهجوم الصاروخي على القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76793" target="_blank">📅 02:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e1fda2c0.mp4?token=nZeIUAHnMijbCOE_ZIp96vCQpzoI7Lxjlh7nFJu43vjjcrCW9dMbgF31vlUTyD1vPgCD7_gzGT0ug6JjxgnCzzLz02PVloXHpaju9d9a5r90c9Jj4s0auNX5XAGrmc7Iflcp8ZE3K3TX2LMHMiOiOWZAYl-eqVcNEgL24TS9dQKrd4Ol6Mjp84HwOWrCt-F_PSMNjivgV-YOt0Wqz7eCK8bwplEbbyru0LUUCVBA0gyKPQpLXsrkYEx9LsZaaqYyhf684SE8PVwORaEBHpDZWXWltb0Rg03NdAMvop6v0lFNJpa4uaaCE6qMN_ginat4l7keHBIHHs7MqnTCCvryW0oKJYYcwF1acnE-bl1Fz8PJCASpr7NIMbx3K1Y6H0UMQ0OBSKeAc9ho9lj8C8R-OvqUSYefDCwY2TArIYcfaJVNd0TkjZnyClGhYZj7v-uIEcErLprC9HRTEg0MyQNg_r1RXRTLG8VCn4MZNuzQZSwhvcfElWkFTFrFNXAN4bGBhtNLJHO5phz0cOBBzNSDxCNALXl4PKoCsRRFcWkZQtkbQpyBFJ351t1YezxAgVBBAnFBd4cuz1Gupz9FJL9HVflRwjZMUYXR-kSHRF_Fj_kAhXaiozsiHxI4t4Nfwyn7dkcCWz1QGVC2NF1F9dH-D4tufo9BsjjWW_m8A9oXtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e1fda2c0.mp4?token=nZeIUAHnMijbCOE_ZIp96vCQpzoI7Lxjlh7nFJu43vjjcrCW9dMbgF31vlUTyD1vPgCD7_gzGT0ug6JjxgnCzzLz02PVloXHpaju9d9a5r90c9Jj4s0auNX5XAGrmc7Iflcp8ZE3K3TX2LMHMiOiOWZAYl-eqVcNEgL24TS9dQKrd4Ol6Mjp84HwOWrCt-F_PSMNjivgV-YOt0Wqz7eCK8bwplEbbyru0LUUCVBA0gyKPQpLXsrkYEx9LsZaaqYyhf684SE8PVwORaEBHpDZWXWltb0Rg03NdAMvop6v0lFNJpa4uaaCE6qMN_ginat4l7keHBIHHs7MqnTCCvryW0oKJYYcwF1acnE-bl1Fz8PJCASpr7NIMbx3K1Y6H0UMQ0OBSKeAc9ho9lj8C8R-OvqUSYefDCwY2TArIYcfaJVNd0TkjZnyClGhYZj7v-uIEcErLprC9HRTEg0MyQNg_r1RXRTLG8VCn4MZNuzQZSwhvcfElWkFTFrFNXAN4bGBhtNLJHO5phz0cOBBzNSDxCNALXl4PKoCsRRFcWkZQtkbQpyBFJ351t1YezxAgVBBAnFBd4cuz1Gupz9FJL9HVflRwjZMUYXR-kSHRF_Fj_kAhXaiozsiHxI4t4Nfwyn7dkcCWz1QGVC2NF1F9dH-D4tufo9BsjjWW_m8A9oXtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء البحرين تشهد هجوم صاروخي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76792" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4c6cfc93.mp4?token=lCwjFhGcaH_aqZEOBB25bcoaBK7efHfvlwudz6v16QSQ2UMgJNnumCAd-1kkYUaVkQIZlU9Mib3W0zi0yrVzJ1mewgyxygrWOD-P6z0bip7oTpxaXAZ7izlI5JpsNthErokuYbhlrx-JZND_uCkDROyYGEpBORqfTDi9Wo6xUy093rIqH1cESOOHFdXL3PVvmmq95sA4aTxxV1UCwMAaG072bkCfMukFu4kodGAPy4xxqeIJPKj7jrAJV5XC3p_UK9STbHBWoN_IPngSsr4jmGSQ3QgmJbYjWy-k7FJqD_YMHWScB0o4_IVYlf9mS28-ZXFQPWEY9L3MDsS0NWtcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4c6cfc93.mp4?token=lCwjFhGcaH_aqZEOBB25bcoaBK7efHfvlwudz6v16QSQ2UMgJNnumCAd-1kkYUaVkQIZlU9Mib3W0zi0yrVzJ1mewgyxygrWOD-P6z0bip7oTpxaXAZ7izlI5JpsNthErokuYbhlrx-JZND_uCkDROyYGEpBORqfTDi9Wo6xUy093rIqH1cESOOHFdXL3PVvmmq95sA4aTxxV1UCwMAaG072bkCfMukFu4kodGAPy4xxqeIJPKj7jrAJV5XC3p_UK9STbHBWoN_IPngSsr4jmGSQ3QgmJbYjWy-k7FJqD_YMHWScB0o4_IVYlf9mS28-ZXFQPWEY9L3MDsS0NWtcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76791" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc_3smLtDUiWO4-BmUF_PfPNl54ghRvBpC1T9-ST8QhzBj0xZ9IZL-tuoflEIe_dVYTMbYW1H6buZ0WPVMxJ6n4vqpIDrnRz-JD7KRo3m3PYU6BPM8-7fHgeqxnnRJzKYf9bb-znoehiW17RhMGfZ_agt8XIo-HGeJIRXbOUCldOIECIlB278ClhlZo9R7zvYtAySVQ0Zirh5Ak5iviHrLDzsQYT98i95MhbYEjBbCR4fPTK7EztyIpUtpbbc-dJdghn2u2hG8DGoDLIghiSdTzTBXz_QLbHiJlQZexhZwFj1McMVF6UG9OyJtRB5iTagNQO6AeDqhFzoObkAbwEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من ايران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76790" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bix4u0HCJAX-u6TNGl9kJUHExFCif7JCC0arAF280mt3JfykAYyhzLKmUQhmZjXeKH3K4aAQOPQ9zmO92KegvGbqxtQ1iV6c4hZDsnq1Z460I4MJbg6aBN3JpVTOdXQsRzo6m7tPJsJojIXYjCbjl5k9cAOLGxitb3I4Oy9gks_1EK472-IAnBmHM2mnzKsivDYpoYH5efLnJ_Vo_O496hROHyLdFXB3nX6HB5-C-byho9a_9luceMr5HDykzKLz0k1HZqAe0cQsaQBOYDyG_2610BnsIWg1nMo841oz0JhrUTJlJFVic4lrynzaWdajTbp4Lweao8dR3EQG80cXMxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bix4u0HCJAX-u6TNGl9kJUHExFCif7JCC0arAF280mt3JfykAYyhzLKmUQhmZjXeKH3K4aAQOPQ9zmO92KegvGbqxtQ1iV6c4hZDsnq1Z460I4MJbg6aBN3JpVTOdXQsRzo6m7tPJsJojIXYjCbjl5k9cAOLGxitb3I4Oy9gks_1EK472-IAnBmHM2mnzKsivDYpoYH5efLnJ_Vo_O496hROHyLdFXB3nX6HB5-C-byho9a_9luceMr5HDykzKLz0k1HZqAe0cQsaQBOYDyG_2610BnsIWg1nMo841oz0JhrUTJlJFVic4lrynzaWdajTbp4Lweao8dR3EQG80cXMxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76789" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ab10aec0.mp4?token=ORRoFEFQ8zENUaybyOW9HvWKrg8uD65EggTc_Rx8IOyc18CbDIidgoyIEp_D2uy9DE3fobxd8Et9zu3S8mfznjc8KprgW94Tbx_7mq61jUY-aOxO7Xq2tGX5BzuHqIyNzd6L6H-OFpduh2Qq8gZI0Y4a42hi6YTh4szO1H9Lk7B-4T0kqD5gVFNomVcXICzTmnLmbixz4EmR8wguszO7WlTweW49haqpy5o-8DgqdjGEBPRvNR3QX0dkUc0w2k05pCdOKjEA2vZIjrB0xA1CytpWVh5qT3tCffMy9bMJUrehni7Tese1sb5savHqZxt937lZ8XPUjA35BjqhEkNfCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ab10aec0.mp4?token=ORRoFEFQ8zENUaybyOW9HvWKrg8uD65EggTc_Rx8IOyc18CbDIidgoyIEp_D2uy9DE3fobxd8Et9zu3S8mfznjc8KprgW94Tbx_7mq61jUY-aOxO7Xq2tGX5BzuHqIyNzd6L6H-OFpduh2Qq8gZI0Y4a42hi6YTh4szO1H9Lk7B-4T0kqD5gVFNomVcXICzTmnLmbixz4EmR8wguszO7WlTweW49haqpy5o-8DgqdjGEBPRvNR3QX0dkUc0w2k05pCdOKjEA2vZIjrB0xA1CytpWVh5qT3tCffMy9bMJUrehni7Tese1sb5savHqZxt937lZ8XPUjA35BjqhEkNfCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية تشعل سماء الكويت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76787" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky21UBlxaf1RU-o84V84CYUNrp4sEjwO1-3TsfEunyaJRUkxF20jJv8FiMmgD-eh5lQG_Ll2Ns86iyLsR77luHrWWW2S1pDSMaauTs9wJNJ7yi2A4EOAHR957CgPORtfu8T8-uy-USy6_hKOxp4twhPCY2Ow9jFjKMj2MC3avylF8T0c9RpWbqzPQR9GJ0CM9ttcd__oNHaS_Iisc2bxYivh2DITMII5SLUttk7JSuXOg4EioyN33j4mJHKTECTsbSbdWGtdaqNUXY0yR0l10BSnSo-Y8CBPZs2Y7RflbeO4LD0jchhhIGYqBaos-X3_OzTPF5-rwqWcJPD_ElP5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة اركان الجيش الكويتي: الدفاعات الجوية الكويتية تتصدى حاليًا لهجمات صاروخية وطائرات مسيرة معادية، ندعو الجميع إلى التقيد بتعليمات الأمن والسلامة الصادرة عن الجهات المختصة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76786" target="_blank">📅 02:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76785" target="_blank">📅 02:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76784" target="_blank">📅 02:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئاسة اركان الجيش الكويتي:
الدفاعات الجوية الكويتية تتصدى حاليًا لهجمات صاروخية وطائرات مسيرة معادية، ندعو الجميع إلى التقيد بتعليمات الأمن والسلامة الصادرة عن الجهات المختصة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76783" target="_blank">📅 02:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صواريخ دفاع امريكية تتساقط على سكان الكويت بعد فشلها بالتصدي للهجوم المركب</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76782" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a837cee.mp4?token=Wbj3xJlv9JM53xB9crRrYgmSHy7hmX7vC1AN2ySt-8-DoUgVnBrSFktmh0oAI6oI-RWJ3kb1wlGa4yKxCEHycfrXnBq6m8BPMhfjFSobGTXN_L9LxPTfUrck33DTE6Ptuoc6ErSznks8zZ5OcdcgBLXZJq1-SALQlAJ-091IOLQNgQ0wlFLP9mhMV41MlgAPUNPMQOKmT6ObBwCGTwBlSAdz0-qsDBcQifbJd27VyXQkM3ptRYNzyJxXZJQrVc1BIigIyPudngdmuKizN53CiNZNwW7IvAWcqCsVY0-kJRfzLWc0ZSjDpOpTXPDLRTNyFxock0NqtnxeFWbN3rGFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a837cee.mp4?token=Wbj3xJlv9JM53xB9crRrYgmSHy7hmX7vC1AN2ySt-8-DoUgVnBrSFktmh0oAI6oI-RWJ3kb1wlGa4yKxCEHycfrXnBq6m8BPMhfjFSobGTXN_L9LxPTfUrck33DTE6Ptuoc6ErSznks8zZ5OcdcgBLXZJq1-SALQlAJ-091IOLQNgQ0wlFLP9mhMV41MlgAPUNPMQOKmT6ObBwCGTwBlSAdz0-qsDBcQifbJd27VyXQkM3ptRYNzyJxXZJQrVc1BIigIyPudngdmuKizN53CiNZNwW7IvAWcqCsVY0-kJRfzLWc0ZSjDpOpTXPDLRTNyFxock0NqtnxeFWbN3rGFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الامريكية في الكويت تحاول التصدي للهجوم الصاروخي والمسير</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76781" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76780">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4649ab83e9.mp4?token=iC6Z406rEQO9XdGgNXKusvUipjRA2Dij0XidZHBKgsEQmaC7HQ6kesv_32zn5uU-YpI_veteJRuvSfn678ZS1CmcRTxuMJM38xsk8BV8_vIm8le4qUW0ACpCA2kP8X2nD_6GGNhMahxdTRlGiTxsTsmmMs6z7qVa2XZ3nLfADGHQ9iEKBWIphjg_0PYk2pdFnAqXYOcnNDEBRQEd0YoXqN1rOI7Uc9mJtBUhO2G6kMJD8gX6tHGsCFMhNUwPjwy0VGj-MH33hDsRERDhj6Et1-VtUf726hMG4VIQHgZwBF_7s5vJmdR_mhTk5NYwjWeYMT-xFwPhg62K0a5Y1Eu_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4649ab83e9.mp4?token=iC6Z406rEQO9XdGgNXKusvUipjRA2Dij0XidZHBKgsEQmaC7HQ6kesv_32zn5uU-YpI_veteJRuvSfn678ZS1CmcRTxuMJM38xsk8BV8_vIm8le4qUW0ACpCA2kP8X2nD_6GGNhMahxdTRlGiTxsTsmmMs6z7qVa2XZ3nLfADGHQ9iEKBWIphjg_0PYk2pdFnAqXYOcnNDEBRQEd0YoXqN1rOI7Uc9mJtBUhO2G6kMJD8gX6tHGsCFMhNUwPjwy0VGj-MH33hDsRERDhj6Et1-VtUf726hMG4VIQHgZwBF_7s5vJmdR_mhTk5NYwjWeYMT-xFwPhg62K0a5Y1Eu_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76780" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76779">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3nizMuk33qBlbkh1Epf-lXjtc0IVhKJ4DqNlm1s8b4zz7OCNQA6zmBPZpciqnoFtrV8Zno3VkShF2saEmDu4O0lZ6SE6y25ggc_GSXmIaHKaKoyp43OBg9ZEsEzFmzVtMe3uCdmE7poCX7yQGH-38g1ifeCGIN-a41z-zGADMCgAsSnno8FSsaYzifTKDNh7s0MbX1kjg89P4FICz5_TkNi_J-f287h64KvD_8r5h5PeYdvGNAf7IyTiSSAHM-fgfzVg1UKz3Qr_ITNJeNYbed37j0kJ23N6oHeRBmStH1nwKSEp_p61nUIZ5hXlKdwJiRqhjf7nX5jsNRqvzqsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهود عيان: انفجارات تهز منطقة جنوب السرة في الكويت</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76779" target="_blank">📅 01:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارة الدفاع الكويتية: نتعرض لهجمات صاروخية وطائرات مسيرة معادية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76778" target="_blank">📅 01:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76777" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b49a37c30.mp4?token=deXtTyY4_M6ZLbcd_KcyInlIHsqD58tis46VfGcVsDXjXDXm_X2c5H8k1Pw__bruai5VAd8l6ix-jrCErxJsyEE4JKuNW6uYELMPArJnxkSOLf6jhCYKOeL3O-diRGDnXuyKtwrRnqiIoXm5KH7mCe88yj4PA2JkVkNjytTOk4_eqUe0CaAWQxBvtEz6xJeOWYpcWTan8AALYJdjVnDq4cDCnxdruae2-bXLlnziSyx27v5bScb6ndHf3jbiBjgaKTO_CK323EcVzeLnjbgSmxg0X8e5FJoKax-q3NyvwtitG3UhOfgN6gOyWs7U5UlvGfJ2Um87vXkgcFTI_zv_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b49a37c30.mp4?token=deXtTyY4_M6ZLbcd_KcyInlIHsqD58tis46VfGcVsDXjXDXm_X2c5H8k1Pw__bruai5VAd8l6ix-jrCErxJsyEE4JKuNW6uYELMPArJnxkSOLf6jhCYKOeL3O-diRGDnXuyKtwrRnqiIoXm5KH7mCe88yj4PA2JkVkNjytTOk4_eqUe0CaAWQxBvtEz6xJeOWYpcWTan8AALYJdjVnDq4cDCnxdruae2-bXLlnziSyx27v5bScb6ndHf3jbiBjgaKTO_CK323EcVzeLnjbgSmxg0X8e5FJoKax-q3NyvwtitG3UhOfgN6gOyWs7U5UlvGfJ2Um87vXkgcFTI_zv_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76776" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم الايرانية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76775" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce627a765e.mp4?token=o4Ogln7xBpxtOJB9FjKAFg4Cvyi70xvqMAUmykn5x8TN0ROdgTq1pG-yfvPE_XpWHgFQGJB4FE8hNcLezxJrHC9yCBOyrQvVMWLsBr2XbKFq5lng13JfMkxYVc5uoZL_r9wDwMoKDo5lfhckO1jcBz4M3xJSuNNessPldcGTP-NsfrJG0vgT2uAi5jr_ENNlGhp-ph2z23RJx0YP0LnvnARvVuZKpYx6VCmgz2oQKraLAQErxPgCaF9oYOjuTFsZ_B2aeo_CHlAV2O-s7bDbH1QoN86cukMVKiE9VBbJNN_PZxHqlmp4QUnqbGo0GbX961U78iHCNooKJmUtI202IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce627a765e.mp4?token=o4Ogln7xBpxtOJB9FjKAFg4Cvyi70xvqMAUmykn5x8TN0ROdgTq1pG-yfvPE_XpWHgFQGJB4FE8hNcLezxJrHC9yCBOyrQvVMWLsBr2XbKFq5lng13JfMkxYVc5uoZL_r9wDwMoKDo5lfhckO1jcBz4M3xJSuNNessPldcGTP-NsfrJG0vgT2uAi5jr_ENNlGhp-ph2z23RJx0YP0LnvnARvVuZKpYx6VCmgz2oQKraLAQErxPgCaF9oYOjuTFsZ_B2aeo_CHlAV2O-s7bDbH1QoN86cukMVKiE9VBbJNN_PZxHqlmp4QUnqbGo0GbX961U78iHCNooKJmUtI202IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل عدد من عناصر تنظيم داعش في صحراء البعاج بعملية نوعية للحشد الشعبي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76774" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
أفضل العقول في
شعب إسرائيل
، في
إسرائيل
وأيضًا خارجها، مجندة حاليًا لمشروع ايجاد حل لمشكلة مسيرات حزب الله. سنحل هذه المشكلة. سنُعيد الأمن والازدهار للشمال.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76773" target="_blank">📅 00:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6fd55fe69.mp4?token=Sk--sqEWjH66Gp8npY1WSbbkVX6aOT03I4OhHVPgwkEEs_rIoxyWqHrvjIMq7F2_PwWPFYlWh6Fbey1x1s1bNA7j3W4-t88DysdMbxxVF9k8tjMnPEXlMd2bSMYwOn3Gvjs9PF1SfOYMDm2jo_LX2IkAJmbv76QQ4SeuGNp1s3xQe_lVOhyrh2zDeOBaWuYjSZ-GkFSfnJAotVgjT69ETmpLtsfrMuC75oUFmfa4ZpQ5Yu_xAaDJUlHCsnYGz2pKYG3TEs4fdocslr1zEImGeWXJvECG4QTzwXsuU25l2rg-6e65vmC080ycFksOqtxLwzS9Zp_2vMMJ978MBHEvlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6fd55fe69.mp4?token=Sk--sqEWjH66Gp8npY1WSbbkVX6aOT03I4OhHVPgwkEEs_rIoxyWqHrvjIMq7F2_PwWPFYlWh6Fbey1x1s1bNA7j3W4-t88DysdMbxxVF9k8tjMnPEXlMd2bSMYwOn3Gvjs9PF1SfOYMDm2jo_LX2IkAJmbv76QQ4SeuGNp1s3xQe_lVOhyrh2zDeOBaWuYjSZ-GkFSfnJAotVgjT69ETmpLtsfrMuC75oUFmfa4ZpQ5Yu_xAaDJUlHCsnYGz2pKYG3TEs4fdocslr1zEImGeWXJvECG4QTzwXsuU25l2rg-6e65vmC080ycFksOqtxLwzS9Zp_2vMMJ978MBHEvlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحشد الشعبي العراقي يقتل 3 دواعش في صحراء البعاج ضمن محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76772" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc9160db4.mp4?token=F7B7g9iZyE1Q2I7nU6gttRCKpBISHSGkuvlujo9qMLIMx3SwmQEAv77MO8wB4963JiIAsN4tecGohSkUPj1zNjvk9wtGoAmpXNgzayh9mUAMdAD2h-hoRhL5FP4QlkiSdROt4TOxRHFq7DelLBt1luVN2_dRg-lA8_rHdRYxrj13qEn1q2tfS8IGwxpzv1sQT_dI3Pn1eUExKkwrt_RQsdjpF7MB2ShTEU5bqQfkJEc73QlhZQfK2rLkUcWSH_a_1XG1qJl_gBvARnHeBHEzfdtZJnsDnRnx_S78gw9KVd4lNDGJ0cGsiLR-ZR8GF2yk3LigifpFwYXTzULoL9wfpYX4G-C-pB9ZJWFFgIp7r9ag23EPfM_NMewNGZd1pk-pubFVP0m7NZ5hRS7Ee89kC9artfIgSw-JKTcorbCcLUO3UeNhuQ4ie0WrJO4Xs1D33lFHg25B469YfjLqsfgVVXKoLOxiPB5HoiKgbQrczD9E4VkLYOFFNaA6moCGAltEaf3WLzsoMUTExkmPfI10rgt38Yg7ZDN-ELRAi11-WTOD7URKzh4VxUb1JAf63n3A2eoLU4__UgLoauo_J4WXt5lpDO4Yswj8g0vh_NfhHJ8BanKFlXxrtSeJn6ARDpKApyPbRWun4nmvOupHBT7A-I-ZbAXUKvQ3MPzRespOcx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc9160db4.mp4?token=F7B7g9iZyE1Q2I7nU6gttRCKpBISHSGkuvlujo9qMLIMx3SwmQEAv77MO8wB4963JiIAsN4tecGohSkUPj1zNjvk9wtGoAmpXNgzayh9mUAMdAD2h-hoRhL5FP4QlkiSdROt4TOxRHFq7DelLBt1luVN2_dRg-lA8_rHdRYxrj13qEn1q2tfS8IGwxpzv1sQT_dI3Pn1eUExKkwrt_RQsdjpF7MB2ShTEU5bqQfkJEc73QlhZQfK2rLkUcWSH_a_1XG1qJl_gBvARnHeBHEzfdtZJnsDnRnx_S78gw9KVd4lNDGJ0cGsiLR-ZR8GF2yk3LigifpFwYXTzULoL9wfpYX4G-C-pB9ZJWFFgIp7r9ag23EPfM_NMewNGZd1pk-pubFVP0m7NZ5hRS7Ee89kC9artfIgSw-JKTcorbCcLUO3UeNhuQ4ie0WrJO4Xs1D33lFHg25B469YfjLqsfgVVXKoLOxiPB5HoiKgbQrczD9E4VkLYOFFNaA6moCGAltEaf3WLzsoMUTExkmPfI10rgt38Yg7ZDN-ELRAi11-WTOD7URKzh4VxUb1JAf63n3A2eoLU4__UgLoauo_J4WXt5lpDO4Yswj8g0vh_NfhHJ8BanKFlXxrtSeJn6ARDpKApyPbRWun4nmvOupHBT7A-I-ZbAXUKvQ3MPzRespOcx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحشد الشعبي العراقي يقتل 3 دواعش في صحراء البعاج ضمن محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76771" target="_blank">📅 00:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76770" target="_blank">📅 23:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76769" target="_blank">📅 23:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a991e7184.mp4?token=JysW3BxH6iM9SJAvcK4Fiqb1itfmnGBk2RHp_LUx025pJQSpIK5BoqcYXMV20Cc9ZaQ53UywbihG2iNhGbRgJMdM9FqMyvsrVCoKeVHpjWD5U2g8_YBiWow4pO88Ma6BjLDOWvCRHZ3_EKEFc2yvpuhGC3nT0tgk2oCQgMflmN7DMNO3FeMgRFT95lnin5kedIF5LDQYLgmAQCNRj7U_QvtGcYjcY9YeGq9qAE-2nEVzP5obLKOfSkTCsMrMcsbcvv2CAkTZzxgRvHyxgz0cIEZ6Z16MHFuQSYIzTHtgMkPtzs0t7voMwB4xO5xXnlMkD2XIJ8viSfwlROIaF1875w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a991e7184.mp4?token=JysW3BxH6iM9SJAvcK4Fiqb1itfmnGBk2RHp_LUx025pJQSpIK5BoqcYXMV20Cc9ZaQ53UywbihG2iNhGbRgJMdM9FqMyvsrVCoKeVHpjWD5U2g8_YBiWow4pO88Ma6BjLDOWvCRHZ3_EKEFc2yvpuhGC3nT0tgk2oCQgMflmN7DMNO3FeMgRFT95lnin5kedIF5LDQYLgmAQCNRj7U_QvtGcYjcY9YeGq9qAE-2nEVzP5obLKOfSkTCsMrMcsbcvv2CAkTZzxgRvHyxgz0cIEZ6Z16MHFuQSYIzTHtgMkPtzs0t7voMwB4xO5xXnlMkD2XIJ8viSfwlROIaF1875w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل 4 أشخاص واصابة 12 آخرين كحصيلة أولية جراء اشتباكات بين عصابات الجولاني في بلدة زاكية بريف دمشق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76767" target="_blank">📅 23:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو:
نريد من رئيس وزراء العراق الجديد معالجة مصادر قلقنا، نريد منح رئيس وزراء العراق فرصة للنجاح</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76766" target="_blank">📅 23:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
أصيب مقاتل في الاحتياط بجروح متوسطة وأصيب ثلاثة مقاتلين آخرين بجروح طفيفة اليوم نتيجة انفجار محلّقة مفخخة لحزب الله في جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76765" target="_blank">📅 23:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2zr3c_UYFEbCQfAZHswNrx8BzQJi3w_ARPhwnOyw3Tyl1WEyrSZrcaBthauV19djXdAdY2LS1rXzmVFwvR5yK9pUMHOEXfWonfamyQvJMB3IiP-k2e023IIZPR4cNWEnofbkyiLnLzaUy3u2EVJjP9V_xje82_lgzGmrbtlvrRsYi_j_5HIULWuxihhFw88HDw-8MlWGIrrp7Yf5w1nx80YXcN5GUV-ZUndyDdCtkhReWy0cujLaaPj1glyyvoE9IQ8tl8lMTq2-Ddl3yPD3ui8pog8ik9oO_7-er_9LOtP2FZyJ_RBF1SU6V1Ga56Hh56HoH8mHQMLlUQaQc1F_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
توم باراك يشيد بالفصائل التي نزعت سلاحها
:
نتقدم بأحر التهاني إلى رئيس الوزراء العراقي  على هذه الخطوة الهامة، التي تُمثل حجر الأساس لحكم ذاتي عراقي مُتجدد، قائم على استعادة السيادة، والاستقرار الدائم، ووعد النهضة الوطنية. كما نُشيد بالجماعات التي سيُسهم قرارها المبدئي بإعادة جميع الأسلحة إلى الدولة العراقية في بناء النظام. إن ثقة رئيس الوزراء الزيدي في محلها، فهذه ليست سوى البداية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76764" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ‏روبيو:
نظام إيران لم يتوقف عن دعم الميليشيات رغم العقوبات ومتاعبه الاقتصادية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76763" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abYL8QVO6wVHou1lJJyK5-VskCxRLNBcd6VvYt-rgxVBWLgkrXmwlXTV3V_NbjxW3Pp_FhA9gTU1lzfZ3-XWxymRgA6PvyIsnVhesyEvoKdV3iZM2OlrRxTUUz1Qy-aD23G8uPuC8coKNMILeP5_uSkSMxRAfCO-_6epr70Rzco1vjaeH4d0Kmks-t8n57j65qddJMZmTjAA3KkQGOZEC_X7i5VYWroCvP1_JP2FZUPuyPHn_v4mWuFWXx4XkdnD5E2W1KSO6ycYM-ZVbTO3xWLL90eYhqYQMHF_Cxp6RRe5sJykwh15Fh-TqG3AkulUm8L3UspH3MVpVNI7__d0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
يسرق المهاجرون غير الشرعيين والمحتالين الأجانب المليارات كل عام من دافعي الضرائب الأمريكيين. كجزء من الجهود التاريخية التي تبذلها إدارتي لإنهاء الاحتيال وعكس الهجرة غير الشرعية الجماعية، وقعت مؤخرا أمرا تنفيذيا جديدا قويا، ستقوده وزارة الخزانة، لمنع استخدام البنوك وبطاقات الائتمان والمؤسسات المالية لتسهيل تهريب البشر والاتجار بالمخدرات والهجرة غير الشرعية والكارتلات الإجرامية التي تنظم هذه الأنشطة. يجب أن يقتصر الوصول إلى الأنظمة المالية لأمتنا على أولئك الذين لديهم الحق القانوني في التواجد هنا، والذين يشاركون في التجارة القانونية والمشروعة. سيتم إغلاق الحسابات المصرفية المستخدمة لتمكين الهجرة غير الشرعية، أو لتخزين الرعاية التي يتلقاها الأجانب غير الشرعيين، وستواجه الأموال في نهاية المطاف الحجز والمصادرة حتى يمكن إعادتها إلى دافعي الضرائب. ليس من السخرية، ولكنه خطير للغاية، أن أي أجنبي غير قانوني يمكنه ببساطة تقديم رخصة قيادة الولاية الزرقاء، أو وثيقة بايدن الحدودية، والوصول غير المقيد إلى الولايات المتحدة. النظام المالي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76762" target="_blank">📅 22:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e781b52e.mp4?token=q74q9I55EG4LYRVOsdvhze1Yky0WfftHwId9IwO1wbF2PSuSsN3-yRarnIsQYR1NjFpP9GDLeUOs5HPoiTkmW7F9WE3f1rft4ryyNllCHhVKMvw1mU5gagiMJomy5LdXZLoOuo1xY01JGND3T83z66v_-5GDf3V4B3ppxWCmz8V2JAoxjVBh59jh1RETwMOjAzsPiwF1HZjeqotCd2YFS0o8wnQps_Sj4_MrIP4tccGspQ0_0Q2W03byPBQQLphuNy_SRnj8Z6V4YcnsutYG1vc0TgB6EAcOy-Se-ZqKUAVeQLfNrMGe0QQRbbNQ_bOMf4P1chHyZcGQdExNbLbdCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e781b52e.mp4?token=q74q9I55EG4LYRVOsdvhze1Yky0WfftHwId9IwO1wbF2PSuSsN3-yRarnIsQYR1NjFpP9GDLeUOs5HPoiTkmW7F9WE3f1rft4ryyNllCHhVKMvw1mU5gagiMJomy5LdXZLoOuo1xY01JGND3T83z66v_-5GDf3V4B3ppxWCmz8V2JAoxjVBh59jh1RETwMOjAzsPiwF1HZjeqotCd2YFS0o8wnQps_Sj4_MrIP4tccGspQ0_0Q2W03byPBQQLphuNy_SRnj8Z6V4YcnsutYG1vc0TgB6EAcOy-Se-ZqKUAVeQLfNrMGe0QQRbbNQ_bOMf4P1chHyZcGQdExNbLbdCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
توتر أمني واستنفار كبير لأبناء قبيلة الفواعرة بسبب توقيف أحد وجهاء القبيلة من قبل مايسمى بأمن العام في محافظة حمص السورية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76760" target="_blank">📅 21:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUUkn5p6BlU7APyzcR5b5twmy1A7N31bHxgy5Rv41K7xppdHJpDcBCjfdkCT_Tuz5UilSvrREyXZZa-leEjOIwZdUYMMJFW_ymv-sHAB6Dqtg5toR_9V9pqb6xK0ABP4DSzgiCRM6qLvhPLm9WdT9P8lctSmkxYu30QkA-JmSp8RtAHug_tfctwIQC1ax5HG5Q0s5QutfjXexPF6DfuLECRjWxiZO_6IG-WBK0A1m7ePgqS-6-_0KF2KJx0HUR8EMmKHIyaifIKZwhWNSCFsUA8y47coINpKpKcFg3_-muzcZ75S_gAzcgRzgZRJzDltY-ZNtn2qu7v4k0hw2d-tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
في إشارة إلى القوة والصمود، تم الإعلان للتو أن عشاء مراسلي البيت الأبيض، الذي انتهى بشكل عنيف ومفاجئ في 25 أبريل، سُجل موعدًا جديدًا في 24 يوليو. هذا الإعلان أمر جيد للغاية لأننا لا يمكننا أن نسمح للأشخاص المجانين بتغيير طريقة حياتنا، أو حتى جدولة مواعيدنا. لقد طُلب مني أن أكون هناك، وأن أتحدث، من قبل وييجيا جيانج، رئيس جمعية مراسلي البيت الأبيض، وقد قبلت. لا أعرف ما إذا كنت سأدلي بنفس التصريحات السيئة أم لا، على الأقل فيما يتعلق ببعض الأشخاص، لكننا سنكتشف ذلك قريبًا. على أي حال، ستكون تذكرة "ساخنة"! ومن المثير للاهتمام، أن المكان سيكون ولدورف أستوريا، في شارع بنسلفانيا، وهو مبنى وقاعة حفلات قمت ببنائها.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76759" target="_blank">📅 21:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10423e85a1.mp4?token=ge9qkYL4058z2LQXXkCc94CFmrka7K8Mpmr4_4kZgxHa3r886bF8WN_CAcoLc7UV2RwyaDrco4P-poNfczEQWG8WAnBZOtsnA3qQ8sjP7DCppg0CoinxNTQIYY6lZl-QAMFvPDr5yO84F_BEBEJLyaBHJLmNUY7HVtXqfQdqgJoyX6LABPiUcOSpdcdsv1-W6FgtZ_BLFWBTvXDRwyO_OOooQXgS7Rajqn2T5zP9orfDry2D3SrFCY4OL7c2WbwIpp5yG4LWOnhFU_lu43rkqLROO1uXAJQi3qSVn23jymWgVVsnJaxQr-ToJ5PgUI09Hy8HqN-iebmF3HlNILHIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10423e85a1.mp4?token=ge9qkYL4058z2LQXXkCc94CFmrka7K8Mpmr4_4kZgxHa3r886bF8WN_CAcoLc7UV2RwyaDrco4P-poNfczEQWG8WAnBZOtsnA3qQ8sjP7DCppg0CoinxNTQIYY6lZl-QAMFvPDr5yO84F_BEBEJLyaBHJLmNUY7HVtXqfQdqgJoyX6LABPiUcOSpdcdsv1-W6FgtZ_BLFWBTvXDRwyO_OOooQXgS7Rajqn2T5zP9orfDry2D3SrFCY4OL7c2WbwIpp5yG4LWOnhFU_lu43rkqLROO1uXAJQi3qSVn23jymWgVVsnJaxQr-ToJ5PgUI09Hy8HqN-iebmF3HlNILHIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في حكومة الجولاني مساجد مدينة حلب السورية تتحول من دور عبادة إلى ساحات رقص.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76758" target="_blank">📅 21:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
مشاهد جديدة من "حرب رمضان" تظهر دمار واسع في مناطق سكنية بالعاصمة الإيرانية طهران بعد تعرضها لقصف صهيوأمريكي غاشم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76757" target="_blank">📅 21:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭐️
‏
وكالة الطاقة الذرية:
لا نتصور التوصل لاتفاق مع إيران بدون مراقبة برنامجها النووي بصرامة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76756" target="_blank">📅 21:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇦
ليلا عبد اللطيف فرع أوكرانيا "زيلينسكي":
قد يكون هناك هجوم واسع النطاق هذه الليلة على أوكرانيا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76755" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي:
توقفت وكالة المخابرات المركزية الأمريكية عن المساهمة في بعض التقييمات الاستخباراتية لمكتب مدير الاستخبارات الوطنية، بما في ذلك تلك المتعلقة بالحرب الإيرانية، نتيجة لخلاف دام عامًا بين الوكالتين حول نطاق العمل والمهام.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76754" target="_blank">📅 20:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKbxo7I7g68qKk2j_gec9NmtmbysmeK5otk3qI2IJ2YwCMPlLWBJQvlTDkexfqVjXGjqCMsazeA_HGDLRssGu2ks9qeo_dcqGeKJwG_mbBzm9rZ6Jco7ieoarswualLfkAsoClQ0gVDDIQwzC4Py4SZ8v-aVz5e70uYHS1OAzjq8MTzjtj4x-1na2BzagWveSH51crYkkpvKwkm30pEqc19dDghWcloM9VHvr6bqltAKj-ty9P6sIeXfGJS4rN3rvfxgscRGrpV62JDUd2IpMa09V9kMC-Rm-8SZ74-rTnRKvuDnvJSHy7Xi_BqkEzL8sggCVAS1_q6SH_HHZSbjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تقارير الأخبار المزيفة التي تفيد بأن جمهورية إيران الإسلامية والولايات المتحدة الأمريكية توقفتا عن الكلام قبل بضعة أيام خاطئة وخاطئة. كانت المحادثات بيننا مستمرة، بما في ذلك قبل أربعة أيام، وقبل ثلاثة أيام، وقبل يومين، وقبل يوم واحد، واليوم. حيث يقودون، لا يعرف المرء أبدا، ولكن كما أخبرت إيران، "لقد حان الوقت، بطريقة أو بأخرى، لكي تبرم صفقة. لقد كنت تفعل هذا لمدة 47 عاما، ولا يمكن السماح له بالاستمرار لفترة أطول!"</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76753" target="_blank">📅 20:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
رئيس المؤتمر اليهودي العالمي (WJC)، رونالد لاودر:
منذ 7 أكتوبر، أنفقت جميع المنظمات اليهودية في الولايات المتحدة معًا أكثر من 600 مليون دولار أمريكي لمكافحة هذا الفيضان من معاداة السامية.
هل ساعد ذلك؟ هل منع كل هذا المال - أو حتى أبطأ - الكراهية ضدنا؟
الجواب هو لا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76752" target="_blank">📅 20:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD-6buzosN2ycYa2I4KlDOhWvbh9vI9Pr8OyTwNQm7v3f-hu1qLztEs4vslHnZMx9Uzik3Mr0BY7GDE5FvY_BdT6fTCH68hozc9ioZ6nl6n--mcNJ1T894HafFgR_y-xJST3zpANTm6HVJR_L9EyFsB-1fEJ1s9UeD5hH3MGFJzH0z-aWAuRxa0DfrOEAuCNc3PbekuxUi1RQhDpKdOVOmCkkcR1r5KgrUy-78_8tklY9pMp_qeN8yGCpS7uhdL-uMT2mD_i2efOQp9yGyF-YshsSsVbqJBcNa1CoAyQwvjy3DdZ0yuZg2XA_-ka1O0-7enQn2W2FzUBw7gC7sHTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
‏
جيش الإحتلال الإسرائيلي:
سنصدر إنذارا بإخلاء الحي المسيحي في صور إذا لم يتم إخراج عناصر حزب الله.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76751" target="_blank">📅 20:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اندلاع اشتباكات مسلحة في السيدية بالعاصمة العراقية بغداد ؛ حصيلة اولية مقتل شخص وإصابة اثنين ..</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76750" target="_blank">📅 20:17 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
