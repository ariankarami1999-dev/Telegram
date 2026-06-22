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
<img src="https://cdn4.telesco.pe/file/jThnqugnP8x18RGiS_zkUPZ-CIXnZyJ5E0U1Ttm48i-IQSMFu9UTNoprDPgFhFvFrJW2CuEQiun-GUIwGaGS38Bzi0MsWxFX8kPjukh8hYGWYkndBBDj261BmquOY7_OIpigXFxCDbMw1YbNlu-fGZN_yoy3Mf0zWgx-09ZTkKmRmhXVOeNPJ-CePag0DP-GSmC7E1PG5ifMJeQIbIpESvkN8wO7kS97XQ_tLiYewIJlRI6I06LbAfUendvENfNZDtpVHhnpHlW8L3m9o8mVjCX2rO8I8pCeKnn6rS8BFOu3lZaQz1AgDscaBFr1vNWncuXjpEhrbRv9H_HqGBbANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 168K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رفیقم زنگ زده میگه ضریب عراق جلو فرانسه خوبه ها
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/funhiphop/78480" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=nEsQopdD_-BiPXv2lFP75yrbQ2MjKNvSILW9Jf0gc2WevRmYtBj_cuF3rVR60TgFOxOi85urkV5gZhobG9ZK0Ka-m5MSDvr9_g1QHB7jYtHjK6HjlW3c8ruf4jznK6mGw9NDW06OLE_dvm_fhR8In5PhEBtLY7wYRaiY82T6pBxap1iwZN80OkUlPv7qN69v1QwQ7DNRqtb4380hKTL0z5_CQ9tAX5Ry_mMAFIcO0mRTpwUg16Sj_SVSvXL0jVAUXz-ueNDWVtYDPhbLiueFmbOYdh_73LTnEhCV0tv9gCfc9ss9UXP9jSCXFO9Io9uWlZ9PVyeUvB2oqVfmsuUnFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=nEsQopdD_-BiPXv2lFP75yrbQ2MjKNvSILW9Jf0gc2WevRmYtBj_cuF3rVR60TgFOxOi85urkV5gZhobG9ZK0Ka-m5MSDvr9_g1QHB7jYtHjK6HjlW3c8ruf4jznK6mGw9NDW06OLE_dvm_fhR8In5PhEBtLY7wYRaiY82T6pBxap1iwZN80OkUlPv7qN69v1QwQ7DNRqtb4380hKTL0z5_CQ9tAX5Ry_mMAFIcO0mRTpwUg16Sj_SVSvXL0jVAUXz-ueNDWVtYDPhbLiueFmbOYdh_73LTnEhCV0tv9gCfc9ss9UXP9jSCXFO9Io9uWlZ9PVyeUvB2oqVfmsuUnFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/funhiphop/78479" target="_blank">📅 16:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">برنامه ابوطالب فقط اون تیکه هاییش که اینستا میزارن جالبه، بقیشو ندیدید هم ندیدید</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/78478" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کورتوا حسین کنعانی رو فالو کرده، احتمالا بمب 150 میلیون تومنی پرز کنعانی باشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/78477" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پشه مادرجنده مگه قرار نبود فقط شبا نیش بزنی</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/funhiphop/78476" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK0er49TfgniShfO86WidDhXtpMB9-odAet3SiYmRbdKD_c-9LJ1yD1Cq7Tk6pbcXEazsBp6i7ig3aEFc3l1qO66hTkHgmExSvtpoDFvZSF_SqLtxXrExGKEx-dt78sT7ER0Soi1tscPOi9F-4JlPgSbmvNfUN3SzjwhAzvpDjYgqnmhpl13lfwTJrsaBl1bboJelByjzGfJEWS7vQX4XviMuWa7YrLdn8Mdsjb47ONclCbIKbCi9Ml-TS4yAIc1akO2BroAvBervCH6NQgslsPTIpmQxTLFIn3fI7wyv-wVnl7Gt6J9CYGbgTl4PglYEXcbguk13tfuEND-WRxMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا اینطوری قانع نشده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/funhiphop/78475" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تو جام‌جهانی فقط در صورتی که دستشونو بگیرن تو دهنشون فحش بدن اخراج میشن؟ یعنی حالت عادی بگن کص ننت هیچی نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/78474" target="_blank">📅 14:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbA8OLBdJJM99oOQfThirSjZvkLuD8ghg1M9DmifsphLUqBENNhE4kIAkcpfiJGlyQsiRZiN8AOL7Ia8LyhBk4QPxo_LVSCPdrSRw4X3z3vOawoLK9hvyp-wd8-FaT54hHVVnm71oZxebRdSQMB_GrcSUw9Zpd3gWOGstfyC3GMnJD25NN9D3Sr80GMjo3FZ_sw_aQmwuVs0tfHjNtqBb4FrzrCkTNJ53038k9untSZWVkWq26dzo1mf-kKM0oKnUuSx_pt2F-fMzPbBzuF-VNDqp5FhRb00Ce-ggduQePxxbInEbzh9Pi2aqpPUKnqagDlj6TcwbyHqFCVabdqwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش کبیر از اون دنیا هم رفت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/78473" target="_blank">📅 13:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">با توجه به اتفاقات اخیر بنظرتون بهترین آرتیست نسل چهار کیه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/78472" target="_blank">📅 13:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کیرم بعد ی دوری بسیار طولانی استعفا داد و برگشت پیش خودم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78471" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78469" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78468" target="_blank">📅 12:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beOjx1XmQja9l42geto3xDpVWSSCfo8tae_HUMKMczINm9iYqX7zUNAcBmxGSSZo39VeOdCrAg4zVYDs9JW5zol47FborYzonswNfPOEQlMkKTm15gSz9qcBrMu4wDvsDJHUZLZkS66_c4-vju25gXeMPagXMUsNOvonji5DF_IcXUuPikZwog2RYlp1O3hrh1LhYjaz3bt1JDl9_w01uhdV8xTUz0CpZOfPTF5ySb0eNwdhwuii9OQwWIgPpgd_KLCD4iSrU6QGNYaZ8BTO3AyX8inq76FRRrJC0hMAswTJtcr15fUGQM43fxVp21bwFLaKMLnl6EZf2sDhggK1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر هم بازی خودش رو برد و جدول گروه این شکلی شد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78467" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Km-LuV2bVQUPNFrz7NPdSzJURjq6ushFtNVqMRR6fVMwLqrVsGPY7uTEGVH22xvKGdpOuaSTNh_Wgxc6EKosA2n_1zWSPqW_6P94-qXKEA8qitjrWoqXiUE7YTCPQDYzoemBO1DLGKvyQ1xisDnI89IMNqpPVx0D5GCUgStcUmKSVlnzW7tuKP5_SaVbMgQQkvY_SBNmjGJRGkMJpogy9tNfql9zqijymfytXQN8T3NUdPeI8o1tLtKqsxcRuclsVyPpvzX5XomIea8PHmFyaS72jOG3fwTM2jTbThKBWTTh603-NIKLvONZZ9RFZbsc9Ni38NrL0qB0d6i_qvhCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان این چیه کیرم تو دهنت
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/78466" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/78465" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7YaqWfwuvL36PxbTkx67hLYqnDKWpaEnEiEYsw73j7UJai2b0brQRsxbcpr318W70ZBj99CGVOyNHB8YdB1kSqr7CQmnRBhRzOlACzIv5kIUXeli9BDDtS4vkacQbmPH3-ir1fNFcGLaHcVJJE-bsmx9TFKTVxAJ8nTLE5wJvXJVNO8t2kmPi_DsHf5CILigyrOxrPuUj7LPAB9m5hJtQhZ6KpvOyTeK41s8vS7dc2U61HUVulSZCN5HIrWwMRA8LdhPPMuR4HyFyatHpII_NQLORIiBGE2yPoJBMzzKKkjMQSccJr-nbtQX5cHfPJRu2qbbmUH9jshjJCr2qyxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
R1
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/78464" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRkgguYyHKxqRCaL8oOQX0efYCpM9MY8wYijKmuP7ZBeeSltflUPGgq3QkEJt-i3eWdQ--fkdhshrs6DI5bAIdLXp-Cs2jiyGb5tm1YfK1rO8q6fEyEJEQ_nDSwLVhBSU_nd98KcX2RzAyr2aIt2Yj2ExWOXmhOBV6Lk57NtJvFkHPqr6Mhi2mNEQFCxtDu_1a9spvGFD3URoOfj8yhil5TNny6csFuP7EkyQnn0HqD7uHf8huQ9pIu2aBihex67R4j7z18NWPJ5wnl9owHCWQ10bGs46U6LiRK_bgoAqeiWXRsXTB7sYr8kKkJv9dxq12MzZWcGsEMFbzQzHCuAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78463" target="_blank">📅 10:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVFxS9Xoi6z9hFlOFLrn14Wb4R07IMMLx9r3tJqwRK4ixMP4Ri6IPMGf_Xb2INIscNhifM4x2WHXmDDydI0Zkq8uRpU5BgxAttdtwl3ysx7gQ2cSczacicrdMBx5r6STjyWYDRQhQHs5XgOS_NXp6nLJLxKEllrPwfLkcaCBJlFI5Uu2d02GMd6eBO7RVciL8E1-IZhFarCMh6GJyBL2JzSOaPKoghR3eVaM5ci10SqlWQ_VorQfmMTYX6VBCMhDsslIkKQGgzpKTLVzclJW-yXGbQfOiPf-ZcLeWYv52evXOyon6CmwoiNTVoS8fdmKO8VrOWMskppTZCZhYn4XTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رائفی پور آمریکایی ها ام استادیوم بوده مثل اینکه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78462" target="_blank">📅 03:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از وقتی یادم میاد موسلرا فوق العاده گلر کسشریه
چطوری نزدیک ۲ دهه گلر فیکس اروگوئه بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78459" target="_blank">📅 03:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هم اکنون ریزش شدید فالوور های گلر کیپ ورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78458" target="_blank">📅 02:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پس فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78457" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKJ3hUuyQiqLbGvrykJawl9lOS0b7MGIV-L0oh1Dzqu2VUVAuCZFRXxqoAD-nbQVtZ2p8DlAt9iDsuMLw_V2RBf7YeUqw7J7OeOus7dIA0whGqXSiaQoFf3XUHB2ZZJCGycIZzEvtxO54KxY4DYikqJ6N18DxNbGHMuE-Edt7ZXtbv7ALsOGdH1CnVlBDf8o5cszLDJ7lGtO9b4aYvY8tZiR2OpVj2xjdmk5z8ZX3kqpkx6UWGJsNNuHInMZD_Tom1gUJNihtTXXgd05Bxw88cZ0kIpW-b7u2cCPijEPdexCCnV8O6Y4r6wYE3VBIejAQa6-DYe1tjYIfUgUs9UJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما آخرین پست مربوط به فوتبال.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78456" target="_blank">📅 01:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الان بیرانوند هی اینستاشو رفرش میکنه ببین فالووراش ده میلیون شدن یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78455" target="_blank">📅 01:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj4vqs9gGkFpMKQ9G85rrBz3M2BMexxhETnD1dADV5hXRJgSgkmKeyeAnqEhKhbwR4JPY59j8ACemst5A67JHyLhKZA0GyvqWCLUmASxXBqeCSkqd1FauKP08qtToSKKgiejUK2o3XT76uZk9qEfoh7136maFQMpnEu5lbSm83sxJfqcnBmWjeM3UYibkB79lAYqc0AlxNezpnIlRUpcmtAermlmGQciR-RlIWiBgmDoYpwwl7Ohm0-Rhn3rzk7QBlCx52HJDPkFUDvqW4puxJxkN7WiQ5EDfOSEZq0fIE8-aK0cTjxOyrMXKrbM8fPC18Uh0sLDQjrL0Z6bIB1Xcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید قالیشاه: ما اینطوری از کشورمون دفاع میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78454" target="_blank">📅 01:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF_sSGdLg32XyZwvKGAMWiZt7qE-8KW_wkYN9JaQnxskgdsGTPoIh3HLXW0h5MOtpNBGFcADrcU6JWLBEHAVjUfIRkdlxUqRlUbgcuzxzN5L2IBAAXfCAUED5qbXHIHsifi_yh1S2irh2B5YStfXPR0zGHulia9rxCt2GRkFDLqnuo59ka_a2zg3K8t7IpQ8yBjpcI2BwXXKY1ZxJDZU0uNj1x61EJfSGTDnRnQDXHj5RhRbrTGQDR1BZQN61EQhGD64W7uHvQOmfliXKO8s9QyTi4mHW7vxFiBPbDxo2FCsSfeH97U8zgCy6-o20e2OfsiH-t5JjRRN8oqyqDdiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده نویر
اعتراف کن بوفون
تایید کن کاسیاس
به راستی او بهترین دروازه بان تاریخ نیست؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78453" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب کصخل کورتوا هم نبود بلژیک گل خورده بود</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78452" target="_blank">📅 01:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78451" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78450" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار خطاب به کنعانی: چجوری تونستید بلژیک رو متوقف کنید؟
کنعانی: رفتیم تو اتوووووبوووووث.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78449" target="_blank">📅 01:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHuXW1sEouqMqjSu6K10wqiqxXXOk2QN1ya1jTcM8PYI5CpzzyeZ1bu2Z2Djti7be_cccHU3X8gj3q2TYFpn_NS2YsSAqNGKDHf3yHdo5zseQXj8zt9D3PQDiO0USe43If2OXINxNH4YVB-O-7hFwHAhoA24sH5loN9z3an_vBLpIBLxwNIYW-ZaGdOcBaOvecLTGmxJyLYanOgr0NOH6a3GKEz04ubJvAxeav6tBK7jU-qi9mkpuB7fEm4HA-8MlWWiW4N2BOdFW47NwO4Lt3TKc5xtInUejRCSvVBQnvUoS_fsvM7UYjvwiHVLdGgv2RxDg-y6-h0twpRSuKztPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شوخیو بزاریم کنار کسمادر بقیه بهترین دروازه بان ایران ایشونه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78448" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR02tAaoYZINjYNjcT_TYlh_-kiNdwQnjD9CEQHFyx8gG5J8N3uANeEz5vYVFA2AmqVhVqZnxn7Xpg0Iv9ZOZqMh_JjZyrF4oOoOs4aaVnNA_q3GluaJElW6qYskZeHIpeln7p3qIFywWXxrx3K0Mhs5M_QR8mnXSx6ybmqQjLcQigEb35dfBgYNYQeDsxq-26F7vGpwATRc35BrpBPBdyovwtSfSKzPzb0Uv2MGGEaVx0yFlECtfAOcheHJrr2J2YLPvGc3BffGDPgqkjx2G8IpT_P1HSOEWy27e20oUlZgkVdKnPdDpI0YhMiCkAGEbrvPHRovCw1FeWPHKpPsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78447" target="_blank">📅 01:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZcxJR5QxU3RJqaQn97OOg0mMGbd2H1nTnTk1lYsdGcg8mRJjg9dVCkYxb6_-fpD-oHR-IP-y7r0lC3pvwAnAvsU5_44tuAWQafCSennnupiUaETyPRsaAS6bk2wruPw0XxxUiP7iNL4yvRJygtVLE6l9oADlykkoTbimi0i05W3WeR4UsizC4p-7ac_bP4ZRqa_Njhg7Tu6TugPfNLObpOCKdAx52f1f1JR_SP2EPSciui0WfFuxyX5AuQ5yQ_UzD803OGtOdi1VHKlfUIlyvN5KGt12r4jaMQOse52OelsjPbvoAfmaIgI19opa4HIvHr4_4n6WsynQDMgCdU3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78446" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RngliBk-_uyL9OLDtrcfujd_QK7SvppUD16azUIpHg-hJJgN9nAU7NA9y5m83oamVbI8meoJ-mCWMhU2yv2GupgTEQeOZ5sHKM6-Pd3gR6hz4-r8knNKvb8h6Y7H8gQtjoGRbrNTB7tV4ADEwH_CSbEIwxVI0L-Ih1EqM9icJpz5ESTbFvOOo4WqT4YRQIz7rmrITL2Xf6WkGtp-gH89Myh-cMTTPrnMtJMBHS8LDIHlfDJ05U_80iH6sGAbvtm_F_05VT48CzVjBm-nQuy970BQUn2xOvDLdXET0sKyKpEBtJ7tRHapumw06RCXoc8uc_tqSL_cy_QxOwEbmLC2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78445" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نمره بیرانوندو  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78444" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puxvofyYj_oTGfUfryx9ZAmDzVKPgR49bNU1K8HdZuT0wRTuQ5hBJqRMvHF6CcyJdkAS2qVV8xGFeKxVVN0m8igylJMOZYS3yfTwvpxz7v3jV1hV09h8AFpU9btv5fkP0sdlyywF3FIxJnyL9hcccLXKtI_DVDfnR7phs5r_kn2pX3fM_J6x2IgYgMUHcPelfGKbGOEHqkDSUkeg5v3_s0462DhfROmt90UDKhQYyg-oEmc_CSqR9Bo_DBqCcwAvONT4S2bWNCKdFRcS0yyIodr48-Cn06EvROjPtyCZQPQW0QhlKKZI-i6D-9wz-eUnlsWaIAUUVjqw6BNisTktRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره بیرانوندو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78442" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78441" target="_blank">📅 00:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=mCRc0yYym__cry5xtHlnMkU3Dyy-hfZ38DPrkh9eWKit5AJAp10EzmoIbqTEZyOe_Ccqxx2RQIPXCmRYKMQDumExT2a_hQ1PugwKwR8eziGnOdqqjPgWKkgc04GwvaCX5jMKUQ0xy2CSeqQpBuCNIW1h_C_XZbL-KPbUlbcvjSVgXsqJGGpzA3MJgrhqwzqEN2eTgGcJ8kgpftACJon-gAMRQ7nyCSvoN6va3njxpqrtHJIOLUgXBjrVAjB44q40ZctAMxrnxWuPW49bxnoeLiLnDE-Y5TlVQfLrqdupKDF0G5WM_fgifak1RcTeRdPjfCBM0nAh_eqZaEHpD-9zyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=mCRc0yYym__cry5xtHlnMkU3Dyy-hfZ38DPrkh9eWKit5AJAp10EzmoIbqTEZyOe_Ccqxx2RQIPXCmRYKMQDumExT2a_hQ1PugwKwR8eziGnOdqqjPgWKkgc04GwvaCX5jMKUQ0xy2CSeqQpBuCNIW1h_C_XZbL-KPbUlbcvjSVgXsqJGGpzA3MJgrhqwzqEN2eTgGcJ8kgpftACJon-gAMRQ7nyCSvoN6va3njxpqrtHJIOLUgXBjrVAjB44q40ZctAMxrnxWuPW49bxnoeLiLnDE-Y5TlVQfLrqdupKDF0G5WM_fgifak1RcTeRdPjfCBM0nAh_eqZaEHpD-9zyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکتیک ژنرال برا بازی امروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78434" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امریکا هم نمی تونه این تنگه رو باز بکنه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78433" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=Qa6NCDZloWj-kwBDuyKznl96caJnC2H3fy71Xa25ldIF0lUDhOwyIbM1W71D0PwB5k7wxbXJWOO8cP4IpnxIQI9YWJMvKHStR0QwsbjF6LIqi56lInlZa5ifi6lSd3bDEf9EEwXfkHZloczC2hg1hxsve6lZVZqOLXQ3JXb4Vs--BG2Ohuo3ZxPBIEQOq6xoQuE2iPc-HGRRLWY8uHKRi2HlfnixVfmAcvCaTiMATZD7bqWunDDn7eGjHKnj30owRQ0VPb6ROs41yy6_zMXD5e2ERHMFZQgRyNWhj6QvHZdV8CIdx6C3vhsz8PPd75nmUiCQqbea3jfOhNrfEK1QVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=Qa6NCDZloWj-kwBDuyKznl96caJnC2H3fy71Xa25ldIF0lUDhOwyIbM1W71D0PwB5k7wxbXJWOO8cP4IpnxIQI9YWJMvKHStR0QwsbjF6LIqi56lInlZa5ifi6lSd3bDEf9EEwXfkHZloczC2hg1hxsve6lZVZqOLXQ3JXb4Vs--BG2Ohuo3ZxPBIEQOq6xoQuE2iPc-HGRRLWY8uHKRi2HlfnixVfmAcvCaTiMATZD7bqWunDDn7eGjHKnj30owRQ0VPb6ROs41yy6_zMXD5e2ERHMFZQgRyNWhj6QvHZdV8CIdx6C3vhsz8PPd75nmUiCQqbea3jfOhNrfEK1QVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح ایکیو اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78430" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سیاه پوست فیکس میذاری همین میشه دیگه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78428" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بلژیک اخراجی داد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78426" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl9trXgNSjEgzin_DdMSHZYhLIE74_aD6DcLtDjj9nCdr9q4XUYWacigaPWnUJxcNo2eQo_ptI1vaWC0BmBRe_5pVgJ4ez6HpBB44JmwFoHz7yiFSmo8xLREusxno7a8uZZ039LAfdTFwv8srR9TVeuGPKE47jkZr2iCDxKfBbkOgXpLEyX_Wv5F7848n_Lp5MHDon7_zbwpw_kw5G5pZs__-GsTSNJGC6C3ypGlH1_KuSIKUB2kesuePl0A07OSBcDZEHFig7-mFjcMBjf-jA9R0OZqXycqUXYFIeAatN_GqlnEi6AAL_U34m6vYbw_dZuZu9FkbYORjWAmUnYTfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تماشاگر ایرانی
رشید مظاهری کجاست؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78414" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78412" target="_blank">📅 23:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دیبروینه سوپرگل میزنه و بلژیک میبره
بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78410" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عباس قانع راجب شیر و خورشید: پرچماشون فیک باشه ولی دلشون با تیم ملی باشه اوکیه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78407" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78406" target="_blank">📅 23:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78404">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من کاملا فوتبالی از این تیم کیری بدم میاد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78404" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78403">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78403" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آفساید شه کون میدم   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78399" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آفساید شه کون میدم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78397" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78392" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78390" target="_blank">📅 22:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیرانوند همانند شهید تنگسیری ایستادگی کرد تا تنگه رو بسته نگه داره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78385" target="_blank">📅 22:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بازی تیم مردمی بلژیک هم شروع شد
ببینیم چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78382" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو:
سال‌ها به ما می‌گفتند"نمی‌توانید به خاک ایران حمله کنید."
بله، می‌توانید عملیات‌های موساد انجام دهید. «ما هم عملیات‌های زیادی انجام دادیم، من هم تعداد زیادی را تایید کردم.» اما نمی‌توانید نیروی نظامی‌مان را به ایران بفرستید.
ما این را تغییر دادیم، ما خلبان‌های شجاع‌مان را به آسمان‌های ایران فرستادیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78381" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq2iaqjqTeQWAOqchsv7AHfmMbWVuTKgBERRdnLif9JRzHUCc9EmnUwgA3600hykjsf8lyfmO5857RShSZRSKAOLmAZitlAwKwLIpUQbbES-qSqRWWcXya04uAPhTAm-MhDj5e8u2_HhvGRjJYdEq4WCGgVVjzerwslQg4TuVBgIYEVzH70F7D9R0XH8PAJRn3YSBFJEuWTXSgdphakFQ0dih9EP6pV-8ClpAPg_pSOe6EXAXEGcG7bcdrO8ObuiCOf5hUcKBSUCmXu1wBYo5n_FwSwcycUuYYs1ADmgCpTVL2RiB8kgGfjAhheicOk6NbrZf2FYszy-BFEri0rNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78377" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رو برد مساوی ایران بزنید پولدار شید</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78376" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3L9NQfga6QWNnxHx6ys9coOyPPlEJBT-kbXxFiuo_5_sHqHYdRJw-WcBbMXt5DMoEk_u6PkvE1nXk5osg0fVSGmDpIMK2cYBctbP1cEqCffleB_Ka5MMZHRxQXWlu3ZMEhB4ql5eDvxPTNJbfOPFMAi0b6nsJlq8_WhKKKeZR3xbkK9nxyNfxYzxNnVZwKHSHimj-bwxjC_mbdDBCnYFmlNY5S-_p1fWggIkfRKyGGRalIgqEgHylH77SeO9BVFqc8LCv_t5oLALxTJPBLXmtP0nFobioAwmOXma2ObeJOXTDcbfNFV5hxbBo7n-rA5naqxRADjprXfD99K_5uUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال کاملا حجومی چیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78375" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امضا میکنم که نعمتی امشب بهترین بازیکن از نظر ما میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78373" target="_blank">📅 21:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ65rmnRpKVHysQHLQtUSPZqBDNCrBwjni154DvgukFUG6ybN6SnYbAJhNLmUeBNQU7l4wHJKB3vsSH8BhjlGEEDW5-HVxSCxTscrQmOEYHKYWLIbLSucvhUxcnDqMVA2rJUNipf_guscZ6PiRcfG2FVyY4PLBev-6DjnSFS6MFfytdWEuduk7hzEqX1K_OJuLD3IhK5fAU7yF6c3ocLsboFgmXvltExeCnMUfV0hIPxbsSOQzCOy3tHcX1R9g0d7oQp__pIq5L3eIEpAhjNpRQr4wmhx14xL6i2eY_3zrORzyKXVu5faEtVWnk2w_vHPBtF85ip1beR1dK8x1t4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب مادرجنده ها اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78372" target="_blank">📅 21:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBXDNKE7GAqpSLoC5CuyThW3MNoBtsztpvGUm80mAQA-py7vVPbTVieNcLkMtvzUQBSYMhuMtt5irHNplPdJhpPQ7Vn64-38I3TTYsjHh13_R1Lj5H0WJ0b2v2T2-18yQIA3_T2etyE0tn0Zyv9XBa2qOVWuB16EniysoIPx_VXr3ryAYqjjlt8i1FjWs3xJjbvHNiTIwcoGgzdzPDglPTLpSaSYtgsF4QRbh3gbN8WyCVLn5VYIaJYp0mHi0EhjLCELxUhFRcjJRSAdiSEpDbRvpfxeSMyA24U7rQkA6gw-LVQSYR3dS67uTje6nWMZ7qV6fVm35HWdSOIJCbdpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم ۴۰۵
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78371" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=rQ4YvR98QjPFIgLeFv58SYjNKknlkVGjFbVAK-5QpqVW3cluAdViTaorrh2Ndsfiuh7HmB1uE7JqisozxPDLEQE2d4PPCa3Uy3E_d2X7Sl2kePzhYe9-Ha03sVem0_6aueB_u_BEF1CCkfKyktHMhEodoLg0wEdqlcISHSNWjHiy-imaM5OULvVi6q5K3maxbskEWjrrs6zkSNwjkrV0e3rb8yGszrCAQ51PLXfaknoZYl1l8L0EX64P4VBSfSbEwK-DQiS7Pw6bjT8cfyl7PzS8n-L829D8ObA0aGocR8gxNDKd8n3BzfHe8aMBluGkitqHDcSO5qhJ1xRKbfwxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=rQ4YvR98QjPFIgLeFv58SYjNKknlkVGjFbVAK-5QpqVW3cluAdViTaorrh2Ndsfiuh7HmB1uE7JqisozxPDLEQE2d4PPCa3Uy3E_d2X7Sl2kePzhYe9-Ha03sVem0_6aueB_u_BEF1CCkfKyktHMhEodoLg0wEdqlcISHSNWjHiy-imaM5OULvVi6q5K3maxbskEWjrrs6zkSNwjkrV0e3rb8yGszrCAQ51PLXfaknoZYl1l8L0EX64P4VBSfSbEwK-DQiS7Pw6bjT8cfyl7PzS8n-L829D8ObA0aGocR8gxNDKd8n3BzfHe8aMBluGkitqHDcSO5qhJ1xRKbfwxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی رو برد یه تیم میبنده
بازیکنای تیم مقابل روز مسابقه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78370" target="_blank">📅 20:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ریدم قالیباف: تهدید های ترامپ بکیرمونم نیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78368" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اویارزابال هم که به یامال  ایرانی پاس گل داد اصالتا اهل هراته و ریشه ی ایران باستان داره
هرات استان خونی خاکی ماست و به زودی به خاک مقدس ایران برمیگرده مثل اربیل و سلیمانیه و …
دو ایرانی اصیل کارو برای اسپانیایی های آریایی درآوردن
برادر برای برادر
❤️</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78367" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آرژانتین به عربستان باخت و قهرمان شد
ولی اسپانیا داره به عربستان تجاوز میکنه
ینی قهرمانی اسپانیا منتفی شد ؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78365" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مهد اسلام داره فرو میپاشه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78363" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ8D4bWwOTPrmxdYh6fErNkd5TGsX66Vk0mewvu3PnZIt4kMX0YqGqsibvkq-KBIAjZNUbnumDEn-bBosjE5vCseEjTwAVIMOk2TcIve8ZcKo6I4dWpaI1z5zDzIlwZiBQFcpDb7zt0v9gaOSK2EdRkIvSAVdXxHTHzZLn-xzUk_NDz8j93P7J6vk_gTcsaaW1mXYa4E2u5wYZnn0ZEi67BB8Dh-E3hphpo5rrtNzLUrHiKZukomZYtqV-qPUnnGmTP4d4AL3-_xaqmbTFanJ74biwOTdqo88VAqty2rbBIGrRkWl_nMJd3vqDoOyZVtGjpfFIGOu_p3NxH3kbVuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
قالیباف: تهدید های ترامپ بکیرمونم نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78362" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو: تا هرزمان که لازم باشه برای حفظ شمال اسرائیل توی منطقه(جنوب لبنان) میمونیم و همچنین اجازه نمیدم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه.
ما از جنوب لبنان عقب نشینی نخواهیم کرد و هیچکس نمیتونه اینو تغییر بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78359" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
عباس بیا بگو چیکار کردی چه سوپرایزی برامون داری از مذاکرات
ترامپ به فاکس نیوز:
شاید کنترل تنگه هرمز را بدست بیاوریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78358" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کونکشا دیگه زمستونم که مدرسه و دانشگاه نرفتید، دیگه دلیلتون برا تابستون فن بودن چیه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78357" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اووووو رامین رضاییان
🗣
🗣</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78356" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8_AEu4kk4D9e9zawZ5buSJ9uD5VMThAp7vF0u7lkSCun21Ns41aimIqOQQz5KtdCWS4vm51jl3lx2yG-HI3z6XkB0qUgw_tQoKP6FGwbgVl_7Q9ajbjacyBXeVac4mv_YoNWIDHjL7DXpXRS4mdjYWZD4JBhc6QVFUow-R5AJ_L3JKyHdWEPeU8iHKvDN58AfxA8LqW0i-zvkYhtMOZU599KQ1b1p-prfJaSg_O4FMZE92nXTzPXEUJrYzFmZpNNiPEoU5BXq_-vwFfHdcUXH6ySpsGnqglGnSk-QFms21TEkYl7-_Esv0h1YlFcdoLxoh9uTRTljVJ6r7kwe_Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در بازی آمریکا و استرالیا
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78355" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/78354" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgA9WCTIQrBAfcAwi9T_JTTZbI3zOT6OIFaznbUa-hVOucaWvYUZctITxrvTpApDwjipfxjXYX0jny75Ey766kTAnll5PrstlLaoPsZ6GAG2Atk6EbEPbr3XAqdIFQL2QmEa6gRVwyyzNHeYOx9NMgufGf33xu1b-BBO9eP6NHro4Tu9mlGflmwNVn2LAIP4cd7XvdAwJviYu3rBBzyWrIb_TJLYHuHLjDMxT5w4l0y7YP1gbHshzGPArT_IHlsaoYk5mxN-LXdkd8sMGuoJDmUVVKgL649KySmS7JYQAhHAWAHFTfZTCDWSJNXtXZDNHY4N8MzCY8f0dHKGzpMWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
🅰
g31
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78353" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تحلیل فوتبال با سامان ویلسون مثل تحلیل سیاست آمریکا با مرادویسیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78352" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مطمئنم که سر مهریه به توافق نمیرسن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78351" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ:
به مذاکره‌کنندگان ایرانی در سوئیس گفتم اگر تنگه هرمز را ببندید ما بقیه کشورتان را هم تصرف خواهیم کرد و حتی کشوری نخواهید داشت که بتوانید به آن برگردید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78350" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78349" target="_blank">📅 17:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dac02670.mp4?token=YiEkfpVs-QR4UzyR3OsF332XoFonN1r7HnEZTN6VwNvv8grRMe8DT3mjO8NFL1hrP4K9ygzgsaMYC40i7VkfCkwsXlWpjyhrihkX6sveYhOIprvt2WgxM_-9DjsMG1woPPqT1RB_yKoMbrYluiyAVbhFItSJVRKo0da43qdXGNHYZ5eBt67gr6si2ZR6ZTr7wK0ZhMUz57VgmOwMz5ZC-KToT453A3MjDJHGuTWSm4R2I1jt6QFsgBT5hNFBD5GGuirXLH5Un7bqHCViOE8svsLrxK7IBc1EPd9jUUhIuon2qaBnJ-Fo-QMc4CAxBCpw0jgTiIRMYLd44mYkvb1PDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dac02670.mp4?token=YiEkfpVs-QR4UzyR3OsF332XoFonN1r7HnEZTN6VwNvv8grRMe8DT3mjO8NFL1hrP4K9ygzgsaMYC40i7VkfCkwsXlWpjyhrihkX6sveYhOIprvt2WgxM_-9DjsMG1woPPqT1RB_yKoMbrYluiyAVbhFItSJVRKo0da43qdXGNHYZ5eBt67gr6si2ZR6ZTr7wK0ZhMUz57VgmOwMz5ZC-KToT453A3MjDJHGuTWSm4R2I1jt6QFsgBT5hNFBD5GGuirXLH5Un7bqHCViOE8svsLrxK7IBc1EPd9jUUhIuon2qaBnJ-Fo-QMc4CAxBCpw0jgTiIRMYLd44mYkvb1PDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس یجوری نگاه میکنه انگار اومده قرار دعوا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78348" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیت جمهوری اسلامی و امریکا شروع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78347" target="_blank">📅 17:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78346" target="_blank">📅 17:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umRSF6GM41tQxwa9br8Z060aUGVv9egj7z3Ro-lqf_vHFUP5_6j7VRzF6DGlJmEsLTXMv0FnA-CYy_vPxclmh_DGJ_IKc07AJuhltjtGJ3Vs8iI71VZ5TfPuVvv3LxNYqQ4DA28nUFnhzAIqKd2qLR7MYHEWR5GvBMDKLA6-S8HfhIIjdb3BLoYGLgA1Emv0uPnuqKclruONvQlZI1BogL9jfjjlgn5xjlZD0fLx7KpU1FxVCNDBy04ftAsJPZn4iGvncYJWGgBS3WHlAjQ04yF8hHvtvcHSJfCEHOtC7fSN-nxe27uPwyovjbkNSQtxpkqxryoaUkzOP-e3vEWO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78345" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عباس دهنت سرویس سوئیس هم بگا دادی اخرش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78344" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=OGe9s9iQmUka6q4sJtkiTZAyaM3D281MJNFcdPYxKo15n55SDVVcY0h1OECM0U1XLqTyNTXJeG8BcAm1henM48Klgaybysg6zkpqdZBksNFqHgEX5QTou19IJ0qr4t38UrQypMc7O8g_pt3Yve-pHG_L1RmTak_MCgHGHlP-HIXvCvGVVwd6cnaT_poLp9sEuFNGRUIYuf__eCHSnxX4e215j6c1ZR1yXBp5s8TcRwXS1TrDJqI7u4JsPMXx_U0-Cj1i_qVBGwzdcBmRWZ1KUAv-YaSodd6qJ_DHeKqzhsVhkK-28oIGajSqw0wjsBn6DEl8m9karEbOuXo0mgKgNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=OGe9s9iQmUka6q4sJtkiTZAyaM3D281MJNFcdPYxKo15n55SDVVcY0h1OECM0U1XLqTyNTXJeG8BcAm1henM48Klgaybysg6zkpqdZBksNFqHgEX5QTou19IJ0qr4t38UrQypMc7O8g_pt3Yve-pHG_L1RmTak_MCgHGHlP-HIXvCvGVVwd6cnaT_poLp9sEuFNGRUIYuf__eCHSnxX4e215j6c1ZR1yXBp5s8TcRwXS1TrDJqI7u4JsPMXx_U0-Cj1i_qVBGwzdcBmRWZ1KUAv-YaSodd6qJ_DHeKqzhsVhkK-28oIGajSqw0wjsBn6DEl8m9karEbOuXo0mgKgNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوفون و نویر وقتی میبینن نیاز نبوده ۲۰ سال کون خودشونو پاره کنن و چارتا سیو جام جهانی کافی بوده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78343" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پزشکیان:
نگرانم مردم ناراضی به خیابان بیان و اعتراض کنن. اون وقت ابهت ما فرو می‌ریزه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78341" target="_blank">📅 15:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اگه برزیل با درخشش کونیا میتونه ۳.۰ ببره ما چرا با وجود اینهمه کونی و مادرجنده نمیتونیم کاری کنیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78340" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پزشکیان:
توافق رو گردن من نندازید، تمام فرمانده‌هان قرارگاه، سپاه، ارتش و امنیت در جلسه شورای امنیت ملی با توافق موافق بودن.
دیس به مجتبی خامنه ای؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78339" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستان یه نکته ای بگم
مجتبی خامنه ای طبق بیانیه ای که داد گفت به اصرار پزشکیان این تفاهم نامه رو قبول کردم
نکته ای که وجود داره اینه که حکومت اگه یک درصد امیدوار بود که این مذاکرات نتیجه مثبتی براشون به همراه داره به هیچ وجه اعتبارش رو به پزشکیان نمیدادن
پس نتیجه میگیریم که این مذاکرات صرفا برای وقت خریدن هست نه توافق قطعی
ممنون از توجه شما به این موضوع
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78336" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مذاکرات تو سوئیس شرو شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78335" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه رپرایی با معروفیت کیرگوزی میکنن که سر جم ۵۰ هزار نفر نمیشناسنشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78334" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن    @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78333" target="_blank">📅 14:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ولی خب اسپانیا چون تجربه ندارن قهرمان نمیشهط آرژانتینم چون بیش از حد تجربه دارن(پیرن) نمیشه، تنها تیم معتدل انگلیسه که اونم لوزره</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78332" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هلند بوی دوباره کیر شدن تو فینال توسط اسپانیا میده</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78331" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ژنرال شماره دعانویستو بفرس
تروساد هم از ناحیه کتف بگا رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78330" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78329" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTGbTZ2vwBW-mcr7WvuWubKNsYLAti8a4ecCVTi672A8rn_-z_nimADzv_B3ncrXTXTS9BoTlaoHKY92pTLCaa_c68oEONiL6X-_XRZyiZd6ZeSK85E6LWSRuEbug-y910qQjtSwgnJ16B_51GGJQzHtSWcwS-e4aR8He5vsbFLzqasZ6EEj5RmYsN-Ig-xuOb8ynfWMQrbYLMRHJtg8JRZhc07fYMFK7-g6JwUSxaQmaBCD8qe3omrFUGYNU1gFcxSvnTA0DPGTRButVS72tYqtxYGXaAX7pUfc6krOaozF9xljKDMrILnx5IUlpNAj_AZrbdQABcd0u18egcTckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم یکی از پر افتخارترین تیم های آسیا در بازی دیشب
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78328" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoKh0O3_qHZfQz6Z6tWq0M4jdF7wwCTvLUQVfxnmZGGJkWr6g20FKUTFiVt21TpF7u8HxzPetENggczeO-7jkQJb2GojqQPwcNCZZHpW2tgGqeiaZ19lo1qBhqvv1tzjgmMVRK_xi7Rm9hRP57h7jPpjahFLBBHDVpzGkL_5bFZjhZw_uNscy5D_2v5HUbVHZoPoYbnkNVx_u1GwiHpyJ8qMwGybPjyH4PVRytj70guSj1EeityZ6eWxz8ZG8ovuloxOJG0aPvQNZ_ueRNtXTOSL2AmTh5Uwy86LnnY73DoXgINMe7qL7bXrWGr4X4e4oF_NYaz8a0NBEgwjHkmVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال توی یک تاکتیک پیشرفته رفته عکس بازیکنای بلژیک رو زده روی دیوار بازیکن های تیم ملی تا امشب بازیکنا تو زمین نتزسن.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78327" target="_blank">📅 11:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jULwnjLdwfrecM8xAGh4D_nKInF8qaPv-a8q66Ct3SSH8A7zKoNWJZd3YyuQRQm-p_bXZgRq1PeDz4ktYNpFyaPC_WYM0UAyxviwGvbS7Xk_zcjYtHmam4VMcQhAym11Z7X3e1kT65k9ECIDasBOESRKNqvXojA3JQHOq3Eul26Y69ChBzVDayAW-CPZFegc3tUd1qh_YCyF16-U4N0vl1SawTmWrPf4eJf-6O5NIc2JIyN7L0iyuAZrqZE7BAKul-o2M9rIHirMKBnFJA1Qc5nbs0wLm3y6C44OpwJIMYD5mVvcLcPy1_6-gnCfm6LZVKJUkSvIy7WEcZ3x2OmxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم رونالدو از مسی بهتره، چون ممه های زنش بزرگترن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78326" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78325" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd_iblQXFiJdgMj6D0PuaJLAtRksviKroLoTOpujPzWuQx6qqLnqWb-bJ0Sk7s-KpclTg9T7q4USgWvQjGIFZEf4emFtkqj5ot8g0QXBcqmVm6sQldmnVY4fvspeV1En-D586PuYJhsg_U5tQfhCAF8ZGyiC9Am7bKKaBItaF_pjKZ_UmMCywnxpWkEzt4pqcMNhaA4cRn-IJmTjDec-zB6FJuR2tma-FDMpbeyP4PFFE3DrfDNBU7cYOv1pyON4hfShWlRjjxYDmgY7dxXC9XXY-NQ0QEHhcyBX3etdEWmOshm8pkMMvTp1lBU29zpf3zfZIetu3Kar09SmIvyf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهاد ویژه فقط برای بازی ایران
🇮🇷
- بلژیک
🇧🇪
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل مبلغ شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
R31
🅰
❤️
Winro
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78324" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
