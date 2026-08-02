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
<img src="https://cdn5.telesco.pe/file/t9V3qwRjqkK3Gm4E0f9xr6BO-LmX9NjH0IqfYWSeWlsIiSvL_YOIVhZ1R-3F8MBPhgvlotiG2ZurOOXQ-OoTbaBIX-tMSKqbYpGvVPOGbS57znO2LKARPlNPdroTfHYV5ts-gfEf7-XqzdGCRqBAM20tscYAu12dUkHjTSDDR9Aj-VNj7oL9I4pZdF8cPOpaGKa3e9e3rldKuTi3VGlWrNu53nhPT5H4cJiiTWpxYaMDY3ewNCMpD5rYCtExd_sNS-dPgS2Vqjt2uJkyFca9KmZlu5J3YxIcARAHVqpaJUlnIltmy8pqnrHNqxDi9H7xA0MxNKnD5DttpJ23a847yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 501K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 23:37:37</div>
<hr>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtBuGxMX4z8Q4-7mtkGA1HK0mvta3V4T2H1bEOhj7v3uQvJ7uGSfSQVMunsTzwxce2-2FsGpNsKRZPp8Z8ts4Mn2ubC5ve6-vh4sf46lCnxoc2v-k59SK4rJ3vB2RZVrZccNsAyWH03Op1SFREfHM4xmUO83-ZUGuLZ-8glWLAAz94xK6DW9iA_Zq9iBdhlRzlUPTj9o9_HC8rKa4Z5Gsh1AGy_G6Gr08y2cIOl1Te9O8znxnpJitgtNVsFB1kCP-QPBOqKuv1PHj_T8iidHqaNIwZvjnDOnyVI4IOzi_pIPa_twOaLG1wdsj0WRfHvc-5v_yvYINnxKVmzs6m6YxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuwkUouDRqDTUE1FImiwbLac18WgGcd6Pfywfy49u7T7xbIJ-GqQU0LwuEQofxIGbYR7NdQHd68Xi7Ajc6q5ekwOhjxcTm3wLKKe-aUDLBbf2nqAJCW6vy-1hHVXiXwLSQhftZ5SIeMbk27VzYFVrjfdqP5aIBUpeg43336szcfi7ggSfZ85q1YUSVkjrscMtue9a6fYdQN6TlWP1wsPh1Ja0zPi0CsQh2_F0yy9l5Guehi0SPEnf5Czn45LcXjuzEsIaIJN2cYESh09liW4xvsptHoEclAzP1srLFJa7K2Snqipoxj9Xme54B8o3wwcPqV-p6IcQcOFF4k5TsmFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ofCNhZ1eXlL7KTd0qoSpbRP16wSf9NTFvZa3r1yaLxObgyMuG1DyAPqzV4cVrdkT3pshFu13rlScWl7IsakMSeEZhLOnCYRs1ucpAaabNPYuG7P7cQbV3N7XataSg64968U4W8CSIpqfT-VBIxDHaLu4pxWVrxTUWYjvG-JxLHJ-UiWYyUUQ7M4i1oRV_fcrKXzHolJ0666WGa1Y6gXLAdl8Tg73S9_jp40jxO_wffbm4EATV_YiX6mLEfWn5ejynv9YvdLydl6QHRfHRTsXW8EEze_d-PKlSlEF9j9E7fAy9I0k4tm9a82b9_g7tjwhbysa8fr2pKxYfnSb57rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxmJjOyBZ0BmweILxNdcjJGf-C7iBaQqno2sGN-ynGvbJMWxLJeSbqyVgcG3QbPDqP8ZsUCIrOS619BbMJTKFNbVjVEuHOgRmgesIK3e2UWT_M3p7kLPzjXYvG7uAalJm6qbVBJuq9kt4VGCZ0WXGs99WGzPMT-f4g8PUU6Zsx9rWhSkcKvObUAyrr97ejf8l7YiMrK-KohPlNlKddRZtZNYbW_MBBYGICTRITwgFaVndHQz0A-bUCNilOJ3iKl6lTCzDzQWqbx7-lvFLG0OaQHDBuZTPoLDOTyLJErArSq8C0YuEfskUddrXDD9c1jr1-5Sf8BDs47wVbloI4NazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNd2CdItzmWQo6TQnbKw9Brd0z29wFc-gAxOfjlDA_wsojPV0bd3tKTi5q3XreUmdeUIGMoenMYyFskj1wihTGD0hgPMlfA9PXv3eDhWHvjpRDn1Rw5S3MND4iaD9Fq5ddGWWtVQ1fF5KZyTbx62VvUmzOUkUTOceTyB3ADP_z5CP-kooq3Lz57mVK90XCluycu4P8XEnQxjbDPITS1m_Xxa92glNOvnUENhg_OzpTnF8qyFHs1XgrGnXQGVsb6vBVePUtKWBZ4h-jb5N0GL8eWfXwM9ljakaoAhmb6WG1-NiLOoYuHm8tqWEl3_g1pIlOkBhrrEgtQ2fCJ-HzXn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH_M--OTSpuK6xijkzCgM7EGKq80OhtwgVWGCmearlmC7aC1W7FFknIEq6nL_XcD2-1PRMa7TN_AvioWZgb1Y9Sw1E8lowh6vieTh8Pj8np6ZMteYWfrLAWVOR-hf2cydqxNpt5RoKdl-pDwSGaoaty0l91sblEiaxt8Z0O8zKVwaroAlkMGvzbWxUaclyhTnY7LJBWhYh5b0T3H0A_NzaUxzvLrudZfGUn9iRNmdHVbqT-qhABGowBUMuFm8THUJ9SKGkAKhzapsUIyry2AHAesAlXmkNKOcnvhwtHny1gbkn0Sqjo5bgwrHnjBoFTfKHH3SvosALF03ayGG7uAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C19gnHYhEj1VTaqLa_JsCTh_xcby803d97Nh6n4DhsNQgcavXnqfbwkMDEI42paHkYqeqZPoQ6SucfnB_FZJex5zIXOfPquHvm2Wz38IUdOeGzUGTOHxDktiv3VL-kI3MouDZ8WP1Lv8ZTJedzODGEoCXwCcmVohKL1InJw3qx_Y1_7gyL11FRNSZzdJBEXjEll2zt37BRgi3ceSpSC3-h3LOZmmwR_6wW84BBj8DuHTOh4QG3xUEuQ45FRJhnsbp9JZyfI5EVSVk_zBEiP_V4-4Dq7hNViPYIMu09llUbk-EH5TCczvdC6QRFq5KdRctf5Jbs_Iz6tXaurEgKkPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuH7kZqIo1KPVOKHCVJPbJrNzCiYbxfita9GVSnduXxjTzfi3AKR7QVqD2nd-eWJoNt7Kj_9PkQGXGn8UWeBozdYrnWboh3KRhAYx0KeZEtwFxuqq5M4jdgdPw2qB_T6l7o0U62X0tB8Jgw2fvxLiTlnGlrBI6tIUutdS2_iTbtp6rXArN_o3g-VJdo8kd6NFGJtBPwvzFJNFiou2cFRZ2_md5Uv7DzxLn74LMM7neTNxC9K9pAzd-TYLne0ZX0EjrkVdnU3VhR6E-E9IDaDHVv_A96DjcXfrIwlg3Kik3F141o20II0OP4z49ogoj43VGhubaaRIrXgQM0cjUA70A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx67Yuy0o0FTpB4N8sJK3oDGHy_j7THIM9i-YoN5yu_GjjKxTYfYbSEsz4jE-d3MGf9ANyE2U7g02H78X_ldCmpmmYOLIoA4dOqHs8HQQrMO7I4_GQHECzPawzkkhg34kDnARRD4woG5CstP6V1hkm60EMOXUkkIFpqrwpMxsR4qhAiB8vw6Agkru-xxoAc62Pvty0qRFcvNB-rTr_il0TLB2N6Fgw0mmeX9YezTAqJuZQ_-BB1wDvt4xqAsCk3xJO6zWt_xd8cimQ-HPCASFS6ls6xoogG-VEBQcedBACp85U-qpNJ1gmjuqdGhrABlv9QFfa4qGOCKoT5lxuJTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpIfQ_GT7qrU7EH7jDyci5ZkzH0ZluY8vIFWDzsuErCDf_ePXKwpNjhpQl9fv1E3eO6mhKzNe2Op6fbLgWgzAjYSI08JT0hiFkiczU0tHW6QEVs3ba0dtWkQ8xV8BR194hsE-6XagNoLDBIEqhhTolLN4hJvDd3fVRo7FgamjxCRa7fuu_bpbfWFt0-oblVoMc8anPPnKPQxvjAsd4gXgwRdZZy_fYwaE2NM9UuBttZYv80W-Oc_BSU4DEGZpg8qCV8p_qfVu21B9-GcLCXPf5jMQACbQiWW_l7A0AaKAb7AS-OtfL5IaKxjNUSk9x0iH7ohFEKTBcHIul_g0GAV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1git3DNZi4UbfRWiWLlD1mmu0NapExuNFU4qGBTdm-_vodScDPaAwNxC4nliw-K0Z8iJ4s4r5DWarkKZ6pDGbOd1FXw-jqVJYHgKotSo0cm-GfqEhQ3pQvpHatdzAIB-erj4llSZ62UtBUAZyXaLfNi2yf2mZLZk8y3sI_uHB_g6FEk4JRlcW79YR1TxjU_1UfcuZqGA5nEAJvI0g7l1-THdSkwEeVuehBoKquvSBklv699qzDuaZ8vINGtHK9-9FQzUgzcAy_RY6TpbAUsLcFKROFRoJeoL0FlTVV118_me78zNU7Re38yaFQSRnf_xCSkRFdzBCZhQ3UpJaRSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYdJqaiYXZyYi__F1XAM22YO67kdAKSV0F4hU1wqssDH9Vk7cwuQtWU69sDsUO99X4mp1aBkMjbJ0TmfrLcjVQ_3nCg3b3B5ZX-F9loeZl414NEvwOvVoEgrVOHJXZHtZXuDRrnkCUdkQJw5ToO-54vRfcZ2E1-DzaXQxkofDCjD3ZHTLHihzAr0JR4aKCjox3HAa0-tsXKieWvxWvDTLxoBr3UgU517HxgEARNp71_7cBEyQhEP53rBWZLemQliLNqaKorG3IGvyb7hy0TI-imKL1u_MBE3OWtENz2HpCDlnIjnBWVw7ARVjv9OGyAY3QyOIV9GgSD4XL1W98u-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWyRHGdSdije0HpZGADMkjPvQBjUAqjCQTuhjrTvgFA5h9wsQdvRzOupAYblL4RoSYFRUZBM_goRY31Z84Oq6fYpmzCChxLd8SZydJWdoM5xZUJbcYKi2MqrzRSgGDOYbsWL_76wWEtBaDoF_ckUF0hGU1JXexYFagQxZPWRGhVYQza3vfkEC8sgfz-nBOz4HdPWK5EPPN1_LKF6QokNu0MyGvwR14IHBdMNc7G1DNZj4_fu19NojruX7h_IUv5xq2a7AFgYY-GGAO4ChbhIRarEnc0uMeONnSHjyKPy3MvrTsM8krDFsFPIrjwzNjmlggiN7B9xoUjdmtt2Q4rgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0HCDRgZIIq2HuulZtVyzYvfMi5IeDp_yshZ3Hq5trumVl9DKS2-yiKlleQpPuVcEvcjvhooiEBtifLvo18H1OUNfgkxTfvuLaDB790ZjOsF19TBniimJexe3vrIyknaoFMRsqPpTWceZkWwMeFA9LrNsKiRBO_Sx06-su-YHH4fcVQsX1j2X8ydqWYF9VLVYzrJve4N3ma1G7rBMnl_wyXdhK7rHR38ADbQIZVuB6GqEcJbZnwN3hvT4ILRRSfXpFkB3ruOYlyrXvWXkp27xqsmLLHOAggQqnka4ba3M4x0ZFDqHm1GoEhZ5N4-DLyJk0LYfOBNzdKgLhQI6dpNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBjxBAM1LmO6x9esji0nAoK41Y-y7bqr8CqniZJlzNJQ1NH2wZQ2ynJpVOWfjjhjUEIxp-DVi5Q4_fjeMaPyGuzeIvinf2JDWSadi4dVoc8tTA5NEd1Rg6twC-z4uD1bY0RbqQywaZANpi5PwQAqfhPjxdPW_CHa-Jtf6Q_kPeDTqhKctCYkNOSHJugrkmvkXtt7Z_9P_zzyu5r9GMQERNHV7lkgEXqPSv14H_ROYu_kvV1Kr7mwRCnkgQUgEf1NBBThbTbuKn3vIuCZbm-mnp3yUhlloZ-6kvKA4Ns6hTwH_5PylIu3tYoOpDhepyF11_zg4rESUHMicZlcuUTGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMjJ_qNfR6zo-B4GdnkAhHIIqK3JiGKAmQJH0AtVdW0y-ezq7K_o3o9rdbmafAJFiYp2m2Vu1oX6sKu5xlicb_5lTFuzoNTr9TaL3OxutBt_MfCzq0xOphfkFSYsN_5KXsbjTgqF5gk1dsSc39NB9OfjcIV-DmlO9F3jn52uMYTrOj_GfvzXiCLp7VhZQHdgCfOAZSyRyyPq5KHdTvPnBdD_QprZDyC6k0P4Co864YdMtFybtuu9ISRTJZJm9jZJd4qpcIU2eQH1QvdkJpi5YRwlEm0HUw1I5GqVs2Mr1LX7bkYp32Tq_ac_t2l7YUMJOS85a50B-H2S7JJYNUECWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn6Od9pp-UP1ZWfMdYNRmiEo2G87UABrsayd59oNFuSiX3xHOKJMpUy0FbHEha7ZGI3I42mZIX32KRXZQs7ohDUkiJuWEm_-53bBfIjnDo4KdCNbsFHNiUW8eIORpTiE2Ak23hKor-OGVwP3yQeOrBJnURiqBup0_4mTlclaE0Ij02v9DC7VOpypK0Mj9qfGRiMVo32MWL86FD2_wZoB9-2kV7TLmk8LRa3_30j9Hs6oVT19aC3BLDka7rcc7kIc_DfYfAb7jktbOfaqWk0pcRiG7ujEy5x45rn6j4e9k6Zig0KF1WYI4jS2jiWLXjfXcWTvV7u7JBtd-SlISOMKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAbkOKEeVzbJs-rSYYFtOjGp1A88eyJrnipNsriCzb4bJau4ETL4oQNkcim9BjL_amaZBLGj8_a1TMVzJt9TIOoiDNmShR24-j8X5nqz-OhxNPrC4Jj8nSZY5-niIYQFimw2BLwVAah6Ftzkr_p9Z3tRDFqWco3FbTaX3iHBquIJupV0E0GIhT_UzEiiaVlqIwbUfKJpiTQvpqdAKorwvoNaxSQD3rOR4KDSCv0xl4rMCz1xGtD-sOPZUtyNeDPMzEy-A7PEvCq2--MvpnHRTRVYKLk5DHMyPzaOqcEBlHAM02zp3KJV85PilXh8OCMnq2NTS_2YHb7qvv6EJJQlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEOVHNaZv2Jxpa4FGlutaaQ1RN5oZTeTOac107O3ExlLld8x7-VadbIqSuuLrzTF40_8ltaCjUQ9p_nbge5HvDBAYjNhgxSh7_yre8yTREqJ9qkLg_V9tbEyDjiBKI379_1ohdzErultbb1__og8ixJVCWW26nMZSiA_qgnPIWRnHT98LLzMlO0MakrcdqQUsph1RpQ-pYUkd411SUr7E3UFDuRSU5WvPKLJczswAboac73jrhnvgnPhszQasabTwy5DQ4H8rWAe4667xZwOHPDrWqSVIS2Nl7EiL-P5_9NmebeLm61HBwqHmI9cGSC3bUtpcAZ0IHZZhRRcq4f7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbWpYUj6mrKFYAaIskFT2Bmr0zTJfJoyxk1QMRn0bRYspK79gEyC4Ui8Cg351pDGVRjKYTzClNOLzjNERUte11TgdMqYd_Q0uYFucdHjH-_DbLifbRYE2ePvIL6xnzAgpotLEgMGOw3eunQlFxJ2uvKovdTmUzf0JO_coqPROYc0ssS9QouZAQVEzhf9sjBd-8gN2d3D-xFHEPIKczIc6P921UFhwlT6TPnPuGpXwOvk_yD-0sa9ujO74puX7mnyAcVBf2vj0THcsgLS7lMv0ozFd20iZZuFk-dzpdgfhrmdPDxn_3zTdQJwbClCAsQulgxx3M7qlL7W8BPRWgpL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpMD_1FG6n3vd4aatAz4wQbDPL61KikOWUNgLMz6OcqbIcouug5_F_8InnD8NRM2mNRiRQasEm45dJkAVBb5q_occWGpw9aj0mg27J0Mw1L4Tcj201mKBn3psSMElUx97Z9EHyNHH1EtHzzlVU8NuGDF7XgLPXGcul3X6VuEyb9X6-ho8kI5E5sSVGgpadFTzJeQcHJBBLIsOxyh-ZGV3UwjAD1Az_qJr-x37Gfyh461L5O3t5d4KiuKN2AYRsJ8QPt0kS0ze7jvacwD8XXNuqKji1PRIIYdXTro13kG96hxLgt1P3AiZtAEdWu6saQaOEwzXaPERnqAp7zi5ylLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q59OSAtfrpCUVoTduRY2AMt69f2btWXtgTsWicBIRsiRBvbyE2kZLBtuHnBjJ4R3TMySAgRXHPEOICG4V9aGxevlSb7Sse0FUy6McXh5NH97S9DYfwJlvXKXb_-oKIo014lLqRawODUwk-LB3NA23CGjwobErFgpvQ6ku61OURlFLSgfVNUTNdNTm3_dpN1oHfgWTlI2LMhU0jZDnqgdby7pxCxwqW-j7EzZp7jtrIMb331sIj8rDYdsThpVR6Iw6QbqcvDVTAtgQUqY7gQe6ML3FmyhlOHz_r07Qt1gQ57WszTuDRcTBCkODRxIj60EGRIKM9fOU-ZO2QBz5drzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTMc-Y21r0xJKbsEAbVDDRRfrdt6qMKPKXkeAt6cP7g7fjUvcvQ5w6_kgKtHqX2UPecPVPbWdg5dsBPwQ45Imov_zaXPLqbZr36TAiYonRas5fnMPn3H9roOo420LFJ4y66yF9zX3PVH3el6yWYx6pFeuwNMB4dz4zCQZ5POkiTSglUKkbb4AY64QZNX4V1TIOjmqN0GfNbNWdNFyaYf11Waw9qbPi7swO2ajkdc9Xb_aHwreTq-5dF7lCbz6rkyv_pDocpugHSTcDsZ3NnDqKCrfAz9wgu3pNawSD70X15YRm-T20CjiczRI_-MHlgbMFqZ4DFbxbrpFLjDW82BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=f40KZdm4Ab5t_zLyDUMqYNMdKRq9iFRue-hkJsu5ddONOS-6u2epmU13DXPvNoAdUL52CwNMD_ZpkmYKY8bMSPGJTI-cnaYLFNNkmDaMpqgKt211P5_U4pxWWz6aFpejz29gytiIQu7O6s-R6WexDvDFRjVDc-MHpOMeCsYgRRQfj-hmNpxneGR7TxQkhnT8K38rv5GMUtgzK-qxFfqS0Nb8VQJlvAydZRIOpoJHGtLHrpz59nHg2ZnwGX9MML83Mt6t1zXqFhGWcwU5D3SweYv5CX03TPRYSNcHmg2L7CEOJbNHIfQHmdygjNNaKD0ixa9oR3dkhDLgLQ1w3ZG-ESdzZC3Ki2mlFeqmI6MkWhQweJWxyWYUaSC3hYcYTPWdALYpic628qYD5lbm8qurvcZzkNvboo4sRg_CS2HkPnVva_s-9Jl69EI7iQ3g7OCraGEvJfBavhGGMrFknIIqTZDLyzw9yozYNVXoH9NDmVWHQ5f8-iBfJxSuJEl7EbGADIP3XMJ63otzf9du_usc7OyI29IeFk0AmoN3pLuRN00E9TCvEUBNxkV2oV4tVcvQDjOQ9NoYqJx7Er2BrmyNB0wqNfEw_fTKMrrtHfTjgN0DFUfDy2Gn84LTgoz7_d2yjz6P0NGZRbyFZkoi5EUQZw1pp6ZaVT_5bLSRRiXl_lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=f40KZdm4Ab5t_zLyDUMqYNMdKRq9iFRue-hkJsu5ddONOS-6u2epmU13DXPvNoAdUL52CwNMD_ZpkmYKY8bMSPGJTI-cnaYLFNNkmDaMpqgKt211P5_U4pxWWz6aFpejz29gytiIQu7O6s-R6WexDvDFRjVDc-MHpOMeCsYgRRQfj-hmNpxneGR7TxQkhnT8K38rv5GMUtgzK-qxFfqS0Nb8VQJlvAydZRIOpoJHGtLHrpz59nHg2ZnwGX9MML83Mt6t1zXqFhGWcwU5D3SweYv5CX03TPRYSNcHmg2L7CEOJbNHIfQHmdygjNNaKD0ixa9oR3dkhDLgLQ1w3ZG-ESdzZC3Ki2mlFeqmI6MkWhQweJWxyWYUaSC3hYcYTPWdALYpic628qYD5lbm8qurvcZzkNvboo4sRg_CS2HkPnVva_s-9Jl69EI7iQ3g7OCraGEvJfBavhGGMrFknIIqTZDLyzw9yozYNVXoH9NDmVWHQ5f8-iBfJxSuJEl7EbGADIP3XMJ63otzf9du_usc7OyI29IeFk0AmoN3pLuRN00E9TCvEUBNxkV2oV4tVcvQDjOQ9NoYqJx7Er2BrmyNB0wqNfEw_fTKMrrtHfTjgN0DFUfDy2Gn84LTgoz7_d2yjz6P0NGZRbyFZkoi5EUQZw1pp6ZaVT_5bLSRRiXl_lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/durdPnVviKaUU0CdLGLfsDgHrDwRHmsTFOSvd0UThuIKi_yqPLQqts_I44xuxeqsj_66UvSrSsEpK12z6XywWFaHdHgAgvbAsciEu-MErAnU_Y3p9cV41iRMKC6LziTpRqNZKmKfc0sc6qfek8hZEtTICh12-5GKDOSiaj84jf2f4ugMp0PTBnubYNQYF1qdy68hR6ecyDHQjQzKZj12PpR8AVmNxiF8mcla_z1YUO0X-89_a4s6JseCC5pjW9biYxHOL_QnO7Lw3f1mQjWMmc6BgZaG3ZPRMsR28yrJkEdazsYG74K279njmzscXh1L807M_H85V_gzq3Ie7HSjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=eNuRr7w-EKoc5hhdlsCP43Ah0vwaKJbSYoHgOMFzlFPHwECcjYXm14kuQ_dMT7Vlu27c5Rn7ptgqupol7LAE8HcXuj0tAS82YWWMLTXVoKY0yggQm6LDwzAU2Cm1FxOqg-_wy4-MTengHzhNb8n2fvzBBpBDLkVetsbv94rzbwU4wHizNPEYt-9w7CvQtQsWs7vz8WgybFoV0fRF_HUYciSnT9zfWUVM7-LatpCMMqNmnb7LczcuHDrOmlrz6PCQhoBsSKMDYBigZPdXSWKr6F4Q7c3_TQD1-DJt_dgGw18RWE9tozcB5c-o7ko2o7d4QP-paRPTF03XrtJT5Ticiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=eNuRr7w-EKoc5hhdlsCP43Ah0vwaKJbSYoHgOMFzlFPHwECcjYXm14kuQ_dMT7Vlu27c5Rn7ptgqupol7LAE8HcXuj0tAS82YWWMLTXVoKY0yggQm6LDwzAU2Cm1FxOqg-_wy4-MTengHzhNb8n2fvzBBpBDLkVetsbv94rzbwU4wHizNPEYt-9w7CvQtQsWs7vz8WgybFoV0fRF_HUYciSnT9zfWUVM7-LatpCMMqNmnb7LczcuHDrOmlrz6PCQhoBsSKMDYBigZPdXSWKr6F4Q7c3_TQD1-DJt_dgGw18RWE9tozcB5c-o7ko2o7d4QP-paRPTF03XrtJT5Ticiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TseuQK0iyCPbDdjw2XBT4_t530_wBRhkdxYX73EhNrGj1ivVwBTRCK4_n_zt5cSrw3T7ZPwr-NWtsOlMNrhrzs7oClCqRNRKuDRLxtLs0u0miZYPRoh2Tt2UecRUSuyZiRsSr-ilKqUn5JMX1qRVSamoz6QfG0Vj1gnvBXO-dVhSWO1GZSIMl5ChOf7vx1QdZqUBdR87SKCGBDLXG8ipLzOPK6RYIaj2qNmHP6qLDTkDJmZWO3HfmjoIRM7UqhDTUM4Ndv-ZskQEUxXkHgLuWNn2SJ2ZZGpQDFBbbIa2pSE3XyLNkyp-Qz2irCeI7YHR_04Kwz-tZ_Wd3gsDh6NYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH4fCfzuLFS1Dxaok1vh5ogWnRSjxamZUbuNaLdIT0bvgr9OTV6hwl8z9tJK8aPgpILePZNGbfiSE-dvMnWIIdQptnnFD40jk7NQbEpJ0Vmyn7JfZESFs8JsGhABX7IxOx3w6K7NeB9PO_mnsiCn03zwFW1YZ6O7cUV4cNf9F3c9HdWEX5HGc76MGZPU4GZaj1lIeBW0cYBcvzQgEn8gskWYkZIM3B2AftbLe1wx-mqbkU018gyB1p2L1TDjfPVHRREvp809ZrIWF4J4nxgMeRprgy2RTxiQAyIz-PpNszp2M7qQSkUJIGpx_2FeuMdeBaOlAEbZ1Wl3N7r9aQ1CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPtfnU4hXaw1rUisqzyBQGNueiQbUfDqwjY-acMryk4gvjg3xflMJtiIs8rCwy0Q5vxisBqYbZAxDH5hQFctIo9mJUnjBbqgKnBTWUQvFM-9qakIacjrGhOBUZtCcLYq9CQNiHGPU8CzHGfvs-wOMBCU73xflAemvu_yRKXeynhF8m8ml0zvAA0GdNcKMyMwkgWww3vZhq3pPVnZBoLQwbomcgf4kqQGwcyE_1VK1MUFIDE5j3Y_OeRfNJwKCYf3rJ36Yo1emkc4b81FtkWwUDPns4KC2ZyM-t4wi0nTBkpdQFT6Ydpk9R2cE1da3-d_h-3O4vEKmKmn8g8EDIOGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaEYO5YncbjYYX8HelGpJpz8ss1rXiTncED8k0PpYiRd83Q9aNZAe0ENMvyUuPwcLg0Dv5ORtAtfpVwTKgRbMCD3eQLf1iPGN9ArA6Bw_7JRhIum3ZqbsZ_xlYDu6HjEqL2zNjkoiLLM0kCwjfn3Ad9870xbiBioVFLDCjBxj_iuNsksRZB_irsXXjXdXz8c57RhfQlJS4Q3ulotJaSPVyZ5vta3FpMq9Y5YpkVy1DVohJK5Ih5skb_52-da2WRem-LZjx_3X-XRhspcqDSMFAPr1-eCFvpYpAYBDOcfjCdYDlN0JOfHgcZ1rsNt9yUbWP9QjYieblTUHzsxjzbrhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAtKHMucSMuKxgi9tRWhmeWLECDPLTVLOCMOZMxrlbyOLTr5fJNxn3Xp03AbOscjqGC0HdJnB5FLn5XWkYPJoHEFAn_KHz4i2yBzVGMnpH8SexTZxc45TidW66tO1vXuKz8-HvussZoyCbLeosgAvo6vhCa5Fb9NI5bXhLMQxK0iwuG8hkU3qeweBvy_I2ni7YGAq-cp3hVIpAFDevioS01mUxbuALVeuoBpsOwiMJIx6kSK9GV7FAtv33qnQw7zQRRd7lhxLPwEe4R29Cev6aaRF1lbIscLtjKK6qyMAhQiB3bozQC1ZlIt2hXupHEybFJNm6ZLuxz_n8E0Wgd9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi4l2Ze2bwUGKzJP_pMAMjTeVI3MtTj-C-ZxApfeo-Ls00MXDqP9mGOaDIl4WI5lxJCvYKqEfktQcHbulP7yDa8XI8ogUE3qpgSe2g-Z9M1hAPTZ4fI-aCZvnb-WcDaFPHkUCYbHxmdWeFBY64V5eajiOk_14uEOWfKzTMRe_bTIh48mXkMVMecVe2lYxGnpKP03Fcc5iKi-EjmIAOFxvGLOxcfsNn0E4ltbKVsIoKqj2p0r2QJrSGediemrDlST3lB55ngvSyXyF8JtYW9cryyPeEaN95CetU6GJBml7AlgiyAbPeeQv46ym_8ENhf5DfGWkqTsoRV_TiqvUx65yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0x810XezS1LAufNH133k35b9f0uiHSeWfijF2rScqzAJZ3TPIDYRQiC4JdSMenTaWPzv1WgJ4lZbtsj4I3aEj0opxJtQEXdFmTR-1v82FjaKV7wyGnzbtHo2SsACXXDtIy1zcSlaXYR4jhYzoYEn1sEepPEEZqhbDJG4dmYhmyDCz1cPv7YW0fsx5qVOAiOhR5Fn_CPpzRwaijfAJMG5zzQg2Y-22MYBGcUShcR-xQUhbPvSJuBVeLVw-DXsOruWfFifNwBS4nIJaUO7TloTI12y_hq4aNdu5Ol_vSIeGfDgP0O8gPy8-CnRz0sddOoj8KriRkfDMqgq7gxzUKF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi1EfyvAgJ6GfZXFv4QkgRI6MChS1zbGX6gGKW9t-BFPeY7nLJyTa60pdeIkf1dDx214K28-f3M3Mn7xdWFdSv9fy3nuKXZmau2F7pjhJZdOFLTlCXbbxS9qsob0Gxr9LfB0Uy8CDnqNTVtfeiaoDN3DANbx-ctBmr3S0isSgdTvC5TpaX1ofTA0TkP8lTLdYe7DtlS4KA-YPBPmWFrEgV3Z2gYmII_F8Et9mIoODmjpUyH_EDKjhkScPllEBmovc9nUvuYknWxek-dZD-jSOhd3VUyacyENgUYAiXRiR9aZBBQMgvytfsZmvA2FuIfCWFfhPF-fUOMHhxZwu5YCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-WHYmCA4g2c4Sdx0zoBfXLv1XRCshEuI2-_JLHcP7aC0-KJpxyiZDvaUhAH-FRWDOXodiC2a-B1SbJ-R7ThQhONHtHBaVat8NDpucSuBMYd-LkOuzI1B2vBFc9tuL1TEQ_FTsH6C4Oaihaiexx6OGC4RKW7F_ZsQij2TJw784HKdz5PtthwApqoxgDBjCN-bouyiHEQDKlcdLL_ahX3TKoFtxGnHcPhTQoKNPOj5n_kbxTKgsoYze5YTuPyc9J5cQOb1EVmRtU8N401sKv5sAGopAKFe6nk5xnN8M3-IfXXeBZk-E6AftEKxFMX3nJF5_HWIYOTjDeyXlEj8Ss8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKlbAQqSQ8uvu6gHVruY_eI-PDUw9_aKL74_-EioNakmJeWodfp1osSB07TYLaVXKmUvkzeRgQLObWAOWGFZACGO0oMlUb_D4XLuuBbVi00mh00Sni_2Aim7fc1na6MNPnGzCcqVD1XIn9H-tcsZ0k8xEcnx2imX285f6Mhq_NflJlv5NbdROeGkySW_9jlIgcTyUn-JF3w5AmLvZPLS0f5NCzvUrZw8HHLLUxZNBkRPc1_tZsLFXqzMmT8pZ94XOuItMf_BaRWprsjdpnJuhWLYcSb7KKNpYk-_YkYtJoVvsveitEOIk5tWxYn4Nsb71m4PtD2PgV3yyTEuNk-ZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEBegP2wEFqY8Uvo2mMK1kT0LFxCAb7_R4C4kJwbZsL-JrJLLBTvTF5ik8NIaH_cfggkYqM8NZ6kc7T8vL0v393_njM16pvKA8qLM0ZXIvhtKbbRZYoYGBrKbg4nNhHloj4nuW_AvCLbNG5g4ExykGUxTeRNoudontko3yQIqmqFjZhdvUCOXhkQPWAeE8cAneP61BRVLoZEDsb-3pMJzGJUgaK91ssM5GihLfnGXUByEtpXEmFNPFJ1f51yXeZqpxaSLJdcfLcm-mcxxQM_v1nbYNZ9_Fy4w1ztf2nSUkRZ9Bh5w42j6XrglQhV_7V8kzGTyglVk9pW5dOBLFWFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEXsdBxEAeqxAq80qYYKElmTjEv21zeP2IwZxN0kjDNVQCI-tIPoQP84eODDR8aJmm8MhTL7WH6gusTbitCF5uLN0DYfqdz2yr_Sink21rIark2JytXEdyTWY0APSyWBzpz4DR5O5boPXlGC3sLI9I9EYKglR4za-CRpykF7f5Botn53XBIgKC4-9zCwnm5Rdc_76aq8SkHUYjxMV3QTYMaBL6hTNrmVwNJyCiUWPKRDR2x4xRw94hZ27Mfrb2MnsF5SsJz64_H-aVAcplSrsqkxs9ymW2gOTVPEYRqpUwc4JkrNq0B1wQRBKB0ChldrMz1kOjcciF3QZ33cxgUGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXCZbLc7Ss2O_h7VaEaRWdQSmhyB_OgCQ1WzXTPwaZURcEn2Lx7rcbj1FQV5YCFMSjpfSgw6DeA15Ei0yQsicXsZHf1CGyPxaD7oLBL-phGaihkBck-2SwXDbBz3qib37qlHu0DqPH052i7L9RHbh-16r6E8_hm3-01kyhiCOGn8pdD9AiP25gdVonNK5AYQWXBtGj2lKNVjZY6szHM7fB2iwNBtWReh8xLQxwsAIgU_jWfqKR1JjpIC6fIJP9Vjuqg4HAe4uAN9KrT1l2Dw1fLUSzi1KFPH7hcpg1W1jNaG8CPJAiQfH7-TWkZkNVB2qGNnEb4WFeCOZJjSyERLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S79rdOkaVKgNZR92Y4fIUoclIwGrEm6wbxVh88jNaCjurEH0UdjFuzEvN3vMKmOuTUsP6wWu0UCfNbsB7rV-fjsT-WL-8TIe6nJAb3Q54fe-Irh70pNTpPLMFXssA7DgebWBwPxgsyKx2D32iVMZ99wJWn_SsEhSGjf5uB0eyKAKn5dszk_HxbC8jOqBDVTaX_QYPd7C90XT8YDdIV5fhZuRCWDnRwGp2GwRA9pJCHWo7HC9vh4wDzePdJglvZpQg1g4BxE7Q2okfLvoVi28tsnBhDLQ6sl9QVpN0ZYE40DoBjhBQazrMbx_CKskGk5Aefy3jZ1q7ryi7GQejLCxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyqUmBSmvVwX5sjigdv9BlUD5H7UCCCWQsu8JTvlp1gEsdkVncjQXxQ-BZODN8nA6jfoqriQVvdsga9WrX2cZYgG8DBgB6csYGMqZf6Mp9u1EqNedcFl8QMB3WEmbbDD0j_U5MpBVGr92XmQv3vpOJo_1E2L2LnjalZm92KYqzZVuT7MqUmTeWmWuc6jq4l_kGH1iSE1UoljDsjbLEAAkXCarJEULpEJuQqfC6Md_z3YljC5xEn3n3FK9NmAFEBkaJssPAucaVR-PmY2tGhsK-dLv_I_jKOPRENcHp6Nm52zZss3VkDmucpByxRHo8sNuuLvj-eqLxSdI3oHzCIuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f75pqvvZNXF0wI1XIMS7rp9xcFEEHFj2_OxQ8qzIWYthVr_o0vgNsXxZvF7FwagrBZguIzGMdPID_Wj-tcfY4aVvWVa50rRS1m_PvJ8smEa3pV2M7p2Gs8oFPTZIt9NCZGC-WXXau7k3eFnx3ajXeP8fO59qXlJUTTP8OELqYmVT8Z_-BMJ4iwjnIz1OP7DgA5bFj4hKcGxt7JJm2J5fAqUlgTv56kML-6zS1Y0UXNLn6F6OxouUrw2DBVLOpU4jw7FrVDz7jeIMsLylsew_HpKWGXoW23qcRLlIBlf7LpJxXEPOrJleHjTQ-TyVw242LhsCOvHlPU9isGGppbtqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGqFf38VhYa8aQrwFm_Iz0nzXz1JI6HcOBEHJWerzhlYBJJc9lpoydPm8jyXfHcKULTS9zuacWvbXffAXZRAtHrMGorejDtz82pBjwXuYyZ8CjiLnmfD4tTeSeaN1GaQc_jWgAKYNRPXZ-RvJmOCVl33qgHrsTc-Sq9VoF5OKxCDB0nlq4R2O1zMRU5Kpp1QQSzu5qIuffAwwzgNwbRRxU_Ik5_8SLm4cR23l9pFCuvS4St-OXd4NtuatD2JSMW6R_1tsXoXmmPg5EdcHLy3KmqoGW0n-wfFdBsJyCUF24SekLDydWadn0OzM2tnzzesfJjMRfrqGIYP0_5rRXmVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbn2MRvq5ecKusg8PCBBqwB2OCMWCYrDCyBW1N3G6REektr40_UW2VIZt1ekQWtLujUAltTSVdRhFkuYQlTVxd6Hi8DB-9o3zdObo7wn7UBQKuiT4LIU94Q5fve_dkYybq6KD1GbiGu6ipgYTHAU2TI8eJrHvyCR4phfmprCvV7ECrMpozBjjmhA-7BhAw4Zv1IKWaoURJ5LfIZOvWlOaHk8cSOAUXhcIql3fbrH91KX8ajpSmYgsUG28bcc3iVDOOwSrQIEe3nXb11QMFPGzgqfr5JhPlOb6XAwhXW1m5AbZt9XH5xMxDUBaC3rLK5vUaVIx0wSNhLbiF8zYfG3R5rcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbn2MRvq5ecKusg8PCBBqwB2OCMWCYrDCyBW1N3G6REektr40_UW2VIZt1ekQWtLujUAltTSVdRhFkuYQlTVxd6Hi8DB-9o3zdObo7wn7UBQKuiT4LIU94Q5fve_dkYybq6KD1GbiGu6ipgYTHAU2TI8eJrHvyCR4phfmprCvV7ECrMpozBjjmhA-7BhAw4Zv1IKWaoURJ5LfIZOvWlOaHk8cSOAUXhcIql3fbrH91KX8ajpSmYgsUG28bcc3iVDOOwSrQIEe3nXb11QMFPGzgqfr5JhPlOb6XAwhXW1m5AbZt9XH5xMxDUBaC3rLK5vUaVIx0wSNhLbiF8zYfG3R5rcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrclVqrCWrcBIdO41DM-xAm2T-f_G5cxUrOR0GdA68FoV2TNiFLqr4pf2feftCOuUlHy6pgPbdMX_wY_f0-lXGnz-mdf_w3ljLXHbqM4MZrHV1FsnV2fr_60whtoUOXIiiQPSGLV85IF0LFDY3SZyObjaGh1zDtVUXj-irGOQonmIaOCibWcaBGJ5MD1NGVDEXh7OqVQ74JR9L_D51Tp13uTCJmwH3eP711j0eavmwtbk56T4Msr7tZD9YnTStJwcgEcP63FV8vvS-5OcCCm_mngg7wtqPaaxO-3_ko9mQRfLLNVbEWdizWVaONsnEAogtPtGv-Ru0M37qP12Wbshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqvd-1hIdjWBMi7m8xC7MUSmmx8Had1ak__y-BdDgFV9NhWY838HdXJjWhuf-gnNjqO0UZnLUIgQOPt__Fl3EP7cLuhRpOzXpBSSwbYCllANsif0s6xlYNmQ_Ed-PsoOXol8UCvkKznH1QTzl3ooIUkJyYh1DYWmv4-7Ni9NKrt8KGr_vdKHxdm7Ah5VUrw7qHKao_zJpnc38IB-q0uXbr7BD34_tqiTTOKghCgdgyJNGE2btajkZUUWFhwGDkO78dlmznoSVEE0dhgwT8Bmdlao8wIU-xiy1Zex30K4moeznzeCiTwIOq5KlvXEScSIEB2VLl9BGtk_ZF8pzyABHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QttsORR08qRhF1ag7y3ZDj0M3Jz76tm5BF9N8hXvXX1FkcwTFwlReRuhKmLVHkFEkobRiT4-WXQnYnWPxBoHDtqTg8VLfC8yZNRufrMaGQUtGHdgwPLCzxzNkESYStHW4ZwdFMpeG7J_tSLPyHe04Fpdy2GwY2hKGjct3-EtvNbSm61JR6AHh5NWHdvwAsdevVtXt9W1pWIrtRnOjjIpwoj1CwKSyhnKxcLhvysW7oW0WM6fFIxgXVmmEE4YmpccBZwkfLm1iNejVNMZUts4mzkCOWh12EgIBs9Rsdvdwf-dTerYVZi7AmrMpDVMH6KxKpmzW7wIWG5yH7FtllPTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9pls2J2Z6ZEdImmQ4oBmmHMuTnPxqZDBjZB1xO89EwfsgP-OrFQhSj8rY3EzX4tDF6y1tHJyuFc1_gEpX12zQOc8SceaOO1z0T-RDJcxwinSLeKJTh9Byz5nHqcurpl2toHFjpJ1bi3HxBDqnVtDsyhKyeHxj312KK94dEFpKVjFWs4kQPEpxlZldNOZlu0RxqoUFmETM0fvvxBt4N8Rn2ZqIP25jG_JXBeEo3-ZP92Br46uQt6aDGk8jMxAf4OOGG8YzMMS3ZZhPM6UXuuV1AzDJt2jJeRA6amTdMts8wbLmesLXAfKDUR5Mr-IKDWiflRG-MY6ZVcjRfaE_27Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBQuL6aYy_H9KNXWQqSQnJHDBQvvRZHHlL_bCl9IqfV3r7uO0M8vrmlR6T0SW2Mc6WFl9IkwhZOTc-khfhL0KvVF-dlcVC-hPac7end2kanI2p0BlyDoIkaVc0ZXdowsiGHnTDJWNogSlyniqwZvWkOYZMIrZPJdu0tQW3UnzOCpo8iVqJdFIWvU9jBP6uft3_GRlrsXa-CZGxsqZTIVT3Ec2IQxClRI7Tb7o7fQuQsVj6kqoHM5B_l93J_wDnMvwyjwfjfMFjmHbNb1Lc6w2J5k3YjzCSILuUED9u0umCO3B009m-cA1xIMSsP6mMuu8ruO8aAzMHYaMIbYb_JGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=q-VpXpiKggRZZTu5zKq6TNokXF0QfeXLtsuSYlhUCdXUoAUaDyMz1DUocDnQH4m-n_ut0g3Gl1L4ctDRGxavHaVR5RK1m37x1mZR4kKUmCZdrOhBtHl-elXi4fA6MOfCEAQ5MS1ppvGLyP4GLLsQUbaHNAOg699ctNGWOc9fmh6Obq1j1_XuQjGsXO-_7y6L3l9flGbPb_qoXWkALXdYPV4l5-73u4tJNNl1Q6rl8UINmKYtNfTFlrCYRAzMEk4fPwlEySml0NNOZ8mhM0G6UEGE-6SdVCvcp3PN-kXXFvP3nYw8JCwt8KmbHYtOjkjf9hn-bn8_8jlopp6sRvHQ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=q-VpXpiKggRZZTu5zKq6TNokXF0QfeXLtsuSYlhUCdXUoAUaDyMz1DUocDnQH4m-n_ut0g3Gl1L4ctDRGxavHaVR5RK1m37x1mZR4kKUmCZdrOhBtHl-elXi4fA6MOfCEAQ5MS1ppvGLyP4GLLsQUbaHNAOg699ctNGWOc9fmh6Obq1j1_XuQjGsXO-_7y6L3l9flGbPb_qoXWkALXdYPV4l5-73u4tJNNl1Q6rl8UINmKYtNfTFlrCYRAzMEk4fPwlEySml0NNOZ8mhM0G6UEGE-6SdVCvcp3PN-kXXFvP3nYw8JCwt8KmbHYtOjkjf9hn-bn8_8jlopp6sRvHQ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7uKhLarvT2KBV14N6ADQ4WLr81bIdGn_LMOHG5HALmCB_C5eL-9XcDdFEiimjUo2baDM8qxwp1u5f7NxHVBWQEQPe38lNAG7A0bPcVMzKU2GsI76P6PhUkRwuoFkJKHzAtKE_d8k3IPsHtzbJR5mDvKfH_tmZfjmdYXG46bjKoGkcqo6XbEn8s-36vKmUUMbcXXqx978_BDcEtHl1S3epE_shnbdhT98LldB7Rg7MWZovPb938onFbraTkCQfH0ZIZ923SijSfS42nPwANmXRQW98iEYVTSQi38mNqVDG51n70PKfxfJltD62RRiP6_ChCvTjPbiesyE-VIFb2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E14sGUQyas46H8toaKevIMnPnG9gQ2r1nuzFkFOiJrVgKdIiG74la9EnQXi_XTBfOkRaMF1t-YH-7dTjXJu9z9JgqFwx6y-_hhrvakBfP9hCt3mfseoP61RTVxBjoVrKaccutJY96OBcUySoKh_L6-9DybhGAagAWf5Da3GD3H5oyUEIxCN1LIaU2D3piBddqdHsfLMoAIIdEBZpjQa4tBN72jwbgi0g-OPQVJkfzL1GCtjdFqQCQYBG3FhhZpZEDT0RgfpLVviqa02oFh8Ei4Me_6LEOddiR7HFHlmFg0WYLF2J_kpA4WISAbPuWWlXozfAQlWQ9m5VZJ57rTrb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjLGUwTJJnM9RBhqs6FH3PYcl3Lq2NUnc1u4BA0ofeOpv7BKYW9VYZAMyI22sDWxeQ7z70Hl5AdgsU6YNdd8n_2hdwdUHd3Z5t8aCGrtC2Z8lav9UBWRKQwZiK7mTg7coQGNwpICscn9JlBI4J0pMzNbfMaOfjhHdFq2TvG5yf7JGpP3NeGF51oQ7FQl2sycwfUWJD_vpxY9kcOS1mQc39TRQpeoIFouzolAtz6KwTKUHM3h07HLQSTt_EkjAJ8leOPuOGRYZNFzm4BTfZUJJjT5yXOESxHOAs8lNyL-kVnvS8F_dX-FBm-LHOSOzE7ViAKK1gy8G5gv0_QBJLcuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjx6RxSrlxUzJ-hLqrr6-8B-L6PhSF-9vy-yVkctm9Vbamm1G9Q36Ho839zj67ZyOOZx5fXo_41q1n3kZp55TaX5dJXk6So6BS3l1UG3a_G-YS4GMVQycbySgCRwH2ghFxOhzqcoVXne_ALlwGZzy_hWj2yKYHicctJAjex9z18hjl_MF36ixAeFzybeo9dKwn7YAlM_4c7yODlirQIgZSCC20Z40AisFQstVszyFucdis4WdGWFbPtjP3h-l3--9zNW99kyvqnUo2CpwVI9zIpeGOyr7y4A1g2bGCCPgy4vaVIW4vNBKRUaTYmkQ0CERMIh_aIDPNfn30FWjqC67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AESgujNLoVlRFMdhIqi9cVqt5P63vu8w73bn58i2Pt-8TrPALpIYCmq41gqsgogdJ064F1IVOQ7TKiqja6QzIK-Pk9wBRIJ69qptNy1VHFi2JmJKJBSkhIOq-B8gprvsiuMFkiZ80l_qoeolBCDFRxZNe9B23asx10bzXaKrG0sRjS1jU0co50LuYQVf2ABa0dHaby5QNR5-b0f1c-6f7LHMg4iTSLHW0vQ3cJ15p2QYa-BjDhAcH8H9fiMdEZ195mPalZ9FekzzB69do5vFFeov_j9dQ6ge0VOmpjAq8l1C8HbtEwJ_YxLduuCpYdmwsPs1HuTXnxrxDja6N83DIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLdBVtFEVVsuqoaUcKq_t6iBoUaIz2G1M9pzJQgmR2UyHPEa3TxmY4A_GgD9oTxdQqf6OdQ_IfIKql2niydUL0Ms3PnpQ7vRnq7ya0AnPMmMgJL23gOMm3fcwDB7fkR7Ugm9LA159oFGCHNEKHL_AhoYCOYewNo5rKfKxhdX0CENlemwdgixkIZ7lxjor7qGOggXOCHNUjodShb0xxZkXEdEkzCYmYoJxrSevJtADKfGvw_uXxKVURRqSzmbFzlG07shyxmrZLC6U-uQuSoj7PL6OpTqj1T2kaT8kTvY88MZgktY-qlnyT-n8555fqtG8L9tAegSNCUKQYv7f5iSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xv4gY7HxMeou4QmDwYIwaYY8_g6iVeyhq0ksrZ23AzH0oMp9gQZpvXk5_fg5DPAI_Bi2xWNZMIStiDfzN43jEydVbMTz6KkTMSD41HH66r7bLWn3TFfooSO7FDeXWtMRkzyNBwjat_c25usE70z_OCv2pr7O-HY8x3jZG4uWaqXu_x4ucFglFvVuSwBCy74w85vOPqOMtSmYmN8dSGAqk6J5QIxAAI8YNchl4jZM3CkUK3jO9ruXHd1ZAGR8-R56wnRA1cWVeANCODtPyXjc_Mi0rKv5jLlF2egMAjtDqNMRBTJ8BvSwfklZqUYV00OqoBx8E_deGYTli4cQRsfG7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMNmMUBfXI37qhRRtBXxNe3_0u5lk0KJOjvLJ84BxqwULgX3jYF--MuGv-LmBnCYPto1zedJV-npbAM2yxKbb-VtFhCpGU_7c6DmspQ8U66kGiftdSlILpzml-BqE3GUfS1XTpWogsPC6a8kcV8DXa2jg40Exi61REv5W3C6TlanEDy7XMGTTua4zggOZqhk3j8Dwe1GAEMMK7Z0DEwNd_V-aUhD-evUMYDvlaaL9eMQ2zWtbtSTEcByttjxC7Fk5MhmtED775VPYXyiNtRagjzKKFIBCDAOym_AXHxM4kklb2jG66mLTAlU2UixdUNUKM0XE2_saz23nmp6JPJTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKgZCLjO2qHtxO5tZNZXydB1QPKRQQeQM062RO3fSaItlnplOPYjBV3_30DXggwxltYW_djmyw77qyo2CQQEFe_jHFJJsDruHWouRAOiZvbld5KJWbB0HX5YXDZb9_NWGh4GWyHNE8nO6VodiCHpJmPJGUJQpcla2-wiB2zqStgMDjNyhXaywZUrX4rP5DNeJntZa-0QaMgENcyTgJf51uyAE7Z5IYdIrCJDE37s__MnzObUatXaAB4lzA-YikxQJlDxcIR8gs9KMADqB0m8driDhZ_sBmDCTgJ1U3pwCjMN7Caz97UgQKToHhbkz9B3kVD8jZ4L4HzfCxPH79QKgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBylAaQTdlw14CFHb-XxBlF9-U6rUQuzxB5Lks0kcnOibsjIlcL8TiBbLztWdMtmpTh1O8WAAcyTe-RjkYVOY6KpWII5yDO00EOCOontwlgT0nkOqlIj6LAgfcNEhlPtUaKvwt265am2ob7h9xRiWypIN2wy1OuKVRAjIN0_LS5MFdErelALE9LplzaD6nf2HC_4CFIt-_dj8ElLDcyguFY6n_tWRrIhbTlIQoW0Dr4JAYFIutA4SUUq2-3q8Z_yTl_G1SGCp7XMqcGtil5B1UV8P9XqJ5IMdaRJR9GzBlButIVlcegof6x2Cy27FhXpuSnm4EReKkCILRaR6TN8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRzZowdkKBn1EreMTpzXQqE30HO8l4T-9pzuvKrhLpcTmLhE5Ez-qAq_LNOXWXh71xknz74j1Z5JpOImmY-cRfWdLh2K40E7yYMXS3tzcJ-MalJii9M1Ml7cGIFc1peoyk3GdrsKTnzMfTB6FeijP6-y_BjRSaZ3QYVZWWrHEGjA9r3beZs9458puyGt0L48HB5Wy4ZB_kLvOeTEj-Z2VL1Wma9oVOE4jPT4-piHdeILGd1KtiWyQ2rN0y6_8cCmcP7utjOP04SN3Ci31aJF3a_hQlfc2_-nrsFyqchJdGdJlrIsYwSl8Ob3BBm_aH5Z865zJ59Fzcn5Lww01K_wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=lr52CELBuNYJxg8mA65oJMzE_JB-QQXeU-OyHxUZ4pUBhjtpkXyvty5y1H0vRQT14JN0AF9CWYbG-ADXW2fVbhSTJdzBq4EBzWhvNmysMP0W2xjjJD_rVUwpSFydc32rxvnWdpwXdSyEOk-nE-F8Rc7H7NnOgxwtFaGAfzthySh0yfumgMb8AqbUMh03Azuh7FA-9Y0nAR827D9wrp0RzEuibKgfg2C18h4IaF6wxHRInVwu2lL6Vag-A5-WT0TtQXo_wiSwzkoT7larUa-pwII8qtOdG3L70p38-zLAoj1fb-Lz1M3mX9aW61UGKP-R7T6BoIiKzNKN0HSCi_8feDj3puKW2k7Ijotwfy8IQKS6MrFQnKNRY6k9CT9yBewv4Cg5op84t9dYnj57RItroufA2Wx3FwIO7EsQjdrB9uIKuu3XYZWqjo_m8xVzIKuOtUlZck4DFmxM6hHHR6zg8ON96BDdeeJB-l5RNp9YdIXqeVt8FpaLpYJlrIDfiF05uyXoO4DgeX3_spF7_601LZtQpEm7baowH5ZE2yBBRmWT9XR9MH1FRmzZL3MzaYLNyXI1vjrdvdGxxrb5V4aUyPWemDtQViSrYfbhMdHygPVsMRQlwXwoFjNWEeqfWfzwL-Eqe3odT_3eT-3r3-zm8t-rSOwC3HPdmVgHutb5rdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=lr52CELBuNYJxg8mA65oJMzE_JB-QQXeU-OyHxUZ4pUBhjtpkXyvty5y1H0vRQT14JN0AF9CWYbG-ADXW2fVbhSTJdzBq4EBzWhvNmysMP0W2xjjJD_rVUwpSFydc32rxvnWdpwXdSyEOk-nE-F8Rc7H7NnOgxwtFaGAfzthySh0yfumgMb8AqbUMh03Azuh7FA-9Y0nAR827D9wrp0RzEuibKgfg2C18h4IaF6wxHRInVwu2lL6Vag-A5-WT0TtQXo_wiSwzkoT7larUa-pwII8qtOdG3L70p38-zLAoj1fb-Lz1M3mX9aW61UGKP-R7T6BoIiKzNKN0HSCi_8feDj3puKW2k7Ijotwfy8IQKS6MrFQnKNRY6k9CT9yBewv4Cg5op84t9dYnj57RItroufA2Wx3FwIO7EsQjdrB9uIKuu3XYZWqjo_m8xVzIKuOtUlZck4DFmxM6hHHR6zg8ON96BDdeeJB-l5RNp9YdIXqeVt8FpaLpYJlrIDfiF05uyXoO4DgeX3_spF7_601LZtQpEm7baowH5ZE2yBBRmWT9XR9MH1FRmzZL3MzaYLNyXI1vjrdvdGxxrb5V4aUyPWemDtQViSrYfbhMdHygPVsMRQlwXwoFjNWEeqfWfzwL-Eqe3odT_3eT-3r3-zm8t-rSOwC3HPdmVgHutb5rdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=ADIxXGRExW0VZ9sw6pqTMaW_KdfUvKglBjdOzh6DfyY4rG8SVh50yim5VqhzVlN5Hjkn6lj9dPeqoGMvBXpTcWa8MLIwOYAHUZPqBVVGzcwqufphzeCcn-DUOyt1yKsSyNRp8J5OIlG4JblcKTEi7_FNCirPgB0l_KJfAJkOnm9H6Cy8yBHibVqRJVy3PyuFVfwszZNO--ylBhdtQoucJvioOo6JPoHnfDCZ3GTub08bFoGr9qPt4bu0BwuCB1ejH8BlQjt-aSyxGN3ZQUi8B0hiii_968FTUXIarjAfygU-UD-D0HwlQ-FfGJZKWBQErDpt4Ac42zo2_M-D_DAu0VoMeL26kp6izzD7byYwDV4iuZEMd3O4VgK-Vs5GyBBGBoO4KQHi0ZdV7n7Tbq4bKhniw9TlTMtV-13gptDH09vrs0P7_CedRRPSTMXaea283v_ES5C1Ci1YEGZ_ggTtDYg3xCf-PTZ69TUDzLNrLp9HxLVhXOipmf8-bggOZWAWCxoJ5u8Kt3b9XfcbUlyBR0oqxRSIE8QmH1SM_BxTK8Xmm6m6qaSDpndtRyDn6lt9tWb6TLWUM3uw3Vg6WKqDuCf9FTwc4Hjx7N0ahPCvcKmoWRbLiS5O-FI17ISgLbwKndFkXq735kf1d1yskUUaghePQoFiKYxG9YaZpQS0xgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=ADIxXGRExW0VZ9sw6pqTMaW_KdfUvKglBjdOzh6DfyY4rG8SVh50yim5VqhzVlN5Hjkn6lj9dPeqoGMvBXpTcWa8MLIwOYAHUZPqBVVGzcwqufphzeCcn-DUOyt1yKsSyNRp8J5OIlG4JblcKTEi7_FNCirPgB0l_KJfAJkOnm9H6Cy8yBHibVqRJVy3PyuFVfwszZNO--ylBhdtQoucJvioOo6JPoHnfDCZ3GTub08bFoGr9qPt4bu0BwuCB1ejH8BlQjt-aSyxGN3ZQUi8B0hiii_968FTUXIarjAfygU-UD-D0HwlQ-FfGJZKWBQErDpt4Ac42zo2_M-D_DAu0VoMeL26kp6izzD7byYwDV4iuZEMd3O4VgK-Vs5GyBBGBoO4KQHi0ZdV7n7Tbq4bKhniw9TlTMtV-13gptDH09vrs0P7_CedRRPSTMXaea283v_ES5C1Ci1YEGZ_ggTtDYg3xCf-PTZ69TUDzLNrLp9HxLVhXOipmf8-bggOZWAWCxoJ5u8Kt3b9XfcbUlyBR0oqxRSIE8QmH1SM_BxTK8Xmm6m6qaSDpndtRyDn6lt9tWb6TLWUM3uw3Vg6WKqDuCf9FTwc4Hjx7N0ahPCvcKmoWRbLiS5O-FI17ISgLbwKndFkXq735kf1d1yskUUaghePQoFiKYxG9YaZpQS0xgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKqLfuWj_4GQLuHLy9CFxEXhn7_1B25zWy2NN_s5qLRUkBQslwn8SkjdFvaOSLnjq9mPLNgoNKe_jVu2G8ZP0SX3h--ek0ffhq1pB9cYgdV5tRlrMKrucUhktxMOX8X3XOl8osIKGSyIOyOHrGyOQRtr10AYiN7jHp0GvuoNC8twj3ZWvATxCVQ9Pqr6a1KlM_G9TEhjpSaV8khSigXCk7wxp6wxP7PDtQXSevh3QnRfLNHSQ33vSBXu-PxudV51uZlBttAJwnx4BC8jZKUm9McDgGNvE63KMMCFvrJ_IDOKfd3JP-qhaMJnASnGGFfiVohhkpey1fXEvg0-Mv-Eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=G4kHt4p8huJ2f0JiB-CDCD5JH2mm7wgFP1CXEcUJRRDhxyrcmZYL1utV2iCLZW68b68ImzIA4zSdyjP_v9_tIgJmrvBdj3nNlwl_L3pmCWKIQmjZ7Ngg-l5hwKoSqag-aWCdlqx-N_Tx3Mt7pgmNdnpkQhbaYHK0cxAHHopGi3MAiFqlWIHj-sMdXg4GjbgSa_DXRk7H6kDnrHjxwsNAt3hhsiTTn9755x44VVm-WC6OtzDrzOjCEYu81kST_FkY2-JAP06XZ-KMaUSh99opZgnB-N0ASPzzH-PAfkkURT0P1JvgcMvTZcOrvnKxUmsMDNY-5bcf8X-HH1WNArvtyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=G4kHt4p8huJ2f0JiB-CDCD5JH2mm7wgFP1CXEcUJRRDhxyrcmZYL1utV2iCLZW68b68ImzIA4zSdyjP_v9_tIgJmrvBdj3nNlwl_L3pmCWKIQmjZ7Ngg-l5hwKoSqag-aWCdlqx-N_Tx3Mt7pgmNdnpkQhbaYHK0cxAHHopGi3MAiFqlWIHj-sMdXg4GjbgSa_DXRk7H6kDnrHjxwsNAt3hhsiTTn9755x44VVm-WC6OtzDrzOjCEYu81kST_FkY2-JAP06XZ-KMaUSh99opZgnB-N0ASPzzH-PAfkkURT0P1JvgcMvTZcOrvnKxUmsMDNY-5bcf8X-HH1WNArvtyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8SPZsRHRXJHK_lcOiUHafbWCRTU1dxtwyXFUOxHx_Ui-dNWcBpwZPuA5jTmdcfSuB1t5VJKN3atg-culcmsRs6CnlONrRpycCD9qrHDW2wy4yVwTIRTGTEFnzAMCecDXPYz_9NvJNTxnZMOnw880IN_eq6J7ob2vypikXp9FacwGb4agez9bj4jQ_LAx-DOj9Z6ujhMIJSXb7NQCvviJWoH9UPhIynUjLezqw-eaCTF5DWIqd3_sSQPanTfofqAvhbB2YpPl4ZCEjcnc9tDX8FIC0sxHyuBSCbOzFwCjlw4cEoJwIW5Qne9Bv8DOPGwo7lCFqaJt7KWYl-9boGs0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4GrqDx529r2Ct-w5NGjpl6KaEo44jyDKgkLPLeNYM9IYtOUba-hVCEcTTCV7jdxMZ5dxHhFg-uzWZFd4RqZ5RCYlidXIIMkthp2FwP4xPBvkNGwwun4EBwyBHKxNpzgLNdXhzYAS5PnNSXIL6rdNNCQuQzIiit3XkheNWLAl-tZiOmBBsGRcI57Q7fZy7IOz5oEmS-QPjc2jcOdbN0zd6yQ3jqHeHQ5MIHphkpVwoTJ9XdUTcauLv0xtpEZSbMVsYBnF-CyGNawxdr2fYVR53mzuZj7T3KhxcCTl2-18ER45tP4gSiuZs7Lz0JlB_kjxAqhaUW_gej4RCOSdFepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQHz9yAVB_VFb6Arb35xmUSnNfq0vOruG8jFLnrTXBxIFtw0yegaWqdaNdg09rkQkqq5J7y5etTIwXJvvkRAeNAQB9wvnLVDnmw8KxSlhzdWSJ4CCKaPH-6SfU7htfVtjFgXYDXyeue7U9ZTbX_KOrO_XFx1GJnMM-ThJSixfg322Q3kWB_cRm_XPTTuR5psvT7CrXmXsElcl2WPq9-S-gB_fwamHDfLfqIZXJ4c-kHxvYYC4FEBTzRCvQ4C96HIbdDsRKURAFAn0q212Iewu9qTvzKmUuZY2iBzJVni94HErq_vNRUfFqe-ZgYkQzwih7Gq9NrogkMJFeDGZpc7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnaZecuy1ETUkbZqPKy_3eJqeZzlrhOnox0D2cSz1AmHCZOf156F2lyi3fD63E1gHVZGwlEr9XXUTQCBxlx_a5UNr-XxEhNNovxRTBUzwVj2Ey6R5NihTQbj2fiQsrtUk1Mo4hgrrPO7BxTCcIGvIqc98Vz-jCbTh-IS0FloEA2o-QDBsnzmr7dJTHbdLpw6Z5DOpVZqczyUhRj0BWW1iwO27bK_c2Zpx1cmv9OE9N3keSkIesbPFVeuBcruZsLnIDMahDm6-SnkdOujyLxxKTm7Ryj5XLuJ1dHG5lmeNPjNRtKKIoKcG3wxRCYQ_ChT74A4tkBR7eLNBZfxXtlJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3OSkCfk2t2h9NBtjmwjCYM_YUE1KEdH2WX3GB5E0PMbpkJjPDY_ntHsPTdBCbL0kondH1gKVZkeYQBc8pkC_A5wPsCKhjrlkDngDdA7jHo0KhKadfSWzpremONv7IcJ8d7Nf4I5dR91NxLZb-wl1ndFcQlLK58pG3AnyrO65R3Ki7a1yWcmqtpQi-kL0vyYngJgB1dXWlO6IKeg-a5z8QEA6eROBBXBPGQrwlezd8NceBQPTlxLxZUTNGfAHr182LrVZyZhTur9s59Y3vb-RqAr8-Dp5x_ozxCG1NQ8boWDBbtZmETh-JyyZLQ1P0CFENZE4LlreiJkLfRLuAiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJLZiX8KxUpLcNdY_Xk7B4oSI_9EKq9Fm5XfBdhmu1kBhAv6K8AjjjfTuvW1QyCxVrtVCh2sL4Xxw5ya1xAw4Er4xRSGUsuQv8hFlsJqTNrf0_rqoPajhOe0IItWdqYo4194nd4diZYu9a-V13sznmBsrSCLuEwrAmXUZbUagCzLuNBhHx3AgV3Nr4848Q0JTW3FnfAWZtCMVW7YsVBPHDZFNpwQtpHNRRn_B-RJ_yzf1Bscj7lUfS1ClciVxXbPQIUHq6XADS9tar5DeKH7LubteK1IGWqEh-tfI06B1xGcVKquHU_LTCavoAUMUvKsvCvGmb0RuDJNN6U4TbFkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYzvJ0OKpcE3j-JKoW9GGMqxLRvwnLjHjW3G-C_qjMdUcd5jBbi1yu29tevpX0rWmtyAtcXeuIx5gjT3ZJ4GNHM2npmQlmtAh1fjNjYMt3AGcaNRLSn5lCi8xR65qdz6bowZJ5oOoEHjm1yuEPNNRYjkrEs4fvM_jB4VNUWilRn3zMTMeT1jDp9AdiMKfuNW51oZQux3NUIPPQI9Sf6QFwVbDtBkPFkjqRFFxUVG7-KdGxwJilGATHaGwwnFcwKkT8q5jKOB7SeyiTIsayaysLBjSfplM0uCgPwzrt0-eBFQOu4CKJIWu-JM0N3eu9H9J_59rbSixuPM0fCGK_0tiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu68Tkqjg3olTlfBxVEi6VpbkNKhiz6vpVU7KvVPrbOIfysuY_uewMJ2q4q_NZoUMuNe3dfRAioq3tLvdKpvUbt70PE39s_To4dZbAegNgTB4GeR6jz-e_4Vla5bTZjqTMk3eGdWKJVvwb85xqGBQjCEx0Sk0bmtGNkNkogedFggASLAVh9rmwRkqwAYZjBLBRvEvdM2vacTD8mnz1FO5DmA2avhxmRhVurJB5_a0eCWAZ-UtJMMNxh7Ayvf_Ce7vAh480_vYL1amf8JZNxGC7h1z8q7LthS6-YpWQdcOZUFPJGcMoEomeJe7NGjGYI3_Tncg52Gd9i8UluXnJIAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTSwdRqMsr2QPb5OoRnGUNXSUt7DURvEmXvSI8w3G9nKTuROJxutWU6p-AfynukSEx-W55M0AzNJ3r9NNeSGc3Myeg665qguZM_GlBcs-lFvUpB8Ysjh6ILQl_NZ_1-sG9Z2ocbl3_8kkWeCP6rzpQ-XuZOai9Ito1yXL6cFT77HkO3mtjipLvXPAcx07AvkCpQTr-GOmT3SWnAb0bJ-8zLIAkflh9QEBxn_0TiqxNBAeW_ZvtmRhdfaqIX6jO0DvQrC7O-ika3s5UReaGnFsYyBJpJgaBE9hW9kY_BrTXJOjdS2MIR1oVRYhqDOSioFoYo15n5fsGD3Cq5Qo7kX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8TMavtTqMT3BKpeuBwVifLpvU1FOm-KEu8N-kUmZeBeCCjlvpAMXqHs7fpJ86DAFq9kE8V-B_E-uH4DopySlgNaRVyEp3BTUxcmKba2k0aGeHEQw3yIqjemaM5c2qz77dq1XQzG65VORnJsqoqjGilbaXvSqe8hAWq4myCD64dyZPePsefeEeMZjH_uTAFdlb72CuwGhCLhb2J8tMuCrXMMIRXnB3SYhMnel3GwPZN8rpgnPLjLE3pB08cPXDnCQJ4jtDG7NSthdW0skOOAyJRd_5ZtWXKN5y1AZhJTqyzqN_7E7BK8Zu3bH_t8zw5oOsoFTCH7aYPSIgzkfey7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwVgD2twD52PVUeUP0CigpwwE4O_scoKdTFYgJ3Q4GNsVUh_xAC514dmoM4R3sbl44C-SlO3Z0y8R4Tjsmt7LqWDE4TsK4csFoq1P076saQF6Z0_hiGZ0NyGrk4pHGS3DtIkjWEdQ-rf-5gVA7hcd_W0I-KeNEYGB9uUsGeQlpokirgDl0hEJmR4iKJ25zydMtHhP35lWpuHABlvHBGUeFpf3Tnyr1CXeEJmqEdmnRQaOEtP7cTkjpbzuEHlqB5WP24C-bZ6zRQxHgBm0scXt7qm5gy-GiASH3ajdKqw4sLn8uZ9OvUNcPLarBjP6FVWKWl6LVtGZjjwVCsV0SUqpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5HtRmyxUnTC3Pb42LSF799X3qjl603eulpFXBPp1TFBNK2WuTcz1TjLKv_IgZZwhYW7vtEmcmgE_xs63tfQ4QvOK2swy3GaQwSaO01K8HHNcBJSilZZ_rRfErwqpRwraAHdlBlkAq5E4XZ_YGj8AFJL1-ik6mdAyoGsG8W6Bp7sI-9eg2d7kMeFFLLQvguwBiHaeIc5aFk-CYvifaCihFOKivjpsnEe5thLeq7tEgQMijKUiVZspmPBSK45Ha1uU6DaRquuWhvUX6fY-p2rYLR537W2HaWuGKSoSNtRYkwNNf8fUjOLuPK8DA857gJWbkiKZpxuGvkiOYRQxwX_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=AWy4LdguvRs7uwwcADylAG3WQNwJ_7F7bqWzJrOhXvGJW_B2LiE8SteDObgH7uX_YJiXJV7dhyJ-8s9MT4OO3rTVGmnUuMnx123ES9blQ8sYFdKsgxu6sRqe5he9LsJrxTCS9VjDJQNwePd5gicbtkX3FHOOovOVKFuqHmBbOvFulm1LkUqEcq-UuoWVTwVUw_uJDTsCV7b1Zda7rmtlAyH9_rmC_EzCQ8pADGScf54xGG48jt5gDEfT9DdVtM17_vHDZ5ExR2r9Hm22lMdAj4Cp4cC36bxCO8JP-zvcmKdX960iHiI_egQvkpyPIOszm0AJmegBNE6y4nFwQpO19g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=AWy4LdguvRs7uwwcADylAG3WQNwJ_7F7bqWzJrOhXvGJW_B2LiE8SteDObgH7uX_YJiXJV7dhyJ-8s9MT4OO3rTVGmnUuMnx123ES9blQ8sYFdKsgxu6sRqe5he9LsJrxTCS9VjDJQNwePd5gicbtkX3FHOOovOVKFuqHmBbOvFulm1LkUqEcq-UuoWVTwVUw_uJDTsCV7b1Zda7rmtlAyH9_rmC_EzCQ8pADGScf54xGG48jt5gDEfT9DdVtM17_vHDZ5ExR2r9Hm22lMdAj4Cp4cC36bxCO8JP-zvcmKdX960iHiI_egQvkpyPIOszm0AJmegBNE6y4nFwQpO19g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMejGISI8jCF7yxWFALUp-Wgr0u_OZ6PkY3DCToMn8b3zmgqegcIb0zpAWs-2oLjFfOEkPjvbdX7KxrlvEO8AgtbhujLZq1wO9vapMMXZ28V92oUYRmHQHbZ87W1jKVQHP4z8UCEpsryU3JSq6GCRGD73Zs2t8mv_SFDJEdY0BYAHhafHGm9AtSUh8C2ysu75rnLj14-EwG_sPpJDBnO6H405eYGnU54_4InQijHpTPMwrErtPh1g0YWqVreKfzYn3FznBX5M98QVMRVQELsmeFnFps2pzpEeshgTGFw-7xfhRkoDIcwYymbiGT--EgPpDHq6f9oQo45lNW6Pzckig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbakFsA7BenSwBEkRPnkrQ0it5sas8hDqyryj7ZbJgU9NBdPPrxF8EOp4jsn0eHLsNExfpnHcHSSQl7FDrytcrK1os64bB6Dkb9EpMcVx4clUKsUjgYzIyiXkB3_wuVbJq-xevXDCG3M60eFOQ5AO3DKTpG1sgh32A83ktFba6yUF_xwe6dkDiZQQ0dxqwfyLZ409m2KKP798nxa7IIenVxopO5awL18AKZss5Q14S0k6trADUXWKzljyUr8Bha62R1lptQOCahRrke4sNKMIyC2Fdix_XG9EPmgkThxoCAnQgoYScjEaF7KV3n09pdkLNU1vot5I5E-l_Id_JQZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCZMjRConR-zLdG776cErCtQ8SBiEjMCyHzNpI4xIKErM9mYTeqFolmA9Z2M4P16IgAcwasnMfvhgm-06qxwY3dmJqv_yb2QamVr0hg-O1n1MdsnjxAfYCMZ0oiD7mRvxaYmu-F70UzYHCBscLws8b-YKG5UjZGLryjSmjUXu0gUSgAJwHLMRC5Ora3CRi2k9-7KHFle9VfQ6usph9-dcZ34jd1UTS2tjW6egxhzxDROqNYR86VMEr79gVELHRwx2w3jHPm6IjmY3tEqHzs7tdxm82YFmi0gBAzVJ7T8Sg2KNO5Qp2HUkGjA9bfilL0aYSaog7-fQRUVlMOqmWd7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMc7i6CcefyueuyV93kLX8PWxaZNFgdImB3fPbA9V0187uKG77PZAN8Rj_g4W1I5o5abdPMLx0etwQQnWonTpt5cYooXrVTUh7Q5BHiQFU8fEh1uRvVXvbG8EgT2zGHoQOe3-GIWx5PTYGhwS1mTWudZyW_Jp6QNL_gCmvv1FQaSVh1vzxE-gINNqQ3srMNRiOLudPRcyo3GKKhcRBMuS4jYVAbZMBaflaXhn8cwbeNkZpRpY_6Ab1bhvY4WL9kDa462ZrAD4O5tFZ3jk13wMXVIaktJIGFD_5QDQ5p9OJSDrvdyvU3VFaIVJTz8XQG7C7rKluzuS_L0SlaVM5gerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=hTkVO3o9OjlxYPDLFAPkz7o8lB8ejbusjzvBXZnTuWxiMYp1FIU6VYXQ_F6GA7ya91Wej1WjMWqMtkT3dwHAMSY-MLT4Qe4_82Dflo1E6Bka2BonsxZvthQasIsZflDvBOZ25Iv4KTHHfgPdEay2HMlrlyhUPRAKwREaSSyM1L7AFmOVhH-E7SNSYb0Vq9G9m3u96Wh74qRvmsc8C2WTsvKfGg7f7EcinZeM3q1CGn-G_-1U40AQZIoYz_KXHK_GFS4OYziEyVwJ-YJ_kN5HzDtVbbeUsMkyhyKeJEZN5KsLYYYDZ_1LrLSmVnecGAYL3_5W-LP3ahnvSH0he_0dDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=hTkVO3o9OjlxYPDLFAPkz7o8lB8ejbusjzvBXZnTuWxiMYp1FIU6VYXQ_F6GA7ya91Wej1WjMWqMtkT3dwHAMSY-MLT4Qe4_82Dflo1E6Bka2BonsxZvthQasIsZflDvBOZ25Iv4KTHHfgPdEay2HMlrlyhUPRAKwREaSSyM1L7AFmOVhH-E7SNSYb0Vq9G9m3u96Wh74qRvmsc8C2WTsvKfGg7f7EcinZeM3q1CGn-G_-1U40AQZIoYz_KXHK_GFS4OYziEyVwJ-YJ_kN5HzDtVbbeUsMkyhyKeJEZN5KsLYYYDZ_1LrLSmVnecGAYL3_5W-LP3ahnvSH0he_0dDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foh_MUltJe9GaIPu5UwDb0TGSVHnQ-NKHbyDxQ3kPFqBr7j9vVzty-jPiABhuB_6f9kvQlJmXz76OQgsFiQGHVoNzrExKsE4B2vJwUECHHGa27YdJw9mO37V2B9wqWNES13B2gl5fEoPmrYc74wWZZmA7DlTO2pygRlP4ddhwXSBpeZzNY_00husOzJhjKty6LesWV6_QM4S1S_F6erKrYkFRYy19jcNdbZBJxXStYfn_Y2Srj77VOgYWH5La_6O9SHvfvzc_sSOivMDGexaNV0AR3mOSCe6aoET2quG2ANldon36hDaix9bIejxQphw9Gmg8ylnA6dBfAUPF0sRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=BBD-EOqiUp_sHaIJmOz8U72WJQ8bagYs2cN9l_dYMzznVxThblVG0MmFTrsJmZ9Ao44zwZ9uVEPcmiVpiGwKHYXsrD0RWuGM7k94bdkFWg240Ws9urTFpjWWLhDFlt1Hf4cmRTlTqWopMAOpncQ9wAwxu4WzakZkbLBdqZYQUb3V_MlGwyV1QgIfNMg1hrGmn58j7DuE9J9DRsW0f7_nIpud6IPbuBvKKK_Txwr21UgguDijje9__t2JXiQml0Yj4-Fe0CA3Od6m_l9UoVAd8PICG7sI_8htPfo5av9JvGrHkWo5HRRaZPwrhVDFJTCOl72FLsAQYGTO38YAlt1pGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=BBD-EOqiUp_sHaIJmOz8U72WJQ8bagYs2cN9l_dYMzznVxThblVG0MmFTrsJmZ9Ao44zwZ9uVEPcmiVpiGwKHYXsrD0RWuGM7k94bdkFWg240Ws9urTFpjWWLhDFlt1Hf4cmRTlTqWopMAOpncQ9wAwxu4WzakZkbLBdqZYQUb3V_MlGwyV1QgIfNMg1hrGmn58j7DuE9J9DRsW0f7_nIpud6IPbuBvKKK_Txwr21UgguDijje9__t2JXiQml0Yj4-Fe0CA3Od6m_l9UoVAd8PICG7sI_8htPfo5av9JvGrHkWo5HRRaZPwrhVDFJTCOl72FLsAQYGTO38YAlt1pGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
